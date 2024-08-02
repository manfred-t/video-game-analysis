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


### Data querying

Next, we performed basic analysis on the data set. The cleaned data was transferred to an SQL database.


### Tableau

The results were published onto [Tableau Public](https://public.tableau.com/app/profile/manfred.tan/viz/VideoGameSalesAnalysis_17225403248090/VideoGameSalesAnalysis).

<div class='tableauPlaceholder' id='viz1722579427858' style='position: relative'><noscript><a href='#'><img alt='Video Game Sales Analysis ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Vi&#47;VideoGameSalesAnalysis_17225403248090&#47;VideoGameSalesAnalysis&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='VideoGameSalesAnalysis_17225403248090&#47;VideoGameSalesAnalysis' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Vi&#47;VideoGameSalesAnalysis_17225403248090&#47;VideoGameSalesAnalysis&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en-US' /></object></div>
