import matplotlib.pyplot as plt
def collatz(x):
    a = [x]
    while x != 1:
        if x % 2 == 0:
            x = x/2
        else:
            x = 3*x + 1
        a.append(x)
    return(a)
x=[]
y=[]
for i in range(1,10000):
    a = collatz(i)
    x.append(i)
    y.append(len(a))
plt.bar(x,y,color='maroon',width=0.4)
plt.show()
