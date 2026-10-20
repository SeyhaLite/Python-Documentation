.. _strings-collections:

.. container:: src-note

   ប្រភពដើម៖ CPython ``Doc/tutorial/datastructures.rst``,
   ``Doc/tutorial/introduction.rst`` (ផ្នែក Text),
   ``Doc/tutorial/inputoutput.rst`` (f-strings), ``Doc/library/stdtypes.rst`` ·
   `ឯកសារផ្លូវការ <https://docs.python.org/3/tutorial/datastructures.html>`_

###############################################
ខ្សែអក្សរ និងសំណុំទិន្នន័យ
###############################################

ជំពូកនេះគ្របដណ្ដប់ប្រភេទទិន្នន័យសំខាន់ៗបំផុតរបស់ Python ចំនួនប្រាំ៖
``str``, ``list``, ``tuple``, ``set`` និង ``dict``។

.. _str-type:

ខ្សែអក្សរ (``str``)
===================

``str`` គឺជាលំដាប់នៃតួអក្សរ Unicode ដែល **immutable**។

.. _str-creating:

ការបង្កើតខ្សែអក្សរ
----------------------

.. code-block:: python

   single = 'ខ្ញុំប្រើសញ្ញាសម្រង់ទោល'
   double = "ខ្ញុំប្រើសញ្ញាសម្រង់ពីរ"

   # ខ្សែអក្សរច្រើនបន្ទាត់
   triple_double = """បន្ទាត់ទីមួយ
   បន្ទាត់ទីពីរ"""

   # មានសញ្ញាសម្រង់ក្នុងខ្សែអក្សរ
   quote_in = "គាត់និយាយថា 'សួស្ដី'"
   escaped  = 'គាត់និយាយថា \'សួស្ដី\''

.. note::

   សញ្ញាសម្រង់ទោល ``'`` និងពីរ ``"`` មានអត្ថន័យ **ដូចគ្នាទាំងស្រុង**។
   PEP 8 មិនកំណត់ជម្រើសទេ — សំខាន់គឺប្រើមួយប្រភេទ **ជាប់លាប់**
   ក្នុងគម្រោងរបស់អ្នក។

.. _str-escapes:

តួអក្សរពិសេស (Escape Sequence)
-------------------------------

.. list-table::
   :header-rows: 1
   :widths: 20 80

   * - Escape
     - អត្ថន័យ
   * - ``\n``
     - បន្ទាត់ថ្មី (newline)
   * - ``\t``
     - tab
   * - ``\\``
     - backslash ខ្លួនឯង
   * - ``\'``  ``\"``
     - សញ្ញាសម្រង់
   * - ``\r``
     - carriage return
   * - ``\x41``
     - តួអក្សរតាម hex byte (``'A'``)
   * - ``\u0041``
     - តួអក្សរតាម Unicode ១៦ bit (``'A'``)
   * - ``\U0001F600``
     - តួអក្សរតាម Unicode ៣២ bit (``'😀'``)

.. code-block:: pycon

   >>> print("បន្ទាត់១\nបន្ទាត់២")
   បន្ទាត់១
   បន្ទាត់២
   >>> print("C:\\Users\\sokha")     # backslash ពិតត្រូវដាក់ពីរ
   C:\Users\sokha

.. _raw-strings:

Raw String
~~~~~~~~~~

ដាក់ ``r`` នៅមុខសញ្ញាសម្រង់ ដើម្បីឱ្យ backslash ទាំងអស់ត្រូវបានចាត់ទុក
ជាតួអក្សរធម្មតា។ សំខាន់ណាស់សម្រាប់ *regular expression* និង path របស់ Windows៖

.. code-block:: pycon

   >>> print("C:\\Users\\sokha")
   C:\Users\sokha
   >>> print(r"C:\Users\sokha")
   C:\Users\sokha

   >>> import re
   >>> re.findall(r"\d+", "a1b22c333")    # គ្មាន r ត្រូវសរសេរ "\\d+"
   ['1', '22', '333']

.. _str-indexing:

Indexing និង Slicing
--------------------

ខ្សែអក្សរជា *sequence* ដូច្នេះអ្នកអាចចូលមើលតួអក្សរនីមួយៗបាន៖

.. code-block:: pycon

   >>> word = "Python"
   >>> word[0]        # តួអក្សរដំបូង
   'P'
   >>> word[5]        # តួអក្សរចុងក្រោយ
   'n'
   >>> word[-1]       # លេខអវិជ្ជមាន = រាប់ពីចុង
   'n'
   >>> word[-6]
   'P'
   >>> word[10]       # លើសដែន
   Traceback (most recent call last):
     ...
   IndexError: string index out of range

**Slicing** ប្រើទម្រង់ ``s[start:stop:step]`` ដែល ``stop`` **មិនរាប់បញ្ចូល**៖

.. code-block:: pycon

   >>> word = "Python"
   >>> word[0:2]      # ពី index 0 ដល់មុន 2
   'Py'
   >>> word[2:]       # ពី index 2 ដល់ចុង
   'thon'
   >>> word[:4]       # ពីដើមដល់មុន index 4
   'Pyth'
   >>> word[:]        # ចម្លងទាំងអស់
   'Python'
   >>> word[1:5:2]    # step = 2 (រំលងម្ដងមួយៗ)
   'yh'
   >>> word[::-1]     # ត្រឡប់ខ្សែអក្សរ
   'nohtyP'

.. tip::

   ចងចាំថា index ដំបូងនៃ slice ត្រូវបាន **រាប់បញ្ចូល** ហើយ index ទីពីរ
   **មិនរាប់បញ្ចូល**។ នេះធ្វើឱ្យ ``word[:i] + word[i:]`` ស្មើ ``word``
   ជានិច្ច។

.. _str-operations:

ប្រតិបត្តិការលើខ្សែអក្សរ
--------------------------

.. code-block:: pycon

   >>> "Py" + "thon"      # ភ្ជាប់ (concatenate)
   'Python'
   >>> "ab" * 3           # គុណ (repeat)
   'ababab'
   >>> len("Python")      # ប្រវែង
   6
   >>> "th" in "Python"   # ពិនិត្យវត្តមាន
   True
   >>> "xyz" not in "Python"
   True

