import psutil
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Explicitly set the Matplotlib backend
matplotlib.use('MacOSX')  

# Function to get memory usage
def get_memory_usage():
    memory_info = psutil.virtual_memory()
    return memory_info.percent

# Function to update the plot
def update_plot(frame, y_data, line):
    y_data.append(get_memory_usage())
    if len(y_data) > 100:  # Keep only the last 100 data points
        y_data.pop(0)
    line.set_ydata(y_data)
    line.set_xdata(range(len(y_data)))
    ax.relim()
    ax.autoscale_view()
    return line,

# Setup the plot
fig, ax = plt.subplots()
y_data = [get_memory_usage()]
line, = ax.plot(y_data)
ax.set_ylim(0, 100)  # Memory usage in percentage
ax.set_xlim(0, 100)
ax.set_xlabel('Time')
ax.set_ylabel('Memory Usage (%)')
ax.set_title('Real-time Memory Usage')

# Start animation and assign to a variable to prevent garbage collection
ani = animation.FuncAnimation(fig, update_plot, 
fargs=(y_data, line), interval=1000, blit=False)

# Display the plot
plt.show()