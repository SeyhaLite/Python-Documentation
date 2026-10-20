.. _iterators-generators:

.. container:: src-note

   ប្រភពដើម៖ CPython ``Doc/tutorial/classes.rst`` (ផ្នែក *Iterators*,
   *Generators*, *Generator Expressions*), ``Doc/library/itertools.rst``,
   ``Doc/reference/expressions.rst`` (``yield``), ``Doc/glossary.rst`` ·
   `ឯកសារផ្លូវការ <https://docs.python.org/3/tutorial/classes.html#iterators>`_

##########################
Iterators និង Generators
##########################

ជំពូកនេះពន្យល់អំពី **iteration protocol** — យន្តការដែលធ្វើឱ្យ
``for x in y:`` ដំណើរការ — និងអំពី **generator** ដែលជាវិធីសាមញ្ញបំផុត
ក្នុងការបង្កើត iterator។

.. _iteration-protocol:

Iteration Protocol
==================

នៅពីក្រោយរង្វិលជុំ ``for`` Python ធ្វើការពីរជំហាន៖

#. ហៅ ``iter(y)`` ដើម្បីទទួល **iterator** object
#. ហៅ ``next()`` លើ iterator នោះម្ដងហើយម្ដងទៀត រហូតដល់វាបញ្ចេញ
   ``StopIteration``

.. code-block:: pycon

   >>> s = "abc"
   >>> it = iter(s)
   >>> next(it)
   'a'
   >>> next(it)
   'b'
   >>> next(it)
   'c'
   >>> next(it)
   Traceback (most recent call last):
     ...
   StopIteration

រង្វិលជុំ ``for char in s:`` គឺស្មើនឹង៖

.. code-block:: python

   it = iter(s)
   while True:
       try:
           char = next(it)
       except StopIteration:
           break
       print(char)

.. note::

   ``for`` loop **ចាប់យក** ``StopIteration`` ដោយស្វ័យប្រវត្តិ។ នេះជា
   ករណីមួយក្នុងចំណោមករណីមិនច្រើនទេដែល Python ប្រើ exception ជា
   ផ្នែកធម្មតានៃ control flow។

.. _iterable-vs-iterator:

Iterable ធៀបនឹង Iterator
------------------------

នេះជាភាពខុសគ្នាសំខាន់បំផុតដែលមនុស្សជាច្រើនច្រឡំ៖

.. list-table::
   :header-rows: 1
   :widths: 22 39 39

   * -
     - **Iterable**
     - **Iterator**
   * - ត្រូវមាន
     - ``__iter__()``
     - ``__iter__()`` **និង** ``__next__()``
   * - អាចដើរលើបានច្រើនដង?
     - ✅ បាទ/ចាស
     - ❌ ទេ — ដើរបានតែ **ម្ដង**
   * - ឧទាហរណ៍
     - ``list``, ``str``, ``tuple``, ``dict``, ``set``, ``range``
     - ``iter(list)``, generator, file object, ``enumerate`` object
   * - ទទួលបានដោយ
     - សរសេរផ្ទាល់
     - ``iter(iterable)``

.. code-block:: pycon

   >>> nums = [1, 2, 3]
   >>> it = iter(nums)
   >>> list(it)              # ប្រើអស់ហើយ
   [1, 2, 3]
   >>> list(it)              # ❌ ទទេ — iterator ដើរបានតែម្ដង
   []
   >>> list(nums)            # ✅ list ដើមនៅតែដើរបានច្រើនដង
   [1, 2, 3]

   >>> iter(nums) is nums            # list មិនមែនជា iterator ទេ
   False
   >>> it = iter(nums)
   >>> iter(it) is it                # iterator ត្រឡប់ខ្លួនឯង
   True

.. warning::

   ភាពខុសគ្នានេះបង្កើត bug ស្ងាត់៖

   .. code-block:: pycon

      >>> data = (x * 2 for x in range(3))    # generator expression — ខ្ជិល
      >>> sum(data)
      6
      >>> sum(data)                            # ❌ 0 — អស់ហើយ!
      0

   បើអ្នកត្រូវការដើរលើទិន្នន័យច្រើនដង សូមប្រើ ``list`` ឬហៅ
   generator function ម្ដងទៀត។

.. _custom-iterator:

ការបង្កើត Iterator ផ្ទាល់ខ្លួន
----------------------------------

