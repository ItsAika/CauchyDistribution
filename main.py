import matplotlib.pyplot as plt
import math
import random as rand
import matplotlib.animation as animation

gamma = 1
x_nought = 0
threshold = 10
nbBox = 300
nbIteration = 10
func = list()
itTtl = 100

gay = ['r','g','b','c','m','y','purple','orange']


def f(x):
    return (1 / ((math.pi * gamma) * (1 + pow(((x - x_nought) / gamma), 2.0))))

for i in range(-1000,1000):
    func.append(f(i/100))

"""print(func)
plt.plot(func)
plt.show()
"""
boxList = list()
for i in range(0,nbBox):
    boxList.append(0)

fig, ax = plt.subplots(1, 1, figsize=(9, 3), sharey=True)

def animate(cti):
   ax.clear()
   for i in range(0, nbIteration):
       temp = rand.uniform(0, 1)
       x_trial = x_nought + gamma * math.tan(math.pi * (temp - 0.5));
       if x_trial > -threshold and x_trial < threshold:
           qlbox = math.floor(((x_trial + threshold) * nbBox) / (2 * threshold))
           # print("qd " + str(qlbox) + " " + str(x_trial))
           boxList[qlbox] += 1
       else:
           pass
   names = list()
   for i in range(nbBox):
       names.append(i)
   if cti >= itTtl:
       exit()
   ax.bar(names, boxList, color=gay[rand.randint(0,len(gay)-1)])



ani = animation.FuncAnimation(fig, animate, 1, interval=1, blit=False)
plt.show()
#print(boxList)


