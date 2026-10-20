.. _type-hints:

.. container:: src-note

   ប្រភពដើម៖ CPython ``Doc/library/typing.rst``,
   ``Doc/tutorial/controlflow.rst`` (*Function Annotations*),
   ``Doc/reference/compound_stmts.rst`` (*Annotated parameter lists*),
   ``Doc/howto/annotations.rst`` ·
   `ឯកសារផ្លូវការ <https://docs.python.org/3/library/typing.html>`_

############
Type Hints
############

**Type hint** (ឬ *type annotation*) គឺជាព័ត៌មានប្រភេទដែលអ្នកភ្ជាប់ទៅ
អថេរ parameter និងតម្លៃត្រឡប់។ Python **មិនពិនិត្យ** វានៅពេលដំណើរការទេ —
ឧបករណ៍ខាងក្រៅដូចជា ``mypy``, ``pyright`` និង IDE ប្រើវា។

.. _why:

ហេតុអ្វីប្រើ Type Hints?
========================

.. list-table::
   :header-rows: 1
   :widths: 26 74

   * - អត្ថប្រយោជន៍
     - ការពន្យល់
   * - រកកំហុសមុនដំណើរការ
     - type checker រកឃើញ ``TypeError`` ជាច្រើនដោយមិនចាំបាច់ដំណើរការកូដ
   * - IDE ល្អជាង
     - autocomplete, go-to-definition, refactor ត្រឹមត្រូវជាង
   * - ឯកសារខ្លួនឯង
     - signature ប្រាប់អ្នកអានថាត្រូវបញ្ជូនអ្វី ដោយមិនចាំបាច់អាន docstring
   * - Refactor ដោយទំនុកចិត្ត
     - ប្ដូរ signature រួច checker ប្រាប់កន្លែងទាំងអស់ដែលត្រូវកែ
   * - មិនប៉ះពាល់ល្បឿន
     - Python មិនពិនិត្យ annotation នៅពេលដំណើរការទេ

.. warning::

   **Python មិនរារាំងទេ** បើអ្នកបញ្ជូនប្រភេទខុស៖

   .. code-block:: pycon

      >>> def double(n: int) -> int:
      ...     return n * 2
      ...
      >>> double(5)
      10
      >>> double("ab")            # មិនមានកំហុសទេ!
      'abab'

   Type hint គឺជា **ឯកសារដែលម៉ាស៊ីនអានបាន** មិនមែនជាការត្រួតពិនិត្យ
   ពេលដំណើរការទេ។ ដើម្បីទទួលបានអត្ថប្រយោជន៍ អ្នកត្រូវដំណើរការ
   type checker (``mypy``, ``pyright``) ជាផ្នែកនៃ CI របស់អ្នក។

.. _basic-syntax:

វាក្យសម្ពន្ធមូលដ្ឋាន
========================

.. code-block:: python

   # Parameter និងតម្លៃត្រឡប់
   def greet(name: str, times: int = 1) -> str:
       return f"សួស្ដី {name}! " * times


   # អថេរ
   count: int = 0
   names: list[str] = []
   config: dict[str, int] = {"timeout": 30}

   # ប្រកាសដោយមិនផ្ដល់តម្លៃ
   total: float

   # ថេរកម្រិត module
   MAX_RETRIES: int = 3

.. code-block:: pycon
   :no-test:

   >>> greet.__annotations__
   {'name': <class 'str'>, 'times': <class 'int'>, 'return': <class 'str'>}
   >>> count.__class__.__name__
   'int'

.. _builtin-generics:

ប្រភេទ Built-in ជា Generic
==========================

.. versionchanged:: 3.9
   អ្នកអាចប្រើប្រភេទ built-in ដោយផ្ទាល់ជា generic — មិនចាំបាច់
   ``typing.List``, ``typing.Dict`` ទៀតទេ។

