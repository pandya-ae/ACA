#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd

df = pd.read_excel(r'C:\Users\pandy\Documents\UGM\Akademik\Semester 3\MII2201 Analisis Algoritma dan Kompleksitas\6\Tugas\radixSort.xlsx')
print(df)


# In[2]:


import matplotlib.pyplot as plt

x = df['n']
y = df['avg']
fig, ax = plt.subplots()
ax.plot(x, y, '-o', label = 'radix sort')
plt.xlabel('number of data (n)')
plt.xticks(rotation = 45)
plt.ylabel('average running time (seconds)')
plt.title('Radix sort time complexity')
plt.xticks(rotation = 45)
plt.grid(linestyle = 'dotted')
plt.legend()
plt.savefig('radixSort.png', dpi = 300, bbox_inches = 'tight')

for i, txt in enumerate(y):
    ax.annotate(txt, (x[i], y[i]))

plt.show()


# In[ ]:




