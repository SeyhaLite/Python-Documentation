.. _syntax-variables-types:

.. container:: src-note

   ប្រភពដើម៖ CPython ``Doc/tutorial/introduction.rst``,
   ``Doc/reference/lexical_analysis.rst``, ``Doc/library/stdtypes.rst``,
   ``Doc/library/keyword.rst`` ·
   `ឯកសារផ្លូវការ <https://docs.python.org/3/library/stdtypes.html>`_

##########################################################
វាក្យសម្ពន្ធ អថេរ និងប្រភេទទិន្នន័យ
##########################################################

.. _comments:

អត្ថាធិប្បាយ (Comment)
=======================

សញ្ញា ``#`` ចាប់ផ្ដើមអត្ថាធិប្បាយ ហើយអ្វីៗពីក្រោយវារហូតដល់ចុងបន្ទាត់
ត្រូវបាន Python មិនអើពើ។ អត្ថាធិប្បាយអាចនៅលើបន្ទាត់ដាច់ដោយឡែក
ឬនៅចុងបន្ទាត់កូដ៖

.. code-block:: python

   # នេះជាអត្ថាធិប្បាយពេញមួយបន្ទាត់
   x = 5  # នេះជាអត្ថាធិប្បាយនៅចុងបន្ទាត់

   print(x)  # បោះពុម្ព 5

.. note::

   Python **មិនមាន** អត្ថាធិប្បាយច្រើនបន្ទាត់ដូច ``/* ... */`` របស់ C ទេ។
   អ្នកត្រូវដាក់ ``#`` នៅមុខបន្ទាត់នីមួយៗ។ ខ្សែអក្សរដែលដាក់ដោយខ្លួនឯង
   (``"""..."""``) ក៏មិនអើពើដោយ interpreter ដែរ ហើយជួនកាលត្រូវបាន
   ប្រើជាអត្ថាធិប្បាយច្រើនបន្ទាត់ ប៉ុន្តែគោលបំណងពិតរបស់វាគឺជា
   *docstring* (មើលជំពូក :doc:`functions_scope`)។

.. _indentation:

Indentation និង Block
=====================

ភាសាភាគច្រើនប្រើវង់ក្រចកដង្កៀប ``{}`` ឬពាក្យ ``begin``/``end`` ដើម្បី
បង្រួបបង្រួមបន្ទាត់កូដជា block។ Python ប្រើ **indentation** វិញ។

បន្ទាត់ដែលបញ្ចប់ដោយសញ្ញាពីរគូស ``:`` (ដូចជា ``if``, ``for``, ``while``,
``def``, ``class``, ``with``, ``try``) បើក block មួយ ហើយបន្ទាត់ទាំងអស់
ដែលចូលក្រោមវាជាផ្នែកនៃ block នោះ៖

.. code-block:: python

   age = 20

   if age >= 18:
       print("ពេញវ័យ")        # ចូល ៤ ដកឃ្លា — ក្នុង block
       print("អាចបោះឆ្នោត")   # ក្នុង block ដូចគ្នា
   print("ចប់")                # មិនចូល — ក្រៅ block ដំណើរការជានិច្ច

លទ្ធផល៖

.. code-block:: text

   ពេញវ័យ
   អាចបោះឆ្នោត
   ចប់

ច្បាប់សំខាន់៖

* បន្ទាត់ទាំងអស់ក្នុង block តែមួយត្រូវមាន **កម្រិតចូលដូចគ្នា**។
* ស្តង់ដារ `PEP 8 <https://peps.python.org/pep-0008/>`_ ណែនាំឱ្យប្រើ
  **space ៤** ក្នុងមួយកម្រិត។
* កុំលាយឡំ tab និង space។ បើលាយ Python នឹងបញ្ចេញ ``TabError``។

.. _statements:

Statement និងការបំបែកបន្ទាត់
================================

ជាធម្មតា មួយ statement ស្ថិតលើមួយបន្ទាត់។ ប៉ុន្តែអ្នកអាចបន្ត statement
ទៅបន្ទាត់ថ្មីបានពីរវិធី៖

**១. បន្តដោយស្វ័យប្រវត្តិក្នុងវង់ក្រចក** — ណែនាំបំផុត៖

.. code-block:: python

   total = (1 + 2 + 3 +
            4 + 5 + 6)

   names = [
       "សុខា",
       "ដារ៉ា",
       "សុភា",
   ]

**២. ប្រើ backslash** ``\`` នៅចុងបន្ទាត់៖

.. code-block:: python

   if age >= 18 and \
      age <= 65:
       print("វ័យធ្វើការ")

.. warning::

   កុំដាក់អត្ថាធិប្បាយក្រោយ backslash — វានឹងបណ្ដាលឱ្យមាន
   ``SyntaxError``។ ហើយកុំមានដកឃ្លាទទេក្រោយ backslash ដែរ។

អ្នកក៏អាចដាក់ statement ច្រើនលើបន្ទាត់តែមួយដោយប្រើ ``;`` ប៉ុន្តែ
វាមិនត្រូវបានណែនាំទេ ព្រោះអានពិបាក៖

