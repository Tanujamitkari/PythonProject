class Operations:
    def __init__(self, first_num, sec_num):
        self.first_num = first_num
        self.sec_num = sec_num

    def add(self):
        """
        this is add method
        """
        out = self.first_num + self.sec_num
        return out

    def sub(self):
        out = 0
        if self.first_num > self.sec_num:
            out = self.first_num - self.sec_num
        elif self.sec_num > self.first_num:
            out = self.sec_num - self.first_num
        return out

    def mul(self):
        out = self.first_num * self.sec_num
        return out

    def div(self):
        try:
            out = self.first_num / self.sec_num
        except ZeroDivisionError as e:
            print(f"division by zero is not allowed so exiting by returning error code -1:{e}")
            return -1
        return out

    def actual_operation(self, operation_input):
        """
        this is driver code
        """
        if operation_input == 1:
            out = self.add()
            print(f"{self.first_num} + {self.sec_num} = {out}")
        elif operation_input == 2:
            out = self.sub()
            print(f"{self.first_num} - {self.sec_num} = {out}")
        elif operation_input == 3:
            out = self.mul()
            print(f"{self.first_num} * {self.sec_num} = {out}")
        elif operation_input == 4:
            out = self.div()
            print(f"{self.first_num} / {self.sec_num} = {out}")




