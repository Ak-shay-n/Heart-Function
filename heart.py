import numpy as np
import matplotlib.pyplot as plt

class HeartPlot:
    #class to generate and plot a heart shape using parametric equations
    def __init__(self, points=1000):
        #initializes the HeartPlot class
        self.points = points
        self.x, self.y = self._generate_heart_curve()
    def _generate_heart_curve(self):
        #generates x and y coordinates that form the heart shape
        #returns a tuple containing x and y coordinates
        t = np.linspace(0, 2 * np.pi, self.points)  #creates an array of values from 0 to 2π
        x = 16 * np.sin(t)**3  #heart curve x-coordinates using sine function
        y = 13 * np.cos(t) - 5 * np.cos(2*t) - 2 * np.cos(3*t) - np.cos(4*t)  #heart curve y-coordinates
        return x, y

    def plot(self): #plots the heart shape outline on a graph
        fig, ax = plt.subplots(figsize=(6, 6))  #creates a figure and axis with equal size
        ax.plot(self.x, self.y, color='red', linewidth=2, label="Heart Outline")  #plots the heart curve
        ax.axhline(0, color='black', linewidth=0.5)  #draws a horizontal reference line
        ax.axvline(0, color='black', linewidth=0.5)  #draws a vertical reference line
        ax.grid(True, linestyle='--', linewidth=0.5)  #enables grid with dashed lines
        ax.legend()  #displays the legend
        ax.set_title("Heart Shape Outline")  #sets title for the graph
        ax.set_xlabel("X-axis")  #label for X-axis
        ax.set_ylabel("Y-axis")  #label for Y-axis
        plt.show()  #renders the plot

#creating an instance of the heartPlot class and plotting the heart
if __name__ == "__main__":
    heart_plot = HeartPlot()
    heart_plot.plot()
