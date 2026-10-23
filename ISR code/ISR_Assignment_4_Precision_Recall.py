def calculate_precision_recall(retrieved_docs, relevant_docs):
    # Convert to sets to make intersection easier
    retrieved = set(retrieved_docs)
    relevant = set(relevant_docs)

    # True Positives: relevant and retrieved
    relevant_retrieved = retrieved.intersection(relevant)

    # Precision = |Relevant n Retrieved| / |Retrieved|
    precision = len(relevant_retrieved) / len(retrieved) if retrieved else 0

    # Recall = |Relevant n Retrieved| / |Relevant|
    recall = len(relevant_retrieved) / len(relevant) if relevant else 0

    # F1 Score (optional)
    f1_score = (2 * precision * recall) / (precision + recall) if (precision + recall) else 0

    return precision, recall, f1_score


if __name__ == "__main__":
    print("=== Precision and Recall Calculator ===")

    # Example Input
    relevant_docs = input("Enter relevant document IDs (comma separated): ").split(",")
    retrieved_docs = input("Enter retrieved document IDs (comma separated): ").split(",")

    # Clean up whitespace
    relevant_docs = [doc.strip() for doc in relevant_docs if doc.strip()]
    retrieved_docs = [doc.strip() for doc in retrieved_docs if doc.strip()]

    precision, recall, f1 = calculate_precision_recall(retrieved_docs, relevant_docs)

    print("\n--- Results ---")
    print(f"Relevant Documents: {relevant_docs}")
    print(f"Retrieved Documents: {retrieved_docs}")
    print(f"Precision = {precision:.2f}")
    print(f"Recall    = {recall:.2f}")
    print(f"F1 Score  = {f1:.2f}")
