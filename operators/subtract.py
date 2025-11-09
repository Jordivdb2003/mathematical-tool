from operators.binary import Binary

class Subtract(Binary):
    def __str__(self) -> str:
        return f"{self.children[0].__str__()} - {self.children[1].__str__()}"