.. _testing-debugging:

.. container:: src-note

   ប្រភពដើម៖ CPython ``Doc/library/unittest.rst``, ``Doc/library/doctest.rst``,
   ``Doc/library/pdb.rst``, ``Doc/library/timeit.rst``,
   ``Doc/develop/testing.rst``, ``Doc/library/logging.rst`` ·
   `ឯកសារផ្លូវការ <https://docs.python.org/3/library/unittest.html>`_

###########################################
Testing, Debugging និង Best Practices
###########################################

.. _why-test:

ហេតុអ្វីត្រូវសាកល្បង?
=========================

.. list-table::
   :header-rows: 1
   :widths: 26 74

   * - អត្ថប្រយោជន៍
     - ការពន្យល់
   * - រកកំហុសមុនអ្នកប្រើ
     - test ដែលដំណើរការស្វ័យប្រវត្តិរកឃើញ regression ភ្លាម
   * - Refactor ដោយទំនុកចិត្ត
     - បើ test នៅឆ្លង អ្នកដឹងថាអាកប្បកិរិយាមិនបានប្រែប្រួល
   * - ឯកសារដែលមានជីវិត
     - test បង្ហាញពីរបៀបប្រើ API — វាមិនអាចខុសពីកូដបានទេ
   * - រចនាល្អជាង
     - កូដដែលងាយសាកល្បង ជាធម្មតាមាន coupling ទាប និងទំនួលខុសត្រូវតែមួយ

.. _test-pyramid:

Test Pyramid
------------

.. code-block:: text

        /\        ← End-to-end (តិច យឺត ថ្លៃ)
       /  \
      /----\      ← Integration (មធ្យម)
     /      \
    /--------\    ← Unit (ច្រើន លឿន ថោក)

* **Unit test** — សាកល្បងអនុគមន៍ ឬ class តែមួយ ដាច់ដោយឡែក។
  សរសេរច្រើនបំផុត។
* **Integration test** — សាកល្បងផ្នែកច្រើនធ្វើការជាមួយគ្នា
  (database, API, ឯកសារ)។
* **End-to-end test** — សាកល្បងកម្មវិធីទាំងមូលពីមុខអ្នកប្រើ។
  សរសេរតិចបំផុត ព្រោះយឺត និងងាយបែក។

.. _doctest:

``doctest`` — សាកល្បងពីឧទាហរណ៍
==============================

``doctest`` ស្វែងរកឧទាហរណ៍ដែលមានទម្រង់ REPL (``>>>``) ក្នុង docstring
ហើយដំណើរការវា៖

.. code-block:: python

   def celsius_to_fahrenheit(celsius: float) -> float:
       """បំលែង Celsius ទៅ Fahrenheit។

       >>> celsius_to_fahrenheit(0)
       32.0
       >>> celsius_to_fahrenheit(100)
       212.0
       >>> round(celsius_to_fahrenheit(-40), 1)
       -40.0
       """
       return celsius * 9 / 5 + 32

.. code-block:: pycon

   >>> import doctest
   >>> doctest.run_docstring_examples(
   ...     celsius_to_fahrenheit,
   ...     {"celsius_to_fahrenheit": celsius_to_fahrenheit},
   ...     verbose=False,
   ... )
   >>> celsius_to_fahrenheit(0)
   32.0
   >>> celsius_to_fahrenheit(100)
   212.0

**ដំណើរការពីបន្ទាត់ពាក្យបញ្ជា៖**

.. code-block:: console

   $ python3 -m doctest -v temperature.py
   Trying:
       celsius_to_fahrenheit(0)
   Expecting:
       32.0
   ok
   1 items passed all tests

.. list-table:: Directive សំខាន់ៗ
   :header-rows: 1
   :widths: 30 70

   * - Directive
     - ការប្រើប្រាស់
   * - ``# doctest: +ELLIPSIS``
     - អនុញ្ញាត ``...`` ជា wildcard
   * - ``# doctest: +SKIP``
     - រំលងឧទាហរណ៍នេះ
   * - ``# doctest: +NORMALIZE_WHITESPACE``
     - មិនអើពើដកឃ្លាខុសគ្នា
   * - ``# doctest: -IGNORE_EXCEPTION_DETAIL``
     - ប្រៀបធៀបតែប្រភេទ exception

