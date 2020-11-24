import praw
import nltk
from collections import Counter
"""nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')"""

reddit = praw.Reddit(client_id='cxDsStgRZ0k3xg',client_secret='2RW2pqoy0mdvghUBM0Juu7F7T3A',username='engg_garbage98',password='nYuker_98',user_agent='tryingsomething')

sub = reddit.subreddit('AWW')

hot= sub.hot(limit=5)
titles=[]
for submission in hot:
    if not submission.stickied:
        titles.append(submission.title)
        print('Title: {}, ups: {}, downs: {}, Have we visited?: {}'.format(submission.title,submission.ups,submission.downs,submission.visited))
        print(20*'^!')

for i in titles: 
    tokens=nltk.word_tokenize(i)
    tags=nltk.pos_tag(tokens)
    print(tags,'\n')
    counts=Counter(tag for words,tag in tags)
    print(counts)
    print()