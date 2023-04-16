---
layout: post
title: 10 The interactive Router
math: true
---



* TOC
{:toc }

<span class="ptmb7t-x-x-172">Magic Tutorial \#10: The Interactive
Router</span>  
<span class="ptmri7t-x-x-120">Michael Arnold</span>  
O Division  
Lawrence Livermore National Laboratory  
Livermore, CA 94550  
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
<td class="tabbing">:iroute</td>
</tr>
</tbody>
</table>

<span class="ptmb7t-x-x-144">Macros introduced in this tutorial:</span>

<table class="tabbing" data-cellpadding="0" data-border="0">
<tbody>
<tr class="odd tabbing" style="vertical-align:baseline;">
<td class="tabbing">̂R, ̂N</td>
</tr>
</tbody>
</table>

## <span class="titlemark">1 </span> <span id="x1-10001"></span>Introduction

The Magic interactive router, <span
class="ptmri7t-x-x-120">Irouter</span>, provides an interactive
interface to Magic’s internal maze router. It is intended as an aid to
manual routing. Routing is done one connection at a time, the user
specifying a starting point and destination areas prior to each
connection. The user determines the order in which signals are routed
and how multi-point nets are decomposed into point-to-area connections.
In addition parameters and special Magic <span
class="ptmri7t-x-x-120">hint </span>layers permit the user to control
the nature of the routes. Typically the user determines the overall path
of a connection, and leaves the details of satisfying the design-rules,
and detouring around or over minor obstacles, to the router.

The interactive router is not designed for fully automatic routing:
interactions between nets are not considered, and net decomposition is
not automatic. Thus netlists are generally not suitable input for the
Irouter. However it can be convenient to obtain endpoint information
from netlists. The <span class="ptmri7t-x-x-120">Net2ir </span>program
uses netlist information to generate commands to the Irouter with
appropriate endpoints for specified signals. Typically a user might
setup parameters and hints to river-route a set of connections, and then
generate Irouter commands with the appropriate endpoints via Net2ir. For
details on Net2ir see the manual page <span
class="ptmri7t-x-x-120">net2ir(1)</span>.

This tutorial provides detailed information on the use of the Irouter.
On-line help, Irouter subcommands, Irouter parameters, and hint-layers
are explained.

## <span class="titlemark">2 </span> <span id="x1-20002"></span>Getting Started—‘Cntl-R’, ‘Cntl-N’, ‘:iroute’ and ‘:iroute help’

To make a connection with the Irouter, place the cursor over one end of
the desired connection (the <span
class="ptmri7t-x-x-120">start-point</span>) and the box at the other end
(the <span class="ptmri7t-x-x-120">destination-area</span>). Then type

<table class="tabbing" data-cellpadding="0" data-border="0">
<tbody>
<tr class="odd tabbing" style="vertical-align:baseline;">
<td class="tabbing"><span class="ptmb7t-x-x-120">Cntl-R</span></td>
</tr>
</tbody>
</table>

Note that the box must be big enough to allow the route to terminate
entirely within it. A design-rule correct connection between the cursor
and the box should appear. The macro

<table class="tabbing" data-cellpadding="0" data-border="0">
<tbody>
<tr class="odd tabbing" style="vertical-align:baseline;">
<td class="tabbing"><span class="ptmb7t-x-x-120">Cntl-R</span></td>
</tr>
</tbody>
</table>

and the long commands

<table class="tabbing" data-cellpadding="0" data-border="0">
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd tabbing" style="vertical-align:baseline;">
<td class="tabbing"><span class="ptmb7t-x-x-120">:iroute</span><br />
<span class="ptmb7t-x-x-120">:iroute route</span></td>
</tr>
</tbody>
</table>

are all equivalent. They invoke the Irouter to connect the cursor with
the interior of the box. Note that the last connection is always left
selected. This allows further terminals to be connected to the route
with the second Irouter macro, <span
class="ptmb7t-x-x-120">Cntl-N</span>. Try typing

<table class="tabbing" data-cellpadding="0" data-border="0">
<tbody>
<tr class="odd tabbing" style="vertical-align:baseline;">
<td class="tabbing"><span class="ptmb7t-x-x-120">Cntl-N</span></td>
</tr>
</tbody>
</table>

