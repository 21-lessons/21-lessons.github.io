---
layout: lesson
title: Down the Rabbit Hole
quote: "I almost wish I hadn't gone down that rabbit-hole, and yet, and yet - it's rather curious, you know, this sort of life."
permalink: rabbithole
order: ch4-05
toc: true
---

### Through the Looking Glass

After writing 21 Lessons, I wrote some articles and essays to explore a few of
Bitcoin's aspects further. These articles are marked by an 🔍.

I am currently working on my second book, [21 Ways](http://21waysbook.com/).

----

### Down the Rabbit Hole

Find all 'Down the Rabbit Hole' links for each lesson below. A curated list of Bitcoin resources is available at [bitcoin-resources.com][resources].

{% assign lessons_sorted = site.lessons | sort: 'order' %}
{% for lesson in lessons_sorted %}

---

#### [{{ lesson.title }}]({{ lesson.url }}): {{ lesson.subtitle }}

{% include rabbit-hole.html lesson=forloop.index hide_heading=true %}

{% endfor %}

----

<center>
<figure>
  <a href="https://bitcoin-resources.com"><img src="/assets/images/bitcoin-resources.png"/></a>
  <figcaption>Further resources: <a href="https://bitcoin-resources.com">bitcoin-resources.com</a></figcaption>
</figure>
</center>

<!-- Links -->
[resources]: https://bitcoin-resources.com
