#splitting files

import pandas as pd

file=pd.read_excel('combi11.xlsx')

grouped_file = file.groupby('ТЦ')


for data in grouped_file:
    
    a=grouped_file.get_group(data[0])
    a.columns=file.columns
    b=a.to_excel('Store'+str(data[0])+'.xlsx',index=False) 
    
    import pandas as pd

#combining

excel_names=[]
for n in range (10, 344):

    names=('Мин УТЗ Store '+str(n)+'.xlsx')
    excel_names.append(names)

excels = [pd.read_excel(name).drop([0,1,2,3,4,5,6], axis=0) for name in excel_names] 
#функцией drop() удаляем лишне строки (если нужно), индексами в списке [] указываем какие строки по порядку удалить 

combined=pd.concat(excels, ignore_index=True)

combined.to_excel("combined_v1.5.xlsx", header=False,index=False)
