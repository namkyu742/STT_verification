# from datetime import datetime

# t = datetime.today().strftime("%Y-%m-%d_%H-%M-%S")
# print(t)


class A():
    def __init__(self, a, b):
        self.r_a = a
        self.r_b = b

        try:
            self.c = open("", "rt")
            print("!!!")
        except Exception as e:
            print("Exception :", e)

    def sum(self):
        return self.r_a + self.r_b



test = A(3, 5)

print(test.sum())