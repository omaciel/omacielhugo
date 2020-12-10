---

date: "2007-04-12 00:53"
slug: |
  simplificando-o-gtktreeview
tags:
 - portuguese
title: Simplificando o gtk.TreeView?
---

Estes dias quando estava trabalhando em uma nova interface grÃ¡fica para
um programa em python, reparei que toda vez que preciso de adicionar um
gtk.TreeView como uma lista (pense em uma planilha), sempre acabo
re-escrevendo o mesmo cÃ³digo que utilizei em um outro projeto... e
pensei:

\"Por que nÃ£o criar meu prÃ³prio kit/widget e parar de repetir
cÃ³digo?\"

Como nÃ£o tinha muito que fazer neste Ãºltimo sÃ¡bado, acabei criando o
**GenericList**, minha abstraÃ§Ã£o de um grk.TreeView.

[![A very generic gtk.TreeView base
class](http://farm1.static.flickr.com/252/456015767_28555b03d4.jpg)](http://www.flickr.com/photos/25563799@N00/456015767/)

Agora, toda vez que eu precisar adicionar uma lista em um de meus
programas, tudo que tenho de fazer Ã© instanciar esta classe, passando
somente a disposiÃ§Ã£o das columnas que eu preciso. Ou, criar uma nova
classe que "herda" desta classe genÃ©rica:

[![Subclassing the generic
list](http://farm1.static.flickr.com/252/456015819_4d8b64dd30.jpg)](http://www.flickr.com/photos/25563799@N00/456015819/)

O cÃ³digo para a classe acima Ã© sÃ³ isso aÃ­ mesmo... Dentro do meu
cÃ³digo eu instancio ela e posso adicionar, remover, etc registros
simplesmente usando os mÃ©todos genÃ©ricos add(), remove(), etc, etc,
como exibido abaixo:

> from billlistview import BillListView as ListView self.list =
> ListView() pixbuf = gtk.gdk.pixbuf_new_from_file('coin.jpg') list =
> \[\[pixbuf, 'Verizon', '\$ 49,00', '04/27/2007'\], \[pixbuf,
> 'T-Mobile', '\$ 55,99', '04/15/2007'\], \[pixbuf, 'Cable', '\$
> 111,99', '04/15/2007'\]\] self.list.addList(list)

[![A little test
application](http://farm1.static.flickr.com/245/456016226_d409606743.jpg)](http://www.flickr.com/photos/25563799@N00/456016226/)

E Ã© claro que nÃ£o podia faltar um screenshot do exemplo acima em
execuÃ§Ã£o.

[![A sample
demo](http://farm1.static.flickr.com/178/456016228_e7c4899286_o.png)](http://www.flickr.com/photos/25563799@N00/456016228/)

Ainda pretendo adicionar mais alguns mÃ©todos antes de usÃ¡-la no
[BillReminder](http://billreminder.sourceforge.net/), por exemplo.
