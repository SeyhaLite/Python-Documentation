.. _exceptions:

.. container:: src-note

   ប្រភពដើម៖ CPython ``Doc/tutorial/errors.rst``,
   ``Doc/library/exceptions.rst``, ``Doc/reference/simple_stmts.rst`` ·
   `ឯកសារផ្លូវការ <https://docs.python.org/3/tutorial/errors.html>`_

#######################################
Exceptions និងការគ្រប់គ្រងកំហុស
#######################################

Python មានកំហុសពីរប្រភេទខុសគ្នាដាច់ស្រឡះ៖

.. list-table::
   :header-rows: 1
   :widths: 24 76

   * - ប្រភេទ
     - កើតឡើងពេលណា
   * - **Syntax Error**
     - ពេល **parse** កូដ — មុនដំណើរការ។ កម្មវិធីមិនចាប់ផ្ដើមទេ
   * - **Exception**
     - ពេល **ដំណើរការ** (runtime) — ទោះបីជាវាក្យសម្ពន្ធត្រឹមត្រូវក៏ដោយ

.. _syntax-errors:

Syntax Error
============

.. code-block:: pycon

   >>> while True print("x")
     File "<stdin>", line 1
       while True print("x")
                  ^^^^^
   SyntaxError: invalid syntax

   >>> print("មិនបានបិទ
     File "<stdin>", line 1
       print("មិនបានបិទ
             ^
   SyntaxError: unterminated string literal (detected at line 1)

Python បង្ហាញ **ទីតាំងជាក់លាក់** ដែលវារកឃើញបញ្ហា ដោយប្រើសញ្ញា ``^``
ចង្អុលទៅកន្លែងខុស។

.. tip::

   Python 3.10+ មានសារ SyntaxError លម្អិតណាស់ — វាអាចចង្អុលបង្ហាញ
   វង់ក្រចកដែលមិនបានបិទ ការខ្វះ indentation និងកំហុស f-string។
   សូម **អានសារកំហុសទាំងមូល** មិនមែនតែបន្ទាត់ចុងក្រោយទេ។

.. _exceptions-basics:

Exception
=========

Exception គឺជា **object** ដែល Python បង្កើតនៅពេលមានអ្វីខុសកំឡុងពេល
ដំណើរការ។ បើមិនបានចាប់យក (handle) កម្មវិធីនឹងឈប់ ហើយបោះពុម្ព
**traceback**៖

.. code-block:: pycon

   >>> 10 / 0
   Traceback (most recent call last):
     ...
   ZeroDivisionError: division by zero

   >>> int("abc")
   Traceback (most recent call last):
     ...
   ValueError: invalid literal for int() with base 10: 'abc'

   >>> undefined_name
   Traceback (most recent call last):
     ...
   NameError: name 'undefined_name' is not defined

   >>> [1, 2, 3][10]
   Traceback (most recent call last):
     ...
   IndexError: list index out of range

.. _reading-traceback:

ការអាន Traceback
----------------

Traceback អាន **ពីលើចុះក្រោម** — បង្ហាញជាមុនថាការហៅបានឆ្លងកាត់
អនុគមន៍ណាខ្លះ រួចបញ្ចប់ដោយកំហុសជាក់ស្ដែងនៅ **បន្ទាត់ចុងក្រោយ**៖

.. code-block:: text

   Traceback (most recent call last):        ← ចាប់ផ្ដើម
     File "app.py", line 42, in handle      ← កម្រិតខាងក្រៅបំផុត
       result = process(data)
     File "core.py", line 17, in process    ← កម្រិតខាងក្នុង
       return parse(value)
     File "core.py", line 9, in parse       ← កន្លែងកំហុសកើតឡើង
       return int(value)
   ValueError: invalid literal for int()    ← ប្រភេទកំហុស + សារ
           with base 10: 'hello'

**លំដាប់សម្រាប់អាន៖**

#. អាន **បន្ទាត់ចុងក្រោយ** ជាមុន — វាប្រាប់ប្រភេទកំហុស និងមូលហេតុ។
#. បន្ទាប់មកអាន **frame ចុងក្រោយ** (បន្ទាត់មុនចុងក្រោយ) — វាប្រាប់
   ឯកសារ លេខបន្ទាត់ និងអនុគមន៍ដែលកំហុសកើតឡើង។
#. បើត្រូវការយល់បរិបទ សូមអានឡើងលើ។

.. note::

   ``(most recent call last)`` មានន័យថា frame **ចុងក្រោយ** គឺជាការហៅ
   **ថ្មីបំផុត**។ នេះផ្ទុយពីភាសាខ្លះដែលរាយពីក្នុងចេញក្រៅ។

.. _try-except:

``try`` / ``except``
====================

.. code-block:: python

   def safe_divide(a, b):
       """ចែកលេខដោយដោះស្រាយការចែកនឹងសូន្យ។"""
       try:
           return a / b
       except ZeroDivisionError:
           print("មិនអាចចែកនឹងសូន្យបានទេ")
           return None

.. code-block:: pycon

   >>> safe_divide(10, 2)
   5.0
   >>> safe_divide(10, 0)
   មិនអាចចែកនឹងសូន្យបានទេ

រចនាសម្ព័ន្ធពេញលេញ៖

.. code-block:: python
   :no-test:

   try:
       risky_operation()
   except SomeError:
       handle_it()
   except (OtherError, AnotherError) as err:
       handle_multiple(err)
   else:
       runs_only_if_no_exception()
   finally:
       always_runs()

.. list-table::
   :header-rows: 1
   :widths: 18 82

   * - ផ្នែក
     - ពេលណាដំណើរការ
   * - ``try``
     - កូដដែលអាចបញ្ចេញ exception
   * - ``except``
     - តែនៅពេលមាន exception ដែល **ត្រូវគ្នា** កើតឡើង
   * - ``else``
     - តែនៅពេល **គ្មាន** exception កើតឡើងក្នុង ``try``
   * - ``finally``
     - **ជានិច្ច** — សូម្បីតែមាន ``return``, ``break``, ``continue``
       ឬ exception ដែលមិនបានចាប់យក

.. _catching-object:

ចាប់យក Object នៃ Exception
--------------------------

ប្រើ ``as`` ដើម្បីទទួល exception object ផ្ទាល់៖

.. code-block:: pycon

   >>> try:
   ...     int("abc")
   ... except ValueError as err:
   ...     print(type(err).__name__)
   ...     print(err)
   ...     print(err.args)
   ...
   ValueError
   invalid literal for int() with base 10: 'abc'
   ("invalid literal for int() with base 10: 'abc'",)

.. _multiple-except:

ចាប់យក Exception ច្រើន
----------------------

.. code-block:: python

   raw = "0"          # សាកល្បងជាមួយ "abc" ដើម្បីឃើញសាខា ValueError

   # វិធី ១ — clause ដាច់ដោយឡែក (ល្អបំផុត ព្រោះដោះស្រាយខុសគ្នា)
   try:
       value = int(raw)
       result = 100 / value
   except ValueError:
       print("មិនមែនជាលេខទេ")
   except ZeroDivisionError:
       print("មិនអាចចែកនឹងសូន្យទេ")

   # វិធី ២ — tuple (ពេលដោះស្រាយដូចគ្នា)
   try:
       value = int(raw)
       result = 100 / value
   except (ValueError, ZeroDivisionError) as err:
       print(f"កំហុសទិន្នន័យ: {err}")

.. important::

   ``except`` clause ត្រូវបានសាកល្បង **ពីលើចុះក្រោម** ហើយតែមួយគត់
   ដែលត្រូវគ្នានឹងដំណើរការ។ ដូច្នេះដាក់ clause **ជាក់លាក់** នៅខាងលើ
   និង clause **ទូទៅ** នៅខាងក្រោម។

.. _else-clause:

``else`` Clause
---------------

``else`` ដំណើរការតែនៅពេល **គ្មាន** exception។ វាល្អជាងការដាក់កូដ
ក្នុង ``try`` ព្រោះវាច្បាស់ថាកូដណាដែលអាចបរាជ័យ៖

.. code-block:: python

   raw = "42"

   def convert(n):
       return n * 2

   # ❌ មិនច្បាស់ — convert() ក៏អាចបញ្ចេញ ValueError ដែរ
   try:
       value = int(raw)
       result = convert(value)      # បើ convert បរាជ័យ នឹងត្រូវចាប់យកដូចគ្នា
   except ValueError:
       print("ទិន្នន័យមិនត្រឹមត្រូវ")

   # ✅ ច្បាស់លាស់
   try:
       value = int(raw)
   except ValueError:
       print("ទិន្នន័យមិនត្រឹមត្រូវ")
   else:
       result = convert(value)      # ដំណើរការតែពេល int() ជោគជ័យ

.. warning::

   កុំដាក់កូដដែល **មិនអាច** បរាជ័យក្នុង ``try`` block។ ``try`` គួររុំព័ទ្ធ
   តែបន្ទាត់ដែលអ្នករំពឹងថាអាចបញ្ចេញ exception ប៉ុណ្ណោះ។

.. _exception-hierarchy:

ឋានានុក្រម Exception
=====================

Exception ទាំងអស់បន្តពូជ (inherit) ពី ``BaseException``។ ការយល់ដឹងអំពីឋានានុក្រម
សំខាន់ណាស់ ព្រោះ ``except X`` ចាប់យក **X និង subclass ទាំងអស់របស់វា**។

.. code-block:: text

   BaseException
    +-- SystemExit                 ← sys.exit()
    +-- KeyboardInterrupt          ← Control-C
    +-- GeneratorExit
    +-- BaseExceptionGroup
    +-- Exception                  ← កំហុស "ធម្មតា" ទាំងអស់
         +-- StopIteration
         +-- StopAsyncIteration
         +-- ArithmeticError
         |    +-- FloatingPointError
         |    +-- OverflowError
         |    +-- ZeroDivisionError
         +-- AssertionError
         +-- AttributeError
         +-- BufferError
         +-- EOFError
         +-- ExceptionGroup
         +-- ImportError
         |    +-- ModuleNotFoundError
         +-- LookupError
         |    +-- IndexError
         |    +-- KeyError
         +-- MemoryError
         +-- NameError
         |    +-- UnboundLocalError
         +-- OSError                (ហៅផងដែរ IOError, EnvironmentError)
         |    +-- FileNotFoundError
         |    +-- FileExistsError
         |    +-- PermissionError
         |    +-- IsADirectoryError
         |    +-- NotADirectoryError
         |    +-- TimeoutError
         |    +-- ConnectionError
         |         +-- ConnectionRefusedError
         |         +-- ConnectionResetError
         +-- RecursionError
         +-- ReferenceError
         +-- RuntimeError
         |    +-- NotImplementedError
         +-- SyntaxError
         |    +-- IndentationError
         |         +-- TabError
         +-- SystemError
         +-- TypeError
         +-- ValueError
         |    +-- UnicodeError
         |         +-- UnicodeDecodeError
         |         +-- UnicodeEncodeError
         +-- Warning

.. code-block:: pycon

   >>> issubclass(IndexError, LookupError)
   True
   >>> issubclass(FileNotFoundError, OSError)
   True
   >>> issubclass(ZeroDivisionError, ArithmeticError)
   True
   >>> issubclass(ValueError, Exception)
   True
   >>> issubclass(KeyboardInterrupt, Exception)   # ❗ ទេ
   False

.. warning::

   **``KeyboardInterrupt`` និង ``SystemExit`` មិនមែនជា subclass នៃ
   ``Exception`` ទេ** — ពួកវាបន្តពូជពី ``BaseException`` ដោយផ្ទាល់។
   នេះគឺដោយចេតនា៖ ដើម្បីឱ្យ ``except Exception`` មិនស្រូបយក
   Control-C ឬ ``sys.exit()``។

.. _bare-except:

កំហុសធ្ងន់ធ្ងរ — ``except:`` ទទេ
--------------------------------

.. code-block:: python

   # ❌ គ្រោះថ្នាក់បំផុត
   try:
       do_something()
   except:            # ចាប់យក BaseException ទាំងអស់
       pass

   # ❌ ក៏មិនល្អដែរ
   try:
       do_something()
   except Exception:  # ចាប់យកកំហុសធម្មតាទាំងអស់
       pass

បញ្ហា៖

* វាលាក់ **កំហុសកម្មវិធីពិត** (``TypeError``, ``NameError``, ``AttributeError``)
  ដែលអ្នកគួរដឹង។
* វាស្រូប ``KeyboardInterrupt`` ធ្វើឱ្យអ្នកមិនអាចបញ្ឈប់កម្មវិធីដោយ
  Control-C (ករណី ``except:`` ទទេ)។
* ``pass`` ដោយគ្មានការកត់ត្រា = កំហុសបាត់ដោយស្ងាត់។

.. code-block:: python
   :no-test:

   # ✅ ចាប់យកតែអ្វីដែលអ្នកដឹងពីរបៀបដោះស្រាយ
   try:
       do_something()
   except (FileNotFoundError, PermissionError) as err:
       logger.warning("មិនអាចអានឯកសារកំណត់រចនាសម្ព័ន្ធ: %s", err)
       use_defaults()

.. tip::

   បើអ្នក **ត្រូវតែ** ចាប់យក exception ទូទៅ សូម៖

   #. កត់ត្រាវា (``logging.exception(...)`` រួមទាំង traceback)
   #. បញ្ចេញឡើងវិញ ឬបំលែងទៅ exception ដែលមានន័យ
   #. កុំប្រើ ``pass`` ដោយគ្មានមូលហេតុ

.. _raising:

ការបញ្ចេញ Exception (``raise``)
===============================

.. code-block:: pycon

   >>> raise ValueError("តម្លៃមិនត្រឹមត្រូវ")
   Traceback (most recent call last):
     ...
   ValueError: តម្លៃមិនត្រឹមត្រូវ

   >>> raise RuntimeError          # គ្មានសារ
   Traceback (most recent call last):
     ...
   RuntimeError

**បញ្ចេញឡើងវិញ (re-raise)** — កត់ត្រា រួចបណ្ដោយឱ្យកំហុសបន្ត៖

.. code-block:: python
   :no-test:

   try:
       value = int(raw)
   except ValueError:
       logger.error("ទិន្នន័យខូច: %r", raw)
       raise                        # បញ្ចេញ exception ដើមឡើងវិញ

``raise`` ដោយគ្មាន argument ក្នុង ``except`` block បញ្ចេញ exception
បច្ចុប្បន្នឡើងវិញ ដោយរក្សា traceback ដើមទាំងស្រុង។

.. note::

   អ្នកក៏អាចបញ្ចេញ exception ពី class បានដែរ៖

   .. code-block:: pycon

      >>> exc = ValueError("ខុស")
      >>> raise exc
      Traceback (most recent call last):
        ...
      ValueError: ខុស

.. _chaining:

Exception Chaining
==================

នៅពេល exception កើតឡើងក្នុង ``except`` ឬ ``finally`` block Python
ភ្ជាប់វាទៅ exception ដើមដោយស្វ័យប្រវត្តិ៖

.. code-block:: pycon

   >>> try:
   ...     1 / 0
   ... except ZeroDivisionError as exc:
   ...     raise RuntimeError("បរាជ័យក្នុងការគណនា")
   ...
   Traceback (most recent call last):
     ...
   ZeroDivisionError: division by zero

   During handling of the above exception, another exception occurred:

   Traceback (most recent call last):
     ...
   RuntimeError: បរាជ័យក្នុងការគណនា

.. _raise-from:

``raise ... from ...``
----------------------

ប្រើ ``from`` ដើម្បីបញ្ជាក់ចេតនាច្បាស់លាស់៖

.. list-table::
   :header-rows: 1
   :widths: 26 74

   * - វាក្យសម្ពន្ធ
     - អត្ថន័យ និងលទ្ធផល
   * - ``raise New from exc``
     - កំណត់ ``__cause__ = exc`` · បោះពុម្ព *"The above exception was the direct cause of…"*
   * - ``raise New`` (ក្នុង ``except``)
     - កំណត់ ``__context__ = exc`` · បោះពុម្ព *"During handling of the above exception, another exception occurred…"*
   * - ``raise New from None``
     - **លុប** ការភ្ជាប់ទាំងស្រុង · បង្ហាញតែ exception ថ្មី

.. code-block:: python

   def load_config(path):
       try:
           with open(path, encoding="utf-8") as f:
               return json.load(f)
       except OSError as exc:
           # បំលែងកំហុសប្រព័ន្ធទៅជាកំហុសកម្មវិធីដែលមានន័យ
           raise ConfigError(f"មិនអាចផ្ទុក {path}") from exc

.. code-block:: pycon

   >>> try:
   ...     raise ValueError("មូលហេតុដើម")
   ... except ValueError as exc:
   ...     raise RuntimeError("បរាជ័យ") from exc
   ...
   Traceback (most recent call last):
     ...
   ValueError: មូលហេតុដើម

   The above exception was the direct cause of the following exception:

   Traceback (most recent call last):
     ...
   RuntimeError: បរាជ័យ

**លុបការភ្ជាប់** ដោយ ``from None`` — មានប្រយោជន៍ពេលលម្អិតខាងក្នុង
មិនសំខាន់សម្រាប់អ្នកប្រើ៖

.. code-block:: pycon

   >>> try:
   ...     raise ValueError("លម្អិតផ្ទៃក្នុង")
   ... except ValueError:
   ...     raise RuntimeError("សំណើមិនត្រឹមត្រូវ") from None
   ...
   Traceback (most recent call last):
     ...
   RuntimeError: សំណើមិនត្រឹមត្រូវ

.. _custom-exceptions:

Exception ផ្ទាល់ខ្លួន
=========================

បង្កើត exception ផ្ទាល់ខ្លួនដោយបន្តពូជពី ``Exception``៖

.. code-block:: python

   class AppError(Exception):
       """មូលដ្ឋានសម្រាប់កំហុសទាំងអស់របស់កម្មវិធី។"""


   class ValidationError(AppError):
       """ទិន្នន័យមិនត្រឹមត្រូវ។"""

       def __init__(self, field, message):
           super().__init__(message)
           self.field = field


   class NotFoundError(AppError):
       """រកធាតុមិនឃើញ។"""

       def __init__(self, entity, identifier):
           super().__init__(f"{entity} '{identifier}' មិនមានទេ")
           self.entity = entity
           self.identifier = identifier

.. code-block:: pycon

   >>> try:
   ...     raise ValidationError("email", "ត្រូវមាន @")
   ... except ValidationError as err:
   ...     print(err.field, "->", err)
   ...
   email -> ត្រូវមាន @

   >>> try:
   ...     raise NotFoundError("User", 42)
   ... except AppError as err:        # ចាប់យកតាម class មេ
   ...     print(type(err).__name__, ":", err)
   ...
   NotFoundError : User '42' មិនមានទេ

.. tip::

   **អនុសញ្ញា៖**

   * បញ្ចប់ឈ្មោះដោយ ``Error`` បើវាតំណាងឱ្យកំហុស។
   * បង្កើត **class មេមួយ** សម្រាប់បណ្ណាល័យ/កម្មវិធីរបស់អ្នក
     (``AppError``) រួចបន្តពូជពីវា។ នេះអនុញ្ញាតឱ្យអ្នកប្រើចាប់យក
     កំហុសទាំងអស់របស់អ្នកដោយ ``except AppError``។
   * បន្តពូជពី ``Exception`` — **កុំ** បន្តពូជពី ``BaseException``។

.. _finally:

``finally`` — សកម្មភាពសម្អាត
================================

``finally`` block ដំណើរការ **ជានិច្ច** មិនថាមានអ្វីកើតឡើងក៏ដោយ៖

.. code-block:: pycon

   >>> def divide(x, y):
   ...     try:
   ...         result = x / y
   ...     except ZeroDivisionError:
   ...         print("ចែកនឹងសូន្យ!")
   ...     else:
   ...         print("លទ្ធផលគឺ", result)
   ...     finally:
   ...         print("ដំណើរការ finally")
   ...
   >>> divide(2, 1)
   លទ្ធផលគឺ 2.0
   ដំណើរការ finally
   >>> divide(2, 0)
   ចែកនឹងសូន្យ!
   ដំណើរការ finally

.. _finally-return:

ឥរិយាបថពិសេសរបស់ ``finally``
-----------------------------

``finally`` ដំណើរការសូម្បីតែនៅពេលមាន ``return``, ``break`` ឬ ``continue``
ក្នុង ``try``៖

.. code-block:: pycon

   >>> def f():
   ...     try:
   ...         return "ពី try"
   ...     finally:
   ...         print("finally ដំណើរការមុន return")
   ...
   >>> f()
   finally ដំណើរការមុន return
   'ពី try'

.. warning::

   បើ ``finally`` block មាន ``return`` វា **បដិសេធ** តម្លៃត្រឡប់ពី ``try``
   ឬ ``except``៖

   .. code-block:: pycon

      >>> def g():
      ...     try:
      ...         return 1
      ...     finally:
      ...         return 2
      ...
      >>> g()
      2

   នេះជាកំហុសងាយធ្វើ។ **កុំដាក់ ``return`` ក្នុង ``finally``**។

   .. versionadded:: 3.14
      Python បញ្ចេញ ``SyntaxWarning: 'return' in a 'finally' block``
      នៅពេល compile ដើម្បីព្រមានអំពីគំរូនេះជាមុន។

.. warning::

   ``finally`` ក៏ដំណើរការដែរនៅពេល ``try`` block មានរង្វិលជុំដែល
   ``break`` ចេញ ឬនៅពេល exception ត្រូវបានបញ្ចេញឡើងវិញ។ នេះហើយ
   ជាមូលហេតុដែលវាសមស្របសម្រាប់ការបិទធនធាន។

.. _exceptions-with-statement:

``with`` — Predefined Clean-up Actions
==========================================

object ខ្លះត្រូវការសម្អាតជានិច្ច ទោះបីជាប្រើជោគជ័យក៏ដោយ។ ``with``
ធ្វើវាដោយស្វ័យប្រវត្តិ៖

.. code-block:: pycon

   >>> from pathlib import Path
   >>> Path("data.txt").write_text("x", encoding="utf-8")
   1
   >>> with open("data.txt", encoding="utf-8") as f:
   ...     print(f.read())
   ...
   x
   >>> f.closed          # បិទរួចហើយ ទោះបីជាគ្មាន finally
   True

``with`` គឺជាការប្រើ **context manager**។ វាស្មើនឹង៖

.. code-block:: python

   f = open("data.txt", encoding="utf-8")
   try:
       print(f.read())
   finally:
       f.close()

.. note::

   object ដែលគាំទ្រ ``with`` ត្រូវមាន ``__enter__()`` និង ``__exit__()``។
   ឧទាហរណ៍ក្នុងបណ្ណាល័យស្តង់ដារ៖ file objects, ``threading.Lock``,
   ``decimal.localcontext()``, ``contextlib.suppress()``, database
   connections និងច្រើនទៀត។

   សូមមើលជំពូក :doc:`file_handling` សម្រាប់ការប្រើជាមួយឯកសារ។

**បង្កើត context manager ផ្ទាល់ខ្លួន** ដោយ ``contextlib.contextmanager``៖

.. code-block:: pycon

   >>> import contextlib, time
   >>> @contextlib.contextmanager
   ... def timed(label):
   ...     start = time.perf_counter()
   ...     try:
   ...         yield
   ...     finally:
   ...         print(f"{label}: {(time.perf_counter() - start)*1000:.1f} ms")
   ...
   >>> with timed("រង្វិលជុំ"):
   ...     total = sum(range(100_000))
   ...
   រង្វិលជុំ: ... ms

.. _exception-groups:

``ExceptionGroup`` និង ``except*``
======================================

.. versionadded:: 3.11

បើមានកំហុស **ច្រើនក្នុងពេលតែមួយ** (ឧ. ក្នុង concurrency ឬការផ្ទៀងផ្ទាត់
ច្រើនវាល (field)) អ្នកអាចបញ្ចេញពួកវាជាក្រុម៖

.. code-block:: pycon

   >>> def validate(fields):
   ...     errors = []
   ...     for name, value in fields.items():
   ...         try:
   ...             int(value)
   ...         except ValueError as exc:
   ...             errors.append(exc)
   ...     if errors:
   ...         raise ExceptionGroup("ការផ្ទៀងផ្ទាត់បរាជ័យ", errors)
   ...
   >>> validate({"a": "1", "b": "x", "c": "y"})
   Traceback (most recent call last):
     ...
     | ExceptionGroup: ការផ្ទៀងផ្ទាត់បរាជ័យ (2 sub-exceptions)
     +-+---------------- 1 ----------------
       | Traceback (most recent call last):
       | ...
       | ValueError: invalid literal for int() with base 10: 'x'
       +---------------- 2 ----------------
       | Traceback (most recent call last):
       | ...
       | ValueError: invalid literal for int() with base 10: 'y'
       +------------------------------------

**``except*``** ចាប់យកតែ exception ដែលត្រូវគ្នាពីក្រុម៖

.. code-block:: python

   data = {"a": "1", "b": "x"}

   try:
       validate(data)
   except* ValueError as eg:
       for err in eg.exceptions:
           print("តម្លៃខុស:", err)
   except* TypeError as eg:
       print("ប្រភេទខុស:", len(eg.exceptions))

.. important::

   ភាពខុសគ្នារវាង ``except`` និង ``except*``៖

   .. list-table::
      :header-rows: 1
      :widths: 20 80

      * -
        - ឥរិយាបថ
      * - ``except T``
        - ចាប់យក group **ទាំងមូល** បើ group ខ្លួនឯងត្រូវគ្នា
      * - ``except* T``
        - **បំបែក** group ហើយចាប់យកតែ exception ដែលជា ``T``។
          សល់នៅក្នុង group ត្រូវបានបញ្ចេញបន្ត

   ``except*`` clause ច្រើនអាចដំណើរការសម្រាប់ group តែមួយ។

.. note::

   ``ExceptionGroup`` បន្តពូជពី ``Exception`` ដូច្នេះ ``except Exception``
   ចាប់យកវាបាន។ ``BaseExceptionGroup`` បន្តពូជពី ``BaseException``
   សម្រាប់ករណីដែលមាន ``KeyboardInterrupt`` ជាដើម។

.. _exception-notes:

ការបន្ថែមចំណាំទៅ Exception
===========================

.. versionadded:: 3.11

``add_note()`` បន្ថែមបរិបទដោយមិនប្ដូរប្រភេទ ឬសារដើម៖

.. code-block:: pycon

   >>> err = ValueError("តម្លៃខុស")
   >>> err.add_note("កើតឡើងពេលផ្ទុកឯកសារ config.yaml")
   >>> err.add_note("បន្ទាត់ ៤២")
   >>> raise err
   Traceback (most recent call last):
     ...
   ValueError: តម្លៃខុស
   កើតឡើងពេលផ្ទុកឯកសារ config.yaml
   បន្ទាត់ ៤២

   >>> err.__notes__
   ['កើតឡើងពេលផ្ទុកឯកសារ config.yaml', 'បន្ទាត់ ៤២']

.. tip::

   ``add_note()`` មានប្រយោជន៍ជាងការបញ្ចេញ exception ថ្មី ព្រោះវារក្សា
   traceback និងប្រភេទដើមទាំងស្រុង ហើយចំណាំលេចឡើងនៅក្នុង traceback
   ដោយស្វ័យប្រវត្តិ។

.. _assert:

``assert``
==========

``assert`` បញ្ចេញ ``AssertionError`` បើលក្ខខណ្ឌមិនពិត៖

.. code-block:: pycon

   >>> def average(nums):
   ...     assert nums, "បញ្ជីមិនអាចទទេទេ"
   ...     return sum(nums) / len(nums)
   ...
   >>> average([1, 2, 3])
   2.0
   >>> average([])
   Traceback (most recent call last):
     ...
     ...
   AssertionError: បញ្ជីមិនអាចទទេទេ

.. warning::

   ``assert`` គឺសម្រាប់ **ការត្រួតពិនិត្យខាងក្នុង** (invariant) មិនមែន
   សម្រាប់ផ្ទៀងផ្ទាត់ទិន្នន័យពីអ្នកប្រើទេ។ មូលហេតុ៖

   .. code-block:: console

      $ python3 -O app.py     # -O ដក assert ទាំងអស់ចេញ!

   សម្រាប់ទិន្នន័យខាងក្រៅ ប្រើ ``raise ValueError(...)`` ជំនួសវិញ។

.. _exceptions-best-practices:

ការអនុវត្តល្អបំផុត
======================

#. **ចាប់យកជាក់លាក់** — ចាប់យកតែប្រភេទដែលអ្នកដឹងពីរបៀបដោះស្រាយ។
   កុំប្រើ ``except:`` ទទេ ឬ ``except Exception: pass``។
#. **រុំ ``try`` ឱ្យតូច** — តែបន្ទាត់ដែលអាចបរាជ័យ។
#. **ប្រើ ``else``** ដើម្បីញែកកូដដែលមិនអាចបរាជ័យចេញពី ``try``។
#. **ប្រើ ``with``** សម្រាប់ធនធាន ជំនួស ``try``/``finally`` ដោយដៃ។
#. **បញ្ចេញ exception ជាក់លាក់** — ``raise ValueError("…")`` ល្អជាង
   ``raise Exception("…")``។
#. **ប្រើ ``raise ... from exc``** ដើម្បីរក្សាប្រវត្តិកំហុស។
#. **កុំប្រើ exception សម្រាប់ control flow** ធម្មតា។ ប៉ុន្តែសម្រាប់
   Python ករណី "EAFP" (ដំណើរការ រួចដោះស្រាយកំហុស) ជារឿយៗល្អជាង
   "LBYL" (ពិនិត្យមុន)។
#. **កំណត់ exception ផ្ទាល់ខ្លួន** សម្រាប់បណ្ណាល័យរបស់អ្នក ដោយមាន
   class មេតែមួយ។
#. **កត់ត្រា** exception ដែលអ្នកចាប់យក — ប្រើ ``logging.exception()``។
#. **កុំលាក់កំហុស** — បើអ្នកមិនអាចដោះស្រាយ សូមបញ្ចេញឡើងវិញ។

.. _exceptions-summary:

សង្ខេប
======

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - គោលគំនិត
     - សង្ខេប
   * - SyntaxError
     - កំហុសវាក្យសម្ពន្ធ — កើតមុនដំណើរការ
   * - Exception
     - object កើតឡើងពេលដំណើរការ
   * - ``try``/``except``/``else``/``finally``
     - ចាប់យក ដោះស្រាយ និងសម្អាត
   * - ``raise``
     - បញ្ចេញ exception។ ``raise`` ទទេ = បញ្ចេញឡើងវិញ
   * - ``raise X from Y``
     - ភ្ជាប់ exception ដោយចេតនា (``__cause__``)
   * - ``from None``
     - លុបការភ្ជាប់
   * - ``finally``
     - ដំណើរការជានិច្ច — សម្រាប់សម្អាត
   * - ``with``
     - សម្អាតស្វ័យប្រវត្តិតាម context manager
   * - ``ExceptionGroup`` / ``except*``
     - កំហុសច្រើនក្នុងពេលតែមួយ (3.11+)
   * - ``add_note()``
     - បន្ថែមបរិបទដោយមិនប្ដូរ exception (3.11+)
   * - ``assert``
     - ត្រួតពិនិត្យខាងក្នុង — ត្រូវបានដកចេញដោយ ``-O``

.. rubric:: ប្រភពយោង

* `Errors and Exceptions <https://docs.python.org/3/tutorial/errors.html>`_
* `Built-in Exceptions <https://docs.python.org/3/library/exceptions.html>`_
* `Exception hierarchy <https://docs.python.org/3/library/exceptions.html#exception-hierarchy>`_
* `contextlib — Utilities for with-statement contexts <https://docs.python.org/3/library/contextlib.html>`_
* `logging — Logging facility <https://docs.python.org/3/library/logging.html>`_
* `PEP 654 — Exception Groups and except* <https://peps.python.org/pep-0654/>`_
