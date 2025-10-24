from math import cos, sin, pi
from settings import *

class Cube:
    x = [ 1, 1, -1, -1, 1, 1, -1, -1]
    y = [1, 1, 1, 1,- 1,- 1,- 1,- 1]
    z = [-1, 1, 1, -1, -1, 1, 1, -1]

    def __init__(self, a=1, b=2, c=3, factor=0.5):
        # 0 → 6.28 (2 pi)
        self.a = a # rotation autour de X
        self.b = b # rotation autour  de Y
        self.c = c # rotation autour de Z 

        self.factor = factor

        self.points = None
        self.faces = None

    def x_x(self):
        return cos(self.c)*cos(self.b)

    def x_y(self):
        return cos(self.c)*sin(self.b)*sin(self.a) - sin(self.c)*cos(self.a)
    
    def x_z(self):
        return cos(self.c)*sin(self.b)*cos(self.a) + sin(self.c)*sin(self.a)
    
    def y_x(self):
        return sin(self.c)*cos(self.b)
    
    def y_y(self):
        return sin(self.c)*sin(self.b)*sin(self.a) + cos(self.c)*cos(self.a)
    
    def y_z(self):
        return sin(self.c)*sin(self.b)*cos(self.a) - cos(self.c)*sin(self.a)
    
    def z_x(self):
        return -sin(self.b)
    
    def z_y(self):
        return cos(self.b) * sin(self.a)
    
    def z_z(self):
        return cos(self.b) * cos(self.a)
    

    def get_projected_points(self):
        # Calcul des coefficients
        xx = self.x_x()
        xy = self.x_y()
        xz = self.x_z()
        
        yx = self.y_x()
        yy = self.y_y()
        yz = self.y_z()
        
        zx = self.z_x()
        zy = self.z_y()
        zz = self.z_z()

        # Projection de chaque point
        projected_points = []
        for i in range(len(self.x)):
            X = self.x[i] * xx + self.y[i] * xy + self.z[i] * xz
            Y = self.x[i] * yx + self.y[i] * yy + self.z[i] * yz
            Z = self.x[i] * zx + self.y[i] * zy + self.z[i] * zz
            projected_points.append((X, Y, Z))
        return projected_points

    def get_ordered_faces(self):
        """
        Calcule l'ordre d'affichage des faces du cube.
        Les faces sont triées par profondeur moyenne (Z) décroissante,
        donc la face la plus proche s'affichera en dernier.
        """       
        faces = []
        for i, face in enumerate(FACES):
            z_sum = 0
            face_points = []
            for point in face:
                face_points.append(self.points[point])
                z_sum += self.points[point][2]  # Z est à l'index 2
            avg_depth = z_sum / len(face)
            faces.append([face_points, COLORS[i], avg_depth])
        faces.sort(key=lambda x: x[2], reverse=True)
        return faces
    
    def compute(self):
        self.points = self.get_projected_points()
        self.faces = self.get_ordered_faces()
