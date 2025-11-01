# 3d cube engine
## Fonctionnement
La rotation repose sur l'utilisations des quaternions.

Un quaternion est un nombre complexe appartenant à l'ensemble des hypercomplexes noté ${\displaystyle \mathbb {H} }$ :

$$ 
q = w + xi + yj = zk 
$$

et défini par :

$$
i^{2} = j^{2} = k^{2} = ijk = -1
$$

avec w, x, y, z des réels et i, j, k coefficients imaginaires

L'ordre dans leqel on tourne le cube importe. Si je tourne en avant puis sur la droite, je n'aurai pas le même résultat que si je tourne d'abord le cube vers la droite puis vers l'avant la rotation importe. 


En effet, La multipilcation des quaterions est non **commutative**.

|  ↓*→  | **1** | **i** | **j** | **k** |
|-------|-------|-------|-------|-------|
| **1** |   1   |   i   |   j   |   k   |
| **i** |   i   |  -1   |   k   |  -j   |
| **j** |   j   |  -k   |  -1   |   i   |
| **k** |   k   |   j   |  -i   |  -1   |


Par exemple : 

(2 - i + 4j + 3k)(-3 + 2i + j - 2k) 
= -2 - 4i - 6j -22k

alors que si on multiplie dans l'autre sens..

(-3 + 2i + j - 2k)(2 - i + 4j + 3k)
= -2  + 18i - 14j - 4k

formule de rotation :

$$  
v' = qvq^{-1} 
\Leftrightarrow 
v'=R(q)v
$$
 
- v' représente le vecteur après rotation
- q est votre quaternion unitaire de rotation
- v correspond au vecteur original à faire tourner
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

un quaternion de rotation est créé par :

$$
r = cos(\theta/2) + sin(\theta/2)(xi + yj + zk)
$$

## Demo

![demo](https://github.com/user-attachments/assets/6f516e0c-4d08-4061-8420-63a3771d44a4)

## Commandes

Pour faire tourner le cube, maintenez le clic gauche et bougez la souris.

Vous pouvez aussi utiliser les touches directionnelles.

Pour redimensionner le cube, défilez la mollete de la souris.

***

Voir la version 1: [cube.py](https://github.com/Cosmow22/3d-cube-engine/blob/1cdf3bcdde26174029ca023df321337f17115e5b/cube.py)

Merci à [@Ge0](https://github.com/Ge0) pour son aide sur la v2
