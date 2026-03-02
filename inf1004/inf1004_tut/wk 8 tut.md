

# Q1

k = (2,3)
m = (2,2)
w = (-2,-2)

a)
k - m + w = q
q = (2-2-2,3-2-2) = (-2,-1)
---- correct

b)
k = $\begin{pmatrix}2\cr3\end{pmatrix}$
m = $\begin{pmatrix}2\cr2\end{pmatrix}$
w = $\begin{pmatrix}-2\cr-2\end{pmatrix}$
q = $\begin{pmatrix}-2\cr-1\end{pmatrix}$
------ correct

c)
$\hat{i} = \begin{pmatrix}1\cr0\end{pmatrix}$,    $\hat{j} = \begin{pmatrix}0\cr1\end{pmatrix}$

k = $2\hat{i} + 3\hat{j}$
m = $2\hat{i} + 2\hat{j}$
w = $-2\hat{i} + -2\hat{j}$
q = $-2\hat{i} + -1\hat{j}$
------ correct

d)
![[math tut 8 q1.png]] ------ correct


# Q2

$\hat{v} = \frac{v}{||v||}$
$||v|| = \sqrt{a_1^2+a_2^2+...+a_n^2}$

$\hat{v_1} = \frac{1}{||v_1||}v_1 = \frac{1}{\sqrt{3^2+4^2}}(3,4) = \frac{1}{5}(3,4) = (0.6,0.8)$
$\hat{v_2} = \frac{1}{||v_2||}v_2 = \frac{1}{\sqrt{-1^2+-2^2+3^2}}(-1,-2,3) = \frac{1}{\sqrt{14}}(-1,-2,3) = (-\frac{1}{\sqrt{14}},-\frac{2}{\sqrt{14}},\frac{3}{\sqrt{14}})$
$\hat{v_3} = \frac{1}{||v_3||}v_3 = \frac{1}{\sqrt{(-7)^2+2^2+(-4)^2+(\sqrt{12})^2}}(-7,2,-4,\sqrt{12}) = \frac{1}{9}(-7,2,-4,\sqrt{12}) = (-\frac{7}{9},\frac{2}{9},-\frac{4}{9},\frac{\sqrt{12}}{9})$
--- correct
# Q3
Task 1
$u \cdot v = ||u||\ ||v||\ \cos(\theta)$
$u \cdot v = u_1v_1 + u_2v_2 + u_3v_3 = 3(1) + 2(-2) + 2(2) = 3$ ------ ans correct
$||u|| = \sqrt{3^2 + (-2)^2 + 2^2} = \sqrt{17}$
$||v|| = \sqrt{1^2 + 2^2 + 2^2} = \sqrt{9} = 3$
$\cos \theta = \frac{u \cdot v}{||u||\ ||v||} = \frac{3}{3(\sqrt{17})} = \frac{1}{\sqrt{17}}$
$\theta = \arccos (\frac{1}{\sqrt{17}}) = 1.3258 rad = 1.3258(\frac{180}{\pi}) = 75.97\degree$ ------- ans correct

Task 2
$a \cdot b = a_1b_1 + a_2b_2 + a_3b_3 = 1(2) + 0(1) + 1(-2) = 0$
$b \cdot c = b_1c_1 + b_2c_2 + b_3c_3 = 2(\frac{1}{2\sqrt{2}}) + 1(-\frac{\sqrt{3}}{2}) + -2(\frac{1}{2\sqrt{2}}) = -\frac{\sqrt{3}}{2}$
$a \cdot c = a_1c_1 + a_2c_2 + a_3c_3 = 1(\frac{1}{2\sqrt{2}}) + 0(-\frac{\sqrt{3}}{2}) + 1(\frac{1}{2\sqrt{2}}) = \frac{1}{\sqrt{2}}$

$(a \cdot b, b \cdot c, a \cdot c,)(0,-\frac{\sqrt{3}}{2},\frac{1}{\sqrt{2}})$ ------ ans

identify most aligned = smallest $\theta$

