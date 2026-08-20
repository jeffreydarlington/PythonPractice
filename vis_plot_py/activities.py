import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

activities = ['Sleep', 'Working', 'Eating', 'Commuting', 'Leisure']
hours = [8, 9, 2, 1, 5]

df = pd.DataFrame({'Activity': activities, 'Hours': hours})

plt.figure(figsize=(8,8))

plt.pie(
    df['Hours'],
    labels=df['Activity'],
    autopct='%1.1f%%',
    startangle= 90,
    colors= plt.cm.Paired.colors
)

plt.title('Daily Time Allocation (24 Hours)')

plt.show()