.. list-table::
   :header-rows: 1
   :widths: 34 34 32

   * - ទម្រង់ថ្មី (3.9+)
     - ទម្រង់ចាស់
     - អត្ថន័យ
   * - ``list[int]``
     - ``typing.List[int]``
     - list នៃ ``int``
   * - ``dict[str, int]``
     - ``typing.Dict[str, int]``
     - dict ពី ``str`` ទៅ ``int``
   * - ``set[str]``
     - ``typing.Set[str]``
     - set នៃ ``str``
   * - ``tuple[int, str]``
     - ``typing.Tuple[int, str]``
     - tuple មានធាតុ ២ ជាក់លាក់
   * - ``tuple[int, ...]``
     - ``typing.Tuple[int, ...]``
     - tuple ប្រវែងណាក៏បាន នៃ ``int``
   * - ``frozenset[int]``
     - ``typing.FrozenSet[int]``
     - frozenset
   * - ``type[MyClass]``
     - ``typing.Type[MyClass]``
     - class ខ្លួនឯង (មិនមែន instance)

.. code-block:: python

   def top_scores(scores: dict[str, int], n: int = 3) -> list[tuple[str, int]]:
       """ត្រឡប់ពិន្ទុខ្ពស់បំផុត n ។"""
       return sorted(scores.items(), key=lambda kv: kv[1], reverse=True)[:n]

.. code-block:: pycon

   >>> top_scores({"math": 87, "physics": 92, "chem": 78, "bio": 95}, 2)
   [('bio', 95), ('physics', 92)]

.. note::

   ទម្រង់ចាស់ ``typing.List`` ជាដើម **នៅតែដំណើរការ** ប៉ុន្តែត្រូវបាន
   ចាត់ទុកជា *deprecated* ក្នុងឯកសារ។ សម្រាប់កូដថ្មី សូមប្រើទម្រង់
   built-in។

.. _union-optional:

Union និង Optional
==================

.. versionchanged:: 3.10
   សញ្ញា ``|`` ជំនួស ``typing.Union``។

.. code-block:: python

   from typing import Optional, Union


   # ទម្រង់ថ្មី (3.10+) — ណែនាំ
   def parse(value: int | str) -> str:
       return str(value).strip()


   def find_user(uid: int) -> User | None:      # អាចរកមិនឃើញ
       ...


   # ទម្រង់ចាស់
   def parse_old(value: Union[int, str]) -> str: ...
   def find_user_old(uid: int) -> Optional[User]: ...

.. list-table::
   :header-rows: 1
   :widths: 32 68

   * - វាក្យសម្ពន្ធ
     - អត្ថន័យ
   * - ``int \| str``
     - ``int`` ឬ ``str``
   * - ``X \| None``
     - ``X`` ឬ ``None`` — ស្មើនឹង ``Optional[X]``
   * - ``Optional[X]``
     - ដូច ``X \| None`` **មិនមែន** "មិនចាំបាច់" ទេ
   * - ``Any``
     - ប្រភេទណាក៏បាន — បិទការត្រួតពិនិត្យ

.. warning::

   ``Optional[X]`` **មិនមានន័យថា parameter នេះមិនចាំបាច់** ទេ។
   វាមានន័យថាតម្លៃអាចជា ``None``។ ដើម្បីធ្វើឱ្យ parameter មិនចាំបាច់
   អ្នកត្រូវផ្ដល់ **តម្លៃលំនាំដើម**៖

   .. code-block:: python

      # ត្រូវបញ្ជូន name ជានិច្ច (ប៉ុន្តែអាចជា None)
      def f(name: str | None) -> None: ...

      # មិនចាំបាច់បញ្ជូន name
      def g(name: str | None = None) -> None: ...

.. _none-vs-noreturn:

``None``, ``NoReturn`` និង ``Never``
====================================

.. list-table::
   :header-rows: 1
   :widths: 24 76

   * - Annotation
     - ប្រើសម្រាប់
   * - ``-> None``
     - អនុគមន៍ដែលមិនត្រឡប់អ្វីមានន័យ (ត្រឡប់ ``None``)
   * - ``-> NoReturn``
     - អនុគមន៍ដែល **មិនដែលត្រឡប់** ដោយធម្មតា — បញ្ចេញ exception ឬ ``sys.exit()``
   * - ``-> Never``
     - ដូច ``NoReturn`` (3.11+) — ឈ្មោះច្បាស់ជាង។ ``NoReturn`` គឺជា alias
   * - ``None`` ជាប្រភេទ
     - ប្រភេទនៃ object ``None`` ផ្ទាល់ (``NoneType``)

