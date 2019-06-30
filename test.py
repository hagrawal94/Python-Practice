import pandas as pd
dictionary={"Name":["Harshit","Swati","Aditi"],"Age":[20,30,20]}
dictionary1={"Name":["Shaily","Anshika","Palak"],"Age":[20,30,20]}
df=pd.DataFrame(dictionary,index=[1,2,3])
df1=pd.DataFrame(dictionary1,index=[1,2,3])
merged=pd.merge(df,df1)
print(merged)
