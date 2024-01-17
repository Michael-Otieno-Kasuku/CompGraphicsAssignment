"""
Using PIL for Python and docstrings and OOP:

37. Write a program using mipmaps in which each mipmap is constructed from a different
image. Is there a practical application for such a program?
"""

from PIL import Image
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

class MipmapProgram:
    def __init__(self, base_image_path, num_mipmaps):
        self.base_image = Image.open(base_image_path)
        self.num_mipmaps = num_mipmaps
        self.mipmaps = self.generate_mipmaps()

        glutInit()
        glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
        glutInitWindowSize(self.base_image.width, self.base_image.height)
        glutCreateWindow("Mipmap Example")

        glutDisplayFunc(self.display)
        glutReshapeFunc(self.reshape)
        self.setup()

    def generate_mipmaps(self):
        mipmaps = [self.base_image]
        width, height = self.base_image.size

        for i in range(1, self.num_mipmaps):
            width //= 2
            height //= 2
            mipmap = self.base_image.resize((width, height), Image.ANTIALIAS)
            mipmaps.append(mipmap)

        return mipmaps

    def setup(self):
        glEnable(GL_TEXTURE_2D)
        glGenTextures(1, self.texture_id)
        glBindTexture(GL_TEXTURE_2D, self.texture_id[0])

        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR_MIPMAP_LINEAR)
        gluBuild2DMipmaps(GL_TEXTURE_2D, GL_RGB, self.base_image.width, self.base_image.height,
                          GL_RGB, GL_UNSIGNED_BYTE, self.base_image.tobytes())

    def display(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glBegin(GL_QUADS)
        glTexCoord2f(0, 0)
        glVertex2f(-1, -1)
        glTexCoord2f(1, 0)
        glVertex2f(1, -1)
        glTexCoord2f(1, 1)
        glVertex2f(1, 1)
        glTexCoord2f(0, 1)
        glVertex2f(-1, 1)
        glEnd()
        glutSwapBuffers()

    def reshape(self, width, height):
        glViewport(0, 0, width, height)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluOrtho2D(-1, 1, -1, 1)
        glMatrixMode(GL_MODELVIEW)

    def run(self):
        glutMainLoop()

if __name__ == "__main__":
    program = MipmapProgram("base_image.jpg", num_mipmaps=5)
    program.run()
