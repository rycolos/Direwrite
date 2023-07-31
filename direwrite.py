import pandas as pd
import time
from datetime import date
from papirus import PapirusTextPos

#CONFIG
refresh = 25   #refresh time
logdir = '/home/gktnc/direwolf-logs'

today = date.today()
logfile = f"{logdir}/{today}.log"

#initialize Papirus display
text = PapirusTextPos()
text.AddText("Direwrite for APRS", 20, 20, Id="splash", size=20)
time.sleep(3)
text.RemoveText("splash")

text.AddText(f"Initializing...\nRefresh rate {refresh} seconds.", 0, 0, Id="message", size=15)

#at refresh interval, read csv, update display, don't update if no change
try:
    while True:
     
     #read last line of log file, handle new lines in data   
        try:
            #print(f"Reading {logfile}...")
            df_curr = pd.read_csv(logfile, encoding = "ISO-8859-1").tail(1).replace(r'\n',' ', regex=True)
            if df_curr.equals(df_prev):
                cols = df_curr[['isotime', 'source', 'heard', 'symbol', 'level', 'latitude', 'longitude', 'comment']]
                row_list = cols.values.flatten().tolist()
                isotime, source, heard, symbol, level, latitude, longitude, comment = row_list

            #write to display
                msg = (f"{isotime}\n"
                    f"{source}, {heard}, {symbol}, {level}\n"
                    f"{latitude}, {longitude}\n"
                    f"{comment}\n"
                    )
                text.UpdateText("message", msg)
            df_prev = df_curr
    
    #show error if no logs yet
        except:
            text.UpdateText("message", "Waiting for logs to populate...")
      
      #wait for refresh time  
        finally:
            time.sleep(refresh)
   
except KeyboardInterrupt:
    text.Clear()