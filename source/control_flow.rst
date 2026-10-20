.. _control-flow:

.. container:: src-note

   ប្រភពដើម៖ CPython ``Doc/tutorial/controlflow.rst`` (ផ្នែក ១–៦),
   ``Doc/reference/simple_stmts.rst``, ``Doc/reference/compound_stmts.rst`` ·
   `ឯកសារផ្លូវការ <https://docs.python.org/3/tutorial/controlflow.html>`_

####################################
លក្ខខណ្ឌ និងរង្វិលជុំ
####################################

*Control flow* គឺជារបៀបដែលកម្មវិធីសម្រេចចិត្តថាត្រូវដំណើរការកូដណាខ្លះ
និងដំណើរការម្ដងប៉ុន្មាន។ Python មានឧបករណ៍សំខាន់ពីរប្រភេទ៖
**លក្ខខណ្ឌ** (``if``, ``match``) និង **រង្វិលជុំ** (``for``, ``while``)។

.. _if-statement:

ពាក្យបញ្ជា ``if``
=================

.. code-block:: python

   temperature = 35

   if temperature > 30:
       print("ក្ដៅខ្លាំង")
   elif temperature > 20:
       print("ក្ដៅល្មម")
   elif temperature > 10:
       print("ត្រជាក់ល្មម")
   else:
       print("ត្រជាក់")

លទ្ធផល៖ ``ក្ដៅខ្លាំង``

ចំណុចសំខាន់៖

* ``elif`` គឺជាទម្រង់ខ្លីនៃ "else if"។ អ្នកអាចមាន ``elif`` ច្រើនតាមចិត្ត។
* ``elif`` ជំនួស ``switch``/``case`` របស់ភាសាផ្សេងៗ។
* ``else`` និង ``elif`` ទាំងអស់ **មិនចាំបាច់** ទេ។
* Python វាយតម្លៃលក្ខខណ្ឌ **ពីលើចុះក្រោម** ហើយដំណើរការតែមួយសាខា
  ដំបូងដែលពិត — សាខាផ្សេងទៀតទាំងអស់ត្រូវបានរំលង។

.. _truthiness-recap:

ភាពពិតក្នុងលក្ខខណ្ឌ
--------------------

លក្ខខណ្ឌមិនចាំបាច់ជា ``bool`` ទេ — object ណាក៏អាចប្រើបាន។ Python
បំលែងវាតាមច្បាប់ *truthiness*៖

.. code-block:: pycon

   >>> if []:
   ...     print("មិនដែលដំណើរការ")
   ...
   >>> if [0]:
   ...     print("ដំណើរការ — list មិនទទេ")
   ...
   ដំណើរការ — list មិនទទេ

Falsy រួមមាន៖ ``False``, ``None``, ``0``, ``0.0``, ``""``, ``()``, ``[]``,
``{}``, ``set()``, ``range(0)``។ អ្វីៗក្រៅពីនេះគឺ truthy។

.. warning::

   ``if x:`` ខុសពី ``if x is not None:``។ បើ ``x`` អាចជា ``0`` ឬ ``""``
   ដែលជាតម្លៃត្រឹមត្រូវ លក្ខខណ្ឌទីមួយនឹងរំលងវាដោយច្រឡំ។

.. _comparison-operators:

ប្រមាណវិធីប្រៀបធៀប
====================

.. list-table::
   :header-rows: 1
   :widths: 16 34 50

   * - ប្រមាណវិធី
     - អត្ថន័យ
     - ឧទាហរណ៍ (លទ្ធផល ``True``)
   * - ``==``
     - ស្មើតម្លៃ
     - ``5 == 5``
   * - ``!=``
     - មិនស្មើ
     - ``5 != 6``
   * - ``<``  ``<=``
     - តូចជាង / តូចជាងឬស្មើ
     - ``5 < 6``
   * - ``>``  ``>=``
     - ធំជាង / ធំជាងឬស្មើ
     - ``6 > 5``
   * - ``is``
     - object តែមួយ
     - ``x is None``
   * - ``is not``
     - object ផ្សេងគ្នា
     - ``x is not None``
   * - ``in``
     - ស្ថិតក្នុងលំដាប់
     - ``"a" in "cat"``
   * - ``not in``
     - មិនស្ថិតក្នុងលំដាប់
     - ``"z" not in "cat"``

.. _chained-comparison:

ការប្រៀបធៀបខ្សែ
---------------

