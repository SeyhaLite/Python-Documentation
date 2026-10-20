.. _modules-packages:

.. container:: src-note

   ប្រភពដើម៖ CPython ``Doc/tutorial/modules.rst``, ``Doc/reference/import.rst``,
   ``Doc/library/sys.rst``, ``Doc/library/importlib.rst`` ·
   `ឯកសារផ្លូវការ <https://docs.python.org/3/tutorial/modules.html>`_

#############################
Modules និង Packages
#############################

នៅពេលកម្មវិធីរបស់អ្នកវែងឡើង ការដាក់កូដទាំងអស់ក្នុងឯកសារតែមួយធ្វើឱ្យវា
ពិបាកថែទាំ។ Python ដោះស្រាយបញ្ហានេះដោយ **module** និង **package**។

.. _what-is-module:

តើ Module ជាអ្វី?
===================

**Module** គឺជាឯកសារ ``.py`` មួយដែលមានកូដ Python។ ឈ្មោះឯកសារ (ដក
``.py`` ចេញ) ក្លាយជាឈ្មោះ module។

ឧទាហរណ៍ បង្កើតឯកសារ ``greetings.py``៖

.. code-block:: python

   """ម៉ូឌុលសាកល្បង — ផ្ដល់ពាក្យសួស្ដីជាច្រើនភាសា។"""

   DEFAULT_LANGUAGE = "km"

   _TRANSLATIONS = {
       "km": "សួស្ដី",
       "en": "Hello",
       "ja": "こんにちは",
   }


   def greet(name, lang=None):
       """ត្រឡប់ពាក្យសួស្ដីសម្រាប់មនុស្សម្នាក់។"""
       word = _TRANSLATIONS.get(lang or DEFAULT_LANGUAGE, _TRANSLATIONS["en"])
       return f"{word}, {name}!"


   def supported_languages():
       """ត្រឡប់បញ្ជីភាសាដែលគាំទ្រ។"""
       return sorted(_TRANSLATIONS)

.. _importing:

ការនាំចូល (Import)
======================

មានវិធីនាំចូលបួនយ៉ាង៖

.. code-block:: python

   # ១. នាំចូល module ទាំងមូល — ចូលដំណើរការតាមឈ្មោះ module
   import greetings
   print(greetings.greet("សុខា"))

   # ២. នាំចូលធាតុជាក់លាក់
   from greetings import greet, supported_languages
   print(greet("ដារ៉ា"))

   # ៣. នាំចូលដោយដាក់ឈ្មោះហៅក្រៅ (alias)
   import greetings as gr
   print(gr.greet("សុភា"))

   # ៤. នាំចូលទាំងអស់ — ⚠ មិនណែនាំ
   from greetings import *

.. code-block:: pycon

   >>> import greetings
   >>> greetings.greet("សុខា")
   'សួស្ដី, សុខា!'
   >>> greetings.DEFAULT_LANGUAGE
   'km'
   >>> greetings.supported_languages()
   ['en', 'ja', 'km']
   >>> greetings.__name__
   'greetings'
   >>> greetings.__doc__.splitlines()[0]
   'ម៉ូឌុលសាកល្បង — ផ្ដល់ពាក្យសួស្ដីជាច្រើនភាសា។'

.. warning::

   **កុំប្រើ ``from module import *``** លើកលែងតែក្នុង REPL ឬកូដសាកល្បង។
   វាបញ្ចូលឈ្មោះដែលអ្នកមិនដឹងទៅក្នុង namespace របស់អ្នក ហើយអាច
   **បិទបាំង** (shadow) ឈ្មោះដែលមានស្រាប់ ធ្វើឱ្យ bug ពិបាករក។

   បើ module កំណត់ ``__all__`` វានឹងកំណត់ថាឈ្មោះណាត្រូវបាននាំចេញ
   (មើលផ្នែក :ref:`all-variable`)។

.. _import-mechanics:

