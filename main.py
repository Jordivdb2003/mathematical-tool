


if __name__ == "__main__":
    from operators.node import Node
    from operators.constant import Constant
    from operators.variable import Variable
    from operators.plus import Plus
    from operators.mul import Mul   
    from operators.power import Power
    from operators.subtract import Subtract
    from operators.division import Division

    x = Variable("x")
    y = Variable("y")
    z = Variable("z")
    expression1 = Mul(x, Power(y, z))

    print(f"Expression 1: {expression1}")