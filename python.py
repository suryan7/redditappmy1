import praw
from textblob import TextBlob

# Function to categorize comment sentiment
def categorize_sentiment(comment):
    analysis = TextBlob(comment.body)
    if analysis.sentiment.polarity > 0:
        return 'positive'
    elif analysis.sentiment.polarity < 0:
        return 'negative'
    else:
        return 'neutral'

# Function to analyze Reddit post
def analyze_reddit_post(url):
    # Specify your Reddit API credentials
    reddit_client_id = 'KgUj77hxO9B_oiFOL9nnVg'
    reddit_client_secret = 'Sn3XWSwmvXBDETO2lIYEok6_vNhHfQ'
    reddit_user_agent = 'Reddit Post Analyzer by /u/sur0007'

    # Authenticate with Reddit API
    reddit = praw.Reddit(client_id=reddit_client_id,
                         client_secret=reddit_client_secret,
                         user_agent=reddit_user_agent)
    
    # Get submission object for the provided URL
    submission = reddit.submission(url=url)
    
    # Fetch comments from the submission
    submission.comments.replace_more(limit=None)
    
    # Initialize counters for sentiment categories
    positive_count = 0
    negative_count = 0
    neutral_count = 0
    
    # Iterate through comments and categorize sentiment
    for comment in submission.comments.list():
        sentiment = categorize_sentiment(comment)
        if sentiment == 'positive':
            positive_count += 1
        elif sentiment == 'negative':
            negative_count += 1
        else:
            neutral_count += 1
    
    # Print results
    print("Sentiment Analysis Results:")
    print(f"Total Comments: {len(submission.comments)}")
    print(f"Positive Comments: {positive_count}")
    print(f"Negative Comments: {negative_count}")
    print(f"Neutral Comments: {neutral_count}")

# Example usage
if __name__ == "__main__":
    reddit_post_url = input("Enter the URL of the Reddit post you want to analyze: ")
    analyze_reddit_post(reddit_post_url)
