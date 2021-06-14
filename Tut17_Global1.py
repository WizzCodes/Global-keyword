l=10            #Global (scope)
def function1(n):
     l=5            #Local
     m=25
     print(l, m)
     print(n, "Print the value")

function1("This is the value")
print(l)
