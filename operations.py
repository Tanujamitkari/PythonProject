def add(first_num, sec_num):
    out = first_num + sec_num
    return out


def sub(first_num, sec_num):
    out = first_num - sec_num
    return out


def mul(first_num, sec_num):
    out = first_num * sec_num
    return out


def div(first_num, sec_num):
    out = first_num / sec_num
    return out


def actual_operation(operation_input,first_num, sec_num):
    if operation_input == 1:
        out = add(first_num, sec_num)
        print(f"{first_num} + {sec_num} = {out}")
    elif operation_input == 2:
        out = sub(first_num, sec_num)
        print(f"{first_num} - {sec_num} = {out}")
    elif operation_input == 3:
        out = mul(first_num, sec_num)
        print(f"{first_num} * {sec_num} = {out}")
    elif operation_input == 4:
        out = div(first_num, sec_num)
        print(f"{first_num} / {sec_num} = {out}")
