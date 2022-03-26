---
layout: lesson
title: Hlouběji králičí norou
quote: "Skoro bych si přála, abych do té králičí nory nespadla, a přece, a přece - je to docela zvláštní, víte, tenhle život."
permalink: rabbithole
order: ch4-05
toc: true
---

### Za zrcadlem

Po napsání 21 lekcí jsem napsal další články a eseje, ve kterých jsem se 
věnoval některým aspektům bitcoinu podrobněji. Tyto články jsou označeny 🔍.

V současné době pracuji na své druhé knize [21 Ways](http://21waysbook.com/) ("21 možností").

----

### Hlouběji králičí norou

Níže naleznete všechny odkazy "Hlouběji králičí norou" z jednotlivých lekcí. Kurátorovaný 
seznam zdrojů o Bitcoinu je k dispozici na adrese [bitcoin-resources.com][resources].

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