A connection between the cursor and the previous route should appear. In
general <span class="ptmb7t-x-x-120">Cntl-N </span>routes from the
cursor to the selection.

There are a number of commands to set parameters and otherwise interact
with the Irouter. These commands have the general form

<table class="tabbing" data-cellpadding="0" data-border="0">
<tbody>
<tr class="odd tabbing" style="vertical-align:baseline;">
<td class="tabbing"><span class="ptmb7t-x-x-120">:iroute</span><span
class="ptmri7t-x-x-120">subcommand </span>[<span
class="ptmri7t-x-x-120">arguments</span>]</td>
</tr>
</tbody>
</table>

For a list of subcommands and a short description of each, type

<table class="tabbing" data-cellpadding="0" data-border="0">
<tbody>
<tr class="odd tabbing" style="vertical-align:baseline;">
<td class="tabbing"><span class="ptmb7t-x-x-120">:iroute
help</span></td>
</tr>
</tbody>
</table>

Usage information on a subcommand can be obtained by typing

<table class="tabbing" data-cellpadding="0" data-border="0">
<tbody>
<tr class="odd tabbing" style="vertical-align:baseline;">
<td class="tabbing"><span class="ptmb7t-x-x-120">:iroute help
</span>[<span class="ptmri7t-x-x-120">subcommand</span>]</td>
</tr>
</tbody>
</table>

As with Magic in general, unique abbreviations of subcommands and most
of their arguments are permitted. Case is generally ignored.

## <span class="titlemark">3 </span> <span id="x1-30003"></span>:Undo and Cntl-C

As with other Magic commands, the results of <span
class="ptmb7t-x-x-120">:iroute </span>can be undone with <span
class="ptmb7t-x-x-120">:undo</span>, and if the Irouter is taking too
long it can be interrupted with <span
class="ptmb7t-x-x-120">Cntl-C</span>. This makes it easy to refine the
results of the Irouter by trial and error. If you don’t like the results
of a route, undo it, tweak the Irouter parameters or hints you are using
and try again. If the Irouter is taking too long, you can very likely
speed things up by interrupting it, resetting performance related
parameters, and trying again. The details of parameters and hints are
described later in this document.

## <span class="titlemark">4 </span> <span id="x1-40004"></span>More about Making Connections—‘:iroute route’

Start points for routes can be specified via the cursor, labels, or
coordinates. Destination areas can be specified via the box, labels,
coordinates or the selection. In addition start and destination layers
can be specified explicitly. For the syntax of all these options type

<table class="tabbing" data-cellpadding="0" data-border="0">
<tbody>
<tr class="odd tabbing" style="vertical-align:baseline;">
<td class="tabbing"><span class="ptmb7t-x-x-120">:iroute help
route</span></td>
</tr>
</tbody>
</table>

When a start point lies on top of existing geometry it is assumed that a
connection to that material is desired. If this is not the case, the
desired starting layer must be explicitly specified. When routing to the
selection it is assumed that connection to the selected material is
desired. By default, routes to the box may terminate on any active route
layer. If you are having trouble connecting to a large region, it may be
because the connection point or area is too far in the interior of the
region. Try moving it toward the edge. (Alternately see the discussion
of the <span class="ptmri7t-x-x-120">penetration </span>parameter in the
wizard section below.)

## <span class="titlemark">5 </span> <span id="x1-50005"></span>Hints

Magic has three built-in layers for graphical control of the Irouter,
<span class="ptmb7t-x-x-120">fence </span>(<span
class="ptmb7t-x-x-120">f</span>), <span class="ptmb7t-x-x-120">magnet
</span>(<span class="ptmb7t-x-x-120">mag</span>), and <span
class="ptmb7t-x-x-120">rotate</span> (<span
class="ptmb7t-x-x-120">r</span>). These layers can be painted and erased
just like other Magic layers. The effect each has on the Irouter is
described below.

### <span class="titlemark">5.1 </span> <span id="x1-60005.1"></span>The Fence Layer

The Irouter won’t cross fence boundaries. Thus the fence layer is useful
both for carving out routing-regions and for blocking routing in given
areas. It is frequently useful to indicate the broad path of one or a
series of routes with fence. In addition to guiding the route, the use
of fences can greatly speed up the router by limiting the search.

