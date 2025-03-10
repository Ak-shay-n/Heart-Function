import numpy as np
import matplotlib.pyplot as plt

class HeartPlot:
    """class to generate and plot a heart shape using parametric equations"""

    def __init__(self, points=1000):
        """
        initializes the heartPlot class
        no of points to generate for the heart curve
        """
        self.points = points
        self.x, self.y = self._generate_heart_curve()

    def _generate_heart_curve(self):
        """
        this generates x and y coordinates for the heart shape
        return tuple containing x and y coordinates
        """
        t = np.linspace(0, 2 * np.pi, self.points)  # Creates an array of values from 0 to 2π
        x = 16 * np.sin(t)**3  # Heart curve x-coordinates using sine function
        y = 13 * np.cos(t) - 5 * np.cos(2*t) - 2 * np.cos(3*t) - np.cos(4*t)  # Heart curve y-coordinates
        return x, y

    def plot(self):
        """
        plots the heart shape outline on a graph
        """
        fig, ax = plt.subplots(figsize=(6, 6))  # Create a figure and an axis with equal size
        ax.plot(self.x, self.y, color='red', linewidth=2, label="Heart Outline")  # Plot the heart curve
        ax.axhline(0, color='black', linewidth=0.5)  # Draw a horizontal reference line
        ax.axvline(0, color='black', linewidth=0.5)  # Draw a vertical reference line
        ax.grid(True, linestyle='--', linewidth=0.5)  # Enable grid with dashed lines
        ax.legend()  # Display legend
        ax.set_title("Heart Shape Outline")  # Set title for the graph
        ax.set_xlabel("X-axis")  # Label for X-axis
        ax.set_ylabel("Y-axis")  # Label for Y-axis
        plt.show()  # Render the plot

# Creating an instance of the HeartPlot class and plotting the heart
heart_plot = HeartPlot()
heart_plot.plot()
