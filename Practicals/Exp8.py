class S:
    def __init__(self, s):
        self.var_s = s

    def dis(self):
        print(self.var_s, "I am Class God")

    def mod(self, s):
        self.var_s = s


class A(S):
    def __init__(self, s, a):
        self.var_a = a
        S.__init__(self, s)

    def dis(self):
        print(self.var_a, "I am Class A")
        S.dis(self)

    def mod(self, s,  a):
        S.mod(self, s)
        self.var_a = a


class B(S):
    def __init__(self, s, b):
        self.var_b = b
        S.__init__(self, s)

    def dis(self):
        print(self.var_b, "I am Class B")
        S.dis(self)

    def mod(self, s,  b):
        S.mod(self, s)
        self.var_b = b


class C(A, B):
    def __init__(self, s, a, b, c):
        A.__init__(self, s, a)
        B.__init__(self, s, b)
        self.var_c = c

    def dis(self):
        A.dis(self)
        B.dis(self)
        print(self.var_c, "I am Class C")

    def mod(self, s, a, b, c):
        A.mod(self, s, a)
        B.mod(self, s, b)
        self.var_c = c


obj = C("Harsh", "Om", "Kirtik", "Shrutam")
obj.dis()
obj.mod("Singh", "Waje", "Ganesan", "Tambe")
obj.dis()
