---
date:
  created: 2025-03-22
authors:
  - Burhan-Q
tags: 
    - vibe-coding
    - trends
    - rant
    - llm
    - code
    - opinion
---

# You Probably Won't Benefit from Vibe Coding

Recently, the term "vibe coding" has come into fashion. I have thoughts and want to put them out in the world (among the many others doing the same).

<!-- more -->

## What's Vibe Coding?

Likely made popular by a post from Andrej Karpathy on 2025-02-02.

![Post by Andrej Karpathy](https://github.com/user-attachments/assets/20ee3172-d742-4820-8a78-271fa1af9da4)

??? note "Full text of Andrej Karpathy's post"

    > There's a new kind of coding I call "vibe coding", where you fully give in to
    > the vibes, embrace exponentials, and forget that the code even exists. It's
    > possible because the LLMs (e.g. Cursor Composer w Sonnet) are getting
    > too good. Also I just talk to Composer with SuperWhisper so I barely even
    > touch the keyboard. I ask for the dumbest things like "decrease the
    > padding on the sidebar by half" because 11m too lazy to find it. I "Accept
    > All" always, I don't read the diffs anymore. When I get error messages I just
    > copy paste them in with no comment, usually that fixes it. The code grows
    > beyond my usual comprehension, I'd have to really read through it for a
    > while. Sometimes the LLMs can't fix a bug so I just work around it or ask for
    > random changes until it goes away. It's not too bad for throwaway
    > weekend projects, but still quite amusing. I'm building a project or webapp,
    > but it's not really coding - I just see stuff, say stuff, run stuff, and copy paste
    > stuff, and it mostly works.

---

I'm not going to dig into the post, but just pointing out that this is what kicked off the recent trend. It's not _really_ a new idea, as pointed out by others, 
[theprimeagen](https://www.twitch.tv/theprimeagen) mentioned, it's just a rebrand of "no-code" solutions. That said, I think the reason that vibe coding has
more appeal than when building no-code solutions were such a big deal, is multifaceted.

## Why (probably) it's Popular

Like with anything that gains popularity or notoriety, there's likely multiple reasons. I don't have any hard evidence, just throwing my deductions out to the world. 
In no particular order:

1. The promise of creativity.
2. Popularity of LLM use and general availability.
3. Easy for anyone to build a product/service.
4. The dream of self-employment.
5. Left-shift thinking and attitudes.

First, there's probably a greater appeal since the term "vibe" insinuates a more artistic, intuitive, or chill approach when it comes to coding. It would be unsurprising 
if people thought they should be able to more easily express unique visions, especially compared to "no-code" solutions, which often felt more like working "on rails" or 
forced to use "cookie cutter" assets. It makes coding more about the 'feeling' or 'vibe' over rigid technical constraints, and maybe appear less stressful.

The rise of large language models (LLMs) makes vibe coding accessible and feasible via prompting for code, significantly lowering the barrier for entry compared to 
traditional "no-code" products. It's not really a surprise, as it's almost like the Star Trek computer, which could be directed using voice commands to accomplish 
any task. There's something else here too, but I'll speak more to that later.

Vibe coding likely also develops the belief that anyone can actualize their ideas into tangible digital products or services quickly. An almost "effortless" path to product 
creation, and money generation. The idea of min-maxing is nothing new, but vibe coding takes it to another level.

Would it be any surprise that someone might believe they can finally build and launch their own businesses with minimal technical investment? Having a tough time finding a 
new job? Sick of dealing with return to office, office politics, or a terrible manager? Given how rough the professional market has been (for a while now), I wouldn't be 
surprised if anyone thought of vibe coding as a way to support themselves.

I haven't written about "left-shift" thinking and attitudes yet, but it's on my mind and there will be something eventually. What I mean here by "left-shift" is an overall 
degradation of quality in work/effort, primarily driven by the "move fast and deliver" mentality. It's my opinion, that there's been a tremendous shift away from quality 
work, understanding around how something is built/made, and considerate decision making. Vibe coding is a product of that shift, as it encourages production over 
methodology and sacrifices quality for minimal effort.

---

![I built my SaaS with Cursor, now I'm getting hacked.](https://github.com/user-attachments/assets/0f927a6b-43f7-4a1d-bcc1-63aeb91f58c4)

---

## Who is it for?

You may be wondering who I think vibe coding is for if not the users? I suspect it's for the providers of the vibe coding solutions, since as the saying goes, 

> When everyone digs for gold, sell shovels.

The ones who are likely _most_ to benefit are those who charge by the token. The frontier LLM providers, with the biggest, fastest, and most expensive models, they're the 
benefactors more than anyone else. Let's take a quick look at the OpenAI API pricing (as of 2025-03-22, all in USD):

| Model       | $/1M tokens (input) | $/1M tokens (output) |
| :---------: | :-----------------: | :------------------: |
| GPT4.5      |       $ 75.00       |       $150.00        |
| o1          |       $ 15.00       |       $ 60.00        |
| GPT-4o      |       $  2.50       |       $ 10.00        |
| o3-mini     |       $  1.10       |       $  4.40        |
| GPT-4o mini |       $  0.15       |        $ 0.60        |

You might be thinking, what about the ChatGPT Plus plan? Sure, someone vibe coding could copy-paste code, but I suspect that most are going to be using something much more 
integrated, like Cursor, Windsurf, or others. It gives the LLM much more agency to build and more context regarding inputs/outputs. Although services like Cursor and 
Windsurf don't have such a hefty looking price tag, they come with limitations. 

The constraints are where the money is to be made on providers of vibe coding solutions or tools. If you cross a limit, you get slowed down or might get stuck until you 
pay extra. Someone who isn't technically savvy might think they'd never hit those limits, or if using the OpenAI API directly, never run up a large bill, but those who 
know can guess as to why that's incorrect.

## A Runaway Money Sink

Starting out, I suspect many vibe coders will feel great. A short time, a few prompts, and their ideas spring to life. From there they deploy and start working on the 
marketing push to drive some business. After things start picking up, it's time to relax and watch the numbers go up!

Except that's not how it works. Software always breaks, always. Someone has to fix it, otherwise the money will stop coming in. That means more vibe coding and that means 
more token usage. Especially since it's now a matter of fixing a problem without creating more and without breaking anything that was working. The amount of information 
the model needs gets larger, and there's a lot more back and forth to resolve the problem. Suddenly and seemingly out of nowhere, the limit is hit and there's either no 
response or slow responses. Need to keep things going, so throw some money at the problem and keep vibe'n.

Sooner or later the problems may get resolved and things calm down again. That's when the feature requests start coming in, or perhaps even a competitor pops up. Adding 
new features is much like fixing bugs, can't break what's already working to add something new. Larger and larger portions of the code have to be sent to ensure that 
the changes for the new features don't break anything existing, and once again the limit is exceeded, but this time much quicker than before.

Eventually this will likely end in one of a few ways. I suspect that the most likely possibility is that they just keep paying for higher and higher limits to keep things 
going. Assuming there was still a profit to be made, or they believed there was, I'd guess many would take this route. Of course that's why the frontier model providers
are the most likely to benefit from vibe coding.

What group of people are more likely to throw money at a problem than someone who is looking to try to take a shortcut to make money? Who is more likely to double down 
on fixing a problem the one way they 'know' how? Would anyone choosing the "easy" path to profitability be likely to recognize an intractable technical problem? Who better 
to make money from, than those who are most likely to _need_ your service, don't have the know how to work around it, and are likely to see your service as the best (or 
only solution)?

## The Cost of Vibe Coding

According to [OpenAI](https://platform.openai.com/docs/concepts/tokens#tokens), as a rough approximation $1$ token is ~$4$ characters and for anyone curious you can try their 
[online tokenizer](https://platform.openai.com/tokenizer). As a point of reference, the previous sentence (including all the markdown formatting) was only $55$ tokens using 
the `GPT-4o` and `GPT-4o mini` tokenizers. Not that much considering that costs are `$/1M tokens`, however this entire article is $3,313$ tokens and while still small, is
nowhere near the length of what a live website, SaaS service, or fully developed code project would require. So what's the point about the pricing then?

Without LLMs, vibe coding wouldn't exist. Since the release of ChatGPT, lots of people and businesses have been looking for ways to extract value from them. Anyone who's 
been paying attention to the LLM space knows that they're not perfect, and anyone who writes code for a living knows that they can actually be problematic. The LLM that 
creates "perfect" code doesn't exist, and any organization that could build one probably wouldn't sell it, since they could use it to make money directly. One might infer 
that would mean the products currently being sold are not good enough to lock away. In turn that means that the product being sold has no assurance to work reliably or to
produce working code. That would mean that a service built around the use of that product can be sold that perpetuates more use of the service, who wouldn't want that!?

The cost isn't just monetary either. As an individual who might be turning to vibe coding with the idea to build something, start a business, or make some money, there are 
related costs that might come due.

---

![Reddit post: My project became so big that claude can't properly understand it](https://github.com/user-attachments/assets/57160a21-aa6d-4904-9f84-e3573ac29a04)

> I have 0 knowledge about python, it's actually a miracle i got this far with the project, but now it's almost impossible to keep track of things, what do i do? already 
> tried using cursor rules but doesn't seem to work.

??? note "Full text: My Project became so big that claude can't properly understand it"

    > So, I made a project in python entirely using Cursor (composer) and Claude, but it has gotten to a point that the whole codebase is over 30 Python files, code is super 
    > disorganized, might even have duplicate loops, and Claude keeps forgetting basic stuff like imports at this point. When I ask it to optimize the code or to fix a bug, it 
    > doesn’t even recognize the main issue and just ends up deleting random lines or breaking everything completely.
    > 
    > I have 0 knowledge about python, it's actually a miracle i got this far with the project, but now it's almost impossible to keep track of things, what do i do? already 
    > tried using cursor rules but doesn't seem to work.
    > 
    > Edit: My post made it to YouTube! I hope this serves as a historical reminder that having at least some knowledge is still totally necessary, go study, AI is supposed to 
    > assist you, don’t let your projects end up like this.
    > 
    > As for the project, it was just a hobby project, I managed to make it work perfectly and fix some issues by simply improving the context, like providing the files to edit 
    > directly and some source code, etc. but i couldn't get rid of the duplicated stuff. Anyway, don't do this for serious projects please (not knowing what it does), if it's 
    > an actual job don't be lazy, just check everything and be careful :)
    > 
    > If you wanna learn just ask AI to explain what it's changing, how the code works and stuff like that.

---

I don't know the user, but this made the rounds online in developer communities. The top comment on the post sums things up spectacularly.

> I got stressed reading this.

The most stressful times in my life, personally or professionally, are from times when I was completely out of my depth and had no understanding of what was going on. I have no 
doubt that vibe coding can feel great at the start, but there will nearly always be a reckoning and it's not going to be pleasant. Not everyone choosing this path will post 
about it, and not many who do will have their post/story go viral, but my hope is that for anyone attempting to go the route of vibe coding will heed the words of this Reddit 
user:

> I hope this serves as a historical reminder that having at least some knowledge is still totally necessary, go study, AI is supposed to assist you, don’t let your projects 
> end up like this.

## Do by Learning

The big takeaway here is that vibe coding isn't for the benefit of the individual, it's for the people selling the products that drive it. That's not to say don't use an LLM, 
you should, but you should do so with skepticism and caution. You should also learn whatever it is you were planning to skip to build your idea. Yes, it will take time. Yes, 
it might be difficult. It will provide immense value, but you have to put in the effort to tackle the challenge in the first place. If you feel ambitious, you can start with 
trying to build your idea as part of your learning, but it won't be easy and that should be okay. If you're curious, you can check out a little about 
[my journey](../../about/profile/journey.md) and read about how I had to deliver a project while learning something completely new while on the job, maybe it could serve as a 
bit of inspiration to dive into learning something new.
