# Tutorial 1 
## q1
1a. $\displaystyle\sum_{k=1}^5(k+1)$
1. find num of terms, 
2. write out first few terms if have many
3. determine they type of sequence: in ths case: arithmetic

1b. $\displaystyle\sum_{j=0}^4(-2)^j$
1. mind the index
2. mind lower limit
3. determine if this is a special sequence
geometric

1c. $\displaystyle\sum_{i=0}^10-3$
1. mind the index
2. mind lower limit
3. determine if this is a special sequence
4. in this case is geometric or ????

1d. $\displaystyle\sum_{j=0}^8(2^{j+1}-2^j)$
1. Mind index
2. mind lower limit
3. simplify the summation terms in advance: $2*2^j-2^j = $  
OR  
break up into sum of 2 summations: $\displaystyle\sum_{j=0}^8(2^{j+1}) - \displaystyle\sum_{j=0}^8(-2^j)$
4. determine the secial sequence, in this case: geometric

## q2
1. generate terms one after another (recursive formula)
you can determin it is recusive since you see $a_{n-1}$

## q3
1. use heeuristic approach (list first few terms) for calculation or verification  
1 year: $1000 * (1+7\%)^1$  
2 year: $1000 * (1+7\%)^2$  
3 year: $1000 * (1+7\%)^3$  
4 year: $1000 * (1+7\%)^4$

Compund interest is a geometric sequence.  

## q4
Find the sum of the first n terms of an arithmetic series whose first term is 1 and whose common
difference is 5  
$a_n = a + (n-1)d$  
$a_1 = 1$, $d = 5$  
$S_n = \frac{n(2a + (n-1)d)}{2} = \frac{n(5n-3)}{2}$

## q5

application of general formula and summation equation of arithetic progression
only need know first term and common difference to determin an arithmetic progression

term 7 = 7,  
sum of first 10 terms is 60  
$a_7 = a+6d = 7 $  
$S_{10} = \frac{10(2a+9d)}{2} = 60$  
solve the linear equations with two variables, a=3, d=$\frac{2}{3}$

## q6
min the number of terms
find expression for $2(3) +2(3)^2 + ... +2(3)^n$
is geometric  
first term a = 2, common ratio r = 3
total n+1 terms
$$S_{n+1} = \frac{a(1-r^{n+1})}{1-r} = \frac{2(1-3^{n+1})}{1-3} = 3^{n+1}-1$$

$$S_{n+1} = S_n + a_{n+1} = \frac{a(1-r^n)}{1-r} + a_nr$$

## q7

7a. 
$\displaystyle\sum_{j=0}^8 3*2^j$

$j=0, 3*2^0 = 3$  
$j=1, 3*2^1 = 6$  
$j=2, 3*2^2 = 12$  
actually is geometric prograssion  
a = 3, r = 2

7b.
$\displaystyle\sum_{j=0}^8 (-3^j)$

$j=0, -3^0 = 9$  
$j=1, 3^1 = -27$  
$j=2, 3^2 = 81$  
actually is geometric prograssion  
a = 3, r = 2

7c.
$\displaystyle\sum_{j=4}^10 (2+3j)$  
mind lower limit  
mind number of terms  
$a_j=2*3j$  
$a_{j+1}=2*3{j+1}$  
$a_{j+2}=2*3{j+2}$

actually is arithmetic prograssion

## q8

Mind index  
can directly use summation euation for geometric progression when the number of terms is approching infinity

$a_0 = \frac{1}{2^{2n}} = \frac{1}{2^{2*0}} = 1$
$a_1 = \frac{1}{2^{2n}} = \frac{1}{2^{2*1}} = \frac{1}{4}$

geometric progression, a = 1, r = $\frac{1}{4}$

$$lim_{n->∞} S_n = lim_{n->∞} \frac{a(1-r^n)}{1-r} = lim_{n->∞} \frac{1(1-\frac{1}{4}^n)}{1-\frac{1}{4}} = \frac{4}{3}$$

## example exam qn:  
$$\displaystyle\sum_{j=0}^8 (3*2^j+(2+3j))$$
$$\displaystyle\sum_{j=0}^8(3*2^j) + \displaystyle\sum_{j=0}^8(2+3j)$$

# Tutorial 2

first few qn are about modulo ops  
middle few qn are about prime factorisationn
last few qn is euclidian and exxtended euclidian

## Q1

normal long division to find remainder  
or write out $a=qm+r$ into $r=a\mod{m}$

## Q2

$a≡b\mod{m}$ means
$a\mod{m} = b\mod{m}$
$a=qm+r$
q can be any integer. Thus a can be -42,-15,12,39 or onwards
since have constraint $0\leq a\leq26$

## Q3

Check remainder of both left and right portions of equation.
if remainders do not match, then not congruent

## Q4

Brute forcce each mod in the bracckets first then add the two remainders  
OR  
use modulo arithmetic property (Addition) formula

NOTE, following equation is incorrect application of the addition formula:  
$(-133\mod{23})+(26\mod{23})=(-133+26)\mod{23}$  

$(-133\mod{23})$, remainder is between 0 and 22  
$(26\mod{23})$, remainder is between 0 and 22  
BUT if add both remainders together, may result in value more than 23. so thats why need mod again

it should be:  
$(a+b)\mod{m} = ((a\mod{m})+(b\mod{m}))\mod{m}$

## Q5

Be careful of exponentiation and mutiplication property of modulo arithmetic

## Q6

any composite int will have at least 1 prime number divisor that is $\leq \sqrt{n}$

Can prove if prime by checking if number mod all primes less than $\sqrt{n}$ = 0

## Q7

