---

date: 2009-10-22
slug: |
  foresight-linux-quickie
tags:
 - rpath
title: Foresight Linux quickie
---

For those of you out there who are [Foresight
Linux](http://www.foresightlinux.org) users wondering when the next
major software update will hit the stable branch, your wait is almost
over! We've been feverishly making all the latest bits to play nice with
each other so that we can also release newer ISO images of what will be
**Foresight 2.1.2**. Some of the issues we're facing right now are:

-   Issues with latest **\*goocanvas/pycairo** mess
    \[[0](https://bugzilla.gnome.org/show_bug.cgi?id=576198)\]\[[1](http://bugs.freedesktop.org/show_bug.cgi?id=23073)\]\[[2](https://bugzilla.redhat.com/show_bug.cgi?id=515455)\];
-   Epiphany issues with latest WebKit in x86_64;
-   Exotic side effects of **kernel** changes that make audio CDs not
    easilly playable (not a Foresight exclusive issue);
-   **Mono** is somehow partly busted (part of gnome bindings) in x86_64
    -   hits latest **banshee**;
-   Getting **Anaconda** to play nicely with newer kernel drivers for
    some motherboards;

Some of the cool things we're cooking in the development branch are:
latest **KDE**, **GNOME**, **Chromium/Firefox/Opera** web browser, **gst
streamer** bits, latest **kernel**, **Banshee** 1.5.1, **F-Spot**, and
many, many more applications!

If you're trying **Foresight** for the very first time, you'll notice
that the first update will take a while but that is expected. Since it
is a rolling release, our current state is many miles ahead of the ISO
images we have published. [Conary](http://wiki.rpath.com/wiki/Conary),
the package management system, has to pull in all of those changes as
well as version your entire system in order to "apply" these changes. If
you're interested in playing with fire and feel like helping us detect
issues before we release a new version, come on over to the
**\#foresight** IRC channel on **Freenode** and we'll get you started!
