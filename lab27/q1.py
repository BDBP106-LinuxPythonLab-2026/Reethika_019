"""(1) Use the following data to
temps = np.arange(20, 71, 5)
activity = np.array([12, 20, 35, 52, 70, 85, 92, 78, 45, 18, 5]) #relative activity
1. Plot activity against temperature as a line with circle markers.
2. Find the optimum temperature with temps[np.argmax(activity)], not by reading
it off the data.
3. Mark it with a dashed vertical line (ax.axvline) and a text label pointing to the
peak using ax.annotate(). Your plot should show: a rise and fall with the peak, and
the label, at 50oC."""


#1
import numpy as np
import matplotlib.pyplot as plt
temps = np.arange(20, 71, 5)
activity = np.array([12, 20, 35, 52, 70, 85, 92, 78, 45, 18, 5])
plt.plot(temps, activity, marker='o', linestyle='-')
plt.xlabel('Temperature')
plt.ylabel('Relative Activity')
plt.title('Activity vs Temperature')
plt.show()

import numpy as np
import matplotlib.pyplot as plt
temps = np.arange(20, 71, 5)
activity = np.array([12, 20, 35, 52, 70, 85, 92, 78, 45, 18, 5])
fig, ax = plt.subplots()
ax.plot(temps, activity, marker='o', linestyle='-')
ax.set_title('Subquestion 1')
ax.set_xlabel('Temperature')
ax.set_ylabel('Relative Activity')
plt.show()


#2

import numpy as np
import matplotlib.pyplot as plt
temps = np.arange(20, 71, 5)
activity = np.array([12, 20, 35, 52, 70, 85, 92, 78, 45, 18, 5])
optimum_temp = temps[np.argmax(activity)]
print("Optimum Temperature:", optimum_temp)
fig, ax = plt.subplots()
ax.plot(temps, activity, marker='o', linestyle='-', color='tab:blue')
ax.set_title('Sub question 2')
ax.set_xlabel('Temperature')
ax.set_ylabel('Relative Activity')
plt.show()

#3

import numpy as np
import matplotlib.pyplot as plt
temps = np.arange(20, 71, 5)
activity = np.array([12, 20, 35, 52, 70, 85, 92, 78, 45, 18, 5])
optimum_temp = temps[np.argmax(activity)]
print("Optimum Temperature:", optimum_temp)
fig, ax = plt.subplots()
ax.plot(temps, activity, marker='o', linestyle='-', color='tab:blue')
ax.set_title('Activity vs Temperature')
ax.set_xlabel('Temperature')
ax.set_ylabel('Relative Activity')
ax.axvline(optimum_temp, color='black', linestyle='--')
ax.annotate('Optimum (50°C)', xy=(50, 92), xytext=(55, 80))
fig.savefig('plot.png')
plt.show()