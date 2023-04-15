---
layout: post
title: tut11
math: true
---



* TOC
{:toc }

<span class="ptmb7t-x-x-172">Magic Tutorial \#11: Using IRSIM and RSIM
with Magic</span>  
<span class="ptmri7t-x-x-120">Michael Chow</span>  
<span class="ptmri7t-x-x-120">Mark Horowitz</span>  
Computer Systems Laboratory  
Center for Integrated Systems  
Stanford University  
Stanford, CA 94305  
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
Magic Tutorial #4: Cell Hierarchies<br />
Magic Tutorial #8: Circuit Extraction</td>
</tr>
</tbody>
</table>

<span class="ptmb7t-x-x-144">Commands introduced in this
tutorial:</span>

<table class="tabbing" data-cellpadding="0" data-border="0">
<tbody>
<tr class="odd tabbing" style="vertical-align:baseline;">
<td class="tabbing">:getnode, :rsim, :simcmd, :startrsim</td>
</tr>
</tbody>
</table>

<span class="ptmb7t-x-x-144">Macros introduced in this tutorial:</span>

<table class="tabbing" data-cellpadding="0" data-border="0">
<tbody>
<tr class="odd tabbing" style="vertical-align:baseline;">
<td class="tabbing"><span class="ptmri7t-x-x-120">(None)</span></td>
</tr>
</tbody>
</table>

### <span class="titlemark">1 </span> <span id="x1-10001"></span>Introduction

This tutorial explains how to use Magic’s interface to the switch-level
circuit simulators, RSIM and IRSIM. The interface is the same for both
these simulators and, except where noted, RSIM refers to IRSIM as well.
This interface eliminates the tedium of mapping node names to objects in
the layout and typing node names as RSIM input. It allows the user to
select nodes using the mouse and apply RSIM commands to them or to
display the node values determined by RSIM in the layout itself. You
should already be familiar with using both RSIM and Magic’s circuit
extractor. Section 2 describes how to prepare the files necessary to
simulate a circuit. Section 3 describes how to run RSIM interactively
under Magic. Section 4 explains how to determine the node names that
RSIM uses. Lastly, section 5 explains how to use the RSIM tool in Magic
to simulate a circuit.

### <span class="titlemark">2 </span> <span id="x1-20002"></span>Preparations for Simulation

Magic uses the RSIM input file when it simulates the circuit. Before
proceeding any further, make sure you have the correct versions of the
programs <span class="ptmb7t-x-x-120">ext2sim </span>and <span
class="ptmb7t-x-x-120">rsim </span>installed on your system. Important
changes have been made to these programs to support simulation within
Magic. To try out this tool on an example, copy all the <span
class="ptmb7t-x-x-120">tut11</span><span class="ptmbi7t-x-x-120">x
</span>cells to your current directory with the following command:

<table class="tabbing" data-cellpadding="0" data-border="0">
<tbody>
<tr class="odd tabbing" style="vertical-align:baseline;">
<td class="tabbing"><span class="ptmb7t-x-x-120">cp
~cad/lib/magic/tutorial/tut11* .</span></td>
</tr>
</tbody>
</table>

The <span class="ptmb7t-x-x-120">tut11a </span>cell is a simple 4-bit
counter using the Magic scmos technology file. Start Magic on the cell
<span class="ptmb7t-x-x-120">tut11a</span>, and extract the entire cell
using the command:

<table class="tabbing" data-cellpadding="0" data-border="0">
<tbody>
<tr class="odd tabbing" style="vertical-align:baseline;">
<td class="tabbing"><span class="ptmb7t-x-x-120">:extract
all</span></td>
</tr>
</tbody>
</table>

When this command completes, several <span class="ptmb7t-x-x-120">.ext
</span>files will be created in your current directory by the extractor.
The next step is to flatten the hierarchy into a single representation.
Return to the Unix c-shell by quitting Magic.

The program <span class="ptmb7t-x-x-120">ext2sim </span>is used to
flatten the hierarchy. Run this program from the C-shell by typing:

