---
layout: post
title: tut8
math: true
---



* TOC
{:toc }

<span class="ptmb7t-x-x-172">Magic Tutorial \#8: Circuit
Extraction</span>  
<span class="ptmri7t-x-x-120">Walter Scott</span>  
Special Studies Program  
Lawrence Livermore National Laboratory  
P.O. Box 808, L-270  
Livermore, CA 94550  
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
Magic Tutorial #4: Cell Hierarchies</td>
</tr>
</tbody>
</table>

<span class="ptmb7t-x-x-144">Commands introduced in this
tutorial:</span>

<table class="tabbing" data-cellpadding="0" data-border="0">
<tbody>
<tr class="odd tabbing" style="vertical-align:baseline;">
<td class="tabbing">:extract</td>
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

<span class="ptmb7t-x-x-120">Changes since Magic version 4:</span>

<table class="tabbing" data-cellpadding="0" data-border="0">
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd tabbing" style="vertical-align:baseline;">
<td class="tabbing">New form of <span class="ptmb7t-x-x-120">:extract
unique</span><br />
Path length extraction with <span class="ptmb7t-x-x-120">:extract
length</span><br />
Accurate resistance extraction with <span
class="ptmb7t-x-x-120">:extresis</span><br />
Extraction of well connectivity and substrate nodes<br />
Checking for global net connectedness in <span
class="ptmri7t-x-x-120">ext2sim</span> (1)<br />
New programs: <span class="ptmri7t-x-x-120">ext2spice</span> (1) and
<span class="ptmri7t-x-x-120">extcheck</span> (1)<br />
</td>
</tr>
</tbody>
</table>

### <span class="titlemark">1 </span> <span id="x1-10001"></span>Introduction

This tutorial covers the use of Magic’s circuit extractor. The extractor
computes from the layout the information needed to run simulation tools
such as <span class="ptmri7t-x-x-120">crystal</span> (1) and <span
class="ptmri7t-x-x-120">esim</span> (1). This information includes the
sizes and shapes of transistors, and the connectivity, resistance, and
parasitic capacitance of nodes. Both capacitance to substrate and
several kinds of internodal coupling capacitances are extracted.

Magic’s extractor is both incremental and hierarchical: only part of the
entire layout must be re-extracted after each change, and the structure
of the extracted circuit parallels the structure of the layout being
extracted. The extractor produces a separate <span
class="ptmb7t-x-x-120">.ext </span>file for each <span
class="ptmb7t-x-x-120">.mag </span>file in a hierarchical design. This
is in contrast to previous extractors, such as Mextra, which produces a
single <span class="ptmb7t-x-x-120">.sim </span>file that represents the
flattened (fully-instantiated) layout.

Sections 2 through 4 introduce Magic’s <span
class="ptmb7t-x-x-120">:extract </span>command and some of its more
advanced features. Section 5 describes what information actually gets
extracted, and discusses limitations and inaccuracies. Section 6 talks
about extraction styles. Although the hierarchical <span
class="ptmri7t-x-x-120">ext</span> (5) format fully describes the
circuit implemented by a layout, very few tools currently accept it. It
is normally necessary to flatten the extracted circuit using one of the
programs discussed in Section 7, such as <span
class="ptmri7t-x-x-120">ext2sim</span> (1), <span
class="ptmri7t-x-x-120">ext2spice</span> (1), or <span
class="ptmri7t-x-x-120">extcheck</span> (1).

### <span class="titlemark">2 </span> <span id="x1-20002"></span>Basic Extraction

You can use Magic’s extractor in one of several ways. Normally it is not
necessary to extract all cells in a layout. To extract only those cells
that have changed since they were extracted, use:

<table class="tabbing" data-cellpadding="0" data-border="0">
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd tabbing" style="vertical-align:baseline;">
<td class="tabbing"><span class="ptmb7t-x-x-120">:load </span><span
class="ptmri7t-x-x-120">root</span><br />
<span class="ptmb7t-x-x-120">:extract</span></td>
</tr>
</tbody>
</table>

The extractor looks for a <span class="ptmb7t-x-x-120">.ext </span>file
for every cell in the tree that descends from the cell <span
class="ptmri7t-x-x-120">root</span>. The <span
class="ptmb7t-x-x-120">.ext </span>file is searched for in the same
directory that contains the cell’s <span class="ptmb7t-x-x-120">.mag
</span>file. Any cells that have been modified since they were last
extracted, and all of their parents, are re-extracted. Cells having no
<span class="ptmb7t-x-x-120">.ext </span>files are also re-extracted.

To try out the extractor on an example, copy all the <span
class="ptmb7t-x-x-120">tut8</span><span class="ptmri7t-x-x-120">x
</span>cells to your current directory with the following shell
commands:

<table class="tabbing" data-cellpadding="0" data-border="0">
<tbody>
<tr class="odd tabbing" style="vertical-align:baseline;">
<td class="tabbing"><span class="ptmb7t-x-x-120">cp
~cad/lib/magic/tutorial/tut8*.mag</span><span
class="ptmb7t-x-x-120"> </span><span
class="ptmb7t-x-x-120"> .</span></td>
</tr>
</tbody>
</table>

Start magic on the cell <span class="ptmb7t-x-x-120">tut8a </span>and
type <span class="ptmb7t-x-x-120">:extract</span>. Magic will print the
name of each cell (<span class="ptmb7t-x-x-120">tut8a</span>, <span
class="ptmb7t-x-x-120">tut8b</span>, <span
class="ptmb7t-x-x-120">tut8c</span>, and <span
class="ptmb7t-x-x-120">tut8d</span>) as it is extracted. Now type <span
class="ptmb7t-x-x-120">:extract </span>a second time. This time nothing
gets printed, since Magic didn’t have to re-extract any cells. Now
delete the piece of poly labelled “<span class="ptmb7t-x-x-120">delete
me</span>” and type <span class="ptmb7t-x-x-120">:extract </span>again.
This time, only the cell <span class="ptmb7t-x-x-120">tut8a </span>is
extracted as it is the only one that changed. If you make a change to
cell <span class="ptmb7t-x-x-120">tut8b </span>(do it) and then extract
again, both <span class="ptmb7t-x-x-120">tut8b </span>and <span
class="ptmb7t-x-x-120">tut8a </span>will be re-extracted, since <span
class="ptmb7t-x-x-120">tut8a</span> is the parent of <span
class="ptmb7t-x-x-120">tut8b</span>.

To force all cells in the subtree rooted at cell <span
class="ptmri7t-x-x-120">root </span>to be re-extracted, use <span
class="ptmb7t-x-x-120">:extract</span><span
class="ptmb7t-x-x-120"> all</span>:

<table class="tabbing" data-cellpadding="0" data-border="0">
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd tabbing" style="vertical-align:baseline;">
<td class="tabbing"><span class="ptmb7t-x-x-120">:load</span><span
class="ptmri7t-x-x-120">root</span><br />
<span class="ptmb7t-x-x-120">:extract all</span></td>
</tr>
</tbody>
</table>

Try this also on <span class="ptmb7t-x-x-120">tut8a</span>.

You can also use the <span class="ptmb7t-x-x-120">:extract
</span>command to extract a single cell as follows:

<table class="tabbing" data-cellpadding="0" data-border="0">
<tbody>
<tr class="odd tabbing" style="vertical-align:baseline;">
<td class="tabbing"><span class="ptmb7t-x-x-120">:extract cell
</span><span class="ptmri7t-x-x-120">name</span></td>
</tr>
</tbody>
</table>

will extract just the selected (current) cell, and place the output in
the file <span class="ptmri7t-x-x-120">name</span>. Select the cell
<span class="ptmb7t-x-x-120">tut8b</span> (<span
class="ptmb7t-x-x-120">tut8b</span><span
class="ptmb7t-x-x-120">\_0</span>) and type <span
class="ptmb7t-x-x-120">:extract cell differentFile </span>to try this
out. After this command, the file <span
class="ptmb7t-x-x-120">differentFile.ext </span>will contain the
extracted circuit for the cell <span
class="ptmb7t-x-x-120">tut8b</span>. The children of <span
class="ptmb7t-x-x-120">tut8b </span>(in this case, the single cell <span
class="ptmb7t-x-x-120">tut8d</span>) will not be re-extracted by this
command. If more than one cell is selected, the upper-leftmost one is
extracted.

