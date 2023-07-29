import pandas as pd
from papirus import Papirus
from papirus import PapirusText


#read last line of log file, handle newlines in data
df = pd.read_csv('log-test.log').tail(1)
df = df.replace(r'\n',' ', regex=True) 

selection = df[['isotime', 'source', 'heard', 'symbol', 'level', 'latitude', 'longitude', 'comment']]
row_list = selection.values.flatten().tolist()

print(row_list[0])
print(*row_list[1:5])
print(*row_list[5:7])
print(row_list[7])

screen.partial_update()