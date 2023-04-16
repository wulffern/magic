---
layout: post
title: 04 extcheck
math: true
---



* TOC
{:toc }

# NAME

extcheck - check hierarchical *ext* (5) files for global node
connectivity and summarize number of fets, nodes, etc.

# SYNOPSIS

**extcheck** \[ **-c** *cthresh* \] \[ **-p** *path* \] \[ **-r**
*rthresh* \] \[ **-s** *sym***=***value* \] \[ **-C** \] \[ **-R** \] \[
**-S** *symfile* \] \[ **-T** *tech* \] *root*

# DESCRIPTION

*Extcheck* will read an extracted circuit in the hierarchical *ext* (5)
representation produced by Magic, check to ensure that all global nodes
(those to which a label ending in an exclamantion point is attached) are
fully connected in the layout, and then print a count of the number of
various items (nodes, fets, etc) encountered while flattening the
circuit. The root of the tree to be processed is the file
*root***.ext**; it and all the files it references are recursively
flattened.

The following options are recognized:

**-c *cthresh***  
Set the capacitance threshold to *cthresh* femtofarads. *Extcheck* will
count the number of explicit internodal capacitors greater than
*cthresh*, the number of nodes whose capacitance is greater than
*cthresh*, as well as the total number of nodes. (Other programs such as
*ext2sim* (1) use this option as a threshold value below which a
capacitor will not be output). The default value for *cthresh* is 10
femtofarads.

**-p *path***  
Normally, the path to search for **.ext** files is determined by looking
for **path** commands in first ~cad/lib/magic/sys/.magic, then ~/.magic,
then .magic in the current directory. If **-p** is specified, the
colon-separated list of directories specified by *path* is used instead.
Each of these directories is searched in turn for the **.ext** files in
a design.

**-r *rthresh***  
Set the resistance threshold to *rthresh* ohms. Similar in function to
**-c**, but for resistances. The default value for *rthresh* is 10 ohms.

**-s *sym***=***value***  
It's possible to use special attributes attached to transistor gates to
control the length and width of transistors explicitly, rather than
allowing them to be determined by the extractor. These attributes are of
the form **ext:w=***width***^** or **ext:l=***length***^**, where
*width* or *length* can either be numeric, or textual. (The trailing
\`\`**^**'' indicates that these are transistor gate attributes). If
textual, they are treated as symbols which can be assigned a numeric
value at the time *ext2sim* is run. The **-s** flag is used to assign
numeric values to symbols. If a textual symbol appears in one of the
above attributes, but isn't given a numeric value via **-s** (or **-S**
below), then it is ignored; otherwise, the transistor's length or width
is set to the numeric value defined for that symbol. *(This option is
not currently used by extcheck,* but it is common to ext2sim (1) and
other tools that are written using the extflat (3) library)

**-C**  
Set the capacitance threshold to infinity. Because this avoids any
internodal capacitance processing, all tools will run faster when this
flag is given.

**-R**  
Set the resistance threshold to infinity.

**-S *symfile***  
Each line in the file *symfile* is of the form *sym***=***value*, just
like the argument to the **-s** flag above; the lines are interpreted in
the same fashion. *(This option is not currently used by extcheck,* but
it is common to ext2sim et. al.)

**-T *tech***  
Set the technology in the output **.sim** file to *tech*. This overrides
any technology specified in the root **.ext** file.

# SEE ALSO

ext2dlys (1), ext2sim (1), ext2spice (1), magic (1), rsim (1),
sim2spice (1), ext (5), sim (5)

# AUTHOR

Walter Scott

# BUGS

The **-s** mechanism is incomplete; it should allow quantities other
than transistor lengths and widths to be specified.
