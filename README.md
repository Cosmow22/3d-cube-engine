# 3d cube engine
## Fonctionnement
La rotation repose sur l'utilisations des quaternions.

Un quaternion est un nombre complexe dans un espace à 4 dimensions qui se réprésente ainsi :

$$ 
q = w + xi + yj = zk 
$$

formule quaternionique :

$$  
v' = qvq^{-1} 
\Leftrightarrow 
v'=R(q)v
$$
 
- *v'* représente le vecteur après rotation
- *q* est votre quaternion unitaire de rotation
- *v* correspond au vecteur original à faire tourner
- $q^{-1}$ désigne le conjugué du quaternion q

où R(q) est la matrice de rotation équivalente dérivée du quaternion 

$$
\begin{equation*}
 R ( q ) =
\begin{pmatrix}
1-2(y^2 + z^2) & 2(xy - zw) & 2(xz + yw)\\
2(xy + zw) & 1-2(x^2 + z^2) & 2(yz - xw) \\
2(xz - yw) & 2(yz + xw) & 1 - 2(x^2 + y^2)\\
\end{pmatrix}
\end{equation*}
$$

avec *w* l'angle de rotation, et *x y z* les coordonnées 3d de l'axe

## Demo

![demo](https://github.com/user-attachments/assets/6f516e0c-4d08-4061-8420-63a3771d44a4)

## Commandes

Pour faire tourner le cube, maintenez le clic gauche et bougez la souris.

Vous pouvez aussi utiliser les touches directionnelles.

Pour redimensionner le cube, défilez la mollete de la souris.

***

Voir la version 1: [cube.py](https://github.com/Cosmow22/3d-cube-engine/blob/1cdf3bcdde26174029ca023df321337f17115e5b/cube.py](https://github.com/Cosmow22/3d-cube-engine/blob/1cdf3bcdde26174029ca023df321337f17115e5b/cube.py)

Merci à @[Ge0] pour son aide sur la v2