$\theta$ for $a \cdot b = 90\degree$ (dot product = 0, vectors are perpedicular)
$\theta$ for $b \cdot c = \arccos(\frac{-\frac{\sqrt{3}}{2}}{\sqrt{9}\sqrt{1}}) = 106.7786549$ 
$\theta$ for $a \cdot c = \arccos(\frac{\frac{1}{\sqrt{2}}}{\sqrt{9}}\sqrt{1}) = 60\degree$

a and c most aligned in novelty seeking as is highest val of the 3 ??????  --- wrong

a and b dot product is 0, means a and b are perpendicular to each other

a and c smallest theta, so most aligned ----- correction
# Q4

$\vec{u} \times \vec{v} = (||\vec{u}||\ ||\vec{v}||\sin\theta)\vec{n}$
$\vec{u} \times \vec{v} = \begin{bmatrix}u_x \cr u_y \cr u_z\end{bmatrix} \begin{bmatrix} v_x \cr v_y \cr v_z\end{bmatrix} = \begin{bmatrix} u_yv_z - u_zv_y \cr -(u_xv_z - u_zv_x) \cr u_xv_y - u_yv_x\end{bmatrix}$
$u \cdot v = ||u||\ ||v||cos \theta$
$u \cdot v = u_1v_1 + u_2v_2 + ... + u_nv_n$

$\vec{u} = (2,1,0)$
$\vec{v} = (1,3,0)$

1. find $\theta$ with dot product
2. stick $\theta$ into cross product to find $\vec{n}$

$u \cdot v = u_1v_1 + u_2v_2 + u_3v_3 = 2(1) + 1(3) + 0(0) = 5$
$||u|| = \sqrt{2^2 + 1^2 + 0^2} = \sqrt{5}$
$||v|| = \sqrt{1^2 + 3^2 + 0^2} = \sqrt{10}$
$\theta = \arccos(\frac{u \cdot v}{||u||\ ||v||}) = \arccos(\frac{5}{\sqrt{5}\sqrt{10}}) = 45\degree$

$\vec{u} \times \vec{v} = (||\vec{u}||\ ||\vec{v}||\sin\theta)\vec{n}$

$\vec{u} \times \vec{v} = \begin{bmatrix}u_x \cr u_y \cr u_z\end{bmatrix} \begin{bmatrix} v_x \cr v_y \cr v_z\end{bmatrix} = \begin{bmatrix} u_yv_z - u_zv_y \cr -(u_xv_z - u_zv_x) \cr u_xv_y - u_yv_x\end{bmatrix} = \begin{bmatrix} 1(0) - 0(3) \cr -(2(0) - 0(1)) \cr 2(3) - 1(1)\end{bmatrix} =  \begin{bmatrix} 0 \cr 0 \cr 5\end{bmatrix}$

$\begin{bmatrix} 0 \cr 0 \cr 5\end{bmatrix} = (\sqrt{5}\sqrt{10}\sin(45\degree))\hat{n}$
$\begin{bmatrix} 0 \cr 0 \cr 5\end{bmatrix} = (5)\hat{n}$
therefore
$\hat{n} = \begin{bmatrix} 0 \cr 0 \cr 1\end{bmatrix}$


surface is "up"

z is positive so, assuming normal Cartesian Vector Space, surface is facing "up"

# Q5
$u \cdot v = u_1v_1 + u_2v_2 + ... + u_nv_n$
$u \cdot v = ||u||\ ||v||cos \theta$

$a \cdot a = a_1a_1 + a_2a_2 + ... + a_na_n = a_1^2 + a_2^2 + ... + a_n^2$
$b \cdot b = b_1b_1 + b_2b_2 + ... + b_nb_n = b_1^2 + b_2^2 + ... + b_n^2$

$c = a+b = (a_1+b_1, a_2+b_2, ... , a_n+b_n)$
$d = a-b = (a_1-b_1, a_2-b_2, ... , a_n-b_n)$