rather than do normal prime factorisation, you can check for first prime by using the modulo method,  
e.g. 1001 mod 7 = 0  
hence, 1001 = 7 * 143  
then use the modulo method on 143 again to get 11 * 13  
Thus, 1001 = 7 * 11 * 13  

May need to prove all nums are prime  
e.g. 1111 = 11 * 101, need to prove 101 is prime

## Q8

find all **factors** (not prime factors) of each number $n$ from 1 to $n$  
This helps to prove GCD between 2 nums is 1

e.g.  
15: 1,3,5,15  
11: 1,11  
19: 1,19

## Q9

remember, GCD is min power of **common** prime factors  

if number has no prime facctor, can do power 0 to represent easier  
e.g.  
$(3^5 * 5^5)=(2^0 * 3^5 * 5^5)$

## Q10

Prime factorise both numbers  
find gcd and lcm.  
prove with basic math that $gcd(a,b) * lcm(a,b) = ab$

## Q11

normal euclidian algo, just practice application

## Q12

when applying extended euclidian, be careful when simplifying and when making remainder the subject of the equation

------------

# Tutorial 3 

product rule can be extended to more than 2 ways to do task

subtraction rule is more general form off sum rule

$C(n,r) = \frac{n!}{r!(n-r)!} = \frac{P(n,r)}{r!}$

^^ application of division rule, as order does not matter so items that have the same elements in different order are considered identical.

num pigeonholes always less than num pigeons for pigeonhole principle to work

## q1

a:  
subtask 1: find a position for the bride  
subtask 2: find ordered arrangement of 5-1=4 non-repetitive people out of pool of 10-1=9 people  
$P(9,4) = 3024$
$3024*5=15120$
ans: 15120

b: 
subtask1: find pos for brid  
subtask 2: find pos for groom  
subtask 3: find ordered arrangement of 5-2=3 non-repetittive people out of pool of 10-2=8  
$P(8,3) = 336$
$5*4*336 = 6720$
ans: 6720

c:
subtask 1: brid or groom pos  
subtask 2: dettermine iff bride or groom in pic  
subtask 3: find ordered arrangemenr of $5-1=4$ non-repetitive people out of pool of $10-2=8$  
$P(8,4) = 1680$
$5*2*1680=16800$
ans: 16800

Note: be careful of pool to choose from

## q2

a:
apply product rule, cannot use permutation as arrangement can include repetitive elements  
task determine all 8 bit  
eacch bit is subtask with 2 ways to choose  
num ways to do  is $2^8 = 256$
ans: 256

b:
task: determin positions of four 1's in string
find unordered arrangement off 4 non-repetitive positions out of 10
basically, choose from positions, not choose from 0 or 1  
use combination as the order of the 4 chosen positions does not matter  
$C(10,4)=\frac{10!}{4!(10-4)!}=210$
ans:210

c:
task find num strings that contain at most four 1's
same as b, choose from positions, use combination as order of chosen places does not matter  
set of strings with no 1's: $C(10,0) = 1$  
set of strings with one 1: $C(10,1) = 10$  
set of strings with two 1: $C(10,2) = 45$  
set of strings with three 1: $C(10,3) = 120$  
set of strings with four 1: $C(10,4) = 210$  
apply sum rule  
sum all sets: $1+10+45+120+210=386$  
ans: 386

d:
same idea as part c but for 4-10
set of strings with four 1's: $C(10,4) = 210$  
set of strings with five 1: $C(10,1) = 252$  
set of strings with six 1: $C(10,2) = 210$  
set of strings with seven 1: $C(10,3) = 120$  
set of strings with eight 1: $C(10,4) = 45$  
set of strings with nine 1: $C(10,4) = 10$  
set of strings with ten 1: $C(10,4) = 1$  
apply sum rule  
sum all sets: $210+252+210+45+10+1=386$  
ans: 848

## q3
about permutations

a:  
permutation containing string BCD  
let BCD be X  
number off permutation of letters AEFGX  
$P(5,5) = 5! = 120$

b:  
permutation containing string CFEA  
let CFEA be X
num permutations of BDGX  
$P(4,4) = 4! = 24$

c: 
permutation containing string BA and GF  
let BA = X, GF = Y  
num permutations of CEDXY  
$P(5,5) = 5! = 120$

d:  
permutation containing string ABC and DE  
let ABC = X, DE = Y  
num permutations of FGXY  
$P(4,4) = 4! = 24$  

e:  
permutation containing string ABC and CDEF  
string that contains ABC and CDEF must contain ABCDEF = X
num permutations of GX  
$P(2,2) = 2! = 2$ 

f:
permutation containing string CBA and BED  
string is impossible to simultaneously contain CBA and BED as will require both letter A and letter E to come right after B  
num permutations is 0

## q4

question turns into placing women in slots between men

task: form line with 13 people, 8 men 5 women, so that no woman stands next to another women  

subtask 1: find ordered arangement for 8 non-repetitive men out of pool of 8 men

subtask 2: find ordered arrangement of 5 non-repetitive women out of $8+1=9$ slots


num positions for men: 8  
num positions between men for women: 9
possible pos for men: $P(8,8) = 8! = 40,320$
possible pos for women: $P(9,5) = 15,120$
total num ways to arrange: $40,320 * 15,120 = 609,638,400$

## q5

order of chosen members does not matter, so use combination

subtask 1: find unordered arrangement of 4 non-repetitive men out of pool of 10 men
$C(10,4) = \frac{10!}{4!(10-4)!} = 210$


subtask 2: find unordered arrangement of 4 non-repetitive men out of pool of 15 women
$C(15,4) = \frac{15!}{4!(15-4)!} = 1365$
$210 * 1365 = 286650$

