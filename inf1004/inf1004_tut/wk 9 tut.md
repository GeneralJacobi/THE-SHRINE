
# Q1

$\begin{bmatrix} 4&1 \cr 2&6 \end{bmatrix}$

TODO

# Q2
a + c = 5
d = 9-2 = 7
b = 4-3 = 1

a and c can be any set of 2 nums equal to 5 ----- ans

# Q3

$A = \begin{bmatrix} 3&2 \cr 0&-1 \cr 5&2\end{bmatrix}$

$B = \begin{bmatrix} 1&4&2 \cr -2&3&0 \end{bmatrix}$

3(1) + 2(-2)
0(1) + -1(-2)
5(1) + 2(-2)

3(4) + 2(3)
0(4) + -1(3)
5(4) + 22(3)

3(2) + 2(0)
(2) + (0)
5(2) + 2(0)

TODO
# Q4
A and B invertible n x n matrix

prove
$(AB)^{-1} = B^{-1}A^{-1}$

Working
$(AB)(AB)^{-1} = (AB)B^{-1}A^{-1}$
$I = (AB)B^{-1}A^{-1}$  ------- definition of inverse matrix
$(AB)B^{-1}A^{-1} =A(BB^{-1})A^{-1}$
$BB^{-1} = I$ -------- definition of inverse matrix
$A(I)A^{-1} = AA^{-1} = I$
proven
both products results in I
thus 
$(AB)^{-1} = B^{-1}A^{-1}$  ----------- ans


# Q5
$A = \begin{bmatrix} 1&2 \cr 2&3 \end{bmatrix}$
$A^{-1} = \frac{1}{ad-bc}\begin{bmatrix} 3&-2 \cr -2&1 \end{bmatrix} = -1(\begin{bmatrix} 3&-2 \cr -2&1 \end{bmatrix}) = -\begin{bmatrix} -3&2 \cr 2&-1 \end{bmatrix}$


$[3A^T + \begin{pmatrix} 4&0 \cr 1&2 \end{pmatrix}]^T = A + \begin{pmatrix} 2&-1 \cr 0&3 \end{pmatrix}^{-1}$ - original

$[3A^T + \begin{pmatrix} 4&0 \cr 1&2 \end{pmatrix}]^T = 3A + \begin{pmatrix} 4&0 \cr 1&2 \end{pmatrix}^T$

$\begin{pmatrix} 4&0 \cr 1&2 \end{pmatrix}^T = \begin{pmatrix} 4&1 \cr 0&2 \end{pmatrix}$

$\begin{pmatrix} 2&-1 \cr 0&3 \end{pmatrix}^{-1} = \frac{1}{ad-bc}(\begin{pmatrix} 2&-1 \cr -0&3 \end{pmatrix}) = \frac{1}{6}\begin{pmatrix} 2&1 \cr -0&3 \end{pmatrix}$

$3A + \begin{pmatrix} 4&1 \cr 0&2 \end{pmatrix} = A + \frac{1}{6}\begin{pmatrix} 3&1 \cr -0&2 \end{pmatrix}$
$2A = \frac{1}{6}\begin{pmatrix} 3&1 \cr -0&2 \end{pmatrix} - \begin{pmatrix} 4&1 \cr -0&2 \end{pmatrix}$

$2A = \begin{pmatrix} \frac{1}{2}-4&\frac{1}{6}-1 \cr 0&\frac{1}{3}-2 \end{pmatrix}$
$A = \begin{pmatrix} -\frac{7}{4}&-\frac{5}{12} \cr 0&-\frac{5}{6} \end{pmatrix}$ ---ans


#  Q6

$B = \begin{pmatrix} 1&0&2 \cr 2&1&0 \cr 0&1&3 \end{pmatrix}$

$det(B) = 1(det(\begin{pmatrix} 1&0 \cr 1&3 \end{pmatrix})) - 0(det(\begin{pmatrix} 2&3 \cr 0&0 \end{pmatrix})) + 2(det(\begin{pmatrix} 2&1 \cr 0&1 \end{pmatrix}))$

TODO

# Q7

Theorem Proof: Prove that for any square matrix M, if M is skew-symmetric ($M^T = −M$), then all diagonal entries $m_{ii}$ must be zero.

prove diagonal
for skew-symmetric, ($m_{ij}^T = -m_{ij}$) for all i,j

$m_{ij}^T = -m_{ij}$
$m_{ji} = -m_{ij}$

diagonal, i = j
$m_{ii} = -m_{ii}$
$2m_{ii} = 0$
$m_{ii} = 0$



Decomposition Challenge: Any square matrix A can be expressed as the sum of a symmetric matrix S and a skew-symmetric matrix V

A = S+V,    where $S = \frac{1}{2}(A+A^T)$ and $V = \frac{1}{2}(A-A^T)$

Given $A = \begin{pmatrix} 6&8 \cr 2&10 \end{pmatrix}$

$A^T = \begin{pmatrix} 6&2 \cr 8&10 \end{pmatrix}$
$S = \frac{1}{2}(\begin{pmatrix} 6&8 \cr 2&10 \end{pmatrix}+\begin{pmatrix} 6&2 \cr 8&10 \end{pmatrix})$ = $\frac{1}{2}(\begin{pmatrix} 12&10 \cr 10&20 \end{pmatrix})$ = $\begin{pmatrix} 6&5 \cr 5&10 \end{pmatrix}$

$S$ symmetric as $S = S^T$

