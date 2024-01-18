"""
Using PIL for Python and docstrings and OOP:

33. Write a vertex shader that takes as input an angle and an axis of rotation and rotates
vertices about this axis.
"""

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

vertex_shader = """
#version 330 core

layout(location = 0) in vec3 in_position;
uniform float angle;
uniform vec3 axis;

void main()
{
    mat3 rotation_matrix = mat3(
        cos(angle) + (1.0 - cos(angle)) * axis.x * axis.x,
        (1.0 - cos(angle)) * axis.x * axis.y - sin(angle) * axis.z,
        (1.0 - cos(angle)) * axis.x * axis.z + sin(angle) * axis.y,

        (1.0 - cos(angle)) * axis.y * axis.x + sin(angle) * axis.z,
        cos(angle) + (1.0 - cos(angle)) * axis.y * axis.y,
        (1.0 - cos(angle)) * axis.y * axis.z - sin(angle) * axis.x,

        (1.0 - cos(angle)) * axis.z * axis.x - sin(angle) * axis.y,
        (1.0 - cos(angle)) * axis.z * axis.y + sin(angle) * axis.x,
        cos(angle) + (1.0 - cos(angle)) * axis.z * axis.z
    );

    vec3 rotated_position = rotation_matrix * in_position;
    gl_Position = vec4(rotated_position, 1.0);
}
"""

def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glutSwapBuffers()

def main():
    glutInit()
    glutCreateWindow("Vertex Shader Example")
    glutDisplayFunc(display)
    glEnable(GL_DEPTH_TEST)

    # Compile and use the vertex shader
    vertex_shader_id = glCreateShader(GL_VERTEX_SHADER)
    glShaderSource(vertex_shader_id, vertex_shader)
    glCompileShader(vertex_shader_id)

    program_id = glCreateProgram()
    glAttachShader(program_id, vertex_shader_id)
    glLinkProgram(program_id)
    glUseProgram(program_id)

    # Set uniform values (angle and axis of rotation)
    angle_location = glGetUniformLocation(program_id, "angle")
    glUniform1f(angle_location, 0.5)  # Set the rotation angle

    axis_location = glGetUniformLocation(program_id, "axis")
    glUniform3f(axis_location, 1.0, 0.0, 0.0)  # Set the rotation axis (e.g., x-axis)

    glutMainLoop()

if __name__ == "__main__":
    main()