អ្វីកើតឡើងពេល ``import``?
---------------------------

#. Python ស្វែងរក module នៅក្នុង **module search path** (``sys.path``)។
#. បើរកឃើញ វាដំណើរការកូដក្នុងឯកសារ **ម្ដងគត់** ហើយបង្កើត module object។
#. Module object ត្រូវបានរក្សាទុកក្នុង ``sys.modules`` ជា cache។
#. ឈ្មោះ module ត្រូវបានភ្ជាប់ក្នុង namespace បច្ចុប្បន្ន។

.. important::

   Module ត្រូវបានដំណើរការ **តែម្ដងគត់**។ ការ ``import`` លើកទីពីរ
   យកពី cache មិនមែនដំណើរការឯកសារម្ដងទៀតទេ៖

   .. code-block:: pycon

      >>> import sys
      >>> import greetings           # លើកទីពីរ — គ្មានការដំណើរការឡើងវិញ
      >>> sys.modules["greetings"] is greetings
      True

   ដូច្នេះកូដកម្រិត module (ការកំណត់អថេរ, ``print``, ការភ្ជាប់បណ្ដាញ)
   ដំណើរការតែម្ដង។ នេះជាមូលហេតុដែលគេដាក់ការកំណត់រចនាសម្ព័ន្ធ
   (configuration) នៅកម្រិត module។

.. _module-namespace:

Namespace របស់ Module
---------------------

Module គឺជា **object** ដែលមាន attribute។ អថេរ អនុគមន៍ និង class ទាំងអស់
ក្នុងឯកសារក្លាយជា attribute របស់វា៖

.. code-block:: pycon

   >>> import greetings
   >>> [n for n in dir(greetings) if not n.startswith("_")]
   ['DEFAULT_LANGUAGE', 'greet', 'supported_languages']
   >>> greetings.DEFAULT_LANGUAGE = "en"     # attribute អាចកែប្រែបាន
   >>> greetings.greet("សុខា")
   'Hello, សុខា!'

.. note::

   ឈ្មោះដែលចាប់ផ្ដើមដោយ underscore ត្រូវបានចាត់ទុកជា **ផ្ទៃក្នុង**។
   នៅក្នុងឧទាហរណ៍ខាងលើ ``_TRANSLATIONS`` មិនលេចឡើងក្នុង ``dir()``
   ព្រោះយើងត្រងវាចេញ — ប៉ុន្តែវានៅតែអាចចូលដំណើរការបាន។
   នេះគឺជា **អនុសញ្ញា** មិនមែនការហាមឃាត់ទេ។

.. _main-guard:

``if __name__ == "__main__":``
==============================

Python កំណត់អថេរ ``__name__`` ដោយស្វ័យប្រវត្តិ៖

.. list-table::
   :header-rows: 1
   :widths: 40 60

   * - របៀបដំណើរការ
     - តម្លៃ ``__name__``
   * - ``python3 greetings.py`` (ដំណើរការផ្ទាល់)
     - ``"__main__"``
   * - ``import greetings`` (នាំចូល)
     - ``"greetings"``

នេះអនុញ្ញាតឱ្យឯកសារមួយដំណើរការជា **កម្មវិធី** ផង និងជា **បណ្ណាល័យ**
ផង៖

.. code-block:: python

   # greetings.py
   def greet(name, lang=None):
       word = _TRANSLATIONS.get(lang or DEFAULT_LANGUAGE, _TRANSLATIONS["en"])
       return f"{word}, {name}!"


   def _self_test():
       assert greet("សុខា") == "សួស្ដី, សុខា!"
       print("self-test passed")


   if __name__ == "__main__":
       # ដំណើរការតែពេលចាក់ `python3 greetings.py` ប៉ុណ្ណោះ
       _self_test()
       print(greet("ពិភពលោក"))

.. code-block:: console

   $ python3 greetings.py
   self-test passed
   សួស្ដី, ពិភពលោក!

