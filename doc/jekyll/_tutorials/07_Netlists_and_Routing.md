---
layout: post
title: 07 Netlists and Routing
math: true
---



* TOC
{:toc }

<span class="ptmb7t-x-x-172">Magic Tutorial \#7: Netlists and
Routing</span>  
<span class="ptmri7t-x-x-120">John Ousterhout</span>  
Computer Science Division  
Electrical Engineering and Computer Sciences  
University of California  
Berkeley, CA 94720  
<span class="ptmri7t-x-x-120">(Updated by others, too.)</span>  
This tutorial corresponds to Magic version 7.  

<span class="ptmb7t-x-x-144">Tutorials to read first:</span>

<table class="tabbing" data-cellpadding="0" data-border="0">
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd tabbing" style="vertical-align:baseline;">
<td class="tabbing">Magic Tutorial #1: Getting Started<br />
Magic Tutorial #2: Basic Painting and Selection<br />
Magic Tutorial #3: Advanced Painting (Wiring and Plowing)<br />
Magic Tutorial #4: Cell Hierarchies<br />
Magic Tutorial #5: Multiple Windows<br />
</td>
</tr>
</tbody>
</table>

<span class="ptmb7t-x-x-144">Netlist Commands introduced in this
tutorial:</span>

<table class="tabbing" data-cellpadding="0" data-border="0">
<tbody>
<tr class="odd tabbing" style="vertical-align:baseline;">
<td class="tabbing">:extract, :flush, :ripup, :savenetlist, :trace,
:writeall</td>
</tr>
</tbody>
</table>

<span class="ptmb7t-x-x-144">Layout Commands introduced in this
tutorial:</span>

<table class="tabbing" data-cellpadding="0" data-border="0">
<tbody>
<tr class="odd tabbing" style="vertical-align:baseline;">
<td class="tabbing">:channel, :route</td>
</tr>
</tbody>
</table>

<span class="ptmb7t-x-x-144">Macros introduced in this tutorial:</span>

<table class="tabbing" data-cellpadding="0" data-border="0">
<tbody>
<tr class="odd tabbing" style="vertical-align:baseline;">
<td class="tabbing"><span class="ptmri7t-x-x-120">(none)</span></td>
</tr>
</tbody>
</table>

### <span class="titlemark">1 </span> <span id="x1-10001"></span>Introduction

This tutorial describes how to use Magic’s automatic routing tools to
make interconnections between subcells in a design. In addition to the
standard Magic router, which is invoked by the <span
class="ptmb7t-x-x-120">route</span> command and covered in this
tutorial, two other routing tools are available. A gate-array router
<span class="ptmri7t-x-x-120">Garouter </span>permits user specified
channel definitions, terminals in the interior of cells, and
route-throughs across cells. To learn about the gate-array router read
this first then “Magic Tutorial \#12: Routing Gate Arrays”. Finally
Magic provides an interactive maze-router that takes graphic hints, the
<span class="ptmri7t-x-x-120">Irouter</span>, that permits the user to
control the overall path of routes while leaving the tedious details to
Magic. The <span class="ptmri7t-x-x-120">Irouter </span>is documented in
“Magic Tutorial \#10: The Interactive Router”.

The standard Magic router provides an <span
class="ptmri7t-x-x-120">obstacle-avoidance </span>capability: if there
is mask material in the routing areas, the router can work under, over,
or around that material to complete the connections. This means that you
can pre-route key signals by hand and have Magic route the less
important signals automatically. In addition, you can route power and
ground by hand (right now we don’t have any power-ground routing tools,
so you <span class="ptmri7t-x-x-120">have </span>to route them by hand).

The router <span class="ptmri7t-x-x-120">only </span>makes connections
between subcells; to make point-to-point connections between pieces of
layout within a single cell you should use the wiring command described
in “Magic Tutorial \#3: Advanced Painting (Wiring and Plowing) ” or the
maze router described in “Magic Tutorial \#10: The Interactive Router”.
If you only need to make a few connections you are probably better off
doing them manually.

The first step in routing is to tell Magic what should be connected to
what. This information is contained in a file called a <span
class="ptmri7t-x-x-120">netlist</span>. Sections 2, 3, 4, and 5 describe
how to create and modify netlists using Magic’s interactive netlist
editing tools. Once you’ve created a netlist, the next step is to invoke
the router. Section 6 shows how to do this, and gives a brief summary of
what goes on inside the routing tools. Unless your design is very simple
and has lots of free space, the routing probably won’t succeed the first
time. Section 7 describes the feedback provided by the routing tools.
Sections 8 and 9 discuss how you can modify your design in light of this
feedback to improve its routability. You’ll probably need to iterate a
few times until the routing is successful.

### <span class="titlemark">2 </span> <span id="x1-20002"></span>Terminals and Netlists

A netlist is a file that describes a set of desired connections. It
contains one or more <span class="ptmri7t-x-x-120">nets</span>. Each net
names a set of <span class="ptmri7t-x-x-120">terminals </span>that
should all be wired together. A terminal is simply a label attached to a
piece of mask material within a subcell; it is distinguishable from
ordinary labels within a subcell by its presence within a netlist file
and by certain characteristics common to terminals, as described below.

The first step in building a netlist is to label the terminals in your
design. Figure 1 shows an example. Each label should be a line or
rectangle running along the edge of the cell (point terminals are not
allowed). The router will make a connection to the cell somewhere along
a terminal’s length. If the label isn’t at the edge of the cell, Magic
will route recklessly across the cell to reach the terminal, taking the
shortest path between the terminal and a routing channel. It’s almost
always a good idea to arrange for terminal labels to be at cell edges.
The label must be at least as wide as the minimum width of the routing
material; the wider you make the label, the more flexibility you give
the router to choose a good point to connect to the terminal.

<figure>
<img src="tut70x.png" class="graphics" width="978" height="403"
alt="Figure 1: An example of terminal labels. Each terminal should be labeled with a line or rectangle along the edge of the cell." />
<figcaption aria-hidden="true"><span class="id">Figure 1: </span><span
class="content">An example of terminal labels. Each terminal should be
labeled with a line or rectangle along the edge of the
cell.</span></figcaption>
</figure>

Terminal labels must be attached to mask material that connects directly
to one of Magic’s two routing layers (Routing layers are defined in
Magic’s technology file). For example, in the SCMOS process where the
routing layers are metal1 and metal2, diffusion may not be used as a
terminal since neither of the routing layers will connect directly to
it. On the other hand, a terminal may be attached to diffusion-metal1
contact, since the metal1 routing layer will connect properly to it.
Terminals can have arbitrary names, except that they should not contain
slashes (“/”) or the substring “feedthrough”, and should not end in “@”,
“<span class="ptmr8c-x-x-120">$</span>”, or “̂”. See Tutorial \#2 for a
complete description of labeling conventions.

For an example of good and bad terminals, edit the cell <span
class="ptmb7t-x-x-120">tut7a</span>. The cell doesn’t make any
electrical sense, but contains several good and bad terminals. All the
terminals with names like <span class="ptmb7t-x-x-120">bad1 </span>are
incorrect or undesirable for one of the reasons given above, and those
with names like <span class="ptmb7t-x-x-120">good4 </span>are
acceptable.

<figure>
<img src="tut71x.png" class="graphics" width="1370" height="930"
alt="Figure 2: The netlist menu." />
<figcaption aria-hidden="true"><span class="id">Figure 2: </span><span
class="content">The netlist menu.</span></figcaption>
</figure>

