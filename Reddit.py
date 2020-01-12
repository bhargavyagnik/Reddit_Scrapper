import praw
import pandas as pd
import datetime as dt
import pandas as pd

reddit=praw.Reddit(client_id='-bJnuIJV5jOLRQ',client_secret='BOYbv2nQLSEUFS2BiDDG4593lVI',user_agent='Reddit_Scrapper',username='bhargav99',password='Bhargav99@')

list_text=['MachineLearning']
posts=[]
for it in list_text:
    its=str(it)
    sub = reddit.subreddit(its)
    for post in sub.hot(limit=10):
        posts.append([post.title, post.score, post.id, post.subreddit, post.url, post.num_comments, post.selftext, post.created])
    posts = pd.DataFrame(posts,columns=['title', 'score', 'id', 'subreddit', 'url', 'num_comments', 'body', 'created'])
    print(posts)
    adr=its+'.csv'
    posts.to_csv(adr)
