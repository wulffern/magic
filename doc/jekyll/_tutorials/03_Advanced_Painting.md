---
layout: post
title: 03 Advanced Painting
math: true
---



* TOC
{:toc }

<span class="ptmb7t-x-x-172">Magic Tutorial \#3: Advanced Painting
(Wiring and Plowing)</span>  
<span class="ptmri7t-x-x-120">John Ousterhout</span>  
<span class="ptmri7t-x-x-120">Walter Scott</span>  
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
Magic Tutorial #2: Basic Painting and Selection</td>
</tr>
</tbody>
</table>

<span class="ptmb7t-x-x-144">Commands introduced in this
tutorial:</span>

<table class="tabbing" data-cellpadding="0" data-border="0">
<tbody>
<tr class="odd tabbing" style="vertical-align:baseline;">
<td class="tabbing">:array, :corner, :fill, :flush, :plow, :straighten,
:tool, :wire</td>
</tr>
</tbody>
</table>

<span class="ptmb7t-x-x-144">Macros introduced in this tutorial:</span>

<table class="tabbing" data-cellpadding="0" data-border="0">
<tbody>
<tr class="odd tabbing" style="vertical-align:baseline;">
<td class="tabbing"><span class="math inline">&lt;</span>space<span
class="math inline">&gt;</span></td>
</tr>
</tbody>
</table>

## <span class="titlemark">1 </span> <span id="x1-10001"></span>Introduction

Tutorial \#2 showed you the basic facilities for placing paint and
labels, selecting, and manipulating the things that are selected. This
tutorial describes two additional facilities for manipulating paint:
wiring and plowing. These commands aren’t absolutely necessary, since
you can achieve the same effect with the simpler commands of Tutorial
\#2; however, wiring and plowing allow you to perform certain kinds of
manipulations much more quickly than you could otherwise. Wiring is
described in Section 2; it allows you to place wires by pointing at the
ends of legs rather than by positioning the box, and also provides for
convenient contact placement. Plowing is the subject of Section 3. It
allows you to re-arrange pieces of your circuit without having to worry
about design-rule violations being created: plowing automatically moves
things out of the way to avoid trouble.

## <span class="titlemark">2 </span> <span id="x1-20002"></span>Wiring

The box-and-painting paradigm described in Tutorial \#2 is sufficient to
create any possible layout, but it’s relatively inefficient since three
keystrokes are required to paint each new area: two button clicks to
position the box and one more to paint the material. This section
describes a different painting mechanism based on <span
class="ptmri7t-x-x-120">wires</span>. At any given time, there is a
current wiring material and wire thickness. With the wiring interface
you can create a new area of material with a single button click: this
paints a straight-line segment of the current material and width between
the end of the previous wire segment and the cursor location. Each
additional button click adds an additional segment. The wiring interface
also makes it easy for you to place contacts.

## <span class="titlemark">3 </span> <span id="x1-30003"></span>Tools

Before learning about wiring, you’ll need to learn about tools. Until
now, when you’ve pressed mouse buttons in layout windows the buttons
have caused the box to change or material to be painted. The truth is
that buttons can mean different things at different times. The meaning
of the mouse buttons depends on the <span
class="ptmri7t-x-x-120">current tool</span>. Each tool is identified by
a particular cursor shape and a particular interpretation of the mouse
buttons. Initially, the current tool is the box tool; when the box tool
is active the cursor has the shape of a crosshair. To get information
about the current tool, you can type the long command

<table class="tabbing" data-cellpadding="0" data-border="0">
<tbody>
<tr class="odd tabbing" style="vertical-align:baseline;">
<td class="tabbing"><span class="ptmb7t-x-x-120">:tool info</span></td>
</tr>
</tbody>
</table>

This command prints out the name of the current tool and the meaning of
the buttons. Run Magic on the cell <span class="ptmb7t-x-x-120">tut3a
</span>and type <span class="ptmb7t-x-x-120">:tool info</span>.

The <span class="ptmb7t-x-x-120">:tool </span>command can also be used
to switch tools. Try this out by typing the command

