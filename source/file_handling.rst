.. _file-handling:

.. container:: src-note

   ប្រភពដើម៖ CPython ``Doc/tutorial/inputoutput.rst`` (ផ្នែក *Reading and
   writing files*), ``Doc/library/functions.rst`` (``open``),
   ``Doc/library/pathlib.rst``, ``Doc/library/json.rst``, ``Doc/library/os.rst`` ·
   `ឯកសារផ្លូវការ <https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files>`_

##########################
ការគ្រប់គ្រងឯកសារ
##########################

.. _open:

អនុគមន៍ ``open()``
==================

``open()`` ត្រឡប់ **file object** មួយ។ ទម្រង់ដែលប្រើញឹកញាប់បំផុត៖

.. code-block:: python
   :no-test:

   f = open(filename, mode="r", encoding="utf-8")

.. list-table:: Parameter សំខាន់ៗ
   :header-rows: 1
   :widths: 18 82

   * - Parameter
     - ការពិពណ៌នា
   * - ``file``
     - ឈ្មោះឯកសារ (str ឬ path-like object)
   * - ``mode``
     - របៀបប្រើប្រាស់ឯកសារ (មើលតារាងខាងក្រោម)
   * - ``encoding``
     - encoding សម្រាប់ text mode។ **លំនាំដើមអាស្រ័យលើប្រព័ន្ធ** — សូមបញ្ជាក់ជាច្បាស់
   * - ``newline``
     - ការគ្រប់គ្រងការបំលែងបន្ទាត់ថ្មី។ ប្រើ ``""`` សម្រាប់ឯកសារ CSV
   * - ``errors``
     - របៀបដោះស្រាយកំហុស encoding ឧ. ``"strict"`` (លំនាំដើម), ``"replace"``, ``"ignore"``

.. _modes:

Mode របស់ ``open()``
--------------------

.. list-table::
   :header-rows: 1
   :widths: 14 86

   * - Mode
     - អត្ថន័យ
   * - ``"r"``
     - **អាន** តែប៉ុណ្ណោះ (លំនាំដើម)។ ``FileNotFoundError`` បើឯកសារមិនមាន
   * - ``"w"``
     - **សរសេរ**។ បង្កើតឯកសារថ្មី ឬ **លុបមាតិកាចាស់ទាំងអស់** បើមានស្រាប់
   * - ``"a"``
     - **បន្ថែម** (append) នៅចុងឯកសារ។ បង្កើតឯកសារថ្មីបើមិនមាន
   * - ``"x"``
     - **បង្កើតដាច់ខាត**។ ``FileExistsError`` បើឯកសារមានស្រាប់
   * - ``"r+"``
     - អាន **និង** សរសេរ។ មិនលុបមាតិកាចាស់ទេ
   * - ``"w+"``
     - អាន **និង** សរសេរ។ លុបមាតិកាចាស់
   * - ``"a+"``
     - អាន **និង** បន្ថែម
   * - ``"b"``
     - សញ្ញាបន្ថែម — **binary mode**។ ឧ. ``"rb"``, ``"wb"``
   * - ``"t"``
     - សញ្ញាបន្ថែម — **text mode** (លំនាំដើម)។ ឧ. ``"rt"``

.. code-block:: pycon

   >>> open("មិនមាន.txt")            # លំនាំដើម mode="r"
   Traceback (most recent call last):
     ...
   FileNotFoundError: [Errno 2] No such file or directory: 'មិនមាន.txt'

   >>> import os.path
   >>> open("មិនមាន.txt", "x").close()   # បង្កើតបាន
   >>> os.path.exists("មិនមាន.txt")
   True

.. warning::

   ``"w"`` **លុបមាតិកាឯកសារចាស់ទាំងស្រុង** ភ្លាមៗនៅពេលបើក។
   បើអ្នកចង់រក្សាទុកទិន្នន័យចាស់ ប្រើ ``"a"`` (បន្ថែម) ឬ ``"x"``
   (បរាជ័យបើមានស្រាប់)។

.. _text-vs-binary:

Text Mode និង Binary Mode
-------------------------