<table class="tabbing" data-cellpadding="0" data-border="0">
<tbody>
<tr class="odd tabbing" style="vertical-align:baseline;">
<td class="tabbing"><span class="ptmb7t-x-x-120">ext2sim -L -R -c 20
tut11a</span></td>
</tr>
</tbody>
</table>

This program will create the file <span
class="ptmb7t-x-x-120">tut11a.sim </span>in your current directory.

If you are running IRSIM, the <span class="ptmb7t-x-x-120">tut11a.sim
</span>can be used directly as input to the simulator and you should
skip the next step. Instead, if you will be using RSIM, the last step is
to create the binary representation of the flattened hierarchy by using
the program <span class="ptmb7t-x-x-120">presim</span>. To do this,
type:

<table class="tabbing" data-cellpadding="0" data-border="0">
<tbody>
<tr class="odd tabbing" style="vertical-align:baseline;">
<td class="tabbing"><span class="ptmb7t-x-x-120">presim tut11a.sim
tut11a.rsm ~cad/lib/scmos100.prm -nostack -nodrops</span></td>
</tr>
</tbody>
</table>

The third file is the parameter file used by presim for this circuit.
The convention at Stanford is to use the suffix <span
class="ptmri7t-x-x-120">.rsm </span>when naming the RSIM input file. The
file <span class="ptmb7t-x-x-120">tut11a.rsm </span>can also be used as
input for running RSIM alone.

### <span class="titlemark">3 </span> <span id="x1-30003"></span>Using RSIM

Re-run Magic again to edit the cell <span
class="ptmb7t-x-x-120">tut11a</span>. We’ll first learn how to run RSIM
in interactive mode under Magic. To simulate the circuit of tut11a,
using IRSIM type the command:

<table class="tabbing" data-cellpadding="0" data-border="0">
<tbody>
<tr class="odd tabbing" style="vertical-align:baseline;">
<td class="tabbing"><span class="ptmb7t-x-x-120">:rsim scmos100.prm
tut11a.sim</span></td>
</tr>
</tbody>
</table>

To simulate the circuit of tut11a, using RSIM type the command:

<table class="tabbing" data-cellpadding="0" data-border="0">
<tbody>
<tr class="odd tabbing" style="vertical-align:baseline;">
<td class="tabbing"><span class="ptmb7t-x-x-120">:rsim
tut11a.rsm</span></td>
</tr>
</tbody>
</table>

You should see the RSIM header displayed, followed by the standard RSIM
prompt (<span class="ptmb7t-x-x-120">rsim</span>&gt; or <span
class="ptmb7t-x-x-120">irsim</span>&gt;, depending on the simulator) in
place of the usual Magic prompt; this means keyboard input is now
directed to RSIM. This mode is very similar to running RSIM alone; one
difference is that the user can escape RSIM and then return to Magic.
Also, the mouse has no effect when RSIM is run interactively under
Magic.

Only one instance of RSIM may be running at any time under Magic. The
simulation running need not correspond to the Magic layout; however, as
we shall see later, they must correspond for the RSIM tool to work. All
commands typed to the RSIM prompt should be RSIM commands. We’ll first
run RSIM, then escape to Magic, and then return back to RSIM. Type the
RSIM command

<table class="tabbing" data-cellpadding="0" data-border="0">
<tbody>
<tr class="odd tabbing" style="vertical-align:baseline;">
<td class="tabbing"><span class="ptmb7t-x-x-120">@
tut11a.cmd</span></td>
</tr>
</tbody>
</table>

to initialize the simulation. (Note there is a “ ” after the @.) Now
type <span class="ptmb7t-x-x-120">c </span>to clock the circuit. You
should see some information about some nodes displayed, followed by the
time. Set two of the nodes to a logic “1” by typing <span
class="ptmb7t-x-x-120">h RESET</span><span class="ptmb7t-x-x-120">\_B
hold</span>. Step the clock again by typing <span
class="ptmb7t-x-x-120">c</span>, and RSIM should show that these two
nodes now have the value “1”.

You can return to Magic without quitting RSIM and then later return to
RSIM in the same state in which it was left. Escape to Magic by typing:

