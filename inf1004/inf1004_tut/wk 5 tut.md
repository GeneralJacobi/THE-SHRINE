
## Q7

2L : 5L
3 : 2
\[2,2,2,5,5]
sample n = 2
X = ice cream tub sold
P(X = 2) =  3/5
P(X = 5) = 2/5

Mean = 2(3/5) + 5(2/5) = 3.2L

Var = $\displaystyle\sum x^2P(X=x) - \mu^2 = (2^2(\frac{3}{5} + 5^2(\frac{2}{5}))-3.2^2) = 2.16L$

all possible samples
(2,2), (2,5) (5,2) (5,5)

P(S = (2,2)) = 3/5 \* 3/5 = 9/25
P(S = (2,5)) = 3/5 \* 2/5 = 6/25
P(S = (5,2)) = 3/5 \* 2/5 = 6/25
P(S = (5,5)) = 2/5 \* 2/5 = 4/25

Sample mean and population mean are equal
Assumes sample is representative of population
When qn says "sells a large number of ", may be required to assume that probability does not change when choosing values
"Random Sample" assumes fair random choice, which makes sample representative of population

# Q8

| x    | 10  | 20  |
| ---- | --- | --- |
| P(x) | 1/5 | 4/5 |

| packets   | 10,10,10        | 10,10,20           | 10,20,20           | 20,20,20        |
| --------- | --------------- | ------------------ | ------------------ | --------------- |
| count     | 1               | 3                  | 3                  | 1               |
| mode      | 10              | 10                 | 20                 | 20              |
| P(mode)   | 1/5 x 1/5 x 1/5 | 1/5 x 1/5 x 4/5 x3 | 1/5 x 4/5 x 4/5 x3 | 4/5 x 4/5 x 4/5 |
| median    | 10              | 10                 | 20                 | 20              |
| P(median) | 1/5 x 1/5 x 1/5 | 1/5 x 1/5 x 4/5 x3 | 1/5 x 4/5 x 4/5 x3 | 4/5 x 4/5 x 4/5 |

| mode    | 10                  | 20                    |
| ------- | ------------------- | --------------------- |
| P(mode) | (1+12)/125 = 13/125 | (48+64)/125 = 112/125 |
| median  | 10                  | 20                    |
| P(mode) | (1+12)/125 = 13/125 | (48+64)/125 = 112/125 |

# Q9

mean of random sample = mean of pop

var of sample = std dev of pop / sqrt of num samples = 2.5

can assume sample is normal dist even tho pop is right skew since sample size > 30
rmbr quote Central Limit Theorem

$\bar{X}$ ~ $N(\mu_\bar{X},\frac{\sigma^2}{n})$


# Q10

mean = 7.25
std dev = 1.75

50 random samples of n = 30

best estimate for mean = pop mean

best estimate for std dev = pop stddev / sqrt num samples

if random select 30 new borns, would u be surprised if mean 8.30

yes
$(x-\mu)/\sigma = Z$
(8.30 - 7.25)/0.32 = 3.3
P(Z >3.3) = 0.0005


# Extra qn

Assuming
fixed and finite num of identical independent trials
only 2 discrete outcomes
probability is fixed

60% of all calls is spam
sample size = 50
Probability more then half of calls in sample NOT spam

let S be spam
S~B(50 , 0.6)

therefore, S\` is not spam
S\`~B(50 , 0.4)

np = 20
n(1-p) = 30
np(1-p) = 12

Binomial Approx
np > 5, n(1-p) > 5

S\`~N(20 , 12)

P(S\` > (0.5\*50) ) = P(S\` > 25) = P(S\` > 25.5) \[Binomial Continuity Correction]

Z = $\frac{x-\mu}{\sigma} = \frac{25.5-20}{\sqrt(12)} = 1.5877$

P(Z > 1.588) = 1 - P(Z < 1.588) = 1 - 0.9441 = 0.0559



flip 2 fair coins
find probability of:
A = get at most one tail
B = Get 2 faces that are the same
C = get 3 tails
are A and B mutually exclusive

T,T = 0.25
T,H = 0.25
H,T = 0.25
H,H = 0.25

P(A) = P(T<=1) = 1 - P(T>1) = 1 - 0.25 = 0.75
P(B) = P(T,T) + P(H,H) = 0.25 + 0.25 = 0.5
P(C) = 0 \[not enough events to get 3 tails]

exclusive requires one to prove that P(A intersect B) = 0

Set of A = \[(T,H), (H,T), (H,H)]
Set of B = \[(T,T), (H,H)]

A intersect B = \[(H,H)]
P(A intersect B) $\neq$ 0
therefore not mutually exclusive