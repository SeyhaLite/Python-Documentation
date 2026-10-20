.. _classes-oop:

.. container:: src-note

   ប្រភពដើម៖ CPython ``Doc/tutorial/classes.rst``, ``Doc/reference/datamodel.rst``,
   ``Doc/library/dataclasses.rst``, ``Doc/library/abc.rst`` ·
   `ឯកសារផ្លូវការ <https://docs.python.org/3/tutorial/classes.html>`_

######################################################
Classes និង Object-Oriented Programming
######################################################

.. _oop-concepts:

គោលគំនិត OOP
=============

Object-Oriented Programming ផ្អែកលើគំនិតចំនួនបួន៖

.. list-table::
   :header-rows: 1
   :widths: 24 76

   * - គោលគំនិត
     - អត្ថន័យក្នុង Python
   * - **Encapsulation**
     - រុំទិន្នន័យ និងអាកប្បកិរិយាទុកក្នុង object មួយ។ Python ប្រើអនុសញ្ញា ``_name`` មិនមែនការហាមឃាត់ពិតទេ
   * - **Abstraction**
     - លាក់ភាពស្មុគស្មាញខាងក្នុង បង្ហាញតែ interface។ អនុវត្តតាមរយៈ method សាធារណៈ និង special methods
   * - **Inheritance**
     - class ថ្មីបន្តពូជពី class មានស្រាប់ ទទួលបាន attribute និង method របស់វា
   * - **Polymorphism**
     - object ប្រភេទផ្សេងគ្នាឆ្លើយតបទៅនឹង interface ដូចគ្នា។ Python សម្រេចបានតាម *duck typing*

.. _first-class:

Class ដំបូងរបស់អ្នក
====================

.. code-block:: python

   class Product:
       """តំណាងឱ្យទំនិញមួយក្នុងហាង។"""

       tax_rate = 0.10                     # class attribute

       def __init__(self, name, price):
           """បង្កើតផលិតផលថ្មី។"""
           self.name = name                # instance attributes
           self.price = price
           self.sold = 0

       def total_with_tax(self):
           """ត្រឡប់តម្លៃរួមពន្ធ។"""
           return round(self.price * (1 + self.tax_rate), 2)

       def sell(self, quantity=1):
           """កត់ត្រាការលក់។"""
           self.sold += quantity
           return self.sold

       def __repr__(self):
           return f"Product({self.name!r}, {self.price!r})"

.. code-block:: pycon

   >>> book = Product("សៀវភៅ Python", 12.50)
   >>> book
   Product('សៀវភៅ Python', 12.5)
   >>> book.name
   'សៀវភៅ Python'
   >>> book.total_with_tax()
   13.75
   >>> book.sell(3)
   3
   >>> Product.tax_rate
   0.1

.. _self:

តើ ``self`` ជាអ្វី?
--------------------

``self`` គឺជា **instance បច្ចុប្បន្ន**។ Python បញ្ជូនវាដោយស្វ័យប្រវត្តិ
នៅពេលអ្នកហៅ method លើ object មួយ៖

.. code-block:: pycon

   >>> book.total_with_tax()          # Python បញ្ជូន book ជា self
   13.75
   >>> Product.total_with_tax(book)   # ស្មើគ្នាទាំងស្រុង
   13.75
   >>> book.total_with_tax.__func__ is Product.total_with_tax
   True

.. important::

   * ``self`` គ្រាន់តែជា **អនុសញ្ញា** — អ្នកអាចដាក់ឈ្មោះផ្សេងបាន
     ប៉ុន្តែកុំធ្វើ។
   * parameter ដំបូងរបស់ **instance method ទាំងអស់** ត្រូវតែជា ``self``
     (ទោះបីជាអ្នកមិនប្រើវាក៏ដោយ)។
   * ``book.method()`` = ``Class.method(book)``។ នេះហៅថា **bound method**។

.. _init-vs-new:

``__init__`` មិនមែនជា constructor ទេ
------------------------------------

ជាបច្ចេកទេស ``__new__`` បង្កើត object ហើយ ``__init__`` **កំណត់តម្លៃដំបូង**
(initialize) វា។ ក្នុងការអនុវត្តជាក់ស្ដែង អ្នកប្រើ ``__init__`` ជានិច្ច។

