import tkinter as tk
from tkinter import ttk
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Sample DataFrame
data = {'Category': ['A', 'B', 'C'], 'Values': [10, 20, 30]}
df = pd.DataFrame(data)

def plot_data():
    fig, ax = plt.subplots()
    ax.bar(df['Category'], df['Values'])
    ax.set_title('Bar Chart Example')

    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas.get_tk_widget().pack()
    canvas.draw()

root = tk.Tk()
root.title("Data Visualization")
ttk.Button(root, text="Plot Data", command=plot_data).pack()

root.mainloop()
