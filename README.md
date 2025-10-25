# 3D cube engine

Cette simulation est basé sur cette matrice de rotation tridimensionnelle.
Elle correspond à une rotation :
$$ R=R_{x​}(a)R_{y}​(b)R_{z}​(c) $$

Avec *a* l'angle de rotation autour de l'axe X, *b* autour de Y et *c* autour de Z. 

$$
R =
\begin{bmatrix}
\cos b\cos c & \sin a\,\sin b\,\cos c - \sin c\,\cos a & \sin a\,\sin c + \sin b\,\cos a\,\cos c \\[6pt]
\sin c\cos b & \sin a\,\sin b\,\sin c + \cos a\,\cos c & -\sin a\,\cos c + \sin b\,\sin c\,\cos a \\[6pt]
-\sin b & \sin a\,\cos b & \cos a\,\cos b
\end{bmatrix}.
$$

## Commandes

Pour faire tourner le cube, maintenez le clic gauche et bougez la souris.
Vous pouvez aussi utiliser les touches directionnelles.

Pour redimensionner le cube, défilez la mollete de la souris.


## Ameliorations
1. améliorer le mouvement du cube
2. des effets d'ombre et de lumière
3. des textures
4. une physique réaliste
5. des shaders  