.. tip::

   **ដាក់ការពារនេះជានិច្ច** ក្នុងឯកសារដែលអាចដំណើរការបានទាំងពីរយ៉ាង។
   បើគ្មានវា កូដសាកល្បងរបស់អ្នកនឹងដំណើរការរាល់ពេលដែលមានអ្នក
   ``import`` module នោះ។

.. _sys-path:

Module Search Path (``sys.path``)
=====================================

នៅពេលអ្នក ``import x`` Python ស្វែងរក ``x`` តាមលំដាប់នេះ៖

#. Module ដែលមានស្រាប់ក្នុង ``sys.modules`` (cache)
#. Built-in module (បង្កប់ក្នុង interpreter)
#. ថតនីមួយៗក្នុង ``sys.path``៖

   a. ថតដែលមាន script ដែលកំពុងដំណើរការ (ឬថតបច្ចុប្បន្នក្នុង REPL)
   b. អថេរបរិស្ថាន ``PYTHONPATH``
   c. ថតលំនាំដើមនៃការដំឡើង Python

.. code-block:: pycon

   >>> import sys
   >>> isinstance(sys.path, list)      # បញ្ជីនៃខ្សែអក្សរ (ផ្លូវថត)
   True
   >>> len(sys.path) > 1
   True
   >>> sys.path.append("/tmp/my_libs") # អាចបន្ថែមដោយផ្ទាល់ (មិនណែនាំ)
   >>> "/tmp/my_libs" in sys.path
   True

.. warning::

   កុំកែ ``sys.path`` ក្នុងកូដកម្មវិធី លើកលែងតែចាំបាច់ពិតប្រាកដ។
   វិធីល្អជាងគឺ៖

   * ដាក់ project របស់អ្នកជា **package** ដែលអាចដំឡើងបាន
     (មាន ``pyproject.toml``) ហើយដំឡើងជា editable
     (``pip install -e .``)
   * ប្រើ **virtual environment**
   * កំណត់ ``PYTHONPATH`` ក្នុងបរិស្ថាន មិនមែនក្នុងកូដ

.. _pycache:

``__pycache__`` — Compiled Modules
==================================

Python បកប្រែកូដប្រភពទៅជា **bytecode** ហើយរក្សាទុកវាក្នុងថត
``__pycache__`` ជាឯកសារ ``.pyc`` ដើម្បីឱ្យការនាំចូលលើកក្រោយលឿន៖

.. code-block:: text

   project/
   ├── greetings.py
   └── __pycache__/
       └── greetings.cpython-315.pyc

* ឈ្មោះមានលេខកំណែ (``cpython-315``) ដូច្នេះ Python កំណែផ្សេងគ្នា
  អាចនៅជាមួយគ្នាបាន។
* Python ពិនិត្យ **ម៉ោងកែប្រែ** នៃឯកសារប្រភព។ បើឯកសារប្រភពថ្មីជាង
  វាបកប្រែឡើងវិញដោយស្វ័យប្រវត្តិ។
* ``.pyc`` ធ្វើឱ្យការ **នាំចូល** លឿន ប៉ុន្តែមិនធ្វើឱ្យកម្មវិធី **ដំណើរការ**
  លឿនទេ។

.. tip::

   ដាក់ ``__pycache__/`` ក្នុង ``.gitignore``។ កុំ commit វា។

.. _dir-function:

អនុគមន៍ ``dir()``
=================

``dir()`` រាយឈ្មោះដែល module កំណត់៖

.. code-block:: pycon

   >>> import greetings
   >>> [n for n in dir(greetings) if not n.startswith("_")]
   ['DEFAULT_LANGUAGE', 'greet', 'supported_languages']
   >>> "_TRANSLATIONS" in dir(greetings)      # ឈ្មោះផ្ទៃក្នុងក៏នៅតែមាន
   True
   >>> "__file__" in dir(greetings)           # attribute ពិសេសរបស់ module
   True

   >>> "greetings" in dir()           # dir() គ្មាន argument = namespace បច្ចុប្បន្ន
   True

   >>> import builtins
   >>> len(dir(builtins)) > 150       # ឈ្មោះ built-in ទាំងអស់
   True

