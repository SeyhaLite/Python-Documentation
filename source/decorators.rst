.. _decorators:

.. container:: src-note

   ប្រភពដើម៖ CPython ``Doc/glossary.rst`` (*decorator*),
   ``Doc/reference/compound_stmts.rst`` (*Function definitions*),
   ``Doc/library/functools.rst``, ``Doc/whatsnew/2.4.rst`` ·
   `ឯកសារផ្លូវការ <https://docs.python.org/3/glossary.html#term-decorator>`_

############
Decorators
############

**Decorator** គឺជាអនុគមន៍ដែលទទួលអនុគមន៍ (ឬ class) មួយ ហើយត្រឡប់
កំណែដែលបាន **ពង្រីក** ឬ **កែប្រែ** វិញ។ វាអនុញ្ញាតឱ្យអ្នកបន្ថែមអាកប្បកិរិយា
ដោយមិនកែកូដដើម។

.. _what-is-decorator:

តើ Decorator ជាអ្វី?
=====================

វាក្យសម្ពន្ធ ``@`` គ្រាន់តែជាការហៅអនុគមន៍ធម្មតាមួយប៉ុណ្ណោះ៖

.. code-block:: python
   :no-test:

   @my_decorator
   def func():
       ...

គឺស្មើនឹង៖

.. code-block:: python
   :no-test:

   def func():
       ...
   func = my_decorator(func)

.. code-block:: pycon

   >>> def shout(f):
   ...     def wrapper(*args, **kwargs):
   ...         return f(*args, **kwargs).upper()
   ...     return wrapper
   ...
   >>> @shout
   ... def greet(name):
   ...     return f"សួស្ដី {name}"
   ...
   >>> greet("សុខា")
   'សួស្ដី សុខា'
   >>> greet.__name__                  # ⚠ ឈ្មោះបានបាត់បង់
   'wrapper'

.. _first-decorator:

Decorator ដំបូងរបស់អ្នក
========================

.. code-block:: python

   import functools
   import time


   def timer(func):
       """វាស់ពេលដំណើរការរបស់អនុគមន៍។"""

       @functools.wraps(func)                       # ← សំខាន់ណាស់
       def wrapper(*args, **kwargs):
           start = time.perf_counter()
           result = func(*args, **kwargs)
           elapsed = time.perf_counter() - start
           print(f"{func.__name__} ចំណាយ {elapsed * 1000:.2f} ms")
           return result

       return wrapper


   @timer
   def sum_range(n):
       """បូកលេខពី 0 ដល់ n។"""
       return sum(range(n))

.. code-block:: pycon

   >>> total = sum_range(1_000_000)
   sum_range ចំណាយ ... ms
   >>> sum_range.__name__            # ✅ ឈ្មោះដើមត្រូវបានរក្សា
   'sum_range'
   >>> sum_range.__doc__
   'បូកលេខពី 0 ដល់ n។'

.. _functools-wraps:

``functools.wraps`` — កុំភ្លេច
==============================

បើគ្មាន ``@functools.wraps`` អនុគមន៍ដែលបាន decorate នឹង **បាត់បង់
metadata** ទាំងអស់របស់វា៖

.. list-table::
   :header-rows: 1
   :widths: 30 35 35

   * - Attribute
     - គ្មាន ``wraps``
     - មាន ``wraps``
   * - ``__name__``
     - ``'wrapper'``
     - ឈ្មោះដើម
   * - ``__doc__``
     - ``None``
     - docstring ដើម
   * - ``__module__``
     - របស់ decorator
     - របស់អនុគមន៍ដើម
   * - ``__qualname__``
     - ``'timer.<locals>.wrapper'``
     - qualname ដើម
   * - ``__annotations__``
     - របស់ wrapper
     - របស់អនុគមន៍ដើម
   * - ``__dict__``
     - ទទេ
     - បានបញ្ចូលគ្នា
   * - ``__wrapped__``
     - គ្មាន
     - ចង្អុលទៅអនុគមន៍ដើម