.. code-block:: python

   import sys
   from typing import Never, NoReturn


   def fail(message: str) -> Never:
       """មិនដែលត្រឡប់ទេ។"""
       raise SystemExit(message)


   def quit_app(code: int = 0) -> NoReturn:
       sys.exit(code)


   def log(message: str) -> None:
       print(message)

.. note::

   ``Never`` មានប្រយោជន៍ពិសេសក្នុងការពិនិត្យ **exhaustiveness**។
   សូមមើលផ្នែក :ref:`typeguard-typeis`។

.. _callable:

``Callable``
============

.. code-block:: python

   from collections.abc import Callable


   def apply(func: Callable[[int, int], int], a: int, b: int) -> int:
       return func(a, b)


   def add(x: int, y: int) -> int:
       return x + y


   result = apply(add, 3, 4)          # 7

.. list-table::
   :header-rows: 1
   :widths: 40 60

   * - វាក្យសម្ពន្ធ
     - អត្ថន័យ
   * - ``Callable[[int, str], bool]``
     - អនុគមន៍យក ``(int, str)`` ត្រឡប់ ``bool``
   * - ``Callable[[], None]``
     - អនុគមន៍គ្មាន argument មិនត្រឡប់អ្វី
   * - ``Callable[..., int]``
     - argument ណាក៏បាន ត្រឡប់ ``int``
   * - ``Callable[[int, ...], None]``
     - ``int`` ច្រើនតាមចិត្ត (variadic)

.. note::

   នៅក្នុង Python 3.9+ សូមនាំចូល ``Callable`` ពី ``collections.abc``
   ជាជាង ``typing``។ ``typing.Callable`` នៅតែដំណើរការ ប៉ុន្តែទម្រង់
   ``collections.abc`` ជាទម្រង់ដែលណែនាំ។

.. _literal-final:

``Literal``, ``Final`` និង Type Alias
=====================================

.. code-block:: python

   from typing import Final, Literal

   # តម្លៃជាក់លាក់តែប៉ុណ្ណោះ
   def set_mode(mode: Literal["read", "write", "append"]) -> None:
       ...


   set_mode("read")        # ✅
   set_mode("delete")      # ❌ type checker បញ្ចេញកំហុស

   # ថេរដែលមិនគួរប្ដូរ
   MAX_SIZE: Final = 1024
   TIMEOUT: Final[float] = 30.0

.. _type-alias:

Type Alias
----------

.. code-block:: python

   # ទម្រង់ចាស់ — ការផ្ដល់តម្លៃធម្មតា
   UserId = int
   Coordinates = tuple[float, float]
   Matrix = list[list[float]]

   # ទម្រង់ថ្មី (3.12+) — PEP 695
   type UserId = int
   type Coordinates = tuple[float, float]
   type Matrix = list[list[float]]
   type JsonValue = str | int | float | bool | None | list["JsonValue"] | dict[str, "JsonValue"]

.. versionadded:: 3.12
   ពាក្យបញ្ជា ``type`` (PEP 695)។ វាបង្កើត ``TypeAliasType`` object
   ដែល **lazy** និងអាចយោងទៅខ្លួនឯងបានដោយមិនចាំបាច់ខ្សែអក្សរ។

.. code-block:: pycon

   >>> type Vec = list[float]          # 3.12+
   >>> Vec                             # TypeAliasType — repr ជាឈ្មោះ alias
   Vec
   >>> Vec.__value__                   # តម្លៃពិតនៅពីក្រោយ
   list[float]

.. note::

   ``type`` ក្លាយជា **soft keyword** ក្នុង Python 3.12។ អ្នកនៅតែអាចប្រើវា
   ជាឈ្មោះអថេរបាន នៅកន្លែងដែលវាមិនចាប់ផ្ដើមពាក្យបញ្ជា ``type X = ...``។

.. _typed-structures:

TypedDict, NamedTuple និង dataclass
===================================

មានវិធីបីយ៉ាងដើម្បីតំណាងទិន្នន័យរចនាសម្ព័ន្ធ៖

