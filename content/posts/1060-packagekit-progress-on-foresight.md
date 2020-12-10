---

date: "2011-04-13 20:51"
slug: |
  packagekit-progress-on-foresight
tags:
 - english
title: PackageKit Progress on Foresight
---

For a while [Foresight Linux](http://foresightlinux.org) users had no
graphical interface for managing their systems packages and/or updates,
mainly because the development for the **conary backend** fell out of
scope and our radar (this is a nicer way to say that we didn't have
someone to maintain it). But thanks to the work of **zodman**, **jesse**
and others [PackageKit](http://www.packagekit.org/) is making its way
back to our desktop.

\[caption id="attachment_1395" align="aligncenter" width="296"
caption="Available updates"\][![Available
updates](http://www.ogmaciel.com/wp-content/uploads/2011/04/Screenshot-39.png)](http://www.ogmaciel.com/wp-content/uploads/2011/04/Screenshot-39.png)\[/caption\]

There's still some work to be done but I believe that most blockers and
kinks have been ironed out, as I have been able to use it to install
packages and update my system in the last couple of days. Once we deem
it stable for generic use, you will all get it the next time you
manually (hopefully, for the last time) run: sudo conary updateall

\[caption id="attachment_1396" align="aligncenter" width="300"
caption="Applying updates"\][![Applying
updates](http://www.ogmaciel.com/wp-content/uploads/2011/04/Screenshot-Software-Update-1-300x270.png)](http://www.ogmaciel.com/wp-content/uploads/2011/04/Screenshot-Software-Update-1.png)\[/caption\]

If you got copious free time or are just curious about the conary
backend, clone the **PackageKit**
[repository](https://gitorious.org/packagekit) and check it out.
