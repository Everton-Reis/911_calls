# 911 Calls

## Objective

This project aims to analyze and process data from the **'911_Calls_for_Service'** dataset. The analysis focuses on three key hypotheses related to the distribution and frequency of emergency calls across different districts and time periods:

1. **Hypothesis 1**: The most dangerous district is the one with the highest number of emergency calls.
   - _by Everton_

2. **Hypothesis 2**: Specific types of incidents are more likely to occur at night or during particular time intervals.
   - _by Stephany_

3. **Hypothesis 3**: The distribution of emergency calls by category is unevenly spread across Baltimore's districts.
   - _by Eliane_

## General Challenges

During the project, several challenges arose, especially regarding data consistency and complexity:

- **Data Irregularities**: The 'description' column in the dataset contained numerous inconsistencies and required substantial cleaning to ensure proper categorization and analysis.
- **Testing**: Given the dataset's complexity, creating unit tests that covered all possible errors proved difficult. We assumed that users would contribute by reporting or fixing any issues encountered.
- **Documentation**: Setting up and integrating Sphinx for generating project documentation introduced several technical challenges, which were resolved throughout the project's development.

## Contributions

Each team member took responsibility for developing their respective hypothesis. Collaboration was key in certain shared tasks, particularly in the creation of the data cleaning module and the Sphinx-based documentation. Additionally, all contributors were involved in writing tests and ensuring the project was well-documented.

## How to Run the Project

To work with this project, follow these steps:

1. Download the dataset zip from Kaggle: [911 Calls for Service Dataset on Kaggle](https://www.kaggle.com/datasets/ahmadrafiee/911-calls-for-service-metadata-1-million-record).
2. Place the CSV contained in the zip inside the `root`.

### Install Dependencies

Install the necessary Python packages by running the following command in your terminal:

``bash
pip install -r requirements.txt

### Data Cleaning

The data cleaning process was executed through the `limpeza_main.py` module. This module was responsible for handling and correcting inconsistencies in the dataset, making sure that the data was clean and ready for further analysis.
Make sure the dataset is in the `root` and run `limpeza_main.py` to generate the CSV that we will work with:
911_clean.csv.

### Module Execution

1. Ensure you are in the respective folders within the src directory.

To run the modules for Hypothesis 1 (Everton):

cd src/hipotese_1_Everton
python main_everton.py

To run the modules for Hypothesis 2 (Stephany):
cd ../hipotese_2_Stephany
python main_stephany.py

To run the modules for Hypothesis 3 (Eliane):
cd ../hipotese_3_Eliane
python main_eliane.py

##### Generate HTML Documentation

2. Navigate to the docs folder and execute the following command to generate the HTML:
cd ../../docs
make html

### Sphinx

To access the Sphinx documentation go to docs/build/html/index.html