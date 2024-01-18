Question six
============
How are curves like the B ́ezier curve and the B-spline curve useful? 2 Marks. Give an
application where a curve can be used as a reference. Write a program to carry out
subdivision of triangular or quadrilateral meshes. When the subdivision is working
correctly, add the averaging step to form a smoother surface.

1. Bezier Curve and B-spline Curve Utility (1 mark): Both Bézier curves and B-spline curves are widely used in computer graphics and computer-aided design. They provide a flexible and intuitive way to represent and manipulate curves and surfaces, making them valuable in various applications.

2. Application Example (1 mark): One application where curves can be used as a reference is in computer-aided design (CAD). In CAD systems, Bézier curves and B-spline curves are often employed to model and represent shapes of objects. Designers can control the shape of curves by adjusting control points, allowing for precise and smooth curve manipulation. This is crucial in designing anything from automotive parts to consumer products.

MeshSubdivision Class
---------------------

.. py:class:: MeshSubdivision

   The MeshSubdivision class provides functionality for generating, subdividing, and visualizing triangular meshes using the Python Imaging Library (PIL).

   :ivar int width: Width of the image.
   :ivar int height: Height of the image.
   :ivar int num_iterations: Number of subdivision iterations.
   :ivar Image image: Image object.
   :ivar ImageDraw.Draw draw: Drawing object for the image.

   .. method:: __init__(width, height, num_iterations)

      Initialize the MeshSubdivision object.

      :param int width: Width of the image.
      :param int height: Height of the image.
      :param int num_iterations: Number of subdivision iterations.

   .. method:: generate_random_mesh(num_points, num_triangles)

      Generate a random triangular mesh.

      :param int num_points: Number of mesh points.
      :param int num_triangles: Number of triangles in the mesh.

      :returns: List of points and triangles forming the mesh.

   .. method:: draw_mesh(points, triangles)

      Draw the triangular mesh.

      :param list points: List of points.
      :param list triangles: List of triangles represented by point indices.

      :returns: None

   .. method:: subdivide_mesh(points, triangles)

      Subdivide the triangular mesh.

      :param list points: List of points.
      :param list triangles: List of triangles represented by point indices.

      :returns: List of points and triangles after subdivision.

   .. method:: average_mesh(points, triangles)

      Average the mesh to form a smoother surface.

      :param list points: List of points.
      :param list triangles: List of triangles represented by point indices.

      :returns: List of points and triangles after averaging.

   .. method:: save_image(filename)

      Save the image.

      :param str filename: Filename to save the image.

      :returns: None