.. tip::

   ``doctest`` ល្អសម្រាប់ **ឯកសារដែលអាចផ្ទៀងផ្ទាត់បាន** — ឧទាហរណ៍ក្នុង
   docstring របស់អ្នកនឹងមិនអាចខុសពីកូដបានទេ។ ប៉ុន្តែវា **មិនគ្រប់គ្រាន់**
   សម្រាប់ការសាកល្បងពេញលេញទេ — ប្រើ ``unittest`` ឬ ``pytest`` ផង។

.. _unittest:

``unittest``
============

``unittest`` គឺជា framework សាកល្បងស្តង់ដារដែលមកជាមួយ Python។

.. _unittest-example:

ឧទាហរណ៍ពេញលេញ
----------------

.. literalinclude:: _code/test_calculator.py
   :language: python
   :caption: ``test_calculator.py``

.. code-block:: console

   $ python3 -m unittest test_calculator -v
   test_add (test_calculator.TestCalculator.test_add) ... ok
   test_divide_by_zero (test_calculator.TestCalculator.test_divide_by_zero) ... ok
   test_multiply (test_calculator.TestCalculator.test_multiply) ... ok

   ----------------------------------------------------------------------
   Ran 3 tests in 0.000s

   OK

.. _unittest-structure:

រចនាសម្ព័ន្ធ
----------------

.. list-table::
   :header-rows: 1
   :widths: 34 66

   * - ធាតុ
     - ច្បាប់
   * - ឯកសារ
     - ឈ្មោះចាប់ផ្ដើមដោយ ``test_`` ឬបញ្ចប់ដោយ ``_test.py``
   * - Class
     - បន្តពូជពី ``unittest.TestCase`` · ឈ្មោះចាប់ផ្ដើមដោយ ``Test``
   * - Method
     - ឈ្មោះចាប់ផ្ដើមដោយ ``test_``
   * - Setup / teardown
     - ``setUp()``, ``tearDown()``, ``setUpClass()``, ``tearDownClass()``

.. _assertions:

Assertion សំខាន់ៗ
------------------

.. list-table::
   :header-rows: 1
   :widths: 40 60

   * - Method
     - ពិនិត្យ
   * - ``assertEqual(a, b)``
     - ``a == b``
   * - ``assertNotEqual(a, b)``
     - ``a != b``
   * - ``assertTrue(x)`` / ``assertFalse(x)``
     - ``bool(x)`` ពិត / មិនពិត
   * - ``assertIs(a, b)`` / ``assertIsNot``
     - ``a is b``
   * - ``assertIsNone(x)`` / ``assertIsNotNone``
     - ``x is None``
   * - ``assertIn(a, b)`` / ``assertNotIn``
     - ``a in b``
   * - ``assertIsInstance(a, b)``
     - ``isinstance(a, b)``
   * - ``assertAlmostEqual(a, b, places=7)``
     - ខិតជិតគ្នា (សម្រាប់ float)
   * - ``assertRaises(Exc)``
     - បញ្ចេញ exception
   * - ``assertRaisesRegex(Exc, pattern)``
     - exception ជាមួយសារដែលផ្គូផ្គង
   * - ``assertLogs(level=…)``
     - មាន log កើតឡើង
   * - ``assertWarns(Warning)``
     - បញ្ចេញ warning
   * - ``assertDictEqual``, ``assertListEqual``, …
     - ប្រៀបធៀបប្រភេទជាក់លាក់ (សារកំហុសលម្អិតជាង)

.. code-block:: python

   import math
   import unittest


   class TestAssertions(unittest.TestCase):
       def test_floats(self):
           # ❌ មិនអាចទុកចិត្ត: 0.1 + 0.2 != 0.3
           self.assertAlmostEqual(0.1 + 0.2, 0.3, places=7)
           self.assertTrue(math.isclose(0.1 + 0.2, 0.3))

       def test_exceptions(self):
           with self.assertRaises(ZeroDivisionError):
               1 / 0
           with self.assertRaisesRegex(ValueError, "invalid literal"):
               int("abc")

       def test_containers(self):
           self.assertEqual([1, 2], [1, 2])
           self.assertIn("a", {"a": 1})
           self.assertIsInstance(3, int)

