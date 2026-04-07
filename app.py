from fastapi import FastAPI
from models import Action
from environment import GitHubEnv

app = FastAPI()
env = GitHubEnv()

@app.post("/reset")
def reset(task_level: str = "easy"):
    return env.reset(task_level)

@app.post("/step")
def step(action: Action):
    obs, reward, done, info = env.step(action.dict())
    return {"observation": obs, "reward": reward, "done": done}

@app.get("/state")
def state():
    return env._get_obs()