<table class="tabbing" data-cellpadding="0" data-border="0">
<tbody>
<tr class="odd tabbing" style="vertical-align:baseline;">
<td class="tabbing"><span class="ptmb7t-x-x-120">:tool</span></td>
</tr>
</tbody>
</table>

Magic will print out a message telling you that you’re using the wiring
tool, and the cursor will change to an arrow shape. Use the <span
class="ptmb7t-x-x-120">:tool info </span>command to see what the buttons
mean now. You’ll be using the wiring tool for most of the rest of this
section. The macro “ ” (space) corresponds to <span
class="ptmb7t-x-x-120">:tool</span>. Try typing the space key a few
times: Magic will cycle circularly through all of the available tools.
There are three tools in Magic right now: the box tool, which you
already know about, the wiring tool, which you’ll learn about in this
tutorial, and the netlist tool, which has a square cursor shape and is
used for netlist editing. “Tutorial \#7: Netlists and Routing” will show
you how to use the netlist tool.

The current tool affects only the meanings of the mouse buttons. It does
not change the meanings of the long commands or macros. This means, for
example, that you can still use all the selection commands while the
wiring tool is active. Switch tools to the wiring tool, point at some
paint in <span class="ptmb7t-x-x-120">tut3a</span>, and type the <span
class="ptmb7t-x-x-120">s </span>macro. A chunk gets selected just as it
does with the box tool.

## <span class="titlemark">4 </span> <span id="x1-40004"></span>Basic Wiring

There are three basic wiring commands: selecting the wiring material,
adding a leg, and adding a contact. This section describes the first two
commands. At this point you should be editing the cell <span
class="ptmb7t-x-x-120">tut3a </span>with the wiring tool active. The
first step in wiring is to pick the material and width to use for wires.
This can be done in two ways. The easiest way is to find a piece of
material of the right type and width, point to it with the cursor, and
click the left mouse button. Try this in <span
class="ptmb7t-x-x-120">tut3a </span>by pointing to the label <span
class="ptmb7t-x-x-120">1 </span>and left-clicking. Magic prints out the
material and width that it chose, selects a square of that material and
width around the cursor, and places the box around the square. Try
pointing to various places in <span class="ptmb7t-x-x-120">tut3a
</span>and left-clicking.

Once you’ve selected the wiring material, the right button paints legs
of a wire. Left-click on label <span class="ptmb7t-x-x-120">1 </span>to
select the red material, then move the cursor over label <span
class="ptmb7t-x-x-120">2 </span>and right-click. This will paint a red
wire between <span class="ptmb7t-x-x-120">1 </span>and <span
class="ptmb7t-x-x-120">2</span>. The new wire leg is selected so that
you can modify it with selection commands, and the box is placed over
the tip of the leg to show you the starting point for the next wire leg.
Add more legs to the wire by right-clicking at <span
class="ptmb7t-x-x-120">3 </span>and then <span
class="ptmb7t-x-x-120">4</span>. Use the mouse buttons to paint another
wire in blue from <span class="ptmb7t-x-x-120">5 </span>to <span
class="ptmb7t-x-x-120">6</span> to <span
class="ptmb7t-x-x-120">7</span>.

Each leg of a wire must be either horizontal or vertical. If you move
the cursor diagonally, Magic will still paint a horizontal or vertical
line (whichever results in the longest new wire leg). To see how this
works, left-click on <span class="ptmb7t-x-x-120">8 </span>in <span
class="ptmb7t-x-x-120">tut3a</span>, then right-click on <span
class="ptmb7t-x-x-120">9</span>. You’ll get a horizontal leg. Now undo
the new leg and right-click on <span class="ptmb7t-x-x-120">10</span>.
This time you’ll get a vertical leg. You can force Magic to paint the
next leg in a particular direction with the commands

<table class="tabbing" data-cellpadding="0" data-border="0">
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd tabbing" style="vertical-align:baseline;">
<td class="tabbing"><span class="ptmb7t-x-x-120">:wire
horizontal</span><br />
<span class="ptmb7t-x-x-120">:wire vertical</span></td>
</tr>
</tbody>
</table>

