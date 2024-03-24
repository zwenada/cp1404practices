from language import Language

def main():
    """Main program to demonstrate the use of the Language class."""
    python = Language("Python", "Dynamic", True, 1991)
    ruby = Language("Ruby", "Dynamic", True, 1995)
    visual_basic = Language("Visual Basic", "Static", False, 1991)
    languages = [python, ruby, visual_basic]
    print("The dynamically typed languages are:")
    for language in languages:
        if language.is_dynamic():
            print(language.name)

    print(f"\nTesting the __str__ method:")
    for language in languages:
        print(language)

if __name__ == "__main__":
    main()
