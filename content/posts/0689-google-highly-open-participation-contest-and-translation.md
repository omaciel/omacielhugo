---

date: 2007-12-19
slug: |
  google-highly-open-participation-contest-and-translation
tags:
 - rpath
title: Google Highly Open Participation Contest and Translations
---

If you're participating in the [Google Highly Open Participation
Contest](http://code.google.com/opensource/ghop/2007-8) and is involved
with the translation process, or just want a sure way to test your
translations with the latest GNOME, then go get your copy of the [GNOME
Developer Kit now](http://live.gnome.org/GnomeDeveloperKit)!

You could then download the message catalog file for the application you
want to translate (in my case I got the [Brazilian
Portuguese](http://l10n.gnome.org/POT/empathy.HEAD/empathy.HEAD.pt_BR.po)
file for Empathy) to your [language](http://l10n.gnome.org/languages/)
and use **poEdit** (already included) to work on your translation. You
can also take advantage of **translate-toolkit** to really do some
serious QA work!

Once you've gone through the steps above, the best thing to do is file a
new [bug report](http://bugzilla.gnome.org/) choosing the
**Translations** category and attaching your finished master piece. It
is recommended that you get in touch with your language team's
coordinator first to make sure nobody else is already working on the
same application.

Now comes the best part: testing your work! Note that empathy is only
partially translated in the screenshot below (check out the button):

[![Empathy running on GNOME
Live](http://farm3.static.flickr.com/2313/2123268702_99005f40d7.jpg)](http://www.flickr.com/photos/ogmaciel/2123268702/)

One of the benefits of using poEdit for your translations (some people
like to use a combination of poEdit and a text editor, like vim... that
would be me!) is that it automatically checks the file for formatting
issues AND generates a compiled version of your translations. It is this
compiled version, a file that ends with the extension .mo, that gets
used at runtime by your application in order to display its messages in
the chosen language.

What we need to do is make a backup copy of the original compiled file
and substitute it with your brand new translation:

> cp /usr/share/locale/pt_BR/LC_MESSAGES/empathy.mo
> \$HOME/original_empathy.mo cp empathy.mo
> /usr/share/locale/pt_BR/LC_MESSAGES/empathy.mo

Now restart the application, and... voilÃƒÂ¡:

[![Empathy running on GNOME Live, 100%
translated](http://farm3.static.flickr.com/2238/2123268708_cc88d32fee.jpg)](http://www.flickr.com/photos/ogmaciel/2123268708/)

Now, remember that bug report (here's
[mine](http://bugzilla.gnome.org/show_bug.cgi?id=504373)) you've filed
before? Well, once someone from your language team reviews it and
commits it, it is only a matter of waiting for
[conary](http://wiki.rpath.com/wiki/Conary) (the packaging management
system behind the Developer Kit) to notify you when the new version is
available for update. Below is the screenshot of my system running a
vanilla GNOME in Brazilian Portuguese:

[![GNOME Live in Brazilian
Portuguese](http://farm3.static.flickr.com/2166/2123268698_e1f1a4c640.jpg)](http://www.flickr.com/photos/ogmaciel/2123268698/)

Got any questions? Feel free to drop me a line.
