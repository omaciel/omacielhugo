---

date: 2008-07-13
slug: |
  registering-a-gconf-schema-via-setuppy
tags:
 - english
title: Registering a gconf schema via setup.py?
---

I spent a good chunk of my evening trying to implement the automatic
registration of a gconf schema file via a setup.py and... got nowhere.
Seems that most people who wanted to do the same ended up running
gconftool-2 directly as such:

> GCONF_CONFIG_SOURCE=\`gconftool-2 ---get-default-source\` gconftool-2
> ---makefile-install-rule /etc/gconf/schemas/\*.schemas

Has anyone got any advice (patches wouldÂ  be awesome) to go with my
[code](http://code.google.com/p/billreminder/source/browse/trunk/setup.py)?
