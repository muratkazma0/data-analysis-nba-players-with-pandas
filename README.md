# 🏀 NBA Player Data Analysis with Pandas

This project contains a comprehensive script for performing exploratory data analysis (EDA) and generating statistical insights on a dataset of NBA players using the Python Pandas library.

The analysis covers player demographics, salary distribution, team structure, and position-specific statistics. This repository serves as a practical demonstration of core data manipulation and aggregation techniques.

## 🚀 Key Features

* **Data Loading & Inspection:** Loading the dataset and viewing initial records (`df.head(10)`).
* **Descriptive Statistics:** Calculation of total records, average, maximum, minimum salary, and average age.
* **Filtering and Querying:** Identifying players within specific age ranges (e.g., 20-25).
* **Aggregation:** Calculating key metrics grouped by **Team** and **Position**, such as average salary and average age per team.
* **Ranking:** Identifying the top 10 highest-paid and lowest-paid players.

## 🛠️ Technologies Used

* **Language:** Python
* **Library:** Pandas

## 💾 Dataset

The analysis uses an `nba.csv` dataset, which includes the following columns:

| Column | Description |
| :--- | :--- |
| **Name** | Player's name |
| **Team** | Player's current team |
| **Position** | Player's position (PG, SG, SF, PF, C) |
| **Age** | Player's age |
| **Salary** | Player's annual salary |

## 💻 Output Screenshot

A screenshot of the script execution showing various analysis results:

![Ekran görüntüsü 2024-07-11 215409](https://github.com/muratkazma0/Data-Analysis-of-NBA-Players-with-Pandas/assets/154098001/1ea5d9d6-1cf3-4f33-9b6f-2515cd3a7930)

## ✍️ Analysis Questions Answered in `main.py`

The script provides the answers to the following questions:

* Total number of records.
* Average and maximum salary of all players.
* Identification of the player with the highest salary.
* Names and teams of players aged 20-25.
* Team-wise average salary and age.
* Number of unique teams and player count per team.
* Identification of the oldest and youngest players.
* Distribution of players by age and position.
* Top 10 highest-paid and lowest-paid players.
* Average salary by position.
