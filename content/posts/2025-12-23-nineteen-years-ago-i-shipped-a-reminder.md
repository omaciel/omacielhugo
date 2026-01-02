---
author:
- Og Maciel
date: 2025-12-23
description: "Nineteen Years Ago, I Shipped a Reminder"
title: "Nineteen Years Ago, I Shipped a Reminder"
tags:
 - software engineering
 - open source
 - nostalgia
 - personal
 - substack
type: post
---

# Nineteen Years Ago, I Shipped a Reminder

### How BillReminder, Glade, and a stubborn love of simplification shaped my early years in open source.

![](/images/nineteen-years-ago-i-shipped-a-reminder-image-1.heic)BillReminder screens

I recently wrote about some of the reasons _[why](https://ogmaciel.substack.com/p/tracing-the-edges-of-my-ikigai)_ I do [what](https://ogmaciel.substack.com/p/tracing-the-edges-of-my-ikigai-what) I do, especially when it comes to the professional path I’ve taken. It started long before software, back when I wanted to be a scientist—working in genetic recombination and gene therapy, trying to help people overcome genetic conditions as early as possible, ideally before they ever had to live with the consequences of them.

That same motivation eventually carried me into software engineering. I’ve always been drawn to simplifying things, improving systems, and finding ways to make people’s lives a little easier through the tools I build.

Today, while going through some old photos, I came across screenshots from projects I worked on back in 2006 and 2007—right around the time I was trying to rebrand myself. Until then, I had mostly been a desktop software engineer working with Microsoft technologies like Visual Basic. But I wanted to expand beyond that, to become a Python developer and a C# developer as well—especially as C# was beginning to be open-sourced and made available on Linux. That shift opened the door for me to think seriously about building native Linux applications.

One project from that time stood out: **[BillReminder](https://github.com/omaciel/billreminder)**.

[![](/images/nineteen-years-ago-i-shipped-a-reminder-image-2.heic)](https://substackcdn.com/image/fetch/$s_!lqAW!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F95c03cd8-139b-454d-8c5f-ce9c3f3061b4_374x111.heic)BillReminder notification

Back then, if you wanted an experience even remotely similar to what Visual Studio or Visual Basic offered, but for GTK-based applications, you used a tool called **Glade**. Glade gave me a familiar, visual way to design interfaces, which made the transition easier. My approach to learning has always been the same: build something I would actually use every day. That way, I’d have skin in the game. If it annoyed me, I’d fix it. If it was missing a feature, I’d add it.

BillReminder did exactly that. It reminded me when bills were due, sent notifications, and showed a clear graphical breakdown of expenses and deadlines. I depended on it daily, which meant I was constantly improving it.

By April of 2007, while working on BillReminder, I ran into a familiar frustration. I needed a table—rows and columns—to display bills. GTK’s TreeView widget was powerful, but painfully verbose. Getting even a simple grid on screen required an overwhelming amount of boilerplate code, right down to the cell level.

So I did what felt natural: [I abstracted it](https://omaciel.github.io/posts/simplifying-gtktreeview/).

I built a generic TreeView helper that allowed me to define tables using a simple, Pythonic dictionary. Instead of pages of repetitive setup code, I could describe what I wanted declaratively and get a working table immediately. It dramatically simplified my own code—and, as it turned out, other people’s as well.

I shared the [code](https://omaciel.github.io/posts/generic-gtktreeview-generator/). I wrote [examples](https://omaciel.github.io/posts/another-post-about-a-generic-gtktreeview/). I documented how to use it.

![Generic PyGTK TreeView](/images/nineteen-years-ago-i-shipped-a-reminder-image-3.png)![Generic PyGTK TreeView](/images/nineteen-years-ago-i-shipped-a-reminder-image-4.jpeg)

![Generic PyGTK TreeView](/images/nineteen-years-ago-i-shipped-a-reminder-image-5.jpeg)![Generic PyGTK TreeView](/images/nineteen-years-ago-i-shipped-a-reminder-image-6.jpeg)

Generic PyGTK TreeView

That small decision ended up having a much larger impact than I expected. It brought attention to my work, helped establish me as a Linux-focused Python developer, and—more importantly—connected me with an incredible group of people. Other programmers contributed code, sent feedback, fixed bugs, and taught me things I didn’t know. I learned as much from that community as I did from the code itself.

Those relationships mattered. When I later went looking for work, doors opened—not because I checked every box on a job description, but because people knew my work. They’d read my posts. They’d used my code. They had a sense of who I was and how I approached problems.

Recently, I looked back at the BillReminder [repository](https://gitlab.gnome.org/Archive/billreminder). Some of that code is nearly **19 years old** —which feels like a lifetime in software. The last [contributions](https://gitlab.gnome.org/Archive/billreminder/-/commit/75206e05b53e7af70d29b0f327d63cbeaea0d31b) were made about nine years ago, mostly translations. The project has long since been archived in practice, even if not officially.

But the impact remains.

I made friends. I learned a ton. And over the years, I’ve heard from people who said those posts or that code helped them get started, helped them learn, or pushed them to build something of their own. Some of them went on to do remarkable things in open source and beyond.

If I allow myself one small moment of pride, it’s this: knowing I may have played—even in a tiny way—a role in someone else’s trajectory. All because of a persistent need I’ve always had: to simplify what’s complex, share what I learn, and build things that make life just a little easier.
