from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import random
import time



def draw_points(x, y):
    glPointSize(3) #pixel size. by default 1 thake
    glBegin(GL_POINTS)
    glColor3f(1, 0, 0)
    glVertex2f(x, y) #jekhane show korbe pixel
    glEnd()

def iterate():
    glViewport(0, 0, 500, 500)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 500, 0.0, 500, 0.0, 1.0)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()

def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    glColor3f(255.0, 255.0, 0.0)
    #call the draw methods here
    glBegin(GL_TRIANGLES)
    glColor3f(255.0, 255.0, 0.0)
    glVertex3f(355, 380, 0)
    glVertex3f(200, 240, 0)
    glVertex3f(500, 240, 0)
    glEnd()

    glBegin(GL_QUADS)
    glColor3f(255, 0, 0)
    glVertex2i(200, 240)
    glVertex2i(500, 240)
    glVertex2i(500, 0)
    glVertex2i(200, 0)
    glEnd()

    glBegin(GL_QUADS)
    glColor3f(255, 255, 255)
    glVertex2i(240, 200)
    glVertex2i(320, 200)
    glVertex2i(320, 130)
    glVertex2i(240, 130)
    glEnd()

    glBegin(GL_QUADS)
    glColor3f(255, 255, 255)
    glVertex2i(380, 200)
    glVertex2i(460, 200)
    glVertex2i(460, 130)
    glVertex2i(380, 130)
    glEnd()

    glBegin(GL_QUADS)
    glColor3f(255, 255, 255)
    glVertex2i(300, 80)
    glVertex2i(400, 80)
    glVertex2i(400, 0)
    glVertex2i(300, 0)
    glEnd()
    glutSwapBuffers()



glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(700, 500)
glutInitWindowPosition(0, 0)
wind = glutCreateWindow(b"Task 2")
glutDisplayFunc(showScreen)

glutMainLoop()
