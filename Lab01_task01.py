from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import random
import time


def draw_points(x, y):
    glPointSize(4)
    glBegin(GL_POINTS)
    glColor3f(5, 1, 3)
    glVertex2f(x, y)
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
    glColor3f(5.0, 1.0, 3.0)
    #call the draw methods here
    for i in range(50):
        x = random.randint(1, 500)
        y = random.randint(1, 500)
        draw_points(x, y)

    glutSwapBuffers()



glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(500, 500) #window size
glutInitWindowPosition(0, 0)
wind = glutCreateWindow(b"Task 1") #window name
glutDisplayFunc(showScreen)

glutMainLoop()