.. warning::

   ប្រើ ``assertAlmostEqual`` ឬ ``math.isclose()`` សម្រាប់ **float** —
   កុំប្រើ ``assertEqual``។ មើលជំពូក :doc:`syntax_variables_types`
   សម្រាប់ហេតុផល។

.. _setup-teardown:

``setUp`` និង ``tearDown``
------------------------------

.. code-block:: python

   import unittest
   from pathlib import Path


   class TestFileOps(unittest.TestCase):
       def setUp(self):
           """ដំណើរការមុន test នីមួយៗ។"""
           self.tmp = Path("test_data.txt")
           self.tmp.write_text("មាតិកា", encoding="utf-8")

       def tearDown(self):
           """ដំណើរការក្រោយ test នីមួយៗ — សូម្បីតែបើ test បរាជ័យ។"""
           self.tmp.unlink(missing_ok=True)

       def test_read(self):
           self.assertEqual(self.tmp.read_text(encoding="utf-8"), "មាតិកា")

.. tip::

   ប្រើ ``addCleanup()`` ឬ context manager ជំនួស ``tearDown`` បើអ្នកមាន
   ការសម្អាតច្រើន — វាដំណើរការតាមលំដាប់ច្រាស (LIFO) ហើយមិនអាចបំភ្លេចបាន៖

   .. code-block:: python
      :no-test:

      def setUp(self):
          self.conn = connect()
          self.addCleanup(self.conn.close)

.. _subtest:

``subTest`` — សាកល្បងករណីច្រើនក្នុង test មួយ
--------------------------------------------

.. code-block:: python

   import unittest


   class TestIsEven(unittest.TestCase):
       def test_many_values(self):
           cases = [(0, True), (1, False), (2, True), (-3, False), (100, True)]
           for value, expected in cases:
               with self.subTest(value=value):
                   self.assertEqual(value % 2 == 0, expected)

.. note::

   បើគ្មាន ``subTest`` test នឹង **ឈប់** នៅកំហុសដំបូង។ ជាមួយ
   ``subTest`` វាបន្តសាកល្បងករណីដែលនៅសល់ ហើយរាយការណ៍កំហុសទាំងអស់ —
   អ្នកឃើញបញ្ហាទាំងមូលក្នុងការដំណើរការម្ដង។

.. _skip:

ការរំលង និងកំហុសដែលរំពឹងទុក
---------------------------

.. code-block:: python

   import sys
   import unittest


   class TestSkips(unittest.TestCase):
       @unittest.skip("មិនទាន់អនុវត្ត")
       def test_future_feature(self):
           self.fail("មិនគួរដំណើរការ")

       @unittest.skipIf(sys.platform == "win32", "Unix តែប៉ុណ្ណោះ")
       def test_unix_only(self):
           pass

       @unittest.skipUnless(sys.version_info >= (3, 12), "ត្រូវការ 3.12+")
       def test_modern_feature(self):
           pass

       @unittest.expectedFailure
       def test_known_bug(self):
           self.assertEqual(1, 2)          # រំពឹងថាបរាជ័យ

.. _mock:

``unittest.mock`` — ជំនួស dependency
========================================

``mock`` អនុញ្ញាតឱ្យអ្នកជំនួស object ពិត (API, database, ពេលវេលា)
ដោយ object ក្លែងដែលអ្នកគ្រប់គ្រងបាន៖

.. code-block:: python

   from unittest import mock


   def fetch_temperature(city: str) -> float:
       """ហៅ API អាកាសធាតុ (ឧទាហរណ៍)។"""
       import urllib.request

       with urllib.request.urlopen(f"https://api.example.com/{city}") as r:
           return float(r.read().decode())

