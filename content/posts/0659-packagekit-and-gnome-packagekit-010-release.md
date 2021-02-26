---

date: 2007-10-15
slug: |
  packagekit-and-gnome-packagekit-010-release
tags:
 - english
title: PackageKit and gnome-packagekit 0.1.0 release!
---

[PackageKit](http://www.packagekit.org/) is DBUS packaging abstraction
layer that makes use of a cross-distro, cross-architecture API to manage
your system's packages. In other words, it is a way for updating and
administering software on a GNU/Linux system without worrying about the
distro or underlying package management system.

Having gone from concept to release in inly 6 weeks of intensive
collaborative work, version 0.1.0 already sports backends for
[conary](http://en.wikipedia.org/wiki/Conary_%28package_manager%29),
[yum](http://en.wikipedia.org/wiki/Yellow_dog_Updater%2C_Modified),
[apt](http://en.wikipedia.org/wiki/Advanced_Packaging_Tool), box, and
alpm as well as comprehensive documentation and some translations
([Vladimir Melo](http://vladimirmelo.wordpress.com/) and I managed to
get the Brazilian Portuguese translation done just in time!).

[![GNOME PackageKit in
action](http://farm3.static.flickr.com/2112/1581501049_68f463f34d.jpg)](http://www.flickr.com/photos/ogmaciel/1581501049/)

More information about this release can be found
[here](http://lists.freedesktop.org/archives/packagekit/2007-October/000657.html),
including information on where to get tarballs and RPMs. Want to help
out with the translations? Feel like adding a backend for your distro?
Just come by \#PackageKit on Freenode and join our [mailing
list](http://lists.freedesktop.org/mailman/listinfo/packagekit).

As always, [Foresight](http://www.foresightlinux.org) users can get this
goodness by running *sudo conary updateall*. Then kiss the command line
goodbye and use the Add/Remove Software entry in the System -\>
Administration menu.

With the upcoming [FOSSCamp](http://fosscamp.org), I'd love to talk to
some of the Ubuntu guys (yeah [Jorge
Castro](http://stompbox.typepad.com/blog/), I'm talking to you!) about
getting PackageKit into Ubuntu 8.04.

Speaking of Ubuntu, I'll be in Boston on Oct. 26-28 and would love to
meet and hangout with the Brazilian and Portuguese \[add your country
here\] guys going to [UDS](https://wiki.ubuntu.com/UDS-Boston/). What do
you say guys?
