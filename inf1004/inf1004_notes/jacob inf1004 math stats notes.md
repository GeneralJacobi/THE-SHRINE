
# tutorial timetable

- Wk2: descriptivve stats + probability theory
- Wk3: Probability theory +Discrete probability distribution
- Wk4: Continuous probability distribution (Q1-6)
- Wk5: Sampling distributions (Q7-10)
- Wk6: revision

Show workings in exams
Blue / black pen only in exam
expected to attempt tutorial qn before class
open mouth and ask qns if dk
solve qns independently and correctly
# Chap 1: Descriptive Statistics

### Formulas & Symbols

| Parameter (population) / Statistic (Sample) | Populaion                  | Sample            |
| ------------------------------------------- | -------------------------- | ----------------- |
| Mean                                        | $\mu$ / mu                 | $\bar{x}$ / x-bar |
| Variance                                    | $\sigma^2$ / sigma squared | $s^2$ / s squared |
| Standard Deviation                          | $\sigma$ / sigma           | $s$ / just s      |
| Proportion                                  | p / just p                 | $\hat{p}$ / p-hat |

general formula for mean = $\frac{ x_1f_1 + x_2f_2 + ... + x_kf_k}{ n }$ = $\frac{ \displaystyle\sum_{} x_if_i } {n}$

mean (discrete data) = $\frac{ \displaystyle\sum_{} x_i } {n}$   
- $x_i$ = each value from set
- no $f_i$ as frequency for each discrete data is 1

mean (grouped data) = $\frac{ \displaystyle\sum_{} {group\ average}_i \times {group\ frequency}_i} {n}$   

median (odd num of values) = middle num
median (even num of values) = two middle nums / 2
median (grouped data) = $L_m + (\frac{ \frac{n}{2} - cf_{m-1} }{ f_m })w_m$
- n = number of values
- $L_m$ = Lower bound of class containing median
- $f_m$ = frequency of class containing median
- $cf_{m-1}$ = cumilative freq of class before median class
- $w_m$ = width of class containing median (e.g. category range is 20-60, so $w_m$ is 40 )

Population variance $\sigma^2$ = $\frac{\displaystyle\sum{} (x_i - \mu)^2}{N}$  
Alt formula = $\frac{1}{N}[\displaystyle\sum{}x_i^2 - \frac{(\displaystyle\sum{}x_i)^2}{N}]$
- $x_i$ = each value from set
- $\mu$ = set mean
- N = population size
- 
- note
- may be easier to use alt formula when you do not have the mean or difference to mean for each val

Sample variance $s^2$ = $\frac{\displaystyle\sum{} (x_i - \bar{x})^2}{n - 1}$  
Alt formula = $\frac{1}{n-1}[\displaystyle\sum{}x_i^2 - \frac{(\displaystyle\sum{}x_i)^2}{n}]$
- $x_i$ = each value from set
- $\bar{x}$ = sample mean
- n = sample size
- is n-1 for precision
- 
- note
- may be easier to use alt formula when you do not have the mean or difference to mean for each val

standard deviation = $\sqrt{varience}$ = $\sqrt{\frac{\displaystyle\sum{} (x_i - \mu)^2}{N}}\ \ \ OR\ \ \ \sqrt{\frac{\displaystyle\sum{} (x_i - \bar{x})^2}{n - 1}}$  
- $x_i$ = each value from set
- $\mu$ = set mean
- n = set size

InterQuartile Range (IQR) = $Q3 - Q1$
- Q1 = median of lower quartile
- Q3 = median of upper quartile

coeffecient of variation = CV = $\frac{\sigma}{\mu} * 100\%$ OR $\frac{s}{\bar{x}} * 100\%$
- $\sigma$ = population standard deviation
- $\mu$ = mean
- $s$ = sample standard deviation
- $\bar{x}$ = sample mean

Proportion (Population)  $P_i = \frac{f_i}{N}$
Proportion (Sample)  $\hat{p_i} = \frac{f_i}{n}$

$f_i$ = frequency of specific category
N = $\displaystyle\sum{f_i}$ (All data)
n = size of sample


$Outlier < [Q1 - 1.5(IQR)]$
OR
$Outlier < [Q3 + 1.5(IQR)]$

