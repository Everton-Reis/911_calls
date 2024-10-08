import auxiliary_stephany as ax
import visual_stephany as visual

filepath = "911_Calls_for_Service.csv"

df = ax.Load_datafile(filepath)
sub_df = ax.get_hour("callDateTime", df)
sub_groupby_1=ax.groupby_by_hour(sub_df, 'hour')
#visual.plot_graf_bar(sub_groupby_1, 'calls', 'hour')
sub_groupby_2= ax.groupby_by_hour(sub_df, 'description')
sub_df_2 = ax.most_frequenci(sub_df, sub_groupby_2, 15)
visual.plot_graf_pie_by_hour(sub_df_2, "23", 'test_3.png')