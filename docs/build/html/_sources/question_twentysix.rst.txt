Question Twenty Six
===================
The goal of this assignment is to introduce you to mesh representation,
curve/surface smoothing, and modeling. You will be creating a basic interactive
modeling program for generating smooth surfaces that allows a user to drag
vertices of a coarse control mesh in 3D while displaying an associated smooth
surface. You will be asked to implement aspects of both the user interface and the
subdivision algorithm, and finally use your program to construct several models.
Specifically, you will write a program that reads a set of triangle from a. ray file,
builds a "control" mesh from these triangles (shown in green above), and displays
it in a window using OpenGL. As the program executes, a user can subdivide the
control mesh (each press of the `S' key subdivides one level further) to produce a
smooth subdivision surface for display (shown in gray above). The user may also
drag vertices of the control mesh with the mouse while the corresponding finest
level of the subdivision surface is updated continuously in the display. To create the smooth surface, we will be implementing the Loop subdivision scheme.