.. code-block:: python

   class Countdown:
       """រាប់ថយក្រោយពី start ដល់ 1។"""

       def __init__(self, start):
           self.start = start
           self.current = start

       def __iter__(self):
           return self                    # ខ្លួនឯងជា iterator

       def __next__(self):
           if self.current <= 0:
               raise StopIteration
           self.current -= 1
           return self.current + 1

.. code-block:: pycon

   >>> for n in Countdown(3):
   ...     print(n, end=" ")
   ...
   3 2 1
   >>> c = Countdown(2)
   >>> next(iter(c))
   2
   >>> list(c)                            # ដើរបានតែម្ដង
   [1]

.. important::

   ``__next__()`` **ត្រូវតែ** បញ្ចេញ ``StopIteration`` នៅពេលអស់ទិន្នន័យ។
   បើវាត្រឡប់ ``None`` ឬបន្តរហូត រង្វិលជុំ ``for`` នឹងមិនឈប់ទេ។

.. _iter-sentinel:

``iter()`` ជាមួយ Sentinel
--------------------------

``iter(callable, sentinel)`` ហៅ callable រហូតដល់វាត្រឡប់ sentinel៖

.. code-block:: pycon

   >>> from pathlib import Path
   >>> Path("data.bin").write_bytes(b"AB\x00CD")
   5
   >>> with open("data.bin", "rb") as f:
   ...     chunks = list(iter(lambda: f.read(2), b""))
   ...
   >>> chunks
   [b'AB', b'\x00C', b'D']

នេះមានប្រយោជន៍សម្រាប់អានឯកសារ ឬទិន្នន័យបណ្ដាញជាដុំៗ។

----

.. _generators:

Generators
==========

**Generator** គឺជាវិធីសាមញ្ញបំផុតក្នុងការបង្កើត iterator។ អ្នកសរសេរវា
ដូចអនុគមន៍ធម្មតា ប៉ុន្តែប្រើ ``yield`` ជំនួស ``return``៖

.. code-block:: python

   def countdown(n):
       """រាប់ថយក្រោយពី n ដល់ 1។"""
       print("ចាប់ផ្ដើម")
       while n > 0:
           yield n
           n -= 1
       print("ចប់")

.. code-block:: pycon

   >>> gen = countdown(3)
   >>> gen                      # មិនទាន់ដំណើរការទេ!
   <generator object countdown at 0x...>
   >>> next(gen)
   ចាប់ផ្ដើម
   3
   >>> next(gen)
   2
   >>> next(gen)
   1
   >>> next(gen)
   ចប់
   Traceback (most recent call last):
     ...
   StopIteration

.. _generator-lazy:

Generator ជា Lazy
------------------

អ្វីដែលមាននៅក្នុង generator function **មិនដំណើរការទេ** រហូតដល់មាន
ការហៅ ``next()``។ ហើយវាឈប់នៅត្រង់ ``yield`` រួច **ចងចាំ** ស្ថានភាព
ទាំងអស់ (អថេរ local, ទីតាំងកូដ) រហូតដល់ការហៅបន្ទាប់។

.. code-block:: pycon

   >>> def traced():
   ...     print("A")
   ...     yield 1
   ...     print("B")
   ...     yield 2
   ...     print("C")
   ...
   >>> g = traced()             # គ្មានអ្វីត្រូវបានបោះពុម្ពទេ
   >>> next(g)
   A
   1
   >>> next(g)
   B
   2
   >>> next(g)
   C
   Traceback (most recent call last):
     ...
   StopIteration

.. _generator-memory:

អត្ថប្រយោជន៍អង្គចងចាំ
----------------------

Generator ផលិតតម្លៃ **ម្ដងមួយៗ** ដូច្នេះវាមិនត្រូវការផ្ទុកទិន្នន័យទាំងអស់
ក្នុងអង្គចងចាំទេ៖

.. code-block:: pycon

   >>> import sys
   >>> big_list = list(range(1_000_000))
   >>> big_gen = (x for x in range(1_000_000))
   >>> sys.getsizeof(big_list) > 8_000_000     # រាប់លាន byte
   True
   >>> sys.getsizeof(big_gen) < 300            # តែរាប់រយ byte
   True

**ឧទាហរណ៍ជាក់ស្ដែង** — អានឯកសារធំដោយមិនផ្ទុកទាំងមូល៖