.. list-table:: ឧបករណ៍ស្វែងយល់ module
   :header-rows: 1
   :widths: 30 70

   * - ឧបករណ៍
     - ការប្រើប្រាស់
   * - ``dir(mod)``
     - រាយឈ្មោះទាំងអស់
   * - ``mod.__doc__``
     - docstring របស់ module
   * - ``mod.__file__``
     - ផ្លូវឯកសារប្រភព
   * - ``vars(mod)``
     - namespace ជា ``dict``
   * - ``help(mod)``
     - ឯកសារពេញលេញ
   * - ``inspect.getsource(mod.fn)``
     - កូដប្រភពនៃអនុគមន៍
   * - ``mod.__all__``
     - ឈ្មោះសាធារណៈដែលកំណត់ដោយអ្នកសរសេរ (បើមាន)

----

.. _packages:

Packages
========

**Package** គឺជា module ដែលមានរចនាសម្ព័ន្ធ — វាជា **ថត** ដែលមាន
ឯកសារ ``__init__.py``។

.. code-block:: text

   shop/                          ← package កម្រិតខ្ពស់
   ├── __init__.py
   ├── cart.py                    ← module
   ├── models/                    ← sub-package
   │   ├── __init__.py
   │   ├── product.py
   │   └── order.py
   └── payments/
       ├── __init__.py
       ├── stripe_provider.py
       └── tests/
           ├── __init__.py
           └── test_stripe.py

* ``__init__.py`` ធ្វើឱ្យ Python ចាត់ទុកថតនោះជា package។
  វាអាច **ទទេ** ក៏បាន។
* ``__init__.py`` ដំណើរការនៅពេល package ត្រូវបាននាំចូល។
* ``models`` និង ``payments`` គឺជា **sub-package**។

.. _package-imports:

ការនាំចូលពី Package
--------------------

.. code-block:: python

   # នាំចូល module ពេញលេញ
   import shop.models.product
   shop.models.product.Product("សៀវភៅ", 12.5)

   # នាំចូលធាតុជាក់លាក់
   from shop.models.product import Product
   Product("សៀវភៅ", 12.5)

   # នាំចូល module ពី package
   from shop.models import product
   product.Product("សៀវភៅ", 12.5)

   # ជាមួយ alias
   from shop.payments import stripe_provider as stripe

.. note::

   ``import shop.models.product`` ដំណើរការ ``shop/__init__.py``,
   ``shop/models/__init__.py`` **និង** ``shop/models/product.py`` តាមលំដាប់។

.. _init-py:

តួនាទីរបស់ ``__init__.py``
---------------------------

វាអាចធ្វើបានបីយ៉ាង៖

**១. ទទេ** — គ្រាន់តែសម្គាល់ថតជា package៖

.. code-block:: python

   # shop/__init__.py  (ទទេ)

**២. លើកកម្ពស់ API សាមញ្ញ** — ដើម្បីឱ្យអ្នកប្រើមិនចាំបាច់វាយផ្លូវវែង៖

.. code-block:: python
   :no-test:

   # shop/__init__.py
   """បណ្ណាល័យហាងលក់ទំនិញអនឡាញ។"""

   from .cart import Cart
   from .models.product import Product
   from .models.order import Order

   __all__ = ["Cart", "Product", "Order"]
   __version__ = "1.4.0"

ឥឡូវអ្នកប្រើអាចសរសេរ៖

.. code-block:: python

   from shop import Cart, Product        # ខ្លី ជាជាង
   # from shop.models.product import Product

