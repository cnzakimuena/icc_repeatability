# Intraclass Correlation Coefficient
Script to generate test-retest reliability (relative repeatability) of a measurement using the intraclass correlation coefficient (ICC) ([Rajaratnam, 1960](https://doi.org/10.1007/BF02289730)). The UCLA repeated measures exercise dataset ([UCLA Office of Advanced Research Computing, n.d.](https://stats.idre.ucla.edu/stat/data/exer.csv)) is used for demonstration. The two-way random effects, absolute agreement, and single measurement convention is used ([McGraw et al, 1996](https://www.academia.edu/download/25350178/mcgrawk1996a.pdf); [Koo et al, 2016](https://pmc.ncbi.nlm.nih.gov/articles/PMC4913118/pdf/main.pdf)). Accordingly, the ICC is obtained through the following equation,

$$
\text{ICC(A,1)} = \frac{\text{MS}_R - \text{MS}_E}{\text{MS}_R + (k - 1)\text{MS}_E + \frac{k}{n}(\text{MS}_C - \text{MS}_E)}
$$

where $\text{MS}_R$ is the mean square for subjects (rows), $\text{MS}_C$ is the mean square for raters (columns), $\text{MS}_E$ is the residual mean square, $\text{k}$ is the number of raters/measurements and $\text{n}$ is the number of subjects. The mean square variables used to compute ICC are obtained using the following equations,

$$\begin{aligned}
\text{MS}_R &= k\sigma^2_r + \sigma^2_e \\
\text{MS}_C &= n\sigma^2_c + \sigma^2_e \\
\text{MS}_E &= \sigma^2_e
\end{aligned}$$

where $\sigma_r^2$ is the variance between subjects (rows), $\sigma_c^2$ is the variance between raters (columns), and $\sigma_e^2$ is the residual variance.

Environment setup:

```bash
conda create -n myenv python=3.10
conda activate myenv
```

Dependencies installation:

```bash
pip install -r requirements.txt
```

Usage:

```bash
python generate_repeatability.py
```

Cite As

[Nzakimuena, C. B., Solano, M. M., Marcotte-Collard, R., Lesk, M. R., & Costantino, S. (2025). Spatial and temporal changes in choroid morphology associated with long-duration spaceflight. Investigative Ophthalmology & Visual Science, 66(5), 17-17.](https://doi.org/10.1167/iovs.66.5.17)

### References

1. [Rajaratnam, N. (1960). Reliability formulas for independent decision data when reliability data are matched. Psychometrika, 25(3), 261-271.](https://doi.org/10.1007/BF02289730)
1. UCLA Office of Advanced Research Computing. (n.d.). Exercise repeatability dataset [Data set]. University of California, Los Angeles. https://stats.idre.ucla.edu/stat/data/exer.csv
1. [McGraw, K. O., & Wong, S. P. (1996). Forming inferences about some intraclass correlation coefficients. Psychological methods, 1(1), 30.](https://psycnet.apa.org/record/1996-03170-003)
1. [Koo, T. K., & Li, M. Y. (2016). A guideline of selecting and reporting intraclass correlation coefficients for reliability research. Journal of chiropractic medicine, 15(2), 155-163.](https://doi.org/10.1016/j.jcm.2016.02.012)
