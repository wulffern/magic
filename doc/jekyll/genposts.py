#!/usr/bin/env python3

import os
import re

ss = """---
layout: post
title: {title}
math: true
---

""" + """

* TOC
{:toc }

"""


def convertFiles(files,dirname,outputdir,replace=False):

    if(not os.path.exists(outputdir)):
        os.system(f"mkdir {outputdir}")

    for f in files:
        name = files[f]
        fname = name.replace(" ","_")
        with open(f"{outputdir}/{fname}.md","w") as fo:
            fo.write(ss.replace("{title}",name))
            with open(f"{dirname}/{f}.md") as fi:
                for line in fi:
                    if(replace):
                        line = re.sub("^###","##",line)
                    fo.write(line)

#---------------------------------------------------------------
#- Convert latexfiles to markdown
#---------------------------------------------------------------
txfiles = {
    "introduction": "Introduction",
    "tut1": "01 What is Magic",
    "tut2": "02 Basic Painting and Selection",
    "tut3": "03 Advanced Painting",
    "tut4": "04 Cell Hierarchies ",
    "tut5": "05 Multiple Windows",
    "tut6": "06 Design-Rule Checking",
    "tut7": "07 Netlists and Routing",
    "tut8": "08 Circuit-Extraction",
    "tut9": "09 Format Conversion for CIF and Calma (GDSII)",
    "tut10": "10 The interactive Router",
    "copyright": "Copyright"
}


latexfiles= "../latexfiles"
mdfiles = "tmp/man"

if(not os.path.exists(mdfiles)):
    os.system(f"mkdir {mdfiles}")

#- TeX and pandoc must be installed
for f in txfiles:
    if(not os.path.exists(f"{latexfiles}/{f}.html")):
        os.system(f"cd {latexfiles};make4ht {f}.tex 'mathml,mathjax'")
        os.system(f"cd {latexfiles};cp *.png ../jekyll/_tutorials/")
    if(not os.path.exists(f"{mdfiles}/{f}.md")):
        os.system(f"cd {latexfiles}/; pandoc -s  -t markdown_strict {f}.html -o ../jekyll/{mdfiles}/{f}.md")

convertFiles(txfiles,mdfiles,"_tutorials",replace=True)

#---------------------------------------------------------------
#- Convert shortcuts to markdown
#---------------------------------------------------------------
start = 0
with open("shortcuts.md","w") as fo:
    fo.write("""---
layout: page
title: Macros
math: true
permalink: macros
---

These are the default macros in Magic

""")
    fo.write("\n| Macro Key | Command|\n")
    fo.write("|:---|:---|\n")
    with open("../textfiles/default_macros.txt") as fi:
        for line in fi:

            if(start == 1):
                if(re.search("^\s+",line)):
                    continue
                ar = re.split("\s+",line)
                fo.write(f"|{ar[0]}|" + " ".join(ar[1:]) + "|\n")

            if(start > 1):
                start -= 1
            if(re.search("macro key",line)):
                start = 2


#---------------------------------------------------------------
#- Convert manpages to markdown
#---------------------------------------------------------------

manfiles = {
    "magic.1" : "01 magic",
    "ext2sim.1" : "02 ext2sim",
    "ext2spice.1" : "03 ext2spice",
    "extcheck.1" : "04 extcheck",
    "displays.5" : "05 displays",
    "cmap.5" : "06 cmap",
    "dlys.5" : "07 dlys",
    "dstyle.5" : "08 dstyle",
    "ext.5" : "09 ext",
    "glyphs.5" : "10 glyphs",
    "mag.5" : "11 mag",
    "net.5" : "12 net",
    "sim.5" : "13 sim"
}


manfilesdir= "../man"
mdmanfiles = "tmp/man"

if(not os.path.exists(mdmanfiles)):
    os.system(f"mkdir {mdmanfiles}")

#- Pandoc must be installed
for f in manfiles:
    if(not os.path.exists(f"{mdmanfiles}/{f}.md")):
        os.system(f"cd {manfilesdir}/; pandoc -s  -t markdown_strict {f} -o ../jekyll/{mdmanfiles}/{f}.md")

convertFiles(manfiles,mdmanfiles,"_man")


#---------------------------------------------------------------
#- Convert html to markdown
#---------------------------------------------------------------
htmlpath = "../html"
outdir = "../jekyll/tmp/html/"


def readAndFilter(name):
    with open(f"{outdir}{name}.md") as fi:
        buffer = ""
        output = 0
        for l in fi:
            if(re.search("^##",l)):
                output = 1
            if(re.search("graphics/line1.gif",l)):
                output = 0

            if(re.search("Command Reference",l)):
                output = 0

            l = re.sub("^> *","",l)
            l = re.sub("^> *","",l)

            l = re.sub("href=\"","href=\"#",l)

            if(re.search("\.html",l)):
                l = l.replace(".html","")
                l = l.replace("(","(#")
            if(output):
                buffer += l

        return buffer


if(not os.path.exists(outdir)):
    os.system(f"mkdir {outdir}")
onlyfiles = [f for f in os.listdir(htmlpath) if os.path.isfile(os.path.join(htmlpath, f)) and f.endswith(".html")]
for f in onlyfiles:
    ofile = outdir + f.replace(".html",".md")
    if(not os.path.exists(ofile)):
        os.system(f"cd {htmlpath};pandoc -s -t markdown_strict {f} -o {ofile}")


with open("commands.md","w") as fo:
    fo.write("""---
layout: post
title: Commands
math: true
---

* TOC
{:toc }



    """)
    fo.write("\n")


    fo.write(readAndFilter("commands"))

    for f in sorted(onlyfiles):
        name = f.replace(".html","")
        if(name == "commmands"):
            continue
        fo.write(readAndFilter(name))
