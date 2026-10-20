.. _getting-started:

.. container:: src-note

   ប្រភពដើម៖ CPython ``Doc/tutorial/appetite.rst``, ``Doc/tutorial/interpreter.rst``,
   ``Doc/using/unix.rst``, ``Doc/using/windows.rst``, ``Doc/using/mac.rst``,
   ``Doc/using/cmdline.rst`` ·
   `ឯកសារផ្លូវការ <https://docs.python.org/3/tutorial/index.html>`_

############################################
ចាប់ផ្ដើម និងការដំឡើង Python
############################################

.. _what-is-python:

តើ Python ជាអ្វី?
==================

Python គឺជាភាសាកម្មវិធី (programming language) កម្រិតខ្ពស់ ដែលរចនាឡើងដោយ
លោក **Guido van Rossum** នៅដើមទសវត្សរ៍ ១៩៩០។ វាលេចធ្លោដោយសារ៖

* **វាក្យសម្ពន្ធសាមញ្ញ** — កូដ Python អានដូចអង់គ្លេសសាមញ្ញ ដូច្នេះងាយរៀន
  និងងាយថែទាំ។
* **រចនាសម្ព័ន្ធទិន្នន័យកម្រិតខ្ពស់មានស្រាប់** — ``list``, ``dict``, ``set``,
  ``tuple`` ដំណើរការលឿន និងមិនចាំបាច់ប្រកាសទំហំជាមុន។
* **បណ្ណាល័យស្តង់ដារ (standard library) ធំ** — មានម៉ូឌុលសម្រាប់ឯកសារ,
  បណ្ដាញ, JSON, ពេលវេលា, regular expression និងច្រើនទៀត ដោយមិនចាំបាច់
  ដំឡើងអ្វីបន្ថែម។
* **Interpreted language** — អ្នកអាចសាកល្បងកូដភ្លាមៗក្នុង REPL ដោយមិនចាំបាច់
  compile ជាមុន។
* **Dynamic typing** — អថេរមិនចាំបាច់ប្រកាសប្រភេទ (type) ជាមុនទេ។

.. note::

   Python នៅទីនេះសំដៅលើ **Python 3** ប៉ុណ្ណោះ។ Python 2 ត្រូវបានបញ្ឈប់
   ការគាំទ្រជាផ្លូវការតាំងពីថ្ងៃទី ១ មករា ២០២០ ហើយមិនទទួលបានការជួសជុល
   សុវត្ថិភាពទៀតទេ។

.. _installation:

ការដំឡើង Python
================

.. _install-windows:

Windows
-------

មានជម្រើសធំៗពីរ៖

**ជម្រើសទី ១ — Installer ផ្លូវការពី python.org (ណែនាំ)**

1. ទៅកាន់ https://www.python.org/downloads/windows/ ហើយទាញយកកំណែ
   *Windows installer (64-bit)* ចុងក្រោយ។
2. ដំណើរការឯកសារ ``.exe`` ដែលបានទាញយក។
3. **សំខាន់បំផុត៖** ក្នុងអេក្រង់ដំបូង សូមធីកប្រអប់
   ``Add python.exe to PATH`` មុនចុច *Install Now*។ បើអ្នកភ្លេចធីក
   ពាក្យបញ្ជា ``python`` នឹងមិនដំណើរការក្នុង Command Prompt ទេ។

**ជម្រើសទី ២ — Microsoft Store**

ស្វែងរក "Python" ក្នុងកម្មវិធី Microsoft Store ហើយចុច *Get*។ វិធីនេះងាយ
បំផុត ហើយធ្វើបច្ចុប្បន្នភាពដោយស្វ័យប្រវត្តិ ប៉ុន្តែមានដែនកំណត់មួយចំនួន
លើការចូលដំណើរការឯកសារក្រៅផ្ទះរបស់អ្នក។

**ការផ្ទៀងផ្ទាត់**

បើក Command Prompt (``cmd``) ឬ PowerShell ហើយវាយ៖

.. code-block:: console

   C:\> py -V
   Python 3.15.0

   C:\> python --version
   Python 3.15.0

នៅលើ Windows ពាក្យបញ្ជា ``py`` គឺជា **Python launcher** ដែលអនុញ្ញាតឱ្យ
អ្នកជ្រើសរើសកំណែជាក់លាក់បាន ឧទាហរណ៍ ``py -3.13`` ឬ ``py -3.15``។

.. _install-macos:

macOS
-----

**Installer ផ្លូវការ (ណែនាំ)**

1. ទៅ https://www.python.org/downloads/macos/ ហើយទាញយកឯកសារ
   *macOS 64-bit universal2 installer*។