.. list-table::
   :header-rows: 1
   :widths: 22 26 26 26

   * -
     - ``TypedDict``
     - ``NamedTuple``
     - ``@dataclass``
   * - ប្រភេទមូលដ្ឋាន
     - ``dict``
     - ``tuple``
     - class ផ្ទាល់ខ្លួន
   * - Mutable
     - ✅
     - ❌
     - ✅ (ឬ ❌ ដោយ ``frozen``)
   * - ចូលដំណើរការ
     - ``d["key"]``
     - ``t.key`` ឬ ``t[0]``
     - ``obj.attr``
   * - ប្រើសម្រាប់
     - JSON, config, API response
     - កំណត់ត្រាថេរសាមញ្ញ
     - domain model ពេញលេញ

.. code-block:: python

   from typing import NamedTuple, NotRequired, TypedDict
   from dataclasses import dataclass


   class UserDict(TypedDict):
       id: int
       name: str
       email: NotRequired[str]


   class UserTuple(NamedTuple):
       id: int
       name: str
       email: str = ""


   @dataclass
   class UserClass:
       id: int
       name: str
       email: str = ""

.. code-block:: pycon

   >>> u1: UserDict = {"id": 1, "name": "សុខា"}
   >>> u1["name"]
   'សុខា'
   >>> u2 = UserTuple(2, "ដារ៉ា")
   >>> u2.name, u2[0]
   ('ដារ៉ា', 2)
   >>> u3 = UserClass(3, "សុភា")
   >>> u3
   UserClass(id=3, name='សុភា', email='')

.. note::

   ``TypedDict`` គ្រាន់តែជា ``dict`` ធម្មតានៅពេលដំណើរការ — Python
   **មិន** បង្កើតប្រភេទថ្មី ឬពិនិត្យ key ទេ។ វាមានប្រយោជន៍តែសម្រាប់
   type checker។

   ``NotRequired[...]`` (3.11+) បញ្ជាក់ថា key នេះអាចអវត្តមាន។
   ``Required[...]`` បញ្ជាក់ផ្ទុយវិញ (មានប្រយោជន៍ក្នុង
   ``TypedDict`` ដែលមាន ``total=False``)។

.. _protocol:

``Protocol`` — Structural Typing
================================

.. versionadded:: 3.8

``Protocol`` អនុញ្ញាតឱ្យអ្នកកំណត់ **interface** ដោយមិនចាំបាច់ inheritance៖

.. code-block:: python

   from typing import Protocol, runtime_checkable


   @runtime_checkable
   class Drawable(Protocol):
       """Object ណាក៏បានដែលមាន method draw()។"""

       def draw(self) -> str: ...


   class Circle:                          # មិនបានប្រកាសថា implement ទេ
       def draw(self) -> str:
           return "○"


   class Square:
       def draw(self) -> str:
           return "□"


   def render(shapes: list[Drawable]) -> str:
       return " ".join(s.draw() for s in shapes)

.. code-block:: pycon

   >>> render([Circle(), Square()])
   '○ □'
   >>> isinstance(Circle(), Drawable)     # ត្រូវការ @runtime_checkable
   True
   >>> isinstance("not drawable", Drawable)
   False

.. note::

   នេះហៅថា **structural typing** ("static duck typing") — ប្រភេទត្រូវបាន
   កំណត់ដោយ **រចនាសម្ព័ន្ធ** ដែល object មាន មិនមែនដោយឈ្មោះ class
   ដែលវាប្រកាសទេ។ វាខុសពី ``abc.ABC`` ដែលតម្រូវឱ្យប្រកាស inheritance
   ដោយច្បាស់ (*nominal typing*)។

   ``@runtime_checkable`` ធ្វើឱ្យ ``isinstance()`` ដំណើរការ ប៉ុន្តែវាពិនិត្យ
   តែ **វត្តមាន method** មិនមែន signature ទេ។

.. _typevar-generics:

TypeVar និង Generic
===================

``TypeVar`` អនុញ្ញាតឱ្យអ្នកសរសេរកូដដែល **រក្សាប្រភេទ** តាមរយៈការហៅ៖

