---
layout: post
title: 01 What is Magic
math: true
---



* TOC
{:toc }

<span class="ptmb7t-x-x-172">Magic Tutorial \#1: Getting
Started</span>  
<span class="ptmri7t-x-x-120">John Ousterhout</span>  
Computer Science Division  
Electrical Engineering and Computer Sciences  
University of California  
Berkeley, CA 94720  
<span class="ptmri7t-x-x-120">(Updated by others, too.)</span>  
This tutorial corresponds to Magic version 7.  

## <span class="titlemark">1 </span> <span id="x1-10001"></span>What is Magic?

Magic is an interactive system for creating and modifying VLSI circuit
layouts. With Magic, you use a color graphics display and a mouse or
graphics tablet to design basic cells and to combine them hierarchically
into large structures. Magic is different from other layout editors you
may have used. The most important difference is that Magic is more than
just a color painting tool: it understands quite a bit about the nature
of circuits and uses this information to provide you with additional
operations. For example, Magic has built-in knowledge of layout rules;
as you are editing, it continuously checks for rule violations. Magic
also knows about connectivity and transistors, and contains a built-in
hierarchical circuit extractor. Magic also has a <span
class="ptmri7t-x-x-120">plow </span>operation that you can use to
stretch or compact cells. Lastly, Magic has routing tools that you can
use to make the global interconnections in your circuits.

Magic is based on the Mead-Conway style of design. This means that it
uses simplified design rules and circuit structures. The simplifications
make it easier for you to design circuits and permit Magic to provide
powerful assistance that would not be possible otherwise. However, they
result in slightly less dense circuits than you could get with more
complex rules and structures. For example, Magic permits only <span
class="ptmri7t-x-x-120">Manhattan </span>designs (those whose edges are
vertical or horizontal). Circuit designers tell us that our conservative
design rules cost 5-10% in density. We think that the density sacrifice
is compensated for by reduced design time.

<span id="x1-10011"></span>

