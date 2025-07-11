import pandas as pd

# Desired columns in order
columns = [
    'BranchName', 'Company', 'CompanyState', 'BranchNMLS', 'LoanOfficerID', 'NMLS',
    'FirstName', 'LastName', 'FullName', 'WorkEmail', 'OfficePhone', 'PersonalEmail',
    'CellPhone', 'Loan Ct', 'Loan Vol', 'Joined', 'IsManager', 'Company#',
    'Licensed?', 'Client Stat', 'Last Contact', 'Sales Team', 'Lead Driver'
]

df = pd.read_csv('output.csv')

# Only keep columns that exist in the file
existing_columns = [col for col in columns if col in df.columns]
filtered = df[existing_columns]
filtered.to_csv('output_filtered.csv', index=False)
print(f"Saved filtered data to output_filtered.csv with columns: {existing_columns}") 