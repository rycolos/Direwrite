import pandas as pd
import time
refresh = 5
try:
    while True:
     
     #read last line of log file, handle newlines in data   
        try:
            #print(f"Reading {logfile}...")
            df = pd.read_csv('log-test.log', encoding = "ISO-8859-1").tail(1).replace(r'\n',' ', regex=True) 
            last = df[['isotime', 'source', 'heard', 'symbol', 'level', 'latitude', 'longitude', 'comment']]
            row_list = last.values.flatten().tolist()
            isotime, source, heard, symbol, level, latitude, longitude, comment = row_list

        #write to display
            print(isotime)
            #time.sleep(refresh)
    
    #show error if no logs yet
        except:
            print("waiitng for logs")
            #time.sleep(refresh)

    #wait for refresh time
        finally:
            time.sleep(refresh)
            
   
except KeyboardInterrupt:
    pass