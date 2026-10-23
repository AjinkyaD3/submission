import os
import re
from collections import defaultdict


# --- Function to preprocess text (remove punctuation, lowercase) ---
def preprocess(text):
    text = text.lower()
    text = re.sub(r'[^a-z0-9\s]', '', text)
    return text.split()


def build_inverted_index(folder_path):
    inverted_index = defaultdict(list)
    files = [f for f in os.listdir(folder_path) if f.endswith('.txt')]

    for idx, file in enumerate(files):
        with open(os.path.join(folder_path, file), 'r', encoding='utf-8') as f:
            words = preprocess(f.read())
            for position, word in enumerate(words):
                inverted_index[word].append((file, position))

    return inverted_index, files


def search_word(inverted_index, query):
    query = query.lower()
    if query in inverted_index:
        return inverted_index[query]
    else:
        return []


def display_index(inverted_index):
    print("\n--- Inverted Index ---")
    for word, occurrences in inverted_index.items():
        print(f"{word}: {occurrences}")


if __name__ == "__main__":
    folder = "documents"  # folder containing your text files
    inverted_index, files = build_inverted_index(folder)

    # Display complete index
    display_index(inverted_index)

    # --- Query input ---
    while True:
        query = input("\nEnter a word to search (or 'exit' to quit): ").strip()
        if query.lower() == 'exit':
            break
        results = search_word(inverted_index, query)
        if results:
            print(f"\n'{query}' found in:")
            for file, pos in results:
                print(f"  -> {file} (position {pos})")
        else:
            print(f"\n'{query}' not found in any document.")
