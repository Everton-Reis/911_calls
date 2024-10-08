import auxiliary as ax
import avisual as visual

filepath = "911_Calls_for_Service.csv"

df = ax.load_datafile(filepath)
sub_df = ax.get_hour(df)
sub_groupby_1=ax.groupby_by(sub_df, 'hour')
#visual.plot_graf_bar(sub_groupby_1, 'calls', 'hour')
sub_groupby_2= ax.groupby_by(sub_df, 'description')
sub_df_2 = ax.get_first_15_most_frequency(sub_df, sub_groupby_2)
visual.plot_graf_pie_by_hour(sub_df_2, "09", 'test_1.png')