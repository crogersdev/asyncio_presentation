# asyncio_presentation
for offsite lightning talk

## What?
I gave a 10 minute talk on python asyncio at OrbitalInsight's 2019 Developer offsite.

Slides here: 
https://docs.google.com/presentation/d/1HzI9zvITUlg-vwylrsmYiwQQgEvTpY6PwFnBCV9E-jg/edit?usp=sharing

I wanted to talk a teeny bit about what asyncio is and more importantly, when to use it.  I started out talking about how a lot of folks don't understand it either, so you shouldn't feel bad if you're still struggling with it.  If you were interested in trying to deep dive, and I certainly encourage it, then there are some valuable links in the slides that I'll also put in this README.  After an introduction to what it is and how cooperative multitasking works, I talk a little about how it's just another tool to put in the toolbag and it's up to us to recognize when we have a asyncio nail and we need an asycnio hammer or if we have a generator bolt and need a generator wrench or we have a synchronous dovetail joint and we have a synchronous dovetail jig, hammer, chisel, knife, hand plane, etc...

## Why?

It's good to know what the language represents and that concepts that are new to the developer are not panacea; but they can be useful.  It's our job as developers to know when to use this pattern or that library or this other framework because of how well we understand the problem and how the solution proposes to remedy the situation.

## How?

I recommend putting in a virtual environment or a conda environment and installing what you need.

The fib.py program will show you how running fibonacci sequences between sync, async, and generator based methods will showcase that asyncio doesn't help -- it in fact hurts you -- for CPU bound tasks.

You can run sync_server.py and/or async_server.py and then run the different clients against one (or both) of those servers to see how serving up the full text of The Count of Monte Cristo to a synchronous client or asynchronous client performs, especially if many requests are issued.  

## Examples