.. code-block:: pycon

   >>> age = 25
   >>> 18 <= age < 60           # ស្មើនឹង 18 <= age and age < 60
   True
   >>> a, b, c = 1, 2, 3
   >>> a < b < c
   True
   >>> a < b > c                # ស្មើនឹង a < b and b > c
   False

.. note::

   Python វាយតម្លៃ expression នីមួយៗតែ **ម្ដងគត់** ក្នុងការប្រៀបធៀបខ្សែ។
   ដូច្នេះ ``a < f() < b`` ហៅ ``f()`` តែម្ដង។

.. _boolean-operators:

ប្រមាណវិធីប៊ូលីន
=================

.. list-table::
   :header-rows: 1
   :widths: 14 86

   * - ប្រមាណវិធី
     - អត្ថន័យ
   * - ``x and y``
     - បើ ``x`` មិនពិត → ត្រឡប់ ``x``; បើមិនដូច្នោះ → ត្រឡប់ ``y``
   * - ``x or y``
     - បើ ``x`` ពិត → ត្រឡប់ ``x``; បើមិនដូច្នោះ → ត្រឡប់ ``y``
   * - ``not x``
     - បញ្ច្រាសភាពពិតនៃ ``x``

**អាទិភាព** (ពីទាបទៅខ្ពស់)៖ ``or`` < ``and`` < ``not``។

.. _short-circuit:

Short-circuit Evaluation
------------------------

``and`` និង ``or`` **ឈប់វាយតម្លៃ** នៅពេលលទ្ធផលត្រូវបានកំណត់រួចហើយ៖

.. code-block:: pycon

   >>> def check(value):
   ...     print(f"  ពិនិត្យ {value!r}")
   ...     return value             # ត្រឡប់ operand ខ្លួនឯង មិនមែន bool
   ...
   >>> check("") and check("b")     # '' មិនពិត → ឈប់ ត្រឡប់ ''
     ពិនិត្យ ''
   ''
   >>> check("a") or check("b")     # 'a' ពិត → ឈប់ ត្រឡប់ 'a'
     ពិនិត្យ 'a'
   'a'

ឥរិយាបថនេះអនុញ្ញាតឱ្យប្រើវាជា **ការការពារ**៖

.. code-block:: python

   x = 0

   # ❌ អាចបញ្ចេញ ZeroDivisionError
   # result = 10 / x

   # ✅ បើ x == 0 នឹងមិនដល់ការចែកទេ
   result = x != 0 and 10 / x
   print(result)          # False

.. note::

   ``and``/``or`` ត្រឡប់ **operand ពិតប្រាកដ** មិនមែន ``True``/``False``
   ទេ។ ដូច្នេះ ``0 or "លំនាំដើម"`` ត្រឡប់ ``"លំនាំដើម"``។

.. warning::

   កុំប្រើ ``x or default`` ដើម្បីផ្ដល់តម្លៃលំនាំដើម បើ ``x`` អាចជា
   ``0``, ``""`` ឬ ``[]`` ដែលជាតម្លៃមានន័យ។ ក្នុងករណីនោះប្រើ
   ``x if x is not None else default``។

.. _conditional-expression:

Conditional Expression (Ternary)
================================

.. code-block:: python

   status = "ពេញវ័យ" if age >= 18 else "អនីតិជន"

ទម្រង់ទូទៅ៖ ``A if condition else B`` — វាយតម្លៃ ``condition`` រួចត្រឡប់
``A`` បើពិត ឬ ``B`` បើមិនពិត។

.. code-block:: pycon

   >>> n = 7
   >>> "គូ" if n % 2 == 0 else "សេស"
   'សេស'

.. tip::

   ប្រើវាសម្រាប់ការជ្រើសរើសតម្លៃ **សាមញ្ញ** ប៉ុណ្ណោះ។ បើមាន nested
   ternary (ternary ក្នុង ternary) សូមបំលែងទៅជា ``if``/``else`` ធម្មតាវិញ។

----

.. _while-loop:

រង្វិលជុំ ``while``
===================

ដំណើរការ block ម្ដងហើយម្ដងទៀត តราบណាលក្ខខណ្ឌនៅពិត៖

.. code-block:: pycon

   >>> count = 0
   >>> while count < 3:
   ...     print(count, end=" ")
   ...     count += 1
   ...
   0 1 2