.. list-table::
   :header-rows: 1
   :widths: 20 40 40

   * -
     - **Text mode** (លំនាំដើម)
     - **Binary mode** (បន្ថែម ``b``)
   * - អាន/សរសេរជា
     - ``str``
     - ``bytes``
   * - ``encoding``
     - អាចបញ្ជាក់បាន
     - ❌ មិនអាច — ``ValueError``
   * - បំលែងបន្ទាត់ថ្មី
     - ✅ បំលែង ``\r\n`` ↔ ``\n`` ស្វ័យប្រវត្តិ
     - ❌ គ្មានការបំលែង
   * - ប្រើសម្រាប់
     - ឯកសារអត្ថបទ ``.txt``, ``.py``, ``.csv``, ``.json``
     - រូបភាព សំឡេង វីដេអូ PDF ``.zip`` ``.exe``

.. important::

   បើអ្នកអានឯកសារ binary (ដូចជា JPEG) ក្នុង text mode ទិន្នន័យនឹង **ខូច**។
   ប្រើ ``"rb"`` ជានិច្ចសម្រាប់ឯកសារដែលមិនមែនជាអត្ថបទ។

.. _with-statement:

ពាក្យបញ្ជា ``with`` — វិធីត្រឹមត្រូវ
====================================

.. code-block:: python

   from pathlib import Path

   Path("notes.txt").write_text("មាតិកាសាកល្បង", encoding="utf-8")

   with open("notes.txt", encoding="utf-8") as f:
       content = f.read()

   print(content)       # មាតិកាសាកល្បង
   print(f.closed)      # True — ឯកសារត្រូវបានបិទដោយស្វ័យប្រវត្តិ

``with`` បង្កើត *context manager* ដែលធានាថាឯកសារត្រូវបាន **បិទត្រឹមត្រូវ**
បន្ទាប់ពី block ចប់ — សូម្បីតែបើមាន exception កើតឡើង។

.. warning::

   បើអ្នក **មិន** ប្រើ ``with`` អ្នកត្រូវហៅ ``f.close()`` ដោយខ្លួនឯង។
   ការសរសេរ ``f.write()`` ដោយមិនបិទឯកសារ **អាច** បណ្ដាលឱ្យទិន្នន័យ
   មិនត្រូវបានសរសេរទៅថាសពេញលេញ សូម្បីតែកម្មវិធីបញ្ចប់ដោយជោគជ័យក៏ដោយ។
   ដូច្នេះ **ប្រើ ``with`` ជានិច្ច**។

.. code-block:: python

   from pathlib import Path
   Path("data.txt").write_text("ទិន្នន័យ", encoding="utf-8")

   # ❌ មិនណែនាំ — អាចបែកធ្លាយធនធាន
   f = open("data.txt", encoding="utf-8")
   data = f.read()
   f.close()          # មិនដំណើរការបើមាន exception

   # ✅ ណែនាំ
   with open("data.txt", encoding="utf-8") as f:
       data = f.read()

អ្នកក៏អាចបើកឯកសារច្រើនក្នុង ``with`` តែមួយ៖

.. code-block:: python

   from pathlib import Path
   Path("input.txt").write_text("abc", encoding="utf-8")

   with (
       open("input.txt", encoding="utf-8") as src,
       open("output.txt", "w", encoding="utf-8") as dst,
   ):
       dst.write(src.read().upper())

   print(Path("output.txt").read_text(encoding="utf-8"))   # ABC

.. note::

   វាក្យសម្ពន្ធ វង់ក្រចកនៅក្នុង ``with`` ត្រូវការ Python 3.10+ ដើម្បីដំណើរការ
   ត្រឹមត្រូវជាមួយ context manager ច្រើន។ សម្រាប់កំណែចាស់ជាង ប្រើ backslash
   ឬ ``contextlib.ExitStack``។

.. _reading:

ការអានឯកសារ
============

.. _read-methods:

Method សម្រាប់អាន
-----------------

