---

date: 2007-09-11
slug: |
  mysql-issue-when-upgrading-to-wordpress-223
tags:
 - english
title: MySQL issue when upgrading to WordPress 2.2.3
---

Thought this may be helpful to someone else who also uses
[WordPress](http://wordpress.org/). Shortly after upgrading to the
latest version, I found the following warning message sprinkled all over
the administrative interface:

`[Can't open file: 'wp_comments.MYI'. (errno: 145)]`

A quick search pointed me to the
[solution](http://en.newinstance.it/2007/08/29/wordpress-database-error-cant-open-file-wp_commentsmyi-errno-145/):

`mysql> repair table wp_comments;`
