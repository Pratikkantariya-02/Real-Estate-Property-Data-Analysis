import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset

data = pd.read_csv('data.csv')
# print(data.head())
# print(data.info())
# print(data.shape)


# Data Cleaning

# Clean column names
data.columns = data.columns.str.strip().str.lower().str.replace(' ', '_')
# print(data.columns.tolist())

# Remove duplicates
data = data.drop_duplicates()
# print(data.shape)

# Clean column values

data['price'] = data['price'].astype(str).str.replace(',', '').astype(float)
# print(data['price'])

data['area'] = data['area'].astype(str).str.replace(',', '').astype(int)
# print(data['area'])

data['rate_per_sqft'] = data['rate_per_sqft'].astype(str).str.replace(',', '').astype(int)
# print(data['rate_per_sqft'])

data['rera_approval'] = data['rera_approval'].astype(str).str.strip().str.lower().map({'approved by rera': True, 'not approved by rera': False})
# print(data['rera_approval'])

data['flat_type'] = data['flat_type'].astype(str).str.strip().str.lower()
# print(data['flat_type'])

data['status'] = data['status'].astype(str).str.strip().str.lower()
# print(data['status'])

# Question 1: Which is the costliest flat?

costliest_flat = data.loc[data['price'].idxmax()], '''.loc is used to select a row using its index.'''
# print(costliest_flat)


# Question 2: Which locality has the highest average price?

locality_avg_price = data.groupby('locality')['price'].mean().idxmax()
# print(f"Locality with the highest average price: {locality_avg_price}")


# Question 3: Which locality has the highest rate per square foot?

locality_avg_rate = data.groupby('locality')['rate_per_sqft'].mean().idxmax()
# print(f"Locality with the highest rate per square foot: {locality_avg_rate}")


# Question 4: Do ready-to-move properties cost more than under-construction properties?

ready_to_move_avg_price = data[data['status'] == 'ready to move']['price'].mean()
under_construction_avg_price = data[data['status'] == 'under construction']['price'].mean()

# if ready_to_move_avg_price > under_construction_avg_price:
#     print(f"Ready-to-move flats are more expensive on average: {ready_to_move_avg_price}")
# else:
#     print(f"Under-construction flats are more expensive on average: {under_construction_avg_price}")


# Question 5: Do RERA-approved properties command a price premium?

rera_approved_avg_price = data[data['rera_approval'] == True]['price'].mean()
rera_not_approved_avg_price = data[data['rera_approval'] == False]['price'].mean()

# if rera_approved_avg_price > rera_not_approved_avg_price:
#     print(f"RERA-approved flats are more expensive on average: {rera_approved_avg_price}")
# else:
#     print(f"RERA-approved flats are not more expensive on average: {rera_not_approved_avg_price}")


# Question 6: How does area (sqft) impact property price?

# sns.scatterplot(x='area', y='price', data=data)
# plt.xlabel('Area (sqft)')
# plt.ylabel('Price')
# plt.title('Impact of Area on Property Price')
# plt.show()

# Question 7: Which BHK configuration is the most expensive on average?

bhk_avg_price = data.groupby('bhk_count')['rate_per_sqft'].mean().idxmax()
# print(f"Most expensive BHK configuration on average: {bhk_avg_price} BHK.")

# Question 8: Which property type (Apartment, Floor, Plot) is the costliest?

property_type_avg_price = data.groupby('flat_type')['rate_per_sqft'].mean().idxmax()
# print(f"Costliest property type: {property_type_avg_price}")

# Question 9: Do certain builders or companies consistently price higher?

builder_avg_price = data.groupby('company_name')['rate_per_sqft'].mean().sort_values(ascending=False).idxmax()
# print(f"Builder with the highest average price: {builder_avg_price}")

# Question 10: Are larger homes always more expensive per square foot?

# sns.scatterplot(x='area', y='rate_per_sqft', data=data)
# plt.xlabel('Area (sqft)')
# plt.ylabel('Rate per Square Foot')
# plt.title('Impact of Area on Rate per Square Foot')
# plt.show()