.. list-table::
   :header-rows: 1
   :widths: 26 74

   * - Method
     - ត្រឡប់
   * - ``f.read()``
     - មាតិកា **ទាំងអស់** ជាខ្សែអក្សរតែមួយ
   * - ``f.read(size)``
     - តួអក្សរច្រើនបំផុត ``size`` (ឬ byte ក្នុង binary mode)
   * - ``f.readline()``
     - **មួយបន្ទាត់** រួមទាំង ``\n`` នៅចុង (លើកលែងបន្ទាត់ចុងក្រោយ)
   * - ``f.readlines()``
     - **list** នៃបន្ទាត់ទាំងអស់
   * - ``for line in f:``
     - ដើរលើបន្ទាត់ម្ដងមួយៗ — **ល្អបំផុតសម្រាប់ឯកសារធំ**

.. code-block:: pycon

   >>> # បង្កើតឯកសារសាកល្បង
   >>> with open("demo.txt", "w", encoding="utf-8") as f:
   ...     n = f.write("បន្ទាត់ទីមួយ\nបន្ទាត់ទីពីរ\nបន្ទាត់ទីបី\n")
   ...
   >>> n                       # ចំនួនតួអក្សរដែលបានសរសេរ
   38

   >>> with open("demo.txt", encoding="utf-8") as f:
   ...     print(repr(f.read()))
   ...
   'បន្ទាត់ទីមួយ\nបន្ទាត់ទីពីរ\nបន្ទាត់ទីបី\n'

   >>> with open("demo.txt", encoding="utf-8") as f:
   ...     print(repr(f.readline()))
   ...     print(repr(f.readline()))
   ...
   'បន្ទាត់ទីមួយ\n'
   'បន្ទាត់ទីពីរ\n'

   >>> with open("demo.txt", encoding="utf-8") as f:
   ...     lines = f.readlines()
   ...
   >>> len(lines)
   3

**ដើរលើឯកសារបន្ទាត់ម្ដងមួយៗ** — ប្រើអង្គចងចាំតិចបំផុត៖

.. code-block:: python

   with open("demo.txt", encoding="utf-8") as f:
       for line in f:
           print(line.strip())     # strip() លុប \n នៅចុង

.. tip::

   ប្រើ ``for line in f:`` ជំនួស ``f.readlines()`` សម្រាប់ឯកសារធំ។
   ``readlines()`` ផ្ទុកឯកសារ **ទាំងមូល** ក្នុងអង្គចងចាំ ខណៈការដើរលើ
   file object អានតែមួយបន្ទាត់ក្នុងពេលតែមួយ។

.. important::

   បើអ្នកហៅ ``f.read()`` ពីរដង ការហៅលើកទីពីរត្រឡប់ **ខ្សែអក្សរទទេ**
   ព្រោះទីតាំងអានបានដល់ចុងឯកសារហើយ៖

   .. code-block:: pycon

      >>> with open("demo.txt", encoding="utf-8") as f:
      ...     first = f.read()
      ...     second = f.read()
      ...
      >>> len(first) > 0, second
      (True, '')

.. _writing:

ការសរសេរឯកសារ
==============

.. list-table::
   :header-rows: 1
   :widths: 26 74

   * - Method
     - ការពិពណ៌នា
   * - ``f.write(s)``
     - សរសេរខ្សែអក្សរ ``s``។ ត្រឡប់ចំនួនតួអក្សរដែលបានសរសេរ
   * - ``f.writelines(seq)``
     - សរសេរលំដាប់នៃខ្សែអក្សរ។ **មិនបន្ថែម** ``\n`` ដោយស្វ័យប្រវត្តិទេ
   * - ``f.flush()``
     - បញ្ជូន buffer ទៅឯកសារភ្លាម ដោយមិនបិទឯកសារ

.. code-block:: python

   with open("output.txt", "w", encoding="utf-8") as f:
       f.write("បន្ទាត់ទីមួយ\n")       # ត្រូវដាក់ \n ដោយខ្លួនឯង
       f.write("បន្ទាត់ទីពីរ\n")

   with open("output.txt", "a", encoding="utf-8") as f:
       f.write("បន្ទាត់បន្ថែម\n")

   lines = ["ក", "ខ", "គ"]
   with open("list.txt", "w", encoding="utf-8") as f:
       f.writelines(line + "\n" for line in lines)   # បន្ថែម \n ដោយខ្លួនឯង

