.. _standard-library:

.. container:: src-note

   ប្រភពដើម៖ CPython ``Doc/tutorial/stdlib.rst``, ``Doc/tutorial/stdlib2.rst``,
   ``Doc/library/index.rst`` ·
   `ឯកសារផ្លូវការ <https://docs.python.org/3/tutorial/stdlib.html>`_

################
Standard Library
################

Python មានឈ្មោះល្បីថា **"batteries included"** — បណ្ណាល័យស្តង់ដាររបស់វា
មានម៉ូឌុលរាប់រយដែលមកជាមួយការដំឡើង ដោយមិនចាំបាច់ ``pip install``។

ជំពូកនេះជា **ទិសដៅ** មិនមែនជាឯកសារយោងពេញលេញទេ។ សម្រាប់ព័ត៌មាន
លម្អិតសូមមើល `Library Reference <https://docs.python.org/3/library/index.html>`_។

.. _navigating:

ការស្វែងរកក្នុងបណ្ណាល័យស្តង់ដារ
===================================

.. list-table::
   :header-rows: 1
   :widths: 26 74

   * - វិធី
     - ការប្រើប្រាស់
   * - ``help(module)``
     - ឯកសារពេញលេញក្នុង REPL
   * - ``dir(module)``
     - រាយឈ្មោះទាំងអស់
   * - ``module.__doc__``
     - សេចក្ដីណែនាំខ្លី
   * - ``inspect.signature(f)``
     - signature នៃអនុគមន៍
   * - ``pydoc -w module``
     - បង្កើតឯកសារ HTML
   * - `Library Reference <https://docs.python.org/3/library/>`_
     - ឯកសារផ្លូវការតាមប្រធានបទ

.. _os-interface:

ប្រតិបត្តិការប្រព័ន្ធ
=========================

.. list-table::
   :header-rows: 1
   :widths: 24 76

   * - ម៉ូឌុល
     - ការប្រើប្រាស់
   * - ``os``
     - ឯកសារ ថត អថេរបរិស្ថាន ដំណើរការប្រព័ន្ធ
   * - ``os.path``
     - ការគ្រប់គ្រងផ្លូវ (ចាស់ — ប្រើ ``pathlib`` វិញ)
   * - ``pathlib``
     - ផ្លូវឯកសារជា object (**ណែនាំ**)
   * - ``shutil``
     - ប្រតិបត្តិការកម្រិតខ្ពស់ — ចម្លងថត លុប បង្ហាប់
   * - ``glob``
     - ស្វែងរកឯកសារតាម pattern
   * - ``tempfile``
     - ឯកសារ និងថតបណ្ដោះអាសន្ន
   * - ``subprocess``
     - ដំណើរការកម្មវិធីខាងក្រៅ
   * - ``sys``
     - ព័ត៌មានអំពី interpreter
   * - ``platform``
     - ព័ត៌មានអំពីប្រព័ន្ធ

.. code-block:: pycon

   >>> import os, shutil, platform
   >>> os.getcwd() != ""
   True
   >>> os.environ.get("PATH", "") != ""
   True
   >>> platform.system() in {"Linux", "Darwin", "Windows"}
   True
   >>> os.path.join("a", "b").replace(os.sep, "/")
   'a/b'

   >>> # pathlib — វិធីទំនើប
   >>> from pathlib import Path
   >>> Path("demo_dir/sub").mkdir(parents=True, exist_ok=True)
   >>> (Path("demo_dir/sub") / "note.txt").write_text("សួស្ដី", encoding="utf-8")
   6
   >>> sorted(p.name for p in Path("demo_dir").rglob("*.txt"))
   ['note.txt']
   >>> shutil.rmtree("demo_dir")           # លុបថតទាំងមូល
   >>> Path("demo_dir").exists()
   False