.. warning::

   ``str`` គឺ immutable — អ្នក **មិនអាច** កែតួអក្សរណាមួយបានទេ៖

   .. code-block:: pycon

      >>> word = "Python"
      >>> word[0] = "J"
      Traceback (most recent call last):
        ...
      TypeError: 'str' object does not support item assignment

   បើចង់បានខ្សែអក្សរថ្មី ចូរបង្កើតមួយថ្មី៖ ``"J" + word[1:]`` → ``'Jython'``។

.. _str-methods:

Method សំខាន់ៗរបស់ ``str``
-----------------------------

.. list-table:: ការកែទម្រង់
   :header-rows: 1
   :widths: 28 72

   * - Method
     - លទ្ធផល
   * - ``upper()`` / ``lower()``
     - អក្សរធំទាំងអស់ / អក្សរតូចទាំងអស់
   * - ``capitalize()``
     - អក្សរធំតែតួដំបូង
   * - ``title()``
     - អក្សរធំដំបូងនៃពាក្យនីមួយៗ
   * - ``casefold()``
     - អក្សរតូចខ្លាំងជាង ``lower()`` សម្រាប់ប្រៀបធៀបភាសាអន្តរជាតិ
   * - ``swapcase()``
     - ប្ដូរអក្សរធំ↔តូច
   * - ``strip([chars])``
     - លុបដកឃ្លា (ឬតួអក្សរកំណត់) នៅសងខាង
   * - ``lstrip()`` / ``rstrip()``
     - លុបខាងឆ្វេង / ខាងស្ដាំ
   * - ``removeprefix(p)`` / ``removesuffix(s)``
     - លុបបុព្វបទ / អនុបទ បើមាន
   * - ``replace(old, new[, n])``
     - ជំនួសខ្សែអក្សររង
   * - ``center(w)``, ``ljust(w)``, ``rjust(w)``
     - តម្រឹមក្នុងទទឹង ``w``
   * - ``zfill(w)``
     - បំពេញសូន្យនៅខាងឆ្វេង
   * - ``expandtabs(n)``
     - បំលែង tab ទៅជាដកឃ្លា

.. code-block:: pycon

   >>> "  សុខា  ".strip()
   'សុខា'
   >>> "...សុខា...".strip(".")
   'សុខា'
   >>> "python".upper()
   'PYTHON'
   >>> "hello world".title()
   'Hello World'
   >>> "a-b-c".replace("-", "+")
   'a+b+c'
   >>> "a-b-c".replace("-", "+", 1)     # ជំនួសតែម្ដងដំបូង
   'a+b-c'
   >>> "file.txt".removesuffix(".txt")
   'file'
   >>> "https://x.com".removeprefix("https://")
   'x.com'
   >>> "42".zfill(5)
   '00042'

.. list-table:: ការស្វែងរក និងពិនិត្យ
   :header-rows: 1
   :widths: 28 72

   * - Method
     - លទ្ធផល
   * - ``find(sub[, start[, end]])``
     - index ដំបូងដែលរកឃើញ ឬ ``-1`` បើគ្មាន
   * - ``rfind(sub)``
     - index ចុងក្រោយ ឬ ``-1``
   * - ``index(sub)``
     - ដូច ``find()`` ប៉ុន្តែបញ្ចេញ ``ValueError`` បើរកមិនឃើញ
   * - ``count(sub)``
     - ចំនួនដងដែល ``sub`` លេចឡើង
   * - ``startswith(p)`` / ``endswith(s)``
     - ``True``/``False`` (អាចផ្ដល់ tuple នៃបុព្វបទ)
   * - ``isdigit()``
     - តួអក្សរទាំងអស់ជាលេខ (``0``–``9``)
   * - ``isnumeric()``
     - ជាតួអក្សរលេខនៃប្រព័ន្ធណាក៏បាន (រួមលេខខ្មែរ ``១២៣``)
   * - ``isalpha()``
     - ជាអក្សរទាំងអស់
   * - ``isalnum()``
     - ជាអក្សរ ឬលេខទាំងអស់
   * - ``isspace()``
     - ជាដកឃ្លាទាំងអស់
   * - ``isidentifier()``
     - អាចប្រើជាឈ្មោះអត្តសញ្ញាណ Python បាន

.. code-block:: pycon

   >>> "Python".find("th")
   2
   >>> "Python".find("z")
   -1
   >>> "banana".count("na")
   2
   >>> "banana".startswith(("ap", "ba"))    # ពិនិត្យច្រើនបុព្វបទ
   True
   >>> "123".isdigit()
   True
   >>> "12.3".isdigit()
   False
   >>> "១២៣".isnumeric()      # លេខខ្មែរ — isdigit() ក៏ True ដែរ
   True
   >>> "abc".isalpha()
   True
   >>> "សុខា".isalpha()       # ⚠ False — មើលចំណាំខាងក្រោម
   False

.. important::

   **``isalpha()`` មិនដំណើរការដូចការរំពឹងទុកលើអក្សរខ្មែរទេ។**

   ``isalpha()`` ត្រឡប់ ``True`` តែនៅពេល **គ្រប់តួអក្សរ** ស្ថិតក្នុង Unicode
   category ``L*`` (Letter)។ ប៉ុន្តែពាក្យខ្មែរផ្សំឡើងពី ព្យញ្ជនៈ (category
   ``Lo``) **បូកនឹងស្រៈ និងជើង** ដែលជា combining marks (category ``Mn``
   និង ``Mc``)។ ដូច្នេះវាត្រឡប់ ``False``៖

   .. code-block:: pycon

      >>> import unicodedata
      >>> for ch in "សុខា":
      ...     print(f"U+{ord(ch):04X} {unicodedata.category(ch)} {ch.isalpha()}")
      ...
      U+179F Lo True
      U+17BB Mn False
      U+1781 Lo True
      U+17B6 Mc False
      >>> "សុខា".isalnum()      # ក៏ False ដែរ
      False

   បើអ្នកត្រូវការផ្ទៀងផ្ទាត់អត្ថបទខ្មែរ សូមពិនិត្យ Unicode category ដោយផ្ទាល់
   ឬប្រើ regular expression ជាមួយជួរ code point ខ្មែរ (``\u1780-\u17FF``)៖

   .. code-block:: pycon

      >>> import re
      >>> bool(re.fullmatch(r"[\u1780-\u17FF]+", "សុខា"))
      True

.. warning::

   ``find()`` ត្រឡប់ ``-1`` បើរកមិនឃើញ — ដែលជា index ត្រឹមត្រូវមិនមែនទេ
   ប៉ុន្តែអាចបង្កើត bug ស្ងាត់បាន។ បើអ្នកចង់ឱ្យមានកំហុសលេចឡើងភ្លាម
   ប្រើ ``index()`` វិញ។

