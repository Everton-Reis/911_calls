import auxiliary_stephany as ax
import visual_stephany as visual

filepath = "911_Calls_for_Service.csv"

#Tratando o dataframe
df = ax.load_datafile(filepath)
sub_df = ax.get_hour(df)

#Dados relacionando ligações por hora.
sub_groupby_1=ax.groupby_by(sub_df, 'hour')
visual.plot_graf_bar(sub_groupby_1, 'calls', 'hour', 'calls_per_hour.png')

#Dados relacionando ocorencias por hora.
sub_groupby_2= ax.groupby_by(sub_df, 'description')
sub_df_2 = ax.get_first_15_most_frequency(sub_df, sub_groupby_2)
visual.plot_graf_pie_by_hour(sub_df_2, "09", 'description_per_hour.png', 'description')

#Dados relacionando gravidade das ocorencias por hora.
visual.plot_graf_pie_by_hour(sub_df_2, "18", 'priority_per_hour.png', 'priority')