Try out this feature by left-clicking on <span class="ptmb7t-x-x-120">8
</span>in <span class="ptmb7t-x-x-120">tut3a</span>, moving the cursor
over <span class="ptmb7t-x-x-120">10</span>, and typing <span
class="ptmb7t-x-x-120">:wire ho</span> (abbreviations work for <span
class="ptmb7t-x-x-120">:wire </span>command options just as they do
elsewhere in Magic). This command will generate a short horizontal leg
instead of a longer vertical one.

## <span class="titlemark">5 </span> <span id="x1-50005"></span>Contacts

When the wiring tool is active, the middle mouse button places contacts.
Undo all of your changes to <span class="ptmb7t-x-x-120">tut3a </span>by
typing the command <span class="ptmb7t-x-x-120">:flush </span>and
answering <span class="ptmb7t-x-x-120">yes </span>to the question Magic
asks. This throws away all of the changes made to the cell and re-loads
it from disk. Draw a red wire leg from <span class="ptmb7t-x-x-120">1
</span>to <span class="ptmb7t-x-x-120">2</span>. Now move the cursor
over the blue area and click the middle mouse button. This has several
effects. It places a contact at the end of the current wire leg, selects
the contact, and moves the box over the selection. In addition, it
changes the wiring material and thickness to match the material you
middle-clicked. Move the cursor over <span class="ptmb7t-x-x-120">3
</span>and right-click to paint a blue leg, then make a contact to
purple by middle-clicking over the purple material. Continue by drawing
a purple leg to <span class="ptmb7t-x-x-120">4</span>.

Once you’ve drawn the purple leg to <span
class="ptmb7t-x-x-120">4</span>, move the cursor over red material and
middle-click. This time, Magic prints an error message and treats the
click just like a left-click. Magic only knows how to make contacts
between certain combinations of layers, which are specified in the
technology file (see “Magic Maintainer’s Manual \#2: The Technology
File”). For this technology, Magic doesn’t know how to make contacts
directly between purple and red.

## <span class="titlemark">6 </span> <span id="x1-60006"></span>Wiring and the Box

In the examples so far, each new wire leg appeared to be drawn from the
end of the previous leg to the cursor position. In fact, however, the
new material was drawn from the <span class="ptmri7t-x-x-120">box
</span>to the cursor position. Magic automatically repositions the box
on each button click to help set things up for the next leg. Using the
box as the starting point for wire legs makes it easy to start wires in
places that don’t already have material of the right type and width.
Suppose that you want to start a new wire in the middle of an empty
area. You can’t left-click to get the wire started there. Instead, you
can left-click some other place where there’s the right material for the
wire, type the space bar twice to get back the box tool, move the box
where you’d like the wire to start, hit the space bar once more to get
back the wiring tool, and then right-click to paint the wire. Try this
out on <span class="ptmb7t-x-x-120">tut3a</span>.

When you first start wiring, you may not be able to find the right kind
of material anywhere on the screen. When this happens, you can select
the wiring material and width with the command

<table class="tabbing" data-cellpadding="0" data-border="0">
<tbody>
<tr class="odd tabbing" style="vertical-align:baseline;">
<td class="tabbing"><span class="ptmb7t-x-x-120">:wire type </span><span
class="ptmri7t-x-x-120">layer width</span></td>
</tr>
</tbody>
</table>

Then move the box where you’d like the wire to start, switch to the
wiring tool, and right-click to add legs.

## <span class="titlemark">7 </span> <span id="x1-70007"></span>Wiring and the Selection

