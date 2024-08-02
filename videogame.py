import csv
import pandas as pd

def date_parser(date_string, format=None, dayfirst=True, timezone='Europe/London'):
  return pd.to_datetime(date_string, format=format, dayfirst=False, utc=False).tz_localize(timezone)


with open('Video Games Data copy.csv', newline='') as source, open("cleaned_data_VG.csv", "w", encoding='utf-8') as target:
    reader = csv.DictReader(source)
    writer = csv.DictWriter(target, fieldnames =['img','title','console','genre','publisher','developer','critic_score','total_sales','na_sales','jp_sales','pal_sales','other_sales','release_date','last_update'])
    writer.writeheader()

    for row in reader:
      newRowDict = (row)
      if row['release_date']:
        newRowDict['release_date'] = date_parser(row['release_date'])
      else:
        newRowDict['release_date'] = None
      if row['last_update']:
        newRowDict['last_update'] = date_parser(row['last_update'])
      else:
        newRowDict['last_update'] = None
      writer.writerow(newRowDict)