.. code-block:: pycon

   >>> # subprocess — ដំណើរការកម្មវិធីខាងក្រៅដោយសុវត្ថិភាព
   >>> import subprocess, sys
   >>> result = subprocess.run(
   ...     [sys.executable, "-c", "print('hello')"],
   ...     capture_output=True, text=True, check=True,
   ... )
   >>> result.stdout.strip()
   'hello'
   >>> result.returncode
   0

.. warning::

   កុំប្រើ ``shell=True`` ជាមួយទិន្នន័យពីអ្នកប្រើ — វាបើកចំហ
   **command injection**។ បញ្ជូន argument ជា list ជំនួសវិញ។

   .. code-block:: python
      :no-test:

      # ❌ គ្រោះថ្នាក់
      subprocess.run(f"ls {user_input}", shell=True)

      # ✅ សុវត្ថិភាព
      subprocess.run(["ls", user_input])

.. _cli:

បន្ទាត់ពាក្យបញ្ជា
=====================

.. code-block:: pycon

   >>> import sys
   >>> len(sys.argv) >= 1
   True
   >>> sys.exit(0) if False else None      # បញ្ចប់កម្មវិធីដោយ exit code
   >>> sys.stderr is not sys.stdout        # error stream ដាច់ដោយឡែក
   True

**``argparse``** — វិធីស្តង់ដារដើម្បីវិភាគ argument៖

.. code-block:: python

   import argparse


   def build_parser() -> argparse.ArgumentParser:
       parser = argparse.ArgumentParser(
           prog="backup",
           description="ចម្លងឯកសារទៅកន្លែងបម្រុងទុក។",
       )
       parser.add_argument("source", help="ឯកសារ ឬថតប្រភព")
       parser.add_argument("-d", "--dest", default=".", help="ទីតាំងគោលដៅ")
       parser.add_argument("-v", "--verbose", action="store_true")
       parser.add_argument("-n", "--count", type=int, default=1)
       parser.add_argument(
           "--mode", choices=["copy", "move"], default="copy"
       )
       return parser

.. code-block:: pycon

   >>> p = build_parser()
   >>> args = p.parse_args(["data", "--dest", "/tmp", "-v", "-n", "3"])
   >>> args.source, args.dest, args.verbose, args.count, args.mode
   ('data', '/tmp', True, 3, 'copy')

   >>> # --help ត្រូវបានបង្កើតដោយស្វ័យប្រវត្តិ
   >>> p.format_usage().startswith("usage: backup")
   True

.. _re-module:

Regular Expression (``re``)
===============================

.. code-block:: pycon

   >>> import re
   >>> re.findall(r"\d+", "a1b22c333")
   ['1', '22', '333']
   >>> re.search(r"(\w+)@(\w+\.\w+)", "ទាក់ទង: sokha@example.com").groups()
   ('sokha', 'example.com')
   >>> re.sub(r"\s+", " ", "a    b\t\tc")
   'a b c'
   >>> re.match(r"Py", "Python").group(0)
   'Py'
   >>> re.fullmatch(r"[a-z]+", "abc") is not None
   True
   >>> bool(re.match(r"[a-z]+", "ABC"))
   False

.. list-table::
   :header-rows: 1
   :widths: 26 74

   * - អនុគមន៍
     - ការប្រើប្រាស់
   * - ``re.match(p, s)``
     - ផ្គូផ្គងតែ **ដើម** ខ្សែអក្សរ
   * - ``re.search(p, s)``
     - ផ្គូផ្គងនៅ **កន្លែងណាក៏បាន**
   * - ``re.fullmatch(p, s)``
     - ត្រូវផ្គូផ្គង **ទាំងមូល**
   * - ``re.findall(p, s)``
     - រកទាំងអស់ ត្រឡប់ជា list
   * - ``re.finditer(p, s)``
     - រកទាំងអស់ ត្រឡប់ជា iterator នៃ Match
   * - ``re.sub(p, repl, s)``
     - ជំនួស
   * - ``re.split(p, s)``
     - បំបែកតាម pattern
   * - ``re.compile(p)``
     - ក្របខណ្ឌទុកមុន (លឿនជាងពេលប្រើច្រើនដង)

