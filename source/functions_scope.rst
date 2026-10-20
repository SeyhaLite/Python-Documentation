.. _functions-scope:

.. container:: src-note

   ប្រភពដើម៖ CPython ``Doc/tutorial/controlflow.rst`` (ផ្នែក ៤ និង ៥),
   ``Doc/tutorial/classes.rst`` (ផ្នែក *Python Scopes and Namespaces*),
   ``Doc/reference/compound_stmts.rst`` ·
   `ឯកសារផ្លូវការ <https://docs.python.org/3/tutorial/controlflow.html#defining-functions>`_

###############################
អនុគមន៍ និងវិសាលភាពអថេរ
###############################

.. _defining-functions:

ការកំណត់អនុគមន៍
===============

អនុគមន៍ (function) គឺជាប្លុកកូដដែលមានឈ្មោះ អាចហៅម្ដងទៀតបាន។
វាជួយឱ្យកូដរបស់អ្នក **មិនស្ទួន** **ងាយអាន** និង **ងាយសាកល្បង**។

.. code-block:: python

   def greet(name):
       """បោះពុម្ពពាក្យសួស្ដីទៅកាន់មនុស្សម្នាក់។"""
       print(f"សួស្ដី {name}!")

   greet("សុខា")     # ហៅអនុគមន៍

ទម្រង់ទូទៅ៖

.. code-block:: text

   def ឈ្មោះអនុគមន៍(parameter1, parameter2, ...):
       """docstring (មិនចាំបាច់ ប៉ុន្តែណែនាំ)"""
       statement
       statement
       return expression      # មិនចាំបាច់

* ពាក្យគន្លឹះ ``def`` ចាប់ផ្ដើមការកំណត់អនុគមន៍។
* តាមពីក្រោយដោយ **ឈ្មោះអនុគមន៍** និងបញ្ជី parameter ក្នុងវង់ក្រចក។
* ខ្លួនអនុគមន៍ចាប់ផ្ដើមនៅបន្ទាត់បន្ទាប់ ហើយត្រូវ **ចូលបន្ទាត់**។

.. _docstrings:

Docstring
---------

ខ្សែអក្សរដំបូងក្នុងខ្លួនអនុគមន៍គឺជា **docstring**។ ឧបករណ៍ជាច្រើន
(IDE, ``help()``, ឯកសារស្វ័យប្រវត្តិ) ប្រើវា៖

.. code-block:: pycon

   >>> def add(a, b):
   ...     """ត្រឡប់ផលបូកនៃ a និង b។"""
   ...     return a + b
   ...
   >>> add.__doc__
   'ត្រឡប់ផលបូកនៃ a និង b។'
   >>> help(add)
   Help on function add in module ...:

   add(a, b)
       ត្រឡប់ផលបូកនៃ a និង b។

អនុសញ្ញា docstring ច្រើនបន្ទាត់៖

.. code-block:: python

   def calculate_tax(income, rate):
       """គណនាពន្ធលើចំណូល។

       Args:
           income: ចំណូលប្រចាំឆ្នាំជាលេខ (int ឬ float)។
           rate: អត្រាពន្ធជាភាគរយទសភាគ ឧ. 0.2 សម្រាប់ ២០%។

       Returns:
           ចំនួនពន្ធជា float។

       Raises:
           ValueError: បើ income អវិជ្ជមាន។
       """
       if income < 0:
           raise ValueError("ចំណូលមិនអាចអវិជ្ជមានទេ")
       return income * rate

.. tip::

   សរសេរ docstring សម្រាប់អនុគមន៍ **សាធារណៈ** ទាំងអស់។ សម្រាប់អនុគមន៍
   ឯកជនតូចៗដែលច្បាស់លាស់ អត្ថាធិប្បាយមួយបន្ទាត់គឺគ្រប់គ្រាន់។

.. _return:

``return`` និងតម្លៃត្រឡប់
--------------------------

.. code-block:: pycon

   >>> def square(n):
   ...     return n ** 2
   ...
   >>> square(5)
   25

   >>> def no_return():
   ...     print("គ្មាន return")
   ...
   >>> result = no_return()
   គ្មាន return
   >>> print(result)
   None

ច្បាប់សំខាន់៖

* ``return expression`` បញ្ចប់អនុគមន៍ភ្លាម និងត្រឡប់តម្លៃ។
* ``return`` ដោយគ្មាន expression ត្រឡប់ ``None``។
* អនុគមន៍ដែល **ដំណើរការដល់ចុង** ដោយគ្មាន ``return`` ក៏ត្រឡប់
  ``None`` ដែរ។

**ត្រឡប់ច្រើនតម្លៃ** — តាមពិតគឺត្រឡប់ ``tuple`` មួយ៖

.. code-block:: pycon

   >>> def min_max(nums):
   ...     return min(nums), max(nums)
   ...
   >>> min_max([4, 1, 7])
   (1, 7)
   >>> lo, hi = min_max([4, 1, 7])      # unpacking
   >>> lo, hi
   (1, 7)