**៣. ធ្វើការកំណត់រចនាសម្ព័ន្ធ** — ប៉ុន្តែចៀសវាងកូដធ្ងន់ៗ ព្រោះវាដំណើរការ
រាល់ពេលនាំចូល។

.. warning::

   កុំដាក់កូដដែលមាន **side effect** ធ្ងន់ធ្ងរ (ភ្ជាប់ database, ហៅ API,
   អានឯកសារធំ) ក្នុង ``__init__.py``។ វានឹងដំណើរការរាល់ពេលដែលមានអ្នក
   ``import`` អ្វីមួយពី package នោះ។

.. _relative-imports:

Relative Import
===============

នៅ **ក្នុង** package អ្នកអាចប្រើចុចដើម្បីយោងទៅ module ជិតខាង៖

.. list-table::
   :header-rows: 1
   :widths: 24 76

   * - វាក្យសម្ពន្ធ
     - អត្ថន័យ
   * - ``from . import x``
     - module ``x`` ក្នុង package បច្ចុប្បន្ន
   * - ``from .mod import y``
     - ``y`` ពី ``mod`` ក្នុង package បច្ចុប្បន្ន
   * - ``from .. import z``
     - ``z`` ពី package **មេ**
   * - ``from ..other import w``
     - ``w`` ពី ``other`` ក្នុង package មេ
   * - ``from ...deep import v``
     - ឡើងបីកម្រិត (កម្រប្រើ — ស្មុគស្មាញពេក)

.. code-block:: python
   :no-test:

   # shop/payments/stripe_provider.py
   from ..models.order import Order        # absolute សម្រាប់ cross-package
   from . import config                    # relative សម្រាប់ module ជិតខាង

.. important::

   Relative import **ដំណើរការតែក្នុង package** ប៉ុណ្ណោះ។ បើអ្នកដំណើរការ
   ឯកសារដោយផ្ទាល់ (``python3 stripe_provider.py``) អ្នកនឹងទទួល៖

   .. code-block:: text

      ImportError: attempted relative import with no known parent package

   ដំណោះស្រាយ៖ ដំណើរការជា module ពីឫស project៖
   ``python3 -m shop.payments.stripe_provider``

.. tip::

   សម្រាប់គម្រោងធំ ស្ទីលដែលណែនាំ (PEP 8) គឺប្រើ **absolute import**
   ជាលំនាំដើម ហើយប្រើ relative import តែនៅពេលវាធ្វើឱ្យកូដអានងាយជាង
   ពិតប្រាកដ។

.. _all-variable:

``__all__`` និង ``import *``
================================

``__all__`` គឺជាបញ្ជីឈ្មោះដែលកំណត់ថាអ្វីត្រូវបាននាំចេញនៅពេលមាន
``from package import *``៖

.. code-block:: python
   :no-test:

   # shop/models/__init__.py
   from .product import Product
   from .order import Order
   from .product import _internal_helper     # ផ្ទៃក្នុង

   __all__ = ["Product", "Order"]            # មិនរួម _internal_helper

.. code-block:: pycon

   >>> from shop.models import *
   >>> Product          # ✅ មាន
   <class 'shop.models.product.Product'>
   >>> _internal_helper # ❌ មិនត្រូវបាននាំចេញ
   Traceback (most recent call last):
     ...
   NameError: name '_internal_helper' is not defined

``__all__`` ក៏ជា **ឯកសារ** នៃ API សាធារណៈរបស់ package ផងដែរ —
ឧបករណ៍ lint និង IDE ប្រើវា។

.. _namespace-packages:

Namespace Package
=================

បើថតមួយ **គ្មាន** ``__init__.py`` Python 3.3+ នៅតែអាចនាំចូលវាជា
*namespace package*។ វាអនុញ្ញាតឱ្យ package មួយរីករាលដាលលើថតច្រើន
(ឬ distribution ច្រើន)៖

.. code-block:: text

   /libs-a/shared/plugins/one.py      ← គ្មាន __init__.py ណាមួយ
   /libs-b/shared/plugins/two.py

