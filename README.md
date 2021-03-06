![cover_image](./images/olist_dream_money_1000x445.jpg)

# Introduction
**Low customer satisfaction** can have direct and indirect costs (e.g., refunds, customer support, bad word-of-mouth, etc.). Especially when online platforms display ratings for sellers or products, these negative online reviews can have long-lasting and outsized effects on the bottom line and brand. 

**[Olist](https://olist.com/pt-br/)** is a rapidly growing Brazilian e-commerce platform that connects small merchants to major online regional marketplaces and offers sellers an integrated solution such as fulfillment, customer support, and payment services. 

In this project, I analyze a dataset containing 100k orders from Olist to address a question asked by the executive team: 

>*How can the company increase customer satisfaction (so as to increase profit margins) while still maintaining a healthy order volume?* 


# Analysis 📊 

To answer this question, I break it down into 2 parts:

*1. What factors influence customer satisfaction?*

*2. What impact does adjusting those factors have on profits margins and order volume?*

### **Part 1:** *What factors influence customer satisfaction?*
- [Orders Data Analysis](https://nbviewer.org/github/phlln/olist-analysis/blob/main/notebooks/Orders%20Data%20Analysis.ipynb?flush_cache=True)
- [Sellers Data Analysis](https://nbviewer.org/github/phlln/olist-analysis/blob/main/notebooks/Sellers%20Data%20Analysis.ipynb?flush_cache=True)

### **Part 2:** *What impact does adjusting those factors have on profits margins and order volume?*
- [Profit Analysis & Recommendations](https://nbviewer.org/github/phlln/olist-analysis/blob/main/notebooks/Profit%20Analysis%20%26%20Recommendations.ipynb?flush_cache=True)

### Summary
For a high-level overview, check out the executive summary and presentation links below:
- [**Executive Summary**](https://nbviewer.org/github/phlln/olist-analysis/blob/main/notebooks/Profit%20Analysis%20%26%20Recommendations.ipynb?flush_cache=True) (Jupyter Notebook)

### **Data Visualizations (Tableau)**

![olist_presentation_preview](./images/olist_presentation_preview_cost_curve_500x225.jpg)

- [Presentation](https://public.tableau.com/app/profile/phil.lin/viz/OlistPoor-performingSellersSTORY/Poor-performersOutsizedImpact)
- [Dashboard](https://public.tableau.com/app/profile/phil.lin/viz/OlistPoor-performingSellersDASHBOARD/InteractiveDash)



### Supplementary Notebooks 
*Supplementary Notebooks showing Custom Class & Method Implementation:*
- [Olist Class](https://nbviewer.org/github/phlln/olist-analysis/blob/main/notebooks/Olist%20Class%20-%20Method%20Implementation.ipynb?flush_cache=True)
- [Order Class](https://nbviewer.org/github/phlln/olist-analysis/blob/main/notebooks/Order%20Class%20-%20Method%20Implementation.ipynb?flush_cache=True)
- [Seller Class](https://nbviewer.org/github/phlln/olist-analysis/blob/main/notebooks/Seller%20Class%20-%20Method%20Implementation.ipynb?flush_cache=True)

## Requirements
- [Python 3.8.6](https://www.python.org/downloads/release/python-386/)
- [Jupyter Notebook](http://jupyter.org/)

## Dependencies
- [pandas](https://pandas.pydata.org/)
- [numpy](http://www.numpy.org/)
- [seaborn](https://seaborn.pydata.org/) 
- [matplotlib](https://matplotlib.org/)
- [statsmodels](https://www.statsmodels.org/)

## License
- [Attribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA 4.0)](https://creativecommons.org/licenses/by-nc-sa/4.0/)