ans: 286650

## q6

find correspondance between question and piggeonholes  
$n$ pigeons placed in $k$ pigeon holes  
at least one **box** contains at least $\lceil\frac{n}{k}\rceil$ pigeons  
"*at least 7 students* get the same **score**"

pigeons: students n  
pigeonholes: possible scores k = 101  

$$\lceil\frac{n}{k}\rceil = \lceil\frac{n}{101}\rceil \geq 7$$
$$= \frac{n}{101} > 7-1$$
$$= n > 6*101 $$
$$= n \geq 607$$

ans: $n \geq 607$

## q7

a;
find correspondance between question and piggeonholes  
$n$ pigeons placed in $k$ pigeon holes  
at least one **box** contains at least $\lceil\frac{n}{k}\rceil$ pigeons 

pairs of int with sum 9 = (1,8), (2,7), (3,6), (4,5)

"there must be a pair on integers with a sum equal to 9" is equivalent to:  
"at least *two selected numbers* belong to **one of the four pairs** above"

pigeons: selected positive int in range [1,8], n=5  
pigeonholes: pairs of int that sum to 9, k=4  

$$\lceil\frac{n}{k}\rceil = \lceil\frac{5}{4}\rceil = 2$$

At least 2 int selected is from one of the four pairs with a sum of 9

b:  
pigeons: selected positive int in range [1,8], n=4  
pigeonholes: pairs of int that sum to 9, k=4  
$$\lceil\frac{n}{k}\rceil = \lceil\frac{4}{4}\rceil = 1$$
At least 1 int selected is from one of the four pairs with a sum of 9

## q8

better to make set of pairs rather than assume all even or all odd

pigeons: houses, n = 51  
pigeonholes: pairs of consecutive addresses, k = 50
$$\lceil\frac{n}{k}\rceil = \lceil\frac{51}{50}\rceil = 2$$

50 pairs of onseccutive addresses: (1000, 1001), (1002, 1003), ... , (1098,1099)
first 50 choose one of two addresses within unique pair
last house will be unable to choose from a unique pair

-----------

# Tutorial 4 
## q1

a. Missing the final exam implies you will not pass the course  
ans: if miss then fail  
b. Having Covid-19 or missing the final exam implies you will not pass the course  
ans: if have covid, then fail or if miss, then fail

|$p$|$q$|$r$|$¬r$|$p → ¬r$|$q → ¬r$|$(p → ¬r) ∨ (q→ ¬r)$|$(p ∨ q) → ¬r$ (wrong)|
|---|---|---|----|--------|--------|--------------------|--------------|
| F | F | F | T  |   T    |   T    |         T          |     T        |
| F | F | T | F  |   T    |   T    |         T          |     T        |
| F | T | F | T  |   T    |   T    |         T          |     T        |
| F | T | T | F  |   T    |   F    |         T          |     F        |
| T | F | F | T  |   T    |   T    |         T          |     T        |
| T | F | T | F  |   F    |   T    |         T          |     F        |
| T | T | F | T  |   T    |   T    |         T          |     T        |
| T | T | T | F  |   F    |   F    |         F          |     F        |

c. You will pass the course if you did not miss the exam or missed the exam due to having having COVID-19  
Ans: either have coccid and miss or do not miss and pass

|$p$|$q$|$r$|$¬q$|$p ∧ q$|$¬q ∧ r$|$(p ∧ q) ∨ (¬q ∧ r)$|
|---|---|---|----|-------|--------|--------------------|
| F | F | F | T  |   F   |   F    |         F          |
| F | F | T | T  |   F   |   T    |         T          |
| F | T | F | F  |   F   |   F    |         F          |
| F | T | T | F  |   F   |   F    |         F          |
| T | F | F | T  |   F   |   F    |         F          |
| T | F | T | T  |   F   |   T    |         T          |
| T | T | F | F  |   T   |   F    |         T          |
| T | T | T | F  |   T   |   F    |         T          |

## q2

'but not' is just 'and not'
'still' is just 'and'
'nevertheless' is just and

'is sufficent' is just 'implies'
'is necessary' is just 'implies'

p is sufficent for q
q is necessary for p

a. $r ∧ ¬q$  
ans: $r ∧ ¬q$  
b. $(p ∧ ¬q) ∧ r$  
ans: $(p ∧ ¬q) ∧ r$  

|$p$|$q$|$r$|$¬q$|$(p ∧ ¬q)$|$(p ∧ ¬q) → r$|
|---|---|---|----|----------|--------------|
| F | F | F | T  |     F    |      T       |
| F | F | T | T  |     F    |      T       |
| F | T | F | F  |     F    |      T       |
| F | T | T | F  |     F    |      T       |
| T | F | F | T  |     T    |      F       |
| T | F | T | T  |     T    |      T       |
| T | T | F | F  |     F    |      T       |
| T | T | T | F  |     F    |      T       |

c. $(p ∧ q) → r$  
ans: $(p ∧ q) → r$  

d. $r ⇔ (p ∨ q)$  
ans: $r ⇔ (q ∨ p)$  


## q3

a.  
p = get to top of Bukit Timah Hill  
q = need to hike 2km  
if you want to get to top of Bukit Timah Hill, then you need to hike 2km  
ans:
p = get to top of Bukit Timah Hill  
q = need to hike 2km  
If you get to the top of Bukit Timah Hill, then you must have hiked 2km

b.  
p = drive more than 650 km  
q = need to buy gasoline  
if you drive more than 650 km, then you will need to buy gasoline.
correct

