# Reddit_Scrapper
A reddit scrapper in python
czcbznfsnsfnfnf
![](http://www.vectorsland.com/imgd/l58587-reddit-logo-55371.png)
Reddit is an American social news aggregation, web content rating, and discussion website. Registered members submit content to the site such as links, text posts, and images, which are then voted up or down by other members. 
PRAW, an acronym for “Python Reddit API Wrapper”, is a python package that allows for simple access to reddit’s API. PRAW aims to be as easy to use as possible and is designed to follow all of reddit’s API rules. You have to give a useragent that follows the rules, everything else is handled by PRAW so you needn’t worry about violating them.

Here’s a quick peek, getting the first 5 submissions from the ‘hot’ section of the ‘opensource’ subreddit:

>>> import praw
>>> r = praw.Reddit(user_agent='my_cool_application')
>>> submissions = r.get_subreddit('opensource').get_hot(limit=5)
>>> [str(x) for x in submissions]
This will display something similar to the following:

