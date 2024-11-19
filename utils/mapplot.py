import geopandas as gpd
import pandas as pd

# Load the DataFrame (df) and GeoDataFrame (gdf)
df = pd.read_csv("cleaned_dataset.csv")  # Replace with your actual dataset file
gdf = gpd.read_file("postaldistricts.shp")  # Replace with your actual shapefile

# Check data types for 'postal_code' in df and 'nouveau_PO' in gdf
print(df['postal_code'].dtype)  # Check type in df
print(gdf['nouveau_PO'].dtype)  # Check type in gdf

# If they are not the same, convert them to the same type
# Option 1: Convert both to string (recommended for postcodes, which may include leading zeros)
df['postal_code'] = df['postal_code'].astype(str)
gdf['nouveau_PO'] = gdf['nouveau_PO'].astype(str)

# Option 2: If you need both columns as integers, use the following instead
# df['postal_code'] = df['postal_code'].astype(int)
# gdf['nouveau_PO'] = gdf['nouveau_PO'].astype(int)

# Merge the two DataFrames (GeoDataFrame and DataFrame)
gdf = gdf.merge(df[['postal_code', 'price']], left_on='nouveau_PO', right_on='postal_code', how='left')

# Check the first few rows of the merged GeoDataFrame
print(gdf.head())

# Now you can plot or analyze the merged data
# For example, plotting the average price by postcode
import matplotlib.pyplot as plt


# Calculate the IQR (Interquartile Range)
Q1 = gdf['price'].quantile(0.25)
Q3 = gdf['price'].quantile(0.75)
IQR = Q3 - Q1

# Define the lower and upper bounds for outliers
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

# Filter out the outliers
gdf_filtered = gdf[(gdf['price'] >= lower_bound) & (gdf['price'] <= upper_bound)]

# Calculate the average price for the filtered data
average_price_filtered = gdf_filtered['price'].mean()

# Normalize the prices based on the average price after outlier removal
gdf_filtered['price_normalized'] = gdf_filtered['price'] / average_price_filtered

# Create the plot
fig, ax = plt.subplots(figsize=(10, 10))

gdf_filtered.plot(column='price_normalized',  # Use the normalized price values
                 cmap='coolwarm',  # Choose a color map
                 legend=True,
                 legend_kwds={'label': f"Property Price (Relative to Average: {average_price_filtered:.2f} €)"},
                 ax=ax,
                 edgecolor=None)

# Add a title
plt.title("Property Prices by Postcode (Relative to Average, After Outlier Removal)", fontsize=16)
plt.axis('off')  # Turn off axes for a cleaner look
plt.show()



