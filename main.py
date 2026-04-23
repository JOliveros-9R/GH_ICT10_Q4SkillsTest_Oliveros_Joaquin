from pyscript import display, document  
import numpy as np
import matplotlib.pyplot as plt
import logging


logging.getLogger('matplotlib').setLevel(logging.ERROR)

plt.figure()
plt.plot([0, 1], [0, 1])
plt.close()


months = np.array(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
absences = np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0])

def attendance_graph(e):
    months_index = int(document.getElementById('AttendanceDropdown').value)
    absences_num = int(document.getElementById('input2').value)

    absences[months_index] += absences_num

    fig, ax = plt.subplots()
    ax.plot(months, absences, marker='o', color='blue')

    ax.set_title("Attendance Tracker")
    ax.set_xlabel('Months')
    ax.set_ylabel('Absences')
    ax.grid(linestyle='-', alpha=0.5)

    output = document.getElementById('output')
    output.innerHTML = ""
    display(fig, target="output")