<span id="x1-20031"></span>

<table id="TBL-1" class="tabular" data-rules="groups">
<tbody>
<tr class="odd hline">
<td><hr /></td>
<td><hr /></td>
</tr>
<tr id="TBL-1-1-" class="even" style="vertical-align:baseline;">
<td id="TBL-1-1-1" class="td11"
style="text-align: left; white-space: nowrap;">Button</td>
<td id="TBL-1-1-2" class="td11"
style="text-align: left; white-space: nowrap;">Action</td>
</tr>
<tr class="odd hline">
<td><hr /></td>
<td><hr /></td>
</tr>
<tr id="TBL-1-2-" class="even" style="vertical-align:baseline;">
<td id="TBL-1-2-1" class="td11"
style="text-align: left; white-space: nowrap;">Current Text</td>
<td id="TBL-1-2-2" class="td11"
style="text-align: left; white-space: nowrap;">Left-click: prompt for
more labels</td>
</tr>
<tr id="TBL-1-3-" class="odd" style="vertical-align:baseline;">
<td id="TBL-1-3-1" class="td11"
style="text-align: left; white-space: nowrap;"></td>
<td id="TBL-1-3-2" class="td11"
style="text-align: left; white-space: nowrap;">Right-click: advance to
next label</td>
</tr>
<tr class="even hline">
<td><hr /></td>
<td><hr /></td>
</tr>
<tr id="TBL-1-4-" class="odd" style="vertical-align:baseline;">
<td id="TBL-1-4-1" class="td11"
style="text-align: left; white-space: nowrap;">Placer</td>
<td id="TBL-1-4-2" class="td11"
style="text-align: left; white-space: nowrap;">Left-click: place
label</td>
</tr>
<tr id="TBL-1-5-" class="even" style="vertical-align:baseline;">
<td id="TBL-1-5-1" class="td11"
style="text-align: left; white-space: nowrap;"></td>
<td id="TBL-1-5-2" class="td11"
style="text-align: left; white-space: nowrap;">Right-click: change label
text position</td>
</tr>
<tr class="odd hline">
<td><hr /></td>
<td><hr /></td>
</tr>
<tr id="TBL-1-6-" class="even" style="vertical-align:baseline;">
<td id="TBL-1-6-1" class="td11"
style="text-align: left; white-space: nowrap;">Pumps</td>
<td id="TBL-1-6-2" class="td11"
style="text-align: left; white-space: nowrap;">Left-click: decrement
number</td>
</tr>
<tr id="TBL-1-7-" class="odd" style="vertical-align:baseline;">
<td id="TBL-1-7-1" class="td11"
style="text-align: left; white-space: nowrap;"></td>
<td id="TBL-1-7-2" class="td11"
style="text-align: left; white-space: nowrap;">Right-click: increment
number</td>
</tr>
<tr class="even hline">
<td><hr /></td>
<td><hr /></td>
</tr>
<tr id="TBL-1-8-" class="odd" style="vertical-align:baseline;">
<td id="TBL-1-8-1" class="td11"
style="text-align: left; white-space: nowrap;">Find</td>
<td id="TBL-1-8-2" class="td11"
style="text-align: left; white-space: nowrap;">Search under box,
highlight labels</td>
</tr>
<tr id="TBL-1-9-" class="even" style="vertical-align:baseline;">
<td id="TBL-1-9-1" class="td11"
style="text-align: left; white-space: nowrap;"></td>
<td id="TBL-1-9-2" class="td11"
style="text-align: left; white-space: nowrap;">matching current
text</td>
</tr>
<tr class="odd hline">
<td><hr /></td>
<td><hr /></td>
</tr>
<tr id="TBL-1-10-" class="even" style="vertical-align:baseline;">
<td id="TBL-1-10-1" class="td11"
style="text-align: left; white-space: nowrap;">Current Netlist</td>
<td id="TBL-1-10-2" class="td11"
style="text-align: left; white-space: nowrap;">Left-click: prompt for
new netlist name</td>
</tr>
<tr id="TBL-1-11-" class="odd" style="vertical-align:baseline;">
<td id="TBL-1-11-1" class="td11"
style="text-align: left; white-space: nowrap;"></td>
<td id="TBL-1-11-2" class="td11"
style="text-align: left; white-space: nowrap;">Right-click: use edit
cell name as netlist name</td>
</tr>
<tr class="even hline">
<td><hr /></td>
<td><hr /></td>
</tr>
<tr id="TBL-1-12-" class="odd" style="vertical-align:baseline;">
<td id="TBL-1-12-1" class="td11"
style="text-align: left; white-space: nowrap;">Verify</td>
<td id="TBL-1-12-2" class="td11"
style="text-align: left; white-space: nowrap;">Check that wiring matches
netlist (same as</td>
</tr>
<tr id="TBL-1-13-" class="even" style="vertical-align:baseline;">
<td id="TBL-1-13-1" class="td11"
style="text-align: left; white-space: nowrap;"></td>
<td id="TBL-1-13-2" class="td11"
style="text-align: left; white-space: nowrap;">typing <span
class="ptmb7t-x-x-120">:verify </span>command)</td>
</tr>
<tr class="odd hline">
<td><hr /></td>
<td><hr /></td>
</tr>
<tr id="TBL-1-14-" class="even" style="vertical-align:baseline;">
<td id="TBL-1-14-1" class="td11"
style="text-align: left; white-space: nowrap;">Print</td>
<td id="TBL-1-14-2" class="td11"
style="text-align: left; white-space: nowrap;">Print names of all
terminals in selected net</td>
</tr>
<tr id="TBL-1-15-" class="odd" style="vertical-align:baseline;">
<td id="TBL-1-15-1" class="td11"
style="text-align: left; white-space: nowrap;"></td>
<td id="TBL-1-15-2" class="td11"
style="text-align: left; white-space: nowrap;">(same as typing <span
class="ptmb7t-x-x-120">:print </span>command)</td>
</tr>
<tr class="even hline">
<td><hr /></td>
<td><hr /></td>
</tr>
<tr id="TBL-1-16-" class="odd" style="vertical-align:baseline;">
<td id="TBL-1-16-1" class="td11"
style="text-align: left; white-space: nowrap;">Terms</td>
<td id="TBL-1-16-2" class="td11"
style="text-align: left; white-space: nowrap;">Place feedback areas on
screen to identify all terminals</td>
</tr>
<tr id="TBL-1-17-" class="even" style="vertical-align:baseline;">
<td id="TBL-1-17-1" class="td11"
style="text-align: left; white-space: nowrap;"></td>
<td id="TBL-1-17-2" class="td11"
style="text-align: left; white-space: nowrap;">in current netlist (same
as <span class="ptmb7t-x-x-120">:showterms </span>command)</td>
</tr>
<tr class="odd hline">
<td><hr /></td>
<td><hr /></td>
</tr>
<tr id="TBL-1-18-" class="even" style="vertical-align:baseline;">
<td id="TBL-1-18-1" class="td11"
style="text-align: left; white-space: nowrap;">Cleanup</td>
<td id="TBL-1-18-2" class="td11"
style="text-align: left; white-space: nowrap;">Check current netlist for
missing labels and nets</td>
</tr>
<tr id="TBL-1-19-" class="odd" style="vertical-align:baseline;">
<td id="TBL-1-19-1" class="td11"
style="text-align: left; white-space: nowrap;"></td>
<td id="TBL-1-19-2" class="td11"
style="text-align: left; white-space: nowrap;">with less than two
terminals (same as typing</td>
</tr>
<tr class="even hline">
<td><hr /></td>
<td><hr /></td>
</tr>
<tr id="TBL-1-20-" class="odd" style="vertical-align:baseline;">
<td id="TBL-1-20-1" class="td11"
style="text-align: left; white-space: nowrap;"></td>
<td id="TBL-1-20-2" class="td11"
style="text-align: left; white-space: nowrap;"><span
class="ptmb7t-x-x-120">:cleanup </span>command)</td>
</tr>
<tr id="TBL-1-21-" class="even" style="vertical-align:baseline;">
<td id="TBL-1-21-1" class="td11"
style="text-align: left; white-space: nowrap;">No Net</td>
<td id="TBL-1-21-2" class="td11"
style="text-align: left; white-space: nowrap;">Delete selected net (same
as <span class="ptmb7t-x-x-120">:dnet </span>command)</td>
</tr>
<tr class="odd hline">
<td><hr /></td>
<td><hr /></td>
</tr>
<tr id="TBL-1-22-" class="even" style="vertical-align:baseline;">
<td id="TBL-1-22-1" class="td11"
style="text-align: left; white-space: nowrap;">Show</td>
<td id="TBL-1-22-2" class="td11"
style="text-align: left; white-space: nowrap;">Highlight paint connected
to material under box</td>
</tr>
<tr id="TBL-1-23-" class="odd" style="vertical-align:baseline;">
<td id="TBL-1-23-1" class="td11"
style="text-align: left; white-space: nowrap;"></td>
<td id="TBL-1-23-2" class="td11"
style="text-align: left; white-space: nowrap;">(same as typing <span
class="ptmb7t-x-x-120">:shownet </span>command)</td>
</tr>
<tr class="even hline">
<td><hr /></td>
<td><hr /></td>
</tr>
<tr id="TBL-1-24-" class="odd" style="vertical-align:baseline;">
<td id="TBL-1-24-1" class="td11"
style="text-align: left; white-space: nowrap;"></td>
<td></td>
</tr>
</tbody>
</table>