### types of stats:  
Descriptive : 
- needs collecting, 
- Organizing, 
- Summarizing, 
- Presenting of Data, 
- only deal with outcome from sample data  
Inferential : 
- Making inferences,
- Hypothesis testing, 
- Making predictions, 
- Determining relationships, 
- given the outcome, infere for the popultion
Probability Theory: 
- Understanding the uncertainty of data, 
- given the population and sample size, predict the probability of an outcome

descriptive generally tells you the population size, or only describes the outcome

inferential generally does not say source or population size, may make assumptions of the population based on info from the outcome, may add on further ideas to the outcome or inferences from the outcome

these 2 stats will result in different presentation of the data
---e.g.---
280 randomly selected people in town  
210 have last name Nicolussi  
Descriptive: 220 (75%) of these 280 people have last name Nicolussi  
Inferential: 75$ of all people living in italy have the last name Nicolussi

on last 3 sundays, Henry sold 2,1,0 cars respectivly  
descriptive: Henry averaged 1 new car sold, per Sunday, for the last 3 Sundays  
inferential: Heney never sells more than 2 cars on a Sunday
\---------

### Stats can be misused

Ambiguity:  
Bank A: "Our interest rates are 1% lower"  
Ambiguity 1: lower than which bank?  
ambiguity 2: if Bank B = 2%, is Bank A 1% or 1.98%  

Misleading:  
President Trump's approval rating amoing Latinos going up to 50%  
National Polling results for only 153 Latino voters  
Mean Margin of error is +- 9.9%
all stats will have margin of error  


For accuracy, should collect census of whole population but impractical/immpossible (may miss people who have left which turns the census into a sample; or maybe take too long)  
so use sample, which is a smaller subset of population, which should be fair (in terms of reasonably similar distribution to the rest of the population and of a sufficent size to reflect overall trends in population) in order to infer for population

Parameter - a summary number describing **POPULATION**  
	$\mu$ / mu - mean  
    $\sigma^2$ / sigma squared - varience  
    $\sigma$ / sigma - standard deviation  
    $p$ - population

Statistic - a summary number for a **SAMPLE**  
    $\bar{x}$ / x bar - mean  
    $s^2$ / s squared - varience  
    $s$ / s - standard deviation  
    $\hat{p}$ / p hat - proportion / sample  

### Types of data
Qualitative data:
describe characteristic / quality of variable
scale of measurement is a set of catagories / split into various categories (even if they are numerical like zipcodes)  
there is no "larger" or "smaller" to these values  
e.g.  racial groups

Quantitative data:
numerical, differ in magnitude
can be used in calculations
scale for measurement has numerical values that represent different magnitudes of the variable  
"larger / greater than" and "smaller / less than" are relevant and important
e.g. height weight

types of quatitative data:  
Diesccrete (countable)  
Continuous (non-countable) (possible infinite precision and total if the precision of the measuring instrument was not a limiting factor)  

qualitative categorical data commonly presented as bar or pie chart

quantitative data can be identified as frequencey distribution as well, shown in histogram

large data set / quantitative continuous data, can use classes covering continnuous non-overlapping range of values to group data together

Crosstabulation shows relationship between 2 variables, either can be qualitative/quantitative data  


## Frequency analysis

to quantify qualitative/categorical data 

Tally total
Obtain frequency of each
calculate relative frequency

Use pie chart/bar chart to represent frequency

Collection of all categories and their corresponding relative frequencies = the relative frequency distribution of a variable

once calculate relative frequency can display in histogram of frequency on y axis and quantitative value on x axis marking the left and right boundary of the category

can change histogram from freq analysis to percentage on y axis and each category mean on x axis

for big ass set of quantitative continuous data, tend to group data into categories to be able to present more succinctly

recommend 5 - 14 classes on contiuous non-overlapping
### Formula

$P_i = \frac{f_i}{N}$
$\hat{p_i} = \frac{f_i}{n}$

$f_i$ = frequency of specific category
N = $\displaystyle\sum{f_i}$ (All data)
n = size of sample

## Bivarate Data

sometimes categories may have to be broad to make the histogram with contiguous data
will skew how histogram looks if using raw frequency on x axis

using density on y axis will give more accurate chart

Density = $\frac{Relative\ frequenccy}{Class\ Width}$

