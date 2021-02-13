---

date: 2008-09-12
slug: |
  billreminder-royal-with-cheese-released
tags:
 - english
title: BillReminder \"Royale with cheese\" released
---

[![BillReminder](http://farm1.static.flickr.com/155/426001389_82fe3885b7_m.jpg)](http://www.flickr.com/photos/ogmaciel/426001389/)

It is with extreme pleasure that I annound the release of
[BillReminder](http://billreminder.gnulinuxbrasil.org) **\"Royale with
cheese\"** version **0.3.2**! This released was concentrated on fixing
bugs, adding more translations, and getting some work done for future
reporting features.

Straight from the NEWS file, here's what you'll find in this release:

**Bugs**:

-   Paid/Not Paid entries exist in File and Edit menus; Make them
    toggle/untoggle appropriately (Bug
    [\#13](http://code.google.com/p/billreminder/issues/detail?id=13))
-   Issues with date and time locale? (Bug
    [\#12](http://code.google.com/p/billreminder/issues/detail?id=12))
-   Ambiguity with Alerts and Alarms in preferences dialog (Bug
    [\#11](http://code.google.com/p/billreminder/issues/detail?id=11))
-   Make category names a unique field. (Bug
    [\#1](http://code.google.com/p/billreminder/issues/detail?id=1))
-   Newly added categories should be selected automatically (Bug
    [\#2](http://code.google.com/p/billreminder/issues/detail?id=2))
-   Make setting an alarm really optional. (Bug
    [\#4](http://code.google.com/p/billreminder/issues/detail?id=4))

**Backend**:

-   Changed BillReminder to use GConf for is configuration values.
    Thanks **Wilson Pinto Junior**
-   Changed BillReminder's command line parsing to use OptionParser.
    (Bug
    [\#3](http://code.google.com/p/billreminder/issues/detail?id=3))

**Translations**:

-   cs.po:Â  Pavel Å efrÃ¡nek
-   de.po:Â  Lorenz
-   en_CA.po:Â  Stuart Read
-   en_GB.po:Â  Jen Ockwell
-   es.po:Â  RamÃ³n CalderÃ³n
-   fi.po:Â  Ilkka Tuohela
-   fr.po:Â  Robert-AndrÃ© Mauchin
-   he.po:Â  Yaron
-   hr.po:Â  Mario Ä?aniÄ‡
-   hu.po:Â  HORVATH, Akos
-   it.po:Â  Sergio Zanchetta
-   nb.po: Tommy Mikkelsen
-   nl.po:Â  Martijn Cielen
-   pl.po:Â  Tomasz Z. Napierala
-   pt_BR.po:Â  Djavan Fagundes and Vladimir Melo
-   pt.po:Â  Susana Pereira
-   ro.po:Â  IonuÈ› Jula
-   ru.po:Â  Ilya B
-   sl.po:Â  Martin
-   sv.po:Â  Daniel Nylander
-   tl.po:Â  Jerome S. Gotangco
-   tr.po:Â  Rail Aliev

**Graphical Interface**:

-   Mnemonic labels/widgets and HIG work done to dialogs. Thanks
    **Wilson Pinto Junior**
-   Ask user for confirmation before editing an existing category.
-   Added pycairo as a dependency instead of python-Image. Color-coded
    categories now have a border around the colored tile.

**General**:

-   Renamed MANTAINERS to MAINTAINERS
-   Added uninstall method and versioning via autotools (Bug
    [\#547768](http://bugzilla.gnome.org/show_bug.cgi?id=547768))

Source code
[downloads](http://billreminder.gnulinuxbrasil.org/?page_id=26) are
currently available as well as an Ubuntu package. Please report any
issues, comments or feature requests using the
[Bugzilla](http://bugzilla.gnome.org/enter_bug.cgi?product=billreminder)
page.