<span class="id">Table 1: </span><span class="content">A summary of all
the netlist menu button actions.</span>

If you create two or more terminal labels with the same name in the same
cell the router will assume that they are electrically equivalent
(connected together within the cell). Because of this, when routing the
net it will feel free to connect to whichever one of the terminals is
most convenient, and ignore the others. In some cases the router may
take advantage of electrically equivalent terminals by using <span
class="ptmri7t-x-x-120">feed throughs</span>: entering a cell at one
terminal to make one connection, and exiting through an equivalent
terminal on the way to make another connection for the same net.

### <span class="titlemark">3 </span> <span id="x1-30003"></span>Menu for Label Editing

Magic provides a special menu facility to assist you in placing terminal
labels and editing netlists. To make the menu appear, invoke the Magic
command

<table class="tabbing" data-cellpadding="0" data-border="0">
<tbody>
<tr class="odd tabbing" style="vertical-align:baseline;">
<td class="tabbing"><span class="ptmb7t-x-x-120">:specialopen
netlist</span></td>
</tr>
</tbody>
</table>

A new window will appear in the lower-left corner of the screen,
containing several rectangular areas on a purple background. Each of the
rectangular areas is called a <span
class="ptmri7t-x-x-120">button</span>. Clicking mouse buttons inside the
menu buttons will invoke various commands to edit labels and netlists.
Figure 2 shows a diagram of the netlist menu and Table I summarizes the
meaning of button clicks in various menu items. The netlist menu can be
grown, shrunk, and moved just like any other window; see “Magic Tutorial
\#5: Multiple Windows” for details. It also has its own private set of
commands. To see what commands you can type in the netlist menu, move
the cursor over the menu and type

<table class="tabbing" data-cellpadding="0" data-border="0">
<tbody>
<tr class="odd tabbing" style="vertical-align:baseline;">
<td class="tabbing"><span class="ptmb7t-x-x-120">:help</span></td>
</tr>
</tbody>
</table>

You shouldn’t need to type commands in the netlist menu very often,
since almost everything you’ll need to do can be done using the menu.
See Section 9 for a description of a few of the commands you can type;
the complete set is described in the manual page <span
class="ptmri7t-x-x-120">magic(1)</span>. One of the best uses for the
commands is so that you can define macros for them and avoid having to
go back and forth to the menu; look up the <span
class="ptmb7t-x-x-120">:send </span>command in the man page to see how
to do this. The top half of the menu is for placing labels and the
bottom half is for editing netlists. This section describes the label
facilities, and Section 4 describes the netlist facilities.

The label menu makes it easy for you to enter lots of labels,
particularly when there are many labels that are the same except for a
number, e.g. <span class="ptmb7t-x-x-120">bus1</span>, <span
class="ptmb7t-x-x-120">bus2</span>, <span
class="ptmb7t-x-x-120">bus3</span>, etc. There are four sections to the
label menu: the current text, the placer, two pumps, and the <span
class="ptmb7t-x-x-120">Find </span>button. To place labels, first click
the left mouse button over the current text rectangle. Then type one or
more labels on the keyboard, one per line. You can use this mechanism to
enter several labels at once. Type return twice to signal the end of the
list. At this point, the first of the labels you typed will appear in
the current text rectangle.

To place a label, position the box over the area you want to label, then
click the left mouse button inside one of the squares of the placer
area. A label will be created with the current text. Where you click in
the placer determines where the label text will appear relative to the
label box: for example, clicking the left-center square causes the text
to be centered just to the left of the box. You can place many copies of
the same label by moving the box and clicking the placer area again. You
can re-orient the text of a label by clicking the right mouse button
inside the placer area. For example, if you would like to move a label’s
text so that it appears centered above the label, place the box over the
label and right-click the top-center placer square.

If you entered several labels at once, only the first appears in the
current text area. However, you can advance to the next label by
right-clicking inside the current text area. In this way you can place a
long series of labels entirely with the mouse. Try using this mechanism
to add labels to <span class="ptmb7t-x-x-120">tut7a</span>.

The two small buttons underneath the right side of the current text area
are called pumps. To see how these work, enter a label name containing a
number into the current text area, for example, <span
class="ptmb7t-x-x-120">bus1</span>. When you do this, the “1” appears in
the left pump. Right-clicking the pump causes the number to increment,
and left-clicking the pump causes the number to decrement. This makes it
easy for you to enter a series of numbered signal names. If a name has
two numbers in it, the second number will appear in the second pump, and
it can be incremented or decremented too. Try using the pumps to place a
series of numbered names.

The last entry in the label portion of the menu is the <span
class="ptmb7t-x-x-120">Find </span>button. This can be used to locate a
label by searching for a given pattern. If you click the <span
class="ptmb7t-x-x-120">Find </span>button, Magic will use the current
text as a pattern and search the area underneath the box for a label
whose name contains the pattern. Pattern-matching is done in the same
way as in <span class="ptmri7t-x-x-120">csh</span>, using the special
characters “\*”, “?”, “  
”, “\[”, and “\]”. Try this on <span
class="ptmb7t-x-x-120">tut7a</span>: enter “good\*” into the current
text area, place the box around the whole cell, then click on the “Find”
button. For each of the good labels, a feedback area will be created
with white stripes to highlight the area. The <span
class="ptmb7t-x-x-120">:feedback find </span>command can be used to step
through the areas, and <span class="ptmb7t-x-x-120">:feedback clear
</span>will erase the feedback information from the screen. The <span
class="ptmb7t-x-x-120">:feedback </span>command has many of the same
options as <span class="ptmb7t-x-x-120">:drc </span>for getting
information about feedback areas; see the Magic manual page for details,
or type <span class="ptmb7t-x-x-120">:feedback help </span>for a
synopsis of the options.