.. warning::

   **រង្វិលជុំគ្មានទីបញ្ចប់ (infinite loop)** កើតឡើងបើលក្ខខណ្ឌមិនដែល
   ក្លាយជាមិនពិត។ ត្រូវប្រាកដថាមានអ្វីមួយផ្លាស់ប្ដូរក្នុងរង្វិលជុំ៖

   .. code-block:: python
      :no-test:

      # ❌ រង្វិលជុំគ្មានទីបញ្ចប់ — count មិនដែលផ្លាស់ប្ដូរ
      count = 0
      while count < 3:
          print(count)

      # ✅
      count = 0
      while count < 3:
          print(count)
          count += 1

   បើកម្មវិធីរបស់អ្នកជាប់ក្នុងរង្វិលជុំគ្មានទីបញ្ចប់ សូមចុច
   :kbd:`Control-C` ដើម្បីបញ្ឈប់វា។

រង្វិលជុំ ``while`` សមស្របនៅពេលអ្នក **មិនដឹងចំនួនដងជាមុន**។
ឧទាហរណ៍ ការសួរអ្នកប្រើរហូតដល់បានចម្លើយត្រឹមត្រូវ៖

.. code-block:: python
   :no-test:

   while True:
       answer = input("បញ្ចូលលេខ (ឬ 'q' ដើម្បីចេញ): ")
       if answer == "q":
           break
       if answer.isdigit():
           print(f"អ្នកបានបញ្ចូល {answer}")

----

.. _for-loop:

រង្វិលជុំ ``for``
=================

``for`` របស់ Python ខុសពីភាសាផ្សេងៗ — វាមិនមែនជារង្វិលជុំរាប់លេខទេ
ប៉ុន្តែជារង្វិលជុំ **ដើរលើធាតុនៃលំដាប់** (iterate)។

.. code-block:: pycon

   >>> for fruit in ["ចេក", "ស្វាយ", "ទុំរេន"]:
   ...     print(fruit)
   ...
   ចេក
   ស្វាយ
   ទុំរេន

   >>> for char in "Py":          # ខ្សែអក្សរក៏ជា iterable
   ...     print(char)
   ...
   P
   y

   >>> for key in {"a": 1, "b": 2}:   # dict — ដើរលើ key
   ...     print(key)
   ...
   a
   b

.. _modifying-during-loop:

ការកែប្រែលំដាប់កំពុងដើរលើវា
------------------------------

.. warning::

   កុំបន្ថែម ឬលុបធាតុពីលំដាប់ដែលអ្នកកំពុងដើរលើវា។ លទ្ធផលគឺមិនអាច
   ទាយបាន។ ចូរដើរលើ **ចម្លង** ឬបង្កើតលំដាប់ **ថ្មី**៖

   .. code-block:: python

      my_list = [1, -2, 3, -4]

      # ❌ កែប្រែកំពុងដើរ — រំលងធាតុ
      for x in my_list:
          if x < 0:
              my_list.remove(x)

      # ✅ ដើរលើចម្លង
      my_list = [1, -2, 3, -4]
      for x in my_list.copy():
          if x < 0:
              my_list.remove(x)
      print(my_list)            # [1, 3]

      # ✅ ល្អបំផុត — បង្កើត list ថ្មី
      my_list = [1, -2, 3, -4]
      my_list = [x for x in my_list if x >= 0]
      print(my_list)            # [1, 3]

.. _range:

អនុគមន៍ ``range()``
===================

``range()`` បង្កើតលំដាប់លេខគត់។ វាជា *lazy sequence* — មិនផ្ទុកលេខ
ទាំងអស់ក្នុងអង្គចងចាំទេ។

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - ទម្រង់
     - អត្ថន័យ
   * - ``range(stop)``
     - ពី ``0`` ដល់ ``stop - 1``
   * - ``range(start, stop)``
     - ពី ``start`` ដល់ ``stop - 1``
   * - ``range(start, stop, step)``
     - ពី ``start`` ដល់ ``stop - 1`` ដោយជំហាន ``step``

.. code-block:: pycon

   >>> list(range(5))
   [0, 1, 2, 3, 4]
   >>> list(range(2, 6))
   [2, 3, 4, 5]
   >>> list(range(0, 10, 3))
   [0, 3, 6, 9]
   >>> list(range(5, 0, -1))        # រាប់ថយក្រោយ
   [5, 4, 3, 2, 1]
   >>> list(range(0))               # ទទេ
   []

