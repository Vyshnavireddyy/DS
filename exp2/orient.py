import pandas as pd
"""data = {'col1': ['1','2','3','4'],'col2':['a','b','c','d']}
df=pd.DataFrame.from_dict(data,orient='index',columns=['a','b','c','d'])
print(df)"""
#using roll no,name,age,section,and 3 diff subs marks ds qc toc 10 rows for these values
data={'roll':['250','270','348','425','448','449','550','666','700','795'],
      'name':['Akash','Nirmal','Abhishek','Deepthi','Vyshnavi','Sanjana','Niharika','Laya','Simran'],
      'age':['19','19','18','19','19','19','19','19','19','20'],
      'section':['A','C','A','A','C','B','A','C','A','B'],
      'TOC marks':[35,42,41,50,50,30,12,40,32],
      'DS marks':[20,41,36,50,50,23,35,29,34],
      'QC marks':[40,34,24,50,50,38,25,34,40]
      }
df=pd.DataFrame.from_dict(data,orient='index',columns=['1','2','3','4','5','6','7','8','9','10'])
print(df)
print(df.to_csv('studentdata.csv',index=False  ))