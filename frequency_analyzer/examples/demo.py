from frequency_analyzer.analyzer import (
    remove_gutenberg_header,
    top_n_words,
    word_frequency,
)


# helper function to load the data
# encoding= "utf-8" tells py how to map characters
def load_text(filepath):
    with open(filepath, mode="r", encoding="utf-8") as file:
        return file.read()


# helper function to print words
def print_top_words(counts, title, n=10):
    print(f"\n{title}")
    print("-" * len(title))

    for word, count in top_n_words(counts, n):
        print(f"{word}: {count}")


def main():
    shakespeare = load_text("data/raw/shakespeare.txt")
    shakespeare = remove_gutenberg_header(shakespeare)
    shakespeare_counts = word_frequency(shakespeare)

    messy = load_text("data/raw/messy.txt")
    messy_counts = word_frequency(messy)

    alice = load_text("data/raw/alice.txt")
    alice_counts = word_frequency(alice)

    print_top_words(shakespeare_counts, "Shakespeare")
    print_top_words(messy_counts, "Messy Text")
    print_top_words(alice_counts, "Alice Text")


if __name__ == "__main__":
    main()
