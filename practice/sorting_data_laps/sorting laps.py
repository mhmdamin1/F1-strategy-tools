import pandas as pd

data = {
    "Driver": ["VER", "HAM", "LEC", "NOR"],
    "Lap1": [91.2, 90.1, 91.4, 90.9],
    "Lap2": [90.8, 91.7, 91.0, 91.1],
    "Lap3": [91.5, 92.0, 91.8, 90.7]
}

df = pd.DataFrame(data)
print(df)
df["Avr_lap"] = df[["Lap1", "Lap2", 'Lap3']].mean(axis=1)

result = df.sort_values(by="Avr_lap")
print(result)

result2 = df.sort_values(by="Avr_lap", ascending=False)
print(result2)

fastest = df["Avr_lap"].idxmin()
driver = df.loc[fastest, "Driver"]
print(df.loc[fastest, "Driver"])
avr = df.loc[fastest, "Avr_lap"]
print(df.loc[fastest, "Avr_lap"])

print(f"the fasrest driver is {driver} with an {avr} laptime of 90.89999 secs")

slowest = df["Avr_lap"].idxmax()
driver = df.loc[slowest, "Driver"]
print(df.loc[slowest, "Driver"])
avr = df.loc[slowest, "Avr_lap"]
print(df.loc[slowest, "Avr_lap"])
print(f"the slowest driver is {driver} with an {avr} laptime of 90.89999 secs")