You should be careful about using <span class="ptmb7t-x-x-120">:extract
cell</span>, since even though you may only make a change to a child
cell, all of its parents may have to be re-extracted. To re-extract all
of the parents of the selected cell, you may use

<table class="tabbing" data-cellpadding="0" data-border="0">
<tbody>
<tr class="odd tabbing" style="vertical-align:baseline;">
<td class="tabbing"><span class="ptmb7t-x-x-120">:extract
parents</span></td>
</tr>
</tbody>
</table>

Try this out with <span class="ptmb7t-x-x-120">tut8b </span>still
selected. Magic will extract only the cell <span
class="ptmb7t-x-x-120">tut8a</span>, since it is the only one that uses
the cell <span class="ptmb7t-x-x-120">tut8b</span>. To see what cells
would be extracted by <span class="ptmb7t-x-x-120">:extract parents
</span>without actually extracting them, use

<table class="tabbing" data-cellpadding="0" data-border="0">
<tbody>
<tr class="odd tabbing" style="vertical-align:baseline;">
<td class="tabbing"><span class="ptmb7t-x-x-120">:extract
showparents</span></td>
</tr>
</tbody>
</table>

Try this command as well.

### <span class="titlemark">3 </span> <span id="x1-30003"></span>Feedback: Errors and Warnings

When the extractor encounters problems, it leaves feedback in the form
of stippled white rectangular areas on the screen. Each area covers the
portion of the layout that caused the error. Each area also has an error
message associated with it, which you can see by using the <span
class="ptmb7t-x-x-120">:feedback </span>command. Type <span
class="ptmb7t-x-x-120">:feedback help </span>while in Magic for
assistance in using the <span class="ptmb7t-x-x-120">:feedback</span>
command.

The extractor will always report extraction <span
class="ptmri7t-x-x-120">errors</span>. These are problems in the layout
that may cause the output of the extractor to be incorrect. The layout
should be fixed to eliminate extraction errors before attempting to
simulate the circuit; otherwise, the results of the simulation may not
reflect reality.

Extraction errors can come from violations of transistor rules. There
are two rules about the formation of transistors: no transistor can be
formed, and none can be destroyed, as a result of cell overlaps. For
example, it is illegal to have poly in one cell overlap diffusion in
another cell, as that would form a transistor in the parent where none
was present in either child. It is also illegal to have a buried contact
in one cell overlap a transistor in another, as this would destroy the
transistor. Violating these transistor rules will cause design-rule
violations as well as extraction errors. These errors only relate to
circuit extraction: the fabricated circuit may still work; it just won’t
be extracted correctly.

In general, it is an error for material of two types on the same plane
to overlap or abut if they don’t connect to each other. For example, in
CMOS it is illegal for p-diffusion and n-diffusion to overlap or abut.

In addition to errors, the extractor can give <span
class="ptmri7t-x-x-120">warnings</span>. If only warnings are present,
the extracted circuit can still be simulated. By default, only some
types of warnings are reported and displayed as feedback. To cause all
warnings to be displayed, use

<table class="tabbing" data-cellpadding="0" data-border="0">
<tbody>
<tr class="odd tabbing" style="vertical-align:baseline;">
<td class="tabbing"><span class="ptmb7t-x-x-120">:extract warn
all</span></td>
</tr>
</tbody>
</table>

The command

<table class="tabbing" data-cellpadding="0" data-border="0">
<tbody>
<tr class="odd tabbing" style="vertical-align:baseline;">
<td class="tabbing"><span class="ptmb7t-x-x-120">:extract warn
</span><span class="ptmri7t-x-x-120">warning</span></td>
</tr>
</tbody>
</table>

may be used to enable specific warnings selectively; see below. To cause
no warnings to be displayed, or to disable display of a particular <span
class="ptmri7t-x-x-120">warning</span>, use respectively

<table class="tabbing" data-cellpadding="0" data-border="0">
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd tabbing" style="vertical-align:baseline;">
<td class="tabbing"><span class="ptmb7t-x-x-120">:extract warn no all
</span>or<br />
<span class="ptmb7t-x-x-120">:extract warn no </span><span
class="ptmri7t-x-x-120">warning</span></td>
</tr>
</tbody>
</table>

Three different kinds of warnings are generated. The <span
class="ptmb7t-x-x-120">dup </span>warning checks to see whether you have
two electrically unconnected nodes in the same cell labelled with the
same name. If so, you are warned because the two unconnected nodes will
appear to be connected in the resulting <span
class="ptmb7t-x-x-120">.ext </span>file, which means that the extracted
circuit would not represent the actual layout. This is bad if you’re
simulating the circuit to see if it will work correctly: the simulator
will think the two nodes are connected, but since there’s no physical
wire between them, the electrons won’t! When two unconnected nodes share
the same label (name), the extractor leaves feedback squares over each
instance of the shared name.

It’s an excellent idea to avoid labelling two unconnected nodes with the
same name within a cell. Instead, use the ”correct” name for one of the
nodes, and some mnemonic but textually distinct name for the other
nodes. For example, in a cell with multiple power rails, you might use
<span class="ptmb7t-x-x-120">Vdd! </span>for one of the rails, and names
like <span class="ptmb7t-x-x-120">Vdd#1 </span>for the others. As an
example, load the cell <span class="ptmb7t-x-x-120">tut8e</span>. If the
two nodes are connected in a higher-level cell they will eventually be
merged when the extracted circuit is flattened. If you want to simulate
a cell out of context, but still want the higher-level nodes to be
hooked up, you can always create a dummy parent cell that hooks them
together, either with wire or by using the same name for pieces of paint
that lie over the terminals to be connected; see the cell <span
class="ptmb7t-x-x-120">tut8f </span>for an example of this latter
technique.

You can use the command

<table class="tabbing" data-cellpadding="0" data-border="0">
<tbody>
<tr class="odd tabbing" style="vertical-align:baseline;">
<td class="tabbing"><span class="ptmb7t-x-x-120">:extract
unique</span></td>
</tr>
</tbody>
</table>

as an automatic means of labelling nodes in the manner described above.
Run this command on the cell <span class="ptmb7t-x-x-120">tut8g</span>.
A second version of this command is provided for compatibility with
previous versions of Magic. Running

<table class="tabbing" data-cellpadding="0" data-border="0">
<tbody>
<tr class="odd tabbing" style="vertical-align:baseline;">
<td class="tabbing"><span class="ptmb7t-x-x-120">:extract unique
#</span></td>
</tr>
</tbody>
</table>

will only append a unique numeric suffix to labels that end with a
“<span class="ptmb7t-x-x-120">\#</span>”. Any other duplicate nodenames
that also don’t end in a “<span class="ptmb7t-x-x-120">!</span>” (the
global nodename suffix as described in Section 5) are flagged by
feedback.

A second type of warning, <span class="ptmb7t-x-x-120">fets</span>,
checks to see whether any transistors have fewer diffusion terminals
than the minimum for their types. For example, the transistor type
“<span class="ptmb7t-x-x-120">dfet</span>” is defined in the <span
class="ptmb7t-x-x-120">nmos </span>technology file as requiring two
diffusion terminals: a source and a drain. If a capacitor with only one
diffusion terminal is desired in this technology, the type <span
class="ptmb7t-x-x-120">dcap </span>should be used instead. The <span
class="ptmb7t-x-x-120">fets </span>warning is a consistency check for
transistors whose diffusion terminals have been accidentally shorted
together, or for transistors with insufficiently many diffusion
terminals.

The third warning, <span class="ptmb7t-x-x-120">labels</span>, is
generated if you violate the following guideline for placement of
labels: Whenever geometry from two subcells abuts or overlaps, it’s a
good idea to make sure that there is a label attached to the geometry in
each subcell <span class="ptmri7t-x-x-120">in the area of the overlap or
along the line of abutment</span>. Following this guideline isn’t
necessary for the extractor to work, but it will result in noticeably
faster extraction.

