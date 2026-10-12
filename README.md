# CSE423 Computer Graphics Labs

Raster graphics algorithms from **CSE423 Computer Graphics** at BRAC University (Spring 2022), written in Python with PyOpenGL.

| File | Algorithm |
|---|---|
| `Lab01_task01.py`, `Lab01_task02.py` | OpenGL basics: drawing points |
| `Lab01_task03.py` | **DDA** line drawing, including dotted lines |
| `Lab02.py` | **Midpoint line** algorithm with eight-zone conversion, used to draw digits |
| `Lab03.py` | **Midpoint circle** algorithm with eight-way symmetry |

The lab briefs are included as PDFs.

## Run

```bash
pip install PyOpenGL PyOpenGL_accelerate
python Lab03.py
```

GLUT must be installed (`freeglut`). The `freeglut64.vc14.dll` in this repo is for Windows. On macOS GLUT comes with the system, and on Linux install `freeglut3-dev`.
