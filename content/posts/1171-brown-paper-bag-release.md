---

date: "2014-05-09 17:00:00"
tags:
 - python
 - testing
 - qe
title: FauxFactory 0.2.1
---

![](https://farm4.staticflickr.com/3373/3204502310_f8025dbd75_m.jpg)

Short on its heels, today I\'m releasing **FauxFactory 0.2.1** to fix a
[brown paper bag
bug](http://catb.org/jargon/html/B/brown-paper-bag-bug.html) I
encountered last night before going to bed.

Basically, the new \"Lorem Ipsum\" generator was not honoring the
**words** parameter if you asked for a string longer than 70 characters.
I have fixed the issue as well as added a new test to make sure that the
generator does the right thing.

The package is available on
[Pypi](https://pypi.python.org/pypi/fauxfactory/0.2.0) (sadly the page
is **still** not rendering correctly\... suggestions welcome) and can be
installed via **pip install fauxfactory**.

If you have any constructive feedback, suggestions, or file a bug report
or feature request, please use the
[Github](https://github.com/omaciel/fauxfactory) page.

*Image:Cry*\* by [LLewleyn Williams a.k.a.
SCUD](https://secure.flickr.com/photos/privatenobby/), some rights
reserved\*.