.. code-block:: pycon
   :no-test:

   >>> import functools, inspect
   >>> def plain(f):
   ...     def wrapper(*a, **k):
   ...         return f(*a, **k)
   ...     return wrapper
   ...
   >>> @plain
   ... def original(x: int) -> str:
   ...     """docstring ដើម"""
   ...     return str(x)
   ...
   >>> original.__name__
   'wrapper'
   >>> inspect.signature(original)
   <Signature (*a, **k)>

   >>> def polite(f):
   ...     @functools.wraps(f)
   ...     def wrapper(*a, **k):
   ...         return f(*a, **k)
   ...     return wrapper
   ...
   >>> @polite
   ... def original2(x: int) -> str:
   ...     """docstring ដើម"""
   ...     return str(x)
   ...
   >>> original2.__name__
   'original2'
   >>> inspect.signature(original2)          # ផ្ទៀងផ្ទាត់តាម REAL_SCRIPT_CHECKS
   <Signature (x: int) -> str>

.. important::

   ``@functools.wraps`` ធ្វើឱ្យ **debugging**, **documentation**,
   **introspection** និង **framework** ដំណើរការត្រឹមត្រូវ។ សរសេរវា
   **ជានិច្ច** នៅពេលអ្នកបង្កើត decorator។

   វាក៏កំណត់ ``__wrapped__`` ផងដែរ ដែលអនុញ្ញាតឱ្យអ្នកចូលទៅអនុគមន៍ដើម៖
   ``original2.__wrapped__``។

.. _decorators-with-arguments:

Decorator ដែលមាន Argument
===========================

Decorator ដែលទទួល argument ត្រូវការ **បីជាន់**៖

.. code-block:: python

   import functools


   def repeat(times):
       """ហៅអនុគមន៍ ``times`` ដង។"""

       def decorator(func):
           @functools.wraps(func)
           def wrapper(*args, **kwargs):
               result = None
               for _ in range(times):
                   result = func(*args, **kwargs)
               return result

           return wrapper

       return decorator


   @repeat(times=3)
   def say_hello(name):
       print(f"សួស្ដី {name}")
       return name

.. code-block:: pycon

   >>> say_hello("សុខា")
   សួស្ដី សុខា
   សួស្ដី សុខា
   សួស្ដី សុខា
   'សុខា'
   >>> say_hello.__name__
   'say_hello'

**លំដាប់នៃការដំណើរការ៖**

#. ``repeat(times=3)`` ត្រូវបានហៅភ្លាម → ត្រឡប់ ``decorator``
#. ``decorator(say_hello)`` ត្រូវបានហៅ → ត្រឡប់ ``wrapper``
#. ``say_hello`` ឥឡូវចង្អុលទៅ ``wrapper``

.. tip::

   ចងចាំថា ``@repeat(times=3)`` មាន **វង់ក្រចក** — វាហៅ ``repeat`` ជាមុន។
   ``@repeat`` ដោយគ្មានវង់ក្រចក នឹងព្យាយាមប្រើ ``times`` ជាអនុគមន៍។

   អ្នកអាចធ្វើឱ្យ decorator មួយដំណើរការទាំងពីររបៀប ដោយពិនិត្យ
   ប្រភេទ argument ដំបូង៖

   .. code-block:: python

      def log(func=None, *, level="INFO"):
          """ដំណើរការទាំង @log និង @log(level="DEBUG")។"""
          if func is None:
              return functools.partial(log, level=level)

          @functools.wraps(func)
          def wrapper(*args, **kwargs):
              print(f"[{level}] {func.__name__}")
              return func(*args, **kwargs)

          return wrapper

.. _stacking:

ការដាក់ Decorator ច្រើនជាន់
===========================

Decorator ត្រូវបានអនុវត្ត **ពីក្រោមឡើងលើ**៖

.. code-block:: python

   import functools


   def bold(func):
       @functools.wraps(func)
       def wrapper(*a, **k):
           return f"<b>{func(*a, **k)}</b>"
       return wrapper


   def italic(func):
       @functools.wraps(func)
       def wrapper(*a, **k):
           return f"<i>{func(*a, **k)}</i>"
       return wrapper


   @bold
   @italic
   def label(text):
       return text

.. code-block:: pycon

   >>> label("សួស្ដី")
   '<b><i>សួស្ដី</i></b>'