.. _split-join:

``split()`` និង ``join()``
~~~~~~~~~~~~~~~~~~~~~~~~~~

``split()`` បំបែកខ្សែអក្សរទៅជា ``list``។ ``join()`` ភ្ជាប់ ``list`` ត្រឡប់
ទៅជាខ្សែអក្សរវិញ៖

.. code-block:: pycon

   >>> "apple,banana,cherry".split(",")
   ['apple', 'banana', 'cherry']
   >>> "apple,banana,cherry".split(",", 1)     # បំបែកតែម្ដងដំបូង
   ['apple', 'banana,cherry']
   >>> "a b   c".split()      # គ្មាន argument = បំបែកតាមដកឃ្លាណាក៏បាន
   ['a', 'b', 'c']
   >>> "line1\nline2".splitlines()
   ['line1', 'line2']

   >>> ", ".join(['apple', 'banana', 'cherry'])
   'apple, banana, cherry'
   >>> "-".join("abc")        # ដំណើរការលើខ្សែអក្សរផងដែរ
   'a-b-c'

.. important::

   ``join()`` គឺជា **method របស់ខ្សែអក្សរដែលជាតួបំបែក** មិនមែនរបស់ list
   ទេ។ សរសេរ ``",".join(names)`` — កុំសរសេរ ``names.join(",")``។
   វិធីនេះលឿនជាងការបូកខ្សែអក្សរក្នុងរង្វិលជុំច្រើនដង ព្រោះ ``str`` ជា
   immutable។

.. _f-strings:

f-string — ការបង្កើតខ្សែអក្សរមានទម្រង់
--------------------------------------

**f-string** (formatted string literal) គឺជាវិធីណែនាំសម្រាប់បញ្ចូលតម្លៃ
ក្នុងខ្សែអក្សរ។ ដាក់ ``f`` នៅមុខសញ្ញាសម្រង់ រួចដាក់ expression ក្នុង
វង់ក្រចកដង្កៀប ``{}``៖

.. code-block:: pycon

   >>> name = "សុខា"
   >>> age = 25
   >>> f"{name} មានអាយុ {age} ឆ្នាំ"
   'សុខា មានអាយុ 25 ឆ្នាំ'
   >>> f"ឆ្នាំក្រោយគាត់នឹងមានអាយុ {age + 1}"     # expression ពេញលេញ
   'ឆ្នាំក្រោយគាត់នឹងមានអាយុ 26'
   >>> f"{name.upper()}"                                # ហៅ method
   'សុខា'

.. _format-spec:

Format Specification
~~~~~~~~~~~~~~~~~~~~

ទម្រង់ពេញលេញគឺ ``{expression:format_spec}``៖

.. list-table::
   :header-rows: 1
   :widths: 22 78

   * - Format
     - លទ្ធផល
   * - ``{x:.2f}``
     - ទសភាគ ២ ខ្ទង់ → ``3.14``
   * - ``{x:.0f}``
     - គ្មានទសភាគ → ``3``
   * - ``{x:10}``
     - ទទឹងអប្បបរមា ១០ តម្រឹមស្ដាំ (លំនាំដើម)
   * - ``{x:>10}``
     - តម្រឹមស្ដាំក្នុងទទឹង ១០
   * - ``{x:<10}``
     - តម្រឹមឆ្វេង
   * - ``{x:^10}``
     - តម្រឹមកណ្ដាល
   * - ``{x:0>8}``
     - បំពេញដោយ ``0`` នៅខាងឆ្វេង
   * - ``{n:,}``
     - បំបែកលេខដោយសញ្ញាក្បៀស → ``1,234,567``
   * - ``{n:_}``
     - បំបែកដោយ underscore → ``1_234_567``
   * - ``{x:%}``
     - ជាភាគរយ → ``85.000000%``
   * - ``{x:.1%}``
     - ភាគរយ ១ ខ្ទង់ → ``85.0%``
   * - ``{n:b}`` ``{n:o}`` ``{n:x}`` ``{n:X}``
     - binary / octal / hex តូច / hex ធំ
   * - ``{x=}``
     - បោះពុម្ពទាំង expression និងតម្លៃ (សម្រាប់ debug)
   * - ``{x!r}`` ``{x!s}`` ``{x!a}``
     - បំលែងតាម ``repr()`` / ``str()`` / ``ascii()``

.. code-block:: pycon

   >>> pi = 3.14159265
   >>> f"{pi:.3f}"
   '3.142'
   >>> f"{pi:>10.2f}|"
   '      3.14|'
   >>> f"{'left':<8}|"
   'left    |'
   >>> f"{'mid':^9}|"
   '   mid   |'
   >>> f"{1234567:,}"
   '1,234,567'
   >>> f"{0.856:.1%}"
   '85.6%'
   >>> f"{255:x} / {255:X} / {255:b}"
   'ff / FF / 11111111'
   >>> count = 7
   >>> f"{count=}"
   'count=7'

.. versionchanged:: 3.12
   f-string អាចមានវង់ក្រចកដង្កៀប nested បានច្រើន អាចប្រើសញ្ញាសម្រង់ដដែល
   ក្នុង expression ខាងក្នុង និងអាចមានអត្ថាធិប្បាយក្នុងវង់ក្រចកដង្កៀប។
   ឧទាហរណ៍ខាងក្រោម **មិនដំណើរការ** មុន Python 3.12៖

   .. code-block:: python

      songs = ["Take Me Home", "Shake It Off"]
      print(f"បទដែលខ្ញុំចូលចិត្ត: {", ".join(songs)}")

.. versionadded:: 3.8
   ទម្រង់ ``{x=}`` សម្រាប់ debug។

.. _other-formatting:

វិធី format ផ្សេងទៀត
~~~~~~~~~~~~~~~~~~~~

.. code-block:: pycon

   >>> # str.format() — មុន f-string
   >>> "{} មានអាយុ {} ឆ្នាំ".format("សុខា", 25)
   'សុខា មានអាយុ 25 ឆ្នាំ'
   >>> "{name} -> {value:.2f}".format(name="pi", value=3.14159)
   'pi -> 3.14'
   >>> "{0}-{1}-{0}".format("a", "b")      # អាចយោង index ម្ដងទៀត
   'a-b-a'

   >>> # % formatting — ចាស់បំផុត កុំប្រើក្នុងកូដថ្មី
   >>> "%s មានអាយុ %d ឆ្នាំ" % ("សុខា", 25)
   'សុខា មានអាយុ 25 ឆ្នាំ'