.. _call-semantics:

អនុគមន៍គឺជា Object
--------------------

នៅក្នុង Python អនុគមន៍គឺជា **object ធម្មតាមួយ**។ អ្នកអាចផ្ដល់វាទៅអថេរ
បញ្ជូនវាទៅអនុគមន៍ផ្សេង ឬរក្សាទុកវាក្នុង list៖

.. code-block:: pycon

   >>> def double(x):
   ...     return x * 2
   ...
   >>> f = double            # គ្មានវង់ក្រចក — មិនមែនការហៅទេ
   >>> f(21)
   42
   >>> double                # វាជា object
   <function double at 0x...>

   >>> def apply(func, value):
   ...     return func(value)
   ...
   >>> apply(double, 5)
   10

.. note::

   ភាពខុសគ្នារវាង ``f`` និង ``f()`` គឺសំខាន់ណាស់។ ``f`` គឺជា object
   អនុគមន៍ខ្លួនឯង; ``f()`` គឺជា **ការហៅ** អនុគមន៍នោះ។

.. _execution-model:

អ្វីកើតឡើងពេលហៅអនុគមន៍?
---------------------------

ការ **ដំណើរការ** អនុគមន៍បង្កើត *symbol table* ថ្មីមួយសម្រាប់អថេរ local។
ដំណើរការស្វែងរកឈ្មោះអថេរធ្វើឡើងតាមលំដាប់៖

1. symbol table local របស់អនុគមន៍
2. symbol table local របស់អនុគមន៍ដែលរុំព័ទ្ធ (enclosing functions)
3. symbol table global របស់ module
4. តារាងឈ្មោះ built-in

Argument ត្រូវបានបញ្ជូនដោយ **call by object reference** — តម្លៃដែល
បញ្ជូនគឺជា *reference* ទៅ object មិនមែនជាចម្លងនៃ object ទេ។

.. code-block:: pycon

   >>> def modify(x):
   ...     x = x + 1        # បង្កើត object ថ្មី បញ្ជូនមកក្រៅទេ
   ...     print("ក្នុងអនុគមន៍:", x)
   ...
   >>> n = 10
   >>> modify(n)
   ក្នុងអនុគមន៍: 11
   >>> n                    # មិនផ្លាស់ប្ដូរទេ
   10

ប៉ុន្តែបើ object ជា **mutable** ការកែប្រែនឹងលេចចេញមកក្រៅ៖

.. code-block:: pycon

   >>> def add_item(lst):
   ...     lst.append("ថ្មី")     # កែប្រែ list ដើម
   ...
   >>> items = ["ចាស់"]
   >>> add_item(items)
   >>> items
   ['ចាស់', 'ថ្មី']

.. warning::

   នេះជាប្រភព bug ទូទៅ។ អនុគមន៍ដែល **កែប្រែ** argument របស់វា
   ហៅថាមាន *side effect*។ វាល្អជាងក្នុងការត្រឡប់តម្លៃថ្មីជំនួសវិញ
   លើកលែងតែចេតនាច្បាស់លាស់។

----

.. _default-arguments:

Default Argument Value
======================

Parameter អាចមានតម្លៃលំនាំដើម។ ពួកវាត្រូវតែនៅ **ខាងចុង**៖

.. code-block:: python

   def connect(host, port=3306, timeout=30):
       return f"{host}:{port} (timeout={timeout})"

.. code-block:: pycon

   >>> connect("localhost")
   'localhost:3306 (timeout=30)'
   >>> connect("db.example.com", 5432)
   'db.example.com:5432 (timeout=30)'
   >>> connect("db.example.com", 5432, 60)
   'db.example.com:5432 (timeout=60)'

.. important::

   តម្លៃលំនាំដើមត្រូវបានវាយតម្លៃ **តែម្ដងគត់** — នៅពេលដែលអនុគមន៍ត្រូវបាន
   *កំណត់* (definition) មិនមែននៅពេលហៅទេ។ នេះនាំទៅរកបញ្ហាធំមួយ៖

.. _mutable-default-pitfall:

អន្ទាក់ — Default Argument ជា Mutable
----------------------------------------

.. code-block:: python

   # ❌ កំហុស — កុំសរសេរបែបនេះ
   def append_to(item, target=[]):
       target.append(item)
       return target

.. code-block:: pycon

   >>> append_to(1)
   [1]
   >>> append_to(2)          # រំពឹង [2] ប៉ុន្តែបាន [1, 2]!
   [1, 2]
   >>> append_to(3)
   [1, 2, 3]

list ទទេដូចគ្នាត្រូវបាន **ចែករំលែក** រវាងការហៅទាំងអស់។ វិធីត្រឹមត្រូវ៖

.. code-block:: python

   # ✅ ត្រឹមត្រូវ
   def append_to(item, target=None):
       if target is None:
           target = []
       target.append(item)
       return target

