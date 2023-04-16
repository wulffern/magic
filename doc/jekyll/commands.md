---
layout: post
title: Commands
math: true
---


    
### Table of Contents

[Command-line invocation (usage)](#Usage)  
[Script Invocation](#Script)  
[Magic command summary](#Commands)  

Obligatory Screenshot

[Screenshot of Magic](../giffiles/magic-screenshot.gif)

This screenshot, from Magic version 7.2, shows off a number of
features of the Tcl version, including the cell manager window, the
tech manager window, the toolbar, the console command-line entry
window, and popup dialog boxes. Also shows off the version 7.1+
features of the OpenGL display and the non-Manhattan geometry
extension.

Magic version 7.4 Usage (command-line invocation)

Basic usage:  


<table data-border="1" data-frame="box" data-rules="none"
data-cellpadding="6" data-bgcolor="white">
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><table data-border="0" data-frame="box" data-rules="none"
data-cellspacing="0" data-cellpadding="0" data-bgcolor="white">
<tbody>
<tr class="odd">
<td><strong>magic</strong>
[<strong>-noc</strong>[<strong>onsole</strong>]]
[<strong>-now</strong>[<strong>rapper</strong>]] [<strong>-d</strong>
<em>devType</em>] [<strong>-T</strong> <em>technology</em>]
[<em>file</em>]</td>
</tr>
</tbody>
</table></td>
</tr>
</tbody>
</table>


where:

**-noconsole**

(Tcl version only) Uses the calling terminal for terminal-based
command-line input. Otherwise, a Tk console window is used.

**-nowrapper**

(Tcl version only) Magic layout windows use the GUI wrapper,
including cell and technology manager windows, layer toolbar, and
file menu.

**-d** *devType*

(all versions) Select the graphics interface at runtime. Specifying
an invalid *devType* will result in a list of known types. The
possible values of *devType* are determined at compile time, but the
usual ones are **NULL** (no graphics), **X11**, and **OpenGL**. X11
is the usual default.

**-T** *technology*

(all versions) Select the appropriate technology (.tech) file. At
present (this is on the to-do list), magic cannot change technology
after startup. So the technology file corresponding to the layout to
be loaded must be supplied to the command line at startup. The
default technology is scmos, which is included with the magic source
distribution. The complete list of available technology files
depends on what has been installed on the system (see the
[technology file](#tech) page for details).

*file*

(all versions) Load the layout (.mag) file *file* into the layout
window on startup.

Other standard usage:  


**magic** \[**-dnull**\] \[*file*\]

  

**magic** \[**-r**\[**ecover**\]\]

  
where options are as follows:

-recover  

This option recovers a layout after a crash. Note that crash
recovery files are only *automatically* created and updated by the
Tcl/Tk version of magic. A single file containing multiple layouts
is placed in the /tmp directory. Upon normal program exit, it is
removed. However, if magic terminates abnormally due to a program
bug, reception of a termination signal from the operating system, or
a system crash or shutdown, the file will remain and can be
recovered. It is *very* important that you recover the file from the
same directory where it was initially created; otherwise, if startup
conditions are different (such as a different technology specified),
layout may be lost.

-dnull *file*  

This option starts magic without graphics. It is appropriate for
running magic in batch mode from a script. Note that there is a
subtle difference between options "-d null" and "-dnull". The former
starts magic without the ability to create a layout window, but
still invokes the graphics initialization routines (in the Tcl/Tk
version, a Tk window may briefly appear). The latter form
specifically ignores all graphics and therefore runs with less
overhead on startup.

Complete usage information:  
  

<table data-border="1" data-frame="box" data-rules="none"
data-cellpadding="6" data-bgcolor="white">
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><table data-border="0" data-frame="box" data-rules="none"
data-cellspacing="0" data-cellpadding="0" data-bgcolor="white">
<tbody>
<tr class="odd">
<td><strong>magic</strong>
[<strong>-noc</strong>[<strong>onsole</strong>]]
[<strong>-now</strong>[<strong>rapper</strong>]]
[<strong>-nowindow</strong>] [<strong>-d</strong> <em>devType</em>]
[<strong>-T</strong> <em>technology</em>] [<strong>-m</strong>
<em>monType</em>] [<strong>-D</strong>] [<em>file</em>]</td>
</tr>
</tbody>
</table></td>
</tr>
</tbody>
</table>

  
where the additional options not covered above are:  
  

-nowindow  

(Tcl version only) Run without displaying an initial layout window.
This is used mainly for GUI wrapper scripts which like to generate
and handle their own windows.

-m *monType*  

(obscure) *monType* names a monitor type. This is used in the search
for the colomap file name, which is designated
&lt;tech&gt;.&lt;planes&gt;.&lt;mon&gt;.cmap1. The default is
"**std**" (corresponding to colormap file "mos.7bit.std.cmap1". The
only other monitor type for which colormaps exist in the
distribution is "mraster". This provides a way for users to override
the system color assignments.

-D  

(all versions) Run in Debug mode.

Obsolete usage information:  
  

**magic** \[-g *gPort*\] \[-i *tabletPort*\] \[-F *objFile* *saveFile*\]
...

  
where the additional options not covered above are:  
  

-g *gPort*  

(largely obsolete) *gPort* names a device to use for the display.
This was generally used in the past with dual-monitor systems,
especially Sun systems in which the layout display might go to
/dev/fb.

-i *tabletPort*  

(largely obsolete) *tabletPort* names a device to use for graphics
input. This has not been tested with modern graphics tablet devices.
It is ignored by the X11 and OpenGL display interfaces.

-F *objFile* *saveFile*  

(largely obsolete) Create an executable file of the current magic
process, a core image snapshot taken after all initialization.
*objFile* is the name of the original executable, and the image will
be saved in *saveFile*. This only works on VAXen and SUNs running an
old SunOS (using a.out executables).

Script invocation

Often it is helpful to have a shell script invoke magic with specific
options to perform tasks such as generating a GDS file for tapeout.
The following example code clip imports GDS into magic as a "vendor
cell":

<table data-border="1" data-frame="box" data-rules="none"
data-cellpadding="6" data-bgcolor="beige">
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><table data-border="0" data-frame="box" data-rules="none"
data-cellspacing="0" data-cellpadding="0" data-bgcolor="white">
<tbody>
<tr class="odd">
<td>magic -dnull -noconsole &lt;&lt; EOF</td>
</tr>
<tr class="even">
<td>drc off</td>
</tr>
<tr class="odd">
<td>box 0 0 0 0</td>
</tr>
<tr class="even">
<td>load vtop.mag -force</td>
</tr>
<tr class="odd">
<td>drc off</td>
</tr>
<tr class="even">
<td>gds readonly true</td>
</tr>
<tr class="odd">
<td>gds rescale false</td>
</tr>
<tr class="even">
<td>gds read ${cellname}.gds</td>
</tr>
<tr class="odd">
<td>cellname rename ${cellname} vtmp</td>
</tr>
<tr class="even">
<td>load vtmp</td>
</tr>
<tr class="odd">
<td>select top cell</td>
</tr>
<tr class="even">
<td>set pname [lindex [cellname list children] 0]</td>
</tr>
<tr class="odd">
<td>cellname rename \\\$pname ${cellname}</td>
</tr>
<tr class="even">
<td>select cell \\\${pname}_0</td>
</tr>
<tr class="odd">
<td>identify ${cellname}_0</td>
</tr>
<tr class="even">
<td>writeall force ${cellname}</td>
</tr>
<tr class="odd">
<td>quit -noprompt</td>
</tr>
<tr class="even">
<td>EOF</td>
</tr>
</tbody>
</table></td>
</tr>
</tbody>
</table>



General window commands (for all windows)

<table data-border="1" data-frame="box" data-rules="none" width="90%"
data-cellspacing="0" data-cellpadding="5" data-bgcolor="#ccffff">
<tbody>
<tr class="odd">
<td><a href="#center"><strong>center</strong></a></td>
<td><a href="#closewindow"><strong>closewindow</strong></a></td>
<td><a href="#cursor"><strong>cursor</strong></a></td>
</tr>
<tr class="even">
<td><a href="#help"><strong>help</strong></a></td>
<td><a href="#imacro"><strong>imacro</strong></a></td>
<td><a href="#logcommands"><strong>logcommands</strong></a></td>
</tr>
<tr class="odd">
<td><a href="#macro"><strong>macro</strong></a></td>
<td><a href="#openwindow"><strong>openwindow</strong></a></td>
<td><a href="#redo"><strong>redo</strong></a></td>
</tr>
<tr class="even">
<td><a href="#redraw"><strong>redraw</strong></a></td>
<td><a href="#scroll"><strong>scroll</strong></a></td>
<td><a href="#setpoint"><strong>setpoint</strong></a></td>
</tr>
<tr class="odd">
<td><a href="#sleep"><strong>sleep</strong></a></td>
<td><a href="#specialopen"><strong>specialopen</strong></a></td>
<td><a href="#quit"><strong>quit</strong></a></td>
</tr>
<tr class="even">
<td><a href="#undo"><strong>undo</strong></a></td>
<td><a href="#updatedisplay"><strong>updatedisplay</strong></a></td>
<td><a href="#version"><strong>version</strong></a></td>
</tr>
<tr class="odd">
<td><a href="#view"><strong>view</strong></a></td>
<td><a href="#windowborder"><strong>windowborder</strong></a></td>
<td><a href="#windowcaption"><strong>windowcaption</strong></a></td>
</tr>
<tr class="even">
<td><a href="#windownames"><strong>windownames</strong></a></td>
<td><a
href="#windowscrollbars"><strong>windowscrollbars</strong></a></td>
<td><a href="#xview"><strong>xview</strong></a></td>
</tr>
<tr class="odd">
<td><a href="#zoom"><strong>zoom</strong></a></td>
<td><a href="#tk_path_name"><em>tk_path_name</em></a></td>
<td></td>
</tr>
</tbody>
</table>

## Layout window commands and window-less commands

[**addcommandentry**](#addcommandentry)

[**addpath**](#addpath)

[**antennacheck**](#antennacheck)

[**array**](#array)

[**box**](#box)

[**calma**](#calma)

[**caption**](#caption)

[**cellmanager**](#cellmanager)

[**cellname**](#cellname)

[**cellsearch**](#cellsearch)

[**channels**](#channels)

[**cif**](#cif)

[**clockwise**](#clockwise)

[**closewrapper**](#closewrapper)

[**contact**](#contact)

[**copy**](#copy)

[**corner**](#corner)

[**crash**](#crash)

[**crashbackups**](#crashbackups)

[**crosshair**](#crosshair)

[**def**](#def)

[**delete**](#delete)

[**deletecommandentry**](#deletecommandentry)

[**down**](#down)

[**drc**](#drc)

[**dump**](#dump)

[**edit**](#edit)

[**element**](#element)

[**erase**](#erase)

[**expand**](#expand)

[**ext**](#ext)

[**ext2sim**](#ext2sim)

[**ext2spice**](#ext2spice)

[**extract**](#extract)

[**extresist**](#extresist)

[**exttosim**](#ext2sim)

[**exttospice**](#ext2spice)

[**feedback**](#feedback)

[**fill**](#fill)

[**findbox**](#findbox)

[**findlabel**](#findlabel)

[**flatten**](#flatten)

[**flush**](#flush)

[**garoute**](#garoute)

[**gds**](#gds)

[**get**](#get)

[**getcell**](#getcell)

[**getnode**](#getnode)

[**goto**](#goto)

[**grid**](#grid)

[**help**](#help)

[**identify**](#identify)

[**initialize**](#initialize)

[**instance**](#instance)

[**iroute**](#iroute)

[**irsim**](#irsim)

[**label**](#label)

[**lef**](#lef)

[**load**](#load)

[**maketoolbar**](#maketoolbar)

[**move**](#move)

[**measure**](#measure)

[**openwrapper**](#openwrapper)

[**paint**](#paint)

[**path**](#path)

[**peekbox**](#peekbox)

[**plot**](#plot)

[**plow**](#plow)

[**polygon**](#polygon)

[**popbox**](#popbox)

[**popstack**](#popstack)

[**port**](#port)

[**promptload**](#promptload)

[**promptsave**](#promptsave)

[**property**](#property)

[**pushbox**](#pushbox)

[**pushstack**](#pushstack)

[**render3d**](#render3d)

[**resumeall**](#resumeall)

[**rotate**](#rotate)

[**route**](#route)

[**save**](#save)

[**scalegrid**](#scalegrid)

[**search**](#search)

[**see**](#see)

[**select**](#select)

[**setlabel** *(#version 8.0)*](#setlabel)

[**shell**](#shell)

[**sideways**](#sideways)

[**snap**](#snap)

[**spliterase**](#spliterase)

[**splitpaint**](#splitpaint)

[**startup**](#startup)

[**straighten**](#straighten)

[**stretch**](#stretch)

[**suspendall**](#suspendall)

[**tag**](#tag)

[**tech**](#tech)

[**techmanager**](#techmanager)

[**tool** *(#non-Tcl version)*](#tool)

[**tool** *(#Tcl version)*](#changetool)

[**unexpand**](#unexpand)

[**unmeasure**](#unmeasure)

[**upsidedown**](#upsidedown)

[**what**](#what)

[**wire**](#wire)

[**writeall**](#writeall)

[**xload**](#xload)

## Netlist window commands

[**add**](#netlist/add)

[**cleanup**](#netlist/cleanup)

[**cull**](#netlist/cull)

[**dnet**](#netlist/dnet)

[**dterm**](#netlist/dterm)

[**extract**](#netlist/extract)

[**find**](#netlist/find)

[**flush**](#netlist/flush)

[**join**](#netlist/join)

[**netlist**](#netlist/netlist)

[**orient**](#netlist/orient)

[**pushbutton**](#netlist/pushbutton)

[**print**](#netlist/print)

[**ripup**](#netlist/ripup)

[**savenetlist**](#netlist/savenetlist)

[**shownet**](#netlist/shownet)

[**showterms**](#netlist/showterms)

[**trace**](#netlist/trace)

[**verify**](#netlist/verify)

[**writeall**](#netlist/writeall)

## 3D window commands

[**cif**](#wind3d/cif)

[**closewindow**](#wind3d/closewindow)

[**cutbox**](#wind3d/cutbox)

[**defaults**](#wind3d/defaults)

[**help**](#wind3d/help)

[**level**](#wind3d/level)

[**refresh**](#wind3d/refresh)

[**render**](#wind3d/render)

[**scroll**](#wind3d/scroll)

[**see**](#wind3d/see)

[**view**](#wind3d/view)

[**zoom**](#wind3d/zoom)

## Color window commands

[**pushbutton**](#color/pushbutton)

[**color**](#color/color)

[**load**](#color/load)

[**save**](#color/save)

## "Wizard" (developer) layout commands

[**\*bypass**](#wizard/bypass)

[**\*coord**](#wizard/coord)

[**\*extract**](#wizard/extract)

[**\*plow**](#wizard/plow)

[**\*psearch**](#wizard/psearch)

[**\*showtech**](#wizard/showtech)

[**\*tilestats**](#wizard/tilestats)

[**\*tsearch**](#wizard/tsearch)

[**\*watch**](#wizard/watch)

## "Wizard" (developer) window commands

[**\*crash**](#wizard/crash)

[**\*files**](#wizard/files)

[**\*grstats**](#wizard/grstats)

[**\*pause**](#wizard/pause)

[**\*winddebug**](#wizard/winddebug)

[**\*winddump**](#wizard/winddump)

## User's Guide Development

To be done:

-   Add some general topics, not command-specific.
-   Incorporate a lot of the currently text-only material into HTML
format.
-   Run latex2html on all of the LaTeX distribution documentation.
-   More information on the routers and netlists
-   Subject index.

## addcommandentry

------------------------------------------------------------------------

Generate a new frame for command-line entry.

------------------------------------------------------------------------

### Usage:

**addcommandentry** *framename*  


where *framename* is the Tk pathname of a frame.

### Summary:

The **addcommandentry** command is used with the GUI wrapper in magic
version 7.3. It adds a narrow text entry frame to the bottom of the
window. This frame duplicates the output of the Tk console, and can be
used as an alternative console from which to enter command-line
commands. The *framename* is the Tk path name of the frame holding the
layout window. By default these are named **.layout1**, **.layout2**,
etc., for each call to **openwrapper**.

The command entry window has a prompt with the name of the Tk frame,
e.g., "layout1&gt;", and all window commands entered into this area
will be relative to the associated layout window.

### Implementation Notes:

**addcommandentry** is implemented as a Tcl procedure defined in the
GUI wrapper script. It is only available when the wrapper is used,
that is, when **magic** is invoked with argument **-w**.

### See Also:

[**deletecommandentry**](#deletecommandentry)  
[**openwrapper**](#openwrapper)  

## addpath

------------------------------------------------------------------------

Append to current search path

------------------------------------------------------------------------

### Usage:

**addpath** \[*path*\]  


where *path* is the path of a directory to add to the list of
directories searched for layout cells, relative to the current
working directory.

### Summary:

The **addpath** command is used to control which directories magic
searches when attempting to read an undefined cell. It can only be
used to append new directories to the existing search path (see
below). This command is most often used when groups of subcells such
as a standard-cell library or padframe library is kept in a separate
place from the rest of the layout. In such cases it is convenient to
put this command in the **.magic** file in the layout directory to
ensure that all cells required by the layout are accessible at
runtime.

### Implementation Notes:

**addpath** is a **magic** built-in command. It is retained for
backwards compatibility, but is superceded by the **path** command,
which allows complete control over the layout search path contents, as
well as other search paths used by **magic**.

### See Also:

[**path**](#path)  
[**getcell**](#getcell)  

## antennacheck

------------------------------------------------------------------------

Run antenna violation checks on the current edit cell.

------------------------------------------------------------------------

### Usage:

**antennacheck** \[*option*\]  


where *option* may be one of the following:

**run**  
"**antennacheck run**" is equivalent to "**antennacheck**" with no
arguments, and causes an antenna violation check to be run.

**debug**  
Sets up debug mode for the next antenna run. In addition to feedback
entries, additional information will be printed to the terminal
about each error encountered.

### Summary:

The **antennacheck** command runs a full check for antenna violations
on the entire area of the cell being edited. Antenna violations are
defined in the technology file as the ratios of metal area to
sensitive MOSFET transistor gate areas to which the metal is attached.
The antenna effect is a manufacturing problem caused by charge buildup
on gates during metal etching. The metal being etched forms an antenna
that gathers charge on the net connected to the gate. If the area of
metal is large enough the gate can be destroyed by the process of
etching. The foundry specifies what the area ratio limit must be. The
check is done progressively from the lowest metal layer to the
highest. If violations are found, then feedback entries are created
covering the area of both the gate and the metal layer at which the
violation occurred.

The **extract** command must be run prior to **antennacheck** to
obtain the extracted characteristics of the design, so that all
sensitive transistor gates can be identified and enumerated.

### Implementation Notes:

**antennacheck** is implemented as a built-in **magic** command. The
**antennacheck** command was introduced in magic version 8.2.150 along
with technology file extensions to support the antenna rule violations
(see the online Maintainer's Manual \#2).

### See Also:

[*extract*](#extract)  

## array

------------------------------------------------------------------------

Array everything in the current selection

------------------------------------------------------------------------

### Usage:

**array** *option*  


where *option* is one of the following:

*xsize ysize*  
Array the selection with *xsize* copies in the **x** (horizontal)
direction and *ysize* copies in the **y** (vertical) direction.
Array pitch is determined by the current cursor box.

*xlo xhi ylo yhi*  
Array the selection with indices *xlo, xhi, ylo*, and *yhi*
inclusive. Thus, (*xhi* - *xlo* + 1) copies will be created in the
**x** direction and (*yhi* - *ylo* + 1) copies will be created in
the **y** direction. Arrayed cell uses will be numbered according to
the indices. Array pitch is determined by the current cursor box.

**count** \[\[*xlo*\] *xhi* \[*ylo*\] *yhi*\]  
With no arguments, returns the array indices of the currently
selected cell. With arguments, is equivalent to the first two
options (see above).

**width** \[*value*\]  
With no arguments, returns the array spacing in **x** of the
currently selected cell. With arguments, redefines the spacing in
**x** between cells in the array.

**height** \[*value*\]  
With no arguments, returns the array spacing in **y** of the
currently selected cell. With arguments, redefines the spacing in
**y** between cells in the array.

**pitch** \[*x y*\]  
With no arguments, returns the array spacing in **x** and **y** of
the currently selected cell. With arguments, redefines the spacing
in **x** and **y** between cells in the array.

**position** \[*x y*\]  
With no arguments, returns the position of the array origin. With
arguments, redefines the array origin.

**help**  
Print help information

### Summary:

The **array** command creates multiple copies of the current paint
selection. In the case of selected paint, only the first two options
are available, and the function makes multiple copies of the selected
paint in the **x** and/or **y** direction(s). In the case of selected
cells, the cell is copied multiple times but is maintained in the
database as an *array* type, rather than multiple individual uses. As
an *array* type, certain functions such as **move** or **copy**
operate on the array as a single unit, and subsequent calles to the
**array** command may resize the array.

The cursor box defines the pitch between cells or paint copies in the
array. The height of the box is the pitch in **y**, and the width of
the box is the pitch in **x**.

The Tcl version allows useful constructs on the command line such as:

**array width \[expr {1 + \[array width\]}\]**  
**move s \[array height\]**

The first example expands the pitch of the array by 1 unit in the
**x** direction without requiring explicitly sizing the cursor box to
match the array pitch. The second example moves the array down by the
**y**

### Implementation Notes:

**array** is implemented as a **magic** built-in command. Command
options which return values from a selected array generate Tcl
results in the Tcl version of **magic**.

## box

------------------------------------------------------------------------

Move box dist units in direction or (with no arguments) show box size.

------------------------------------------------------------------------

### Shortcuts:

Key macro **b** implements the command **box** (with no arguments),
which prints information about the box to the console (terminal
stdout).

### Usage:

**box** \[*option*\]  


where *option* is one of the following:

\[[*direction*](#direction) \[[*distance*](#distance)\]\]  
Move the box in the indicated direction by the indicated distance.

**width** \[*width*\]  
Set or return box width

**height** \[*height*\]  
Set or return box height

**size** \[*width height*\]  
Set or return box size

**position** \[*llx lly*\] \[**-edit**\]  
Set or return box position

**values** \[*llx lly urx ury*\] \[**-edit**\]  
Set or return box coordinates.

**move** *direction distance*|**cursor**  
Move box position

**grow** *direction distance*  
Expand box size

**shrink** *direction distance*  
Shrink box size

**corner** *direction distance*|**cursor**  
Reposition a box corner

**exists**  
Is the cursor box present?

**remove**  
Make the cursor box disappear from the window

**help**  
Print help information

### Summary:

The **box** command, with no arguments, prints information about the
current position and size of the cursor box to the console (terminal
stdout). The output shows the lower-left and upper-right coordinates
of the box, plus the box width, height, and area. These coordinates
and dimensions are shown both in microns and in lambda units. If the
internal grid has been subdivided to a finer grid than lambda, then
internal units will also be reported.

With arguments, the **box** command adjusts the position and
dimensions of the cursor box as outlined in the Usage section (see
above). The **-edit** switch causes coordinate values to be reported
relative to the origin of the current edit cell, if the edit cell is
not the topmost cell in the layout window.

**NOTE:** Prior to magic 8.1.43, the "**-edit**" switch did not work
with "**position**". Starting from magic 8.1.43, "**-edit**" works
with any **box** option and returns values in the coordinate system of
the child cell, if the current edit cell is not the topmost cell in
the window.

For a discussion of valid distances, see the page
[*distance*](#distance). This includes dimensional values such as
*width* and *height*, e.g.,

**box width 1.2um**

Note that because metric dimensions do not always match lambda
dimensions, the dimension may be rounded down to the nearest lambda.
This is important in case this use of **box** is intended to meet some
DRC requirement. For the options **move** and **corner**, the
*distance* may be the keyword "**cursor**", indicating that the box
should be moved or the corner repositioned to the position of the
cursor. These versions of the command implement the standard mouse
button bindings for the "box tool" in layout windows.

For a discussion of valid directions, see the page
[**direction**](#direction). Note that special cases **box grow
center** and **box shrink center** will cause the box to expand or
shrink on all sides, whereas **box move center** is nonfunctional.
Also, the **box corner** command expects the direction to be a
nonmanhattan direction (**ur**, **bl**, etc.), indicating the corner
to be repositioned.

### Implementation Notes:

**box** is implemented as a **magic** built-in command. Command
options with keywords and no arguments return Tcl results in the Tcl
version of **magic**. However, to be backwardly compatible with
versions of **magic** prior to 7.3, the **box** command with no
arguments prints information directly to stdout (the command-line
console). The separate option **box values** is provided to return the
two box coordinates (lower-left and upper-right) as a Tcl list.

The use of returned Tcl values allows various useful constructs on the
command-line, such as:

**box move e \[box width\]** **box height \[box width\]**

The first example moves the box to the right by the width of the box,
while the second example makes the box square by adjusting the height
to match the width.

### See Also:

[**snap**](#snap) [**scalegrid**](#scalegrid)

## gds, calma

------------------------------------------------------------------------

Read GDSII input or generate GDSII output.

------------------------------------------------------------------------

### Usage:

**gds** \[*option*\]  

**calma** \[*option*\]  


where *option* is one of the following:  
Primary options:

**help**  
Print usage information

**read** *file*  
Read GDSII format from file *file* into the edit cell. If *file*
does not have a file extension, then **magic** searches for a file
named *file*, *file*.gds, *file*.gds2, or *file*.strm.

**warning** \[*option*\]  
Set warning information level. "*option*" may be one of the
following:

**default**  
The default setting is equivalent to all the other options
(**align**, **limit**, **redirect**, and **none**) being disabled.

**align**  
Generate warnings during a "**cif see**" command if the alignment of
geometry is on fractional lambda. Normally, magic allows contacts to
be drawn at half-lambda positions. If this violates DRC requirements
for the minimum output grid, this warning setting can be used to
detect such violations.

**limit**  
Limit warnings to the first 100 warnings or errors only.

**redirect** \[*file*\]  
Redirect all warnings to an output file named *file*. If *file* is
not given, then redirection is disabled.

**none**  
Do not produce any warning messages on GDS input.

**write** *file*  
Output GDSII format to "*file*" for the window's root cell.

Options for **gds read**:

**datestamp** \[**yes**|**no**|*value*\]  
When reading a GDS file, the resulting layout views in magic will be
timestamped according to the declared datestamp action. If **yes**
(the default), then the creation date timestamp from the GDS file is
transferred to the layout cell. If **no**, then the datestamp is set
to zero and will be created when the cell is saved to disk. If
*value*, then the specified value (in UNIX format of seconds since
the epoch) will be used for the layout timestamp.

**drccheck** \[**yes**|**no**\]  
If set to **no**, then do not mark cells read from GDS as requiring
DRC checks (default **yes**).

**flatglob** \[**none**|*string*\]  
Flatten cells by name pattern on input. This is the more exacting
version of **flatten**, as it allows specific cells to be flattened.
Each call with an argument *string* adds *string* to the list of
name patterns to be checked. A call with the option **none** will
remove all patterns. A call with no options will return the list of
string patterns that will be applied to inputs. The strings may use
standard shell-type glob patterns, with **\*** for any length string
match, **?** for any single character match, **\\** for special
characters, and **\[\]** for matching character sets or ranges
(introduced in version 8.3.102).

**flatten** \[**yes**|**no**|*number*\]  
Flatten simple cells (e.g., contacts) on input. This helps magic to
use its contact-area representation of contacts, and can also avoid
situations where contacts are lost or translated to "generic" types
because the arrayed part of the contacts is missing one or more
residue layers. The default number of shapes in an input to be
considered "simple" is 10, but this can be set with the *number*
argument. A *number* of zero implies **flatten no**, and a non-zero
*number* implies **flatten yes**. Otherwise, the use of **yes** and
**no** toggles the flattening behavior without affecting any value
previously set by **flatten** *number*.

**maskhints** \[**yes**|**no**|*layers*\]  
When set to **yes**, then after reading each cell definition from
the GDS file, magic will re-generate the GDS output data from its
internal representation of the cell. Where the output data does not
match the input data, and where the technology file defines mask
hints in the **cifoutput** section for a GDS layer, magic will
automatically generate the mask hint property for the cell such that
writing GDS of the cell will produce exactly the same mask data as
was in the original GDS file. Alternatively to specifying "**yes**",
a comma-separated list *layers* of GDS layers to create mask hints
for can be specified (default **no**).

**noduplicates** \[**yes**|**no**\]  
When reading a GDS file, this option forces magic to ignore cell
definitions in the GDS file that are already present in the database
(that is, for which a cell of the same name already exists). This
can be used, for example, to pre-load an abstract view of a cell
before reading a GDS file containing that cell. This option should
be used with extreme caution, since there is no check as to whether
the existing view is compatible with the one in the GDS file.

**ordering** \[**yes**|**no**\]  
Forces post-ordering of subcells read from a GDS file; that is, if a
cell use is encountered before it is defined, magic will read
through the remainder of the file until it finds the definition,
read it, and then return to the original file position to continue
reading. This option is always enabled when using **gds flatten**.
Otherwise, the default behavior is **ordering no** to avoid lengthy
searches through the GDS stream file.

**polygon subcells** \[**yes**|**no**\]  
Put non-Manhattan polygons into subcells. Default is "no". Normally
this option is not needed. However, input layout that defines a
number of angled wires, particularly those that are closely spaced,
can cause **magic** to generate literally millions of internal
tiles. This tends to be true in particular for corner cells in
padframes for deep submicron feature sizes, where the angled corners
are required to meet the DRC specification. When set to "yes", each
polygon encountered in the GDS input is placed in its own
uniquely-named subcell. This prevents interations with other
polygons on the same plane and so reduces tile splitting.

**readonly** \[**yes**|**no**\]  
Set cell as "read-only". This has the effect of marking each cell
definition (using the **property** method) with the start and end
positions of the cell definition in the input file. In subsequent
output, the cell definition will be transferred verbatim from the
input to the output file. This is useful for 3rd-party standard
cells or pad cells where the original GDS is trusted and it is
desirable to bypass the boolean operators of **magic**'s GDS reader
and writer to prevent the layout from being altered. Note that
"read-only" layout can be written to a .mag file, but the contents
of this file are representational only. It can be useful to keep a
simplified respresentation in the case of pad cells or digital
standard cells, for example, by reading them using a GDS input style
that defines only metal layers.

**rescale** \[**yes**|**no**\]  
Allow or disallow internal grid subdivision while reading GDS input.
Default is "yes". Normally, one wants to allow rescaling to ensure
that the GDS is displayed exactly as it is in the input file.
Occasionally, however, the GDS input is on a very fine scale, such
as nanometers, and it is preferable to snap the input to lambda
boundaries rather than to subsplit the internal grid to such a fine
value. The "**cif limit**" function may also be used to limit grid
subdivision to a minimum value.

**unique** \[**yes**|**no**\]  
When reading a GDS file, this option forces magic to rename cell
definitions in the database when a cell of the same name is
encountered in the GDS file. The default behavior is to overwrite
the cell with the new definition. The existing cell is renamed by
adding a suffix with an underscore and a number. The number is
incremented until the name fails to match any known cell name in the
database.

Options for **gds write**:

**abstract** \[**allow**|**disallow**\]  
Define the behavior for abstract cells (e.g., cells derived from LEF
views). If allowed, then these cells will be written to GDS even if
the abstraction layers (e.g., metal obstructions) have no defined
GDS layers. If disallowed, the GDS file will not be written if
abstract cells exist. The default behavior is **disallow**.

**addendum** \[**yes**|**no**\]  
Do not output vendor (readonly) cell definitions. Only the
references will be output. This makes the output file an addendum to
any existing vendor GDS libraries.

**arrays** \[**yes**|**no**\]  
Output arrays as individual subuses (like in CIF). Default is "no".
Normally there is no reason to do this.

**compress** \[*value*\]  
For non-zero *value*, apply gzip-style compression to the output
stream. Per the gzip compression algorithm, *value* represents a
level of compression effort, and ranges from 1 to 9. When *value* is
zero, no compression is applied and the output is standard GDS
format, and the output file extension is ".gds". When *value* is
non-zero, compression is applied, and the output file extension is
".gds.gz". With no argument, return the current compression setting.
The default compression setting is zero (no compression applied;
output is plain GDS).

**contacts** \[**yes**|**no**\]  
Causes contacts to be written to the GDS file as subcell arrays
(experimental, introduced in version 7.3.55). This method can
produce very efficient output compared to writing each contact cut
square separately.

**datestamp** \[**yes**|**no**|*value*\]  
When writing a GDS file, each cell definition is given a header
containing two date stamps, one for the creation date, and one for
the modification date. By default, magic writes the cell's internal
timestamp as the creation date, and sets the modification date stamp
to zero. The **datestamp** option, if set to **no**, will also set
the creation date stamp to zero. If set to *value*, then the
specified stamp value will be output for the creation date. The
stamp value should be an integer in the format used by the UNIX
time() system call, which is the number of seconds since January 1,
1970, or equivalently the Tcl command "**clock seconds**". Note that
very few tools make use of the GDS date stamps. But having a valid
date stamp means that a GDS file cannot be written twice with the
exact same contents, which has implications for repositories like
git. When writing libraries, it is useful to set a date stamp tied
to a version number and apply that date stamp to all files written
for the library.

**labels** \[**yes**|**no**\]  
Cause labels to be output when writing GDSII. Default is "yes".
Normally there is no reason not to do this.

**library** \[**yes**|**no**\]  
Do not write the top level cell into the output GDS file, but write
only the subcells of the top level cell. Default is "no".

**lower** \[**yes**|**no**\]  
Allow both upper and lower case in labels. Default is "yes".

**merge** \[**yes**|**no**\]  
Concatenate connected tiles into polygons when generating output.
Depending on the tile geometry, this may make the output file up to
four times smaller, at the cost of speed in generating the output
file. Some programs like the field equation solver HFSS won't work
properly with layout broken into many tiles; other programs like
Calibre will complain about acute angles when non-Manhattan geometry
is broken into triangles. GDS output limits polygon boundaries to a
maximum of 200 points, which limits the efficiency of the merge
method. The default value if "no"; e.g., all GDS output is a direct
conversion of tiles to rectangle and triangle boundary records.

**nodatestamp** \[**yes**|**no**\]  
Backwardly compatible alternative to the **datestamp** option.
Setting **nodatestamp yes** is equivalent to setting **datestamp
no** (see above).

**undefined** \[**allow**|**disallow**\]  
Define the behavior for undefined cells (e.g., cells whose layout
contents could not be found). If allowed, then the calls to these
cells will be written to GDS even if the cell itself is not defined
in the GDS (see the **addendum** option, above). If disallowed, the
GDS file will not be written if undefined references exist. The
default behavior is **disallow**.

### Summary:

The **gds** command reads or produces GDSII output (also known as
"stream" output, or "calma" output after the name of the company that
invented the format), or sets various parameters affecting the GDS
input and output. In magic, the GDS read and write routines are a
subset of the CIF read and write routines, and so it is important to
note that certain **cif** command options (q.v.) also affect GDS input
and output. In particular, **cif istyle** and **cif ostyle** set the
input and output styles from the technology file, respectively.

If no option is given, a CALMA GDS-II stream file is produced for the
root cell, with the default name of the root cell definition and the
filename extension ".gds".

**gds read** will read both (gzip-)compressed and uncompressed GDS
files. **gds write** will only write compressed files as indicated by
the **gds compress** setting.

### Implementation Notes:

**gds** is implemented as a built-in function in **magic**. The
**calma** command is an alias for **gds** and is exactly equivalent.

### Bugs:

-   The **cif** command options that affect GDS input and output
should *really* be duplicates as options of the GDS command.
-   GDS input is "interpreted" through boolean operations in the
technology file definition, and so it is not guaranteed that all
input will be read correctly.
-   Not all non-Manhattan geometry is read correctly.
-   The input can be fouled up if the magic grid is rescaled during
input. This error can be avoided by scaling the grid prior to GDS
read-in.
-   "polygon subcells" in GDS creates a duplicate image of the layout
read into the subcells; this needs to be fixed.

### See Also:

[**cif**](#cif)  

## caption

------------------------------------------------------------------------

Configures the titlebar of the GUI wrapper on a layout window

------------------------------------------------------------------------

### Usage:

**caption** *layoutwindow*  


where *layoutwindow* is the Tk pathname of the layout window (not
the top-level frame).

### Summary:

The **caption** command is used by the GUI wrapper script and is
normally not a user command. It configures the titlebar of the wrapper
frame in a way that is similar to the titlebar in the original
(non-Tcl, non-GUI) versions of **magic**. The style and contents of
the titlebar may be changed by redefining this procedure in Tcl.

### Implementation Notes:

**caption** is implemented as a Tcl script in the GUI wrapper.

### See Also:

[**windowcaption**](#windowcaption)  

## cellmanager

------------------------------------------------------------------------

Invoke the cell manager GUI window

------------------------------------------------------------------------

### Shortcuts:

Menu option *Options-&gt;Cell Manager* implements the command
**cellmanager create** in the GUI layout window. This menu item has a
checkbox and is used both to open and to close the Cell Manager
window.

### Usage:

**cellmanager** \[*option*\]  


where *option* is optional and may be one of the following:

**update**  
The default option if no option is given. Update the cell manager to
reflect the current state of the layout.

**create**  
Create the cell manager window. This option is normally called only
from the "*Cell Manager*" button in the **magic** GUI layout window.

### Summary:

The **cellmanager** command is normally invoked automatically from
inside the GUI wrapper procedures and tag callbacks, and normally
should not be called directly from the command line.

![](graphics/cellmgr.gif)  
*Figure 1. The Cell Manager Window*

The Cell Manager window (see above) is a separate top-level window
with Tk pathname "**.cellmgr**". It consists of a tree widget (defined
in the Tcl package "BLT") display in the center, a message window and
button on the bottom, and a row of menu buttons at the top.

The Cell Manager displays cells for everything stored in the layout
database. As such, it is only necessary to have a single cell manager
for all layout windows. However, commands such as "Load", "Edit",
etc., apply to a specific window. When a new layout window is created,
rather than generate a new Cell Manager window, the new window is
added to the list of "target windows". The currently selected target
window is displayed at the bottom of the Cell Manager. This is also a
button that can be used to select a new target window. If only one
layout window is present, the target is declared "default" and may be
left alone.

The hierarchical tree view shows all of the *instances* (cell uses) in
a layout. When first invoked, the top-level cell only is shown, with a
"folder" icon showing that this cell contains uses. By clicking on the
"+" symbol next to the folder icon, the tree view is expanded to show
the cell instances used by the top-level layout cell. This expansion
may continue until a cell instance is found that does not contain any
descendents. Note that the name displayed is the name of the cell
*definition*, with the instance number given in parentheses after the
name. If the instance name is non-default (e.g., because it came from
a 3rd party vendor database or was altered with the **identify**
command), the full name of the instance is shown in the parentheses.
If the instance is arrayed, the array indices are shown in brackets
("**\[\]**") after the instance number or name.

The use of tag callbacks on commands allows the cell manager to be
updated in response to certain commands entered on the command line.
The cell manager will be updated in response to a "**load**" or
"**getcell**" command.

The menu buttons perform certain functions based on the selection made
in the tree window. These functions are as follows:

**Load**  
load the selected cell into the window. The **load** command is
invoked and passed the cell definition name of the selected cell
instance. Note that this menu function operates on the cell
*definition* of the selected cell *instance*.

**Edit**  
edit the selected cell instance. The cell instance selected becomes
the current edit cell.

**Expand**  
expand (or unexpand, if already expanded) the selected cell
instance.

**Zoom**  
change the current view of the layout so that it is centered on the
selected cell instance, and scaled so that the cell instance fills
the screen.

### Implementation Notes:

**cellmanager** is implemented as a Tcl procedure in the GUI wrapper
script. Because layouts with complicated hierarchy can cause **magic**
to run very slowly due to processing in the cell manager window, this
window does not exist on startup and is deleted entirely when turned
off in the "*Options*" menu of the GUI wrapper layout window.

**cellmanager** uses the tree display widget from the tcl package
"BLT". Therefore, in order to see the Cell Manager window, it is
necessary to have BLT installed on the system. If BLT is not
installed, no option for "Cell Manager" will appear in the "Options"
menu of the GUI wrapper window.

**cellmanager** depends on the GUI wrapper window, as it is defined in
the wrapper script. Therefore, to use the cell manager, it is
necessary to invoke magic with the option "**-w**".

### Bugs:

The "**Expand**" function should expand everything above the selected
cell. Otherwise, if something higher up in the hierarchy is
unexpanded, the selected cell will not be expanded.

### See Also:

[**load**](#load)  
[**edit**](#edit)  
[**expand**](#expand)  
[**zoom**](#zoom)  

## cellname

------------------------------------------------------------------------

Operations on cell definitions.

------------------------------------------------------------------------

### Usage:

**cellname** *option*  


where *option* is one of the following:

\[**list**\] **children** \[*name*\]  
List all of the children definitions of cell *name*, or the children
of the currently selected cell instance.

\[**list**\] **childinst** \[*name*\]  
List all of the children instances of cell *name*, or the children
of the currently selected cell instance.

\[**list**\] **parent** \[*name*\]  
List the parent cell definition of cell *name*, or the parent of the
currently selected cell instance.

\[**list**\] **exists**|**self** \[*name*\]  
Returns the name of the cell if the cell exists, or false (0) if the
cell does not exist (is not loaded into the database; the cell may
still exist on disk). If *name* is not present, returns the name of
the currently selected cell.

\[**list**\] **allcells**  
List all of the cells in the database. Note that expansion is not
automatic, so cells that are not expanded are not searched.

\[**list**\] **topcells**  
List the name of the top-level cell or cells. Note that the cells
are searched in the whole database, so multiple cells may be
returned, regardless of what cell is the topmost cell in the layout
window. For that, use **cellname window** (see below).

\[**list**\] **window**  
List the name of the topmost cell in the window. If only one window
exists, it is implicit. If more than one window exists, the command
operates on the window from which the command was called if the ":"
macro was used to invoke the command. Otherwise, the window can be
specified as the command (q.v. *tk\_path\_name*).

**create** *name*  
Create a new cell definition with name *name*. This is most often
used with scripts, where it is not necessary or desirable to load
the cell into the window. Note that this command does not search the
layout search path for a cell named *name*.mag, so it can be used to
replace a cell which exists on disk but is not currently loaded.

**rename** *name newname*  
Change the name of the cell definition *name* to *newname*.

**delete** *name*  
Delete the cell definition with name *name*. If cell *name* is a
descendent of another cell, the command will be prohibited. If the
cell *name* is currently the topmost cell in the window, the window
will be loaded with default cell "(UNNAMED)".

**dereference** *name*  
Perform a flush of the cell (per the "**flush**" command), first
removing any file path associated with the cell, so that the cell
will be reloaded from the first valid location found using the
search paths.

**flags**  
Reports flag settings for the cell. Flags which are reported are
"available", "modified", and "readonly". Flag "available" is true if
the cell has been loaded into the database. Flag "modified" is true
if layout changes have been made to the cell. Flag "readonly" is
true if the cell has been locked to prevent edits.

**timestamp** *name* \[*value*\]  
Reports or sets the cell timestamp value. Note that timestamps
should be handled automatically, so setting the timestamp is
discouraged outside of limited functions like creating cell
libraries. The timestamp is in the usual integer format and can be
printed as a human-readable date using the Tcl **clock** command,
e.g., "clock format \[cellname timestamp\]".

**filepath** *name* \[**default**|*pathname*\]  
With no option, this command returns the path to the file for the
cell *name*, or the keyword "**default**" if the cell is not
associated with a specific file path. With option "**default**", if
the cell is associated with a specific file path, that association
is removed. With option "*pathname*", the cell is associated with
the given file path. Note that this is meant to be used to resolve
issues with database libraries being moved from one location or
another. More typically, the "**save**" command should be used to
create a copy of the (possibly modified) cell in a new location.
Changing the filepath will not perform any disk reads or writes.

**writeable** *name* \[**true**|**false**\]  
Option **writeable false** makes the current cell read-only and
therefore prevents any edits from being written to disk. If magic is
compiled with file-locking, then any advisory lock on the file is
released. Option **writeable true** makes the current cell
read-write. If magic is compiled with file-locking, then magic
attempts to grab an advisory lock on the file. If a lock is already
held on the file, then the command cannot be executed, and the cell
remains read-only. Option **writeable** with no other arguments
returns the state of the cell (roughly equivalent to **cellname
flags readonly**).

### Summary:

The **cellname** command performs various operations on cell
definitions. For the first four options listed above, **cellname**
lists cells by their relationship to cell *name*, or to the current
selection if no *name* is given. The optional argument **list**
returns the result as a list. In particular, in the Tcl version of
magic, this list is a Tcl result that may be operated on by Tcl
procedures.

### Implementation Notes:

**cellname** is implemented as a built-in function in **magic** The
Tcl version of magic returns Tcl results when the "**list**" option is
present. **instance** is essentially an alias for the **cellname**
command, and takes the same options, but references are to cell
instances rather that cell definitions (q.v.).

The command option **cellname list exists** is nonsensical from the
standpoint of the end-user (if the cell is selected, of course it
exists). However, it is a very useful function for Tcl scripts to
determine the name of the cell that is currently selected.

The **cellname** command replaces a number of commands that briefly
appeared in version 7.1, such as **parent**, **child**, and **top**.
These commands are now options of the **cellname** and **instance**
commands.

### See Also:

[**instance**](#instance)  
[**load**](#load)  
[**path**](#path)  
[**flush**](#flush)  
[*tk\_path\_name*](#tk_path_name)  

## cellsearch

------------------------------------------------------------------------

Execute a TCL procedure on each cell definition or instance in the
hierarchy

------------------------------------------------------------------------

### Usage:

**cellsearch** \[**instances**\] *procedure*  


where *procedure* is the name of a predefined Tcl procedure (see
Summary, below).

### Summary:

The **cellsearch** command is a method for user access to the
**magic** database search routines. It searches the hierarchical
database for all cell definitions and applies the callback procedure
to each. If the **instances** keyword is present, it searches the
database for all cell instances and applies the callback procedure to
each. The callback procedure must be defined as described below. Note
that the callback method into Tcl is inherently slow and should only
be used for non-compute-intensive tasks.

The Tcl callback procedure for the **instances** version of the
**cellsearch** command is passed six values, the bounding box
coordinates of the instance, the instance use name (id), and the name
of the parent cell definition. The procedure must be defined to accept
these six arguments, as in the following example:

proc inst_callback {llx lly urx ury usename defname} {
puts stdout "Instance $usename of $defname bbox $llx $lly $urx $ury"
}


The Tcl callback procedure for the cell definition search is passed
one value, the name of the cell definition. The procedure must be
defined to accept this single argument, as in the following example:

proc def_callback {defname} {
puts stdout "Cell $defname"
}


### Implementation Notes:

**cellsearch** is implemented as an internal **magic** command that
links to an external Tcl procedure as a callback function. This
routine is experimental and subject to change without notice.

### Bugs:

As currently implemented, there is no protection against calling a
**magic** command from the callback procedure that will alter the
internal cell hash table while it is being traversed, causing a crash.
The implementation should be changed to a 2-step procedure that
traverses the cell hash table first, creating an internal list of
function arguments to pass for each cell, and then executes the
callback function on each.

There are more efficient ways of executing the callback function than
Tcl\_EvalEx(). In particular, the procedure should be cast as a Tcl
object and Tcl\_EvalObjEx() used.

The callback function should allow in-line Tcl procedures and use the
standard Tcl/Tk method of "%" escape sequences used as arguments to
the callback function that allow the user to specify what arguments
are passed to the callback function (as is done for the **tag**
command).

### See Also:

[**search**](#search)  

## center

------------------------------------------------------------------------

Center the layout window view on the cursor lower-left coordinate, or
the indicated coordinate if present.

------------------------------------------------------------------------

### Usage:

**center** \[*x y*\]  


where *x y* is a coordinate in default magic units

### Summary:

Without arguments, the **center** command centers the layout window on
the lower-left corner of the cursor box. When values *x* and *y* are
given, the view is centered on that coordinate. Coordinate values must
be in (integer) units of the **magic** internal grid. This command is
similar to the "**view** *llx lly urx ury*" command, which centers on
a box instead of a point.

### Implementation Notes:

**center** is implemented as a magic built-in command.

### Bugs:

Coordinate values should be any acceptable value, including lambda,
grid, and metric values, as they are for the **box** command.

### See Also:

[**view**](#view)  

## tool

------------------------------------------------------------------------

Change the layout "tool" (button bindings). This page describes the
version of the command used by the Tcl version of magic.

------------------------------------------------------------------------

### Shortcuts:

Key macro *space* implements the command **tool**.  
Key macro *shift-space* implements the command **tool box**.

### Usage:

**tool** \[*name*|**info**\]  


where *name* may be one of **box**, **wiring**, **netlist**, or
**pick**.

### Summary:

The **tool** command selects or queries the mode of operation of the
mouse buttons in the layout window. Each *tool* type has a unique set
of button bindings.

Without arguments, the **tool** command selects the next tool type in
round-robin fashion. With a tool type as argument, the button bindings
switch to those for the indicated tool. With the **info** option, a
summary of the commands bound to each mouse button is given for the
current tool.

The default mouse bindings for each of the three tools is as follows:

-   *Box Tool*
**left**  
Move the box so its lower-left corner is at cursor position

**right**  
Resize box by moving upper-right corner to cursor position

**middle**  
Paint box area with material underneath cursor

In addition, you can move or resize the box by different corners
by pressing left or right, holding it down, moving the cursor near
a different corner and clicking the other (left or right) button
down then up without releasing the initial button.
-   *Wiring Tool*
**left**  
Pick wire material and size from under the cursor and begin
interactive wire placement.

**right**  
Cancel interactive wire placement.

**middle**  
Place a wire at the position shown by the interactive wire tool
highlight box, and continue interactive wire placement.

*shift-***left**  
Change the type of wire to the next plane (e.g., metal1 to metal2)

*shift-***right**  
Change the type of wire to the previous plane (e.g., metal2 to
metal1)

*shift-***middle**  
Place a contact at the current location and switch to the wire
type on the next plane.

**scrollwheel up **  
Increase the wire size by one unit

**scrollwheel down **  
Decrease the wire size by one unit

Note that the methods for the wire tool differ significantly
between Tcl-based magic, with its interactive capabilities, and
non-Tcl-based magic.
-   *Netlist Tool*
**left**  
Select the net containing the terminal nearest the cursor

**right**  
Toggle the terminal nearest the cursor into/out of current net

**middle**  
Join current net and net containing terminal nearest the cursor
-   *Pick Tool*
**left**  
Remove the current selection from the layout, place it in the pick
buffer, and follow the cursor.

**right**  
Cancel the current pick buffer and stop following the cursor.

**middle**  
Place a copy of the pick buffer at the current location, and
continue following the cursor.

*shift-***middle**  
Make a copy of the current selection from the layout, place it in
the pick buffer, and follow the cursor.

The pick tool is an interactive feature only available in the
Tcl-based version of magic.

### Implementation Notes:

**tool** is implemented as a Tcl script in the Tcl-based version of
**magic**. The command duplicates the function of the original
**tool** command, which remains for the non-Tcl based version of
magic, and which performs the function of changing the cursor style in
the window.

Button functions for each "tool" may be added to or modified in the
startup scripts. The Tcl variable **Opts(tool)** contains the current
tool name, and may be used by a user **tool** procedure overriding the
default one in "tools.tcl".

### See Also:

[**tool (#non-Tcl version)**](#tool)

## channels

------------------------------------------------------------------------

See channels (as feedback) without doing routing.

------------------------------------------------------------------------

### Usage:

**channels** \[*netlist\_file*\]  


where *netlist\_file* is the name of a .net file containing a
routing netlist.

### Summary:

The **channels** command is part of the routing module in **magic**.
It shows available routing channels in the current layout using the
feedback layer mechanism.

### Implementation Notes:

**channesl** is implemented as a built-in command in **magic** when
the router modules are compiled in (which currently they are, in the
default compilation configuration).

### See Also:

[**route**](#route)  
[**iroute**](#iroute)  
[**garoute**](#garoute)  

## cif

------------------------------------------------------------------------

Read CIF input or generate CIF output.

------------------------------------------------------------------------

### Usage:

**cif** \[*option*\]  


where *option* is one of the following:

**help**  
Print usage information

**arealabels** \[**yes**|**no**\]  
Enable/disable use of the CIF area label extension. The default is
"yes". Normally there is no reason not to do this.

\[**list**\] **coverage** *layer* \[**box**\]  
Report the coverage of the indicated CIF layer within the bounds of
the current edit cell. This is useful for fabrication processes that
require a minimum amount of coverage for specific layers (usually
the metal routing layers). With option **list** in front, return
only the coverage value, as a decimal. Otherwise, the value is
returned as a percentage, with additional diagnostic information
about the area analyzed.

With option "**box**", report the density inside the cursor box area
only.

**idcell** \[**yes**|**no**\]  
Enable/disable use of the CIF cell ID extension. The default is
"yes". Normally there is no reason not to do this.

**scale** **in**|**out**  
Report the number of microns per internal unit for the current
style. If "**in**" is specified, the value is reported for the
current CIF/GDS input style. If "**out**" is specified, the value is
reported for the current CIF/GDS output style.

*Warning:* For a long time (prior to magic 8.0.180), this function
was "**cif lambda in**|**out**" and claimed to return the number of
microns per lambda. For backwards compatibility, this syntax is
retained, but its use is discouraged.

**limit** \[*value*\]  
Limit the amount of internal grid subdivision to the indicated value
(which is dimensionless, the ratio of the maximum subdivision to the
current lambda value). If no *value* is given, the current limit is
reported. By default, the value is set to 100, as grid subdivision
smaller than this amount can result in integer overflow on
subsequent CIF or GDS output.

**rescale** \[**yes**|**no**\]  
Allow or disallow internal grid subdivision while reading CIF input.
Default is "yes". Normally, one wants to allow rescaling to ensure
that the CIF is displayed exactly as it is in the input file.
Occasionally, however, the CIF input is on a very fine scale, such
as nanometers, and it is preferable to snap the input to lambda
boundaries rather than to subsplit the internal grid to such a fine
value. The **limit** option may also be used to limit grid
subdivision to a minimum value (see above).

**drccheck** \[**yes**|**no**\]  
(Introduced in Magic version 8.0.176) Set to "yes" by default,
causing all cells in the input file to be marked as not checked by
DRC as they are input. Set this to "no" to force magic to treat the
CIF cells as "known DRC clean".

**warning** \[*option*\]  
Set warning information level. "*option*" may be one of the
following:

**default**  
The default setting is equivalent to all the other options
(**align**, **limit**, **redirect**, and **none**) being disabled.

**align**  
Generate warnings during a "**cif see**" command if the alignment of
geometry is on fractional lambda. Normally, magic allows contacts to
be drawn at half-lambda positions. If this violates DRC requirements
for the minimum output grid, this warning setting can be used to
detect such violations.

**limit**  
Limit warnings to the first 100 warnings or errors only.

**redirect** \[*file*\]  
Redirect all warnings to an output file named *file*. If *file* is
not given, then redirection is disabled.

**none**  
Do not produce any warning messages on CIF input.

**polygon subcells** \[**yes**|**no**\]  
Put non-Manhattan polygons into subcells. Default is "no". Normally
this option is not needed. However, input layout that defines a
number of angled wires, particularly those that are closely spaced,
can cause **magic** to generate literally millions of internal
tiles. This tends to be true in particular for corner cells in
padframes for deep submicron feature sizes, where the angled corners
are required to meet the DRC specification. When set to "yes", each
polygon encountered in the CIF input is placed in its own
uniquely-named subcell. This prevents interations with other
polygons on the same plane and so reduces tile splitting.

**paint** *cif\_layers* *magic\_layer* \[*cellname*\]  
Generate the CIF layer(s) specified by *cif\_layers*, then import
them into the Magic database as layer *magic\_layer*. If *cellname*
is specified, then the paint is generated in that cell (which will
be created, if it does not already exist). Otherwise, paint is
generated directly in the edit cell. This is a very useful function,
as it allows the automatic generation of layout from boolean
operations. Principal uses are to auto-generate fill patterns,
auto-generate obstruction geometry in a standard cell, to
automatically place substrate and well contacts into a standard-cell
array, and so forth.

**see** *layers*  
View the CIF/GDS output layers in the comma-separated list *layers*
as feedback entries on the layout. This is useful for determining
what the actual foundry layer types are doing as a result of the
boolean operations in the CIF/GDS output style. Most useful for
debugging technology file CIF/GDS output style sections, or tracing
DRC error reports from sources other than **magic**. CIF output is
computed and feedback is shown only inside the cursor box area.

![](graphics/cif_see.gif)  
*Figure 1. Command **cif see CSP** shows the P+ implant layer
surrounding the P diffusion regions within the cursor box area.*

**statistics**  
Print statistics from the CIF generator, including tile operations,
rectangles output, and interactions between cells. Not especially
useful to the typical end-user.

**prefix** \[*path*\]  
Prepend the path name *path* to cell names in the CIF output. If no
*path* is specified, reports the existing path name.

\[**list|listall**\] **istyle** \[*style*\]  
Set the current input style to *style*. If no *style* is specified,
returns the current input style. To get a list of all available
input styles in the current technology, use the **listall istyle**
option. The **list istyle** option returns the current style name as
a Tcl result.

\[**list|listall**\] **ostyle** \[*style*\]  
Set the current output style to *style*. If no *style* is specified,
returns the current output style. To get a list of all available
output styles in the current technology, use the **listall ostyle**
option. The **list ostyle** option returns the current style name as
a Tcl result.

**flat** *file*  
Output CIF format to "*file*" for the window's root cell, flattening
the hierarchy prior to output.

**read** *file*  
Read CIF format from file *file* into the edit cell. If *file* does
not have a file extension, then **magic** searches for a file named
*file* or *file*.cif.

**write** *file*  
Output CIF format to "*file*" for the window's root cell.


"Wizard" options: Where *option* is one of the following:  

**\*hier** *layer*  
This option is like "**cif see**" but shows the layers that are
generated as the result of hierarchical interactions between
subcells (not including interactions between components of a subcell
array; see below).

**\*array** *layer*  
This option is like "**cif see**" but shows the layers that are
generated as the result of hierarchical interactions between
components of subcell arrays.

**\*hier write** \[ **enable** | **disable** \]  
This sets a global option that enables (default) or disables the
generation of output CIF or GDS layers due to interaction between
subcells (not including inter-array interactions; see below). For
large standard cell layouts where the standard cells are known to
abut properly without causing spacing or overlap errors, disabling
hierarchical generation can greatly reduce the amount of time needed
to generate output. Defining the property **CIFhier** inside a cell
will override the use of **\*hier write disable** and force
hierarchical output for that cell and its descendents.

**\*array write** \[ **enable** | **disable** \]  
This sets a global option that enables (default) or disables the
generation of output CIF or GDS layers due to interaction between
components of subcell arrays. If cells are known to abut properly
without generating spacing errors between them, disabling
hierarchical generation can greatly reduce the amount of time needed
to generate output. Defining the property **CIFhier** inside a cell
will override the use of **\*array write disable** and force
hierarchical output for that cell and its descendents.

### Summary:

The **cif** command reads CIF input or produces CIF input/output
("Caltech Intermediate Format", as described in Mead & Conway), or
sets various parameters affecting the CIF (and GDS) input and output.
Certain **cif** command options also affect GDS input and output.

If no option is given, a CIF file is produced for the root cell, with
the default name of the root cell definition and the filename
extension ".cif".

### Implementation Notes:

**cif** is implemented as a built-in function in **magic**. Options
**list** and **listall** cause output to be returned as a Tcl result,
rather than printed to stdout (the console).

### See Also:

[**gds** (#**calma**)](#gds)  
[**property**](#property) (#property "CIFhier")  

## clockwise

------------------------------------------------------------------------

Rotate the selection and box clockwise

------------------------------------------------------------------------

### Shortcuts:

Key macro **r** implements the command **clockwise** (or **rotate
90**).  
Key macro **R** implements the command **clockwise 270** (or **rotate
-90**).  
Key macro *Control-***R** implements the command **clockwise 180**

### Usage:

**clockwise** \[*degrees*\] \[**-origin**\]  


where *degrees* is the number of degrees to rotate, and must be a
manhattan amount (90, 180, 270).

### Summary:

The **clockwise** command rotates the current selection by the
specified amount, in degrees. The default rotation is by 90 degrees.
The amount of rotation must be one of 90, 180, or 270.

If **-origin** is specified, the rotation is around the origin of the
selection, not around the lower left-hand corner.

### Implementation Notes:

**clockwise** is implemented as a built-in **magic** command. Because
a "standard abbreviation" is **clock** and conflicts with the Tcl
command **clock**, this case is handled specially. The command
**clock** is deprecated in favor of the more general command
**rotate**, but is maintained for backward compatibility.

### See Also:

[**rotate**](#rotate)  

## closewindow

------------------------------------------------------------------------

Close a (non-GUI) window

------------------------------------------------------------------------

### Shortcuts:

Key macro **O** implements the command **closewindow**. This macro is
disabled when using the GUI wrapper.

### Usage:

**closewindow** \[*name*\]  


where *name* is the name of a window.

### Summary:

The **closewindow** command closes a window. Without arguments, if
only one window is present, that window will be closed. Otherwise, if
multiple windows are present, the window to be closed must be
specified by name.

**closewindow** closes both layout windows created with the
**openwindow** command or windows created with the **specialopen**
command.

### Implementation Notes:

**closewindow** is implemented as a built-in **magic** window command.
It should not be used with the GUI wrapper (invoked with **magic
-w**); instead, the **closewrapper** function should be used.

### See Also:

[**openwindow**](#openwindow)  
[**specialopen**](#specialopen)  
[**closewrapper**](#closewrapper)  

## closewrapper

------------------------------------------------------------------------

Close a GUI layout window and all of its associated frames.

------------------------------------------------------------------------

### Shortcuts:

Menu option *File-&gt;Close* implements the command **closewrapper**
*tk\_path\_name* in the GUI layout window.

### Usage:

**closewrapper** *frame\_name*  


where *frame\_name* is the Tk path name of the top-level layout GUI
window frame. By default, this name is .layout1, .layout2, etc., for
successive windows created with the **openwrapper** command.

### Summary:

The **closewrapper** command removes a layout window in the Tcl
version of magic. It is only applicable when magic is invoked with the
GUI wrapper, using **magic -w**, and supercedes the built-in command
**closewindow**.

### Implementation Notes:

**closewrapper** is implemented as a Tcl procedure in the GUI wrapper
script.

### See Also:

[**closewindow**](#closewindow)  
[**openwrapper**](#openwrapper)  

### Table of Contents

[Command-line invocation (usage)](#Usage)  
[Script Invocation](#Script)  
[Magic command summary](#Commands)  

Obligatory Screenshot

[Screenshot of Magic](../giffiles/magic-screenshot.gif)

This screenshot, from Magic version 7.2, shows off a number of
features of the Tcl version, including the cell manager window, the
tech manager window, the toolbar, the console command-line entry
window, and popup dialog boxes. Also shows off the version 7.1+
features of the OpenGL display and the non-Manhattan geometry
extension.

Magic version 7.4 Usage (command-line invocation)

Basic usage:  


<table data-border="1" data-frame="box" data-rules="none"
data-cellpadding="6" data-bgcolor="white">
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><table data-border="0" data-frame="box" data-rules="none"
data-cellspacing="0" data-cellpadding="0" data-bgcolor="white">
<tbody>
<tr class="odd">
<td><strong>magic</strong>
[<strong>-noc</strong>[<strong>onsole</strong>]]
[<strong>-now</strong>[<strong>rapper</strong>]] [<strong>-d</strong>
<em>devType</em>] [<strong>-T</strong> <em>technology</em>]
[<em>file</em>]</td>
</tr>
</tbody>
</table></td>
</tr>
</tbody>
</table>


where:

**-noconsole**

(Tcl version only) Uses the calling terminal for terminal-based
command-line input. Otherwise, a Tk console window is used.

**-nowrapper**

(Tcl version only) Magic layout windows use the GUI wrapper,
including cell and technology manager windows, layer toolbar, and
file menu.

**-d** *devType*

(all versions) Select the graphics interface at runtime. Specifying
an invalid *devType* will result in a list of known types. The
possible values of *devType* are determined at compile time, but the
usual ones are **NULL** (no graphics), **X11**, and **OpenGL**. X11
is the usual default.

**-T** *technology*

(all versions) Select the appropriate technology (.tech) file. At
present (this is on the to-do list), magic cannot change technology
after startup. So the technology file corresponding to the layout to
be loaded must be supplied to the command line at startup. The
default technology is scmos, which is included with the magic source
distribution. The complete list of available technology files
depends on what has been installed on the system (see the
[technology file](#tech) page for details).

*file*

(all versions) Load the layout (.mag) file *file* into the layout
window on startup.

Other standard usage:  


**magic** \[**-dnull**\] \[*file*\]

  

**magic** \[**-r**\[**ecover**\]\]

  
where options are as follows:

-recover  

This option recovers a layout after a crash. Note that crash
recovery files are only *automatically* created and updated by the
Tcl/Tk version of magic. A single file containing multiple layouts
is placed in the /tmp directory. Upon normal program exit, it is
removed. However, if magic terminates abnormally due to a program
bug, reception of a termination signal from the operating system, or
a system crash or shutdown, the file will remain and can be
recovered. It is *very* important that you recover the file from the
same directory where it was initially created; otherwise, if startup
conditions are different (such as a different technology specified),
layout may be lost.

-dnull *file*  

This option starts magic without graphics. It is appropriate for
running magic in batch mode from a script. Note that there is a
subtle difference between options "-d null" and "-dnull". The former
starts magic without the ability to create a layout window, but
still invokes the graphics initialization routines (in the Tcl/Tk
version, a Tk window may briefly appear). The latter form
specifically ignores all graphics and therefore runs with less
overhead on startup.

Complete usage information:  
  

<table data-border="1" data-frame="box" data-rules="none"
data-cellpadding="6" data-bgcolor="white">
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><table data-border="0" data-frame="box" data-rules="none"
data-cellspacing="0" data-cellpadding="0" data-bgcolor="white">
<tbody>
<tr class="odd">
<td><strong>magic</strong>
[<strong>-noc</strong>[<strong>onsole</strong>]]
[<strong>-now</strong>[<strong>rapper</strong>]]
[<strong>-nowindow</strong>] [<strong>-d</strong> <em>devType</em>]
[<strong>-T</strong> <em>technology</em>] [<strong>-m</strong>
<em>monType</em>] [<strong>-D</strong>] [<em>file</em>]</td>
</tr>
</tbody>
</table></td>
</tr>
</tbody>
</table>

  
where the additional options not covered above are:  
  

-nowindow  

(Tcl version only) Run without displaying an initial layout window.
This is used mainly for GUI wrapper scripts which like to generate
and handle their own windows.

-m *monType*  

(obscure) *monType* names a monitor type. This is used in the search
for the colomap file name, which is designated
&lt;tech&gt;.&lt;planes&gt;.&lt;mon&gt;.cmap1. The default is
"**std**" (corresponding to colormap file "mos.7bit.std.cmap1". The
only other monitor type for which colormaps exist in the
distribution is "mraster". This provides a way for users to override
the system color assignments.

-D  

(all versions) Run in Debug mode.

Obsolete usage information:  
  

**magic** \[-g *gPort*\] \[-i *tabletPort*\] \[-F *objFile* *saveFile*\]
...

  
where the additional options not covered above are:  
  

-g *gPort*  

(largely obsolete) *gPort* names a device to use for the display.
This was generally used in the past with dual-monitor systems,
especially Sun systems in which the layout display might go to
/dev/fb.

-i *tabletPort*  

(largely obsolete) *tabletPort* names a device to use for graphics
input. This has not been tested with modern graphics tablet devices.
It is ignored by the X11 and OpenGL display interfaces.

-F *objFile* *saveFile*  

(largely obsolete) Create an executable file of the current magic
process, a core image snapshot taken after all initialization.
*objFile* is the name of the original executable, and the image will
be saved in *saveFile*. This only works on VAXen and SUNs running an
old SunOS (using a.out executables).

Script invocation

Often it is helpful to have a shell script invoke magic with specific
options to perform tasks such as generating a GDS file for tapeout.
The following example code clip imports GDS into magic as a "vendor
cell":

<table data-border="1" data-frame="box" data-rules="none"
data-cellpadding="6" data-bgcolor="beige">
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><table data-border="0" data-frame="box" data-rules="none"
data-cellspacing="0" data-cellpadding="0" data-bgcolor="white">
<tbody>
<tr class="odd">
<td>magic -dnull -noconsole &lt;&lt; EOF</td>
</tr>
<tr class="even">
<td>drc off</td>
</tr>
<tr class="odd">
<td>box 0 0 0 0</td>
</tr>
<tr class="even">
<td>load vtop.mag -force</td>
</tr>
<tr class="odd">
<td>drc off</td>
</tr>
<tr class="even">
<td>gds readonly true</td>
</tr>
<tr class="odd">
<td>gds rescale false</td>
</tr>
<tr class="even">
<td>gds read ${cellname}.gds</td>
</tr>
<tr class="odd">
<td>cellname rename ${cellname} vtmp</td>
</tr>
<tr class="even">
<td>load vtmp</td>
</tr>
<tr class="odd">
<td>select top cell</td>
</tr>
<tr class="even">
<td>set pname [lindex [cellname list children] 0]</td>
</tr>
<tr class="odd">
<td>cellname rename \\\$pname ${cellname}</td>
</tr>
<tr class="even">
<td>select cell \\\${pname}_0</td>
</tr>
<tr class="odd">
<td>identify ${cellname}_0</td>
</tr>
<tr class="even">
<td>writeall force ${cellname}</td>
</tr>
<tr class="odd">
<td>quit -noprompt</td>
</tr>
<tr class="even">
<td>EOF</td>
</tr>
</tbody>
</table></td>
</tr>
</tbody>
</table>



General window commands (for all windows)

<table data-border="1" data-frame="box" data-rules="none" width="90%"
data-cellspacing="0" data-cellpadding="5" data-bgcolor="#ccffff">
<tbody>
<tr class="odd">
<td><a href="#center"><strong>center</strong></a></td>
<td><a href="#closewindow"><strong>closewindow</strong></a></td>
<td><a href="#cursor"><strong>cursor</strong></a></td>
</tr>
<tr class="even">
<td><a href="#help"><strong>help</strong></a></td>
<td><a href="#imacro"><strong>imacro</strong></a></td>
<td><a href="#logcommands"><strong>logcommands</strong></a></td>
</tr>
<tr class="odd">
<td><a href="#macro"><strong>macro</strong></a></td>
<td><a href="#openwindow"><strong>openwindow</strong></a></td>
<td><a href="#redo"><strong>redo</strong></a></td>
</tr>
<tr class="even">
<td><a href="#redraw"><strong>redraw</strong></a></td>
<td><a href="#scroll"><strong>scroll</strong></a></td>
<td><a href="#setpoint"><strong>setpoint</strong></a></td>
</tr>
<tr class="odd">
<td><a href="#sleep"><strong>sleep</strong></a></td>
<td><a href="#specialopen"><strong>specialopen</strong></a></td>
<td><a href="#quit"><strong>quit</strong></a></td>
</tr>
<tr class="even">
<td><a href="#undo"><strong>undo</strong></a></td>
<td><a href="#updatedisplay"><strong>updatedisplay</strong></a></td>
<td><a href="#version"><strong>version</strong></a></td>
</tr>
<tr class="odd">
<td><a href="#view"><strong>view</strong></a></td>
<td><a href="#windowborder"><strong>windowborder</strong></a></td>
<td><a href="#windowcaption"><strong>windowcaption</strong></a></td>
</tr>
<tr class="even">
<td><a href="#windownames"><strong>windownames</strong></a></td>
<td><a
href="#windowscrollbars"><strong>windowscrollbars</strong></a></td>
<td><a href="#xview"><strong>xview</strong></a></td>
</tr>
<tr class="odd">
<td><a href="#zoom"><strong>zoom</strong></a></td>
<td><a href="#tk_path_name"><em>tk_path_name</em></a></td>
<td></td>
</tr>
</tbody>
</table>

## Layout window commands and window-less commands

[**addcommandentry**](#addcommandentry)

[**addpath**](#addpath)

[**antennacheck**](#antennacheck)

[**array**](#array)

[**box**](#box)

[**calma**](#calma)

[**caption**](#caption)

[**cellmanager**](#cellmanager)

[**cellname**](#cellname)

[**cellsearch**](#cellsearch)

[**channels**](#channels)

[**cif**](#cif)

[**clockwise**](#clockwise)

[**closewrapper**](#closewrapper)

[**contact**](#contact)

[**copy**](#copy)

[**corner**](#corner)

[**crash**](#crash)

[**crashbackups**](#crashbackups)

[**crosshair**](#crosshair)

[**def**](#def)

[**delete**](#delete)

[**deletecommandentry**](#deletecommandentry)

[**down**](#down)

[**drc**](#drc)

[**dump**](#dump)

[**edit**](#edit)

[**element**](#element)

[**erase**](#erase)

[**expand**](#expand)

[**ext**](#ext)

[**ext2sim**](#ext2sim)

[**ext2spice**](#ext2spice)

[**extract**](#extract)

[**extresist**](#extresist)

[**exttosim**](#ext2sim)

[**exttospice**](#ext2spice)

[**feedback**](#feedback)

[**fill**](#fill)

[**findbox**](#findbox)

[**findlabel**](#findlabel)

[**flatten**](#flatten)

[**flush**](#flush)

[**garoute**](#garoute)

[**gds**](#gds)

[**get**](#get)

[**getcell**](#getcell)

[**getnode**](#getnode)

[**goto**](#goto)

[**grid**](#grid)

[**help**](#help)

[**identify**](#identify)

[**initialize**](#initialize)

[**instance**](#instance)

[**iroute**](#iroute)

[**irsim**](#irsim)

[**label**](#label)

[**lef**](#lef)

[**load**](#load)

[**maketoolbar**](#maketoolbar)

[**move**](#move)

[**measure**](#measure)

[**openwrapper**](#openwrapper)

[**paint**](#paint)

[**path**](#path)

[**peekbox**](#peekbox)

[**plot**](#plot)

[**plow**](#plow)

[**polygon**](#polygon)

[**popbox**](#popbox)

[**popstack**](#popstack)

[**port**](#port)

[**promptload**](#promptload)

[**promptsave**](#promptsave)

[**property**](#property)

[**pushbox**](#pushbox)

[**pushstack**](#pushstack)

[**render3d**](#render3d)

[**resumeall**](#resumeall)

[**rotate**](#rotate)

[**route**](#route)

[**save**](#save)

[**scalegrid**](#scalegrid)

[**search**](#search)

[**see**](#see)

[**select**](#select)

[**setlabel** *(#version 8.0)*](#setlabel)

[**shell**](#shell)

[**sideways**](#sideways)

[**snap**](#snap)

[**spliterase**](#spliterase)

[**splitpaint**](#splitpaint)

[**startup**](#startup)

[**straighten**](#straighten)

[**stretch**](#stretch)

[**suspendall**](#suspendall)

[**tag**](#tag)

[**tech**](#tech)

[**techmanager**](#techmanager)

[**tool** *(#non-Tcl version)*](#tool)

[**tool** *(#Tcl version)*](#changetool)

[**unexpand**](#unexpand)

[**unmeasure**](#unmeasure)

[**upsidedown**](#upsidedown)

[**what**](#what)

[**wire**](#wire)

[**writeall**](#writeall)

[**xload**](#xload)

## Netlist window commands

[**add**](#netlist/add)

[**cleanup**](#netlist/cleanup)

[**cull**](#netlist/cull)

[**dnet**](#netlist/dnet)

[**dterm**](#netlist/dterm)

[**extract**](#netlist/extract)

[**find**](#netlist/find)

[**flush**](#netlist/flush)

[**join**](#netlist/join)

[**netlist**](#netlist/netlist)

[**orient**](#netlist/orient)

[**pushbutton**](#netlist/pushbutton)

[**print**](#netlist/print)

[**ripup**](#netlist/ripup)

[**savenetlist**](#netlist/savenetlist)

[**shownet**](#netlist/shownet)

[**showterms**](#netlist/showterms)

[**trace**](#netlist/trace)

[**verify**](#netlist/verify)

[**writeall**](#netlist/writeall)

## 3D window commands

[**cif**](#wind3d/cif)

[**closewindow**](#wind3d/closewindow)

[**cutbox**](#wind3d/cutbox)

[**defaults**](#wind3d/defaults)

[**help**](#wind3d/help)

[**level**](#wind3d/level)

[**refresh**](#wind3d/refresh)

[**render**](#wind3d/render)

[**scroll**](#wind3d/scroll)

[**see**](#wind3d/see)

[**view**](#wind3d/view)

[**zoom**](#wind3d/zoom)

## Color window commands

[**pushbutton**](#color/pushbutton)

[**color**](#color/color)

[**load**](#color/load)

[**save**](#color/save)

## "Wizard" (developer) layout commands

[**\*bypass**](#wizard/bypass)

[**\*coord**](#wizard/coord)

[**\*extract**](#wizard/extract)

[**\*plow**](#wizard/plow)

[**\*psearch**](#wizard/psearch)

[**\*showtech**](#wizard/showtech)

[**\*tilestats**](#wizard/tilestats)

[**\*tsearch**](#wizard/tsearch)

[**\*watch**](#wizard/watch)

## "Wizard" (developer) window commands

[**\*crash**](#wizard/crash)

[**\*files**](#wizard/files)

[**\*grstats**](#wizard/grstats)

[**\*pause**](#wizard/pause)

[**\*winddebug**](#wizard/winddebug)

[**\*winddump**](#wizard/winddump)

## User's Guide Development

To be done:

-   Add some general topics, not command-specific.
-   Incorporate a lot of the currently text-only material into HTML
format.
-   Run latex2html on all of the LaTeX distribution documentation.
-   More information on the routers and netlists
-   Subject index.

## contact

------------------------------------------------------------------------

Paint a contact at the intersection of two layers.

------------------------------------------------------------------------

### Usage:

**contact** \[**erase**\] *type*  


### Summary:

The **contact** command computes the intersection area (inside the
cursor box) of the two (or more) residue types that make up the
contact type *type*, and paints the contact type *type* on top of the
area of intersection.

Option **contact erase** erases contacts from the area of the cursor
box without affecting the metal layers (or stacked contacts)
surrounding the contact being erased. (Note that the **erase** command
will remove both the contact type and the surrounding metal layers.)

### Implementation Notes:

**contact** is implemented as a built-in layout command in **magic**.

### See Also:

[**paint**](#paint)  
[**erase**](#erase)  

## copy

------------------------------------------------------------------------

Make a copy of the selection.

------------------------------------------------------------------------

### Shortcuts:

Key macro **c** implements the command **copy**.

### Usage:

**copy** \[*option*\]  


where *option* is one of the following:

[*direction*](#direction) \[[*distance*](#distance)\]  
Copy the selection relative to the original in the direction
*direction* by an amount *distance*.

**to** *x y*  
Copy the selection to the coordinate location specified by the
coordinate pair *x y*.

### Summary:

The **copy** command creates a copy of the current selection. Without
arguments, the lower-left hand corner of the copied selection is
placed at the current cursor position (the X11 cursor, not the
**magic** "cursor box"). With arguments *direction* and *distance*,
the new copy is placed relative to the original in the indicated
direction by the indicated amount. The default distance is 1 unit
(#usually lambda; see [*distance*](#distance) for further
explication).

Note that usage **copy center** is useful to make a copy in the
current edit cell of a selection of paint and/or subcells in a
non-edit cell. With this use, the copy will be generated directly on
top of the original.

### Implementation Notes:

**copy** is implemented as a built-in **magic** command.

### See Also:

[*direction*](#direction)  
[*distance*](#distance)  

## corner

------------------------------------------------------------------------

Make L-shaped wires inside the cursor box.

------------------------------------------------------------------------

### Usage:

**corner** *d1 d2* \[*layers*\]  


where *d1* and *d2* are valid manhattan
[*directions*](#direction), and *layers* is an optional
comma-separated list of valid paint layers.

### Summary:

The **corner** command makes L-shaped wires inside the cursor box,
filling first in direction *d1*, then in direction *d2*. If no
*layers* are specified, then the cornering algorithm is applied to all
layers crossing the cursor box boundary opposite to direction *d1*. If
*layers* is specified, the cornering algorithm is applied only to
those layers specified. The usage of **corner** is similar to that for
the command **fill** (q.v.).

Below is an example showing how the cornering algorithm responds to
the command **corner n e**. First it finds layers crossing the cursor
box boundary to the south (opposite to the first specified direction,
**north**), and then extends these layers as wires first to the north,
then to the east. The position of the layers leaving the box to the
east is such that the same distance is maintained from each layer to
the north side of the box at the exit point as it was from each layer
to the east side of the box at the entrance point.

![](graphics/corner1.gif) ![](graphics/corner2.gif)  
*Figure 1: The cornering operation in response to the layout shown,
given magic command **corner n e***.

### Implementation Notes:

**corner** is implemented as a built-in **magic** command.

### Bugs:

If the area in the box is not large enough for the cornering algorithm
to produce the cornered wires, unpredictable results often result.

### See Also:

[*direction*](#diretion)  
[**fill**](#fill)  

## crash

------------------------------------------------------------------------

Handle crash backup files

------------------------------------------------------------------------

### Usage:

**crash save** | **recover** \[*filename*\]  


### Summary:

The **crash** command handles crash backup files. The exact operation
depends on the options, and are outlined below:

**crash save**  
creates and writes to a single file a copy of the contents of all
modified cells. If **crash save** has been called previously, then the
filename specified or generated will be used again. If this is the
first call to **crash save**, or if the previous call was **crash save
""**, then a new, unique filename of a file in the system temporary
directory (normally "/tmp") is created and remembered for subsequent
calls to **crash save**.

**crash save** *filename*  
creates and writes to the file *filename* a copy of the contents of
all modified cells. *filename* is retained as the crash filename, so
subsequent uses of **crash save** without a filename specified will
also write to this file.

**crash save ""**  
causes magic to forget the name of the crash file. The next use of
**crash save** without a filename will revert to the behavior of
generating a unique filename in the system temporary directory.

**crash recover**  
searches the system temporary directory for magic crash recovery
files. If one or more such files is found, then the user is prompted
for the action of either recovering or ignoring the most recent file
found. If the chosen action is to recover the file, then the contents
of the saved crash file are loaded into the database, and the file is
removed.

**crash recover** *filename*  
recovers the database from the contents of the saved crash file
*filename* upon successful read-in, the file *filename* is removed.

If a crash file has been generated during a layout editing session,
and magic is exited normally with the "quit" command, then the crash
backup file is removed.

For backward-compatibility, crash backup files are always generated
when magic receives a SIGTERM signal. In the non-Tcl version of magic,
periodic backups are not made.

### Implementation Notes:

**crash** is implemented as a built-in command in **magic**. The
Tcl/Tk version defines various scripts in "tools.tcl" that implement a
periodic backup using the **crash** command. Invoking magic on the
command-line using "**magic -r**" is equivalent to starting magic
followed by the command "**crash recover**".

### See Also:

[**crashbackups**](#crashbackups)  

## crashbackups

------------------------------------------------------------------------

Handle periodic backups during a layout editing session.

------------------------------------------------------------------------

### Usage:

**crashbackups** \[**start**|**stop**|**resume**|**disable**\]  


### Summary:

The **crashbackups** procedure enables or disables the periodic saving
of crash recovery backup files. **crashbackups** or **crashbackups
start** sets the timer for the first periodic save. After the timer
times out, backup file is generated and written in the system temporary
directory, and the timer is reset. By default, the backup interval is 10
minutes (600000 msec). The interval can be changed by setting the value
of Tcl variable **$Opts(backupinterval)** to the interval value in
msec.  
  
**crashbackups stop** removes the timer callback and thus prevents
further writing of backup files. Note that if crash recovery is stopped
or started multiple times during a session, the same filename is used to
save the data.  
  
**crashbackups resume** resumes running interval backups if stopped
using **crashbackups stop**. If the interval backups have never been
started, or have been disabled, this command does nothing.  
  
**crashbackups disable** stops running interval backups and resets to
the state of never having started interval backups. **resume** will have
no effect in this state, and **start** must be issued to start the
interval backups again.  
  

### Implementation Notes:

**crashbackups** is implemented as a Tcl procedure in the "tools.tcl"
script file. It calls the magic command "**crash save**".  

The crash backup interval is handled by the **itimer** system
subroutine. There is only one timer per process. A timer is also used
by some long-running commands such as **extract** to track progress,
so the crash backups must necessarily be suspended when those commands
are using the process timer.

### See Also:

[**crash**](#crash)  

## crosshair

------------------------------------------------------------------------

Implements a crosshair highlight on top of the layout.

------------------------------------------------------------------------

### Usage:

**crosshair** *x y*  

**crosshair off**  


### Summary:

The **crosshair** command generates, moves, or removes a crosshair
highlight in the layout window. Option **off** removes the crosshair,
while coordinates *x y* place the crosshair at a specific layout
location, creating the crosshair if it has been previously disabled.
The crosshair is disabled by default upon startup.

### Implementation Notes:

**crosshair** is implemented as a built-in window command in
**magic**. The crosshair is available as an interactive feature in the
Tcl/Tk version of magic from the "Options" menu. The commands above
are executed in response to pointer motion events.

## cursor

------------------------------------------------------------------------

Return **magic** internal coordinates of the cursor (X11 pointer)

------------------------------------------------------------------------

### Usage:

**cursor** *glyphnum*  

**cursor** \[**internal**|**lambda**|**user**\]  

**cursor** \[**microns**|**window**|**screen**\]

### Summary:

The **cursor** command has two distinct uses. When followed by an
integer value, the cursor glyph is changed to the indicated glyph, as
defined internally to Magic.  
When used without an option, or when followed by a measurement metric
"internal", "lambda", or "user", the **cursor** command returns the
current position of the cursor (the X11 pointer, not the **magic**
cursor box) in layout coordinates. The coordinates are given in the
indicated metric, or in internal units by default.

Magic version 8.1 defines the additional option "**microns**", which
is like the metrics mentioned above bug returns the current position
of the cursor in micron units, where the scalefactor for determining
micron units is defined by the current CIF/GDS output style.

Magic version 8.1 also defines two options for returning pixel
coordinates: Option "**window**" returns the pointer coordinate in
pixels from the bottom left-hand corner of the layout window. Option
"**screen**" returns the pointer coordinate in pixels relative to the
root screen. In X11, this is defined as the top left-hand corner of
the screen. This second form is useful for interacting with the window
manager, for example, to open up a new window or drop-down menu next
to the pointer position.

### Implementation Notes:

**cursor** is implemented as a built-in window command in **magic**.
In the Tcl version of magic, it returns a Tcl result (list of two
elements, **x** and **y** coordinates).

Like all window commands, it reports relative to the existing window
if only one window is present, or the active window if called with the
":" macro. Otherwise, it must be called using the *tk\_path\_name*
command to specify relative to which layout window the cursor
coordinates will be given.

The value returned by **cursor** may be modified according to the
state set by the **snap** command. **cursor user** reports units
relative to the grid set by the **grid** command, which may differ in
aspect between the X and Y axes.

Note, as stated above, which versions of magic support which options.

### See Also:

[**snap**](#snap)  
[**grid**](#grid)  
[*tk\_path\_name*](#tk_path_name)  

## def

------------------------------------------------------------------------

Read or write DEF format files.

------------------------------------------------------------------------

### Usage:

**def** *option*  


where *option* is one of the following:

**read** *filename* \[**-labels**\] \[**-annotate**\] \[**-noblockage**\]  
Read a DEF file *filename*\[**.def**\]

**write** \[*cell*\] \[**-units** *value*\]  
Write DEF for current or indicated cell named *cell*

**help**  
Print help information (command summary)

### Summary:

The **def** command reads and writes DEF format files. These files are
generally assumed to be digital standard-cell based layouts. The DEF
format has no real concept of hierarchy. To generate a valid DEF file
that may be recognized by other software, it is necessary to have a
layout with standard cells using the **port** method to declare input
and output ports. In particular, the **port class** and **port use**
are designed to work with the DEF read and write routines.

The technology file should have a **lef** section describing how LEF
and DEF files should be written. However, if an appropriate LEF file
exists and is read prior to writing a DEF format file, the technology
will be initialized from the file if it is not declared in the
technology file.

Normally the DEF file is written in units of nanometers according to
the active GDS output scale (UNITS DISTANCE MICRONS 1000). If option
"**-units** *value*" is used, then the units indicated by *value* are
used instead of 1000. This option can be used, for example, to
preserve units when re-writing a DEF file that was read with "**def
read**". There is no guarantee that values can be accurately
represented at the specified scale. The **-units** option was
introduced in magic version 8.2.113.

The "**-labels**" option to the "**def read**" command causes each net
in the NETS and SPECIALNETS sections of the DEF file to be annotated
with a label having the net name as the label text.

The "**-annotate**" option will add labels to a layout from a DEF
file, but will not add layer geometry or subcells. This is useful for
labeling all of the regular nets if the DEF file was previously read
without the **-labels** option.

The "**-noblockage**" option will ignore all BLOCKAGES sections in the
DEF file, in effect producing only mask layer geometry. If not
specified, then layer BLOCKAGES in the DEF file are treated like
obstructions in LEF files, and translated into obstruction layers in
magic (per the definition of obstruction layers in either the "lef"
section of the magic technology file, or in a technology LEF file read
prior to reading the DEF file).

### Implementation Notes:

**def** is implemented as a built-in **magic** command. Only the
critical part of the DEF definition has been implemented. Some
uncommon forms of syntax such as wire extensions are not implemented.
This is largely due to the incomplete nature of the LEF/DEF spec. It
is unlikely that such forms will be encountered in third-party input.

### See Also:

[**lef**](#lef)  
[**port**](#port)  

## delete

------------------------------------------------------------------------

Delete everything in selection

------------------------------------------------------------------------

### Shortcuts:

Key macro **d** implements the command **delete**.

### Usage:

**delete**

### Summary:

The **delete** command deletes whatever cells and paint are in the
current selection.

### Implementation Notes:

**delete** is implemented as a built-in **magic** command.

## deletecommandentry

------------------------------------------------------------------------

Remove the GUI window frame for additional command-line entry.

------------------------------------------------------------------------

### Usage:

**deletecommandentry** *framename*  


where *framename* is the Tk pathname of a frame.

### Summary:

The **deletecommandentry** command is used with the GUI wrapper in
magic version 7.3. It removes the text entry frame at the bottom of
the window that duplicates the output of the Tk console. The
*framename* is the Tk path name of the frame holding the layout
window. By default these are named **.layout1**, **.layout2**, etc.,
for each call to **openwrapper**.

### Implementation Notes:

**deletecommandentry** is implemented as a Tcl procedure defined in
the GUI wrapper script. It is only available when the wrapper is used,
that is, when **magic** is invoked with argument **-w**.

### See Also:

[**addcommandentry**](#addcommandentry)  
[**openwrapper**](#openwrapper)  

## *direction*

------------------------------------------------------------------------

Valid direction options in magic

------------------------------------------------------------------------

### Summary:

Directions may be any valid known direction known to magic, including
the following standard directions:

-   **north**, **up**, **top**
-   **south**, **down**, **bottom**
-   **east**, **right**
-   **west**, **left**
-   **center**

Directions may also be one of the combinations:

-   **northeast**
-   **northwest**
-   **southeast**
-   **southwest**

Directions may also be abbreviated. The following abbreviations are
explicitly defined in magic, and all other abbreviations are accepted
as long as the abbreviation can be uniquely identified (such as **r**
for **right** and **l** for **left**).

-   **n**, **u**
-   **s**, **d**
-   **e**
-   **w**
-   **ne**, **ur**, **tr**
-   **se**, **dr**, **br**
-   **sw**, **dl**, **bl**
-   **nw**, **ul**, **tl**

### See Also:

[*distance*](#distance)

## display

------------------------------------------------------------------------

Print graphics mode information

------------------------------------------------------------------------

### Usage:

**display**  


### Summary:

The **display** command prints the type of graphics being used. The
returned value is a string which may be one of the following:
"**NULL**", "**X11**", "**OPENGL**", "**CAIRO**", or some
typographical variant thereof. The returned string will be equal to
the string passed to the "**-d**" command-line option. If no such
option was given on the command line, then the value reflects the
default graphics mode in effect.

### Implementation Notes:

**display** is implemented as a built-in command in **magic**.

## *distance*

------------------------------------------------------------------------

Valid distance specifications in magic.

------------------------------------------------------------------------

### Summary:

Distances are normally interpreted as *lambda* values. However, this
depends on the last use of the **snap** command; **snap internal**
changes the interpretation of units to the internal grid, while **snap
user** changes the interpretation of units to the user grid. Distances
may always be explicitly called out by appending one of the following
to the distance value (with no intervening whitespace):

**i**  
internal units

**l**  
lambda units

**um**  
microns

**mm**  
millimeters

**cu**  
centimicrons

In any case where the internal grid is finer than the declared
distance measure, fractional distances may be specified; e.g.,

**box move e 1.25um**

### See Also:

[**direction**](#direction) [**snap**](#snap)

## down

------------------------------------------------------------------------

Load selected cell into a window

------------------------------------------------------------------------

### Usage:

**down**

### Summary:

The **down** command loads the currently selected cell into the
window. If more than one cell is selected, the one closest to the
cursor (pointer) position will be used, or at worst, one will be
selected arbitrarily.

### Implementation Notes:

**down** is implemented as a built-in window command in **magic**. In
the Tcl version of magic, it is generally deprecated in favor of the
scripted Tcl procedure **pushstack**, and the "tools" script
implementation of the "**&gt;**" macro to invoke **pushstack** on a
selected cell.

### See Also:

[**load**](#load)  
[**pushstack**](#pushstack)  

## drc

------------------------------------------------------------------------

Background design rule checker control and status.

------------------------------------------------------------------------

### Usage:

**drc** *option*  


where *option* is one of the following:

**catchup**  
Run checker and wait for it to complete

**check**  
Recheck area under box in all cells

**count**  
Count and report error tiles in the edit cell.

**euclidean on**|**off**  
Enable/disable Euclidean geometry checking

**find** \[*nth*\]  
Locate next (or *nth*) error in current cell

**help**  
Print help information

**off**  
Turn off background checker

**on**  
Reenable background checker

**status**  
Report whether the background checker is on or off.

**printrules** \[*file*\]  
Print out design rules in *file* or to stdout

**rulestats**  
Print out statistics about design rule database

**statistics**  
Print out statistics gathered by checker

**why**  
Print out reasons for errors under box

**\*halo** \[*value*\]  
Without option *value*, prints out the DRC halo distance, which is
the largest distance at which a DRC interaction can occur outside of
any area to be checked. Becuase large DRC haloes can cause very long
delays in the interactive DRC checks, it can be helpful to use
*value* to force a smaller halo. This causes certain DRC errors to
be missed, but allows all the basic short-distance design rules to
be checked without undue processing delays.

**\*stepsize** \[*value*\]  
The step size is the length of a side of the area into which the DRC
checker routine breaks up larger areas for more efficient
processing. Changing this value can greatly effect the speed of the
DRC checker, although it is difficult to predict what step size is
"optimal". Without option *value*, returns the current value of the
step size.

The Tcl/Tk version of magic defines additional handling with the
"**list**" and "**listall**" keyword before the option name,
indicating that the information be passed back to the interpreter as a
list instead of being printed to the terminal window as text.

**drc list** *option*  


where *option* is one of the following:

**style**  
Return the currently active DRC style name to the interpreter.

**count** \[**total**\]  
Return the DRC error count as a list pair comprising the edit cell
name and the total number of errors found. With **total**, returns
just the count as an integer.

**find** \[*nth*\]  
Return the error description of the next, or *nth*, error to the
interpreter.

**why**  
Return the error description of all errors intersecting the cursor
box to the interpreter, as a list

**drc listall** *option*  


where *option* is one of the following:

**style**  
Return a list of all available DRC styles to the interpreter.

**count** \[**total**\]  
Return the DRC error count as a nested list, where each list item is
a pair comprising the cell name of the cell containing the errors,
and the total number of errors found. With **total**, returns only
the sum of all the values (probably not very useful).

**why**  
Return a nested list containing a detailed description of all errors
intersecting the cursor box to the interpreter. In the topmost list,
every other entry is the text description of a DRC error class. The
list item following the DRC error description is a list of all
errors of that type. Each error is presented as a list of four
values indicating the bounding box of the error, as {*llx lly urx
ury*} values in internal database units.

### Summary:

The **drc** command controls the behavior of magic's "background"
design rule checker. Normally the design rule checker is invoked
whenever the design is changed and checks all parts of the design
close to the changed area that might have been affected by the change.
The design rule checker flags areas that have been checked as it runs.
It starts whenever a layout change has been made or after any command
has been executed if areas of the layout still need to be checked. Any
macro keystroke in the layout window or command executed on the
command line will interrupt the design rule checker pending completion
of the action, at which time the design rule checker will be
reactivated.

The **drc on** and **drc off** options are the main controls for
starting and stopping the design rule checker. **drc status** returns
the status of the background checker, either "on" or "off". The Tcl
version of magic returns a boolean value (0 or 1).

The **drc check** option marks all areas of the layout under the box
as requiring a check and restarts the design rule checker.

The **drc why** and **drc find** commands can be used to query errors
in the layout discovered by the design rule checker. **drc why**
reports the reason for all error regions found inside the **magic**
cursor box. The **drc find** command can be used to find errors that
may not be visible inside the current window view, or that may be
difficult to find on a large layout.

The **drc euclidean on** command can be useful in cases where vendor
design rules intend a Euclidean distance metric (minimum linear
distance) rather than a Manhattan distance metric (minimum distance in
either the **x** or **y** direction, evaluated separately). The
default option is "off", as most vendor rules and design rule checkers
assume Manhattan distances when checking rules.

The remaining options are relativly obscure and unlikely to be useful
to the typical end-user.

### Implementation Notes:

**drc** is implemented as a built-in **magic** command.

## drop

------------------------------------------------------------------------

Paint into descendents of the current edit cell coincident with a
selection.

------------------------------------------------------------------------

### Usage:

**drop** *layers*  


where *layers* is a comma-separated list of types to paint.

### Summary:

The **drop** command paints layer types into descendents of the
current edit cell where selected paint is found. Normally, paint and
erase operations will only change the current edit cell. Selections
can copy paint out of descendents of the current edit cell, but the
descendent cells are not themselves affected. This specialized command
scans an existing selection and determines from which subcell each bit
of paint in the selection was copied from. Then, it paints *layers*
back into those subcells in an area coincident with the selected
paint.

The primary reason this command was created was to deal with regions
such as a pwell region inside a deep nwell. The pwell is often not a
layer in the GDS but is defined by the absence of nwell, over a deep
nwell layer. A drawn pwell is needed for magic to properly extract the
bulk terminal of any transistor in the pwell. But the pwell must exist
in the same cell as the transistor. After reading GDS, a command
sequence such as the following: "**select area dnwell ; select
intersect ~nwell ; drop pwell**" will ensure that the pwell layer
exists over the area inside a deep nwell p-region.

Be aware that because other instances of a cell may exist outside of
the selection area, that all instances of a cell modified by **drop**
will be likewise modified.

### Implementation Notes:

**drop** is implemented as a built-in command in **magic**.

### See Also:

[**select**](#select)  

## dump

------------------------------------------------------------------------

Copy contents of the indicated cell into the current edit cell.

------------------------------------------------------------------------

### Usage:

**dump** *cell* \[*orientation*\] \[**child** *child\_refpoint*\]
\[**parent** *parent\_refpoint*\]  


where *cell* is the name of the cell whose contents are to be
copied, and optional *child\_refpoint* and *parent\_refpoint* are
coordinate pairs of *x y* values, or keywords **ll**, **lr**,
**ul**, or **ur**. The optional *orientation* may be any valid
orientation (flip or rotation), such as **h**, **v**, **90**,
**180**, or **270**. The syntax and use of the orientation and
reference points is the same as for the **getcell** command.

### Summary:

The **dump** command copies contents of the indicated cell *cell* into
the current edit cell. Without arguments, the contents are placed such
that the lower left coordinate of *cell* is at the cursor box lower
left corner. With the **child** argument, the indicated coordinate
position *child\_refpoint* is used instead of the lower-left corner.
With the **parent** argument, the indicated coordinate position
*parent\_refpoint* is used instead of the lower-left corner of the
cursor box.

### Implementation Notes:

**dump** is implemented as a built-in command in **magic**.

### See Also:

[**getcell**](#getcell)

## edit

------------------------------------------------------------------------

Use selected cell as new edit cell

------------------------------------------------------------------------

### Shortcuts:

Key macro **e** implements the command **edit**.

### Usage:

**edit**  


### Summary:

The **edit** command makes the selected cell the new edit cell.

### Implementation Notes:

**edit** is implemented as a built-in **magic** command.

## element

------------------------------------------------------------------------

Handle generic drawing elements (line, box, text) in the layout.

------------------------------------------------------------------------

### Usage:

**element** *option*  


where *option* is one of the following:

**add** *type* *name* *parameters*  
Create a new element. The *name* is a unique name to be assigned to
the new element. The *parameters* depend on the *type*, and are as
follows:

**line** *name style x1 y1 x2 y2*  
Create a new line element, with position starting at coordinate *x1
y1* and ending at *x2 y2*. The line does not need to be on a
Manhattan grid. Initial coordinates must be on internal magic grid
points (that is, must be integer). However, half-grid units can be
generated with the **configure** option (see below).

**rectangle** *name style llx lly urx ury*  
Create a new box element, with lower left corner at coordinate *llx
lly* and upper right corner at coordinate *urx ury*.

**text** *name style cx cy label\_text*  
Create a new text label at coordinate position *cx cy* with text
string "*label\_text*".

For an explanation of the *style* parameter, see the **configure**
option, below.

**delete** *name*  
Delete an existing element by name.

**configure** *name* *config\_option*  
Configure or query an existing element named *name*.
*config\_option* may be one of the following:

**text** \[*new\_label\_text*\]  

**style** \[**add**|**remove** \[*style\_type*\]\]  
With no arguments, return the list of styles used to draw the
element. With option **add** or **remove**, add or remove,
respectively, a style from the list of styles for an element. Styles
are the same as styles for tile types in magic, and are defined in
the "dstyle" file in the **magic** install directory. The "dstyle"
file declares a "long name" for each style type. This "long name" is
what is expected for parameter *style\_type*. The most useful values
are the colors defined in the "dstyle" file, such as **black**,
**white**, **red**, etc.

Like tile types, elements may be drawn in multiple styles. So,
styles are maintained as a list and the **element configure style**
option takes the keyword **add** or **remove** to add or remove
specific styles from the list. Removing the last remaining style for
an element is prohibited. Changing styles requires first adding the
new style type, then removing the original.

**position** \[*x y* \[*x2 y2*\]\]  
With no arguments, returns the position of the element. For text
elements, this is the label position (a single coordinate). For
lines, both endpoint coordinates are returned, and for rectangles,
the lower-left and upper-right coordinates are returned. With one or
two coordinate specified, the position of the element is changed.
For text, a single coordinate indicates the new position of the
text. For lines and rectangles, the two coordinates completely
describe the line or box.

**flags** *flag\_type*  
Add or change flags of an element. The specific flag indicated is
set. Valid flags are as follows. All elements have these flags:

> **temporary**  
> Indicates an element that is not saved to the database with a
> **save** or **writeall** command (the default flag).
>
> **persistent**  
> Indicates an element that is saved to the database with a **save**
> or **writeall** command, and can be recovered with a **load**
> command.

Text elements have the following additional flags:

> **small**, **medium**, **large**, **xlarge**  
> One of four text sizes.
>
> [*direction*](#direction)  
> Any valid *direction* specification in **magic** will be
> translated to a text justification; that is, the text will be
> printed relative to its position in the indicated direction.

Line elements have the following additional flags:

> **halfx**, **halfy**  
> Adjust the position of the line endpoints by one-half unit
> (postive, that is, right or up). This allows lines to be drawn on,
> for example, wire centerlines. There is no allowance for having
> only one endpoint on the half-integer grid.
>
> **exactx**, **exacty**  
> Set line endpoints on the exact coordinates of the line position
> (the default flag).
>
> **arrowleft**, **arrowbottom** **arrowtop**, **arrowright**  
> Add arrows to the line endpoints at the indicated end. Note that
> four possible positions are allowed, although only two will be
> relevant for any given line. Arrowheads are of fixed size and may
> not be visible at large zoom factors.
>
> **plainleft**, **plainbottom** **plaintop**, **plaintright**  
> Draw plain lines, with no arrowheads (the default flags).

Rectangle elements have no additional flags.

**names**  
Print names of all elements

**inbox**  
Print name of element in (or nearest) the box

**help**  
Print help information

### Summary:

The **element** command creates and manipulates general-purpose
"elements", which are lines, rectangles, and text that have no
inherent meaning to the database. They are positioned in units of the
layout and so scale and move with zooms and pans. They are intended to
be used for layout annotation, measurement rulers, user-defined
feedback, flylines, wire paths, and so forth.

### Implementation Notes:

**element** is implemented as a built-in **magic** command. The syntax
is complicated and is expected to be driven by Tcl scripts with
simpler syntax for specific purposes such as annotation or measurement
rulers.

## erase

------------------------------------------------------------------------

Erase paint from the layout inside the bounds of the cursor box.

------------------------------------------------------------------------

### Shortcuts:

Key macro **Control-D** implements the command "**erase $**", which
indicates to erase all paint and labels in the cursor box.  
Key **e** typed while the cursor is in a layer box in the GUI toolbar
implements the command "**erase** *layer*", passing the layer type in
the toolbar.  
Key Shift plus Mouse button 2 implements the command **erase cursor**
when using the "box tool" in a layout window.  

### Usage:

**erase** \[*layers*|**cursor**\]  


where *layers* is a comma-separated list of layer types to be
erased, or **\*** to indicate all paint but not labels, or **$** to
indicate both paint and labels.

### Summary:

The **erase** command erases paint inside the cursor box in the
current edit cell. Without arguments, everything inside the box is
erased. With argument *layers*, only the indicated layers are erased.

Note that some layer types, such as DRC paint, cannot be erased.
Feedback areas are not considered paint and should be erased using the
**feedback clear** command.

The option "**erase cursor**" picks the layers at the position of the
(X11) cursor and erases these from the area of the cursor box.

Note that when applied to contact types, "**erase**" will erase the
entire contact, including the top and bottom metal types comprising
the contact. To remove the contact cuts without affecting the
surrounding material, use the "**contact erase**" command.

### Implementation Notes:

**erase** is implemented as a built-in **magic** command.

### See Also:

[**paint**](#paint)  
[**contact**](#contact)  

## expand

------------------------------------------------------------------------

Expand everything inside or touching the cursor box, or toggle
expanded/unexpanded cells in the current selection.

------------------------------------------------------------------------

### Usage:

**expand** \[**toggle**\]  


### Shortcuts:

Key macro **x** implements the command **expand**.  
Key macro *Control-***X** implements the command **expand toggle**.

### Summary:

The **expand** command expands the view of subcells to display the
contents of the subcells. Without arguments, the **expand** command
expands all unexpanded subcells that touch or intersect the cursor box
in the layout window.

Option **expand toggle** operates on the current selection, not
relative to the cursor box, and will expand a selected cell that is
unexpanded, or unexpand a cell that is already expanded.

### Implementation Notes:

**expand** is implemented as a built-in **magic** command.

### See Also:

[**unexpand**](#unexpand)  

## ext, extract

------------------------------------------------------------------------

Circuit netlist extractor

------------------------------------------------------------------------

### Usage:

**extract** *option*  


where *option* may be one of the following:

**all**  
Extract the root cell and all its children. This bypasses the
incremental extraction and ensures that a new .ext file is written
for every cell definition.

**cell** *name*  
Extract the indicated cell into file *name*

**do**|**no** \[*option*\]  
Enable or disable an extractor option, where *option* may be one of
the following:

> **capacitance**  
>
> **resistance**  
>
> **coupling**  
>
> **length**  
>
> **adjust**  
>
> **all**  

**length** \[*option*\]  
Control pathlength extraction information, where *option* may be one
of the following:

> **driver** *termname*  
>
> **receiver** *termname*  
>
> **clear**  

**help**  
Print help information

**parents**  
Extract the selected cell and all its parents

**showparents**  
List the cell and all parents of selected cell. Note that this is
not really an extract option and is superceded by the **cellname**
command.

\[**list**|**listall**\] **style** \[*stylename*\]  
Set the current extraction style to *stylename*. Without arguments,
print the current extraction style. With keyword **list**, return
the current extraction style as a Tcl result. With keyword
**listall**, return all valid extraction styles for the technology
as a Tcl list.

**unique** \[*\#*\]  
Generate unique names when different nodes have the same name

**warn** \[\[**no**\] *option*\]  
Enable/disable reporting of non-fatal errors, where *option* may be
one of the following:

> **fets**  
>
> **labels**  
>
> **dup**  
>
> **all**  

### Summary:

With no options given, the **extract** command incrementally extracts
the root cell and all its children into separate .ext files. With
options, the effect is as described in the Usage section above.

### Implementation Notes:

**extract** is implemented as a built-in **magic** command.

**ext** is an alias for command **extract** (allowed abbreviation
where the usage would otherwise be ambiguous).

### See Also:

[**extresist**](#extresist)  
[**ext2spice**](#ext2spice)  
[**ext2sim**](#ext2sim)  

## ext2sim, exttosim

------------------------------------------------------------------------

Convert extracted file(s) to a ".sim" format file.

------------------------------------------------------------------------

### Usage:

**ext2sim** \[*option*\]  


where *option* is one of the following:

\[**run**\] \[*runtime\_options*\]  
Run exttosim on current cell, with command-line options (see
Summary, below).

**alias on**|**off**  
Enable/disable alias (.al) file. This file contains all of the node
aliases (different node names that correspond to the same node). If
"off", the statements are output directly to the .sim file. If "on",
the statements are moved to the ".al" file.

**labels on**|**off**  
Enable/disable labels (.nodes) file. The labels file is used by the
extresist command.

**default**  
Reset to default values

**format MIT**|**SU**|**LBL**  
Set output format

**rthresh** \[*value*\]  
Set resistance threshold value. Lumped resistances below this value
will not be written to the output. The value is in ohms, or may be
the keyword **infinite** to prohibit writing any lumped resistances
to the output.

**cthresh** \[*value*\]  
Set capacitance threshold value. The value is in femtofarads, or may
be the keyword **infinite** to prohibit writing any parasitic
capacitances to the output.

**merge** \[*merge\_option*\]  
Merge parallel devices/transistors. The valid merge options are:

> **conservative**  
> Merge transistors and capacitors having the same device type and
> node connections and having the same width and length. Widths are
> summed in the final output for transistors. Capacitor values are
> summed in the final output.
>
> **aggressive**  
> Merge transistors having the same node connections and having the
> same length. Widths are summed in the final output. Merge any
> capacitors having the same device type and node connections.
> Capacitance is summed in the final output.
>
> **none**  
> Do not merge any devices.

**extresist on**|**off**  
Incorporate output from the command **extresist** into the final
.sim file.

**help**  
Print help information

### Summary:

Without options, or with the option **run**, the **ext2sim** command
converts the hierarchical extracted netlist information produced by
the **extract** command in a series of .ext files into a flattened
representation in the .sim format, used for switch-level simulation.

*runtime\_options* may be passed on the command line, and represent
the original command-line options passed to the standalone version of
ext2sim. A number of the original command-line options have been
deprecated in the Tcl-based version, and some are duplicated by other
**ext2sim** options. Valid *runtime\_options* are:

**-B**  
Don't output transistor or node attributes in the .sim file. This
option will also disable the output of information such as the area
and perimeter of source and drain diffusion and the FET substrate.

**-F**  
Don't output nodes that aren't connected to devices (floating
nodes).

**-t***char*  
Trim characters from node names when writing the output file. *char*
should be either "**\#**" or "**!**". The option may be used twice
if both characters require trimming.

**-y** *num*  
Select the precision for outputting capacitors. The default is 1
which means that the capacitors will be printed to a precision of
0.1 fF.

**-J** **hier**|**flat**  
Select the source/drain area and perimeter extraction algorithm. If
**hier** is selected then the areas and perimeters are extracted
only within each subcell. For each device in a subcell the area and
perimeter of its source and drain within this subcell are output. If
two or more devices share a source/drain node then the total area
and perimeter will be output in only one of them and the other will
have 0. If **flat** is selected the same rules apply, only the scope
of search for area and perimeter is the whole netlist. In general,
**flat** (which is the default) will give accurate results (it will
take into account shared sources/drains).

With options, the command sets various parameters affecting the output
format and content.

### Implementation Notes:

**ext2sim** is implemented as a separate loadable Tcl package, but one
which depends on the presence of the standard "tclmagic" package.
**magic** is set up with a placeholder command for **ext2sim**, and
will automatically load the Tcl package when this command is invoked.

**exttosim** is an alias for **ext2sim**, to satisfy the grammatically
anal retentive. **ext2sim** is also implemented as a script to be run
from the shell command line, where it executes magic in batch mode
(i.e., using the **-dnull** option) and runs the ext2sim command
automatically. With this usage, the syntax is:

**ext2sim** \[ *magic\_options* **--** \] *ext2sim\_runtime\_options
ext\_file*

The double-dash separates command options passed to magic on startup
(such as "**-T** *technology*" to specify the technology) from those
runtime options (see above) passed to the **ext2sim** command.

### See Also:

[**extract**](#extract)  
[**extresist**](#extresist)  
[**ext2spice**](#ext2spice)  
[**irsim**](#irsim)  

## ext2spice, exttospice

------------------------------------------------------------------------

Convert extracted file(s) to a SPICE format file.

------------------------------------------------------------------------

### Usage:

**ext2spice** \[*option*\] \[*cellname*\]  


where *option* is one of the following:

\[**run**\] \[*runtime\_options*\]  
Run **ext2spice** on current cell, with command-line options (see
Summary, below).

**default**  
Reset to default values

**format hspice**|**spice2**|**spice3**|**ngspice**  
Set output format. **spice3** is the default, for compatibility with
**tclspice**. This is a change from previous versions of magic,
where the default was **hspice**.

**rthresh** \[*value*\]  
Set resistance threshold value. Lumped resistances below this value
will not be written to the output. The value is in ohms, or may be
the keyword **infinite** to prohibit writing any lumped resistances
to the output.

**cthresh** \[*value*\]  
Set capacitance threshold value. The value is in femtofarads, or may
be the keyword **infinite** to prohibit writing any parasitic
capacitances to the output.

**merge** \[*merge\_option*\]  
Merge parallel devices/transistors. The valid merge options are:

> **conservative**  
> Merge transistors and capacitors having the same device type and
> node connections and having the same width and length. Device
> multipliers ("M=") are output for each set of merged devices.
>
> **aggressive**  
> Merge transistors having the same node connections and having the
> same length. Widths are summed in the final output. Merge any
> capacitors having the same device type and node connections.
> Capacitance is summed in the final output.
>
> **none**  
> Do not merge any devices.

**extresist on**|**off**  
Incorporate output from the command **extresist** into the final
SPICE file.

**resistor tee** \[**on**|**off**\]  
Model resistor capacitance as a T-network. Each resistor device is
split into two, with all substrate and overlap capacitance placed on
the node between the two half-length devices. Without this option,
resistor devices lose all parasitic capacitance information, and
**ext2spice** may produce warnings about unknown nodes. However, use
of this option may conflict with LVS (layout-vs.-schematic), when
only one resistor is expected per drawn device.

**subcircuit** \[**on**|**off**\]  
When set to **on** (the default), and if the cell selected for SPICE
output has defined ports on the top level, then the cell becomes a
subcircuit definition in the output, and the output has no top-level
calls to any devices. This format is appropriate for including in a
testbench netlist, for example. If the top-level cell does not have
defined ports, then there is no way for magic to determine what the
ports might be, or what order they may be in, making it impossible
to generate a consistent subcircuit, so in the absence of ports,
this option has no function. Ports are defined by the use of the
**port** method for labeling input and output ports. When option
**subcircuit** is set to **off**, the top-level circuit will be the
top level of the netlist, and it will have no associated subcircuit
definition.

**subcircuit top** \[**on**|**off**\]  
This variant of the **subcircuit** option controls whether or not
ext2spice generates a .subckt wrapper around the top-level circuit.
If the top-level circuit does not have defined ports, then no
.subckt wrapper will ever be generated, because ext2spice will not
be able to know which nets are the ports.

**subcircuit descend** \[**on**|**off**\]  
When set to **off**, the **subcircuit descend** option will not
descend into any subcells below the top level, writing only the
top-level circuit to the output. The default is **on**. This option
can be useful for writing out digital circuits made from standard
cells, since the digital subcircuits can usually be included from a
vendor library.

**scale** \[**on**|**off**\]  
When set to **on**, the scale value is set by the SPICE "**.scale**"
card, recognized by some SPICE parsers. All device lengths, widths,
and areas are then given in integer units (internal database units).
When set to **off**, all device widths, lengths, and areas are given
in unscaled, physical dimensions.

**short** \[**voltage**|**resistor**|**none**\]  
Determines behavior with respect to ports with different names
connected to the same net. SPICE does not have a universal method
for describing a net with more than one name. A common way of
handling this is by separating differently-named parts of a net with
a zero-ohm ideal resistor or a zero-volt DC source. "**ext2spice
short**" uses one of these methods to preserve duplicate port names.
"**ext2spice short resistor**" uses the zero-ohm resistor method,
which "**ext2spice short voltage**" uses the zero-volt source
method. "**ext2spice short none**" reverts to the default behavior,
which is to remove all port names except for one from the netlist.

**hierarchy** \[**on**|**off**\]  
When set to **on**, magic will extract a hierarchical representation
of the circuit, in which the cell hierarchy of the layout is
represented in SPICE by "**.subckt**" macros. "ext2spice hierarchy"
does not require that subcircuits have port labels. Each subcircuit
will be analyzed for port connections, and port connections will be
consistent in the SPICE output between the subcircuit definition
(".subckt") and instantiated calls ("X") to that subcircuit.

**blackbox** \[**on**|**off**\]  
When set to "on", views marked as abstract will be output as
subcircuit calls ("X") but there will be no associated subcircuit
definition output. A circuit is considered "abstract" if at the time
of extraction it has a property named "LEFview". A cell will
automatically be given this property if it is read from a LEF input
file. It may also be given this property using the "**property**"
command. In order for the blackbox view to be meaningful, the
subcell must declare ports (see the "port" command).

**renumber** \[**on**|**off**\]  
When set to **on**, subcircuit calls (see above; only used for
certain options such as "subcircuit", "hierarchy", or with extracted
device types "subcircuit" or "rsubcircuit") are numbered
sequentially "X1", "X2", etc., as encountered by the extractor. When
set to **off**, subcircuit calls (when used with options
"subcircuit" or "hierarchy", but not applying to low-level extracted
subcircuit devices) will be rendered in the SPICE output file as "X"
followed by the ID (name) of the cell instance.

**global** \[**on**|**off**\]  
When set to **on** or default, unconnected global nets of the same
name in subcells are merged in the output. When set to **off**, such
nets are left unconnected.

*cellname*  
Name of the cell to generate output for. This item is optional; if
not specified, then ext2spice generates output for the current edit
cell.

**lvs**  
Apply settings appropriate for running LVS (layout vs. schematic).
These settings are as follows:

-   hierarchy on
-   format ngspice
-   cthresh infinite
-   rthresh infinite
-   renumber off
-   scale off
-   blackbox on
-   subcircuit top auto
-   global off

This command applies the settings but does not generate output
(*i.e.*, does not run **ext2spice**), so that settings can be
overridden if necessary.  
(The **lvs** option was introduced in version 8.2.79).

**help**  
Print help information.

### Summary:

Without options, or with the option **run**, the **ext2spice** command
converts the hierarchical extracted netlist information produced by
the **extract** command in a series of .ext files into a flattened
representation in SPICE format, used for detailed analog simulation.

*runtime\_options* may be passed on the command line, and represent
the original command-line options passed to the standalone version of
ext2spice. A number of the original command-line options have been
deprecated in the Tcl-based version, and some are duplicated by other
**ext2spice** options. Valid *runtime\_options* are:

**-M**  
Aggressive merging of devices. If the lengths of FET devices
connected in parallel are equal, then add their widths together to
form a single device. Overrides any value specified by the
"ext2spice merge" command option.

**-m**  
Conservative merging of devices. If the lengths and widths of FET
devices connected in parallel are equal, then add their widths
together to form a single device. Overrides any value specified by
the "ext2spice merge" command option.

**-o** *filename*  
Save the output as file *filename* (*filename* must include any file
extension, as there is no standard extension for SPICE files).

**-j** *device***:***class* \[**/***subclass*\] **/***subsnode*  
Override values of resistance class, substrate resistance class, and
substrate node name for device type *device*. Resistance classes are
indexed by number and must match the definition in the technology
file's extract section.

**-f spice2**|**spice3**|**hspice**|**ngspice**  
Choose the output SPICE format for compatibility with different
versions of SPICE.

**-d**  
Distribute junction areas and perimeters. The Magic extractor
computes area and perimter values per *node*, not per *device*. For
devices that share a node, Magic cannot distinguish between the
devices (for parasitic calculations, it's not necessary to
distinguish between the devices). Normally, when generating device
output, Magic writes the lumped area and perimeter values along with
the first device attached to a node, and sets the area and perimeter
values for all remaining devices on that node to zero. The **-d**
option causes Magic to distribute the node area and perimeter evenly
among all devices attached to that node.

**-B**  
Don't output transistor or node attributes in the SPICE file. This
option will also disable the output of information such as the area
and perimeter of source and drain diffusion and the FET substrate.

**-F**  
Don't output nodes that aren't connected to devices (floating
nodes).

**-t***char*  
Trim characters from node names when writing the output file. *char*
should be either "**\#**" or "**!**". The option may be used twice
if both characters require trimming.

**-y** *num*  
Select the precision for outputting capacitors. The default is 1
which means that the capacitors will be printed to a precision of
0.1 fF.

**-J** **hier**|**flat**  
Select the source/drain area and perimeter extraction algorithm. If
**hier** is selected then the areas and perimeters are extracted
only within each subcell. For each device in a subcell the area and
perimeter of its source and drain within this subcell are output. If
two or more devices share a source/drain node then the total area
and perimeter will be output in only one of them and the other will
have 0. If **flat** is selected the same rules apply, only the scope
of search for area and perimeter is the whole netlist. In general,
**flat** (which is the default) will give accurate results (it will
take into account shared sources/drains).

With options, the command sets various parameters affecting the output
format and content.

### Implementation Notes:

**ext2spice** is implemented as a separate loadable Tcl package, but
one which depends on the presence of the standard "tclmagic" package.
**magic** is set up with a placeholder command for **ext2spice**, and
will automatically load the Tcl package when this command is invoked.

**exttospice** is an alias for **ext2spice**, to satisfy the
grammatically anal retentive. **ext2spice** is also implemented as a
script to be run from the shell command line, where it executes magic
in batch mode (i.e., using the **-dnull** option) and runs the
ext2spice command automatically. With this usage, the syntax is:

**ext2spice** \[ *magic\_options* **--** \]
*ext2spice\_runtime\_options ext\_file*

The double-dash separates command options passed to magic on startup
(such as "**-T** *technology*" to specify the technology) from those
runtime options (see above) passed to the **ext2spice** command.

### See Also:

[**extract**](#extract)  
[**ext2sim**](#ext2sim)  

## ext, extract

------------------------------------------------------------------------

Circuit netlist extractor

------------------------------------------------------------------------

### Usage:

**extract** *option*  


where *option* may be one of the following:

**all**  
Extract the root cell and all its children. This bypasses the
incremental extraction and ensures that a new .ext file is written
for every cell definition.

**cell** *name*  
Extract the currently selected cell into file *name*

**do**|**no** \[*option*\]  
Enable or disable an extractor option, where *option* may be one of
the following:

> **capacitance**  
> Extract local parasitic capacitance values to substrate
>
> **resistance**  
> Extract lumped resistance values. Note that this is *not* the same
> as full parasitic resistance. The values extracted are "lumped"
> resistance and indicate the value for which the delay through the
> net can be computed with R times C, where R is the lumped
> resistance and C is the parasitic capacitance. This is a very
> coarse approximation, as it assumes equal delay from the driver to
> any receiver. For full R-C extraction, see the **extresist**
> command. Lumped resistances have no meaning in SPICE netlists and
> will only be used when running **ext2sim** to generate a .sim
> netlist.
>
> **coupling**  
> Extract the parasitic coupling capacitance between nodes.
>
> **length**  
> Extract the length of the shortest path from a driver to a
> receiver, for computing more accurate parasitic resistances.
>
> **adjust**  
> Adjust all capacitances for overlap between a parent cell and
> child instance, or between instances in an array. Parasitic
> capacitance is removed to account for the amount of overlap. Note
> that this method can produce negative capacitors in the parent.
> When the netlist is flattened for simulation, the total of all
> capacitances in parent and child, or between array instances, is
> guaranteed to be strictly positive.
>
> **all**  
> Apply all standard options (does not include options "local",
> "labelcheck", or "aliases").
>
> **local**  
> Write all .ext files to the current working directory. If not
> specified, each .ext file will be placed in the same directory as
> the .mag file from which it is derived, unless the .mag file is in
> a directory which is not writable. In that case, the .ext file
> will also be written to the current working directory.
>
> **labelcheck**  
> Check for labels which have zero area and connect to a subcell on
> the edge; this case is rare but is computationally expensive to
> check for, so the feature is disabled by default.
>
> **aliases**  
> By default (starting with version 8.3.217), magic only extracts a
> single name for a net, unless the net connects to a port, in which
> case the port name is extracted as well. With the **aliases**
> option enabled, all names for a net are extracted; this can be
> useful for debugging but will usually just slow down processing by
> commands like "ext2spice" that use the .ext file contents, so it
> is disabled by default.

These options (except for "local") determine how much information is
written to the output file. By default, all options are selected.
Normally, the options in **ext2spice** or **ext2sim** are used to
select which information from the .ext file is used in the resulting
netlist. There is no need to restrict the information being
extracted. All options add relatively little overhead to the
extraction time. The output file size can be reduced by not
generating some extraction information.

**length** \[*option*\]  
Control pathlength extraction information, where *option* may be one
of the following:

> **driver** *termname*  
>
> **receiver** *termname*  
>
> **clear**  

**help**  
Print help information

**parents**  
Extract the selected cell and all its parents

**showparents**  
List the cell and all parents of selected cell. Note that this is
not really an extract option and is superceded by the **cellname**
command.

\[**list**|**listall**\] **style** \[*stylename*\]  
Set the current extraction style to *stylename*. Without arguments,
print the current extraction style. With keyword **list**, return
the current extraction style as a Tcl result. With keyword
**listall**, return all valid extraction styles for the technology
as a Tcl list.

**unique** \[*\#*\]  
Generate unique names when different nodes have the same name. When
option "*\#*" is present, only make unique names for labels tagged
by ending with the "**\#**" character.  
*Warning:* This operation immediately modifies the existing layout
in preparation for extraction. Label modifications are permanent,
and cannot be undone. All cells in the hierarchy may potentially be
modified.  

**unique** \[*option*\]  
(From Magic 8.1.24) With no option, generate unique names when
different nodes have the same name. *option* may be one of the
following:

> **all**  
> Equivalent to no option; all labels with the same name on
> different nets are given unique names.
>
> **\#**  
> Labels that are tagged by ending with the character "**\#**" are
> made unique for each instance on an electrically unique node.
>
> **noports**  
> Labels that are not ports are made unique when on different nets.
> Ports, however, are ignored. This option is useful for standard
> cells which may be hiding internal connectivity.
>
> **notopports**  
> This option behaves like **extract unique noports** on the topmost
> cell in the hierarchy, and otherwise behaves like **extract unique
> all** on all cells below the top (available from magic 8.3.205).

*Warning:* This operation immediately modifies the existing layout
in preparation for extraction. Label modifications are permanent,
and cannot be undone. All cells in the hierarchy may potentially be
modified.  

**warn** \[\[**no**\] *option*\]  
Enable/disable reporting of non-fatal errors, where *option* may be
one of the following:

> **fets**  
>
> **labels**  
>
> **dup**  
>
> **all**  

### Summary:

With no options given, the **extract** command incrementally extracts
the root cell and all its children into separate .ext files. With
options, the effect is as described in the Usage section above.

### Implementation Notes:

**extract** is implemented as a built-in **magic** command.

**ext** is an alias for command **extract** (allowed abbreviation
where the usage would otherwise be ambiguous).

### See Also:

[**extresist**](#extresist)  
[**ext2spice**](#ext2spice)  
[**ext2sim**](#ext2sim)  

## extresist

------------------------------------------------------------------------

Patch the extraction .ext files with detailed route resistance
information.

------------------------------------------------------------------------

### Usage:

**extresist** *option*  


where *option* may be one of the following:

**tolerance** *value*  
Set the ratio between resistor and transistor tolerance for
determining when to insert resistance into a network route.

**all**  
Extract all the nets.

**simplify** \[**on**|**off**\]  
Turn on/off simplification of resistor nets.

**extout** \[**on**|**off**\]  
Turn on/off writing of the .res.ext file.

**lumped** \[**on**|**off**\]  
Turn on/off writing of updated lumped resistances.

**silent** \[**on**|**off**\]  
Turn off/on printing of net statistics.

**skip** *mask*  
Don't extract types indicated in the comma-separated list *mask*

**ignore** \[*netname*|**none**\]  
Don't extract the net named *netname*. The list of ignored nets is
global, cumulative, and persistent; it will only be cleared when the
**extresist ignore none** command is issued (option available from
version 8.3.207).

**include** \[*netname*|**all**\]  
Extract the net named *netname*. When this option is called at least
once, the behavior of the extraction changes to extract only the
nets that have been specified by **extresist include** commands. The
list of included nets is global, cumulative, and persistent; it will
only be cleared when the **extresist include all** command is issued
(option available from version 8.3.213).

**box** *type*  
Extract the signal under the cursor box on layer *type*

**cell** *cellname*  
Extract the network for the cell named *cellname*

**geometry**  
Extract network geometry and present as a collection of line
elements on the layout.

**fasthenry** \[*freq*\]  
Extract subcircuit network geometry into a **fasthenry**-format .fh
file. If *freq* is specified, the file will be customized for
**fasthenry** analysis at the indicated frequency (in Hz).

**help**  
Print help information

### Summary:

The normal flow through layout extraction into a simulation file
treats routes as nonphysical entities, that is, with infinitesimal
impedence through the wires. Extraction for digital simulation using
**irsim** generates "lumped resistances", a single resistance per
network node that, along with the node capacitance to substrate,
provides an *RC* time constant to approximately model the delay from
point to point in the network node. The lumped resistance model is
inappropriate for analog (i.e., SPICE) simulation, and for digital
simulation, is a poor approximation for branching networks, where the
delay between endpoints is different for each pair of endpoints in the
network node.

The **extresist** command provides a method for generating a more
detailed model of resistance, in which long network routes and
branching routes are replaced with resistor devices and device
networks.

Using **extresist** is a multi-step process. It is first necessary to
run both **extract** and **ext2sim** to get the initial netlist (with
lumped, not detailed, resistances). After a .sim file has been
generated, the **extresist all** command may be run. The output is a
file .res.ext for each cell in the hierarchy. Finally, with the option
**extresist on** set, **ext2sim** or **ext2spice** will generate the
final, detailed simulation file.

More details on using **extresist** can be found in **magic** Tutorial
number 8.

### Implementation Notes:

**extresist** is implemented as a built-in command in **magic**.

### See Also:

[**extract**](#extract)  
[**ext2sim**](#ext2sim)  

## ext2sim, exttosim

------------------------------------------------------------------------

Convert extracted file(s) to a ".sim" format file.

------------------------------------------------------------------------

### Usage:

**ext2sim** \[*option*\]  


where *option* is one of the following:

\[**run**\] \[*runtime\_options*\]  
Run exttosim on current cell, with command-line options (see
Summary, below).

**alias on**|**off**  
Enable/disable alias (.al) file

**labels on**|**off**  
Enable/disable labels (.nodes) file

**default**  
Reset to default values

**format MIT**|**SU**|**LBL**  
Set output format

**rthresh** \[*value*\]  
Set resistance threshold value. Lumped resistances below this value
will not be written to the output. The value is in ohms, or may be
the keyword **infinite** to prohibit writing any lumped resistances
to the output.

**cthresh** \[*value*\]  
Set capacitance threshold value. The value is in femtofarads, or may
be the keyword **infinite** to prohibit writing any parasitic
capacitances to the output.

**merge** \[*merge\_option*\]  
Merge parallel devices/transistors. The valid merge options are:

> **conservative**  
> Merge transistors and capacitors having the same device type and
> node connections and having the same width and length. Widths are
> summed in the final output for transistors. Capacitor values are
> summed in the final output.
>
> **aggressive**  
> Merge transistors having the same node connections and having the
> same length. Widths are summed in the final output. Merge any
> capacitors having the same device type and node connections.
> Capacitance is summed in the final output.
>
> **none**  
> Do not merge any devices.

**extresist on**|**off**  
Incorporate output from the command **extresist** into the final
.sim file.

**help**  
Print help information

### Summary:

Without options, or with the option **run**, the **ext2sim** command
converts the hierarchical extracted netlist information produced by
the **extract** command in a series of .ext files into a flattened
representation in the .sim format, used for switch-level simulation.

*runtime\_options* may be passed on the command line, and represent
the original command-line options passed to the standalone version of
ext2sim. A number of the original command-line options have been
deprecated in the Tcl-based version, and some are duplicated by other
**ext2sim** options. Valid *runtime\_options* are:

**-B**  
Don't output transistor or node attributes in the .sim file. This
option will also disable the output of information such as the area
and perimeter of source and drain diffusion and the FET substrate.

**-F**  
Don't output nodes that aren't connected to devices (floating
nodes).

**-t***char*  
Trim characters from node names when writing the output file. *char*
should be either "**\#**" or "**!**". The option may be used twice
if both characters require trimming.

**-y** *num*  
Select the precision for outputting capacitors. The default is 1
which means that the capacitors will be printed to a precision of
0.1 fF.

**-J** **hier**|**flat**  
Select the source/drain area and perimeter extraction algorithm. If
**hier** is selected then the areas and perimeters are extracted
only within each subcell. For each device in a subcell the area and
perimeter of its source and drain within this subcell are output. If
two or more devices share a source/drain node then the total area
and perimeter will be output in only one of them and the other will
have 0. If **flat** is selected the same rules apply, only the scope
of search for area and perimeter is the whole netlist. In general,
**flat** (which is the default) will give accurate results (it will
take into account shared sources/drains).

With options, the command sets various parameters affecting the output
format and content.

### Implementation Notes:

**ext2sim** is implemented as a separate loadable Tcl package, but one
which depends on the presence of the standard "tclmagic" package.
**magic** is set up with a placeholder command for **ext2sim**, and
will automatically load the Tcl package when this command is invoked.

**exttosim** is an alias for **ext2sim**, to satisfy the grammatically
anal retentive.

### See Also:

[**extract**](#extract)  
[**extresist**](#extresist)  
[**ext2spice**](#ext2spice)  
[**irsim**](#irsim)  

## ext2spice, exttospice

------------------------------------------------------------------------

Convert extracted file(s) to a SPICE format file.

------------------------------------------------------------------------

### Usage:

**ext2spice** \[*option*\]  


where *option* is one of the following:

\[**run**\] \[*runtime\_options*\]  
Run **ext2spice** on current cell, with command-line options (see
Summary, below).

**default**  
Reset to default values

**format hspice**|**spice2**|**spice3**  
Set output format. **spice3** is the default, for compatibility with
**tclspice**. This is a change from previous versions of magic,
where the default was **hspice**.

**rthresh** \[*value*\]  
Set resistance threshold value. Lumped resistances below this value
will not be written to the output. The value is in ohms, or may be
the keyword **infinite** to prohibit writing any lumped resistances
to the output.

**cthresh** \[*value*\]  
Set capacitance threshold value. The value is in femtofarads, or may
be the keyword **infinite** to prohibit writing any parasitic
capacitances to the output.

**merge** \[*merge\_option*\]  
Merge parallel devices/transistors. The valid merge options are:

> **conservative**  
> Merge transistors and capacitors having the same device type and
> node connections and having the same width and length. Widths are
> summed in the final output for transistors. Capacitor values are
> summed in the final output.
>
> **aggressive**  
> Merge transistors having the same node connections and having the
> same length. Widths are summed in the final output. Merge any
> capacitors having the same device type and node connections.
> Capacitance is summed in the final output.
>
> **none**  
> Do not merge any devices.

**extresist on**|**off**  
Incorporate output from the command **extresist** into the final
SPICE file.

**resistor tee** \[**on**|**off**\]  
Model resistor capacitance as a T-network. Each resistor device is
split into two, with all substrate and overlap capacitance placed on
the node between the two half-length devices. Without this option,
resistor devices lose all parasitic capacitance information, and
**ext2spice** may produce warnings about unknown nodes. However, use
of this option may conflict with LVS (layout-vs.-schematic), when
only one resistor is expected per drawn device.

**subcircuits** \[**on**|**off**\]  
When set to **on** (the default), standard cells become subcircuit
calls ("X") in the SPICE output. The contents of the standard cells
are not output, and it is assumed that a pre-characterized SPICE
deck exists modeling the behavior of each standard cell definition.
Standard cells are defined by the use of the **port** method for
labeling input and output ports. When set to **off**, ports are
ignored, and the entire circuit hierarchy is flattened down to the
device level.

**help**  
Print help information.

### Summary:

Without options, or with the option **run**, the **ext2spice** command
converts the hierarchical extracted netlist information produced by
the **extract** command in a series of .ext files into a flattened
representation in SPICE format, used for detailed analog simulation.

*runtime\_options* may be passed on the command line, and represent
the original command-line options passed to the standalone version of
ext2spice. A number of the original command-line options have been
deprecated in the Tcl-based version, and some are duplicated by other
**ext2spice** options. Valid *runtime\_options* are:

**-B**  
Don't output transistor or node attributes in the SPICE file. This
option will also disable the output of information such as the area
and perimeter of source and drain diffusion and the FET substrate.

**-F**  
Don't output nodes that aren't connected to devices (floating
nodes).

**-t***char*  
Trim characters from node names when writing the output file. *char*
should be either "**\#**" or "**!**". The option may be used twice
if both characters require trimming.

**-y** *num*  
Select the precision for outputting capacitors. The default is 1
which means that the capacitors will be printed to a precision of
0.1 fF.

**-J** **hier**|**flat**  
Select the source/drain area and perimeter extraction algorithm. If
**hier** is selected then the areas and perimeters are extracted
only within each subcell. For each device in a subcell the area and
perimeter of its source and drain within this subcell are output. If
two or more devices share a source/drain node then the total area
and perimeter will be output in only one of them and the other will
have 0. If **flat** is selected the same rules apply, only the scope
of search for area and perimeter is the whole netlist. In general,
**flat** (which is the default) will give accurate results (it will
take into account shared sources/drains).

With options, the command sets various parameters affecting the output
format and content.

### Implementation Notes:

**ext2spice** is implemented as a separate loadable Tcl package, but
one which depends on the presence of the standard "tclmagic" package.
**magic** is set up with a placeholder command for **ext2spice**, and
will automatically load the Tcl package when this command is invoked.

**exttospice** is an alias for **ext2spice**, to satisfy the
grammatically anal retentive.

### See Also:

[**extract**](#extract)  
[**ext2sim**](#ext2sim)  

## feedback

------------------------------------------------------------------------

Query or manipulate feedback entry areas.

------------------------------------------------------------------------

### Usage:

**feedback** *option*  


where *option* may be one of the following:

**add** *text* \[*style*\] \[*x1 y1 ...*\]  
Create a new feedback area. If positions *x1 y1 ...* are not
specified, then the feedback area created corresponds to the area of
the cursor box. The feedback entry will be associated with the text
*text*, which will be reported on execution of a **feedback why**
query. The feedback area will be drawn in style *style*, which may
be one of the following:

-   **dotted**
-   **medium**
-   **outline**
-   **pale**
-   **solid**

From magic version 7.3.110, *any* style from the ".dstyle" file may
be specified (e.g., "yellow1"). If points *x1 y1 ...* are specified,
then they represent a polygonal area for the feedback entry. This
area may be a point, line, or polygon, and may be specified in
internal units or metric units. If the feedback area is a point,
line, or degenerate polygon (polygon with zero internal area), then
the *style* must be an outlined style; otherwise, the style is
changed to style **outline** so that the feedback area is ensured to
be visible.

**clear** \[*substring*\]  
Without the argument *substring*, clears all feedback info. When
*substring* is specified, only feedback entries containing the text
*substring* will be removed. For example, if "cif see CMF" is
followed by "cif see CCC", the contact cuts will not be seen due to
being overlapped by the feedback for metal1. However, if this is
followed by "feedback clear CMF", the feedback area for metal1 will
be removed, leaving the contact cuts visible.

**count**  
Count the number of feedback entries

**find** \[*nth*\]  
Put the cursor box over next (or *nth*) entry

**help**  
Print help information

**save** *file*  
Save feedback area information into file *file*

**why**  
Print text associated with all feedback areas under the cursor box.

### Summary:

The **feedback** command queries or manipulates feedback areas, which
are areas drawn on top of the layout and may be used for annotations
and markers. Internally, **magic** uses feedback areas to report
CIF/GDS layers (**cif see** command), and errors generated by the
**extract** command. CIF/GDS feedback is placed on the output (usually
centimicron) grid, which cannot be done with the **feedback add**
command directly from the command-line.

Feedback information and areas are not saved in the layout file.

### Implementation Notes:

**feedback** is implemented as a built-in **magic** command.

### Bugs:

Small feedback areas were previously drawn solid to prevent them from
disappearing entirely; however, this created bizarre results in
CIF/GDS feedback when several narrow feedback areas are tiled
together, so it was removed. This leaves the possibility that feedback
areas smaller than the spacing between feedback crosshatch lines might
not be drawn; an inconvenience, but not a serious problem.

There should be a mechanism for removing only the feedback entries
under the cursor box, or the current feedback entry.

## fill

------------------------------------------------------------------------

Fill layers from one side of box to other.

------------------------------------------------------------------------

### Usage:

**fill** *direction* \[*layers*\]  


where *direction* is any valid Manhattan [direction](#direction)
in **magic**, and *layers* is an optional comma-separated list of
layers to restrict the operation of the **fill** command.

### Summary:

The **fill** command extends paint from one side of the cursor box to
the other. It is most often used to fill gaps in wire routes or fill
paint between subcells. The algorithm is to select all paint that
touches or crosses the cursor box on the side opposite the indicated
*direction*, and extend this paint in the indicated *direction* to the
other side of the cursor box. Paint that is in the cursor box but does
not touch the side of entry is not changed.

### Implementation Notes:

**fill** is implemented as a built-in command in **magic**.

### See Also:

[**corner**](#corner)  

## findbox

------------------------------------------------------------------------

Center the window on the box and optionally zoom in.

------------------------------------------------------------------------

### Shortcuts:

Key macro **B** implements the command **findbox**.  
Key macro *Control-***Z** implements the command **findbox zoom**.

### Usage:

**findbox** \[**zoom**\]  


### Summary:

The **findbox** command centers the window on the cursor box. This is
particularly useful in conjunction with other commands such as **drc
find** or **feedback find** that may move the box to an unknown
off-screen location. With the option **zoom**, the window view will be
centered on the cursor box and additionally scaled so that the cursor
box fills the window.

### Implementation Notes:

**findbox** is implemented as a built-in command in **magic**.

## findlabel

------------------------------------------------------------------------

Set the cursor box to the location of the indicated label

------------------------------------------------------------------------

### Usage:

**findlabel** \[**-glob**\] *label* \[*occur*\]  


where *label* is the name of an existing label in magic, and
optional argument *occur* is an integer.

### Summary:

The **findlabel** command can be used to center the cursor box on a
specific named label in the layout.

The **-glob** option causes **findlabel** to find all labels
containing the text pattern of *label*. This is the way the
**findlabel** command worked in versions of **magic** prior to 7.2.

The optional argument *occur* will center the cursor box on the *N*th
instance of the label, where *N*=*occur* (option introduced in version
8.3.86). If *occur* is greater than the number of labels in the edit
cell, then the result is the same as for a label that is not found.

### Implementation Notes:

**findlabel** is implemented as a built-in command in **magic**.

## flatten

------------------------------------------------------------------------

Flatten edit cell into the indicated destination cell.

------------------------------------------------------------------------

### Usage:

**flatten** \[*option*\] *cellname*  


where *cellname* is the name of a cell definition to be created, and
into which the flattened geometry will be placed. *option* may be
one of **-nolabels**, **-nosubcircuits**, or **-noports**,
**-novendor**, **-dotoplabels**, **-doproperty**, and **-dobox**.

### Summary:

The **flatten** command creates a new cell with the indicated name,
then flattens the hierarchy of the current edit cell and copies the
result into the new cell.

The options allow selective flattening, as follows:

**-nolabels**  
Prevents magic from copying labels into the flattened cell. Otherwise,
magic flattens labels by prepending the cell hierarchy to each label
as it copies it into the flat cell.

**-nosubcircuits**  
Prevents magic from flattening cells declared to be subcircuits (by
the presence of ports in the cell). These cells are retained as
subcells in the flattened version.

**-noports**  
Removes port information from labels when flattening, so that the
flattened view will have only labels and not ports.

**-novendor**  
Prevents magic from flattening cells that are vendor cells, that is,
cells that are generated by reading GDS using the **gds readonly**
option, or which have the appropriate property values set.

**-dotoplabels**  
This option tells magic to preserve in the flattened view only the
labels that are in the top level cell. Labels in subcells will be
ignored.

**-doproperty**  
This option will only flatten subcells which are marked with the
property string "**flatten**". This is useful for flattening an entire
set of cells; for example, flattening subcells with routing before
creating a DEF file of a layout.

**-dobox**  
When this option is specified, magic flattens only the area of the
circuit that is inside the boundary of the cursor box.

**-doinplace**  
When this option is specified, *cellname* must be the name of a cell
*use* (instance), not a cell *definition*. The cell use *cellname* is
assumed to exist in the current edit cell. The cell use will be
removed from the edit cell and replaced with its flattened contents.

Note that *cellname* is a top-level cell but is not displayed or saved
subsequent to the **flatten** command. The usual procedure is to
follow the command "**flatten** *cellname*" with "**load**
*cellname*", to view the new flattened layout.

The target cell *cellname* must not already exist in the database
except when using the **-dobox** option. With **-dobox**, using the
same target *cellname* allows a layout to be flattened in pieces.

### Implementation Notes:

**flatten** is implemented as a built-in command in **magic**.

## flush

------------------------------------------------------------------------

Forget changes to the edit cell (or to the indicated cell) since the
last saved version.

------------------------------------------------------------------------

### Usage:

**flush** \[*cellname*\] \[**-dereference**\]  


where *cellname* is the name of a cell definition to be flushed.

### Summary:

The **flush** command reverts a cell definition to the last version
saved to disk, forgetting all changes made in the interim. Without
arguments, the current edit cell is flushed. Otherwise, the named cell
is flushed.

The effects of the **flush** command are irrevocable; the command
cannot be undone with an **undo** command.

With the **-dereference** option, any file path that has been
associated with the cell is discarded, and the cell is reloaded from
the first location found in the search path. With search path
manipulations, this can be used, for example, to switch between
abstract and full views of a cell.

### Implementation Notes:

**flush** is implemented as a built-in command in **magic**. However,
it conflicts with the Tcl **flush** command that flushes an output
pipe. Special processing determines which use is intended.

### See Also:

[**path**](#path)  

## garoute

------------------------------------------------------------------------

Gate-array router

------------------------------------------------------------------------

### Usage:

**garoute** *option*  


where *option* may be one of the following:

**channel** *xl yl xh yh* \[*type*\]  
Define a channel, with indicated coordinates.

**channel** \[*type*\]  
Define a channel

**generate** **h**|**h** \[*file*\]  
Generate channel definition for a horizontal (**h**) or vertical
(**v**) routing channel.

**help**  
Print help information

**nowarn**  
Only warn if all locations of a terminal are unreachable.

**route** \[*netlist*\]  
Route the current cell

**reset**  
Clear all channel definitions

**warn**  
Leave feedback for each location of a terminal that is unreachable.

### Summary:

The **garoute** command controls the gate-array router. There is
currently practically no documentation for the gate-array router. This
section shall be expanded.

### Implementation Notes:

**garoute** is implemented as a built-in command in **magic**.

### See Also:

[**channel**](#channel)  

## gds, calma

------------------------------------------------------------------------

Read GDSII input or generate GDSII output.

------------------------------------------------------------------------

### Usage:

**gds** \[*option*\]  

**calma** \[*option*\]  


where *option* is one of the following:  
Primary options:

**help**  
Print usage information

**read** *file*  
Read GDSII format from file *file* into the edit cell. If *file*
does not have a file extension, then **magic** searches for a file
named *file*, *file*.gds, *file*.gds2, or *file*.strm.

**warning** \[*option*\]  
Set warning information level. "*option*" may be one of the
following:

**default**  
The default setting is equivalent to all the other options
(**align**, **limit**, **redirect**, and **none**) being disabled.

**align**  
Generate warnings during a "**cif see**" command if the alignment of
geometry is on fractional lambda. Normally, magic allows contacts to
be drawn at half-lambda positions. If this violates DRC requirements
for the minimum output grid, this warning setting can be used to
detect such violations.

**limit**  
Limit warnings to the first 100 warnings or errors only.

**redirect** \[*file*\]  
Redirect all warnings to an output file named *file*. If *file* is
not given, then redirection is disabled.

**none**  
Do not produce any warning messages on GDS input.

**write** *file*  
Output GDSII format to "*file*" for the window's root cell.

Options for **gds read**:

**datestamp** \[**yes**|**no**|*value*\]  
When reading a GDS file, the resulting layout views in magic will be
timestamped according to the declared datestamp action. If **yes**
(the default), then the creation date timestamp from the GDS file is
transferred to the layout cell. If **no**, then the datestamp is set
to zero and will be created when the cell is saved to disk. If
*value*, then the specified value (in UNIX format of seconds since
the epoch) will be used for the layout timestamp.

**drccheck** \[**yes**|**no**\]  
If set to **no**, then do not mark cells read from GDS as requiring
DRC checks (default **yes**).

**flatglob** \[**none**|*string*\]  
Flatten cells by name pattern on input. This is the more exacting
version of **flatten**, as it allows specific cells to be flattened.
Each call with an argument *string* adds *string* to the list of
name patterns to be checked. A call with the option **none** will
remove all patterns. A call with no options will return the list of
string patterns that will be applied to inputs. The strings may use
standard shell-type glob patterns, with **\*** for any length string
match, **?** for any single character match, **\\** for special
characters, and **\[\]** for matching character sets or ranges
(introduced in version 8.3.102).

**flatten** \[**yes**|**no**|*number*\]  
Flatten simple cells (e.g., contacts) on input. This helps magic to
use its contact-area representation of contacts, and can also avoid
situations where contacts are lost or translated to "generic" types
because the arrayed part of the contacts is missing one or more
residue layers. The default number of shapes in an input to be
considered "simple" is 10, but this can be set with the *number*
argument. A *number* of zero implies **flatten no**, and a non-zero
*number* implies **flatten yes**. Otherwise, the use of **yes** and
**no** toggles the flattening behavior without affecting any value
previously set by **flatten** *number*.

**maskhints** \[**yes**|**no**|*layers*\]  
When set to **yes**, then after reading each cell definition from
the GDS file, magic will re-generate the GDS output data from its
internal representation of the cell. Where the output data does not
match the input data, and where the technology file defines mask
hints in the **cifoutput** section for a GDS layer, magic will
automatically generate the mask hint property for the cell such that
writing GDS of the cell will produce exactly the same mask data as
was in the original GDS file. Alternatively to specifying "**yes**",
a comma-separated list *layers* of GDS layers to create mask hints
for can be specified (default **no**).

**noduplicates** \[**yes**|**no**\]  
When reading a GDS file, this option forces magic to ignore cell
definitions in the GDS file that are already present in the database
(that is, for which a cell of the same name already exists). This
can be used, for example, to pre-load an abstract view of a cell
before reading a GDS file containing that cell. This option should
be used with extreme caution, since there is no check as to whether
the existing view is compatible with the one in the GDS file.

**ordering** \[**yes**|**no**\]  
Forces post-ordering of subcells read from a GDS file; that is, if a
cell use is encountered before it is defined, magic will read
through the remainder of the file until it finds the definition,
read it, and then return to the original file position to continue
reading. This option is always enabled when using **gds flatten**.
Otherwise, the default behavior is **ordering no** to avoid lengthy
searches through the GDS stream file.

**polygon subcells** \[**yes**|**no**\]  
Put non-Manhattan polygons into subcells. Default is "no". Normally
this option is not needed. However, input layout that defines a
number of angled wires, particularly those that are closely spaced,
can cause **magic** to generate literally millions of internal
tiles. This tends to be true in particular for corner cells in
padframes for deep submicron feature sizes, where the angled corners
are required to meet the DRC specification. When set to "yes", each
polygon encountered in the GDS input is placed in its own
uniquely-named subcell. This prevents interations with other
polygons on the same plane and so reduces tile splitting.

**readonly** \[**yes**|**no**\]  
Set cell as "read-only". This has the effect of marking each cell
definition (using the **property** method) with the start and end
positions of the cell definition in the input file. In subsequent
output, the cell definition will be transferred verbatim from the
input to the output file. This is useful for 3rd-party standard
cells or pad cells where the original GDS is trusted and it is
desirable to bypass the boolean operators of **magic**'s GDS reader
and writer to prevent the layout from being altered. Note that
"read-only" layout can be written to a .mag file, but the contents
of this file are representational only. It can be useful to keep a
simplified respresentation in the case of pad cells or digital
standard cells, for example, by reading them using a GDS input style
that defines only metal layers.

**rescale** \[**yes**|**no**\]  
Allow or disallow internal grid subdivision while reading GDS input.
Default is "yes". Normally, one wants to allow rescaling to ensure
that the GDS is displayed exactly as it is in the input file.
Occasionally, however, the GDS input is on a very fine scale, such
as nanometers, and it is preferable to snap the input to lambda
boundaries rather than to subsplit the internal grid to such a fine
value. The "**cif limit**" function may also be used to limit grid
subdivision to a minimum value.

**unique** \[**yes**|**no**\]  
When reading a GDS file, this option forces magic to rename cell
definitions in the database when a cell of the same name is
encountered in the GDS file. The default behavior is to overwrite
the cell with the new definition. The existing cell is renamed by
adding a suffix with an underscore and a number. The number is
incremented until the name fails to match any known cell name in the
database.

Options for **gds write**:

**abstract** \[**allow**|**disallow**\]  
Define the behavior for abstract cells (e.g., cells derived from LEF
views). If allowed, then these cells will be written to GDS even if
the abstraction layers (e.g., metal obstructions) have no defined
GDS layers. If disallowed, the GDS file will not be written if
abstract cells exist. The default behavior is **disallow**.

**addendum** \[**yes**|**no**\]  
Do not output vendor (readonly) cell definitions. Only the
references will be output. This makes the output file an addendum to
any existing vendor GDS libraries.

**arrays** \[**yes**|**no**\]  
Output arrays as individual subuses (like in CIF). Default is "no".
Normally there is no reason to do this.

**compress** \[*value*\]  
For non-zero *value*, apply gzip-style compression to the output
stream. Per the gzip compression algorithm, *value* represents a
level of compression effort, and ranges from 1 to 9. When *value* is
zero, no compression is applied and the output is standard GDS
format, and the output file extension is ".gds". When *value* is
non-zero, compression is applied, and the output file extension is
".gds.gz". With no argument, return the current compression setting.
The default compression setting is zero (no compression applied;
output is plain GDS).

**contacts** \[**yes**|**no**\]  
Causes contacts to be written to the GDS file as subcell arrays
(experimental, introduced in version 7.3.55). This method can
produce very efficient output compared to writing each contact cut
square separately.

**datestamp** \[**yes**|**no**|*value*\]  
When writing a GDS file, each cell definition is given a header
containing two date stamps, one for the creation date, and one for
the modification date. By default, magic writes the cell's internal
timestamp as the creation date, and sets the modification date stamp
to zero. The **datestamp** option, if set to **no**, will also set
the creation date stamp to zero. If set to *value*, then the
specified stamp value will be output for the creation date. The
stamp value should be an integer in the format used by the UNIX
time() system call, which is the number of seconds since January 1,
1970, or equivalently the Tcl command "**clock seconds**". Note that
very few tools make use of the GDS date stamps. But having a valid
date stamp means that a GDS file cannot be written twice with the
exact same contents, which has implications for repositories like
git. When writing libraries, it is useful to set a date stamp tied
to a version number and apply that date stamp to all files written
for the library.

**labels** \[**yes**|**no**\]  
Cause labels to be output when writing GDSII. Default is "yes".
Normally there is no reason not to do this.

**library** \[**yes**|**no**\]  
Do not write the top level cell into the output GDS file, but write
only the subcells of the top level cell. Default is "no".

**lower** \[**yes**|**no**\]  
Allow both upper and lower case in labels. Default is "yes".

**merge** \[**yes**|**no**\]  
Concatenate connected tiles into polygons when generating output.
Depending on the tile geometry, this may make the output file up to
four times smaller, at the cost of speed in generating the output
file. Some programs like the field equation solver HFSS won't work
properly with layout broken into many tiles; other programs like
Calibre will complain about acute angles when non-Manhattan geometry
is broken into triangles. GDS output limits polygon boundaries to a
maximum of 200 points, which limits the efficiency of the merge
method. The default value if "no"; e.g., all GDS output is a direct
conversion of tiles to rectangle and triangle boundary records.

**nodatestamp** \[**yes**|**no**\]  
Backwardly compatible alternative to the **datestamp** option.
Setting **nodatestamp yes** is equivalent to setting **datestamp
no** (see above).

**undefined** \[**allow**|**disallow**\]  
Define the behavior for undefined cells (e.g., cells whose layout
contents could not be found). If allowed, then the calls to these
cells will be written to GDS even if the cell itself is not defined
in the GDS (see the **addendum** option, above). If disallowed, the
GDS file will not be written if undefined references exist. The
default behavior is **disallow**.

### Summary:

The **gds** command reads or produces GDSII output (also known as
"stream" output, or "calma" output after the name of the company that
invented the format), or sets various parameters affecting the GDS
input and output. In magic, the GDS read and write routines are a
subset of the CIF read and write routines, and so it is important to
note that certain **cif** command options (q.v.) also affect GDS input
and output. In particular, **cif istyle** and **cif ostyle** set the
input and output styles from the technology file, respectively.

If no option is given, a CALMA GDS-II stream file is produced for the
root cell, with the default name of the root cell definition and the
filename extension ".gds".

**gds read** will read both (gzip-)compressed and uncompressed GDS
files. **gds write** will only write compressed files as indicated by
the **gds compress** setting.

### Implementation Notes:

**gds** is implemented as a built-in function in **magic**. The
**calma** command is an alias for **gds** and is exactly equivalent.

### Bugs:

-   The **cif** command options that affect GDS input and output
should *really* be duplicates as options of the GDS command.
-   GDS input is "interpreted" through boolean operations in the
technology file definition, and so it is not guaranteed that all
input will be read correctly.
-   Not all non-Manhattan geometry is read correctly.
-   The input can be fouled up if the magic grid is rescaled during
input. This error can be avoided by scaling the grid prior to GDS
read-in.
-   "polygon subcells" in GDS creates a duplicate image of the layout
read into the subcells; this needs to be fixed.

### See Also:

[**cif**](#cif)  

## get, getcell

------------------------------------------------------------------------

Import a cell as a subcell of the current edit cell.

------------------------------------------------------------------------

### Usage:

**getcell** *cellname* \[*orientation*\]  

**getcell** *cellname* \[**child** *child\_refpoint*\] \[**parent**
*parent\_refpoint*\]  


where *orientation* may be one of the following:

**90**  
Load rotated by 90 degrees clockwise

**180**  
Load rotated by 180 degrees

**270**  
Load rotated by 90 degrees counterclockwise

**v**  
Load flipped top to bottom

**h**  
Load flipped left to right

**90v**  
Load rotated 90 degrees clockwise and flipped top to bottom

**90h**  
Load rotated 90 degrees clockwise and flipped left to right

**180v**  
Load rotated 180 degrees and flipped top to bottom

**180h**  
Load rotated 180 degrees and flipped left to right

**270v**  
Load rotated 90 degrees counterclockwise and flipped top to bottom

**270h**  
Load rotated 90 degrees counterclockwise and flipped left to right

and *child\_refpoint* and *parent\_refpoint* may be *x y* coordinate
pairs, or one of the four keywords **ll**, **lr**, **ul**, or
**ur**, indicating one of the four box corners. For the child,
coordinate pairs are in the coordinate system of the child, and
corners indicate cell bounding box corners. For the parent,
coordinate pairs are in the coordinate system of the parent, and
corners indicate corners of the cursor box.

### Summary:

The **getcell** command creates subcell instances within the current
edit cell. By default, with only the *cellname* given, an orientation
of zero is assumed, and the cell is placed such that the lower-left
corner of the cell's bounding box is placed at the lower-left corner
of the cursor box in the parent cell.

### Implementation Notes:

**getcell** is implemented as a built-in command in **magic**.

**get** is an alias for the command **getcell** (allowed abbreviation
where otherwise use would be ambiguous).

Scripts will find it more convenient to place cells according to the
cell origin, with the usage "**getcell** *cellname* **child 0 0**".

### See Also:

[**dump**](#dump)

## get, getcell

------------------------------------------------------------------------

Import a cell as a subcell of the current edit cell.

------------------------------------------------------------------------

### Usage:

**getcell** *cellname* \[*orientation*\]  

**getcell** *cellname* \[*orientation*\] \[**child**
*child\_refpoint*\] \[**parent** *parent\_refpoint*\]  


where *orientation* may be one of the following:

**90**  
Load rotated by 90 degrees clockwise

**180**  
Load rotated by 180 degrees

**270**  
Load rotated by 90 degrees counterclockwise

**v**  
Load flipped top to bottom

**h**  
Load flipped left to right

**90v**  
Load rotated 90 degrees clockwise and flipped top to bottom

**90h**  
Load rotated 90 degrees clockwise and flipped left to right

**180v**  
Load rotated 180 degrees and flipped top to bottom

**180h**  
Load rotated 180 degrees and flipped left to right

**270v**  
Load rotated 90 degrees counterclockwise and flipped top to bottom

**270h**  
Load rotated 90 degrees counterclockwise and flipped left to right

and *child\_refpoint* and *parent\_refpoint* may be *x y* coordinate
pairs, or one of the four keywords **ll**, **lr**, **ul**, or
**ur**, indicating one of the four box corners, or the name of a
label in the parent or child cell. For the child, coordinate pairs
are in the coordinate system of the child, and corners indicate cell
bounding box corners. For the parent, coordinate pairs are in the
coordinate system of the parent, and corners indicate corners of the
cursor box. If **child** or **parent** options are not provided,
then the default behavior is the same as "**child ll**" and
"**parent ll**", respectively. If a label name is given, then the
position (anchor point) of the label will be used as the reference
point.

### Summary:

The **getcell** command creates subcell instances within the current
edit cell. By default, with only the *cellname* given, an orientation
of zero is assumed, and the cell is placed such that the lower-left
corner of the cell's bounding box is placed at the lower-left corner
of the cursor box in the parent cell.

### Implementation Notes:

**getcell** is implemented as a built-in command in **magic**.

**get** is an alias for the command **getcell** (allowed abbreviation
where otherwise use would be ambiguous).

Scripts will find it more convenient to place cells according to the
cell origin, with the usage "**getcell** *cellname* **child 0 0**".

### See Also:

[**dump**](#dump)

## getnode

------------------------------------------------------------------------

Get node names of all selected paint

------------------------------------------------------------------------

### Usage:

**getnode** \[*option*\]  


where *option* may be one of the following:

**abort** \[*string*\]  
Stop the **getnode** search when the node name *string* is
encountered.

**alias** \[**on**|**off**\]  
If **on**, reports all names found for the node. If **off**, only
the canonical name is returned.

**globals** \[**on**|**off**\]  
If **on**, any global node name (names ending with "!") will
terminate the search, returning the global name. If **off**, global
names are treated like local node names.

**fast**  
Return the first name encountered, rather than finding the canonical
node name.

### Summary:

The **getnode** command queries areas of selected paint for netlist
node names. The converse of this command is **goto**.

### Implementation Notes:

**getnode** is implemented as a built-in command in **magic**. The
node name search uses the same algorithm as the netlist connectivity
selection function, and for very large networks, can be quite slow.

### See Also:

[**goto**](#goto)  

## goto

------------------------------------------------------------------------

Goto the named node

------------------------------------------------------------------------

### Usage:

**goto** *nodename* \[**-nocomplain**\]  


where *nodename* is any valid name for a network node.

### Summary:

The **goto** command moves the cursor box to some position
representing the network node named *nodename*, if it exists in the
layout. Because any given area of the layout may contain more than one
unconnected network node, a layer type is returned. The area of the
cursor box plus the layer type always uniquely identifies the node.

The **-nocomplain** switch supresses the warning message if the node
does not exist. In the Tcl version, an empty list is returned for
nodes that cannot be found, and no error condition is reported.

### Implementation Notes:

**goto** is implemented as a built-in command in **magic**. The Tcl
version of **magic** returns the layer of the node as a Tcl result.

A script may make use of the return value in the following manner:

**select box \[goto** *nodename***\]; select more net**

which selects the entire network named *nodename*.

### See Also:

[**getnode**](#getnode)  

## grid

------------------------------------------------------------------------

Toggle the grid lines on or off, and set grid parameters

------------------------------------------------------------------------

### Shortcuts:

Key macro **g** implements the command **grid** (with no arguments).
Key macro **G** implements the command **grid 2**.

### Usage:

**grid** \[*option*\]  


where *option* may be one of the following:

*x\_spacing* \[*y\_spacing* \[*x\_origin* *y\_origin*\]\]  
set the grid to the indicated spacing, where all spacing and origin
values are any valid **magic** [*distance*](#distance) value.

**on**|**off**  
Set the visibility of the grid on or off, as indicated.

**state**  
Report the state (on or off) of the grid. In the Tcl version, this
is returned as a boolean value (0 or 1).

**box**  
Report the box (rectangle) of the unit grid, in magic internal
coordinates.

**help**  
Print usage information on the **grid** command.

### Summary:

The **grid** command has two purposes: to draw a reference grid on the
screen as an aid to layout placement, and to define a snap grid of
arbitrary (and not necessarily square) units. This second use works in
conjunction with the **snap** command; with the invocation of **snap
grid** (or, equivalently, **snap user**), standard magic dimensions
for commands such as **move**, **copy**, **box**, **stretch**, and
mouse-button movement of the cursor box are parsed as integer
divisions of the user grid. The grid does not have to be visible
("**grid on**") for the snap function to be enabled.

Note that the grid has both spacing values and an offset; unlike the
lambda grid, which is always aligned to the internal coordinate
system, the user grid may be any value; for grid spacings that are not
a multiple of internal or lambda values, the grid may need to be
offset from the origin to get the desired alignment. To do this,
specify the *x\_origin* and *y\_origin* values, which describe the
offset of the grid origin from the internal coordinate system origin.

Usually there is no reason to have different *x\_spacing* and
*y\_spacing* values (only one spacing value is required for both).
However, occasionally it may be useful to define something like the
following:

**grid 150um 3l; snap grid**

This example makes it easy to draw a number of horizontal routing
lines aligned to a pad cell spacing of 150 microns.

Note that even when the grid is set to visible, at a large enough zoom
factor, where the grid lines become dense, the grid will not be drawn.

**grid** with no arguments toggles the visibility of the grid lines on
the screen.

### Implementation Notes:

**grid** is implemented as a built-in window command in **magic**.

### See Also:

[**snap**](#snap)  

## help

------------------------------------------------------------------------

Print out synopses for all commands valid in the current window (or
restrict output to those containing the indicated pattern)

------------------------------------------------------------------------

### Usage:

**help** \[*pattern*\]  


where *pattern* is any keyword or text string.

### Summary:

The **help** command invokes the built-in help function in **magic**,
which lists the summary usage information that has been compiled into
magic for each command. The summary help information is usually only a
single line of text. Commands that have complicated sets of options
have their own **help** option, which is not part of the **help**
command.

Without arguments, **help** reports a summary usage for every command
in magic. With arguments, magic filters the output to report only
those commands matching the indicated text *pattern*.

The output is divided into general-purpose and window-specific
sections. The window-specfic section depends on the active window. For
instance, with a single layout window present, **help cleanup**
returns no information. However, the command **specialopen netlist**
followed by **help cleanup** will report the usage of the command
**cleanup**, which is a command that can only be invoked from the
netlist window.

### Implementation Notes:

**help** is implemented as a built-in command in **magic**. Note that
there is no general-purpose command-line-based help method for Tcl
commands, so the **help** command will not provide any information
about magic commands written as Tcl procedures, such as
**openwrapper** or **pushstack**. The general convention is for each
Tcl procedure to allow the option **help** and provide its own usage
information.

## identify

------------------------------------------------------------------------

Set the use identifier of the selected cell

------------------------------------------------------------------------

### Usage:

**identify** *use\_id*  


where *use\_id* is a unique name to identify the cell use.

### Summary:

The **identify** command renames cell uses in **magic**. By default,
**magic** names cell uses with the name of the cell definition
followed by an underscore, followed by a unique index number for the
cell use in the parent cell. This is merely a convention, and any
unique identifier suffices to name the cell use.

### Implementation Notes:

**identify** is implemented as a built-in command in **magic**.

### See Also:

[**instance**](#instance)  

## imacro

------------------------------------------------------------------------

Define or print an interactive macro.

------------------------------------------------------------------------

### Usage:

**imacro** \[*window\_type*\] *key value*  


where *key* is a valid name for a keyboard key and *value* is the
command to be printed to the console, pending completion. If
present, *window\_type* must be one of the window types recognized
by the **specialopen** command: **layout**, **color**, **netlist**,
or **wind3d**. If omitted, the **layout** window type is assumed,
unless the command was called from inside a window using the colon
or semicolon escape to the command-line, in which case the type of
the calling window is assumed.

### Summary:

The **imacro** command allows a variant of the **macro** command in
which the bound command, rather than being immediately executed, is
instead printed to the console as the beginning portion of a command,
awaiting completion. It can be used to simplify typing of commands by
pre-formatting the command line with the command and possibly some
options. For example,

**imacro p "paint "**

will allow the single keystroke "p" to automatically format the
command "paint " on the command line, waiting for the user to enter
the type to paint and execute the command.

Unlike the **macro** command, commands entered by **imacro** are
ultimately evaluated by the Tcl interpreter, and so may contain Tcl
commands as well as magic commands.

### Implementation Notes:

**imacro** is implemented as a built-in window command in **magic**.

### See Also:

[**macro**](#macro)  

## initialize

------------------------------------------------------------------------

Initialization of **magic** from the Tcl interpreter.

------------------------------------------------------------------------

### Usage:

**initialize** \[*arguments*\]  


where *arguments* is the list of arguments passed to **magic** on
the UNIX command-line.

### Summary:

The **initialize** command is part of the procedure for starting magic
from inside the Tcl interpreter. It is not a user command. Other
Tcl-based packages that wish to use **magic** directly should follow
this procedure:

-   Load the tclmagic.so object file.
-   Call **initialize** with arguments passed to **magic** on the
command line.
-   Call **startup**

### Implementation Notes:

**initialize** is implemented as a built-in command in **magic**, but
only in the Tcl version.

### See Also:

[**startup**](#startup)  

## instance

------------------------------------------------------------------------

Operations on cell instances (uses).

------------------------------------------------------------------------

### Usage:

**instance** *option*  


where *option* is one of the following:

\[**list**\] **children** \[*name*\]  
List all of the children instances of cell use *name*, or the
children of the currently selected cell instance.

\[**list**\] **parent** \[*name*\]  
List the parent cell definition of cell use *name*, or the parent of
the currently selected cell instance.

\[**list**\] **exists**|**self** \[*name*\]  
Returns the name of the instance if the cell exists, or false (0) if
the instance does not exist (is not loaded into the database; the
cell may still exist on disk). If *name* is not present, returns the
name of the currently selected instance.

\[**list**\] **allcells**  
List all of the cell instances in the database. Note that expansion
is not automatic, so cells that are not expanded are not searched.

**orientation** \[*name*\] \[**-def**\]  
Returns the orientation of the instance. By default, returns the
orientation in the naming convention used by the "**getcell**"
command. If the option "**-def**" is specified, then the orientation
is given in the naming convention used by the DEF format for
component placement. if *name* is given, then return the orientation
of the named instance. Otherwise, the orientation of all selected
instances is returned as an unordered list.

\[**list**\] **abutment**  
Returns the coordinates of the instance's abutment box (the bounding
box formed by the coordinates saved in the FIXED\_BBOX property in
the cell), translated into the coordinate system of the parent cell
(which must be the edit cell). This should be used, for example,
when replacing an instance of a standard cell with another standard
cell, to move the cursor box to the abutment box position so that
the new cell has the same alignment as the old cell (see also
**orientation**, above).

**lock**|**unlock** \[*name*\]  
Locking an instance prevents it from being moved, rotated, flipped,
deleted, or copied. This is useful, for example, when part of a
layout is declared "final" and changes to that area are prohibited.
The cell instance's lock status can be saved to and read from the
layout file, so the lock will remain in effect until the instance is
unlocked. Cells that are locked have the character "**\***"
prepended to the instance name in the display. With no *name* given
to the command, the lock will be applied to all selected cell
instances.

### Summary:

The **instance** command performs various operations on cell uses, or
instances. For the first four options listed above, **instance** lists
cells by their relationship to cell use *name*, or to the current
selection if no *name* is given. The optional argument **list**
returns the result as a list. In particular, in the Tcl version of
magic, this list is a Tcl result that may be operated on by Tcl
procedures.

### Implementation Notes:

**instance** is implemented as a built-in function in **magic** The
Tcl version of magic returns Tcl results when the "**list**" option is
present. **instance** is essentially an alias for the **cellname**
command, and takes many of the same options, but references are to
cell instances rather that cell definitions (q.v.). A number of
options to **cellname** are meaningless for instances.

*Warning:* Because instance names are arbitrary, looking up an
instance name is computationally intensive compared to looking up a
cell name. When used inside a loop, such as to search the cell name
hierarchy, use command **cellname** on cell definitions instead of
command **instance** on cell instance names whenever possible.

The command option **instance list exists** is nonsensical from the
standpoint of the end-user (if the cell is selected, of course it
exists). However, it is a very useful function for Tcl scripts to
determine the name of the cell instance that is currently selected.

### Bugs:

Technically, **instance rename** should be implemented as a
replacement for the command **identify**.

### See Also:

[**cellname**](#cellname)  
[**load**](#load)  
[**getcell**](#getcell)  
[*tk\_path\_name*](#tk_path_name)  

## <span id="Usage">Magic version 7.3 Usage</span>

Basic usage:  


<table data-border="1" data-frame="box" data-rules="none"
data-cellpadding="6" data-bgcolor="white">
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><table data-border="0" data-frame="box" data-rules="none"
data-cellspacing="0" data-cellpadding="0" data-bgcolor="white">
<tbody>
<tr class="odd">
<td>magic [-noc[onsole]] [-w[rapper]] [-d <em>devType</em>] [-T
<em>technology</em>] [<em>file</em>]</td>
</tr>
</tbody>
</table></td>
</tr>
</tbody>
</table>


where:  


-noconsole  

> (Tcl version only) Uses the calling terminal for terminal-based
> command-line input. Otherwise, a Tk console window is used.

-wrapper  

> (Tcl version only) Magic layout windows use the GUI wrapper,
> including cell and technology manager windows, layer toolbar, and
> file menu.

-d *devType*  

>   
> (all versions) Select the graphics interface at runtime.
> Specifying an invalid *devType* will result in a list of known
> types. The possible values of *devType* are determined at compile
> time, but the usual ones are **NULL** (no graphics), **X11**, and
> **OpenGL**. X11 is the usual default.

-T *technology*  

> (all versions) Select the appropriate technology (.tech27) file.
> At present (this is on the to-do list), magic cannot change
> technology after startup. So the technology file corresponding to
> the layout to be loaded must be supplied to the command line at
> startup. The default technology is scmos, which is included with
> the magic source distribution. The complete list of available
> technology files depends on what has been installed on the system
> (#see the [technology file](#tech) page for details).

*file*  

> (all versions) Load the layout (.mag) file *file* into the layout
> window on startup.

Complete usage information:  


magic \[-noc\[onsole\]\] \[-w\[rapper\]\] \[-nowindow\] \[-d
*devType*\] \[-T *technology*\] \[-m *monType*\] \[-D\] \[*file*\]  

where the additional options not covered above are:  


-nowindow  

> (Tcl version only) Run without displaying an initial layout
> window. This is used mainly for GUI wrapper scripts which like to
> generate and handle their own windows.

-m *monType*  

> (obscure) *monType* names a monitor type. This is used in the
> search for the colomap file name, which is designated
> &lt;tech&gt;.&lt;planes&gt;.&lt;mon&gt;.cmap1. The default is
> "**std**" (corresponding to colormap file "mos.7bit.std.cmap1".
> The only other monitor type for which colormaps exist in the
> distribution is "mraster". This provides a way for users to
> override the system color assignments.

-D  

> (all versions) Run in Debug mode.

Obsolete usage information:  


magic \[-g *gPort*\] \[-i *tabletPort*\] \[-F *objFile* *saveFile*\]
...  

where the additional options not covered above are:  


-g *gPort*  

> (largely obsolete) *gPort* names a device to use for the display.
> This was generally used in the past with dual-monitor systems,
> especially Sun systems in which the layout display might go to
> /dev/fb.

-i *tabletPort*  

> (largely obsolete) *tabletPort* names a device to use for graphics
> input. This has not been tested with modern graphics tablet
> devices. It is ignored by the X11 and OpenGL display interfaces.

-F *objFile* *saveFile*  

> (largely obsolete) Create an executable file of the current magic
> process, a core image snapshot taken after all initialization.
> *objFile* is the name of the original executable, and the image
> will be saved in *saveFile*. This only works on VAXen and SUNs
> running an old SunOS (using a.out executables).
## iroute

------------------------------------------------------------------------

Do interactive point-to-point routing from the pointer cursor to the
cursor box

------------------------------------------------------------------------

### Usage:

**iroute** *option*  


where *option* may be one of the following:

**contacts** \[*type*\] \[*parameter*\] \[*value*...\]

Set route-contact parameters. *parameter* may be one of the
following keywords:

**active**  

**width**  

**cost**  

**help** \[*option\_name*\]

Summarize iroute subcommands

**layers** \[*type*\] \[*parameter*\] \[*value*...\]

Set route-layer parameters. *parameter* may be one of the following
keywords:

**active**  

**width**  

**hCost**  

**vCost**  

**jogCost**  

**hintCost**  

**route** *node\_name*...

Connect point to named node(s)

**route** *option*...

Connect points as specified in the options. *option* my be one of
the following:

**-dbox**  
Route to the area of the cursor box.

**-dlabel** *node\_name*  
Route to the destination network named *node\_name*. The name may be
hierarchical, specifying a labeled node in a nested list of subcell
instances.

**-dlayers** *layer\_list*  
Force the route to end on of one the layers in the comma-separated
list.

**-drect** *llx lly urx ury*  
Force the route to end within the designated rectangular area.

**-dselection**  
Force the route to end on the area of selected paint.

**-scursor**  
Start the route at the cursor position.

**-slabel** *node\_name*  
Route from the start network named *node\_name*. The name may be
hierarchical, specifying a labeled node in a nested list of subcell
instances.

**-slayers** *layer\_list*  
Force the route to start on one of the layers in the comma-separated
list.

**-spoint** *px py*  
Start the route at the indicated point.

**-timeout** *value*  
If the maze router is unable to find a valid route, it may wander
off into an indefinitely long search. The search can be interrupted
by typing a control-C into the calling terminal, but one can also
specify a timed break using the timeout option, where *value* is in
seconds. Typically, 4 or 5 seconds is a useful value.

By far, the most useful and most common invocation is "**iroute
route -slabel** *sname* **-dlabel** *dname*" to route between two
named pins.

Write out all irouter parameters. These are written out as command
calls so they can be read back with the Tcl **source** command.

**search** **rate**|**width**

Set parameters controlling the internal search for routes

**spacings** *type*

Set minimum spacing between route-type and arbitrary type

**verbosity** *level*

Control the amount of messages printed

**version**

Identify irouter version

**wizard** *parameter*

Set miscellaneous parameters. *parameter* may be one of the
following keywords:

**bloom**  

**boundsIncrement**  

**estimate**  

**expandDests**  

**penalty**  

**penetration**  

**window**  

### Summary:

The **iroute** command invokes Magic's maze router algorithm. This is
a point-to-point, over-the-cell algorithm based on costs specified in
the technology file's "**mzrouter**" section, style "**iroute**". It
is not a channel router, and will select the best path to connect the
chosen start and destination nodes, using whatever layers are
specified as active in the technology file, switching layers and
adding contacts as necessary, and avoiding obstacles. The quality of
the route is highly dependent upon both the existing layout and the
cost specification.

Special layer types "**fence**", "**rotate**", and "**magnet**" are
built-in types available in all technologies. Painting the "**fence**"
layer creates a boundary inside of which Magic will not route. Under a
block of "**rotate**" layer paint, Magic will reverse the vertical and
horizontal costs of all layers. If the technology file specifies
unbalanced horizontal and vertical costs, for example to tend to force
horizontal routes in metal2 and vertical routes in metal3, then areas
painted with "rotate" will tend to get horizontal routes in metal3 and
vertical routes in metal2.

### Implementation Notes:

**iroute** is implemented as a built-in command in **magic**.

### See Also:

[**route**](#route)  
[**garoute**](#garoute)  

## irsim

------------------------------------------------------------------------

Invoke the **irsim** switch-level digital simulator.

------------------------------------------------------------------------

### Usage:

**irsim** \[*args*\]  


where *args* are any arguments to be passed to the **irsim** program
as they would from the command line. See the **irsim** documentation
for an explanation of its valid command-line arguments.

### Summary:

The **irsim** command starts the **irsim** simulator. While previous
versions of magic did this by forking the **irsim** process, Tcl-based
**magic** can load the Tcl-based **irsim** as a package directly into
the interpreter. Commands for **irsim** are added to the Tcl namespace
and are available directly from the the **magic** command line.

As a Tcl script, the **irsim** command attempts to set up the
simulation arguments to ensure proper startup. It also checks for a
valid .sim file matching the layout, and generates one if it does not
already exist.

A number of commands are available for viewing signal values directly
on the layout. For a complete description of these commands and the
Tcl-based **irsim** simulation environment, see the documentation on
**irsim**.

### Implementation Notes:

**irsim** is implemented as a Tcl procedure that loads the Tcl-package
based version of **irsim**, then executes its startup procedure. The
**irsim** Tcl package itself is compiled and installed separately from
**magic**.

### See Also:

[**ext2sim**](#ext2sim)  

## label

------------------------------------------------------------------------

Place a label in the layout

------------------------------------------------------------------------

### Usage:

**label** *string* \[*position* \[*layer*\]\]  


where *string* is the text of the label, *position* may be any valid
[*direction*](#direction) in **magic**, and *layer* may be any
valid layer in the technology.

**label** *string* \[*font* \[*size* \[*rotation* \[*offsetx offsety*
\[*position* \[*layer*\]\]\]\]\]  


where *string* is the text of the label, *font* is the name or
number of a font, *size* is the integer size of the font, in
standard [distance](#distance) units; *rotation* is the rotation
(in degrees) of the font, *offsetx* and *offsety* are the distance
of the printed text relative to the reference position (in quarter
units of [distance](#distance)); *position* may be any valid
[direction](#direction) in **magic**, and *layer* may be any
valid layer in the technology. This usage is only available in
**magic** version 8.0 and above. See the
[**setlabel**](#setlabel) command for details on each of the
label options. **setlabel -default** can be used to set default
values for all of the optional properties when they are not present
on the **label** command line.

### Summary:

The **label** command places a label on the layout. The label is
marked by a point, line, or rectangle, depending on the size of the
cursor box. If the area under the cursor box contains exactly one
type, the label will be "attached" to that type; that is, the label
will name the network of the node containing that type. If the area
under the cursor box contains multiple layers, one will be chosen for
attachment to the label. If there are multiple network nodes under the
cursor box, the result may not be what the user intended; in such
cases, the user should specify which *layer* the label should be
attached to, so that the appropriate network node will be labeled.

The label text is placed to one side of the marker in the direction
indicated by the *position* argument. For example, "**label text
north**" will draw the label string "text" to the north (above) the
marker.

In versions of **magic** prior to 8.0, labels cannot be directly
modified; modifications should be handled by first erasing the label
with "**erase label**" and then redrawing. Versions 8.0 and higher use
the [**setlabel**](#setlabel) command to modify selected labels.

Versions of **magic** from 8.0.139 allow the *layer* name to have a
dash ("**-**") in front (e.g., "**-metal1**") to indicate a "sticky
label", that is, one that is attached to the specified layer type
*layer*, and which cannot be reattached to another layer.

### Implementation Notes:

**label** is implemented as a built-in command in **magic**.

### See Also:

[**setlabel**](#setlabel)  
[**port**](#port)  

## lef

------------------------------------------------------------------------

LEF-format input and output

------------------------------------------------------------------------

### Usage:

**lef** *option*  


where *option* may be one of the following:

**read** \[*filename*\]  
Read a LEF file named *filename*\[**.lef**\]

**read** \[*filename*\] **-import**  
Read a LEF file. Import standard cells from .mag files

**read** \[*filename*\] **-annotate**  
Read a LEF file. Use any macros defined in the LEF file to annotate
existing layouts, and ignore all other macros.

**write** \[*cell*\] \[**-tech**\] \[**-hide** \[*distance*\]\] \[**-toplayer**\] \[**-pinonly** \[*distance*\]\] \[**-nomaster**\]  
Write LEF for the current or indicated cell.  
Option **-tech** writes the technology information (layer mapping
and rules) to the same file as the cell macro.  
Option **-hide** generates an abstract view that has all interior
detail removed, leaving only pins and obstruction layers covering
the entire cell with cut-out areas for the pins. Option **-hide**
may take an additional value argument *distance* which will hide the
central part of a cell starting a distance *distance* from the edge.
The *distance* value is in units of lambda by default, but like
other distance measurements changes with respect to the **snap**
command setting, and can take a suffix such as "**um**" to specify a
physical distance relative to the current CIF/GDS output scale.  
Option **-toplayer** outputs pin geometry only for the topmost layer
belonging to the pin; all connected layers underneath will be output
as obstructions.  
Option **-pinonly** will mark only areas that are port labels as
pins, while marking the rest of each related net as an obstruction.
Value *distance*, if given, will extend any pin beyond the marked
port label along the length of the same net, to the specified
distance into the interior of the cell.  
Option **-nomaster** will prevent the generation of output geometry
on layers defined as MASTERSLICE.

**writeall** \[**-tech**\] \[**-hide** \[*distance*\]\] \[**-notop**\] \[**-toplayer**\] \[**-nomaster**\]  
Write all cells including the top-level cell. This might be
appropriate if the top-level cell is a compendium of standard
cells.  
With option **-notop**: Write all subcells of the top-level cell,
but not the top-level cell itself. This is appropriate for
generating a LEF library from a layout, for which the layout itself
would be written to a DEF file.  
Options **-hide**, **-tech**, and **-toplayer** are the same as for
the **lef write** command.

**datestamp** \[*value*|**default**\]  
Force all cell definitions generated from LEF macros to have the
datestamp (timestamp) of *value*. This can be used to ensure that
the timestamps of abstract views match the timestamps of the
equivalent full views, so that switching between abstract and full
views does not cause timestamp mismatch handling. The string
**default** cancels any fixed timestamps.

**help**  
Print help information

### Summary:

The **lef** command writes LEF-format files, which are files
containing technology information and information about the content of
standard cells. It is used in conjunction with the **def** command to
read databases of routed digital standard-cell layouts. The .lef file
shares some information with the technology file in **magic**. At a
minimum, to read .lef files from third-party sources, the technology
file should have a **lef** section that maps magic layers to layer
names that are found in the .lef and .def files. Without this
information, **magic** will attempt to make an educated guess about
the routing layers, which normally will be named in an obvious manner
such as "metal1", "metal2", etc. The technology file section may be
necessary to handle more complicated input such as obstruction layers.
Most other aspects of a technology will be contained within the .lef
file. When writing .lef files, **magic** will use internal layer names
for the routing layers if no other information is present in the
**lef** section of the technology file.

Because the **lef** format allows standard cells to be minimally
defined (for purposes of protecting intellectual property), often the
.lef file contains no actual layout information for the standard
cells. **magic** provides a command option "**-import**". When
specified, for each macro cell in the input .lef file, **magic** will
look for a .mag file of the same name. If found, it will be loaded and
used in preference to the definition in the lef file.

Magic uses the **port** mechanism for labels to determine what are the
standard cells in a design. All cells containing **port** labels will
be considered standard cells when writing a .lef file. Ports retain
various bits of information used by the LEF/DEF definition, including
the port use and direction. See the **port** documentation for more
information.

Macro cell properties common to the LEF/DEF definition but that have
no corresponding database interpretation in **magic** are retained
using the cell **property** method in **magic**. There are specific
property names associated with the LEF format. These are as follows:

**LEFclass**  
Corresponds to the value of **CLASS** for a macro cell in the LEF
format.

**LEFsymmetry**  
Corresponds to the value of **SYMMETRY** for a macro cell in the LEF
format.

**LEFsite**  
Corresponds to the value of **SITE** for a macro cell in the LEF
format.

**LEFproperties**  
Corresponds to the value of **PROPERTY** for a macro cell in the LEF
format. LEF properties should be specified in a single cell property,
in key:value pairs and space-separated. Like all properties containing
spaces, the entire property string should be enclosed in quotes. When
writing output, each of the space-separated entries will be output on
its own PROPERTY line in the LEF file.

Normally, when importing a LEF/DEF layout into **magic**, one will
first execute a **lef read** command followed by a **def read**
command. Likewise, when writing a layout, one will first execute a
**lef writeall -notop** command followed by a **def write** command.

If a LEF file of macro definitions is read when the same cells as
named in the macros already exist in the magic database, then the LEF
file macros will be used to annotate the existing layout. This
includes setting pin properties (see above), extending the area of
labels to cover an entire port, and setting a bounding box on the cell
corresponding to the LEF origin and size.

Note that **lef write -hide** will generate only the minimum amount of
obstruction bounding any non-pin geometry inside a layout. To enforce
a larger obstruction area, the property "**OBS\_BBOX**" can be created
in the cell, a string with four values for the lower left and upper
right corners of the bounding box, in magic internal database units.

### Implementation Notes:

**lef** is implemented as a built-in command in **magic**. Only the
critical portion of the LEF syntax has been implemented. In
particular, simulation-specific properties of the technology and of
macro cells are not implemented.

### See Also:

[**def**](#def)  
[**port**](#port)  
[**property**](#property)  
[**snap**](#snap)  

## load

------------------------------------------------------------------------

Load a cell into the layout window

------------------------------------------------------------------------

### Usage:

**load** \[*cellname* \[**scaled** *n* \[*d*\]\]\] \[**-force**\]
\[**-dereference**\] \[**-quiet**\] \[**-silent**\] \[**-fail**\]  


where *cellname* is the name of a cell that presumably exists either
in the database memory or on disk as a .mag file. *n* and *d* are
the numerator and denominator, respectively, of a magnification
factor, if it is desired to load the cell at a different scale than
it was written. *d* defaults to 1 if not specified.

### Summary:

The **load** command loads a cell into the database and displays it in
the current layout window (if available). If the cell is not already
in the database memory, it is loaded from disk. If it cannot be found
on disk, then a new cell definition of name *cellname* is created and
loaded into the window.

By default, **magic** loads a cell from disk only if the technology
name matches the current technology. Historically, this has led to
most technologies being named "scmos" which undermines the purpose of
having a technology name in the first place. In magic-7.2 and 7.3,
this behavior can be overridden with the **-force** option. **magic**
will read the cell to the extent that layer names match between the
current technology and the technology of the file.

The **-force** option and **scaled** option can be used together to
port layouts from one technology to another. The **scaled** option
implements a scale conversion during input by redefining the ratio of
lambda to internal units during the load. This is useful if a cell was
written in a lambda-based technology but needs to be read into a
vendor-rules-based technology with a fine internal scale such as 0.1
micron per internal unit. The **scaled** option may also be used
simply to resize cell geometry, although this is generally only useful
to do for layout such as logos and text lettering drawn in routing
layers.

The **-silent** option prevents magic from generating error messages
during loads. This can be used to prevent magic from complaining that
a file does not exist when "**load**" is being used to create a new
cell, rather than load one from disk.

The **-quiet** option prevents magic from generating diagnostic output
during a file load. It will only print important warnings and errors.

By default, if a cell cannot be found in the search path, then a new
empty layout is created with the name of the specified cell. The
**-fail** option prevents magic from creating a new cell. Instead, if
the cell cannot be found in the search path, the load will simply
fail.

Since version 8.2.50, magic saves the path to each subcell used in a
design in the .mag file, to help with version control. This breaks
backwards compatibility with the traditional **load** command, which
would always use the search paths set by the
[**addpath**](#addpath) command. The **-dereference** option
restores the traditional behavior by ignoring all path references in
the input file and relying only on known search paths to locate the
source file for each subcell in the layout.

Note that if it is not desired to have *cellname* created if not found
on disk (e.g., because the path for the cell was missing from the
search path), the database can be updated with the **flush** command
or the **cellname delete** command.

Use of **load** with no *cellname* given will result in creating a new
cell called "(UNNAMED)".

### Implementation Notes:

**load** is implemented as a built-in command in **magic**.

### See Also:

[**xload**](#xload)  

## locking

------------------------------------------------------------------------

Control the behavior of file locking.

------------------------------------------------------------------------

### Usage:

**locking** \[**enable**|**disable**\]  


### Summary:

The **locking** command controls the behavior of file locking, which
is an operating system-level protocol for preventing multiple
processes from attempting to write to the same file at the same time.
The behavior of the protocol is operating system dependent; for
Linux/UNIX systems, this is a feature of the system fcntl() call. When
a file is opened, the file descriptor is associated with an exclusive
lock that prevents any other process from opening the same file for
writing or appending. When using the file locking feature, two
processes of magic cannot open the same file in read/write mode. The
first process to open the file will have the exclusive right to alter
the file contents. The second process may only view the layout in
read-only mode.

Any cell that is read-only can be forced editable using the
"**cellname writeable**" command option. Note that this does not make
the file writeable if another process has obtained a lock on the file;
it merely makes it editable, but to save the modified layout to disk
would require that the name of the cell be changed or that the process
holding the file lock releases it.

This is not a perfect protection mechanism, since the "**cellname
writeable**" command option can subvert the intent of the file lock by
allowing a cell to be read in read-only mode while another process has
it locked; then, after the other process has released the lock, the
file can be forced writeable and saved to the same file, potentially
overwriting modifications made by the other process. In normal use
cases, however, the file locking serves to prevent unintended
overwriting of file modifications.

The file locking is enabled by default when magic starts up. Generally
speaking, there is no reason to disable it. However, some operating
systems have strict limits on the allowed number of open file
descriptors, and it is possible for a sufficiently complex layout for
there to be more files open than available file descriptors. In that
case, the **locking disable** command option will prevent issues with
the filesystem at the expense of file lock protection.

With no arguments, **locking** returns the state of the file locking,
either "**enabled**" or "**disabled**".

### Implementation Notes:

**locking** is implemented as a built-in command in **magic** from
version tag 8.3.249.

### See Also:

[**cellname**](#cellname)  

## logcommands

------------------------------------------------------------------------

Log all commands into a file

------------------------------------------------------------------------

### Usage:

**logcommands** \[*file* \[**update**\]\]  


where *file* is the name of the log file to write to.

### Summary:

The **logcommands** command tells magic to write all command-line
commands and button pushes to the log file named *file*. If **update**
is specified, a screen update is generated after each command
executes.

### Implementation Notes:

**logcommands** is implemented as a built-in command in **magic**.

## macro

------------------------------------------------------------------------

Define or print a macro called char

------------------------------------------------------------------------

### Usage:

**macro** \[*window\_type*\] \[*key* \[*value*\]\]  


where *key* is the name of a valid key (see below), and *value* is a
**magic** command-line command. If present, *window\_type* must be
one of the four window types accepted by the **specialopen**
command: **layout**, **color**, **netlist**, and **wind3d**. If
omitted, the layout window is assumed by default, unless the command
has been called from inside a window (using the colon or semicolon
escape to the command-line), in which case that window type is
assumed.

### Summary:

The **macro** command translates keystrokes typed into a layout window
into **magic** command-line commands. When the key *key* is pressed in
a layout window, the command stored in *value* is executed relative to
that layout window. The default bindings are specified in the system
.magic file, read at startup. These macros may be arbitrarily rebound
using the **macro** command.

A key **macro** may be unbound from a command by passing an empty
string ("") for the *value*.

*key* is any valid name for a keyboard keypress event. In its simplest
form, this may just be the name of the key, such as "g" or "X". The
space bar key must be quoted in double-quotes; most other characters
may be unquoted. Control characters may be specified by the
two-character combination of the carat ("^") key followed by a capital
letter, such as "^Z". The use of embedded control characters is
deprecated, as it is incompatible with Tcl syntax.

*key* may also be specified as any valid X11 name for a key as defined
in the include file keysymdef.h on UNIX systems. This allows
specification of function keys such as "XK\_F8" or keypad keys such as
"XK\_KP\_Right".

Buttons are treated just like keys for the purpose of defining macros.
While the official names for buttons in keysymdef.h are
"**XK\_Pointer\_Button\_1**", etc., the **macro** command accepts the
abbreviated forms **Button1**, and so forth.

Finally, key modifiers may be prepended to the key name. Valid key
modifiers are **Shift\_**, **Control\_**, **Alt\_**, and **Meta\_**,
and may be coupled in any combination. Mouse buttons may also be
combined with key modifiers, so, for example, **Shift\_Button1** is a
legal, unique binding.

### Implementation Notes:

**macro** is implemented as a built-in window command in **magic**.

### See Also:

[**imacro**](#imacro)  

## maketoolbar

------------------------------------------------------------------------

Generate the GUI layout window toolbar.

------------------------------------------------------------------------

### Shortcuts:

Menu item *Options-&gt;Toolbar* implements the command
**maketoolbar**.

### Usage:

**maketoolbar** *frame\_name*  


where *frame\_name* is the Tk path name of a GUI layout window frame
(e.g., ".layout1", ".layout2").

### Summary:

The **maketoolbar** command generates the toolbar for the GUI layout
window. The toolbar contains a set of buttons representing each layer
type in the technology file. Each toolbar button has bindings for
mouse buttons and keys to implement shortcut commands in **magic**.
While the mouse pointer is inside the boundary of the toolbar button,
the name of the layer represented by the toolbar is printed in the
title bar of the window.

![](graphics/toolbar.gif)  
*Figure 1. The GUI toolbar for the default scmos technology.*

The default bindings for the toolbar buttons and the **magic**
commands they invoke are as follows:

*Button-***1**  
**see** *layername*

*Button-***3**  
**see no** *layername*

*Button-***2**  
**paint** *layername*

*Shift-Button-***2**  
**erase** *layername*

*Key-***p**  
**paint** *layername*

*Key-***e**  
**erase** *layername*

*Key-***s**  
**select more area** *layername*

*Key-***S**  
**select less area** *layername*

The toolbar is not present on window startup due to timing problems
with several window managers that prevents the correct measurement of
window height.

### Implementation Notes:

**maketoolbar** is implemented as a Tcl procedure in the GUI wrapper
script.

## measure

------------------------------------------------------------------------

Create a ruler to measure the distance between two points on a layout.

------------------------------------------------------------------------

### Usage:

**measure** \[*orient*\]  


### Summary:

The **measure** command is a script that creates a ruler to measure
the distance between two points on a layout. The ruler is positioned
within the bounds of the cursor box. The option *orient* may be
"**horizontal**", "**vertical**", or "**auto**", and determines
whether the ruler measures a width or a height. Without any option,
orientation **auto** is assumed. Automatic orientation chooses the
longer dimension of the cursor box as the dimension to measure.
Dimensions are printed in microns.

### Implementation Notes:

**measure** is implemented as a Tcl procedure in the "tools" script.
The ruler itself is implemented as elements (see the **element**
command), including line elements for the ruler and a text element for
the printed dimension.

### See Also:

[**unmeasure**](#unmeasure)  
[**element**](#element)  

## move

------------------------------------------------------------------------

Move the cursor box and the selection.

------------------------------------------------------------------------

### Shortcuts:

Key macro **m** implements the command **move** (no arguments).  
Key macro *Keypad-***8** implements the command **move n 1**  
Key macro *Keypad-***6** implements the command **move e 1**  
(and so forth for all 8 compass rose directions).

### Usage:

**move** \[**origin**\] \[*option*\]  


where *option* is one of the following:

[*direction*](#direction) \[[*distance*](#distance)\]  
Move the selection relative to the original position in the
direction *direction* by an amount *distance*.

**to** *x y*  
Move the selection to the coordinate location specified by the
coordinate pair *x y*.

### Summary:

The **move** command erases the current selection from its current
position and moves it according to the command arguments. Without
arguments, the lower-left hand corner of the selection is moved to the
current cursor position (the X11 cursor, not the **magic** "cursor
box"). With arguments *direction* and *distance*, the selection is
moved relative to the original in the indicated direction by the
indicated amount. The default distance is 1 unit (usually lambda; see
[*distance*](#distance) for further explication).

The option **origin** does not require a selection. It will relocate
the entire design such that the origin (coordianate 0, 0) is at the
position indicated by *option*. Note that this is more efficient than
unexpanding the contents of the top-level cell, selecting everything,
and moving the selection. For very large layouts, repositioning the
origin of a cell can be prohibitive (may overrun available memory),
and "**move origin**" is always preferred.

### Implementation Notes:

**move** is implemented as a built-in **magic** command.

### See Also:

[*direction*](#direction)  
[*distance*](#distance)  

## netlist

------------------------------------------------------------------------

Netlist operations for use with the "netlist tool" in a layout window.

------------------------------------------------------------------------

### Usage:

**netlist** *option*  


wher *option* may be one of the following:

**help**  
Print usage information

**select**  
Select the network nearest the cursor

**join**  
Join the current network and the network containing the terminal
nearest the cursor.

**terminal**  
Toggle the terminal nearest the cursor into or out of the current
network.

### Summary:

The **netlist** command works with the "netlist tool" and is the
interface between the layout window and the netlist window as
generated by the "**specialopen netlist**" command. The command
options, outlined above, allow interactive creation of netlists from a
layout. Note that this is only interface code; most manipulation of
the netlist is handled by the netlist window commands (see the section
in the [table of contents](#commands) on the netlist window
command set).

### Implementation Notes:

**netlist** is implemented as a built-in command in **magic**. Prior
to magic-7.3 revision 61, these functions were only available as
built-in button callbacks. They have been changed to command-line
commands with the switch to handling buttons like keys, with macro
bindings.

### See Also:

[**specialopen netlist**](#specialopen)  

## openwindow

------------------------------------------------------------------------

Open a new (non-GUI) layout window with indicated name, bound to
indicated cell

------------------------------------------------------------------------

### Shortcuts:

Key macro **o** implements the command **openwindow**. This macro is
disabled when using the GUI wrapper.

### Usage:

**openwindow** \[*cell*\] \[*name*\]  


where *cell* is the name of a cell to be loaded into the new window,
and *name* is the Tk path name of a top-level window (see below). An
empty string or Tcl NULL list "{}" for *cell* will cause the default
cell "(UNNAMED)" to be loaded.

### Summary:

The **openwindow** command opens a new layout window. Without
arguments, a new layout window named "magic*n*" is created, where *n*
is the index of the *n*th window to be created. Without a named cell,
the new window is loaded with a copy of the cell that was present in
the last generated layout window.

The use of parameter *name* is used in conjunction with a wrapper
script to attach the layout window to an existing Tk frame window.

### Implementation Notes:

**openwindow** is implemented as a built-in **magic** window command.
It should not be used with the GUI wrapper (invoked with **magic
-w**); instead, the **openwrapper** function should be used. Note that
it is possible to use this command in batch mode, although there is no
useful reason to do so.

### See Also:

[**closewindow**](#closewindow)  
[**openwrapper**](#openwrapper)  

## openwrapper

------------------------------------------------------------------------

Open a GUI layout window and all of its associated frames.

------------------------------------------------------------------------

### Shortcuts:

Menu option *File-&gt;New window* implements the command
**openwrapper** in the GUI layout window.

### Usage:

**openwrapper** \[*cellname*\] *frame\_name*\]\]  


where *frame\_name* is the Tk path name of the top-level layout GUI
window frame. By default, this name is .layout1, .layout2, etc., for
successive layout windows. *cellname* is the name of a cell to be
loaded into the window. Options behave the same was as they do for
the non-GUI **openwindow** command.

### Summary:

The **openwrapper** command creates a new layout window in the Tcl
version of magic. It is only applicable when magic is invoked with the
GUI wrapper, using **magic -w**, and supercedes the built-in command
**openwindow**.

### Implementation Notes:

**openwrapper** is implemented as a Tcl procedure in the GUI wrapper
script.

### See Also:

[**openwindow**](#openwindow)  
[**closewrapper**](#closewrapper)  

## orient

------------------------------------------------------------------------

Orient the selection according to the specified orientation.

------------------------------------------------------------------------

### Usage:

**orient** \[*orientation*\] \[**-origin**\]  


where *orientation* is an orientaton in the form given by the
**instance orientation** command, or an orienation in DEF format
(see below).

### Summary:

The **orient** command orients the selection according to the given
*orientation*, which may be in the same syntax returned by the
"**instance orientation**" command, or according to the syntax used by
the DEF format.

Valid values for *orientation* are: **0**, **90**, **180**, **270**,
**h**, **v**, or any combination of rotation and **h** or **v** (e.g.,
**90h**); or the DEF orientations **N**, **S**, **E**, **W**, **FN**,
**FS**, **FE**, and **FW**.

If **-origin** is specified, the orientation is around the origin of
the selection, not around the lower left-hand corner (see the
**clockwise** command).

### Implementation Notes:

**orient** is implemented as a built-in **magic** command.

### See Also:

[**clockwise**](#clockwise)  
[**sideways**](#sideways)  
[**upsidedown**](#upsidedown)  
[**instance**](#instance)  
[**getcell**](#getcell)  

## paint

------------------------------------------------------------------------

Paint mask information into the current edit cell

------------------------------------------------------------------------

### Shortcuts:

Key interactive macro **p** implements the command **paint** and waits
for input of the layer type.  
Mouse button 2 implements the command **paint cursor** when using the
"box tool" in a layout window.  

### Usage:

**paint** *layers*|**cursor**  


where *layers* is a comma-separated list of types to paint.

### Summary:

The **paint** command paints layer types in the current edit cell
inside the area of the cursor box.

Note that some layers, such as DRC layers, cannot be painted. Elements
are painted with the **element** command and feedback areas are
painted using the **feedback** command.

The "**paint cursor**" option picks the layers underneath the position
of the (X11) cursor and fills the cursor box with these types.
However, when no material (e.g., "space") is present under the cursor,
then all material and labels are erased from the area of the cursor
box.

### Implementation Notes:

**paint** is implemented as a built-in command in **magic**.

### See Also:

[**erase**](#erase)  

## path

------------------------------------------------------------------------

Modify or query **magic**'s search paths

------------------------------------------------------------------------

path \[search|cell|sys\] \[\[+\]path\]

### Usage:

**path** \[**search**|**cell**|**sys**\] \[\[**+**\]*path*\]  


### Summary:

The **path** command queries and manipulates the various search
paths used by magic. Without arguments, path **search** is assumed.
The three search paths are:

**search**  
The search path for layout files.

**cell**  
Search path for tutorial cells.

**sys**  
Search path for technology files.

The **+** option allows the path component *path* to be appended to
the indicated search path. Otherwise, the indicated search path is
replaced by the contents of *path*.

### Implementation Notes:

**path** is implemented as a built-in command in **magic**. The use
**path search +***path* supercedes the **addpath** command, as the
**path** command is more general.

### See Also:

[**addpath**](#addpath)  

## peekbox

------------------------------------------------------------------------

Query the last saved cursor box position

------------------------------------------------------------------------

### Usage:

**peekbox**  


### Summary:

The **peekbox** command sets the cursor box to the position of the box
last saved with the **pushbox** command. This is like the **popbox**
command except that the box is left on the stack.

### Implementation Notes:

**peekbox** is implemented as a Tcl procedure in the "tools" script.
It is useful when writing automated layout-generating Tcl scripts.

### See Also:

[**pushbox**](#pushbox)  
[**popbox**](#popbox)  

## plot

------------------------------------------------------------------------

Hardcopy plotting

------------------------------------------------------------------------

### Usage:

**plot** *option*  


where *option* may be one of the following:

**postscript** *file* \[*layers*\]  
Generate a PostScript file of layout underneath the box.

**pnm** *file* \[*scale* \[*layers*\]\]  
Generate a .pnm ("portable anymap") file of layout underneath the
box. The output size is propotional to *scale*, where a scale of 1
is one output pixel per **magic** internal unit. The default *scale*
value, if unspecified, is 0.5.  

*Note:* Magic version 7.5.45 changed the syntax to  
**plot pnm** *file* \[*width* \[*layers*\]\]  
where *width* is the width of the output, in pixels, having a
default value of 1500 if unspecified (which is reasonably
photographic when scaled to the size of a printed page). If the
parameter "**pnmplotRTL**" is set to **true**, then output is
filtered into HPRTL or HPGL2 format according to the "color
versatec" style settings. In that case, the filename is optional; if
missing, a temporary file is created.

**svg** *file*  
Generate an SVG (scalable vector graphics) file of the exact
contents of the layout window. Note that this command has no options
other than the name of the output file: SVG graphics are scalable,
so no scalefactor is necessary, and it is intended as a WYSIWYG
option. This option is *only* availble when magic is invoked with
the Cairo graphics interface ("magic -d XR"), because the libcairo
library has interchangeable back-end rendering engines and can
quickly swap out the X11 window rendering target for an SVG file
rendering target, something that cannot be done in the straight-up
Xlib or OpenGL interfaces. Note that when rendering to the screen,
no layout can be represented below the scale of a screen pixel,
whereas with scalable vector graphics, *all* layout is rendered, no
matter how dense. Therefore, for large full-chip layouts, the SVG
output can be very large and very dense. For full-chip rendering,
the PNM plot style is usually a better choice.

**versatec** *scale* \[*layers*\]  
Generate an HPRTL or HPGL2 rasterized rendering of the layout
underneath the box. The *scale* value is an absolute scale,
according to the physical size of the layout as determined by the
CIF or GDS output style, and the resolution of the rendering device
(i.e., printer or plotter). The device resolution is declared in the
plot parameters (see below).

**parameters** \[*name value*\]  
Set or print out plotting parameters (see Summary below).

**help**  
Print help information

### Summary:

The **plot** command generates hardcopy plots of a layout. The use of
**plot** for any particular output format requires that the parameters
of the format be defined in the **plot** section of the technology
file. However, from magic-7.3.56, the PNM handler will create a
default set of output styles from the existing layout styles for the
technology. This makes **plot pnm** compatible with *all* technology
files, regardless of whether or not a section exists for "**style
pnm**".

Each **plot** format has its own set of parameters, but all parameters
are controlled with the **plot parameters** option. Valid parameters
and their defaults are as follows:

General parameters:

<table data-border="0">
<tbody>
<tr class="odd">
<td><em>parameter name</em></td>
<td><em>default value</em></td>
</tr>
<tr class="even">
<td><strong>showCellNames</strong></td>
<td><strong>true</strong></td>
</tr>
</tbody>
</table>

PostScript parameters:

<table data-border="0">
<tbody>
<tr class="odd">
<td><em>parameter name</em></td>
<td><em>default value</em></td>
<td><em>explanation</em></td>
</tr>
<tr class="even">
<td><strong>PS_cellIdFont</strong></td>
<td><strong>/Helvetica</strong></td>
<td>Font used for writing cell use IDs</td>
</tr>
<tr class="odd">
<td><strong>PS_cellNameFont</strong></td>
<td><strong>/HelveticaBold</strong></td>
<td>Font used for writing cell definition names</td>
</tr>
<tr class="even">
<td><strong>PS_labelFont</strong></td>
<td><strong>/Helvetica</strong></td>
<td>Font used for writing label text</td>
</tr>
<tr class="odd">
<td><strong>PS_cellIdSize</strong></td>
<td><strong>8</strong></td>
<td>Font size for writing cell use IDs (in points)</td>
</tr>
<tr class="even">
<td><strong>PS_cellNameSize</strong></td>
<td><strong>12</strong></td>
<td>Font size for writing cell definition names (in points)</td>
</tr>
<tr class="odd">
<td><strong>PS_labelSize</strong></td>
<td><strong>12</strong></td>
<td>Font size for writing label text (in points)</td>
</tr>
<tr class="even">
<td><strong>PS_boundary</strong></td>
<td><strong>true</strong></td>
<td>Whether to draw boundaries around layers in addition to fill
patterns</td>
</tr>
<tr class="odd">
<td><strong>PS_width</strong></td>
<td><strong>612 (8.5in)</strong></td>
<td>Page width of the target output</td>
</tr>
<tr class="even">
<td><strong>PS_height</strong></td>
<td><strong>792 (11in)</strong></td>
<td>Page height of the target output</td>
</tr>
<tr class="odd">
<td><strong>PS_margin</strong></td>
<td><strong>72 (1in)</strong></td>
<td>Minimum margin to allow on all sides of the output page</td>
</tr>
</tbody>
</table>

HPRTL/HPGL2 parameters:

<table data-border="0">
<tbody>
<tr class="odd">
<td><em>parameter name</em></td>
<td><em>default value</em></td>
<td><em>explanation</em></td>
</tr>
<tr class="even">
<td><strong>cellIdFont</strong></td>
<td><strong>vfont.I.12</strong></td>
<td>Font used for cell use identifier names. The default font is part of
the Magic distribution.</td>
</tr>
<tr class="odd">
<td><strong>cellNameFont</strong></td>
<td><strong>vfont.B.12</strong></td>
<td>Font used for cell definition names. The default font is part of the
Magic distribution.</td>
</tr>
<tr class="even">
<td><strong>labelFont</strong></td>
<td><strong>vfont.R.8</strong></td>
<td>Font used for labels. The default font is part of the Magic
distribution.</td>
</tr>
<tr class="odd">
<td><strong>directory</strong></td>
<td><strong>/tmp</strong></td>
<td>The directory used to store the temporary output file that is
generated prior to spooling for the printer.</td>
</tr>
<tr class="even">
<td><strong>dotsPerInch</strong></td>
<td><strong>300</strong></td>
<td>The native resolution of the target rendering device (printer or
plotter)</td>
</tr>
<tr class="odd">
<td><strong>printer</strong></td>
<td><strong>versatec</strong></td>
<td>Name of the print spool queue.</td>
</tr>
<tr class="even">
<td><strong>spoolCommand</strong></td>
<td><strong>lp -d %s %s</strong></td>
<td>The OS command to use to send the plot to the printer or
plotter.</td>
</tr>
<tr class="odd">
<td><strong>swathHeight</strong></td>
<td><strong>64</strong></td>
<td>The number of lines of output resolution that Magic will generate at
a time. Normally it is not necessary to mess with this value.</td>
</tr>
<tr class="even">
<td><strong>width</strong></td>
<td><strong>2400</strong></td>
<td>The pixel width of the output device.</td>
</tr>
<tr class="odd">
<td><strong>plotType</strong></td>
<td><strong>hprtl</strong></td>
<td>The format of the plot to make. The choices are
<strong>hprtl</strong> (equivalent to PCL5) and <strong>hpgl2</strong>
for the most common raster plot formats. The two (very!) outdated
formats <strong>versatec_color</strong> and <strong>versatec_bw</strong>
are retained for compatibility.</td>
</tr>
</tbody>
</table>

PNM parameters:

<table data-border="0">
<tbody>
<tr class="odd">
<td><em>parameter name</em></td>
<td><em>default value</em></td>
<td><em>explanation</em></td>
</tr>
<tr class="even">
<td><strong>pnmmaxmem</strong></td>
<td><strong>65536</strong></td>
<td>Maximum memory (in KB) to use to generate output. Larger values
allow larger chunks of the layout to be processed at a time. Normally,
anything larger than the default will just take a long time to render,
so it's better to leave it alone and let the <strong>plot pnm</strong>
routine downsample the image to fit in memory if the size of the layout
requires it.</td>
</tr>
<tr class="odd">
<td><strong>pnmbackground</strong></td>
<td><strong>255</strong></td>
<td>Value of the background, where 0=black and 255=white. White is
default to match the printed page, which is where the plots usually end
up. A value of 200 is approximately the default background color in
<strong>magic</strong>.</td>
</tr>
<tr class="even">
<td><strong>pnmdownsample</strong></td>
<td><strong>0</strong></td>
<td>Number of bits to downsample the original layout. In the first pass,
one pixel is generated for each <em>n</em> magic internal units in each
of x and y, where <em>n</em> is the downsampling value. Each
downsampling bit therefore represents a factor of 4 in decreased
computation time. Generally speaking, downsampling causes information to
be lost in the translation from layout to the PNM file. However, if the
grid has been scaled from the original lambda, then downsampling up to
the scale factor will have no impact on the output other than speeding
up the rendering (because the minimum feature size is still in lambda,
so no feature will be overstepped by the downsampling). For example, for
a grid scaling of 1:10 the proper downsampling would be 3 bits. Note
that layouts that are too large for the allocated memory blocksize
<strong>pnmmaxmem</strong> will force downsampling regardless of the
value of <strong>pnmdownsample</strong>.</td>
</tr>
<tr class="odd">
<td><strong>pnmplotRTL</strong></td>
<td><strong>false</strong></td>
<td>When set to value <strong>true</strong>, this parameter pipes the
PNM plot output through the raster driver used by "plot versatec". This
allows rendered, antialiased PNM plots to be sent directly to a printer.
The versatec parameters are used to determine what format, printer,
spooler command, temporary directory, and printer pixel width and
resolution. The filename is optional in the "plot pnm" command when this
parameter is set. If the filename is missing, a temporary filename will
be generated for creating the file that is spooled to the printer
queue.</td>
</tr>
</tbody>
</table>

PostScript plotting is best suited for drawing small layouts with
relatively few components. PNM plotting is best suited for drawing
large layouts. For chip-size layouts, the PNM plots are virtually
identical to chip photographs. From magic version 7.3.56, plotting PNM
files requires no special entries in the technology file. Although
such entries can fine-tune the output, this is usually not necessary.
Also, since version 7.3.56, magic makes intelligent decisions about
memory usage, so it's generally not necessary to change the PNM plot
parameters. Raster plotting in HPGL2 and HPRTL formats are a good
alternative to PostScript for printers and plotters that support those
formats. The output is not scalable, but the size of the output plot
is much smaller and the speed of rendering is much faster.

### Implementation Notes:

**plot** is implemented as a built-in command in **magic**.

Original plot styles **versatec** and **gremlin** have been removed,
but shells of the code are retained so that magic doesn't complain
when encountering styles for these types in a technology file.

## plow

------------------------------------------------------------------------

Layout stretching and compaction

------------------------------------------------------------------------

### Usage:

**plow** *option*  


where *option* may be one of the following:

*direction*  
Where *direction* may be any valid Manhattan
[direction](#direction), and causes the plow to be moved in that
direction.

**boundary**  
Set boundary around area plowing may affect

**help**  
Print help information

**horizon** *n*  
Set the horizon for jog introduction to *n* lambda units.

**jogs**  
Reenable jog insertion (set horizon to 0)

**selection** \[*direction* \[*distance*\]\]  
Plow the selection in the indicated [*direction*](#direction)
for the indicated [*distance*](#distance).

**straighten**  
Automatically straighten jogs after each plow

**noboundary**  
Remove boundary around area plowing may affect

**nojogs**  
Disable jog insertion (infinite jog horizon)

**nostraighten**  
Don't automatically straighten jogs after each plow

### Summary:

The **plow** command implements a sophisticated method of stretching
and compacting layout. The cursor box can be used to shove layout in
one direction or another, preserving net connectivity through the
modifications.

Results of **plow** are usually messier than most VLSI designers care
to cope with. The best cell compaction is realized with careful
floorplanning considerations, not brute force pushing and shoving.

### Implementation Notes:

**plow** is implemented as a built-in command in **magic**.

### See Also:

[**straighten**](#straighten)  

## polygon

------------------------------------------------------------------------

Generate polygons from the command line.

------------------------------------------------------------------------

### Shortcuts:

None.

### Usage:

**polygon** *type x1 y1 x2 y2* ... *xn yn*  


where *type* is a tile type to draw, and *x1 y1* ... *xn yn* are *n*
vertices of a polygon.

### Summary:

The **polygon** command allows generation of polygons on the layout
from the command line, similarly to the **wire segment** command. The
**polygon** command automatically generates the proper tile geometry
for the polygon as specified by vertices. Vertex points are pairs of X
Y coordinates, and may take any dimensional value (default lambda, but
may be internal units or metric units). Note that polygons should be
convex; the tile generation algorithm is not guaranteed to work with
non-convex geometries.

While simple non-Manhattan structures (triangles) can be generated
with the "splitpaint" and "spliterase" commands using macros, there is
no convenient interactive method for generating complex polygon
geometry. The **polygon** command is best used in scripts to create
specific patterns based on known geometry.

### Implementation Notes:

**polygon** is implemented as a built-in command in **magic**.

### See Also:

[**wire**](#wire)  

## popbox

------------------------------------------------------------------------

Retrieve the last saved cursor box position

------------------------------------------------------------------------

### Usage:

**popbox**  


### Summary:

The **popbox** command sets the cursor box to the position of the box
last saved with the **pushbox** command, removing the saved position
from the stack.

### Implementation Notes:

**popbox** is implemented as a Tcl procedure in the "tools" script. It
is useful when writing automated layout-generating Tcl scripts.

### See Also:

[**pushbox**](#pushbox)  
[**peekbox**](#peekbox)  

## popstack

------------------------------------------------------------------------

Return from editing a cell that was loaded using **pushstack**.

------------------------------------------------------------------------

### Shortcuts:

Key macro **&lt;** implements the command **popstack**.

### Usage:

**popstack**  


### Summary:

The **popstack** command returns from editing a cell that was loaded
using the **pushstack** command, reverting the layout window to the
cell that was loaded prior to the **pushstack** call. This is
implemented as a stack, and calls may be nested.

### Implementation Notes:

**popstack** is implemented as a Tcl procedure in the "tools" script.

### See Also:

[**pushstack**](#pushstack)  

## port

------------------------------------------------------------------------

Declare a label to be a subcircuit port, or manipulate port parameters.

------------------------------------------------------------------------

### Usage:

**port** \[*name*|*index*\] *option*  


where *option* may be one of the following:

index *directions*  
Declare a label to be a port with order number *index* and with
allowed connection directions specified by the list *directions*.
This is equivalent to the **make** option, except that the index and
direction must be specified.

**class** \[*type*\]  
Get \[set\] port class type (see Summary, below).

**use** \[*type*\]  
Get \[set\] port use type (see Summary, below).

**shape** \[*type*\]  
Get \[set\] port shape type (see Summary, below).

**index** \[*number*\]  
Get \[set\] port number

**name** \[*name*\]  
Get \[set\] port name. This is equivalent to **setlabel text**.

**first**  
Return the first (lowest) port number used

**next** \[*number*\]  
Return the next (higher) port number used after port *number* if
specified, or after the currently selected port if not specified. If
*number* or the currently selected port is the last port number
used, then this command returns the value -1.

**last**  
Return the last (highest) port number used.

**equivalent** \[*number*\]  
Make the port equivalent to the (other) port numbered *number*.

**connections** \[*directions*\]  
Get \[set\] port connection directions

**make** \[index\] \[*directions*\]  
Declare a label to be a port with order number *index* and with
allowed connection directions specified by the list *directions*. If
not specified, the index is set to the first unused number, starting
with 1, and the direction defaults to the direction of the label
text. That is, if the label text is drawn to the right of the port,
then connections are allowed to the right side of the port.

**remove**  
Turn a port back into an ordinary label, removing all of its port
properties.

**renumber**  
Renumber all of the (unique) ports in the edit cell by alphabetical
order of the port label text. This will ensure that the order of
ports in a SPICE netlist generated by "extract" and "ext2spice" will
always be the same and not depend on artifacts of the way the cell
is extracted.

**help**  
Print help information

### Summary:

The **port** command turns labels into ports and manipulates the
properties of those ports. The **port** command gives **magic** some
understanding of "standard cells". A cell definition that contains
declared ports is treated specially by the **extract**, **ext2spice**,
**lef**, and **def** commands. All other commands interpret ports as
ordinary labels. **ext2spice** only interprets ports specially if the
option **ext2spice subcircuits on** is enabled. Cells that contain
port labels are assumed in these cases to be *standard cells*, that
is, cells which are pre-characterized, and for which the layout is not
to be interpreted as a physical circuit. When writing SPICE output, a
cell containing port labels that is a descendent cell of the top-level
layout is written as a subcircuit call, that is, an "X" record. If the
top-level cell in the layout contains ports, then the SPICE output is
written as a subcircuit definition, that is, wrapped in a ".subckt . .
. .ends" pair. For LEF files, a cell that contains ports is written as
a macro cell, and the ports are the declared PINs of the macro. For
DEF files, a cell that contains ports is written as a COMPONENT.

The "index" property of the port is used only when the cell is written
into a SPICE deck as a subcircuit entry, when the **ext2spice
subcircuit on** option is enabled (which it is by default). In that
case, the subcircuit call parameters (nodes) are written in the order
of the port indices, which are then assumed to match the definition
for the subcircuit. Likewise, if the circuit is written as a
subcircuit to a SPICE file, the order of parameters in the subcircuit
definition will match the order of the port indices. Note that the
actual port numbers are ignored; the port values will be written in
ascending order starting with the lowest numbered port and ending with
the highest numbered port.

The "direction" property of the port has no particular meaning to
magic but may be used by other programs to control the allowed
direction of routes into a standard cell. The "direction" value should
be a string containing one or more of the compass directions **n**,
**s**, **e**, and/or **w**. The default direction when not specified
is all four directions, **nsew**.

The "class", "use", and "shape" properties of the port have no
internal meaning to magic but are used by the LEF and DEF format read
and write routines, and match the LEF/DEF CLASS, USE, and SHAPE
properties for macro cell pins. Valid classes are: **default**,
**input**, **output**, **tristate**, **bidirectional**, **inout**,
**feedthrough**, and **feedthru**. Valid uses are: **default**,
**analog**, **signal**, **digital**, **power**, **ground**, and
**clock**. Valid shapes are: **default**, **abutment**, **ring**, and
**feedthrough** or **feedthru**.

Normally the **port** command operates on a selected label. However,
use of the optional *name* or *index* value in front of the command
option will cause the command to operate on the given label as
determined by the label text (*name*) or port index (*index*). In the
case of an invalid *name* or *index*, the command returns a null value
(empty string) and prints an error message. If the command ends with
the "**-quiet**" option, then no error message is printed.

### Implementation Notes:

**port** is implemented as a built-in command in **magic**.

### See Also:

[**label**](#label)  
[**lef**](#lef)  

## promptload

------------------------------------------------------------------------

Invoke the load-file widget in the GUI version of magic, prompting for a
file to load.

------------------------------------------------------------------------

### Shortcuts:

Menu item **File-&gt;Load layout** implements the command **promptload
magic**.  
Menu item **File-&gt;Read CIF** implements the command **promptload
cif**.  
Menu item **File-&gt;Read GDS** implements the command **promptload
gds**.

### Usage:

**promptload** **magic**|**cif**|**gds**  


### Summary:

The **promptload** command handles input of various file formats for
the GUI layout window in the Tcl-based version of magic when invoked
with the **magic -w** option. The handling is more sophisticated than
the underlying magic calls. The **gds** read function will attempt to
find the top-level GDS cell and load it into the current window.
Likewise, the **cif** read function will name the top-level cell with
the root name of the file being read. The **magic** load will append
the path of the indicated file to the search path, so that if the file
makes calls to additional cells in the same directory, they will be
found and loaded.

### Implementation Notes:

**promptload** is implemented as a Tcl procedure in the "wrapper"
script. It calls the **tk\_getOpenFile** widget in Tk.

### See Also:

[**promptsave**](#promptsave)  

## promptsave

------------------------------------------------------------------------

Invoke the load-file widget in the GUI version of magic, prompting for a
file to load.

------------------------------------------------------------------------

### Shortcuts:

Menu item **File-&gt;Save layout** implements the command **promptsave
magic**.  
Menu item **File-&gt;Write CIF** implements the command **promptsave
cif**.  
Menu item **File-&gt;Write GDS** implements the command **promptsave
gds**.

### Usage:

**promptsave** **magic**|**cif**|**gds**  


### Summary:

The **promptsave** command handles output of various file formats for
the GUI layout window in the Tcl-based version of magic when invoked
with the **magic -w** option. The handling of CIF and GDS formats
merely makes calls to the **cif** and **gds** write routines. The
handling of **magic** (.mag) format appends the destination path to
the search path. If the destination filename is changed in the Tk file
window, the **save** command is invoked to rename the top-level layout
appropriately before writing the output.

### Implementation Notes:

**promptsave** is implemented as a Tcl procedure in the "wrapper"
script. It calls the **tk\_getSaveFile** widget in Tk.

### See Also:

[**promptload**](#promptload)  

## property

------------------------------------------------------------------------

Attach a "property" (string key and value pair) to the edit cell

------------------------------------------------------------------------

### Usage:

**property** \[*key* \[*value*\]\]  


where *key* and *value* are any text strings.

### Summary:

The **property** command implements a general-purpose method of
attaching information to a cell definition. Except for a few
properties known to the **lef**, **extract**, and **gds** commands
(q.v.), properties have no inherent meaning to magic but may be used
with other programs or scripts to add additional information about a
cell definition.

With no arguments, all properties of the current edit cell are listed.
With only the *key* argument, the value associated with the key is
returned. With both arguments, the string *value* is associated with
the string *key* as a property of the cell. If *key* is an existing
key, then its original value will be overwritten.

Property names reserved by and used by magic:

**GDS\_FILE**  
The value is the name of a GDS file which contains the mask data for
the cell. The cell is then effectively an abstract view, because its
contents are in the GDS file and do not necessarily match what is
displayed (although they might).

**GDS\_START**  
If a **GDS\_FILE** is defined, then this value indicates the byte
position of the start of mask data for this cell definition in the
file. If set to value **0**, then the file will be searched for the
data bounds.

**GDS\_END**  
If a **GDS\_FILE** is defined, then this value indicates the byte
position of the end of mask data for this cell definition in the file.
If **GDS\_START** is set to **0**, then this property may be omitted.

**LEFview**  
If set to **TRUE**, this cell is an abstract view such as that
obtained from a LEF macro, and should not be used for extraction or
for writing mask data (unless **GDS\_FILE** is defined).

**LEFproperties**  
If the file was read from a LEF macro, then this property corresponds
to the LEF **PROPERTY** block values. All values from the block are
contatenated into the single property string.

**LEFsymmetry**  
If the file was read from a LEF macro, then this property corresponds
to the macro's **SYMMETRY** value.

**LEFclass**  
If the file was read from a LEF macro, then this property corresponds
to the macro's **CLASS** value.

**LEFsite**  
If the file was read from a LEF macro, then this property corresponds
to the macro's **SITE** value.

**CIFhier**  
If defined, then this cell will be written to CIF or GDS output with
hierachical processing regardless of the settings of the command
options "cif \*hier write disable" and "cif \*array write disable".
That allows those commands to be used to avoid time-consuming and
unnecessary hierarchical processing of a top-level chip assembly with
mostly correct-by-design components (such as a digital standard cell
layout) while preserving necessary hierarchical processing on blocks
(such as analog circuits) that need them.

**FIXED\_BBOX**  
This property value is a space-separated list of four integer values
corresponding to the abutment box of the cell, in magic's internal
units. The abutment box is automatically read from LEF files, but may
be defined for any file and can be used for placement alignment.

**OBS\_BBOX**  
This property value is a space-sparated list of four integer values
corresponding to a bounding box to be used when generating a LEF file
abstract view of a cell. The area inside the bounding box will be
entirely covered in obstruction layers (unless cut-outs are required
to accommodate pins). Any set-back applied by the "lef write -hide "
option will be applied to this obstruction box.

**device**  
This property declares that the cell is a device or contains a single
device that is not a known extractable device defined in the
technology file. In the first case, the device to be extracted is a
subcircuit and the name of the device is the same as the name of the
cell. In this case, the property value should begin with
"**primitive**". This may be followed by any parameters associated
with the device that need to be output in the netlist; e.g.,
"**primitive nf=4**. When the cell is recast as a primitive device, it
is necessary for the port order in the cell to match the port order of
the device as it must appear in the output netlist. In the second
case, the device to be extracted is either a low-level component type
(not a subcircuit), or is a subcircuit with a different name than the
cell. In that case, the value string should be the text of the line as
it should appear in a "**device**" line in the output .ext file when
the cell is extracted. That includes the names of all ports and any
parameters to be output. As the output device is defined inside the
subcircuit of the cell in which it is defined, the ports may be
reordered between the subcircuit and the instantiation of the device.
The use of either form of the **device** property precludes the
generation of parasitics associated with the cell. All parasitics are
assumed to be included in the device model.

**parameter**  
If, when an instance of the cell's subcircuit is generated in the
output netlist, the instance should be passed one or more parameters,
then those parameter *key***=***value* pairs (as a single,
space-separated string) should be defined as the value to the
**parameter** property.

**MASKHINTS\_***type*  
The value is a string of consecutive sets of four integer values, each
set representing the bounding box of a rectangle defining the area of
CIF type *type*, in magic's internal units. This indicates that magic
will always generate mask layer *type* in the specified rectangle area
when writing GDS or CIF output. *type* may be a templayer, such that
*type* could be defined as the absence of a mask layer, for example.

### Implementation Notes:

**property** is implemented as a built-in command in **magic**. The
property structure itself is implemented as a hash table in the cell
definition structure.

## pushbox

------------------------------------------------------------------------

Save the cursor box position on a stack for later restoring.

------------------------------------------------------------------------

### Usage:

**pushbox**  


### Summary:

The **pushbox** command saves the position of the cursor box onto a
stack, where it may be retrieved or queried using the **popbox** and
**peekbox** commands, respectively.

### Implementation Notes:

**pushbox** is implemented as a Tcl procedure in the "tools" script.
It is useful when writing automated layout-generating Tcl scripts.

### See Also:

[**popbox**](#popbox)  
[**peekbox**](#peekbox)  

## pushbutton

------------------------------------------------------------------------

Emulate a mouse button event.

------------------------------------------------------------------------

### Usage:

**pushbutton** *button action*  


where *button* is one of **left**, **middle**, or **right**, and
*action* is is one of **up** or **down**.

### Summary:

The **pushbutton** command is a way of invoking the actions associated
with mouse buttons from the command-line, or from a Tcl script.

### Implementation Notes:

**pushbutton** is implemented as a built-in window command in
**magic**. However, it is functionally equivalent to calling the Tk
function **event generate**.

### Bugs:

This is all backwards! There should be commands implemented to
generate the actions that are caused by button pushes in each tool,
and these commands should be bound to the button events. Presumably
the existing setup is a holdover from pre-X11 days.

## pushstack

------------------------------------------------------------------------

Load the selected cell and remember the action for later recall using
**popstack**.

------------------------------------------------------------------------

### Shortcuts:

Key macro **&gt;** implements the command **pushstack**.

### Usage:

**pushstack**  


### Summary:

The **pushstack** command loads the selected cell into the layout
window. However, unlike the **load** command, the **pushstack**
command remembers the action by saving the currently loaded cell on a
stack, so it can be recalled with the **popstack** command. Due to the
stack implemention, calls may be nested.

### Implementation Notes:

**pushstack** is implemented as a Tcl procedure in the "tools" script.

### See Also:

[**popstack**](#popstack)  

## quit

------------------------------------------------------------------------

Exit magic

------------------------------------------------------------------------

### Shortcuts:

Key macro *Control-Shift-***q** implements the command **quit**.

### Usage:

**quit**  


### Summary:

The **quit** command implements a resonably gentle exit from magic,
first prompting the user if layouts with changes have not yet been
committed to disk.

Note that in the Tcl version, if the magic package is unable to load
for some reason, the **quit** command will not be present, and the Tcl
**exit** command is required to quit the program. The Tcl **exit**
command will *always* exit **magic** immediately, without prompting or
cleanup or any other niceties.

### Implementation Notes:

**quit** is implemented as a built-in window command in **magic**.

## random

------------------------------------------------------------------------

Generate a random number or set a random seed.

------------------------------------------------------------------------

### Usage:

**random** \[**seed** \[*value*\]\]  


where *value* is any integer.

### Summary:

The **random** command with no arguments generates and returns a
random integer value. With option **seed** and no additional argument,
it sets the random seed value according to the current time. With
option **seed** and additional argument *value*, it sets the random
seed to the specified value.

When used with option **seed**, no value is returned.

Random numbers are generally frowned upon in layout because they can
make certain things non-reproducible from run to run. Magic uses
random numbers in only one very restricted circumstance, for GDS
output. The use in GDS output is restricted to the single circumstance
of writing an entire GDS file due to use of the "GDS\_FILE" property
in a cell with a "GDS\_START" property value of "0". Because the GDS
file may contain cells of unknown names, and these names could collide
with names in the database, the GDS file cells are all prefixed with a
random two-character string. To prevent the same prefix from being
used on any run of magic, the random number generator should be
appropriately seeded.

Note that there is no random number seeding on startup of magic, so if
needed, the random seed should be set in the startup file or on the
command line.

### Implementation Notes:

**random** is implemented as a built-in **magic** command.

### See Also:

[**gds**](#gds)  

## readspice

------------------------------------------------------------------------

Read a SPICE netlist file and use the information from subcircuit
definitions in the file to set port indexes.

------------------------------------------------------------------------

### Usage:

**readspice** *filename*  


where *filename* is the path name of a SPICE netlist file containing
one or more subcircuit definitions.

### Summary:

The **readspice** command is used to ensure that port indexes on port
labels in a cell match the port order specified in an existing SPICE
netlist for that cell. This is generally used with standard cell
libraries to ensure that port order is maintained in cells that are
read from GDS or LEF, neither of which declares a port order. It will
also create ports from labels in the case where a file read from GDS
does not contain layers that are interpreted as ports by the
technology file's **cifinput** section.

### Implementation Notes:

**readspice** is implemented as a Tcl procedure defined in the GUI
wrapper script. It is only available when the wrapper is used, that
is, when **magic** is invoked with argument **-w**, although the
script can be sourced from the runtime library.

### See Also:

[**port**](#port)  

## redo

------------------------------------------------------------------------

Redo commands

------------------------------------------------------------------------

### Shortcuts:

Key macro **U** implements the command **redo**.

### Usage:

**redo** \[**print** \[*count*\]\]  


where *count* indicates a number of events to be redone (default 1
event), and must be a nonzero positive integer.

### Summary:

The **redo** command reverses the effect of an **undo** command,
returning the layout in a specific window to the state it was in prior
to execution of the **undo** command.

The **print** option allows stack tracing for the **redo** command,
printing the top *count* events on the event stack in excruciating
detail.

### Implementation Notes:

**redo** is implemented as a built-in window command in **magic**.

### See Also:

[**undo**](#undo)  

## redraw

------------------------------------------------------------------------

Redraw the display.

------------------------------------------------------------------------

### Usage:

**redraw**  


### Summary:

The **redraw** command completely redraws the layout window. Normally,
**magic** records regions that require updating and redraws those
portions of the layout. However, key and button events are allowed to
interrupt the redraw, so on occasion it may be necessary to force a
refresh of the display.

### Implementation Notes:

**redraw** is implemented as a built-in window command in **magic**.

## render3d

------------------------------------------------------------------------

Create a top-level GUI frame for handling the 3D display window.

------------------------------------------------------------------------

### Usage:

**render3d**  


### Summary:

The **render3d** command creates a Tk top-level window for handling
the 3D display window. Currently, the window is rudimentary and does
essentially nothing more than the **specialopen wind3d** command does.

### Implementation Notes:

**render3d** is implemented as a Tcl procedure in the "wrapper"
script. This is basically a placeholder for a more complete GUI frame
for manipulating the 3D view.

### See Also:

[**specialopen**](#specialopen)  

## resumeall

------------------------------------------------------------------------

Resume normal display refresh on all windows.

------------------------------------------------------------------------

### Usage:

**resumeall**  


### Summary:

The **resumeall** command is a script that invokes the command
**update resume** on all layout windows. It is used in conjunction
with the **suspendall** command and is intended for use in Tcl scripts
that perform multiple manipulations on layout in a window, where it is
desired to have the entire display refresh at one time at the end of
the script rather than for each command within the script.

Because calls to **update** can be nested, calls to **suspendall** and
**resumeall** are likewise nested. The **resumeall** command will have
no effect until the same number of **resumeall** calls has been
encountered as the number of **suspendall** calls made.

### Implementation Notes:

**resumeall** is implemented as a Tcl procedure in the "tools" script.

### See Also:

[**update**](#update)  
[**suspendall**](#suspendall)  

## rotate

------------------------------------------------------------------------

Rotate the selection and box clockwise by the indicated amount.

------------------------------------------------------------------------

### Usage:

**rotate** \[**+**|**-**\]\[*degrees*\] \[**-origin**\]  


where *degrees* is the number of degrees to rotate, and must be a
manhattan amount (90, 180, 270).

### Summary:

The **rotate** command rotates the current selection by the specified
amount, in degrees. The default rotation is by 90 degrees. The amount
of rotation can be positive or negative, but must be one of the
Manhattan rotations 90, 180, or 270.

If **-origin** is specified, the rotation is around the origin of the
selection, not around the lower left-hand corner.

### Implementation Notes:

**rotate** is implemented as a built-in **magic** command. It is
equivalent to the **clockwise** command but allows negative values to
represent counterclockwise rotation.

### See Also:

[**clockwise**](#clockwise)  

## route

------------------------------------------------------------------------

Route the current cell

------------------------------------------------------------------------

### Usage:

**route** *option*  


where *option* may be one of the following:

**end** *value*  
Set channel router end constant. *value* type is real, and defaults
to 1.0.

**help**  
Print help information

**jog** *length*  
Set minimum jog length (integer grid units)

**metal**  
Toggle metal maximization (default is "on").

**netlist** *file*  
Set current netlist (default NULL)

**obstacle** *value*  
Set obstacle constant. *value* type is real, and defaults to 0.7.

**origin** \[*x y*\]  
Print or set routing grid origin

**stats**  
Print and clear previous route statistics

**settings**  
Show router parameters

**steady** *value*  
Set steady net constant. *value* type is integer, and defaults to 1.

**tech**  
Show router parameters read from the technology file.

**vias** *value*  
Set metal maximization via limit (grid units). *value* type is
integer, and defaults to 2.

**viamin**  
Via minimization

### Summary:

The **route** command performs standard routing of networks in a
netlist.

### Implementation Notes:

**route** is implemented as a built-in command in **magic**.

### See Also:

[**iroute**](#iroute)  
[**garoute**](#garoute)  

## ruler

------------------------------------------------------------------------

Create ruler markings inside the box with indicated text.

------------------------------------------------------------------------

### Usage:

**ruler** \[*text* \[*orient*\]\]  


where *orient* is either **vertical**, **horizontal**, or **auto**
(the default), and where *text* is any string. If the string
contains whitespace, it must be quoted.

### Summary:

The **ruler** command generates a "ruler", a set of lines indicating a
dimension. It is used to annotate layouts with the indicated text. If
no orientation is given, then automatic orientation it used, in which
the presented dimension (the line or lines with arrowheads) is
whichever box dimension (width or height) is longer. The ruler may be
removed with the **unmeasure** command. The **measure** command is a
specific type of ruler where the text is set to the presented box
dimension.

### Implementation Notes:

**ruler** is implemented as a Tcl procedure defined in the "tools"
script. It generates a set of elements (lines and text) with the
**element add** command.

### See Also:

[**measure**](#measure)  
[**unmeasure**](#unmeasure)  

## save

------------------------------------------------------------------------

Save edit cell on disk

------------------------------------------------------------------------

### Usage:

**save** \[*filename*\]  


where *filename* is a new name for the cell as well as the root name
of the .mag file to be saved.

### Summary:

The **save** command saves the current edit cell to disk. If
*filename* is specified, then the layout will be saved to
"*filename*.mag", and the current edit cell will be renamed to
*filename*.

The **save** command differs from **writeall** in several ways:
**save** does not descend the hierarchy, and does not prompt the user
for an action.

### Implementation Notes:

**save** is implemented as a built-in command in **magic**.

### See Also:

[**writeall**](#writeall)  

## scalegrid

------------------------------------------------------------------------

Set the ratio of magic internal units to lambda units

------------------------------------------------------------------------

### Usage:

**scalegrid** *a b*  


where *a* and *b* are integers.

### Summary:

The **scalegrid** command sets the ratio of magic internal units to
lambda units by rescaling the internal database and appropriate
technology parameters. The values *a* and *b* are interpreted to mean
that all positions in the database should be multiplied by the factor
*b* / *a*. An equivalent meaning is that there should be *b* internal
units per *a* lambda units in the database. For example,

**scalegrid 1 2**

means 2 internal units per lambda, or an internal grid that is twice
as finely spaced as the default. The grid scaling can be queried using
the **tech lambda** command. Grid scaling is interpreted relative to
the current scale, so

**scalegrid 1 2**  
**scalegrid 1 2**

results in 4 internal units per lambda.

### Implementation Notes:

**scalegrid** is implemented as a built-in command in **magic**.

### See Also:

[**snap**](#snap)  
[**tech**](#tech)  

## scroll

------------------------------------------------------------------------

Scroll the window

------------------------------------------------------------------------

### Shortcuts:

The keyboard arrow keys implement the command. Without modifiers, the
window scrolls by 1/10 width in the indicated direction. With *Shift*,
the window scrolls by one width in the indicated direction.

### Usage:

**scroll** *direction* \[*amount* \[*units*\]\]  


where *direction* is a valid Manhattan [direction](#direction),
and *amount* by default is an absolute [distance](#distance) in
any acceptable units. If *units* is **w**, then the *amount* is
interpreted as a fraction of the screen width. If *units* ls **l**,
then the *amount* is interpreted as a fraction of the layout width.
Note that units of distance for *amount*, such as "um" for microns
or "i" for internal units, are attached to the value with no
intervening space, whereas the two *units* keywords accepted by the
**scroll** command are a separate argument and separated from
*amount* by whitespace.

### Summary:

The **scroll** command implements a pan of the layout in the window in
the indicated direction by the indicated amount. The interpretation of
*amount* is described above in the Usage section.

### Implementation Notes:

**scroll** is implemented as a built-in window command in **magic**.

## search

------------------------------------------------------------------------

Execute a TCL procedure on each tile in the current edit cell
definition.

------------------------------------------------------------------------

### Usage:

**search** \[*layers*\] *procedure*  


where *layers* is a comma-separated list of layer types to generate
a mask to limit the tile search, and *procedure* is the name of a
predefined Tcl procedure (see Summary, below).

### Summary:

The **search** command is a method for user access to the **magic**
database search routines. It searches the tile database of the current
edit cell definition and its hierarchy of descendents and applies the
callback procedure to each. The callback procedure must be defined as
described below.

Note that the callback method into Tcl is inherently slow and should
only be used for non-compute-intensive tasks. In particular, unless it
is known that the cell definition being traversed has relatively few
structures, the *layers* argument should be used to severely limit the
scope of the search. This function can be useful in certain
situations, such as parsing a layout for layer "pad" to enumerate the
number of pads in a design.

The Tcl callback procedure is passed five values, the four coordinates
of the tile, and the layer type of the tile. The procedure must be
defined to accept these five arguments, as in the following example:

proc tile_callback {llx lly urx ury ttype} {
puts stdout "Tile type $ttype at $llx $lly $urx $ury"
}


When non-manhattan tiles are parsed, the type $ttype is passed as a
list of two string elements, the type on the left side of the diagonal
split, and the type on the right side of the diagonal split.

### Implementation Notes:

**search** is implemented as an internal **magic** command that links
to an external Tcl procedure as a callback function. This routine is
experimental and subject to change without notice.

### Bugs:

As currently implemented, there is no protection against calling a
**magic** command from the callback procedure that will alter the
internal tile structures while the tile plane is being traversed,
causing a crash. The implementation should be changed to a 2-step
procedure that traverses the tile plane first, creating an internal
list of function arguments to pass for each tile, and then executes
the callback function on each.

There are more efficient ways of executing the callback function than
Tcl\_EvalEx(). In particular, the procedure should be cast as a Tcl
object and Tcl\_EvalObjEx() used.

The callback function should allow in-line Tcl procedures and use the
standard Tcl/Tk method of "%" escape sequences used as arguments to
the callback function that allow the user to specify what arguments
are passed to the callback function (as is done for the **tag**
command).

### See Also:

[**cellsearch**](#cellsearch)  

## see

------------------------------------------------------------------------

Change what layers are displayed in the window

------------------------------------------------------------------------

### Shortcuts:

Mouse buttons 1 and 3 pressed in the GUI window toolbar implement the
**see** and **see no** commands for the layer represented by the
toolbar button.

### Usage:

**see** \[**no**\] *layers*|**allSame**  


where *layers* is a comma-separated list of layers in the
technology, and may also be the character **\*** indicating all
layers but not labels, **$** indicating all layers under the cursor
not including labels and subcells, **labels** indicating only
labels, **error** indicating DRC error paint, **subcell** indicating
subcells, and **connect** indicating all types connected to the type
or types preceding it.

### Summary:

The **see** command allows various layers in the layout to be made
visible, including labels and error paint. With the keyword **no**,
the command causes these layers to be made invisible on the display.

The keyword **allSame** is a special use and indicates that non-edit
cells should be drawn in the same manner as the edit cell, rather than
being drawn in the "pale" styles.

The keyword **connect** is only meaningful when it comes after one or
more listed types. It will expand the list of types to include types
electrically connected to those types.

The special keyword **$** is only meaningful when used with option
"**see no**", as it refers to all layers visible directly under the
pointer cursor, and it is not possible to query invisible layers.

Starting with Magic version 7.5, contacts whose residue layers (layers
surrounding the cut) are partially visible and partially invisible
will show the visible residue when the contact type itself is
invisible. That way, the command "**see no \* ; see m1**", for
example, will show all metal1 including that under contacts,
preventing the display of gaps in the metal1 layer where contacts are
present. Note that this applies *only* to contacts, where the residue
layers are declared in the techfile and therefore known *a priori*.
Other layers, such as metal1 resistor (often appears as "rmetal1" in
techfiles), have no relation to metal1 that can be definitively
determined from the techfile. Therefore, to see all layers
corresponding to a single production mask layer, it is necessary to
explicitly call out all such layers int the *layers* list.

Undisplayed layers generally do not respond to commands such as
**erase** or **select**. However, network selection will select across
invisible layers, and copying or moving such a network selection will
alter the invisible layers as well as the visible.

### Implementation Notes:

**see** is implemented as a built-in command in **magic**.

### Bugs:

It should be enforced everywhere in the code that invisible layers
cannot be altered. This may require removing invisible layers from a
selection after doing a network connectivity search.

## select

------------------------------------------------------------------------

Select or unselect portions of the layout according to the options, or
create a new cell definition from a selection.

------------------------------------------------------------------------

### Shortcuts:

Key macro **,** (comma) implements the command **select clear**.  
Key macro **s** implements the command **select**.  
Key macro **S** implements the command **select more**.  
Key macro *Control-***S** implements the command **select less**.  
Key macro **a** implements the command **select visible**.  
Key macro **A** implements the command **select more visible**.  
Key macro *Control-***A** implements the command **select less
visible**.  
Key macro **i** implements the command **select cell**.  
Key macro **I** implements the command **select more cell**.  
Key macro *Control-***I** implements the command **select less cell**.

### Usage:

**select** *option*  


where *option* may be one of the following:

\[**more** | **less**\] \[*layers*\]  
\[De\]select material under cursor, or \[de\]select a subcell if the
cursor is over space.

**nocycle** \[*layers*\]  
Select material without cycling through different tile types when
"select" is called from the same cursor position more than once.

\[**do** | **no** | **simple**\] **labels**  
Set policy for copying labels during a network selection.

\[**more** | **less**\] **area** \[*layers*\] \[*pattern*\]  
\[De\]select all material under box in layers *layers*. The optional
glob-style matching pattern *pattern* will select or deselect any
labels according to the pattern.

\[**more** | **less**\] **visible** \[*layers*\]  
\[De\]select all visible material under box in layers *layers*.

\[**more** | **less**\] **box** \[*layers*\]  
\[De\]select material specified by the boundary of the cursor box

\[**more** | **less**\] **chunk** \[*layers*\]  
\[De\]select a network chunk (largest rectangle) specified by the
lower left corner of the cursor box

\[**more** | **less**\] **region** \[*layers*\]  
\[De\]select a network region specified by the lower left corner of
the cursor box

\[**more** | **less**\] **net** \[*layers*\]  
\[De\]select an entire electrical network specified by the lower
left corner of the cursor box

\[**more** | **less**\] **cell** \[*name*\]  
\[De\]select the cell under cursor, or the cell use (instance) named
*name*.

**top cell**  
Select the topmost cell in the window, which does not have an
instance name and therefore cannot be selected with the **select
cell** command.

**save** *cell*  
Save selection as cell named *cell*, which is also saved to disk as
*cell*.mag.

**intersect** \[**~**\]*layer*  
Keep only the selected paint that intersects with *layer*. Used with
"**~**" or "**!**" in front of the layer, keep only the selected
paint that does not intersect with *layer*.

**clear**  
Clear selection

**pick**  
Remove the selection from the layout, but retain the selection
buffer for interactive processing.

**flat**  
Flatten the contents of the selection buffer.

**keep**  
Copy the selection from the layout into the selection buffer, and
keep the selection buffer for interactive processing.

**move** *x y*  
Move the selection buffer to position *x y*, relative to the cell
definition origin.

**bbox**  
Return the bounding box of the selection.

**feedback** \[ *style* \[ *text* \]\]  
(From Magic version 8.1.35) Copy the selection into a feedback area
for permanent display (until removed using "feedback clear"). The
selection will be displayed in style "*style*", which is one of the
styles defined in the graphics style file (e.g, colors like
"orange", "white"; layout styles like "pwell"; or technical styles
like "vert\_highlights"). The *text* is attached to the highlight
for querying using the "feedback why" command.

**short** *label1* *label2*  
(From Magic version 8.0.105) Find the path that electrically
connects (shorts) the nodes labeled "*label1*" and "*label2*". Note
that this is a simple tile-based search, so the highlighted path may
show only parts of wires, and may extend past points where the path
turns, but it will find a valid path if one exists.

**help**  
Print help information

### Summary:

The **select** command changes what material is in the current
selection. **magic** maintains a separate cell definition that
represents the current selection. Without the options **more** or
**less**, the selection is cleared prior to executing the new
selection command. Otherwise, **more** adds to the existing selection
and **less** subtracts from it.

Network selection differs from other types of selection in that
**magic** uses a sophisticated algorithm to determine what is
electrically connected together throughout the layout. A **chunk** is
the largest rectangle containing a single layer type. A **region** is
the largest network area containing a single layer type. The region
stops where the net connects to a different layer type. The **net** is
the entire electrical network.

The **select labels** option sets the policy for the selection of
labels when doing a **region** or **network** selection. The options
are **select do labels**, which is the default behavior, **select no
labels**, and **select simple labels**. The default behavior is to
copy all labels into the selection, but create hierarchical names for
any labels found in subcells by prepending the subcell instance name
in front with a slash ("/") character separator, in the same way as
hierarchical net names are generated in flattened SPICE output. This
allows a network selection to be copied without causing name
collisions among labels in subcells, and is the "safe" option.
However, such labels are often long and clutter up the layout. The
**no labels** option selects a network without selecting any labels at
all. The **simple labels** selects labels in subcells but does not
expand them into hierarchical names.

The **select save** option differs from the rest in that it does not
alter the current selection, but creates a new cell definition from
the current selection. Note that this cell is created as a top-level
cell, and does not replace the current selection as a use in the edit
cell. To do that requires "**select save** *cell*" followed by
"**delete**" and "**getcell child 0 0 parent 0 0**". The last command
syntax is used because the bounds of the selection may differ from the
cursor box.

The **select intersect** function allows the manipulation of the
selection using boolean operators that are much like the ones used in
reading and generating GDS files. **select intersect** *layer*
computes the value of the selection AND *layer* and replaces the
selection with the result. **select intersect ~***layer* computes the
value of the selection AND-NOT *layer* and replaces the selection with
the result.

The **select short** function finds an electrical connection between
two labeled points. It works by starting a "**select net**" net search
at the first label, continuing until it reaches the second label, and
then pruning back any branches of the search not directly connecting
the two points.

The **select bbox** function is useful when some command that only
operates on the contents of the cursor box needs to be applied to the
area of a selection. It returns the coordinates of the bounding box of
the selection. The cursor can be set to this using the Tcl command
**box values {\*}\[select bbox\]**. **select bbox** returns values in
internal coordinates, so be sure to set the snap spacing to **snap
internal** before doing this.

The remaining options such as **pick**, **clear**, and **flat** all
operate on the selection buffer without clearing the contents of the
buffer. They are used primarily by the "pick tool" for interactive
copy and paste functions. The following command sequence creates a new
cell from the selection and replaces the selected material with the
new cell:

**select pick**  
**select save** *cellname*  
**getcell** *cellname*

The following sequence flattens cells within a layout. This differs
from both the "**flatten**" and "**dump**" commands by being able to
flatten a group of cell uses, and being able to directly replace the
existing cell with the flattened paint. In effect, it is the reverse
of the operation above.

**select pick**  
**select flat**  
**select keep**

### Implementation Notes:

**select** is implemented as a built-in command in **magic**. The
**select keep**, **select move**, and **select pick** are interactive
functions used by the "pick" tool.

### See Also:

[**flatten**](#flatten)  
[**dump**](#dump)  
[**tool** (#Tcl script version)](#changetool)

### Bugs:

To be consistent, **select save** should be a separate command, since
like other commands it operates on the selection rather than alter
what is in the selection.

## setlabel

------------------------------------------------------------------------

Manipulate rendered font labels

------------------------------------------------------------------------

### Usage:

**setlabel** \[**-default**\] *option*  


where *option* is one of the following:

**box** \[*llx lly urx ury*\]  
Report the bounds of the attachment box for all selected labels, or
set the coordinates of the attachment box to the indicated values.

**font** \[*name* \[*scale*\]\]  
Report the font of all selected labels, or set the font to the font
named *name*, where *name* is one of the known fonts returned by the
command "**setlabel fontlist**". If the named font is not in the
list, magic will attempt to load it, if the font vector list can be
found (the font vector list should be in an unencoded PostScript
Type3 font format). Magic scales all fonts such that label size can
be specified in database units. Unfortunately, fonts tend to have
characters (accents, for example) well above the height of a
standard capital letter, and these characters result in the
inability to extract the font height from the font metrics. In such
(common) cases, the optional floating-point *scale* value specifies
the difference between the character height and the font height
reported by the font metrics. Typically, this number is around 0.6.

**font** *number*  
For *number* zero or larger, this option returns the name of the
font that is index *number* into the list of loaded fonts. No other
action is taken. For *number* equal to **-1**, the font of the
selected label is reset to the default X11 font, and properties such
as scale, offset, and rotation are ignored. Justification is
retained.

**fontlist**  
Return a list of the known, loaded fonts.

**justify** \[*position*\]  
Report the justification of all selected labels, or change the
justification to *position*, which may be any compass direction or
"center".

**layer** \[*name*\]  
Report the layer type to which the label is attached. If the
optional *name* is given, and is a valid layer name, then the label
is modified to be attached to that layer type. Note that if the
layer is not also declared "sticky" (see below), then it is likely
to be reattached to the original layer during certain operations.

**offset** \[*x y*\]  
Report the offset of all selected labels (in *x y* pairs), or change
the offset, which is the spacing between the point marked by the
label and the label text. In the case of a rectangle identifying a
label, the spacing is measured from the center of the rectangle.

**rotate** \[*value*\]  
Report the angle of rotation of all selected labels, or change the
angle, which is measured in degrees counterclockwise. Any integer
angle is acceptable. Labels are always drawn upright, so labels
rotated from 90 to 270 degrees undergo an additional 180 degree
rotation *within their bounding box* to ensure that the text always
remains upright. Likewise, rotations and reflections of subcells are
applied to the label bounding box, with the text rotated within the
bounding box to ensure an upright orientation. If this explanation
is a bit obscure, then the rule is: if a label is drawn on a cell
such that it occupies a specific place with respect to the cell
layout, then it will always appear in that same place regardless of
how the cell is oriented in the hierarchy of a layout.

**size** \[*value*\]  
Report the size of all selected labels, or change the size of
selected labels to *value*, which may be given in units of lambda,
or a metric measurement (e.g., "**1um**"). The text will be adjusted
so that the height of capitalized text from the text baseline is
equal to the requested value.

**sticky** \[**true**|**false**\]  
Report the status of the "sticky" flag for the label. Labels which
have the "sticky" flag set can only attach to the assigned layer
type. Such labels may be placed over a layer that exists only in a
subcell, unlike non-sticky labels, which will reattach to any
available layer or else be assigned to "space". Value returned is 1
(true) or 0 (false). If "**true**" or "**false**" is specified, then
the sticky flag is set or cleared, respectively.

**text** \[*string*\]  
Report the text string of all selected labels, or change the text
string of selected labels to *string*.

### Summary:

The **setlabel** command manipulates selected text labels. In versions
of **magic** prior to 8.0, labels could not be manipulated, but could
only be changed by removing and replacing the label. Labels were drawn
in an X11 font that was scaled relative to the window, not the layout.
**setlabel** not only allows text strings to be modified on any
labels, but also allows labels to be drawn in scaled fonts, rotated
and offset to a specific position. Fonts are read from simple,
ASCII-encoded PostScript Type-3 font files, such as provided by the
Freefont project.  

If **-default** is specified, then the given option is set as a
default, if a value is supplied. If no value is supplied, then the
value of the default is returned. The default values are applied when
the "**label** command is issued without the full set of values. The
**-default** option may be used with any label property except for
*text* and *box*.  

The default values, if not changed by using the **-default** option,
are as follows:

**font**  
**default** Fixed-width X11 bitmap font.

**justify**  
**-1** Default justification, automatically determined.

**size**  
**0** Size is determined by the default font.

**offset**  
**0 0** Text is not offset.

**rotate**  
**0** Text is not rotated.

**layer**  
**-1** Default layer type, automatically determined.

**sticky**  
**0** Labels are not sticky by default.

### Implementation Notes:

**setlabel** is implemented as a built-in command in **magic** version
8.0 (or higher) only.

### See Also:

[**label**](#label)  

## setpoint

------------------------------------------------------------------------

Set the value of the cursor reference point in a specific window.

------------------------------------------------------------------------

### Usage:

**setpoint** \[*x y* \[*window\_id*\]  


where *x* and *y* are screen coordinates and *window\_id* is the
identifying number for a layout window.

### Summary:

The **setpoint** command forces the reference point for a specific
window. Each command that executes relative to a window must be able
to translate from the pointer position to a layout coordinate.
Commands that are executed from a script or from the command-line may
not have access to the pointer, but can set the reference point with
this command so that the effect of the command is predictable.

Normally, in interactive this command is not used. However, scripts
that open more than one window need to specify which one is to take
the action of the command. In the Tcl/Tk version, this can be done by
using the *tk\_path\_name* command to pass a command to a specific
window. The non-Tcl/Tk version, and the Tcl/Tk version using the
"-dnull" option on the command line (i.e., no graphics package
initialized) must use the **setpoint** command to track windows.
Although possible, it is generally a bad idea for a script running in
batch mode ("-dnull") to create and access multiple windows, since the
window structures have no useful function outside of a graphics
environment. Nevertheless, it is important to realize that the
**openwindow** command *will* generate multiple virtual windows in a
batch-mode environment, and these can only be separately accessed
using the **setpoint** command.

### Implementation Notes:

**setpoint** is implemented as a built-in window command in **magic**.

### Bugs:

The use of the window ID number is unique to this command and should
be a window name like every other window-related command. Likewise,
scripts would best make use of this command if the position were in
layout coordinates, and **magic** translated them back to screen
coordinates in the indicated window to set the reference point.

## shell

------------------------------------------------------------------------

Execute a command in a UNIX subshell

------------------------------------------------------------------------

### Usage:

**shell** \[*command*\]  


where *command* is a valid UNIX command-line command.

### Summary:

The **shell** command allows UNIX commands to be executed from the
magic command line. This use is superceded by the Tcl interpreter,
which executes shell commands directly from the interpreter prompt.
Differences between the two uses is noted below.

### Implementation Notes:

**shell** is implemented as a built-in command in **magic**. This is
similar to the Tcl interpreter execution of shell commands directly
from the Tcl command-line. The primary difference is that results from
the shell interpreter are printed to the calling terminal with
**shell**, and are printed to the console when invoked directly from
Tcl. For example, note the difference in the output target for:

**ls -l**



*vs.*  
**shell ls -l**

## sideways

------------------------------------------------------------------------

Flip selection and box sideways

------------------------------------------------------------------------

### Shortcuts:

Key macro **f** implements the command **sideways**.

### Usage:

**sideways**  


### Summary:

The **sideways** command flips the selection from left to right.
Flipping is done such that the lower left-hand corner of the selection
remains in the same place through the flip.

### Implementation Notes:

**sideways** is implemented as a built-in command in **magic**.

### See Also:

[**upsidedown**](#upsidedown)  

## sleep

------------------------------------------------------------------------

Sleep for a number of seconds

------------------------------------------------------------------------

### Usage:

**sleep** *seconds*  


where *seconds* is the number of seconds to sleep.

### Summary:

The **sleep** command implements the UNIX system sleep() call to
suspend the process for a number of seconds. This function is only
particularly useful for demonstration purposes. In the Tcl version of
magic, it is effectively superceded by the Tcl **after** command.

### Implementation Notes:

**sleep** is implemented as a built-in command in **magic**.

## snap

------------------------------------------------------------------------

Cause box to snap to the selected grid when moved by the cursor. Also,
cause distance measurements to be interpreted by default as measurments
in the selected grid.

------------------------------------------------------------------------

### Usage:

**snap** \[**internal**|**lambda**|**user**\]  


### Summary:

The **snap** command causes the cursor box to snap to the selected
grid when moved by pointer button events. The selected grids are
**internal**, the size of the internal database, **lambda**, the
lambda grid based on the technology minimum feature size, and
**user**, based on the value given by the user to the **grid**
command.

In addition to changing the behavior of the box to mouse button
events, the **snap** command also changes the way that [distance
measurements](#distance) are interpreted in commands that take
distance arguments, such as **move**, **copy**, and **stretch**. An
integer number with no other identifying units is interpreted as a
measurement in the current snap grid. All other measurements must have
an identifying unit: **i** for internal units, **l** for lambda units,
and **g** for user grid units (as well as the usual metric units).
Even when **snap** is set to the larger lambda or user grids, it is
possible to move the cursor box to finer grid positions from the
command line. See the reference page on [distance
measures](#distance) for a complete description of distance
values.

**snap** with no arguments returns the current snap grid type.

By default, the internal and lambda grids are the same. However, CIF,
GDS, or LEF/DEF input on a finer scale can cause the internal grid to
be set finer than the lambda grid. Also, the **scalegrid** command can
be used to separate the internal and lambda grids. Note that the use
of "lambda" is merely a convention. Traditionally, scalable CMOS rules
were based on units of "lambda", equal to one-half the minimum feature
size of the technology. Many technology files are still based on
lambda rules, which are usually more conservative than vendor rules.
However, some technology files may be based on exactly implementing
vendor rules, and may set the internal grid spacing to a finer
resolution, such as 0.1 micron or smaller. In such cases, the use of
the term "lambda" is a misnomer.

### Implementation Notes:

**snap** is implemented as a built-in command in **magic**.

### See Also:

[**grid**](#grid)  

## specialopen

------------------------------------------------------------------------

Open a window of a specific type.

------------------------------------------------------------------------

### Usage:

**specialopen** *type* \[*arguments*\]  


where *type* may be one of the following:

**layout**  
Open a layout window. Equivalent to the **openwindow** command.

**wind3d** *tk\_path\_name*  
Generate the 3D window. Only available when using OpenGL graphics
("**magic -d OGL**"). The *tk\_path\_name* argument allows the
window to be inserted into a Tk frame instead of generated directly
on the desktop.

**color**  
Open a window allowing layout colors to be edited.

**netlist**  
Open a window allowing interactive definition of netlists.

### Summary:

The **specialopen** command opens one of several special-purpose
windows known to **magic**, as well as the default layout window. Each
window has a set of commands associated with it. The layout window
commands are listed in this reference guide along with the
general-purpose commands, because the layout window is the most common
type. For the command sets of the other special-purpose windows, see
the sections on the colormap, netlist, and 3D rendering.

### Implementation Notes:

**specialopen** is implemented as a built-in window command in
**magic**.

### See Also:

[**openwindow**](#openwindow)  

## spliterase

------------------------------------------------------------------------

Paint into the cursor box, splitting the box diagonally with one layer
forming a right triangle in one corner and space or another layer in the
other.

------------------------------------------------------------------------

### Usage:

**spliterase** *dir layer*  


where *dir* is a valid non-Manhattan direction indicating the
direction of the right angle corner of the right triangle to be
erased. Any paint of layer type *layer* is erased from this
triangular area.

### Summary:

The **spliterase** command implements a form of non-Manhattan geometry
that conforms to the corner-stitched tile database format used by
**magic** for painting and searching operations in a plane. It lets a
rectangular area, as defined by the position of the cursor box, be
split diagonally, with one half containing one layer type, and the
other half containing another. While the **splitpaint** command
generates non-Manhattan areas by adding paint in a triangular area,
**spliterase** creates non-Manhattan areas by subtracting paint from a
triangular area.

Note that **spliterase**, like **splitpaint**, is somewhat cumbersome
to use; to generate diagonal wires, use the **wire segment** command
instead, which is also able to compute mitred joints between segments
at different angles.

### Implementation Notes:

**spliterase** is implemented as a built-in command in **magic**.

### See Also:

[**splitpaint**](#splitpaint)  
[**wire**](#wire)  

## splitpaint

------------------------------------------------------------------------

Paint into the cursor box, splitting the box diagonally with one layer
forming a right triangle in one corner and space or another layer in the
other.

------------------------------------------------------------------------

### Usage:

**splitpaint** *dir layer* \[*layer2*\]  


where *dir* is a valid non-Manhattan direction indicating the
direction of the right angle corner of the right triangle to be
painted. This triangle is painted with layer type *layer*. If
specified, the opposite triangle is painted with layer type
*layer2*; otherwise, it is unpainted.

### Summary:

The **splitpaint** command implements a form of non-Manhattan geometry
that conforms to the corner-stitched tile database format used by
**magic** for painting and searching operations in a plane. It lets a
rectangular area, as defined by the position of the cursor box, be
split diagonally, with one half containing one layer type, and the
other half containing another.

Note that **splitpaint** is somewhat cumbersome to use; to generate
diagonal wires, use the **wire segment** command, which is also able
to compute mitred joints between segments at different angles.

### Implementation Notes:

**splitpaint** is implemented as a built-in command in **magic**.

### See Also:

[**spliterase**](#spliterase)  
[**wire**](#wire)  

## startup

------------------------------------------------------------------------

Start magic from inside the Tcl interpreter.

------------------------------------------------------------------------

### Usage:

**startup**  


### Summary:

The **startup** command is not a user command. It is called by Tcl
packages that wish to use **magic** from the interpreter. The
procedure for starting magic is as follows:

-   Load the tclmagic.so object file.
-   Call **initialize** with arguments passed to **magic** on the
command line.
-   Call **startup**

### Implementation Notes:

**startup** is implemented as a built-in command in **magic**, but
only defined by the Tcl version.

### See Also:

[**initialize**](#initialize)  

## straighten

------------------------------------------------------------------------

Straighten jogs by pulling in direction

------------------------------------------------------------------------

### Usage:

**straighten** *direction*  


where *direction* is any valid Manhattan [direction](#direction)
in **magic**.

### Summary:

The **straighten** command attempts to straighten jogs in wire paths.
It is part of the **plow** method, and helps to clean up areas that
have been altered using the **plow** command.

### Implementation Notes:

**straighten** is implemented as a built-in command in **magic**.

### See Also:

[**plow**](#plow)  

## stretch

------------------------------------------------------------------------

Stretch the cursor box and the selection.

------------------------------------------------------------------------

### Shortcuts:

Key macro **M** implements the command **move** (no arguments).  
Key macro *Shift-Keypad-***8** implements the command **stretch n
1**  
Key macro *Shift-Keypad-***6** implements the command **stretch e
1**  
(and so forth for all 8 compass rose directions).

### Usage:

**stretch** \[*direction* \[*distance*\]\]  


where *direction* is any valid [direction](#direction)
specification in magic, and *distance* is any valid
[distance](#distance) specification.

### Summary:

The **stretch** command moves the current selection from its current
position according to the command arguments, and fills in behind with
material such that electrical connections are maintained across the
area in between the original and final positions.

Without arguments, the lower-left hand corner of the selection is
moved to the current cursor position (the X11 cursor, not the
**magic** "cursor box"). With arguments *direction* and *distance*,
the selection is moved relative to the original in the indicated
direction by the indicated amount. The default distance is 1 unit
(#usually lambda; see [*distance*](#distance) for further
explication).

The stretching algorithm fills in with the material that crosses or
touches the cursor box in the opposite direction to the direction
being stretched. If two different materials are on opposite sides of
this boundary, the effect depends on the material types. Contact types
will not be stretched unless the contact material is on both sides of
the cursor box boundary. If two different contact types are on
opposite sides of the boundary, then the material that electrically
connects those two contacts (if any) will be filled in the stretch
area.

### Implementation Notes:

**stretch** is implemented as a built-in **magic** command.

### See Also:

[*direction*](#direction)  
[*distance*](#distance)  

## suspendall

------------------------------------------------------------------------

Suspend normal display refresh on all windows until the invocation of a
corresponding **resumeall** command.

------------------------------------------------------------------------

### Usage:

**suspendall**  


### Summary:

The **suspendall** command is a script that invokes the command
**update suspend** on all layout windows. It is used in conjunction
with the **resumeall** command and is intended for use in Tcl scripts
that perform multiple manipulations on layout in a window, where it is
desired to have the entire display refresh at one time at the end of
the script rather than for each command within the script.

Because the **update** command can be nested, calls to **suspendall**
and **resumeall** are likewise nested. **resumeall** does not resume
the window refresh until it has been called the same number of times
as **suspendall** was called.

### Implementation Notes:

**suspendall** is implemented as a Tcl procedure in the "tools"
script.

### See Also:

[**resumeall**](#resumeall)  
[**update**](#update)  

## tag

------------------------------------------------------------------------

Register a tag callback command.

------------------------------------------------------------------------

### Usage:

**tag** *command\_name* \[*procedure*\]  


where *command\_name* is the name of any **magic** command, and
*procedure* is any valid Tcl procedure.

### Summary:

The **tag** command is registers callback procedures to be executed
after the indicated **magic** command has been executed. The primary
use of the **tag** command is to register procedures that update the
GUI window in response to commands that are typed on the command line
or generated from macro calls.

In keeping with standard methods for Tcl callback functions, certain
"escape sequences" beginning with the percent ("**%**") character are
allowed to be embedded in the callback function *procedure*, and are
substituted prior to execution, with the substitutions defined as
follows:

**%W**  
Substitute the Tk path of the layout window from which or in
reference to which *command\_name* was invoked.

**%r**  
Substitute the previous Tcl result string, but do not reset the Tcl
result of the execution of *procedure*.

**%R**  
Substitute the previous Tcl result string and reset the Tcl result
from the execution of *procedure* such that the the result of
*command\_name* becomes the result of *procedure*.

**%**\[**0**-**5**\]  
Substitute the zeroth to fifth argument to the original command.

**%%**  
Substitute a single percent character.

**%***char*  
where *char* is any character not defined above: No action, print
exactly as written.

When a tag callback is used, the return value seen by the interpreter
is the return value of the function *procedure*, not the return value
of the tagged command *command\_name*. The escape sequence **%R** can
be used to force the result of *command\_name* to become the result of
*procedure* (unless *procedure* produces an error condition, in which
case the error is returned). The escape sequence *%r* passes the
result of *command\_name* as an argument to the procedure, which may
choose to return it as a result, or not.

If no *procedure* is present, then the **tag** command returns
whatever procedure string is attached to the indicated
*command\_name*, if any. This can be used as a way to prevent infinite
recursion inside a tag callback; for example,

**set savetag \[tag callback** *command***\]**  
*(procedure calls, which may include a call to* command*)*  
**tag** *command* **$savetag**

Another way to avoid infinite recursion is to check the procedure
depth from within the tag callback procedure using the Tcl command
"**info level**", to avoid executing the callback procedure if the
level is not zero.

Only one tag callback is allowed per command name. However, only one
is needed as that procedure may call as many other procedures as it
wants to.

### Implementation Notes:

**tag** is implemented as a built-in command in **magic**, but only in
the Tcl version.

## tech

------------------------------------------------------------------------

Query properties of the current technology, or change the current
technology.

------------------------------------------------------------------------

### Usage:

**tech** *option*  


where *option* may be one of the following:

**load** *filename* \[**-noprompt**\]\[**-nooverride**\]  
Load a new technology from the file *filename*\[.tech\].

**help**  
Display help information

**name**  
Show current technology name

**filename**  
Show current technology filename

**version**  
Show current technology version and description strings

**lambda**  
Show internal units per lambda

**planes**  
Show defined planes

**layers** \[*layer*\]  
Show defined layers

**layers lock**|**unlock** \[*layer*\]  
Lock or unlock layers. When locked, a layer cannot be changed on the
layout. Paint of that layer type cannot be copied, moved, deleted,
or operated upon in any manner that would change the geometry of
that layer. This is useful, for example, to prevent mask layers from
being modified when working on modifications to a process back-end.
Note that layers can be marked locked in a tech file by prefixing
the layer name with "-".

**layers revert**  
Return the set of locked and unlock layers to the state subsequent
to reading the tech file (available from magic version 8.0.183).

**drc** *option*  
Query the DRC ruleset, where *option* is one of the following:

**width** *layer*  
Return the minimum allowed width for the indicated layer type.

**spacing** *layer1* \[*layer2*\]  
Return the minimum allowed spacing between *layer1* and *layer2*, if
*layer2* is specified, or between *layer1* and itself, if not.

### Summary:

The **tech** command queries aspects of the current technology, and
can also be used to change the current technology. The **tech load**
command completely replaces the technology. Normally a call to **tech
load** generates a dialog window asking the user for confirmation,
since the **tech load** command is potentially destructive and can
cause loss of an existing layout. The **-noprompt** option forces a
technology load without presenting a dialog. This is particularly
useful to put a "**tech load** *name* **-noprompt**" command in a
.magic startup file in the directory of a project, so that it is not
necessary to specify the technology on the command line when invoking
**magic**. However, occasionally one may want to run magic from the
same project directory with a different technology. The
**-nooverride** option prevents the **tech load** command from
overriding a technology name entered on the UNIX command line when
starting **magic**.

Technology file reloading is especially useful when developing a
technology file, to immediately see the results of a change made to
the file. The current technology can be reloaded with the simple Tcl
command "**tech load \[tech filename\]**".

Note that there is a slightly different meaning between the command
"**tech layers**" and "**tech layers "\*"**". The former prints a
formatted list of layers, including all aliases for each layer, to the
console. The second returns a Tcl list of all layers, with only the
primary name for each layer.

A few aspects of the technology must be queried from other commands.
The CIF/GDS input and output styles are given by the **cif istyle**
and **cif ostyle** commands, while the extraction style is given by
the **extract style** command.

The **drc** option is intended for use by Tcl scripted procedures that
wish to place layout while satisfying the DRC rules. The two accepted
*rule* options are **spacing** and **width**.

### Implementation Notes:

**tech** is implemented as a built-in command in **magic**. The
command replaces the original **techinfo** command, which no longer
exists.

### Bugs:

**tech drc** may not return the correct value in all cases.

## techmanager

------------------------------------------------------------------------

Generate the technology manager GUI window.

------------------------------------------------------------------------

### Shortcuts:

Menu item *Options-&gt;Technology manager* implements the command
**techmanager**.

### Usage:

**techmanager**  


### Summary:

The **techmanager** command generates the "technology manager" GUI
window (see Figure 1 below). This window shows the current technology
along with its version and description strings shows the internal grid
scaling, the current and available CIF/GDS input and output styles,
and the current and available extraction styles. It also shows the
known technology files by searching the *system* search path (see the
command **path** for more information). It allows a new technology to
be loaded, or the CIF/GDS and extraction styles to be changed, as well
as allowing internal grid rescaling by specifying the internal units
per lambda.

![](graphics/techmgr.gif)  
*Figure 1. The technology manager GUI window.*

### Implementation Notes:

**techmanager** is implemented as a Tcl procedure in the "wrapper"
script.

## command\_name

------------------------------------------------------------------------

Short summary.

------------------------------------------------------------------------

### Shortcuts:

Key macro **k** implements the command **command\_name option**.

### Usage:

**command\_name** *option*  


where *option* may be one of the following:

**option\_1**  

### Summary:

The **command\_name** command is. . .

### Implementation Notes:

**command\_name** is implemented as a built-in command in **magic**.

### See Also:

[**other\_command**](#other_command)  

## *tk\_path\_name*

------------------------------------------------------------------------

Execute a window command in the indicated window.

------------------------------------------------------------------------

### Shortcuts:

Key macro **:** (colon) implements the command *tk\_path\_name* by
prepending the window name to the command typed on the command line
when the command is executed. This action is, however, transparent to
the end user.

### Usage:

*tk\_path\_name command\_name*  


where *command\_name* is any valid window command for the type of
window indicated by *tk\_path\_name*.

### Summary:

The *tk\_path\_name* command is unique for each window that is created
in magic. The name of the window is registered as a command name with
the Tcl interpreter. When the window name is used as a command, the
arguments of the command are passed to the **magic** command
interpreter to be executed in the context of that specific window.
Effectively, it is the same as typing the macro "**:**" (colon) in a
layout window, and then typing the command on the command line.

For example, the default first window that is created in the Tcl GUI
version of magic is **.layout1.magic**. Upon creation, the command
name **.layout1.magic** is registered with the Tcl interpreter.
Subsequently, any command on the command-line will be executed in
relation to that window if it is specified as an option to the
**.layout1.magic** command:

**.layout1.magic box 0 0 10 10**

which is exactly the same as putting the X11 pointer cursor in the
layout window, typing the "**:**" (colon) macro, then typing the
command **box 0 0 10 10** into the command line and hitting the
**return** key.

Similarly to layout windows, windows created with the **specialopen**
command have their Tk path names registered as commands with the Tcl
interpreter, and can be passed commands recognized by the specific
window type (e.g., netlist commands in the netlist special window).

The *tk\_path\_name* commands effectively implement the command
"**send**" as it is used in the non-Tcl-based versions of Magic. For
example, the command "send netlist shownet" can be written, in
Tcl-based Magic, as the following:

**\[windownames netlist\] shownet**

Note here the nested command "**windownames netlist**" that returns
the Tk path name of the netlist window, which is then evaluated as a
command.

### See Also:

[**windownames**](#windownames)

### Implementation Notes:

*tk\_path\_name* is implemented as a built-in command in **magic**
which is registered with the Tcl interpreter when the window is
created and unregistered when the window is destroyed.

## tool

------------------------------------------------------------------------

Change layout tool or print information about what the button bindings
are for the current tool. This page describes the **tool** command as
implemented in the non-Tcl version of magic.

------------------------------------------------------------------------

### Shortcuts:

Key macro *space* implements the command **tool**.  
Key macro *shift-space* implements the command **tool box**.

### Usage:

**tool** \[*name*|**info**\]  


where *name* may be one of **box**, **wiring**, **netlist**, or
**rsim**.

### Summary:

The **tool** command selects or queries the mode of operation of the
mouse buttons in the layout window. Each **tool** type has a unique
set of button bindings.

Without arguments, the **tool** command selects the next tool type in
round-robin fashion. With a tool type as argument, the button bindings
switch to those for the indicated tool. With the **info** option, a
summary of the mouse buttons is given for the current tool.

The mouse bindings for each of the three tools is as follows:

-   *Box Tool*
**left**  
Move the box so its lower-left corner is at cursor position

**right**  
Resize box by moving upper-right corner to cursor position

**middle**  
Paint box area with material underneath cursor

In addition, you can move or resize the box by different corners
by pressing left or right, holding it down, moving the cursor near
a different corner and clicking the other (left or right) button
down then up without releasing the initial button.
-   *Wiring Tool*
**left**  
Pick a wiring layer and width (same as "**wire type**")

**right**  
Add a leg to the wire (same as "**wire leg**")

**middle**  
Place a contact to switch layers (same as "**wire switch**")
-   *Netlist Tool*
**left**  
Select the net containing the terminal nearest the cursor

**right**  
Toggle the terminal nearest the cursor into/out of current net

**middle**  
Join current net and net containing terminal nearest the cursor
-   *Rsim Tool*
**left**  

**right**  

**middle**  

### Implementation Notes:

**tool** is implemented as a built-in command in the non-Tcl version
of **magic**.

### See Also:

[**tool** *(#Tcl version)*](#changetool)

## undo

------------------------------------------------------------------------

Undo commands

------------------------------------------------------------------------

### Shortcuts:

Key macro **U** implements the command **undo**.

### Usage:

**undo** \[**print** \[*count*\]\]  

**undo** **enable**|**disable**  


where *count* indicates a number of events to be undone (default 1
event), and must be a nonzero positive integer.

### Summary:

The **undo** command reverses the effect of the last executed command
(command-line, script, or macro-invoked), returning the layout to the
state it was in prior to execution of that command.

Certain commands in **magic** disable the undo mechanism, thus
preventing the command from being undone. These include layout reads
and writes, CIF, GDS, and LEF/DEF reads and writes.

The **print** option generates a stack trace of the top *count* events
in the undo stack, in excruciating detail.

The **undo disable** option disables the command queue and prevents
all following commands to be undoable until the **undo enable**
command option is given. This can save time and memory for operations
in a batch file where commands will never be able to be undone.

### Implementation Notes:

**undo** is implemented as a built-in window command in **magic**.

### See Also:

[**redo**](#redo)  

## unexpand

------------------------------------------------------------------------

Unexpand everything inside or touching the cursor box.

------------------------------------------------------------------------

### Usage:

**unexpand**  


### Shortcuts:

Key macro **X** implements the command **unexpand**.  

### Summary:

The **unexpand** command unexpands the view of subcells to hide the
contents of the subcells and show the bounding box outline only. The
**unexpand** command unexpands all subcells that touch or intersect
the cursor box in the layout window.

### Implementation Notes:

**unexpand** is implemented as a built-in **magic** command.

### See Also:

[**expand**](#expand)  

## unmeasure

------------------------------------------------------------------------

Remove a ruler generated with the **measure** script.

------------------------------------------------------------------------

### Usage:

**unmeasure**  


### Summary:

The **unmeasure** command is a script that removes a ruler that was
created with the corresponding **measure** command. Any ruler that is
found within the cursor box will be removed.

### Implementation Notes:

**unmeasure** is implemented as a Tcl procedure in the "tools" script.

### See Also:

[**measure**](#measure)  

## updatedisplay

------------------------------------------------------------------------

Force display update, or suspend/resume updates

------------------------------------------------------------------------

### Usage:

**updatedisplay** \[**suspend**|**resume**\]  


### Summary:

The **updatedisplay** command allows the display redraw to be
suspended and resumed. The main situation where this is useful is
inside a script or series of commands, where it is not desired to have
the display refresh at each step. Areas needing to be redrawn will
accumulate and be processed all at once when **updatedisplay resume**
is called.

Calls to **updatedisplay suspend** can be nested, so that the display
will not update until the same number of calls to **updatedisplay
resume** have been encountered.

Without arguments, **updatedisplay** forces an immediate display
redraw.

### Implementation Notes:

**updatedisplay** is implemented as a built-in window command in
**magic**.

### See Also:

[**suspendall**](#suspendall)  
[**resumeall**](#resumeall)  

## upsidedown

------------------------------------------------------------------------

Flip selection and box upside down

------------------------------------------------------------------------

### Shortcuts:

Key macro **F** implements the command **upsidedown**.

### Usage:

**upsidedown**  


### Summary:

The **upsidedown** command flips the selection from top to bottom.
Flipping is done such that the lower left-hand corner of the selection
remains in the same place through the flip.

### Implementation Notes:

**upsidedown** is implemented as a built-in command in **magic**.

### See Also:

[**sideways**](#sideways)  

## version

------------------------------------------------------------------------

Print version and revision info

------------------------------------------------------------------------

### Usage:

**version**  


### Summary:

The **version** command prints the version number and revision number
of **magic**, and the compilation date and time.

### Implementation Notes:

**version** is implemented as a built-in command in **magic**.

## view

------------------------------------------------------------------------

Zoom window out so everything is visible, or zoom window to the
specified area bounds.

------------------------------------------------------------------------

### Shortcuts:

Key macro **v** implements the command **view**.

view \[get|bbox|llx lly urx ury\]

### Usage:

**view** \[**get**|**bbox**|*llx lly urx ury*  


where *llx lly urx ury* are layout dimensions to become the screen
view limits.

### Summary:

The **view** command is most often used without arguments to center
and scale the screen view of the layout window to fit the layout.

**view bbox** returns the bounding box dimensions of the layout, in
the coordinate system of the layout.

**view get** returns the coordinates of the screen limits in the
coordinate system of the layout (internal database units).

**view** *llx lly urx ury* sets the view so that the corners of the
screen are at the indicated positions in the coordinate system of the
layout. Where the dimensions do not match exactly to the screen aspect
ratio, the view will be centered on the indicated coordinates.

### Implementation Notes:

**view** is implemented as a built-in command in **magic**.

## what

------------------------------------------------------------------------

Print out information about what material is in the current selection.
Short summary.

------------------------------------------------------------------------

### Shortcuts:

Key macro **/** (slash) implements the command **what**.

### Usage:

**what** \[**-list**\[**all**\]\]  


### Summary:

The **what** command queries what material is in the current
selection. This includes a report on layers, labels, and subcell
instances that are selected.

In the Tcl version of **magic**, the **-list** option returns the
result as a Tcl list containing three sub-lists. The first sub-list
contains the types found, the second contains the labels found, and
the third contains the subcells found. Each label in the second
sub-list is itself a list of three items: The label text, the layer
the label is attached to, and the cell def containing the label. Each
subcell in the third sub-list is itself a list of two items: The
subcell instance ID name, and the cell definition name.

**-listall** is a variant of the Tcl list, in which the first sub-list
contains the types found, where each entry is itself a list. Each list
entry first item is the name of the layer, and the second entry is a
list containing the names of all subcells where that type is found.

### Implementation Notes:

**what** is implemented as a built-in command in **magic**.

## windowborder

------------------------------------------------------------------------

Toggle border drawing for new windows

------------------------------------------------------------------------

### Usage:

**windowborder** \[**on**|**off**\]  


### Summary:

The **windowborder** command turns the drawing of the window border on
or off. Normally, this will be **on** in the non-GUI version of magic,
and **off** in the GUI version, where the border area is handled by
the Tk frame window. Note that the command does not affect the current
layout windows, but takes effect for all windows created after the
command has been called.

### Implementation Notes:

**windowborder** is implemented as a built-in window command in
**magic**.

## windowcaption

------------------------------------------------------------------------

Toggle title caption for new windows

------------------------------------------------------------------------

### Usage:

**windowcaption** \[**on**|**off**\]  


### Summary:

The **windocaption** command turns the drawing of the window title
area (caption) on or off. Normally, this will be **on** in the non-GUI
version of magic, and **off** in the GUI version, where the title area
is handled by the Tk frame window and the **caption** procedure.

Note that the command does not affect the current layout windows, but
takes effect for all windows created after the command has been
called.

### Implementation Notes:

**windocaption** is implemented as a built-in command in **magic**.

## windownames

------------------------------------------------------------------------

Get name of current or all windows

------------------------------------------------------------------------

### Usage:

**windownames** \[**all**|*type*\]  


where *type* is one of the window types known to the **specialopen**
command, which are: **layout**, **wind3d**, **color**, and
**netlist**.

### Summary:

The **windownames** command returns a list of **magic** windows as
specified by the command options. No options is equivalent to option
**all**, and prints the names of all existing windows. Otherwise,
windows can be listed by *type*, where *type* is the type of window as
understood by the **specialopen** command.

The Tcl/Tk version of magic returns the full Tk path name of each
window, including any parent frames. The non-Tcl/Tk version of magic
returns window IDs (the ID is an integer number used by the
**setpoint** command.

### See Also:

[**setpoint**](#setpoint)  
[*tk\_path\_name*](#tk_path_name)

### Implementation Notes:

**windownames** is implemented as a built-in command in **magic**. The
Tcl version returns a Tcl list of Tk path names for each window. The
non-Tcl version of magic writes the window list to standard output.

## windowscrollbars

------------------------------------------------------------------------

Toggle scroll bars for new windows

------------------------------------------------------------------------

### Usage:

**windowscrollbars** \[**on**|**off**\]  


### Summary:

The **windowscrollbars** command turns the drawing of the window
scrollbars on or off. Normally, this will be **on** in the non-GUI
version of magic, and **off** in the GUI version, where the scrollbars
are handled by the Tk frame window and the GUI "wrapper" script.

Note that the command does not affect the current layout windows, but
takes effect for all windows created after the command has been
called.

### Implementation Notes:

**windowscrollbars** is implemented as a built-in window command in
**magic**.

### See Also:

[*wire*](#wire)  

Magic-7.3 Command Reference

# ![Magic VLSI Layout Tool Version 8.2](graphics/magic_title8_2.png) <img src="graphics/magic_OGL_sm.gif" data-align="top" alt="*" />

## wire

------------------------------------------------------------------------

Generate wires from the command line.

------------------------------------------------------------------------

### Shortcuts:

Mouse buttons in conjunction with the **wire** tool implement various
**wire** commands (see the **tool** command reference).

### Usage:

**wire** *option*  


where *option* may be one of the following:

**help**  
Print help information

**horizontal**  
Add a new horizontal wire leg

**leg**  
Add a new horizontal or vertical leg

**switch** \[*layer width*\]  
Place contact and switch layers

**type** \[*layer width*\]  
Select the type and size of wires

**vertical**  
add a new vertical wire leg

**segment** *layer width x1 y1 x2 y2*... \[**-noendcap**\]  
Paint one or more wire segments

**segment** *layer width filename* \[**-noendcap**\]  
Paint one or more wire segments taken from the text file *filename*
containing two coordinates X and Y per line, one line per path
point.

**show**  
Determine where the next wire leg will be according to the rules for
**wire leg**, but place the result in the selection buffer rather
than directly on the layout.

**increment layer**  
Change the layer type used for wires to the wire type on the plane
above the plane of the current wire type.

**decrement layer**  
Change the layer type used for wires to the wire type on the plane
below the plane of the current wire type.

**increment width**  
Increment the width of the current wire by 1 internal unit.

**decrement width**  
Decrement the width of the current wire by 1 internal unit.

### Summary:

The **wire** command allows quick generation of wires on the layout.
Some of these commands are bound to mouse button events in the wire
tool, making a convenient interface for fast wiring where full netlist
routing is not required. Due to the presence of the wire tool, most of
these commands are not typically called from the command line.

The **wire segment** command can generate non-Manhattan segments. All
other wiring commands generate only Manhattan routes. This command
places wire segments in relation to the *centerline* coordinates
specified by *x1 y1*, *x2 y2*, and so forth. By default, wires are
drawn with an endcap extension of one-half the wire width. The
**-noendcap** option causes the wire to end at the coordinate, with no
extension. The **wire segment** command is intended to be used from
Tcl scripts for automatic layout generation.

The first format for **wire segment** has coordinates specified on the
command line. For wire segments with too many points, this command may
overrun the internal limit on either number of command-line arguments
or the total number of characters in the command line. To work around
these limits, the second format of the command specifies a filename in
place of the coordinate list. The file is a simple text file, with one
line per coordinate pair. X and Y values must be separated by
whitespace. The syntax for each value is the same as for the command;
e.g., one can use integers which will be interpreted relative to the
current snap setting, or one can specify the units, such as "100um".

When generating path points from a script, the most convenient method
is to create an empty list ("{}"), then use "lappend" to add
coordinates to the list. Once the list is complete, it is necessary to
use "eval" to decompose the list.

Incorrect: **wire segment m1 50 $pointlist**  
Correct: **eval "wire segment m1 50 $pointlist"**

### Implementation Notes:

**wire** is implemented as a built-in command in **magic**.

### See Also:

[**polygon**](#polygon)  

## writeall

------------------------------------------------------------------------

Write out all modified cells to disk

------------------------------------------------------------------------

### Shortcuts:

Key macro **w** implements the command **writeall**.  
Key macro **W** implements the command **writeall force**.

### Usage:

**writeall** \[**force**|**modified**|**noupdate** *cell1
cell2...*\]  


### Summary:

The **writeall** command generates a popup dialog prompting for action
on writing each cell definition in the layout hierarchy to disk. As
shown in the figure below, the popup dialog presents five choices:

**write**  
Writes the single cell and continues the prompting for the next cell.

**flush**  
Reverts the cell to what was originally on the disk, like the
**flush** command. Continues prompting for the next cell.

**skip**  
No action for the indicated cell definition; continue prompting for
the next cell.

**abort**  
Stop all writing and terminate the command with no further prompting
or processing.

**autowrite**  
Write all the cells, with no further prompting.

![](graphics/writeall.gif)  
*Figure 1. The popup dialog of the **writeall** command.*

With the option **writeall force**, the command writes all cells in
the hierarchy with no prompting. If one or more cell names follows
**write force**, the cells listed will be written (action "write") and
all other cells will be ignored (action "skip").

With the option **writeall modified**, the command writes all cells in
the hierarchy which have been modified, ignoring those cells marked as
needing only a bounding box or timestamp update.

With the option **writeall noupdate**, the command writes all cells in
the hierarchy like it would for **write force**, but it does not
update timestamps.

### Implementation Notes:

**writeall** is implemented as a built-in command in **magic**.

### See Also:

[**save**](#save)  

## xload

------------------------------------------------------------------------

Load a cell into a window unexpanded

------------------------------------------------------------------------

### Usage:

**xload** *cellname*  


where *cellname* is the name of a layout cell in the database memory
or on disk.

### Summary:

The **xload** command works exactly like the **load** command, but
keeps the top-level cell *cellname* unexpanded. This can be useful for
large layouts where the expanded view takes a long time to redraw.

### Implementation Notes:

**xload** is implemented as a built-in command in **magic**.

### See Also:

[**load**](#load)  
[**xview**](#xview)  

## xor

------------------------------------------------------------------------

Perform exclusive-or between the current cell and the indicated
destination cell. The destination cell is overwritten with the result.

------------------------------------------------------------------------

### Usage:

**xor** \[*option*\] *cellname*  


where *cellname* is the name of a cell definition to be compared
against, and into which the compared geometry will be placed.
*option* may be one of **-nolabels**, **-nosubcircuit**, or
**-novendor**, similar to the "**flatten**" command.

### Summary:

The **xor** command compares the current edit cell against the target
cell *cellname* by flattening and exclusive-or, replacing the target
cell paint as it works. The result is an empty cell if the two cells
have exactly the same geometry; otherwise, paint remains in the target
cell where the geometry of the current edit cell does not match the
geometry of the target cell.

The target cell is assumed to be flattened already. That is, to
compare hierarchical layout *layout1* to hierarchical layout
*layout2*, one would normally do:

load *layout1*  
flatten *dest*  
load *layout2*  
xor *dest*  

This will result in cell *dest* containing geometry mismatches between
cell *layout1* and cell *layout2*.

The options allow selective flattening, as follows:

**-nolabels**  
Prevents magic from copying labels into the flattened cell. Otherwise,
magic flattens labels by prepending the cell hierarchy to each label
as it copies it into the flat cell.

**-nosubcircuit**  
Prevents magic from flattening cells declared to be subcircuits (by
the presence of ports in the cell). These cells are retained as
subcells in the flattened version.

**-novendor**  
Prevents magic from flattening cells that are vendor cells, that is,
cells that are generated by reading GDS using the **gds readonly**
option, or which have the appropriate property values set.

In effect, **xor** is just the command **flatten** called with a
special paint translation table that erases paint in the target when
painted with the same type from the source.

Note that *cellname* is a top-level cell but is not displayed or saved
subsequent to the **xor** command. The usual procedure is to follow
the command "**xor** *cellname*" with "**load** *cellname*", to view
the new compared layout.

Also note that a technology file's paint and erase tables can
interfere with strict XOR function results. Typical paint and erase
rules will tend to generate a result that is useful for a yes-no
answer (cells either match or not), and for finding places in
mismatched cells where differences occur. But it may not be possible
to determine exactly what the difference is from the **xor** output.
For a "proper" XOR function, use a techfile that does not have
interacting types and planes, and draws contact cuts on separate
planes rather than using magic's contact types (which automatically
have interacting paint and erase rules).

### Implementation Notes:

**xor** is implemented as a built-in command in **magic**, available
from magic version 8.1.64.

## xview

------------------------------------------------------------------------

Change the view in the current layout window so that everything is
visible but unexpanded.

------------------------------------------------------------------------

### Usage:

**xview**  


### Summary:

The **xview** command changes the view so that the layout fits the
window, as in the **view** command, but ensures that all cells are
unexpanded. This is useful for large layouts where the full view can
take a long time to refresh.

### Implementation Notes:

**xview** is implemented as a built-in command in **magic**.

### See Also:

[**view**](#view)  
[**xload**](#xload)  

## zoom

------------------------------------------------------------------------

Zoom window by specified magnification factor.

------------------------------------------------------------------------

### Shortcuts:

Key macro **z** implements the command **zoom 0.5** (zoom out by a
factor of 2).  
Key macro **Z** implements the command **zoom 2** (zoom in by a factor
of 2).

### Usage:

**zoom** *factor*  


where *factor* is any real value. Values larger than 1 indicate a
zoom in, while values smaller than 1 indicate a zoom out.

### Summary:

The **zoom** command implements view scaling in the layout window in
and out by the indicated magnification factor.

Note that several other commands effect a change in the view scale
factor, including **findbox zoom** and **view** with coordinate
arguments.

### Implementation Notes:

**zoom** is implemented as a built-in window command in **magic**.

### See Also:

[**center**](#center)  
[**view**](#view)  
[**findbox**](#findbox)  