$V = \frac{1}{2}(\begin{pmatrix} 6&8 \cr 2&10 \end{pmatrix}-\begin{pmatrix} 6&2 \cr 8&10\end{pmatrix})$ = $\frac{1}{2}(\begin{pmatrix} 0&6 \cr -6&0 \end{pmatrix})$ = $\begin{pmatrix} 0&3 \cr -3&0 \end{pmatrix}$

$V$ is skew-symmetric as $V^T = -V$

$S + V$ = $\begin{pmatrix} 6&5 \cr 5&10 \end{pmatrix}$ + $\begin{pmatrix} 0&3 \cr -3&0 \end{pmatrix}$ = $\begin{pmatrix} 6&8 \cr 2&10 \end{pmatrix}$ = A

yes symmetric and skew-symmetric ------ ans



# EXTRA QN

$A = \begin{pmatrix} 1&2&2 \cr 2&1&2 \cr 2&2&1 \end{pmatrix}$

Find $A^{-1}$ using $A^{-1} = \frac{A_{adj}}{det(A)} = \frac{A_{adj}}{|A|}$

Matrix of Minors = $$\begin{pmatrix} 
\begin{pmatrix} 2&2 \cr 2&2 \end{pmatrix}
&
\begin{pmatrix} 2&2 \cr 2&2 \end{pmatrix}
&
\begin{pmatrix} 2&2 \cr 2&1 \end{pmatrix}
\cr 
\begin{pmatrix} 2&1 \cr 2&2 \end{pmatrix}
&
\begin{pmatrix} 1&1 \cr 2&2 \end{pmatrix}
&
\begin{pmatrix} 1&2 \cr 2&2 \end{pmatrix}
\cr 
\begin{pmatrix} 2&2 \cr 1&2 \end{pmatrix}
&
\begin{pmatrix} 1&2 \cr 2&2 \end{pmatrix}
&
\begin{pmatrix} 1&1 \cr 2&2 \end{pmatrix}
\end{pmatrix}$$
= $\begin{pmatrix} 0&0&-2 \cr 2&0&-2 \cr 2&-2&0 \end{pmatrix}$
$C_{ij} = (-1)^{i+j}M_{ij}$ = $\begin{pmatrix} +(0)&-(0)&+(-2) \cr -(2)&+(0)&-(-2) \cr +(2)&-(-2)&+(0) \end{pmatrix}$ = $\begin{pmatrix} 0&0&-2 \cr -2&0&2 \cr 2&2&0 \end{pmatrix}$

Expand 1st row
$det(A)$ = $1(det(\begin{pmatrix} 2&2 \cr 2&2 \end{pmatrix})) - 2(det(\begin{pmatrix} 2&2 \cr 2&2 \end{pmatrix})) + 2(det(\begin{pmatrix} 2&2 \cr 2&1 \end{pmatrix}))$ = $1(0) - 2(0) + 2(-2)$ = $-4$

$adj(A) = C^T$ = $\begin{pmatrix} 0&-2&2 \cr 0&0&2 \cr -2&2&0 \end{pmatrix}$
$A^{-1} = \frac{A_{adj}}{det(A)} = \frac{A_{adj}}{|A|}$ = $-\frac{1}{4}\begin{pmatrix} 0&-2&2 \cr 0&0&2 \cr -2&2&0 \end{pmatrix}$ = $\frac{1}{4}\begin{pmatrix} 0&2&-2 \cr 0&0&-2 \cr 2&-2&0 \end{pmatrix}$ 








Given $A^2 - 4A - 5I = 0$
Where $A = \begin{pmatrix} 1&2&2 \cr 2&1&2 \cr 2&2&1 \end{pmatrix}$
Find $A^-1$

$A^2 = \begin{pmatrix} 1&2&2 \cr 2&1&2 \cr 2&2&1 \end{pmatrix} \times \begin{pmatrix} 1&2&2 \cr 2&1&2 \cr 2&2&1 \end{pmatrix}$ = $\begin{pmatrix} 9&8&8 \cr 8&9&8 \cr 8&8&9 \end{pmatrix}$
$4A = 4\begin{pmatrix} 1&2&2 \cr 2&1&2 \cr 2&2&1 \end{pmatrix}$ = $\begin{pmatrix} 4&8&8 \cr 8&4&8 \cr 8&8&4 \end{pmatrix}$
$5I = \begin{pmatrix} 5&0&0 \cr 0&5&0 \cr 0&0&5 \end{pmatrix}$

$A^2 - 4A - 5I = 0$
$\begin{pmatrix} 9&8&8 \cr 8&9&8 \cr 8&8&9 \end{pmatrix}$ - $\begin{pmatrix} 4&8&8 \cr 8&4&8 \cr 8&8&4 \end{pmatrix}$ - $\begin{pmatrix} 5&0&0 \cr 0&5&0 \cr 0&0&5 \end{pmatrix}$ = 0


$A^2 - 4A - 5I = 0$
$A^2 - 4A - 5(AA^{-1}) = 0$
$A(A - 4 - 5(A^{-1}) = 0$
$A-4-5(A^{-1}) = 0$
$5A^{-1} = A-4$
$A^{-1} = \frac{1}{5}(A-4)$


Correction
$A^2 - 4A - 5I = 0$
$(A^{-1})A^2 - (A^{-1})4A - (A^{-1})5I = 0$
$IA - 4I - 5A(A^{-1}A^{-1}) = 0$


Ans should be same as previous



$A^2 + I = 8A$
$A^2 - 8A + I = 0$
$(A^{-1})A^2 - 8A(A^{-1}) + I(A^{-1}) = 0$
$IA - 8I + A^{-1} = 0$
$IA - 8I = -A^{-1}$
$8I - IA = A^{-1}$
$(8 - A)I = A^{-1}$  or $8I - A = A^{-1}$

