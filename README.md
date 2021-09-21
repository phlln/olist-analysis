# Olist E-commerce Platform | Data Analysis

This repo is a collection of Jupyter Notebooks sharing my data analysis for **Olist**, a Brazilian e-commerce platform. The [dataset](https://www.kaggle.com/olistbr/brazilian-ecommerce) contains information on 100k orders from 2016 to 2018 made publicly available by **Olist** on Kaggle.

As part of an individual project for **Le Wagon | Data Science Bootcamp**, the analysis, conclusions, and recommendations are framed as an analytics team responding to a prompt by the CEO.

***CEO QUESTION:*** *How do we increase customer satisfaction (so as to increase profit margins) while maintaining a healthy order volume?*

In order to address this question, we break it down into 2 parts:

*1. What factors influence customer satisfaction?*

*2. What impact does adjusting those factors have on profits margins and order volume?*


**PART 1**

To understand more clearly what factors influence customer satisfaction (as measured by review scores), we first perform exploratory data analysis on the Orders and Sellers datasets by examining the characteristics of the data, distributions, and correlations. Then, we run linear regression models to identify which features have the largest impact on customer review scores. To corroborate our findings, we also re-frame our analysis to run logistic regression models on the data. 

**Detailed Analyses for Part 1:**
- [Orders Data Analysis](https://github.com/phlln/olist-analysis/blob/main/notebooks/Orders%20Data%20Analysis.ipynb)
- [Sellers Data Analysis](https://github.com/phlln/olist-analysis/blob/main/notebooks/Sellers%20Data%20Analysis.ipynb)

***Supplementary Notebooks showing Custom Class & Method Implementation:***
- [Olist Class](https://github.com/phlln/olist-analysis/blob/main/notebooks/Olist%20Class%20-%20Method%20Implementation.ipynb)
- [Order Class](https://github.com/phlln/olist-analysis/blob/main/notebooks/Order%20Class%20-%20Method%20Implementation.ipynb)
- [Seller Class](https://github.com/phlln/olist-analysis/blob/main/notebooks/Seller%20Class%20-%20Method%20Implementation.ipynb)

**PART 2**

Given our findings from Part 1, we assess which factors (if any) can be adjusted in the short term and ultimately propose removing poor-performing sellers from the platform. We then move forward in our analysis by evaluating its impact on revenues, costs, order volumes, and profits. We conclude with a summary of our findings and make recommendations to the CEO.

**Detailed Analysis (including an Executive Summary) for Part 2:**

- [Profit Analysis & Recommendations](https://github.com/phlln/olist-analysis/blob/main/notebooks/Profit%20Analysis%20%26%20Recommendations.ipynb)

## Requirements
- Python 3.6
- Jupyter Notebook

## Dependencies
- pandas
- numpy
- seaborn 
- matplotlib
- statsmodels
- math
