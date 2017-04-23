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

- In this analysis I tried to use gensim and LSA to mine topics from the files. Because my computer didn't have the processing power, I only used a random sample of 100 files for each so it's not comprehensive of the entire dataset
- I used BeautifulSoup to read the xml files and get all of the text from the post tags
- The punctuation was removed from each post then it was broken into word tokens and stopwords were removed.
- The posts were then added to the dictionary if they weren't already and vectorized. 
- The dictionary was saved in [text.dict](https://github.com/boucheral/Data-Analysis/blob/master/Final/Analysis%203/test.dict)
- All of the vectors were saved to [test.mm](https://github.com/boucheral/Data-Analysis/blob/master/Final/Analysis%203/test.mm)
- I then applies term frequency - inverse document frequency (tf-idf) to weight the corpus so that the more important words had a higher value
- I then used the tf-idf model and Latent Semantic Indexing to try and mine 10 different topics from the corpus. 
- If you run the entire program again you will get different results because I only used a sample of the blogs but this time my results were :
```
[(0,
  '0.298*"urllink" + 0.165*"im" + 0.125*"dont" + 0.119*"like" + 0.110*"really" + 0.106*"know" + 0.100*"get" + 0.098*"well" + 0.096*"got" + 0.096*"think"'),
 (1,
  '-0.941*"urllink" + 0.060*"im" + 0.047*"dont" + -0.047*"terrance" + 0.039*"like" + 0.038*"know" + 0.038*"really" + 0.036*"well" + 0.036*"time" + 0.035*"get"'),
 (2,
  '0.633*"ja" + 0.272*"ettã¤" + 0.227*"ei" + 0.193*"se" + 0.175*"kun" + 0.160*"mutta" + 0.152*"sitten" + 0.136*"niin" + 0.119*"ihan" + 0.119*"en"'),
 (3,
  '0.194*"went" + 0.165*"lol" + 0.159*"band" + 0.154*"na" + 0.134*"u" + 0.130*"got" + 0.125*"lolx" + -0.120*"poem" + 0.118*"gon" + 0.116*"haha"'),
 (4,
  '-0.378*"terrance" + -0.265*"krys" + -0.193*"poem" + 0.188*"dont" + -0.178*"new" + 0.159*"im" + -0.145*"got" + -0.112*"went" + 0.111*"feel" + 0.111*"love"'),
 (5,
  '0.607*"terrance" + 0.450*"krys" + -0.181*"poem" + 0.155*"trina" + -0.147*"new" + -0.133*"got" + 0.098*"dont" + -0.092*"poetry" + 0.083*"feel" + 0.079*"sling"'),
 (6,
  '-0.285*"u" + 0.216*"im" + -0.181*"blog" + 0.162*"poem" + -0.138*"tat" + 0.136*"really" + -0.116*"mi" + -0.112*"lolx" + 0.109*"gon" + -0.104*"dun"'),
 (7,
  '0.308*"poem" + 0.248*"blog" + 0.174*"u" + 0.158*"im" + 0.153*"terrance" + 0.148*"krys" + 0.135*"poems" + 0.132*"poetry" + 0.122*"new" + 0.116*"na"'),
 (8,
  '0.359*"poem" + -0.277*"blog" + -0.221*"band" + 0.131*"new" + 0.123*"love" + 0.105*"u" + 0.101*"im" + -0.095*"people" + -0.088*"dave" + 0.087*"red"'),
 (9,
  '0.383*"band" + -0.215*"blog" + 0.202*"poem" + 0.132*"marching" + -0.123*"im" + -0.115*"lol" + 0.107*"na" + 0.094*"told" + -0.091*"work" + -0.091*"today"')]
```

---

### Analysis 4

---

### Analysis 5
