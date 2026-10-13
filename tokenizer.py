from transformers import AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained(
    "bert-base-uncased"
)
text = "unbelievability"
encoded = tokenizer(text)
print("Original text:",text)

print("Token ID's:", encoded["input_ids"])

print("Attention mask:", encoded["attention_mask"])

tokens = tokenizer.convert_ids_to_tokens(
    encoded["input_ids"]
)

print("Tokens:", tokens)

decoded =  tokenizer.decode(
    encoded["input_ids"]
)

print("Decoded text:", decoded)

print(
    "Decoded without special token:",
    tokenizer.decode(
        encoded["input_ids"],
        skip_special_tokens= True
    )
)