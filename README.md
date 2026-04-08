---
title: Github Triage Env
emoji: 🤖
colorFrom: green
colorTo: blue
sdk: docker
pinned: false
---

# 🚀 GitHub Triage OpenEnv

A custom environment for training and evaluating AI agents on software maintenance tasks.

### 📂 Key Files (Project Structure)
1.  **[Dockerfile](./Dockerfile)**: The environment configuration and build instructions.
2.  **[inference.py](./inference.py)**: The main entry point for the agent (compliant with OpenEnv logs).
3.  **[app.py](./app.py)**: The FastAPI server hosting the environment logic.
4.  **[openenv.yaml](./openenv.yaml)**: Specification compliance file.

## 🛠️ Setup
The environment is containerized and hosted live on Hugging Face Spaces.

**Live API:** https://huggingface.co/spaces/AayushiPriya/github-triage-env
