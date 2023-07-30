import pandas as pd
import time
from papirus import PapirusText
from papirus import PapirusTextPos

refresh = 15   #refresh time
file = 'log-test.log'

#every 30s, read csv, update display, don't update if no change
try:
    while True:
        #read last line of log file, handle newlines in data
        df = pd.read_csv(file).tail(1).replace(r'\n',' ', regex=True) 
        last = df[['isotime', 'source', 'heard', 'symbol', 'level', 'latitude', 'longitude', 'comment']]
        row_list = last.values.flatten().tolist()
        isotime, source, heard, symbol, level, latitude, longitude, comment = row_list

        #write to display
        msg = (f"""
            {isotime})
            {source}, {heard}, {symbol}, {level}
            {latitude}, {longitude})
            {comment}
            """)
        print(msg)
        
        rot = 0 
        text = PapirusTextPos()
        text.AddText(f"{isotime}\n{source} {heard} {symbol} {level}\n{latitude} {longitude}\n{comment}",
            0, 0, Id="row1", size=15)

        #wait for refresh time
        time.sleep(refresh)
    
except KeyboardInterrupt:
    pass