.. warning::

   ``writelines()`` **មិនបន្ថែមបន្ទាត់ថ្មីទេ** — ឈ្មោះរបស់វាបង្កើតការយល់ច្រឡំ។
   អ្នកត្រូវដាក់ ``"\n"`` ក្នុងខ្សែអក្សរនីមួយៗដោយខ្លួនឯង។

.. code-block:: pycon

   >>> with open("bad.txt", "w", encoding="utf-8") as f:
   ...     f.writelines(["a", "b", "c"])
   ...
   >>> print(open("bad.txt", encoding="utf-8").read())
   abc

.. _seek-tell:

``seek()`` និង ``tell()``
-------------------------

.. list-table::
   :header-rows: 1
   :widths: 26 74

   * - Method
     - ការពិពណ៌នា
   * - ``f.tell()``
     - ទីតាំងបច្ចុប្បន្នក្នុងឯកសារ (ជា byte)
   * - ``f.seek(offset[, whence])``
     - ផ្លាស់ទីតាំង។ ``whence``: 0=ដើម (លំនាំដើម), 1=បច្ចុប្បន្ន, 2=ចុង

.. code-block:: pycon

   >>> with open("demo.txt", "rb") as f:
   ...     print("ទីតាំងដើម:", f.tell())
   ...     chunk = f.read(4)
   ...     print("បន្ទាប់ពីអាន 4 byte:", f.tell())
   ...     _ = f.seek(0)
   ...     print("បន្ទាប់ពី seek(0):", f.tell())
   ...
   ទីតាំងដើម: 0
   បន្ទាប់ពីអាន 4 byte: 4
   បន្ទាប់ពី seek(0): 0

.. note::

   ក្នុង **text mode** ``tell()`` ត្រឡប់លេខ opaque ដែលមិនមែនជាចំនួនតួអក្សរ
   ទេ ហើយ ``seek()`` អាចប្រើបានតែជាមួយតម្លៃដែលទទួលពី ``tell()``
   (ឬ 0)។ សម្រាប់ការគ្រប់គ្រងទីតាំងពិតប្រាកដ សូមប្រើ **binary mode**។

.. _closed-files:

ឯកសារដែលបានបិទ
-----------------

.. code-block:: pycon

   >>> f = open("demo.txt", encoding="utf-8")
   >>> f.close()
   >>> f.closed
   True
   >>> f.read()
   Traceback (most recent call last):
     ...
   ValueError: I/O operation on closed file.

----

.. _pathlib:

``pathlib`` — ការគ្រប់គ្រងផ្លូវឯកសារ
====================================

ម៉ូឌុល ``pathlib`` ផ្ដល់វិធីស្អាតជាងក្នុងការធ្វើការជាមួយផ្លូវឯកសារ
ជំនួសឱ្យការភ្ជាប់ខ្សែអក្សរ។

.. code-block:: pycon

   >>> from pathlib import Path
   >>> p = Path("data") / "reports" / "2026.txt"     # / ភ្ជាប់ផ្លូវ
   >>> p
   PosixPath('data/reports/2026.txt')
   >>> p.name
   '2026.txt'
   >>> p.stem
   '2026'
   >>> p.suffix
   '.txt'
   >>> p.parent
   PosixPath('data/reports')
   >>> p.parts
   ('data', 'reports', '2026.txt')
   >>> p.with_suffix(".md")
   PosixPath('data/reports/2026.md')

.. note::

   នៅលើ Windows ``repr()`` បង្ហាញជា ``WindowsPath(...)`` ហើយផ្លូវប្រើ
   backslash។ ``pathlib`` ដោះស្រាយភាពខុសគ្នានេះដោយស្វ័យប្រវត្តិ —
   ដូច្នេះកូដរបស់អ្នកដំណើរការលើគ្រប់ប្រព័ន្ធ។

.. _pathlib-io:

អាន និងសរសេរដោយផ្ទាល់
-----------------------

