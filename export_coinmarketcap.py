#!/usr/bin/python
import coinmarketcap_usd_history
import csv


# Parameters
csv_of_cryptocurrencies = 'cryptos.csv' 
startdate = '2014-12-30'
enddate = '2018-04-17'


# Convert CSV of all cryptos into a python readable list
cryptocurrencies = []
with open(csv_of_cryptocurrencies) as csvDataFile:
    csvReader = csv.reader(csvDataFile)
    for row in csvReader:
        cryptocurrencies.append(row[0])
        
        
# Rank of cryprocurrency on coinmarketcap by market cap, is used to index files
i = 1

             
for cryptocurrency in cryptocurrencies:
    
    # Extract data from coinmarketcap as tuple
    data = coinmarketcap_usd_history.main([cryptocurrency, startdate, enddate])
    
    
    # Format the tuple into a list of lists, makes it easier to export into CSV
    # Try / except for cases when a coin was not listed before end-date
    t = len(data[1])
    d = [[] for x in xrange(t+1)]
    d[0] = data[0]
    
    try:
        d[1] = data[1][0]
        for k in range(t):
            index = k + 1
            d[index] = data[1][k]
    except:
        pass
    
    
    # Create filename for exported csv
    filename = str(i) + '-' + str(cryptocurrency) +'.csv'
    
    
    # Write into CSV file
    with open(filename, "wb") as f:
        writer = csv.writer(f)
        writer.writerows(d)


    # Increment rank
    i = i + 1
    