### <span class="titlemark">5.2 </span> <span id="x1-70005.2"></span>The Magnet Layer

Magnets attract the route. They can be used to pull routes in a given
direction, e.g., towards one edge of a channel. Over use of magnets can
make routing slow. In particular magnets that are long and far away from
the actual route can cause performance problems. (If you are having
problems with magnets and performance, see also the discussion of the
<span class="ptmri7t-x-x-120">penalty </span>parameter in the wizard
section below.)

### <span class="titlemark">5.3 </span> <span id="x1-80005.3"></span>The Rotate Layer

The Irouter associates different weights with horizontal and vertical
routes (see the layer-parameter section below). This is so that a
preferred routing direction can be established for each layer. When two
good route-layers are available (as in a two-layer-metal process)
interference between routes can be minimized by assigning opposite
preferred directions to the layers.

The rotate layer locally inverts the preferred directions. An example
use of the rotate layer might involve an <span
class="ptmb7t-x-x-120">L</span>-shaped bus. The natural preferred
directions on one leg of the <span class="ptmb7t-x-x-120">L </span>are
the opposite from the other, and thus one leg needs to be marked with
the rotate layer.

## <span class="titlemark">6 </span> <span id="x1-90006"></span>Subcells

As with painting and other operations in Magic, the Irouter’s output is
written to the cell being edited. What the router sees, that is which
features act as obstacles, is determined by the window the route is
issued to (or other designated reference window - see the wizard
section.) The contents of subcells expanded in the route window are
visible to the Irouter, but it only sees the bounding boxes of
unexpanded subcells. These bounding boxes appear on a special <span
class="ptmb7t-x-x-120">SUBCELL</span> pseudo-layer. The spacing
parameters to the <span class="ptmb7t-x-x-120">SUBCELL </span>layer
determine exactly how the Irouter treats unexpanded subcells. (See the
section on spacing parameters below.) By default, the spacings to the
<span class="ptmb7t-x-x-120">SUBCELL </span>layer are large enough to
guarantee that no design-rules will be violated, regardless of the
contents of unexpanded subcells. Routes can be terminated at unexpanded
subcells in the same fashion that connections to other pre-existing
features are made.

## <span class="titlemark">7 </span> <span id="x1-100007"></span>Layer Parameters—‘:iroute layers’

<span class="ptmri7t-x-x-120">Route-layers</span>, specified in the
<span class="ptmb7t-x-x-120">mzrouter </span>section of the technology
file, are the layers potentially available to the Irouter for routing.
The <span class="ptmb7t-x-x-120">layer </span>subcommand gives access to
parameters associated with these route-layers. Many of the parameters
are weights for factors in the Irouter cost-function. The Irouter
strives for the cheapest possible route. Thus the balance between the
factors in the cost-function determines the character of the routes:
which layers are used in which directions, and the number of contacts
and jogs can be controlled in this way. But be careful! Changes in these
parameters can also profoundly influence performance. Other parameters
determine which of the route-layers are actually available for routing
and the width of routes on each layer. It is a good idea to inactivate
route-layers not being used anyway, as this speeds up routing.

The layers subcommand takes a variable number of arguments.

<table class="tabbing" data-cellpadding="0" data-border="0">
<tbody>
<tr class="odd tabbing" style="vertical-align:baseline;">
<td class="tabbing"><span class="ptmb7t-x-x-120">:iroute
layers</span></td>
</tr>
</tbody>
</table>

prints a table with one row for each route-layer giving all parameter
values.

<table class="tabbing" data-cellpadding="0" data-border="0">
<tbody>
<tr class="odd tabbing" style="vertical-align:baseline;">
<td class="tabbing"><span class="ptmb7t-x-x-120">:iroute
layers</span><span class="ptmri7t-x-x-120">type</span></td>
</tr>
</tbody>
</table>

prints all parameters associated with route-layer <span
class="ptmri7t-x-x-120">type</span>.