<table class="tabbing" data-cellpadding="0" data-border="0">
<tbody>
<tr class="odd tabbing" style="vertical-align:baseline;">
<td class="tabbing"><span class="ptmb7t-x-x-120">.</span></td>
</tr>
</tbody>
</table>

(a single period) to the RSIM prompt. Next, type a few Magic commands to
show you’re really back in Magic (signified by the Magic prompt).

You can return to RSIM by typing the Magic command <span
class="ptmb7t-x-x-120">rsim </span>without any arguments. Type:

<table class="tabbing" data-cellpadding="0" data-border="0">
<tbody>
<tr class="odd tabbing" style="vertical-align:baseline;">
<td class="tabbing"><span class="ptmb7t-x-x-120">:rsim</span></td>
</tr>
</tbody>
</table>

The RSIM prompt will be displayed again, and you are now back in RSIM in
the state you left it in. Experiment with RSIM by typing some commands.
To quit RSIM and return to Magic, type:

<table class="tabbing" data-cellpadding="0" data-border="0">
<tbody>
<tr class="odd tabbing" style="vertical-align:baseline;">
<td class="tabbing"><span class="ptmb7t-x-x-120">q</span></td>
</tr>
</tbody>
</table>

in response to the RSIM prompt. You’ll know you’re back in Magic when
the Magic prompt is redisplayed. If you should interrupt RSIM (typing a
control-C), you’ll probably kill it and then have to restart it. RSIM
running standalone will also be killed if you interrupt it. If you
interrupt IRSIM (typing a control-C), the simulator will abort whatever
it’s doing (a long simulation run, for example) and return to the
command interpreter by prompting again with <span
class="ptmb7t-x-x-120">irsim</span>&gt;.

### <span class="titlemark">4 </span> <span id="x1-40004"></span>Node Names

It’s easy to determine node names under Magic. First, locate the red
square region in the middle right side of the circuit. Move the cursor
over this region and select it by typing <span
class="ptmb7t-x-x-120">s</span>. To find out the name for this node,
type:

<table class="tabbing" data-cellpadding="0" data-border="0">
<tbody>
<tr class="odd tabbing" style="vertical-align:baseline;">
<td class="tabbing"><span class="ptmb7t-x-x-120">:getnode</span></td>
</tr>
</tbody>
</table>

Magic should print that the node name is <span
class="ptmri7t-x-x-120">RESET</span><span
class="ptmri7t-x-x-120">\_B</span>. The command <span
class="ptmb7t-x-x-120">getnode </span>prints the names of all nodes in
the current selection. Move the cursor over the square blue region in
the upper right corner and add this node to the current selection by
typing <span class="ptmb7t-x-x-120">S</span>. Type <span
class="ptmb7t-x-x-120">:getnode </span>again, and Magic should print the
names of two nodes; the blue node is named <span
class="ptmri7t-x-x-120">hold</span>. You can also print aliases for the
selected nodes. Turn on name-aliasing by typing:

<table class="tabbing" data-cellpadding="0" data-border="0">
<tbody>
<tr class="odd tabbing" style="vertical-align:baseline;">
<td class="tabbing"><span class="ptmb7t-x-x-120">:getnode alias
on</span></td>
</tr>
</tbody>
</table>

Select the red node again, and type <span
class="ptmb7t-x-x-120">:getnode</span>. Several names will be printed;
the last name printed is the one RSIM uses, so you should use this name
for RSIM. Note that <span class="ptmb7t-x-x-120">getnode </span>is not
guaranteed to print all aliases for a node. Only those alises generated
when the RSIM node name is computed are printed. However, most of the
alaiases will usually be printed. Printing aliases is also useful to
monitor the name search, since <span class="ptmb7t-x-x-120">getnode
</span>can take several seconds on large nodes. Turn off aliasing by
typing:

<table class="tabbing" data-cellpadding="0" data-border="0">
<tbody>
<tr class="odd tabbing" style="vertical-align:baseline;">
<td class="tabbing"><span class="ptmb7t-x-x-120">:getnode alias
off</span></td>
</tr>
</tbody>
</table>

