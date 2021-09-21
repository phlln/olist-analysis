# Olist E-commerce Platform | Review Score Data Analysis

This repo is a collection of Jupyter Notebooks sharing my data analysis for Olist, a Brazilian e-commerce platform. The [dataset](https://www.kaggle.com/olistbr/brazilian-ecommerce) contains information on 100k orders from 2016 to
2018 made publicly available by Olist on Kaggle.

As part of an individual project for **Le Wagon | Data Science Bootcamp**, the analysis, conclusions, and recommendations are framed as an analytics team response to a prompt by the CEO:

**CEO Question:**

*How do we increase customer satisfaction (so as to increase profit margins) while maintaining a healthy order volume?*

In order to address this question, we break this question down into 2 parts:

**1. What factors influence customer satisfaction?** 

**2. What impact does adjusting those factors have on profits margins and order volume?**

***Part 1***

To understand more clearly what factors influence customer satisfaction, we first perform exploratory data analysis on the Orders and Sellers datasets by examining the characterstics of the data, distributions, and correlations. Then, we run linear regression models to identify which features have the largest impact on customer review scores. To corroborate our findings, we re-frame our analysis to run logistic regression models on the data. 

**Detailed Analysis for part 1 can be found at the following notebooks:**
- [Orders Data Analysis](https://github.com/phlln/olist-analysis/blob/main/notebooks/Orders%20Data%20Analysis.ipynb)
- [Sellers Data Analysis](https://github.com/phlln/olist-analysis/blob/main/notebooks/Sellers%20Data%20Analysis.ipynb)

***Supplementary Notebooks showing Custom Class & Method Implementation***
- [Olist Class](https://github.com/phlln/olist-analysis/blob/main/notebooks/Olist%20Class%20-%20Method%20Implementation.ipynb)
- [Order Class](https://github.com/phlln/olist-analysis/blob/main/notebooks/Order%20Class%20-%20Method%20Implementation.ipynb)
- [Seller Class](https://github.com/phlln/olist-analysis/blob/main/notebooks/Seller%20Class%20-%20Method%20Implementation.ipynb)

***Part 2***

Given our findings from part 1, we assess which factors (if any) can be adjusted in the short term and ultimately propose removing
poor-performing sellers from the platform. We then move forward in our analysis by evaluating the impact on revenues, costs, order volumes, and profits. Finally, we summarize our findings and make a recommendation to the CEO.  

**Detailed Analysis for part 2 can be found at the following notebook:**





In order to address this question, we break this problem down into 2 parts: 
1) First try to understand which factors have an impact on customer satisfaction (as measured by customer review scores). 
2) Second, given our findings we make recommendations on what changes can be made in the short term and calculate the impact of those changes on profit margins and order volume. 

In part 1, we perform exploraatory data analysis on the Orders and Sellers datasets followed by linear and logistic regression models to further understand the relationship 
between various features and review scores.

In part 2, we identify poor-performing sellers on the platform and do a profit analysis based on their removal. 


## Executive Summary & Recommendations
From our analyis of both the Orders and Sellers Database, we found that *long wait times* and single orders containing *multiple products or sellers* were associated with lower
review scores. However, our findings suggest that there are other unaccounted for factors (likely outside of these datasets) that have an impact on low review scores.

Given our limited view of all the factors influencing low review scores, we decided to respond to the issues of customer satisfaction and profit margins from a different approach.
Instead of trying to figure out which individual factors are connected to low review scores, we shifted attention to quantifying the impact on Olist if poor-performing 
sellers (defined as sellers with enough bad reviews to have a negative profit for Olist) were removed from the platform.

In this alternative approach, we discovered that roughly 9% of sellers can be classified as 'poor-performing' because of negative profits to Olist. Additionally, this small group
of sellers had 7x the order volume of other sellers and accounted for 40% of cumulative IT costs.

Our conclusions found that removal of 'poor-performing' sellers that can improve overall customer satisfaction, keep a healthy order volume, and boost profits in the short term 
by 46% or 580,196 BRL (110,598 USD).

Recommendation to CEO:

In the short term, we believe that Olist can improve profits and overall customer satisfaction by removing poor-performing sellers. Our preliminary analysis shows that removing these 
sellers from the platform will immediately increase Olist profits by reducing costs on two fronts:

1. Costs Associated with Bad Reviews - removal of sellers who have received enough bad reviews to have a drag on Olist margins will boost profits by 20% amounting to an increase 
of 313,277 BRL (58,246 USD).

2. IT Costs - IT costs are a function of overall order volume, and since poor-performing sellers have been found to have a disproportionately large order volume, their removal translates 
into an overall 40% reduction in IT costs amounting to a savings of 266,919 BRL (~50,868 USD).

In conclusion, by removing poor-performing sellers from the platform, Olist stands to see an immediate gain of 580,196 BRL (~110,484 USD) or increase of 46% to its financial performance. 
Additionally, we would expect to see an overall improvement in brand reputation as average customer satisfaction increases.

**Caveats**

These findings have been made based on assumptions for the monetary costs associated with bad reviews as well as the model for IT infrastructure costs.

**Other Areas For Further Analysis**

A more fine-toothed analysis for identifying poor-performing sellers might also distinguish sellers who have only just recently joined the platform and not gained enough experience 
to use the platform effectively or engage with customers. With sufficient support, they may potentially become high performing sellers and also advocates for the platform with a good 
on-ramping process and support system for new sellers.     

Other datasets to explore include Products data which could bring to light if product quality is a source of low review scores. Additionally, a text analysis of the reviews could also 
uncover more explicitly the specific reasons for customer dissatisfaction. 





## Notebooks

### Analysis & Recommendations








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