c.  
Xiaoming will go swimming unless the water is too cold.  
p = water is not too cold  
q = Xiaoming will go swimming  
if the water is not too cold, then Xiaoming will go swimming  

alt ans:
If Xiaoming not swimming, water must be too cold

## q4

a. $(p → q) ⇔ (¬p → ¬q)$  

|$p$|$q$|$¬p$|$¬q$|$(p → q)$|$(¬p → ¬q)$|$(p → q) ⇔ (¬p → ¬q)$|
|:-:|:-:|:--:|:--:|:-------:|:----------:|:-------------------:|
| F | F | T  | T  |    T    |     T      |         T           |
| F | T | T  | F  |    T    |     F      |         F           |
| T | F | F  | T  |    F    |     T      |         F           |
| T | T | F  | F  |    T    |     T      |         T           |

ans$(p → q) ⇔ (¬q → ¬p)$ all true
|$p$|$q$|$¬p$|$¬q$|$(p → q)$|$(¬q → ¬p)$|$(p → q) ⇔ (¬q → ¬p)$|
|:-:|:-:|:--:|:--:|:-------:|:----------:|:-------------------:|
| F | F | T  | T  |    T    |     T      |         T           |
| F | T | T  | F  |    T    |     T      |         T           |
| T | F | F  | T  |    F    |     F      |         T           |
| T | T | F  | F  |    T    |     T      |         T           |

b. $(p ⊕ q) ∧ (p ⊕ ¬q)$  
correct
|$p$|$q$|$¬q$|$(p ⊕ q)$|$(p ⊕ ¬q)$|$(p ⊕ q) ∧ (p ⊕ ¬q)$|
|:-:|:-:|:--:|:--------:|:---------:|:--------------------:|
| F | F | T  |    F     |     T     |          F           |
| F | T | F  |    T     |     F     |          F           |
| T | F | T  |    T     |     F     |          F           |
| T | T | F  |    F     |     T     |          F           |


c. $(p ↔ q) ∨ (¬q ↔ r)$  
correct
|$p$|$q$|$r$|$¬q$|$(p ↔ q)$|$(¬q ↔ r)$|$(p ↔ q) ∨ (¬q ↔ r)$|
|:-:|:-:|:-:|:--:|:-------:|:--------:|:------------------:|
| F | F | F | T  |    T    |    F     |        T           |
| F | F | T | T  |    T    |    T     |        T           |
| F | T | F | F  |    F    |    T     |        T           |
| F | T | T | F  |    F    |    F     |        F           |
| T | F | F | T  |    F    |    F     |        F           |
| T | F | T | T  |    F    |    T     |        T           |
| T | T | F | F  |    T    |    T     |        T           |
| T | T | T | F  |    T    |    F     |        T           |


d. $((p → q) → r) → s$
ccorrect
|$p$|$q$|$r$|$s$|$(p → q)$|$(p → q) → r$|$((p → q) → r) → s$|
|:-:|:-:|:-:|:-:|:-------:|:-----------:|:-----------------:|
| F | F | F | F |    T    |      F      |        T          |
| F | F | F | T |    T    |      F      |        T          |
| F | F | T | F |    T    |      T      |        F          |
| F | F | T | T |    T    |      T      |        T          |
| F | T | F | F |    T    |      F      |        T          |
| F | T | F | T |    T    |      F      |        T          |
| F | T | T | F |    T    |      T      |        F          |
| F | T | T | T |    T    |      T      |        T          |
| T | F | F | F |    F    |      T      |        F          |
| T | F | F | T |    F    |      T      |        T          |
| T | F | T | F |    F    |      T      |        F          |
| T | F | T | T |    F    |      T      |        T          |
| T | T | F | F |    T    |      F      |        T          |
| T | T | F | T |    T    |      F      |        T          |
| T | T | T | F |    T    |      T      |        F          |
| T | T | T | T |    T    |      T      |        T          |

e. $(p ∧ r ∧ s) ↔ (p ∨ q)$
correct
|$p$|$q$|$r$|$s$|$(p ∧ r ∧ s)$|$(p ∨ q)$|$(p ∧ r ∧ s) ↔ (p ∨ q)$|
|:-:|:-:|:-:|:-:|:-----------:|:-------:|:----------------------:|
| F | F | F | F |      F      |    F    |            T           |
| F | F | F | T |      F      |    F    |            T           |
| F | F | T | F |      F      |    F    |            T           |
| F | F | T | T |      F      |    F    |            T           |
| F | T | F | F |      F      |    T    |            F           |
| F | T | F | T |      F      |    T    |            F           |
| F | T | T | F |      F      |    T    |            F           |
| F | T | T | T |      F      |    T    |            F           |
| T | F | F | F |      F      |    T    |            F           |
| T | F | F | T |      F      |    T    |            F           |
| T | F | T | F |      F      |    T    |            F           |
| T | F | T | T |      T      |    T    |            T           |
| T | T | F | F |      F      |    T    |            F           |
| T | T | F | T |      F      |    T    |            F           |
| T | T | T | F |      F      |    T    |            F           |
| T | T | T | T |      T      |    T    |            T           |

## q5

a. correct  
p = Smartphone B RAM > Smartphone A RAM  
q = Smartphone B RAM > Smartphone C RAM  
$p ∧ q = T$

b. correct  
p = Smartphone C ROM > Smartphone B ROM  
q = Smartphone C Camera Resolution > Smartphone B Camera Resolution  
$p ∨ q = T$

c. correct  
p = Smartphone B RAM > Smartphone A RAM   
q = Smartphone B ROM > Smartphone A ROM   
r = Smartphone B Camera Resolution > Smartphone A Camera Resolution  
$p ∧ q ∧ r = F$