<span class="ptmb7t-x-x-120">getnode </span>works by extracting a single
node. Consequently, it can take a long time to compute the name for
large nodes, such as <span class="ptmri7t-x-x-120">Vdd </span>or <span
class="ptmri7t-x-x-120">GND</span>. Select the horizontal blue strip on
top of the circuit and run <span class="ptmb7t-x-x-120">:getnode
</span>on this. You’ll find that this will take about six seconds for
<span class="ptmb7t-x-x-120">getnode </span>to figure out that this is
<span class="ptmri7t-x-x-120">Vdd</span>. You can interrupt <span
class="ptmb7t-x-x-120">getnode </span>by typing <span
class="ptmb7t-x-x-120">̂C </span>(control-C), and <span
class="ptmb7t-x-x-120">getnode </span>will return the “best” name found
so far. There is no way to tell if this is an alias or the name RSIM
expects unless <span class="ptmb7t-x-x-120">getnode </span>is allowed to
complete. To prevent these long name searches, you can tell <span
class="ptmb7t-x-x-120">getnode </span>to quit its search when certain
names are encountered. Type:

<table class="tabbing" data-cellpadding="0" data-border="0">
<tbody>
<tr class="odd tabbing" style="vertical-align:baseline;">
<td class="tabbing"><span class="ptmb7t-x-x-120">:getnode abort
Vdd</span></td>
</tr>
</tbody>
</table>

Select the blue strip on top of the circuit and type <span
class="ptmb7t-x-x-120">:getnode</span>. You’ll notice that the name was
found very quickly this time, and <span class="ptmb7t-x-x-120">getnode
</span>tells you it aborted the search of <span
class="ptmri7t-x-x-120">Vdd</span>. The name returned may be an alias
instead of the the one RSIM expects. In this example, the abort option
to <span class="ptmb7t-x-x-120">getnode</span> will abort the name
search on any name found where the last component of the node name is
<span class="ptmri7t-x-x-120">Vdd</span>. That is, <span
class="ptmb7t-x-x-120">getnode </span>will stop if a name such as
“miasma/crock/<span class="ptmri7t-x-x-120">Vdd</span>” or “hooha/<span
class="ptmri7t-x-x-120">Vdd</span>” is found.

You can abort the search on more than one name; now type <span
class="ptmb7t-x-x-120">:getnode abort GND</span>. Select the bottom
horizontal blue strip in the layout, and type <span
class="ptmb7t-x-x-120">:getnode</span>. The search will end almost
immediately, since this node is <span
class="ptmri7t-x-x-120">GND</span>. <span class="ptmb7t-x-x-120">getnode
</span>will now abort any node name search when either <span
class="ptmri7t-x-x-120">Vdd </span>or <span class="ptmri7t-x-x-120">GND
</span>is found. The search can be aborted on any name; just supply the
name as an argument to <span class="ptmb7t-x-x-120">getnode
abort</span>. Remember that only the last part of the name counts when
aborting the name search. To cancel all name aborts and resume normal
name searches, type:

<table class="tabbing" data-cellpadding="0" data-border="0">
<tbody>
<tr class="odd tabbing" style="vertical-align:baseline;">
<td class="tabbing"><span class="ptmb7t-x-x-120">:getnode
abort</span></td>
</tr>
</tbody>
</table>

<span class="ptmb7t-x-x-120">getnode </span>will no longer abort the
search on any names, and it will churn away unless interrupted by the
user.

### <span class="titlemark">5 </span> <span id="x1-50005"></span>RSIM Tool

You can also use the mouse to help you run RSIM under Magic. Instead of
typing node names, you can just select nodes with the mouse, tell RSIM
what to do with these nodes, and let Magic do the rest. Change tools by
typing:

<table class="tabbing" data-cellpadding="0" data-border="0">
<tbody>
<tr class="odd tabbing" style="vertical-align:baseline;">
<td class="tabbing"><span class="ptmb7t-x-x-120">:tool rsim</span></td>
</tr>
</tbody>
</table>

or hit the space bar until the cursor changes to a pointing hand. The
RSIM tool is active when the cursor is this hand. The left and right
mouse buttons have the same have the same function as the box tool. You
use these buttons along with the select command to select the nodes. The
middle button is different from the box tool. Clicking the middle button
will cause all nodes in the selection to have their logical values
displayed in the layout and printed in the text window. We need to have
RSIM running in order to use this tool. Start RSIM by typing:

