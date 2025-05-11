from etls.reddit_etl import connect_reddit, extract_posts
from utils.constants import CLIENT_ID, SECRET


def reddit_pipeline(filename: str, subreddit: str, time_filter='day', limit=None):
    #Connect reddit instance
    instance = connect_reddit(CLIENT_ID, SECRET, 'Airscholar Agent')
    #Extract
    posts = extract_posts(instance, subreddit, time_filter, limit)
    #Transform

    #Load to csv