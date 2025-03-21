from google.colab import files
uploaded = files.upload()
#  upload file to googlecolab and read the file like below

import pandas as pd

#  faker is module not found that is reason faker with error so for that we need install module like below

# pip install faker

from faker import Faker
import hashlib
# Load the dataset
df = pd.read_csv("bank-marketing.csv")

# View dataset structure
print(df.info())
print(df.head())

#  Data Masking (Replace values with a masked format)

df['phone'] = df['phone'].apply(lambda x: 'XXXX-XXX-XXXX' if pd.notna(x) else x)

# Pseudonymization (Replace real names with fake values)

# Store the original 'email' and 'age' columns in a backup DataFrame
# original_data = df[['email', 'age']].copy()

# # Save the backup to a separate file
# original_data.to_csv("bank_marketing_original.csv", index=False)
# fake = Faker()

df['job'] = df['job'].apply(lambda x: fake.job())  # Replace with random job titles

# Generalization (Convert age to ranges)

df['age_group'] = pd.cut(df['age'], bins=[18, 30, 50, 70, 100], labels=["18-30", "31-50", "51-70", "71+"])
df.drop(columns=['age'], inplace=True)  # Drop original age column

# Hashing (Convert contact details to irreversible hashes)

df['email_hash'] = df['email'].apply(lambda x: hashlib.sha256(x.encode()).hexdigest() if pd.notna(x) else x)
df.drop(columns=['email'], inplace=True)  # Remove original email

# Store the Anonymized Data in a New File or Database
# Save the anonymized dataset as a new .csv file for further analysis.

df.to_csv("bank_marketing_anonymized.csv", index=False)