<table class="tabbing" data-cellpadding="0" data-border="0">
<tbody>
<tr class="odd tabbing" style="vertical-align:baseline;">
<td class="tabbing"><span class="ptmb7t-x-x-120">:startrsim
tut11a.rsm</span></td>
</tr>
</tbody>
</table>

The <span class="ptmb7t-x-x-120">.rsm </span>file you simulate must
correspond to the root cell of the layout. If not, Magic will generate
node names that RSIM will not understand and things won’t work properly.
If any paint is changed in the circuit, the circuit must be re-extracted
and a new <span class="ptmb7t-x-x-120">.rsm </span>file must be created
to reflect the changes in the circuit.

Magic will print the RSIM header, but you return to Magic instead of
remaining in RSIM. This is an alternate way of starting up RSIM, and it
is equivalent to the command <span class="ptmb7t-x-x-120">rsim
tut11a.rsm </span>and typing a period (<span
class="ptmb7t-x-x-120">.</span>) to the RSIM prompt, escaping to Magic.
We need to initialize RSIM, so get to RSIM by typing <span
class="ptmb7t-x-x-120">:rsim </span>and you’ll see the RSIM prompt
again. As before, type <span class="ptmb7t-x-x-120">@ tut11a.cmd
</span>to the RSIM prompt to initialize everything. Type a period (<span
class="ptmb7t-x-x-120">.</span>) to return to Magic. We are now ready to
use the RSIM tool.

As mentioned earlier, <span class="ptmb7t-x-x-120">tut11a </span>is a
4-bit counter. We’ll reset the counter and then step it using the RSIM
tool. Locate the square blue area on the top right corner of the
circuit. Place the cursor over this region and select it. Now click the
middle button, and the RSIM value for this node will be printed in both
the text window and in the layout. Magic/RSIM will report that the node
is named <span class="ptmri7t-x-x-120">hold </span>and that its current
value is <span class="ptmri7t-x-x-120">X</span>. You may not be able to
see the node value in the layout if you are zoomed out too far. Zoom in
closer about this node if necessary. Try selecting other nodes, singly
or in groups and click the middle button to display their values. This
is an easy way to probe nodes when debugging a circuit.

Select <span class="ptmri7t-x-x-120">hold </span>again (the blue
square). This node must be a “1” before resetting the circuit. Make sure
this is the only node in the current selection. Type:

<table class="tabbing" data-cellpadding="0" data-border="0">
<tbody>
<tr class="odd tabbing" style="vertical-align:baseline;">
<td class="tabbing"><span class="ptmb7t-x-x-120">:simcmd h</span></td>
</tr>
</tbody>
</table>

to set it to a “1”. Step the clock by typing:

<table class="tabbing" data-cellpadding="0" data-border="0">
<tbody>
<tr class="odd tabbing" style="vertical-align:baseline;">
<td class="tabbing"><span class="ptmb7t-x-x-120">:simcmd c</span></td>
</tr>
</tbody>
</table>

Click the middle button and you will see that the node has been set to a
“1.” The Magic command <span class="ptmb7t-x-x-120">simcmd </span>will
take the selected nodes and use them as RSIM input. These uses of <span
class="ptmb7t-x-x-120">simcmd </span>are like typing the RSIM commands
<span class="ptmri7t-x-x-120">h hold </span>followed by <span
class="ptmri7t-x-x-120">c</span>. The arguments given to <span
class="ptmb7t-x-x-120">simcmd </span>are normal RSIM commands, and <span
class="ptmb7t-x-x-120">simcmd </span>will apply the specified RSIM
command to each node in the current selection. Try RSIM commands on this
node (such as <span class="ptmri7t-x-x-120">? </span>or <span
class="ptmri7t-x-x-120">d</span>) by using the command as an argument to
<span class="ptmb7t-x-x-120">simcmd</span>.

You can enter RSIM interactively at any time by simply typing <span
class="ptmb7t-x-x-120">:rsim</span>. To continue using the RSIM tool,
escape to Magic by typing a period (<span
class="ptmb7t-x-x-120">.</span>) to the RSIM prompt.