Each time you paint a new wire leg or contact using the wiring commands,
Magic selects the new material just as if you had placed the cursor over
it and typed <span class="ptmb7t-x-x-120">s</span>. This makes it easy
for you to adjust its position if you didn’t get it right initially. The
<span class="ptmb7t-x-x-120">:stretch </span>command is particularly
useful for this. In <span class="ptmb7t-x-x-120">tut3a</span>, paint a
wire leg in blue from <span class="ptmb7t-x-x-120">5 </span>to <span
class="ptmb7t-x-x-120">6 </span>(use <span class="ptmb7t-x-x-120">:flush
</span>to reset the cell if you’ve made a lot of changes). Now type
<span class="ptmb7t-x-x-120">R </span>two or three times to stretch the
leg over to the right. Middle-click over purple material, then use <span
class="ptmb7t-x-x-120">W </span>to stretch the contact downward.

It’s often hard to position the cursor so that a wire leg comes out
right the first time, but it’s usually easy to tell whether the leg is
right once it’s painted. If it’s wrong, then you can use the stretching
commands to shift it over one unit at a time until it’s correct.

## <span class="titlemark">8 </span> <span id="x1-80008"></span>Bundles of Wires

Magic provides two additional commands that are useful for running <span
class="ptmri7t-x-x-120">bundles </span>of parallel wires. The commands
are:

<table class="tabbing" data-cellpadding="0" data-border="0">
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd tabbing" style="vertical-align:baseline;">
<td class="tabbing"><span class="ptmb7t-x-x-120">fill </span><span
class="ptmri7t-x-x-120">direction </span>[<span
class="ptmri7t-x-x-120">layers</span>]<br />
<span class="ptmb7t-x-x-120">corner </span><span
class="ptmri7t-x-x-120">direction1 direction2 </span>[<span
class="ptmri7t-x-x-120">layers</span>]</td>
</tr>
</tbody>
</table>

To see how they work, load the cell <span
class="ptmb7t-x-x-120">tut3b</span>. The <span
class="ptmb7t-x-x-120">:fill </span>comand extends a whole bunch of
paint in a given direction. It finds all paint touching one side of the
box and extends that paint to the opposite side of the box. For example,
<span class="ptmb7t-x-x-120">:fill left </span>will look underneath the
right edge of the box for paint, and will extend that paint to the left
side of the box. The effect is just as if all the colors visible
underneath that edge of the box constituted a paint brush; Magic sweeps
the brush across the box in the given direction. Place the box over the
label “Fill here” in <span class="ptmb7t-x-x-120">tut3b </span>and type
<span class="ptmb7t-x-x-120">:fill</span> <span
class="ptmb7t-x-x-120">left</span>.

The <span class="ptmb7t-x-x-120">:corner </span>command is similar to
<span class="ptmb7t-x-x-120">:fill </span>except that it generates
L-shaped wires that follow two sides of the box, travelling first in
<span class="ptmri7t-x-x-120">direction1 </span>and then in <span
class="ptmri7t-x-x-120">direction2</span>. Place the box over the label
“Corner here” in <span class="ptmb7t-x-x-120">tut3b </span>and type
<span class="ptmb7t-x-x-120">:corner right up</span>.

In both <span class="ptmb7t-x-x-120">:fill </span>and <span
class="ptmb7t-x-x-120">:corner</span>, if <span
class="ptmri7t-x-x-120">layers </span>isn’t specified then all layers
are filled. If <span class="ptmri7t-x-x-120">layers </span>is given then
only those layers are painted. Experiment on <span
class="ptmb7t-x-x-120">tut3b </span>with the <span
class="ptmb7t-x-x-120">:fill </span>and <span
class="ptmb7t-x-x-120">:corner </span>commands.

When you’re painting bundles of wires, it would be nice if there were a
convenient way to place contacts across the whole bundle in order to
switch to a different layer. There’s no single command to do this, but
you can place one contact by hand and then use the <span
class="ptmb7t-x-x-120">:array </span>command to replicate a single
contact across the whole bundle. Load the cell <span
class="ptmb7t-x-x-120">tut3c</span>. This contains a bundle of wires
with a single contact already painted by hand on the bottom wire. Type
<span class="ptmb7t-x-x-120">s </span>with the cursor over the contact,
and type <span class="ptmb7t-x-x-120">S </span>with the cursor over the
stub of purple wiring material next to it. Now place the box over the
label “Array” and type the command <span class="ptmb7t-x-x-120">:array 1
10</span>. This will copy the selected contact across the whole bundle.

