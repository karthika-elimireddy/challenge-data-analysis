
# Real Estate Dataset Analysis

## Introduction
We received a dataset from our previous web scraping project, containing **16,110 rows** and **25 columns**. To ensure a sequential workflow, we first imported the CSV file into a Jupyter notebook. 

The dataset comprises both **quantitative** (12 columns) and **qualitative** (3 columns) data, alongside several location-related fields. However, it is missing essential information such as **province**, **region**, and **municipality**. Using external databases like **Wikipedia** and **atlas-belgique.be**, we can enrich the dataset with additional location details. Furthermore, a calculated column for **price per sqm**—absent in the scraped data—has been added to enhance the analysis.

---

## Data Cleaning
After inspecting the dataset, the following issues were identified:
1. A property located in Holland was filtered.
2. Two high-priced properties with mismatched locality name (**Cadzand**) and postcode (**4xxx**)  were filtered out.
3. Missing data accounted for **12.90%** of the dataset:
   - Most missing values are in **address-related columns**.
   - Missing values in columns such as **terracesurface**, **facades building**, and **landsurface** are likely due to non-existent features in those properties.

We also identified that a separate dataset for **houses** and **apartments** might be more relevant in future projects.

---

## Feature Engineering
To facilitate further analysis:
1. **Binary encoding** was applied to non-numeric columns, creating new columns with `0` or `1` values.
2. A correlation analysis was performed to assess the influence (positive or negative) of various variables on **price**. 

---

## Correlation Analysis
- **Positive Influence (close to +1):**
  - **Living area, bedrooms, facades, plot/land surface, AS_NEWS, fireplace, pool, garden, terrace.**

- **Negative Influence (close to -1):**
  - **To renovate, to be done up, kot, service flat, ground floor, chalet, furnished, to restore.**

- **Neutral Influence (close to 0):**
  - **Presence of a kitchen, subtype of property (e.g., mansion, cottage, manor).**

We plotted outliers to gain further insights into the dataset.

---

## Refinement
Variables such as **type of sale** and **fireplace counts** were deemed irrelevant for our analysis and were filtered out. After additional research, the **five most important variables** were determined to be:
1. **Price**  
2. **Living area**  
3. **Bedrooms**  
4. **Subtype of property**  
5. **Postcode/municipality**

These variables had the most significant influence on price and are crucial for answering key questions about the real estate market.

---

## Key Insights
We computed the following rankings based on **mean**, **median**, and **price per sqm**:

1. **Top 5 Most Expensive Municipalities in Belgium:**
   - By mean: Tinlot (712k), Wezembeek-Oppem (659k), Lasne (646k), Hogstraten Minderhout (645k), Kraainem (623k)
   - By median: Sint-Martens-Latem (1.14m), Lasne Plancenoit(0.99m), Martelange (0.9m), Knokke (0.89m), Dilsen (0.84m)
   - By price per sqm: Knokke (7493/sqm), Nieuwpoort (4483/sqm), Leuven (4290/sqm), Ixelles (4150/sqm), Etterbeek (4186€/sqm)

2. **Top 5 Most Expensive Municipalities in Brussels:**
   - By mean: Woluwe-Saint-Pierre (522k), Ixelles (466k), Uccle (466k), Watermael-Boitsfort (443k), Woluwe-Saint-Lambert (428k)
   - By median: Woluwe-Saint-Pierre (525k), Ixelles (425k), Watermael-Boitsfort (422k), Uccle (420k), Woluwe-Saint-Lambert (399k)
   - By price per sqm:Ixelles (4202€/sqm), Etterbeek (4186€/sqm), Brussel-center (4038e/sqm), Woluwe-Saint-Pierre (3806€/sqm), Woluwe-Saint-Lambert (3793€/sqm)

3. **Top 5 Most Expensive Municipalities in Flanders:**
   - By mean: Wezembeek-Oppem (659k), Hoogstraten (645k), Kraainem (623k), Knokke (621k), Sint Martens Latel (593k)
   - By median: Wezembeek-Oppem (695k), Hoogstraten (645k), Knokke (622k), Kraainem (598k), Schilde (590k)
   - By price per sqm: Knokke (7493/sqm), Nieuwpoort (4483€/sqm), Leuven (4290€/sqm), Middelkerke (3909€/sqm), Oostduinkerke (3653€/sqm)

4. **Top 5 Most Expensive Municipalities in Wallonia:**
   - By mean: Tinlot (712k), Lase (646k), Grandmetz (620k), Chimay (600k), Bertogne (590k)
   - By median: Tinlot (712k), Pont-De-Loup (699k), Lasne (695k), Grandmetz (620k), Ham sur Heure (605k)
   - By price per sqm: Chastre (4000€/sqm), Eupen (3752€/sqm), Court-Saint-Etienne (3639€/sqm), Rouvroy (3543€/sqm), Martelange (3491€/sqm)

5. **Top 5 Least Expensive Municipalities in Belgium:**
   - By mean: Viroinval (45k), Peruwelz (70k), Wasme (72.5k), Raeren (100k), Antoing (110k)
   - By median: Viroinval (45k), Peruwekz (70k), Wasmes (80k), Raeren (100k) Antoing (110k)
   - By price per sqm: Raeren (625€/sqm), Comblain au pont (730€/sqm), Viroinval (750€/sqm), Comines Warneton (844€/sqm), Peruwez (875€/sqm)

6. **Top 5 Least Expensive Municipalities in Brussels:**
   - By mean: Koelberg (258k), Molenbeek (273k), Ganshoren (282k), Jette (288k), forest (304k)
   - By median: Gashoren (240k), Molenbeek (247k), Koekelberg (249k), Jette (254k), Anderlecht (265k)
   - By price per sqm: Molenbeek (2698€/sqm), Koekelberg (2787€/sqm), Laeken (2833€/sqm), Jette (2864€/sqm), Ganshoren (2865€/sqm)

7. **Top 5 Least Expensive Municipalities in Flanders:**
   - By mean: Alveringem (189k), Heers, (2017k), Geluw (219k), Menen (224k), Zoutleeuw (230k)
   - By median: Menen (179k), Ooostrozebeke (183k), Alveringem (189k), Geluwe (204k), Ieper (229k)
   - By price per sqm: Alveringem (880e/sqm), Geluwe (1144€/sqm), Riesmt (1343€/sqm), Heers (1417/sqm), Zoutleeuw (1423€/sqm)

8. **Top 5 Least Expensive Municipalities in Wallonia:**
   - By mean: Viroinval (45k), Peruwelz (70k), Wasme (72.5k), Raeren (100k), Antoing (110k)
   - By median: Viroinval (45k), Peruwekz (70k), Wasmes (80k), Raeren (100k) Antoing (110k)
   - By price per sqm: Raeren (625€/sqm), Comblain au pont (730€/sqm), Viroinval (750€/sqm), Comines Warneton (844€/sqm), Peruwez (875€/sqm)

---

## Key Takeaways
1. **Correlation Highlights:** 
   - Strong positive influences include living area, bedrooms, and the presence of amenities such as a pool or garden.
   - Renovation needs and niche property types (e.g., service flats, chalets) negatively affect property prices.
   
2. **Data Segmentation:** 
   - Separating houses and apartments for distinct analyses might yield better insights in future work.

3. **Enrichment Potential:**
   - Adding more granular location data (e.g., region, municipality) significantly improves the dataset's value.

4. **Actionable Metrics:**
   - Price per sqm is a critical metric for regional and municipal comparisons in the Belgian real estate market.

With these findings, we now have a robust dataset to address key questions about real estate pricing in Belgium, focusing on **regions** and **municipalities**.
