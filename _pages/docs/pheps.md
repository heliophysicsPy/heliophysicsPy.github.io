---
layout: page
title: PHEPs
permalink: /docs/pheps/
exclude: true
---
<!-- Temp hack to add "No data available in table" to empty tables with JavaScript (can remove once both tables have entries) -->
<script type="text/javascript" src="../../js/projects.js" class="init"></script> 

{% assign sorted_pheps = site.data.pheps | sort:'PHEP' %}
<p>
PyHC Enhancement Proposals are developed via the <a href="https://github.com/heliophysicsPy/standards/">PyHC standards repository</a>. PHEPs which have gone through the acceptance process, whether finally accepted or rejected, are linked here.
</p>

<br>

<h3>Final</h3>
<p>
  These PHEPs have been accepted and are currently in force.
</p>
{% assign id = 1 %}
{% include phep_table.html sorted_pheps=sorted_pheps table_id=id %}

<br>

<h3>Other</h3>
<p>
  These PHEPs have been rejected, withdrawn, or replaced, and thus are not currently in force.
</p>
{% assign id = 2 %}
{% include phep_table.html sorted_pheps=sorted_pheps table_id=id %}