d. correct  
p = Smartphone B RAM > Smartphone C RAM   
q = Smartphone B ROM > Smartphone C ROM   
r = Smartphone B Camera Resolution > Smartphone C Camera Resolution  
$(p ∧ q) → r = F$

e. correct  
p = Smartphone A Camera Resolution > Smartphone B Camera Resolution  
q = Smartphone A Camera Resolution > Smartphone C Camera Resolution  
r = Smartphone A RAM > Smartphone B RAM  
s = Smartphone A RAM > Smartphone C RAM  
$(p ∧ q) → (r ∧ s) = F$

## q6

a. correct, is an example of commutative law  
$p ∨ q ≡ q ∨ p$  
sentance is true as truth tables are identical  

|$p$|$q$|$p ∨ q$|$q ∨ p$|
|:-:|:-:|:-----:|:-----:|
| F | F |   F   |   F   |
| F | T |   T   |   T   |
| T | F |   T   |   T   |
| T | T |   T   |   T   |

b. correct. Cannot use laws since laws are for and or nto only  
$p ↔ q ≡ ¬(p → q) ∧ (¬q → p)$  
sentance is not correct. This is because the truth tables for $p ↔ q$ and $¬(p → q) ∧ (¬q → p)$ are not identical  

|$p$|$q$|$¬q$|$p ↔ q$|$¬(p → q)$|$(¬q → p)$|$¬(p → q) ∧ (¬q → p)$|
|:-:|:-:|:--:|:-----:|:--------:|:--------:|:-------------------:|
| F | F | T  |   T   |    F     |    T     |          F          |
| F | T | F  |   F   |    F     |    F     |          F          |
| T | F | T  |   F   |    T     |    T     |          T          |
| T | T | F  |   T   |    F     |    T     |          F          |


c. correct, no law as is implication  
$p ∨ q ≡ ¬p → q$  
sentance is true as truth tables are identical  

|$p$|$q$|$¬p$|$p ∨ q$|$¬p → q$|
|:-:|:-:|:--:|:-----:|:------:|
| F | F | T  |   F   |   F    |
| F | T | T  |   T   |   T    |
| T | F | F  |   T   |   T    |
| T | T | F  |   T   |   T    |

## q7

correct

p = customer’s insurance premium payment DOES arrive by the deadline  
q = email reminder is sent  

original sentance = when $¬p$, $q$  
= $¬p → q$  

**Converse** : swap left and right hand sides  
**Contrapositive** : swap left and right hand sides, NOT both sides  
**Inverse** : NOT both sides  

Therefore:  
Converse: $q → ¬p$  
When an email reminder is sent, customer’s insurance premium payment did not arrive by the deadline.  
Ans: if sent, then payment did not arrive on time

Contrapositive: $¬q → p$  
When an email reminder is not sent, customer’s insurance premium payment did arrive by the deadline.  
Ans: If not sent, payment arrive on time

Inverse: $p → ¬q$
When customer’s insurance premium payment DOES arrive by the deadline, an email reminder is not sent  
Ans: If payment arrives on time, then email not sent

## q8

correct

$¬q ∧ (p → q) → ¬p$  

|$p$|$q$|$¬p$|$¬q$|$(p → q)$|$¬q ∧ (p → q)$|$¬q ∧ (p → q) → ¬p$|
|:-:|:-:|:--:|:--:|:-------:|:------------:|:-----------------:|
| F | F | T  | T  |    T    |      T       |         T         |
| F | T | T  | F  |    T    |      F       |         T         |
| T | F | F  | T  |    F    |      F       |         T         |
| T | T | F  | F  |    T    |      F       |         T         |

Since the Truth Table of $¬q ∧ (p → q) → ¬p$ is all True, $¬q ∧ (p → q) → ¬p$ is a Tautology  

# Tutorial 5

## q1
When all variables in a predicate are given specific values, it becomes a proposition

It is easier to prove an exitental quantifier to be true than false, only need 1 example.

try to eliminnate negation infrom of predicate first

negation outside a quantifier means it can e simplified and is currently not a proposition