.. code-block:: python

   x = 1; y = 2; print(x + y)   # ដំណើរការ ប៉ុន្តែមិនស្អាត

.. _identifiers:

អត្តសញ្ញាណ (Identifier) និងពាក្យគន្លឹះ
==========================================

**អត្តសញ្ញាណ** គឺជាឈ្មោះដែលអ្នកដាក់ឱ្យអថេរ អនុគមន៍ class ឬ module។
ច្បាប់៖

* ចាប់ផ្ដើមដោយអក្សរ (``a``–``z``, ``A``–``Z`` ឬអក្សរ Unicode ដូចជាអក្សរខ្មែរ)
  ឬសញ្ញា underscore ``_``។
* បន្ទាប់មកអាចជាអក្សរ លេខ (``0``–``9``) ឬ ``_``។
* មិនអាចចាប់ផ្ដើមដោយលេខ។
* មិនអាចជាពាក្យគន្លឹះ។
* Case-sensitive៖ ``age``, ``Age`` និង ``AGE`` ជាអត្តសញ្ញាណបីផ្សេងគ្នា។

.. code-block:: pycon

   >>> user_name = "sokha"     # ត្រឹមត្រូវ
   >>> _private = 42           # ត្រឹមត្រូវ
   >>> ឈ្មោះ = "សុភា"          # ត្រឹមត្រូវ — Python 3 អនុញ្ញាត Unicode

   >>> 2nd_place = "silver"    # ❌ ចាប់ផ្ដើមដោយលេខ
     File "<stdin>", line 1
       ...
   SyntaxError: invalid decimal literal

.. tip::

   ទោះបី Python 3 អនុញ្ញាតឱ្យប្រើអក្សរខ្មែរជាឈ្មោះអថេរក៏ដោយ
   សូមប្រើ **ឈ្មោះជាអង់គ្លេស** សម្រាប់អត្តសញ្ញាណ។ ឧបករណ៍ជាច្រើន
   (formatter, linter, library ខាងក្រៅ) សន្មតថាឈ្មោះជា ASCII ហើយ
   កូដរបស់អ្នកនឹងចែករំលែកជាមួយអ្នកដទៃបានងាយជាង។ ប្រើខ្សែអក្សរខ្មែរ
   សម្រាប់ **ទិន្នន័យ** និង **អត្ថាធិប្បាយ** វិញ។

.. _keywords:

ពាក្យគន្លឹះ (Keyword)
---------------------

ពាក្យគន្លឹះគឺជាពាក្យបម្រុងរបស់ភាសា — អ្នកមិនអាចប្រើវាជាឈ្មោះអថេរបានទេ។
Python 3.15 មានពាក្យគន្លឹះ **៣៥**៖

.. code-block:: text

   False   None    True    and     as      assert  async   await
   break   class   continue        def     del     elif    else
   except  finally for     from    global  if      import  in
   is      lambda  nonlocal        not     or      pass    raise
   return  try     while   with    yield

អ្នកអាចពិនិត្យបញ្ជីនេះដោយខ្លួនឯង៖

.. code-block:: pycon

   >>> import keyword
   >>> len(keyword.kwlist)
   35
   >>> keyword.iskeyword("class")
   True
   >>> keyword.iskeyword("classy")
   False

.. _soft-keywords:

Soft Keyword
~~~~~~~~~~~~

មានពាក្យមួយចំនួនដែលជាពាក្យគន្លឹះ **តែក្នុងបរិបទជាក់លាក់** ប៉ុណ្ណោះ។
នៅកន្លែងផ្សេងវានៅតែអាចប្រើជាឈ្មោះអថេរបាន។ នៅក្នុង Python 3.15
ពួកវាគឺ ``_``, ``case``, ``lazy``, ``match`` និង ``type``៖

.. code-block:: pycon

   >>> import keyword
   >>> keyword.softkwlist
   ['_', 'case', 'lazy', 'match', 'type']

   >>> match = "ការប្រកួត"      # ត្រឹមត្រូវ — 'match' ជាអថេរធម្មតានៅទីនេះ
   >>> print(match)
   ការប្រកួត

.. versionadded:: 3.10
   ``match`` និង ``case`` ត្រូវបានបន្ថែមសម្រាប់ *structural pattern matching*
   (មើលជំពូក :doc:`control_flow`)។

.. versionadded:: 3.12
   ``type`` ត្រូវបានបន្ថែមសម្រាប់ពាក្យបញ្ជា ``type X = ...`` (type alias)។

.. versionadded:: 3.15
   ``lazy`` ត្រូវបានបន្ថែមសម្រាប់ ``lazy import`` (PEP 810) ដែលពន្យារ
   ការផ្ទុកម៉ូឌុលរហូតដល់វាត្រូវបានប្រើពិតប្រាកដ។

.. _naming-conventions:

អនុសញ្ញាក្នុងការដាក់ឈ្មោះ
---------------------------