| Histogram (Density)                                                                  | Barchart                                                          |
| ------------------------------------------------------------------------------------ | ----------------------------------------------------------------- |
| Bars cannot be reorderd                                                              | Categorical                                                       |
| bars width represent bins/classes/intervals of values<br>can be of different lengths | bars widths is the same<br>Width no meaning                       |
| no gaps ( if have gap, value in that range is 0)                                     | May have gaps between bars for visual neatness<br>Gaps no meaning |
| used to see distributions                                                            | Height of archart is frequency                                    |
|                                                                                      | Barchart compares variables                                       |

## Cross Tabulation

To find relationship between 2 variables
Variables can be different types of data; qualitative or quantitative

Cross tabulation creates a contingency table

for quantitative data, create ranges and use the ranges in the contingency table
so the table wil have qualitative categories on one axis and  ranges on the other

rmbr add totals column/row for each axis

contingency table can be presented as clustered/stacked bar chart
clustered chart: easier to see distribution
stacked chart: easier to proportion

## Mean Mode Median / measures of concentration of data
Individual values used to express collecction of data
diffreent ways to measure concentration of data
by itself, insufficient to summarize whole dataset

Mean Average
Mode most common
Median middle most

for grouped data, given the mean for each range and the frequency of each range


if mean < median  &&  mean < mode : negatively skewed
mean = median = mode :  perfect normal distribution / not enuf data lol
if mean > median  &&  mean > mode : positively skewed

unimodal: only 1 value which is most frequent
bimodal: 2 values which is most frequent OR 2 distinct peaks in histogram
trimodal: 3 values which is most frequent OR 3 distinct peaks in histogram
quadmodal: 4 values which is most frequent OR 4 distinct peaks in histogram

## Outliers
outliers heavily influence the mean of a set
may cause misleading due to skewing of data

solutions:
1. remove outlier
2. use median instead

### Formula for proving outlier

$Outlier < [Q1 - 1.5(IQR)]$
OR
$Outlier < [Q3 + 1.5(IQR)]$

![[outlier.png]]

## Variance and standard deviation / measures of spread of data

- Range
	- Highest_val - lowest val
	- Susceptible to outliers, which may make range look very big
- Interquartile Range
	- upper_quartile Q3 - lower_quartile Q1
	- Middle quartile Q2= median
	- describes spread around the middle
	- we will use exclude method for the module
	- i.e.
	- 3,4,4,5,6,8,8
		- 5 is q2, exclude from sets to find q1 and q3
	- 1,3,4,4,5,6,6,7,8,8
		- q2 = (5+6)/2; 
		- 5 is part of q1 set
		- 6 is part of q3 set
- Varience
	- Average of the distances (squared deviations) from the mean
	- Bigger distinction than standard deviation between values further away from the mean cus squared
	- $\frac{\displaystyle\sum{} (x_i - \mu)^2}{N}\ \ \ OR\ \ \ \frac{\displaystyle\sum{} (x_i - \bar{x})^2}{n - 1}$
		- $x_i$ = each sample in set
		- $\mu$ = population mean
		- N = population size
		- $\bar{x}$ = sample mean
		- $n$ = sample size
- Standard Deviation
	- the difference between each data point from the mean
	- $\sqrt{\sigma^2}\ \ \ OR\ \ \ \sqrt{s^2}$

box plot:
- ![[box_plot_example.png]]

## Coefficient of Variance
measure of relative variability
ratio of standard deviation to mean
also called risk


# Chap 2: Probability theory

## How to interpret probability

Mathematical definition:
- a number between 0 and 1 (inclusive) that is assigned to a random outcome of uncertainties

Interpretations of probability;
- Classical (theoretical) probability
	- all random outcomes are equally likely to occur
	- can only use classical probability formula when all events equally likely
- Relative frequency (Empirical) probability

## Classical Probability

P(A) = Number of different outcomes in A / Total number f possible outcomes
- there may be more events after A so count all final states after event A
- P(A) = f/N
- f = num outcomes of A
- N = total outcomes

## Relative Frequency Probability
Collect data over time / use existing past data

P(A) = $\frac{f}{N}$
- f = number of times the outcome occurs
- N = total number of observations

Possible Concerns:
- how many times are considered a long run
- What if the outcome cannot be repeated
- What if no past data as is new situation

## Probability of events

note regardless of which interpretation you use, theory of probability applies to both