|Predicate|True/False/Nether|Explanation|Ans|
|:-------:|:---------------:|:---------:|:-:|
|a. ¬𝑃𝑟𝑖𝑚𝑒(10) ∨ 𝐼𝑛(10,5,20)|True|¬𝑃𝑟𝑖𝑚𝑒(10) = True, True ∨ anything = True|¬𝑃𝑟𝑖𝑚𝑒(10) = True, 𝐼𝑛(10,5,20) = True, ¬𝑃𝑟𝑖𝑚𝑒(10) ∨ 𝐼𝑛(10,5,20) = True ∨ True = True|
|b. ∃𝑛𝑃𝑟𝑖𝑚𝑒(𝑛)|True|Domain given and Prime(2) = True|there exists an integer such that is it a prime number, give example n=2 which is prime, ∃𝑛𝑃𝑟𝑖𝑚𝑒(𝑛) = True |
|c. ∃𝑛¬𝑃𝑟𝑖𝑚𝑒(𝑛)|True|Domain given and ¬Prime(4) = True|there exists an integer such that is is not a prime. example, n = 4 which is not prime,∃𝑛¬𝑃𝑟𝑖𝑚𝑒(𝑛) = true|
|d. ∀𝑛𝑃𝑟𝑖𝑚𝑒(𝑛)|False|Domain given but Prime(4) = False|find counter example, n=4 false|
|e. ∀𝑛¬𝑃𝑟𝑖𝑚𝑒(𝑛)|False|Domain given but ¬Prime(2) = False|find counter example, n=2 false|
|f. ¬∀𝑛𝑃𝑟𝑖𝑚𝑒(𝑛)|True|Domain given and $¬∀n\ Prime(n) \equiv ∃n(¬Prime(n))$, ∃𝑛¬𝑃𝑟𝑖𝑚𝑒(𝑛) proven true in part c.|
|g. ∀𝑛(𝐼𝑛(𝑛, 1,3) → 𝑃𝑟𝑖𝑚𝑒(𝑛))|True|Domain Given, when n!=2, 𝐼𝑛(𝑛, 1,3) = false, 𝐼𝑛(𝑛, 1,3) → 𝑃𝑟𝑖𝑚𝑒(𝑛) = true. When n = 2, 𝐼𝑛(𝑛, 1,3) = true an 𝑃𝑟𝑖𝑚𝑒(𝑛) = true.| when n!=2, 𝐼𝑛(𝑛, 1,3) = false, means n = 1 is counter example, ans is false| 
|h. ∀𝑛(𝐼𝑛(𝑛, 8,10) → 𝑃𝑟𝑖𝑚𝑒(𝑛))|False|Domain given but when n=9, 𝐼𝑛(𝑛, 8,10) =True but 𝑃𝑟𝑖𝑚𝑒(𝑛) = False, thus 𝐼𝑛(𝑛, 8,10) → 𝑃𝑟𝑖𝑚𝑒(𝑛) = False|when n=8, 𝐼𝑛(𝑛, 8,10) = False, counterexample so proposition is false|
|i. ∀𝑛(𝐼𝑛(𝑛, 𝑎, 𝑏) → ¬𝑃𝑟𝑖𝑚𝑒(𝑛)), Where 𝑎 and 𝑏 are integer smaller than 10|||for every integerr, if it is larger than or equal to a and smaller than or equalt to b, then it is not a prime number. neither true or false as no values give.|
|j. ∃𝑛𝑃𝑟𝑖𝑚𝑒(𝑛) → 𝐼𝑛(𝑛, 30,40)|||if there exists an integer that is prime number, then n is larger or equal to 30 and smaller than or equal to 40. The IN() is not a proposition as has a variable. ∃𝑛𝑃𝑟𝑖𝑚𝑒(𝑛) is a proposition as has quantifier and we can suggest an example. since cannot get truth value of 𝐼𝑛(𝑛, 30,40), overall statement is neither true or false|

## q2
Let 𝐵𝐵(𝑥) be the statement “𝑥 plays basketball every week”, where the domain of 𝑥 is all students of ICT. Express each of the following in English:  
. ∃𝑥𝐵𝐵(𝑥)  
- There is a student of ICT who plays basketball every week; correct  

b. ∀𝑥𝐵𝐵(𝑥)  
- All students of ICT play basketball every week; correct  

c. ¬∀𝑥𝐵𝐵(𝑥)  
- Not every students of ICT play basketball every week; correct  

d. ∃𝑥¬𝐵𝐵(𝑥)  
- There is a student of ICT who does not play basketball every week; correct  
- alt representation: ∃𝑥¬𝐵𝐵(𝑥) = ¬∀𝑥𝐵𝐵(𝑥)  

## q3

all correct

a. i. Cal(x): x knows calculus, domain: all rabbits, statement: ¬∃𝑥 Cal(x) = ∀𝑥 ¬Cal(x)  
   ii. ¬¬∃𝑥 Cal(x) = ∃𝑥 Cal(x)  
   iii. There exists a rabbit that knows calculus  

b. i. Talk(x): x can talk, domain: all birds, statement: ∃𝑥 Talk(x)  
   ii. ¬∃𝑥 Talk(x) = ∀𝑥 ¬Talk(x)  
   iii. All birds cannot talk  

c. i.F(x): x knows French  R(x): x knows russian, domain: all students in this class, statement: ∀𝑥 ¬(F(x)∧R(x)) / ¬∃𝑥 (F(x)∧R(x))  
   ii. ¬∀𝑥 ¬(F(x)∧R(x)) = ∃𝑥 (F(x)∧R(x))  
   iii. There is someone in this class who knnows French and Russian  

d. i. M(x): x is a Marvel FFan, domain: all students in this class, statement: ∀𝑥 M(x)  
   ii. ¬∀𝑥 M(x) = ∃𝑥 ¬M(x)  
   iii. There is a student in this class who is not a Marvel Fan  

## q4

a.  
Credits (x,y): x has taken y credits thus semester  
A(x,y): student x recieved an 'A' grade in module y  
∃𝑥(Credits(x,21)∧∀y(x,y)), domain: all students; correct  

b.  
M(x,y): passenger x flies more than y miles in a year  
F(x,y): passenger x takes more than y flights in a year  
Q(x): passenger x qualifies as an 'Elite Flyer'  
Q(x) → M(x,25000) ∨ F(x,25), domain: all airline passengers; wrong
∀x(M(x,25000)∨ F(x,25) → Q(x)); corrction

c.  
M(x,y): Man x previous best time < y hours  
W(x,y): Woman x previous best time < y hours  
Q(x): person x qualifies for the marathon  
Q(x) → M(x,3) ∨ W(x,3.5), domain: all applicants; wrong

Man(x): x is a man
Woman(x): x is a woman
Best(x,y): best previous time of x is less than y hours
Q(x): x qualifies for the marathon
∀x((Man(x) ∧ Best(x,3)) ∨ (Woman(x) ∧ Best(x,3.5))); correction


## q5
a. 
some students: ∃𝑥  
and: ∧  
|domain: all students|domain: all people|
|-|-|
|∃𝑥(L(x) ∧ D(x))|S(x): x is a student in this class|
||∃𝑥(S(x) ∧ L(x) ∧ D(x))|

