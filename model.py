import sys
from PyQt6.QtCore import Qt, QBuffer
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtOpenGLWidgets import QOpenGLWidget
from PyQt6.QtGui import QImage, QQuaternion
from OpenGL.GL import *
from OpenGL.GLU import *
from objloader import OBJ
import os
import numpy as np


class GLWidget(QOpenGLWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.vertices = []
        self.normals = []
        self.texcoords = []
        self.faces = []
        self.texture_id = 0
        self.yawangle = 0
        self.pitchangle = 0
        self.rollangle =0

    def initializeGL(self):
        glEnable(GL_DEPTH_TEST)
        glEnable(GL_TEXTURE_2D)
        glEnable(GL_LIGHTING)
        glEnable(GL_LIGHT0)
        glLightfv(GL_LIGHT0, GL_POSITION, [0, 1, 1, 0])
        glClearColor(0.0, 0.0, 0.0, 1.0)
        self.texture = glGenTextures(1)
        self.load_obj()

    def load_obj(self):
        obj = OBJ('chibi.obj', swapyz=False)
        self.vertices = obj.vertices
        self.normals = obj.normals
        self.texcoords = obj.texcoords
        self.faces = obj.faces

        # Create dictionary mapping vertex index to texture coordinate
        self.texcoord_dict = {}
        for i, texcoord in enumerate(self.texcoords):
            self.texcoord_dict[i] = texcoord

        # Compute vertex normals
        vertex_normals = np.zeros((len(self.vertices), 3))
        for face in self.faces:
            for i in range(3):
                vertex_index = face[0][i] - 1
                normal_index = face[1][i] - 1
                vertex_normals[vertex_index] += self.normals[normal_index]
        self.normals = vertex_normals / np.linalg.norm(vertex_normals, axis=1)[:, np.newaxis]

    def paintGL(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        gluLookAt(10, 10, 50, 0, 0, 0, 0, 1, 0)
        glRotatef(self.yawangle, 0.0, 1.0, 0.0)
        glRotatef(self.rollangle, 0.0, 0.0, 1.0)
        glRotate(self.pitchangle,0,0,0)
        glBindTexture(GL_TEXTURE_2D, self.texture)
        glBegin(GL_TRIANGLES)
        for face in self.faces:
            for i in range(3):
                vertex_index = face[0][i] - 1
                texture_index = face[2][i] - 1
                if vertex_index < len(self.vertices):
                    texcoord = self.texcoord_dict.get(texture_index)
                    if texcoord is not None:
                        glTexCoord2f(*texcoord)
                    glNormal3f(*self.normals[vertex_index])
                    glVertex3f(*self.vertices[vertex_index])
        glEnd()



    def resizeGL(self, width, height):
        glViewport(0, 0, width, height)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(45, width / height, 0.1, 100)




""" class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('OBJ Viewer')
        self.gl_widget = GLWidget()
        self.setCentralWidget(self.gl_widget) """




""" if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    window.gl_widget.rollangle =90
    window.gl_widget.update()
    sys.exit(app.exec())
 """