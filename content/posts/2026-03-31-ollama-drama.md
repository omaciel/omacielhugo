---
author:
- Og Maciel
date: 2026-03-31
description: "Where Engineers Herd LLMs and Wrangle Prompts"
title: "Ollama Drama"
tags:
 - substack
type: post
---

# Ollama Drama

## Where Engineers Herd LLMs and Wrangle Prompts

[![](/images/ollama-drama-01.png)](https://substackcdn.com/image/fetch/$s_!aHHu!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F1ee0e43d-b06d-4e8d-a716-a0584afdbe3d_1067x600.png)

Ollama Drama Workshop

So, let me tell you about this thing called **[Ollama Drama](https://github.com/omaciel/ollama-drama/tree/main)** and why it exists.

Last spring, I ran an internal workshop at work because I had been noticing the same thing over and over again: a lot of people were curious about LLMs, a lot of people had opinions about AI, a lot of people had maybe played with ChatGPT once or twice, but not that many people had actually sat down and gotten their hands dirty with the tooling in a way that felt practical, safe, and not too scary.

And I wanted to change that.

Not by giving a big philosophical talk about the future of AI, not by making it overly academic, and definitely not by assuming everyone in the room already knew what they were doing.

The whole point was the opposite of that.

The workshop was built for people who know their way around GitHub — and I say GitHub on purpose, not necessarily git — and for people who have maybe entry-level Python skills and are willing to poke around and see what happens. That was enough. That was the bar. If you had that, then I figured I could get you from “I’ve heard of this stuff” to “Oh, wait a second, I can actually do something with this.”

And that’s really what **Ollama Drama** was… or is.

It’s a hands-on workshop where engineers get to play with LLMs locally, through the command line, through simple Python scripts, through prompts, through small exercises, and do it all in a way that feels more like a lab than a lecture. The idea was always to make it light, practical, and fun. That was the promise. We were going to herd some LLMs, wrangle some prompts, and hopefully not fry anybody’s laptop in the process.

And, by the way, it worked.

The workshop was well received, well attended, and, to my pleasant surprise, it even got delivered again later by another engineer (hi [Andrew Potozniak](https://open.substack.com/users/6463517-andrew-potozniak?utm_source=mentions) ) who attended the first session and volunteered to run it himself. That to me was probably the best sign that the workshop had landed the way I hoped it would. When someone takes your material and says, “Yeah, I want to help other people learn this too,” that’s a pretty good feeling.

So what actually happens in the workshop?

Well, first and foremost, people get to run LLMs **locally**. That part mattered a lot to me. I wanted to remove as much friction as possible. No cloud dependency. No worrying about API rate limits. No having to send prompts somewhere else and wonder if you just pasted something you shouldn’t have.

Just install Ollama, pull down a model, and go. That was one of the big selling points from the start: privacy, speed, simplicity. Everything local. Everything simple enough that someone with a reasonably modern laptop could follow along. That was a major goal of the workshop from day one.

From there, we start playing.

We look at models. We talk about what model sizes mean. We talk about why a tiny little model with fewer parameters might still be perfectly fine for what you want to do, and why trying to run some giant monster model locally might be a very effective way to turn your laptop into a breakfast appliance. We compare things. We try stuff. We make jokes. We ask silly questions. We ask serious questions. We see how different models answer the same prompt in different ways. And that part alone is always fun because it stops being abstract very quickly.

Then we move into the command line.

This is where people get to see that working with local LLMs does not need to be some giant ordeal. You can list models. Pull models. Run models. Stop them. Copy them. Remove them. Chat with them. Feed them a file. Ask them to summarize something. Hit them through curl. Use the generate endpoint. Use the chat endpoint. All that good stuff. And suddenly the whole thing starts feeling much less mystical and much more like, “Oh, okay, this is just another tool. A really interesting one, yes, but still a tool.”

Then comes the fun part.

The workshop was designed as a hands-on experiment, so I created a GitHub [repository](https://github.com/omaciel/ollama-drama/tree/main) with a few small challenges in it. Nothing too crazy. Fairly easy problems, but didactic ones. The kind of problems that force you to touch the right things. You clone the repository, create a Python virtual environment, install a handful of dependencies, run a chatbot, inspect a script, change a prompt, run tests, fix what’s broken, and then submit a pull request when you’re done.

That’s really the heartbeat of the whole workshop.

People aren’t just watching me do things. They’re actually doing them.

They are modifying prompts.

They are seeing tests fail.

They are making them pass.

They are creating small custom models.

They are realizing, usually in real time, that a lot of what feels magical at first is actually very approachable once you understand where the levers are.

[![](/images/ollama-drama-02.png)](https://substackcdn.com/image/fetch/$s_!pUAA!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F53eface7-a4d3-47a2-a9c6-15a29cfcfbe5_1066x598.png)

Certificate of Completion

And if they complete everything successfully, they get a certificate of completion. Which, yes, is a little bit silly and a little bit fun, but that was deliberate too. The whole workshop was meant to have some playfulness baked into it. If you’re going to spend 60 to 90 minutes learning something new, then I want you to enjoy it. I want you to walk away feeling like you learned a thing and had a good time doing it.

The [study plan](https://github.com/omaciel/ollama-drama/blob/main/studyplan.md) behind the workshop is pretty straightforward.

- You start with installation, setup, and why local models are useful.
- Then you move into model architecture and the tradeoffs around size, performance, and resources.
- Then into the CLI and the core commands you need to actually do something useful.

And then finally into the customization and integration side of things: system prompts, Modelfiles, Python scripts, curl, APIs, tests — all the good stuff.

In other words, enough to get someone started for real, without drowning them in theory. And that’s important to me.

Because I didn’t want this to be a workshop where people leave saying, “Wow, that was interesting,” but then never touch the technology again. I wanted people to leave saying, “I think I can keep going on my own.”

That was always the goal.

Now, the repository is public. The exercises are there. The whole thing has been around for almost a year now, and even now people still reference it, share it, and mention that they found it useful and fun. That makes me really happy, because I do think there’s something special about giving engineers a safe, low-friction playground where they can learn by doing instead of just listening.

If you want to take a look, the repository is [here](https://github.com/omaciel/ollama-drama) and the [slides](https://docs.google.com/presentation/d/e/2PACX-1vSI1N_ZOv6SSDNG562EkNI9bpM8_RbkiaglMs6NRtsTXWW95nbPlGvhRwEt3CiDOv-xOYfF5HV2A-a6/pub?start=true&loop=true&delayms=5000) are here.

Now, on a more personal note, my last post here was on **March 6**, and I haven’t really written much since then other than the occasional note. That’s mostly because I’ve been on a bit of a self-improvement journey at work that has consumed a lot of the time I used to spend writing here. Reading time, thankfully, I protected. Time with my family too. But writing had to give a little.

And if I’m being honest, the journey has felt a bit like Odysseus trying to get back to Ithaca after the war. A lot of detours. A lot of delays. A lot of weird islands you didn’t plan on visiting. But closer to Ithaca I am, I think. Slowly.

So this felt like a good post to come back with.

Because **Ollama Drama** is one of those things I built that was practical, useful, and fun all at once. It helped people. It got reused. It lowered the barrier for folks to start playing with AI tools. And those are exactly the kinds of things I like to make.

So if you want to use it, adapt it, borrow from it, or turn it into something better for your own team, by all means, please do.

Use it.

Change it.

Break it.

Improve it.

And if you do find it useful, fun, ridiculous, helpful, or all of the above, drop me a line and let me know. I’d genuinely love to hear how it goes.

Because at the end of the day, this course is really about giving engineers a practical way to stop being intimidated by LLMs and start treating them the way engineers tend to treat every other interesting system:

- By poking at it.
- By testing it.
- By modifying it.
- And by seeing what happens.

And that, to me, is where the real fun begins.
