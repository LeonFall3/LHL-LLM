# LLM Project

## Project Task
I picked topic modeling as my task. I took text from the `20_newsgroups` dataset and sorted it into groups

## Dataset
The `20_newsgroups` dataset is pre-divided into training and testing sets, each labeled with true categories provided as both numerical values and strings. The string labels indicate that broader, less specific categories have been subdivided into more detailed ones. The training set contains 11.3k items, while the test set includes 7.5k items, with the 20 categories being almost evenly distributed.

## Pre-trained Model
I utilized the DistilBert model, specifically `DistilBertForSequenceClassification`, along with its paired tokenizer, `DistilBertTokenizer`, for preprocessing. Both were initialized using the pretrained `distilbert-base-uncased` instance.

## Performance Metrics
Since this is a classification task, the model uses a cross-entropy loss function by default to evaluate its performance, as far as I know and based on available documentation. This loss function is applied only when labeled data is provided during training, which applies to my labeled dataset. With 7 labels, random guessing would result in a loss score of approximately **1.95**.  

- In contrast, the model achieved:  
  - A training loss of **0.81** at the start.  
  - A final training loss of **0.52** on the training set.  
  - A test set loss of **0.63**.  