.. list-table:: ស្ទីលឈ្មោះតាម PEP 8
   :header-rows: 1
   :widths: 24 26 50

   * - ស្ទីល
     - ឧទាហរណ៍
     - ប្រើសម្រាប់
   * - ``snake_case``
     - ``user_name``, ``total_price``
     - អថេរ និងអនុគមន៍ (លំនាំដើម)
   * - ``PascalCase``
     - ``BankAccount``, ``HttpClient``
     - ឈ្មោះ class
   * - ``UPPER_CASE``
     - ``MAX_SIZE``, ``API_URL``
     - ថេរ (constant) កម្រិត module
   * - ``_leading_underscore``
     - ``_cache``
     - ធាតុផ្ទៃក្នុង (internal) — អនុសញ្ញា មិនមែនការហាមឃាត់
   * - ``__double_leading``
     - ``__secret``
     - ក្នុង class បង្កើត *name mangling*
   * - ``__dunder__``
     - ``__init__``, ``__name__``
     - ឈ្មោះពិសេសដែល Python កំណត់ទុក — កុំបង្កើតថ្មីដោយខ្លួនឯង

.. warning::

   កុំដាក់ឈ្មោះអថេរដូចឈ្មោះ built-in។ បើអ្នកសរសេរ ``list = [1, 2]``
   អ្នកនឹងបាត់បង់ function ``list()`` ក្នុង scope នោះ ហើយកូដបន្ទាប់
   ``list("abc")`` នឹងបញ្ចេញ ``TypeError``។ ចៀសវាងឈ្មោះដូចជា ``list``,
   ``dict``, ``set``, ``str``, ``int``, ``type``, ``id``, ``input``, ``sum``,
   ``format``, ``file``។

.. _variables:

អថេរ និងការផ្ដល់តម្លៃ (Assignment)
======================================

នៅក្នុង Python អ្នកមិន **ប្រកាស** អថេរទេ — អ្នកគ្រាន់តែ **ផ្ដល់តម្លៃ** ឱ្យវា។
អថេរកើតឡើងភ្លាមៗនៅពេលផ្ដល់តម្លៃដំបូង។

.. code-block:: python

   city = "ភ្នំពេញ"      # str
   population = 2_281_951  # int  (សញ្ញា _ ធ្វើឱ្យលេខអានងាយ)
   area_km2 = 679.0       # float
   is_capital = True      # bool
   mayor = None           # NoneType

   print(city, population, area_km2, is_capital, mayor)

លទ្ធផល៖

.. code-block:: text

   ភ្នំពេញ 2281951 679.0 True None

.. _dynamic-typing:

Dynamic Typing
--------------

អថេរមិនមានប្រភេទជាប់ជាមួយវាទេ — **object** ទេដែលមានប្រភេទ។ អថេរគ្រាន់តែ
ជាឈ្មោះដែលចង្អុលទៅ object មួយ។ ដូច្នេះអ្នកអាចផ្ដល់តម្លៃប្រភេទផ្សេងទៅ
អថេរដដែលបាន៖

.. code-block:: pycon

   >>> value = 100        # ចង្អុលទៅ int
   >>> type(value)
   <class 'int'>
   >>> value = "១០០"       # ឥឡូវចង្អុលទៅ str
   >>> type(value)
   <class 'str'>
   >>> value = [1, 2, 3]  # ឥឡូវចង្អុលទៅ list
   >>> type(value)
   <class 'list'>

ការដែលគ្មានការត្រួតពិនិត្យប្រភេទនៅពេលសរសេរ (compile time) ធ្វើឱ្យ Python
រហ័សក្នុងការសរសេរ ប៉ុន្តែកំហុសប្រភេទនឹងលេចឡើង **នៅពេលដំណើរការ**
(runtime) វិញ៖

.. code-block:: pycon

   >>> "1" + 1
   Traceback (most recent call last):
     ...
   TypeError: can only concatenate str (not "int") to str

.. _multiple-assignment:

ការផ្ដល់តម្លៃច្រើនក្នុងពេលតែមួយ
-----------------------------------

.. code-block:: pycon

   >>> x, y, z = 1, 2, 3          # ផ្ដល់តម្លៃ ៣ ក្នុងពេលតែមួយ
   >>> a = b = c = 0              # តម្លៃដូចគ្នាទៅអថេរច្រើន

   >>> x, y = y, x                # ប្ដូរតម្លៃគ្នា (swap) ដោយមិនចាំបាច់អថេរជំនួយ
   >>> x, y
   (2, 1)

   >>> first, *rest = [10, 20, 30, 40]   # unpacking ជាមួយ *
   >>> first
   10
   >>> rest
   [20, 30, 40]

.. _augmented-assignment:

Augmented Assignment
--------------------

.. list-table::
   :header-rows: 1
   :widths: 18 42 40

   * - ប្រមាណវិធី
     - មានន័យថា
     - ឧទាហរណ៍
   * - ``x += n``
     - ``x = x + n``
     - ``total += 5``
   * - ``x -= n``
     - ``x = x - n``
     - ``balance -= 100``
   * - ``x *= n``
     - ``x = x * n``
     - ``count *= 2``
   * - ``x /= n``
     - ``x = x / n`` (តែងតែ ``float``)
     - ``avg /= 3``
   * - ``x //= n``
     - ``x = x // n`` (ចែកយកផ្នែកគត់)
     - ``n //= 2``
   * - ``x %= n``
     - ``x = x % n`` (សំណល់)
     - ``i %= 10``
   * - ``x **= n``
     - ``x = x ** n`` (ស្វ័យគុណ)
     - ``area **= 2``

