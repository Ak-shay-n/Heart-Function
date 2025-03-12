import numpy as np
import matplotlib.pyplot as plt

class HeartPlot:
    #Class to generate and plot a heart shape using parametric equations
    def __init__(self, points=1000):
        #Initializes the HeartPlot class
        self.points = points
        self.x, self.y = self._generate_heart_curve()

    def _generate_heart_curve(self):
        #Generates x and y coordinates that form the heart shape
        #Returns a tuple containing x and y coordinates
        t = np.linspace(0, 2 * np.pi, self.points)  #Creates an array of values from 0 to 2π
        x = 16 * np.sin(t)**3  #Heart curve x-coordinates using sine function
        y = 13 * np.cos(t) - 5 * np.cos(2*t) - 2 * np.cos(3*t) - np.cos(4*t)  #Heart curve y-coordinates
        return x, y

    def plot(self):
        #Plots the heart shape outline on a graph
        fig, ax = plt.subplots(figsize=(6, 6))  #Creates a figure and axis with equal size
        ax.plot(self.x, self.y, color='red', linewidth=2, label="Heart Outline")  # Plots the heart curve
        ax.axhline(0, color='black', linewidth=0.5)  # Draws a horizontal reference line
        ax.axvline(0, color='black', linewidth=0.5)  # Draws a vertical reference line
        ax.grid(True, linestyle='--', linewidth=0.5)  # Enables grid with dashed lines
        ax.legend()  # Displays the legend
        ax.set_title("Heart Shape Outline")  # Sets title for the graph
        ax.set_xlabel("X-axis")  # Label for X-axis
        ax.set_ylabel("Y-axis")  # Label for Y-axis
        plt.show()  # Renders the plot

# Creating an instance of the HeartPlot class and plotting the heart
if __name__ == "__main__":
    heart_plot = HeartPlot()
    heart_plot.plot()