By default, the <span class="ptmb7t-x-x-120">dup </span>and <span
class="ptmb7t-x-x-120">fets </span>warnings are enabled, and the <span
class="ptmb7t-x-x-120">labels </span>warning is disabled.

Load the cell <span class="ptmb7t-x-x-120">tut8h</span>, expand all its
children (<span class="ptmb7t-x-x-120">tut8i </span>and <span
class="ptmb7t-x-x-120">tut8j</span>), and enable all extractor warnings
with <span class="ptmb7t-x-x-120">:extract warn all</span>. Now extract
<span class="ptmb7t-x-x-120">tut8h </span>and all of its children with
<span class="ptmb7t-x-x-120">:extract</span>, and examine the feedback
for examples of fatal errors and warnings.

### <span class="titlemark">4 </span> <span id="x1-40004"></span>Advanced Circuit Extraction

#### <span class="titlemark">4.1 </span> <span id="x1-50004.1"></span>Lengths

The Magic extractor has a rudimentary ability to compute wire lengths
between specific named points in a circuit. This feature is intended for
use with technologies where the wire length between two points is more
important than the total capacitance on the net; this may occur, for
example, when extracting circuits with very long wires being driven at
high speeds (<span class="ptmri7t-x-x-120">e.g.</span>, bipolar
circuits). Currently, you must indicate to Magic which pairs of points
are to have distances computed. You do this by providing two lists: one
of <span class="ptmri7t-x-x-120">drivers </span>and one of <span
class="ptmri7t-x-x-120">receivers</span>. The extractor computes the
distance between each driver and each receiver that it is connected to.

Load the cell <span class="ptmb7t-x-x-120">tut8k</span>. There are five
labels: two are drivers (<span class="ptmb7t-x-x-120">driver1 </span>and
<span class="ptmb7t-x-x-120">driver2</span>) and three are receivers
(<span class="ptmb7t-x-x-120">receiverA</span>, <span
class="ptmb7t-x-x-120">receiverB</span>, and <span
class="ptmb7t-x-x-120">receiverC</span>). Type the commands:

<table class="tabbing" data-cellpadding="0" data-border="0">
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd tabbing" style="vertical-align:baseline;">
<td class="tabbing"><span class="ptmb7t-x-x-120">:extract length driver
driver1 driver2</span><br />
<span class="ptmb7t-x-x-120">:extract length receiver receiverA
receiverB receiverC</span></td>
</tr>
</tbody>
</table>

Now enable extraction of lengths with <span
class="ptmb7t-x-x-120">:extract do length </span>and then extract the
cell (<span class="ptmb7t-x-x-120">:extract</span>). If you examine
<span class="ptmb7t-x-x-120">tut8k.ext</span>, you will see several
<span class="ptmb7t-x-x-120">distance </span>lines, corresponding to the
driver-receiver distances described above. These distances are through
the centerlines of wires connecting the two labels; where multiple paths
exist, the shortest is used.

Normally the driver and receiver tables will be built by using <span
class="ptmb7t-x-x-120">:source </span>to read a file of <span
class="ptmb7t-x-x-120">:extract length</span> <span
class="ptmb7t-x-x-120">driver </span>and <span
class="ptmb7t-x-x-120">:extract length receiver </span>commands. Once
these tables are created in Magic, they remain until you leave Magic or
type the command

<table class="tabbing" data-cellpadding="0" data-border="0">
<tbody>
<tr class="odd tabbing" style="vertical-align:baseline;">
<td class="tabbing"><span class="ptmb7t-x-x-120">:extract length
clear</span></td>
</tr>
</tbody>
</table>

which wipes out both tables.

Because extraction of wire lengths is <span class="ptmri7t-x-x-120">not
</span>performed hierarchically, it should only be done in the root cell
of a design. Also, because it’s not hierarchical, it can take a long
time for long, complex wires such as power and ground nets. This feature
is still experimental and subject to change.

#### <span class="titlemark">4.2 </span> <span id="x1-60004.2"></span>Resistance

Magic provides for more accurate resistance extraction using the <span
class="ptmb7t-x-x-120">:extresis </span>command. <span
class="ptmb7t-x-x-120">:extresis </span>provides a detailed
resistance/capacitance description for nets where parasitic resistance
is likely to significantly affect circuit timing.

##### <span class="titlemark">4.2.1 </span> <span id="x1-70004.2.1"></span>Tutorial Introduction

To try out the resistance extractor, load in the cell <span
class="ptmb7t-x-x-120">tut8r</span>. Extract it using <span
class="ptmb7t-x-x-120">:extract</span>, pause magic, and run ext2sim on
the cell with the command

<table class="tabbing" data-cellpadding="0" data-border="0">
<tbody>
<tr class="odd tabbing" style="vertical-align:baseline;">
<td class="tabbing"><span class="ptmb7t-x-x-120">ext2sim
tut8r</span></td>
</tr>
</tbody>
</table>

This should produce <span class="ptmb7t-x-x-120">tut8r.sim</span>, <span
class="ptmb7t-x-x-120">tut8r.nodes</span>, and <span
class="ptmb7t-x-x-120">tut8r.al</span>. Restart magic and type

<table class="tabbing" data-cellpadding="0" data-border="0">
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd tabbing" style="vertical-align:baseline;">
<td class="tabbing"><span class="ptmb7t-x-x-120">:extresis tolerance
10</span><br />
<span class="ptmb7t-x-x-120">:extresis</span></td>
</tr>
</tbody>
</table>

This will extract interconnect resistances for any net where the
interconnect delay is at least one-tenth of the transistor delay. Magic
should give the messages:

<table class="tabbing" data-cellpadding="0" data-border="0">
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd tabbing" style="vertical-align:baseline;">
<td class="tabbing"><span class="ptmb7t-x-x-120">:extresis tolerance
10</span><br />
<span class="ptmb7t-x-x-120">:extresis</span><br />
<span class="ptmb7t-x-x-120">Adding net2; Tnew = 0.428038ns,Told =
0.3798ns</span><br />
<span class="ptmb7t-x-x-120">Adding net1; Tnew = 0.529005ns,Told =
0.4122ns</span><br />
<span class="ptmb7t-x-x-120">Total Nets: 7</span><br />
<span class="ptmb7t-x-x-120">Nets extracted: 2 (0.285714)</span><br />
<span class="ptmb7t-x-x-120">Nets output: 2 (0.285714)</span></td>
</tr>
</tbody>
</table>

These may vary slightly depending on your technology parameters. The
<span class="ptmb7t-x-x-120">Adding \[net\] </span>lines describe which
networks for which magic produced resistor networks. <span
class="ptmb7t-x-x-120">Tnew </span>is the estimated delay on the net
including the resistor parasitics, while <span
class="ptmb7t-x-x-120">Told </span>is the delay without parasitics. The
next line describes where magic thinks the slowest node in the net is.
The final 3 lines give a brief summary of the total number of nets, the
nets requiring extraction, and the number for which resistors were added
to the output.

Running the resistance extractor also produced the file <span
class="ptmb7t-x-x-120">cell.res.ext</span>. To produce a <span
class="ptmb7t-x-x-120">.sim </span>file containing resistors, quit magic
and type:

<table class="tabbing" data-cellpadding="0" data-border="0">
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd tabbing" style="vertical-align:baseline;">
<td class="tabbing"><span class="ptmb7t-x-x-120">cat tut8r.ext
tut8r.res.ext </span><span class="math inline">&gt;</span><span
class="ptmb7t-x-x-120">tut8r.2.ext</span><br />
<span class="ptmb7t-x-x-120">ext2sim -R -t! -t# tut8r.2</span></td>
</tr>
</tbody>
</table>

Comparing the two files, <span class="ptmb7t-x-x-120">tut8r.sim
</span>and <span class="ptmb7t-x-x-120">tut8r.2.sim</span>, shows that
the latter has the nodes net1 and net2 split into several parts, with
resistors added to connect the new nodes together.

##### <span class="titlemark">4.2.2 </span> <span id="x1-80004.2.2"></span>General Notes on using the resistance extractor

