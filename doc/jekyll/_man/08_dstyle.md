---
layout: post
title: 08 dstyle
math: true
---



* TOC
{:toc }

# NAME

dstyle - format of .dstyle files (display styles)

# DESCRIPTION

Display styles indicate how to render information on a screen. Each
style describes one way of rendering information, for example as a solid
area in red or as a dotted outline in purple. Different styles
correspond to mask layers, highlights, labels, menus, window borders,
and so on. See \`\`Magic Maintainer's Manual \#3: Display Styles, Color
Maps, and Glyphs'' for more information on how the styles are used.

Dstyle files usually have names of the form *x***.***y***.dstyle***n*,
where *x* is a class of technologies, *y* is a class of displays, and
*n* is a version number (currently **5**). The version number may
increase in the future if the format of dstyle files changes. For
example, the display style file **mos.7bit.dstyle5** provides all the
rendering information for our nMOS and CMOS technologies for color
displays with at least 7 bits of color.

Dstyle files are stored in ASCII as a series of lines. Lines beginning
with \`\`#'' are considered to be comments and are ignored. The rest of
the lines of the file are divided up into two sections separated by
blank lines. There should not be any blank lines within a section.

# DISPLAY\_STYLES SECTION

The first section begins with a line

**display\_styles** *planes*

where *planes* is the number of bits of color information per pixel on
the screen (between 1 and 8). Each line after that describes one display
style and contains eight fields separated by white space:

*style writeMask color outline fill stipple shortName longName*

The meanings of the fields are:

*style*  
The number of this style, in decimal. Styles 1 through 64 are used to
display mask layers in the edit cell. The style number(s) to use for
each mask layer is (are) specified in the technology file. Styles 65-128
are used for displaying mask layers in non-edit cells. If style *x* is
used for a mask layer in the edit cell, style *x*+64 is used for the
same mask layer in non-edit cells. Styles above 128 are used by the
Magic code for various things like menus and highlights. See the file
*styles.h* in Magic for how styles above 128 are used. When
redisplaying, the styles are drawn in order starting at 1, so the order
of styles may affect what appears on the screen.

*writeMask*  
This is an octal number specifying which bit-planes are to be modified
when this style is rendered. For example, 1 means only information in
bit-plane 0 will be affected, and 377 means all eight bit-planes are
affected.

*color*  
An octal number specifying the new values to be written into the
bit-planes that are modified. This is used along with *writeMask* to
determine the new value of each pixel that's being modified:

newPixel = (oldPixel & ∼writeMask) | (color & writeMask)

The red, green, and blue intensities displayed for each pixel are not
deterimined directly by the value of the pixel; they come from a color
map that maps the eight-bit pixel values into red, green, and blue
intensities. Color maps are stored in separate files.

*outline*  
If this field is zero, then no outline is drawn. If the field is
non-zero, it specifies that outlines are to be drawn around the
rectangular areas rendered in this style, and the octal value gives an
eight-bit pattern telling how to draw the outline. For example, 377
means to draw a solid line, 252 means to draw a dotted line, 360
specifies long dashes, etc. This field only indicates *which* pixels
will be modified: the *writeMask* and *color* fields indicate how the
pixels are modified.

*fill*  
This is a text string specifying how the areas drawn in this style
should be filled. It must have one of the values **solid**, **stipple**,
**cross**, **outline**, **grid**. **Solid** means that every pixel in
the area is to modified according to *writeMask* and *color*.
**Stipple** means that the area should be stippled: the stipple pattern
given by *stipple* is used to determine which pixels in the area are to
be modified. **Cross** means that an X is drawn in a solid line between
the diagonally-opposite corners of the area being rendered. **Outline**
means that the area should not be filled at all; only an outline is
drawn (if specified by *outline*). **Grid** is a special style used to
draw a grid in the line style given by *outline*. The styles **cross**
and **stipple** may be supplemented with an outline by giving a non-zero
*outline* field. The **outline** and **grid** styles don't make sense
without an an outline, and **solid** doesn't make sense with an outline
(since all the pixels are modified anyway).

*stipple*  
Used when *fill* is **stipple** to specify (in decimal) the stipple
number to use.

*shortName*  
This is a one-character name for this style. These names are used in the
specification of glyphs and also in a few places in the Magic source
code. Most styles have no short name; use a \`\`-'' in this field for
them.

*longName*  
A more human-readable name for the style. It's not used at all by Magic.

# STIPPLES SECTION

The second section of a dstyle file is separated from the first by a
blank line. The first line of the second section must be

**stipples**

and each additional line specifies one stipple pattern with the syntax

*number pattern name*

*Number* is a decimal number used to name the stipple in the *stipple*
fields of style lines. *Number* must be no less than 1 and must be no
greater than a device-dependent upper limit. Most devices support at
least 15 stipple patterns. *Pattern* consists of eight octal numbers,
each from 0-377 and separated by white space. The numbers form an 8-by-8
array of bits indicating which pixels are to be modified when the
stipple is used. The *name* field is just a human-readable description
of the stipple; it isn't used by Magic.

# FILES

∼cad/lib/magic/sys/mos.7bit.dstyle5

# SEE ALSO

magic (1), cmap (5), glyphs (5)
