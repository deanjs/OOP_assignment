# Resotre the history of the conversation
from dataclasses import dataclass, field
from core.message import Message

@dataclass
class Memory:
    agent_name: str
    history: list[Message] = field(default_factory=list)

    # add the new message in the history
    def add(self, message: Message) -> None:
        self.history.append(message)

    # get the n numbers of the recent messages
    def get_recent(self, n: int) -> list[Message]:
        return self.history[-n:]
    
    # clear the history
    def clear(self) ->None:
        self.history.clear()

    # return the len of the message
    def __len__(self):
        return len(self.history)