### <span class="titlemark">4 </span> <span id="x1-40004"></span>Netlist Editing

After placing terminal labels, the next step is to specify the
connections between them; this is called netlist editing. The bottom
half of the netlist menu is used for editing netlists. The first thing
you must do is to specify the netlist you want to edit. Do this by
clicking in the current netlist box. If you left-click, Magic will
prompt you for the netlist name and you can type it at the keyboard. If
you right-click, Magic will use the name of the edit cell as the current
netlist name. In either case, Magic will read the netlist from disk if
it exists and will create a new netlist if there isn’t currently a
netlist file with the given name. Netlist files are stored on disk with
a “.net” extension, which is added by Magic when it reads and writes
files. You can change the current netlist by clicking the current
netlist button again. Startup Magic on the cell <span
class="ptmb7t-x-x-120">tut7b</span>, open the netlist menu, and set the
current netlist to <span class="ptmb7t-x-x-120">tut7b</span>. Then
expand the subcells in <span class="ptmb7t-x-x-120">tut7b </span>so that
you can see their terminals.

<span id="x1-40012"></span>

<table id="TBL-2" class="tabular" data-rules="groups">
<tbody>
<tr class="odd hline">
<td><hr /></td>
<td><hr /></td>
</tr>
<tr id="TBL-2-1-" class="even" style="vertical-align:baseline;">
<td id="TBL-2-1-1" class="td11"
style="text-align: left; white-space: nowrap;">Button</td>
<td id="TBL-2-1-2" class="td11"
style="text-align: left; white-space: nowrap;">Action</td>
</tr>
<tr class="odd hline">
<td><hr /></td>
<td><hr /></td>
</tr>
<tr id="TBL-2-2-" class="even" style="vertical-align:baseline;">
<td id="TBL-2-2-1" class="td11"
style="text-align: left; white-space: nowrap;">Left</td>
<td id="TBL-2-2-2" class="td11"
style="text-align: left; white-space: nowrap;">Select net, using nearest
terminal to cursor.</td>
</tr>
<tr class="odd hline">
<td><hr /></td>
<td><hr /></td>
</tr>
<tr id="TBL-2-3-" class="even" style="vertical-align:baseline;">
<td id="TBL-2-3-1" class="td11"
style="text-align: left; white-space: nowrap;">Right</td>
<td id="TBL-2-3-2" class="td11"
style="text-align: left; white-space: nowrap;">Toggle nearest terminal
into or out of</td>
</tr>
<tr id="TBL-2-4-" class="odd" style="vertical-align:baseline;">
<td id="TBL-2-4-1" class="td11"
style="text-align: left; white-space: nowrap;"></td>
<td id="TBL-2-4-2" class="td11"
style="text-align: left; white-space: nowrap;">current net.</td>
</tr>
<tr class="even hline">
<td><hr /></td>
<td><hr /></td>
</tr>
<tr id="TBL-2-5-" class="odd" style="vertical-align:baseline;">
<td id="TBL-2-5-1" class="td11"
style="text-align: left; white-space: nowrap;">Middle</td>
<td id="TBL-2-5-2" class="td11"
style="text-align: left; white-space: nowrap;">Find nearest terminal,
join its net with the</td>
</tr>
<tr id="TBL-2-6-" class="even" style="vertical-align:baseline;">
<td id="TBL-2-6-1" class="td11"
style="text-align: left; white-space: nowrap;"></td>
<td id="TBL-2-6-2" class="td11"
style="text-align: left; white-space: nowrap;">current net.</td>
</tr>
<tr class="odd hline">
<td><hr /></td>
<td><hr /></td>
</tr>
<tr id="TBL-2-7-" class="even" style="vertical-align:baseline;">
<td id="TBL-2-7-1" class="td11"
style="text-align: left; white-space: nowrap;"></td>
<td></td>
</tr>
</tbody>
</table>

<span class="id">Table 2: </span><span class="content">The actions of
the mouse buttons when the terminal tool is in use.</span>

Netlist editing is done with the netlist tool. If you haven’t already
read “Tutorial \#3: Advanced Painting (Wiring and Plowing)”, you should
read it now, up through Section 2.1. Tutorial \#3 explained how to
change the current tool by using the space macro or by typing <span
class="ptmb7t-x-x-120">:tool</span>. Switch tools to the netlist tool
(the cursor will appear as a thick square).

When the netlist tool is in use the left, right, and middle buttons
invoke select, toggle, and join operations respectively (see Table II).
To see how they work, move the cursor over the terminal <span
class="ptmb7t-x-x-120">right4 </span>in the top subcell of <span
class="ptmb7t-x-x-120">tut7b </span>and click the left mouse button (you
may have to zoom in a bit to see the labels; terminals are numbered in
clockwise order: <span class="ptmb7t-x-x-120">right4 </span>is the
fourth terminal from the top on the right side). This causes the net
containing that terminal to be selected. Three hollow white squares will
appear over the layout, marking the terminals that are supposed to be
wired together into <span class="ptmb7t-x-x-120">right4</span>’s net.
Left-click over the <span class="ptmb7t-x-x-120">left3 </span>terminal
in the same subcell to select its net, then select the <span
class="ptmb7t-x-x-120">right4 </span>net again.

The right button is used to toggle terminals into or out of the current
net. If you right-click over a terminal that is in the current net, then
it is removed from the current net. If you right-click over a terminal
that isn’t in the current net, it is added to the current net. A single
terminal can only be in one net at a time, so if a terminal is already
in a net when you toggle it into another net then Magic will remove it
from the old net. Toggle the terminal <span class="ptmb7t-x-x-120">top4
</span>in the bottom cell out of, then back into, the net containing
<span class="ptmb7t-x-x-120">right4</span>. Now toggle <span
class="ptmb7t-x-x-120">left3 </span>in the bottom cell into this net.
Magic warns you because it had to remove <span
class="ptmb7t-x-x-120">left3 </span>from another net in order to add it
to <span class="ptmb7t-x-x-120">right4</span>’s net. Type <span
class="ptmb7t-x-x-120">u </span>to undo this change, then left-click on
<span class="ptmb7t-x-x-120">left3 </span>to make sure it got restored
to its old net by the undo. All of the netlist-editing operations are
undo-able.

The middle button is used to merge two nets together. If you
middle-click over a terminal, all the terminals in its net are added to
the current net. Play around with the three buttons to edit the netlist
<span class="ptmb7t-x-x-120">tut7b</span>.

Note: the router does not make connections to terminals in the top level
cell. It only works with terminals in subcells, or sub-subcells, etc.
Because of this, the netlist editor does not permit you to select
terminals in the top level cell. If you click over such a terminal Magic
prints an error message and refuses to make the selection.

If you left-click over a terminal that is not currently in a net, Magic
creates a new net automatically. If you didn’t really want to make a new
net, you have several choices. Either you can toggle the terminal out of
its own net, you can undo the select operation, or you can click the
<span class="ptmb7t-x-x-120">No Net </span>button in the netlist menu
(you can do this even while the cursor is in the square shape). The
<span class="ptmb7t-x-x-120">No Net </span>button removes all terminals
from the current net and destroys the net. It’s a bad idea to leave
single-net terminals in the netlist: the router will treat them as
errors.

