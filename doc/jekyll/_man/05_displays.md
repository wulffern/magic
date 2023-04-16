---
layout: post
title: 05 displays
math: true
---



* TOC
{:toc }

# NAME

displays - Display Configuration File

# DESCRIPTION

The interactive graphics programs Caesar, Magic, and Gremlin use two
separate terminals: a text terminal from which commands are issued, and
a color graphics terminal on which graphical output is displayed. These
programs use a **displays** file to associate their text terminal with
its corresponding display device.

The **displays** file is an ASCII text file with one line for each text
terminal/graphics terminal pair. Each line contains 4 items separated by
spaces: the name of the port attached to a text terminal, the name of
the port attached to the associated graphics terminal, the phosphor type
of the graphics terminal's monitor, and the type of graphics terminal.

An applications program may use the phosphor type to select a color map
tuned to the monitor's characteristics. Only the **std** phosphor type
is supported at UC Berkeley.

The graphics terminal type specifies the device driver a program should
use when communicating with its graphics terminal. Magic supports types
**UCB512**, **AED1024**, and **SUN120**. Other programs may recognize
different display types. See the manual entry for your specific
application for more information.

A sample displays file is:

  
/dev/ttyi1 /dev/ttyi0 std UCB512  
/dev/ttyj0 /dev/ttyj1 std UCB512  
/dev/ttyjf /dev/ttyhf std UCB512  
/dev/ttyhb /dev/ttyhc std UCB512  
/dev/ttyhc /dev/ttyhb std UCB512 ®

  

In this example, **/dev/ttyi1** connects to a text terminal. An
associated **UCB512** graphics terminal with standard phosphor is
connected to **/dev/ttyi0**.

# FILES

Magic uses the displays file ~cad/lib/displays. Gremlin looks in
/usr/local/displays.

# SEE ALSO

magic(1)
