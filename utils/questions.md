## Dataset analysis

- How many rows and columns?
    16110 rows and 25 columns.

- What is the correlation between the variables and the price? (Why might that be?)
    The correlation between varables of the price is the influence postivie or negative, those variables will have on the price, I assume livingarea, bedrooms, localisation, building state, pool

- How are variables correlated to each other? (Why?)

- Which variables have the greatest influence on the price?
    After calculating it: 
    Influence +: livingarea, bedrooms, facades, plot/land surface, AS_NEWS, fireplace, pool, garden, terrace 
    Influence -:To renovate, to be done up, kot, service flat, ground floor, chalet, furnished, to restore

- Which variables have the least influence on the price?
    Kitche, good, mansion, country cottage, manor

- How many qualitative and quantitative variables are there? How would you transform these values into numerical values?
    x qualitatives and x quantititatives, for the qualitatives, i would create extra columns in the dataframe, with binary values, for each =/= quaalitative value

- Percentage of missing values per column?  
    12.90% of missing values average for all columns, but high % of missing values are in the columns facades, terracesurface, buildingstate & landsurface, those values are mostly missing because they don't exist
    Maybe in the future a different dataset for house and apartments would be relevant

- Plot the outliers.
    Plotted them with  box-plot 

- Which variables would you delete and why ?
    Type of sale, fireplacecount

- Represent the number of properties according to their surface using a histogram.
- In your opinion, which 5 variables are the most important and why?
    price, livingarea, bedrooms, postcode/municipalcode, subtype of property as they showed high correlation rate, positive or negative 

- What are the **most** expensive municipalities in Belgium? (Average price, median price, price per square meter)
    
- What are the **most** expensive municipalities in Wallonia? (Average price, median price, price per square meter)
- What are the **most** expensive municipalities in Flanders? (Average price, median price, price per square meter)
- What are the **less** expensive municipalities in Belgium? (Average price, median price, price per square meter)
- What are the **less** expensive municipalities in Wallonia? (Average price, median price, price per square meter)
- What are the **less** expensive municipalities in Flanders? (Average price, median price, price per square meter)
