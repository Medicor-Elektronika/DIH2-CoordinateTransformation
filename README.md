# MediSCARA Robotic Transformation Calculator (MRTC)
This easy-to-use Python program allows 3D coordinate transformations for robotic manufacturing of incubator canopies.

The software was codeveloped with HSMa.

## Setup
No setup operation is needed, just open a console on a PC with the requirements preinstalled and run the following:
```
python3 main.py
```

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

## License

>MIT License
>
>Copyright (c) 2022 MEDICOR Elektronika Zrt.
>
>Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

>The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

>THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