$c \cdot d = c_1d_1 + c_2d_2 + ... + c_nd_n$
$= (a_1+b_1)(a_1-b_1) + (a_2+b_2)(a_2-b_2) + ... +(a_n+b_n)(a_n-b_n)$
$= (a_1^2-b_1^2) + (a_2^2-b_2^2) + ... +(a_n^2-b_n^2)$ ------------ after distributive law
$= (a_1^2 + a_2^2 + ... + a_n^2) - (b_1^2 + b_2^2 + ... + b_n^2)$
$= (a \cdot a) - (b \cdot b)$ ------------ ans




$a = (1,2,3,4,5)$
$b = (1,\sqrt{2},\sqrt{3},\sqrt{4},\sqrt{5})$

c = a + b
c = $(1+1,2+\sqrt{2},3+\sqrt{3},4+\sqrt{4},5+\sqrt{5})$
$= (2,2+\sqrt{2},3+\sqrt{3},4+\sqrt{4},5+\sqrt{5})$

d = a - b
d = $(1-1,2-\sqrt{2},3-\sqrt{3},4-\sqrt{4},5-\sqrt{5})$
$= (0,2-\sqrt{2},3-\sqrt{3},4-\sqrt{4},5-\sqrt{5})$

$c \cdot d = ||c||\ ||d||cos \theta$

$c \cdot d = c_1d_1 + c_2d_2 + ... + c_nd_n$
$= 2(0) + (2+\sqrt{2})(2-\sqrt{2}) + (3+\sqrt{3})(3-\sqrt{3}) + (4+\sqrt{4})(4-\sqrt{4}) + (5+\sqrt{5})(5-\sqrt{5})$
$= 0+2+6+12+20$
$= 40$

$a \cdot a = a_1^2 + a_2^2 + ... + a_n^2 = 1^2 + 2^2 + 3^2 + 4^2 + 5^2 = 55$
$b \cdot b = b_1^2 + b_2^2 + ... + b_n^2 = 1^2 + \sqrt{2}^2 + \sqrt{3}^2 + \sqrt{4}^2 + \sqrt{5}^2 = 1+2+3+4+5 = 15$
$(a \cdot a) - (b \cdot b) = 55 - 15 = 40$

$||c|| = \sqrt{2^2 + (2+\sqrt{2})^2 + (3+\sqrt{3})^2 + (4+\sqrt{4})^2 +(5+\sqrt{5})^2} = 11.24321301$
$||d|| = \sqrt{0^2 + (2-\sqrt{2})^2 + (3-\sqrt{3})^2 + (4-\sqrt{4})^2 +(5-\sqrt{5})^2} = 3.686482572$
$\theta = \arccos(\frac{c \cdot d}{||c||\ ||d||}) = 15.18906411\degree$

# Q6

Line
equation : $\vec{r} = \begin{bmatrix}x \cr mx +c\end{bmatrix}$ 
$r = r_0 +tv$

let $r_0$ be when x=0
$y = -(0) + 1$
$y = 1$
$r_0 = (0,1)$

let $r_1$ be when y = 0
$0 = -x+1$
$x = 1$
$r_1 = (1,0)$

$v = r_1 - r_0 = (1-0,0-1) = (1,-1)$
thus
$\vec{r} = r_0 + tv = \begin{bmatrix}0 \cr 1\end{bmatrix} + t\begin{bmatrix}1 \cr -1\end{bmatrix}$ --------- ans



can also do
let x = t
y = -t + 1
$\vec{r} = \begin{bmatrix}t \cr -t+1 \end{bmatrix} = \begin{bmatrix}0 \cr 1\end{bmatrix} + t\begin{bmatrix}1 \cr -1\end{bmatrix}$




----------------------------------------------------------------

Plane
$x+1 = y+2 = z+3$

let x = 0
$y+2 = 0+1$
$y = -1$
$z + 3 = 0 +1$
$z = -2$
let $r_0 = \begin{bmatrix} 0 \cr -1 \cr -2 \end{bmatrix}$ 

