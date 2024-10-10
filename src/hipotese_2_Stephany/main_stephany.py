import auxiliary_stephany as ax
import visual_stephany as visual

filepath = "../../911_clean.csv"

#Treating the dataframe.
df = ax.load_datafile(filepath)
sub_df = ax.get_hour(df)

#Data relating calls per hour.
sub_groupby_1= sub_df.groupby('hour').size()
visual.plot_graf_bar(sub_groupby_1, 'calls', 'hour', 'calls_per_hour.png')

#Data relating occurrences per hour.
sub_groupby_2= sub_df.groupby('description').size()
sub_df_2 = ax.get_first_15_most_frequency(sub_df, sub_groupby_2)
visual.plot_graf_pie_by_hour(sub_df_2, "09", 'description_per_hour.png', 'description')

#Data relating the severity of incidents per hour.
visual.plot_graf_pie_by_hour(sub_df_2, "18", 'priority_per_hour.png', 'priority')