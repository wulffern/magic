---
layout: post
title: 02 ext2sim
math: true
---



* TOC
{:toc }

# NAME

ext2sim - convert hierarchical *ext* (5) extracted-circuit files to flat
*sim* (5) files

# SYNOPSIS

**ext2sim** \[ **-a** *aliasfile* \] \[ **-l** *labelsfile* \] \[ **-o**
*simfile* \] \[ **-A** \] \[ **-B** \] \[ **-F** \] \[ **-L** \] \[
**-t** \] \[ *extcheck-options* \] \[ *-y num* \] \[ *-f mit|lbl|su* \]
\[ *-J hier|flat* \] \[ *-j
device:sdRclass\[/subRclass\]/defaultSubstrate* \] *root*

# DESCRIPTION

Ext2sim will convert an extracted circuit from the hierarchical
*ext* (5) representation produced by Magic to the flat *sim* (5)
representation required by many simulation tools. The root of the tree
to be extracted is the file *root***.ext**; it and all the files it
references are recursively flattened. The result is a single, flat
representation of the circuit that is written to the file
*root***.sim**, a list of node aliases written to the file
*root***.al**, and a list of the locations of all nodenames in CIF
format, suitable for plotting, to the file *root***.nodes**. The file
*root***.sim** is suitable for use with programs such as *crystal* (1),
*esim* (1), or *sim2spice* (1).

The following options are recognized:

**-a *aliasfile***  
Instead of leaving node aliases in the file *root***.al**, leave it in
*aliasfile*.

**-l *labelfile***  
Instead of leaving a CIF file with the locations of all node names in
the file *root***.nodes**, leave it in *labelfile*.

**-o *outfile***  
Instead of leaving output in the file *root***.sim**, leave it in
*outfile*.

**-A**  
Don't produce the aliases file.

**-B**  
Don't output transistor or node attributes in the **.sim** file. This
option will also disable the output of information such as the area and
perimeter of source and drain diffusion and the fet substrate. For
compatibitlity reasons the latest version of ext2sim outputs this
information as node attibutes. This option is necessary when preparing
input for programs that don't know about attributes, such as
*sim2spice* (1) (which is actually made obsolete by *ext2spice* (1),
anyway), or *rsim* (1).

**-F**  
Don't output nodes that aren't connected to fets (floating nodes).

**-L**  
Don't produce the label file.

**-t*char***  
Trim characters from node names when writing the output file. *Char*
should be either "#" or "!". The option may be used twice if both
characters are desired.

**-f *MIT|LBL|SU***  
Select the output format. MIT is the traditional *sim*(5) format. LBL is
a variant of it understood by *gemini*(1) which includes the substrate
connection as a fourth terminal before length and width. SU is the
internal Stanford format which is described also in *sim*(5) and
includes areas and perimeters of fet sources, drains and substrates.

**-y *num***  
Select the precision for outputing capacitors. The default is 1 which
means that the capacitors will be printed to a precision of .1 fF.

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

# SCALING AND UNITS

If all of the **.ext** files in the tree read by *ext2sim* have the same
geometrical scale (specified in the **scale** line in each **.ext**
file), this scale is reflected through to the output, resulting in
substantially smaller **.sim** files. Otherwise, the geometrical unit in
the output **.sim** file is a centimicron.

Resistance and capacitance are always output in ohms and femptofarads,
respectively.

# SEE ALSO

extcheck (1), ext2dlys (1), ext2spice (1), magic (1), rsim (1), ext (5),
sim (5)

# AUTHOR

Walter Scott additions/fixes by Stefanos Sidiropoulos.

# BUGS

Transistor gate capacitance is typically not included in node
capacitances, as most analysis tools compute the gate capacitance
directly from the gate area. The **-c** flag therefore provides a limit
only on non-gate capacitance. The areas and perimeters of fet sources
and drains work only with the simple extraction algorith and not with
the extresis flow. So you have to model them as linear capacitors
(create a special extraction style) if you want to extract parasitic
resistances with extresis.