let y = 0
$x+1 = 0+2$
$x = 1$
$z + 3 = 0 + 2$
$z = -1$
let $r_1 = \begin{bmatrix} 1 \cr 0 \cr -1 \end{bmatrix}$ 

$v = r_1 - r_0 = \begin{bmatrix} 1 \cr 0 \cr -1 \end{bmatrix} - \begin{bmatrix} 0 \cr -1 \cr -2 \end{bmatrix} = \begin{bmatrix} 1 \cr 1 \cr 1 \end{bmatrix}$


$\vec{r} = r_0 + tv = \begin{bmatrix} 0 \cr -1 \cr -2 \end{bmatrix} + t\begin{bmatrix} 1 \cr 1 \cr 1 \end{bmatrix}$ --------- ans


position vectors can be different as long as direction vector same

-----------------------------------------------------

$\vec{r} = \begin{bmatrix} -3 \cr 2 \cr 1 \end{bmatrix} + t\begin{bmatrix} 3 \cr 0 \cr 0 \end{bmatrix}$

$\begin{bmatrix} x \cr y \cr z \end{bmatrix} = \begin{bmatrix} -3 \cr 2 \cr 1 \end{bmatrix} + t\begin{bmatrix} 3 \cr 0 \cr 0 \end{bmatrix}$

$\frac{x-x_0}{a} = \frac{y-y_0}{b} = \frac{z-z_0}{c} = t$

a = 3, b = 0, c = 0

since $a = 3$, $x = \frac{x-x_0}{3} = \frac{x+3}{3}$
since $b = 0$, $y = y_0 = 2$ 
since $c = 0$, $z = z_0 = 1$


# Q7

$x + y + z = 2$ ---- cartesian
a = 1, b = 1, c = 1, k = 2

$r = r_0 + tv + su$


let x = 0, y = 0
z = 2
$r_0 = \begin{bmatrix} 0 \cr 0 \cr 2 \end{bmatrix}$

let x = 0, z = 0
y = 2
$r_1 = \begin{bmatrix} 0 \cr 2 \cr 0 \end{bmatrix}$

let y = 0, z = 0
x = 2
$r_2 = \begin{bmatrix} 2 \cr 0 \cr 0 \end{bmatrix}$

$v = r_1 - r_0 = \begin{bmatrix} 0 \cr 2 \cr 0 \end{bmatrix} - \begin{bmatrix} 0 \cr 0 \cr 2 \end{bmatrix} = \begin{bmatrix} 0 \cr 2 \cr -2 \end{bmatrix}$
$u = r_2 - r_0 = \begin{bmatrix} 2 \cr 0 \cr 0 \end{bmatrix} - \begin{bmatrix} 0 \cr 0 \cr 2 \end{bmatrix} = \begin{bmatrix} 2 \cr 0 \cr -2 \end{bmatrix}$

vector equation of $x + y + z = 2$
$\vec{r} = \begin{bmatrix} 0 \cr 0 \cr 2 \end{bmatrix} + t\begin{bmatrix} 0 \cr 2 \cr -2 \end{bmatrix} + s\begin{bmatrix} 2 \cr 0 \cr -2 \end{bmatrix}$ -------- ans

$\vec{r} = 2(\begin{bmatrix} 0 \cr 0 \cr 1 \end{bmatrix} + t\begin{bmatrix} 0 \cr 1 \cr -1 \end{bmatrix} + s\begin{bmatrix} 1 \cr 0 \cr -1 \end{bmatrix})$

also can
let $x+1 = t$
$x = t - 1$
$y = t-2$
$z = t-3$

$\vec{r} = \begin{bmatrix} x \cr y \cr z \end{bmatrix} = \begin{bmatrix} t-1 \cr t-2 \cr t-3 \end{bmatrix} = \begin{bmatrix} -1 \cr -2 \cr -3 \end{bmatrix} + t\begin{bmatrix} 1 \cr 1 \cr 1 \end{bmatrix}$

--------------

