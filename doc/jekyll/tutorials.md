---
layout: page
title: Tutorials
permalink: /tut/ 
---

<ul>
  {% for tut in site.tutorials %}
    <li><a href="{{site.baseurl}}/{{ tut.url }}">{{ tut.title }}</a></li>

  {% endfor %}
</ul>