.. tip::

   ប្រើ **f-string** សម្រាប់កូដថ្មី។ វាខ្លីជាង លឿនជាង និងអានងាយជាង។
   រក្សាទុក ``str.format()`` សម្រាប់ពេលដែលអ្នកត្រូវការខ្សែអក្សរទម្រង់ដែល
   មិនស្គាល់ជាមុន (ឧ. ពីឯកសារកំណត់រចនាសម្ព័ន្ធ)។

.. _str-encoding:

Encoding និង ``bytes``
----------------------

``str`` គឺជាអត្ថបទ Unicode។ ``bytes`` គឺជាទិន្នន័យ binary ឆៅ។
អ្នកត្រូវ **encode** ដើម្បីទៅ bytes និង **decode** ដើម្បីត្រឡប់មក str៖

.. code-block:: pycon

   >>> text = "សួស្ដី"
   >>> raw = text.encode("utf-8")
   >>> raw
   b'\xe1\x9e\x9f\xe1\x9e\xbd\xe1\x9e\x9f\xe1\x9f\x92\xe1\x9e\x8a\xe1\x9e\xb8'
   >>> len(text), len(raw)        # ៦ តួអក្សរ ប៉ុន្តែ ១៨ byte
   (6, 18)
   >>> raw.decode("utf-8")
   'សួស្ដី'

.. warning::

   កំហុសទូទៅបំផុតក្នុងការអានឯកសារអក្សរខ្មែរគឺ **មិនបញ្ជាក់ encoding**។
   សូមប្រើ ``encoding="utf-8"`` ជានិច្ច (មើលជំពូក :doc:`file_handling`)។

----

.. _list-type:

បញ្ជី (``list``)
================

``list`` គឺជាលំដាប់ **mutable** ដែលអាចផ្ទុកធាតុប្រភេទផ្សេងៗគ្នាលាយឡំគ្នា។

.. _list-creating:

ការបង្កើត
-------------

.. code-block:: pycon

   >>> fruits = ["ចេក", "ស្វាយ", "ទុំរេន"]
   >>> numbers = [1, 2, 3, 4, 5]
   >>> mixed = [1, "ពីរ", 3.0, True, None]
   >>> empty = []
   >>> nested = [[1, 2], [3, 4]]
   >>> list("abc")            # ពី iterable
   ['a', 'b', 'c']
   >>> list(range(5))
   [0, 1, 2, 3, 4]

.. _list-access:

ការចូលមើល និងកែប្រែ
--------------------

.. code-block:: pycon

   >>> fruits = ["ចេក", "ស្វាយ", "ទុំរេន"]
   >>> fruits[0]
   'ចេក'
   >>> fruits[-1]
   'ទុំរេន'
   >>> fruits[0] = "ម្នាស់"        # កែប្រែបាន (mutable)
   >>> fruits
   ['ម្នាស់', 'ស្វាយ', 'ទុំរេន']
   >>> fruits[1:3] = ["ដូង", "ពោធិ៍សាត់"]   # ជំនួសផ្នែកមួយ
   >>> fruits
   ['ម្នាស់', 'ដូង', 'ពោធិ៍សាត់']
   >>> fruits[1:1] = ["ក្រូច"]      # បញ្ចូលដោយមិនជំនួស
   >>> fruits
   ['ម្នាស់', 'ក្រូច', 'ដូង', 'ពោធិ៍សាត់']
   >>> del fruits[0]                # លុបតាម index
   >>> fruits
   ['ក្រូច', 'ដូង', 'ពោធិ៍សាត់']

.. _list-methods:

Method របស់ ``list``
---------------------

.. list-table::
   :header-rows: 1
   :widths: 32 68

   * - Method
     - ការពិពណ៌នា
   * - ``append(x)``
     - បន្ថែមធាតុមួយនៅចុងបញ្ជី
   * - ``extend(iterable)``
     - បន្ថែមធាតុទាំងអស់នៃ iterable នៅចុងបញ្ជី
   * - ``insert(i, x)``
     - បញ្ចូល ``x`` នៅ index ``i``
   * - ``remove(x)``
     - លុបធាតុដំបូងដែលស្មើ ``x`` (``ValueError`` បើគ្មាន)
   * - ``pop([i])``
     - ដកធាតុនៅ index ``i`` ហើយត្រឡប់វា (លំនាំដើម: ធាតុចុងក្រោយ)
   * - ``clear()``
     - លុបធាតុទាំងអស់
   * - ``index(x[, start[, end]])``
     - index ដំបូងនៃ ``x``
   * - ``count(x)``
     - ចំនួនដងដែល ``x`` លេចឡើង
   * - ``sort(key=None, reverse=False)``
     - តម្រៀបនៅនឹងកន្លែង (in-place)
   * - ``reverse()``
     - ត្រឡប់លំដាប់នៅនឹងកន្លែង
   * - ``copy()``
     - ចម្លងរាក់ (shallow copy)

.. code-block:: pycon

   >>> a = [3, 1, 2]
   >>> a.append(4)
   >>> a
   [3, 1, 2, 4]
   >>> a.extend([5, 6])          # បន្ថែមធាតុនីមួយៗ
   >>> a
   [3, 1, 2, 4, 5, 6]
   >>> a.insert(0, 0)
   >>> a
   [0, 3, 1, 2, 4, 5, 6]
   >>> a.remove(0)
   >>> a.pop()                   # ដកធាតុចុងក្រោយ
   6
   >>> a.pop(0)                  # ដកធាតុដំបូង
   3
   >>> a
   [1, 2, 4, 5]
   >>> a.count(1)
   1
   >>> a.index(4)
   2

.. warning::

   ភាពខុសគ្នារវាង ``append()`` និង ``extend()``៖

   .. code-block:: pycon

      >>> a = [1, 2]
      >>> a.append([3, 4])     # បន្ថែម list ជា **ធាតុមួយ**
      >>> a
      [1, 2, [3, 4]]
      >>> b = [1, 2]
      >>> b.extend([3, 4])     # បន្ថែម **ធាតុទាំងអស់**
      >>> b
      [1, 2, 3, 4]

.. _list-sorting:

ការតម្រៀប
-------------

