
from featurelib import optimize, feature, endpoint

class A(feature):
    def method1(self):
        print('OK')

class B(feature):
    def method2(self):
        print('OK2')

class C(*optimize(A, B), endpoint=True):
    def x(self):
        self.method1()

    def __init__(self) -> None: pass