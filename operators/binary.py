from operators.node import Node
from typing import Optional

class Binary(Node):
    def __init__(self, left: Optional[Node] = None, right: Optional[Node] = None):
        super().__init__(left, right)