There are two ways to save netlists on disk; these are similar to the
ways you can save layout cells. If you type

<table class="tabbing" data-cellpadding="0" data-border="0">
<tbody>
<tr class="odd tabbing" style="vertical-align:baseline;">
<td class="tabbing"><span class="ptmb7t-x-x-120">:savenetlist
</span>[<span class="ptmri7t-x-x-120">name</span>]</td>
</tr>
</tbody>
</table>

with the cursor over the netlist menu, the current netlist will be saved
on disk in the file <span class="ptmri7t-x-x-120">name</span>.<span
class="ptmb7t-x-x-120">net</span>. If no <span
class="ptmri7t-x-x-120">name </span>is typed, the name of the current
netlist is used. If you type the command

<table class="tabbing" data-cellpadding="0" data-border="0">
<tbody>
<tr class="odd tabbing" style="vertical-align:baseline;">
<td class="tabbing"><span class="ptmb7t-x-x-120">:writeall</span></td>
</tr>
</tbody>
</table>

then Magic will step through all the netlists that have been modified
since they were last written, asking you if you’d like them to be
written out. If you try to leave Magic without saving all the modified
netlists, Magic will warn you and give you a chance to write them out.

If you make changes to a netlist and then decide you don’t want them,
you can use the <span class="ptmb7t-x-x-120">:flush </span>netlist
command to throw away all of the changes and re-read the netlist from
its disk file. If you create netlists using a text editor or some other
program, you can use <span class="ptmb7t-x-x-120">:flush </span>after
you’ve modified the netlist file in order to make sure that Magic is
using the most up-to-date version.

The <span class="ptmb7t-x-x-120">Print </span>button in the netlist menu
will print out on the text screen the names of all the terminals in the
current net. Try this for some of the nets in <span
class="ptmb7t-x-x-120">tut7b</span>. The official name of a terminal
looks a lot like a Unix file name, consisting of a bunch of fields
separated by slashes. Each field except the last is the id of a subcell,
and the last field is the name of the terminal. These hierarchical names
provide unique names for each terminal, even if the same terminal name
is re-used in different cells or if there are multiple copies of the
same cell.

The <span class="ptmb7t-x-x-120">Verify </span>button will check the
paint of the edit cell to be sure it implements the connections
specified in the current netlist. Feedback areas are created to show
nets that are incomplete or nets that are shorted together.

The <span class="ptmb7t-x-x-120">Terms </span>button will cause Magic to
generate a feedback area over each of the terminals in the current
netlist, so that you can see which terminals are included in the
netlist. If you type the command <span class="ptmb7t-x-x-120">:feedback
clear </span>in a layout window then the feedback will be erased.

The <span class="ptmb7t-x-x-120">Cleanup </span>button is there as a
convenience to help you cleanup your netlists. If you click on it, Magic
will scan through the current netlist to make sure it is reasonable.
<span class="ptmb7t-x-x-120">Cleanup </span>looks for two error
conditions: terminal names that don’t correspond to any labels in the
design, and nets that don’t have at least two terminals. When it finds
either of these conditions it prints a message and gives you the chance
to either delete the offending terminal (if you type <span
class="ptmb7t-x-x-120">dterm</span>), delete the offending net (<span
class="ptmb7t-x-x-120">dnet</span>), skip the current problem without
modifying the netlist and continue looking for other problems (<span
class="ptmb7t-x-x-120">skip</span>), or abort the <span
class="ptmb7t-x-x-120">Cleanup </span>command without making any more
changes (<span class="ptmb7t-x-x-120">abort</span>).

The <span class="ptmb7t-x-x-120">Show </span>button provides an
additional mechanism for displaying the paint in the net. If you place
the box over a piece of paint and click on <span
class="ptmb7t-x-x-120">Show</span>, Magic will highlight all of the
paint in the net under the box. This is similar to pointing at the net
and typing <span class="ptmb7t-x-x-120">s </span>three times to select
the net, except that <span class="ptmb7t-x-x-120">Show </span>doesn’t
select the net (it uses a different mechanism to highlight it), and
<span class="ptmb7t-x-x-120">Show </span>will trace through all cells,
expanded or not (the selection mechanism only considers paint in
expanded cells). Once you’ve used <span class="ptmb7t-x-x-120">Show
</span>to highlight a net, the only way to make the highlighting go away
is to place the box over empty space and invoke <span
class="ptmb7t-x-x-120">Show </span>again. <span
class="ptmb7t-x-x-120">Show </span>is an old command that pre-dates the
selection interface, but we’ve left it in Magic because some people find
it useful.

### <span class="titlemark">5 </span> <span id="x1-50005"></span>Netlist Files

Netlists are stored on disk in ordinary text files. You are welcome to
edit those files by hand or to write programs that generate the netlists
automatically. For example, a netlist might be generated by a schematic
editor or by a high-level simulator. See the manual page <span
class="ptmri7t-x-x-120">net(5) </span>for a description of netlist file
format.

### <span class="titlemark">6 </span> <span id="x1-60006"></span>Running the Router

Once you’ve created a netlist, it is relatively easy to invoke the
router. First, place the box around the area you’d like Magic to
consider for routing. No terminals outside this area will be considered,
and Magic will not generate any paint more than a few units outside this
area (Magic may use the next routing grid line outside the area). Load
<span class="ptmb7t-x-x-120">tut7d</span>, <span
class="ptmb7t-x-x-120">:flush </span>the netlist if you made any changes
to it, set the box to the bounding box of the cell, and then invoke the
router using the command:

<table class="tabbing" data-cellpadding="0" data-border="0">
<tbody>
<tr class="odd tabbing" style="vertical-align:baseline;">
<td class="tabbing"><span class="ptmb7t-x-x-120">:route</span></td>
</tr>
</tbody>
</table>

When the command completes, the netlist should be routed. Click the
<span class="ptmb7t-x-x-120">Verify </span>netlist button to make sure
the connections were made correctly. Try deleting a piece from one of
the wires and verify again. Feedback areas should appear to indicate
where the routing was incorrect. Use the <span
class="ptmb7t-x-x-120">:feedback </span>command to step through the
areas and, eventually, to delete the feedback (<span
class="ptmb7t-x-x-120">:feedback help </span>gives a synopsis of the
command options).

If the router is unable to complete the connections, it will report
errors to you. Errors may be reported in several ways. For some errors,
such as non-existent terminal names, messages will be printed. For other
errors, cross-hatched feedback areas will be created. Most of the
feedback areas have messages similar to “Net shifter/bit\[0\]/phi1:
Can’t make bottom connection.” To see the message associated with a
feedback area, place the box over the feedback area and type <span
class="ptmb7t-x-x-120">:feedback why</span>. In this case the message
means that for some reason the router was unable to connect the
specified net (named by one of its terminals) within one of the routing
channel. The terms “bottom”, “top”, etc. may be misnomers because Magic
sometimes rotates channels before routing: the names refer to the
direction at the time the channel was routed, not the direction in the
circuit. However, the location of the feedback area indicates where the
connection was supposed to have been made.