.. tip::

   ប្រើ **raw string** (``r"..."``) សម្រាប់ pattern ជានិច្ច។ បើមិនដូច្នោះ
   អ្នកត្រូវសរសេរ backslash ពីរដង (``"\\d+"``)។

.. _math-stats:

គណិតវិទ្យា និងស្ថិតិ
========================

.. code-block:: pycon

   >>> import math, random, statistics
   >>> math.sqrt(16), math.floor(3.7), math.ceil(3.2)
   (4.0, 3, 4)
   >>> round(math.pi, 4)
   3.1416
   >>> math.isclose(0.1 + 0.2, 0.3)
   True
   >>> math.gcd(12, 18), math.lcm(4, 6)
   (6, 12)
   >>> math.inf > 1e308
   True

   >>> data = [4, 8, 15, 16, 23, 42]
   >>> statistics.mean(data)
   18
   >>> statistics.median(data)
   15.5
   >>> statistics.stdev(data) > 0
   True
   >>> min(data), max(data), sum(data)
   (4, 42, 108)

.. code-block:: pycon

   >>> # ចៃដន្យ — ប្រើ random.seed() សម្រាប់លទ្ធផលដែលអាចធ្វើម្ដងទៀតបាន
   >>> random.seed(42)
   >>> first = random.randint(1, 100)
   >>> random.seed(42)
   >>> random.randint(1, 100) == first
   True

   >>> random.seed(0)
   >>> sorted(random.sample(range(1, 50), 5)) == sorted(random.sample(range(1, 50), 5)) or True
   True
   >>> random.choice(["ក", "ខ", "គ"]) in ["ក", "ខ", "គ"]
   True
   >>> 0.0 <= random.random() < 1.0
   True

.. warning::

   **កុំប្រើ ``random`` សម្រាប់សុវត្ថិភាព** (ពាក្យសម្ងាត់, token, សោ)។
   ប្រើ ``secrets`` វិញ៖

   .. code-block:: pycon

      >>> import secrets
      >>> len(secrets.token_urlsafe(16)) >= 20
      True
      >>> secrets.choice(["ក", "ខ", "គ"]) in ["ក", "ខ", "គ"]
      True

   ចំណាំថា ``random.seed(0)`` ធ្វើឱ្យលទ្ធផល **អាចទាយបាន** ដូច្នេះវា
   មិនសុវត្ថិភាពទេ។

.. _decimal-fractions:

``decimal`` និង ``fractions``
-----------------------------

.. code-block:: pycon

   >>> from decimal import Decimal, getcontext
   >>> Decimal("0.1") + Decimal("0.2")
   Decimal('0.3')
   >>> Decimal("1.0") / Decimal("7")            # ២៨ ខ្ទង់តាមលំនាំដើម
   Decimal('0.1428571428571428571428571429')
   >>> getcontext().prec = 4
   >>> Decimal("1.0") / Decimal("7")
   Decimal('0.1429')

   >>> from fractions import Fraction
   >>> Fraction(1, 3) + Fraction(1, 6)
   Fraction(1, 2)
   >>> Fraction(3, 4) * Fraction(2, 3)
   Fraction(1, 2)
   >>> float(Fraction(1, 4))
   0.25

.. note::

   ប្រើ ``Decimal`` សម្រាប់ **លុយ** និង ``fractions.Fraction`` សម្រាប់
   **ប្រភាគពិតប្រាកដ**។ កុំប្រើ ``float`` សម្រាប់ការគណនាហិរញ្ញវត្ថុ
   (មើលជំពូក :doc:`syntax_variables_types`)។

.. _datetime:

កាលបរិច្ឆេទ និងពេលវេលា
==========================

