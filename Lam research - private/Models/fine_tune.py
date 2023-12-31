# -*- coding: utf-8 -*-
"""Fine_tune.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1AKvtcIsNr-91RIz5gmbHPVxGbL7xCZtc
"""

# pip install transformers

import pandas as pd
from transformers import GPT2Tokenizer

# Load your tabular data (replace with your own)
data = {
    "Name": ["John", "Alice", "Bob"],
    "Age": [25, 30, 22],
    "City": ["New York", "San Francisco", "Los Angeles"],
}


df = pd.DataFrame(data)

# Convert tabular data to text
text_data = []
for index, row in df.iterrows():
    row_text = " ".join([f"[{col}]: {str(row[col])}" for col in df.columns])
    text_data.append(row_text)

data

df

text_data

from transformers import GPT2LMHeadModel, GPT2Tokenizer, GPT2Config
from torch.utils.data import DataLoader

# Load the GPT-2 tokenizer
tokenizer = GPT2Tokenizer.from_pretrained("gpt2-large")

# Convert tabular data to text
text_data = []
for index, row in df.iterrows():
    row_text = " ".join([f"[{col}]: {str(row[col])}" for col in df.columns])
    text_data.append(row_text)

# Tokenize the tabular data
tokenized_data = [tokenizer.encode(row, return_tensors="pt") for row in text_data]

# DataLoader for training
dataloader = DataLoader(tokenized_data, batch_size=2, shuffle=True)

# Example fine-tuning function
def fine_tune_gpt2(model_name, dataloader, output_dir):
    # Load GPT-2 model
    model = GPT2LMHeadModel.from_pretrained(model_name)

    # Fine-tuning setup...
    # (You can use the provided fine-tuning function or customize it based on your specific needs)

    # Example training loop
    for epoch in range(5):
        for inputs in dataloader:
            model.train()
            # Your training code here...
            # (This is where you update the model with your training data)

    # Save the fine-tuned model
    model.save_pretrained(output_dir)
    tokenizer.save_pretrained(output_dir)

# Example usage
fine_tune_gpt2("gpt2-large", dataloader, "output")

for i in dataloader:
  print(i)

from transformers import GPT2LMHeadModel, GPT2Tokenizer

model_name = "output"  # Replace with the actual path
model = GPT2LMHeadModel.from_pretrained(model_name)
tokenizer = GPT2Tokenizer.from_pretrained(model_name)

def generate_text(prompt, max_length=100, temperature=0.7, top_k=100):
    input_ids = tokenizer.encode(prompt, return_tensors="pt")
    output = model.generate(
        input_ids,
        max_length=max_length,
        temperature=temperature,
        top_k=top_k,
        pad_token_id=tokenizer.eos_token_id,
        do_sample=True
    )
    generated_text = tokenizer.decode(output[0], skip_special_tokens=True)
    return generated_text

prompt = "User: [Name]: John [Age]: 25 [City]: New York,User: [Name]: Alice [Age]: 30 [City]: San Francisco,User: [Name]: Bob [Age]: 22 [City]: Los Angeles"
generated_text = generate_text(prompt, max_length=120)
print(generated_text)

x = generated_text.split(',')

x

x.pop(7)

x



import re
pattern = r"User: \[Name\]: ([\w\s]+) \[Age\]: (\d+) \[City\]: ([\w\s]+)"
matches = re.findall(pattern,generated_text)

df = pd.DataFrame(matches, columns=["Name", "Age", "City"])

# Converting columns to appropriate data types
df["Age"] = df["Age"].astype(int)

df

