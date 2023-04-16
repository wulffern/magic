---
layout: post
title: Introduction
math: true
---



* TOC
{:toc }

This tutorial corresponds to Magic version 7.  

### <span class="titlemark">1 </span> <span id="x1-10001"></span>Introduction

This version of Magic, version 6, gathers together work done by numerous
people at several institutions since Magic version 4 was released from
Berkeley on the 1986 VLSI tools tape. This is a release of Magic and
IRSIM only. You’ll probably want to obtain other tools by ordering the
1986 VLSI Tools Tape from Berkeley.

This release has been prepared with the assistance of several groups.
Much of the new software came from Walter Scott’s group at the Lawrence
Livermore National Labs (LLNL). LLNL also provided partial funding to
help prepare the release. Digital Equipment Corporation’s Western
Research Lab (DECWRL) helped out by providing computer equipment, a
place to work, and the services of one of us (Robert Mayo). Don Stark,
Michael Arnold, and Gordon Hamachi also worked on the release at DECWRL.
Stanford donated significant pieces of new code, including a simulation
system called IRSIM. Other individuals and institutions have also
contributed code and assistance in ways too numerous to detail here.

New features in Magic Version 6 include:

-   New and Improved Routing—<span class="ptmri7t-x-x-120">Michael
    Arnold and Walter Scott of LLNL </span>  
    Three major routing improvements have been made in this version of
    Magic. There is a new, improved, global router courtesy of Walter
    Scott (of LLNL). Walter Scott has also added a gate array router.
    See the “garoute” command in the manual page for details. Michael
    Arnold (of LLNL) has written an interactive maze router that allows
    the user to specify hints to control the routing. See the
    documentation for the “iroute” command.

-   Extractor Enhancements—<span class="ptmri7t-x-x-120">Don Stark of
    Stanford and Walter Scott of LLNL </span>  
    The new “extresis” command, developed by Don Stark, provides
    substantially better resistance extraction. Magic’s normal
    extraction (“extract”) lumps resistances on a node into a single
    value. In branching networks, this approximation is often not
    acceptable. Resis was written to solve this problem. Walter Scott
    added accurate path length extraction, an important feature when
    dealing with high speed circuits, such as ECL.

-   New contact structure—<span class="ptmri7t-x-x-120">Walter Scott and
    Michael Arnold of LLNL and Don Stark of Stanford</span>  
    Multilayer contacts are handled better. In the previous version of
    Magic, there needed to be a separate contact type for each possible
    combination of contact layers over a given point. This caused a
    combinatorial explosion of tile types for multi-layer technologies
    with stacked contacts. Under the new scheme, there are only a couple
    of tile types for each layer: one that connects up, one that
    connects down, and one that connects in both directions.

-   Simulator Interface to IRSIM—<span class="ptmri7t-x-x-120">Stanford
    </span>  
    A simulator interface is provided courtesy of Stanford. See the
    commands “startrsim”, “simcmd”, and “rsim”. The irsim simulator,
    Stanford’s much improved rewrite of esim, is included in this
    distribution. Credit goes to Mike Chow, Arturo Salz, and Mark
    Horowitz.

-   New device/machine Support—<span class="ptmri7t-x-x-120">Various
    </span>  
    X11 is fully supported in this release, and is the preferred
    interface. Older drivers for graphics terminals and X10 are also
    included, but X11 is the preferred interface (meaning it is better
    supported and you’ll have lots of company). Magic’s X11 driver has a
    long history, starting with an X10 driver by Doug Pan at Stanford.
    Brown University, the University of Southern California, the
    University of Washington, and Lawrence Livermore National Labs all
    prepared improved versions, some of them for X11. Don Stark of
    Stanford took on the task of pulling these together and producing
    the X11 driver in this release.

    Magic runs on a number of workstations, such as the DECstation 3100
    and Sun’s SPARC processors. Partial Unix System V support is
    provided, via the compilation flags mentioned below. The system also
    runs on the MacII. Don Stark gets credit for the System V mods and
    support for HP machines, while Mike Chow helped get it running on
    the MacII.

    To assist people with small machines (such as the Mac II), Magic can
    now be compiled without some of its fancy features. Compilation
    flags are provided, as indicated below, to eliminate things like
    routing, plotting, or calma output. This is courtesy of Don Stark.

-   Reorganization of Magic Source Directory  
    Magic, as previously distributed, was set up with the assumption
    that lots of people would be changing the code at the same time. As
    a result, the makefiles did all sorts of paranoid things like making
    extra copies of the source code whenever a module was re-installed.

    Since Magic is more stable now, this copying is no longer needed.
    Instead, each makefile invokes the script <span
    class="ptmb7t-x-x-120">../:instclean </span>after installing a
    module. This script, by default, doesn’t copy the source code but
    does leave the .o files around. This cuts down on the disk space
    needed by a factor of two. You can change the script if you want the
    copying, or if you want to delete unused .o files to save even more
    disk space.

-   Lots of bug fixes—<span class="ptmri7t-x-x-120">Various </span>  
    Lots of bugs have been fixed in this release. We’d like to thank
    everybody that has reported bugs in the past. If you find a new bug,
    please report it as mentioned below.

### <span class="titlemark">2 </span> <span id="x1-20002"></span>Distribution Information

This version of Magic is available via FTP. Contact “<span
class="pcrr7t-x-x-120">magic@decwrl.dec.com</span>” for information.

