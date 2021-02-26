---
category: |
  Portuguese
date: 2006-10-13
slug: |
  br-office-packaged-for-foresight-linux
tags:
 - rpath, foresight linux, conary, br-office
title: BR-Office empacotado para o Foresight Linux
---

Aproveitei o dia hoje para empacotar o
[Br-Office](http://openoffice.org.br/) para o [Foresight
Linux](http://www.foresightlinux.com/)!!! Como podem ver, esta' rodando
"redondinho"! :) No processo de empacota-lo, acabei descobrindo um
[bug](http://issues.rpath.com/browse/RPL-713) no glibc. Mas o pessoal da
rPath ja' tinha um patch e assim que o glibc for arrumado e for liberado
no repositorio oficial, voces poderao usufruir do Br-Office tambem.

[![image0](http://static.flickr.com/92/268734323_fc5248714f.jpg)](http://static.flickr.com/92/268734323_fc5248714f_b.jpg)

Para instala-lo:

> sudo conary update broffice.org

Caso voce ainda tenha a versao oficial do OpenOffice instalado, nao se
esqueca de remove-lo:

> sudo conary update broffice.org -openoffice.org
