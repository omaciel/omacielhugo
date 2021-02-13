---

date: 2007-03-23
slug: |
  problemas-usando-o-vmware-workstation-6-beta
tags:
 - portuguese
title: Problemas usando o VMware Workstation 6 (Beta)?
---

Testando a versÃ£o 6 do VMware Workstation (ainda em beta), eu recebi a
seguinte mensagem no console:

> /usr/lib/vmware/bin/vmware: /usr/lib/libstdc++.so.6: version
> \`CXXABI_1.3.1' not found (required by
> /usr/lib/vmware/lib/libvmwareui.so.0/libvmwareui.so.0)

Como eu tambÃ©m tinha visto uma mensagem durante o processo de
instalaÃ§Ã£o reclamando sobre o Gtk 2.4 (mais velho que Matuzalem), fui
trocar umas idÃ©ias com o pessoal aqui... e foi aÃ­ que descobri que
esta versÃ£o, por motivos que ninguÃ©m entende, usa uma versÃ£o antiga
do Gtk.

Para resolver o problema, modifique o atalho (ou crie um script) do
lanÃ§ado para contar a seguinte linha:

> LD_LIBRARY_PATH= VMWARE_USE_SHIPPED_GTK=yes vmware

Problema resolvido.