<table id="TBL-1" class="tabular" data-rules="groups">
<tbody>
<tr class="odd hline">
<td><hr /></td>
</tr>
<tr id="TBL-1-1-" class="even" style="vertical-align:baseline;">
<td id="TBL-1-1-1" class="td11"
style="text-align: left; white-space: nowrap;">Magic Tutorial #1:
Getting Started</td>
</tr>
<tr id="TBL-1-2-" class="odd" style="vertical-align:baseline;">
<td id="TBL-1-2-1" class="td11"
style="text-align: left; white-space: nowrap;">Magic Tutorial #2: Basic
Painting and Selection</td>
</tr>
<tr id="TBL-1-3-" class="even" style="vertical-align:baseline;">
<td id="TBL-1-3-1" class="td11"
style="text-align: left; white-space: nowrap;">Magic Tutorial #3:
Advanced Painting (Wiring and Plowing)</td>
</tr>
<tr id="TBL-1-4-" class="odd" style="vertical-align:baseline;">
<td id="TBL-1-4-1" class="td11"
style="text-align: left; white-space: nowrap;">Magic Tutorial #4: Cell
Hierarchies</td>
</tr>
<tr id="TBL-1-5-" class="even" style="vertical-align:baseline;">
<td id="TBL-1-5-1" class="td11"
style="text-align: left; white-space: nowrap;">Magic Tutorial #5:
Multiple Windows</td>
</tr>
<tr id="TBL-1-6-" class="odd" style="vertical-align:baseline;">
<td id="TBL-1-6-1" class="td11"
style="text-align: left; white-space: nowrap;">Magic Tutorial #6:
Design-Rule Checking</td>
</tr>
<tr id="TBL-1-7-" class="even" style="vertical-align:baseline;">
<td id="TBL-1-7-1" class="td11"
style="text-align: left; white-space: nowrap;">Magic Tutorial #7:
Netlists and Routing</td>
</tr>
<tr id="TBL-1-8-" class="odd" style="vertical-align:baseline;">
<td id="TBL-1-8-1" class="td11"
style="text-align: left; white-space: nowrap;">Magic Tutorial #8:
Circuit Extraction</td>
</tr>
<tr id="TBL-1-9-" class="even" style="vertical-align:baseline;">
<td id="TBL-1-9-1" class="td11"
style="text-align: left; white-space: nowrap;">Magic Tutorial #9: Format
Conversion for CIF and Calma</td>
</tr>
<tr id="TBL-1-10-" class="odd" style="vertical-align:baseline;">
<td id="TBL-1-10-1" class="td11"
style="text-align: left; white-space: nowrap;">Magic Tutorial #10: The
Interactive Route</td>
</tr>
<tr id="TBL-1-11-" class="even" style="vertical-align:baseline;">
<td id="TBL-1-11-1" class="td11"
style="text-align: left; white-space: nowrap;">Magic Tutorial #11: Using
RSIM with Magic</td>
</tr>
<tr class="odd hline">
<td><hr /></td>
</tr>
<tr id="TBL-1-12-" class="even" style="vertical-align:baseline;">
<td id="TBL-1-12-1" class="td11"
style="text-align: left; white-space: nowrap;">Magic Maintainer’s Manual
#1: Hints for System Maintainers</td>
</tr>
<tr id="TBL-1-13-" class="odd" style="vertical-align:baseline;">
<td id="TBL-1-13-1" class="td11"
style="text-align: left; white-space: nowrap;">Magic Maintainer’s Manual
#2: The Technology File</td>
</tr>
<tr id="TBL-1-14-" class="even" style="vertical-align:baseline;">
<td id="TBL-1-14-1" class="td11"
style="text-align: left; white-space: nowrap;">Magic Maintainer’s Manual
#3: Display Styles, Color Maps, and Glyphs</td>
</tr>
<tr id="TBL-1-15-" class="odd" style="vertical-align:baseline;">
<td id="TBL-1-15-1" class="td11"
style="text-align: left; white-space: nowrap;">Magic Maintainer’s Manual
#4: Using Magic Under X Windows</td>
</tr>
<tr class="even hline">
<td><hr /></td>
</tr>
<tr id="TBL-1-16-" class="odd" style="vertical-align:baseline;">
<td id="TBL-1-16-1" class="td11"
style="text-align: left; white-space: nowrap;">Magic Technology Manual
#1: NMOS</td>
</tr>
<tr id="TBL-1-17-" class="even" style="vertical-align:baseline;">
<td id="TBL-1-17-1" class="td11"
style="text-align: left; white-space: nowrap;">Magic Technology Manual
#2: SCMOS</td>
</tr>
<tr class="odd hline">
<td><hr /></td>
</tr>
<tr id="TBL-1-18-" class="even" style="vertical-align:baseline;">
<td id="TBL-1-18-1" class="td11"
style="text-align: left; white-space: nowrap;"></td>
</tr>
</tbody>
</table>

<span class="id">Table 1: </span><span class="content">The Magic
tutorials, maintenance manuals, and technology manuals.</span>

## <span class="titlemark">2 </span> <span id="x1-20002"></span>How to Get Help and Report Problems