.. code-block:: pycon
   :no-test:

   >>> import sys
   >>> sys.path[:0] = ["/libs-a", "/libs-b"]
   >>> import shared.plugins.one, shared.plugins.two
   >>> shared.plugins.__path__          # មានផ្លូវច្រើន
   _NamespacePath(['/libs-a/shared/plugins', '/libs-b/shared/plugins'])

.. note::

   សម្រាប់ package ធម្មតា សូមប្រើ ``__init__.py`` (regular package)។
   Namespace package មានប្រយោជន៍តែសម្រាប់ករណីពិសេសដូចជា plugin
   ecosystem ដែល distribution ផ្សេងគ្នាត្រូវចែករំលែក namespace តែមួយ។

.. _reloading:

ការផ្ទុក Module ឡើងវិញ
==========================

Python cache module ក្នុង ``sys.modules`` ដូច្នេះការកែឯកសារប្រភព
**មិន** មានឥទ្ធិពលលើ session ដែលកំពុងដំណើរការទេ។ ដើម្បីផ្ទុកឡើងវិញ៖

.. code-block:: pycon

   >>> import importlib, greetings
   >>> importlib.reload(greetings)
   <module 'greetings' from '.../greetings.py'>

.. warning::

   ``reload()`` មានគ្រោះថ្នាក់។ វាដំណើរការឯកសារឡើងវិញក្នុង namespace
   ដើម ប៉ុន្តែ **object ចាស់ដែលបាននាំចេញរួចហើយនៅតែចង្អុលទៅកំណែចាស់**៖

   .. code-block:: pycon

      >>> from greetings import greet      # ចាប់យកអនុគមន៍ចាស់
      >>> _ = importlib.reload(greetings)  # ផ្ទុកឡើងវិញ
      >>> greet("សុខា")                     # នៅតែប្រើកំណែចាស់!
      'សួស្ដី, សុខា!'

   កុំពឹងផ្អែកលើ ``reload()`` ក្នុងកូដផលិតកម្ម។ ចាប់ផ្ដើង interpreter
   ឡើងវិញវិញ ឬប្រើ auto-reload របស់ framework។

.. _circular-imports:

Circular Import
===============

កំហុសទូទៅបំផុតក្នុងការរៀបចំ module៖

.. code-block:: python
   :no-test:

   # a.py
   from b import helper_b
   def helper_a(): return "a"

.. code-block:: python
   :no-test:

   # b.py
   from a import helper_a          # ❌ ត្រឡប់ទៅ a វិញ
   def helper_b(): return "b"

.. code-block:: pycon
   :no-test:

   >>> import a
   Traceback (most recent call last):
     ...
   ImportError: cannot import name 'helper_a' from partially initialized module 'a' (most likely due to a circular import)

**វិធីដោះស្រាយ៖**

#. **រៀបចំរចនាសម្ព័ន្ធឡើងវិញ** — ដកកូដដែលចែករំលែកទៅ module ទីបី
   (ឧ. ``common.py``) ដែល ``a`` និង ``b`` ទាំងពីរនាំចូល។
#. **នាំចូលយឺត** — ផ្លាស់ទី ``import`` ទៅក្នុងអនុគមន៍៖

   .. code-block:: python

      # b.py
      def helper_b():
          from a import helper_a       # នាំចូលពេលហៅ មិនមែនពេលផ្ទុក
          return helper_a()

#. **ប្រើ type annotation ជាខ្សែអក្សរ** សម្រាប់បញ្ហាដែលកើតពី type hints តែប៉ុណ្ណោះ៖

   .. code-block:: python

      from __future__ import annotations   # ឬ ប្រើ "ClassName" ជាខ្សែអក្សរ