.. code-block:: pycon

   >>> with mock.patch("urllib.request.urlopen") as fake:
   ...     fake.return_value.__enter__.return_value.read.return_value = b"27.5"
   ...     result = fetch_temperature("phnom-penh")
   ...
   >>> result
   27.5
   >>> fake.called, fake.call_count
   (True, 1)

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - ឧបករណ៍
     - ការប្រើប្រាស់
   * - ``mock.patch(target)``
     - ជំនួស object ក្នុង module ណាមួយជាបណ្ដោះអាសន្ន
   * - ``mock.MagicMock()``
     - object ក្លែងដែលឆ្លើយតបទៅ method ណាក៏បាន
   * - ``mock.Mock(return_value=x)``
     - object ក្លែងដែលត្រឡប់តម្លៃកំណត់
   * - ``m.called`` / ``m.call_count``
     - តើបានហៅប៉ុន្មានដង
   * - ``m.call_args`` / ``m.call_args_list``
     - argument នៃការហៅ
   * - ``m.assert_called_once_with(...)``
     - ផ្ទៀងផ្ទាត់ការហៅជាក់លាក់
   * - ``mock.patch.object(obj, "attr")``
     - ជំនួស attribute នៃ object
   * - ``mock.patch.dict(os.environ, {...})``
     - ជំនួស dict (ឧ. អថេរបរិស្ថាន)

.. warning::

   កុំ mock ច្រើនពេក។ បើ test របស់អ្នកមាន ``mock.patch`` ច្រើនជាងកូដ
   ដែលសាកល្បង នោះជាសញ្ញាថារចនាសម្ព័ន្ធមាន coupling ខ្ពស់ពេក។
   ជម្រើសល្អជាងគឺ **dependency injection** — បញ្ជូន dependency ជា
   argument ជំនួសការហៅវាដោយផ្ទាល់។

.. _running-tests:

ការដំណើរការ Test
================

.. code-block:: console

   # ស្វែងរក និងដំណើរការ test ទាំងអស់
   $ python3 -m unittest discover

   # ឯកសារជាក់លាក់
   $ python3 -m unittest test_calculator

   # class ឬ method ជាក់លាក់
   $ python3 -m unittest test_calculator.TestCalculator.test_add

   # លម្អិត
   $ python3 -m unittest discover -v

   # ឈប់នៅកំហុសដំបូង
   $ python3 -m unittest discover --failfast

.. _pytest:

``pytest`` (ភាគីទីបី)
=========================

``pytest`` គឺជា framework ដែលពេញនិយមបំផុតក្នុងសហគមន៍ Python។
វាដំណើរការ test ``unittest`` បានដែរ ប៉ុន្តែផ្ដល់វាក្យសម្ពន្ធសាមញ្ញជាង៖

.. code-block:: python
   :no-test:

   # test_example.py — pytest style
   def add(a, b):
       return a + b


   def test_add():
       assert add(2, 3) == 5


   def test_add_negative():
       assert add(-1, -1) == -2


   import pytest


   @pytest.mark.parametrize("value, expected", [(0, 0), (1, 1), (5, 25)])
   def test_square(value, expected):
       assert value ** 2 == expected

.. code-block:: console

   $ pip install pytest
   $ pytest -v
   ============================= test session starts ==============================
   collected 5 items

   test_example.py::test_add PASSED
   test_example.py::test_add_negative PASSED
   test_example.py::test_square[0-0] PASSED
   test_example.py::test_square[1-1] PASSED
   test_example.py::test_square[5-25] PASSED

   =============================== 5 passed in 0.02s ===============================

.. list-table::
   :header-rows: 1
   :widths: 34 33 33

   * -
     - ``unittest``
     - ``pytest``
   * - មកជាមួយ Python
     - ✅
     - ❌ (``pip install``)
   * - វាក្យសម្ពន្ធ
     - class + method
     - អនុគមន៍ធម្មតា + ``assert``
   * - សារកំហុស
     - សាមញ្ញ
     - លម្អិត (assertion rewriting)
   * - Fixture
     - ``setUp``/``tearDown``
     - ``@pytest.fixture`` (ខ្លាំងជាង)
   * - Parametrize
     - ``subTest``
     - ``@pytest.mark.parametrize``
   * - Plugin
     - មានកម្រិត
     - ច្រើនណាស់ (``pytest-cov``, ``pytest-xdist``)
   * - ដំណើរការ test ``unittest``
     - —
     - ✅