.. code-block:: pycon

   >>> p = Path("quick.txt")
   >>> p.write_text("មាតិកា\nបន្ទាត់ពីរ\n", encoding="utf-8")
   18
   >>> p.read_text(encoding="utf-8")
   'មាតិកា\nបន្ទាត់ពីរ\n'
   >>> len(p.read_bytes())            # ចំនួន byte ក្នុងឯកសារ
   50
   >>> p.exists()
   True
   >>> p.is_file()
   True
   >>> p.is_dir()
   False
   >>> p.stat().st_size               # ទំហំជា byte
   50
   >>> p.unlink()                     # លុបឯកសារ
   >>> p.exists()
   False

.. important::

   ចំណាំលេខខាងលើ៖ ``write_text()`` ត្រឡប់ **១៨** (ចំនួនតួអក្សរ) ប៉ុន្តែ
   ``stat().st_size`` គឺ **៥០** (ចំនួន byte)។ អក្សរខ្មែរមួយត្រូវការ ៣ byte
   ក្នុង UTF-8 ដូច្នេះលេខទាំងពីរខុសគ្នា។ កុំច្រឡំ "ចំនួនតួអក្សរ"
   ជាមួយ "ទំហំឯកសារ"។

.. _pathlib-dirs:

ថត និងការស្វែងរក
------------------

.. code-block:: pycon

   >>> import tempfile
   >>> root = Path(tempfile.mkdtemp())       # ថតសាកល្បងដាច់ដោយឡែក
   >>> (root / "data" / "reports").mkdir(parents=True)
   >>> (root / "data" / "reports" / "2026.txt").write_text("x", encoding="utf-8")
   1
   >>> (root / "notes.txt").write_text("y", encoding="utf-8")
   1

   >>> [p.name for p in sorted(root.iterdir())]        # ធាតុក្នុងថត
   ['data', 'notes.txt']
   >>> [p.name for p in sorted(root.glob("*.txt"))]    # តែកម្រិតបច្ចុប្បន្ន
   ['notes.txt']
   >>> [p.relative_to(root).as_posix()
   ...  for p in sorted(root.rglob("*.txt"))]         # recursive
   ['data/reports/2026.txt', 'notes.txt']

   >>> Path.cwd() == Path(".").resolve()   # ថតបច្ចុប្បន្ន
   True
   >>> Path.home().is_absolute()           # ថតផ្ទះ
   True
   >>> (root / "notes.txt").resolve() == (root / "notes.txt").absolute()
   True

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Method
     - ការពិពណ៌នា
   * - ``Path.mkdir(parents=True, exist_ok=True)``
     - បង្កើតថត (រួមទាំងថតមេ) ដោយមិនបញ្ចេញកំហុសបើមានស្រាប់
   * - ``p.iterdir()``
     - ធាតុក្នុងថត (មិន recursive)
   * - ``p.glob(pattern)``
     - ស្វែងរកតាម pattern ក្នុងថតបច្ចុប្បន្ន
   * - ``p.rglob(pattern)``
     - ស្វែងរក recursive គ្រប់ថតរង
   * - ``p.walk()``
     - ដើរលើថតទាំងអស់ (Python 3.12+)
   * - ``p.unlink(missing_ok=True)``
     - លុបឯកសារ (Python 3.8+ សម្រាប់ ``missing_ok``)
   * - ``p.rmdir()``
     - លុបថតទទេ
   * - ``p.rename(target)``
     - ប្ដូរឈ្មោះ ឬផ្លាស់ទី
   * - ``p.absolute()`` / ``p.resolve()``
     - ផ្លូវពេញលេញ
   * - ``p.cwd()`` / ``Path.home()``
     - ថតបច្ចុប្បន្ន / ថតផ្ទះ

.. tip::

   ``exist_ok=True`` នៅក្នុង ``mkdir()`` មានប្រយោជន៍ណាស់ — វាជៀសវាង
   ``FileExistsError`` ដោយមិនត្រូវការពិនិត្យ ``exists()`` ជាមុន។

----

.. _errors:

