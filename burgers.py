from manim import *
import numpy as np

"""
Visualization of the Burgers' equation using Manim.

Burgers' equation is a fundamental partial differential equation (PDE) from fluid mechanics:
    du/dt + u * du/dx = nu * d^2u/dx^2

Where:
    u is the velocity field.
    nu (v) is the kinematic viscosity.

This script simulates the time evolution of the Burgers' equation using a simple finite difference method.
"""

class BurgersEquation(Scene):
    def construct(self):
        # Parameters for the simulation
        nu = 0.1  # Viscosity coefficient
        L = 10    # Length of the spatial domain
        T = 5     # Total time for the simulation
        dt = 0.01 # Time step
        dx = 0.1  # Spatial step size
        x = np.arange(-L, L, dx)  # Discretized spatial domain
        nx = len(x)  # Number of spatial points

        # Initial condition: a combination of Gaussian functions
        u = np.e**(-((x-1)**2)/2) - np.e**(-((x+1)**2)/2)

        # Create the coordinate axes for plotting
        graph = Axes(
            x_range=[-L, L, 1],     # X-axis range and tick interval
            y_range=[-1.5, 1.5, 0.5],  # Y-axis range and tick interval
            axis_config={"color": BLUE},  # Color of the axes
        )

        # Create initial curve based on the initial condition
        curve = graph.plot(lambda x_val: np.interp(x_val, x, u), color=YELLOW)

        # Create the differential equation text and position it in the top-left corner
        equation = Tex(r"$\frac{\partial u}{\partial t} + u \frac{\partial u}{\partial x} = \nu \frac{\partial^2 u}{\partial x^2}$")
        equation.to_corner(UP + LEFT)  # Position the equation at the top left

        # Animate the creation of the graph and initial curve over 3 seconds
        self.play(Create(graph), Create(curve), run_time=3)
        # Animate the writing of the differential equation text
        self.play(Write(equation))  

        # Array to store the updated values of u
        u_new = np.zeros(nx)

        # Time-stepping loop to update the solution over time
        for t in np.arange(0, T, dt):
            # Update the values of u at each spatial point using finite differences
            for i in range(1, nx - 1):
                u_new[i] = u[i] - (dt / dx) * u[i] * (u[i] - u[i-1]) + \
                            (nu * dt / dx**2) * (u[i+1] - 2 * u[i] + u[i-1])

            # Create a new curve using interpolation for smooth transitions
            new_curve = graph.plot(lambda x_val: np.interp(x_val, x, u_new), color=YELLOW)
            # Animate the transition from the current curve to the new curve
            self.play(Transform(curve, new_curve), run_time=dt)
            # Update u for the next iteration
            u = u_new.copy()

        # Hold the final frame to allow the viewer to observe the last state of the simulation
        self.wait()
