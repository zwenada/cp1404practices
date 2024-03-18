def count_occurrences_in_text(text_data):
    word_occurrences = {}
    words = text_data.split()

    for word in words:
        word_occurrences[word] = word_occurrences.get(word, 0) + 1

    return word_occurrences

def main():
    text_data = input("Enter the text: ")
    word_occurrences = count_occurrences_in_text(text_data)

    max_word_length = max(len(word) for word in word_occurrences.keys())

    for word, count in sorted(word_occurrences.items()):
        print(f"{word:>{max_word_length}} : {count}")

if __name__ == "__main__":
    main()
