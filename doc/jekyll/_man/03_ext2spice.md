---
layout: post
title: 03 ext2spice
math: true
---



* TOC
{:toc }

# NAME

ext2spice - convert hierarchical *ext* (5) extracted-circuit files to
flat *spice*  files

# SYNOPSIS

**ext2spice** \[ **-B** \] \[ *extcheck-options* \] \[ *-M|m* \] \[ *-y
num* \] \[ *-f hspice|spice3|spice2* \] \[ *-J hier|flat* \] \[ *-j
device:sdRclass\[/subRclass\]/defaultSubstrate* \] *root*

# DESCRIPTION

Ext2spice will convert an extracted circuit from the hierarchical
*ext* (5) representation produced by Magic to a flat spice file which
can be accepted by spice2, spice3, hspice and other simulation tools.
The root of the tree to be extracted is the file *root***.ext**; it and
all the files it references are recursively flattened. The result is a
single, flat representation of the circuit that is written to the file
*root***.spice** .

The following options are recognized:

**-o *outfile***  
Instead of leaving output in the file *root***.spice**, leave it in
*outfile*.

**-B**  
Don't output transistor or node attributes in the spice file. Usually
the attributes of a node or a device are output as special comments
\*\*fetattr and \*\*nodeatrr which can be processed further to create
things such a initial conditions etc.

**-F**  
Don't output nodes that aren't connected to fets (floating nodes).
Normally capacitance from these nodes is output with the comment
\*\*FLOATING attached on the same line.

**-t*char***  
Trim characters from node names when writing the output file. *Char*
should be either "#" or "!". The option may be used twice if both
characters are desired. Trimming "#" and "!" is enabled by default when
the format is hspice.

**-*M|m***  
Merge parallel fets. *-m* means conservative merging of fets that have
equal widths only (usefull with hspice format multiplier if delta W
effects need to be taken care of). -M means aggressive merging: the fets
are merged if they have the same terminals and the same length.

**-y *num***  
Select the precision for outputing capacitors. The default is 1 which
means that the capacitors will be printed to a precision of .1 fF.

**-f *hspice|spice2|spice3***  
Select the output format. Spice3 is the the format understood by the
latest version of berkeley spice. Node names have the same names as they
would in a *sim*(5) file and no special constructs are used. Spice2 is
the format understood by the older version of spice (which usually has
better convergence). Node names are numbers and a dictionary of number
and corresponding node is output in the end. HSPICE is a format
understood by meta-software's hspice and other commercial tools. In this
format node names cannot be longer than 15 characters long (blame the
fortran code): so if a hierarchical node name is longer it is truncated
to something like x1234/name where x1234 is an alias of the normal node
hierarchical prefix and name its hierarchical postfix (a dictionary
mapping prefixes to real hierarchical paths is output at the end of the
spice file). If the node name is still longer than 15 characters long
(again blame the fortran code) it is translated to something like z@1234
and the equivalent name is output as a comment. In addition since hspice
supports scaling and multipliers so the output dimensions are in lambdas
and if parallel fets are merged the hspice construct *M* is used.

**-J *hier|flat***  
Select the source/drain area and perimeter extraction algorithm. If
*hier* is selected then the areas and perimeters are extracted *only
within each subcell*. For each fet in a subcell the area and perimeter
of its source and drain within this subcell are output. If two or more
fets share a source/drain node then the total area and perimeter will be
output in only one of them and the other will have 0. If *flat* is
selected the same rules apply only that the scope of search for area and
perimeter is the whole netlist. In general *flat* (which is the default)
will give accurate results (it will take into account shared
sources/drains) but hier is provided for backwards compatibility with
version 6.4.5. On top of this selection you can individually control how
a terminal of a specific fet will be extracted if you put a source/drain
attribute. *ext:aph* makes the extraction for that specific terminal
hierarchical and *ext:apf* makes the extraction flat (see the magic
tutorial about attaching attribute labels). Additionaly to ease
extraction of bipolar transistors the gate attribute *ext:aps* forces
the output of the substrate area and perimeter for a specific fet (in
flat mode only).

**-j *device:sdRclass\[/subRclass\]/defaultSubstrate***  
Gives ext2sim information about the source/drain resistance class of the
fet type *device*. Makes *device* to have *sdRclass* source drain
resistance class, *subRclass* substrate (well) resistance class and the
node named *defaultSubstrate* as its default substrate. The defaults are
nfet:0/Gnd! and pfet:1/6/Vdd! which correspond to the MOSIS technology
file but things might vary in your site. Ask your local cad
administrator.

The way the extraction of node area and perimeter works in magic the
total area and perimeter of the source/drain junction is summed up on a
single node. That is why all the junction areas and perimeters are
summed up on a single node (this should not affect simulation results
however).

*Special care must be taken when the substrate of a fet is tied to a*
node other than the default substrate (eg in a bootstraping charge
pump). To get the correct substrate info in these cases the fet(s) with
separate wells should be in their own separate subcell with ext:aph
attributes attached to their sensitive terminals (also all the
transistors which share sensistive terminals with these should be in
another subcell with the same attributes).

In addition, all of the options of *extcheck* (1) are accepted.

The awk filter spice2sim is provided with the current distribution for
debugging purposes.

# SEE ALSO

extcheck (1), ext2spice (1), magic (1), rsim (1), ext (5), sim (5)

# AUTHOR

Stefanos Sidiropoulos.

# BUGS

The areas and perimeters of fet sources and drains work only with the
simple extraction algorith and not with the extresis flow. So you have
to model them as linear capacitors (create a special extraction style)
if you want to extract parasitic resistances with extresis.
