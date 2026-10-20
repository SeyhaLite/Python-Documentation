.. _virtual-environments:

.. container:: src-note

   ប្រភពដើម៖ CPython ``Doc/tutorial/venv.rst``, ``Doc/library/venv.rst``,
   ``Doc/installing/index.rst``, ``Doc/using/cmdline.rst`` ·
   `ឯកសារផ្លូវការ <https://docs.python.org/3/tutorial/venv.html>`_

####################################
Virtual Environments និង Packages
####################################

.. _why-venv:

ហេតុអ្វីត្រូវការ Virtual Environment?
=====================================

កម្មវិធី Python ជាច្រើនប្រើ package ដែលមិនមែនជាផ្នែកនៃបណ្ណាល័យស្តង់ដារ។
ជួនកាលកម្មវិធីពីរត្រូវការ **កំណែខុសគ្នា** នៃបណ្ណាល័យដូចគ្នា៖

.. code-block:: text

   កម្មវិធី A  →  ត្រូវការ requests 2.28
   កម្មវិធី B  →  ត្រូវការ requests 2.32

បើអ្នកដំឡើងទាំងពីរក្នុង Python តែមួយ វានឹង **ប៉ះទង្គិចគ្នា**។

**Virtual environment** គឺជាថតដាច់ដោយឡែកមួយដែលមានការដំឡើង Python
ផ្ទាល់ខ្លួន និង package ផ្ទាល់ខ្លួន។ កម្មវិធីនីមួយៗអាចមាន environment
របស់វា ដោយមិនរំខានគ្នា។

.. list-table:: អត្ថប្រយោជន៍
   :header-rows: 1
   :widths: 30 70

   * - អត្ថប្រយោជន៍
     - ការពន្យល់
   * - ដាច់ស្រឡះ
     - គម្រោងនីមួយៗមាន dependency ផ្ទាល់ខ្លួន មិនប៉ះទង្គិចគ្នា
   * - ស្អាត
     - មិនបំពុល Python របស់ប្រព័ន្ធ
   * - អាចធ្វើម្ដងទៀតបាន
     - ``requirements.txt`` ឬ ``pyproject.toml`` អនុញ្ញាតឱ្យអ្នកផ្សេងដំឡើងដូចគ្នា
   * - មិនត្រូវការសិទ្ធិ admin
     - មិនចាំបាច់ ``sudo`` ដើម្បីដំឡើង package

.. _creating-venv:

ការបង្កើត Virtual Environment
=================================

.. code-block:: console

   $ cd my-project
   $ python3 -m venv .venv

* ``-m venv`` ដំណើរការម៉ូឌុល ``venv`` ជា script។
* ``.venv`` គឺជាឈ្មោះថត។ អនុសញ្ញាទូទៅគឺ ``.venv`` ឬ ``venv``។

.. important::

   ប្រើ **interpreter ជាក់លាក់** បើអ្នកចង់បានកំណែជាក់លាក់៖

   .. code-block:: console

      $ python3.15 -m venv .venv     # environment សម្រាប់ Python 3.15
      $ py -3.13 -m venv .venv       # Windows — ជ្រើសរើសកំណែ

   ``venv`` ដំឡើងកំណែ Python ដែល **បានដំណើរការពាក្យបញ្ជា** នោះ។

.. _activating:

ការធ្វើឱ្យសកម្ម (Activate)
==============================

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - ប្រព័ន្ធ / Shell
     - ពាក្យបញ្ជា
   * - Linux / macOS (bash, zsh)
     - ``source .venv/bin/activate``
   * - Linux / macOS (fish)
     - ``source .venv/bin/activate.fish``
   * - Linux / macOS (csh/tcsh)
     - ``source .venv/bin/activate.csh``
   * - Windows (Command Prompt)
     - ``.venv\\Scripts\\activate.bat``
   * - Windows (PowerShell)
     - ``.venv\\Scripts\\Activate.ps1``

.. code-block:: console

   $ source .venv/bin/activate
   (.venv) $ python --version
   Python 3.15.0
   (.venv) $ which python
   /home/user/my-project/.venv/bin/python

សញ្ញា ``(.venv)`` នៅមុខ prompt បញ្ជាក់ថា environment កំពុងសកម្ម។

**បិទ (deactivate)៖**

.. code-block:: console

   (.venv) $ deactivate
   $