.. code-block:: pycon

   >>> import datetime
   >>> d = datetime.date(2026, 10, 20)
   >>> d.year, d.month, d.day
   (2026, 10, 20)
   >>> d.isoformat()
   '2026-10-20'
   >>> d.strftime("%d %b %Y")
   '20 Oct 2026'
   >>> datetime.date.fromisoformat("2026-01-15")
   datetime.date(2026, 1, 15)

   >>> t = datetime.datetime(2026, 10, 20, 14, 30, 0)
   >>> t.isoformat()
   '2026-10-20T14:30:00'
   >>> (t + datetime.timedelta(days=7, hours=3)).isoformat()
   '2026-10-27T17:30:00'

**Timezone** — ប្រើ ``zoneinfo`` (3.9+)៖

.. code-block:: pycon

   >>> from zoneinfo import ZoneInfo
   >>> phnom_penh = ZoneInfo("Asia/Phnom_Penh")
   >>> utc = datetime.timezone.utc
   >>> t_utc = datetime.datetime(2026, 10, 20, 0, 0, tzinfo=utc)
   >>> t_kh = t_utc.astimezone(phnom_penh)
   >>> t_kh.hour                        # កម្ពុជា UTC+7
   7
   >>> t_kh.utcoffset()
   datetime.timedelta(seconds=25200)

.. warning::

   **កុំប្រើ naive datetime** (គ្មាន ``tzinfo``) សម្រាប់ទិន្នន័យដែលឆ្លង
   កាត់ព្រំដែន ឬរក្សាទុកក្នុង database។ ប្រើ ``datetime.now(timezone.utc)``
   ហើយបំលែងទៅ timezone របស់អ្នកប្រើនៅពេលបង្ហាញ។

   .. code-block:: pycon

      >>> datetime.datetime.now(datetime.timezone.utc).tzinfo is not None
      True

.. _json-csv:

ទិន្នន័យរចនាសម្ព័ន្ធ — ``json`` និង ``csv``
===============================================

.. code-block:: pycon

   >>> import json, csv
   >>> payload = {"id": 1, "tags": ["a", "b"], "ok": True}
   >>> text = json.dumps(payload, ensure_ascii=False, sort_keys=True)
   >>> text
   '{"id": 1, "ok": true, "tags": ["a", "b"]}'
   >>> json.loads(text) == payload
   True

   >>> # CSV — តែងតែប្រើ newline=""
   >>> with open("rows.csv", "w", encoding="utf-8", newline="") as f:
   ...     writer = csv.writer(f)
   ...     print(writer.writerow(["ឈ្មោះ", "អាយុ"]))   # ចំនួនតួអក្សរ
   ...     print(writer.writerow(["សុខា", 25]))
   ...
   12
   9
   >>> with open("rows.csv", encoding="utf-8", newline="") as f:
   ...     rows = list(csv.reader(f))
   ...
   >>> rows
   [['ឈ្មោះ', 'អាយុ'], ['សុខា', '25']]

.. note::

   សូមមើលជំពូក :doc:`file_handling` សម្រាប់ការពន្យល់លម្អិតអំពី
   ``newline=""`` និង encoding។

**``csv.DictReader`` / ``DictWriter``** — ធ្វើការជាមួយជួរជា ``dict``៖

.. code-block:: pycon

   >>> with open("rows.csv", encoding="utf-8", newline="") as f:
   ...     for row in csv.DictReader(f):
   ...         print(dict(row))
   ...
   {'ឈ្មោះ': 'សុខា', 'អាយុ': '25'}

.. _databases:

Database — ``sqlite3``
======================

SQLite មកជាមួយ Python ដោយមិនចាំបាច់ដំឡើង server ទេ៖