.. code-block:: python

   from pathlib import Path

   Path("big.log").write_text("\n".join(f"line {i}" for i in range(100_000)),
                              encoding="utf-8")


   def errors_only(path):
       """ផលិតតែបន្ទាត់ដែលមានពាក្យ ERROR។"""
       with open(path, encoding="utf-8") as f:
           for line in f:                    # អានម្ដងមួយបន្ទាត់
               if "ERROR" in line:
                   yield line.rstrip()


   count = sum(1 for _ in errors_only("big.log"))   # គ្មាន list ក្នុងអង្គចងចាំ

.. _generator-pipelines:

Generator Pipeline
------------------

Generator អាចត្រូវបាន **តភ្ជាប់** គ្នាដូចបំពង់ — ទិន្នន័យហូរកាត់ម្ដងមួយធាតុ៖

.. code-block:: python

   def read_lines(path):
       with open(path, encoding="utf-8") as f:
           for line in f:
               yield line.rstrip()


   def filter_errors(lines):
       for line in lines:
           if "ERROR" in line:
               yield line


   def extract_messages(lines):
       for line in lines:
           yield line.split("ERROR", 1)[1].strip()


   pipeline = extract_messages(filter_errors(read_lines("big.log")))

.. code-block:: pycon

   >>> sum(1 for _ in pipeline)
   0

.. note::

   Pipeline នេះ **មិនអានឯកសារទេ** រហូតដល់មានការទាញយកតម្លៃដំបូង។
   ហើយវាប្រើអង្គចងចាំតែប៉ុន្មានបន្ទាត់ប៉ុណ្ណោះ ទោះបីជាឯកសារមាន
   រាប់លានបន្ទាត់ក៏ដោយ។ នេះជាគុណសម្បត្តិធំបំផុតរបស់ generator។

.. _infinite-generators:

Generator គ្មានទីបញ្ចប់
------------------------

Generator អាចផលិតលំដាប់គ្មានទីបញ្ចប់បាន ព្រោះវាផលិតតាមតម្រូវការ៖

.. code-block:: pycon

   >>> def natural_numbers(start=1):
   ...     n = start
   ...     while True:
   ...         yield n
   ...         n += 1
   ...
   >>> import itertools
   >>> list(itertools.islice(natural_numbers(), 5))
   [1, 2, 3, 4, 5]
   >>> list(itertools.islice(natural_numbers(100), 3))
   [100, 101, 102]

.. warning::

   កុំសរសេរ ``list(natural_numbers())`` — វានឹងព្យាយាមផ្ទុកលេខគ្មានទីបញ្ចប់
   ហើយអស់អង្គចងចាំ។ ប្រើ ``itertools.islice()`` ដើម្បីយកតែចំនួនកំណត់។

.. _yield-from:

``yield from``
--------------

``yield from`` បញ្ជូនតម្លៃទាំងអស់ពី iterable ឬ generator ផ្សេងទៀត៖

.. code-block:: pycon
   :no-test:

   >>> def flatten(nested):
   ...     for item in nested:
   ...         if isinstance(item, list):
   ...             yield from flatten(item)     # បញ្ជូនបន្តជា recursion
   ...         else:
   ...             yield item
   ...
   >>> list(flatten([1, [2, [3, 4]], 5]))
   [1, 2, 3, 4, 5]

   >>> def chained():
   ...     yield from [1, 2]
   ...     yield from (3, 4)
   ...     yield from "ab"
   ...
   >>> list(chained())
   [1, 2, 3, 4, 'a', 'b']

``yield from x`` ខ្លីជាង៖

.. code-block:: python
   :no-test:

   for item in x:
       yield item

ប៉ុន្តែវាខ្លាំងជាង ព្រោះវាក៏បញ្ជូន ``send()``, ``throw()`` និង ``close()``
ទៅ generator រងផងដែរ។

.. _generator-expressions:

Generator Expression
====================

Generator expression ដូច list comprehension ប៉ុន្តែប្រើវង់ក្រចកមូល ``( )``
ជំនួសវង់ក្រចកការ៉េ ``[ ]``៖

.. code-block:: pycon

   >>> squares_list = [x ** 2 for x in range(5)]     # list — ផ្ទុកភ្លាម
   >>> squares_gen = (x ** 2 for x in range(5))      # generator — ខ្ជិល
   >>> squares_list
   [0, 1, 4, 9, 16]
   >>> squares_gen
   <generator object <genexpr> at 0x...>
   >>> list(squares_gen)
   [0, 1, 4, 9, 16]
   >>> list(squares_gen)                             # អស់ហើយ
   []