.. code-block:: pycon

   >>> class Trace:
   ...     def __new__(cls, *args):
   ...         print("1. __new__ បង្កើត object")
   ...         return super().__new__(cls)
   ...     def __init__(self, value):
   ...         print("2. __init__ កំណត់តម្លៃដំបូង")
   ...         self.value = value
   ...
   >>> t = Trace(42)
   1. __new__ បង្កើត object
   2. __init__ កំណត់តម្លៃដំបូង

.. _class-vs-instance:

Class Attribute និង Instance Attribute
======================================

.. list-table::
   :header-rows: 1
   :widths: 26 74

   * -
     - Class attribute · Instance attribute
   * - កំណត់នៅ
     - ក្នុងខ្លួន class (កម្រិតខាងក្រៅ method) · ក្នុង ``__init__`` ជា ``self.x``
   * - ចែករំលែក
     - ដោយ **instance ទាំងអស់** · ដោយ instance **មួយៗ**
   * - ចូលដំណើរការ
     - ``Product.tax_rate`` ឬ ``book.tax_rate`` · ``book.name`` តែប៉ុណ្ណោះ
   * - ប្រើសម្រាប់
     - ថេរ ឬលំនាំដើមដែលចែករំលែក · ទិន្នន័យរបស់ object នីមួយៗ

.. code-block:: pycon

   >>> a = Product("A", 10)
   >>> b = Product("B", 20)
   >>> a.tax_rate, b.tax_rate          # ចែករំលែកតម្លៃដូចគ្នា
   (0.1, 0.1)
   >>> Product.tax_rate = 0.2          # ផ្លាស់ប្ដូរសម្រាប់ **ទាំងអស់**
   >>> a.tax_rate, b.tax_rate
   (0.2, 0.2)
   >>> a.tax_rate = 0.05               # ⚠ បង្កើត **instance** attribute ថ្មី
   >>> a.tax_rate, b.tax_rate          # b មិនផ្លាស់ប្ដូរទេ
   (0.05, 0.2)

.. note::

   ការ **អាន** ``a.tax_rate`` ស្វែងរកតាមលំដាប់៖ instance → class →
   class មេ។ ការ **សរសេរ** ``a.tax_rate = x`` តែងតែបង្កើត instance
   attribute (លើកលែងតែ class attribute នោះជា descriptor ដូចជា
   ``property``)។

.. _mutable-class-attr:

អន្ទាក់ — Class Attribute ជា Mutable
--------------------------------------

.. code-block:: pycon

   >>> class BadTeam:
   ...     members = []                    # ❌ ចែករំលែករវាង instance ទាំងអស់
   ...     def add(self, name):
   ...         self.members.append(name)
   ...
   >>> t1 = BadTeam()
   >>> t2 = BadTeam()
   >>> t1.add("សុខា")
   >>> t2.members                          # ❗ សុខា លេចឡើងក្នុង t2
   ['សុខា']

   >>> class GoodTeam:
   ...     def __init__(self):
   ...         self.members = []           # ✅ instance attribute
   ...     def add(self, name):
   ...         self.members.append(name)
   ...
   >>> g1, g2 = GoodTeam(), GoodTeam()
   >>> g1.add("សុខា")
   >>> g2.members
   []

.. warning::

   កុំប្រើ object **mutable** (``list``, ``dict``, ``set``) ជា class
   attribute លើកលែងតែអ្នក **ចង់** ឱ្យវាចែករំលែក។ នេះជាកំហុសដូចគ្នា
   នឹង *mutable default argument* (មើលជំពូក :doc:`functions_scope`)។

.. _methods:

ប្រភេទ Method ទាំងបី
====================

.. code-block:: python

   class Temperature:
       """សីតុណ្ហភាពជា Celsius។"""

       instances = 0

       def __init__(self, celsius):
           self.celsius = celsius
           Temperature.instances += 1

       # --- instance method: ទទួល self -------------------------------
       def to_fahrenheit(self):
           return self.celsius * 9 / 5 + 32

       # --- class method: ទទួល cls ---------------------------------
       @classmethod
       def from_fahrenheit(cls, f):
           return cls((f - 32) * 5 / 9)

       @classmethod
       def count(cls):
           return cls.instances

       # --- static method: មិនទទួលអ្វីសោះ -------------------------
       @staticmethod
       def is_freezing(celsius):
           return celsius <= 0

.. code-block:: pycon

   >>> t = Temperature(25)
   >>> t.to_fahrenheit()
   77.0
   >>> hot = Temperature.from_fahrenheit(212)    # alternative constructor
   >>> round(hot.celsius)
   100
   >>> Temperature.count()
   2
   >>> Temperature.is_freezing(-5)               # ហៅលើ class បាន
   True
   >>> t.is_freezing(30)                         # ហៅលើ instance ក៏បាន
   False

