# Messages Agents exchanges one another
from dataclasses import dataclass, field
from datetime import datetime

@dataclass
class Message:
    sender: str     
    content: str
    timestamp: str = field(
         default_factory=lambda: datetime.now().strftime("%H:%M:%S")
    )

    def __str__(self):
        return f"[{self.timestamp}] {self.sender}: {self.content}"