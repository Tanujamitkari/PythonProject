import operations


def operation():
    print("########################")
    print("  PYTHON CALCULATOR PROJECT   ")
    print("########################")
    print("")
    print("Select Operation")
    print("1 - Add")
    print("2 - Subtract")
    print("3 - Multiply")
    print("4 - Divide")
    print("")
    print("#######################")
    print("")
    next_cal = "y"
    while next_cal == "y":
        try:
            operation_input = int(input("Enter integer 1-4 (1/2/3/4):"))
            if operation_input > 4 or operation_input < 1:
                print("enter a valid integer 1-4")
                continue
        except ValueError:
            print("please enter a valid integer 1-4")
            continue
        first_num = int(input("Enter first number:"))
        sec_num = int(input("Enter second number:"))
        operations.actual_operation(operation_input, first_num, sec_num)
        next_cal = input("Let's do next calculation? (y/n):")


if __name__=="__main__":
    operation()