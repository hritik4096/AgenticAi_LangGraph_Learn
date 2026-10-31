#so now we are creating a graph
#and the first thing u create is a state

import os


#1) typed DICT(Most Common approach)

from typing import TypedDict

class State(TypedDict):
    topic: str
    summary: str
    score: int



#2) pydantic approach
# it is good at data validation and type checking at run time

from pydantic import BaseModel,field_validator


class State(BaseModel):
    topic: str
    summary: str=""
    score: int

    @field_validator("score")
    def score_positive(cls, value):
         if value < 0:
                raise ValueError("Score must be a positive integer")

         

#3) python dataclass approach
# it is good for simple data structures and less boilerplate code   
# it is used very rarly

from dataclasses import dataclass, field

@dataclass
class State:
    topic: str
    summary: str = ""
    messages: list = field(default_factory=list)



from langgraph.graph import MessagesState

class State(MessagesState):
     #messages field is already included with add_messages reducer
     #just add your extra fields here
     user_name: str
     language: str = "en"


 
