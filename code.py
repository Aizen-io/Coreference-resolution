import spacy

def coreference_resolution_without_neuralcoref(text):
    # Load the spaCy English language model
    nlp = spacy.load("en_core_web_sm")

    # Process the input text using spaCy
    doc = nlp(text)

    # Iterate over the sentences and print the coreference-resolved output
    for sent in doc.sents:
        print("Original Sentence:", sent.text)
 # Iterate over the entities in the sentence
        for ent in sent.ents:
            if ent.root.head.text.lower() == "he" or ent.root.head.text.lower() == "she":
                # Replace "he" or "she" with the entity text
                resolved_text = sent.text.replace(ent.root.head.text, ent.text, 1)
                print("Coreference Resolved Sentence:", resolved_text)

        print("\n")

if __name__ == "__main__":
    # Example usage
    text = "John is a data scientist. He works at a tech company. John loves his job."
    coreference_resolution_without_neuralcoref(text)
