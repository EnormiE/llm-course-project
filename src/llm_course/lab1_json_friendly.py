import json
from transformers import AutoTokenizer

MODEL_NAME_V1 = "Qwen/Qwen2.5-0.5B-Instruct"
tokenizer_v1 = AutoTokenizer.from_pretrained(MODEL_NAME_V1)
MODEL_NAME_V2 = "bert-base-cased"
tokenizer_v2 = AutoTokenizer.from_pretrained(MODEL_NAME_V2)

samples = [
    "Jacak",
    "for name, tokenizer in [(MODEL_NAME_V1, tokenizer_v1), (MODEL_NAME_V2, tokenizer_v2)]:",
    "55",
    "🤣👌",
    "Duży model językowy",
    "LLM-y 🤖 kosztują 0.01 USD",
]

results = {}

# cleanup for json purposes, struct to dict
for name, tokenizer in [(MODEL_NAME_V1, tokenizer_v1), (MODEL_NAME_V2, tokenizer_v2)]:
    model_data = []
    for text in samples:
        ids = tokenizer.encode(text, add_special_tokens=False)
        pieces = [tokenizer.decode([token_id]) for token_id in ids]
        model_data.append({
            "text": text,
            "token_ids": ids,
            "tokens": pieces,
            "token_count": len(ids)
        })
    results[name] = model_data

# print dict in json format
print(json.dumps(results, indent=4, ensure_ascii=False))