.. code-block:: pycon

   >>> append_to(1)
   [1]
   >>> append_to(2)
   [2]

.. warning::

   ចៀសវាងប្រើ object **mutable** ជាតម្លៃលំនាំដើម៖ ``list``, ``dict``,
   ``set``, ``bytearray``។ ប្រើ ``None`` ជា *sentinel* ហើយបង្កើត object
   ថ្មីក្នុងខ្លួនអនុគមន៍។

   បើអ្នកពិតជាចង់បាន object mutable ចែករំលែក ប្រើ attribute របស់អនុគមន៍
   ដើម្បីឱ្យចេតនាច្បាស់លាស់៖ ``append_to.default = []``។

----

.. _keyword-arguments:

Keyword Argument
================

អ្នកអាចហៅអនុគមន៍ដោយបញ្ជាក់ឈ្មោះ parameter៖

.. code-block:: python

   def create_user(name, age, city, active=True):
       return {"name": name, "age": age, "city": city, "active": active}

.. code-block:: pycon

   >>> # positional ទាំងអស់
   >>> create_user("សុខា", 25, "ភ្នំពេញ")
   {'name': 'សុខា', 'age': 25, 'city': 'ភ្នំពេញ', 'active': True}

   >>> # keyword ទាំងអស់ — លំដាប់មិនសំខាន់
   >>> create_user(city="សៀមរាប", name="ដារ៉ា", age=30)
   {'name': 'ដារ៉ា', 'age': 30, 'city': 'សៀមរាប', 'active': True}

   >>> # លាយឡំ — positional ត្រូវតែមកមុន keyword
   >>> create_user("សុភា", 22, city="បាត់ដំបង", active=False)
   {'name': 'សុភា', 'age': 22, 'city': 'បាត់ដំបង', 'active': False}

ច្បាប់៖

1. argument **positional** ទាំងអស់ត្រូវតែមកមុន argument **keyword**។
2. មិនអាចផ្ដល់តម្លៃពីរដងទៅ parameter ដូចគ្នា។
3. parameter ដែលគ្មានតម្លៃលំនាំដើម ត្រូវតែទទួលបាន argument។

.. code-block:: pycon

   >>> create_user(name="សុខា", 25, "ភ្នំពេញ")   # keyword មុន positional
   Traceback (most recent call last):
     ...
   SyntaxError: positional argument follows keyword argument

   >>> create_user("សុខា", 25, "ភ្នំពេញ", name="ដារ៉ា")
   Traceback (most recent call last):
     ...
   TypeError: create_user() got multiple values for argument 'name'

   >>> create_user("សុខា", 25)                   # ខ្វះ city
   Traceback (most recent call last):
     ...
   TypeError: create_user() missing 1 required positional argument: 'city'

.. tip::

   ប្រើ keyword argument នៅពេលអ្នកហៅអនុគមន៍ដែលមាន parameter
   boolean ច្រើន ឬនៅពេលអ្នករំលង parameter ខ្លះ។ វាធ្វើឱ្យកូដអានងាយ
   និងកាត់បន្ថយកំហុសពីលំដាប់ argument។

----

.. _special-parameters:

Special Parameter — ``/`` និង ``*``
===================================

Python អនុញ្ញាតឱ្យអ្នក **កំណត់** ថា parameter ណាត្រូវបញ្ជូនជា positional
ឬ keyword៖

.. code-block:: text

   def f(pos1, pos2, /, pos_or_kwd, *, kwd1, kwd2):
         └── positional-only ──┘ └── ទាំងពីរ ──┘ └ keyword-only ┘

.. list-table::
   :header-rows: 1
   :widths: 14 86

   * - សញ្ញា
     - អត្ថន័យ
   * - ``/``
     - parameter ទាំងអស់ខាង **ឆ្វេង** របស់វាត្រូវបញ្ជូនជា positional តែប៉ុណ្ណោះ
   * - ``*``
     - parameter ទាំងអស់ខាង **ស្ដាំ** របស់វាត្រូវបញ្ជូនជា keyword តែប៉ុណ្ណោះ

.. code-block:: pycon

   >>> def divide(a, b, /, *, precision=2):
   ...     return round(a / b, precision)
   ...
   >>> divide(10, 3)
   3.33
   >>> divide(10, 3, precision=4)
   3.3333
   >>> divide(a=10, b=3)           # a និង b សុទ្ធតែ positional-only
   Traceback (most recent call last):
     ...
   TypeError: divide() got some positional-only arguments passed as keyword arguments: 'a, b'
   >>> divide(10, 3, 4)            # precision គឺ keyword-only
   Traceback (most recent call last):
     ...
   TypeError: divide() takes 2 positional arguments but 3 were given

.. note::

   បណ្ណាល័យស្តង់ដារប្រើ ``/`` ដើម្បីការពារឈ្មោះ parameter ក្លាយជាផ្នែក
   នៃ API សាធារណៈ។ ឧទាហរណ៍ ``len(obj)`` — អ្នកមិនអាចសរសេរ
   ``len(obj="abc")`` បានទេ។

   .. versionadded:: 3.8
      វាក្យសម្ពន្ធ positional-only ``/``។

