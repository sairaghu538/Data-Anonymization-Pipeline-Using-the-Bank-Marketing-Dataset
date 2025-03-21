# Separate the dataset into different DataFrames based on the age group
age_18_30 = df[df['age_group'] == "18-30"]
age_31_50 = df[df['age_group'] == "31-50"]
age_51_70 = df[df['age_group'] == "51-70"]
age_71_plus = df[df['age_group'] == "71+"]

# Save each age group to a separate CSV file
age_18_30.to_csv("age_group_18_30.csv", index=False)
age_31_50.to_csv("age_group_31_50.csv", index=False)
age_51_70.to_csv("age_group_51_70.csv", index=False)
age_71_plus.to_csv("age_group_71_plus.csv", index=False)

from google.colab import files

# Download the CSV files to your local machine
files.download('age_group_18_30.csv')
files.download('age_group_31_50.csv')
files.download('age_group_51_70.csv')
files.download('age_group_71_plus.csv')

from google.colab import drive

# Mount Google Drive
drive.mount('/content/drive')

# Specify the path to save the files in Google Drive
path = '/content/drive/My Drive/'

# Save each file to Google Drive
age_18_30.to_csv(path + "age_group_18_30.csv", index=False)
age_31_50.to_csv(path + "age_group_31_50.csv", index=False)
age_51_70.to_csv(path + "age_group_51_70.csv", index=False)
age_71_plus.to_csv(path + "age_group_71_plus.csv", index=False)