The syntax of the <span class="ptmb7t-x-x-120">:array </span>command is

<table class="tabbing" data-cellpadding="0" data-border="0">
<tbody>
<tr class="odd tabbing" style="vertical-align:baseline;">
<td class="tabbing"><span class="ptmb7t-x-x-120">:array </span><span
class="ptmri7t-x-x-120">xsize ysize</span></td>
</tr>
</tbody>
</table>

This command makes the selection into an array of identical elements.
<span class="ptmri7t-x-x-120">Xsize </span>specifies how many total
instances there should be in the x-direction when the command is
finished and <span class="ptmri7t-x-x-120">ysize </span>specifies how
many total instances there should be in the y-direction. In the <span
class="ptmb7t-x-x-120">tut3c </span>example, <span
class="ptmb7t-x-x-120">xsize </span>was one, so no additional copies
were created in that direction; <span class="ptmb7t-x-x-120">ysize
</span>was 10, so 9 additional copies were created. The box is used to
determine how far apart the elements should be: the width of the box
determines the x-spacing and the height determines the y-spacing. The
new material always appears above and to the right of the original copy.

In <span class="ptmb7t-x-x-120">tut3c</span>, use <span
class="ptmb7t-x-x-120">:corner </span>to extend the purple wires and
turn them up. Then paint a contact back to blue on the leftmost wire,
add a stub of blue paint above it, and use <span
class="ptmb7t-x-x-120">:array </span>to copy them across the top of the
bundle. Finally, use <span class="ptmb7t-x-x-120">:fill </span>again to
extend the blue bundle farther up.

## <span class="titlemark">9 </span> <span id="x1-90009"></span>Plowing

Magic contains a facility called <span class="ptmri7t-x-x-120">plowing
</span>that you can use to stretch and compact cells. The basic plowing
command has the syntax

<table class="tabbing" data-cellpadding="0" data-border="0">
<tbody>
<tr class="odd tabbing" style="vertical-align:baseline;">
<td class="tabbing"><span class="ptmb7t-x-x-120">:plow </span><span
class="ptmri7t-x-x-120">direction </span>[<span
class="ptmri7t-x-x-120">layers</span>]</td>
</tr>
</tbody>
</table>

where <span class="ptmri7t-x-x-120">direction </span>is a Manhattan
direction like <span class="ptmb7t-x-x-120">left </span>and <span
class="ptmri7t-x-x-120">layers </span>is an optional, comma-separated
list of mask layers. The plow command treats one side of the box as if
it were a plow, and shoves the plow over to the other side of the box.
For example, <span class="ptmb7t-x-x-120">:plow up </span>treats the
bottom side of the box as a plow, and moves the plow to the top of the
box.

As the plow moves, every edge in its path is pushed ahead of it (if
<span class="ptmri7t-x-x-120">layers </span>is specified, then only
edges on those layers are moved). Each edge that is pushed by the plow
pushes other edges ahead of it in a way that preserves design rules,
connectivity, and transistor and contact sizes. This means that material
ahead of the plow gets compacted down to the minimum spacing permitted
by the design rules, and material that crossed the plow’s original
position gets stretched behind the plow.

You can compact a cell by placing a large plow off to one side of the
cell and plowing across the whole cell. You can open up space in the
middle of a cell by dragging a small plow across the area where you want
more space.

To try out plowing, edit the cell <span
class="ptmb7t-x-x-120">tut3d</span>, place the box over the rectangle
that’s labelled “Plow here”, and try plowing in various directions.
Also, try plowing only certain layers. For example, with the box over
the “Plow here” label, try

<table class="tabbing" data-cellpadding="0" data-border="0">
<tbody>
<tr class="odd tabbing" style="vertical-align:baseline;">
<td class="tabbing"><span class="ptmb7t-x-x-120">:plow right
metal2</span></td>
</tr>
</tbody>
</table>