----

.. _arbitrary-arguments:

បញ្ជី Argument តាមចិត្ត — ``*args`` និង ``**kwargs``
====================================================

.. code-block:: pycon

   >>> def total(*numbers):              # ទទួល positional ច្រើនតាមចិត្ត
   ...     return sum(numbers)
   ...
   >>> total(1, 2, 3)
   6
   >>> total()
   0
   >>> numbers                          # វាជា tuple ក្នុងអនុគមន៍
   Traceback (most recent call last):
     ...
   NameError: name 'numbers' is not defined. Did you forget to import 'numbers'?

   >>> def describe(**details):          # ទទួល keyword ច្រើនតាមចិត្ត
   ...     return ", ".join(f"{k}={v}" for k, v in details.items())
   ...
   >>> describe(name="សុខា", age=25, city="ភ្នំពេញ")
   'name=សុខា, age=25, city=ភ្នំពេញ'

**លាយឡំទាំងអស់គ្នា** — លំដាប់ត្រូវតែ៖ positional → ``*args`` →
keyword-only → ``**kwargs``៖

.. code-block:: python

   def api_call(endpoint, *args, method="GET", timeout=30, **kwargs):
       return {
           "endpoint": endpoint,
           "args": args,
           "method": method,
           "timeout": timeout,
           "kwargs": kwargs,
       }

.. code-block:: pycon

   >>> api_call("/users", 1, 2, method="POST", page=3)
   {'endpoint': '/users', 'args': (1, 2), 'method': 'POST', 'timeout': 30, 'kwargs': {'page': 3}}

.. _unpacking-arguments:

Unpacking Argument
--------------------

``*`` និង ``**`` ក៏ប្រើដើម្បី **បំបែក** (unpack) iterable/dict ទៅជា
argument ដែរ — ទិសដៅផ្ទុយគ្នា៖

.. code-block:: pycon

   >>> def point(x, y, z):
   ...     return (x, y, z)
   ...
   >>> coords = [1, 2, 3]
   >>> point(*coords)                  # unpack list → positional
   (1, 2, 3)

   >>> config = {"x": 1, "y": 2, "z": 3}
   >>> point(**config)                 # unpack dict → keyword
   (1, 2, 3)

.. list-table::
   :header-rows: 1
   :widths: 26 74

   * - ទីតាំង
     - អត្ថន័យ
   * - ក្នុង **ការកំណត់** (``def f(*args)``)
     - **ប្រមូល** argument ចូលជា tuple/dict
   * - ក្នុង **ការហៅ** (``f(*lst)``)
     - **បំបែក** iterable/dict ចេញជា argument

----

.. _lambda:

អនុគមន៍ ``lambda``
===================

``lambda`` បង្កើតអនុគមន៍អនាមិក (anonymous) ដែលមាន **expression តែមួយ**៖

.. code-block:: pycon

   >>> square = lambda x: x ** 2
   >>> square(6)
   36

   >>> pairs = [(1, "b"), (3, "a"), (2, "c")]
   >>> sorted(pairs, key=lambda p: p[1])
   [(3, 'a'), (1, 'b'), (2, 'c')]

.. note::

   * ``lambda`` អាចមាន parameter ច្រើន ប៉ុន្តែខ្លួនវាត្រូវតែជា
     **expression តែមួយ** — មិនអាចមាន statement (``if`` block, ``for``,
     ``return``) បានទេ។
   * ``lambda`` មាន scope local របស់វាផ្ទាល់ ដូចអនុគមន៍ ``def``។
   * ``lambda`` មិនត្រូវបានកំណត់ឱ្យធ្វើឱ្យកូដខ្លីជាងទេ — វាមានប្រយោជន៍
     នៅពេលអ្នកត្រូវការអនុគមន៍តូចមួយជា argument។

.. warning::

   កុំផ្ដល់ ``lambda`` ទៅអថេរ៖

   .. code-block:: python

      # ❌ មិនត្រឹមត្រូវ
      f = lambda x: x * 2

      # ✅
      def f(x):
          return x * 2

   ហេតុផលគឺ traceback មិនអាចបង្ហាញឈ្មោះអនុគមន៍មានន័យបានទេ។

----

.. _annotations:

Function Annotation (Type Hint)
===================================

Annotation គឺជាព័ត៌មានប្រភេទ **ស្រេចចិត្ត** សម្រាប់ parameter និងតម្លៃ
ត្រឡប់។ Python **មិនពិនិត្យ** វានៅពេលដំណើរការទេ — ឧបករណ៍ដូចជា
``mypy``, ``pyright`` និង IDE ប្រើវា៖