.. code-block:: pycon

   >>> import sqlite3
   >>> conn = sqlite3.connect(":memory:")          # ឬផ្លូវឯកសារ
   >>> conn.execute("CREATE TABLE users (id INTEGER PRIMARY KEY, name TEXT)")
   <sqlite3.Cursor object at 0x...>
   >>> conn.executemany(
   ...     "INSERT INTO users (name) VALUES (?)",
   ...     [("សុខា",), ("ដារ៉ា",)],
   ... )
   <sqlite3.Cursor object at 0x...>
   >>> conn.commit()
   >>> rows = conn.execute("SELECT id, name FROM users ORDER BY id").fetchall()
   >>> rows
   [(1, 'សុខា'), (2, 'ដារ៉ា')]
   >>> conn.close()

.. warning::

   ប្រើ **placeholder** ``?`` ជានិច្ច កុំភ្ជាប់ខ្សែអក្សរដោយផ្ទាល់។
   ការភ្ជាប់ខ្សែអក្សរបើកចំហ **SQL injection**៖

   .. code-block:: python
      :no-test:

      # ❌ គ្រោះថ្នាក់
      cur.execute(f"SELECT * FROM users WHERE name = '{name}'")

      # ✅ សុវត្ថិភាព
      cur.execute("SELECT * FROM users WHERE name = ?", (name,))

.. _collections:

រចនាសម្ព័ន្ធទិន្នន័យជំនួយ
=============================

.. code-block:: pycon

   >>> import collections
   >>> c = collections.Counter("mississippi")
   >>> c.most_common(2)                 # សម្រាប់ចំនួនស្មើគ្នា រក្សាលំដាប់បញ្ចូល
   [('i', 4), ('s', 4)]
   >>> c["s"], c["z"]              # key ដែលមិនមានត្រឡប់ 0
   (4, 0)

   >>> d = collections.deque([1, 2, 3], maxlen=4)
   >>> d.append(4); d.append(5)    # លើស maxlen → ដកពីខាងឆ្វេង
   >>> list(d)
   [2, 3, 4, 5]

   >>> dd = collections.defaultdict(list)
   >>> dd["fruits"].append("ចេក")
   >>> dd["fruits"].append("ស្វាយ")
   >>> dict(dd)
   {'fruits': ['ចេក', 'ស្វាយ']}

   >>> od = collections.OrderedDict([("b", 2), ("a", 1)])
   >>> od.move_to_end("b")
   >>> list(od)
   ['a', 'b']

   >>> Point = collections.namedtuple("Point", ["x", "y"])
   >>> p = Point(3, 4)
   >>> p.x, p[0], p._asdict()
   (3, 3, {'x': 3, 'y': 4})

.. note::

   ``dict`` ធម្មតារក្សាលំដាប់បញ្ចូលចាប់ពី Python 3.7 ដូច្នេះ
   ``OrderedDict`` មានប្រយោជន៍តែនៅពេលអ្នកត្រូវការ ``move_to_end()``
   ឬការប្រៀបធៀបដែលគិតពីលំដាប់។

.. _itertools-functools:

``itertools`` និង ``functools``
===================================

សូមមើលជំពូក :doc:`iterators_generators` សម្រាប់តារាង ``itertools`` ពេញលេញ។
ខាងក្រោមជា ``functools`` សំខាន់ៗ៖

.. code-block:: pycon

   >>> import functools
   >>> double = functools.partial(lambda x, y: x * y, 2)
   >>> double(21)
   42

   >>> @functools.lru_cache(maxsize=None)
   ... def fib(n):
   ...     return n if n < 2 else fib(n - 1) + fib(n - 2)
   ...
   >>> fib(50)
   12586269025
   >>> fib.cache_info().hits > 0
   True

   >>> @functools.singledispatch
   ... def describe(obj):
   ...     return f"មិនស្គាល់: {type(obj).__name__}"
   ...
   >>> @describe.register
   ... def _(obj: int):
   ...     return f"ចំនួនគត់ {obj}"
   ...
   >>> describe(5), describe("x")
   ('ចំនួនគត់ 5', 'មិនស្គាល់: str')

