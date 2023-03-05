import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# Functions
def func(pct, allvalues):
    return "{:.1f}%".format(pct)

# Variables

url = "https://pkgstore.datahub.io/world-bank/en.atm.co2e.kt/data_csv/data/f5bebe03414aed80d7c6d107766c22d7/data_csv.csv"
df_B = pd.read_csv("budget_csv.csv")
df_p = pd.read_csv(url, index_col= 0)
df_f = pd.read_csv('https://pkgstore.datahub.io/world-bank/se.sec.prog.fe.zs/data_csv/data/d9da18077c2f8c578336837468697cff/data_csv.csv',index_col=0)
df_m = pd.read_csv('https://pkgstore.datahub.io/world-bank/se.sec.prog.ma.zs/data_csv/data/4bfc86397648eb23b6f6cafee61d80ca/data_csv.csv',index_col=0)


Branchdata1 = df_B[df_B["Name"]=="Legislative Branch"]
Branchdata2 = df_B[df_B["Name"]=="Judicial Branch"]
Branchdata3 = df_B[df_B["Name"]=="Department of the Interior"]
df_f = df_f[df_f["Year"] == 2014]
df_m = df_m[df_m["Year"] == 2014]
df_f = df_f.loc[["Bolivia","Kazakhstan","Nepal","Uzbekistan","Belarus"]]
df_m = df_m.loc[["Bolivia","Kazakhstan","Nepal","Uzbekistan","Belarus"]]

colors  = ["blue","orange","y","r","violet"]
pie_style = {'linewidth' : 2, 'edgecolor' : 'white' }
df_p = pd.read_csv(url, index_col= 0)
df_p = df_p[df_p["Year"] == 2000]
df_p = df_p.loc[["India","China","United Kingdom","Spain","Romania"]]

x = np.arange(len(df_f['Value']))
width = .20

# Line Chart

plt.figure(figsize=(10,6), layout='constrained')
plt.plot(Branchdata1['Year'],Branchdata1['Value'], label = "Legislative Branch")
plt.plot(Branchdata2['Year'],Branchdata2['Value'], label = "Judicial")
plt.plot(Branchdata3['Year'],Branchdata3['Value'], label = "Department of the interior")
#label the Xaxis and Yaxis
plt.ylabel("Value in millions of dollars ")
plt.xlabel("YEAR ")
plt.title("United States of America education budget analysis")
plt.grid(True)
plt.legend()
plt.show()
plt.close()

 # Bar Chart
plt.figure(figsize = (12,6), layout = "constrained")
plt.bar(x - width / 2, df_m["Value"], width, label="male")
plt.bar(x + width / 2, df_f["Value"], width, label="female")
plt.xticks(x, labels = df_m.index)
plt.ylabel("Value of students enrolled")
plt.xlabel("Region Name")
plt.title("Progression to secondary school of female and male students in the year 2014")
plt.legend()
plt.show()
plt.close()

# Pie Chart
plt.figure(figsize =(12,7),layout = 'constrained')
plt.rcParams['font.size'] = 14
plt.pie(df_p["Value"], labels = df_p.index,autopct = lambda pct: func(pct, df_p["Value"]),colors=colors, wedgeprops = pie_style,)
plt.title('Carbon dioxide emissions in different coutries')
plt.legend()
plt.show()
plt.close()