.. code-block:: python

   def greet(name: str, times: int = 1) -> str:
       """ត្រឡប់ពាក្យសួស្ដីដែលបានបញ្ចូលគ្នា times ដង។"""
       return f"សួស្ដី {name}! " * times

   def scores() -> dict[str, int]:
       return {"math": 90}

.. code-block:: pycon
   :no-test:

   >>> greet("សុខា", 2)
   'សួស្ដី សុខា! សួស្ដី សុខា! '
   >>> greet.__annotations__
   {'name': <class 'str'>, 'times': <class 'int'>, 'return': <class 'str'>}
   >>> greet(42)                # Python មិនរារាំងទេ!
   'សួស្ដី 42! '

..  :no-test: — ឧទាហរណ៍នេះត្រូវបានផ្ទៀងផ្ទាត់ដោយឡែកជា script ពិត
..  (មើល ``REAL_SCRIPT_CHECKS`` ក្នុង ``tools/run_examples.py``)។
..  មូលហេតុ៖ PEP 649 (Python 3.14+) ដោះស្រាយ annotation របស់អនុគមន៍
..  ធៀបនឹង module ពិតប្រាកដរបស់វា។ ការដំណើរការកូដដដែលតាមរយៈ ``exec()``
..  ក្នុង namespace សាកល្បង អាចធ្វើឱ្យវាធ្លាក់ទៅជា STRING format វិញ
..  ដូច្នេះលទ្ធផលមិនតំណាងឱ្យឥរិយាបថពិតដែលអ្នកអាននឹងឃើញទេ។

.. note::

   ``dict[str, int]`` (ប្រើប្រភេទ built-in ដោយផ្ទាល់) ត្រូវការ Python 3.9+។
   មុននោះត្រូវប្រើ ``typing.Dict[str, int]``។ សម្រាប់ annotation ដែលយោង
   ទៅ class ខ្លួនឯង ឬទៅឈ្មោះដែលមិនទាន់មាន ប្រើខ្សែអក្សរ
   ``-> "MyClass"`` ឬ ``from __future__ import annotations``។

   សូមមើលជំពូក *Type Hints* (មិនទាន់បានសរសេរ) សម្រាប់ព័ត៌មានលម្អិត។

----

.. _recursion:

អនុគមន៍ហៅខ្លួនឯង (Recursion)
=============================

អនុគមន៍អាចហៅខ្លួនឯងបាន។ ការហៅម្ដងៗបង្កើត symbol table local ថ្មី៖

.. code-block:: python

   def factorial(n):
       """ត្រឡប់ n! ដោយប្រើ recursion។"""
       if n <= 1:              # base case — ចាំបាច់!
           return 1
       return n * factorial(n - 1)

.. code-block:: pycon

   >>> factorial(5)
   120
   >>> factorial(0)
   1

.. warning::

   រាល់អនុគមន៍ recursive ត្រូវតែមាន **base case** ដែលឈប់ការហៅខ្លួនឯង។
   បើគ្មាន អ្នកនឹងទទួល ``RecursionError``៖

   .. code-block:: pycon

      >>> def forever():
      ...     return forever()
      ...
      >>> forever()
      Traceback (most recent call last):
        ...
      RecursionError: maximum recursion depth exceeded

   ដែនកំណត់លំនាំដើមគឺ ១០០០ ជាន់។ ពិនិត្យដោយ
   ``sys.getrecursionlimit()`` ហើយកែដោយ ``sys.setrecursionlimit(n)``
   (ប៉ុន្តែកុំកំណត់ខ្ពស់ពេក — អាចបណ្ដាលឱ្យ crash)។

.. tip::

   សម្រាប់បញ្ហាដែលដោះស្រាយបានដោយរង្វិលជុំ សូមប្រើរង្វិលជុំ។
   Recursion សមស្របសម្រាប់រចនាសម្ព័ន្ធដែលមានភាពជាន់ៗគ្នា
   (ដើមឈើ ឯកសារ JSON លើសពីមួយកម្រិត)។ Python មិនបានធ្វើ
   *tail call optimization* ទេ។

----

.. _scopes-namespaces:

វិសាលភាព (Scope) និង Namespace
==================================

.. _namespace:

Namespace គឺជាអ្វី?
-------------------

**Namespace** គឺជាផែនទីពី **ឈ្មោះ** ទៅ **object**។ Namespace ភាគច្រើន
ត្រូវបានអនុវត្តជា ``dict`` ខាងក្នុង។

ឧទាហរណ៍នៃ namespace៖

* ឈ្មោះ built-in (``abs``, ``len``, ``print``, ``ValueError``, …)
* ឈ្មោះ global ក្នុង module មួយ
* ឈ្មោះ local ក្នុងការហៅអនុគមន៍មួយ
* attribute របស់ object មួយ

ចំណុចសំខាន់បំផុត៖ **គ្មានទំនាក់ទំនងរវាងឈ្មោះក្នុង namespace ផ្សេងគ្នា**។
module ពីរអាចមានអនុគមន៍ឈ្មោះ ``maximize`` ដូចគ្នាដោយមិនមានជម្លោះ —
អ្នកប្រើត្រូវដាក់ឈ្មោះ module នៅមុខ។