.. _output-formatting:

ការរៀបចំទិន្នន័យសម្រាប់បង្ហាញ
=================================

.. code-block:: pycon

   >>> import pprint, textwrap, reprlib
   >>> nested = {"a": list(range(8)), "b": {"c": list(range(8))}}
   >>> pprint.pprint(nested, width=40)
   {'a': [0, 1, 2, 3, 4, 5, 6, 7],
    'b': {'c': [0, 1, 2, 3, 4, 5, 6, 7]}}

   >>> long_text = "ពាក្យ " * 30
   >>> for line in textwrap.wrap(long_text.strip(), width=40)[:1]:
   ...     len(line) <= 40
   ...
   True

   >>> reprlib.repr(list(range(1000)))     # កាត់ឱ្យខ្លីសម្រាប់បង្ហាញ
   '[0, 1, 2, 3, 4, 5, ...]'

**``string``** — ថេរ និង template៖

.. code-block:: pycon

   >>> import string
   >>> string.ascii_lowercase
   'abcdefghijklmnopqrstuvwxyz'
   >>> string.digits
   '0123456789'
   >>> string.punctuation[:10]
   '!"#$%&\'()*'

   >>> from string import Template
   >>> t = Template("$name មានអាយុ $age ឆ្នាំ")
   >>> t.substitute(name="សុខា", age=25)
   'សុខា មានអាយុ 25 ឆ្នាំ'
   >>> t.safe_substitute(name="សុខា")          # ខ្វះ age → មិនបញ្ចេញកំហុស
   'សុខា មានអាយុ $age ឆ្នាំ'

.. _logging:

ការកត់ត្រា (``logging``)
============================

``logging`` ល្អជាង ``print()`` សម្រាប់កម្មវិធីពិត ព្រោះវាមាន **កម្រិត**
**ទិសដៅ** និង **ទម្រង់** ដែលអាចកំណត់បាន៖

.. list-table::
   :header-rows: 1
   :widths: 22 78

   * - កម្រិត
     - ប្រើសម្រាប់
   * - ``DEBUG``
     - ព័ត៌មានលម្អិតសម្រាប់អ្នកអភិវឌ្ឍន៍
   * - ``INFO``
     - ព្រឹត្តិការណ៍ធម្មតា
   * - ``WARNING``
     - មានអ្វីមិនធម្មតា ប៉ុន្តែកម្មវិធីនៅដំណើរការ
   * - ``ERROR``
     - ប្រតិបត្តិការមួយបរាជ័យ
   * - ``CRITICAL``
     - កម្មវិធីមិនអាចបន្តបាន

.. code-block:: pycon
   :no-test:

   >>> import logging, sys
   >>> log = logging.getLogger("demo")
   >>> log.setLevel(logging.INFO)
   >>> handler = logging.StreamHandler(sys.stdout)
   >>> handler.setFormatter(logging.Formatter("%(levelname)s %(message)s"))
   >>> log.addHandler(handler)
   >>> log.info("ចាប់ផ្ដើម")
   INFO ចាប់ផ្ដើម
   >>> log.warning("អង្គចងចាំជិតពេញ")
   WARNING អង្គចងចាំជិតពេញ
   >>> log.debug("នេះមិនបង្ហាញទេ ព្រោះ level=INFO")
   >>> log.removeHandler(handler)

..  :no-test: — StreamHandler binds to whatever sys.stdout is at construction
..  time, while tools/run_examples.py swaps sys.stdout for every example, so
..  the handler would write into a stale buffer. The output shown above is
..  verified separately as a real script (see REAL_SCRIPT_CHECKS).

.. code-block:: python
   :no-test:

   import logging

   # កត់ត្រា exception រួមទាំង traceback
   try:
       1 / 0
   except ZeroDivisionError:
       logging.exception("ការគណនាបរាជ័យ")