.. list-table::
   :header-rows: 1
   :widths: 26 37 37

   * -
     - List comprehension ``[ ]``
     - Generator expression ``( )``
   * - ផ្ទុកក្នុងអង្គចងចាំ
     - ទាំងអស់ភ្លាមៗ
     - ម្ដងមួយធាតុ
   * - ដើរបានច្រើនដង
     - ✅
     - ❌
   * - ល្បឿន (ទិន្នន័យតូច)
     - លឿនជាងបន្តិច
     - យឺតជាងបន្តិច
   * - ប្រើពេលណា
     - ត្រូវការ list ពិត ឬដើរច្រើនដង
     - ទិន្នន័យធំ ឬប្រើតែម្ដង

.. tip::

   នៅពេលបញ្ជូន generator expression ជា **argument តែមួយគត់** អ្នកអាចលុប
   វង់ក្រចកមួយជាន់៖

   .. code-block:: pycon

      >>> sum(x ** 2 for x in range(5))       # គ្មានវង់ក្រចកពីរជាន់
      30
      >>> max(len(w) for w in ["a", "bbb", "cc"])
      3
      >>> any(x > 2 for x in [1, 2, 3])
      True
      >>> all(x > 0 for x in [1, 2, 3])
      True

   នេះមានប្រសិទ្ធភាពជាង ``sum([x ** 2 for x in range(5)])`` ព្រោះវា
   មិនបង្កើត list កណ្ដាលទេ។

.. _generator-methods:

``send()``, ``throw()`` និង ``close()``
===========================================

Generator អាច **ទទួល** តម្លៃពីខាងក្រៅបានផងដែរ (coroutine)៖

.. code-block:: pycon

   >>> def accumulator():
   ...     total = 0
   ...     while True:
   ...         value = yield total        # ទទួលតម្លៃ ហើយបញ្ជូន total ចេញ
   ...         if value is None:
   ...             break
   ...         total += value
   ...
   >>> acc = accumulator()
   >>> next(acc)                          # ចាប់ផ្ដើម (prime the generator)
   0
   >>> acc.send(10)
   10
   >>> acc.send(5)
   15
   >>> acc.close()                        # បញ្ឈប់

.. list-table::
   :header-rows: 1
   :widths: 26 74

   * - Method
     - ឥទ្ធិពល
   * - ``next(g)`` ឬ ``g.send(None)``
     - ដំណើរការបន្ត រហូតដល់ ``yield`` បន្ទាប់
   * - ``g.send(value)``
     - ដំណើរការបន្ត ហើយធ្វើឱ្យ ``yield`` ត្រឡប់ ``value``
   * - ``g.throw(exc)``
     - បញ្ចេញ exception នៅត្រង់ ``yield`` បច្ចុប្បន្ន
   * - ``g.close()``
     - បញ្ចេញ ``GeneratorExit`` ខាងក្នុង · generator ត្រូវបញ្ចប់

.. important::

   អ្នក **ត្រូវតែ** ហៅ ``next(g)`` (ឬ ``g.send(None)``) មុន ``send()``
   លើកដំបូង ព្រោះ generator មិនទាន់ដំណើរការដល់ ``yield`` ដំបូងទេ។
   បើមិនដូច្នោះ អ្នកនឹងទទួល ``TypeError``។

.. note::

   ``close()`` បញ្ចេញ ``GeneratorExit`` នៅត្រង់ ``yield``។ Generator អាច
   ចាប់យកវាដើម្បីសម្អាតធនធាន ប៉ុន្តែ **មិនអាច** ``yield`` បន្ទាប់ពីនោះទេ —
   វានឹងបញ្ចេញ ``RuntimeError``។

   សម្រាប់ការសម្អាតធនធាន វិធីសាមញ្ញបំផុតគឺប្រើ ``try``/``finally`` ក្នុង
   generator៖

   .. code-block:: python

      def read_rows(path):
          f = open(path, encoding="utf-8")
          try:
              for line in f:
                  yield line.rstrip()
          finally:
              f.close()          # ដំណើរការទោះបី generator ត្រូវបាន close()

.. _return-in-generator:

``return`` ក្នុង Generator
--------------------------

``return value`` ក្នុង generator បញ្ចប់វា ហើយដាក់ ``value`` ទៅក្នុង
``StopIteration.value``៖