.. important::

   * ធាតុដំបូងត្រូវបាន **រាប់បញ្ចូល**; ធាតុចុងក្រោយ **មិនរាប់បញ្ចូល**។
     ``range(5)`` មាន ៥ ធាតុ គឺ 0 ដល់ 4។
   * ``range()`` ត្រឡប់ **object range** មិនមែន ``list`` ទេ។
     ប្រើ ``list(range(...))`` បើអ្នកចង់បាន list។

   .. code-block:: pycon

      >>> range(5)
      range(0, 5)
      >>> type(range(5))
      <class 'range'>
      >>> len(range(5))            # ប៉ុន្តែមានប្រវែង និង index
      5
      >>> range(5)[2]
      2

.. _break-continue:

``break`` និង ``continue``
==========================

.. list-table::
   :header-rows: 1
   :widths: 20 80

   * - ពាក្យបញ្ជា
     - ឥទ្ធិពល
   * - ``break``
     - ចេញពីរង្វិលជុំ **ភ្លាម** (ទាំងស្រុង)
   * - ``continue``
     - រំលងធាតុបច្ចុប្បន្ន ទៅធាតុ **បន្ទាប់**

.. code-block:: pycon

   >>> for n in range(10):
   ...     if n == 5:
   ...         break              # ឈប់នៅពេល n == 5
   ...     print(n, end=" ")
   ...
   0 1 2 3 4

   >>> for n in range(10):
   ...     if n % 2 == 0:
   ...         continue           # រំលងលេខគូ
   ...     print(n, end=" ")
   ...
   1 3 5 7 9

**``break`` ក្នុងរង្វិលជុំ nested** — វាចេញតែពីរង្វិលជុំ **ខាងក្នុងបំផុត** ប៉ុណ្ណោះ៖

.. code-block:: pycon

   >>> for i in range(3):
   ...     for j in range(3):
   ...         if j == 1:
   ...             break          # ចេញពីរង្វិលជុំ j តែប៉ុណ្ណោះ
   ...         print(f"i={i} j={j}")
   ...
   i=0 j=0
   i=1 j=0
   i=2 j=0

.. tip::

   បើអ្នកត្រូវការចេញពីរង្វិលជុំ nested ទាំងអស់ វិធីស្អាតបំផុតគឺដាក់កូដ
   ក្នុង **អនុគមន៍** ហើយប្រើ ``return``។

.. _loop-else:

``else`` នៅលើរង្វិលជុំ
========================

នេះជាលក្ខណៈពិសេសរបស់ Python ដែលភាសាផ្សេងគ្មាន។ ``else`` នៅលើរង្វិលជុំ
ដំណើរការ **លុះត្រាតែរង្វិលជុំបញ្ចប់ដោយធម្មតា** — ពោលគឺ **មិនមាន ``break``**។

.. code-block:: pycon

   >>> # មាន break → else មិនដំណើរការ
   >>> for n in range(2, 10):
   ...     if n % 5 == 0:
   ...         print(f"រកឃើញ {n}")
   ...         break
   ... else:
   ...     print("មិនបានរកឃើញ")
   ...
   រកឃើញ 5

   >>> # គ្មាន break → else ដំណើរការ
   >>> for n in range(2, 4):
   ...     if n % 5 == 0:
   ...         print(f"រកឃើញ {n}")
   ...         break
   ... else:
   ...     print("មិនបានរកឃើញ")
   ...
   មិនបានរកឃើញ

**ឧទាហរណ៍ជាក់ស្ដែង** — ស្វែងរកចំនួនបឋម៖

.. code-block:: pycon

   >>> for n in range(2, 10):
   ...     for x in range(2, n):
   ...         if n % x == 0:
   ...             break
   ...     else:
   ...         # រង្វិលជុំខាងក្នុងបញ្ចប់ដោយគ្មាន break → n ជាចំនួនបឋម
   ...         print(n, "ជាចំនួនបឋម")
   ...
   2 ជាចំនួនបឋម
   3 ជាចំនួនបឋម
   5 ជាចំនួនបឋម
   7 ជាចំនួនបឋម

.. note::

   ``else`` ក៏ដំណើរការលើ ``while`` ដែរ — វាដំណើរការនៅពេលលក្ខខណ្ឌ
   ក្លាយជាមិនពិត ប៉ុន្តែមិនដំណើរការបើមាន ``break``។

   ចងចាំថា៖ ``else`` នៅលើរង្វិលជុំមានន័យថា **"no break"** មិនមែន
   "ផ្សេងទៀត" ទេ។