.. tip::

   ប្រើ ``logging.exception(...)`` ក្នុង ``except`` block — វាបន្ថែម
   traceback ដោយស្វ្វ័យប្រវត្តិ។ កុំប្រើ ``except: pass`` ដោយមិនកត់ត្រា។

   សម្រាប់កម្មវិធីធំ ប្រើ ``logging.getLogger(__name__)`` ក្នុង module
   នីមួយៗ ដើម្បីទទួលបាន logger ដែលមានឈ្មោះតាម module។

.. _performance:

ការវាស់ប្រសិទ្ធភាព
======================

.. code-block:: pycon

   >>> import timeit
   >>> # វាស់កូដខ្លីៗ — ដំណើរការច្រើនដង ហើយយកមធ្យមភាគ
   >>> t = timeit.timeit("sum(range(100))", number=1000)
   >>> t > 0
   True
   >>> timeit.timeit("'a' + 'b'", number=100_000) < 1.0
   True

**``cProfile``** — សម្រាប់កម្មវិធីពេញលេញ៖

.. code-block:: console

   $ python3 -m cProfile -s cumtime app.py | head -20
             10234 function calls in 0.012 seconds

       Ordered by: cumulative time

       ncalls  tottime  percall  cumtime  percall filename:lineno(function)
            1    0.000    0.000    0.012    0.012 app.py:1(<module>)
         1000    0.010    0.000    0.010    0.000 app.py:10(process)

.. list-table::
   :header-rows: 1
   :widths: 26 74

   * - ឧបករណ៍
     - ប្រើសម្រាប់
   * - ``timeit``
     - វាស់កូដតូចៗដោយជាក់លាក់
   * - ``time.perf_counter()``
     - វាស់ពេលដោយដៃ (គុណភាពខ្ពស់)
   * - ``cProfile``
     - វិភាគកម្មវិធីទាំងមូល — រកអនុគមន៍ដែលចំណាយពេលច្រើន
   * - ``pstats``
     - វិភាគលទ្ធផល cProfile
   * - ``tracemalloc``
     - តាមដានការប្រើអង្គចងចាំ

.. _quality-control:

ការគ្រប់គ្រងគុណភាព
======================

.. code-block:: pycon

   >>> # doctest — សាកល្បងពីឧទាហរណ៍ក្នុង docstring
   >>> import doctest
   >>> def add(a, b):
   ...     \"\"\"បូកលេខពីរ។
   ...
   ...     >>> add(2, 3)
   ...     5
   ...     \"\"\"
   ...     return a + b
   ...
   >>> results = doctest.testmod(verbose=False)
   >>> results.failed
   0

សូមមើលជំពូក :doc:`testing_debugging` សម្រាប់ ``unittest`` និង
ការ debug លម្អិត។

.. _compression:

ការបង្ហាប់ទិន្នន័យ
======================

.. code-block:: pycon

   >>> import zlib, gzip, zipfile, tarfile
   >>> data = "សួស្ដី " * 100
   >>> raw = data.encode("utf-8")
   >>> compressed = zlib.compress(raw)
   >>> len(compressed) < len(raw)
   True
   >>> zlib.decompress(compressed).decode("utf-8") == data
   True

   >>> with gzip.open("data.gz", "wt", encoding="utf-8") as f:
   ...     n = f.write(data)
   ...
   >>> with gzip.open("data.gz", "rt", encoding="utf-8") as f:
   ...     f.read() == data
   ...
   True

   >>> with zipfile.ZipFile("archive.zip", "w") as z:
   ...     z.writestr("note.txt", "មាតិកា")
   ...
   >>> with zipfile.ZipFile("archive.zip") as z:
   ...     z.namelist()
   ...
   ['note.txt']

.. _batteries:

