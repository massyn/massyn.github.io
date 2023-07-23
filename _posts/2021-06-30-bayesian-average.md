---
layout: post
title: Bayesian Average
author: "Phil Massyn"
categories: math
tags: ["math"]
# image: php.jpg
---

The [Bayesian Average](https://en.wikipedia.org/wiki/Bayesian_average) is a mathematical formula that is used to derive average in a data set when the data set may be small.  Typically you'll see the bayesian average used on sites like Yelp.

Let's assume for a moment, there are a number of restaurants, with various ratings across the board.  Each of them is shown a rating from 1 to 5 stars.  A new restaurant enters the site, and they have received a single, 5 star rating.  If you were to consider all ratings only as an average, this new restaurant with their single rating, will now be considered the highest rated restaurant in the entire city, which may not be entirely accurate.

This is where the Bayesian Average comes in.  In essence, the number of ratings (or votes) has an influence on the total outcome.  It may be better to illustrate this with an example.  Here is our data set.  Every line contains the result of an individual vote.  Right at the end, you'll see Luigi's, which had a single rating of 5.

| Vote | Rating |
|--|--|
|Mario|4|
|Brando|4|
|Rocco|3|
|Franco|2|
|Mario|3|
|Brando|2|
|Rocco|5|
|Franco|5|
|Mario|2|
|Brando|2|
|Rocco|3|
|Mario|3|
|Brando|3|
|Luigi|5|

## Step 1 - Tally it up

We need to tally up the totals. Average the rating for each restaurant (this_rating), and count how many ratings (this_num_votes) each restaurant received.

|Vote|this_rating|this_num_votes|
|--|--|--|
|Mario|3.00|4|
|Brando|2.75|4|
|Rocco|3.67|3|
|Franco|3.50|2|
|Luigi|5.00|1|

## Step 2 - Calculate average

Calculate the average rating (avg_rating) and the average number of votes (avg_num_votes) by averaging the totals received from step 1. In this example **avg_rating = 3.58** and **avg_num_votes = 2.80**

## Step 3 - Calculate the Bayesian average

With all of this information, we can now calculate the bayesian average for each restaurant. The formula for the bayesian average is :

```
br = ( (avg_num_votes * avg_rating) + (this_num_votes * this_rating) ) / (avg_num_votes + this_num_votes)
```

This leaves us with the following result. Even though Luigi’s only has one vote, the Bayesian Average comes in at 3.96. While it is still higher than all of his competitors, it is more realistic considering the total number of votes that have been received.

|Vote|this_rating|this_num_votes|Bayesian|
|--|--|--|--|
|Mario|3.00|4|3.24|
|Brando|2.75|4|3.09|
|Rocco|3.67|3|3.63|
|Franco|3.50|2|3.55|
|Luigi|5.00|1|3.96|

## Python example

This example will demonstrate how you can calculate the Bayesian Average using Python.

```python
import json
# Bayesian Average example in Python

# Step 0 - Feed the data set with the data we are interested in
data_set = [
	{'vote' : 'Mario'	, 'rating' : 4},
	{'vote' : 'Brando'	, 'rating' : 4},
	{'vote' : 'Rocco'	, 'rating' : 3},
	{'vote' : 'Franco'	, 'rating' : 2},
	{'vote' : 'Mario'	, 'rating' : 3},
	{'vote' : 'Brando'	, 'rating' : 2},
	{'vote' : 'Rocco'	, 'rating' : 5},
	{'vote' : 'Franco'	, 'rating' : 5},
	{'vote' : 'Mario'	, 'rating' : 2},
	{'vote' : 'Brando'	, 'rating' : 2},
	{'vote' : 'Rocco'	, 'rating' : 3},
	{'vote' : 'Mario'	, 'rating' : 3},
	{'vote' : 'Brando'	, 'rating' : 3},
	{'vote' : 'Luigi'	, 'rating' : 5}
]

# Step 1 - Tally up the totals
totals = {}
for d in data_set:
    # -- setup the dictionary
    if not d['vote'] in totals:
        totals[d['vote']] = { '_total' : 0, 'this_num_votes' : 0, 'this_rating' : 0.0 , 'bayesian_average' : 0 }

    # -- start counting the individual results 
    totals[d['vote']]['this_num_votes'] += 1
    totals[d['vote']]['_total'] += d['rating']
    totals[d['vote']]['this_rating'] = totals[d['vote']]['_total'] / totals[d['vote']]['this_num_votes']

# Step 2 - Calculate the averages
count = 0
avg_rating_total = 0
avg_rating = 0
avg_num_votes_total = 0
avg_num_votes = 0

for d in totals:
    count += 1
    
    # == calculate avg_rating
    avg_rating_total += totals[d]['this_rating']
    avg_rating = avg_rating_total / count
    
    # == calculate avg_num_votes
    avg_num_votes_total += totals[d]['this_num_votes']
    avg_num_votes = avg_num_votes_total / count  

# Step 3 - Calculate the Bayesian Average
for d in totals:
    totals[d]['bayesian_average'] = ( (avg_num_votes * avg_rating) + (totals[d]['this_num_votes'] * totals[d]['this_rating']) ) / (avg_num_votes + totals[d]['this_num_votes'])
    print('{vote} = {br}'.format(vote = d, br = totals[d]['bayesian_average']))

# Step 4 - Show the data we have collected, including the Bayesian Averages
print(json.dumps(totals,indent=4))
```

