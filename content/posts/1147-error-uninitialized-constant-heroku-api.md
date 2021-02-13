---

date: 2012-08-23
slug: |
  error-uninitialized-constant-heroku-api
tags:
 - Fedora 17, Heroku, english
title: "Error: uninitialized constant Heroku::API (NameError)"
---

Got stuck with this error on **Fedora 17** while trying to get a project
onto **Heroku**:

> Error: uninitialized constant Heroku::API (NameError)

After some quick back and forth with the Heroku guys I finally got it
fixed:

> \$  rvm uninstall 1.9.3  \$  rvm reset \$  sudo yum reinstall openssl
> openssl-devel \$  rvm install 1.9.3  \$  rvm use 1.9.3 ---default \$
>  heroku login

Hope this helps someone else :)