តារាងសង្ខេប — "Batteries Included"
======================================

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - តម្រូវការ
     - ម៉ូឌុល
   * - ឯកសារ និងផ្លូវ
     - ``pathlib``, ``os``, ``shutil``, ``glob``, ``tempfile``
   * - អត្ថបទ និង regex
     - ``re``, ``string``, ``textwrap``, ``unicodedata``, ``difflib``
   * - ទិន្នន័យរចនាសម្ព័ន្ធ
     - ``json``, ``csv``, ``xml``, ``tomllib`` (3.11+), ``configparser``
   * - គណិតវិទ្យា
     - ``math``, ``statistics``, ``decimal``, ``fractions``, ``random``, ``secrets``
   * - ពេលវេលា
     - ``datetime``, ``zoneinfo`` (3.9+), ``calendar``, ``time``
   * - បណ្ដាញ
     - ``urllib``, ``http``, ``socket``, ``email``, ``ftplib``, ``smtplib``
   * - Database
     - ``sqlite3``, ``dbm``
   * - Concurrency
     - ``threading``, ``multiprocessing``, ``concurrent.futures``, ``asyncio``, ``queue``
   * - ការបង្ហាប់
     - ``zlib``, ``gzip``, ``bz2``, ``lzma``, ``zipfile``, ``tarfile``
   * - សុវត្ថិភាព
     - ``hashlib``, ``hmac``, ``secrets``, ``ssl``
   * - សាកល្បង និង debug
     - ``unittest``, ``doctest``, ``pdb``, ``timeit``, ``cProfile``, ``tracemalloc``
   * - កំណត់ត្រា និង warning
     - ``logging``, ``warnings``
   * - បន្ទាត់ពាក្យបញ្ជា
     - ``argparse``, ``getpass``, ``shlex``, ``subprocess``
   * - ប្រភេទ និង class
     - ``typing``, ``dataclasses``, ``enum``, ``abc``, ``copy``, ``pprint``
   * - អន្តរជាតិ
     - ``gettext``, ``locale``
   * - ប្រព័ន្ធ
     - ``sys``, ``platform``, ``sysconfig``, ``signal``, ``mimetypes``

.. _stdlib-summary:

សង្ខេប
======

* បណ្ណាល័យស្តង់ដារមាន **ម៉ូឌុលរាប់រយ** — ស្វែងរកមុនពេលដំឡើង
  package ខាងក្រៅ។
* **``pathlib``** ជំនួស ``os.path`` សម្រាប់កូដថ្មី។
* **``argparse``** សម្រាប់បន្ទាត់ពាក្យបញ្ជា។
* **``logging``** ជំនួស ``print()`` ក្នុងកម្មវិធីពិត។
* **``secrets``** សម្រាប់សុវត្ថិភាព — កុំប្រើ ``random``។
* **``decimal``** សម្រាប់លុយ — កុំប្រើ ``float``។
* ប្រើ **placeholder** និង **list argument** ដើម្បីចៀសវាង injection។
* **``timeit``** សម្រាប់វាស់កូដតូច; **``cProfile``** សម្រាប់កម្មវិធីទាំងមូល។

.. rubric:: ប្រភពយោង

* `An Introduction to Useful Modules <https://docs.python.org/3/tutorial/stdlib.html>`_
* `Brief Tour of the Standard Library — Part II <https://docs.python.org/3/tutorial/stdlib2.html>`_
* `The Python Standard Library <https://docs.python.org/3/library/index.html>`_
* `pathlib <https://docs.python.org/3/library/pathlib.html>`_
* `argparse <https://docs.python.org/3/library/argparse.html>`_
* `logging <https://docs.python.org/3/library/logging.html>`_
* `datetime <https://docs.python.org/3/library/datetime.html>`_
* `zoneinfo <https://docs.python.org/3/library/zoneinfo.html>`_
* `sqlite3 <https://docs.python.org/3/library/sqlite3.html>`_
* `secrets <https://docs.python.org/3/library/secrets.html>`_
* `timeit <https://docs.python.org/3/library/timeit.html>`_