To use <span class="ptmb7t-x-x-120">:extresis</span>, the circuit must
first be extracted using <span class="ptmb7t-x-x-120">:extract
</span>and flattened using ext2sim. When ext2sim is run, do not use the
<span class="ptmb7t-x-x-120">-t# </span>and <span
class="ptmb7t-x-x-120">-t! </span>flags (i.e. don’t trim the trailing
”#” and ”!” characters) or the <span class="ptmb7t-x-x-120">-R</span>
flag because <span class="ptmb7t-x-x-120">:extresis </span>needs the
<span class="ptmb7t-x-x-120">.sim </span>and <span
class="ptmb7t-x-x-120">.ext </span>names to correspond exactly, and it
needs the lumped resistance values that the extractor produces. Also, do
not delete or rename the <span class="ptmb7t-x-x-120">.nodes
</span>file; <span class="ptmb7t-x-x-120">:extresis </span>needs this to
run. Once the <span class="ptmb7t-x-x-120">.sim </span>and <span
class="ptmb7t-x-x-120">.nodes </span>files have been produced, type the
command <span class="ptmb7t-x-x-120">:extresis </span>while running
magic on the root cell. As the resistance extractor runs, it will
identify which nets (if any) for which it is producing RC networks, and
will identify what it thinks is the ”slowest” point in the network. When
it completes, it will print a brief summary of how many nets it
extracted and how many required supplemental networks. The resistance
networks are placed in the file <span
class="ptmb7t-x-x-120">root.res.ext</span>. To produce a <span
class="ptmb7t-x-x-120">.sim </span>file with the supplemental resistors,
type <span class="ptmb7t-x-x-120">cat root.ext root.res.ext</span>
&gt;<span class="ptmb7t-x-x-120">newname.ext</span>, and then rerun
<span class="ptmb7t-x-x-120">ext2sim </span>on the new file. During this
second <span class="ptmb7t-x-x-120">ext2sim </span>run, the <span
class="ptmb7t-x-x-120">-t </span>flag may be used.

Like extraction of wire lengths, resistance extraction is <span
class="ptmri7t-x-x-120">not </span>performed hierarchically; it should
only be done in the root cell of a design and can take a long time for
complex wires.

##### <span class="titlemark">4.2.3 </span> <span id="x1-90004.2.3"></span>Options, Features, Caveats and Bugs

The following is a list of command line options and the arguments that
they take.

-   <span class="ptmb7t-x-x-120">tolerance \[value\] </span>  
    This controls how large the resistance in a network must be before
    it is added to the output description. <span
    class="ptmb7t-x-x-120">value </span>is defined as the minimum ratio
    of transistor resistance to interconnect resistance that requires a
    resistance network. The default value is 1; values less than 1 will
    cause fewer resistors to be output and will make the program run
    faster, while values greater than 1 will produce more a larger, more
    accurate description but will run slower.

-   <span class="ptmb7t-x-x-120">all </span>  
    Causes all nets in the circuit to be extracted; no comparison
    between transistor size and lumped resistance is performed. This
    option is not recommended for large designs.

-   <span class="ptmb7t-x-x-120">simplify \[on/off\] </span>  
    Turns on/off the resistance network simplification routines. Magic
    normally simplifies the resistance network it extracts by removing
    small resistors; specifying this flag turns this feature off.

-   <span class="ptmb7t-x-x-120">extout \[on/off\] </span>  
    Turns on and off the writing of the <span
    class="pcrr7t-x-x-120">root.res.ext </span>file. The default value
    is on.

-   <span class="ptmb7t-x-x-120">lumped \[on/off\] </span>  
    Turns on the writing of <span
    class="pcrr7t-x-x-120">root.res.lump</span>. This file contains an
    updated value of the lumped resistance for each net that <span
    class="ptmb7t-x-x-120">:extresis </span>extracts.

-   <span class="ptmb7t-x-x-120">silent \[on/off\] </span>  
    This option suppresses printing of the name and location of nets for
    which resistors are produced.

-   <span class="ptmb7t-x-x-120">skip mask </span>  
    Specifies a list of layers that the resistance extractor is to
    ignore.

-   <span class="ptmb7t-x-x-120">help </span>  
    Print brief list of options.

Attribute labels may also be used to specify certain extractor options.
For a description of attributes and how they work, see tutorial 2.
Following is a description of <span class="ptmb7t-x-x-120">:extresis
</span>attributes.

-   <span class="ptmb7t-x-x-120">res:skip@ </span>  
    Causes this net to be skipped. This is useful for avoiding
    extraction of power supplies or other DC signals that are not
    labeled Vdd or GND.

-   <span class="ptmb7t-x-x-120">res:force@ </span>  
    Forces extraction of this net regardless of its lumped resistance
    value. Nets with both skip and force labels attached will cause the
    extractor to complain.

-   <span class="ptmb7t-x-x-120">res:min=\[value\]@ </span>  
    Sets the smallest resistor size for this net. The default value is
    the resistance of the largest driving transistor divided by the
    tolerance described above.

-   <span class="ptmb7t-x-x-120">res:drive@ </span>- Nets with no
    driving transistors will normally not be extracted. This option
    allows the designer to specify from where in the net the signal is
    driven. This is primarily useful when extracting subcells, where the
    transistors driving a given signal may be located in a different
    cell.

##### <span class="titlemark">4.2.4 </span> <span id="x1-100004.2.4"></span>Technology File Changes

Certain changes must be made in the extract section of the technology
file to support resistance extraction. These include the <span
class="ptmb7t-x-x-120">fetresist </span>and <span
class="ptmb7t-x-x-120">contact </span>lines, plus a small change to the
fet line. Full details can be found in Magic Maintainer’s Manual \#2.
The only thing to note is that, contrary to the documentation, the <span
class="ptmb7t-x-x-120">gccap</span> and <span
class="ptmb7t-x-x-120">gscap </span>parts of the fet line MUST be set;
the resistance extractor uses them to calculate RC time constants for
the circuit.

### <span class="titlemark">5 </span> <span id="x1-110005"></span>Extraction Details and Limitations

This section explores in greater depth what gets extracted by Magic, as
well as the limitations of the circuit extractor. A detailed explanation
of the format of the <span class="ptmb7t-x-x-120">.ext </span>files
output by Magic may be found in the manual page <span
class="ptmri7t-x-x-120">ext</span> (5). “Magic Maintainer’s Manual #2:
The Technology File” describes how extraction parameters are specified
for the extractor.

<figure>
<img src="tut80x.png" class="graphics" width="645" height="649"
alt="Figure 1: Each node extracted by Magic has a lumped resistance R and a lumped capacitance C to the substrate. These lumped values can be interpreted as in the diagram above, in which each device connected to the node is attached to one of the points 1, 2, …, N." />
<figcaption aria-hidden="true"><span class="id">Figure 1: </span><span
class="content">Each node extracted by Magic has a lumped resistance
<span class="ptmri7t-x-x-120">R </span>and a lumped capacitance <span
class="ptmri7t-x-x-120">C</span> to the substrate. These lumped values
can be interpreted as in the diagram above, in which each device
connected to the node is attached to one of the points <span
class="ptmri7t-x-x-120">1</span>, <span
class="ptmri7t-x-x-120">2</span>, …, <span
class="ptmri7t-x-x-120">N</span>.</span></figcaption>
</figure>

#### <span class="titlemark">5.1 </span> <span id="x1-120005.1"></span>Nodes

Magic approximates the pieces of interconnect between transistors as
“nodes”. A node is like an equipotential region, but also includes a
lumped resistance and capacitance to substrate. Figure 1 shows how these
lumped values are intended to be interpreted by the analysis programs
that use the extracted circuit.

Each node in an extracted circuit has a name, which is either one of the
labels attached to the geometry in the node if any exist, or
automatically generated by the extractor. These latter names are always
of the form <span class="ptmri7t-x-x-120">p</span><span
class="ptmri7t-x-x-120">\_x</span><span
class="ptmri7t-x-x-120">\_y#</span>, where <span
class="ptmri7t-x-x-120">p</span>, <span
class="ptmri7t-x-x-120">x</span>, and <span class="ptmri7t-x-x-120">y
</span>are integers, <span class="ptmri7t-x-x-120">e.g.</span>, <span
class="ptmb7t-x-x-120">3</span><span
class="ptmb7t-x-x-120">\_104</span><span
class="ptmb7t-x-x-120">\_17#</span>. If a label ending in the character
“<span class="ptmb7t-x-x-120">!</span>” is attached to a node, the node
is considered to be a “global”. Post-processing programs such as <span
class="ptmri7t-x-x-120">ext2sim</span> (1) will check to ensure that
nodes in different cells that are labelled with the same global name are
electrically connected.

Nodes may have attributes attached to them as well as names. Node
attributes are labels ending in the special character “<span
class="ptmb7t-x-x-120">@</span>”, and provide a mechanism for passing
information to analysis programs such as <span
class="ptmri7t-x-x-120">crystal</span> (1). The man page <span
class="ptmri7t-x-x-120">ext</span> (5) provides additional information
about node attributes.

#### <span class="titlemark">5.2 </span> <span id="x1-130005.2"></span>Resistance

Magic extracts a lumped resistance for each node, rather than a
point-to-point resistance between each pair of devices connected to that
node. The result is that all such point-to-point resistances are
approximated by the worst-case resistance between any two points in that
node.

By default, node resistances are approximated rather than computed
exactly. For a node comprised entirely of a single type of material,
Magic will compute the node’s total perimeter and area. It then solves a
quadratic equation to find the width and height of a simple rectangle
with this same perimeter and area, and approximates the resistance of
the node as the resistance of this “equivalent” rectangle. The
resistance is always taken in the longer dimension of the rectangle.
When a node contains more than a single type of material, Magic computes
an equivalent rectangle for each type, and then sums the resistances as
though the rectangles were laid end-to-end.

This approximation for resistance does not take into account any
branching, so it can be significantly in error for nodes that have side
branches. Figure 2 gives an example. For global signal trees such as
clocks or power, Magic’s estimate of resistance will likely be several
times higher than the actual resistance between two points.

<figure>
<img src="tut81x.png" class="graphics" width="1565" height="630"
alt="Figure 2: Magic approximates the resistance of a node by assuming that it is a simple wire. The length and width of the wire are estimated from the node’s perimeter and area. (a) For non-branching nodes, this approximation is a good one. (b) The computed resistance for this node is the same as for (a) because the side branches are counted, yet the actual resistance between points 1 and 2 is significantly less than in (a)." />
<figcaption aria-hidden="true"><span class="id">Figure 2: </span><span
class="content">Magic approximates the resistance of a node by assuming
that it is a simple wire. The length and width of the wire are estimated
from the node’s perimeter and area. (a) For non-branching nodes, this
approximation is a good one. (b) The computed resistance for this node
is the same as for (a) because the side branches are counted, yet the
actual resistance between points 1 and 2 is significantly less than in
(a).</span></figcaption>
</figure>

The approximated resistance also does not lend itself well to
hierarchical adjustments, as does capacitance. To allow programs like
<span class="ptmb7t-x-x-120">ext2sim </span>to incorporate hierarchical
adjustments into a resistance approximation, each node in the <span
class="ptmb7t-x-x-120">.ext </span>file also contains a perimeter and
area for each “resistance class” that was defined in the technology file
(see “Maintainer’s Manual \#2: The Technology File,” and <span
class="ptmri7t-x-x-120">ext</span> (5)). When flattening a circuit,
<span class="ptmb7t-x-x-120">ext2sim </span>uses this information along
with adjustments to perimeter and area to produce the value it actually
uses for node resistance.

If you wish to disable the extraction of resistances and node perimeters
and areas, use the command

<table class="tabbing" data-cellpadding="0" data-border="0">
<tbody>
<tr class="odd tabbing" style="vertical-align:baseline;">
<td class="tabbing"><span class="ptmb7t-x-x-120">:extract no
resistance</span></td>
</tr>
</tbody>
</table>

which will cause all node resistances, perimeters, and areas in the
<span class="ptmb7t-x-x-120">.ext </span>file to be zero. To re-enable
extraction of resistance, use the command

<table class="tabbing" data-cellpadding="0" data-border="0">
<tbody>
<tr class="odd tabbing" style="vertical-align:baseline;">
<td class="tabbing"><span class="ptmb7t-x-x-120">:extract do
resistance</span>.</td>
</tr>
</tbody>
</table>

Sometimes it’s important that resistances be computed more accurately
than is possible using the lumped approximation above. Magic’s <span
class="ptmb7t-x-x-120">:extresist </span>command does this by computing
explicit two-terminal resistors and modifying the circuit network to
include them so it reflects more exactly the topology of the layout. See
the section on <span class="ptmb7t-x-x-120">Advanced Extraction
</span>for more details on explicit resistance extraction with <span
class="ptmb7t-x-x-120">:extresist</span>.

<figure>
<img src="tut82x.png" class="graphics" width="978" height="646"
alt="Figure 3: Each type of edge has capacitance to substrate per unit length. Here, the diffusion-space perimeter of 13 units has one value per unit length, and the diffusion-buried perimeter of 3 units another. In addition, each type of material has capacitance per unit area." />
<figcaption aria-hidden="true"><span class="id">Figure 3: </span><span
class="content">Each type of edge has capacitance to substrate per unit
length. Here, the diffusion-space perimeter of 13 units has one value
per unit length, and the diffusion-buried perimeter of 3 units another.
In addition, each type of material has capacitance per unit
area.</span></figcaption>
</figure>

#### <span class="titlemark">5.3 </span> <span id="x1-140005.3"></span>Capacitance

Capacitance to substrate comes from two different sources. Each type of
material has a capacitance to substrate per unit area. Each type of edge
(i.e, each pair of types) has a capacitance to substrate per unit
length. See Figure 3. The computation of capacitance may be disabled
with

<table class="tabbing" data-cellpadding="0" data-border="0">
<tbody>
<tr class="odd tabbing" style="vertical-align:baseline;">
<td class="tabbing"><span class="ptmb7t-x-x-120">:extract no
capacitance</span></td>
</tr>
</tbody>
</table>

which causes all substrate capacitance values in the <span
class="ptmb7t-x-x-120">.ext </span>file to be zero. It may be re-enabled
with

<table class="tabbing" data-cellpadding="0" data-border="0">
<tbody>
<tr class="odd tabbing" style="vertical-align:baseline;">
<td class="tabbing"><span class="ptmb7t-x-x-120">:extract do
capacitance</span>.</td>
</tr>
</tbody>
</table>

Internodal capacitance comes from three sources, as shown in Figure 4.
When materials of two different types overlap, the capacitance to
substrate of the one on top (as determined by the technology) is
replaced by an internodal capacitance to the one on the bottom. Its
computation may be disabled with

<table class="tabbing" data-cellpadding="0" data-border="0">
<tbody>
<tr class="odd tabbing" style="vertical-align:baseline;">
<td class="tabbing"><span class="ptmb7t-x-x-120">:extract no
coupling</span></td>
</tr>
</tbody>
</table>

which will also cause the extractor to run 30% to 50% faster. Extraction
of coupling capacitances can be re-enabled with

<table class="tabbing" data-cellpadding="0" data-border="0">
<tbody>
<tr class="odd tabbing" style="vertical-align:baseline;">
<td class="tabbing"><span class="ptmb7t-x-x-120">:extract do
coupling</span>.</td>
</tr>
</tbody>
</table>

<figure>
<img src="tut83x.png" class="graphics" width="1467" height="621"
alt="Figure 4: Magic extracts three kinds of internodal coupling capacitance. This figure is a cross-section (side view, not a top view) of a set of masks that shows all three kinds of capacitance. Overlap capacitance is parallel-plate capacitance between two different kinds of material when they overlap. Sidewall capacitance is parallel-plate capacitance between the vertical edges of two pieces of the same kind of material. Sidewall overlap capacitance is orthogonal-plate capacitance between the vertical edge of one piece of material and the horizontal surface of another piece of material that overlaps the first edge." />
<figcaption aria-hidden="true"><span class="id">Figure 4: </span><span
class="content">Magic extracts three kinds of internodal coupling
capacitance. This figure is a cross-section (side view, not a top view)
of a set of masks that shows all three kinds of capacitance. <span
class="ptmri7t-x-x-120">Overlap </span>capacitance is parallel-plate
capacitance between two different kinds of material when they overlap.
<span class="ptmri7t-x-x-120">Sidewall </span>capacitance is
parallel-plate capacitance between the vertical edges of two pieces of
the same kind of material. <span class="ptmri7t-x-x-120">Sidewall
overlap </span>capacitance is orthogonal-plate capacitance between the
vertical edge of one piece of material and the horizontal surface of
another piece of material that overlaps the first
edge.</span></figcaption>
</figure>

<figure>
<img src="tut84x.png" class="graphics" width="1467" height="1089"
alt="Figure 5: (a) When transistors are rectangular, it is possible to compute \left. L\slash W \right. exactly. Here gateperim= 4, srcperim= 6, drainperim= 6, and \left. L\slash W = 2\slash 6 \right.. (b) The \left. L\slash W \right. of non-branching transistors can be approximated. Here gateperim= 4, srcperim= 6, drainperim= 10. By averaging srcperim and drainperim we get \left. L\slash W = 2\slash 8 \right.. (c) The \left. L\slash W \right. of branching transistors is not well approximated. Here gateperim= 16, srcperim= 2, drainperim= 2. Magic’s estimate of \left. L\slash W \right. is \left. 8\slash 2 \right., whereas in fact because of current spreading, W is effectively larger than 2 and L effectively smaller than 8, so \left. L\slash W \right. is overestimated." />
<figcaption aria-hidden="true"><span class="id">Figure 5: </span><span
class="content">(a) When transistors are rectangular, it is possible to
compute <span class="math inline"><em>L</em>/<em>W</em></span> exactly.
Here <span class="ptmri7t-x-x-120">gateperim</span><span
class="math inline"> = 4</span>, <span
class="ptmri7t-x-x-120">srcperim</span><span
class="math inline"> = 6</span>, <span
class="ptmri7t-x-x-120">drainperim</span><span
class="math inline"> = 6</span>, and <span
class="math inline"><em>L</em>/<em>W</em>=2/6</span>. (b) The <span
class="math inline"><em>L</em>/<em>W</em></span> of non-branching
transistors can be approximated. Here <span
class="ptmri7t-x-x-120">gateperim</span><span
class="math inline"> = 4</span>, <span
class="ptmri7t-x-x-120">srcperim</span><span
class="math inline"> = 6</span>, <span
class="ptmri7t-x-x-120">drainperim</span><span
class="math inline"> = 10</span>. By averaging <span
class="ptmri7t-x-x-120">srcperim </span>and <span
class="ptmri7t-x-x-120">drainperim </span>we get <span
class="math inline"><em>L</em>/<em>W</em>=2/8</span>. (c) The <span
class="math inline"><em>L</em>/<em>W</em></span> of branching
transistors is not well approximated. Here <span
class="ptmri7t-x-x-120">gateperim</span><span
class="math inline"> = 16</span>, <span
class="ptmri7t-x-x-120">srcperim</span><span
class="math inline"> = 2</span>, <span
class="ptmri7t-x-x-120">drainperim</span><span
class="math inline"> = 2</span>. Magic’s estimate of <span
class="math inline"><em>L</em>/<em>W</em></span> is <span
class="math inline">8/2</span>, whereas in fact because of current
spreading, <span class="math inline"><em>W</em></span> is effectively
larger than <span class="math inline">2</span> and <span
class="math inline"><em>L</em></span> effectively smaller than <span
class="math inline">8</span>, so <span
class="math inline"><em>L</em>/<em>W</em></span> is
overestimated.</span></figcaption>
</figure>

Whenever material from two subcells overlaps or abuts, the extractor
computes adjustments to substrate capacitance, coupling capacitance, and
node perimeter and area. Often, these adjustments make little difference
to the type of analysis you are performing, as when you wish only to
compare netlists. Even when running Crystal for timing analysis, the
adjustments can make less than a 5% difference in the timing of critical
paths in designs with only a small amount of inter-cell overlap. To
disable the computation of these adjustments, use

<table class="tabbing" data-cellpadding="0" data-border="0">
<tbody>
<tr class="odd tabbing" style="vertical-align:baseline;">
<td class="tabbing"><span class="ptmb7t-x-x-120">:extract no
adjustment</span></td>
</tr>
</tbody>
</table>

which will result in approximately 50% faster extraction. This speedup
is not entirely additive with the speedup resulting from <span
class="ptmb7t-x-x-120">:extract no coupling</span>. To re-enable
computation of adjustments, use <span class="ptmb7t-x-x-120">:extract
do</span> <span class="ptmb7t-x-x-120">adjustment</span>.

#### <span class="titlemark">5.4 </span> <span id="x1-150005.4"></span>Transistors

Like the resistances of nodes, the lengths and widths of transistors are
approximated. Magic computes the contribution to the total perimeter by
each of the terminals of the transistor. See Figure 5. For rectangular
transistors, this yields an exact <span class="ptmr8c-x-x-120">$</span>L
/ W<span class="ptmr8c-x-x-120">$</span>. For non-branching,
non-rectangular transistors, it is still possible to approximate <span
class="ptmr8c-x-x-120">$</span>L / W<span class="ptmr8c-x-x-120">$
</span>fairly well, but substantial inaccuracies can be introduced if
the channel of a transistor contains branches. Since most transistors
are rectangular, however, Magic’s approximation works well in practice.

<span id="x1-150011"></span>

<table id="TBL-1" class="tabular" data-rules="groups">
<tbody>
<tr class="odd hline">
<td><hr /></td>
<td><hr /></td>
<td><hr /></td>
<td><hr /></td>
<td><hr /></td>
<td><hr /></td>
<td><hr /></td>
</tr>
<tr id="TBL-1-1-" class="even" style="vertical-align:baseline;">
<td id="TBL-1-1-1" class="td11"
style="text-align: center; white-space: nowrap;">Type</td>
<td id="TBL-1-1-2" class="td11"
style="text-align: center; white-space: nowrap;">Loc</td>
<td id="TBL-1-1-3" class="td11"
style="text-align: center; white-space: nowrap;">A P</td>
<td id="TBL-1-1-4" class="td11"
style="text-align: center; white-space: nowrap;">Subs</td>
<td id="TBL-1-1-5" class="td11"
style="text-align: center; white-space: nowrap;">Gate</td>
<td id="TBL-1-1-6" class="td11"
style="text-align: center; white-space: nowrap;">Source</td>
<td id="TBL-1-1-7" class="td11"
style="text-align: center; white-space: nowrap;">Drain</td>
</tr>
<tr class="odd hline">
<td><hr /></td>
<td><hr /></td>
<td><hr /></td>
<td><hr /></td>
<td><hr /></td>
<td><hr /></td>
<td><hr /></td>
</tr>
<tr id="TBL-1-2-" class="even" style="vertical-align:baseline;">
<td id="TBL-1-2-1" class="td11"
style="text-align: center; white-space: nowrap;">fet nfet</td>
<td id="TBL-1-2-2" class="td11"
style="text-align: center; white-space: nowrap;">59 1 60 2</td>
<td id="TBL-1-2-3" class="td11"
style="text-align: center; white-space: nowrap;">8 12</td>
<td id="TBL-1-2-4" class="td11"
style="text-align: center; white-space: nowrap;">GND!</td>
<td id="TBL-1-2-5" class="td11"
style="text-align: center; white-space: nowrap;">Mid2 4 <span
class="ptmb7t-x-x-120">N3</span></td>
<td id="TBL-1-2-6" class="td11"
style="text-align: center; white-space: nowrap;">Out 4 0</td>
<td id="TBL-1-2-7" class="td11"
style="text-align: center; white-space: nowrap;">Vss#0 4 0</td>
</tr>
<tr id="TBL-1-3-" class="odd" style="vertical-align:baseline;">
<td id="TBL-1-3-1" class="td11"
style="text-align: center; white-space: nowrap;">fet nfet</td>
<td id="TBL-1-3-2" class="td11"
style="text-align: center; white-space: nowrap;">36 1 37 2</td>
<td id="TBL-1-3-3" class="td11"
style="text-align: center; white-space: nowrap;">8 12</td>
<td id="TBL-1-3-4" class="td11"
style="text-align: center; white-space: nowrap;">Float</td>
<td id="TBL-1-3-5" class="td11"
style="text-align: center; white-space: nowrap;">Mid1 4 <span
class="ptmb7t-x-x-120">N2</span></td>
<td id="TBL-1-3-6" class="td11"
style="text-align: center; white-space: nowrap;">Mid2 4 0</td>
<td id="TBL-1-3-7" class="td11"
style="text-align: center; white-space: nowrap;">Vss#0 4 0</td>
</tr>
<tr id="TBL-1-4-" class="even" style="vertical-align:baseline;">
<td id="TBL-1-4-1" class="td11"
style="text-align: center; white-space: nowrap;">fet nfet</td>
<td id="TBL-1-4-2" class="td11"
style="text-align: center; white-space: nowrap;">4 1 5 2</td>
<td id="TBL-1-4-3" class="td11"
style="text-align: center; white-space: nowrap;">8 12</td>
<td id="TBL-1-4-4" class="td11"
style="text-align: center; white-space: nowrap;">Vss#0</td>
<td id="TBL-1-4-5" class="td11"
style="text-align: center; white-space: nowrap;">In 4 <span
class="ptmb7t-x-x-120">N1 </span></td>
<td id="TBL-1-4-6" class="td11"
style="text-align: center; white-space: nowrap;">Mid1 4 0</td>
<td id="TBL-1-4-7" class="td11"
style="text-align: center; white-space: nowrap;">Vss#0 4 0</td>
</tr>
<tr id="TBL-1-5-" class="odd" style="vertical-align:baseline;">
<td id="TBL-1-5-1" class="td11"
style="text-align: center; white-space: nowrap;">fet pfet</td>
<td id="TBL-1-5-2" class="td11"
style="text-align: center; white-space: nowrap;">59 25 60 26</td>
<td id="TBL-1-5-3" class="td11"
style="text-align: center; white-space: nowrap;">8 12</td>
<td id="TBL-1-5-4" class="td11"
style="text-align: center; white-space: nowrap;">Vdd!</td>
<td id="TBL-1-5-5" class="td11"
style="text-align: center; white-space: nowrap;">Mid2 4 <span
class="ptmb7t-x-x-120">P3</span></td>
<td id="TBL-1-5-6" class="td11"
style="text-align: center; white-space: nowrap;">Vdd#0 4 0</td>
<td id="TBL-1-5-7" class="td11"
style="text-align: center; white-space: nowrap;">Out 4 0</td>
</tr>
<tr id="TBL-1-6-" class="even" style="vertical-align:baseline;">
<td id="TBL-1-6-1" class="td11"
style="text-align: center; white-space: nowrap;">fet pfet</td>
<td id="TBL-1-6-2" class="td11"
style="text-align: center; white-space: nowrap;">36 25 37 26</td>
<td id="TBL-1-6-3" class="td11"
style="text-align: center; white-space: nowrap;">8 12</td>
<td id="TBL-1-6-4" class="td11"
style="text-align: center; white-space: nowrap;">VBias</td>
<td id="TBL-1-6-5" class="td11"
style="text-align: center; white-space: nowrap;">Mid1 4 <span
class="ptmb7t-x-x-120">P2</span></td>
<td id="TBL-1-6-6" class="td11"
style="text-align: center; white-space: nowrap;">Vdd#0 4 0</td>
<td id="TBL-1-6-7" class="td11"
style="text-align: center; white-space: nowrap;">Mid2 4 0</td>
</tr>
<tr id="TBL-1-7-" class="odd" style="vertical-align:baseline;">
<td id="TBL-1-7-1" class="td11"
style="text-align: center; white-space: nowrap;">fet pfet</td>
<td id="TBL-1-7-2" class="td11"
style="text-align: center; white-space: nowrap;">4 25 5 26</td>
<td id="TBL-1-7-3" class="td11"
style="text-align: center; white-space: nowrap;">8 12</td>
<td id="TBL-1-7-4" class="td11"
style="text-align: center; white-space: nowrap;">Vdd#0</td>
<td id="TBL-1-7-5" class="td11"
style="text-align: center; white-space: nowrap;">In 4 <span
class="ptmb7t-x-x-120">P1 </span></td>
<td id="TBL-1-7-6" class="td11"
style="text-align: center; white-space: nowrap;">Vdd#0 4 0</td>
<td id="TBL-1-7-7" class="td11"
style="text-align: center; white-space: nowrap;">Mid1 4 0</td>
</tr>
<tr class="even hline">
<td><hr /></td>
<td><hr /></td>
<td><hr /></td>
<td><hr /></td>
<td><hr /></td>
<td><hr /></td>
<td><hr /></td>
</tr>
<tr id="TBL-1-8-" class="odd" style="vertical-align:baseline;">
<td id="TBL-1-8-1" class="td11"
style="text-align: center; white-space: nowrap;"></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

<span class="id">Table 1: </span><span class="content">The transistor
section of <span class="ptmb7t-x-x-120">tut8l.ext</span>.</span>

In addition to having gate, source, and drain terminals, MOSFET
transistors also have a substrate terminal. By default, this terminal is
connected to a global node that depends on the transistor’s type. For
example, p-channel transistors might have a substrate terminal of <span
class="ptmb7t-x-x-120">Vdd!</span>, while n-channel transistors would
have one of <span class="ptmb7t-x-x-120">GND!</span>. However, when a
transistor is surrounded by explicit “well” material (as defined in the
technology file), Magic will override the default substrate terminal
with the node to which the well material is connected. This has several
advantages: it allows simulation of analog circuits in which wells are
biased to different potentials, and it provides a form of checking to
ensure that wells in a CMOS process are explicitly tied to the
appropriate DC voltage.

Transistor substrate nodes are discovered by the extractor only if the
transistor and the overlapping well layer are in the same cell. If they
appear in different cells, the transistor’s substrate terminal will be
set to the default for the type of transistor.

Load the cell <span class="ptmb7t-x-x-120">tut8l</span>, extract it, and
look at the file <span class="ptmb7t-x-x-120">tut8l.ext</span>. Table 1
shows the lines for the six transistors in the file. You’ll notice that
the substrate terminals (the <span class="ptmri7t-x-x-120">Subs
</span>column) for all transistors are different. Since each transistor
in this design has a different gate attribute attached to it (shown in
bold in the table, <span class="ptmri7t-x-x-120">e.g.</span>, <span
class="ptmb7t-x-x-120">N1</span>, <span
class="ptmb7t-x-x-120">P2</span>, etc), we’ll use them in the following
discussion.

The simplest two transistors are <span class="ptmb7t-x-x-120">N3
</span>and <span class="ptmb7t-x-x-120">P3</span>, which don’t appear in
any explicitly drawn wells. The substrate terminals for these are <span
class="ptmb7t-x-x-120">GND! </span>and <span class="ptmb7t-x-x-120">Vdd!
</span>respectively, since that’s what the technology file says is the
default for the two types of transistors. <span
class="ptmb7t-x-x-120">N1 </span>and <span class="ptmb7t-x-x-120">P1
</span>are standard transistors that lie in wells tied to the ground and
power rails, labelled in this cell as <span
class="ptmb7t-x-x-120">Vss#0</span> and <span
class="ptmb7t-x-x-120">Vdd#0 </span>respectively. (They’re not labelled
<span class="ptmb7t-x-x-120">GND! </span>and <span
class="ptmb7t-x-x-120">Vdd! </span>so you’ll see the difference between
<span class="ptmb7t-x-x-120">N1 </span>and <span
class="ptmb7t-x-x-120">N3</span>). <span class="ptmb7t-x-x-120">P2
</span>lies in a well that is tied to a different bias voltage, <span
class="ptmb7t-x-x-120">VBias</span>, such as might occur in an analog
design. Finally, <span class="ptmb7t-x-x-120">N2 </span>is in a well
that isn’t tied to any wire. The substrate node appears as <span
class="ptmb7t-x-x-120">Float </span>because that’s the label that was
attached to the well surrounding <span class="ptmb7t-x-x-120">N2</span>.