.. tip::

   សម្រាប់គម្រោងថ្មី ភាគច្រើនជ្រើសរើស ``pytest``។ សម្រាប់កូដដែលមាន
   ``unittest`` រួចហើយ អ្នកអាចដំណើរការវាជាមួយ ``pytest`` ដោយមិន
   ប្ដូរអ្វីសោះ។

.. _coverage:

Code Coverage
-------------

Coverage វាស់ថា **ប៉ុន្មានភាគរយ** នៃកូដរបស់អ្នកត្រូវបានសាកល្បង៖

.. code-block:: console

   $ pip install coverage
   $ coverage run -m unittest discover
   $ coverage report -m
   Name                  Stmts   Miss  Cover   Missing
   ---------------------------------------------------
   calculator.py            42      4    90%   38-41
   ---------------------------------------------------
   TOTAL                    42      4    90%

.. warning::

   **Coverage ១០០% មិនមានន័យថាគ្មាន bug ទេ។** វាគ្រាន់តែបញ្ជាក់ថា
   បន្ទាត់ទាំងអស់ត្រូវបាន **ដំណើរការ** មិនមែនថាត្រូវបាន **ផ្ទៀងផ្ទាត់**
   ទេ។ Test ដែលគ្មាន assertion ក៏រាប់ជា covered ដែរ។

   ប្រើ coverage ជា **ឧបករណ៍រកកន្លែងដែលមិនទាន់សាកល្បង** មិនមែនជា
   គោលដៅទេ។

.. _debugging:

ការ Debug
=========

.. _traceback:

អាន Traceback
-------------

សូមមើលជំពូក :doc:`exceptions` សម្រាប់ការណែនាំពេញលេញ។ សង្ខេប៖

#. អាន **បន្ទាត់ចុងក្រោយ** — ប្រភេទកំហុស និងសារ
#. អាន **frame ចុងក្រោយ** — ឯកសារ បន្ទាត់ អនុគមន៍
#. Python 3.11+ បង្ហាញ ``^^^^`` ចង្អុលទៅផ្នែកជាក់លាក់នៃ expression

.. _pdb:

``pdb`` — Python Debugger
-------------------------

.. code-block:: python

   def buggy_average(numbers):
       breakpoint()                 # ឈប់នៅទីនេះ ហើយបើក pdb
       return sum(numbers) / len(numbers)

.. code-block:: console

   $ python3 app.py
   > /home/user/app.py(3)buggy_average()
   -> return sum(numbers) / len(numbers)
   (Pdb) numbers
   [1, 2, 3]
   (Pdb) len(numbers)
   3
   (Pdb) sum(numbers)
   6
   (Pdb) continue

.. list-table:: ពាក្យបញ្ជា ``pdb`` សំខាន់ៗ
   :header-rows: 1
   :widths: 24 76

   * - ពាក្យបញ្ជា
     - ការប្រើប្រាស់
   * - ``h`` ឬ ``help``
     - ជំនួយ
   * - ``p expr``
     - បោះពុម្ពតម្លៃ
   * - ``pp expr``
     - បោះពុម្ពដោយ ``pprint``
   * - ``l`` (list)
     - បង្ហាញកូដជុំវិញ
   * - ``ll``
     - បង្ហាញអនុគមន៍ទាំងមូល
   * - ``n`` (next)
     - បន្ទាត់បន្ទាប់ (មិនចូលអនុគមន៍)
   * - ``s`` (step)
     - ចូលក្នុងអនុគមន៍
   * - ``c`` (continue)
     - ដំណើរការបន្តរហូតដល់ breakpoint បន្ទាប់
   * - ``r`` (return)
     - ដំណើរការរហូតដល់អនុគមន៍ត្រឡប់
   * - ``b file:line``
     - បន្ថែម breakpoint
   * - ``b``
     - រាយ breakpoint ទាំងអស់
   * - ``cl n``
     - លុប breakpoint លេខ n
   * - ``w`` (where)
     - បង្ហាញ stack trace
   * - ``u`` / ``d``
     - ឡើង / ចុះក្នុង stack
   * - ``!statement``
     - ដំណើរការកូដ Python ក្នុង scope បច្ចុប្បន្ន
   * - ``q`` (quit)
     - ចេញ