Nothing happens. This is because there are no metal2 <span
class="ptmri7t-x-x-120">edges </span>in the path of the plow. If instead
you had typed

<table class="tabbing" data-cellpadding="0" data-border="0">
<tbody>
<tr class="odd tabbing" style="vertical-align:baseline;">
<td class="tabbing"><span class="ptmb7t-x-x-120">:plow right
metal1</span></td>
</tr>
</tbody>
</table>

only the metal would have been plowed to the right.

In addition to plowing with the box, you can plow the selection. The
command to do this has the following syntax:

<table class="tabbing" data-cellpadding="0" data-border="0">
<tbody>
<tr class="odd tabbing" style="vertical-align:baseline;">
<td class="tabbing"><span class="ptmb7t-x-x-120">:plow selection
</span>[<span class="ptmri7t-x-x-120">direction </span>[<span
class="ptmri7t-x-x-120">distance</span>]]</td>
</tr>
</tbody>
</table>

This is very similar to the <span class="ptmb7t-x-x-120">:stretch
</span>command: it picks up the selection and the box and moves both so
that the lower-left corner of the box is at the cursor location. Unlike
the <span class="ptmb7t-x-x-120">:stretch</span> command, though, <span
class="ptmb7t-x-x-120">:plow selection </span>insures that design rule
correctness and connectivity are preserved.

Load the cell <span class="ptmb7t-x-x-120">tut3e </span>and use <span
class="ptmb7t-x-x-120">a </span>to select the area underneath the label
that says “select me”. Then point with the cursor to the point labelled
“point here” and type <span class="ptmb7t-x-x-120">:plow
selection</span>. Practice selecting things and plowing them. Like the
<span class="ptmb7t-x-x-120">:stretch </span>command, there is also a
longer form of <span class="ptmb7t-x-x-120">:plow</span> <span
class="ptmb7t-x-x-120">selection</span>. For example, <span
class="ptmb7t-x-x-120">:plow selection down 5 </span>will plow the
selection and the box down 10 units.

Selecting a cell and plowing it is a good way to move the cell. Load
<span class="ptmb7t-x-x-120">tut3f </span>and select the cell <span
class="ptmb7t-x-x-120">tut3e</span>. Point to the label “point here” and
plow the selection with <span class="ptmb7t-x-x-120">:plow
selection</span>. Notice that all connections to the cell have remained
attached. The cell you select must be in the edit cell, however.

The plowing operation is implemented in a way that tries to keep your
design as compact as possible. To do this, it inserts jogs in wires
around the plow. In many cases, though, the additional jogs are more
trouble than they’re worth. To reduce the number of jogs inserted by
plowing, type the command

<table class="tabbing" data-cellpadding="0" data-border="0">
<tbody>
<tr class="odd tabbing" style="vertical-align:baseline;">
<td class="tabbing"><span class="ptmb7t-x-x-120">:plow
nojogs</span></td>
</tr>
</tbody>
</table>

From now on, Magic will insert as few jogs as possible when plowing,
even if this means moving more material. You can re-enable jog insertion
with the command

<table class="tabbing" data-cellpadding="0" data-border="0">
<tbody>
<tr class="odd tabbing" style="vertical-align:baseline;">
<td class="tabbing"><span class="ptmb7t-x-x-120">:plow jogs</span></td>
</tr>
</tbody>
</table>

Load the cell <span class="ptmb7t-x-x-120">tut3d </span>again and try
plowing it both with and without jog insertion.

There is another way to reduce the number of jogs introduced by plowing.
Instead of avoiding jogs in the first place, plowing can introduce them
freely but clean them up as much as possible afterward. This results in
more dense layouts, but possibly more jogs than if you had enabled <span
class="ptmb7t-x-x-120">:plow nojogs</span>. To take advantage of this
second method for jog reduction, re-enable jog insertion (<span
class="ptmb7t-x-x-120">:plow jogs</span>) and enable jog cleanup with
the command

