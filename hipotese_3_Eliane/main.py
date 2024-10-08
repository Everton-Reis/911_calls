import calls_by_category
import auxiliary
import image_generator


filepath = "911_Calls_for_Service.csv"

filepath2 = "Call_Distribution_Percentage.csv"

filepath3 = "Cleaned_Call_Distribution.csv"


# Main of the file 'calls_by_category.py'
output_filepath = 'Call_Distribution_Percentage.csv'
calls_by_category.process_and_save_data(filepath, output_filepath)

# Main of the file 'auxiliary.py'
auxiliary.process_and_save_data(filepath, filepath2)

# Main of the file 'image_generator.py'
image_generator.process_and_save_images(filepath, filepath3)