.. code-block:: pycon

   >>> def gen_with_return():
   ...     yield 1
   ...     yield 2
   ...     return "លទ្ធផលចុងក្រោយ"
   ...
   >>> g = gen_with_return()
   >>> next(g), next(g)
   (1, 2)
   >>> try:
   ...     next(g)
   ... except StopIteration as e:
   ...     print("StopIteration.value =", e.value)
   ...
   StopIteration.value = លទ្ធផលចុងក្រោយ

``yield from`` ចាប់យកតម្លៃនេះដោយស្វ័យប្រវត្តិ៖

.. code-block:: pycon

   >>> def wrapper():
   ...     result = yield from gen_with_return()
   ...     print("ទទួលបានពី sub-generator:", result)
   ...
   >>> list(wrapper())
   ទទួលបានពី sub-generator: លទ្ធផលចុងក្រោយ
   [1, 2]

.. _itertools:

ម៉ូឌុល ``itertools``
=====================

``itertools`` ផ្ដល់ generator ដែលមានប្រសិទ្ធភាពខ្ពស់សម្រាប់ដំណើរការលើ
លំដាប់។ ទាំងអស់ជា **lazy**។

.. list-table:: បង្កើតលំដាប់
   :header-rows: 1
   :widths: 32 68

   * - អនុគមន៍
     - លទ្ធផល
   * - ``count(start, step)``
     - លេខគ្មានទីបញ្ចប់
   * - ``cycle(iterable)``
     - ដើរម្ដងទៀតគ្មានទីបញ្ចប់
   * - ``repeat(x, n)``
     - តម្លៃដដែល ``n`` ដង
   * - ``range()`` (built-in)
     - លេខគត់ក្នុងជួរ

.. list-table:: បញ្ចប់លំដាប់
   :header-rows: 1
   :widths: 32 68

   * - អនុគមន៍
     - លទ្ធផល
   * - ``islice(it, stop)`` ឬ ``islice(it, start, stop, step)``
     - យកផ្នែកមួយ (ដូច slicing ប៉ុន្តែសម្រាប់ iterator)
   * - ``takewhile(pred, it)``
     - យកធាតុខណៈពេល ``pred`` ពិត
   * - ``dropwhile(pred, it)``
     - រំលងធាតុខណៈពេល ``pred`` ពិត រួចយកទាំងអស់
   * - ``filterfalse(pred, it)``
     - យកធាតុដែល ``pred`` **មិន** ពិត

.. list-table:: រួមបញ្ចូល
   :header-rows: 1
   :widths: 32 68

   * - អនុគមន៍
     - លទ្ធផល
   * - ``chain(a, b, ...)``
     - ភ្ជាប់លំដាប់ជាបន្តបន្ទាប់
   * - ``chain.from_iterable(it)``
     - ដូចគ្នា ប៉ុន្តែពី iterable នៃ iterables
   * - ``zip_longest(a, b, fillvalue=…)``
     - ដូច ``zip()`` ប៉ុន្តែបន្តរហូតដល់លំដាប់ **វែងបំផុត** អស់
   * - ``product(a, b)``
     - ផលគុណ Cartesian
   * - ``permutations(a, r)``
     - ការរៀបចំលំដាប់
   * - ``combinations(a, r)`` / ``combinations_with_replacement``
     - ការជ្រើសរើសដោយមិនគិតលំដាប់

.. list-table:: ក្រុម និងសម្រួល
   :header-rows: 1
   :widths: 32 68

   * - អនុគមន៍
     - លទ្ធផល
   * - ``groupby(it, key)``
     - ក្រុមធាតុជាប់គ្នាដែលមាន key ដូចគ្នា (**ត្រូវតម្រៀបជាមុន**)
   * - ``accumulate(it, func)``
     - ផលបូកបង្គរ (ឬ func ផ្សេង)
   * - ``pairwise(it)``
     - គូជាប់គ្នា ``(a,b), (b,c), (c,d)``
   * - ``batched(it, n)``
     - បែងចែកជាដុំនៃ ``n`` (Python 3.12+)
   * - ``starmap(func, it)``
     - ``func(*args)`` សម្រាប់ tuple នីមួយៗ