.. _namespace-lifetime:

អាយុកាលនៃ Namespace
---------------------

.. list-table::
   :header-rows: 1
   :widths: 26 74

   * - Namespace
     - បង្កើតពេលណា · បំផ្លាញពេលណា
   * - built-in
     - ពេល interpreter ចាប់ផ្ដើម · មិនដែលលុប
   * - module global
     - ពេល module ត្រូវបានអាន · ជាធម្មតារហូតដល់ interpreter បញ្ចប់
   * - function local
     - ពេលអនុគមន៍ត្រូវបានហៅ · ពេលអនុគមន៍ត្រឡប់ ឬបញ្ចេញ exception
       ដែលមិនបានចាប់យក

.. note::

   statement ដែលដំណើរការនៅកម្រិតខ្ពស់បំផុត (top-level) ត្រូវបានចាត់ទុក
   ជាផ្នែកនៃ module ឈ្មោះ ``__main__``។ ឈ្មោះ built-in រស់នៅក្នុង module
   ឈ្មោះ ``builtins``។

   .. code-block:: pycon

      >>> import builtins
      >>> builtins.__name__
      'builtins'
      >>> len(dir(builtins)) > 150      # ១៦៣ ឈ្មោះ built-in ក្នុង Python 3.15
      True

.. _scope:

Scope គឺជាអ្វី?
----------------

**Scope** គឺជាតំបន់អក្សរ (textual region) នៃកម្មវិធី Python ដែល namespace
មួយអាចចូលដំណើរការ **ដោយផ្ទាល់**។ "ដោយផ្ទាល់" មានន័យថា ការយោងទៅឈ្មោះ
ដោយមិនមានបុព្វបទ នឹងព្យាយាមស្វែងរកឈ្មោះនោះក្នុង namespace នេះ។

នៅពេលណាក៏ដោយកំឡុងពេលដំណើរការ មាន scope ជាន់ៗគ្នា ៣ ឬ ៤
ដែលអាចចូលដំណើរការដោយផ្ទាល់។ នេះហៅថា **LEGB**៖

.. list-table::
   :header-rows: 1
   :widths: 16 24 60

   * - លំដាប់
     - Scope
     - មានអ្វី
   * - **L**
     - Local
     - ស្វែងរកមុនគេ — ឈ្មោះ local នៃអនុគមន៍បច្ចុប្បន្ន
   * - **E**
     - Enclosing
     - ឈ្មោះក្នុងអនុគមន៍ដែលរុំព័ទ្ធ (ចាប់ពីជិតបំផុតចេញក្រៅ)
   * - **G**
     - Global
     - ឈ្មោះ global នៃ module បច្ចុប្បន្ន
   * - **B**
     - Built-in
     - ស្វែងរកចុងក្រោយ — ឈ្មោះ built-in

.. code-block:: python

   name = "global"        # G — module level

   def outer():
       name = "enclosing"  # E

       def inner():
           name = "local"   # L
           print(name)      # → "local"

       inner()

   outer()

.. code-block:: pycon

   >>> print(name)          # នៅ module level → G
   global

.. _scopes-textual:

Scope ត្រូវបានកំណត់តាមអក្សរ
----------------------------

ចំណុចសំខាន់មួយដែលមនុស្សជាច្រើនយល់ច្រឡំ៖ **scope ត្រូវបានកំណត់តាម
អក្សរ** (statically) ប៉ុន្តែ **ប្រើតាមពេលដំណើរការ** (dynamically)។

scope global នៃអនុគមន៍មួយ គឺជា namespace នៃ **module ដែលកំណត់អនុគមន៍នោះ**
— មិនមែន module ដែលហៅវាទេ៖

.. code-block:: python
   :no-test:

   # ឯកសារ module_a.py
   counter = 0

   def increment():
       global counter
       counter += 1
       return counter

.. code-block:: python
   :no-test:

   # ឯកសារ module_b.py
   import module_a

   counter = 100          # អថេរផ្សេងដាច់ស្រឡះពី module_a.counter

   module_a.increment()   # ប៉ះពាល់ module_a.counter មិនមែន counter នៅទីនេះ
   print(counter)         # 100
   print(module_a.counter)  # 1

.. note::

   នេះមានន័យថា អថេរ global ដែលត្រូវបានយោងក្នុងអនុគមន៍ គឺជាអថេរ global
   នៃ module ដែល **មានកូដអនុគមន៍នោះ** — ទោះបីជាអនុគមន៍ត្រូវបានហៅពី
   module ផ្សេងក៏ដោយ។

   លើសពីនេះ នៅពេល class ត្រូវបានកំណត់ វាបង្កើត namespace ថ្មីមួយទៀត
   សម្រាប់ខ្លួនវា។ សូមមើលជំពូក *Classes និង OOP* (មិនទាន់បានសរសេរ)។