Sample Space (S)
- Set of all possible outcomes of a random phenomenon
- Is the box in Venn Diagram
Event (A)
- set of all outcomes we are interested in
- is circle/ellipse within sample space inn Venn Diagram

![[probability.png]]

0 < P(A) < 1
P(S) = 1

## Complementary

Probability event A does not happen = A\` = 1 - P(A)

## Multiple Events occur

Event A = P(A)
Event B = P(B)

Event A OR B  P(A∪B) = P(A) + P(B) - P(A∩B)
Minus for double count

Event A AND B = P(A∩B)


Mutually Exclusive;
- P(A∩B) = 0
- P(A∪B) = P(A) + P(B)

## Conditional Probability

### Formula
P(A|B) = $\frac{P(A∩B)}{P(B)}$
P(B|A) = $\frac{P(A∩B)}{P(A)}$

P(A|B) read as P(A) given B occurred

P(A|B) $\neq$ P(B|A)

P(A|B) $\neq$ P(A∩B)

Reason:
![[Conditional_probability.png]]

## Multiplicative Rules

From P(A|B) = $\frac{P(A∩B)}{P(B)}$
we have P(A∩B) = P(A|B)P(B)

P(A∩B) means B happened first then A, which is why we multiply the chance of B happening with the chance of A happening after B

## Independent vs Mutually exclusive 

Mutually Exclusive:
- Definition: Cannot happen simultaneously
- Dependency: Occurrence of one event results in the NON-occurrence of the other
- Probability of both events happening P(A∩B) = 0
- Venn Diagram: sets do not overlap
- Must be dependent because occurrence of one event affects the other 
Independent:
- Definition: occurrence and outcome of 1 event does not control occurrence or outcome of other event
- Dependency: Occurrence of one event has no influence on the occurrence of the other
- Probability of both events happening P(A∩B) = P(A) - P(B)
- Venn Diagram: sets overlap
- Cannot be mutually Exclusive as both events can happen together

| When event are:    | P(A or B) is:            | P(A and B) is | P(A\|B) is:                 |
| ------------------ | ------------------------ | ------------- | --------------------------- |
| Mutually Exclusive | P(A) + P(B)              | 0             | 0                           |
| Independent        | P(A) + P(B) - P(A)P(B)   | P(A)P(B)      | P(A)                        |
| Any                | P(A) + P(B) - P(A and B) | P(A)P(B\|A)   | $\frac{P(A\ and\ B)}{P(B)}$ |

If P(A|B) = P(A) and P(B|A) = P(B),
A and B are independent events

If A and B are independent, 
P(A∩B) = P(A)P(B)

Can extend to repeat of same event if Independent from itself
$P(A_1∩A_2∩A_3∩...∩A_n) = P(A_1)P(A_3)P(A_2)...P(A_n)$

Tree diagram helpful when time / order is involved
Write probability of individual event on each branch


## Bayes Theorem

exhaustive events: P(A∪B) = P(S) = 1
is any number of events covers all possible outcomes, the set of all participating events is considered exhaustive (the union of this set of events is exhaustive)

### Law of total probability

Given a set of ***mutually exclusive and exhaustive events ($S_1...S_k$)**,* probability of event A (P(A)) can now be expressed using the law of total probability

P(A) = P(A∩$S_1$) + P(A∩$S_2$) + ... + P(A∩$S_k$)

rewrite with multiplicative rule
P(A) = P(A|$S_1$)P($S_1$) + P(A|$S_2$)P($S_2$) + ... + P(A|$S_k$)P($S_k$)


### Back to Bayes-ics theorem
Using conditional probability equations, 
P(A|B) = $\frac{P(A∩B)}{P(B)}$
P(B|A) = $\frac{P(A∩B)}{P(A)}$
Bayes combines the 2 into P(B|A) = $\frac{P(A|B)P(B)}{P(A)}$

Which then he rewrite denominator using law of total probability,
set of mutually exclusive exhaustive events are B and B\`
P(B|A) = $\frac{P(A|B)P(B)}{P(A|B)P(B) + P(A|B^`)P(B^`)}$

Bayes theorem useful when data given only has 1 specific event first as well as the probability of that event e.g. always A first then B, P(A) given


# Chap 3

Random variable:
- Denoted with capitol letter
- Possible values are numerical outcomes of a random phenomenon
