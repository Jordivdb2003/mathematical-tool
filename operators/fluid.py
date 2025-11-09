from operators.node import Node

class Fluid(Node):
    def __init__(self, *args):
        self.children = [arg for arg in args]

        