.. note::

   អ្នក **មិនចាំបាច់** activate ទេ — អ្នកអាចហៅ interpreter ដោយផ្ទាល់៖

   .. code-block:: console

      $ .venv/bin/python app.py
      $ .venv/bin/pip install requests

   នេះមានប្រយោជន៍ក្នុង script ឬ CI ដែលការ activate មិនងាយស្រួល។

.. _venv-structure:

រចនាសម្ព័ន្ធនៃ Virtual Environment
--------------------------------------

.. code-block:: text

   .venv/
   ├── bin/                    (Windows: Scripts\)
   │   ├── python  →  python3.15
   │   ├── pip
   │   └── activate
   ├── include/
   ├── lib/
   │   └── python3.15/
   │       └── site-packages/  ← package របស់អ្នកនៅទីនេះ
   └── pyvenv.cfg              ← កំណត់រចនាសម្ព័ន្ធ

.. important::

   **ដាក់ ``.venv/`` ក្នុង ``.gitignore``**។ កុំ commit environment ទេ —
   វាធំ អាស្រ័យលើប្រព័ន្ធ និងអាចបង្កើតឡើងវិញបានពី
   ``requirements.txt``។

   .. code-block:: text

      # .gitignore
      .venv/
      venv/
      __pycache__/
      *.py[cod]

.. _pip:

``pip`` — ការគ្រប់គ្រង Package
==================================

``pip`` គឺជាឧបករណ៍ដំឡើង package ស្តង់ដារ ដែលមកជាមួយ Python។

.. list-table::
   :header-rows: 1
   :widths: 40 60

   * - ពាក្យបញ្ជា
     - ការប្រើប្រាស់
   * - ``pip install requests``
     - ដំឡើងកំណែចុងក្រោយ
   * - ``pip install "requests==2.32.3"``
     - ដំឡើងកំណែជាក់លាក់
   * - ``pip install "requests>=2.31,<3"``
     - ដំឡើងក្នុងជួរកំណែ
   * - ``pip install -U requests``
     - ធ្វើបច្ចុប្បន្នភាព
   * - ``pip uninstall requests``
     - ដកចេញ
   * - ``pip list``
     - រាយ package ទាំងអស់ដែលបានដំឡើង
   * - ``pip list --outdated``
     - រាយ package ដែលមានកំណែថ្មីជាង
   * - ``pip show requests``
     - ព័ត៌មានលម្អិតអំពី package មួយ
   * - ``pip freeze``
     - បញ្ចេញជាទម្រង់ ``name==version``
   * - ``pip install -r requirements.txt``
     - ដំឡើងពីឯកសារ
   * - ``pip check``
     - ពិនិត្យ dependency ដែលបែកបាក់
   * - ``pip download pkg -d ./wheels``
     - ទាញយកដោយមិនដំឡើង

.. code-block:: console

   (.venv) $ pip install requests
   Collecting requests
     Downloading requests-2.32.3-py3-none-any.whl.metadata (4.6 kB)
   Collecting charset-normalizer<4,>=2 (from requests)
     Downloading charset_normalizer-3.4.0-py3-none-any.whl.metadata (34 kB)
   ...
   Successfully installed requests-2.32.3 urllib3-2.2.3

.. note::

   ``pip`` ដំឡើង **dependency ដោយស្វ័យប្រវត្តិ**។ ក្នុងឧទាហរណ៍ខាងលើ
   ``requests`` ទាញយក ``charset-normalizer``, ``idna``, ``certifi`` និង
   ``urllib3`` ផងដែរ។

.. _version-specifiers:

Version Specifier
-----------------

.. list-table::
   :header-rows: 1
   :widths: 24 76

   * - Specifier
     - អត្ថន័យ
   * - ``==2.32.3``
     - កំណែជាក់លាក់នេះតែប៉ុណ្ណោះ
   * - ``!=2.32.0``
     - គ្រប់កំណែ លើកលែងកំណែនេះ
   * - ``>=2.31``
     - កំណែនេះ ឬថ្មីជាង
   * - ``>2.31``
     - ថ្មីជាងដាច់ខាត
   * - ``<3``
     - ចាស់ជាងដាច់ខាត
   * - ``<=2.32.3``
     - កំណែនេះ ឬចាស់ជាង
   * - ``~=2.32``
     - *compatible release* — ស្មើ ``>=2.32, ==2.*``
   * - ``===2.32.3``
     - ផ្គូផ្គងខ្សែអក្សរដាច់ខាត (កម្រប្រើ)

