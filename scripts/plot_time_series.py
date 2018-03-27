
# coding: utf-8

# In[ ]:

from sys import argv
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from scipy import stats
import matplotlib
from matplotlib import cm

ncol = 12
values = np.linspace(0,1, ncol)
colors_ = cm.Paired(values)


def round5(n):
   """Up round a decimal number to next, 0.5 multiple
   
   Arguments:
   - `n`: float
   """
   res = n % 0.5
   plus = 0.5 - res
   if n < 0:
       rounded = n - res
   elif n > 0:
       rounded = n + plus
   else:
       rounded = n
   return rounded

   
if __name__ == '__main__':
   if len(argv) >3:
     fname = argv[1]
     perc5rnd = float(argv[2])
     perc95rnd = float(argv[3])
   elif len(argv) > 1: 
     fname = argv[1]
     perc5rnd = 0.0
     perc95rnd = 0.0
   else:
     print ("""Usage:
       $python3 plot_time_series.py data.tab [ something] [ somethig]
       """)
     exit()

   # Use . as decimal indicator
   data = pd.read_table(fname, index_col=0, decimal='.')
   
   # Area plot
   plt.figure(figsize=(12,7))
   data.T.plot(kind='area', legend =False, color=colors_ )
   plt.xticks(size='small')
   plt.yticks(size='medium')
   plt.ylabel('Relative abundance', size='small')
   plt.ylim(0,1)
   plt.savefig(argv[1]+"_area_plot.png",dpi=500)
   plt.close()
  
   #barplot 
   data.columns = ['Autumn 2012', 'Spring 2013', 'Autumn 2013', 'Spring 2014']
   data.T.plot(kind='barh',stacked=True,color=colors_, legend=False)
   #plt.legend(bbox_to_anchor=(1, 1), loc=2, borderaxespad=0.05 ,labelspacing=0.25)
   #plt.title("Site A", weight='bold', size='large')
   #plt.xlabel("Relative abundance")
   plt.tight_layout()
   plt.savefig(argv[1]+"_barplot.png",dpi=500)

   #Log plot  
   plt.figure(figsize=(12,7))
   data_n = data.T / data.T.iloc[0]
   data_n.plot(legend=False, color=colors_)
   plt.yscale('log')
   plt.ylabel('Relative abundance (Log)', size='small')
   plt.savefig(argv[1]+"_log_plot.png",dpi=500)
   plt.close()   
  
   #Log change  
   mask1 = data_n >= 10
   mask2 = mask1.sum() >= 1
   data_1order = data_n.T[mask2]
   mask3 = np.isinf(data_1order.T.sum())
   #data_1order[~mask3]
   
   plt.figure(figsize=(12,7))
   data_1order[~mask3].T.plot(color=colors_)
   
   plt.yscale('log')
   plt.ylabel('Relative abundance (Log)', size='small')
   plt.savefig(argv[1]+"_log_change.plot.png",dpi=500)
   plt.close()
   
   #Differential plot
   dif = data.T - data['1']
   dif = dif.drop('1' )
   meandif = dif.mean(1)
   stddif = dif.std(1)
   labels=['Autumn 2012', 'Spring 2013', 'Autumn 2013', 'Spring 2014']
   x = [1, 2, 3, 4]
   plt.errorbar(meandif.index, meandif, yerr=stddif, fmt='k--o')
   plt.xticks(x, labels, rotation='horizontal')
   plt.ylabel('Relative Abundance difference (log) ')
   #plt.xlim(1.5,4.5)
   #plt.ylim(-0.005,0.005)
   plt.savefig(argv[1]+"_differential.plot.png",dpi=500)

