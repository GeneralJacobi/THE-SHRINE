
# Q1

17 19 22 26 28 31 34 36 38 39 41 42 43 47 50 51 53 55 57 58 (60 62 97)

a) mean = $\frac{\displaystyle\sum{x_i}}{n}$ = $\frac{787}{20}$ = 39.35

std dev = $\sqrt{varience}$ = $\frac{1}{n-1}[\displaystyle\sum{x_i^2} - \frac{(\displaystyle\sum{x_i})^2}{n}]$ = 12.68

b) IQR = Q3 - Q1 = 24
17 19 22 26 28 \[31] 34 36 38 39 41 \[42] 43 47 50 51 \[53] 55 57 58 60 62 97

31 = Q1 median
42 = Q2 median
53 = Q3 median

c) Outliers?
Yes, difference between 97 and its adjacent number is greater than difference between any  other adjacent values

correction:

Outlier formula = observation falling below Q1 - 1.5(IQR) / falling above Q3 +1.5(IQR)
Q3 + 1.5(IQR) = 55 +36 = 91
97 > 91, therefore is outlier


# Q2

## i
a ; P($A_1$)
## ii
a ; P($B_2$)
correction : y is conditional, require A1 hapen first,
i.e. P($B_2|A_1$)
## iii
d ; P($C_1|B_2∩A_1$)
## iv
c ; P($C_1 ∩ B_2 ∩ A_1$)
## v
P(A\`) = 1 - P(A)
P($A ∪ B$) = P(A) + P(B) - P($A ∩ B$) 


P($(A ∪ B)$\`) = $\frac{3}{8}$
P($(A ∪ B)$) = $1-\frac{3}{8} = \frac{5}{8}$
## vi
P(C) = 0.5
P($C ∩ D$) = 0.2
P(($C ∪ D$)\`) = 0.4

P($C ∪ D$) = 1 - P(($C ∪ D$)\`) = 0.6
P(D) - P($C ∩ D$) = 1 - P(C) + P(($C ∪ D$)\`) = 0.1
P(D) = 0.1 + P($C ∩ D$) = 0.1 + 0.2 = 0.3


# Q3

## a) 
P(uni quality first reason) = P($\frac{821}{1929}$) = 0.426 (3dp)

## b) 
P(uni student and uni quality first reason) = P($\frac{fulltime\ student\ uni\ quality}{all\ fulltime\ students}$) = P($\frac{421}{890}$) = 0.473 (3dp)
also can: P(uni quality | full time student) = $\frac{P(UniQuality ∩ Fulltime)}{P(Full time)}$ = $\frac{\frac{421}{1929}}{\frac{890}{1929}}$ = 0.473

conditional probability formula : P(A | B) = $\frac{P(A∩B)}{P(B)}$
## c) 
A = P(student is full time) = $\frac{890}{1929}$ = 0.461 (3dp)
B = P(uni quality) = $\frac{821}{1929}$ = 0.426 (3dp)

is it independent, yes

correction
proof: 
P(A | B) = P(A)   AND   P(B|A) = P(B)

P(B) = 0.426 (from part a)
P(B | A) = 0.473 (from part b)
since P(B | A) != P(B), hence is not independent
# Q4


| THE TEST       | has disease (D)            | no disease (D\`)          |
| -------------- | -------------------------- | ------------------------- |
| positive (T)   | 0.96; true pos             | 1- 0.94 = 0.06; false pos |
| negative (T\`) | 1 - 0.96 = 0.04; false neg | 0.94; true neg            |


# a)
D = has disease
T = tested positive

P(D) = 0.02
P(T | D) = 0.96
P(T\` | D\`) = 0.94

P(D|T)

correction: 
Bayers Theorem
P(B|A) = $\frac{P(A|B)P(B)}{P(A|B)P(A) + P(A|B^`)P(B^`)}$
$P(A|B)P(A) + P(A|B^`)P(B^`)$ = P(B)

Jia Bao theorem = $\frac{true\ positive}{all\ positive}$

ANS: 0.2467
# b)

correction:
P(D\` | T\`)

P(D\` | T\`) = $\frac{ \frac{P(T^`|D)}{} }{}$
0.94*0.98 / (0.94*0.98 + 0.04*0.02)


# Q5


| 1/3 | Identical |
| --- | --------- |
| 2/3 | Fraternal |

| identical | 1/2 | BB  |
| --------- | --- | --- |
|           | 1/2 | GG  |

| Fraternal | 1/4 | BB  |
| --------- | --- | --- |
|           | 1/4 | GB  |
|           | 1/4 | BG  |
|           | 1/4 | GG  |
P(I | BB) = $\frac{ P(BB | I)P(I) }{P(BB)}$ = 1/2

!!!!!!!!!!!!!!! to do !!!!!!!!!!!!!!!!

Jia Bao theorem = $\frac{ identical\ bb }{ all\ bb }$


# Q6
correction
## a)

A rep Alice born
B rep Bob born
C rep Carl born

P(A > B | A > C) = $\frac{ P( A > B ∩ A>C) }{ P(A > C) }$

## b)

P(A>B|A>C) != P(A>B)
dependant


# Q7


| G; 0.6   | E; 0.8   |
| -------- | -------- |
|          | E\`;0.2  |
| G\`; 0.4 | E; 0.5   |
|          | E\`; 0.5 |
G AND E = TREAT
## a)
P(G AND E) = 0.6 \* 0.8 = 0.48
## b)
P(G\` AND E) = P(E|G\`)P(G\`)
P(G\` AND E) = 0.4 \* 0.5 = 0.2
## c)
P(E) = P(G AND E) + P(G\` AND E) = 0.68 \[law of total probability]
## d)
P(G\` | E) = P(G\` ∩E)/P(E) = 0.2/0.68 = 0.29
# Q8

sample 1
10 samples
samaple mean = 2.4h
std dev = 0.8h
total = 24h

sample 2
5 samples
sample mean = 2.0h
std dev = 1.2h
total = 10h


new mean  = $\bar{z}$ = $\frac{ \displaystyle\sum{x_i} + \displaystyle\sum{y_i} }{n_x + n_y}$ = $\frac{24 + 10}{10 + 5}$ = $\frac{34}{15}$ = 2.267 (3dp)

 variance = $\frac{1}{n-1}[\displaystyle\sum{x_i^2} - \frac{(\displaystyle\sum{x_i})^2}{n}]$ 
combining varience to find combined std dev = 
$s_z^2$ = $\frac{1}{n_x + n_y - 1}[\displaystyle\sum{x_i^2} + \displaystyle\sum{y_i^2} - \frac{(\displaystyle\sum{x_i} + \displaystyle\sum{y_i})^2}{n_x + n_y}]$ 

 need find $\displaystyle\sum{x_i^2}$ and  $\displaystyle\sum{y_i^2}$

re arrange varience  !!!!!!!!!!!!!!!!!!!!!!!!to do !!!!!!!!!!!!!!!!

$(n-1)varience = \displaystyle\sum{x_i^2} - \frac{(\displaystyle\sum{x_i})^2}{n}$

$\displaystyle\sum{x_i^2}$ = 63.36
$\displaystyle\sum{y_i^2}$ = 25.76

new varience = $\frac{1}{14}[65.56 + 25.76 - \frac{(24+10)^2}{15}]$  = 0.86

new std dev = $\sqrt{0.86}$ = 0.93


# Q9

3/6 \* 2/5 \* 1/4 = 6/
120 = 0.05

# BONUS

BONUS ON XSITE GO DO

Q7

Q9