.. code-block:: pycon

   >>> nums = [5, 2, 9, 1]
   >>> nums.sort()               # កែប្រែ list ដើម ត្រឡប់ None
   >>> nums
   [1, 2, 5, 9]

   >>> nums = [5, 2, 9, 1]
   >>> sorted(nums)              # បង្កើត list ថ្មី ទុក list ដើមនៅដដែល
   [1, 2, 5, 9]
   >>> nums
   [5, 2, 9, 1]

   >>> sorted(nums, reverse=True)
   [9, 5, 2, 1]

   >>> words = ["banana", "apple", "cherry"]
   >>> sorted(words, key=len)    # តម្រៀបតាមប្រវែង
   ['apple', 'banana', 'cherry']

   >>> people = [("សុខា", 30), ("ដារ៉ា", 25)]
   >>> sorted(people, key=lambda p: p[1])
   [('ដារ៉ា', 25), ('សុខា', 30)]

.. important::

   ``list.sort()`` ត្រឡប់ ``None`` — វាកែប្រែ list នៅនឹងកន្លែង។
   កុំសរសេរ ``nums = nums.sort()`` ព្រោះអ្នកនឹងបាត់បញ្ជីរបស់អ្នក។
   ប្រើ ``sorted(nums)`` បើអ្នកចង់បាន list ថ្មី។

ការតម្រៀបគឺ **stable** — ធាតុដែលស្មើគ្នារក្សាលំដាប់ដើម។

.. _list-comprehensions:

List Comprehension
------------------

វិធីខ្លីដើម្បីបង្កើត list ថ្មីពី iterable មួយ៖

.. code-block:: python

   squares = [x ** 2 for x in range(10)]
   # ស្មើនឹង:
   squares = []
   for x in range(10):
       squares.append(x ** 2)

.. code-block:: pycon

   >>> [x ** 2 for x in range(6)]
   [0, 1, 4, 9, 16, 25]
   >>> [x for x in range(10) if x % 2 == 0]      # មានលក្ខខណ្ឌ
   [0, 2, 4, 6, 8]
   >>> [(x, y) for x in [1, 2] for y in ["a", "b"]]   # រង្វិលជុំច្រើន
   [(1, 'a'), (1, 'b'), (2, 'a'), (2, 'b')]
   >>> [x.strip() for x in ["  a  ", "b "]]
   ['a', 'b']

**Nested comprehension** — រាបស្មើ matrix៖

.. code-block:: pycon

   >>> matrix = [[1, 2, 3], [4, 5, 6]]
   >>> [n for row in matrix for n in row]
   [1, 2, 3, 4, 5, 6]
   >>> [[n for n in row] for row in matrix]     # ចម្លងរចនាសម្ព័ន្ធ
   [[1, 2, 3], [4, 5, 6]]

**ប្តូរជួរឈរ និងជួរដេក (transpose)** ដោយប្រើ ``zip()``៖

.. code-block:: pycon

   >>> matrix = [[1, 2, 3], [4, 5, 6]]
   >>> list(zip(*matrix, strict=True))
   [(1, 4), (2, 5), (3, 6)]

.. tip::

   ប្រើ comprehension សម្រាប់ការបំលែងសាមញ្ញប៉ុណ្ណោះ។ បើវាមានរង្វិលជុំ
   ច្រើនជាងពីរ ឬលក្ខខណ្ឌស្មុគស្មាញ សូមប្រើ ``for`` loop ធម្មតាវិញ —
   វាអានងាយជាង។

.. versionadded:: 3.10
   ``strict=True`` សម្រាប់ ``zip()`` ដែលបញ្ចេញ ``ValueError`` បើ iterable
   មានប្រវែងមិនស្មើគ្នា។ វាល្អជាងការបណ្ដោយឱ្យទិន្នន័យត្រូវបានកាត់ចោល
   ដោយស្ងាត់។

.. _list-stack-queue:

បញ្ជីជា Stack និង Queue
-------------------------

.. code-block:: pycon

   >>> # Stack — LIFO (Last In, First Out)
   >>> stack = [1, 2]
   >>> stack.append(3)      # push
   >>> stack
   [1, 2, 3]
   >>> stack.pop()          # pop
   3

សម្រាប់ **queue** (FIFO) ``list.pop(0)`` យឺតណាស់ ព្រោះវាត្រូវរុញធាតុ
ទាំងអស់។ ប្រើ ``collections.deque`` វិញ៖

.. code-block:: pycon

   >>> from collections import deque
   >>> queue = deque(["a", "b"])
   >>> queue.append("c")        # បន្ថែមនៅខាងស្ដាំ
   >>> queue.popleft()          # ដកពីខាងឆ្វេង — O(1)
   'a'
   >>> queue
   deque(['b', 'c'])

----

.. _tuple-type:

ទុប (``tuple``)
===============

``tuple`` គឺជាលំដាប់ **immutable**។ វាលឿនជាង ``list`` បន្តិច ហើយអាចប្រើ
ជា key នៃ ``dict`` បាន។

.. code-block:: pycon

   >>> point = (3, 4)
   >>> single = (5,)          # សំខាន់: ត្រូវមានក្បៀស!
   >>> not_tuple = (5)        # នេះគ្រាន់តែជាលេខ 5 ក្នុងវង់ក្រចក
   >>> empty = ()
   >>> no_parens = 1, 2, 3    # វង់ក្រចកមិនចាំបាច់ទេ — សញ្ញាក្បៀសសំខាន់ជាង
   >>> type(single), type(not_tuple)
   (<class 'tuple'>, <class 'int'>)

.. warning::

   ``(5)`` មិនមែនជា tuple ទេ — វាគ្រាន់តែជាលេខ ``5`` ដែលដាក់ក្នុងវង់ក្រចក។
   tuple មានធាតុតែមួយត្រូវសរសេរ ``(5,)`` ដោយមាន **ក្បៀស**។

.. _tuple-packing-unpacking:

Packing និង Unpacking
---------------------

.. code-block:: pycon

   >>> # Packing — ផ្គុំតម្លៃចូល tuple
   >>> t = "សុខា", 25, "ភ្នំពេញ"
   >>> t
   ('សុខា', 25, 'ភ្នំពេញ')

   >>> # Unpacking — បំបែកចេញទៅអថេរ
   >>> name, age, city = t
   >>> name
   'សុខា'

   >>> # Unpacking ជាមួយ * សម្រាប់ធាតុនៅសល់
   >>> first, *middle, last = [1, 2, 3, 4, 5]
   >>> first, middle, last
   (1, [2, 3, 4], 5)

   >>> # Unpacking ក្នុងការហៅអនុគមន៍
   >>> def add(a, b, c):
   ...     return a + b + c
   ...
   >>> args = (1, 2, 3)
   >>> add(*args)
   6

