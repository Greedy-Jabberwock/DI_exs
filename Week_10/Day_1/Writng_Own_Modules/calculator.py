# import operators
# from operators import addOperator, divideOperator
# from operators import *
from Week_10.Day_1.Writng_Own_Modules.operators import addOperator as adder, divideOperator as divider


def main():
    # print(operators.addOperator(2, 4))
    # print(operators.divideOperator(9, 3))

    # print(addOperator(2, 4))
    # print(divideOperator(9, 3))

    print(adder(2, 4))
    print(divider(9, 3))

main()
