###----------------------------------------------------
##--Installing Libreries
import pandas as pd
from openpyxl import Workbook
import numpy as np
from collections import Counter
###---------------------------------------------------
##--Importing data and superficial checkings

df = pd.read_csv('C:/Users/Miguel.Llorente/OneDrive - FleetCor/Desktop/London Houses/housing_in_london_monthly_variables.csv')

df.he~ad(10) # Printing the first 10 row to check if data uploag great.

df.info()# Cheaking data type.

df.describe() #Checking averages for main data source.

df.count()# Checking number houses

 ###---------------------------------------------------
 ##Count how many diferent areas are in the database
 
df_exploded = df.explode('area')

areas = df_exploded['area'].unique()

print(areas)

areas= len(areas)###Count number of different elements Total of 45

###----------------------------------------------------
##Most expensive area

average_per_area = df.groupby('area')['average_price'].mean().reset_index()
print(average_per_area)

average_per_area.sort_values(by = 'average_price', ascending = False).reset_index()### Code showing the average per aera sorted from the most expensive to the cheapes one


###-------------------------------------------------------
##Count how many houses are per area in this data base, and check the most expensive and cheapest house.

df['RefNumber'] = range(1, len(df) + 1)## Assigning a ref number to each house.
df.set_index('RefNumber', inplace = True)## Moving the reference number to the index colum so is the first one to see in the DF


count_per_area = df.groupby('area').size().reset_index(name='Count_RefNumber')## Counting how many houses are in each area
print(count_per_area)
 
 
 
df['IDarea'] = df.groupby('area').ngroup() + 1## I add a ID number to each area so i can use it to sort 


expensivest_house_area = df.loc[df.groupby('area')['average_price'].idxmax()]
cheapest_house_area = df.loc[df.groupby('area')['average_price'].idxmin()]
print(expensivest_house_area)

expensivest_house_area.sort_values(by='average_price', ascending=False).reset_index(drop=True)##chechink where are the most expensive houses.
cheapest_house_area.sort_values(by='average_price', ascending=True).reset_index(drop=True)##chechink where are the most expensive houses.


###-------------------------------------------------------------
##See all data for the houses for a especific area

specific_area = 'kensington and chelsea'

data_especific_area = df[df['area'] == specific_area] 
print(data_especific_area)

###-----------------------------------------------------------
##Try to calculate how much teh price rise per month in average

# Convertir 'date' a tipo datetime
df['date'] = pd.to_datetime(df['date'])

# Calcular la variación mensual en porcentaje
df['monthly_variation_pct'] = df.groupby('area')['average_price'].pct_change() * 100

# Calcular la variación total en porcentaje
monthly_varation_ptc = (df.groupby('area')['average_price'].last() / df.groupby('area')['average_price'].first() - 1) * 100

# Calcular la variación anual en porcentaje
df['year'] = df['date'].dt.year
df['monthly_varation_ptc'] = df.groupby(['area', 'year'])['average_price'].transform(lambda x: (x.iloc[-1] / x.iloc[0] - 1) * 100)

print("DataFrame with monthly porcentaje varation:")
print(df[['date', 'area', 'average_price', 'monthly_varation_ptc']])

print("\nTotal variation from the beggining until the end in porcenatje:")
print(monthly_varation_ptc)

print("\nMontly varation:")
print(df[['area', 'year', 'monthly_varation_ptc']].drop_duplicates())


df_sorted = df.sort_values(by='monthly_varation_ptc', ascending=False).reset_index(drop=True)
print(df_sorted)



df_sorted = df.sort_values(by='monthly_varation_ptc', ascending=False).reset_index(drop=True)###intentando pirntear la variacion total que ha habido ordeanda

print(df_sorted)


# Calcular la variación total en porcentaje
monthly_varation_ptc = (df.groupby('area')['average_price'].last() / df.groupby('area')['average_price'].first() - 1) * 100

# Crear un nuevo DataFrame con la variación total y ordenarlo
df_sorted_total_variation = pd.DataFrame({'area': monthly_varation_ptc.index, 'monthly_varation_ptc': monthly_varation_ptc.values})
df_sorted_total_variation = df_sorted_total_variation.sort_values(by='monthly_varation_ptc', ascending=False).reset_index(drop=True)

print("DataFrame ordenado por variación total desde el inicio hasta el final en porcentaje:")
print(df_sorted_total_variation)