You’ve probably noticed by now that the router sometimes generates
unnecessary wiring, such as inserting extra jogs and U-shapes in wires
(look next to <span class="ptmb7t-x-x-120">right3 </span>in the top
cell). These jogs are particularly noticeable in small examples.
However, the router actually does <span class="ptmri7t-x-x-120">better
</span>on larger examples: there will still be a bit of extra wire, but
it’s negligible in comparison to the total wire length on a large chip.
Some of this wire is necessary and important: it helps the router to
avoid several problem situations that would cause it to fail on more
difficult examples. However, you can use the <span
class="ptmb7t-x-x-120">straighten </span>command described in “Magic
Tutorial \#3: Advanced Painting (Wiring and Plowing)” to remove
unnecessary jogs. Please don’t judge the router by its behavior on small
examples. On the other hand, if it does awful things on big examples,
we’d like to know about it.

All of the wires placed by the router are of the same width, so the
router won’t be very useful for power and ground wiring.

When using the Magic router, you can wire power and ground by hand
before running the router. The router will be able to work around your
hand-placed connections to make the connections in the netlist. If there
are certain key signals that you want to wire carefully by hand, you can
do this too; the router will work around them. Signals that you route by
hand should not be in the netlist. <span
class="ptmb7t-x-x-120">Tutorial7b </span>has an example of “hand
routing” in the form of a piece of metal in the middle of the circuit.
Undo the routing, and try modifying the metal and/or adding more hand
routing of your own to see how it affects the routing.

The Magic router has a number of options useful for getting information
about the routing and setting routing parameters. You need to invoke the
<span class="ptmb7t-x-x-120">route </span>command once for each option
you want to specify; then type <span class="ptmb7t-x-x-120">:route
</span>with no options to start up the router with whatever parameters
you’ve set. The <span class="ptmb7t-x-x-120">viamin</span>, option which
invokes a routing post-pass is, of course, invoked AFTER routing. Type
<span class="ptmb7t-x-x-120">:route netlist </span><span
class="ptmri7t-x-x-120">file </span>to specify a netlist for the routing
without having to open up the netlist menu. The <span
class="ptmb7t-x-x-120">metal </span>option lets you toggle metal
maximization on and off; if metal maximization is turned on, the router
converts routing from the alternate routing layer (“poly”) to the
preferred routing layer (“metal”) wherever possible. The <span
class="ptmb7t-x-x-120">vias </span>option controls metal maximization by
specifying how many grid units of “metal” conversion make it worthwhile
to place vias; setting this to 5 means that metal maximization will add
extra vias only if 5 or more grid units of “poly” can be converted to
“metal”. View the current technology’s router parameters with the <span
class="ptmb7t-x-x-120">tech </span>option. The <span
class="ptmb7t-x-x-120">jog</span>, <span
class="ptmb7t-x-x-120">obstacle</span>, and <span
class="ptmb7t-x-x-120">steady </span>options let you view and change
parameters to control the channel router (this feature is for advanced
users). The <span class="ptmb7t-x-x-120">viamin </span>option invokes a
via minimization algorithm which reduces the number of vias in a routed
layout. This can be used as a post-processing step to improve the
quality of the routing. This may be useful even when using another
router to do the actual routing. Finally, show all parameter values with
the <span class="ptmb7t-x-x-120">settings </span>option. The options and
their actions are summarized in Table III.

<span id="x1-60013"></span>

<table id="TBL-3" class="tabular" data-rules="groups">
<tbody>
<tr class="odd hline">
<td><hr /></td>
<td><hr /></td>
</tr>
<tr id="TBL-3-1-" class="even" style="vertical-align:baseline;">
<td id="TBL-3-1-1" class="td11"
style="text-align: left; white-space: nowrap;">Option</td>
<td id="TBL-3-1-2" class="td11"
style="text-align: left; white-space: nowrap;">Action</td>
</tr>
<tr class="odd hline">
<td><hr /></td>
<td><hr /></td>
</tr>
<tr id="TBL-3-2-" class="even" style="vertical-align:baseline;">
<td id="TBL-3-2-1" class="td11"
style="text-align: left; white-space: nowrap;"><span
class="ptmb7t-x-x-120">end </span></td>
<td id="TBL-3-2-2" class="td11"
style="text-align: left; white-space: nowrap;">Print the channel router
end constant</td>
</tr>
<tr id="TBL-3-3-" class="odd" style="vertical-align:baseline;">
<td id="TBL-3-3-1" class="td11"
style="text-align: left; white-space: nowrap;"><span
class="ptmb7t-x-x-120">end</span><span class="ptmri7t-x-x-120">real
</span></td>
<td id="TBL-3-3-2" class="td11"
style="text-align: left; white-space: nowrap;">Set the channel router
end constant</td>
</tr>
<tr class="even hline">
<td><hr /></td>
<td><hr /></td>
</tr>
<tr id="TBL-3-4-" class="odd" style="vertical-align:baseline;">
<td id="TBL-3-4-1" class="td11"
style="text-align: left; white-space: nowrap;"><span
class="ptmb7t-x-x-120">help </span></td>
<td id="TBL-3-4-2" class="td11"
style="text-align: left; white-space: nowrap;">Print a summary of the
router options</td>
</tr>
<tr class="even hline">
<td><hr /></td>
<td><hr /></td>
</tr>
<tr id="TBL-3-5-" class="odd" style="vertical-align:baseline;">
<td id="TBL-3-5-1" class="td11"
style="text-align: left; white-space: nowrap;"><span
class="ptmb7t-x-x-120">jog </span></td>
<td id="TBL-3-5-2" class="td11"
style="text-align: left; white-space: nowrap;">Print the channel router
minimum jog length</td>
</tr>
<tr id="TBL-3-6-" class="even" style="vertical-align:baseline;">
<td id="TBL-3-6-1" class="td11"
style="text-align: left; white-space: nowrap;"><span
class="ptmb7t-x-x-120">jog </span><span class="ptmri7t-x-x-120">int
</span></td>
<td id="TBL-3-6-2" class="td11"
style="text-align: left; white-space: nowrap;">Set the minimum jog
length, measured in grid units</td>
</tr>
<tr class="odd hline">
<td><hr /></td>
<td><hr /></td>
</tr>
<tr id="TBL-3-7-" class="even" style="vertical-align:baseline;">
<td id="TBL-3-7-1" class="td11"
style="text-align: left; white-space: nowrap;"><span
class="ptmb7t-x-x-120">metal </span></td>
<td id="TBL-3-7-2" class="td11"
style="text-align: left; white-space: nowrap;">Toggle metal maximization
on or off</td>
</tr>
<tr class="odd hline">
<td><hr /></td>
<td><hr /></td>
</tr>
<tr id="TBL-3-8-" class="even" style="vertical-align:baseline;">
<td id="TBL-3-8-1" class="td11"
style="text-align: left; white-space: nowrap;"><span
class="ptmb7t-x-x-120">netlist </span></td>
<td id="TBL-3-8-2" class="td11"
style="text-align: left; white-space: nowrap;">Print the name of the
current net list</td>
</tr>
<tr id="TBL-3-9-" class="odd" style="vertical-align:baseline;">
<td id="TBL-3-9-1" class="td11"
style="text-align: left; white-space: nowrap;"><span
class="ptmb7t-x-x-120">netlist </span><span class="ptmri7t-x-x-120">file
</span></td>
<td id="TBL-3-9-2" class="td11"
style="text-align: left; white-space: nowrap;">Set the current net
list</td>
</tr>
<tr class="even hline">
<td><hr /></td>
<td><hr /></td>
</tr>
<tr id="TBL-3-10-" class="odd" style="vertical-align:baseline;">
<td id="TBL-3-10-1" class="td11"
style="text-align: left; white-space: nowrap;"><span
class="ptmb7t-x-x-120">obstacle </span></td>
<td id="TBL-3-10-2" class="td11"
style="text-align: left; white-space: nowrap;">Print the channel router
obstacle constant</td>
</tr>
<tr id="TBL-3-11-" class="even" style="vertical-align:baseline;">
<td id="TBL-3-11-1" class="td11"
style="text-align: left; white-space: nowrap;"><span
class="ptmb7t-x-x-120">obstacle </span><span
class="ptmri7t-x-x-120">real</span></td>
<td id="TBL-3-11-2" class="td11"
style="text-align: left; white-space: nowrap;">Set the obstacle
constant</td>
</tr>
<tr class="odd hline">
<td><hr /></td>
<td><hr /></td>
</tr>
<tr id="TBL-3-12-" class="even" style="vertical-align:baseline;">
<td id="TBL-3-12-1" class="td11"
style="text-align: left; white-space: nowrap;"><span
class="ptmb7t-x-x-120">settings </span></td>
<td id="TBL-3-12-2" class="td11"
style="text-align: left; white-space: nowrap;">Print a list of all
router parameters</td>
</tr>
<tr class="odd hline">
<td><hr /></td>
<td><hr /></td>
</tr>
<tr id="TBL-3-13-" class="even" style="vertical-align:baseline;">
<td id="TBL-3-13-1" class="td11"
style="text-align: left; white-space: nowrap;"><span
class="ptmb7t-x-x-120">steady </span></td>
<td id="TBL-3-13-2" class="td11"
style="text-align: left; white-space: nowrap;">Print the channel router
steady net constant</td>
</tr>
<tr id="TBL-3-14-" class="odd" style="vertical-align:baseline;">
<td id="TBL-3-14-1" class="td11"
style="text-align: left; white-space: nowrap;"><span
class="ptmb7t-x-x-120">steady </span><span class="ptmri7t-x-x-120">int
</span></td>
<td id="TBL-3-14-2" class="td11"
style="text-align: left; white-space: nowrap;">Set the steady net
constant, measured in grid units</td>
</tr>
<tr class="even hline">
<td><hr /></td>
<td><hr /></td>
</tr>
<tr id="TBL-3-15-" class="odd" style="vertical-align:baseline;">
<td id="TBL-3-15-1" class="td11"
style="text-align: left; white-space: nowrap;"><span
class="ptmb7t-x-x-120">tech </span></td>
<td id="TBL-3-15-2" class="td11"
style="text-align: left; white-space: nowrap;">Print router technology
information</td>
</tr>
<tr class="even hline">
<td><hr /></td>
<td><hr /></td>
</tr>
<tr id="TBL-3-16-" class="odd" style="vertical-align:baseline;">
<td id="TBL-3-16-1" class="td11"
style="text-align: left; white-space: nowrap;"><span
class="ptmb7t-x-x-120">vias </span></td>
<td id="TBL-3-16-2" class="td11"
style="text-align: left; white-space: nowrap;">Print the metal
maximization via limit</td>
</tr>
<tr id="TBL-3-17-" class="even" style="vertical-align:baseline;">
<td id="TBL-3-17-1" class="td11"
style="text-align: left; white-space: nowrap;"><span
class="ptmb7t-x-x-120">vias </span><span class="ptmri7t-x-x-120">int
</span></td>
<td id="TBL-3-17-2" class="td11"
style="text-align: left; white-space: nowrap;">Set the via limit</td>
</tr>
<tr class="odd hline">
<td><hr /></td>
<td><hr /></td>
</tr>
<tr id="TBL-3-18-" class="even" style="vertical-align:baseline;">
<td id="TBL-3-18-1" class="td11"
style="text-align: left; white-space: nowrap;"><span
class="ptmb7t-x-x-120">viamin </span></td>
<td id="TBL-3-18-2" class="td11"
style="text-align: left; white-space: nowrap;">Minimize vias in a routed
layout.</td>
</tr>
<tr class="odd hline">
<td><hr /></td>
<td><hr /></td>
</tr>
<tr id="TBL-3-19-" class="even" style="vertical-align:baseline;">
<td id="TBL-3-19-1" class="td11"
style="text-align: left; white-space: nowrap;"></td>
<td></td>
</tr>
</tbody>
</table>

