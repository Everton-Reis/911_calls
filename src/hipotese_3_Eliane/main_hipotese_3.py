import calls_eliane as cl
import auxiliary_eliane as ax
import visual_eliane as vs


filepath = "911_clean.csv"

filepath2 = "Call_Distribution_Percentage.csv"

filepath3 = "Cleaned_Call_Distribution.csv"


# Main of the file 'calls_by_category.py'
output_filepath = 'Call_Distribution_Percentage.csv'
cl.process_and_save_data(filepath, output_filepath)

# Main of the file 'auxiliary.py'
ax.process_and_save_data(filepath, filepath2)

# Main of the file 'image_generator.py'
vs.process_and_save_images(filepath, filepath3)