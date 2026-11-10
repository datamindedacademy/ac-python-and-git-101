---
layout: section
---

# Scripts and <span class="dm-accent">notebooks</span>

<!--
First decision: what form does your Python code take? Two forms dominate engineering work, scripts and notebooks. We compare them honestly, then pick one for today.
-->

---
layout: default
label: 1 · Scripts and notebooks
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
label: 1 · Scripts and notebooks
---

# Scripts versus <span class="dm-accent">notebooks</span>

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
Neither is better in general, they serve different jobs. Scripts win when the result must be repeatable and shareable. Notebooks win when you are still figuring out what the data looks like. The last row matters for the Git block this afternoon: a script diff shows exactly the lines you changed, a notebook diff is full of output blobs.
-->

---
layout: default
label: 1 · Scripts and notebooks
---

# The notebook trap: <span class="dm-accent">hidden state</span>

```python
# Cell 1                  # Cell 2                  # Cell 3
limit_bar = 9.0           limit_bar = 6.0           print(limit_bar)
```

<v-clicks>

- You ran cell 1, then cell 2, then edited cell 2 away and forgot about it
- Cell 3 prints a value that no longer appears anywhere in the visible code
- A colleague runs the notebook top to bottom and gets a different answer

</v-clicks>

<style>
.slidev-code { font-size: 17px !important; line-height: 1.5 !important; }
</style>

<!--
The kernel remembers variables from every cell you ran, in the order you ran them, not the order on the page. After an hour of exploring, the notebook on screen and the memory in the kernel can disagree. A script cannot do this to you, because it always starts from a clean process. The habit that protects you in notebooks: restart the kernel and run all cells before you trust a result. Rule of thumb: explore in a notebook, and once you would run it twice, move it into a script. We work with scripts today and meet notebooks again on day 2.
-->

