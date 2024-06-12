from transformers import AutoModelForCausalLM, AutoTokenizer
import wonderwords

model_name = "microsoft/DialoGPT-medium"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

def generate_discord_message(prompt, max_length=150, num_return_sequences=30):
    inputs = tokenizer.encode(prompt, return_tensors='pt')
    
    outputs = model.generate(
        inputs,
        max_length=max_length,
        num_return_sequences=num_return_sequences,
        no_repeat_ngram_size=3,
        do_sample=True,
        top_k=50,
        top_p=0.95,
        temperature=0.7,
    )
    
    generated_messages = [tokenizer.decode(output, skip_special_tokens=True) for output in outputs]
    return generated_messages

prompt = ""
messages = []
num_of_prompts= 100
for i in range(num_of_prompts):
    prompt = wonderwords.RandomWord().word()
    messages.append(generate_discord_message(prompt, num_return_sequences=1))

print(messages)


# for i, message in enumerate(messages):
#     print(f"Generated Message {i + 1}: {message[0]}")
