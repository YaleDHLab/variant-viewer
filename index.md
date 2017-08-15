---
layout: default
---
{% include header.html %}
<div class='container'>
  <div class='hero'>
    <div class='hero-overlay'>
      <div class='tagline'>{{ site.tagline }}</div>
      {%- if site.data.authors.size == 1 -%}
        {%- for a in site.data.authors %}
            {%- assign author_id = a[1].id %}
          {%- endfor %}
        <a href='{{ site.baseurl }}/authors/{{ author_id }}'>
      {%- else -%}
        <a href='{{ site.baseurl }}/authors'>
      {%- endif -%}
          <div class='button'>Enter</div>
        </a>
    </div>
  </div>
  <div class='push'></div>
</div>