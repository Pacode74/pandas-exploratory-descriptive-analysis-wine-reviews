![Exploratory and Descriptive Wine Reviews Analysis](./support_files/readme_image.jpg)

This project is based on "The Complete Pandas Bootcamp 2023 - Data Science with Python", a course offered by Udemy
and taught by Alexander Hagmann. 

The dataset for this project comes from Kaggle - Wine Reviews https://www.kaggle.com/datasets/zynicide/wine-reviews.
The dataset was scrapped from https://www.wineenthusiast.com/">Wineenthusiast.com.

This project focuses on Exploratory Data Analysis (EDA), Descriptive analysis, and basic Inferential analysis. 

The primary objectives of this project:

# <font color="#b33939" color face="Giorgia">**Data Inspection**</font>

- Import the Datasets winemag-data_first150k.csv and Inspect! winemag-data_first150k.csv contains 10 columns and 150k rows of wine reviews.

One consideration is that this data is from one month in the summer (June 2017) and was collected from a website based in the United States. The demographics of those people making the Wine Reviews are undoubtedly American and might be prone to drink more American wines due to the domestic costs.

# <font color="#b33939" color face="Giorgia">**Data Cleaning**</font>

## 1. Rename all column names to title and set index  
## 2. Drop duplicated rows  
## 3. Handle missing values in the dataset 
### 3.1 Fill in the missing values in the 'Country' column  
### 3.2 Fill in the missing values in the 'Province' column  
### 3.3 Handling Missing Values in Prices  
#### 3.3.1 Analyze the distribution of 'Price'  
#### 3.3.2 Can we simply drop rows with missing Price values?   
#### 3.3.3 Remove Tunisia and Egypt countries because the number of reviews for them are too small and there are no available prices.    
#### 3.3.4 Which Approach to take to fill out missing prices? Group Median Imputation approach vs KNN Imputation Approach  
#### 3.3.5 **Hybrid Approach:** use the group median method for low variability groups and use KNN imputation methods for high variability groups. **Created reviews_hybrid dataset.**  
##### 3.3.5.1 Option one - Spliting datasets into two. One dataset use for group media approach and another dataset use for KNN approach. Then merge two datasets.  
##### 3.3.5.2 Option Two (Best) - performing inplace Imputation for both group median and KNN approaches.  
#### 3.3.6 **Group Median Imputation Approach** to fill out missing prices. Replace the missing values by groups(Country and Province) specific values. Use `.transform()` method. **Created reviews_gm dataset.**    
##### 3.3.6.1 Analysis if for missing price values by group specific we should use mean price of median price?  
##### 3.3.6.2 After we choose to use median price value as group specific value for missing price. Lets fill out the missing price values in the dataset.  
#### 3.3.7 **K-nearest neighbors(KNN) Imputation Approach** to fill out missing prices. **Created reviews_knn dataset.**    
#### 3.3.8 Compare Hybrib Imputation vs K-nearest neighbors(KNN) Imputation Approach vs Group Median Approach to fill out missing prices.  

For our further analysis we choose to use Hybrid Approach (3.3.5) in our further analysis that is we will use `reviews_hybrid`.   

## 4. Handle outliers in the `reviews_hybrid` dataset.   
### 4.1 Analyze the distribution of 'Price'  
### 4.2 Handle the Outliers type 2: Values are correct but extreme to our other data points  
Given this information, we have several options for handling these outliers, depending on my specific analysis goals:  
#### 4.2.1 **Keep the outliers**: If the high-priced wines are of particular interest or if we're analyzing market segments that include premium wines, we might choose to retain these data points.  
#### 4.2.2 **Exclude the outliers**: For analyses where extreme values might skew the results, such as when calculating average prices, we might consider excluding these outliers.  
#### 4.2.3 **Cap and Floor the values**: We can cap and floor prices at a certain thresholds to lessen the impact of extremely high/low prices. But the data will not be excluded only the price values will be overwritten.  
#### 4.2.4 **Discretization and Binning of 'Points' into 'Rating'**: I will use this for my further analysis.  
#### 4.2.5 **Discretization and Binning of 'Price' into 'Price_cat'**: I will use this for my further analysis.  
##### 4.2.5.1 Approach Discretizing Price based on Equal width bins.  
##### 4.2.5.2 Approach Discretizing Price based on putting the same number of reviews into different brackets.    
##### 4.2.5.3 Approach Discretizing Price based on defining customized quanlites.   
##### 4.2.5.4 Approach Discretizing Price based on defining customized quanlites and considering outliers.  
##### 4.2.5.5 Approach K-Means Clustering for Price Binning.  
For our further analysis, we choose to use the Descritization and Binning approach according to 4.2.4 and 4.2.5.5   

## 5. Convert Rating and Price_Category to categorical data and set the order in `reviews_hybrid` dataset.    

# <font color="#b33939" color face="Giorgia">**Pattern Discovery Part I - Data Aggregation**</font>  

## 1. Which country is dominant in Wine industry production?  
## 2. What is the most common variety reviewed in each country?  
## 3. What are the most expensive and the cheapest wines?
## 4. What Variety of Wine was reviewed most often and how many unique Varieties?
## 5. What is the most popular Variety of Wine by Country?
## 6. Plotting Points and Price grouped by Variety.
## 7. What are the Perfect Score?
## 8. Identifies the top 10 provinces based on the number of wine reviews, finds the most reviewed wine variety within each of those provinces.
## 9. Heatmap of the top 20 wine-producing countries based on the frequency of wines falling into different Rating categories.
## 10. Heatmap of the top 20 wine-producing countries based on the frequency of wines falling into different Price categories.

# <font color="#b33939" color face="Giorgia">**Pattern Discovery Part II - Exploratory and Descriptive Analysis**</font>

## 1. Does Country has significal effect on Price? Use ANOVA test.
## 2. Is Higher Point(Rating) associated with Higher Price or vice versa? Use  Pearson correlation coefficient and Linear Regression analysis to measure the linear relationship.
## 3. Descriptive Price Category analysis.
## 4. Does Price Categories have significant effect on Price? Use ANOVA test.
## 5. Compare Price and Point Distributions. Transformed Price and Points columns to a standard normal distribution. Use Z-score analysis.
## 6. How each wine's quality rating compares to the average rating of wines from the same country. Use Z-score analysis.
## 7. How each wine's price compares to the average price of wines from the same country. Use Z-score analysis.
## 8. Hypothesis: Wines from France have higher average ratings than wines from Italy. Perform independent sample t-test.

During data cleaning process we created many other different approaches of handle missing values and handling outliers.  
We have chosen only one of those approaches and for the future project it is worth to choose also other approaches to 
understand different strategies in exploratory, descriptive, and inferential analysis.