import pandas as pd
import time
from datetime import date
from papirus import PapirusTextPos

refresh = 15   #refresh time
logdir = '~/direwolf-logs'
file1 = 'log-test.log'
logfile = f"{logdir}/{date.today}.log"

#initialize Papirus
text = PapirusTextPos()
text.Clear()

#every 30s, read csv, update display, don't update if no change
try:
    while True:
     
     #read last line of log file, handle newlines in data   
        try:
            df = pd.read_csv(logfile).tail(1).replace(r'\n',' ', regex=True) 
            last = df[['isotime', 'source', 'heard', 'symbol', 'level', 'latitude', 'longitude', 'comment']]
            row_list = last.values.flatten().tolist()
            isotime, source, heard, symbol, level, latitude, longitude, comment = row_list

        #write to display
            msg = (f"{isotime}\n"
            f"{source}, {heard}, {symbol}, {level}\n"
            f"{latitude}, {longitude}\n"
            f"{comment}\n"
            )
            print(msg)
            text.AddText(msg, 0, 0, Id="decode", size=15)
    
    #show error if no logs yet
        except:
            text.AddText("Waiting for logs to populate...", 0, 0, Id="error", size=15)

    #wait for refresh time
        finally:
            time.sleep(refresh)
            text.Clear()

            
    
except KeyboardInterrupt:
    pass
