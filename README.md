# Incubator Canopy Coordinate Transformation
This easy-to-use Python program allows 3D coordinate transformations for robotic manufacturing of incubator canopies.

## Inputs and outputs
As input the program GUI only needs translation and orientation of the pneumatic gripper with the gripper width and the fixed laser translational point with focus length. Given the input coordinates, the program calculates the coordinates and orientation of all 7 sides of the canopy, which can then be used for the industrial robot’s gripper control points.

![Coordinate transform GUI](/coordtransf_gui.png)

## Requirements
Tested software versions mentioned:
```
Python 3.x
Tkinter 8.6
Pillow 9.1.0
Numpy 1.21.0
```
