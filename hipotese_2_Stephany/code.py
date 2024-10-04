import pandas as pd
from matplotlib import pyplot as plt

filepath = "911_Calls_for_Service.csv"
#lendo o arquivo
filepath = "dados_modificados.csv"
sub_df = pd.read_csv(filepath)

def get_hour(entrada,arquivo):
    "Get the hour from the 'entrada' column and transfer it to a new 'time' column'"
    horas=[]
    for key in arquivo[entrada]:
        horas.append((key.split(" ")[1]).split(":")[0])
    sub_df['hour']=horas
    return sub_df

#aplicando a função get_hour
sub_df = get_hour("callDateTime",sub_df)

#agrupando pelo horario
sub_groupby = sub_df.groupby(['hour']).size()
'''sub_groupby.plot.bar(x='calls', y='hour')'''
#plotando o grafico 'ligações x horas'
'''plt.savefig('test.png', dpi=300)'''

#selecionando as descrições mais frequentes
sub_groupby_1= sub_df.groupby(['description']).size()
sub_groupby_1 = sub_groupby_1.sort_values(ascending=False)
primeiros_50=sub_groupby_1.head(15)

#Obtendo apenas as linhas com as descrições mais frequentes
sub_df=sub_df[sub_df['description'].isin(primeiros_50.index)]

#agrupando por hora e descrição
#sub_groupby_2 =  sub_df.groupby(['hour','description']).size().reset_index(name = 'index')
#sub_groupby_2 = sub_groupby_2.sort_values(by=['hour', 'index'], ascending=[True, False])

sub_df_1 = sub_df[sub_df['hour'] == "00"]
print(sub_df_1)
sub_groupby_2 = sub_df_1.groupby(['description']).size()
sub_groupby_2 = sub_groupby_2.sort_values(ascending=[False])

#sub_groupby_2.plot.pie(y='description')
#plt.savefig('test_2.png', dpi=300)

sub_df_2 = sub_df[sub_df['hour'] == "15"]
sub_groupby_3 =  sub_df_2.groupby(['description']).size()
sub_groupby_3 = sub_groupby_3.sort_values(ascending=[False])

sub_groupby_3.plot.pie(y='description')
plt.savefig('test_3.png', dpi=300)