.. warning::

   ``x += 1`` **មិនមែន** ដូចគ្នាទាំងស្រុងទេសម្រាប់ object *mutable*។
   សម្រាប់ ``list`` ប្រតិបត្តិការ ``+=`` កែប្រែ list ដើមនៅនឹងកន្លែង
   (in-place) តាម ``list.extend()`` មិនមែនបង្កើត list ថ្មីទេ៖

   .. code-block:: pycon

      >>> a = [1, 2]
      >>> b = a
      >>> a += [3]        # កែប្រែ list ដើម
      >>> b
      [1, 2, 3]

      >>> a = [1, 2]
      >>> b = a
      >>> a = a + [3]     # បង្កើត list ថ្មី ហើយ a ចង្អុលទៅវា
      >>> b
      [1, 2]

.. _type-checking:

ការពិនិត្យប្រភេទ
====================

.. code-block:: pycon

   >>> type(42)
   <class 'int'>
   >>> type(3.14)
   <class 'float'>
   >>> type("Python")
   <class 'str'>
   >>> type(True)
   <class 'bool'>
   >>> type(None)
   <class 'NoneType'>
   >>> type([1, 2])
   <class 'list'>
   >>> type((1, 2))
   <class 'tuple'>
   >>> type({"a": 1})
   <class 'dict'>
   >>> type({1, 2})
   <class 'set'>

ប្រើ ``isinstance()`` ដើម្បីពិនិត្យ — វាល្អជាង ``type()`` ព្រោះវាគោរព
inheritance៖

.. code-block:: pycon

   >>> isinstance(42, int)
   True
   >>> isinstance(True, int)      # bool គឺជា subclass នៃ int
   True
   >>> isinstance(42, (int, float))   # ពិនិត្យច្រើនប្រភេទក្នុងពេលតែមួយ
   True

.. note::

   ``isinstance(True, int)`` ត្រឡប់ ``True`` ព្រោះ ``bool`` គឺជា subclass
   នៃ ``int``។ នេះមានន័យថា ``True + True == 2``។ បើអ្នកចង់បែងចែកដាច់ខាត
   សូមពិនិត្យ ``isinstance(x, bool)`` ជាមុន។

.. _data-types:

ប្រភេទទិន្នន័យមូលដ្ឋាន
==========================

.. list-table:: ប្រភេទដែលប្រើញឹកញាប់
   :header-rows: 1
   :widths: 16 18 66

   * - ប្រភេទ
     - ឈ្មោះ class
     - ការពិពណ៌នា
   * - ចំនួនគត់
     - ``int``
     - ចំនួនគត់គ្មានដែនកំណត់ទំហំ (arbitrary precision)។ ឧ. ``0``, ``-7``, ``10**100``
   * - ចំនួនទសភាគ
     - ``float``
     - ចំនួនពិតតាមស្តង់ដារ IEEE 754 double precision។ ឧ. ``3.14``, ``1e-9``, ``-0.5``
   * - ចំនួនកុំផ្លិច
     - ``complex``
     - មានផ្នែកពិត និងផ្នែកនិម្មិត។ ឧ. ``3+4j``
   * - ប៊ូលីន
     - ``bool``
     - មានតែ ``True`` និង ``False``
   * - ខ្សែអក្សរ
     - ``str``
     - អត្ថបទ Unicode ដែល **មិនអាចកែប្រែ** (immutable)
   * - ទិន្នន័យ binary
     - ``bytes``
     - លំដាប់ byte ដែល immutable។ ឧ. ``b"hello"``
   * - ទទេ
     - ``NoneType``
     - មានតម្លៃតែមួយគត់គឺ ``None``
   * - បញ្ជី
     - ``list``
     - លំដាប់ដែល **អាចកែប្រែ** (mutable)។ ឧ. ``[1, 2, 3]``
   * - ទុប
     - ``tuple``
     - លំដាប់ដែល immutable។ ឧ. ``(1, 2, 3)``
   * - សំណុំ
     - ``set``
     - ធាតុមិនស្ទួនគ្នា គ្មានលំដាប់។ ឧ. ``{1, 2, 3}``
   * - វចនានុក្រម
     - ``dict``
     - គូ key–value។ ឧ. ``{"name": "Sokha"}``

.. _int:

ចំនួនគត់ (``int``)
------------------

Python ``int`` មិនមានដែនកំណត់ទំហំទេ — វាអាចធំប៉ុណ្ណាក៏បាន
(គ្រាន់តែកំណត់ដោយអង្គចងចាំរបស់ម៉ាស៊ីន)៖

.. code-block:: pycon

   >>> 2 ** 100
   1267650600228229401496703205376
   >>> len(str(2 ** 1000))    # លេខមាន ៣០២ ខ្ទង់
   302

សញ្ញា underscore ``_`` អាចប្រើជាទីបំបែកលេខ ដើម្បីងាយអាន
(Python មិនអើពើវាទេ)៖

