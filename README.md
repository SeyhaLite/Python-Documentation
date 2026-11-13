# ឯកសារ Python ជាភាសាខ្មែរ

គម្រោងឯកសារបង្រៀន **Python ជាភាសាខ្មែរ** សម្រាប់អ្នកដែលចង់រៀនពីមូលដ្ឋាន រហូតដល់ប្រធានបទសំខាន់ៗនៃការសរសេរកម្មវិធី។ មាតិកាត្រូវបានសរសេរឡើងវិញដោយយោងតាមឯកសារផ្លូវការរបស់ CPython ក្នុងថត `Doc/` ដោយរក្សាពាក្យគន្លឹះ កូដ និងឈ្មោះ API ដើមជាភាសាអង់គ្លេស។

**គោលដៅរបស់គម្រោង** គឺធ្វើឱ្យការរៀន Python ងាយយល់សម្រាប់អ្នកសិក្សាខ្មែរ ដោយពន្យល់ជាភាសាខ្មែរច្បាស់ៗ និងប្រើឧទាហរណ៍កូដដែលអាចសាកល្បងបាន។

## តំណសំខាន់ៗ

- **[អានឯកសារតាមគេហទំព័រ](https://seyhalite.github.io/Python-Documentation/)**
- [មើលមេរៀនទាំងអស់](#មាតិកាមេរៀន)
- [របៀបដំឡើង និងសាកល្បង](#ដំឡើងនិងសាកល្បងក្នុងម៉ាស៊ីនរបស់អ្នក)
- [របៀបចូលរួមកែលម្អ](#ការចូលរួម)
- [អាជ្ញាបណ្ណ និងប្រភព](#អាជ្ញាបណ្ណនិងប្រភព)

## ស្ថានភាព និងកំណែ Python

| ព័ត៌មាន | ស្ថានភាព |
|---|---|
| វិសាលភាពមាតិកា | មេរៀនស្នូល ១៥ ជំពូក |
| កំណែ Python គោលដៅ | Python 3.15 |
| កំណែដែលបានប្រើសាកល្បងឧទាហរណ៍កូដដោយ CI | CPython 3.15.2 (`tools/run_examples.py`) |
| កំណែថែទាំចុងក្រោយរបស់ Python 3.15 | 3.15.2 (គិតត្រឹម ១៣ វិច្ឆិកា ២០២៦) |
| ប្រព័ន្ធបង្កើតឯកសារ | Sphinx + sphinx_rtd_theme |
| គេហទំព័រឯកសារ | GitHub Pages |

> **សូមចំណាំអំពីវិសាលភាព៖** មេរៀន ១៥ ជំពូកខាងក្រោមបានបញ្ចប់តាមផែនការមាតិកាស្នូលរបស់គម្រោង។ នេះមិនមែនមានន័យថាឯកសារ Python ផ្លូវការទាំងមូលត្រូវបានបកប្រែរួចហើយទេ។ ផ្នែកធំៗដូចជា Library Reference ពេញលេញ, Language Reference, C API និង What's New នៅមិនទាន់មានក្នុងគម្រោងនេះទេ។
>
> កំណែ 3.15.2 ចេញផ្សាយនៅថ្ងៃទី ២៥ តុលា ២០២៦។ ក្នុង CI របស់គម្រោង `tools/run_examples.py` ត្រូវបានដំណើរការលើ CPython 3.15.2។ វាសាកល្បង `python` និង `pycon` code blocks ក្នុង `source/*.rst` ព្រមទាំង scripts ដែលបានកំណត់ក្នុង test harness។ ការធ្វើតេស្តនេះមិនផ្ទៀងផ្ទាត់អត្ថបទពន្យល់, output គំរូក្នុង `console` blocks ឬការណែនាំដំឡើងដែលអាស្រ័យលើប្រព័ន្ធប្រតិបត្តិការទាំងអស់ទេ។ ផ្នែកទាំងនេះត្រូវបន្តពិនិត្យក្នុង Phase 1។
>
> ប្រភពកំណែ៖ [Python Documentation by Version](https://www.python.org/doc/versions/) · [Python 3.15.2 Release](https://www.python.org/downloads/release/python-3152/)

## មាតិកាមេរៀន

មេរៀនទាំងនេះត្រូវបានរៀបចំតាមលំដាប់ពីមូលដ្ឋានទៅប្រធានបទដែលស្មុគស្មាញជាងមុន។ ចុចលើឈ្មោះមេរៀនដើម្បីអាន។

| ល.រ. | មេរៀន | អ្វីដែលនឹងរៀន |
|---:|---|---|
| ១ | [ចាប់ផ្ដើម និងការដំឡើង Python](https://seyhalite.github.io/Python-Documentation/getting_started.html) | ដំឡើង Python និងចាប់ផ្ដើមដំណើរការកម្មវិធី |
| ២ | [វាក្យសម្ពន្ធ អថេរ និងប្រភេទទិន្នន័យ](https://seyhalite.github.io/Python-Documentation/syntax_variables_types.html) | Syntax, variables និង data types |
| ៣ | [ខ្សែអក្សរ និងសំណុំទិន្នន័យ](https://seyhalite.github.io/Python-Documentation/strings_collections.html) | Strings, lists, tuples, sets និង dictionaries |
| ៤ | [លក្ខខណ្ឌ និងរង្វិលជុំ](https://seyhalite.github.io/Python-Documentation/control_flow.html) | if, for, while និងការគ្រប់គ្រងលំហូរកម្មវិធី |
| ៥ | [អនុគមន៍ និងវិសាលភាពអថេរ](https://seyhalite.github.io/Python-Documentation/functions_scope.html) | Functions, parameters, return និង scope |
| ៦ | [ការគ្រប់គ្រងឯកសារ](https://seyhalite.github.io/Python-Documentation/file_handling.html) | អាន សរសេរ និងគ្រប់គ្រង files |
| ៧ | [Modules និង Packages](https://seyhalite.github.io/Python-Documentation/modules_packages.html) | បំបែកកូដ និងប្រើ modules/packages |
| ៨ | [Exceptions និងការគ្រប់គ្រងកំហុស](https://seyhalite.github.io/Python-Documentation/exceptions.html) | ចាប់ និងដោះស្រាយ exceptions |
| ៩ | [Classes និង Object-Oriented Programming](https://seyhalite.github.io/Python-Documentation/classes_oop.html) | Classes, objects, inheritance និង OOP |
| ១០ | [Iterators និង Generators](https://seyhalite.github.io/Python-Documentation/iterators_generators.html) | Iteration, iterators និង generators |
| ១១ | [Decorators](https://seyhalite.github.io/Python-Documentation/decorators.html) | របៀបប្រើ និងបង្កើត decorators |
| ១២ | [Type Hints](https://seyhalite.github.io/Python-Documentation/type_hints.html) | សរសេរ type annotations ឱ្យកូដងាយយល់ |
| ១៣ | [Standard Library](https://seyhalite.github.io/Python-Documentation/standard_library.html) | ប្រើបណ្ណាល័យដែលភ្ជាប់មកជាមួយ Python |
| ១៤ | [Virtual Environments និង Packages](https://seyhalite.github.io/Python-Documentation/virtual_environments.html) | បង្កើតបរិស្ថានដាច់ដោយឡែក និងដំឡើង packages |
| ១៥ | [Testing, Debugging និង Best Practices](https://seyhalite.github.io/Python-Documentation/testing_debugging.html) | សាកល្បងកូដ ស្វែងរកកំហុស និងសរសេរកូដឱ្យមានគុណភាព |

## លក្ខណៈពិសេស

- **ពន្យល់ជាភាសាខ្មែរ៖** ផ្ដោតលើការពន្យល់ងាយយល់ ខណៈពាក្យគន្លឹះ និង API របស់ Python នៅដដែល។
- **ឧទាហរណ៍កូដ៖** ប្រើ code blocks និងឯកសារ `.py` ពិតក្នុង `source/_code/` សម្រាប់ឧទាហរណ៍ដែលត្រូវយកទៅប្រើឡើងវិញ។
- **ពុម្ពអក្សរខ្មែរ៖** Noto Sans Khmer និង Noto Serif Khmer ពី Google Fonts ជាមួយ CSS កែសម្រួលកម្ពស់បន្ទាត់។
- **Light/Dark mode៖** មានជម្រើសប្ដូររបៀបបង្ហាញ និងរក្សាទុកជម្រើសរបស់អ្នកក្នុង browser។
- **អានកូដងាយស្រួល៖** Python syntax highlighting, line numbers និងប៊ូតុងចម្លងកូដ។
- **ងាយស្វែងរក៖** មាន Search, Sidebar, Table of Contents និងតំណទៅមេរៀនមុន/បន្ទាប់។
- **Responsive layout៖** រៀបចំឱ្យអាចប្រើបានលើទូរស័ព្ទ និងកុំព្យូទ័រ។
- **ការពិនិត្យគុណភាព៖** មាន script សម្រាប់ដំណើរការឧទាហរណ៍កូដ និងពិនិត្យ contrast ពណ៌។

## រចនាសម្ព័ន្ធគម្រោង

```text
Python-Documentation/
├── .readthedocs.yaml       # ការកំណត់ Read the Docs
├── LICENSE                 # PSF License Version 2 សម្រាប់មាតិកាដើម
├── LICENSE-CODE            # MIT License សម្រាប់កូដគេហទំព័រ
├── Makefile                # ពាក្យបញ្ជា build និង linkcheck
├── README.md
├── requirements.txt        # Sphinx និង extensions
├── source/                 # ឯកសារប្រភពដែលត្រូវកែ
│   ├── conf.py
│   ├── index.rst
│   ├── *.rst               # មេរៀន និង license attribution
│   ├── _code/              # ឧទាហរណ៍កូដ Python
│   ├── _static/            # CSS, logo និង favicon
│   ├── _templates/         # HTML templates
│   └── _extra/             # ឯកសារបន្ថែមដូចជា robots.txt
├── tools/
│   ├── run_examples.py     # ដំណើរការឧទាហរណ៍កូដ
│   ├── check_contrast.py   # ពិនិត្យ contrast ពណ៌
│   └── fix_rst.py          # ជំនួយកែទម្រង់ reStructuredText
└── docs/                   # HTML ដែលបាន build សម្រាប់ GitHub Pages
```

**ចំណុចសំខាន់៖** កែឯកសារនៅក្នុង `source/` ជាចម្បង។ ថត `docs/` ជាលទ្ធផលពីការសាងសង់ HTML ដូច្នេះកុំកែ HTML ដោយដៃ ប្រសិនបើអាចកែពីឯកសារប្រភពបាន។

## ដំឡើងនិងសាកល្បងក្នុងម៉ាស៊ីនរបស់អ្នក

ត្រូវមាន Python 3.15 និង pip។ បើប្រើកំណែផ្សេង សូមពិនិត្យភាពឆបគ្នាជាមួយមេរៀន និងឧទាហរណ៍កូដជាមុន។

### ១. ទាញយកគម្រោង

```bash
git clone https://github.com/SeyhaLite/Python-Documentation.git
cd Python-Documentation
```

### ២. បង្កើត virtual environment

**Linux / macOS**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

**Windows PowerShell**

```powershell
py -3.15 -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### ៣. ដំឡើង dependency

```bash
python -m pip install -r requirements.txt
```

### ៤. សាងសង់ឯកសារ HTML

**Linux / macOS (ប្រើ Make)**

```bash
make html
```

**Windows ឬម៉ាស៊ីនដែលមិនមាន Make**

```bash
python -m sphinx -b html source docs -q -W --keep-going
```

ជម្រើស `-W` ធ្វើឱ្យ Sphinx ចាត់ទុក warning ជា error។ ប្រសិនបើមាន warning ការសាងសង់នឹងបរាជ័យ ដើម្បីឱ្យអាចរកឃើញបញ្ហាមុនពេលបញ្ចូលការផ្លាស់ប្ដូរ។

### ៥. បើកមើលលទ្ធផល

```bash
python -m http.server -d docs 8000
```

បន្ទាប់មកបើក [http://localhost:8000](http://localhost:8000) ក្នុង browser។

### ៦. រត់ការត្រួតពិនិត្យ

```bash
python tools/run_examples.py
python tools/check_contrast.py
```

ពិនិត្យតំណក្នុងឯកសារផងដែរ៖

```bash
make linkcheck
```

បើមិនមាន Make អាចប្រើ៖

```bash
python -m sphinx -b linkcheck source docs -q -W --keep-going
```

សូមពិនិត្យលទ្ធផលនៃពាក្យបញ្ជានីមួយៗ។ កុំសន្មតថាការសាងសង់ ឬការតេស្តបានជោគជ័យ ប្រសិនបើមិនទាន់បានដំណើរការវា។

## ការចូលរួម

អ្នកអាចជួយកែលម្អការពន្យល់ កូដ ឬកែបញ្ហាឯកសារបាន៖

1. Fork repository នេះ ឬបង្កើត branch ពី `main`។
2. កែឯកសារមេរៀន `.rst` នៅក្នុង `source/`។
3. ប្រសិនបើបន្ថែមមេរៀនថ្មី សូមបន្ថែមឈ្មោះឯកសារទៅ `toctree` ក្នុង `source/index.rst`។
4. បញ្ជាក់ប្រភពដើមក្នុង CPython `Doc/` ដោយប្រើ `.. container:: src-note` នៅទីតាំងសមស្រប។
5. សាកល្បងឧទាហរណ៍កូដ និងដំណើរការ build ដោយគ្មាន warning។
6. បង្កើត Pull Request ដោយពិពណ៌នាអំពីអ្វីដែលបានកែ និងលទ្ធផលតេស្ត។

### គោលការណ៍សម្រាប់មាតិកា

- កុំបកប្រែ Python keywords ដូចជា `if`, `for`, `def`, `class`, `return`, `True`, `False` និង `None`។
- កុំបកប្រែឈ្មោះ function, class, module, parameter ឬ API។
- ពន្យល់ពាក្យបច្ចេកទេសជាភាសាខ្មែរ ហើយដាក់ពាក្យអង់គ្លេសក្នុងវង់ក្រចកនៅពេលចាំបាច់។
- បញ្ជាក់កំណែ Python សម្រាប់មុខងារដែលអាស្រ័យលើកំណែ ដោយប្រើ `.. versionadded::` ឬ `.. versionchanged::`។
- ឧទាហរណ៍កូដត្រូវប្រើ API ពិត និងអាចដំណើរការបាន។ កុំបង្កើត API ឬលទ្ធផលដោយស្មាន។
- រក្សា Change Log និង Release Notes ដើមឱ្យនៅដដែល។

## អាជ្ញាបណ្ណនិងប្រភព

គម្រោងនេះប្រើអាជ្ញាបណ្ណផ្សេងគ្នាសម្រាប់មាតិកាដើម និងកូដគេហទំព័រ៖

- **មាតិកាដែលយោងតាម CPython៖** PSF License Version 2។ សូមអាន [LICENSE](LICENSE) និង [សេចក្ដីបញ្ជាក់ប្រភព/អាជ្ញាបណ្ណ](source/license_attribution.rst)។
- **កូដគេហទំព័រ៖** MIT License។ សូមអាន [LICENSE-CODE](LICENSE-CODE)។

មាតិកាដើមរក្សាសិទ្ធិដោយ **Python Software Foundation (PSF)**។ កំណែខ្មែរនេះជាការងារកែសម្រួលបន្តពីប្រភពដើម ហើយត្រូវរក្សាសេចក្ដីជូនដំណឹង និងព័ត៌មានអាជ្ញាបណ្ណតាមលក្ខខណ្ឌដែលពាក់ព័ន្ធ។

ឈ្មោះ **Python** និងរូបសញ្ញា Python ជាពាណិជ្ជសញ្ញារបស់ PSF។ សូមមើល [PSF Trademark Usage Policy](https://www.python.org/psf/trademarks/) និងឯកសារអាជ្ញាបណ្ណក្នុង repository សម្រាប់ព័ត៌មានលម្អិត។ គម្រោងនេះមិនត្រូវបានអនុម័ត ឬឧបត្ថម្ភដោយ PSF ទេ។

### ប្រភពផ្លូវការ

- [Python Documentation](https://docs.python.org/3/)
- [CPython Source — Doc/](https://github.com/python/cpython/tree/main/Doc)
- [Python Releases](https://www.python.org/downloads/)
- [PSF Trademark Usage Policy](https://www.python.org/psf/trademarks/)