.. code-block:: python

   # ទម្រង់ចាស់
   from typing import TypeVar, Generic

   T = TypeVar("T")


   def first_old(items: list[T]) -> T:
       return items[0]

.. code-block:: python

   # ទម្រង់ថ្មី (3.12+) — PEP 695
   def first[T](items: list[T]) -> T:
       return items[0]


   class Stack[T]:
       def __init__(self) -> None:
           self._items: list[T] = []

       def push(self, item: T) -> None:
           self._items.append(item)

       def pop(self) -> T:
           return self._items.pop()

.. code-block:: pycon

   >>> first([1, 2, 3])          # checker ដឹងថាត្រឡប់ int
   1
   >>> first(["a", "b"])         # checker ដឹងថាត្រឡប់ str
   'a'

**ប្រៀបធៀបជាមួយ ``Any``៖**

.. code-block:: python

   from typing import Any


   def first_any(items: list[Any]) -> Any:   # ❌ បាត់បង់ព័ត៌មានប្រភេទ
       return items[0]


   def first_t[T](items: list[T]) -> T:      # ✅ រក្សាប្រភេទ
       return items[0]

.. note::

   ``TypeVar`` អាចមាន **constraint** ឬ **bound**៖

   .. code-block:: python

      from typing import TypeVar

      # ត្រូវតែជាប្រភេទណាមួយក្នុងបញ្ជី
      StrOrBytes = TypeVar("StrOrBytes", str, bytes)

      # ត្រូវតែជា subclass នៃ bound
      NumberT = TypeVar("NumberT", int, float)

   PEP 695 ផ្ដល់វាក្យសម្ពន្ធខ្លីជាង៖ ``def f[T: (str, bytes)](...)`` និង
   ``def g[T: int](...)``។

.. versionadded:: 3.13
   ``TypeVar`` អាចមាន **តម្លៃលំនាំដើម** (PEP 696)៖
   ``T = TypeVar("T", default=int)``។

.. _paramspec:

``ParamSpec`` — រក្សា Signature
===============================

.. versionadded:: 3.10

``ParamSpec`` អនុញ្ញាតឱ្យ decorator រក្សា signature ពេញលេញនៃអនុគមន៍
ដែលវា decorate៖

.. code-block:: python

   from collections.abc import Callable
   from typing import ParamSpec
   import functools

   P = ParamSpec("P")
   R = TypeVar("R")


   def logged(func: Callable[P, R]) -> Callable[P, R]:
       """រក្សាទាំង parameter និងតម្លៃត្រឡប់។"""

       @functools.wraps(func)
       def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
           print(f"ហៅ {func.__name__}")
           return func(*args, **kwargs)

       return wrapper


   @logged
   def divide(a: int, b: int) -> float:
       return a / b

.. code-block:: pycon
   :no-test:

   >>> import inspect
   >>> inspect.signature(divide)
   <Signature (a: int, b: int) -> float>
   >>> divide(10, 4)
   ហៅ divide
   2.5

.. note::

   បើគ្មាន ``ParamSpec`` អ្នកត្រូវប្រើ ``Callable[..., R]`` ដែលបាត់បង់
   ព័ត៌មាន parameter។ ``P.args`` និង ``P.kwargs`` តំណាងឱ្យ positional
   និង keyword argument រៀងៗខ្លួន។

   ``typing.Concatenate[X, P]`` អនុញ្ញាតឱ្យ decorator បន្ថែម ឬដក
   parameter មួយ។

.. _self-classvar:

``Self`` និង ``ClassVar``
=========================

.. code-block:: python

   from typing import ClassVar, Self


   class Builder:
       version: ClassVar[str] = "1.0"      # របស់ class មិនមែន instance

       def __init__(self) -> None:
           self.parts: list[str] = []

       def add(self, part: str) -> Self:   # ត្រឡប់ instance នៃ class បច្ចុប្បន្ន
           self.parts.append(part)
           return self


   class SubBuilder(Builder):
       pass

.. code-block:: pycon

   >>> b = Builder().add("a").add("b")     # chaining
   >>> b.parts
   ['a', 'b']
   >>> s = SubBuilder().add("x")
   >>> type(s).__name__                    # ✅ SubBuilder មិនមែន Builder
   'SubBuilder'

