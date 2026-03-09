
# Q1

# Q2
univalve : bivalves
76:24

choose 100
each shell is independent
probability unchanged

criteria
fixed finite independent identical
discrete outcome
probability fixed

mean and varience looking to find bivalves

X ~ B(100, 1-0.76) = B(100, 0.24)

mean = np = 100\*0.24 = 24
var = npq = 100\*0.24\*0.76 = 18.24

p(X=1) = $(100 C 1)(0.24)^1(0.76)^{99}$


Y~B(100,0.76)
P(Y>86)
np>5
nq>5

Y~N(np,npq) = N(76,18.24)

since approx, check table
p(Y>86.5)

Z = ($\frac{86.5-76}{\sqrt{18.24}}$) = 2.458

1-0.9929 = 0.0071
1-0.9931 = 0.0069


# Q3

P(A) = (.5\*.1) + (.3\*.3) + (.2\*.8)

P(C|A\`) = $\frac{P(A`|C)P(C)}{P(A`)}$ = 0.6429

# Q4

X~N(40,5^2)

P(X<25) = 0.0013
P(X<45) = 0.843
P(25<x<45) = 0.84


# Q5

| X      | 10  | 20  | 30  | 40  | 50  |
| ------ | --- | --- | --- | --- | --- |
| P(X=x) | 0.4 | 0.2 | 0.2 | 0.0 | 0.2 |
a)
E(x) = $\mu$ = (10 x .4) + (20 x .2) + (30 x .2) + (50 x .2) = 4 + 4 + 6 + 10 = 24
var $\sigma^2$= $(10-24)^2(.4) + (20-24)^2(.2) + (30-24)^2(.2) + (50-24)^2(.2)$ 
= 78.5+3.2+7.2+135.2
= 224.1
std dev = $\sqrt{224.1}$ = 14.96996994

b)
P($x \leq 30$) = .4+.2+.2 = .8

c)
n = 45
sample mean = pop mean = 24
$s$ =  $\frac{\sigma}{\sqrt{n}}$  = $\frac{\sqrt{224.1}}{\sqrt{45}}$ = 2.231093404

d)
n=45
n>30, use CLT
X~N(24,$(2.23)^2$)
P($\bar{x} \leq 30$)
Z = $\frac{30-24}{2.23}$ = 2.69
P(Z < 2.69) = 0.9964

e)
P(Z < ???) = 0.036
P(Z > ???) = 1 - 0.036 = 0.9640
Z = -1.80
Z = $\frac{x-24}{2.23}$ 
x = -1.8 x 2.23 + 24 = 19.986 approx 20


# Q2
n = 5
P(A) = 1/3
X~B(5,1/3)
P($X \geq 3$) = $5C3(1/3)^3(2/3)^2 + 5C4(1/3)^4(2/3) + 5C5(1/3)^5$
= 0.2098765432 = $\frac{17}{81}$

# Q3
$\mu = 80$
$\sigma = 24$
n = 36
n $\geq$ 30, use CLT

X~N(80,$24^2$)

sample mean = pop mean = 80
sample std dev = $\frac{\sigma}{\sqrt{n}} = \frac{24}{\sqrt{36}} = 4$

2 std dev away = 80 + 2(4) = 88