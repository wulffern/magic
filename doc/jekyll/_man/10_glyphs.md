---
layout: post
title: 10 glyphs
math: true
---



* TOC
{:toc }

# NAME

glyphs - format of .glyphs files

# DESCRIPTION

Glyph files (\`\`.glyph'' extension) are used to store commonly-used bit
patterns (glyphs) for Magic. Right now, the bit patterns are used for
two purposes in Magic. First, they specify patterns for programmable
cursors: each cursor shape (e.g. the arrow used for the wiring tool) is
read in as a glyph from a glyph file. Second, glyphs are used by the
window manager to represent the icons displayed at the ends of scroll
bars. Glyph file names normally have the extension **.glyph**.

Glyph files are stored in ASCII format. Lines beginning with \`\`#'' are
considered to be comments and are ignored. Blank lines are also ignored.
The first non-comment line in a glyph file must have the syntax

**size ***nGlyphs width height*

The *nGlyphs* field must be a number giving the total number of glyphs
stored in the file. The *width* and *height* fields give the dimensions
of each glyph in pixels. All glyphs in the same file must have the same
size.

The **size** line is followed by a description for each of the glyphs.
Each glyph consists of *height* lines each containing 2×*width*
characters. Each pair of characters corresponds to a bit position in the
glyph, with the leftmost pair on the topmost line corresponding to the
upper-left pixel in the glyph.

The first character of each pair specifies the color to appear in that
pixel. The color is represented as as a single character, which must be
the short name of a display style in the current display style file.
Some commonly-used characters are **K** for black, **W** for white, and
**.** for the background color (when **.** is used in a cursor, it means
that that pixel position is transparent: the underlying picture appears
through the cursor). See \`\`Magic Maintainer's Manual \#3: Display
Styles, Color Maps, and Glyphs'' for more information.

The second character of each pair is normally blank, except for one
pixel per glyph which may contain a \`\`\*'' in the second character.
The \`\`\*'' is used for programmable cursors to indicate the hot-spot:
the pixel corresponding to the \`\`\*'' is the one that the cursor is
considered to point to.

For an example of a glyph file, see ∼cad/lib/magic/sys/color.glyphs.

# SEE ALSO

magic (1), dstyle (5)