<table class="tabbing" data-cellpadding="0" data-border="0">
<tbody>
<tr class="odd tabbing" style="vertical-align:baseline;">
<td class="tabbing"><span class="ptmb7t-x-x-120">:iroute
layers</span><span class="ptmri7t-x-x-120">type parameter</span></td>
</tr>
</tbody>
</table>

prints the value of <span class="ptmri7t-x-x-120">parameter </span>for
layer <span class="ptmri7t-x-x-120">type</span>. If <span
class="ptmri7t-x-x-120">type </span>is ‘<span
class="ptmb7t-x-x-120">\*</span>’, the value of <span
class="ptmri7t-x-x-120">parameter </span>is printed for all layers.

<table class="tabbing" data-cellpadding="0" data-border="0">
<tbody>
<tr class="odd tabbing" style="vertical-align:baseline;">
<td class="tabbing"><span class="ptmb7t-x-x-120">:iroute layers
</span><span class="ptmri7t-x-x-120">type parameter value</span></td>
</tr>
</tbody>
</table>

sets <span class="ptmri7t-x-x-120">parameter </span>to <span
class="ptmri7t-x-x-120">value </span>on layer <span
class="ptmri7t-x-x-120">type</span>. If <span
class="ptmri7t-x-x-120">type </span>is ‘<span
class="ptmb7t-x-x-120">\*</span>’, <span
class="ptmri7t-x-x-120">parameter </span>is set to <span
class="ptmri7t-x-x-120">value </span>on all layers.

<table class="tabbing" data-cellpadding="0" data-border="0">
<tbody>
<tr class="odd tabbing" style="vertical-align:baseline;">
<td class="tabbing"><span class="ptmb7t-x-x-120">:iroute layers
</span><span class="ptmri7t-x-x-120">type </span><span
class="ptmb7t-x-x-120">* </span><span class="ptmri7t-x-x-120">value1
value2 </span>…<span class="ptmri7t-x-x-120">valuen</span></td>
</tr>
</tbody>
</table>

sets a row in the parameter table.

<table class="tabbing" data-cellpadding="0" data-border="0">
<tbody>
<tr class="odd tabbing" style="vertical-align:baseline;">
<td class="tabbing"><span class="ptmb7t-x-x-120">:iroute layers
*</span><span class="ptmri7t-x-x-120">parameter value1 </span><span
class="ptmri7t-x-x-120">…valuen</span></td>
</tr>
</tbody>
</table>

sets a column in the table.

There are six layer parameters.

-   <span class="ptmb7t-x-x-120">active </span>  
    Takes the value of <span class="ptmb7t-x-x-120">YES </span>(the
    default) or <span class="ptmb7t-x-x-120">NO</span>. Only active
    layers are used by the Irouter.

-   <span class="ptmb7t-x-x-120">width </span>  
    Width of routing created by the Irouter on the given layer. The
    default is the minimum width permitted by the design rules.

-   <span class="ptmb7t-x-x-120">hcost </span>  
    Cost per unit-length for horizontal segments on this layer.

-   <span class="ptmb7t-x-x-120">vcost </span>  
    Cost per unit-length for vertical segments.

-   <span class="ptmb7t-x-x-120">jogcost </span>  
    Cost per jog (transition from horizontal to vertical segment).

-   <span class="ptmb7t-x-x-120">hintcost </span>  
    Cost per unit-area between actual route and magnet segment.

## <span class="titlemark">8 </span> <span id="x1-110008"></span>Contact Parameters—‘:iroute contacts’

The <span class="ptmb7t-x-x-120">contacts </span>subcommand gives access
to a table of parameters for contact-types used in routing, one row of
parameters per type. The syntax is identical to that of the <span
class="ptmb7t-x-x-120">layers </span>subcommand described above, and
parameters are printed and set in the same way.

There are three contact-parameters.

-   <span class="ptmb7t-x-x-120">active </span>  
    Takes the value of <span class="ptmb7t-x-x-120">YES </span>(the
    default) or <span class="ptmb7t-x-x-120">NO</span>. Only active
    contact types are used by the Irouter.

-   <span class="ptmb7t-x-x-120">width </span>  
    Diameter of contacts of this type created by the Irouter. The
    default is the minimum width permitted by the design-rules.

