---

date: 2013-12-09
slug: |
  emacs-rope-for-python-development
tags:
 - Emacs
 - Python
 - Rope
 - Pymacs
 - gnome
title: Emacs + Rope for Python Development
---

![screenshot](https://farm3.staticflickr.com/2875/11294955694_5450819b65_z_d.jpg)

**Disclaimer:** This is more of a note for myself than a proper
tutorial or howto, so I make no promises that this will work for you.
The setup used through this post was a Mac OS laptop upgraded to the
very latest version of the OS.

Ever since I started doing **Python** development using **Emacs**, I
have unsuccessfully tried to configure [Rope](http://rope.sourceforge.net/), "a python refactoring library"... until last Friday. Turns out I wasn't too far off the mark
during the many iterations I went through to get it done, but the
following post was tremendously helpful to
me: <http://www.saltycrane.com/blog/2010/05/my-emacs-python-environment/>

Here's what worked for me:

Install **Pymacs** (Emacs part):

-   [Download](https://github.com/pinard/Pymacs/tarball/v0.2) latest
    (0.25 as of the writing of this post)
-   cd to the source code directory
-   make
-   mkdir \~/.emacs.d/vendor/pymacs
-   cp pymacs.el \~/.emacs.d/vendor/pymacs/pymacs.el
-   [emacs -batch -eval '(byte-compile-file
    "\~/.emacs.d/vendor/pymacs/pymacs.el")'](https://github.com/pinard/Pymacs/tarball/v0.25)

[Install Pymacs (](https://github.com/pinard/Pymacs/tarball/v0.25)Python
part):

-   sudo pip install <https://github.com/pinard/Pymacs/tarball/v0.2>

Install **ropemacs** and **rope** with sudo pip install
<http://bitbucket.org/agr/ropemacs/get/tip.tar.gz>

Now configure Emacs by adding the following lines to your init.el file:

| (require 'pymacs)
| (pymacs-load "ropemacs" "rope-")
| (setq ropemacs-enable-autoimport t)

Finally, start up Emacs and make sure to read this
[document](https://bitbucket.org/agr/ropemacs) for some examples on how
to use Rope.
