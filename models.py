from pydantic import BaseModel, Field
from typing import List, Optional, Literal

class Action(BaseModel):
    action_type: Literal["add_label", "remove_label", "post_comment", "close_issue"]
    issue_id: int
    label: Optional[str] = None
    comment: Optional[str] = None

class Observation(BaseModel):
    issue_id: int
    title: str
    body: str
    current_labels: List[str]
    comments: List[str]
    is_open: bool

class Reward(BaseModel):
    value: float = Field(ge=0.0, le=1.0)
    feedback: str
