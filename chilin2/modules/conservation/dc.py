from samflow.command import ShellCommand
from samflow.workflow import attach_back

from pkg_resources import resource_filename
from chilin2.modules.conservation.qc import stat_conservation
from chilin2.modules.conservation.tex import tex_conserv

def conservation(workflow, conf):
    get_top_peaks = attach_back(workflow,
                                ShellCommand(
                                    "{tool} -n {param[peaks]} {input} | cut -f 1,2,3,4,9 > {output}",
                                    tool="head",
                                    input=conf.prefix + "_sort_summits.bed" if conf.get("macs2", "type") in ["both", "narrow"] else conf.prefix + "_b_sort_peaks.broadPeak",
                                    output=conf.prefix + "_peaks_top_conserv.bed",
                                    param= {"peaks": 5000},
                                    name="top summits for conservation"))
    get_top_peaks.update(param=conf.items("conservation"))
    peaks_input = conf.prefix + "_peaks_top_conserv.bed"

    conservation = attach_back(workflow,
                               ShellCommand(
                                   "{tool} -t Conservation_at_summits \
                                   -d {input[phast]} -o {param[prefix]} -l Peak_summits {input[bed]} -w {param[width]} > {output[score]}",
                                   tool="conservation_plot.py",
                                   input={"bed": peaks_input,
                                          "phast": conf.get_path(conf.get("basics", "species"), "conservation")},
                                   output={"pdf": conf.prefix + "_conserv.pdf",
                                           "R": conf.prefix + "_conserv.R",
                                           "score": conf.prefix + "_conserv.txt"},
                                   param={"tool": resource_filename("chilin2.modules", "conservation/conservation_plot.py"),
                                          "prefix": conf.prefix + "_conserv",
                                          "width": 400 if conf.get("conservation", "type").lower() == "tf" else 4000},
                                   name="conservation"))
    conservation.update(param=conf.items('conservation'))

    attach_back(workflow,
                ShellCommand(
                    "{tool} -resize 500x500 -density 50  {input[pdf]} {output[pdf]}",
                    tool="convert", ## width differs histone mark and TF
                    input={"pdf": conf.prefix + "_conserv.pdf",
                           "R": conf.prefix + "_conserv.R"},
                    output={"pdf": conf.prefix + "_conserv_img.pdf"},
                    name="convert pdf to png"))

    ## QC parts
    stat_conservation(workflow, conf)
    if conf.long:
        tex_conserv(workflow, conf)