.. tip::

   ចាប់ផ្ដើង debugger ដោយផ្ទាល់លើ script៖

   .. code-block:: console

      $ python3 -m pdb app.py            # ឈប់នៅបន្ទាត់ដំបូង
      $ python3 -m pdb -c continue app.py  # ដំណើរការរហូតដល់កំហុស

   **Post-mortem debugging** — ស៊ើបអង្កេតកំហុសដែលបានកើតឡើងរួច៖

   .. code-block:: console

      $ python3 -c "import pdb, sys; ..."
      >>> import pdb
      >>> try:
      ...     1 / 0
      ... except ZeroDivisionError:
      ...     pdb.post_mortem()
      ...

.. _debug-strategies:

យុទ្ធសាស្ត្រ Debug
------------------

.. list-table::
   :header-rows: 1
   :widths: 28 72

   * - យុទ្ធសាស្ត្រ
     - ពេលណាប្រើ
   * - ``breakpoint()`` + ``pdb``
     - បញ្ហាស្មុគស្មាញ ត្រូវការពិនិត្យស្ថានភាព
   * - ``logging.debug()``
     - កូដផលិតកម្ម ឬពេលមិនអាច attach debugger
   * - ``print()``
     - សាកល្បងរហ័ស — ប៉ុន្តែ **កុំភ្លេចលុប**
   * - សរសេរ test ដែលបង្កើតកំហុសឡើងវិញ
     - វិធីល្អបំផុត — អ្នកទទួលបាន regression test ផង
   * - ``python3 -X dev app.py``
     - បើក development mode: warning ច្រើនជាង, ពិនិត្យ resource
   * - ``faulthandler``
     - សម្រាប់ crash កម្រិត C (segfault)
   * - ``git bisect``
     - រក commit ដែលណែនាំ bug

.. code-block:: console

   # Development mode — បើក warning និងការពិនិត្យបន្ថែម
   $ python3 -X dev app.py

   # បើក faulthandler ដោយស្វ័យប្រវត្តិ
   $ PYTHONFAULTHANDLER=1 python3 app.py

.. warning::

   កុំទុក ``print()`` សម្រាប់ debug ក្នុងកូដផលិតកម្ម។ ប្រើ ``logging``
   ដែលអ្នកអាចបិទ/បើក និងកំណត់ទិសដៅបាន។

.. _testing-best-practices:

Best Practices សរុប
===================

.. _zen:

The Zen of Python
-----------------

.. code-block:: console

   $ python3 -c "import this"

.. code-block:: text

   Beautiful is better than ugly.
   Explicit is better than implicit.
   Simple is better than complex.
   Complex is better than complicated.
   Flat is better than nested.
   Sparse is better than dense.
   Readability counts.
   ...

គោលការណ៍សំខាន់ៗដែលអនុវត្តបានភ្លាម៖

.. list-table::
   :header-rows: 1
   :widths: 34 66

   * - គោលការណ៍
     - ការអនុវត្ត
   * - **Readability counts**
     - កូដត្រូវបានអានច្រើនជាងសរសេរ។ ប្រើឈ្មោះច្បាស់លាស់ ដកឃ្លា និងបន្ទាត់ទទេ
   * - **Explicit is better than implicit**
     - បញ្ជាក់ ``encoding``, បញ្ជាក់តម្លៃត្រឡប់ កុំពឹងលើលំនាំដើមដែលមិនច្បាស់
   * - **Flat is better than nested**
     - ប្រើ *early return* ជំនួស ``if`` ជាន់ច្រើន
   * - **Sparse is better than dense**
     - កុំសរសេរបន្ទាត់វែងពេក (អតិបរមា ៧៩–១០០ តួអក្សរ)
   * - **Errors should never pass silently**
     - កុំប្រើ ``except: pass``។ កត់ត្រា ឬបញ្ចេញឡើងវិញ
   * - **There should be one obvious way**
     - កុំសរសេរវិធីពីរដើម្បីធ្វើអ្វីមួយក្នុង codebase តែមួយ