.. _local-assignment:

ការផ្ដល់តម្លៃបង្កើតអថេរ Local
---------------------------------

លក្ខណៈពិសេសមួយរបស់ Python៖ បើគ្មានពាក្យបញ្ជា ``global`` ឬ ``nonlocal``
ទេ **ការផ្ដល់តម្លៃ** ទៅឈ្មោះណាមួយក្នុងអនុគមន៍ តែងតែបង្កើតអថេរ local
នៅក្នុង scope ខាងក្នុងបំផុត។

.. code-block:: pycon

   >>> count = 0
   >>> def bump():
   ...     count = count + 1     # ❌ count ខាងស្ដាំត្រូវបានចាត់ទុកជា local
   ...
   >>> bump()
   Traceback (most recent call last):
     ...
   UnboundLocalError: cannot access local variable 'count' where it is not associated with a value

Python ឃើញ ``count = ...`` ហើយសម្រេចថា ``count`` ជាអថេរ local សម្រាប់
អនុគមន៍ទាំងមូល។ ដូច្នេះការ **អាន** ``count`` នៅខាងស្ដាំបរាជ័យ ព្រោះវា
មិនទាន់មានតម្លៃ។

.. _global-statement:

ពាក្យបញ្ជា ``global``
---------------------

``global`` ប្រាប់ Python ថាឈ្មោះនេះស្ថិតនៅក្នុង scope global ហើយត្រូវ
ផ្ដល់តម្លៃនៅទីនោះ៖

.. code-block:: pycon

   >>> counter = 0
   >>> def increment():
   ...     global counter
   ...     counter += 1
   ...     return counter
   ...
   >>> increment()
   1
   >>> increment()
   2
   >>> counter
   2

**ការអាន** អថេរ global មិនត្រូវការ ``global`` ទេ — មានតែការ **សរសេរ** ប៉ុណ្ណោះ៖

.. code-block:: pycon

   >>> PI = 3.14159
   >>> def circle_area(r):
   ...     return PI * r ** 2      # អាន PI — មិនត្រូវការ global
   ...
   >>> circle_area(2)
   12.56636

.. _nonlocal-statement:

ពាក្យបញ្ជា ``nonlocal``
-----------------------

``nonlocal`` ធ្វើដូច ``global`` ប៉ុន្តែសម្រាប់ scope នៃអនុគមន៍ដែល
**រុំព័ទ្ធ** (enclosing) — មិនមែន global ទេ៖

.. code-block:: pycon

   >>> def make_counter():
   ...     hits = 0
   ...     def increment():
   ...         nonlocal hits       # ចងទៅ hits របស់ make_counter
   ...         hits += 1
   ...         return hits
   ...     return increment
   ...
   >>> counter = make_counter()
   >>> counter()
   1
   >>> counter()
   2
   >>> hits                        # មិនមាននៅ module level
   Traceback (most recent call last):
     ...
   NameError: name 'hits' is not defined

.. warning::

   ``nonlocal`` តម្រូវឱ្យមានឈ្មោះនោះនៅក្នុង scope រុំព័ទ្ធ **ពិតប្រាកដ**។
   បើគ្មាន វានឹងបញ្ចេញ ``SyntaxError`` ក្នុងពេល compile។

.. tip::

   ការប្រើ ``global`` ច្រើនពេកធ្វើឱ្យកូដពិបាកសាកល្បង និងពិបាកយល់។
   ជម្រើសល្អជាងគឺ **បញ្ជូនតម្លៃចូល និងត្រឡប់តម្លៃចេញ**។ ប្រើ ``global``
   សម្រាប់ថេរកម្រិត module ឬការកំណត់រចនាសម្ព័ន្ធដែលចាំបាច់ពិតប្រាកដប៉ុណ្ណោះ។

.. _shadowing:

ការបិទបាំងឈ្មោះ (Shadowing)
-----------------------------

អថេរ local អាច **បិទបាំង** ឈ្មោះនៅ scope ខាងក្រៅ៖

.. code-block:: pycon

   >>> x = "global"
   >>> def show():
   ...     x = "local"
   ...     print(x)
   ...
   >>> show()
   local
   >>> x
   'global'

កំហុសដែលគ្រោះថ្នាក់បំផុតគឺការបិទបាំង **built-in**៖

.. code-block:: pycon

   >>> def process(data):
   ...     list = data.split(",")    # ❌ បិទបាំង built-in list
   ...     return len(list)
   ...
   >>> process("a,b,c")
   3
   >>> list("abc")                   # ដំណើរការនៅ module level
   ['a', 'b', 'c']

ប៉ុន្តែបើការបិទបាំងកើតឡើងនៅ module level វា **បំផ្លាញ** built-in
សម្រាប់ module ទាំងមូល៖