<span class="id">Table 3: </span><span class="content">A summary of all
of Magic router options.</span>

### <span class="titlemark">7 </span> <span id="x1-70007"></span>How the Router Works

In order to make the router produce the best possible results, it helps
to know a little bit about how it works. The router runs in three
stages, called <span class="ptmri7t-x-x-120">channel definition</span>,
<span class="ptmri7t-x-x-120">global routing</span>, and <span
class="ptmri7t-x-x-120">channel routing</span>. In the channel
definition phase, Magic divides the area of the edit cell into
rectangular routing areas called channels. The channels cover all the
space under the box except the areas occupied by subcells. All of
Magic’s routing goes in the channel areas, except that stems (Section
8.2) may extend over subcells.

To see the channel structure that Magic chose, place the box in <span
class="ptmb7t-x-x-120">tut7d </span>as if you were going to route, then
type the command

<table class="tabbing" data-cellpadding="0" data-border="0">
<tbody>
<tr class="odd tabbing" style="vertical-align:baseline;">
<td class="tabbing"><span class="ptmb7t-x-x-120">:channel</span></td>
</tr>
</tbody>
</table>

in the layout window. Magic will compute the channel structure and
display it on the screen as a collection of feedback areas. The channel
structure is displayed as white rectangles. Type <span
class="ptmb7t-x-x-120">:feedback clear</span> when you’re through
looking at them.

The second phase of routing is global routing. In the global routing
phase, Magic considers each net in turn and chooses the sequence of
channels the net must pass through in order to connect its terminals.
The <span class="ptmri7t-x-x-120">crossing points </span>(places where
the net crosses from one channel to another) are chosen at this point,
but not the exact path through each channel.

In the third phase, each channel is considered separately. All the nets
passing through that channel are examined at once, and the exact path of
each net is decided. Once the routing paths have been determined, paint
is added to the edit cell to implement the routing.

The router is grid-based: all wires are placed on a uniform grid. For
the standard nMOS process the grid spacing is 7 units, and for the
standard SCMOS process it is 8 units. If you type <span
class="ptmb7t-x-x-120">:grid 8 </span>after routing <span
class="ptmb7t-x-x-120">tut7b</span>, you’ll see that all of the routing
lines up with its lower and left sides on grid lines. Fortunately, you
don’t have to make your cell terminals line up on even grid boundaries.
During the routing Magic generates <span class="ptmri7t-x-x-120">stems
</span>that connect your terminals up to grid lines at the edges of
channels. Notice that there’s space left by Magic between the subcells
and the channels; this space is used by the stem generator.

### <span class="titlemark">8 </span> <span id="x1-80008"></span>What to do When the Router Fails

Don’t be surprised if the router is unable to make all the connections
the first time you try it on a large circuit. Unless you have extra
routing space in your chip, you may have to make slight re-arrangements
to help the router out. The paragraphs below describe things you can do
to make life easier for the router. This section is not very well
developed, so we’d like to hear about techniques you use to improve
routability. If you discover new techniques, send us mail and we’ll add
them to this section.

#### <span class="titlemark">8.1 </span> <span id="x1-90008.1"></span>Channel Structure