2. ដំណើរការឯកសារ ``.pkg`` ហើយដើរតាមជំហានរហូតដល់ចប់។
3. បន្ទាប់ពីដំឡើងរួច សូមដំណើរការឯកសារ
   ``Install Certificates.command`` ដែលនៅក្នុងថត
   ``/Applications/Python 3.15/``។ ជំហាននេះដំឡើងវិញ្ញាបនបត្រ SSL ដែល
   ``pip`` និង ``urllib`` ត្រូវការ ដើម្បីភ្ជាប់ទៅគេហទំព័រ HTTPS។

**Homebrew**

.. code-block:: console

   $ brew install python@3.15

**ការផ្ទៀងផ្ទាត់** — បើក Terminal ហើយវាយ៖

.. code-block:: console

   $ python3 --version
   Python 3.15.0

.. attention::

   នៅលើ macOS ពាក្យបញ្ជា ``python`` (គ្មានលេខ ៣) អាចសំដៅលើ Python ចាស់
   របស់ប្រព័ន្ធ ឬមិនមានសោះ។ សូមប្រើ ``python3`` ជានិច្ច។

.. _install-linux:

Linux
-----

ភាគច្រើននៃ distribution Linux សម័យថ្មីមាន Python 3 ដំឡើងរួចហើយ។ ពិនិត្យដោយ៖

.. code-block:: console

   $ python3 --version

បើមិនមាន សូមដំឡើងតាម package manager របស់អ្នក៖

.. code-block:: console

   # Debian / Ubuntu
   $ sudo apt update && sudo apt install python3 python3-pip python3-venv

   # Fedora / RHEL
   $ sudo dnf install python3 python3-pip

   # Arch Linux
   $ sudo pacman -S python python-pip

   # openSUSE
   $ sudo zypper install python3 python3-pip

   # Alpine
   $ sudo apk add python3 py3-pip

.. tip::

   នៅលើ Linux កុំលុប ឬជំនួស ``/usr/bin/python3`` ដែលមកជាមួយប្រព័ន្ធ។
   ឧបករណ៍ប្រព័ន្ធជាច្រើនពឹងផ្អែកលើវា។ បើអ្នកត្រូវការកំណែផ្សេង
   សូមដំឡើងនៅកន្លែងផ្សេង ឬប្រើ virtual environment
   (មើលជំពូក *Virtual Environments*)។

.. _verify-install:

ការផ្ទៀងផ្ទាត់ការដំឡើង
----------------------

វិធីលឿនបំផុតគឺបើក REPL ហើយពិនិត្យព័ត៌មានកំណែ៖

.. code-block:: console

   $ python3
   Python 3.15.0 (main, Oct 14 2026, 01:05:07) [Clang 23.1.3] on linux
   Type "help", "copyright", "credits" or "license" for more information.
   >>> import sys
   >>> sys.version_info
   sys.version_info(major=3, minor=15, micro=0, releaselevel='final', serial=0)
   >>> sys.executable
   '/usr/local/bin/python3'
   >>> exit()

.. _repl:

REPL — របៀប Interactive
========================

**REPL** (Read–Eval–Print Loop) គឺជាម៉ូដអន្តរកម្ម ដែល Python អានបន្ទាត់កូដ
ដំណើរការវា បោះពុម្ពលទ្ធផល ហើយរង់ចាំបន្ទាត់បន្ទាប់។ វាល្អបំផុតសម្រាប់សាកល្បង
គំនិតតូចៗ និងរៀនភាសា។

.. code-block:: pycon

   >>> 2 + 3
   5
   >>> "Python" * 2
   'PythonPython'
   >>> name = "ខ្មែរ"
   >>> print(f"សួស្ដី {name}!")
   សួស្ដី ខ្មែរ!

**សញ្ញា prompt ពីរប្រភេទ៖**

.. list-table::
   :header-rows: 1
   :widths: 15 85

   * - Prompt
     - អត្ថន័យ
   * - ``>>>``
     - *Primary prompt* — រង់ចាំបន្ទាត់កូដថ្មី (statement ពេញលេញ)។
   * - ``...``
     - *Secondary prompt* — បន្តបន្ទាត់នៃ block ដែលមិនទាន់ចប់
       (ឧ. ខ្លួន ``if``, ``for``, ``def``)។

ចេញពី REPL ដោយ៖

* **Unix / Linux / macOS** — ចុច :kbd:`Control-D`
* **Windows** — ចុច :kbd:`Control-Z` រួច :kbd:`Enter`
* **គ្រប់ប្រព័ន្ធ** — វាយ ``quit()`` ឬ ``exit()``

.. _indentation-in-repl:

Indentation គឺចាំបាច់
----------------------

Python ប្រើ **ការចូលបន្ទាត់ (indentation)** ដើម្បីកំណត់ block ជំនួសឱ្យ
វង់ក្រចក ``{}`` ឬពាក្យ ``begin``/``end``។ នៅក្នុង REPL អ្នកត្រូវចុច
:kbd:`Enter` ទទេម្ដងទៀតដើម្បីបញ្ចប់ block៖

