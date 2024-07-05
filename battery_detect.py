import psutil
import tkinter as tk

# Function to fetch battery information
def get_battery_info():
    battery = psutil.sensors_battery()
    percent = battery.percent if battery is not None else "N/A"
    status = battery.power_plugged if battery is not None else "Unknown"
    return percent, status

# Function to update battery information in GUI
def update_battery_info():
    percent, status = get_battery_info()
    battery_level.config(text=f"Battery Level: {percent}%")
    battery_status.config(text=f"Status: {'Charging' if status else 'Discharging'}")
    root.after(1000, update_battery_info)  # Update every second

# Creating GUI
root = tk.Tk()
root.title("Battery Level Detector")

battery_frame = tk.Frame(root, padx=20, pady=20)
battery_frame.pack()

battery_level = tk.Label(battery_frame, font=("Arial", 18))
battery_level.pack()

battery_status = tk.Label(battery_frame, font=("Arial", 12))
battery_status.pack()

update_battery_info()

root.mainloop()
