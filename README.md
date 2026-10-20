# ឯកសារ Python ជាភាសាខ្មែរ · Python Documentation in Khmer

ឯកសារបង្រៀនភាសា **Python** ជាភាសាខ្មែរ ដែលសរសេរឡើងវិញដោយយោងតាម
ឯកសារផ្លូវការរបស់ CPython (ថត `Doc/`).

> **ស្ថានភាព៖ កំពុងអភិវឌ្ឍ។** បច្ចុប្បន្នមានតែ **៦ ជំពូកមូលដ្ឋានគ្រឹះ**
> ប៉ុណ្ណោះដែលបានបញ្ចប់។ ឯកសារ Python ទាំងមូល **មិនទាន់** ត្រូវបាន
> បកប្រែទេ។

- **កំណែ Python គោលដៅ៖** 3.15 (stable ចេញថ្ងៃ ៩ តុលា ២០២៦)
- **ឯកសារបានផ្ទៀងផ្ទាត់លើ៖** CPython 3.15.0
- **អាជ្ញាបណ្ណមាតិកា៖** PSF License Version 2 (derivative work)
- **អាជ្ញាបណ្ណកូដគេហទំព័រ៖** MIT (មើល `LICENSE-CODE`)

---

## មាតិកា

| # | ជំពូក | ឯកសារ | ស្ថានភាព |
|---|--------|--------|-----------|
| ១ | ចាប់ផ្ដើម និងការដំឡើង Python | `source/getting_started.rst` | ✅ |
| ២ | វាក្យសម្ពន្ធ អថេរ និងប្រភេទទិន្នន័យ | `source/syntax_variables_types.rst` | ✅ |
| ៣ | ខ្សែអក្សរ និងសំណុំទិន្នន័យ | `source/strings_collections.rst` | ✅ |
| ៤ | លក្ខខណ្ឌ និងរង្វិលជុំ | `source/control_flow.rst` | ✅ |
| ៥ | អនុគមន៍ និងវិសាលភាពអថេរ | `source/functions_scope.rst` | ✅ |
| ៦ | ការគ្រប់គ្រងឯកសារ | `source/file_handling.rst` | ✅ |
| ៧ | Modules និង Packages | — | ⬜ |
| ៨ | Exceptions | — | ⬜ |
| ៩ | Classes និង OOP | — | ⬜ |
| ១០ | Iterators និង Generators | — | ⬜ |
| ១១ | Decorators | — | ⬜ |
| ១២ | Type Hints | — | ⬜ |
| ១៣ | Standard Library | — | ⬜ |
| ១៤ | Virtual Environments និង Packages | — | ⬜ |
| ១៥ | Testing, Debugging និង Best Practices | — | ⬜ |

---

## រចនាសម្ព័ន្ធគម្រោង

```
Python-Documentation/
├── .readthedocs.yaml        # ការកំណត់ Read the Docs build
├── LICENSE                  # PSF License v2 + សង្ខេបការផ្លាស់ប្ដូរ
├── LICENSE-CODE             # MIT សម្រាប់កូដគេហទំព័រ
├── Makefile                 # make html / make linkcheck / make clean
├── README.md
├── requirements.txt         # dependency សម្រាប់ Sphinx
├── source/                  # ← ឯកសារប្រភព (កែប្រែនៅទីនេះ)
│   ├── conf.py
│   ├── index.rst
│   ├── getting_started.rst
│   ├── syntax_variables_types.rst
│   ├── strings_collections.rst
│   ├── control_flow.rst
│   ├── functions_scope.rst
│   ├── file_handling.rst
│   ├── license_attribution.rst
│   ├── _code/               # ឯកសារ .py ពិតដែល literalinclude យោងទៅ
│   ├── _static/khmer.css    # ពុម្ពអក្សរខ្មែរ + palette light/dark
│   ├── _templates/          # layout.html, breadcrumbs.html
│   └── _extra/robots.txt
├── tools/                   # script សាកល្បង (មិនមែនផ្នែកនៃ build)
└── docs/                    # ← HTML ដែលបានសាងសង់ (commit សម្រាប់ GitHub Pages)
```

**ហេតុអ្វីឈ្មោះឯកសារជាអង់គ្លេស?** ឈ្មោះឯកសារខ្មែរអាចបង្កបញ្ហាជាមួយ
URL encoding, ស្វែងរក និង cross-reference នៅលើ build system មួយចំនួន។
ដូច្នេះយើងប្រើ **ឈ្មោះឯកសារអង់គ្លេស + ចំណងជើងខ្មែរ** ដែលដំណើរការ
បានគ្រប់ទីកន្លែង។

---

## ការសាងសង់ក្នុងម៉ាស៊ីនរបស់អ្នក