-   <span class="ptmb7t-x-x-120">cost </span>  
    Cost per contact charged by the Irouter cost-function.

## <span class="titlemark">9 </span> <span id="x1-120009"></span>Spacing Parameters—‘:iroute spacing’

The spacing parameters specify minimum spacings between the route-types
(route-layers and route-contacts) and arbitrary Magic types. These
spacings are the design-rules used internally by the Irouter during
routing. Default values are derived from the <span
class="ptmb7t-x-x-120">drc </span>section of the technology file. These
values can be overridden in the <span class="ptmb7t-x-x-120">mzrouter
</span>section of the technology file. (See the <span
class="ptmri7t-x-x-120">Magic Maintainers Manual on</span> <span
class="ptmri7t-x-x-120">Technology Files </span>for details.) Spacings
can be examined and changed at any time with the <span
class="ptmb7t-x-x-120">spacing</span> subcommand. Spacing values can be
<span class="ptmb7t-x-x-120">nil</span>, <span
class="ptmb7t-x-x-120">0</span>, or positive integers. A value of <span
class="ptmb7t-x-x-120">nil </span>means there is no spacing constraint
between the route-layer and the given type. A value of <span
class="ptmb7t-x-x-120">0 </span>means the route-layer may not overlap
the given type. If a positive value is specified, the Irouter will
maintain the given spacing between new routing on the specified
route-layer and pre-existing features of the specified type (except when
connecting to the type at an end-point of the new route).

The <span class="ptmb7t-x-x-120">spacing </span>subcommand takes several
forms.

<table class="tabbing" data-cellpadding="0" data-border="0">
<tbody>
<tr class="odd tabbing" style="vertical-align:baseline;">
<td class="tabbing"><span class="ptmb7t-x-x-120">:iroute
spacing</span></td>
</tr>
</tbody>
</table>

prints spacings for all route-types. (Nil spacings are omitted.)

<table class="tabbing" data-cellpadding="0" data-border="0">
<tbody>
<tr class="odd tabbing" style="vertical-align:baseline;">
<td class="tabbing"><span class="ptmb7t-x-x-120">:iroute spacing
</span><span class="ptmri7t-x-x-120">route-type</span></td>
</tr>
</tbody>
</table>

prints spacings for <span class="ptmri7t-x-x-120">route-type</span>.
(Nil spacings are omitted.)

<table class="tabbing" data-cellpadding="0" data-border="0">
<tbody>
<tr class="odd tabbing" style="vertical-align:baseline;">
<td class="tabbing"><span class="ptmb7t-x-x-120">:iroute spacing
</span><span class="ptmri7t-x-x-120">route-type type</span></td>
</tr>
</tbody>
</table>

prints the spacing between <span class="ptmri7t-x-x-120">route-type
</span>and <span class="ptmri7t-x-x-120">type</span>.

<table class="tabbing" data-cellpadding="0" data-border="0">
<tbody>
<tr class="odd tabbing" style="vertical-align:baseline;">
<td class="tabbing"><span class="ptmb7t-x-x-120">:iroute spacing
</span><span class="ptmri7t-x-x-120">route-type type value</span></td>
</tr>
</tbody>
</table>

sets the spacing between <span class="ptmri7t-x-x-120">route-type
</span>and <span class="ptmri7t-x-x-120">type </span>to <span
class="ptmri7t-x-x-120">value</span>.

The spacings associated with each route-type are the ones that are
observed when the Irouter places that route-type. To change the spacing
between two route-types, two spacing parameters must be changed: the
spacing to the first type when routing on the second, and the spacing to
the second type when routing on the first.

Spacings to the <span class="ptmb7t-x-x-120">SUBCELL </span>pseudo-type
give the minimum spacing between a route-type and unexpanded subcells.
The <span class="ptmb7t-x-x-120">SUBCELL </span>spacing for a given
route-layer defaults to the maximum spacing to the route-layer required
by the design-rules (in the <span class="ptmb7t-x-x-120">drc
</span>section of the technology file). This ensures that no
design-rules will be violated regardless of the contents of the subcell.
If subcell designs are constrained in a fashion that permits closer
spacings to some layers, the <span class="ptmb7t-x-x-120">SUBCELL
</span>spacings can be changed to take advantage of this.