កំហុសទូទៅ
==========

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Exception
     - កើតឡើងពេលណា
   * - ``FileNotFoundError``
     - ឯកសារ ឬថតមិនមាន (mode ``r``, ``r+``, ``x`` លើឯកសារមានស្រាប់គឺផ្ទុយគ្នា)
   * - ``FileExistsError``
     - mode ``"x"`` លើឯកសារដែលមានស្រាប់ ឬ ``mkdir()`` ដោយគ្មាន ``exist_ok``
   * - ``PermissionError``
     - គ្មានសិទ្ធិអាន/សរសេរ
   * - ``IsADirectoryError``
     - ព្យាយាមអានថតជាឯកសារ
   * - ``NotADirectoryError``
     - ផ្លូវមិនមែនជាថត
   * - ``UnicodeDecodeError``
     - encoding ខុស
   * - ``ValueError``
     - ប្រតិបត្តិការលើឯកសារដែលបានបិទហើយ
   * - ``OSError``
     - ថាសពេញ ឬកំហុសប្រព័ន្ធផ្សេងទៀត (ជា class មេនៃភាគច្រើនខាងលើ)

.. code-block:: python

   from pathlib import Path

   def read_safely(filename):
       """អានឯកសារដោយដោះស្រាយកំហុសទូទៅទាំងអស់។"""
       try:
           with open(filename, encoding="utf-8") as f:
               return f.read()
       except FileNotFoundError:
           print(f"ឯកសារ '{filename}' មិនមានទេ")
       except PermissionError:
           print(f"គ្មានសិទ្ធិអាន '{filename}'")
       except IsADirectoryError:
           print(f"'{filename}' គឺជាថត មិនមែនឯកសារ")
       except UnicodeDecodeError:
           print(f"'{filename}' មិនមែនជាអត្ថបទ UTF-8")
       return None

.. note::

   សូមមើលជំពូក *Exceptions* (មិនទាន់បានសរសេរ) សម្រាប់ការពន្យល់ពេញលេញ
   អំពី ``try``/``except``/``else``/``finally``។

.. _encoding-best-practice:

ការអនុវត្តល្អបំផុតអំពី Encoding
-------------------------------

.. warning::

   **តែងតែបញ្ជាក់ ``encoding="utf-8"``** នៅពេលបើកឯកសារអត្ថបទ។

   លំនាំដើមរបស់ ``open()`` គឺ ``locale.getencoding()`` ដែល **ខុសគ្នាតាម
   ប្រព័ន្ធ**៖ UTF-8 នៅលើ Linux/macOS ភាគច្រើន ប៉ុន្តែអាចជា
   ``cp1252`` នៅលើ Windows អឺរ៉ុប ឬ ``cp874``/``TIS-620`` នៅលើ
   Windows ខ្មែរ។ កូដដែលដំណើរការលើម៉ាស៊ីនរបស់អ្នកអាចបរាជ័យលើ
   ម៉ាស៊ីនអ្នកផ្សេង។

   បញ្ហានេះធ្ងន់ធ្ងរជាពិសេសសម្រាប់អត្ថបទខ្មែរ។

.. code-block:: python

   from pathlib import Path
   Path("khmer.txt").write_text("សួស្ដី", encoding="utf-8")

   # ❌ គ្រោះថ្នាក់ — encoding អាស្រ័យលើប្រព័ន្ធ
   with open("khmer.txt") as f:
       text = f.read()

   # ✅ ត្រឹមត្រូវ
   with open("khmer.txt", encoding="utf-8") as f:
       text = f.read()

.. versionchanged:: 3.15
   Python មានផែនការផ្លាស់ប្ដូរ encoding លំនាំដើមទៅ UTF-8 ជាសកល
   (PEP 686)។ ទោះជាយ៉ាងណាក៏ដោយ សូមបញ្ជាក់ ``encoding`` ជានិច្ច
   ដើម្បីឱ្យកូដច្បាស់លាស់ និងអាចយល់បានដោយអ្នកអាន។

----

.. _json:

ការរក្សាទុកទិន្នន័យរចនាសម្ព័ន្ធជាមួយ ``json``
==============================================

JSON គឺជាទម្រង់ស្តង់ដារសម្រាប់ផ្លាស់ប្ដូរទិន្នន័យរចនាសម្ព័ន្ធ។