.. code-block:: pycon

   >>> for i in range(3):
   ...     print(i, end=" ")
   ...
   0 1 2

.. warning::

   ប្រើ **ដកឃ្លា (space) ៤** សម្រាប់ indentation ជានិច្ច កុំលាយឡំជាមួយ
   tab។ ការលាយឡំបណ្ដាលឱ្យមាន ``IndentationError`` ឬ ``TabError``
   ដែលពិបាកមើលឃើញ។ កំណត់ editor របស់អ្នកឱ្យបំលែង tab ទៅជា space ៤។

.. _running-scripts:

ការដំណើរការ Script
===================

ដាក់កូដក្នុងឯកសារដែលមានផ្នែកបន្ថែម ``.py`` ឧទាហរណ៍ ``hello.py``៖

.. literalinclude:: _code/hello.py
   :language: python
   :caption: ``hello.py``

ដំណើរការវា៖

.. code-block:: console

   $ python3 hello.py
   សួស្ដីពី Python 3.15!
   ផលបូក 1 + 2 = 3

.. _command-line-options:

ជម្រើសបន្ទាត់ពាក្យបញ្ជាដែលសំខាន់
------------------------------------

.. list-table::
   :header-rows: 1
   :widths: 28 72

   * - ពាក្យបញ្ជា
     - ការប្រើប្រាស់
   * - ``python3 script.py``
     - ដំណើរការឯកសារ script។
   * - ``python3 -c "code"``
     - ដំណើរការកូដដែលបានវាយផ្ទាល់។ ដាក់កូដក្នុងសញ្ញាសម្រង់ជានិច្ច។
   * - ``python3 -m module``
     - ដំណើរការម៉ូឌុលជា script ឧ. ``python3 -m json.tool`` ឬ ``python3 -m venv .venv``។
   * - ``python3 -i script.py``
     - ដំណើរការ script រួចបន្តចូល REPL ដើម្បីពិនិត្យអថេរ។
   * - ``python3 -V``
     - បោះពុម្ពកំណែ Python។
   * - ``python3 -h``
     - បង្ហាញជម្រើសទាំងអស់។

ឧទាហរណ៍ជាក់ស្ដែង៖

.. code-block:: console

   $ python3 -c "import platform; print(platform.python_version())"
   3.15.0

   $ python3 -m this | head -3
   The Zen of Python, by Tim Peters

   Beautiful is better than ugly.

.. _shebang:

Shebang នៅលើ Unix
-------------------

ដើម្បីដំណើរការ script ដោយផ្ទាល់ (``./hello.py``) សូមដាក់បន្ទាត់ដំបូងជា
*shebang*៖

.. code-block:: python

   #!/usr/bin/env python3

រួចផ្ដល់សិទ្ធិប្រតិបត្តិ៖

.. code-block:: console

   $ chmod +x hello.py
   $ ./hello.py
   សួស្ដីពី Python 3.15!

វិធី ``/usr/bin/env python3`` ល្អជាង ``/usr/bin/python3`` ព្រោះវាស្វែងរក
Python ក្នុង ``PATH`` របស់អ្នកប្រើ។

.. _command-line-arguments:

ការទទួល Argument ពីបន្ទាត់ពាក្យបញ្ជា
------------------------------------

Argument ទាំងអស់ត្រូវបានដាក់ក្នុង list ឈ្មោះ ``sys.argv``។ ធាតុដំបូង
``sys.argv[0]`` គឺឈ្មោះ script ខ្លួនឯង។

.. literalinclude:: _code/argv_demo.py
   :language: python
   :caption: ``argv_demo.py``

.. code-block:: console

   $ python3 argv_demo.py សុខា ដារ៉ា
   ['argv_demo.py', 'សុខា', 'ដារ៉ា']
   ចំនួន argument (មិនរាប់ឈ្មោះឯកសារ): 2
   argument ដំបូង: សុខា

.. _encoding:

Encoding — UTF-8 ជាលំនាំដើម
============================

ចាប់តាំងពី Python 3 មក ឯកសារប្រភព (``.py``) ត្រូវបានអានជា **UTF-8**
ជាលំនាំដើម។ ដូច្នេះអ្នកអាចប្រើអក្សរខ្មែរក្នុងខ្សែអក្សរ (string) និងក្នុង
អត្ថាធិប្បាយ (comment) បានដោយសេរី៖

.. code-block:: pycon

   >>> greeting = "សួស្ដី ពិភពលោក"
   >>> len(greeting)                 # ១៤ តួអក្សរ (រួមទាំងដកឃ្លាមួយ)
   14
   >>> len(greeting.encode("utf-8")) # ៤០ byte
   40
   >>> greeting[0]
   'ស'

