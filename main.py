# NBA Oyuncularının Veri Analizi / Data Analysis of NBA Players 

import pandas as pd

df = pd.read_csv("datasets/nba.csv")

# İlk 10 kaydı getiriniz / Get the first 10 records
result = df.head(10)
print(result)

# Toplam kaç kayıt var? / How many total records are there?
result = len(df.index)
print(result)

# Tüm oyuncuların toplam maaş ortalaması nedir? / What is the average salary of all players?
result = df["Salary"].mean()
print(result)

# En yüksek maaşı ne kadardır? / What is the highest salary?
result = df["Salary"].max()
print(result)

# En yüksek maaşı alan oyuncu kimdir? / Who is the player with the highest salary?
result = df[df["Salary"] == df["Salary"].max()]["Name"].iloc[0]
print(result)

# Yaşı 20 - 25 arasında olan oyuncuların isim ve oynadıkları takımlar / Names and teams of players aged 20-25
result = df[(df["Age"] >= 20) & (df["Age"] < 25)][["Name", "Team", "Age"]]
print(result)

# 'John Holland' isimli oyuncunun oynadığı takım hangisidir? / Which team does 'John Holland' play for?
result = df[df["Name"] == "John Holland"]["Team"].iloc[0]
print(result)

# Takımlara göre oyuncuların ortalama maaş bilgileri / Average salary information of players by team
result = df.groupby("Team").mean()["Salary"]
print(result)

# Kaç farklı takım mevcut? / How many different teams are there?
result = len(df.groupby("Team"))
print(result)

# Her takımda kaç oyuncu oynamaktadır? / How many players are there in each team?
result = df["Team"].value_counts()
print(result)

# En yaşlı oyuncu kimdir? / Who is the oldest player?
result = df[df["Age"] == df["Age"].max()]["Name"].iloc[0]
print(result)

# En genç oyuncu kimdir? / Who is the youngest player?
result = df[df["Age"] == df["Age"].min()]["Name"].iloc[0]
print(result)

# Pozisyonlara göre oyuncuların sayısı / Number of players by position
result = df["Position"].value_counts()
print(result)

# Ortalama yaş nedir? / What is the average age?
result = df["Age"].mean()
print(result)

# Her takımda ortalama yaş nedir? / What is the average age in each team?
result = df.groupby("Team").mean()["Age"]
print(result)

# En çok oyuncuya sahip takım hangisidir? / Which team has the most players?
result = df["Team"].value_counts().idxmax()
print(result)

# Oyuncuların yaşlarına göre dağılımı / Distribution of players by age
result = df["Age"].value_counts()
print(result)

# En yüksek maaşı alan 10 oyuncunun isimleri ve maaşları / Names and salaries of the top 10 highest-paid players
result = df.nlargest(10, "Salary")[["Name", "Salary"]]
print(result)

# En düşük maaşı alan 10 oyuncunun isimleri ve maaşları / Names and salaries of the top 10 lowest-paid players
result = df.nsmallest(10, "Salary")[["Name", "Salary"]]
print(result)

# Her pozisyonda ortalama maaş bilgileri / Average salary information by position
result = df.groupby("Position").mean()["Salary"]
print(result)