b. 
all students: ∀𝑥  
all macOS users have a laptop: →  
|domain: all students|domain: all people|
|-|-|
|∀x(M(x) → L(x))|S(x): x is a student in this class|
||∀𝑥((S(x) ∧ M(x)) → L(x))|

c.  
all students: ∀𝑥  
either or both: ∨  
|domain: all students|domain: all people|
|-|-|
|∀x(M(x) ∨ W(x))|S(x): x is a student in this class|
||∀𝑥(S(x) → (M(x) ∨ W(x)))|

## Q6

quantifiers have no intrinsic precedence, do left to right  
expect readable English sentance instead of plain translation of quantified predicate  

a.  
∀x∃y(x < y), domain of x and y: all real numbers  
for every real number x, there is another real number y, such that y is larger then x.  
there is no largest number  

b.  
∀x∀y((($x \geq 0$) ∧ ($y \geq 0$) → ($xy>=0$)))  
for every combination of real numbers x and y, if x is no-negative and y is non-negative, xy is non-negative  
product of two non negative numbers is also non negative  

c.  
∀x∀y∃z($x + y = z$)  
For every combination of real numbers x and y, there is a real number z,  is the sum of x and y  
the sum of two real numbers is a real number  


## q7

F(x,y): x and y are friends  
domain: all students in SIT

a.  
∀x∃y(F(x,y)∧∀z((y != z) → ¬F(x,z)))  
for every SIT student x, there is one SIT student y, such that x and y are friends. and for every student z, if z is different from y, then x and z are not friends  
for every SIT student x, there is one SIT student y, such that x and y are friends, and there is no other SIT student who is considered a friend of x  
Every sit student has exactly one friend

b.  
∃∀y∀z(F(x,y) ∧ F(x,y) ∧ (y != z) → ¬F(x,z))  
There is a student x, for every combinatino of student y and z, if x and y are friends, and x and z are friends, and y and z are different students, then y and z are not friends  
There is a student x, whose every combination of two friends are not friends with each other.  
There is a student whose SIT friends are not friends with each other


# Tutorial 6

## q1

a:  
p: work all night  
q: ans all q  
r: understand  

premise 1 : p → q  
premise 2 : q → r  
conclusion: p → r  

rule used: hypothetical syllogism  

b:  
p: n is real, n>3  
q: n is real, 2n>6  
r: n>=2  

premise 1: p → q  
premise 2: r  
conclusion: r → q  
cannot conclude (q could be either true or false)  

rule used: None

c:  
p: snows  
q: uni is closed  

premise 1: p → q  
premise 2: ¬q  
conclusion: ¬p  

rule used: modus tollens


d:
p: stay in sun too long
q: go swimming

premise 1: q ∨ p $\equiv$ p ∨ q  (commutative law)  
premise 2: ¬p  
conclusion: q

rule used: disjunctive syllogism

e:
p: n is real, n>2  
q: n is real, $n^2$>4  

premise 1: p → q  
premise 2: ¬q  
conclusion: ¬p  

rule used: modus tollens

## q2

p: rains  
q: foggy  
r: sailing race held  
s: lifesaving demo  
t: trophy

1) premise a: ¬p ∨ q → r ∧ s  
2) premise b: r → t  
3) premise c: ¬t  
conclusion: p

steps:  

4) from 1) : ¬p ∨ q → r  
rules used: hypothetical Syllogism and Simplifiction

5) from 2) : ¬r
rule used: moodus tollens

6) from 4) and 5): ¬(¬p ∨ q) $\equiv$ p ∧ ¬q
rule used: De Morgan's law

7) from 6): p
rule used: simplification

## q3

p: is raining  
q: has umbrella  
r: does snot get wet  

Premise a: ¬p ∨ q  
Premise b: q → r  
Premise c: p ∨ r  
conclusion: r

steps:  
1) Premise a: ¬p ∨ q  
2) Premise b: q → r  
3) Premise c: p ∨ r 
4) from 1) and 3): q ∨ r 
rule used: resolution 
5) from 2): q → r $\equiv$ ¬q ∨ r (in formula sheet)  
6) from 4) and 5): r ∨ r $\equiv$ r (Idempotent Law)  
rule used: Resolution

## q4

Premise a: (p ∨ q) ∧ (¬p → ¬q)
Premise b: p → r

steps:  
1) Premise a: (p ∨ q) ∧ (¬p → ¬q)
2) Premise b: p → r
3) from 1): p ∨ q
rule used: simplification
4) from 1): ¬p → ¬q
5) from 4): ¬p → ¬q $\equiv$ ¬(¬p) ∨ ¬q $\equiv$ p ∨ ¬q (De morgan)
6) from 3) and 5): p ∨ p $\equiv$ p (resolution)
7) from 2) and 6): r (modus ponens)
8) from 7): r ∨ t (addition)


## q5

premise a: (p → q) ∧ (r → s)
premise b: p
premise c: ¬s

steps:
1) premise a: (p → q) ∧ (r → s)  
2) premise b: p  
3) premise c: ¬s  
4) from 1) (p → q)  
5) from 1) (r → s)  
6) from 2) and 4)q (modus ponens)  
7) from 3) and 5) ¬r (modus tollens)  
8) from 6) and 7) q ∧ ¬r  (conjunction)

## q6

S(x): x is student in class
P(x): x passed first calss test

premise 1: ∀x(S(x) → P(x))  
premise 2: S(Alice)  
Conclusion: P(Alice)  