The ability to extract transistor substrate nodes allows you to perform
a simple check for whether or not transistors are in properly connected
(<span class="ptmri7t-x-x-120">e.g.</span>, grounded) wells. In a p-well
CMOS process, for example, you might set the default substrate node for
n-channel transistors to be some distinguished global node other than
ground, <span class="ptmri7t-x-x-120">e.g.</span>, <span
class="ptmb7t-x-x-120">NSubstrateNode!</span>. You could then extract
the circuit, flatten it using <span
class="ptmri7t-x-x-120">ext2spice</span> (1) (which preserves substrate
nodes, unlike <span class="ptmri7t-x-x-120">ext2sim</span> (1) which
ignores them), and look at the substrate node fields of all the
n-channel transistors: if there were any whose substrate nodes weren’t
connected to <span class="ptmb7t-x-x-120">GND!</span>, then these
transistors appear either outside of any explicit well (their substrate
nodes will be the default of <span
class="ptmb7t-x-x-120">NSubstrateNode</span>), or in a well that isn’t
tied to <span class="ptmb7t-x-x-120">GND! </span>with a substrate
contact.

### <span class="titlemark">6 </span> <span id="x1-160006"></span>Extraction styles

Magic usually knows several different ways to extract a circuit from a
given layout. Each of these ways is called a <span
class="ptmri7t-x-x-120">style</span>. Different styles can be used to
handle different fabrication facilities, which may differ in the
parameters they have for parasitic capacitance and resistance. For a
scalable technology, such as the default <span
class="ptmb7t-x-x-120">scmos</span>, there can be a different extraction
style for each scale factor. The exact number and nature of the
extraction styles is described in the technology file that Magic reads
when it starts. At any given time, there is one current extraction
style.

