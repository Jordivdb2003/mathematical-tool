from operators.binary import Binary

class Power(Binary):
    def __str__(self) -> str:
        from operators.constant import Constant
        from operators.variable import Variable

        result = ""

        if isinstance(self.children[0], (Constant, Variable)):
            result += f"{self.children[0].__str__()}"
        else:
            result += f"({self.children[0].__str__()})"
        
        result += " ^ "
        if isinstance(self.children[1], (Constant, Variable)):
            result += f"{self.children[1].__str__()}"
        else:
            result += f"({self.children[1].__str__()})"

        return result