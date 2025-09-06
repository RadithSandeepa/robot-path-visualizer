# Robot Path Visualizer (Pygame)

This project demonstrates a tiny Python app that replays a precomputed robot trajectory `(x, y, θ)` using **Pygame** and **NumPy**. It rotates a robot sprite along the path and draws a trail, handy for quick demos and visual debugging of differential-drive motion.

## Summary
- Loads `simulationData.npy` → shape **(N, 3)** as columns: **x**, **y**, **theta_rad**.
- Converts `theta` (radians) to degrees for sprite rotation.
- Animates `robotImage.png` (50×50) across a `1200×800` window.
- Draws a yellow polyline trail of visited points.

## Files
- differential_robot.py → Generates simulationData.npy using a diff-drive ODE model + quick plots
- simulation_DDRobot.py → Visualizes the saved trajectory with Pygame (rotating sprite + trail)
- simulationData.npy → Generated trajectory file (created by differential_robot.py)
- robotImage.png → Robot sprite (will be scaled to 50x50)
- README.md

## What it does
### 1) `differential_robot.py` - Simulation
- Defines robot params: wheel radius `r` and wheelbase `s`.
- Sets wheel angular velocities `ΔL(t)` and `ΔR(t)`.
- Simulates the kinematics with SciPy ``` `odeint`:
  \[
  \dot{x} = \frac{r}{2}\cos(\theta)\,(\Delta_R + \Delta_L) \quad
  \dot{y} = \frac{r}{2}\sin(\theta)\,(\Delta_R + \Delta_L) \quad
  \dot{\theta} = \frac{r}{s}(\Delta_R - \Delta_L)
  \]```
- Saves the result to **`simulationData.npy`** with shape `(N, 3)` = `[x, y, theta]` (theta in **radians**).
- Shows quick Matplotlib plots for sanity-check.

### 2) `simulation_DDRobot.py` - Visualization
- Opens a `1200×800` Pygame window.
- Loads `simulationData.npy`, converts `theta` to degrees (and flips sign for Pygame’s rotation).
- Draws `robotImage.png` at `(x[i], y[i])` with correct rotation and a yellow path trail.

> **Coordinate system:** Pygame’s origin is top-left, **y increases downward**.  
> If you want a math-style y-up view, pre-flip `y` in your data before saving.

## Screenshots

![Run1](https://github.com/RadithSandeepa/robot-path-visualizer/blob/main/Images/Img_1.png)

![Run2](https://github.com/RadithSandeepa/robot-path-visualizer/blob/main/Images/Img_2.png)

## Requirements
```bash
python -m pip install -r requirements.txt
```

- NumPy, SciPy, Matplotlib, Pygame

## Run
1) Generate the trajectory

```bash
python differential_robot.py
```
- This creates simulationData.npy and shows plots.

2) Visualize the trajectory

```bash
python simulation_DDRobot.py
```
- Make sure robotImage.png is in the same folder.

## Data Format
### simulationData.npy: NumPy array with shape (N, 3)
- Column 0 → x (pixels)
- Column 1 → y (pixels)
- Column 2 → theta (radians)

![Diagram](https://github.com/RadithSandeepa/robot-path-visualizer/blob/main/Images/Img_3.png)