To print a list of the extraction styles available, type the command

<table class="tabbing" data-cellpadding="0" data-border="0">
<tbody>
<tr class="odd tabbing" style="vertical-align:baseline;">
<td class="tabbing"><span class="ptmb7t-x-x-120">:extract
style</span>.</td>
</tr>
</tbody>
</table>

The <span class="ptmb7t-x-x-120">scmos </span>technology currently has
the styles <span class="ptmb7t-x-x-120">lambda=1.5</span>, <span
class="ptmb7t-x-x-120">lambda=1.0</span>, and <span
class="ptmb7t-x-x-120">lambda=0.6</span>, though this changes over time
as technology evolves. To change the extraction style to <span
class="ptmri7t-x-x-120">style</span>, use the command

<table class="tabbing" data-cellpadding="0" data-border="0">
<tbody>
<tr class="odd tabbing" style="vertical-align:baseline;">
<td class="tabbing"><span class="ptmb7t-x-x-120">:extract
style</span><span class="ptmri7t-x-x-120">style</span></td>
</tr>
</tbody>
</table>

Each style has a specific scale factor between Magic units and physical
units (<span class="ptmri7t-x-x-120">e.g.</span>, microns); you can’t
use a particular style with a different scale factor. To change the
scalefactor, you’ll have to edit the appropriate style in the <span
class="ptmb7t-x-x-120">extract </span>section of the technology file.
This process is described in “Magic Maintainer’s Manual \#2: The
Technology File.”