.. list-table::
   :header-rows: 1
   :widths: 28 72

   * - អនុគមន៍
     - ការពិពណ៌នា
   * - ``json.dumps(obj)``
     - បំលែង object → ខ្សែអក្សរ JSON
   * - ``json.loads(s)``
     - បំលែងខ្សែអក្សរ JSON → object
   * - ``json.dump(obj, f)``
     - សរសេរ object ទៅ **file object**
   * - ``json.load(f)``
     - អាន object ពី **file object**

.. code-block:: pycon

   >>> import json
   >>> data = {"name": "សុខា", "age": 25, "tags": ["a", "b"], "active": True}
   >>> text = json.dumps(data, ensure_ascii=False, indent=2)
   >>> print(text)
   {
     "name": "សុខា",
     "age": 25,
     "tags": [
       "a",
       "b"
     ],
     "active": true
   }
   >>> json.loads(text) == data
   True

**សរសេរ និងអានពីឯកសារ៖**

.. code-block:: python

   import json

   config = {"theme": "dark", "font_size": 14, "lang": "km"}

   # សរសេរ
   with open("config.json", "w", encoding="utf-8") as f:
       json.dump(config, f, ensure_ascii=False, indent=2)

   # អាន
   with open("config.json", encoding="utf-8") as f:
       loaded = json.load(f)

.. list-table:: Parameter មានប្រយោជន៍
   :header-rows: 1
   :widths: 26 74

   * - Parameter
     - ការពិពណ៌នា
   * - ``ensure_ascii=False``
     - **សំខាន់សម្រាប់ខ្មែរ** — រក្សាអក្សរ Unicode ដូចដើម ជំនួស ``\uXXXX``
   * - ``indent=2``
     - ធ្វើឱ្យ JSON ស្អាត ងាយអាន
   * - ``sort_keys=True``
     - តម្រៀប key តាមអក្ខរក្រម (ល្អសម្រាប់ diff ក្នុង git)
   * - ``default=func``
     - ដោះស្រាយប្រភេទដែល JSON មិនស្គាល់

.. note::

   JSON គាំទ្រតែប្រភេទមូលដ្ឋានប៉ុណ្ណោះ៖ ``dict``, ``list``, ``str``, ``int``,
   ``float``, ``bool``, ``null``។ ប្រភេទដូចជា ``set``, ``tuple``, ``datetime``
   ឬ class ផ្ទាល់ខ្លួន នឹងបញ្ចេញ ``TypeError`` លើកលែងតែអ្នកផ្ដល់
   ``default=``។ ចំណាំថា ``tuple`` ត្រូវបានបំលែងទៅជា JSON array ហើយ
   ត្រឡប់មកវិញជា ``list``។

----

.. _os-module:

ម៉ូឌុល ``os`` — ការងារមូលដ្ឋាន
==============================

``pathlib`` គ្របដណ្ដប់ភាគច្រើន ប៉ុន្តែ ``os`` នៅតែមានប្រយោជន៍៖

.. code-block:: pycon

   >>> import os
   >>> os.makedirs("a/b/c", exist_ok=True)
   >>> sorted(os.listdir("a"))         # ធាតុក្នុងថត
   ['b']
   >>> os.path.exists("a/b/c")
   True
   >>> os.path.join("a", "b", "c").replace(os.sep, "/")   # ភ្ជាប់ផ្លូវតាមប្រព័ន្ធ
   'a/b/c'
   >>> os.rename("a/b/c", "a/b/d")
   >>> sorted(os.listdir("a/b"))
   ['d']

   >>> Path("tmp.txt").write_text("x", encoding="utf-8")
   1
   >>> os.remove("tmp.txt")            # លុបឯកសារ
   >>> os.path.exists("tmp.txt")
   False
   >>> os.rmdir("a/b/d")               # លុបថតទទេ

   >>> os.getcwd() == str(Path.cwd())  # ថតបច្ចុប្បន្ន
   True
   >>> "HOME" in os.environ or "USERPROFILE" in os.environ
   True