.. code-block:: pycon

   >>> 1_000_000 == 1000000
   True
   >>> 0b1010          # binary
   10
   >>> 0o17            # octal
   15
   >>> 0xFF            # hexadecimal
   255

.. _float:

ចំនួនទសភាគ (``float``) និងកំហុសនៃភាពជាក់លាក់
---------------------------------------------

``float`` ក្នុង Python គឺជា IEEE 754 double precision (៦៤ bit)។ វាមិនអាច
តំណាងចំនួនទសភាគមួយចំនួនបានត្រឹមត្រូវទេ ព្រោះកុំព្យូទ័រប្រើប្រព័ន្ធ
គោលពីរ៖

.. code-block:: pycon

   >>> 0.1 + 0.2
   0.30000000000000004
   >>> 0.1 + 0.2 == 0.3
   False

**នេះមិនមែនជាកំហុសរបស់ Python ទេ** — ភាសាដែលប្រើ IEEE 754 ទាំងអស់
មានបញ្ហានេះ។ វិធីដោះស្រាយ៖

.. code-block:: pycon

   >>> # ១. ប្រៀបធៀបដោយមានភាពអត់ធ្មត់
   >>> abs((0.1 + 0.2) - 0.3) < 1e-9
   True

   >>> # ២. ប្រើ math.isclose() — ណែនាំបំផុត
   >>> import math
   >>> math.isclose(0.1 + 0.2, 0.3)
   True

   >>> # ៣. សម្រាប់លុយ ប្រើ decimal
   >>> from decimal import Decimal
   >>> Decimal("0.1") + Decimal("0.2")
   Decimal('0.3')

   >>> # ៤. សម្រាប់ប្រភាគពិតប្រាកដ ប្រើ fractions
   >>> from fractions import Fraction
   >>> Fraction(1, 10) + Fraction(2, 10)
   Fraction(3, 10)

.. warning::

   កុំប្រើ ``float`` សម្រាប់ **លុយ**។ ប្រើ ``decimal.Decimal`` ឬរក្សាទុក
   ជាចំនួនគត់នៃ *សេន*។ កំហុសបង្គត់តូចៗអាចកើនឡើងក្នុងការគណនាច្រើន។

   ចំណាំថា ``Decimal("0.1")`` (ពីខ្សែអក្សរ) ត្រឹមត្រូវ ប៉ុន្តែ
   ``Decimal(0.1)`` (ពី float) នឹងផ្ទុកកំហុសបង្គត់ដែលមានស្រាប់។

``float`` ក៏មានតម្លៃពិសេស៖

.. code-block:: pycon

   >>> float("inf"), float("-inf")
   (inf, -inf)
   >>> float("nan") == float("nan")     # NaN មិនស្មើខ្លួនឯងទេ!
   False
   >>> math.isnan(float("nan"))
   True
   >>> 1.0 / 0
   Traceback (most recent call last):
     ...
   ZeroDivisionError: division by zero

.. _arithmetic:

ប្រមាណវិធីគណនា
---------------

.. list-table::
   :header-rows: 1
   :widths: 14 30 24 32

   * - ប្រមាណវិធី
     - ឈ្មោះ
     - ឧទាហរណ៍
     - លទ្ធផល
   * - ``+``
     - បូក
     - ``7 + 2``
     - ``9``
   * - ``-``
     - ដក
     - ``7 - 2``
     - ``5``
   * - ``*``
     - គុណ
     - ``7 * 2``
     - ``14``
   * - ``/``
     - ចែក (តែងតែ ``float``)
     - ``7 / 2``
     - ``3.5``
   * - ``//``
     - ចែកយកផ្នែកគត់ (floor)
     - ``7 // 2``
     - ``3``
   * - ``%``
     - សំណល់ (modulo)
     - ``7 % 2``
     - ``1``
   * - ``**``
     - ស្វ័យគុណ
     - ``7 ** 2``
     - ``49``
   * - ``divmod()``
     - ផ្នែកគត់ និងសំណល់ក្នុងពេលតែមួយ
     - ``divmod(7, 2)``
     - ``(3, 1)``

.. code-block:: pycon

   >>> 7 / 2       # ចែកធម្មតា — តែងតែ float
   3.5
   >>> 7 // 2      # floor division
   3
   >>> -7 // 2     # floor ទៅរកចំនួនតូចជាង (មិនមែនទៅរកសូន្យទេ)
   -4
   >>> 7 // -2
   -4
   >>> -7 % 2      # សំណល់មានសញ្ញាតាមភាគបែង
   1
   >>> divmod(-7, 2)
   (-4, 1)
   >>> 2 ** 0.5    # ស្វ័យគុណទសភាគ = ឫសការ៉េ
   1.4142135623730951

.. note::

   ``//`` គឺ **floor** division — វាបង្គត់ចុះក្រោមជានិច្ច មិនមែនបង្គត់ទៅរកសូន្យ
   ទេ។ ដូច្នេះ ``-7 // 2 == -4`` មិនមែន ``-3``។ បើអ្នកចង់បាន
   truncation ទៅរកសូន្យ ប្រើ ``int(-7 / 2)`` ឬ ``math.trunc()``។