.. list-table::
   :header-rows: 1
   :widths: 22 30 48

   * - ប្រភេទ
     - Parameter ដំបូង
     - ប្រើពេលណា
   * - instance method
     - ``self``
     - ត្រូវការទិន្នន័យរបស់ object
   * - ``@classmethod``
     - ``cls``
     - alternative constructor · ប្រតិបត្តិការលើ class ទាំងមូល · គោរព inheritance
   * - ``@staticmethod``
     - គ្មាន
     - អនុគមន៍ជំនួយដែលស្ថិតក្នុង namespace របស់ class តែមិនត្រូវការ ``self``/``cls``

.. tip::

   បើ method មិនប្រើ ``self`` ទេ វាគួរតែជា ``@staticmethod`` ឬអនុគមន៍
   ធម្មតានៅកម្រិត module។ IDE និង linter នឹងព្រមានអ្នកអំពីរឿងនេះ។

.. _property:

``@property``
=============

``property`` អនុញ្ញាតឱ្យអ្នកប្រើ **វាក្យសម្ពន្ធ attribute** ប៉ុន្តែដំណើរការ
**method** នៅពីក្រោយ៖

.. code-block:: python

   class Account:
       """គណនីធនាគារដែលមានការពារមិនឱ្យដកលើសសមតុល្យ។"""

       def __init__(self, owner, balance=0):
           self.owner = owner
           self._balance = balance          # ផ្ទៃក្នុង

       @property
       def balance(self):
           """សមតុល្យ — អានបានតែប៉ុណ្ណោះ។"""
           return self._balance

       @balance.setter
       def balance(self, value):
           if value < 0:
               raise ValueError("សមតុល្យមិនអាចអវិជ្ជមានទេ")
           self._balance = value

       @property
       def is_overdrawn(self):
           """គណនាតម្លៃថ្មីរាល់ពេលហៅ។"""
           return self._balance < 0

.. code-block:: pycon

   >>> acc = Account("សុខា", 100)
   >>> acc.balance              # អាន — ហៅ getter
   100
   >>> acc.balance = 250        # សរសេរ — ហៅ setter
   >>> acc.balance
   250
   >>> acc.balance = -10
   Traceback (most recent call last):
     ...
   ValueError: សមតុល្យមិនអាចអវិជ្ជមានទេ
   >>> acc.is_overdrawn
   False

.. note::

   ``@property`` មានប្រយោជន៍ព្រោះអ្នកអាច **ចាប់ផ្ដើមពី attribute ធម្មតា**
   ហើយបំលែងវាទៅជា property នៅពេលក្រោយ **ដោយមិនបំបែកកូដអ្នកប្រើ**៖

   .. code-block:: python

      # កំណែ ១
      class Circle:
          def __init__(self, r):
              self.radius = r

      # កំណែ ២ — បន្ថែមការផ្ទៀងផ្ទាត់ ដោយមិនប្ដូរ API
      class Circle:
          def __init__(self, r):
              self.radius = r          # ហៅ setter

          @property
          def radius(self):
              return self._radius

          @radius.setter
          def radius(self, value):
              if value <= 0:
                  raise ValueError("កាំត្រូវតែវិជ្ជមាន")
              self._radius = value

.. _inheritance:

Inheritance
===========

.. code-block:: python

   class Animal:
       """Class មេ។"""

       def __init__(self, name):
           self.name = name

       def speak(self):
           raise NotImplementedError("subclass ត្រូវអនុវត្ត method នេះ")

       def introduce(self):
           return f"{self.name} និយាយថា៖ {self.speak()}"


   class Dog(Animal):
       """Class កូន — បន្តពូជពី Animal។"""

       def speak(self):
           return "Gav!"


   class Cat(Animal):
       def speak(self):
           return "Meow"


   class Puppy(Dog):
       """កូនចៅជាន់ទីពីរ។"""

       def __init__(self, name, weeks_old):
           super().__init__(name)         # ហៅ __init__ របស់ class មេ
           self.weeks_old = weeks_old