## <span class="titlemark">10 </span> <span id="x1-1300010"></span>Search Parameters—‘:search’

The Mzrouter search is windowed. Early in the search only partial paths
near the start point are considered; as the search progresses the window
is moved towards the goal. This prevents combinatorial explosion during
the search, but still permits the exploration of alternatives at all
stages. The <span class="ptmb7t-x-x-120">search</span> subcommand
permits access to two parameters controlling the windowed search, <span
class="ptmb7t-x-x-120">rate</span>, and <span
class="ptmb7t-x-x-120">width</span>. The <span
class="ptmb7t-x-x-120">rate </span>parameter determines how fast the
window is shifted towards the goal, and the <span
class="ptmb7t-x-x-120">width</span> parameter gives the width of the
window. The units are comparable with those used in the cost parameters.
If the router is taking too long to complete, try increasing <span
class="ptmb7t-x-x-120">rate</span>. If the router is choosing poor
routes, try decreasing <span class="ptmb7t-x-x-120">rate</span>. The
window width should probably be at least twice the rate.

The subcommand has this form:

<table class="tabbing" data-cellpadding="0" data-border="0">
<tbody>
<tr class="odd tabbing" style="vertical-align:baseline;">
<td class="tabbing"><span class="ptmb7t-x-x-120">:iroute search
</span>[<span class="ptmri7t-x-x-120">parameter</span>] [<span
class="ptmri7t-x-x-120">value</span>]</td>
</tr>
</tbody>
</table>

If <span class="ptmri7t-x-x-120">value </span>is omitted, the current
value is printed, if <span class="ptmri7t-x-x-120">parameter </span>is
omitted as well, both parameter values are printed.

## <span class="titlemark">11 </span> <span id="x1-1400011"></span>Messages—‘:iroute verbosity’

The number of messages printed by the Irouter is controlled by

<table class="tabbing" data-cellpadding="0" data-border="0">
<tbody>
<tr class="odd tabbing" style="vertical-align:baseline;">
<td class="tabbing"><span class="ptmb7t-x-x-120">:iroute
verbosity</span><span class="ptmri7t-x-x-120">value</span></td>
</tr>
</tbody>
</table>

If verbosity is set to <span class="ptmb7t-x-x-120">0</span>, only
errors and warnings are printed. A value of <span
class="ptmb7t-x-x-120">1 </span>(the default) results in short messages.
A value of <span class="ptmb7t-x-x-120">2 </span>causes statistics to be
printed.

## <span class="titlemark">12 </span> <span id="x1-1500012"></span>Version—‘:iroute version’

The subcommand

<table class="tabbing" data-cellpadding="0" data-border="0">
<tbody>
<tr class="odd tabbing" style="vertical-align:baseline;">
<td class="tabbing"><span class="ptmb7t-x-x-120">:iroute
version</span></td>
</tr>
</tbody>
</table>

prints the Irouter version in use.

## <span class="titlemark">13 </span> <span id="x1-1600013"></span>Saving and Restoring Parameters—‘:iroute save’

The command

<table class="tabbing" data-cellpadding="0" data-border="0">
<tbody>
<tr class="odd tabbing" style="vertical-align:baseline;">
<td class="tabbing"><span class="ptmb7t-x-x-120">:iroute save
</span><span class="ptmri7t-x-x-120">file</span><span
class="ptmb7t-x-x-120">.ir</span></td>
</tr>
</tbody>
</table>

saves away the current settings of all the Irouter parameters in file
<span class="ptmri7t-x-x-120">file</span><span
class="ptmb7t-x-x-120">.ir</span>. Parameters can be reset to these
values at any time with the command

<table class="tabbing" data-cellpadding="0" data-border="0">
<tbody>
<tr class="odd tabbing" style="vertical-align:baseline;">
<td class="tabbing"><span class="ptmb7t-x-x-120">:source </span><span
class="ptmri7t-x-x-120">file</span><span
class="ptmb7t-x-x-120">.ir</span></td>
</tr>
</tbody>
</table>

This feature can be used to setup parameter-sets appropriate to
different routing contexts. Note that the extension <span
class="ptmb7t-x-x-120">.ir </span>is recommended for Irouter
parameter-files.

