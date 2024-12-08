# LLM Project

## Project Task
I picked topic modeling as my task. I took text from the `20_newsgroups` dataset and sorted it into groups

## Dataset
The `20_newsgroups` dataset is pre-divided into training and testing sets, each labeled with true categories provided as both numerical values and strings. The string labels indicate that broader, less specific categories have been subdivided into more detailed ones. The training set contains 11.3k items, while the test set includes 7.5k items, with the 20 categories being almost evenly distributed.

## Pre-trained Model
I utilized the DistilBert model, specifically `DistilBertForSequenceClassification`, along with its paired tokenizer, `DistilBertTokenizer`, for preprocessing. Both were initialized using the pretrained `distilbert-base-uncased` instance.

## Performance Metrics
Avg Weighted Precision = 75%
Avg Weighted Recall = 80%
Avg Weighted F1 = 80%

Avg Unweighted Precision = 75%
Avg Unweighted Recall = 74%
Avg Unweighted F1 = 74%

F1 Accuracy = 80%



## Bussiness and Data
This model could be used in policial applications such as political parties or reaserch to gain insight into public opinion. Other applications for this type of could be scanning reviews of a product to gain sentiment from the customer base. 