There are several ways you can get help about Magic. If you are trying
to learn about the system, you should start off with the Magic
tutorials, of which this is the first. Each tutorial introduces a
particular set of facilities in Magic. There is also a set of manuals
intended for system maintainers. These describe things like how to
create new technologies. Finally, there is a set of technology manuals.
Each one of the technology manuals describes the features peculiar to a
particular technology, such as layer names and design rules.
Table [1](#x1-10011) lists all of the Magic manuals. The tutorials are
designed to be read while you are running Magic, so that you can try out
the new commands as they are explained. You needn’t read all the
tutorials at once; each tutorial lists the other tutorials that you
should read first.

The tutorials are not necessarily complete. Each one is designed to
introduce a set of facilities, but it doesn’t necessarily cover every
possibility. The ultimate authority on how Magic works is the reference
manual, which is a standard Unix <span class="ptmri7t-x-x-120">man
</span>page. The <span class="ptmri7t-x-x-120">man </span>page gives
concise and complete descriptions of all the Magic commands. Once you
have a general idea how a command works, the <span
class="ptmri7t-x-x-120">man </span>page is probably easier to consult
than the tutorial. However, the <span class="ptmri7t-x-x-120">man
</span>page may not make much sense until after you’ve read the
tutorial.

A third way of getting help is available on-line through Magic itself.
The <span class="ptmb7t-x-x-120">:help </span>command will print out one
line for each Magic command, giving the command’s syntax and an
extremely brief description of the command. This facility is useful if
you’ve forgotten the name or exact syntax of a command. After each
screenful of help information, <span class="ptmb7t-x-x-120">:help
</span>stops and prints “–More–”. If you type a space, the next
screenful of data will be output, and if you type <span
class="ptmb7t-x-x-120">q </span>the rest of the output will be skipped.
If you’re interested in information about a particular subject, you can
type

<table class="tabbing" data-cellpadding="0" data-border="0">
<tbody>
<tr class="odd tabbing" style="vertical-align:baseline;">
<td class="tabbing"><span class="ptmb7t-x-x-120">:help </span><span
class="ptmri7t-x-x-120">subject</span></td>
</tr>
</tbody>
</table>

This command will print out each command description that contains the
<span class="ptmri7t-x-x-120">subject </span>string.

If you have a question or problem that can’t be answered with any of the
above approaches, you may contact the Magic authors by sending mail to
<span class="pcrr7t-x-x-120">magic@ucbarpa.Berkeley.EDU</span>. This
will log your message in a file (so we can’t forget about it) and
forward the message to the Magic maintainers. Magic maintenance is a
mostly volunteer effort, so when you report a bug or ask a question,
<span class="ptmri7t-x-x-120">please </span>be specific. Obviously, the
more specific you are, the more likely we can answer your question or
reproduce the bug you found. We’ll tend to answer the specific bug
reports first, since they involve less time on our part. Try to describe
the exact sequence of events that led to the problem, what you expected
to happen, and what actually happened. If possible, find a small example
that reproduces the problem and send us the relevant (small!) files so
we can make it happen here. Or best of all, send us a bug fix along with
a small example of the problem.

## <span class="titlemark">3 </span> <span id="x1-30003"></span>Graphics Configuration

Magic can be run with different graphics hardware. The most common
configuration is to run Magic under X11 on a workstation. Another way to
run Magic is under SunView on a Sun workstation, or under OpenGL (in an
X11 environment) on an SGI workstation or Linux box with accelerated 3D
video hardware and drivers. Legacy code exists supporting AED graphics
terminals and X10 (the forerunner of X11). The rest of this section
concerns X11.

Before starting up magic, make sure that your <span
class="pcrr7t-x-x-120">DISPLAY </span>variable is set correctly. If you
are running magic and your X server on the same machine, set it to <span
class="pcrr7t-x-x-120">unix:0</span>:

<table class="tabbing" data-cellpadding="0" data-border="0">
<tbody>
<tr class="odd tabbing" style="vertical-align:baseline;">
<td class="tabbing"><span class="ptmb7t-x-x-120">setenv </span><span
class="pcrr7t-x-x-120">DISPLAY unix:0</span></td>
</tr>
</tbody>
</table>

The Magic window is an ordinary X window, and can be moved and resized
using the window manager.

For now, you can skip to the next major section: ”Running Magic”.

## <span class="titlemark">4 </span> <span id="x1-40004"></span>Advanced X Use

The X11 driver can read in window sizing and font preferences from your
<span class="ptmri7t-x-x-120">.Xdefaults </span>file. The following
specifications are recognized:

<table class="tabbing" data-cellpadding="0" data-border="0">
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd tabbing" style="vertical-align:baseline;">
<td class="tabbing"><span class="ptmb7t-x-x-120">magic.window:
</span>1000x600+10+10<br />
<span class="ptmb7t-x-x-120">magic.newwindow:
</span>300x300+400+100<br />
<span class="ptmb7t-x-x-120">magic.small: </span>helvetica8<br />
<span class="ptmb7t-x-x-120">magic.medium: </span>helvetica12<br />
<span class="ptmb7t-x-x-120">magic.large: </span>helvetica18<br />
<span class="ptmb7t-x-x-120">magic.xlarge: </span>helvetica24</td>
</tr>
</tbody>
</table>

<span class="ptmb7t-x-x-120">magic.window </span>is the size and
position of the initial window, while <span
class="ptmb7t-x-x-120">magic.newwindow </span>is the size and position
of subsequent windows. If these are left blank, you will be prompted to
give the window’s position and size. <span
class="ptmb7t-x-x-120">small</span>, <span
class="ptmb7t-x-x-120">medium</span>, <span
class="ptmb7t-x-x-120">large</span>, and <span
class="ptmb7t-x-x-120">xlarge </span>are various fonts magic uses for
labels. Some X11 servers read the <span
class="pcrr7t-x-x-120">.Xdefaults </span>file only when you initially
log in; you may have to run <span class="pcrr7t-x-x-120">xrdb
-load</span> <span class="pcrr7t-x-x-120">˜/.Xdefaults </span>for the
changes to take effect.

Under X11, Magic can run on a display of any depth for which there are
colormap and dstyle files. Monochrome, 4 bit, 6 bit, 7 bit, and 24 bit
files for MOS are distributed in this release. You can explicitly
specify how many planes Magic is to use by adding a suffix numeral
between 1 and 7 to “XWIND” when used with Magic’s “-d” option. For
example, “magic -d XWIND1” runs magic on a monochrome display and “magic
-d XWIND7” runs magic on a 7 plane display. If this number is not
specified, magic checks the depth of the display and picks the largest
number in the set <span class="cmsy-10x-x-120">{</span>1, 4, 6, 7, 16,
24<span class="cmsy-10x-x-120">} </span>that the display will support.
Another way to force the display type is to set an environment variable
called <span class="pcrr7t-x-x-120">MAGIC</span><span
class="pcrr7t-x-x-120">\_COLOR </span>to one of the strings “8bit”,
“16bit”, or “24bit”.

<span class="ptmbi7t-x-x-120">Linux note: </span>  
Magic’s “native” display (except when using the OpenGL interface) is the
8-bit PseudoColor visual type. 24-bit TrueColor visuals prevent Magic
from allocating colors for bit-plane logical operations, so the 24-bit
interface is visually somewhat sub-par, requiring stipple patterns on
all metal layers, for instance. Under Linux, a few (commercial) X
drivers will support 8-bit overlays on top of 24-bit TrueColor when
using 32-bit color. This is the ideal way to use magic, because the
colormap for the rest of the display is preserved when the cursor is
inside the Magic window. Otherwise, the X session may have to be started
using “<span class="pcrr7t-x-x-120">startx --bpp 8</span>” to force it
to use the 8-bit PseudoColor visual.

<span class="ptmbi7t-x-x-120">X11 remote usage note: </span>  
When running Magic remotely on an X terminal, the colormap allocation
may differ for the local machine compared to the remote machine. In some
cases, this can cause the background of magic to appear black, usually
with a black-on-black cursor. This is known to be true of X11 drivers
for Windows (such as PC-XWare), due to the way the Windows 8-bit
PseudoColor colormap is set up. This behavior can be corrected by
setting two environment variables on the remote machine as follows:

<table class="tabbing" data-cellpadding="0" data-border="0">
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd tabbing" style="vertical-align:baseline;">
<td class="tabbing"><span class="ptmb7t-x-x-120">setenv </span><span
class="pcrr7t-x-x-120">X</span><span
class="pcrr7t-x-x-120">_COLORMAP</span><span
class="pcrr7t-x-x-120">_BASE 128</span><br />
<span class="ptmb7t-x-x-120">setenv </span><span
class="pcrr7t-x-x-120">X</span><span
class="pcrr7t-x-x-120">_COLORMAP</span><span
class="pcrr7t-x-x-120">_DEFAULT 0</span><br />
</td>
</tr>
</tbody>
</table>

This causes Magic to avoid trying to allocate the first color in the
colormap, which under Windows is fixed as black.

## <span class="titlemark">5 </span> <span id="x1-50005"></span>Running Magic

From this point on, you should be sitting at a Magic workstation so you
can experiment with the program as you read the manuals. Starting up
Magic is usually pretty simple. Just log in and, if needed, start up
your favorite window system. Then type the shell command

<table class="tabbing" data-cellpadding="0" data-border="0">
<tbody>
<tr class="odd tabbing" style="vertical-align:baseline;">
<td class="tabbing"><span class="ptmb7t-x-x-120">magic tut1</span></td>
</tr>
</tbody>
</table>

<span class="ptmb7t-x-x-120">Tut1 </span>is the name of a library cell
that you will play with in this tutorial. At this point, several colored
rectangles should appear on the color display along with a white box and
a cursor. A message will be printed on the text display to tell you that
<span class="ptmb7t-x-x-120">tut1 </span>isn’t writable (it’s in a
read-only library), and a “&gt;” prompt should appear. If this has
happened, then you can skip the rest of this section (except for the
note below) and go directly to Section 5.

Note: in the tutorials, when you see things printed in boldface, for
example, <span class="ptmb7t-x-x-120">magic tut1 </span>from above, they
refer to things you type exactly, such as command names and file names.
These are usually case sensitive (<span class="ptmb7t-x-x-120">A
</span>is different from <span class="ptmb7t-x-x-120">a</span>). When
you see things printed in italics, they refer to classes of things you
might type. Arguments in square brackets are optional. For example, a
more complete description of the shell command for Magic is

<table class="tabbing" data-cellpadding="0" data-border="0">
<tbody>
<tr class="odd tabbing" style="vertical-align:baseline;">
<td class="tabbing"><span class="ptmb7t-x-x-120">magic </span>[<span
class="ptmri7t-x-x-120">file</span>]</td>
</tr>
</tbody>
</table>

You could type any file name for <span
class="ptmri7t-x-x-120">file</span>, and Magic would start editing that
file. It turns out that <span class="ptmb7t-x-x-120">tut1 </span>is just
a file in Magic’s cell library. If you didn’t type a file name, Magic
would load a new blank cell.

If things didn’t happen as they should have when you tried to run Magic,
any of several things could be wrong. If a message of the form “magic:
Command not found” appears on your screen it is because the shell
couldn’t find the Magic program. The most stable version of Magic is the
directory <span class="pcrr7t-x-x-120">˜cad/bin</span>, and the newest
public version is in <span class="pcrr7t-x-x-120">˜cad/new</span>. You
should make sure that both these directories are in your shell path.
Normally, <span class="pcrr7t-x-x-120">˜cad/new </span>should appear
before <span class="pcrr7t-x-x-120">˜cad/bin</span>. If this sounds like
gibberish, find a Unix hacker and have him or her explain to you about
paths. If worst comes to worst, you can invoke Magic by typing its full
name:

<table class="tabbing" data-cellpadding="0" data-border="0">
<tbody>
<tr class="odd tabbing" style="vertical-align:baseline;">
<td class="tabbing"><span class="ptmb7t-x-x-120">~cad/bin/magic
tut1</span></td>
</tr>
</tbody>
</table>

Another possible problem is that Magic might not know what kind of
display you are using. To solve this, use magic’s <span
class="ptmb7t-x-x-120">-d </span>flag:

<table class="tabbing" data-cellpadding="0" data-border="0">
<tbody>
<tr class="odd tabbing" style="vertical-align:baseline;">
<td class="tabbing"><span class="ptmb7t-x-x-120">magic -d </span><span
class="ptmri7t-x-x-120">display </span><span
class="ptmb7t-x-x-120">tut1</span></td>
</tr>
</tbody>
</table>

<span class="ptmri7t-x-x-120">Display </span>is usually the model number
of the workstation you are using or the name of your window system. Look
in the manual page for a list of valid names, or just guess something.
Magic will print out the list of valid names if you guess wrong.

If you are using a graphics terminal (not a workstation), it is possible
that Magic doesn’t know which serial line to use. To learn how to fix
this, read about the <span class="ptmb7t-x-x-120">-g </span>switch in
the magic(1) manual page. Also read the displays(5) manual page.

## <span class="titlemark">6 </span> <span id="x1-60006"></span>The Box and the Cursor

Two things, called the <span class="ptmri7t-x-x-120">box </span>and the
<span class="ptmri7t-x-x-120">cursor</span>, are used to select things
on the color display. As you move the mouse, the cursor moves on the
screen. The cursor starts out with a crosshair shape, but you’ll see
later that its shape changes as you work to provide feedback about what
you’re doing. The left and right mouse buttons are used to position the
box. If you press the left mouse button and then release it, the box
will move so that its lower left corner is at the cursor position. If
you press and release the right mouse button, the upper right corner of
the box will move to the cursor position, but the lower left corner will
not change. These two buttons are enough to position the box anywhere on
the screen. Try using the buttons to place the box around each of the
colored rectangles on the screen.

Sometimes it is convenient to move the box by a corner other than the
lower left. To do this, press the left mouse button and <span
class="ptmri7t-x-x-120">hold it down</span>. The cursor shape changes to
show you that you are moving the box by its lower left corner:

<table id="TBL-2" class="tabular" data-rules="groups">
<tbody>
<tr class="odd hline">
<td><hr /></td>
</tr>
<tr id="TBL-2-1-" class="even" style="vertical-align:baseline;">
<td id="TBL-2-1-1" class="td11"
style="text-align: center; white-space: nowrap;"></td>
</tr>
<tr class="odd hline">
<td><hr /></td>
</tr>
<tr id="TBL-2-2-" class="even" style="vertical-align:baseline;">
<td id="TBL-2-2-1" class="td11"
style="text-align: center; white-space: nowrap;"></td>
</tr>
</tbody>
</table>

While holding the button down, move the cursor near the lower right
corner of the box, and now click the right mouse button (i.e. press and
release it, while still holding down the left button). The cursor’s
shape will change to indicate that you are now moving the box by its
lower right corner. Move the cursor to a different place on the screen
and release the left button. The box should move so that its lower right
corner is at the cursor position. Try using this feature to move the box
so that it is almost entirely off-screen to the left. Try moving the box
by each of its corners.

You can also reshape the box by corners other than the upper right. To
do this, press the right mouse button and hold it down. The cursor shape
shows you that you are reshaping the box by its upper right corner:

<table id="TBL-3" class="tabular" data-rules="groups">
<tbody>
<tr class="odd hline">
<td><hr /></td>
</tr>
<tr id="TBL-3-1-" class="even" style="vertical-align:baseline;">
<td id="TBL-3-1-1" class="td11"
style="text-align: center; white-space: nowrap;"></td>
</tr>
<tr id="TBL-3-2-" class="odd" style="vertical-align:baseline;">
<td id="TBL-3-2-1" class="td11"
style="text-align: center; white-space: nowrap;"></td>
</tr>
</tbody>
</table>

Now move the cursor near some other corner of the box and click the left
button, all the while holding the right button down. The cursor shape
will change to show you that now you are reshaping the box by a
different corner. When you release the right button, the box will
reshape so that the selected corner is at the cursor position but the
diagonally opposite corner is unchanged. Try reshaping the box by each
of its corners.

## <span class="titlemark">7 </span> <span id="x1-70007"></span>Invoking Commands

Commands can be invoked in Magic in three ways: by pressing buttons on
the mouse; by typing single keystrokes on the text keyboard (these are
called <span class="ptmri7t-x-x-120">macros</span>); or by typing longer
commands on the text keyboard (these are called <span
class="ptmri7t-x-x-120">long commands</span>). Many of the commands use
the box and cursor to help guide the command.

To see how commands can be invoked from the buttons, first position the
box over a small blank area in the middle of the screen. Then move the
cursor over the red rectangle and press the middle mouse button. At this
point, the area of the box should get painted red. Now move the cursor
over empty space and press the middle button again. The red paint should
go away. Note how this command uses both the cursor and box locations to
control what happens.

As an example of a macro, type the <span class="ptmb7t-x-x-120">g
</span>key on the text keyboard. A grid will appear on the color
display, along with a small black box marking the origin of the cell. If
you type <span class="ptmb7t-x-x-120">g </span>again, the grid will go
away. You may have noticed earlier that the box corners didn’t move to
the exact cursor position: you can see now that the box is forced to
fall on grid points.

Long commands are invoked by typing a colon (“:”) or semi-colon (“;”).
After you type the colon or semi-colon, the “&gt;” prompt on the text
screen will be replaced by a “:” prompt. This indicates that Magic is
waiting for a long command. At this point you should type a line of
text, followed by a return. When the long command has been processed,
the “&gt;” prompt reappears on the text display. Try typing semi-colon
followed by return to see how this works. Occasionally a “\]” (right
bracket) prompt will appear. This means that the design-rule checker is
reverifying part of your design. For now you can just ignore this and
treat “\]” like “&gt;”.

