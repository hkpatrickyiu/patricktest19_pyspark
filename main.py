#%%
#import dlt
#from pyspark.sql.functions import col, lit, to_date, concat_ws, input_file_name, reverse, split, create_map, date_format, explode, from_utc_timestamp, to_timestamp, convert_timezone, regexp_extract, when
#from pyspark.sql.types import StructType, StructField, StringType, IntegerType, ArrayType, DecimalType, DateType
#from itertools import chain
#from datetime import date
#from dateutil.relativedelta import relativedelta
import pandas as pd
import json

import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np

from jsonpath_ng import jsonpath, parse
import urllib.request, json 
with urllib.request.urlopen("https://www.hko.gov.hk/cis/dailyExtract/dailyExtract_2024.xml") as url:
    json_data = json.load(url)

df = pd.DataFrame(json_data)
for monthlyData in df.stn.data:
    month = monthlyData['month']
    print (month)
    
    if not monthlyData['dayData'] is None and monthlyData['dayData']:
#        plt.plot(monthlyData['dayData'][0], monthlyData['dayData'][3])
        dayArray = list()
        avgTempArray = list()
        for dayData in monthlyData['dayData']:
            if dayData[0].isnumeric():
                dayArray.append(dayData[0])
                avgTempArray.append(float(dayData[3]))
        plt.bar(np.asarray(dayArray, float), avgTempArray, color ='maroon', 
        width = 0.6)
        plt.xlabel(f"Day in month {month}")
        plt.ylabel("Temperature (avg)")
        plt.tick_params(which='major', length=7)

        plt.title("Students enrolled in different courses")

        plt.show()

    for dailyData in monthlyData['dayData']:
        day = dailyData[0]
        print(f'month:{month},day:{day},avgTem:{dailyData[3]}')
"""
x = np.linspace(0, 20, 100)
plt.plot(x, np.sin(x))
plt.show()
"""
#    print(data)
""" jsonpath_expression = parse('$.stn.data[*]')

for monthlyData in jsonpath_expression.find(json_data):
    print(monthlyData.value)
    for dailyData in parse('$.dayData[*]').find(monthlyData.value):
        print(f'data: {dailyData.value}')

 """
        # %%
