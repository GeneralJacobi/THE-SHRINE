# tut1

2's complement trick
find last instance of 1, all 0 right of last instance of 1 remain as 0, flip all bits left of last instance 1 except MSB

e.g.:
|-|-|-|-|-|-|-|-|
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
|1|0|1|0|0|1|0|0|
|[1]|0|1|0|0|[1]|0|0|
|[1]|1|0|1|1|[1]|0|0| -- end

q1a

$\frac{2v}{8}$ step cus $2^3$

0, 0.5, 1.5, 1.75, 1.75

never hits max 2v.  
because need to keep 000 for 0V, no choice have to give up 2v  
considered boundary case

error
0.001, 0.011, 0.068, 0.053, 0.146

standard choice: $\frac{Vmax}{2^n}$  
if req to include Vmax: $\frac{Vmax}{(2^n -1)}$  
other possibility: 000 = midpoint of step between (0 and 0.25)

q1b

sum all absolute / num samples

max error is $\frac{(v/2^n)}{2}$ as max error is when voltage is exactly in middle of diff between step values

q1c

$\frac{(Vmax/2^10)}{2} = \frac{(2/2^10)}{2} = 0.97mV$

q1d  
increase ADC bits increase resolution but also increase overall file size


q2a  
120(dec) = 1000 0000  
NOTE need to delcare somehow that is a positive number. since by default is 2's complement  
e.g. 0 1000 0000 or 1000 000 (unsigned)

q2b  
by default is 2's complement  
neg representation 1010 1011 0001 0010 1110 1111 (bin)  
2's complement pos num: 1101 0100 1110 1101 0001 0001 (bin)

-5 565 713 (dec)

q2c  
164 (unsigned), -36 (sign magnitude), -91(1's complement), -92(2's complement)  (all dec)  
need declare which is which

q2d  
11 1011(sign-magnitude), 10 0100(1's complement), 10 0101(2's complement)  (all bin)  
need declare which is which

q2e  
9.375 

q2f  
0001 0100 0100.1111 (unsigned bin)

q2g  
0101 0011 1001. 0101 0111 (BCD)

q2h    
0 1000 0101 000 0000 0100 0000 0000 0000 (bin floating point)  
word ver: 42804000 (hex)


q2i  
C46A 0840(hex) = 1100 0100 0110 1010 0000 1000 0100 0000 (bin)  
[1][100 0100 0][110 1010 0000 1000 0100 0000]

[100 0100 0] = 136 raw value  
exponent bias: -127 = 9  
mantissa = 1.[110 1010 0000 1000 0100 0000]  
shift bits **right** (since is decoding) by exponent times  
1.110 1010 0000 1000 0100 0000 -> 1110 1010 00.00 1000 0100 0000  
936.12890625 (dec)  
rmbr add neg sign because sign bit is 1  
-936.12890625 (dec)

q3a  
89  = 0101 1001

27  = 0001 1011  
-27 = 1110 0100 +1 = 1110 0101

89-(27)
| | |     |$^2 ->^1$|$^2$|$^2$  |$^2 ->^1$|$^2$| |
|-|-|-----|:-------:|-----|-----|:-------:|----|-|
| |0|~~1~~|    0    |~~1~~|~~1~~|    0    |  0 |1|
|-|0|  0  |    0    |  1  |  1  |    0    |  1 |1|
| |0|  0  |    1    |  1  |  1  |    1    |  1 |0|
    
^^^ result ok

89+(-27)

|$^1$|$^1$| | | | | |$^1$| |
|----|----|-|-|-|-|-|----|-|
|    | 0  |1|0|1|1|0| 0  |1|
|  + | 1  |1|1|0|0|1| 0  |1|
| [1]| 0  |0|1|1|1|1| 1  |0|

^^^ incorrect as carry not shown

q3b
44 = 0010 1100  
-44 = 1101 0011 +1 = 1101 0100  
99 = 0110 0011  
-99 = 1001 1100 +1 = 1001 1101

-44 - (+99)
| |     |$^2$ |$^2$| | |     |$^2 ->^1$|$^2$|
|-|-----|-----|----|-|-|-----|:-------:|----|
| |~~1~~|~~1~~|  0 |1|0|~~1~~|    0    |  0 |
|-|  0  |  1  |  1 |0|0|  0  |    1    |  1 |
| |  0  |  1  |  1 |1|0|  0  |    0    |  1 |

^^^incorrect as is positive, overflow

-44 + (-99)
|$^1$| | |$^1$|$^1$| $^1$| | | |
|----|-|-|----|----|-----|-|-|-|
|    |1|1|  0 |  1 |  0  |1|0|0|
|  + |1|0|  0 |  1 |  1  |1|0|1|
| [1]|0|1|  1 |  1 |  0  |0|0|1|

^^^added extra 1, carry and overflow