Each long command consists of the name of the command followed by
arguments, if any are needed by that command. The command name can be
abbreviated, just as long as you type enough characters to distinguish
it from all other long commands. For example, <span
class="ptmb7t-x-x-120">:h </span>and <span class="ptmb7t-x-x-120">:he
</span>may be used as abbreviations for <span
class="ptmb7t-x-x-120">:help</span>. On the other hand, <span
class="ptmb7t-x-x-120">:u </span>may not be used as an abbreviation for
<span class="ptmb7t-x-x-120">:undo</span> because there is another
command, <span class="ptmb7t-x-x-120">:upsidedown</span>, that has the
same abbreviation. Try typing <span class="ptmb7t-x-x-120">:u</span>.

As an example of a long command, put the box over empty space on the
color display, then invoke the long command

<table class="tabbing" data-cellpadding="0" data-border="0">
<tbody>
<tr class="odd tabbing" style="vertical-align:baseline;">
<td class="tabbing"><span class="ptmb7t-x-x-120">:paint red</span></td>
</tr>
</tbody>
</table>

The box should fill with the red color, just as if you had used the
middle mouse button to paint it. Everything you can do in Magic can be
invoked with a long command. It turns out that the macros are just
conveniences that are expanded into long commands and executed. For
example, the long command equivalent to the <span
class="ptmb7t-x-x-120">g </span>macro is

<table class="tabbing" data-cellpadding="0" data-border="0">
<tbody>
<tr class="odd tabbing" style="vertical-align:baseline;">
<td class="tabbing"><span class="ptmb7t-x-x-120">:grid</span></td>
</tr>
</tbody>
</table>

Magic permits you to define new macros if you wish. Once you’ve become
familiar with Magic you’ll almost certainly want to add your own macros
so that you can invoke quickly the commands you use most frequently. See
the <span class="ptmri7t-x-x-120">magic(1) </span>man page under the
command <span class="ptmb7t-x-x-120">:macro</span>.

One more long command is of immediate use to you. It is

<table class="tabbing" data-cellpadding="0" data-border="0">
<tbody>
<tr class="odd tabbing" style="vertical-align:baseline;">
<td class="tabbing"><span class="ptmb7t-x-x-120">:quit</span></td>
</tr>
</tbody>
</table>

Invoke this command. Note that before exiting, Magic will give you one
last chance to save the information that you’ve modified. Type <span
class="ptmb7t-x-x-120">y </span>to exit without saving anything.
