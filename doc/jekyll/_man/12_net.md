---
layout: post
title: 12 net
math: true
---



* TOC
{:toc }

# NAME

net - format of .net files read/written by Magic's netlist editor

# DESCRIPTION

Netlist files are read and written by Magic's netlist editor in a very
simple ASCII format. The first line contains the characters \`\` Netlist
File'' (the leading blank is important). After that comes a blank line
and then the descriptions of one or more nets. Each net contains one or
more lines, where each line contains a single terminal name. The nets
are separated by blank lines. Any line that is blank or whose first
character is blank is considered to be a separator line and the rest of
its contents are ignored.

Each terminal name is a path, much like a file path name in Unix. It
consists of one or more fields separated by slashes. The last field in
the path is the name of a label in a cell. The other fields (if any),
are cell instance identifiers that form a path from the edit cell down
to the label. The first instance identifier must name a subcell of the
edit cell, the second must be a subcell of the first, and so on.

Instance identifiers are unique within their parent cells, so a terminal
path selects a unique cell to contain the label. However, the same label
may appear multiple times within its cell. When this occurs, Magic
assumes that the identical labels identify electrically equivalent
terminals; it will choose the closest of them when routing to that
terminal. Further, after connecting to one of these terminals Magic may
take advantage of the internal wiring connecting them together and route
through a cell to complete the net's wiring.

An example netlist file follows below. It contains three distinct nets.


     Netlist File

    alu/bit_1/cout
    alu/bit_2/cin


    regcell[21,2]/output
    latch[2]/input
     This line starts with a blank, so it's a separator.
    opcode_pla/out6
    shifter/drivers/shift2

# SEE ALSO

magic (1)