.. warning::

   **Semantic versioning** (``MAJOR.MINOR.PATCH``) គឺជា **អនុសញ្ញា**
   មិនមែនជាការធានាទេ។ Package អាចបំបែក API ក្នុងកំណែ patch។
   សម្រាប់កម្មវិធីផលិតកម្ម សូម **ខ្ទាស់កំណែ** (pin) ឱ្យជាក់លាក់។

.. _requirements:

``requirements.txt``
====================

វិធីសាមញ្ញបំផុតដើម្បីកត់ត្រា dependency៖

.. code-block:: console

   # កត់ត្រា environment បច្ចុប្បន្ន
   (.venv) $ pip freeze > requirements.txt

   # ដំឡើងឡើងវិញនៅកន្លែងផ្សេង
   (.venv) $ pip install -r requirements.txt

**ទម្រង់ឯកសារ៖**

.. code-block:: text

   # requirements.txt
   # ---- runtime ----
   requests==2.32.3
   click>=8.1,<9
   pydantic~=2.9

   # ---- development ----
   -r requirements-dev.txt

   # ---- ពី git ----
   git+https://github.com/user/repo.git@v1.2.3#egg=mypackage

   # ---- ឯកសារ wheel ក្នុងស្រុក ----
   ./wheels/custom-1.0-py3-none-any.whl

.. list-table:: ភាពខុសគ្នារវាងឯកសារពីរប្រភេទ
   :header-rows: 1
   :widths: 30 35 35

   * -
     - ``requirements.txt``
     - ``pyproject.toml``
   * - គោលបំណង
     - កំណត់ environment ជាក់លាក់
     - ប្រកាស metadata និង dependency របស់ package
   * - កំណែ
     - ជាធម្មតាខ្ទាស់ជាក់លាក់ (``==``)
     - ជាធម្មតាជួរ (``>=``, ``~=``)
   * - បង្កើតដោយ
     - ``pip freeze``
     - អ្នកសរសេរដោយដៃ
   * - ប្រើសម្រាប់
     - deployment, CI
     - ការចែកចាយ library, គម្រោងទំនើប

.. tip::

   សម្រាប់គម្រោងផលិតកម្ម អនុវត្តល្អគឺមាន **ពីរឯកសារ**៖

   * ``requirements.in`` ឬ ``pyproject.toml`` — dependency ដែលអ្នកត្រូវការ
     (ជួរកំណែ)
   * ``requirements.txt`` — លទ្ធផលដែលបានខ្ទាស់ជាក់លាក់
     (បង្កើតដោយ ``pip-compile`` ពី ``pip-tools`` ឬ ``uv pip compile``)

.. _pyproject:

``pyproject.toml``
==================

ឯកសារកំណត់រចនាសម្ព័ន្ធស្តង់ដារសម្រាប់គម្រោង Python (PEP 518, 621)៖

.. code-block:: toml

   [build-system]
   requires = ["hatchling"]
   build-backend = "hatchling.build"

   [project]
   name = "my-app"
   version = "1.4.0"
   description = "កម្មវិធីឧទាហរណ៍"
   readme = "README.md"
   requires-python = ">=3.12"
   license = { text = "MIT" }
   authors = [{ name = "Sokha", email = "sokha@example.com" }]
   dependencies = [
       "requests>=2.31,<3",
       "click>=8.1",
   ]

   [project.optional-dependencies]
   dev = [
       "pytest>=8.0",
       "ruff>=0.6",
       "mypy>=1.11",
   ]

   [project.scripts]
   my-app = "my_app.cli:main"

   [tool.ruff]
   line-length = 100
   target-version = "py312"

.. code-block:: console

   # ដំឡើងគម្រោងជា editable (កូដផ្លាស់ប្ដូរភ្លាម មិនចាំបាច់ដំឡើងម្ដងទៀត)
   $ pip install -e .

   # ដំឡើងរួមទាំង optional dependency
   $ pip install -e ".[dev]"

.. _common-problems:

បញ្ហាទូទៅ និងដំណោះស្រាយ
========================

