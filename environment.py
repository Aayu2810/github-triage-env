class GitHubEnv:
    def __init__(self):
        self.tasks = {
            "easy": {"id": 1, "title": "Crash on start", "body": "App dies immediately.", "target": "bug"},
            "medium": {"id": 2, "title": "Feature request", "body": "Add dark mode.", "target": "enhancement"},
            "hard": {"id": 3, "title": "Duplicate of #1", "body": "Login fails.", "target": "duplicate"}
        }
        self.state = {}
        self.current_task = "easy"

    def reset(self, task_level="easy"):
        self.current_task = task_level
        self.state = {"labels": [], "comments": [], "is_open": True, "steps": 0}
        return self._get_obs()

    def _get_obs(self):
        t = self.tasks[self.current_task]
        return {**t, "current_labels": self.state["labels"], "comments": self.state["comments"], "is_open": self.state["is_open"]}

    def step(self, action):
        self.state["steps"] += 1
        reward = 0.0
        # Logic for rewarding correct label
        if action.get("label") == self.tasks[self.current_task]["target"]:
            reward = 1.0
        
        if action["action_type"] == "add_label":
            self.state["labels"].append(action["label"])
        elif action["action_type"] == "close_issue":
            self.state["is_open"] = False
            
        done = self.state["steps"] >= 5 or not self.state["is_open"]
        return self._get_obs(), reward, done, {}
