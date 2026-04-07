import requests
import sys

BASE_URL = "http://localhost:8000"
TASKS = ["easy", "medium", "hard"]

def run_eval():
    total_score = 0
    print("\n=== OpenEnv Baseline Evaluation ===")
    
    for task in TASKS:
        try:
            # 1. Reset
            reset_url = f"{BASE_URL}/reset?task_level={task}"
            reset_res = requests.post(reset_url)
            reset_res.raise_for_status()
            obs = reset_res.json()
            
            # Extract target and ID
            target = obs.get("target")
            issue_id = obs.get("id") or obs.get("issue_id")
            
            # 2. Step
            action = {
                "action_type": "add_label",
                "issue_id": issue_id,
                "label": target
            }
            step_res = requests.post(f"{BASE_URL}/step", json=action)
            step_res.raise_for_status()
            res = step_res.json()
            
            score = res.get("reward", 0.0)
            total_score += score
            print(f"Task: {task:7} | Status: Success | Score: {score}")
        except Exception as e:
            print(f"Task: {task:7} | Status: FAILED  | Error: {e}")

    print("-----------------------------------")
    print(f"FINAL MEAN SCORE: {total_score / len(TASKS):.2f}\n")

if __name__ == "__main__":
    run_eval()
