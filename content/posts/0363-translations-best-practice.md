---

date: "2006-07-21 19:19"
slug: |
  translations-best-practice
tags:
 - english
title: Translations Best Practice
---

Whenever we work on the Brazilian Portuguese translations for Ubuntu
Linux through the Rosetta system, we come across some strings that are
pretty straight forward to translate, such as "The book is on the
table". hehehe But... not all strings are as obvious and require some
further investigation. Our team has compiled a
[document](http://wiki.ubuntubrasil.org/l10n) (pt_BR) which not only
explains how Launchpad and Rosetta work, but also has a section
dedicated to some of the "hairy" strings we've come across.

This article is my attempt to demonstrate, in a somewhat more graphical
manner, some of our best practices for when dealing with these cases.
**First case**: A "normal" string
![image0](http://static.flickr.com/69/194901576_78c2577694.jpg)

Here we can see that the variables %s do not get translated and are kept
in the final translated string.

**Second case**: Dealing with the \[tab\] character

![image1](http://static.flickr.com/57/194901577_c4c8e3aaa1.jpg)

A lot of people will substitute the \[tab\] character for an actual tab,
but... The instruction right between the two text boxes will tell you to
leave them as they are in the final translated string. **Third case**:
Dealing with theÃ¢â€ Âµ character

![image2](http://static.flickr.com/61/194901578_0a3d89e42a.jpg)

Here you are supposed to replace the arrow with a new line character, by
pressing the ENTER key.

**Fourth case**: Dealing with the Ã¢â‚¬Â¢ character

![image3](http://static.flickr.com/60/194901579_9dd0da099e.jpg)

The little dot represents a blank space that needs to be inserted into
the translated string. What if the string has 10 little dots? Well, you
guessed it. You'll have to insert 10 blank spaces.

We can see from the message above that it was actually derived from the
Tray.cs file from the Tomboy program, as show below:

![image4](http://static.flickr.com/63/194901580_5d5c628239.jpg)

**Fifth case**: Dealing with text within XML tags
![image5](http://static.flickr.com/63/194901581_cbd25f14bd.jpg)

The final case I want to demonstrate is how to deal with those pesky
strings which have embedded XML tags in them. The good news is that you
do not translate the attributes inside the tags themselves, but only the
text surrounded by them. In this case, the word "here" is the only part
that gets translated.

Well, hopefully this was helpfull/informative to some of you. I'm
planning to add more articles related to how to participate with the
Ubuntu community soon.
