# Autonomous Vehicle Obstacle Avoidance & Navigation (Webots Simulation)

## Overview
An algorithmic simulation project designed to model obstacle detection, reactive steering, and collision prevention logic for self-driving vehicles within a simulated multi-avenue environment. Developed for the Computational Thinking module (CMP4010) under the Cardiff Metropolitan University curriculum. Grade Achieved: 68% (Upper Second-Class Honours - 2:1).

## Key Features & Logic
- **Algorithmic Decomposition:** Modular implementation of sensory data collection, threshold evaluation, and motor velocity control loops.
- **Sensor-Driven Obstacle Avoidance:** Real-time distance measurement utilizing ultrasonic/distance sensor thresholds to steer the vehicle clear of barriers.
- **Trajectory Planning:** Reactive navigation algorithm ensuring dynamic vehicle alignment and collision-free path execution.

## Technologies & Environment
- **Programming Language:** Python 3
- **Simulation Platform:** Webots Robot Simulator (`.wbt`)
- **Key Concepts:** Computational Thinking, Reactive Robotics, Sensor Feedback Loops, Algorithm Optimization

## Repository Structure
- `new_controller_4.py` - Core Python controller implementing obstacle avoidance routines
- `Confirm.wbt` - Webots 3D simulation environment and world configuration
- `self-driving car project (1).pdf` - Complete analytical project report and methodology documentation

## How to Run the Simulation
1. Install [Webots Robot Simulator](https://cyberbotics.com/).
2. Open the simulation world file:
   ```bash
   Confirm.wbt
