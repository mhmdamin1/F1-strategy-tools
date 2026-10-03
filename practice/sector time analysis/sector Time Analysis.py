# mohamed amin
import pandas as pd
import numpy as np

drivers = ["ham", "rus", "alonso", "norris"]

sector_time = {
               "ham": [22.4, 23.9, 25.7],
               "rus": [21.4, 23.9, 26.7],
               "alonso": [20.8, 26.9, 27.1],
               "norris": [20, 22, 26.900]
                        }
df = pd.DataFrame(sector_time)
print(df)

print(df.mean())
print(df.min())
print(df.std())

result = {
          "drivers": ["hamilton", "russle", "alonso", "norris"],
          "Avr_SecTime": [24.000000, 24.000000, 24.933333, 22.966667],
          "Best_SecTime": [22.4, 21.4, 20.8, 20.0],
          "consistency" : [1.652271,2.651415, 3.580968, 3.550117]
}

d1 = pd.DataFrame(result)
print(d1)