The node <span class="ptmri7t-x-x-120">RESET</span><span
class="ptmri7t-x-x-120">\_B </span>must be set to a “0”. This node is
the red square area at the middle right of the circuit. Place the cursor
over this node and select it. Type the Magic commands <span
class="ptmb7t-x-x-120">:simcmd l </span>followed by <span
class="ptmb7t-x-x-120">:simcmd c </span>to set the selected node to a
“0”. Click the middle mouse button to check that this node is now “0”.
Step the clock once more to ensure the counter is reset. Do this using
the <span class="ptmb7t-x-x-120">:simcmd c</span> command.

The outputs of this counter are the four vertical purple strips at the
bottom of the circuit. Zoom in if necessary, select each of these nodes,
and click the middle button to check that all are “0”. Each of these
four nodes is labeled <span class="ptmri7t-x-x-120">bit</span><span
class="ptmri7t-x-x-120">\_x</span>. If they are all not “0”, check the
circuit to make sure <span class="ptmri7t-x-x-120">hold=1 </span>and
<span class="ptmri7t-x-x-120">RESET</span><span
class="ptmri7t-x-x-120">\_B=0</span>. Assuming these nodes are at their
correct value, you can now simulate the counter. Set <span
class="ptmri7t-x-x-120">RESET</span><span class="ptmri7t-x-x-120">\_B
</span>to a “1” by selecting it (the red square) and then typing <span
class="ptmb7t-x-x-120">:simcmd h</span>. Step the clock by typing <span
class="ptmb7t-x-x-120">:simcmd c</span>. Using the same procedure, set
the node <span class="ptmri7t-x-x-120">hold </span>(the blue square) to
a “0”.

We’ll watch the output bits of this counter as it runs. Place the box
around all four outputs (purple strips at the bottom) and zoom in so
their labels are visible. Select one of the outputs by placing the
cursor over it and typing <span class="ptmb7t-x-x-120">s</span>. Add the
other three outputs to the selection by placing the cursor over each and
typing <span class="ptmb7t-x-x-120">S</span>. These four nodes should be
the only ones in the selection. Click the middle mouse button to display
the node values. Step the clock by typing <span
class="ptmb7t-x-x-120">:simcmd c</span>. Click the middle button again
to check the nodes. Repeat stepping the clock and displaying the outputs
several times, and you’ll see the outputs sequence as a counter. If you
also follow the text on the screen, you’ll also see that the outputs are
also being watched.

You may have noticed that the results are printed very quickly if the
middle button is clicked a second time without changing the selection.
This is because the node names do not have to be recomputed if the
selection remains unchanged. Thus, you can increase the performance of
this tool by minimizing selection changes. This can be accomplished by
adding other nodes to the current selection that you are intending to
check.

To erase all the RSIM value labels from the layout, clear the selection
by typing:

<table class="tabbing" data-cellpadding="0" data-border="0">
<tbody>
<tr class="odd tabbing" style="vertical-align:baseline;">
<td class="tabbing"><span class="ptmb7t-x-x-120">:select
clear</span></td>
</tr>
</tbody>
</table>

and then click the middle mouse button. The RSIM labels do not affect
the cell modified flag, nor will they be written in the <span
class="ptmb7t-x-x-120">.mag </span>file. When you’re finished using
RSIM, resume RSIM by typing <span class="ptmb7t-x-x-120">:rsim
</span>and then quit it by typing a <span class="ptmb7t-x-x-120">q
</span>to the RSIM prompt. Quitting Magic before quitting RSIM will also
quit RSIM.

We’ve used a few macros to lessen the typing necessary for the RSIM
tool. The ones commonly used are:

<table class="tabbing" data-cellpadding="0" data-border="0">
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd tabbing" style="vertical-align:baseline;">
<td class="tabbing"><span class="ptmb7t-x-x-120">:macro h “simcmd
h”</span><br />
<span class="ptmb7t-x-x-120">:macro l “simcmd l”</span><br />
<span class="ptmb7t-x-x-120">:macro k “simcmd c”</span></td>
</tr>
</tbody>
</table>
