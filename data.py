import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Load the dataset
df = pd.read_csv(r"C:\Users\dell\OneDrive\Desktop\Data Analysis Using Python\Zomato-data-analysis.csv")
print(df)

#Data cleaning and processing

#Check for missing values
print(df.isnull().sum())

#Check the first five rows of the dataset
print(df.head())

# Clean the 'rate' column by converting 'X.X/5' format to float
df['rate'] = df['rate'].replace('NEW', np.nan)  # Replace 'NEW' with NaN
df['rate'] = df['rate'].str.extract(r'(\d+\.\d+)').astype(float)  # Extract numeric part

#Drop rows with missing values
print(df.dropna(subset=['name', 'online_order', 'book_table', 'rate', 'votes', 'approx_cost(for two people)', 'listed_in(type)']))

# Plot distribution of restaurant ratings
plt.figure(figsize=(8, 5))
plt.hist(df['rate'].dropna(), bins=10, color='skyblue', edgecolor='black')
plt.xlabel("Restaurant Rating")
plt.ylabel("Number of Restaurants")
plt.title("Distribution of Restaurant Ratings")
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()

# Count restaurants by price range
price_counts = df['approx_cost(for two people)'].value_counts().sort_index()
print(price_counts)

# Plot price distribution
plt.figure(figsize=(8, 5))
plt.bar(price_counts.index.astype(str), price_counts.values, color='lightcoral', edgecolor='black')
plt.xlabel("Approx Cost for Two People")
plt.ylabel("Number of Restaurants")
plt.title("Distribution of Restaurant Pricing")
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()

# Count restaurants offering online ordering
online_order_counts = df['online_order'].value_counts()
print(online_order_counts)

# Plot online order availability
plt.figure(figsize=(6, 4))
plt.pie(online_order_counts, labels=online_order_counts.index, autopct='%1.1f%%', colors=['lightblue', 'lightgreen'])
plt.title("Online Ordering Availability")
plt.show()

# Count restaurants offering table booking
book_table_counts = df['book_table'].value_counts()
print(book_table_counts)

# Plot table booking availability
plt.figure(figsize=(6, 4))
plt.pie(book_table_counts, labels=book_table_counts.index, autopct='%1.1f%%', colors=['gold', 'lightgray'])
plt.title("Table Booking Availability")
plt.show()

# Count restaurants by type
restaurant_types = df['listed_in(type)'].value_counts()
print(restaurant_types)

# Plot restaurant types
plt.figure(figsize=(10, 5))
plt.barh(restaurant_types.index, restaurant_types.values, color='mediumseagreen', edgecolor='black')
plt.xlabel("Number of Restaurants")
plt.ylabel("Restaurant Type")
plt.title("Number of Restaurants by Type")
plt.gca().invert_yaxis()
plt.grid(axis='x', linestyle='--', alpha=0.7)
plt.show()

# Count restaurants by vote count bins
vote_bins = pd.cut(df['votes'], bins=[0, 200, 500, 1000, 2000, df['votes'].max()], labels=["0-200", "200-500", "500-1000", "1000-2000", "2000+"])
vote_counts = vote_bins.value_counts().sort_index()
print(vote_bins)
print(vote_counts)

# Plot votes distribution
plt.figure(figsize=(8, 5))
plt.bar(vote_counts.index.astype(str), vote_counts.values, color='purple', edgecolor='black')
plt.xlabel("Vote Count Range")
plt.ylabel("Number of Restaurants")
plt.title("Distribution of Votes per Restaurant")
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()

# Count restaurants by rating category
rating_bins = pd.cut(df['rate'], bins=[0, 2, 3, 4, 5], labels=["Below 2", "2-3", "3-4", "4-5"])
rating_counts = rating_bins.value_counts().sort_index()
print(rating_bins)
print(rating_counts)

# Plot rating category distribution
plt.figure(figsize=(8, 5))
plt.bar(rating_counts.index.astype(str), rating_counts.values, color='orange', edgecolor='black')
plt.xlabel("Rating Category")
plt.ylabel("Number of Restaurants")
plt.title("Restaurant Count by Rating Category")
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()

# Line chart for number of restaurants per rating
rating_counts_sorted = df['rate'].value_counts().sort_index()
plt.figure(figsize=(8, 5))
plt.plot(rating_counts_sorted.index, rating_counts_sorted.values, marker='o', linestyle='-', color='blue')
plt.xlabel("Restaurant Rating")
plt.ylabel("Number of Restaurants")
plt.title("Number of Restaurants per Rating")
plt.grid(True)
plt.show()

