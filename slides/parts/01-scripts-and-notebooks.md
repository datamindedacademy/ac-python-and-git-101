---
layout: section
---

# Scripts and <span class="dm-accent">notebooks</span>

<!--
Python now runs on your laptop. Next decision: what form does your code take? Two forms dominate engineering work, scripts and notebooks. We compare them honestly, then pick one for today. The first exercise comes at the end of this part.
-->

---
layout: default
label: 2 · Scripts and notebooks
---

# A script is a <span class="dm-accent">text file</span> that runs top to bottom

```python {all|1-2|4-5|7|all}
# bench_summary.py
pressure_bar = 7.5

power_kw = 37.5
print(f"Power: {power_kw} kW at {pressure_bar} bar")

print("Done")
```

<v-click>

```text
Power: 37.5 kW at 7.5 bar
Done
```

</v-click>

<style>
.slidev-code { font-size: 17px !important; line-height: 1.5 !important; }
</style>

<!--
A script is a plain text file with the extension .py. Python reads it from the first line to the last and executes each statement in order. That is the same idea as a MATLAB .m script. You can run it again tomorrow, on another machine, or from a scheduled task, and it does the same thing.
-->

---
layout: default
label: 2 · Scripts and notebooks
---

# Scripts repeat, <span class="dm-accent">notebooks</span> explore

<DmComparison
  class="mt-4"
  :rows="['Runs', 'Great for', 'Weak at', 'In Git']"
  :cols="['Script (.py)', 'Notebook (.ipynb)']"
>
  <template #r0c0>Start to finish, every time, on demand or scheduled</template>
  <template #r0c1>Cell by cell, in any order you click</template>

  <template #r1c0>Automation, reusable tools, anything others run</template>
  <template #r1c1>Exploring data, plotting, explaining results</template>

  <template #r2c0>Slow feedback when exploring</template>
  <template #r2c1>Repeatability and testing</template>

  <template #r3c0>Clean text, easy to compare versions</template>
  <template #r3c1>JSON with embedded output, noisy differences</template>
</DmComparison>

<!--
Neither is better in general, they serve different jobs. This is the first tradeoff of the day, and the pattern for all of them: Copilot will happily produce either form, so you have to know which one the job needs and say so. Scripts win when the result must be repeatable and shareable. Notebooks win when you are still figuring out what the data looks like. The last row matters for the Git block this afternoon: a script diff shows exactly the lines you changed, a notebook diff is full of output blobs.
-->

---
layout: default
label: 2 · Scripts and notebooks
---

# A notebook can run code <span class="dm-accent">you no longer see</span>

<div class="nb">
  <div class="cell"><span class="in">In [1]</span><code>limit_bar = 9.0</code></div>
  <div class="cell ghost"><span class="in">In [2]</span><code>limit_bar = 6.0</code><span class="tag">ran, then deleted</span></div>
  <div class="cell"><span class="in">In [3]</span><code>print(limit_bar)</code></div>
  <div class="out"><span class="in">Out</span><code>6.0</code><span class="tag warn">not 9.0</span></div>
</div>

<v-clicks>

- You ran cell 1, then cell 2, then edited cell 2 away and forgot about it
- Cell 3 prints a value that no longer appears anywhere in the visible code
- A colleague runs the notebook top to bottom and gets a different answer

</v-clicks>

<style>
.slidev-code { font-size: 17px !important; line-height: 1.5 !important; }
.nb { display: flex; flex-direction: column; gap: 6px; margin-bottom: 12px; }
.nb .cell, .nb .out { display: flex; align-items: center; gap: 14px; padding: 7px 14px; border-radius: 8px; }
.nb .cell { background: var(--dm-surface); border-left: 4px solid var(--dm-connecting); }
.nb .ghost { background: none; border: 2px dashed #b9b3e6; opacity: 0.6; }
.nb .ghost code { text-decoration: line-through; }
.nb .out { padding-left: 18px; }
.nb .in { width: 52px; font-size: 13px; color: var(--dm-connecting); font-family: monospace; }
.nb code { background: none !important; font-size: 16px; color: var(--dm-premium); }
.nb .tag { margin-left: auto; font-size: 12px; color: var(--dm-premium); }
.nb .warn { color: #fff; background: var(--dm-connecting); padding: 2px 10px; border-radius: 99px; }
</style>

<!--
The kernel remembers variables from every cell you ran, in the order you ran them, not the order on the page. After an hour of exploring, the notebook on screen and the memory in the kernel can disagree. A script cannot do this to you, because it always starts from a clean process, which is what makes its result reproducible. The habit that protects you in notebooks: restart the kernel and run all cells before you trust a result. Rule of thumb: explore in a notebook, and once you would run it twice, move it into a script. We work with scripts today and meet notebooks again on day 2.
-->

---
layout: statement
---

# Exercise 01: <span class="dm-accent">First script</span>

`exercises/python/01-first-script`

<p class="words"><b>Words you can now use</b> script · notebook · cell · kernel · hidden state · reproducible · interpreter · CPython · terminal · PATH · working folder · uv run</p>

<style>
.words { font-size: 15px; opacity: 0.9; margin-top: 14px; }
.words b { margin-right: 8px; }
</style>

<!--
Everyone creates a script, runs it from PowerShell and from VS Code, and changes it. About 15 minutes. I walk around, and any PATH or interpreter problem is exactly what we want to catch now.
-->


