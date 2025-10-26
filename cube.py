import numpy as np
from settings import *

def quat_multiply(q1, q2):
    """Produit de deux quaternions"""
    w1, x1, y1, z1 = q1
    w2, x2, y2, z2 = q2
    return np.array([
        w1*w2 - x1*x2 - y1*y2 - z1*z2,
        w1*x2 + x1*w2 + y1*z2 - z1*y2,
        w1*y2 - x1*z2 + y1*w2 + z1*x2,
        w1*z2 + x1*y2 - y1*x2 + z1*w2
    ])

def quat_normalize(q):
    return q / np.linalg.norm(q)

def quat_from_axis_angle(axis, angle):
    """Crée un quaternion à partir d’un axe et d’un angle"""
    axis = np.array(axis)
    axis = axis / np.linalg.norm(axis)
    s = np.sin(angle / 2)
    return np.array([np.cos(angle / 2), axis[0]*s, axis[1]*s, axis[2]*s])

def quat_to_matrix(q):
    """Convertit un quaternion en matrice 3x3"""
    w, x, y, z = q
    return np.array([
        [1 - 2*(y**2 + z**2),  2*(x*y - z*w),      2*(x*z + y*w)],
        [2*(x*y + z*w),        1 - 2*(x**2 + z**2), 2*(y*z - x*w)],
        [2*(x*z - y*w),        2*(y*z + x*w),      1 - 2*(x**2 + y**2)]
    ])

class Cube:
    def __init__(self):
        # Coordonnées de base du cube
        self.vertices = np.array([
            [ 1,  1, -1],
            [ 1,  1,  1],
            [-1,  1,  1],
            [-1,  1, -1],
            [ 1, -1, -1],
            [ 1, -1,  1],
            [-1, -1,  1],
            [-1, -1, -1],
        ])
        self.q = np.array([1, 0, 0, 0])  # quaternion initial (aucune rotation)
        self.points = None
        self.faces = None
        self.compute()

    def rotate(self, axis, angle):
        """Applique une rotation autour d’un axe (x,y,z)"""
        q_rot = quat_from_axis_angle(axis, angle)
        self.q = quat_multiply(q_rot, self.q)
        self.q = quat_normalize(self.q)
        self.compute()

    def compute(self):
        """Calcule les points projetés après rotation"""
        R = quat_to_matrix(self.q)
        self.points = np.dot(self.vertices, R.T)

        # Calcul des faces triées par profondeur
        faces = []
        for i, face in enumerate(FACES):
            pts = [self.points[idx] for idx in face]
            avg_z = np.mean([p[2] for p in pts])
            faces.append((pts, COLORS[i], avg_z))
        self.faces = sorted(faces, key=lambda f: f[2])
