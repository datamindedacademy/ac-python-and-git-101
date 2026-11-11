---
layout: section
---

# <span class="dm-accent">Exceptions</span>

<!--
Things will go wrong in scripts that automate work, for example one bad row in a long log. This block shows how to handle an error you expect. You read your first tracebacks this morning.
-->

---
layout: default
label: 5 · Exceptions
---

# <span class="dm-accent">try / except</span> handles an error you expect

<div class="split">
<div>

```python {all|2-3|4-6|all}
text = "seven"
try:
    pressure_bar = float(text)
except ValueError:
    pressure_bar = None
    print(f"Skipping bad value: {text!r}")
print(pressure_bar)
```

<v-click>

```text
Skipping bad value: 'seven'
None
```

</v-click>
</div>

<div v-click>

```mermaid {scale: 0.85}
flowchart TD
    T["try: float(text)"] -- works --> C["carry on"]
    T -- ValueError --> E["except: set None, print"]
    E --> C
    style E fill:#543edc,color:#fff,stroke:#543edc
```

</div>

</div>

<p class="note"><code>float("seven")</code> <b>raises</b> a <code>ValueError</code>. <code>except</code> <b>catches</b> it.</p>

<p class="ask" v-click><b>Question</b>What changes if you write <code>except:</code> without <code>ValueError</code>?</p>

<style>
.slidev-code { font-size: 17px !important; line-height: 1.5 !important; }
</style>

<!--
This morning you read a traceback for the ValueError from float("seven"). Sometimes an error is expected, for example one bad row in a long log. try runs the risky code, and if the named exception occurs, the except block runs instead of crashing the script. The script then carries on. The vocabulary: the code raises an exception, and you catch it. Your own code can raise one too, with the raise keyword, when it receives something it cannot handle. Execution continues after the whole block either way. Question on the slide: it then catches every error, also a typo in your own code and Ctrl+C. The script keeps running and hides the real problem. Name the error you expect.
-->

---
layout: statement
---

# Exercise 07: <span class="dm-accent">Files and exceptions</span>

`exercises/python/07-files-and-exceptions`

<p class="words"><b>Words you can now use</b> exception · raise · catch</p>

<style>
.words { font-size: 15px; opacity: 0.9; margin-top: 14px; }
.words b { margin-right: 8px; }
</style>

<!--
Read and write files, handle a bad row, and then fix one broken script by reading its traceback. Start at the bottom line. The other two broken scripts are optional. About 20 minutes.
-->