q4
decimal x: 86, 126, 6, 0, -128
decimal y: 86, 3, -6, -8, -1
binary z: 1010 1100, 1000 0001, 0000 0000, 1111 1000, 0111 1111
decimal z: -86,-127, 0, -8, 127
overflow: yes,yes,no,no,yes



# tut 4

q1  
a:  
badboy2 = 2 1 4 2 15 25 2
2 + 1 + 4 + 2 + 15 + 25 + 2 = 51  
51 mod 7 = 2  
9(2+1) = 27
reverse = 72  
gb

b:  
chjbup5 = 3 8 10 2 21 16 5
3 + 8 + 10 + 2 + 21 + 16 + 5 = 65
65 mod 7 = 2  
9(2+1) = 27
reverse = 72  

c:  
hash collision, wrong password also can get in.
not possible to reverse engineer original password

q2  
a. 
13 14 22 8 18 19 7 4 7 14 20 17
17 18 0 12 22 23 11 8 11 18 24 21
RSA MW XLI LSYV  

b. no, key 26 will not encrypt the text, as mod 26 will use back original value.

c. brute force all combinations, downside: takes longer  
Pattern / freqeuency analysis, downside: more complexe / need more data to guess / need to know which language used

q3  

get familiar with matric multiplication

$\begin{pmatrix}a&b \cr c&d \end{pmatrix} \begin{pmatrix}1 \cr 2 \end{pmatrix} = \begin{pmatrix}a1+b2 \cr c1+d2 \end{pmatrix}$

$K = \begin{pmatrix}a&b \cr c&d \end{pmatrix}$  
determinant = $(a(c) - b(d)) \mod 26$  
determinant x determinant\` mod 26 = 1  
rearrange  
(26 x determinant\` + 1) mod determinant = 0  
determinant\` = $\frac{1}{ad-bc}$ (not actually a fraction, inverse)  
adj(K) = $\begin{pmatrix}d&-b \cr -c&a \end{pmatrix}$  
$K` = \frac{1}{ad-bc} \begin{pmatrix}d&-b \cr -c&a \end{pmatrix}$  

a.  
helloworld
7 4 11 11 14 22 14 17 11 3

drjiogadxy

b.  
find = $\begin{pmatrix}5&8 \cr 13&3 \end{pmatrix}$  
determinant = $(5(13) - 8(3)) \mod 26 = 15$  
(26 x determinant\` + 1) mod determinant = 0  
(26 x determinant\` + 1) mod 15 = 0
determinant\` = 7  
adj(K) = $\begin{pmatrix}3&-8 \cr -13&5 \end{pmatrix} \mod 26 = \begin{pmatrix}3&18 \cr 13&5 \end{pmatrix}$  
K\` = determinant\` x adj(K) = $7 \times \begin{pmatrix}3&18 \cr 13&5 \end{pmatrix} \mod 26 = \begin{pmatrix}21&22 \cr 13&9 \end{pmatrix}$  

pznumoyzbw = $\begin{pmatrix}p \cr z \end{pmatrix} \begin{pmatrix}n \cr u \end{pmatrix} \begin{pmatrix}m \cr o \end{pmatrix} \begin{pmatrix}y \cr z \end{pmatrix} \begin{pmatrix}b \cr w \end{pmatrix}$  
$= \begin{pmatrix}15 \cr 25 \end{pmatrix} \begin{pmatrix}13 \cr 20 \end{pmatrix} \begin{pmatrix}12 \cr 14 \end{pmatrix} \begin{pmatrix}24 \cr 25 \end{pmatrix} \begin{pmatrix}1 \cr 22 \end{pmatrix}$  

decode $\begin{pmatrix}p \cr z \end{pmatrix}$:  
$\begin{pmatrix}21&22 \cr 13&9 \end{pmatrix} \begin{pmatrix}15 \cr 25 \end{pmatrix} \mod 26 = \begin{pmatrix}7 \cr 4 \end{pmatrix}$

helloworld


q4  

let $k = ab$  
$x^k \mod m = (x^a)^b \mod m$  
$(x^a)^b \mod m = (x^a \mod m)^b \mod m$

let x = 8, k = 2, m = 5  
$x^k \mod m = 8^2 \mod 5$  
$(8 \mod 5) \times (8 \mod 5) \mod 5$


a.  
p = 5, q = 11
n = p*q = 55  
m = (p-1)*(q-1) = 40  

b.  
yes is valid as does not share any factors.  
not always valid, must be **coprime** with m, even though it is prime

c.  
$(d \times e) \mod m = 1$  
$(3d) \mod 40 = 1$  
rearrange  
(x(40)+1) mod 3 = 0, for some int x,  
(x(40)+1) / 3 = d  
d = 27


d.  
$C = M^e \mod n$  
$C = 7^3 \mod 55 = 13$ 

e.  
$M = C^d \mod n$  
$M = 13^27 \mod 55 = 7$