.. code-block:: pycon

   >>> rex = Dog("Rex")
   >>> rex.introduce()          # ប្រើ method ពី Animal
   'Rex និយាយថា៖ Gav!'
   >>> Cat("Mimi").introduce()  # ប្រើ speak របស់ Cat
   'Mimi និយាយថា៖ Meow'

   >>> p = Puppy("Bob", 8)
   >>> p.weeks_old, p.name      # name មកពី super().__init__()
   (8, 'Bob')

   >>> isinstance(p, Puppy), isinstance(p, Dog), isinstance(p, Animal)
   (True, True, True)
   >>> issubclass(Puppy, Dog)
   True
   >>> issubclass(Dog, Cat)
   False

.. _polymorphism:

Polymorphism និង Duck Typing
----------------------------

កូដដែលដំណើរការលើ object ណាក៏បានដែលមាន method ត្រឹមត្រូវ៖

.. code-block:: pycon

   >>> def announce(animals):
   ...     for a in animals:
   ...         print(a.introduce())
   ...
   >>> announce([Dog("Rex"), Cat("Mimi")])
   Rex និយាយថា៖ Gav!
   Mimi និយាយថា៖ Meow

.. note::

   Python ប្រើ **duck typing** — "បើវាដើរដូចទា ហើយស្រែកដូចទា
   វាគឺជាទា"។ អ្នកមិនចាំបាច់ប្រកាស interface ឬបន្តពូជពី class ជាក់លាក់
   ទេ — គ្រាន់តែមាន method ដែលត្រូវការគឺគ្រប់គ្រាន់។

   បើអ្នកចង់បានការត្រួតពិនិត្យជាក់ស្ដែង ប្រើ ``abc.ABC``
   (មើលផ្នែក :ref:`abstract-base`)។

.. _super:

``super()``
-----------

``super()`` ផ្ដល់ការចូលដំណើរការទៅ method របស់ class មេ។ វាសំខាន់ណាស់
ក្នុង multiple inheritance ព្រោះវាដើរតាម **MRO** មិនមែនត្រឹមតែ class មេ
ដំបូងទេ។

.. code-block:: pycon

   >>> class A:
   ...     def who(self):
   ...         return "A"
   >>> class B(A):
   ...     def who(self):
   ...         return "B" + super().who()
   >>> class C(A):
   ...     def who(self):
   ...         return "C" + super().who()
   >>> class D(B, C):
   ...     def who(self):
   ...         return "D" + super().who()
   ...
   >>> D().who()
   'DBCA'
   >>> [k.__name__ for k in D.__mro__]
   ['D', 'B', 'C', 'A', 'object']

.. note::

   លទ្ធផល ``'DBCA'`` បង្ហាញថា ``super()`` ក្នុង ``B`` ហៅ **``C``**
   មិនមែន ``A`` ទេ — ព្រោះ MRO របស់ ``D`` គឺ ``D → B → C → A → object``។
   នេះហៅថា **C3 linearization** ហើយវាធានាថា method នីមួយៗ
   ដំណើរការតែម្ដងគត់។

.. _private:

Private Attribute និង Name Mangling
===================================

Python **មិនមាន** private ពិតទេ។ វាប្រើអនុសញ្ញា៖

.. list-table::
   :header-rows: 1
   :widths: 20 80

   * - ឈ្មោះ
     - អត្ថន័យ
   * - ``name``
     - សាធារណៈ
   * - ``_name``
     - ផ្ទៃក្នុង — អនុសញ្ញាប៉ុណ្ណោះ។ មិនត្រូវបាននាំចេញដោយ ``from m import *``
   * - ``__name``
     - **name mangling** — Python ប្ដូរវាទៅ ``_ClassName__name`` ដើម្បីចៀសវាងជម្លោះក្នុង inheritance
   * - ``__name__``
     - *dunder* — ឈ្មោះពិសេសដែល Python កំណត់។ **កុំបង្កើតថ្មីដោយខ្លួនឯង**

.. code-block:: pycon

   >>> class Vault:
   ...     def __init__(self):
   ...         self.public = 1
   ...         self._internal = 2
   ...         self.__secret = 3
   ...
   >>> v = Vault()
   >>> v.public, v._internal          # ទាំងពីរចូលដំណើរការបាន
   (1, 2)
   >>> v.__secret
   Traceback (most recent call last):
     ...
   AttributeError: 'Vault' object has no attribute '__secret'
   >>> v._Vault__secret               # ឈ្មោះពិតបន្ទាប់ពី mangling
   3