One of the first things to check when the router fails is the channel
structure. If using the Magic router, type <span
class="ptmb7t-x-x-120">:channel </span>to look at the channels. One
common mistake is to have some of the desired routing area covered by
subcells; Magic only runs wires where there are no subcells. Check to be
sure that there are channels everywhere that you’re expecting wires to
run. If you place cells too close together, there may not be enough room
to have a channel between the cells; when this happens Magic will route
willy-nilly across the tops of cells to bring terminals out to channels,
and will probably generate shorts or design-rule violations. To solve
the problem, move the cells farther apart. If there are many skinny
channels, it will be difficult for the router to produce good routing.
Try to re-arrange the cell structure to line up edges of nearby cells so
that there are as few channels as possible and they are as large as
possible (before doing this you’ll probably want to get rid of the
existing routing by undo-ing or by flushing the edit cell).

#### <span class="titlemark">8.2 </span> <span id="x1-100008.2"></span>Stems

Another problem has to do with the stem generator. Stems are the pieces
of wiring that connect terminals up to grid points on the edges of
channels. The current stem generation code doesn’t know about
connectivity or design rules. It simply finds the nearest routing grid
point and wires out to that point, without considering any other
terminals. If a terminal is not on the edge of the cell, the stem runs
straight across the cell to the nearest channel, without any
consideration for other material in the cell. If two terminals are too
close together, Magic may decide to route them both to the same grid
point. When this happens, you have two choices. Either you can move the
cell so that the terminals have different nearest grid points (for
example, you can line its terminals up with the grid lines), or if this
doesn’t work you’ll have to modify the cell to make the terminals
farther apart.

The place where stems cause the most trouble is in PLAs, many of which
have been optimized to space the outputs as closely together as
possible. In some cases the outputs are closer together than the routing
grid, which is an impossible situation for the stem generator. In this
case, we think the best approach is to change the PLA templates to space
the outputs farther apart. Either space them exactly the same as the
router grid (in which case you can line the PLAs up before routing so
the terminals are already on the grid), or space the outputs at least
1.5 grid units apart so the stem generator won’t have troubles. Having
tightly-spaced PLA outputs is false economy: it makes it more difficult
to design the PLAs and results in awful routing problems. Even if Magic
could river-route out from tightly-spaced terminals to grid lines (which
it can’t), it would require *N*<sup>2</sup> space to route out *N*
lines; it takes less area to stretch the PLA.

#### <span class="titlemark">8.3 </span> <span id="x1-110008.3"></span>Obstacles

The router tends to have special difficulties with obstacles running
along the edges of channels. When you’ve placed a power wire or other
hand-routing along the edge of a channel, the channel router will often
run material under your wiring in the other routing layer, thereby
blocking both routing layers and making it impossible to complete the
routing. Where this occurs, you can increase the chances of successful
routing by moving the hand-routing away from the channel edges. It’s
especially important to keep hand-routing away from terminals. The stem
generator will not pay any attention to hand-routing when it generates
stems (it just makes a bee-line for the nearest grid point), so it may
accidentally short a terminal to nearby hand-routing.

<figure>
<img src="tut72x.png" class="graphics" width="782" height="782"
alt="Figure 3: When placing hand routing, it is best to place wires with their left and bottom edges along grid lines, and contacts centered on the wires. In this fashion, the hand routing will block as few routing grid lines as possible." />
<figcaption aria-hidden="true"><span class="id">Figure 3: </span><span
class="content">When placing hand routing, it is best to place wires
with their left and bottom edges along grid lines, and contacts centered
on the wires. In this fashion, the hand routing will block as few
routing grid lines as possible.</span></figcaption>
</figure>

When placing hand-routing, you can get better routing results by
following the advice illustrated in Figure 3. First, display the routing
grid. For example, if the router is using a 8-unit grid (which is true
for the standard SCMOS technology), type <span
class="ptmb7t-x-x-120">:grid 8</span>. Then place all your hand routing
with its left and bottom edges along the grid lines. Because of the way
the routing tools work, this approach results in the least possible
amount of lost routing space.

### <span class="titlemark">9 </span> <span id="x1-120009"></span>More Netlist Commands

In addition to the netlist menu buttons and commands described in
Section 4, there are a number of other netlist commands you can invoke
by typing in the netlist window. Many of these commands are textual
equivalents of the menu buttons. However, they allow you to deal with
terminals by typing the hierarchical name of the terminal rather than by
pointing to it. If you don’t know where a terminal is, or if you have
deleted a label from your design so that there’s nothing to point to,
you’ll have to use the textual commands. Commands that don’t just
duplicate menu buttons are described below; see the <span
class="ptmri7t-x-x-120">magic(1)</span> manual page for details on the
others.

The netlist command

<table class="tabbing" data-cellpadding="0" data-border="0">
<tbody>
<tr class="odd tabbing" style="vertical-align:baseline;">
<td class="tabbing"><span class="ptmb7t-x-x-120">:extract</span></td>
</tr>
</tbody>
</table>

will generate a net from existing wiring. It looks under the box for
paint, then traces out all the material in the edit cell that is
connected electrically to that paint. Wherever the material touches
subcells it looks for terminals in the subcells, and all the terminals
it finds are placed into a new net. Warning: there is also an <span
class="ptmb7t-x-x-120">extract </span>command for layout windows, and it
is totally different from the <span class="ptmb7t-x-x-120">extract
</span>command in netlist windows. Make sure you’ve got the cursor over
the netlist window when you invoke this command!

The netlist editor provides two commands for ripping up existing routing
(or other material). They are

<table class="tabbing" data-cellpadding="0" data-border="0">
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd tabbing" style="vertical-align:baseline;">
<td class="tabbing"><span class="ptmb7t-x-x-120">:ripup</span><br />
<span class="ptmb7t-x-x-120">:ripup netlist</span></td>
</tr>
</tbody>
</table>

The first command starts by finding any paint in the edit cell that lies
underneath the box. It then works outward from that paint to find all
paint in the edit cell that is electrically connected to the starting
paint. All of this paint is erased. (<span class="ptmb7t-x-x-120">:ripup
</span>isn’t really necessary, since the same effect can be achieved by
selecting all the paint in the net and deleting the selection; it’s a
hangover from olden days when there was no selection). The second form
of the command, <span class="ptmb7t-x-x-120">:ripup netlist</span>, is
similar to the first except that it starts from each of the terminals in
the current netlist instead of the box. Any paint in the edit cell that
is electrically connected to a terminal is erased. The <span
class="ptmb7t-x-x-120">:ripup netlist </span>command may be useful to
ripup existing routing before rerouting.

The command

<table class="tabbing" data-cellpadding="0" data-border="0">
<tbody>
<tr class="odd tabbing" style="vertical-align:baseline;">
<td class="tabbing"><span class="ptmb7t-x-x-120">:trace </span>[<span
class="ptmri7t-x-x-120">name</span>]</td>
</tr>
</tbody>
</table>

provides an additional facility for examining router feedback. It
highlights all paint connected to each terminal in the net containing
<span class="ptmri7t-x-x-120">name</span>, much as the <span
class="ptmb7t-x-x-120">Show </span>menu button does for paint connected
to anything under the box. The net to be highlighted may be specified by
naming one of its terminals, for example, <span
class="ptmb7t-x-x-120">:trace shifter/bit\[0\]/phi1</span>. Use the
trace command in conjunction with the nets specified in router feedback
to see the partially completed wiring for a net. Where no net is
specified, the <span class="ptmb7t-x-x-120">:trace </span>command
highlights the currently selected net.