.. code-block:: pycon

   >>> import itertools
   >>> list(itertools.chain([1, 2], "ab"))
   [1, 2, 'a', 'b']
   >>> list(itertools.islice(itertools.count(10, 5), 4))
   [10, 15, 20, 25]
   >>> list(itertools.takewhile(lambda x: x < 4, [1, 3, 5, 2]))
   [1, 3]
   >>> list(itertools.accumulate([1, 2, 3, 4]))
   [1, 3, 6, 10]
   >>> list(itertools.pairwise([1, 2, 3, 4]))
   [(1, 2), (2, 3), (3, 4)]
   >>> list(itertools.product([1, 2], "ab"))
   [(1, 'a'), (1, 'b'), (2, 'a'), (2, 'b')]
   >>> list(itertools.combinations([1, 2, 3], 2))
   [(1, 2), (1, 3), (2, 3)]
   >>> list(itertools.permutations([1, 2, 3], 2))
   [(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)]

.. versionadded:: 3.10
   ``pairwise()``។

.. versionadded:: 3.12
   ``batched()``។

.. code-block:: pycon

   >>> list(itertools.batched("ABCDEFG", 3))
   [('A', 'B', 'C'), ('D', 'E', 'F'), ('G',)]

.. warning::

   ``groupby()`` ក្រុមតែធាតុ **ជាប់គ្នា** ប៉ុណ្ណោះ។ អ្នកត្រូវតម្រៀបទិន្នន័យ
   តាម key ជាមុន៖

   .. code-block:: pycon

      >>> data = [("b", 1), ("a", 2), ("b", 3)]
      >>> # ❌ 'b' ពីរក្រុម
      >>> [(k, len(list(g))) for k, g in itertools.groupby(data, key=lambda t: t[0])]
      [('b', 1), ('a', 1), ('b', 1)]
      >>> data_sorted = sorted(data, key=lambda t: t[0])
      >>> # ✅
      >>> [(k, len(list(g))) for k, g in itertools.groupby(data_sorted, key=lambda t: t[0])]
      [('a', 1), ('b', 2)]

   ចំណាំថា ``groupby()`` ត្រូវបាន **ប្រើប្រាស់ភ្លាម** — បើអ្នកមិនបំលែង
   sub-iterator ``g`` ទៅ list មុនពេលដើរទៅក្រុមបន្ទាប់ វានឹងទទេ។

----

.. _iterator-summary:

សង្ខេប
======

.. list-table::
   :header-rows: 1
   :widths: 28 72

   * - គោលគំនិត
     - សង្ខេប
   * - Iterable
     - មាន ``__iter__()`` · ដើរបានច្រើនដង
   * - Iterator
     - មាន ``__iter__()`` + ``__next__()`` · ដើរបានតែម្ដង · បញ្ចេញ ``StopIteration``
   * - ``for x in y``
     - ``iter(y)`` រួច ``next()`` ម្ដងហើយម្ដងទៀត
   * - Generator function
     - អនុគមន៍ដែលមាន ``yield`` · ត្រឡប់ generator object
   * - Generator expression
     - ``(x for x in y)`` · lazy · ប្រើអង្គចងចាំតិច
   * - ``yield from``
     - បញ្ជូនទៅ sub-iterator រួមទាំង ``send``/``throw``/``close``
   * - ``send()`` / ``throw()`` / ``close()``
     - ទំនាក់ទំនងពីរទិសជាមួយ generator
   * - ``itertools``
     - generator ស្តង់ដារដែលមានប្រសិទ្ធភាពខ្ពស់

.. tip::

   **ជ្រើសរើស generator ពេលណា?**

   * ទិន្នន័យធំ ឬគ្មានទីបញ្ចប់ → generator
   * ដើរលើទិន្នន័យតែម្ដង (ឧ. pipeline) → generator
   * ត្រូវការ index, ប្រវែង ឬដើរច្រើនដង → list
   * ទិន្នន័យតូចហើយច្បាស់ → list (សាមញ្ញជាង)

.. rubric:: ប្រភពយោង

* `Iterators <https://docs.python.org/3/tutorial/classes.html#iterators>`_
* `Generators <https://docs.python.org/3/tutorial/classes.html#generators>`_
* `Generator Expressions <https://docs.python.org/3/tutorial/classes.html#generator-expressions>`_
* `itertools — Functions creating iterators <https://docs.python.org/3/library/itertools.html>`_
* `Glossary: iterator / iterable / generator <https://docs.python.org/3/glossary.html#term-iterator>`_
* `PEP 255 — Simple Generators <https://peps.python.org/pep-0255/>`_
* `PEP 289 — Generator Expressions <https://peps.python.org/pep-0289/>`_
* `PEP 342 — Coroutines via Enhanced Generators <https://peps.python.org/pep-0342/>`_
* `PEP 380 — Syntax for Delegating to a Subgenerator <https://peps.python.org/pep-0380/>`_