.. important::

   ``__name`` មិនមែនជា **សុវត្ថិភាព** ទេ — វាគ្រាន់តែជាការការពារ
   **ជម្លោះឈ្មោះ** ក្នុង inheritance។ ប្រើ ``_name`` សម្រាប់ផ្ទៃក្នុង
   ធម្មតា ហើយប្រើ ``__name`` តែនៅពេលអ្នកដឹងច្បាស់ថាត្រូវការ mangling។

.. _dunder-methods:

Special Methods (Dunder)
========================

Special methods អនុញ្ញាតឱ្យ object របស់អ្នកដំណើរការជាមួយវាក្យសម្ពន្ធ
របស់ Python (``+``, ``len()``, ``for``, ``with``, ``in``, ``[]``, ``print``)។

.. list-table:: ក្រុមសំខាន់ៗ
   :header-rows: 1
   :widths: 26 30 44

   * - Method
     - ត្រូវបានហៅដោយ
     - ឧទាហរណ៍
   * - ``__init__(self, ...)``
     - ការបង្កើត object
     - ``Point(1, 2)``
   * - ``__repr__(self)``
     - ``repr()``, REPL echo
     - គួរតែជាកូដដែលអាចបង្កើត object ឡើងវិញបាន
   * - ``__str__(self)``
     - ``str()``, ``print()``, f-string
     - សម្រាប់អ្នកអាន
   * - ``__eq__(self, other)``
     - ``==``
     - ត្រឡប់ ``NotImplemented`` បើមិនអាចប្រៀបធៀប
   * - ``__lt__``, ``__le__``, ``__gt__``, ``__ge__``
     - ``<``, ``<=``, ``>``, ``>=``
     - ឬប្រើ ``functools.total_ordering``
   * - ``__hash__(self)``
     - ``hash()``, ``set``, ``dict`` key
     - object ដែល ``__eq__`` ត្រូវមាន ``__hash__`` ដែលស្របគ្នា
   * - ``__len__(self)``
     - ``len()``
     - ត្រូវត្រឡប់ ``int`` ≥ 0
   * - ``__getitem__(self, key)``
     - ``obj[key]``, slicing
     - ផ្ដល់ iteration ដោយស្វ័យប្រវត្តិបើប្រើ index គត់
   * - ``__setitem__(self, key, value)``
     - ``obj[key] = value``
     - —
   * - ``__contains__(self, item)``
     - ``x in obj``
     - —
   * - ``__iter__(self)`` / ``__next__(self)``
     - ``for x in obj``
     - មើលជំពូក *Iterators និង Generators*
   * - ``__call__(self, ...)``
     - ``obj(...)``
     - ធ្វើឱ្យ object ហៅបានដូចអនុគមន៍
   * - ``__enter__(self)`` / ``__exit__(self, ...)``
     - ``with obj:``
     - context manager
   * - ``__add__(self, other)`` ជាដើម
     - ``+``, ``-``, ``*``, ``/``
     - operator overloading
   * - ``__bool__(self)``
     - ``if obj:``
     - បើគ្មាន Python ប្រើ ``__len__``

.. code-block:: python

   class Vector:
       """វ៉ិចទ័រ ២ មាត្រដែលគាំទ្រប្រមាណវិធីគណនា។"""

       __slots__ = ("x", "y")

       def __init__(self, x, y):
           self.x = x
           self.y = y

       def __repr__(self):
           return f"Vector({self.x}, {self.y})"

       def __eq__(self, other):
           if not isinstance(other, Vector):
               return NotImplemented
           return (self.x, self.y) == (other.x, other.y)

       def __hash__(self):
           return hash((self.x, self.y))

       def __add__(self, other):
           return Vector(self.x + other.x, self.y + other.y)

       def __mul__(self, scalar):
           return Vector(self.x * scalar, self.y * scalar)

       def __abs__(self):
           return (self.x ** 2 + self.y ** 2) ** 0.5

       def __len__(self):
           return 2

       def __getitem__(self, index):
           return (self.x, self.y)[index]

       def __bool__(self):
           return bool(self.x or self.y)

.. code-block:: pycon

   >>> a, b = Vector(1, 2), Vector(3, 4)
   >>> a + b
   Vector(4, 6)
   >>> a * 3
   Vector(3, 6)
   >>> abs(b)
   5.0
   >>> a == Vector(1, 2)
   True
   >>> a == "not a vector"
   False
   >>> len(a)
   2
   >>> a[1]
   2
   >>> list(a)                      # __getitem__ ផ្ដល់ iteration
   [1, 2]
   >>> bool(Vector(0, 0)), bool(a)
   (False, True)
   >>> len({a, Vector(1, 2)})       # __hash__ + __eq__ ស្របគ្នា
   1

