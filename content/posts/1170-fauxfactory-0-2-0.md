---

date: "2014-05-08 19:12:00"
tags:
 - python
 - testing
 - qe
title: FauxFactory 0.2.0
---

Today I\'m releasing **FauxFactory 0.2.0** with a new feature, a \"Lorem
Ipsum\" generator. I confess that I did not look around for any existing
implementation in python out there and just started writing code. My
idea was to create a method that would:

Return a \"Lorem Ipsum\" string if I passed no arguments:

``` {.python}
In [1]: from fauxfactory import FauxFactory

In [2]: FauxFactory.generate_iplum()
Out[2]: u'Lorem ipsum dolor sit amet, consectetur adipisicing elit,
sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut
enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi
ut aliquip ex ea commodo consequat. Duis aute irure dolor in
reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla
pariatur. Excepteur sint occaecat cupidatat non proident, sunt in
culpa qui officia deserunt mollit anim id est laborum.'
```

Return a single paragraph with a fixed number of words if I passed a
numeric **words=x** argument. If **words** was a large number, the text
would \'wrap around\' as many times as needed:

``` {.python}
In [3]: FauxFactory.generate_iplum(words=8)
Out[3]: u'Lorem ipsum dolor sit amet, consectetur adipisicing elit.'

In [4]: FauxFactory.generate_iplum(words=80)
Out[4]: u'Lorem ipsum dolor sit amet, consectetur adipisicing elit,
sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut
enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi
ut aliquip ex ea commodo consequat. Duis aute irure dolor in
reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla
pariatur. Excepteur sint occaecat cupidatat non proident, sunt in
culpa qui officia deserunt mollit anim id est laborum.'
```

If **paragraphs=x** was used, then a given number of paragraphs
containing the entire \"Lorem Ipsum\" string is returned:

``` {.python}
In [5]: FauxFactory.generate_iplum(paragraphs=1)
Out[5]: u'Lorem ipsum dolor sit amet, consectetur adipisicing elit,
sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut
enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi
ut aliquip ex ea commodo consequat. Duis aute irure dolor in
reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla
pariatur. Excepteur sint occaecat cupidatat non proident, sunt in
culpa qui officia deserunt mollit anim id est laborum.'

In [6]: FauxFactory.generate_iplum(paragraphs=2)
Out[6]: u'Lorem ipsum dolor sit amet, consectetur adipisicing elit,
sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut
enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi
ut aliquip ex ea commodo consequat. Duis aute irure dolor in
reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla
pariatur. Excepteur sint occaecat cupidatat non proident, sunt in
culpa qui officia deserunt mollit anim id est laborum.\nLorem ipsum
dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor
incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam,
quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea
commodo consequat. Duis aute irure dolor in reprehenderit in voluptate
velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint
occaecat cupidatat non proident, sunt in culpa qui officia deserunt
mollit anim id est laborum.'
```

Finally, if both **words** and **paragraphs** are used, then a given
number of paragraphs with the specified number of words is returned,
with the text \'flowing\' and \'wrapping around\' as needed:

``` {.python}
In [7]: FauxFactory.generate_iplum(paragraphs=1, words=7)
Out[7]: u'Lorem ipsum dolor sit amet, consectetur adipisicing.'

In [8]: FauxFactory.generate_iplum(paragraphs=3, words=7)
Out[8]: u'Lorem ipsum dolor sit amet, consectetur adipisicing.\nElit,
sed do eiusmod tempor incididunt ut.\nLabore et dolore magna aliqua.
Ut enim.'
```

The package is available on
[Pypi](https://pypi.python.org/pypi/fauxfactory/0.2.0) (sadly the page
is not rendering correctly\... suggestions welcome) and can be installed
via **pip install fauxfactory**.

If you have any constructive feedback, suggestions, or file a bug report
or feature request, please use the
[Github](https://github.com/omaciel/fauxfactory) page.
