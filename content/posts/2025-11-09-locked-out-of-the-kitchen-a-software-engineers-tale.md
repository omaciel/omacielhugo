---
author:
- Og Maciel
date: 2025-11-09
description: "Locked Out of the Kitchen: A Software Engineer's Tale"
title: "Locked Out of the Kitchen: A Software Engineer's Tale"
tags:
 - software engineering
 - personal
 - humor
 - work
 - substack
type: post
---

# Locked Out of the Kitchen: A Software Engineer’s Saturday

![](/images/locked-out-of-the-kitchen-a-software-image-1.heic)Photo by [Taylor Grote](https://unsplash.com/@taylor_grote?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText) on [Unsplash](https://unsplash.com/photos/person-holds-tray-of-muffins-on-tray-LqkFX2Km1a0?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText)

It’s a Saturday afternoon in early November, and instead of daydreaming about the holidays or planning what I’ll do during our annual office shutdown—a much-appreciated week off right before the end of the year—I find myself working. Babysitting, really. I’m watching over our build system for one of the projects we’re trying to wrap up in the next few days.

I’m sitting in front of my computer, monitoring a process that sometimes takes ages to compile. There’s not much to do except wait—or get up, walk around, and check back every so often to see how things are progressing. I’m lucky to have one of my teammates, who’s just as invested in the success of this task, online with me. But still, no one should be working on a Saturday. Especially not him—he’s in Europe, which means it’s already late evening there, and yet he’s still at it, helping steer this process to completion.

If you have no idea what I’m talking about, let me try to paint a picture. Imagine you have a bakery. (As a side note, it’s funny—every time I try to explain software engineering to someone, especially my wife, I end up using a bakery analogy. Maybe it’s because food analogies are so familiar; everyone gets them.)

So, in our bakery, we have several chefs. One handles the flour, another makes the butter, someone else prepares the chocolate, and another works on the fruit. Each of these chefs is responsible for perfecting their own ingredient. The flour maker might carefully select and grind the best grains; the butter maker might churn and chill it to just the right texture.

At some point, all these ingredients need to come together. That’s where the **build system** comes in—it’s the oven. The oven takes the ingredients and bakes the final product, whether that’s a cake or a loaf of bread. The goal of the build process is to combine everything correctly and produce a finished artifact—our beautifully baked, packaged product—ready for customers to enjoy.

Here’s the tricky part: in our case, we don’t control how the butter is made, how fine the flour is ground, or how the eggs are stored. Inside our private kitchen (our local laptops), we can make our cakes perfectly because we control all those details. But when we use a shared build system—managed by others—we lose that control.

So we provide our recipe, list the ingredients, and hope the external kitchen follows it to the letter. But sometimes, their flour isn’t quite like ours. Their butter may be softer, their eggs larger, their milk colder. Even if they follow the same recipe, the result might look—and taste—completely different.

That’s what we’ve been struggling with: figuring out how to tell this big, shared oven exactly which ingredients and settings to use so the result matches what we bake locally. In theory, we should be able to pass that information during the build process to ensure a consistent outcome.

If you’ve ever built software, none of this should be new. The complication for us is that we don’t actually control the oven. We don’t have full visibility into how it’s configured or how to give it such precise instructions. So our only option right now is **trial and error**.

And that wouldn’t be so bad—if each “trial” didn’t take hours. You tweak one variable—adjust the butter temperature, change the flour texture, switch the eggs—and then you wait. You don’t know whether you’ll get a cake or a disaster until the oven stops running: success or explosion.

So, that’s how my Saturday is going. We’re still not out of the woods yet; one more experiment is in progress. If there’s anything I’ve learned over the last four weeks of working with this system, it’s that I’ll probably be back here on Sunday—with my teammate in Europe—waiting to see what kind of cake we pull out of the oven this time.

Ah, the joys of software engineering: the moments when you’re locked out of the kitchen, hoping your cake still rises.