.. note::

   ``__repr__`` vs ``__str__``៖

   * ``__repr__`` សម្រាប់ **អ្នកអភិវឌ្ឍន៍** — គួរតែជា
     ``Vector(1, 2)`` (កូដដែលអាច ``eval`` ឡើងវិញបាន)។
   * ``__str__`` សម្រាប់ **អ្នកប្រើ**។ បើអ្នកកំណត់តែ ``__repr__``
     Python ប្រើវាសម្រាប់ ``str()`` ដែរ។

.. _slots:

``__slots__``
=============

``__slots__`` កំណត់ attribute ដែលអនុញ្ញាត ហើយជៀសវាង ``__dict__``
ក្នុង instance នីមួយៗ — សន្សំអង្គចងចាំ និងលឿនជាង៖

.. code-block:: pycon

   >>> class Fixed:
   ...     __slots__ = ("a", "b")
   ...     def __init__(self):
   ...         self.a = 1
   ...         self.b = 2
   ...
   >>> f = Fixed()
   >>> f.a
   1
   >>> f.c = 3                      # ❌ មិនអនុញ្ញាត
   Traceback (most recent call last):
     ...
   AttributeError: 'Fixed' object has no attribute 'c' and no __dict__ for setting new attributes
   >>> hasattr(f, "__dict__")
   False

.. warning::

   ដែនកំណត់នៃ ``__slots__``៖

   * មិនអាចបន្ថែម attribute ថ្មីក្រោយពេលបង្កើត។
   * មិនគាំទ្រ ``weakref`` លើកលែងតែដាក់ ``"__weakref__"`` ក្នុង ``__slots__``។
   * subclass ដែល **មិន** កំណត់ ``__slots__`` នឹងមាន ``__dict__`` វិញ
     ដូច្នេះអត្ថប្រយោជន៍ត្រូវបានបាត់បង់។

   ប្រើ ``__slots__`` តែនៅពេលអ្នកបង្កើត **instance រាប់លាន** ឬចង់
   ការពារកំហុសឈ្មោះ attribute។ សម្រាប់ class ធម្មតា កុំប្រើ។

.. _dataclasses:

``dataclasses``
===============

.. versionadded:: 3.7

``@dataclass`` បង្កើត ``__init__``, ``__repr__``, ``__eq__`` និង method
ផ្សេងទៀតដោយស្វ័យប្រវត្តិ៖

.. code-block:: python

   from dataclasses import dataclass, field


   @dataclass
   class Order:
       """ការបញ្ជាទិញ។"""

       order_id: int
       customer: str
       items: list[str] = field(default_factory=list)
       paid: bool = False

       @property
       def total(self):
           return len(self.items) * 10

.. code-block:: pycon

   >>> o = Order(1, "សុខា", ["សៀវភៅ", "ប៊ិក"])
   >>> o
   Order(order_id=1, customer='សុខា', items=['សៀវភៅ', 'ប៊ិក'], paid=False)
   >>> o == Order(1, "សុខា", ["សៀវភៅ", "ប៊ិក"])
   True
   >>> o.total
   20

.. list-table:: Parameter សំខាន់ៗនៃ ``@dataclass``
   :header-rows: 1
   :widths: 26 74

   * - Parameter
     - អត្ថន័យ
   * - ``frozen=True``
     - immutable — ការផ្ដល់តម្លៃបញ្ចេញ ``FrozenInstanceError``។ បង្កើត ``__hash__`` ដោយស្វ័យប្រវត្តិ
   * - ``order=True``
     - បង្កើត ``__lt__``, ``__le__``, ``__gt__``, ``__ge__``
   * - ``slots=True``
     - បង្កើត ``__slots__`` (Python 3.10+)
   * - ``kw_only=True``
     - តម្រូវឱ្យបញ្ជូន argument ជា keyword (Python 3.10+)
   * - ``eq=False``
     - មិនបង្កើត ``__eq__`` (រក្សា ``__hash__`` ដើម)
   * - ``field(default_factory=…)``
     - **ចាំបាច់** សម្រាប់តម្លៃលំនាំដើម mutable