នេះស្មើនឹង ``label = bold(italic(label))``។ ដូច្នេះ ``@bold`` ដែលនៅ
**ខាងលើ** ដំណើរការ **ចុងក្រោយ**។

.. _decorator-syntax:

វាក្យសម្ពន្ធ Decorator
==========================

.. versionchanged:: 3.9
   PEP 614 ធ្វើឱ្យវាក្យសម្ពន្ធធូររលុង — decorator អាចជា **expression ណាក៏បាន**
   ដែលត្រឡប់ callable មិនមែនត្រឹមតែឈ្មោះ ឬការហៅមានចុចប៉ុណ្ណោះទេ។

.. code-block:: python
   :no-test:

   # មុន Python 3.9 — ត្រូវប្រើអថេរជំនួយ
   decorator = registry["debug"]
   @decorator
   def func(): ...

   # Python 3.9+ — អនុញ្ញាតផ្ទាល់
   @registry["debug"]
   def func(): ...

   @buttons[0].clicked.connect
   def on_click(): ...

.. _builtin-decorators:

Decorator ស្តង់ដារដែលអ្នកគួរស្គាល់
===================================

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Decorator
     - ការប្រើប្រាស់
   * - ``@functools.wraps(f)``
     - រក្សា metadata របស់អនុគមន៍ដែលបាន decorate
   * - ``@property``
     - បំលែង method ទៅជា attribute ដែលអានបាន
   * - ``@x.setter`` / ``@x.deleter``
     - កំណត់ setter/deleter សម្រាប់ property
   * - ``@classmethod``
     - method ដែលទទួល ``cls``
   * - ``@staticmethod``
     - method ដែលមិនទទួល ``self`` ឬ ``cls``
   * - ``@functools.lru_cache(maxsize=…)``
     - រក្សាទុកលទ្ធផល (cache) ដោយផ្អែកលើ argument
   * - ``@functools.cache``
     - cache គ្មានដែនកំណត់ (Python 3.9+)
   * - ``@functools.cached_property``
     - គណនាម្ដងគត់ រួចរក្សាទុកជា instance attribute
   * - ``@functools.singledispatch``
     - overloading តាមប្រភេទ argument ដំបូង
   * - ``@functools.total_ordering``
     - បង្កើតប្រមាណវិធីប្រៀបធៀបដែលនៅសល់ពី ``__eq__`` + មួយទៀត
   * - ``@dataclasses.dataclass``
     - បង្កើត ``__init__``/``__repr__``/``__eq__`` ស្វ័យប្រវត្តិ
   * - ``@abc.abstractmethod``
     - បង្ខំឱ្យ subclass អនុវត្ត
   * - ``@contextlib.contextmanager``
     - បង្កើត context manager ពី generator
   * - ``@typing.override``
     - បញ្ជាក់ថា method នេះ override method របស់ class មេ (3.12+)
   * - ``@functools.partial`` (មិនមែន decorator ប៉ុន្តែស្រដៀង)
     - កំណត់ argument ខ្លះជាមុន

.. _lru-cache:

``@lru_cache`` — Caching
------------------------

.. code-block:: pycon

   >>> import functools
   >>> @functools.lru_cache(maxsize=None)
   ... def fib(n):
   ...     if n < 2:
   ...         return n
   ...     return fib(n - 1) + fib(n - 2)
   ...
   >>> fib(30)
   832040
   >>> fib.cache_info()
   CacheInfo(hits=28, misses=31, maxsize=None, currsize=31)
   >>> fib.cache_clear()
   >>> fib.cache_info()
   CacheInfo(hits=0, misses=0, maxsize=None, currsize=0)

.. warning::

   ``@lru_cache`` តម្រូវឱ្យ argument ទាំងអស់ **hashable**។ Argument
   mutable (``list``, ``dict``, ``set``) នឹងបញ្ចេញ ``TypeError``៖

   .. code-block:: pycon

      >>> @functools.lru_cache
      ... def process(items):
      ...     return len(items)
      ...
      >>> process([1, 2, 3])
      Traceback (most recent call last):
        ...
      TypeError: unhashable type: 'list'

   ចំណាំថា cache ក៏រក្សា **reference** ទៅ argument និងលទ្ធផលផងដែរ
   ដូច្នេះវាអាចបណ្ដាលឱ្យអស់អង្គចងចាំបើប្រើដោយប្រុងប្រយ័ត្ន។
   ``@functools.cache`` គឺជាផ្លូវកាត់សម្រាប់ ``lru_cache(maxsize=None)``។