.. note::

   ``Self`` (3.11+) មានប្រយោជន៍សម្រាប់ method ដែលត្រឡប់ instance
   ខ្លួនឯង (fluent interface)។ បើអ្នកសរសេរ ``-> "Builder"`` នោះ
   ``SubBuilder().add()`` នឹងត្រូវបាន checker យល់ថាត្រឡប់ ``Builder``។

   ``ClassVar`` ប្រាប់ type checker ថា attribute នេះជារបស់ **class**
   មិនមែន instance។ ``@dataclass`` ក៏មិនចាត់ទុក ``ClassVar`` ជា field ដែរ។

.. _typeguard-typeis:

``TypeGuard`` និង ``TypeIs``
============================

**Type narrowing** — ប្រាប់ type checker ថាប្រភេទត្រូវបានកំណត់ច្បាស់
ក្នុង scope មួយ៖

.. code-block:: python

   from typing import TypeGuard, TypeIs, assert_never


   def is_str_list_old(val: list[object]) -> TypeGuard[list[str]]:
       return all(isinstance(x, str) for x in val)


   def is_str_list(val: list[object]) -> TypeIs[list[str]]:
       return all(isinstance(x, str) for x in val)

.. list-table::
   :header-rows: 1
   :widths: 24 76

   * -
     - ភាពខុសគ្នា
   * - ``TypeGuard[X]`` (3.10+)
     - បើ ``True`` → ប្រភេទគឺ ``X``។ បើ ``False`` → ប្រភេទដើម **មិនផ្លាស់ប្ដូរ**
   * - ``TypeIs[X]`` (3.13+)
     - បើ ``True`` → ``X``។ បើ ``False`` → ប្រភេទដើម **ត្រូវបានធ្វើឱ្យតូច** ដោយដក ``X`` ចេញ។ ដូច ``isinstance()`` ពិតប្រាកដ

.. tip::

   ប្រើ ``TypeIs`` សម្រាប់កូដថ្មី — វាមានឥរិយាបថស្របនឹងអ្វីដែល
   អ្នកសរសេរកូដរំពឹង។ ``TypeGuard`` នៅតែមានប្រយោជន៍ពេលអ្នកចង់
   បំលែងប្រភេទទាំងស្រុង (ឧ. ពី JSON dict ទៅ dataclass)។

**Exhaustiveness check** ជាមួយ ``assert_never``៖

.. code-block:: python

   from typing import Literal, assert_never


   def describe(value: Literal["a", "b"]) -> str:
       if value == "a":
           return "អក្សរ a"
       elif value == "b":
           return "អក្សរ b"
       else:
           # បើមានតម្លៃថ្មីត្រូវបានបន្ថែមទៅ Literal ខាងលើ
           # type checker នឹងបញ្ចេញកំហុសនៅទីនេះ
           assert_never(value)

.. _override:

``@override``
=============

.. versionadded:: 3.12

.. code-block:: python

   from typing import override


   class Base:
       def process(self) -> None:
           ...


   class Child(Base):
       @override                        # បញ្ជាក់ថា override method របស់ class មេ
       def process(self) -> None:
           ...

បើ ``Base.process`` ត្រូវបានប្ដូរឈ្មោះ ឬលុប type checker នឹងបញ្ចេញ
កំហុសលើ ``Child.process``។ នេះការពារកំហុសនៅពេល refactor។

.. _introspection:

Introspection នៅពេលដំណើរការ
==============================

.. code-block:: pycon
   :no-test:

   >>> import typing
   >>> typing.get_origin(list[int])
   <class 'list'>
   >>> typing.get_args(list[int])
   (<class 'int'>,)
   >>> typing.get_args(dict[str, int])
   (<class 'str'>, <class 'int'>)
   >>> typing.get_origin(int | str)
   <class 'typing.Union'>
   >>> typing.get_args(int | str)
   (<class 'int'>, <class 'str'>)

   >>> def f(a: int, b: str = "x") -> bool:
   ...     return True
   ...
   >>> f.__annotations__
   {'a': <class 'int'>, 'b': <class 'str'>, 'return': <class 'bool'>}
   >>> typing.get_type_hints(f)
   {'a': <class 'int'>, 'b': <class 'str'>, 'return': <class 'bool'>}

