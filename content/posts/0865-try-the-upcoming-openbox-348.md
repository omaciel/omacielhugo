---

date: 2008-11-23
slug: |
  try-the-upcoming-openbox-348
tags:
 - rpath
title: Try the upcoming Openbox 3.4.8
---

if you like [Openbox](http://icculus.org/openbox) and want to play with
the upcoming 3.4.8 version, download the release candidate 1 here:
<http://icculus.org/openbox/releases/openbox-3.4.8-rc1.tar.gz>. Keep in
mind that you'll have to patch
[obconf](http://icculus.org/openbox/index.php/Openbox:Download#ObConf_-_Openbox_configuration_tool)
by basically replacing 'obrender-3.0' and 'obparser-3.0' to
'obrender-4.0' and 'obparser-4.0' respectively in the configure.ac file.

Or you use a **conary-based** system, there is a version packaged
directly from their **git** repository which you can install by running
**sudo conary update openbox=foresightlinux.rpath.org\@fl:2-devel**.

If you find an issue, please read this
[page](http://icculus.org/openbox/index.php/Openbox:Contribute) to learn
how to report it (that goes for translations too).
