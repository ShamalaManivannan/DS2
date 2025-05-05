import numpy as np

def linear_eqn(x):
    y=(2*x)+3
    print(y)

def quadratic_eqn(X):
    a=(x**2)+x+3
    print(a)

type = input("What type of equation do you want(1=Linear , 2=Quadratic)")

if type == "1":
    x=np.array([1,2,3,4,5,6,7,8,9,10])
    linear_eqn(x)
elif type == "2":
    x=np.array([1,2,3,4,5,6,7,8,9,10])
    quadratic_eqn(x)
else:
    print("Invalid choice, pick 1 or 2")