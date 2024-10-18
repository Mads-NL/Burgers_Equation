# Burgers' Equation Visualization with Manim

A visualization of **Burgers' equation** using the [Manim](https://www.manim.community/) library. Burgers' equation is a fundamental partial differential equation in fluid mechanics that combines convection and diffusion:

$$
\frac{\partial u}{\partial t} + u \frac{\partial u}{\partial x} = \nu \frac{\partial^2 u}{\partial x^2}
$$

Where:
- \( u \) is the velocity field.
- \( \nu \) (nu) is the kinematic viscosity.

This animation shows how the initial condition evolves over time, demonstrating the balance between non-linear convection and diffusion effects.

## Example

Check out the animation in action:

[![Burgers' Equation Visualization](https://img.youtube.com/vi/GrWS6cPNonQ/0.jpg)](https://youtu.be/GrWS6cPNonQ)

Click the image above to watch the animation on YouTube.

## Overview

- **Initial Condition**: A combination of two Gaussian curves.
- **Visualization**: Animates the solution over time using numerical methods.
- **LaTeX Support**: Displays the differential equation on the top-left of the animation.

## About the Project

This project is a personal exploration of numerical methods and fluid dynamics, visualized using Manim. It aims to provide an intuitive look at how solutions to Burgers' equation evolve over time.