<table class="tabbing" data-cellpadding="0" data-border="0">
<tbody>
<tr class="odd tabbing" style="vertical-align:baseline;">
<td class="tabbing"><span class="ptmb7t-x-x-120">:plow
straighten</span></td>
</tr>
</tbody>
</table>

From now on, Magic will attempt to straighten out jogs after each plow
operation. To disable straightening, use the command

<table class="tabbing" data-cellpadding="0" data-border="0">
<tbody>
<tr class="odd tabbing" style="vertical-align:baseline;">
<td class="tabbing"><span class="ptmb7t-x-x-120">:plow
nostraighten</span></td>
</tr>
</tbody>
</table>

It might seem pointless to disable jog introduction with <span
class="ptmb7t-x-x-120">:plow nojogs </span>at the same time
straightening is enabled with <span class="ptmb7t-x-x-120">:plow
straighten</span>. While it is true that <span
class="ptmb7t-x-x-120">:plow nojogs </span>won’t introduce any new jogs
for <span class="ptmb7t-x-x-120">:plow straighten </span>to clean up,
plowing will straighten out any existing jogs after each operation.

In fact, there is a separate command that is sometimes useful for
cleaning up layouts with many jogs, namely the command

<table class="tabbing" data-cellpadding="0" data-border="0">
<tbody>
<tr class="odd tabbing" style="vertical-align:baseline;">
<td class="tabbing"><span class="ptmb7t-x-x-120">:straighten
</span><span class="ptmri7t-x-x-120">direction</span></td>
</tr>
</tbody>
</table>

where <span class="ptmri7t-x-x-120">direction </span>is a Manhattan
direction, e.g., <span class="ptmb7t-x-x-120">up</span>, <span
class="ptmb7t-x-x-120">down</span>, <span
class="ptmb7t-x-x-120">right</span>, or <span
class="ptmb7t-x-x-120">left</span>. This command will start from one
side of the box and pull jogs toward that side to straighten them. Load
the cell <span class="ptmb7t-x-x-120">tut3g</span>, place the box over
the label “put box here”, and type <span
class="ptmb7t-x-x-120">:straighten left</span>. Undo the last command
and type <span class="ptmb7t-x-x-120">:straighten</span> <span
class="ptmb7t-x-x-120">right </span>instead. Play around with the <span
class="ptmb7t-x-x-120">:straighten </span>command.

There is one more feature of plowing that is sometimes useful. If you
are working on a large cell and want to make sure that plowing never
affects any geometry outside of a certain area, you can place a <span
class="ptmri7t-x-x-120">boundary </span>around the area you want to
affect with the command

<table class="tabbing" data-cellpadding="0" data-border="0">
<tbody>
<tr class="odd tabbing" style="vertical-align:baseline;">
<td class="tabbing"><span class="ptmb7t-x-x-120">:plow
boundary</span></td>
</tr>
</tbody>
</table>

The box is used to specify the area you want to affect. After this
command, subsequent plows will only affect the area inside this
boundary.

Load the cell <span class="ptmb7t-x-x-120">tut3h </span>place the box
over the label “put boundary here”, and type <span
class="ptmb7t-x-x-120">:plow</span> <span
class="ptmb7t-x-x-120">boundary</span>. Now move the box away. You will
see the boundary highlighted with dotted lines. Now place the box over
the area labelled “put plow here” and plow up. This plow would cause
geometry outside of the boundary to be affected, so Magic reduces the
plow distance enough to prevent this and warns you of this fact. Now
undo the last plow and remove the boundary with

<table class="tabbing" data-cellpadding="0" data-border="0">
<tbody>
<tr class="odd tabbing" style="vertical-align:baseline;">
<td class="tabbing"><span class="ptmb7t-x-x-120">:plow
noboundary</span></td>
</tr>
</tbody>
</table>

Put the box over the “put plow here” label and plow up again. This time
there was no boundary to stop the plow, so everything was moved as far
as the height of the box. Experiment with placing the boundary around an
area of this cell and plowing.