.. code-block:: pycon

   >>> sum = 0                  # ❌ បិទបាំង built-in sum() នៅ module level
   >>> sum([1, 2, 3])
   Traceback (most recent call last):
     ...
   TypeError: 'int' object is not callable
   >>> del sum                  # ស្ដារឡើងវិញក្នុង session
   >>> sum([1, 2, 3])
   6

.. _closures:

Closure
===========

អនុគមន៍ខាងក្នុងអាច **ចងចាំ** តម្លៃពី scope រុំព័ទ្ធ សូម្បីតែបន្ទាប់ពី
អនុគមន៍ខាងក្រៅបានត្រឡប់រួច។ នេះហៅថា **closure**៖

.. code-block:: pycon

   >>> def multiplier(n):
   ...     def multiply(x):
   ...         return x * n          # n ត្រូវបានចងចាំ
   ...     return multiply
   ...
   >>> double = multiplier(2)
   >>> triple = multiplier(3)
   >>> double(10)
   20
   >>> triple(10)
   30
   >>> double.__closure__[0].cell_contents
   2

.. note::

   Closure គឺជាមូលដ្ឋាននៃ **decorator** (មើលជំពូក *Decorators* —
   មិនទាន់បានសរសេរ)។

.. _class-scope-note:

ចំណាំអំពី Class Scope
----------------------

Class បង្កើត namespace ថ្មីមួយទៀត ប៉ុន្តែវាមានលក្ខណៈពិសេស៖ class body
**មិនមែន** ជា enclosing scope សម្រាប់អនុគមន៍ដែលកំណត់ក្នុងវាទេ។

.. code-block:: pycon

   >>> class Demo:
   ...     value = 10
   ...     def show(self):
   ...         return value          # ❌ មើលមិនឃើញ Demo.value ទេ
   ...
   >>> Demo().show()
   Traceback (most recent call last):
     ...
   NameError: name 'value' is not defined. Did you mean: 'self.value'?

   >>> class Demo2:
   ...     value = 10
   ...     def show(self):
   ...         return self.value     # ✅
   ...     def show_class(self):
   ...         return Demo2.value    # ✅ ឬ type(self).value
   ...
   >>> Demo2().show()
   10

ហេតុផលគឺថា អនុគមន៍ក្នុង class ទទួលបាន scope local ផ្ទាល់របស់វា ហើយ
ឈ្មោះ class ត្រូវបានស្វែងរកតាមលំដាប់ LEGB ធម្មតា (មិនមាន class scope
នៅចន្លោះ L និង G)។

----

.. _functions-summary:

សង្ខេប
======

* ``def`` កំណត់អនុគមន៍។ Docstring គឺជាខ្សែអក្សរដំបូងក្នុងខ្លួន។
* អនុគមន៍ត្រឡប់ ``None`` បើគ្មាន ``return``។
* អនុគមន៍គឺជា **object** — អាចផ្ដល់ បញ្ជូន និងរក្សាទុកបាន។
* Argument ត្រូវបានបញ្ជូនដោយ **object reference**។
* កុំប្រើ object mutable ជាតម្លៃលំនាំដើម — ប្រើ ``None`` ជា sentinel។
* ``/`` កំណត់ positional-only; ``*`` កំណត់ keyword-only។
* ``*args`` ប្រមូល positional; ``**kwargs`` ប្រមូល keyword។
* ការផ្ដល់តម្លៃក្នុងអនុគមន៍តែងតែបង្កើតអថេរ **local** លើកលែងតែមាន
  ``global`` ឬ ``nonlocal``។
* លំដាប់ស្វែងរកឈ្មោះគឺ **LEGB**៖ Local → Enclosing → Global → Built-in។
* កុំបិទបាំង built-in ដោយដាក់ឈ្មោះអថេរដូចវា។

.. rubric:: ប្រភពយោង

* `Defining Functions <https://docs.python.org/3/tutorial/controlflow.html#defining-functions>`_
* `More on Defining Functions <https://docs.python.org/3/tutorial/controlflow.html#more-on-defining-functions>`_
* `Default Argument Values <https://docs.python.org/3/tutorial/controlflow.html#default-argument-values>`_
* `Keyword Arguments <https://docs.python.org/3/tutorial/controlflow.html#keyword-arguments>`_
* `Special parameters <https://docs.python.org/3/tutorial/controlflow.html#special-parameters>`_
* `Arbitrary Argument Lists <https://docs.python.org/3/tutorial/controlflow.html#arbitrary-argument-lists>`_
* `Lambda Expressions <https://docs.python.org/3/tutorial/controlflow.html#lambda-expressions>`_
* `Function Annotations <https://docs.python.org/3/tutorial/controlflow.html#function-annotations>`_
* `Python Scopes and Namespaces <https://docs.python.org/3/tutorial/classes.html#python-scopes-and-namespaces>`_
* `PEP 570 — Python Positional-Only Parameters <https://peps.python.org/pep-0570/>`_
* `PEP 3102 — Keyword-Only Arguments <https://peps.python.org/pep-3102/>`_
