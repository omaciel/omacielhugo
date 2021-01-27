---

date: 2007-09-14
slug: |
  adding-vinagre-to-conary
tags:
 - rpath
title: Adding Vinagre to Conary
---

Tonight during our [TriLUG](http://www.trilug.org/) meeting,
[Ken](http://ken.vandine.org/) packaged
[Vinagre](http://www.gnome.org/projects/vinagre/) for the first time
using [Conary](http://wiki.rpath.com/wiki/Conary), the distributed
software management system for Linux distributions. It took him
literally no more than 5 minutes to write up the recipe, cook (package)
it, and send it to the repository.

[![vinagre](http://farm2.static.flickr.com/1118/1375414113_cfb57c6015.jpg)](http://www.flickr.com/photos/ogmaciel/1375414113/)

Vinagre is a VNC client well integrated with GNOME , current being
developed by [Jonh Wendell](http://www.bani.com.br/). For those curious
as to what the recipe for packaging it was, take a look:

```python

loadRecipe('gnomepackage.recipe')
class Vinagre(GnomePackageRecipe):

    name = 'vinagre'
    version = '0.3'

    buildRequires = [
      'GConf:devel',
      'ORBit2:devel',
      'desktop-file-utils:runtime',
      'gnutls:devel',
      'gtk-vnc:devel',
      'libglade:devel',
    ]

```

Then it is a matter of executing:

`cvc cook vinagre.recipe && cvc commit && cvc cook vinagre`

If Jonh releases a new version tomorrow, say 0.4, all we have to do is
edit the file vinagre.recipe and change the 3 for a 4 and execute the
commands above. It doesn t get any easier than this!
