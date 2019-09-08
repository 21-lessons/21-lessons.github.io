---
layout: lesson
title: Down the Rabbit Hole
quote: "I almost wish I hadn't gone down that rabbit-hole, and yet, and yet - it's rather curious, you know, this sort of life."
permalink: rabbithole
order: ch4-05
toc: true
---

{% for i in (1..21) %}

### Lesson {{ i }}

{% include rabbit-hole.html lesson=i %}

{% endfor %}
