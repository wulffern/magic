#!/usr/bin/env python3

import os

files = [
    "introduction",
    "tut1",
    "tut2",
    "tut3",
    "tut4",
    "tut5",
    "tut6",
	"tut7",
    "tut8",
    "tut9",
    "tut10",
    "tut11",
    "copyright"
]

os.system("mkdir mdfiles")
for f in files:
    os.system(f"cd latexfiles;make4ht {f}.tex 'mathml,mathjax';pandoc -s  -t markdown_strict {f}.html -o ../mdfiles/{f}.md")

os.system("cd latexfiles;cp *.png ../jekyll/tutorials/")

ss = """---
layout: post
title: {title}
math: true
---

""" + """

* TOC
{:toc }

"""

for f in files:
    with open(f"jekyll/tutorials/{f}.md","w") as fo:
        fo.write(ss.replace("{title}",f))
        with open(f"mdfiles/{f}.md") as fi:
            for line in fi:
                fo.write(line)