### <span class="titlemark">7 </span> <span id="x1-170007"></span>Flattening Extracted Circuits

Unfortunately, very few tools exist to take advantage of the <span
class="ptmri7t-x-x-120">ext</span> (5) format files produced by Magic’s
extractor. To use these files for simulation or timing analysis, you
will most likely need to convert them to a flattened format, such as
<span class="ptmri7t-x-x-120">sim</span> (5) or <span
class="ptmri7t-x-x-120">spice</span> (5).

There are several programs for flattening <span
class="ptmri7t-x-x-120">ext</span> (5) files. <span
class="ptmri7t-x-x-120">Ext2sim</span> (1) produces <span
class="ptmri7t-x-x-120">sim</span> (5) files suitable for use with <span
class="ptmri7t-x-x-120">crystal</span> (1), <span
class="ptmri7t-x-x-120">esim</span> (1), or <span
class="ptmri7t-x-x-120">rsim</span> (1). <span
class="ptmri7t-x-x-120">Ext2spice</span> (1) is used to produce <span
class="ptmri7t-x-x-120">spice</span> (5) files for use with the
circuit-level simulator <span class="ptmri7t-x-x-120">spice</span> (1).
Finally, <span class="ptmri7t-x-x-120">extcheck</span> (1) can be used
to perform connectivity checking and will summarize the number of
flattened nodes, transistors, capacitors, and resistors in a circuit.
All of these programs make use of a library known as <span
class="ptmri7t-x-x-120">extflat</span> (3), so the conventions for each
and the checks they perform are virtually identical. The documentation
for <span class="ptmri7t-x-x-120">extcheck </span>covers the options
common to all of these programs.

