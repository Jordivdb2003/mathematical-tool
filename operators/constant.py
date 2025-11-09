from operators.node import Node

class Constant(Node):
    def __init__(self, value: float):
        super().__init__()
        self.value = value

    def __str__(self) -> str:
        return str(self.value)