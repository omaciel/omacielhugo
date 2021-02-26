---

date: 2013-06-04
slug: |
  populating-a-katello-instance-using-the-cli
tags:
 - english, katello, Red Hat
title: Populating a Katello instance using the CLI
---

Lately I have been asked a lot about my previous
[script](http://bit.ly/13jSmSx) to automatically populate a
[Katello](http://www.katello.org/) server instance with real data (hi
**reyc**!) I wrote that a while back and though it still does contain
some helpful commands, I figured it was about time I updated it. Well,
it took me longer than I expected to find some time and clean it up, but
I think I can now show you a brand new script which also includes the
extra feature of downloading a manifest file directly from **Red
Hat**\'s portal and importing it as part of the process.

Currently the script assumes that you have the following information
(either as environmental variables or substituted into the script:

> **RHN_USERNAME**: A valid username for <https://access.redhat.com/>
>
> **RHN_PASSWORD**: A valid password for <https://access.redhat.com/>
>
> **DISTRIBUTOR**: An existing distributor UUID with access to Red Hat
> Enterprise Linux 6 Server products

The [new script](http://bit.ly/15Fk4di) is know to work with the very
**latest Katello nightly build**. If you have any suggestions or
constructive feedback, feel free to leave me a comment here or fork the
[gist](http://bit.ly/15Fk4di) and send me a pull request!
