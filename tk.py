
from transformers import AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")

texts = [
    "I am learning Hugging Face!",
    "playing is fun",
    "The unbelievable discovery was fascinating."
]

for text in texts:
    encoded = tokenizer(text)

    tokens = tokenizer.convert_ids_to_tokens(encoded["input_ids"])

    print("\nOriginal text:", text)
    print("Token IDs:", encoded["input_ids"])
    print("Tokens:", tokens)
    print("Number of tokens:", len(encoded["input_ids"]))
