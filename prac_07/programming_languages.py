class ProgrammingLang:
    """Represent information about a programming language."""

    def __init__(self, lang_name, typing_style, has_reflection, first_year):
        """Construct a ProgrammingLang from the given values."""
        self.lang_name = lang_name
        self.typing_style = typing_style
        self.has_reflection = has_reflection
        self.first_year = first_year

    def __repr__(self):
        """Return string representation of a ProgrammingLang."""
        return f"{self.lang_name}, {self.typing_style} Typing, Reflection={self.has_reflection}, First appeared in {self.first_year}"

    def is_dynamic(self):
        """Determine if language is dynamically typed."""
        return self.typing_style == "Dynamic"

def test_languages():
    ruby_lang = ProgrammingLang("Ruby", "Dynamic", True, 1995)
    python_lang = ProgrammingLang("Python", "Dynamic", True, 1991)
    visual_basic_lang = ProgrammingLang("Visual Basic", "Static", False, 1991)

    languages = [ruby_lang, python_lang, visual_basic_lang]
    print(python_lang)

    print("The dynamically typed languages are:")
    for lang in languages:
        if lang.is_dynamic():
            print(lang.lang_name)

test_languages()