``tuple`` ត្រូវបានប្រើនៅគ្រប់ទីកន្លែងដែល Python ត្រូវការលំដាប់ថេរ៖

.. code-block:: pycon

   >>> # ត្រឡប់ច្រើនតម្លៃពីអនុគមន៍
   >>> def min_max(nums):
   ...     return min(nums), max(nums)      # tuple
   ...
   >>> lo, hi = min_max([3, 1, 4])
   >>> lo, hi
   (1, 4)

.. note::

   ទោះបី ``tuple`` ជា immutable ក៏ដោយ បើវាមានធាតុ mutable ខាងក្នុង
   ធាតុនោះនៅតែអាចកែប្រែបាន៖

   .. code-block:: pycon

      >>> t = ([1, 2], [3])
      >>> t[0].append(99)
      >>> t
      ([1, 2, 99], [3])

----

.. _set-type:

សំណុំ (``set``)
===============

``set`` គឺជាសំណុំនៃធាតុ **មិនស្ទួនគ្នា** គ្មានលំដាប់កំណត់។ វាល្អសម្រាប់
លុបធាតុស្ទួន និងធ្វើប្រតិបត្តិការសំណុំ។

.. code-block:: pycon

   >>> fruits = {"ចេក", "ស្វាយ", "ចេក"}      # ស្ទួនត្រូវបានលុបដោយស្វ័យប្រវត្តិ
   >>> sorted(fruits)                         # sorted() ដើម្បីឱ្យលទ្ធផលថេរ
   ['ចេក', 'ស្វាយ']
   >>> sorted(set("mississippi"))             # ពី iterable
   ['i', 'm', 'p', 's']
   >>> empty = set()                          # ⚠ {} បង្កើត dict ទទេ មិនមែន set
   >>> type({}), type(set())
   (<class 'dict'>, <class 'set'>)

.. important::

   ``{}`` បង្កើត **dict** ទទេ មិនមែន set ទទេទេ។ ដើម្បីបង្កើត set ទទេ
   ត្រូវប្រើ ``set()``។

.. _set-operations:

ប្រតិបត្តិការសំណុំ
--------------------

.. list-table::
   :header-rows: 1
   :widths: 22 18 60

   * - ប្រមាណវិធី
     - Method
     - អត្ថន័យ
   * - ``a | b``
     - ``a.union(b)``
     - ធាតុក្នុង ``a`` ឬ ``b`` ឬទាំងពីរ
   * - ``a & b``
     - ``a.intersection(b)``
     - ធាតុក្នុងទាំង ``a`` និង ``b``
   * - ``a - b``
     - ``a.difference(b)``
     - ធាតុក្នុង ``a`` ប៉ុន្តែមិនក្នុង ``b``
   * - ``a ^ b``
     - ``a.symmetric_difference(b)``
     - ធាតុក្នុងមួយ ប៉ុន្តែមិនក្នុងទាំងពីរ
   * - ``a <= b``
     - ``a.issubset(b)``
     - ``a`` ជាសំណុំរងរបស់ ``b``
   * - ``a < b``
     - —
     - ``a`` ជាសំណុំរងពិត (proper subset)
   * - ``a >= b``
     - ``a.issuperset(b)``
     - ``a`` ជាសំណុំមេរបស់ ``b``
   * - ``a == b``
     - —
     - មានធាតុដូចគ្នាទាំងស្រុង
   * - ``a.isdisjoint(b)``
     - —
     - គ្មានធាតុរួម

.. code-block:: pycon

   >>> a = {1, 2, 3, 4}
   >>> b = {3, 4, 5, 6}
   >>> a | b
   {1, 2, 3, 4, 5, 6}
   >>> a & b
   {3, 4}
   >>> a - b
   {1, 2}
   >>> a ^ b
   {1, 2, 5, 6}
   >>> {1, 2} <= {1, 2, 3}
   True
   >>> a.isdisjoint({7, 8})
   True

.. _set-methods:

Method របស់ ``set``
---------------------

.. code-block:: pycon

   >>> s = {1, 2}
   >>> s.add(3)              # បន្ថែមធាតុមួយ
   >>> s.update([4, 5])      # បន្ថែមច្រើនធាតុ
   >>> sorted(s)
   [1, 2, 3, 4, 5]
   >>> s.discard(99)         # លុប បើមិនមានក៏មិនបញ្ចេញកំហុស
   >>> s.remove(5)           # លុប — KeyError បើគ្មាន
   >>> sorted(s)
   [1, 2, 3, 4]
   >>> removed = s.pop()     # ដកធាតុណាមួយ (មិនមានលំដាប់កំណត់)
   >>> s.clear()
   >>> sorted(s)
   []

.. warning::

   ``set`` **គ្មានលំដាប់** ដូច្នេះ ``s.pop()`` ដកធាតុដែលមិនអាចទាយបាន
   ហើយការបោះពុម្ព ``set`` ផ្ទាល់អាចផ្ដល់លំដាប់ខុសគ្នារវាងការដំណើរការម្ដងៗ
   (ដោយសារ hash randomisation)។ នោះជាមូលហេតុដែលឧទាហរណ៍ខាងលើប្រើ
   ``sorted()``។
   បើអ្នកត្រូវការលំដាប់ ប្រើ ``list`` ឬ ``dict`` (ដែលរក្សាលំដាប់បញ្ចូល
   ចាប់ពី Python 3.7)។

ធាតុនៃ ``set`` ត្រូវតែជា **hashable**។ ``list`` និង ``dict`` មិនអាចជា
ធាតុ set បានទេ ប៉ុន្តែ ``tuple`` និង ``frozenset`` អាច៖

.. code-block:: pycon

   >>> {[1, 2]}
   Traceback (most recent call last):
     ...
   TypeError: cannot use 'list' as a set element (unhashable type: 'list')
   >>> {(1, 2)}
   {(1, 2)}
   >>> frozenset([1, 2])
   frozenset({1, 2})

**Set comprehension**៖

.. code-block:: pycon

   >>> sorted({x ** 2 for x in range(-3, 4)})
   [0, 1, 4, 9]
   >>> sorted({w.lower() for w in ["A", "b", "A"]})
   ['a', 'b']

