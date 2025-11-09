from operators.node import Node

class Variable(Node):
    def __init__(self, value: str):
        self.value = value

    def __str__(self) -> str:
        return self.value