---
layout: post
title: 06 cmap
math: true
---



* TOC
{:toc }

# NAME

cmap - format of .cmap files (color maps)

# DESCRIPTION

Color-map files define the mapping between eight-bit color numbers and
red, green and blue intensities used for those numbers. They are read by
Magic as part of system startup, and also by the **:load** and **:save**
commands in color-map windows. Color-map file names usually have the
form *x***.***y***.***z***.cmap***n*, where *x* is a class of technology
files, *y* is a class of displays, *z* is a class of monitors, and *n*
is a version number (currently **1**). The version number will change in
the future if the format of color-map files ever changes. Normally, *x*
and *y* correspond to the corresponding parts of a display styles file.
For example, the color map file **mos.7bit.std.cmap1** is used today for
most nMOS and CMOS technology files using displays that support at least
seven bits of color per pixel and standard-phosphor monitors. It
corresponds to the display styles file **mos.7bit.dstyle5**.

Color-map files are stored in ASCII form, with each line containing four
decimal integers separated by white space. The first three integers are
red, green, and blue intensities, and the fourth field is a color
number. For current displays the intensities must be integers between 0
and 255. The color numbers must increase from line to line, and the last
line must have a color number of 255. The red, green, and blue
intensities on the first line are used for all colors from 0 up to and
including the color number on that line. For other lines, the
intensities on that line are used for all colors starting one color
above the color number on the previous line and continuing up and
through the color number on the current line. For example, consider the
color map below:


    255	0	0	2
    0	0	255	3
    255	255	255	256

This color map indicates that colors 0, 1, and 2 are to be red, color 3
is to be blue, and all other colors are to be white.

# SEE ALSO

magic (1), dstyle (5)
