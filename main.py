def operation():
    print("########################")
    print("   PYTHON CALCULATOR    ")
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
    next_cal="y"
    while next_cal=="y":
        operation_input=int(input("Enter Operation(1/2/3/4):"))
        first_num=int(input("Enter first number:"))
        sec_num=int(input("Enter second number:"))
        if operation_input==1:
            out=first_num+sec_num
            print(f"{first_num} + {sec_num} = {out}")
        elif operation_input==2:
            out = first_num - sec_num
            print(f"{first_num} - {sec_num} = {out}")
        elif operation_input==3:
            out = first_num * sec_num
            print(f"{first_num} * {sec_num} = {out}")
        elif operation_input==4:
            out = first_num / sec_num
            print(f"{first_num} / {sec_num} = {out}")
        next_cal=input("Let's do next calculation? (y/n):")




if __name__=="__main__":
    operation()