.. list-table::
   :header-rows: 1
   :widths: 34 66

   * - បញ្ហា
     - ដំណោះស្រាយ
   * - ``ModuleNotFoundError`` ទោះបីបានដំឡើង
     - អ្នកកំពុងប្រើ interpreter ខុស។ ពិនិត្យ ``which python`` ឬ ``sys.executable``
   * - ``error: externally-managed-environment``
     - PEP 668 — distribution បានហាមដំឡើងទៅ system Python។ **ប្រើ venv** ឬ ``pipx``
   * - ``Permission denied`` ពេល ``pip install``
     - កុំប្រើ ``sudo pip``។ បង្កើត venv វិញ
   * - Prompt មិនបង្ហាញ ``(.venv)``
     - Activate មិនបានជោគជ័យ ឬ prompt របស់អ្នកមិនគាំទ្រ។ ពិនិត្យ ``sys.prefix``
   * - Dependency ប៉ះទង្គិចគ្នា
     - ដំណើរការ ``pip check`` ហើយពិនិត្យជួរកំណែ
   * - ``pip`` យឺត
     - ប្រើ ``--no-cache-dir`` ឬឧបករណ៍ទំនើបដូចជា ``uv``
   * - Activate បរាជ័យលើ Windows PowerShell
     - ការកំណត់ ExecutionPolicy — ដំណើរការ ``Set-ExecutionPolicy -Scope CurrentUser RemoteSigned``

.. code-block:: pycon

   >>> # ពិនិត្យថាអ្នកកំពុងប្រើ interpreter ណា
   >>> import sys
   >>> sys.executable != ""
   True
   >>> sys.prefix == sys.base_prefix      # False = ក្នុង virtual environment
   True

.. important::

   ``sys.prefix != sys.base_prefix`` គឺជាវិធីដែល **អាចទុកចិត្តបាន**
   ដើម្បីពិនិត្យថាអ្នកកំពុងស្ថិតក្នុង virtual environment។

.. _pep668:

PEP 668 — ``externally-managed-environment``
------------------------------------------------

.. versionadded:: 3.11

Distribution Linux ជាច្រើន (Debian 12+, Ubuntu 23.04+, Fedora 38+) បាន
សម្គាល់ Python របស់ប្រព័ន្ធថា **គ្រប់គ្រងដោយខាងក្រៅ**។ នេះមានន័យថា
``pip install`` ទៅប្រព័ន្ធនឹងបរាជ័យ៖

.. code-block:: text

   error: externally-managed-environment
   × This environment is externally managed
   ╰─> To install Python packages system-wide, try apt install python3-xyz...

**នេះគឺជាការការពារ មិនមែនជាកំហុសទេ។** ឧបករណ៍ប្រព័ន្ធជាច្រើនពឹងផ្អែក
លើ Python របស់ប្រព័ន្ធ ហើយ ``pip`` អាចបំបែកវា។

ដំណោះស្រាយត្រឹមត្រូវ៖

.. code-block:: console

   # ១. Virtual environment (ណែនាំសម្រាប់គម្រោង)
   $ python3 -m venv .venv && source .venv/bin/activate
   $ pip install requests

   # ២. pipx (ណែនាំសម្រាប់ឧបករណ៍ CLI)
   $ pipx install black

   # ៣. apt (សម្រាប់ package ប្រព័ន្ធ)
   $ sudo apt install python3-requests

.. warning::

   កុំប្រើ ``pip install --break-system-packages`` ឬ ``sudo pip install``
   លើកលែងតែអ្នកយល់ច្បាស់ពីផលវិបាក។ វាអាចបំផ្លាញឧបករណ៍ប្រព័ន្ធ។

.. _modern-tools:

ឧបករណ៍ទំនើប
============

.. list-table::
   :header-rows: 1
   :widths: 20 80

   * - ឧបករណ៍
     - ការពិពណ៌នា
   * - **uv**
     - ឧបករណ៍គ្រប់គ្រងគម្រោង និង package សរសេរជា Rust។ លឿនជាង ``pip`` ច្រើនដង អាចជំនួស ``venv``, ``pip``, ``pip-tools``, ``pyenv``។ ``uv venv``, ``uv pip install``, ``uv run``
   * - **pipx**
     - ដំឡើងឧបករណ៍ CLI ក្នុង environment ដាច់ដោយឡែក។ ``pipx install black``
   * - **poetry**
     - គ្រប់គ្រង dependency + build + publish។ ប្រើ ``pyproject.toml`` និង lock file
   * - **pdm**
     - ដូច poetry ប៉ុន្តែអនុវត្តតាម PEP 582
   * - **pip-tools**
     - ``pip-compile`` បង្កើត ``requirements.txt`` ដែលបានខ្ទាស់ពី ``.in`` file
   * - **conda / mamba**
     - សម្រាប់វិទ្យាសាស្ត្រទិន្នន័យ — គ្រប់គ្រងទាំង package មិនមែន Python
   * - **pyenv**
     - គ្រប់គ្រង **កំណែ Python** ច្រើន (មិនមែន package)

