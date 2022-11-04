2022-10-17
09:57 pm

Tags: #note

Topics: [[Probability & Statistics]]

# Applications Of Continuous Distributions
---


## Deductible Insurance

Consider a given loss amount [[Random Variable]] $X$ living on the interval $(A, B)$ where $0\le A<B<\infty$. We denote the deductible amount by $d$, where $A\le d<B$. Let $Y$ be the payment random variable resulting from the deductible $d$. Then the relationships between $X$ and $Y$ is given by

$$
Y=\begin{cases}
0 & A\le X<d \\
X-d & d\le X<B
\end{cases}
$$
Often a problem will ask for $E\:[Y]$, the [[Expected Value]] of $Y$ (how much the insurance company pays out).

$$E[Y]=\int_A^d0\cdot f_X(x)\:dx\:+\int_d^B(x-d)\cdot f_X(x)\:dx$$
$$=\int_d^B(x-d)\cdot f_X(x)\:dx$$


## Capped Insurance

Another common practice for reducing $Y$ is to cap the covered loss at a given constant, $C$, which is less than the maximum actual loss $B$. Then the relationship between $X$ and $Y$ is given by 

$$
Y=\begin{cases}
X & A\le X<C \\
C & C\le X<B
\end{cases}
$$

The expected value:

$$E[Y]=\int_A^Cx\:f_X(x)\:dx\:+\int_C^BC\: f_X(x)\:dx=\int_A^Cx\:f_X(x)\:dx\:+C\int_C^Bf_X(x)\:dx$$
$$=\int_A^Cx\:f_X(x)\:dx\:+C\cdot Pr[X>C]$$


## The CDF Method for Deductible and Caps

The following are compact formulas in terms of the [[Cumulative Distribution Function]] of $X$ for capped benefits, benefits with a deductible, and a combined policy.

Let $X$ be a continuous loss random variable with domain $(A,\:B);\:0\le A<B$, and let $C$ be any number such that $A<C<B$.

Let $Y^C$ (benefit capped at C) be

$$
Y^C=\begin{cases}
X & A\le X<C \\
C & C\le X<B
\end{cases}
$$

Let $Y_d$ (benefit with deductible of d) be

$$
Y_d=\begin{cases}
0 & A\le X<d \\
X-d & d\le X<B
\end{cases}
$$

Let $Y_d^C$ (benefit with deductible of d and cap of C) be

$$
Y_d^C=\begin{cases}
0 & A\le X<d \\
X-d & d\le X<C \\
C-d & C\le X<B
\end{cases}
$$

Then the following properties are true

$$(i)\qquad X=Y^C+Y_d$$
$$(ii)\quad E[Y^C]=A+\int_A^C[1-F_X(x)]\:dx$$
$$(iii)\quad E[Y_d]=\int_d^B[1-F_X(x)]\:dx$$
$$(iv)\qquad Y_d^C=Y^C-Y_d$$
$$(v)\quad E[Y_d^C]=\int_d^C[1-F_X(x)]\:dx$$



---
# References

- [[Probability and Statistics with Applications#Chapter 5 5 Applications to Insurance Deductibles and Caps]]
