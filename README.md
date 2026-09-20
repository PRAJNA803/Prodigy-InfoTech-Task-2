\# Prodigy InfoTech Data Science Internship – Task 2

\## Data Cleaning and Exploratory Data Analysis
\### 📌 Task Objective

The objective of this task is to perform \*\*data cleaning and exploratory data analysis (EDA)\*\* on the Titanic dataset.
The analysis focuses on understanding the dataset, handling missing values, and identifying relationships between passenger characteristics and survival.
\---

\## 📂 Dataset
The dataset contains information about Titanic passengers.
\### Files Used
\* `train.csv` – Training dataset containing passenger information and survival status.

\* `test.csv` – Testing dataset containing passenger information.

\* `gender\_submission.csv` – Sample submission file.
\### Important Features
| Feature     | Description                            |
| ----------- | -------------------------------------- |
| PassengerId | Unique passenger identification number |
| Survived    | Survival status: 0 = No, 1 = Yes       |
| Pclass      | Passenger class                        |
| Name        | Passenger name                         |
| Sex         | Passenger gender                       |
| Age         | Passenger age                          |
| SibSp       | Number of siblings/spouses aboard      |
| Parch       | Number of parents/children aboard      |
| Ticket      | Ticket number                          |
| Fare        | Passenger fare                         |
| Cabin       | Cabin information                      |
| Embarked    | Port of embarkation                    |
\---
\## 🧹 Data Cleaning
The following data-cleaning operations were performed:
1\. Missing values in the `Age` column were replaced using the median age.

2\. Missing values in the `Embarked` column were replaced using the most frequent value (mode).

3\. Missing values in the `Fare` column of the test dataset were replaced using the median fare.

4\. Missing values in the `Cabin` column were replaced with `Unknown`.

5\. The cleaned dataset was then used for exploratory data analysis.
\---
\## 📊 Exploratory Data Analysis
Several visualizations were created to understand the Titanic dataset.
\### 1. Survival Count
Shows the number of passengers who survived and did not survive.
\### 2. Survival by Gender
Shows the relationship between passenger gender and survival.
\### 3. Survival by Passenger Class
Shows the relationship between passenger class and survival.
\### 4. Age Distribution
Shows the distribution of passenger ages.
\### 5. Fare Distribution
Shows the distribution of ticket fares.
\### 6. Age vs Survival
Compares passenger age with survival status.
\### 7. Fare Distribution by Passenger Class
Shows how ticket fares vary across passenger classes.
\### 8. Correlation Heatmap
Shows correlations between numerical variables in the dataset.
\### 9. Survival Rate by Gender
Shows the percentage of passengers who survived in each gender category.
\### 10. Survival Rate by Passenger Class
Shows the percentage of passengers who survived in each passenger class.
\---
\## 📈 Generated Visualizations
All visualizations are stored inside the `output` folder.
```text

output/
├── 01\_survival\_count.png
├── 02\_survival\_by\_gender.png
├── 03\_survival\_by\_class.png
├── 04\_age\_distribution.png
├── 05\_fare\_distribution.png
├── 06\_age\_vs\_survival.png
├── 07\_fare\_by\_class.png
├── 08\_correlation\_heatmap.png
├── 09\_survival\_rate\_gender.png
└── 10\_survival\_rate\_class.png
```
\---
\## 🛠️ Technologies Used
\* Python
\* Pandas
\* Matplotlib
\* Seaborn
\---
\## ▶️ How to Run
\### Step 1: Open the project folder
```text
C:\\Users\\PRAJNA\\Downloads\\Task2
```

\### Step 2: Install required libraries
```bash
pip install pandas matplotlib seaborn
```
\### Step 3: Run the Python program
```bash
python task2.py
```
\### Step 4: View the generated charts
The charts will be saved automatically inside the:
```text
output
```
folder.
\---
\## 📁 Project Structure
```text

Task2/
│
├── train.csv
├── test.csv
├── gender\_submission.csv
├── task2.py
├── README.md
│
└── output/
&#x20;   ├── 01\_survival\_count.png
&#x20;   ├── 02\_survival\_by\_gender.png
&#x20;   ├── 03\_survival\_by\_class.png
&#x20;   ├── 04\_age\_distribution.png
&#x20;   ├── 05\_fare\_distribution.png
&#x20;   ├── 06\_age\_vs\_survival.png
&#x20;   ├── 07\_fare\_by\_class.png
&#x20;   ├── 08\_correlation\_heatmap.png
&#x20;   ├── 09\_survival\_rate\_gender.png
&#x20;   └── 10\_survival\_rate\_class.png
```
\---

\## 🎯 Conclusion
This task demonstrates the practical use of data cleaning and exploratory data analysis techniques on the Titanic dataset.

The analysis helps understand passenger characteristics, missing data, survival patterns, and relationships between different numerical and categorical variables.

The project provides experience in using \*\*Pandas for data manipulation\*\* and \*\*Matplotlib and Seaborn for data visualization\*\*.

\---
\## 👩‍💻 Internship
\*\*Prodigy InfoTech – Data Science Internship\*\*
\*\*Task 2: Data Cleaning and Exploratory Data Analysis\*\*
