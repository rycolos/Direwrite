import pandas as pd
import time
from papirus import Papirus
from papirus import PapirusTextPos

refresh = 15   #refresh time

#every 30s, read csv, update display, don't update if no change
try:
    while True:
        #read last line of log file, handle newlines in data
        df = pd.read_csv('log-test.log').tail(1).replace(r'\n',' ', regex=True) 
        last = df[['isotime', 'source', 'heard', 'symbol', 'level', 'latitude', 'longitude', 'comment']]
        row_list = last.values.flatten().tolist()
        isotime, source, heard, symbol, level, latitude, longitude, comment = row_list

        #write to display

        # r1 = row_list[0]
        # r2 = row_list[1:5]
        # r3 = row_list[5:7]
        # r4 = row_list[7]

        # # print(f"""
        # # {row_list[0]}
        # # {row_list[1:5]}
        # # {row_list[5:7]}
        # # {row_list[7]}
        # #     """)

        # # print(r1)
        # # print(' '.join(map(str, r2)))
        # # print(' '.join(map(str, r3)))
        # # print(r4)

        print(isotime)
        print(source, heard, symbol, level)
        print(latitude, longitude)
        print(comment)
        
        rot = 0 
        text = PapirusTextPos()
        text.write(isotime)
        text.write(comment)
        #screen.partial_update()

        #wait for refresh time
        time.sleep(refresh)
    
except KeyboardInterrupt:
    pass