.. _pep8:

PEP 8 — ស្ទីលកូដ
----------------

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - ច្បាប់
     - លក្ខណៈ
   * - Indentation
     - space ៤ (កុំប្រើ tab)
   * - ប្រវែងបន្ទាត់
     - អតិបរមា ៧៩ (ឬ ៨៨/១០០ តាមការព្រមព្រៀងក្រុម)
   * - បន្ទាត់ទទេ
     - ២ រវាង function/class កម្រិតខាងលើ · ១ រវាង method
   * - Import
     - នៅផ្នែកខាងលើ មួយ module មួយបន្ទាត់ ដោយឡែកជាក្រុម
   * - ឈ្មោះអថេរ/អនុគមន៍
     - ``snake_case``
   * - ឈ្មោះ class
     - ``PascalCase``
   * - ថេរ
     - ``UPPER_SNAKE_CASE``
   * - អត្ថាធិប្បាយ
     - ពន្យល់ **ហេតុអ្វី** មិនមែន **អ្វី**
   * - Docstring
     - សម្រាប់ function/class/module សាធារណៈទាំងអស់

.. code-block:: python

   # ❌ មិនតាម PEP 8
   import sys, os
   def CalculateTotal( Items,tax_rate =0.1 ):
       Total=0
       for i in Items:Total=Total+i
       return Total*tax_rate

.. code-block:: python

   # ✅ តាម PEP 8
   from decimal import Decimal


   def calculate_total(items: list[Decimal], tax_rate: Decimal = Decimal("0.1")) -> Decimal:
       """ត្រឡប់ផលបូករួមពន្ធ។"""
       total = sum(items)
       return total * (Decimal(1) + tax_rate)

.. _code-quality:

ឧបករណ៍គុណភាពកូដ
-----------------

.. list-table::
   :header-rows: 1
   :widths: 22 78

   * - ឧបករណ៍
     - តួនាទី
   * - **ruff**
     - linter + formatter សរសេរជា Rust។ លឿនណាស់ ជំនួស ``flake8``, ``isort``, ``pyupgrade`` និងច្រើនទៀត
   * - **black**
     - formatter ដែលមិនអាចប្រកែកបាន ("uncompromising")
   * - **mypy** / **pyright**
     - static type checker
   * - **pytest** + **coverage**
     - សាកល្បង និងវាស់ coverage
   * - **pre-commit**
     - ដំណើរការឧបករណ៍ទាំងអស់ដោយស្វ័យប្រវត្តិមុន commit
   * - **tox** / **nox**
     - សាកល្បងលើកំណែ Python ច្រើន

.. code-block:: yaml

   # .pre-commit-config.yaml
   repos:
     - repo: https://github.com/astral-sh/ruff-pre-commit
       rev: v0.6.9
       hooks:
         - id: ruff
           args: [--fix]
         - id: ruff-format
     - repo: https://github.com/pre-commit/mirrors-mypy
       rev: v1.11.2
       hooks:
         - id: mypy

.. _project-layout:

រចនាសម្ព័ន្ធគម្រោង
------------------

.. code-block:: text

   my-project/
   ├── .gitignore
   ├── .pre-commit-config.yaml
   ├── README.md
   ├── LICENSE
   ├── pyproject.toml
   ├── requirements.txt          (ឬ uv.lock / poetry.lock)
   ├── src/
   │   └── my_project/           ← package ពិត
   │       ├── __init__.py
   │       ├── cli.py
   │       ├── core.py
   │       └── py.typed          ← បញ្ជាក់ថាមាន type hints
   ├── tests/
   │   ├── __init__.py
   │   ├── test_core.py
   │   └── test_cli.py
   └── docs/
       └── ...