----

.. _dict-type:

វចនានុក្រម (``dict``)
=====================

``dict`` ផ្ទុកគូ **key → value**។ ចាប់ពី Python 3.7 វារក្សា **លំដាប់បញ្ចូល**
ជានិច្ច។

.. _dict-creating:

ការបង្កើត
-------------

.. code-block:: pycon

   >>> person = {"name": "សុខា", "age": 25, "city": "ភ្នំពេញ"}
   >>> empty = {}
   >>> from_pairs = dict([("a", 1), ("b", 2)])
   >>> from_kwargs = dict(a=1, b=2)
   >>> fromkeys = dict.fromkeys(["x", "y"], 0)
   >>> fromkeys
   {'x': 0, 'y': 0}

.. important::

   key ត្រូវតែជា **immutable** និង **hashable** — ``str``, ``int``, ``float``,
   ``bool``, ``tuple`` (ដែលមានតែធាតុ immutable) ឬ ``frozenset``។
   ``list`` មិនអាចជា key បានទេ។

.. _dict-access:

ការចូលមើល និងកែប្រែ
--------------------

.. code-block:: pycon

   >>> person = {"name": "សុខា", "age": 25}
   >>> person["name"]                 # ចូលមើល
   'សុខា'
   >>> person["age"] = 26             # កែប្រែ
   >>> person["city"] = "ភ្នំពេញ"      # បន្ថែម key ថ្មី
   >>> person
   {'name': 'សុខា', 'age': 26, 'city': 'ភ្នំពេញ'}

   >>> person["phone"]                # key មិនមាន
   Traceback (most recent call last):
     ...
   KeyError: 'phone'

   >>> person.get("phone")            # ត្រឡប់ None ដោយសុវត្ថិភាព
   >>> person.get("phone", "មិនមាន")  # ឬតម្លៃលំនាំដើម
   'មិនមាន'

   >>> "name" in person               # ពិនិត្យវត្តមាន key
   True

.. tip::

   ប្រើ ``d.get(key, default)`` ជំនួស ``d[key]`` បើ key អាចមិនមាន។
   វាចៀសវាង ``KeyError`` ដោយមិនត្រូវការ ``try``/``except``។

.. _dict-methods:

Method របស់ ``dict``
---------------------

.. list-table::
   :header-rows: 1
   :widths: 32 68

   * - Method
     - ការពិពណ៌នា
   * - ``d.keys()``
     - view នៃ key ទាំងអស់
   * - ``d.values()``
     - view នៃ value ទាំងអស់
   * - ``d.items()``
     - view នៃគូ ``(key, value)`` ទាំងអស់
   * - ``d.get(k[, default])``
     - យក value ដោយសុវត្ថិភាព
   * - ``d.setdefault(k, default)``
     - យក value បើមាន; បើមិនមាន បញ្ចូល ``default`` រួចត្រឡប់វា
   * - ``d.update(other)``
     - បញ្ចូល/ជំនួសគូពី dict ឬ iterable ផ្សេង
   * - ``d.pop(k[, default])``
     - ដក key ចេញ ត្រឡប់ value
   * - ``d.popitem()``
     - ដកគូចុងក្រោយចេញ (LIFO)
   * - ``d.clear()``
     - លុបគូទាំងអស់
   * - ``d.copy()``
     - ចម្លងរាក់
   * - ``d | other``
     - បញ្ចូលគ្នាជា dict ថ្មី (Python 3.9+)
   * - ``d |= other``
     - បញ្ចូលគ្នានៅនឹងកន្លែង (Python 3.9+)

.. code-block:: pycon

   >>> d = {"a": 1, "b": 2}
   >>> list(d.keys())
   ['a', 'b']
   >>> list(d.values())
   [1, 2]
   >>> list(d.items())
   [('a', 1), ('b', 2)]
   >>> d.update({"b": 99, "c": 3})
   >>> d
   {'a': 1, 'b': 99, 'c': 3}
   >>> d.pop("c")
   3
   >>> d.pop("z", "គ្មាន")        # default ចៀសវាង KeyError
   'គ្មាន'

   >>> a = {"x": 1}
   >>> b = {"y": 2}
   >>> a | b                       # Python 3.9+
   {'x': 1, 'y': 2}
   >>> a |= {"x": 10}
   >>> a
   {'x': 10}

**``setdefault()``** មានប្រយោជន៍សម្រាប់បង្កើតរចនាសម្ព័ន្ធជាន់ៗ៖

.. code-block:: pycon

   >>> words = ["apple", "banana", "avocado", "blueberry"]
   >>> groups = {}
   >>> for w in words:
   ...     groups.setdefault(w[0], []).append(w)
   ...
   >>> groups
   {'a': ['apple', 'avocado'], 'b': ['banana', 'blueberry']}

សម្រាប់ករណីនេះ មានជម្រើសស្អាតជាងគឺ ``collections.defaultdict(list)``។

.. _dict-comprehension:

Dict Comprehension
------------------