.. list-table:: ប្រៀបធៀប ``os.path`` និង ``pathlib``
   :header-rows: 1
   :widths: 40 60

   * - ``os.path`` (ចាស់)
     - ``pathlib`` (ណែនាំ)
   * - ``os.path.join(a, b)``
     - ``Path(a) / b``
   * - ``os.path.exists(p)``
     - ``Path(p).exists()``
   * - ``os.path.isfile(p)``
     - ``Path(p).is_file()``
   * - ``os.path.basename(p)``
     - ``Path(p).name``
   * - ``os.path.dirname(p)``
     - ``Path(p).parent``
   * - ``os.path.splitext(p)``
     - ``Path(p).stem`` / ``Path(p).suffix``
   * - ``os.path.getsize(p)``
     - ``Path(p).stat().st_size``
   * - ``os.path.abspath(p)``
     - ``Path(p).resolve()``

.. tip::

   សម្រាប់កូដថ្មី ប្រើ ``pathlib``។ វាអានងាយជាង មិនមានបញ្ហា separator
   តាមប្រព័ន្ធ និងផ្ដល់ method ទាំងអស់នៅលើ object តែមួយ។

----

.. _csv:

ឯកសារ CSV
==========

.. code-block:: python

   import csv

   rows = [
       ["ឈ្មោះ", "អាយុ", "ទីក្រុង"],
       ["សុខា", "25", "ភ្នំពេញ"],
       ["ដារ៉ា", "30", "សៀមរាប"],
   ]

   # សរសេរ
   with open("people.csv", "w", encoding="utf-8", newline="") as f:
       writer = csv.writer(f)
       writer.writerows(rows)

   # អាន
   with open("people.csv", encoding="utf-8", newline="") as f:
       for row in csv.reader(f):
           print(row)

.. important::

   ប្រើ ``newline=""`` ជានិច្ចនៅពេលបើកឯកសារ CSV។ បើមិនដូច្នោះទេ
   នៅលើ Windows អ្នកនឹងទទួលបានបន្ទាត់ទទេរវាងជួរនីមួយៗ ព្រោះ
   ម៉ូឌុល ``csv`` គ្រប់គ្រងបន្ទាត់ថ្មីដោយខ្លួនឯង។

---

.. _best-practices:

ការអនុវត្តល្អបំផុត — សង្ខេប
===============================

#. **ប្រើ ``with`` ជានិច្ច** ដើម្បីធានាថាឯកសារត្រូវបានបិទ។
#. **បញ្ជាក់ ``encoding="utf-8"``** សម្រាប់ឯកសារអត្ថបទទាំងអស់។
#. **ប្រើ ``"rb"``/``"wb"``** សម្រាប់ឯកសារ binary។
#. **អានបន្ទាត់ម្ដងមួយៗ** (``for line in f``) សម្រាប់ឯកសារធំ។
#. **ប្រើ ``pathlib``** សម្រាប់ការគ្រប់គ្រងផ្លូវ។
#. **ប្រើ ``newline=""``** សម្រាប់ឯកសារ CSV។
#. **ចាប់យក exception ជាក់លាក់** — កុំប្រើ ``except:`` ទទេ។
#. **កុំប្រើ mode ``"w"``** លើឯកសារដែលអ្នកមិនចង់លុប។
#. សម្រាប់ការសរសេរដែលត្រូវតែជោគជ័យទាំងស្រុង សូមសរសេរទៅឯកសារ
   បណ្ដោះអាសន្ន រួច ``Path.rename()`` ទៅឈ្មោះចុងក្រោយ។

.. rubric:: ប្រភពយោង

* `Reading and writing files <https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files>`_
* `Methods of File Objects <https://docs.python.org/3/tutorial/inputoutput.html#methods-of-file-objects>`_
* `open() <https://docs.python.org/3/library/functions.html#open>`_
* `pathlib — Object-oriented filesystem paths <https://docs.python.org/3/library/pathlib.html>`_
* `json — JSON encoder and decoder <https://docs.python.org/3/library/json.html>`_
* `os — Miscellaneous operating system interfaces <https://docs.python.org/3/library/os.html>`_
* `csv — CSV File Reading and Writing <https://docs.python.org/3/library/csv.html>`_
