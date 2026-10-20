.. _khmer-python-docs:

#######################################
ឯកសារ Python ជាភាសាខ្មែរ
#######################################

.. admonition:: កំណែ Python ដែលឯកសារនេះយោង
   :class: note

   មាតិកាទាំងអស់សរសេរសម្រាប់ **Python 3.15** (កំណែ stable ចេញថ្ងៃ ៩ តុលា ២០២៦)។
   ឧទាហរណ៍កូដនីមួយៗត្រូវបានដំណើរការផ្ទៀងផ្ទាត់ជាក់ស្ដែងលើ CPython 3.15.0។
   Python 2 មិនត្រូវបានគាំទ្រទេ — សូមកុំប្រើវា។

សូមស្វាគមន៍មកកាន់ឯកសារបង្រៀនភាសា **Python** ជាភាសាខ្មែរ។ គម្រោងនេះយោងតាម
ឯកសារផ្លូវការរបស់ CPython ក្នុងថត ``Doc/`` (``Doc/tutorial/``, ``Doc/using/``
និង ``Doc/library/``) ហើយសរសេរឡើងវិញជាភាសាខ្មែរដើម្បីឱ្យអ្នកសិក្សាខ្មែរងាយយល់។

គោលការណ៍សំខាន់ពីរដែលយើងរក្សាជានិច្ច៖

1. **ពាក្យបច្ចេកទេស និងកូដមិនបកប្រែទេ។** ពាក្យគន្លឹះដូចជា ``if``, ``for``,
   ``while``, ``def``, ``class``, ``import``, ``return``, ``True``, ``False``,
   ``None`` ឈ្មោះ function, class, module និង parameter ទាំងអស់នៅដូចដើម
   ជាភាសាអង់គ្លេស។ មានតែការពន្យល់ប៉ុណ្ណោះដែលជាភាសាខ្មែរ។
2. **ឧទាហរណ៍កូដត្រូវតែដំណើរការពិត។** គ្មាន API ដែលស្មានចិត្ត ឬបង្កើតឡើងទេ។

.. topic:: តើអ្នកគួរចាប់ផ្ដើមពីណា?

   បើអ្នកមិនទាន់ដំឡើង Python ទេ សូមចាប់ផ្ដើមពី
   :doc:`getting_started`។ បើអ្នកចេះភាសាគម្រោងវការផ្សេងរួចហើយ
   អ្នកអាចរំលងទៅ :doc:`syntax_variables_types` បានភ្លាម។

----

.. _status:

ស្ថានភាពនៃការបកប្រែ
====================

ឯកសារនេះ **មិនទាន់បញ្ចប់ទាំងស្រុងទេ**។ ខាងក្រោមជាតារាងស្ថានភាពពិតប្រាកដ៖

.. list-table:: ជំពូកដែលបានបញ្ចប់
   :header-rows: 1
   :widths: 8 42 22 28

   * - លេខ
     - ជំពូក
     - ស្ថានភាព
     - ប្រភពដើមក្នុង CPython ``Doc/``
   * - ១
     - :doc:`getting_started` — ចាប់ផ្ដើម និងការដំឡើង
     - ✅ បញ្ចប់
     - ``tutorial/appetite.rst``, ``tutorial/interpreter.rst``, ``using/unix.rst``, ``using/windows.rst``, ``using/mac.rst``
   * - ២
     - :doc:`syntax_variables_types` — វាក្យសម្ពន្ធ អថេរ និងប្រភេទទិន្នន័យ
     - ✅ បញ្ចប់
     - ``tutorial/introduction.rst``, ``library/stdtypes.rst``, ``reference/lexical_analysis.rst``
   * - ៣
     - :doc:`strings_collections` — ខ្សែអក្សរ និងសំណុំទិន្នន័យ
     - ✅ បញ្ចប់
     - ``tutorial/datastructures.rst``, ``tutorial/inputoutput.rst``, ``library/stdtypes.rst``
   * - ៤
     - :doc:`control_flow` — លក្ខខណ្ឌ និងរង្វិលជុំ
     - ✅ បញ្ចប់
     - ``tutorial/controlflow.rst``
   * - ៥
     - :doc:`functions_scope` — អនុគមន៍ និងវិសាលភាពអថេរ
     - ✅ បញ្ចប់
     - ``tutorial/controlflow.rst``, ``tutorial/classes.rst`` (ផ្នែក Scopes and Namespaces)
   * - ៦
     - :doc:`file_handling` — ការគ្រប់គ្រងឯកសារ
     - ✅ បញ្ចប់
     - ``tutorial/inputoutput.rst``, ``library/pathlib.rst``, ``library/json.rst``, ``library/os.rst``
   * - ៧
     - :doc:`modules_packages` — Modules និង Packages
     - ✅ បញ្ចប់
     - ``tutorial/modules.rst``, ``reference/import.rst``, ``library/sys.rst``, ``library/importlib.rst``
   * - ៨
     - :doc:`exceptions` — Exceptions និងការគ្រប់គ្រងកំហុស
     - ✅ បញ្ចប់
     - ``tutorial/errors.rst``, ``library/exceptions.rst``, ``library/contextlib.rst``
   * - ៩
     - :doc:`classes_oop` — Classes និង OOP
     - ✅ បញ្ចប់
     - ``tutorial/classes.rst``, ``reference/datamodel.rst``, ``library/dataclasses.rst``, ``library/abc.rst``