.. _pass:

ពាក្យបញ្ជា ``pass``
===================

``pass`` មិនធ្វើអ្វីទាំងអស់។ វាមានប្រយោជន៍នៅកន្លែងដែល Python តម្រូវឱ្យ
មាន statement ប៉ុន្តែអ្នកមិនទាន់ចង់សរសេរកូដ៖

.. code-block:: python

   condition = False

   # បង្កើត class ទទេជាអចិន្ត្រៃយ៍
   class Placeholder:
       pass

   # អនុគមន៍ដែលមិនទាន់បានអនុវត្ត
   def not_implemented_yet():
       pass

   # ចាប់យកកំហុស ប៉ុន្តែមិនធ្វើអ្វី
   def risky():
       raise ValueError("មានបញ្ហា")

   try:
       risky()
   except ValueError:
       pass

   # សាខាដែលមិនត្រូវការធ្វើអ្វី
   def do_something():
       print("សាខា else")

   if condition:
       pass
   else:
       do_something()

.. warning::

   ``pass`` ខុសពីអត្ថាធិប្បាយ។ អត្ថាធិប្បាយមិនមែនជា statement ទេ
   ដូច្នេះ block ទទេដែលមានតែអត្ថាធិប្បាយនឹងបញ្ចេញ ``IndentationError``។

----

.. _match-statement:

ពាក្យបញ្ជា ``match`` (Structural Pattern Matching)
===================================================

.. versionadded:: 3.10

``match`` គឺជាវិធីមានអានុភាពជាង ``if``/``elif`` សម្រាប់ផ្គូផ្គង **រចនាសម្ព័ន្ធ**
នៃទិន្នន័យ។

.. code-block:: python

   def describe(command):
       match command.split():
           case ["quit" | "exit" | "bye"]:   # ជាក់លាក់ — ត្រូវនៅមុនគេ
               return "ចេញពីកម្មវិធី"
           case [action]:                     # ទូទៅ — ចាប់យកអ្វីក៏បាន
               return f"សកម្មភាពតែមួយ: {action}"
           case [action, target]:
               return f"{action} លើ {target}"
           case _:
               return "មិនស្គាល់"

.. code-block:: pycon

   >>> describe("run")
   'សកម្មភាពតែមួយ: run'
   >>> describe("delete file")
   'delete លើ file'
   >>> describe("quit")
   'ចេញពីកម្មវិធី'
   >>> describe("do many things now")
   'មិនស្គាល់'

**លក្ខណៈសំខាន់ៗ៖**

.. list-table::
   :header-rows: 1
   :widths: 26 74

   * - លក្ខណៈ
     - ឧទាហរណ៍
   * - Literal
     - ``case 42:``, ``case "text":``
   * - Capture (ចាប់យកតម្លៃ)
     - ``case [x, y]:`` → ភ្ជាប់ ``x`` និង ``y``
   * - Wildcard (ផ្គូផ្គងអ្វីក៏បាន)
     - ``case _:``
   * - OR pattern
     - ``case "a" | "b" | "c":``
   * - Sequence
     - ``case [first, *rest]:``
   * - Mapping
     - ``case {"type": t, **rest}:``
   * - Class pattern
     - ``case Point(x=0, y=0):``
   * - Guard (លក្ខខណ្ឌបន្ថែម)
     - ``case [x, y] if x > y:``

.. code-block:: pycon

   >>> def handle(data):
   ...     match data:
   ...         case {"type": "user", "name": name}:
   ...             return f"អ្នកប្រើ: {name}"
   ...         case {"type": "error", "code": code, **rest}:
   ...             return f"កំហុស {code}: {rest}"
   ...         case [x, y, *more]:
   ...             return f"កូអរដោនេ ({x}, {y}) + {len(more)} ទៀត"
   ...         case str() as s:
   ...             return f"ខ្សែអក្សរ: {s}"
   ...         case _:
   ...             return "មិនស្គាល់"
   ...
   >>> handle({"type": "user", "name": "សុខា"})
   'អ្នកប្រើ: សុខា'
   >>> handle({"type": "error", "code": 404, "url": "/x"})
   "កំហុស 404: {'url': '/x'}"
   >>> handle([1, 2, 3, 4])
   'កូអរដោនេ (1, 2) + 2 ទៀត'
   >>> handle("hello")
   'ខ្សែអក្សរ: hello'

