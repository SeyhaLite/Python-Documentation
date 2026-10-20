"""ម៉ូឌុលសាកល្បង — ផ្ដល់ពាក្យសួស្ដីជាច្រើនភាសា។"""

DEFAULT_LANGUAGE = "km"

_TRANSLATIONS = {
    "km": "សួស្ដី",
    "en": "Hello",
    "ja": "こんにちは",
}


def greet(name, lang=None):
    """ត្រឡប់ពាក្យសួស្ដីសម្រាប់មនុស្សម្នាក់។"""
    word = _TRANSLATIONS.get(lang or DEFAULT_LANGUAGE, _TRANSLATIONS["en"])
    return f"{word}, {name}!"


def supported_languages():
    """ត្រឡប់បញ្ជីភាសាដែលគាំទ្រ។"""
    return sorted(_TRANSLATIONS)


def _self_test():
    assert greet("សុខា") == "សួស្ដី, សុខា!"
    print("self-test passed")


if __name__ == "__main__":
    # ដំណើរការតែពេលចាក់ `python3 greetings.py` ប៉ុណ្ណោះ
    _self_test()
    print(greet("ពិភពលោក"))
