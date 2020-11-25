#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd

df = pd.read_excel(r'C:\Users\pandy\Documents\UGM\Akademik\Semester 3\MII2201 Analisis Algoritma dan Kompleksitas\6\Tugas\sort.xlsx')
print(df)


# In[2]:


import matplotlib.pyplot as plt

x = df['n']
yS = df['avgS']
yH = df['avgH']
yR = df['avgR']
fig, ax = plt.subplots()
ax.plot(x, yS, '-o', label = 'selection sort')
ax.plot(x, yH, '-o', label = 'heap sort')
ax.plot(x, yR, '-o', label = 'radix sort')
plt.xlabel('number of data (n)')
plt.ylabel('average running time (seconds)')
plt.title('Sorting time complexity')
plt.xticks(rotation = 45)
plt.grid(linestyle = 'dotted')
plt.legend()
plt.savefig('sortCombined.png', dpi = 300, bbox_inches = 'tight')

for i, txt in enumerate(yS):
    ax.annotate(txt, (x[i], yS[i]))

for i, txt in enumerate(yH):
    ax.annotate(txt, (x[i], yH[i]))
    
for i, txt in enumerate(yR):
    ax.annotate(txt, (x[i], yR[i]))

plt.show()


# In[ ]:




