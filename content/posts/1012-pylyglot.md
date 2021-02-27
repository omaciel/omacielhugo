---

date: 2010-09-26
slug: |
  pylyglot
tags:
 - english
 - pylyglot
 - translations
title: Pylyglot
---

Been working on a pet project to help out with theÂ **GNOME**
translations (as well as have a chance to learn more about **Django**)
and the end product is now available at
[www.pylyglot.org](http://pylyglot.org/). Basically, it is a database of
all strings from all available GNOME packages parsed to (hopefully) help
open source translators with their effort by providing suggestions based
on existing translations.

But wait, there's more! Since the entire collection of GNOME packages is
available for your perusal, you can check how a certain word was
translated across all packages and use this information to standardize
the translation for the entire project.

![Pylyglot](http://www.ogmaciel.com/wp-content/uploads/2010/09/Pylyglot-300x211.png)

Now, this is not an original idea and I wouldn't be here talking about
[Pylyglot](http://pylyglot.org/) if it weren't for
[Open-Tran.eu](http://open-tran.eu/whatfor.html), one of the coolest
translation tools out there and much more complete than what I have so
far!

Right now, [Pylyglot](http://www.pylyglot.org/) is running on my account
on **Dreamhost** and is limited to whatever their threshold for a
process is, meaning: updating the database is currently done outside of
the system (most of the time on my desktop) and a database dump is later
generated and uploaded to Dreamhost. I've been working out a way to
simplify this process and make it more dynamic and autonomous, but am
not there yet.

Also, there's a preliminary **XML-RPC** interface that may hopefully be
useful to create plugins for your favorite text editor or translation
tool.

Well, if you want to lend a hand, check out the source code and make
sure to read the **README** file. I'm always on **\#pylyglot** at
**freenode** too, so feel free to drop by and say hello.
