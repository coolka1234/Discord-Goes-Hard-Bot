from transformers import GPT2LMHeadModel, GPT2Tokenizer

model_name = "gpt2"
model = GPT2LMHeadModel.from_pretrained(model_name)
tokenizer = GPT2Tokenizer.from_pretrained(model_name)

def generate_sentence(prompt, max_length=50, num_return_sequences=1):
    inputs = tokenizer.encode(prompt, return_tensors='pt')
    attention_mask = inputs.ne(tokenizer.pad_token_id).long()
    outputs = model.generate(
        inputs, 
        max_length=max_length, 
        num_return_sequences=num_return_sequences,
        no_repeat_ngram_size=2,
        top_k=50,
        # top_p=0.95,
        # temperature=0.7,
        attention_mask=attention_mask
        
    )
    generated_sentences = [tokenizer.decode(output, skip_special_tokens=True) for output in outputs]
    return generated_sentences

# Example usage
prompt = "Write a complex sentence about"
sentences = generate_sentence(prompt)

for i, sentence in enumerate(sentences):
    print(f"Generated Sentence {i + 1}: {sentence}")
