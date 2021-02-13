---

date: 2009-12-10
slug: |
  rhel-5-appliance-sneak-peak
tags:
 - rpath
title: RHEL 5 Appliance sneak peak
---

I've already mentioned on my [Twitter](http://twitter.com/ogmaciel)
account about our latest feat here at **rPath**, namely, "[rPath Expands
Operating System Coverage with Red Hat Enterprise Linux 4 and
5](http://www.rpath.com/corp/component/content/article/57-2009-news/541-11302009b)."
But the more I play with our technology, the more gaga I get at how
simple we can make things!

So today I built a plain vanilla appliance based on the **Red Hat
Enterprise Linux Server 5** with**just enough operating system** and
launched it on **VMware vSphere 4**. I then ssh'ed into this system and
ran:

> \[<root@sweet> \~\]\#: conary update httpd Including extra troves to
> resolve dependencies: apr-util:rpm=1.2.7_6-1-1 apr:rpm=1.2.7_11-1-1
> mailcap:rpm=2.1.23_1.fc6-1-1 postgresql-libs:rpm=8.1.4_1.1-1-1
> Applying update job: Install apr(:rpm)=1.2.7_11-1-1 Install
> apr-util(:rpm)=1.2.7_6-1-1 Install httpd(:rpm)=2.2.3_6.el5-1-1 Install
> mailcap(:rpm)=2.1.23_1.fc6-1-1 Install
> postgresql-libs(:rpm)=8.1.4_1.1-1-1 \[<root@sweet> \~\]\# service
> httpd start Starting
> httpd:Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â 
> \[Â  OKÂ  \] \[<root@sweet> \~\]\# rpm -q httpd httpd-2.2.3-6.el5

![Apache Web
Server](http://www.ogmaciel.com/wp-content/uploads/2009/12/Screenshot-7-300x194.png)

In case you missed it, I used **conary** to install the httpd **RPM**
and the entire system is being managed by conary but compliant to what
rpm expects! Christmas did come early this year!!!