.. note::

   រចនាសម្ព័ន្ធ ``src/`` (src layout) ត្រូវបានណែនាំសម្រាប់ package
   ដែលចែកចាយ ព្រោះវាធានាថាអ្នកសាកល្បង **កំណែដែលបានដំឡើង**
   មិនមែនថតប្រភពដោយចៃដន្យទេ។

.. _checklist:

Checklist សម្រាប់កូដ Python ល្អ
-----------------------------------

**រចនាសម្ព័ន្ធ**

* [ ] អនុគមន៍តូច មានទំនួលខុសត្រូវតែមួយ
* [ ] ជម្រៅ nesting មិនលើសពី ៣
* [ ] ឈ្មោះអថេរ/អនុគមន៍ពិពណ៌នាបានច្បាស់
* [ ] មិនមានកូដស្លាប់ (dead code) ឬអត្ថាធិប្បាយដែលបានបិទ

**ភាពជឿជាក់**

* [ ] ប្រើ ``with`` សម្រាប់ធនធានទាំងអស់
* [ ] ចាប់យក exception ជាក់លាក់ មិនមែន ``except:`` ទទេ
* [ ] បញ្ជាក់ ``encoding="utf-8"`` ពេលបើកឯកសារអត្ថបទ
* [ ] គ្មាន mutable default argument
* [ ] ប្រើ ``Decimal`` សម្រាប់លុយ

**ការថែទាំ**

* [ ] Type hints លើ function សាធារណៈ
* [ ] Docstring លើ module, class និង function សាធារណៈ
* [ ] ``if __name__ == "__main__":`` សម្រាប់ script
* [ ] គ្មាន secret ក្នុងកូដ (ប្រើ environment variable)

**ការសាកល្បង**

* [ ] Unit test សម្រាប់ logic សំខាន់ៗ
* [ ] Test ករណីគែម (ទទេ, សូន្យ, អវិជ្ជមាន, ធំពេក)
* [ ] Test ដំណើរការក្នុង CI
* [ ] ``pip check`` ឆ្លង

.. _testing-summary:

សង្ខេប
======

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - ឧបករណ៍
     - ប្រើសម្រាប់
   * - ``doctest``
     - សាកល្បងឧទាហរណ៍ក្នុង docstring
   * - ``unittest``
     - framework សាកល្បងស្តង់ដារ (មកជាមួយ Python)
   * - ``unittest.mock``
     - ជំនួស dependency ក្នុង test
   * - ``pytest``
     - framework ភាគីទីបីដែលពេញនិយមបំផុត
   * - ``coverage``
     - វាស់ភាគរយកូដដែលបានសាកល្បង
   * - ``pdb`` / ``breakpoint()``
     - debugger អន្តរកម្ម
   * - ``python3 -X dev``
     - development mode
   * - ``cProfile`` / ``timeit``
     - វិភាគប្រសិទ្ធភាព
   * - ``logging``
     - កត់ត្រាជំនួស ``print()``
   * - ``ruff`` / ``mypy`` / ``pre-commit``
     - គុណភាពកូដស្វ័យប្រវត្តិ

.. rubric:: ប្រភពយោង

* `unittest — Unit testing framework <https://docs.python.org/3/library/unittest.html>`_
* `unittest.mock <https://docs.python.org/3/library/unittest.mock.html>`_
* `doctest — Test interactive Python examples <https://docs.python.org/3/library/doctest.html>`_
* `pdb — The Python Debugger <https://docs.python.org/3/library/pdb.html>`_
* `Debugging and Profiling <https://docs.python.org/3/library/debug.html>`_
* `timeit <https://docs.python.org/3/library/timeit.html>`_ ·
  `cProfile <https://docs.python.org/3/library/profile.html>`_
* `logging <https://docs.python.org/3/library/logging.html>`_
* `PEP 8 — Style Guide for Python Code <https://peps.python.org/pep-0008/>`_
* `PEP 20 — The Zen of Python <https://peps.python.org/pep-0020/>`_
* `PEP 257 — Docstring Conventions <https://peps.python.org/pep-0257/>`_
* `pytest documentation <https://docs.pytest.org/>`_
* `ruff documentation <https://docs.astral.sh/ruff/>`_
