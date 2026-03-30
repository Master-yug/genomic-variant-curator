import os
import json
from openai import OpenAI
from env import genome_env 
from models import Action

API_BASE_URL = os.getenv("API_BASE_URL")
MODEL_NAME = os.getenv("MODEL_NAME")
HF_TOKEN = os.getenv("HF_TOKEN")

client = OpenAI(base_url=API_BASE_URL, api_key=HF_TOKEN)

def run_inference():
    for _ in range(3):
        obs = genome_env.reset()
        done = False
        while not done:
            prompt = f"Identify if this variant is pathogenic or benign. Gene: {obs.gene_symbol}. Variant: {obs.variant_description}. Functional Data: {obs.tool_outputs}. Return JSON with 'tool_name' and 'label_prediction'."            
            response = client.chat.completions.create(
                model=MODEL_NAME,
                messages=[{"role": "user", "content": prompt}],
                response_format={"type": "json_object"}
            )            
            action_dict = json.loads(response.choices[0].message.content)
            action = Action(**action_dict)
            obs, reward, done = genome_env.step(action)            
        print(f"Final Reward: {reward.score}")

if __name__ == "__main__":
    run_inference()