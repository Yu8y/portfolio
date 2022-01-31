#y = 3x + 1 PROBLEM
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime

start_time = datetime.now()
x = int(input("Please pick any (a long 89565456212) number: "))
input = x

try:
    if int(x):
        print(f"({x}), Good choice!")
except:
    print(f"Please enter a valid number ({x}), restart the program")
    quit()

listwithresults = []

for i in range(1000):
    if x % 2 == 0:
        x = x / 2
        print(x)
        listwithresults.append(int(x))
    elif x == 1:
        print(f"X equals ({x}). We are in a loop, time to break")
        break
    else:
        x = (x*3) + 1
        print(x)
        listwithresults.append(int(x))
run_time = datetime.now()
end_time = run_time - start_time
print(f"There were {len(listwithresults)} moves before infinite loop was reached")
#print(listwithresults)
print(f"3x + 1 runtime for ({input}) input is: {end_time} ")
print("")
print("")
print("Time to see our results on a graph")

# Create a figure containing a single axes.
fig, ax = plt.subplots()
numpyarray = np.array(listwithresults)
print(numpyarray)

ax.plot(numpyarray)
plt.title(f"Graph for input: {input}")
plt.show()