.. warning::

   កុំសរសេរ ``items: list = []`` ក្នុង dataclass — Python នឹងបញ្ចេញ
   ``ValueError``។ ប្រើ ``field(default_factory=list)``។

   .. code-block:: pycon

      >>> from dataclasses import dataclass
      >>> @dataclass
      ... class Broken:
      ...     items: list = []
      ...
      Traceback (most recent call last):
        ...
      ValueError: mutable default <class 'list'> for field items is not allowed...

.. code-block:: pycon

   >>> from dataclasses import dataclass
   >>> @dataclass(frozen=True, slots=True, order=True)
   ... class Point:
   ...     x: int
   ...     y: int
   ...
   >>> p = Point(1, 2)
   >>> p.x = 9
   Traceback (most recent call last):
     ...
   dataclasses.FrozenInstanceError: cannot assign to field 'x'
   >>> sorted([Point(2, 1), Point(1, 5), Point(1, 2)])
   [Point(x=1, y=2), Point(x=1, y=5), Point(x=2, y=1)]
   >>> {p, Point(1, 2)}              # frozen → hashable
   {Point(x=1, y=2)}

.. _abstract-base:

Abstract Base Class (``abc``)
=============================

បើអ្នកចង់ **បង្ខំ** ឱ្យ subclass អនុវត្ត method ជាក់លាក់ ប្រើ ``abc``៖

.. code-block:: python

   from abc import ABC, abstractmethod


   class Shape(ABC):
       """រូបរាង — មិនអាចបង្កើតដោយផ្ទាល់បានទេ។"""

       @abstractmethod
       def area(self) -> float:
           """ត្រឡប់ផ្ទៃក្រឡា។"""

       @abstractmethod
       def perimeter(self) -> float:
           """ត្រឡប់បរិមាត្រ។"""

       def describe(self) -> str:
           return f"{type(self).__name__}: area={self.area():.2f}"


   class Square(Shape):
       def __init__(self, side):
           self.side = side

       def area(self):
           return self.side ** 2

       def perimeter(self):
           return self.side * 4

.. code-block:: pycon

   >>> Shape()
   Traceback (most recent call last):
     ...
   TypeError: Can't instantiate abstract class Shape without an implementation for abstract methods 'area', 'perimeter'

   >>> Square(3).describe()
   'Square: area=9.00'
   >>> isinstance(Square(3), Shape)
   True

.. note::

   ``NotImplementedError`` (ដូចក្នុងឧទាហរណ៍ ``Animal`` ខាងលើ) ផ្ដល់
   កំហុសតែនៅពេល **ហៅ** method ប៉ុណ្ណោះ។ ``@abstractmethod`` ផ្ដល់កំហុស
   នៅពេល **បង្កើត** object — លឿនជាង និងច្បាស់ជាង។

.. _composition:

Composition ធៀបនឹង Inheritance
==============================