.. list-table:: ជំពូកដែលគ្រោងទុក (មិនទាន់បានសរសេរ)
   :header-rows: 1
   :widths: 8 55 37

   * - លេខ
     - ជំពូក
     - ស្ថានភាព
   * - ១០
     - Iterators និង Generators
     - ⬜ មិនទាន់ចាប់ផ្ដើម
   * - ១១
     - Decorators
     - ⬜ មិនទាន់ចាប់ផ្ដើម
   * - ១២
     - Type Hints
     - ⬜ មិនទាន់ចាប់ផ្ដើម
   * - ១៣
     - Standard Library
     - ⬜ មិនទាន់ចាប់ផ្ដើម
   * - ១៤
     - Virtual Environments និង Packages
     - ⬜ មិនទាន់ចាប់ផ្ដើម
   * - ១៥
     - Testing, Debugging និង Best Practices
     - ⬜ មិនទាន់ចាប់ផ្ដើម

.. warning::

   សូមកុំយល់ថាឯកសារ Python ទាំងមូលត្រូវបានបកប្រែរួចហើយ។ បច្ចុប្បន្នមានតែ
   **៩ ជំពូក** ប៉ុណ្ណោះដែលបានបញ្ចប់ ហើយផ្នែកធំនៃឯកសារផ្លូវការ
   (Library Reference, Language Reference, C API) មិនទាន់ត្រូវបានប៉ះពាល់ទេ។

----

មាតិកា
======

.. toctree::
   :maxdepth: 2
   :caption: មេរៀន

   getting_started
   syntax_variables_types
   strings_collections
   control_flow
   functions_scope
   file_handling
   modules_packages
   exceptions
   classes_oop

.. toctree::
   :maxdepth: 1
   :caption: ព័ត៌មានអំពីគម្រោង

   license_attribution

----

ប្រភព និងអាជ្ញាបណ្ណ
=======================

ឯកសារដើមគឺជាប្រភពផ្លូវការរបស់គម្រោង Python៖

* ឯកសារផ្លូវការ — https://docs.python.org/3/
* Source repository — https://github.com/python/cpython/tree/main/Doc

មាតិកាដើមរក្សាសិទ្ធិដោយ **Python Software Foundation (PSF)** ក្រោមអាជ្ញាបណ្ណ
**PSF License Version 2**។ កំណែខ្មែរនេះគឺជា *derivative work* ដែលអាជ្ញាបណ្ណ
នោះអនុញ្ញាត ដោយរក្សាសេចក្ដីជូនដំណឹងអំពីសិទ្ធិដើម និងបញ្ជាក់សង្ខេបអំពី
ការផ្លាស់ប្ដូរដែលបានធ្វើ។ សូមអាន :doc:`license_attribution` និងឯកសារ
``LICENSE`` ក្នុង repository សម្រាប់ព័ត៌មានលម្អិត។

"Python" និងរូបសញ្ញា Python គឺជា trademark របស់ Python Software Foundation។
គម្រោងនេះមិនទទួលបានការអនុម័ត ឬឧបត្ថម្ភពី PSF ទេ។

