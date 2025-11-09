from operators.binary import Binary

class Division(Binary):
    def __str__(self) -> str:
        return f"({self.children[0]}) / ({self.children[1]})"