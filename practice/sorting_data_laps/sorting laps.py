import pandas as pd

data = {
    "Driver": ["VER", "HAM", "LEC", "NOR"],
    "Lap1": [91.2, 90.1, 91.4, 90.9],
    "Lap2": [90.8, 91.7, 91.0, 91.1],
    "Lap3": [91.5, 92.0, 91.8, 90.7]
}

df = pd.DataFrame(data)
print("---> first DataFrame")
print(df)
df["Avr_lap"] = df[["Lap1", "Lap2", 'Lap3']].mean(axis=1)

result = df.sort_values(by="Avr_lap")
print("")
print("--->After add Avr_lap:")
print(result)

result2 = df.sort_values(by="Avr_lap", ascending=False)
print("")
print("--->After make is ascending:")
print(result2)

print("")
print("=> the fastest driver details:" )
fastest = df["Avr_lap"].idxmin()
driver = df.loc[fastest, "Driver"]
print(df.loc[fastest, "Driver"])
avr = df.loc[fastest, "Avr_lap"]
print(df.loc[fastest, "Avr_lap"])
print(f"the fasrest driver is {driver} with an {avr} laptime of 90.89999 secs")

print("")
print("=> the slowest driver details:" )
slowest = df["Avr_lap"].idxmax()
driver = df.loc[slowest, "Driver"]
print(df.loc[slowest, "Driver"])
avr = df.loc[slowest, "Avr_lap"]
print(df.loc[slowest, "Avr_lap"])
print(f"the slowest driver is {driver} with an {avr} laptime of 90.89999 secs")
=> the slowest driver details:
LEC
91.39999999999999
the slowest driver is LEC with an 91.39999999999999 laptime of 90.89999 secs

"""
out put :

---> first DataFrame
  Driver  Lap1  Lap2  Lap3
0    VER  91.2  90.8  91.5
1    HAM  90.1  91.7  92.0
2    LEC  91.4  91.0  91.8
3    NOR  90.9  91.1  90.7

--->After add Avr_lap:
  Driver  Lap1  Lap2  Lap3    Avr_lap
3    NOR  90.9  91.1  90.7  90.900000
0    VER  91.2  90.8  91.5  91.166667
1    HAM  90.1  91.7  92.0  91.266667
2    LEC  91.4  91.0  91.8  91.400000

--->After make is ascending:
  Driver  Lap1  Lap2  Lap3    Avr_lap
2    LEC  91.4  91.0  91.8  91.400000
1    HAM  90.1  91.7  92.0  91.266667
0    VER  91.2  90.8  91.5  91.166667
3    NOR  90.9  91.1  90.7  90.900000

=> the fastest driver details:
NOR
90.89999999999999
the fasrest driver is NOR with an 90.89999999999999 laptime of 90.89999 secs

=> the slowest driver details:
LEC
91.39999999999999
the slowest driver is LEC with an 91.39999999999999 laptime of 90.89999 secs

"""
