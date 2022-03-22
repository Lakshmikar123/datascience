import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def plotcity(df):
	'''This function shows the plot of the count of sales by cities'''
	sns.countplot(x="City", data=df)
	plt.show()

def plotcat(df):
	'''This function shows the plot of the count of categories of items sales by cities'''
	plt.xticks(rotation=90)
	sns.countplot(x="Product line", hue="City", data=df)
	plt.show()

def plotcorr(df):
	'''This function shows the correlation between the numerical columns.'''
	numericals = df[["Unit price", "Quantity", "gross income", "Rating"]].corr()
	sns.heatmap(numericals, annot=True)
	plt.show()


def main():
	'''This is the main function and is used to print basic EDA and call the graphing functions.'''
	df = pd.read_csv("supermarket_sales.csv")
	print("Print top 5 rows")
	print(df.head())
	print("Print count of unique elements")
	print(df.nunique())
	print("Print count of null values")
	print(df.isna().sum())
	plotcity(df)
	plotcat(df)
	plotcorr(df)

if __name__ == "__main__":
	main()