.. list-table::
   :header-rows: 1
   :widths: 34 66

   * - ឧបករណ៍
     - ការប្រើប្រាស់
   * - ``obj.__annotations__``
     - dict នៃ annotation (អាចជាខ្សែអក្សរ បើ lazy)
   * - ``typing.get_type_hints(obj)``
     - ដោះស្រាយ annotation ទៅជា object ពិត — **ណែនាំ**
   * - ``typing.get_origin(t)``
     - ប្រភេទមូលដ្ឋាន (``list[int]`` → ``list``)
   * - ``typing.get_args(t)``
     - parameter នៃ generic
   * - ``inspect.signature(f)``
     - signature ពេញលេញរួមទាំងតម្លៃលំនាំដើម

.. _pep649:

PEP 649 — Annotation ដំណើរការយឺត
===================================

.. versionchanged:: 3.14
   Annotation ត្រូវបានវាយតម្លៃ **យឺត** (lazily)។ ``__annotations__``
   ត្រូវបានគណនានៅពេលអ្នកចូលដំណើរការវា មិនមែននៅពេលកំណត់អនុគមន៍ទេ។

អត្ថប្រយោជន៍៖

* អ្នកអាចយោងទៅ class ដែល **មិនទាន់បានកំណត់** ដោយមិនចាំបាច់ខ្សែអក្សរ៖

  .. code-block:: python

     class Node:
         def child(self) -> Node:      # ✅ ដំណើរការ — មិនចាំបាច់ "Node"
             ...

* ការនាំចូល module លឿនជាង ព្រោះ annotation មិនត្រូវបានវាយតម្លៃ។

.. note::

   ``from __future__ import annotations`` (PEP 563) ធ្វើឱ្យ annotation
   ទាំងអស់ក្លាយជា **ខ្សែអក្សរ**។ វានៅតែដំណើរការ ប៉ុន្តែ PEP 649
   ជាដំណោះស្រាយផ្លូវការចាប់ពី 3.14។ សម្រាប់កូដថ្មី អ្នកមិនចាំបាច់
   ``from __future__ import annotations`` ទៀតទេ។

   បើអ្នកប្រើ ``typing.get_type_hints()`` លើកូដដែលមាន
   ``from __future__ import annotations`` អ្នកត្រូវធានាថាឈ្មោះទាំងអស់
   អាចដោះស្រាយបានក្នុង scope របស់ module។

.. _tools:

ឧបករណ៍ពិនិត្យប្រភេទ
===================

.. list-table::
   :header-rows: 1
   :widths: 22 78

   * - ឧបករណ៍
     - ការពិពណ៌នា
   * - **mypy**
     - type checker ដើម សរសេរដោយ Python។ ``pip install mypy`` រួច ``mypy src/``
   * - **pyright**
     - សរសេរជា TypeScript លឿនជាង។ ជាមូលដ្ឋាននៃ Pylance របស់ VS Code
   * - **pyre**
     - សរសេរជា OCaml ដោយ Meta
   * - **ruff**
     - linter/formatter លឿន (Rust) — មិនមែន type checker ពេញលេញទេ
   * - **pytype**
     - ដោយ Google អាចសន្និដ្ឋានប្រភេទដោយស្វ័យប្រវត្តិ

.. code-block:: console

   $ pip install mypy
   $ mypy --strict src/
   src/app.py:12: error: Argument 1 to "double" has incompatible type "str"; expected "int"
   Found 1 error in 1 file (checked 3 source files)

.. _typehints-best-practices:

ការអនុវត្តល្អបំផុត
======================

#. **ចាប់ផ្ដើមត្រង់ព្រំដែន** — annotate អនុគមន៍សាធារណៈ API boundary
   និងទិន្នន័យដែលមកពីខាងក្រៅជាមុន។ កូដផ្ទៃក្នុងអាចបន្ថែមបន្តិចម្ដងៗ។
