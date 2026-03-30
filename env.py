import json
import random
import os
from typing import Tuple
from fastapi import FastAPI
from models import Observation, Action, Reward

app = FastAPI()

class GenomicCuratorEnv:
    def __init__(self, data_path="variants_db.jsonl"):
        with open(data_path, 'r') as f:
            self.db = [json.loads(line) for line in f]
        self.current_protein = None
        self.current_variant = None
        self.tool_outputs = {}
        self.step_count = 0

    def reset(self) -> Observation:
        self.current_protein = random.choice(self.db)
        self.current_variant = random.choice(self.current_protein['variants'])
        self.tool_outputs = {}
        self.step_count = 0
        return self._get_obs()

    def _get_obs(self) -> Observation:
        return Observation(
            gene_symbol=self.current_protein['gene'],
            protein_accession=self.current_protein['accession'],
            variant_description=f"p.{self.current_variant['orig']}{self.current_variant['pos']}{self.current_variant['alt']}",
            tool_outputs=self.tool_outputs,
            step_count=self.step_count
        )

    def step(self, action: Action) -> Tuple[Observation, Reward, bool]:
        self.step_count += 1
        done = False
        reward_score = 0.0
        feedback = ""
        if action.tool_name == "query_function":
            self.tool_outputs["function"] = self.current_protein.get('function', "No data.")
            feedback = "Retrieved functional data."
        elif action.tool_name == "submit_classification":
            done = True
            if action.label_prediction == self.current_variant['label']:
                reward_score = 1.0
                feedback = "Correct."
            else:
                feedback = f"Incorrect. Correct was {self.current_variant['label']}."        
        return self._get_obs(), Reward(score=reward_score, feedback=feedback), done
genome_env = GenomicCuratorEnv()

@app.get("/")
def health(): return {"status": "ready"}

@app.post("/reset")
def reset(): return genome_env.reset()

@app.post("/step")
def step(action: Action):
    obs, rew, done = genome_env.step(action)
    return {"observation": obs, "reward": rew, "done": done}