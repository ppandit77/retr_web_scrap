import pandas as pd
from getLOs import get_officer_roster

# Read NMLSIDs from branches.csv
branches_df = pd.read_csv('branches.csv', dtype={'NMLSID': str})

all_results = []

for nmlsid in branches_df['NMLSID']:
    print(f"Fetching for NMLSID: {nmlsid}")
    data = get_officer_roster(nmlsid)
    if data:
        # Optionally, add a column to identify which branch/brokerId this data is from
        for row in data:
            row['NMLSID'] = nmlsid
        all_results.extend(data)
    else:
        print(f"No data for NMLSID: {nmlsid}")

if all_results:
    df = pd.DataFrame(all_results)
    df.to_csv('output.csv', index=False)
    print(f"✅ Aggregated data saved to output.csv ({len(all_results)} records)")
else:
    print("⚠️ No data found for any NMLSID.") 