.. _class-decorators:

Class ជា Decorator
==================

Object ណាដែលមាន ``__call__`` អាចជា decorator បាន៖

.. code-block:: python

   import functools


   class CountCalls:
       """រាប់ចំនួនដងដែលអនុគមន៍ត្រូវបានហៅ។"""

       def __init__(self, func):
           functools.update_wrapper(self, func)
           self.func = func
           self.count = 0

       def __call__(self, *args, **kwargs):
           self.count += 1
           return self.func(*args, **kwargs)


   @CountCalls
   def ping():
       return "pong"

.. code-block:: pycon

   >>> ping(), ping()
   ('pong', 'pong')
   >>> ping.count
   2
   >>> ping.__name__
   'ping'

.. note::

   ប្រើ ``functools.update_wrapper(self, func)`` ជំនួស
   ``@functools.wraps`` ព្រោះ ``wraps`` គឺជា decorator សម្រាប់អនុគមន៍
   ខណៈ ``update_wrapper`` គឺជាអនុគមន៍ដែលនៅពីក្រោយវា។

.. _decorating-methods:

Decorator លើ Method
====================

Decorator ដំណើរការមុនពេល method ក្លាយជា bound method ដូច្នេះ ``self``
គ្រាន់តែជា argument ធម្មតាមួយ៖

.. code-block:: python

   import functools


   def requires_auth(func):
       @functools.wraps(func)
       def wrapper(self, *args, **kwargs):
           if not self.logged_in:
               raise PermissionError("ត្រូវតែចូលគណនីជាមុន")
           return func(self, *args, **kwargs)

       return wrapper


   class Account:
       def __init__(self, owner):
           self.owner = owner
           self.logged_in = False

       @requires_auth
       def withdraw(self, amount):
           return f"{self.owner} បានដក {amount}"

.. code-block:: pycon

   >>> acc = Account("សុខា")
   >>> acc.withdraw(100)
   Traceback (most recent call last):
     ...
   PermissionError: ត្រូវតែចូលគណនីជាមុន
   >>> acc.logged_in = True
   >>> acc.withdraw(100)
   'សុខា បានដក 100'

.. _class-decorator-target:

Decorator សម្រាប់ Class
===========================

Decorator ក៏អាចកែប្រែ class បានដែរ៖

.. code-block:: pycon

   >>> import functools
   >>> def add_repr(cls):
   ...     cls.__repr__ = lambda self: f"<{type(self).__name__}>"
   ...     return cls
   ...
   >>> @add_repr
   ... class Thing:
   ...     pass
   ...
   >>> Thing()
   <Thing>

.. note::

   ``@dataclasses.dataclass`` គឺជាឧទាហរណ៍ដ៏ល្បីបំផុតនៃ class decorator —
   វាបន្ថែម ``__init__``, ``__repr__``, ``__eq__`` និង method ផ្សេងទៀត
   ទៅក្នុង class។ សូមមើលជំពូក :doc:`classes_oop`។

.. _real-world:

ឧទាហរណ៍ជាក់ស្ដែង
=================

**១. Retry logic** — សាកល្បងម្ដងទៀតពេលបរាជ័យ៖

.. code-block:: python

   import functools
   import time


   def retry(attempts=3, delay=0.1, exceptions=(OSError,)):
       """សាកល្បងម្ដងទៀតរហូតដល់ជោគជ័យ ឬអស់ attempts។"""

       def decorator(func):
           @functools.wraps(func)
           def wrapper(*args, **kwargs):
               last = None
               for attempt in range(1, attempts + 1):
                   try:
                       return func(*args, **kwargs)
                   except exceptions as exc:
                       last = exc
                       if attempt < attempts:
                           time.sleep(delay)
               raise last

           return wrapper

       return decorator

**២. Validation** — ពិនិត្យ argument៖