.. code-block:: pycon

   >>> {x: x ** 2 for x in range(5)}
   {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
   >>> {v: k for k, v in {"a": 1, "b": 2}.items()}     # បញ្ច្រាស dict
   {1: 'a', 2: 'b'}
   >>> prices = {"apple": 1.5, "banana": 0.8}
   >>> {k: v * 1.1 for k, v in prices.items()}          # ដំឡើងថ្លៃ ១០%
   {'apple': 1.6500000000000001, 'banana': 0.8800000000000001}
   >>> {k: v for k, v in prices.items() if v > 1.0}     # ត្រង
   {'apple': 1.5}

----

.. _looping:

បច្ចេកទេសរង្វិលជុំ
==================

.. _looping-dict:

រង្វិលជុំលើ ``dict``
-----------------------

.. code-block:: pycon

   >>> person = {"name": "សុខា", "age": 25}
   >>> for key in person:                    # លំនាំដើម = key
   ...     print(key)
   ...
   name
   age
   >>> for key, value in person.items():     # ទាំង key និង value
   ...     print(f"{key} = {value}")
   ...
   name = សុខា
   age = 25

.. _enumerate:

``enumerate()`` — ទទួល index និងតម្លៃ
---------------------------------------

.. code-block:: pycon

   >>> fruits = ["ចេក", "ស្វាយ", "ទុំរេន"]
   >>> for i, fruit in enumerate(fruits):
   ...     print(i, fruit)
   ...
   0 ចេក
   1 ស្វាយ
   2 ទុំរេន
   >>> for i, fruit in enumerate(fruits, start=1):    # ចាប់ពី ១
   ...     print(f"{i}. {fruit}")
   ...
   1. ចេក
   2. ស្វាយ
   3. ទុំរេន

កុំសរសេររង្វិលជុំតាម index ដោយដៃ៖

.. code-block:: python

   # ❌ មិន Pythonic
   for i in range(len(fruits)):
       print(i, fruits[i])

   # ✅ Pythonic
   for i, fruit in enumerate(fruits):
       print(i, fruit)

.. _zip:

``zip()`` — ដើរលើលំដាប់ច្រើនក្នុងពេលតែមួយ
----------------------------------------------

.. code-block:: pycon

   >>> names = ["សុខា", "ដារ៉ា"]
   >>> ages = [25, 30]
   >>> for name, age in zip(names, ages):
   ...     print(f"{name}: {age}")
   ...
   សុខា: 25
   ដារ៉ា: 30

   >>> dict(zip(names, ages))       # បង្កើត dict ពី list ពីរ
   {'សុខា': 25, 'ដារ៉ា': 30}

.. warning::

   ``zip()`` ឈប់នៅពេលលំដាប់ **ខ្លីបំផុត** អស់។ បើប្រវែងមិនស្មើគ្នា
   ទិន្នន័យនឹងត្រូវកាត់ចោលដោយស្ងាត់។ ប្រើ ``strict=True`` ដើម្បីឱ្យ
   បញ្ចេញកំហុស៖

   .. code-block:: pycon

      >>> list(zip([1, 2, 3], ["a", "b"]))
      [(1, 'a'), (2, 'b')]
      >>> list(zip([1, 2, 3], ["a", "b"], strict=True))
      Traceback (most recent call last):
        ...
      ValueError: zip() argument 2 is shorter than argument 1

.. _sorted-reversed:

``sorted()`` និង ``reversed()``
-------------------------------

.. code-block:: pycon

   >>> nums = [3, 1, 2]
   >>> for n in sorted(nums):          # ត្រឡប់ list ថ្មីដែលបានតម្រៀប
   ...     print(n)
   ...
   1
   2
   3
   >>> for n in reversed(nums):        # ត្រឡប់ iterator មិនមែន list
   ...     print(n)
   ...
   2
   1
   3

----

.. _comparing:

ការប្រៀបធៀបលំដាប់
=================

Python អាចប្រៀបធៀបលំដាប់ (``list``, ``tuple``, ``str``) ដោយប្រើ
**lexicographical ordering** — ប្រៀបធៀបធាតុដំបូងដែលខុសគ្នា៖

.. code-block:: pycon

   >>> [1, 2, 3] < [1, 2, 4]
   True
   >>> "apple" < "banana"
   True
   >>> "Python" < "python"        # អក្សរធំមានតម្លៃ code point តូចជាង
   True
   >>> [1, 2] < [1, 2, 0]         # លំដាប់ខ្លីជាង មកមុន
   True
   >>> (1, 2, 3) == (1, 2, 3)
   True

ការប្រៀបធៀប **ខ្សែ** (chained comparison) ក៏ដំណើរការដែរ៖

.. code-block:: pycon

   >>> x = 5
   >>> 1 < x < 10          # ស្មើនឹង 1 < x and x < 10
   True
   >>> 1 < x > 10          # ស្មើនឹង 1 < x and x > 10
   False

----

.. _cheatsheet:

តារាងសង្ខេប — ជ្រើសរើសប្រភេទណា?
===============================

.. list-table::
   :header-rows: 1
   :widths: 14 14 12 14 46

   * - ប្រភេទ
     - Mutable?
     - លំដាប់?
     - ស្ទួនបាន?
     - ប្រើពេលណា
   * - ``list``
     - ✅ បាទ/ចាស
     - ✅ មាន
     - ✅ បាន
     - លំដាប់ទូទៅ ដែលត្រូវការបន្ថែម/លុប
   * - ``tuple``
     - ❌ ទេ
     - ✅ មាន
     - ✅ បាន
     - កំណត់ត្រា ឬលំដាប់ដែលមិនគួរផ្លាស់ប្ដូរ; ជា key នៃ dict
   * - ``set``
     - ✅ បាទ/ចាស
     - ❌ ទេ
     - ❌ ទេ
     - លុបធាតុស្ទួន; ស្វែងរកយ៉ាងលឿន; ប្រតិបត្តិការសំណុំ
   * - ``dict``
     - ✅ បាទ/ចាស
     - ✅ មាន (លំដាប់បញ្ចូល)
     - key មិនស្ទួន
     - ផ្គូផ្គង key → value
   * - ``str``
     - ❌ ទេ
     - ✅ មាន
     - ✅ បាន
     - អត្ថបទ

**ល្បឿនស្វែងរក** — ``x in container``៖

.. list-table::
   :header-rows: 1
   :widths: 25 25 50

   * - ប្រភេទ
     - ភាពស្មុគស្មាញ
     - ចំណាំ
   * - ``list``
     - O(n)
     - ស្កេនធាតុទាំងអស់
   * - ``set`` / ``frozenset``
     - O(1) ជាមធ្យម
     - hash lookup
   * - ``dict`` (ពិនិត្យ key)
     - O(1) ជាមធ្យម
     - hash lookup

.. tip::

   បើអ្នកត្រូវពិនិត្យវត្តមានធាតុច្រើនដង សូមបំលែង ``list`` ទៅ ``set``
   ជាមុន។ ការផ្លាស់ប្ដូរនេះអាចធ្វើឱ្យកម្មវិធីលឿនឡើងរាប់ពាន់ដង
   សម្រាប់ទិន្នន័យធំ។

.. rubric:: ប្រភពយោង

* `More on Lists <https://docs.python.org/3/tutorial/datastructures.html#more-on-lists>`_
* `Tuples and Sequences <https://docs.python.org/3/tutorial/datastructures.html#tuples-and-sequences>`_
* `Sets <https://docs.python.org/3/tutorial/datastructures.html#sets>`_
* `Dictionaries <https://docs.python.org/3/tutorial/datastructures.html#dictionaries>`_
* `Looping Techniques <https://docs.python.org/3/tutorial/datastructures.html#looping-techniques>`_
* `Formatted string literals <https://docs.python.org/3/tutorial/inputoutput.html#formatted-string-literals>`_
* `Text Sequence Type — str <https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str>`_