.. tip::

   សម្រាប់អ្នកចាប់ផ្ដើម ``venv`` + ``pip`` គឺគ្រប់គ្រាន់។ នៅពេលគម្រោងធំឡើង
   សូមពិចារណា ``uv`` (លឿន និងសាមញ្ញ) ឬ ``poetry`` (lock file និង
   dependency resolution ខ្លាំង)។

   ``uv`` អាចបង្កើត environment និងដំឡើង package ក្នុងពាក្យបញ្ជាតែមួយ៖

   .. code-block:: console

      $ uv venv                     # បង្កើត .venv
      $ uv pip install requests     # ដំឡើង
      $ uv run app.py               # ដំណើរការក្នុង environment

.. _venv-best-practices:

ការអនុវត្តល្អបំផុត
======================

#. **បង្កើត virtual environment សម្រាប់គម្រោងនីមួយៗ** — គ្មានករណីលើកលែង។
#. **ដាក់ ``.venv/`` ក្នុង ``.gitignore``** — commit តែ
   ``requirements.txt`` ឬ ``pyproject.toml``។
#. **ខ្ទាស់កំណែ** សម្រាប់ deployment (``==``) ប្រើជួរ (``>=``, ``~=``)
   សម្រាប់ library។
#. **កុំប្រើ ``sudo pip``** ឬ ``--break-system-packages``។
#. **ដំណើរការ ``pip check``** ក្នុង CI ដើម្បីរក dependency បែកបាក់។
#. **ប្រើ lock file** (``uv.lock``, ``poetry.lock``, ``requirements.txt``
   ដែលបាន compile) ដើម្បីធានាការដំឡើងដូចគ្នាគ្រប់ទីកន្លែង។
#. **ញែក dev dependency** ពី runtime dependency
   (``[project.optional-dependencies] dev = [...]``)។
#. **ដំឡើងឡើងវិញពីសូន្យ** ជាការសាកល្បង — បើ ``pip install -r``
   មិនដំណើរការលើ machine ស្អាត នោះគម្រោងរបស់អ្នកមិនអាចធ្វើម្ដងទៀតបានទេ។
#. **ធ្វើបច្ចុប្បន្នភាពជាទៀងទាត់** — ``pip list --outdated``។

.. _venv-summary:

សង្ខេប
======

.. list-table::
   :header-rows: 1
   :widths: 34 66

   * - ពាក្យបញ្ជា
     - ការប្រើប្រាស់
   * - ``python3 -m venv .venv``
     - បង្កើត environment
   * - ``source .venv/bin/activate``
     - ធ្វើឱ្យសកម្ម (Unix/macOS)
   * - ``.venv\\Scripts\\activate``
     - ធ្វើឱ្យសកម្ម (Windows)
   * - ``deactivate``
     - បិទ
   * - ``pip install pkg==1.2.3``
     - ដំឡើងកំណែជាក់លាក់
   * - ``pip freeze > requirements.txt``
     - កត់ត្រា environment
   * - ``pip install -r requirements.txt``
     - ស្ដារ environment
   * - ``pip install -e .``
     - ដំឡើងគម្រោងខ្លួនឯងជា editable
   * - ``pip check``
     - ពិនិត្យ dependency បែកបាក់
   * - ``sys.prefix != sys.base_prefix``
     - ពិនិត្យថាស្ថិតក្នុង venv

.. rubric:: ប្រភពយោង

* `Virtual Environments and Packages <https://docs.python.org/3/tutorial/venv.html>`_
* `venv — Creation of virtual environments <https://docs.python.org/3/library/venv.html>`_
* `Installing Python Modules <https://docs.python.org/3/installing/index.html>`_
* `pip documentation <https://pip.pypa.io/>`_
* `PyPI — Python Package Index <https://pypi.org/>`_
* `PEP 405 — Python Virtual Environments <https://peps.python.org/pep-0405/>`_
* `PEP 517/518 — pyproject.toml <https://peps.python.org/pep-0518/>`_
* `PEP 621 — Project metadata in pyproject.toml <https://peps.python.org/pep-0621/>`_
* `PEP 668 — Externally Managed Environments <https://peps.python.org/pep-0668/>`_
* `uv documentation <https://docs.astral.sh/uv/>`_
