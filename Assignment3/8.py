# Given a string (sentence), count the frequency of each word.

def count_word_frequency(sentence: str) -> dict:
    words = sentence.split()
    frequency = {}
    for word in words:
        frequency[word] = frequency.get(word, 0) + 1
    return frequency

def main():
    print("--- Word Frequency Counter ---")
    sentence = input("Enter a sentence: ")
    word_count = count_word_frequency(sentence)
    print("\nWord Frequency:")
    for word, count in word_count.items():
        print(f"'{word}': {count}")

if __name__ == "__main__":
    main()