.. code-block:: python

   import functools


   def positive(*param_names):
       """ធានាថា parameter ដែលបានបញ្ជាក់មានតម្លៃវិជ្ជមាន។"""

       def decorator(func):
           import inspect

           sig = inspect.signature(func)

           @functools.wraps(func)
           def wrapper(*args, **kwargs):
               bound = sig.bind(*args, **kwargs)
               bound.apply_defaults()
               for name in param_names:
                   if bound.arguments[name] <= 0:
                       raise ValueError(f"{name} ត្រូវតែវិជ្ជមាន")
               return func(*args, **kwargs)

           return wrapper

       return decorator

**៣. Deprecation warning**៖

.. code-block:: python

   import functools
   import warnings


   def deprecated(reason):
       def decorator(func):
           @functools.wraps(func)
           def wrapper(*args, **kwargs):
               warnings.warn(
                   f"{func.__name__} ហួសសម័យហើយ: {reason}",
                   DeprecationWarning,
                   stacklevel=2,
               )
               return func(*args, **kwargs)

           return wrapper

       return decorator

.. _decorators-best-practices:

ការអនុវត្តល្អបំផុត
======================

#. **ប្រើ ``@functools.wraps`` ជានិច្ច** — បើគ្មានវា metadata ទាំងអស់បាត់។
#. **កុំប្រើ decorator ច្រើនជាន់ពេក** — លើសពី ២–៣ ជាន់ កូដពិបាកយល់
   និងពិបាក debug។
#. **Decorator ត្រូវតែថ្លា** — វាមិនគួរប្ដូរអាកប្បកិរិយាដែលអ្នកប្រើ
   មិនរំពឹងទេ។ ឧ. កុំបំលែង argument ឬតម្លៃត្រឡប់ដោយស្ងាត់។
#. **ប្រើ decorator សម្រាប់ *cross-cutting concerns*** — logging,
   timing, caching, authorization, validation, retry។ កុំដាក់
   business logic ក្នុង decorator។
#. **គិតអំពីលំដាប់** — decorator ខាងលើដំណើរការចុងក្រោយ។
   ``@lru_cache`` គួរនៅ **ក្រោម** decorator ផ្សេង បើអ្នកចង់ cache
   លទ្ធផលចុងក្រោយ។
#. **សាកល្បងអនុគមន៍ដើម** — ``__wrapped__`` អនុញ្ញាតឱ្យអ្នកហៅអនុគមន៍
   ដែលមិនបាន decorate។
#. **បើអ្នកមិនត្រូវការអាកប្បកិរិយា "decorate" ទេ** គ្រាន់តែហៅអនុគមន៍
   ធម្មតា។ កុំប្រើ decorator គ្រាន់តែដើម្បីស្ទីល។

.. _decorators-summary:

សង្ខេប
======

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - គោលគំនិត
     - សង្ខេប
   * - ``@dec`` លើ ``def f``
     - ស្មើនឹង ``f = dec(f)``
   * - ``@dec(args)``
     - ស្មើនឹង ``f = dec(args)(f)`` — ត្រូវការបីជាន់
   * - ``functools.wraps``
     - រក្សា ``__name__``, ``__doc__``, ``__annotations__``, ``__wrapped__``
   * - ច្រើនជាន់
     - អនុវត្តពីក្រោមឡើងលើ
   * - Class decorator
     - object ដែលមាន ``__call__``
   * - Decorate class
     - decorator អាចកែប្រែ ឬជំនួស class
   * - PEP 614 (3.9+)
     - decorator អាចជា expression ណាក៏បាន

.. rubric:: ប្រភពយោង

* `Glossary: decorator <https://docs.python.org/3/glossary.html#term-decorator>`_
* `Function definitions <https://docs.python.org/3/reference/compound_stmts.html#function-definitions>`_
* `functools — Higher-order functions <https://docs.python.org/3/library/functools.html>`_
* `PEP 318 — Decorators for Functions and Methods <https://peps.python.org/pep-0318/>`_
* `PEP 3129 — Class Decorators <https://peps.python.org/pep-3129/>`_
* `PEP 614 — Relaxing Grammar Restrictions On Decorators <https://peps.python.org/pep-0614/>`_