.. tip::

   ``case`` ត្រូវបានសាកល្បង **ពីលើចុះក្រោម** ហើយ case ដំបូងដែលផ្គូផ្គង
   នឹងឈ្នះ។ ដូច្នេះ៖

   * ដាក់ pattern **ជាក់លាក់** (literal, class pattern) នៅ **ខាងលើ**
   * ដាក់ pattern **ទូទៅ** (capture ដូចជា ``[action]``) នៅ **ខាងក្រោម**
   * ដាក់ ``case _`` (wildcard) នៅ **ចុងក្រោយបំផុត**

   កំហុសទូទៅគឺដាក់ ``case [action]:`` នៅមុន ``case ["quit"]:`` — ពេលនោះ
   ``"quit"`` ត្រូវបានចាប់យកជា ``action`` ហើយ case ជាក់លាក់មិនដែលដំណើរការ៖

   .. code-block:: pycon

      >>> def wrong(command):
      ...     match command.split():
      ...         case [action]:                  # ❌ ចាប់យកអ្វីៗទាំងអស់
      ...             return f"សកម្មភាព: {action}"
      ...         case ["quit"]:                  # មិនដែលដល់ទីនេះទេ
      ...             return "ចេញ"
      ...
      >>> wrong("quit")
      'សកម្មភាព: quit'

.. note::

   ``match`` មិន **fall through** ដូច ``switch`` របស់ C/Java ទេ — នៅពេល
   case មួយផ្គូផ្គង វាដំណើរការហើយចេញពី ``match`` ភ្លាម។ បើអ្នកចង់បាន
   ឥរិយាបថ fall through ប្រើ OR pattern (``case "a" | "b":``)។

----

.. _nested-loops:

រង្វិលជុំ Nested និងឧទាហរណ៍ជាក់ស្ដែង
=====================================

**តារាងគុណ៖**

.. code-block:: pycon

   >>> for i in range(1, 4):
   ...     for j in range(1, 4):
   ...         print(f"{i}×{j}={i*j}", end="  ")
   ...     print()
   ...
   1×1=1  1×2=2  1×3=3
   2×1=2  2×2=4  2×3=6
   3×1=3  3×2=6  3×3=9

**រូបត្រីកោណ៖**

.. code-block:: pycon

   >>> for i in range(1, 6):
   ...     print("*" * i)
   ...
   *
   **
   ***
   ****
   *****

**ស្វែងរកធាតុធំបំផុតដោយមិនប្រើ ``max()``៖**

.. code-block:: pycon

   >>> nums = [3, 7, 2, 9, 4]
   >>> largest = nums[0]
   >>> for n in nums[1:]:
   ...     if n > largest:
   ...         largest = n
   ...
   >>> largest
   9

----

.. _control-flow-summary:

សង្ខេប
======

.. list-table::
   :header-rows: 1
   :widths: 24 76

   * - ឧបករណ៍
     - ប្រើសម្រាប់
   * - ``if`` / ``elif`` / ``else``
     - សម្រេចចិត្តតាមលក្ខខណ្ឌ
   * - ``match`` / ``case``
     - ផ្គូផ្គងរចនាសម្ព័ន្ធទិន្នន័យ (Python 3.10+)
   * - ``for``
     - ដើរលើធាតុនៃលំដាប់
   * - ``range()``
     - បង្កើតលំដាប់លេខគត់
   * - ``while``
     - ដំណើរការម្ដងទៀតតាមលក្ខខណ្ឌ
   * - ``break``
     - ចេញពីរង្វិលជុំភ្លាម
   * - ``continue``
     - រំលងទៅធាតុបន្ទាប់
   * - ``else`` (លើរង្វិលជុំ)
     - ដំណើរការបើរង្វិលជុំ **មិនមាន** ``break``
   * - ``pass``
     - Statement ទទេ

.. rubric:: ប្រភពយោង

* `if Statements <https://docs.python.org/3/tutorial/controlflow.html#if-statements>`_
* `for Statements <https://docs.python.org/3/tutorial/controlflow.html#for-statements>`_
* `The range() Function <https://docs.python.org/3/tutorial/controlflow.html#the-range-function>`_
* `break and continue Statements and else Clauses on Loops <https://docs.python.org/3/tutorial/controlflow.html#break-and-continue-statements-and-else-clauses-on-loops>`_
* `match Statements <https://docs.python.org/3/tutorial/controlflow.html#match-statements>`_
* `The pass statement <https://docs.python.org/3/tutorial/controlflow.html#pass-statements>`_
