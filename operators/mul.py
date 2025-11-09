from operators.fluid import Fluid

class Mul(Fluid):
    def __str__(self) -> str:
        from operators.constant import Constant
        from operators.variable import Variable

        string = []

        for child in self.children:
            if isinstance(child, (Constant, Variable)):
                string.append(f"{child.__str__()}")
            else:
                string.append(f"({child.__str__()})")
        
        return " * ".join(string)