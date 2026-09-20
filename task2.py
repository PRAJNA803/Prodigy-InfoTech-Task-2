import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

print("="*60)
print("PRODIGY INFOTECH-TASK 2")
print("DATA CLEANING AND EXPLORATORY DATA ANALYSIS")
print("="*60)

train=pd.read_csv("train.csv")
test=pd.read_csv("test.csv")

print("\n1.DATASET LOADED SUCCESSFULLY")
print("\nTraining dataset shape:")
print(train.shape)
print("\nTesting dataset shape:")
print(test.shape)

print("\n2.FIRST FIVE ROWS")
print(train.head())

print("\n3.DATASET INFORMATION")
print(train.info())

print("\n4.MISSING VALUES BEFORE CLEANING")
print(train.isnull().sum())
train["Age"]=train["Age"].fillna(train["Age"].median())
train["Embarked"]=train["Embarked"].fillna(train["Embarked"].mode()[0])
test["Fare"]=test["Fare"].fillna(test["Fare"].median())
train["Cabin"]=train["Cabin"].fillna("Unknown")
test["Cabin"]=test["Cabin"].fillna("Unknown")

print("\n5. DATA CLEANING COMPLETED")
print("\nMissing values after cleaning:")
print(train.isnull().sum())
os.makedirs("output", exist_ok=True)
plt.figure(figsize=(8, 5))
sns.countplot(data=train, x="Survived")
plt.title("Titanic Survival Count")
plt.xlabel("Survived(0=No,1=Yes)")
plt.ylabel("Number of Passengers")
plt.tight_layout()
plt.savefig("output/01_survival_count.png", dpi=300)
plt.show()
plt.figure(figsize=(8,5))
sns.countplot(data=train,x="Sex",hue="Survived")
plt.title("Survival by Gender")
plt.xlabel("Gender")
plt.ylabel("Number of Passengers")
plt.tight_layout()
plt.savefig("output/02_survival_by_gender.png",dpi=300)
plt.show()
plt.figure(figsize=(8,5))
sns.countplot(data=train,x="Pclass",hue="Survived")
plt.title("Survival by Passenger Class")
plt.xlabel("Passenger Class")
plt.ylabel("Number of Passengers")
plt.tight_layout()
plt.savefig("output/03_survival_by_class.png",dpi=300)
plt.show()
plt.figure(figsize=(8,5))
sns.histplot(train["Age"],bins=30,kde=True)
plt.title("Age Distribution of Titanic Passengers")
plt.xlabel("Age")
plt.ylabel("Number of Passengers")
plt.tight_layout()
plt.savefig("output/04_age_distribution.png",dpi=300)
plt.show()
plt.figure(figsize=(8,5))
sns.histplot(train["Fare"],bins=30,kde=True)
plt.title("Fare Distribution")
plt.xlabel("Fare")
plt.ylabel("Number of Passengers")
plt.tight_layout()
plt.savefig("output/05_fare_distribution.png",dpi=300)
plt.show()
plt.figure(figsize=(8,5))
sns.boxplot(data=train,x="Survived",y="Age")
plt.title("Age vs Survival")
plt.xlabel("Survived(0=No,1=Yes)")
plt.ylabel("Age")
plt.tight_layout()
plt.savefig("output/06_age_vs_survival.png",dpi=300)
plt.show()

plt.figure(figsize=(8,5))
sns.boxplot(data=train,x="Pclass",y="Fare")

plt.title("Fare Distribution by Passenger Class")
plt.xlabel("Passenger Class")
plt.ylabel("Fare")

plt.tight_layout()
plt.savefig("output/07_fare_by_class.png",dpi=300)
plt.show()
plt.figure(figsize=(10,7))

numeric_data=train.select_dtypes(include="number")

correlation=numeric_data.corr()

sns.heatmap(
    correlation,
    annot=True,
    cmap="coolwarm",
    fmt=".2f"
)

plt.title("Correlation Heatmap")

plt.tight_layout()
plt.savefig("output/08_correlation_heatmap.png",dpi=300)
plt.show()
gender_survival=train.groupby("Sex")["Survived"].mean()

print("\n6. SURVIVAL RATE BY GENDER")
print(gender_survival)

plt.figure(figsize=(8,5))
gender_survival.plot(kind="bar")
plt.title("Survival Rate by Gender")
plt.xlabel("Gender")
plt.ylabel("Survival Rate")

plt.xticks(rotation=0)

plt.tight_layout()
plt.savefig("output/09_survival_rate_gender.png",dpi=300)
plt.show()

class_survival=train.groupby("Pclass")["Survived"].mean()

print("\n7. SURVIVAL RATE BY PASSENGER CLASS")
print(class_survival)
plt.figure(figsize=(8,5))
class_survival.plot(kind="bar")

plt.title("Survival Rate by Passenger Class")
plt.xlabel("Passenger Class")
plt.ylabel("Survival Rate")

plt.xticks(rotation=0)

plt.tight_layout()
plt.savefig("output/10_survival_rate_class.png",dpi=300)
plt.show()
print("\n"+"="*60)
print("TASK 2 COMPLETED SUCCESSFULLY")
print("="*60)

print("\nGenerated files are available inside:")
print("output")

print("\nTotal training passengers:",len(train))

print("\nSurvived:")
print(train["Survived"].value_counts())

print("\nSurvival percentage:")
print(train["Survived"].value_counts(normalize=True)*100)

print("\nGender survival rate:")
print(gender_survival)

print("\nClass survival rate:")
print(class_survival)

print("\nAll charts have been saved successfully.")