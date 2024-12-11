#1. Библиотека requests

import requests

response = requests.get(&#x27;https://api.github.com&#x27;)

print(&quot;Status Code:&quot;, response.status_code)
print(&quot;Response JSON:&quot;, response.json())

#2. Библиотека pandas

#import pandas as pd

#data = pd.read_csv(&#x27;data.csv&#x27;)

#print(data.head())

#average_value = #data[&#x27;column_name&#x27;].mean()
#print(&quot;Average Value:&quot;, #average_value)

#filtered_data = #data[data[&#x27;column_name&#x27;] &gt; #threshold_value]
#print(&quot;Filtered Data:&quot;, filtered_data)

#3. Библиотека matplotlib

#import matplotlib.pyplot as plt

#x = [1, 2, 3, 4, 5]
#y = [2, 3, 5, 7, 11]

#plt.plot(x, y, label=&#x27;Line Graph&#x27;, #color=&#x27;blue&#x27;)

#plt.title(&#x27;Simple Line Plot&#x27;)
#plt.xlabel(&#x27;X-axis&#x27;)
#plt.ylabel(&#x27;Y-axis&#x27;)
#plt.legend()

#plt.show()