.. _precedence:

លំដាប់អាទិភាពប្រមាណវិធី
-----------------------

ពី **ទាប** ទៅ **ខ្ពស់**៖

.. list-table::
   :header-rows: 1
   :widths: 12 88

   * - អាទិភាព
     - ប្រមាណវិធី
   * - ១ (ទាបបំផុត)
     - ``lambda``
   * - ២
     - ``if – else`` (conditional expression)
   * - ៣
     - ``or``
   * - ៤
     - ``and``
   * - ៥
     - ``not x``
   * - ៦
     - ``in``, ``not in``, ``is``, ``is not``, ``<``, ``<=``, ``>``, ``>=``, ``!=``, ``==``
   * - ៧
     - ``|`` (bitwise OR)
   * - ៨
     - ``^`` (bitwise XOR)
   * - ៩
     - ``&`` (bitwise AND)
   * - ១០
     - ``<<``, ``>>`` (bit shift)
   * - ១១
     - ``+``, ``-`` (បូក ដក)
   * - ១២
     - ``*``, ``@``, ``/``, ``//``, ``%``
   * - ១៣
     - ``+x``, ``-x``, ``~x`` (unary)
   * - ១៤
     - ``**`` (ស្វ័យគុណ)
   * - ១៥
     - ``await x``
   * - ១៦
     - ``x[i]``, ``x(...)``, ``x.attr`` (subscription, call, attribute)
   * - ១៧ (ខ្ពស់បំផុត)
     - ``( … )``, ``[ … ]``, ``{ … }`` (វង់ក្រចក តារាងលំដាប់ វចនានុក្រម)

.. code-block:: pycon

   >>> 2 + 3 * 4          # គុណមុនបូក
   14
   >>> (2 + 3) * 4        # វង់ក្រចកបង្ខំលំដាប់
   20
   >>> 2 ** 3 ** 2        # ** ភ្ជាប់ពីស្ដាំទៅឆ្វេង
   512
   >>> -2 ** 2            # unary - មានអាទិភាពទាបជាង **
   -4
   >>> (-2) ** 2
   4
   >>> 2 * 3 % 4          # * និង % អាទិភាពស្មើគ្នា → ពីឆ្វេងទៅស្ដាំ
   2

.. tip::

   បើអ្នកសង្ស័យ **ដាក់វង់ក្រចក**។ វាមិនផ្លាស់ប្ដូរលទ្ធផលទេ ប៉ុន្តែធ្វើឱ្យ
   ចេតនាច្បាស់លាស់សម្រាប់អ្នកអាន។

.. _bool-and-truthiness:

``bool`` និងភាពពិត (Truthiness)
===============================

``bool`` មានតម្លៃតែពីរប៉ុណ្ណោះគឺ ``True`` និង ``False`` (ចាប់ផ្ដើមដោយ
អក្សរធំ)។

.. code-block:: pycon

   >>> 5 > 3
   True
   >>> 5 < 3
   False
   >>> bool(1)
   True
   >>> bool(0)
   False

.. _truth-table:

តារាងតម្លៃ Falsy និង Truthy
---------------------------

Object ខាងក្រោមត្រូវបានចាត់ទុកថា **falsy** (មិនពិត) នៅពេលប្រើក្នុងលក្ខខណ្ឌ៖

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Falsy
     - ការពន្យល់
   * - ``False``
     - តម្លៃ bool មិនពិត
   * - ``None``
     - គ្មានតម្លៃ
   * - ``0``, ``0.0``, ``0j``
     - សូន្យនៃប្រភេទលេខនីមួយៗ
   * - ``""``
     - ខ្សែអក្សរទទេ
   * - ``()``, ``[]``, ``{}``, ``set()``
     - លំដាប់ ឬសំណុំទទេ
   * - ``range(0)``
     - ជួរទទេ

អ្វីៗក្រៅពីនេះគឺ **truthy**។

.. code-block:: pycon

   >>> bool("")
   False
   >>> bool(" ")          # មានដកឃ្លាមួយ → មិនទទេទេ
   True
   >>> bool([])
   False
   >>> bool([0])          # មានធាតុមួយ → truthy ទោះជាធាតុនោះជា 0
   True
   >>> bool(None)
   False

នេះធ្វើឱ្យអាចសរសេរលក្ខខណ្ឌខ្លី៖

.. code-block:: python

   items = []

   # វែង — មិនចាំបាច់
   if len(items) > 0:
       print("មានធាតុ")

   # ខ្លី — Pythonic
   if items:
       print("មានធាតុ")
   else:
       print("ទទេ")

.. warning::

   ប្រុងប្រយ័ត្នពេលពិនិត្យលេខ។ ``if x:`` នឹង **មិនដំណើរការ** បើ ``x == 0``
   ទោះបីជា ``x`` មានតម្លៃត្រឹមត្រូវក៏ដោយ។ សម្រាប់លេខ សូមប្រើ
   ``if x is not None:`` ឬ ``if x != 0:`` ឱ្យច្បាស់លាស់។

.. _none:

``None``
========

