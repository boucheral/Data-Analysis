# Final Project

---

### Data
- Data is the [Blog Corpus](http://u.cs.biu.ac.il/~koppel/BlogCorpus.htm) 
- All files are assuming the data is in a file named Data
- I also used [AFINN-111](http://www2.imm.dtu.dk/pubdb/views/publication_details.php?id=6010) to try and build a basic model for sentiment analysis in Analysis 2

---

### Analysis 1 
- Got all of the filenames from the datafiles in the dataset
- Each of the files was labeled in the form 
> [id].[sex].[age].[topic].[sign].xml
- I broke down the filename to extract all of this data and saved it into the [filenameinfo.csv](https://github.com/boucheral/Data-Analysis/blob/master/Final/csv/filenameinfo.csv)
- I created a boxplot for the ages of males vs females as well as a bargraph showing the distribution of males vs female
  - Both show that it is about equally distributed
- Then I compared the average ages between men and women based on the topic their blog was about. 
- I completed a T-test comparing male and female for each topic and rejected the null hypothesis if the p-value was less then .05 then made a boxplot and bargraph for each of those topics

---

### Analysis 2
- I imported all of the filename data to use in this Analysis
- I also created a sentiment dictionary from the AFINN-111 document to use on the blogs
- With this I created various functions in order to extract the positive and negative features from each of the blogs and add them into the dataframe
- This was then saved into [sentiment.csv](https://github.com/boucheral/Data-Analysis/blob/master/Final/csv/sentiment.csv) file 
- Using this, I compared the average positive and negative values for each topic of blog and used the t test to again compare between men and women. 
- I created boxplots for each topic where the p-value was < .05

---

### Analysis 3

- 

---

### Analysis 4

---

### Analysis 5
