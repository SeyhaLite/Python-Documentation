# Khmer technical glossary — human review notes

**Status:** REVIEW AID ONLY — no term in `translation-glossary.csv` has been approved by a human reviewer.  
**Source:** the 21 draft terms currently marked `ai_reviewed_pending_human`.

This file records issues worth discussing. It must not be treated as approval, and it does not change the status column in the CSV.

## Terms that deserve a decision

| Source term | Current draft | Review finding | Suggested wording to consider |
|---|---|---|---|
| `iterator` | `iterator (ឧបករណ៍ទៅមើលធាតុម្តងមួយៗ)` | The literal wording sounds like a viewing device, not a programming object. | Keep `iterator` and explain as «វត្ថុដែលផ្តល់ធាតុបន្ទាប់ម្តងមួយៗ»។ |
| `generator` | `generator (function ដែលបង្កើតតម្លៃម្តងមួយៗ)` | This can blur the distinction between a *generator function* and the *generator iterator* object it returns. | Keep `generator`; explain it as an iterator that yields values one by one, and separately define `generator function` as the function that creates it. |
| `bytecode` | `កូដបៃ (bytecode)` | «កូដបៃ» may be read as merely a sequence of bytes; it does not communicate that these are interpreter instructions. | Consider keeping `bytecode` with «កូដកម្រិតមធ្យមដែល Python interpreter ដំណើរការ»។ |
| `statement` | `បញ្ជា (statement)` | «បញ្ជា» may be confused with a command-line command. The glossary should distinguish a Python statement from an operating-system command. | Consider «សេចក្ដីបញ្ជា (statement)» or retain `statement` with a short explanation. |
| `argument` | `តម្លៃដែលបញ្ជូនទៅ function (argument)` | The distinction from `parameter` is important. An argument is supplied in a call and may be positional or keyword-based; avoid defining it only as a bare value. | Consider «តម្លៃ ឬការកំណត់ដែលផ្ដល់នៅពេលហៅ function (argument)»; validate against actual examples. |
| `virtual environment` | `បរិស្ថានដាច់ដោយឡែក (virtual environment)` | Clear enough in context, but without “Python” it may be too broad for beginners. | Consider «បរិស្ថាន Python ដាច់ដោយឡែក (virtual environment)»। |

## Other draft terms

The remaining 15 terms also remain **PENDING HUMAN REVIEW**; this automated pass does not approve them:

- `interpreter`, `expression`, `object`, `class`, `module`, `package`, `function`, `parameter`, `exception`, `decorator`, `type hint`, `standard library`, `source code`, `reference count`, `global interpreter lock (GIL)`.

## Reviewer decision procedure

For each term, a Khmer-language reviewer should:

1. Read the source definition and the chapter where the term is first introduced.
2. Check that the Khmer wording is natural for a beginner and does not change the technical meaning.
3. Confirm that related terms remain distinct (especially statement/command, argument/parameter, generator/generator function, and package/distribution).
4. Approve, revise, or reject the proposal with a short reason.
5. Only then change the CSV status to a human-review state and record the reviewer.

Until that work is done, all 21 CSV entries must remain `ai_reviewed_pending_human`.