``None`` គឺជា object តែមួយគត់នៃប្រភេទ ``NoneType``។ វាមានន័យថា
"គ្មានតម្លៃ" ឬ "មិនបានកំណត់"។

.. code-block:: pycon

   >>> x = None
   >>> print(x)
   None
   >>> x is None          # វិធីត្រឹមត្រូវដើម្បីពិនិត្យ None
   True
   >>> x == None          # ដំណើរការដែរ ប៉ុន្តែមិនត្រូវបានណែនាំ
   True

   >>> def no_return():
   ...     pass
   ...
   >>> print(no_return())   # អនុគមន៍គ្មាន return ត្រឡប់ None
   None

.. important::

   ប្រើ ``is None`` ឬ ``is not None`` ជានិច្ច — **កុំ** ប្រើ ``== None``។
   ``is`` ពិនិត្យអត្តសញ្ញាណ object ដែលត្រឹមត្រូវ និងលឿនជាង ហើយ
   PEP 8 ណែនាំវាជាផ្លូវការ។

.. _type-conversion:

ការបំលែងប្រភេទ (Type Conversion)
================================

.. list-table:: អនុគមន៍បំលែងប្រភេទ
   :header-rows: 1
   :widths: 20 40 40

   * - អនុគមន៍
     - បំលែងទៅ
     - ឧទាហរណ៍ និងលទ្ធផល
   * - ``int(x)``
     - ``int``
     - ``int("42")`` → ``42`` · ``int(3.99)`` → ``3`` (truncate ទៅសូន្យ)
   * - ``float(x)``
     - ``float``
     - ``float("3.5")`` → ``3.5`` · ``float(7)`` → ``7.0``
   * - ``str(x)``
     - ``str``
     - ``str(42)`` → ``"42"`` · ``str(None)`` → ``"None"``
   * - ``bool(x)``
     - ``bool``
     - ``bool("")`` → ``False`` · ``bool("0")`` → ``True``
   * - ``list(x)``
     - ``list``
     - ``list("abc")`` → ``['a', 'b', 'c']``
   * - ``tuple(x)``
     - ``tuple``
     - ``tuple([1, 2])`` → ``(1, 2)``
   * - ``set(x)``
     - ``set``
     - ``set("aab")`` → ``{'a', 'b'}``
   * - ``dict(x)``
     - ``dict``
     - ``dict([("a", 1)])`` → ``{'a': 1}``
   * - ``chr(n)``
     - តួអក្សរពី code point
     - ``chr(65)`` → ``'A'``
   * - ``ord(c)``
     - code point ពីតួអក្សរ
     - ``ord('A')`` → ``65``
   * - ``bin(n)`` / ``oct(n)`` / ``hex(n)``
     - ខ្សែអក្សរជាទម្រង់ប្រព័ន្ធលេខ
     - ``hex(255)`` → ``'0xff'``
   * - ``round(x, n)``
     - បង្គត់ទៅ ``n`` ខ្ទង់
     - ``round(3.14159, 2)`` → ``3.14``

.. code-block:: pycon

   >>> int("123")
   123
   >>> int("12.5")        # មិនអាច — មានចុចទសភាគ
   Traceback (most recent call last):
     ...
   ValueError: invalid literal for int() with base 10: '12.5'
   >>> int(float("12.5")) # បំលែងពីរដំណាក់កាល
   12
   >>> int("ff", 16)      # បញ្ជាក់ប្រព័ន្ធលេខជាគោល (base)
   255

.. note::

   ``round()`` ប្រើ **banker's rounding** (round-half-to-even) មិនមែន
   round-half-up ដែលអ្នករំពឹងទេ៖

   .. code-block:: pycon

      >>> round(0.5)
      0
      >>> round(1.5)
      2
      >>> round(2.5)
      2

.. _mutability:

Mutable និង Immutable
=====================

នេះគឺជាគំនិតសំខាន់បំផុតមួយក្នុង Python។

.. list-table::
   :header-rows: 1
   :widths: 50 50

   * - **Immutable** (មិនអាចកែប្រែ)
     - **Mutable** (អាចកែប្រែ)
   * - ``int``, ``float``, ``complex``, ``bool``
     - ``list``
   * - ``str``, ``bytes``
     - ``dict``
   * - ``tuple``, ``frozenset``
     - ``set``
   * - ``None``
     - ``bytearray`` វត្ថុ custom ភាគច្រើន

**Immutable** — object មិនអាចប្រែប្រួលបានទេ។ "ការកែប្រែ" គឺជាការបង្កើត
object ថ្មី៖

.. code-block:: pycon

   >>> s = "abc"
   >>> s[0] = "z"          # មិនអនុញ្ញាត
   Traceback (most recent call last):
     ...
   TypeError: 'str' object does not support item assignment
   >>> s = s + "d"         # បង្កើតខ្សែអក្សរថ្មី ហើយ s ចង្អុលទៅវា
   >>> s
   'abcd'

**Mutable** — object អាចកែប្រែនៅនឹងកន្លែង៖

.. code-block:: pycon

   >>> lst = [1, 2, 3]
   >>> lst[0] = 99          # កែប្រែផ្ទាល់
   >>> lst
   [99, 2, 3]
   >>> lst.append(4)
   >>> lst
   [99, 2, 3, 4]

