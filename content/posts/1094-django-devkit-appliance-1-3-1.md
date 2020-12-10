---

date: "2011-09-14 19:24"
slug: |
  django-devkit-appliance-1-3-1
tags:
 - english
title: Django DevKit Appliance 1.3.1
---

\[caption id="attachment_853" align="alignleft" width="300"
caption="Django"\][![Django
logo](http://www.ogmaciel.com/wp-content/uploads/2010/03/django-logo-negative-300x136.png)](http://www.ogmaciel.com/wp-content/uploads/2010/03/django-logo-negative.png)\[/caption\]

I rebuilt the appliance to use the latest [Django 1.3.1
release](https://www.djangoproject.com/weblog/2011/sep/09/security-releases-issued/)
to deliver the **security fixes** found in the previous version. There
are also several other updated packages included.

If you want to play with this appliance, feel free to download it in the
following formats:

-   [Django DevKit Raw Filesystem
    x86](http://downloads.ogmaciel.com/djangodevkit/v1.3.1/djangodevkit-1-x86.hdd.gz)
    (390 MB - SHA1: 3ae0ab73477be3308011735aac5b33908700a82d)
-   [Django DevKit Raw Filesystem
    x86_64](http://downloads.ogmaciel.com/djangodevkit/v1.3.1/djangodevkit-1-x86_64.hdd.gz)
    (411 MB - SHA1: 3fb040a9b48b0dc248e5424271d4ea9274605530)
-   [Django DevKit ISO
    x86](http://downloads.ogmaciel.com/djangodevkit/v1.3.1/djangodevkit-1-x86-disc1.iso)
    (517 MB - SHA1: 88d5f1065bf5646d7cd952e8ccac435a40176fef)
-   [Django DevKit ISO
    x86_64](http://downloads.ogmaciel.com/djangodevkit/v1.3.1/djangodevkit-1-x86_64-disc1.iso)
    (537 MB - SHA1: cee9f5f584261d69baca09efeb58278d23cab410)

Speaking of Raw Filesystem images, here's how I currently use it  with
**QEMU**. In my **.bashrc** file I have an alias that will boot them and
redirect it's internal ports **80** and **22** (**apache** and **ssh**)
to my system's port **8080** and **2222** respectively. I also forward
port **3389** for Windows systems.

`sudo qemu-kvm -m 2048 -hda "$1" -boot c -soundhw ac97 -redir tcp:8080::80 -redir tcp:2222::22 -redir tcp:9999::3389`

So when I call my alias and pass a raw filesystem image as an argument,
I can then use **localhost** as the destination to my http and ssh
connections.

\[caption id="attachment_1462" align="aligncenter" width="300"
caption="Django Dev Kit on QEMU"\][![Django Dev Kit on
QEMU](http://en.ogmaciel.com/wp-content/uploads/2011/09/Screenshot-QEMU-1-300x175.png)](http://en.ogmaciel.com/wp-content/uploads/2011/09/Screenshot-QEMU-1.png)\[/caption\]

I also have a special configuration in my **.ssh/config** file to make
it easier for me to ssh to these virtual systems and not have to change
my **known_hosts** file every time I boot a different system and try to
ssh to localhost on port 2222:

`Host qemu User root Port 2222 Hostname localhost StrictHostKeyChecking no UserKnownHostsFile /dev/null`