$n \cdot (r - r_0) = 0$
$Ax + By + Cz = K$

$n \cdot (r - r_0) = \begin{bmatrix} -3 \cr 2 \cr 1 \end{bmatrix} \cdot (\begin{bmatrix} x \cr y \cr z \end{bmatrix} - \begin{bmatrix} 0 \cr 0 \cr 0 \end{bmatrix}) = 0$
$\begin{bmatrix} -3 \cr 2 \cr 1 \end{bmatrix} \cdot \begin{bmatrix} x \cr y \cr z \end{bmatrix} - \begin{bmatrix} -3 \cr 2 \cr 1 \end{bmatrix} \cdot \begin{bmatrix} 0 \cr 0 \cr 0 \end{bmatrix}= 0$

$(-3x + 2y + 1z) - ((-3)(0) + 2(0) + 1(0)) = 0$
$-3x + 2y + 1z = 0$



# Q8


$\vec{r_1} = \begin{bmatrix} 1 \cr 1 \cr 1 \end{bmatrix} + s\begin{bmatrix} 2 \cr 1 \cr -1 \end{bmatrix} + t\begin{bmatrix} 0 \cr 1 \cr 2 \end{bmatrix}$

$x = 1 + 2s$
$y = 1 + s + t$
$z = 1 - s + 2t$

$\vec{n_1} = \begin{bmatrix} 2 \cr 1 \cr -1 \end{bmatrix} \times \begin{bmatrix} 0 \cr 1 \cr 2 \end{bmatrix}$
$= \begin{bmatrix} 1(2) - (-1)(1) \cr -(2(2)-(-1)(0)) \cr 2(1)-(1)(0) \end{bmatrix} = \begin{bmatrix} 3 \cr -4 \cr 2 \end{bmatrix}$


$\vec{n_1} \cdot (r - r_0) = 0$
$(r - r_0)$ resolves to a vector ON THE PLANE, let it be $\vec{w_1}$
since $\vec{w_1}$ is on the plane, $\vec{n_1}$ is perpendicular
thus
$\vec{n_1} \cdot \vec{w} = 0$
let us use $r_0$ from equation to derive $\vec{w}$

$\begin{bmatrix} 3 \cr -4 \cr 2 \end{bmatrix} \cdot \begin{bmatrix} x-1 \cr y-1 \cr z-1 \end{bmatrix} = 0$

resolves to cartesian equation of
3x - 4y + 2z = 1

$\vec{r_2} = \begin{bmatrix} 1 \cr 2 \cr 3 \end{bmatrix} + s\begin{bmatrix} 6 \cr 2 \cr -5 \end{bmatrix} + t\begin{bmatrix} 2 \cr -2 \cr -7 \end{bmatrix}$
$x = 1 + 6s + 2t$
$y = 2 + 2s - 2t$
$z = 3 - 5s -7t$
$\vec{n_2} = \begin{bmatrix} 6 \cr 2 \cr -5 \end{bmatrix} \times \begin{bmatrix} 2 \cr -2 \cr -7 \end{bmatrix}$
$= \begin{bmatrix} 2(-7) - (-5)(-2) \cr -(6(-7)-(-5)(2)) \cr 6(-2)-2(2) \end{bmatrix} = \begin{bmatrix} -24 \cr 32 \cr -16 \end{bmatrix}$

$\vec{n_1} \cdot \vec{w} = 0$
$\begin{bmatrix} -24 \cr 32 \cr -16 \end{bmatrix} \cdot \begin{bmatrix} x-1 \cr y-2 \cr z-3 \end{bmatrix} = 0$
$(-24)(x-1) + (32)(y-2) + (-16)(z-3) = 0$
$(-24x+24) + (32y-64) + (-16z+48) = 0$
$-24x + 32y - 16z = -8$
$3x - 4y + 2z = 1$

since Cartesian equation for both vector equations are the same,
both vector equations represent the same plane

ALT
solve for s and t
then able to convert x or y or z into a form without s or t