steps:  
1) premise 1: ∀x(S(x) → P(x))
2) premise 2: S(Alice)
3) from 1): S(Alice) → P(Alice) (Universl Instantiation)
4) from 2) and 3): P(Alice), (Modus Ponens)


J(x): x is junior
I(x): x is ICT stuent
C(x): x on campus on weekend

Premise 1: ∀x(J(x) → ¬C(x))  
Premise 2: ∃x(I(x) → ¬J(x))  
Conlusion: ∃x(I(x) ∧ C(x))  

Steps:  
1) Premise 1: ∀x(J(x) → ¬C(x))  
2) Premise 2: ∃x(I(x) → ¬J(x))  
3) from 2): I(a) ∧ ¬J(a) (existential instantiation)  
4) from 3): I(a) (simplification)  
5) from 3): ¬J(a) (simplification)  
6) from 1): J(a) → ¬C(a) $\equiv$ C(a) → ¬J(a) (Contrapositive)
7) from 5) and 6): cannot conclude C(a) (C(a) can be either true or false based on truth table)
8) from 4) and 7): cannot conclude I(a) ∧ C(a)
9) from 8): cannot conclude ∃x(I(x) ∧ C(x)) (existential generalisation)


P(x): x likes fruit
Q(x): x is a parrot

Premise 1: ∀x(Q(x) → P(x))
Premise 2: ¬Q(my pet bird)
conlusion: ¬P(my pet bird)

steps:  
1) Premise 1: ∀x(Q(x) → P(x))  
2) Premise 2: ¬Q(my pet bird)  
3) from 1): Q(my pet bird) → P(my pet bird) (Universal Instantiation)
4) from 2) and 3) cannot conclude ¬P(my pet bird) (based on truth table)


P(x): x eats granola every day
Q(x): x is healthy

Premise 1: ∀x(P(x) → Q(x))  
Premise 2: ¬Q(Linda)
Conclustion: ¬P(Linda)  

1) Premise 1: ∀x(P(x) → Q(x))  
2) Premise 2: ¬Q(Linda)
3) from 1): P(Linda) → Q(Linda) (Universal Instantiation)  
4) from 3):
????????????//

## q7

step 2 incorrect. Changes from Existential into Universal. Can use normal rules of inference as each quantified expression can be treated as a proposition (x(P(x)))

step 3 incorrect, should be existential not universal

step 4 incorrect: should be existential ot universal

step 5 incorrect: should be existential instantiation not generalisation from 4

step 6 incorrect should be conjunction but of different specific values

step 7 is invalid

|step|proposition|reason|
|-|-|-|
|1|∃xP(x) ∧ ∃xP(x)|Premise|
|2|~~∀xP(x)~~ ∃xP(x)|Simplification from (1)|
|3|P(c)|~~Universal~~ Existential Instantiation from (2)|
|4|~~∀xQ(x)~~ ∃xQ(x)|Simplification from (1)|
|5|Q(C)|Existential ~~generalisation~~ instantiation from (4)|
|6|~~P(c) ∧ Q(c)~~ P(c1) ∧ Q(c2)|~~Simplification from (3) and (5)~~ Conjunction|
|7|∃x(P(x) ∧ Q(x))|~~Existential generalisation from(6)~~ Invalid|



# Tutorial 7

for ∃x (p(x) → q(x)), if q(x) is always false, find a p(c) for some value c such that p(c) → q(c) is true

for ∀x (p(x) → q(x)), if q(x) is always false, go for disprove because universal is easier, so fins a p(c) for some value c such that p(c) → q(c) is false

for ∀x (p(x) → q(x)), if q(x) is always true, cannot find a p(c) for some value c such that p(c) → q(c) is false, so go for direct proof

if asked to prove or disprove, do which ever is easier first, i.e. existentia do prove, universal do disprove

irrational numbers do not have enough properties to prove things.  
meanwhile, rational numbers have properties like all rational numbers can be represented by x/y where x and y are rational numbers  
so for prove irrational number questions, consider proof by contraposition

contrapositive of ∃x (p(x) → q(x)) is ∃x (-q(x) → -p(x)) 
negation of ∃x (p(x) → q(x)) is ∀x (p(x) $\land$ -q(x))

## Q1

p: a + b are two odd integerrs  
q: a+b is even  
prove p → q  

1) a and b are two odd integers | assuming p  
2) ∃x ∈ Z, ∃y ∈ Z, a = 2x +1, b = 2y+1 | by definition  
3) a+b = (2x+1) + (2y+1) = 2*(x+y+1) | By 2)  
4) a + b is an even integer | by definition (proving q)  
5) Sum of two odd integers is even | p → q  

## Q2

p: n is an odd integerrs  
q: 5n+6 is odd  
prove p ↔ q by first proving p → q then proving q → p (p → q) 

1) a and b are two odd integers | assuming p
2) ∃x ∈ Z, ∃y ∈ Z, a = 2x +1, b = 2y+1 | by definition
3) a+b = (2x+1) + (2y+1) = 2*(x+y+1) | By 2)
4) a + b is an even integer | by definition (proving q)
5) Sum of two odd integers is even | p → q

## Q3

p: $n^3+5$ is odd
q: n is evven
prove p → q  

b.  
by contradiction  
¬(p → q) $\equiv$ ¬(¬p∨q) $\equiv$ p∧¬q

1) $n^3+5$


## Q4

p: m+n and n+p are even integer
q: mm+p is even
prove p → q  

1) m+n and n+p are even integers | assuming p
2) ∃x ∈ Z, ∃y ∈ Z, m+n = 2x +1, n+p = 2y+1 | by definition
3) m = 2x-n, p = 

## Q5

## Q6

## Q7

## Q8

## Q9