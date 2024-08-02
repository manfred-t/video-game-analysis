# Video Game Sales Analysis Project

### Overview:

Our objective with this analysis is to gain insights into video game market and estabilsh key decisons to increase profit for video game distributors.

Our data set is the [Video Games Dataset](https://www.kaggle.com/datasets/ujjwalaggarwal402/video-games-dataset) found on Kaggle.


### Data cleanup:

Firstly, the data must be cleaned in order to be processed efficiently in SQL. The numerical values are valid, however some of the dates are formatted differently. Thus, in order to normalize the dates, we used a python script included in the repository. The main normalization function is as follows:

```
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
```
