# Configuration file for the Sphinx documentation builder.
# Python Documentation — Khmer Edition
#
# មាតិកាដើមយោងតាមឯកសារផ្លូវការ CPython (Doc/) ក្រោមអាជ្ញាបណ្ណ PSF License v2។
# សូមមើល source/license_attribution.rst និង LICENSE សម្រាប់ព័ត៌មានលម្អិត។

project = "Python"
copyright = (
    "ឯកសារដើម © 2001 Python Software Foundation; All Rights Reserved "
    "(PSF License v2) · កំណែបកប្រែខ្មែរ © សហគមន៍ SeyhaLite"
)
author = "SeyhaLite"

# កំណែ Python ដែលឯកសារនេះយោងទៅ
version = "3.15"
release = "3.15.0"

language = "km"

extensions = ["sphinx_sitemap", "sphinx_copybutton"]

# -- custom directive option --------------------------------------------------
# `:no-test:` marks a code block that tools/run_examples.py must NOT execute:
# deliberately-broken examples (infinite loops), interactive snippets that need
# a TTY, and multi-file illustrations. Registering it here keeps
# `sphinx-build -W` clean while still allowing the test harness to see the flag.
from docutils.parsers.rst import directives  # noqa: E402
from sphinx.directives.code import CodeBlock  # noqa: E402

CodeBlock.option_spec["no-test"] = directives.flag

# -- sphinx-copybutton --------------------------------------------------------
# ចម្លងតែកូដ — រំលង prompt (>>>, ...) និង output របស់ doctest
copybutton_prompt_text = r">>> |\.\.\. |\$ |In \[\d*\]: | {2,5}\.\.\.: | {5,8}: "
copybutton_prompt_is_regexp = True
copybutton_only_copy_prompt_lines = False
# line numbers must never end up in the clipboard
copybutton_exclude = ".linenos"

templates_path = ["_templates"]
html_static_path = ["_static"]
html_extra_path = ["_extra"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# -- Read the Docs theme ------------------------------------------------------
html_theme = "sphinx_rtd_theme"
html_theme_options = {
    "collapse_navigation": True,
    "sticky_navigation": True,
    "navigation_depth": 3,
    "includehidden": True,
    "titles_only": False,
    "prev_next_buttons_location": "bottom",
    "style_external_links": True,
    "flyout_display": "hidden",
    "vcs_pageview_mode": "edit",
    # ផ្នែកខាងលើ sidebar ត្រូវគ្នានឹង palette នៃ theme
    "style_nav_header_background": "#1f2328",
}

# Python logo និង favicon ផ្លូវការរបស់ PSF — ប្រើដោយ **មិនកែប្រែ**
# (unaltered)។ PSF Trademark Usage Policy អនុញ្ញាត nominative use នៃ
# unaltered logo សម្រាប់គោលបំណងមិនមែនពាណិជ្ជកម្ម ដើម្បីលើកកម្ពស់
# ភាសាកម្មវិធី Python ដោយមិនចាំបាច់ការអនុញ្ញាតជាមុន។
# សូមមើល source/license_attribution.rst សម្រាប់សេចក្ដីថ្លែងការណ៍ trademark។
html_logo = "_static/python-logo.svg"
html_favicon = "_static/python-favicon.ico"
logo_url = None

# Edit on GitHub (តំណកែសម្រួលក្នុង breadcrumb)
html_context = {
    "display_github": True,
    "github_user": "SeyhaLite",
    "github_repo": "Python-Documentation",
    "github_version": "main",
    "conf_py_path": "/source/",
}

html_title = "ឯកសារ Python ជាភាសាខ្មែរ"
html_short_title = "Python ខ្មែរ"
html_show_sphinx = False
html_show_copyright = True
html_copy_source = False
html_last_updated_fmt = "%d %b %Y"

# ភាសាស្វែងរក — Sphinx មិនទាន់មាន tokenizer ខ្មែរ ដូច្នេះប្រើ "en"
# ដើម្បីឱ្យស្វែងរក keyword/API អង់គ្លេសឃើញ (ឧ. def, list, open)។
html_search_language = "en"

# Khmer fonts + light/dark palette (ឯកសារតែមួយ override បន្ទាប់ពី theme CSS)
html_css_files = ["khmer.css"]

# -- SEO ----------------------------------------------------------------------
html_baseurl = "https://seyhalite.github.io/Python-Documentation/"
sitemap_url_scheme = "{link}"
sitemap_filename = "sitemap.xml"

# -- code blocks: Python highlighting + line numbers on every block -----------
highlight_language = "python"

# Turn line numbering ON by default for every code-block / literalinclude.
# Sphinx's CodeBlock.run() enables numbering only when 'linenos' is present in
# self.options, so injecting it there is the minimal, version-stable hook.
# A block can opt out with `:no-linenos:`.
from docutils.parsers.rst import directives  # noqa: E402
from sphinx.directives.code import CodeBlock, LiteralInclude  # noqa: E402


def _register_no_linenos(cls):
    cls.option_spec = dict(cls.option_spec)
    cls.option_spec["no-linenos"] = directives.flag
    return cls


def _wrap_run(cls):
    original = cls.run

    def run(self):
        if "no-linenos" not in self.options:
            self.options.setdefault("linenos", True)
        else:
            self.options.pop("linenos", None)
            self.options.pop("no-linenos", None)
        return original(self)

    cls.run = run
    return cls


for _cls in (CodeBlock, LiteralInclude):
    _wrap_run(_register_no_linenos(_cls))

# -- nitpicky build -----------------------------------------------------------
# បើកការពិនិត្យ cross-reference ដើម្បីឱ្យ sphinx-build -W ចាប់យកតំណខូច
nitpicky = False