.. tip::

   **ចូលចិត្ត composition ជាង inheritance** ("favor composition over
   inheritance")។

   * **Inheritance** = "is-a" — ``Dog`` គឺជា ``Animal``
   * **Composition** = "has-a" — ``Car`` មាន ``Engine``

   Inheritance ជ្រៅពេកបង្កើត *tight coupling* ដែលពិបាកផ្លាស់ប្ដូរ។
   Composition ធ្វើឱ្យផ្នែកនីមួយៗអាចសាកល្បង និងជំនួសបានងាយ។

.. code-block:: python
   :no-test:

   # ❌ inheritance ជ្រៅពេក
   class FlyingSwimmingElectricCar(Car, Boat, Drone):
       pass

   # ✅ composition
   class Car:
       def __init__(self, engine: Engine, gps: GPS | None = None):
           self.engine = engine          # has-a
           self.gps = gps

       def drive(self):
           return self.engine.run()

.. _type-params:

Generic Class (PEP 695)
=======================

.. versionadded:: 3.12

.. code-block:: python

   class Stack[T]:
       """Stack ដែលមាន type parameter។"""

       def __init__(self) -> None:
           self._items: list[T] = []

       def push(self, item: T) -> None:
           self._items.append(item)

       def pop(self) -> T:
           return self._items.pop()

       def __len__(self) -> int:
           return len(self._items)


   type Number = int | float          # type alias (PEP 695)

.. code-block:: pycon

   >>> s: Stack[str] = Stack()
   >>> s.push("ក"); s.push("ខ")
   >>> len(s)
   2
   >>> s.pop()
   'ខ'

.. note::

   វាក្យសម្ពន្ធ ``class Stack[T]:`` ខ្លីជាងទម្រង់ចាស់ដែលត្រូវ
   ``from typing import Generic, TypeVar``។ ទម្រង់ចាស់នៅតែដំណើរការ។
   សូមមើលជំពូក *Type Hints* (មិនទាន់បានសរសេរ)។

.. _classes-best-practices:

ការអនុវត្តល្អបំផុត
======================

#. **ចាប់ផ្ដើមសាមញ្ញ** — ប្រើ function និង module ជាមុនសិន។
   បង្កើត class តែនៅពេលអ្នកត្រូវការ **ទិន្នន័យ + អាកប្បកិរិយា** ជាប់គ្នា។
#. **ប្រើ ``@dataclass``** សម្រាប់ class ដែលផ្ទុកទិន្នន័យភាគច្រើន។
#. **កំណត់ ``__repr__``** សម្រាប់ class ទាំងអស់ — វាធ្វើឱ្យ debug ងាយណាស់។
#. **ប្រើ ``self.x`` ជានិច្ច** ក្នុង method — កុំសរសេរ ``x`` ដោយផ្ទាល់
   (វានឹងបង្កើតអថេរ local មិនមែន attribute ទេ)។
#. **កុំប្រើ mutable class attribute** ជាលំនាំដើម។
#. **រាក់ inheritance** — ១–២ ជាន់គឺគ្រប់គ្រាន់ភាគច្រើន។
#. **ហៅ ``super().__init__()``** នៅពេល override ``__init__``។
#. **ប្រើ ``@property``** ជំនួស getter/setter ដែលសរសេរដោយដៃ។
#. **អនុវត្ត ``__eq__`` និង ``__hash__`` ជាគូ** — បើ object អាចស្មើគ្នា
   វាត្រូវតែ hash ដូចគ្នាដែរ មិនដូច្នោះទេ ``set``/``dict`` នឹងខូច។
#. **ប្រើ ``NotImplemented``** (មិនមែន ``NotImplementedError``) ក្នុង
   ``__eq__`` បើប្រភេទមិនត្រូវគ្នា — នេះអនុញ្ញាតឱ្យ Python សាកល្បង
   reflected operation។

.. _classes-summary:

សង្ខេប
======

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - គោលគំនិត
     - សង្ខេប
   * - ``class X:``
     - កំណត់ class។ ``X(...)`` បង្កើត instance
   * - ``__init__`` / ``self``
     - កំណត់តម្លៃដំបូង · instance បច្ចុប្បន្ន (បញ្ជូនស្វ័យប្រវត្តិ)
   * - Class vs instance attribute
     - ចែករំលែក · របស់ object នីមួយៗ
   * - ``@classmethod`` / ``@staticmethod``
     - ទទួល ``cls`` · មិនទទួលអ្វី
   * - ``@property``
     - attribute syntax ដែលដំណើរការ method
   * - Inheritance
     - ``class Sub(Base):`` · ``super()`` ហៅ method របស់ class មេ
   * - MRO
     - លំដាប់ស្វែងរក attribute · ``Class.__mro__``
   * - ``_x`` / ``__x``
     - ផ្ទៃក្នុង (អនុសញ្ញា) · name mangling
   * - Dunder methods
     - ភ្ជាប់ object ទៅនឹងវាក្យសម្ពន្ធ Python
   * - ``__slots__``
     - សន្សំអង្គចងចាំ · កំណត់ attribute ដែលអនុញ្ញាត
   * - ``@dataclass``
     - បង្កើត ``__init__``/``__repr__``/``__eq__`` ស្វ័យប្រវត្តិ
   * - ``abc.ABC``
     - បង្ខំឱ្យ subclass អនុវត្ត abstract method

.. rubric:: ប្រភពយោង

* `Classes <https://docs.python.org/3/tutorial/classes.html>`_
* `Data model <https://docs.python.org/3/reference/datamodel.html>`_
* `Special method names <https://docs.python.org/3/reference/datamodel.html#special-method-names>`_
* `dataclasses — Data Classes <https://docs.python.org/3/library/dataclasses.html>`_
* `abc — Abstract Base Classes <https://docs.python.org/3/library/abc.html>`_
* `functools.total_ordering <https://docs.python.org/3/library/functools.html#functools.total_ordering>`_
* `PEP 8 — Class naming <https://peps.python.org/pep-0008/#class-names>`_
* `PEP 695 — Type Parameter Syntax <https://peps.python.org/pep-0695/>`_
