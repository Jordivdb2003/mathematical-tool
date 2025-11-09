from operators.fluid import Fluid

class Plus(Fluid):
    def __str__(self) -> str:
        return " + ".join(str(child) for child in self.children)