For a handling fee, this version of Magic may be obtained on magnetic
tape from:

<table class="tabbing" data-cellpadding="0" data-border="0">
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd tabbing" style="vertical-align:baseline;">
<td class="tabbing">EECS/ERL Industrial Liaison Program<br />
479 Cory Hall<br />
University of California at Berkeley<br />
Berkeley, CA 94720</td>
</tr>
</tbody>
</table>

### <span class="titlemark">3 </span> <span id="x1-30003"></span>Bug Reports

Maintenance of Magic is a volunteer effort. Please send descriptions of
bugs via InterNet e-mail to “<span
class="pcrr7t-x-x-120">magic@decwrl.dec.com</span>” or via Uucp e-mail
to “<span class="pcrr7t-x-x-120">decwrl!magic</span>”. If you develop a
fix for the problem, please send that too!

### <span class="titlemark">4 </span> <span id="x1-40004"></span>Changes for Magic maintainers

Previous releases of Magic expected to find their system files in the
home directory of the user <span class="ptmb7t-x-x-120">cad</span>. The
default behavior of version 6 is no different, but it is possible to put
the files in another directory by setting the <span
class="ptmb7t-x-x-120">CAD</span><span class="ptmb7t-x-x-120">\_HOME
</span>shell environment variable. If this variable is set, magic will
use that location instead of the ~cad it finds in the password file.

#### <span class="titlemark">4.1 </span> <span id="x1-50004.1"></span>INSTALLING MAGIC

The distribution tape contains a version of Magic ready to run on
Digital’s line of Ultrix RISC workstations, such as the DECstation 3100.
For other machines, read ahead. In any event, all users should set their
shell environment variable CAD\_HOME to point to the place where the
tape is loaded, unless that place is ~cad, in which case things will
default correctly.

Before installing Magic, you should set your shell environment variable
CAD\_HOME to point to the place where you loaded the tape. If you “cd”
to the magic source directory (<span
class="ptmr8c-x-x-120">$</span>CAD\_HOME/src/magic) you will find a
makefile. A “<span class="ptmb7t-x-x-120">make config</span>” will run a
configuration script that asks questions about your configuration and
sets up magic to be compiled for your local environment.

After running a “make config”, you can run a “<span
class="ptmb7t-x-x-120">make force</span>” to force a complete
recompilation of magic. A ”<span class="ptmb7t-x-x-120">make
install</span>” will then copy the binaries to the <span
class="ptmr8c-x-x-120">$</span>CAD\_HOME/bin area, as well as install
things in <span class="ptmr8c-x-x-120">$</span>CAD\_HOME/lib and <span
class="ptmr8c-x-x-120">$</span>CAD\_HOME/man.

Included in this documentation is a set of Magic maintainer’s manuals.
These should be read by anybody interested in modifying Magic or by
anybody that is having difficulty installing it on their system.

#### <span class="titlemark">4.2 </span> <span id="x1-60004.2"></span>Technology file changes

Users of Magic 4 should have little trouble switching to Magic 6.

A new section, the <span class="ptmb7t-x-x-120">mzrouter </span>section
needs to be added to your technology files. See the mzrouter section of
the tutorial <span class="ptmri7t-x-x-120">Magic Maintainer’s Manual
\#2: The Technology File </span>for details.

Display styles must be defined in the <span
class="ptmri7t-x-x-120">.tech </span>file for the mzrouter hint layers
magnet, fence and rotate. We suggest copying this information from the
styles section of the scmos technology file on the distribution tape.
You’ll also need to include these display styles in your <span
class="ptmri7t-x-x-120">.dstyle</span> file.

### <span class="titlemark">5 </span> <span id="x1-70005"></span>Beta-test Sites

We’d like to thank the beta-test sites that tried out this version of
Magic, reported bugs and fixes in a timely manner, and ported the code
to new machines:

<table class="tabbing" data-cellpadding="0" data-border="0">
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd tabbing" style="vertical-align:baseline;">
<td class="tabbing">Mike Chow, Apple Computer<br />
Arun Rao, Arizona State University<br />
Richard Hughey, Brown University<br />
Rick Carley, Carnegie-Mellon University<br />
Hank Walker, Carnegie-Mellon University<br />
Christos Zoulas, Cornell University<br />
Andreas Andreou, John Hopkins University<br />
George Entenman, The Microelectronics Center of North Carolina<br />
Shih-Lien Lu, The MOSIS Service<br />
Jen-I Pi, The MOSIS Service<br />
Guntram Wolski, Silicon Engineering, Inc.<br />
Don Stark, Stanford University<br />
Gregory Frazier, University of California at Los Angeles<br />
Yuval Tamir, University of California at Los Angeles<br />
Steven Parkes, University of Illinois<br />
Larry McMurchie, University of Washington<br />
Tim Heldt, Washington State University<br />
David Lee, Xerox Palo Alto Research Center<br />
</td>
</tr>
</tbody>
</table>

Martin Harriman of Silicon Engineering wrote a “select less” command for
Magic during the beta-test phase. “Select less” has been a
much-requested feature.

In addition to the persons named above, there were many other beta-test
users of Magic at these and other sites—too many to list here. We
appreciate their help. We also acknowledge the help of the pre-release
sites, who tested a version that included most of the fixes from the
beta-test phase.