To see how <span class="ptmri7t-x-x-120">ext2sim </span>works, load the
cell <span class="ptmb7t-x-x-120">tut8n </span>and expand all the <span
class="ptmb7t-x-x-120">tutm </span>subcells. Notice how the <span
class="ptmb7t-x-x-120">GND! </span>bus is completely wired, but the
<span class="ptmb7t-x-x-120">Vdd! </span>bus is in three disconnected
pieces. Now extract everything with <span
class="ptmb7t-x-x-120">:extract</span>, then exit Magic and run <span
class="ptmb7t-x-x-120">ext2sim tut8n</span>. You’ll see the following
sort of output:

<table class="tabbing" data-cellpadding="0" data-border="0">
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd tabbing" style="vertical-align:baseline;">
<td class="tabbing"><span class="pcrr7t-x-x-120">*** Global name Vdd!
not fully connected:</span><br />
<span class="pcrr7t-x-x-120">One portion contains the
names:</span><br />
<span class="pcrr7t-x-x-120">left/Vdd!</span><br />
<span class="pcrr7t-x-x-120">The other portion contains the
names:</span><br />
<span class="pcrr7t-x-x-120">center/Vdd!</span><br />
<span class="pcrr7t-x-x-120">I’m merging the two pieces into a single
node, but you</span><br />
<span class="pcrr7t-x-x-120">should be sure eventually to connect them
in the layout.</span><br />
<br />
<span class="pcrr7t-x-x-120">*** Global name Vdd! not fully
connected:</span><br />
<span class="pcrr7t-x-x-120">One portion contains the
names:</span><br />
<span class="pcrr7t-x-x-120">left/Vdd!</span><br />
<span class="pcrr7t-x-x-120">center/Vdd!</span><br />
<span class="pcrr7t-x-x-120">The other portion contains the
names:</span><br />
<span class="pcrr7t-x-x-120">right/Vdd!</span><br />
<span class="pcrr7t-x-x-120">I’m merging the two pieces into a single
node, but you</span><br />
<span class="pcrr7t-x-x-120">should be sure eventually to connect them
in the layout.</span><br />
<br />
<span class="pcrr7t-x-x-120">Memory used: 56k</span></td>
</tr>
</tbody>
</table>

The warning messages are telling you that the global name <span
class="ptmb7t-x-x-120">Vdd! </span>isn’t completely wired in the layout.
The flattener warns you, but goes ahead and connects the pieces together
anyway to allow you to simulate the circuit as though it had been
completely wired. The output of <span class="ptmri7t-x-x-120">ext2sim
</span>will be three files: <span
class="ptmb7t-x-x-120">tut8n.sim</span>, <span
class="ptmb7t-x-x-120">tut8n.al</span>, and <span
class="ptmb7t-x-x-120">tut8n.nodes</span>; see <span
class="ptmri7t-x-x-120">ext2sim</span> (1) or <span
class="ptmri7t-x-x-120">sim</span> (5) for more information on the
contents of these files. “<span class="ptmb7t-x-x-120">Magic Tutorial
\#11: Using RSIM with Magic</span>” explains how to use the output of
<span class="ptmri7t-x-x-120">ext2sim </span>with the switch-level
simulator, <span class="ptmri7t-x-x-120">rsim</span> (1).