.. versionadded:: 3.15
   ``lazy import`` (PEP 810) ពន្យារការផ្ទុក module រហូតដល់ឈ្មោះត្រូវបាន
   ប្រើពិតប្រាកដ។ វាជួយកាត់បន្ថយពេលចាប់ផ្ដើម និងអាចដោះស្រាយ circular
   import ខ្លះបាន៖

   .. code-block:: python
      :no-test:

      lazy import numpy as np      # មិនផ្ទុក numpy ទេ រហូតដល់ np ត្រូវបានប្រើ

.. _modules-best-practices:

ការអនុវត្តល្អបំផុត
======================

#. **ដាក់ ``import`` នៅផ្នែកខាងលើ** នៃឯកសារ បន្ទាប់ពី module docstring។
#. **លំដាប់** (PEP 8)៖ (១) standard library (២) ភាគីទីបី (៣) កូដផ្ទៃក្នុង
   project។ ញែកក្រុមដោយបន្ទាត់ទទេ។
#. **មួយ module មួយបន្ទាត់** សម្រាប់ ``import``៖

   .. code-block:: python

      # ✅
      import os
      import sys

      # ❌ (អនុញ្ញាតសម្រាប់ from-import ប៉ុណ្ណោះ)
      import os, sys

#. **ប្រើឈ្មោះ module ពេញលេញ** ក្នុងកូដ លើកលែងតែឈ្មោះវែងពេក
   (``import numpy as np`` ជាអនុសញ្ញាទទួលស្គាល់)។
#. **កុំប្រើ ``import *``** ក្នុងកូដផលិតកម្ម។
#. **កំណត់ API សាធារណៈ** ដោយ ``__all__`` និង underscore សម្រាប់ផ្ទៃក្នុង។
#. **ចៀសវាង circular import** ដោយរចនា layering ច្បាស់លាស់។
#. **ដាក់ ``if __name__ == "__main__":``** សម្រាប់កូដដែលដំណើរការផ្ទាល់។
#. **Module តូចៗ ដែលមានទំនួលខុសត្រូវតែមួយ** ល្អជាង module ធំមួយ។

.. _modules-summary:

សង្ខេប
======

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - គោលគំនិត
     - សង្ខេប
   * - Module
     - ឯកសារ ``.py`` មួយ។ ``import x`` ដំណើរការវាម្ដង ហើយ cache ក្នុង ``sys.modules``
   * - Package
     - ថតដែលមាន ``__init__.py`` (ឬ namespace package ដែលគ្មាន)
   * - ``__name__``
     - ``"__main__"`` ពេលដំណើរការផ្ទាល់; ឈ្មោះ module ពេលនាំចូល
   * - ``__init__.py``
     - ដំណើរការពេល package ត្រូវបាននាំចូល។ អាចទទេ ឬលើកកម្ពស់ API
   * - ``__all__``
     - កំណត់ឈ្មោះសាធារណៈសម្រាប់ ``import *`` និងជាឯកសារ API
   * - ``sys.path``
     - លំដាប់ថតដែល Python ស្វែងរក module
   * - ``__pycache__``
     - bytecode cache។ ដាក់ក្នុង ``.gitignore``
   * - Relative import
     - ``from . import x`` — ដំណើរការតែក្នុង package
   * - ``importlib.reload``
     - ផ្ទុកឡើងវិញ — មានគ្រោះថ្នាក់ កុំប្រើក្នុងផលិតកម្ម

.. rubric:: ប្រភពយោង

* `Modules <https://docs.python.org/3/tutorial/modules.html>`_
* `The Import System <https://docs.python.org/3/reference/import.html>`_
* `sys — System-specific parameters and functions <https://docs.python.org/3/library/sys.html>`_
* `importlib — The implementation of import <https://docs.python.org/3/library/importlib.html>`_
* `PEP 8 — Imports <https://peps.python.org/pep-0008/#imports>`_
* `PEP 420 — Namespace Packages <https://peps.python.org/pep-0420/>`_
* `PEP 810 — Lazy Imports <https://peps.python.org/pep-0810/>`_
