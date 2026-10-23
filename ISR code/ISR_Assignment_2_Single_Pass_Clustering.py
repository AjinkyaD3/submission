import os
import math
from sklearn.feature_extraction.text import CountVectorizer


# --- Function to compute Dice Coefficient ---
def dice_coefficient(text1, text2):
    vectorizer = CountVectorizer(binary=True)
    vectors = vectorizer.fit_transform([text1, text2]).toarray()
    intersection = sum(vectors[0] * vectors[1])
    total = sum(vectors[0]) + sum(vectors[1])
    if total == 0:
        return 0
    return (2 * intersection) / total


def single_pass_clustering(documents, threshold=0.3):
    clusters = []  # list of clusters (each cluster is a list of doc indices)
    representatives = []  # representative document text for each cluster

    for idx, doc in enumerate(documents):
        assigned = False

        for i, rep in enumerate(representatives):
            sim = dice_coefficient(doc, rep)
            if sim >= threshold:
                clusters[i].append(idx)
                # Update representative (can be mean text or concatenation)
                representatives[i] = doc
                assigned = True
                break

        if not assigned:
            clusters.append([idx])
            representatives.append(doc)

    return clusters


# --- Load text files from directory ---
def load_documents_from_folder(folder_path):
    docs = []
    for file in os.listdir(folder_path):
        if file.endswith(".txt"):
            with open(os.path.join(folder_path, file), "r", encoding="utf-8") as f:
                docs.append(f.read())
    return docs


if __name__ == "__main__":
    folder = "documents"  # folder containing your text files
    docs = load_documents_from_folder(folder)

    print(f"Loaded {len(docs)} documents.")
    clusters = single_pass_clustering(docs, threshold=0.4)

    # --- Print results ---
    print("\n--- Clustering Result ---")
    for i, cluster in enumerate(clusters):
        print(f"Cluster {i+1}: Documents {', '.join(str(idx+1) for idx in cluster)}")
