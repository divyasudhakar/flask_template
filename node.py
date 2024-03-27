from dataclasses import dataclass

# dataclass is entirely for serializing and pretty printing
# an object as a JSON object.
@dataclass
class Node:
  id: int
  title: str
  content: str

  def __init__(self, id, title, content):
    self.id = id
    self.title = title
    self.content = content