## <span class="titlemark">14 </span> <span id="x1-1700014"></span>Wizard Parameters—‘:iroute wizard’

Miscellaneous parameters that are probably not of interest to the casual
user are accessed via the <span class="ptmb7t-x-x-120">wizard</span>
subcommand. The parameters are as follows:

<span class="ptmb7t-x-x-120">bloom </span>Takes on a non-negative
integer value. This controls the amount of compulsory searching from a
focus, before the next focus is picked based on the cost-function and
window position. In practice <span class="ptmb7t-x-x-120">1 </span>(the
default value) seems to be the best value. This parameter may be removed
in the future.

<span class="ptmb7t-x-x-120">boundsIncrement </span>Takes on the value
<span class="ptmb7t-x-x-120">AUTOMATIC </span>or a positive integer.
Determines in what size chunks the layout is preprocessed for routing.
This preprocessing (blockage generation) takes a significant fraction of
the routing time, thus performance may well be improved by experimenting
with this parameter.

<span class="ptmb7t-x-x-120">estimate </span>Takes on a boolean value.
If <span class="ptmb7t-x-x-120">ON </span>(the default) an estimation
plane is generated prior to each route that permits cost-to-completion
estimates to factor in subcells and fence regions. This can be very
important to efficient routing. Its rarely useful to turn estimation
off.

<span class="ptmb7t-x-x-120">expandDests </span>Takes on a boolean
value. If <span class="ptmb7t-x-x-120">ON </span>(not the default)
destination areas are expanded to include all of any nodes they overlap.
This is particularly useful if the Irouter is being invoked from a
script, since it is difficult to determine optimal destination areas
automatically.

<span class="ptmb7t-x-x-120">penalty </span>Takes on a rational value
(default is 1024.0). It is not strictly true that the router searches
only within its window. Paths behind the window are also considered, but
with cost penalized by the product of their distance to the window and
the penalty factor. It was originally thought that small penalties might
be desirable, but experience, so far, has shown that large penalties
work better. In particular it is important that the ratio between the
actual cost of a route and the initial estimate is less than the value
of <span class="ptmb7t-x-x-120">penalty</span>, otherwise the search can
explode (take practically forever). If you suspect this is happening,
you can set <span class="ptmb7t-x-x-120">verbosity</span> to <span
class="ptmb7t-x-x-120">2 </span>to check, or just increase the value of
<span class="ptmb7t-x-x-120">penalty</span>. In summary it appears that
the value of penalty doesn’t matter much as long as it is large (but not
so large as to cause overflows). It will probably be removed in the
future.

<span class="ptmb7t-x-x-120">penetration </span>This parameter takes the
value <span class="ptmb7t-x-x-120">AUTOMATIC </span>or a positive
integer. It determines how far into a blocked area the router will
penetrate to make a connection. Note however the router will in no case
violate spacing constraints to nodes not involved in the route.

<span class="ptmb7t-x-x-120">window </span>This parameter takes the
value <span class="ptmb7t-x-x-120">COMMAND </span>(the default) or a
window id (small integers). It determines the reference window for
routes. The router sees the world as it appears in the reference window,
e.g., it sees the contents of subcells expanded in the reference window.
If <span class="ptmb7t-x-x-120">window </span>is set to <span
class="ptmb7t-x-x-120">COMMAND </span>the reference window is the one
that contained the cursor when the route was invoked. To set the
reference window to a fixed window, place the cursor in that window and
type:

<table class="tabbing" data-cellpadding="0" data-border="0">
<tbody>
<tr class="odd tabbing" style="vertical-align:baseline;">
<td class="tabbing"><span class="ptmb7t-x-x-120">:iroute wizard window
.</span></td>
</tr>
</tbody>
</table>

## <span id="x1-1800014"></span>References

<span class="biblabel"> \[1\]<span class="bibsp">   </span></span><span
id="Xarnold"></span>M.H. Arnold and W.S. Scott, “An Interactive Maze
Router with Hints”, <span class="ptmri7t-x-x-120">Proceedings of</span>
<span class="ptmri7t-x-x-120">the 25th Design Automation
Conference</span>, June 1988, pp. 672–676.