#. **Gradual typing** — អ្នកមិនចាំបាច់ annotate គ្រប់យ៉ាងទេ។ Python
   អនុញ្ញាតឱ្យលាយឡំកូដដែលមាន និងគ្មាន annotation។
#. **កុំប្រើ ``Any`` ដើម្បីបំបាត់កំហុស** — វាបិទការត្រួតពិនិត្យទាំងស្រុង។
   បើចាំបាច់ ប្រើ ``object`` វិញ ដែលនៅតែតម្រូវឱ្យពិនិត្យប្រភេទមុនប្រើ។
#. **ប្រើប្រភេទ built-in generic** (``list[int]`` មិនមែន ``List[int]``)។
#. **ប្រើ ``X | None``** ជាជាង ``Optional[X]`` ក្នុងកូដថ្មី។
#. **ប្រើ PEP 695 syntax** (``def f[T](...)``, ``type X = ...``) សម្រាប់
   គម្រោងដែលតម្រូវ Python 3.12+។
#. **ដំណើរការ type checker ក្នុង CI** — annotation ដែលមិនត្រូវបាន
   ពិនិត្យគឺគ្រាន់តែជាអត្ថាធិប្បាយដែលអាចខុសបាន។
#. **កុំពឹងផ្អែកលើ annotation សម្រាប់ validation** — សម្រាប់ទិន្នន័យ
   ពីអ្នកប្រើ ប្រើបណ្ណាល័យដូចជា ``pydantic`` ឬការពិនិត្យដោយផ្ទាល់។
#. **Annotate ``self`` និង ``cls`` មិនចាំបាច់** — type checker ដឹងរួចហើយ។
#. **ប្រើ ``from __future__ import annotations``** តែនៅពេលអ្នកត្រូវការ
   គាំទ្រ Python < 3.10 ហើយចង់បានវាក្យសម្ពន្ធ ``X | Y``។

.. _typehints-summary:

សង្ខេប
======

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - វាក្យសម្ពន្ធ
     - កំណែដែលបានណែនាំ
   * - ``def f(x: int) -> str``
     - 3.0 (PEP 3107)
   * - ``x: int = 0``
     - 3.6 (PEP 526)
   * - ``list[int]``, ``dict[str, int]``
     - 3.9 (PEP 585)
   * - ``int \| None``
     - 3.10 (PEP 604)
   * - ``ParamSpec``, ``Concatenate``
     - 3.10 (PEP 612)
   * - ``TypeGuard``
     - 3.10 (PEP 647)
   * - ``Self``, ``assert_never``, ``LiteralString``
     - 3.11 (PEP 673, 645, 675)
   * - ``TypeVarTuple``, ``Unpack``, ``dataclass_transform``
     - 3.11 (PEP 646, 681)
   * - ``def f[T](...)``, ``class C[T]``, ``type X = ...``
     - 3.12 (PEP 695)
   * - ``@override``, ``TypeAliasType``
     - 3.12 (PEP 698, 695)
   * - ``TypeIs``, ``ReadOnly``, ``NoDefault``
     - 3.13 (PEP 742, 705, 696)
   * - Annotation ដំណើរការយឺត
     - 3.14 (PEP 649)

.. rubric:: ប្រភពយោង

* `typing — Support for type hints <https://docs.python.org/3/library/typing.html>`_
* `Type Hints Specification <https://typing.python.org/en/latest/spec/index.html>`_
* `Annotations Best Practices <https://docs.python.org/3/howto/annotations.html>`_
* `typing — Python documentation <https://docs.python.org/3/library/typing.html#module-typing>`_
* `mypy documentation <https://mypy.readthedocs.io/>`_
* `PEP 484 — Type Hints <https://peps.python.org/pep-0484/>`_
* `PEP 585 — Type Hinting Generics In Standard Collections <https://peps.python.org/pep-0585/>`_
* `PEP 604 — X | Y syntax for unions <https://peps.python.org/pep-0604/>`_
* `PEP 695 — Type Parameter Syntax <https://peps.python.org/pep-0695/>`_
* `PEP 649 — Deferred Evaluation Of Annotations <https://peps.python.org/pep-0649/>`_
