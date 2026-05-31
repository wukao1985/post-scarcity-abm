# Prologue — The Wrong Question
## 序章 · 错误的问题

For about a decade now, a single question has organised almost everything written about
artificial intelligence and the future: *Will it take my job?*

It is a reasonable question. It is also, I think, the wrong one — or at least, the one that
keeps us from seeing the harder thing coming up behind it.

Let me start with a place where the future has, in a small way, already arrived.

Stack Overflow is the website where the world's programmers go to ask and answer technical
questions. For fifteen years it was one of the load-bearing pillars of how software actually
gets made: you hit a problem, you searched, and someone — often a stranger, for free, years
earlier — had written the answer. It ran on a strange and beautiful economy. Nobody was paid.
People answered questions for reputation, for the pleasure of solving a hard problem, for
membership in a community of people who cared about the same obscure things.

Then, at the end of November 2022, ChatGPT arrived, and within a year it could answer most of
those questions instantly, privately, without making you feel stupid for asking.

What happened next is not a forecast. It is a measurement. By my own pull of Stack Overflow's
public data, the number of questions and answers posted each month fell roughly 45% in the
first year — and by early 2026, around 95%. Not a decline. A collapse. An entire ecosystem of
voluntary human contribution, drained in three years.

I spent weeks studying that collapse in detail — who stopped, who stayed, and why. (That study,
and the ways it proved me wrong, is a thread that runs through this book; I'll come back to it.)
But the single most important thing I learned from it had nothing to do with programmers.

It was this. When the work went away, the *income* of those people was mostly fine — they were
never paid for it anyway. What vanished was something else. The reason to show up. The place
where a certain kind of person had been competent, recognised, needed, connected. The platform
didn't take their salaries. It took the thing the work had been *giving* them that they hadn't
known to name.

And that is the question this book is actually about. Not *will AI take your job* — but:

**When the work is gone, even if the money is somehow fine, what is left?**

---

### Two debates, and the one nobody is having

Strip away the noise and the public conversation about AI and work is really two debates.

The loud one is **economic**. Will there be enough jobs? Can we afford universal basic income,
or can we not afford to skip it? Whose wages rise, whose collapse? This debate has economists,
think tanks, central banks, and an ocean of data. It matters. It is also not my subject, and I
am not the person to add to it.

The quiet one — the one with almost no one in the room — is about **meaning**. Suppose the
economic debate resolves in the most optimistic way imaginable: new jobs appear, or a generous
basic income arrives, and nobody goes hungry. *Even then*, a question remains that money does
not touch. Work has never been only a paycheck. It has been, for most adults in the modern
world, the default supplier of structure, status, competence, belonging, and the sense of being
needed. If AI dissolves work as the place those things come from — even while keeping everyone
fed — does the society on the other side stay psychologically and socially whole?

This book lives entirely in that second, quieter debate. I am going to mostly *grant* the
optimists their economics, precisely so we can look clearly at the thing their optimism does
not cover.

### A promise about honesty

I want to make one promise up front, because it is the only thing that makes a book like this
worth your time in a genre this crowded with confident nonsense.

The honest truth is that no one knows how this goes. The future of AI is not knowable the way
next year's weather is roughly knowable. But "we can't predict it" is not the same as "anything
goes," and it is certainly not an excuse to either panic or pretend.

So throughout this book I will hold myself to a discipline of marking exactly what kind of claim
I am making, sentence by sentence:

- **What we actually know** — backed by real data, the kind a future study could prove wrong.
  (There is less of this than anyone would like, and I will not pad it.)
- **What we can reasonably infer** — by analogy and mechanism, always with the places the
  reasoning breaks named out loud.
- **What we have to choose** — the questions that are not predictions at all, but values and
  designs, where the honest standard is not "is it true" but "does it hold up across many
  possible futures."

When I show you data, I'll tell you precisely what it does and does not show. When I reason from
history, I'll point at where the analogy snaps. When I'm urging you toward something, I'll own it
as my judgement, not disguise it as a finding. And when the evidence has embarrassed me — as it
has, more than once — I'll tell you that too.

This is also a book with two readers in mind, who turn out to be the same reader.

The first is the professional watching it happen to their own craft right now — the programmer,
the translator, the illustrator, the copywriter, the analyst — the people standing closest to
the edge as AI moves into work they spent years learning to do well. If that's you, this book is
trying to give you something more useful than reassurance or alarm: a little help, honestly come
by, as you go about the work of finding your place again.

The second reader is everyone, eventually. Because the professionals are not a special case.
They are the *forerunners*. What is happening to them first is, I'll argue, a preview of a
question the rest of us will each have to answer in our own time: when what you produce no
longer defines you — because something else can produce it — who are you, and where does your
life get its meaning?

I can't answer that question for you; no honest book could. But I can walk a little of the way
with you — clear about what we know, what we're only guessing, and what each of us has to choose
for ourselves. That's the whole offer.

We'll start where the loss is easiest to underestimate: with what work was quietly doing for us
all along.

---

> 🔬 **研究事项 RT-00 (minor):** 序章引用的 SO −45%/−95% 数字来自我们自己的平台级 API 拉取
> （`so_sdt_study/platform_trend/`）。出版前需把拉取脚本补成可复现，并交叉核对一个独立来源
> （如 SEDE 年度计数）确认量级。
