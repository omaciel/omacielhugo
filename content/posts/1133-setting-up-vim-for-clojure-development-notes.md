---

date: 2012-05-16
slug: |
  setting-up-vim-for-clojure-development-notes
tags:
 - Eclipse
 - Clojure
 - vim
 - repl
 - lein
 - Dropbox
 - english
title: Setting up Vim for Clojure development notes
---

Started the process of getting jiggy with [Clojure](http://clojure.org/)
at work and didn't like the idea of using **Eclipse** for my day to day
work... so I started looking at how to make **vim** and **clojure** get
along and came across a great [post](http://writequit.org/blog/?p=386)!
Here are the distilled notes plus minor tweaks to get anyone out there
trying to do the same thing going:

1.  Download **VimClojure**
    (<http://www.vim.org/scripts/script.php?script_id=2501>)
2.  Download **VimSlime** (<https://github.com/jpalardy/vim-slime>)
3.  Extract these files into your **\~/.vim** folder
4.  Add the following lines to **\~/.vimrc**:
    -   \" Settings for VimClojure
    -   let vimclojure\#HighlightBuiltins = 1
    -   let vimclojure\#ParenRainbow = 1
    -   \" Send entire file to repl
    -   nmap \<C-m\> ggVG\<C-c\>\<C-c\>
5.  Start a repl session inside screen:
    -   screen -S clojure
    -   lein repl
6.  Open a clojure file with vim and highlight the method you want to
    evaluate
7.  Press ctrl + c twice
    -   For session name prompt, enter 'clojure' which is the name of
        the screen session
    -   For window name prompt, accept the default number displayed
8.  The selected code should be evaluated in the screen session
9.  Press ctrl + c, v to get prompt again

![Vim and Clojure sitting on a
tree](http://dl.dropbox.com/u/102224/vim_clojure.png)

**NOTES**:

-   I chose to start a repl using
    [lein](https://github.com/technomancy/leiningen) but you can use
    whatever you're familar with to get a repl started
-   I have lein inside a directory in my **Dropbox** as well as all of
    my vim files and plugins. I then created soft links to them in my
    \$HOME directory which makes this whole thing very easy to access
    from different systems as long as Dropbox is installed :)