.. note::

   ``len()`` រាប់ចំនួន **តួអក្សរ** (character) មិនមែនចំនួន byte ទេ។
   អក្សរខ្មែរមួយត្រូវការ ៣ byte ក្នុង UTF-8 ប៉ុន្តែរាប់ជា ១ តួអក្សរ។
   ចំណាំថា **ស្រៈ និងជើងអក្សរខ្មែរក៏រាប់ជាតួអក្សរដាច់ដោយឡែកដែរ** —
   ពាក្យ ``"សួស្ដី"`` មាន ៦ តួអក្សរ មិនមែន ៥ ទេ។ បើអ្នកចង់ដឹងចំនួន byte
   ប្រើ ``len(greeting.encode("utf-8"))``។

ពេលអានឬសរសេរឯកសារ សូមបញ្ជាក់ ``encoding="utf-8"`` ជាច្បាស់លាស់ជានិច្ច
(មើលជំពូក :doc:`file_handling`) ព្រោះលំនាំដើមអាចខុសគ្នាតាមប្រព័ន្ធ
ប្រតិបត្តិការ។

.. _editors:

កម្មវិធីកែកូដ (Editor)
==========================

អ្នកអាចសរសេរ Python ដោយប្រើកម្មវិធីអត្ថបទធម្មតាណាក៏បាន ប៉ុន្តែ editor
ដែលមាន *syntax highlighting* និង *indentation* ស្វ័យប្រវត្តិជួយច្រើន៖

.. list-table::
   :header-rows: 1
   :widths: 25 75

   * - ឧបករណ៍
     - ចំណាំ
   * - **IDLE**
     - មកជាមួយការដំឡើង Python ស្តង់ដារ។ សាមញ្ញ សមស្របសម្រាប់អ្នកចាប់ផ្ដើម។
   * - **VS Code**
     - ឥតគិតថ្លៃ មាន extension Python ផ្លូវការ។
   * - **PyCharm**
     - IDE ពេញលេញ មានកំណែ Community ឥតគិតថ្លៃ។
   * - **Vim / Neovim / Emacs**
     - សម្រាប់អ្នកចូលចិត្តធ្វើការក្នុង terminal។

.. tip::

   កំណត់ editor របស់អ្នកឱ្យ៖ (១) រក្សាទុកជា UTF-8, (២) បំលែង tab ទៅ
   space ៤, (៣) បង្ហាញលេខបន្ទាត់។ ការកំណត់ទាំងបីនេះដោះស្រាយបញ្ហា
   ``IndentationError`` និងអក្សរខូចភាគច្រើន។

.. _first-program:

កម្មវិធីដំបូងរបស់អ្នក
=========================

សូមសរសេរឯកសារ ``first.py`` ដូចខាងក្រោម៖

.. literalinclude:: _code/first.py
   :language: python
   :caption: ``first.py``

ដំណើរការ៖

.. code-block:: console

   $ python3 first.py
   សូមបញ្ចូលឈ្មោះរបស់អ្នក: សុភា
   សូមបញ្ចូលអាយុរបស់អ្នក: 20
   សួស្ដី សុភា! អ្នកមានអាយុ 20 ឆ្នាំ។
   ក្នុងរយៈពេល ៥ ឆ្នាំទៀត អ្នកនឹងមានអាយុ 25 ឆ្នាំ។

ចំណុចគួរកត់សម្គាល់ពីឧទាហរណ៍នេះ៖

* ``input()`` តែងតែត្រឡប់ជា **string** ដូច្នេះត្រូវបំលែងទៅ ``int``
  ដោយ ``int(...)`` មុនធ្វើគណនា។
* **f-string** (``f"..."``) អនុញ្ញាតឱ្យបញ្ចូលតម្លៃអថេរក្នុងខ្សែអក្សរ
  ដោយដាក់វាក្នុងវង់ក្រចកដង្កៀប ``{}``។
* ``#`` ចាប់ផ្ដើម **comment** — Python មិនអានវាទេ។

.. _next-steps:

ជំហានបន្ទាប់
=============

ឥឡូវអ្នកមាន Python ដំណើរការរួចហើយ។ ជំពូកបន្ទាប់នឹងពន្យល់អំពីវាក្យសម្ពន្ធ
អថេរ និងប្រភេទទិន្នន័យ៖ :doc:`syntax_variables_types`។

.. rubric:: ប្រភពយោង

* `Using the Python Interpreter <https://docs.python.org/3/tutorial/interpreter.html>`_
* `Using Python on a Unix Platform <https://docs.python.org/3/using/unix.html>`_
* `Using Python on Windows <https://docs.python.org/3/using/windows.html>`_
* `Using Python on macOS <https://docs.python.org/3/using/mac.html>`_
* `Command line and environment <https://docs.python.org/3/using/cmdline.html>`_