.. _references:

អថេរគឺជាឈ្មោះ មិនមែនជាប្រអប់ទេ
--------------------------------------

ការផ្ដល់តម្លៃមិន **ចម្លង** object ទេ — វាគ្រាន់តែបង្កើតឈ្មោះថ្មីដែលចង្អុល
ទៅ object **ដដែល**៖

.. code-block:: pycon

   >>> a = [1, 2, 3]
   >>> b = a                # b និង a ចង្អុលទៅ list តែមួយ
   >>> b.append(4)
   >>> a                    # a ក៏ផ្លាស់ប្ដូរដែរ!
   [1, 2, 3, 4]
   >>> a is b
   True

ដើម្បីចម្លងពិតប្រាកដ៖

.. code-block:: pycon

   >>> a = [1, 2, 3]
   >>> b = a.copy()         # ឬ a[:] ឬ list(a)
   >>> b.append(4)
   >>> a
   [1, 2, 3]
   >>> b
   [1, 2, 3, 4]

សម្រាប់ object ដែលមាន nested structure ប្រើ ``copy.deepcopy()``៖

.. code-block:: pycon

   >>> import copy
   >>> a = [[1, 2], [3, 4]]
   >>> shallow = a.copy()
   >>> deep = copy.deepcopy(a)
   >>> a[0].append(99)
   >>> shallow[0]           # shallow copy ចម្លងតែកម្រិតខាងក្រៅ
   [1, 2, 99]
   >>> deep[0]              # deep copy ចម្លងគ្រប់កម្រិត
   [1, 2]

.. _identity-vs-equality:

``is`` ធៀបនឹង ``==``
---------------------

.. list-table::
   :header-rows: 1
   :widths: 18 42 40

   * - ប្រមាណវិធី
     - ពិនិត្យអ្វី
     - ប្រើពេលណា
   * - ``==``
     - **តម្លៃ** ស្មើគ្នាឬទេ (ស្មើភាព)
     - ភាគច្រើនគ្រប់ករណី
   * - ``!=``
     - តម្លៃមិនស្មើគ្នា
     - ភាគច្រើនគ្រប់ករណី
   * - ``is``
     - **អត្តសញ្ញាណ** — object តែមួយឬទេ
     - តែជាមួយ ``None`` និង *sentinel*
   * - ``is not``
     - object ផ្សេងគ្នា
     - ``if x is not None:``

.. code-block:: pycon

   >>> [1, 2] == [1, 2]     # តម្លៃដូចគ្នា
   True
   >>> [1, 2] is [1, 2]     # object ពីរផ្សេងគ្នា
   False
   >>> x = [1, 2]
   >>> y = x
   >>> y is x               # object តែមួយ
   True

.. warning::

   អ្នកអាចឃើញ ``256 is 256`` ត្រឡប់ ``True`` ខណៈ ``257 is 257``
   ត្រឡប់ ``False``។ នេះដោយសារ CPython ទុកចំនួនគត់តូចៗ (−5 ដល់ 256)
   ជាអចិន្ត្រៃយ៍។ **កុំពឹងផ្អែកលើឥរិយាបថនេះ** — វាជាការបង្កើនប្រសិទ្ធភាព
   នៃ implementation មិនមែនជាការធានាភាសាទេ។ ប្រើ ``==`` សម្រាប់តម្លៃ។

អ្នកអាចមើលអត្តសញ្ញាណ object ដោយ ``id()``៖

.. code-block:: pycon

   >>> x = [1, 2]
   >>> y = x
   >>> id(x) == id(y)
   True

.. _syntax-summary:

សង្ខេប
======

* Python ប្រើ **indentation** ដើម្បីកំណត់ block — ប្រើ space ៤។
* អថេរមិនចាំបាច់ប្រកាសប្រភេទទេ (**dynamic typing**)។
* អថេរគឺជា **ឈ្មោះ** ដែលចង្អុលទៅ object មិនមែនជាប្រអប់ផ្ទុកតម្លៃទេ។
* ប្រភេទ mutable (``list``, ``dict``, ``set``) អាចកែប្រែនៅនឹងកន្លែង;
  immutable (``int``, ``str``, ``tuple``) មិនអាច។
* ប្រើ ``==`` សម្រាប់តម្លៃ និង ``is`` សម្រាប់អត្តសញ្ញាណ (ជាពិសេស ``is None``)។
* ``float`` មានកំហុសបង្គត់ — ប្រើ ``math.isclose()`` ឬ ``Decimal``
  សម្រាប់លុយ។

.. rubric:: ប្រភពយោង

* `Built-in Types <https://docs.python.org/3/library/stdtypes.html>`_
* `Lexical analysis <https://docs.python.org/3/reference/lexical_analysis.html>`_
* `Floating Point Arithmetic: Issues and Limitations <https://docs.python.org/3/tutorial/floatingpoint.html>`_
* `PEP 8 — Style Guide for Python Code <https://peps.python.org/pep-0008/>`_
* `keyword — Testing for Python keywords <https://docs.python.org/3/library/keyword.html>`_