### ១. ដំឡើង dependency

```bash
python3 -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

### ២. សាងសង់

```bash
make html
```

ឬដោយផ្ទាល់ (ដូចគ្នាទៅនឹង Makefile)៖

```bash
sphinx-build -b html source docs -q -W --keep-going
```

`-W` បំលែង warning ទាំងអស់ទៅជា error ដូច្នេះ build ត្រូវតែមាន
**zero warning**។

### ៣. មើលជាមុន

```bash
python3 -m http.server -d docs 8000
# បើក http://localhost:8000
```

### ៤. ពិនិត្យតំណខូច

```bash
make linkcheck
```

### ៥. សាកល្បងឧទាហរណ៍កូដ

```bash
python3 tools/run_examples.py       # ដំណើរការ code-block:: python ទាំងអស់
python3 tools/check_contrast.py     # ពិនិត្យ contrast ≥ 4.5:1
```

---

## លក្ខណៈពិសេសនៃគេហទំព័រ

- **Theme:** `sphinx_rtd_theme` (ដូច Read the Docs)
- **ពុម្ពអក្សរខ្មែរ:** Noto Sans Khmer + Noto Serif Khmer (SIL OFL 1.1)
  ផ្ទុកពី Google Fonts, `line-height: 1.85` ដើម្បីកុំឱ្យកាត់ជើងអក្សរ
- **Light/Dark mode:** dark ជាលំនាំដើម ប្ដូរបានដោយប៊ូតុងអត្ថបទធម្មតា
  នៅ breadcrumb bar ខាងស្ដាំ។ ជម្រើសត្រូវបានរក្សាទុកក្នុង `localStorage`
  ហើយត្រូវបានអនុវត្តមុនការ paint ដើម្បីកុំឱ្យមាន flash។
- **Contrast:** គ្រប់គូ ពណ៌អក្សរ/ផ្ទៃខាងក្រោយ ទាំងអស់យ៉ាងតិច **4.5:1**
  (ផ្ទៀងផ្ទាត់ដោយ `tools/check_contrast.py`)
- **Code copy button:** តាមរយៈ `sphinx-copybutton`
- **Search, sidebar, ToC, prev/next:** stock RTD
- **Responsive:** ដំណើរការលើ mobile និង desktop

---

## ការចូលរួម

1. Fork repository នេះ
2. សរសេរជំពូកថ្មីជា `.rst` ក្នុង `source/` ហើយបន្ថែមវាទៅ `toctree`
   ក្នុង `source/index.rst`
3. ដាក់ `.. container:: src-note` នៅផ្នែកខាងលើដើម្បីបញ្ជាក់ប្រភពដើម
   ក្នុង CPython `Doc/`
4. ដំណើរការឧទាហរណ៍កូដទាំងអស់ដើម្បីផ្ទៀងផ្ទាត់
5. សាងសង់ដោយ `make html` — ត្រូវតែមាន zero warning
6. បើក Pull Request

### ច្បាប់សម្រាប់មាតិកា

- ❌ កុំបកប្រែពាក្យគន្លឹះ Python (`if`, `for`, `def`, `class`, `return`,
  `True`, `False`, `None`, …)
- ❌ កុំបកប្រែឈ្មោះ function, class, module, parameter ឬ API
- ✅ ពន្យល់ពាក្យបច្ចេកទេសជាខ្មែរ ហើយដាក់ពាក្យអង់គ្លេសក្នុងវង់ក្រចក
  ពេលចាំបាច់
- ✅ បញ្ជាក់កំណែ Python បើលក្ខណៈពិសេសអាស្រ័យលើកំណែ
  (ប្រើ `.. versionadded::` / `.. versionchanged::`)
- ✅ ឧទាហរណ៍កូដត្រូវតែដំណើរការពិត — កុំបង្កើត API ដែលមិនមាន
- ❌ កុំកែឯកសារ Changelog / Release Notes

---

## ប្រភព និងអាជ្ញាបណ្ណ

មាតិកាដើម © **Python Software Foundation** — PSF License Version 2។
មើល [`LICENSE`](LICENSE) និង
[`source/license_attribution.rst`](source/license_attribution.rst)
សម្រាប់ព័ត៌មានលម្អិត រួមទាំងសង្ខេបអំពីការផ្លាស់ប្ដូរដែលបានធ្វើ។

"Python" និងរូបសញ្ញា Python គឺជា trademark របស់ PSF។ គម្រោងនេះមិន
ទទួលបានការអនុម័ត ឬឧបត្ថម្ភពី PSF ទេ។

**ប្រភពផ្លូវការ៖**

- ឯកសារ — https://docs.python.org/3/
- Source — https://github.com/python/cpython/tree/main/Doc
