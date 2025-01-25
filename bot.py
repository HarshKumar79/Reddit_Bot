import praw
import logging
from utils import handle_rate_limit
from config import reddit_credentials

# Logging setup
logging.basicConfig(
    filename="bot.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logging.info("Bot started")

try:
    # Initialize Reddit instance
    reddit = praw.Reddit(
        client_id=reddit_credentials["CLIENT_ID"],
        client_secret=reddit_credentials["CLIENT_SECRET"],
        username=reddit_credentials["USERNAME"],
        password=reddit_credentials["PASSWORD"],
        user_agent=reddit_credentials["USER_AGENT"]
    )

    # Functionality 1: Reply to posts in a subreddit
    def reply_to_posts(subreddit_name, limit=5):
        logging.info(f"Starting to reply to posts in subreddit: {subreddit_name}")
        for post in reddit.subreddit(subreddit_name).hot(limit=limit):
            logging.info(f"Processing post: {post.title}")
            try:
                post.reply("Nice post! I'm a bot :) (Automated message)")
                logging.info(f"Replied to post: {post.title}")
            except praw.exceptions.RedditAPIException as e:
                logging.error(f"Error replying to post: {e}")
                handle_rate_limit(e)

    # Functionality 2: Send a direct message
    def send_direct_message(recipient, subject, message):
        logging.info(f"Attempting to send message to {recipient}")
        try:
            reddit.redditor(recipient).message(subject, message)
            logging.info(f"Message sent to {recipient}: {subject}")
        except praw.exceptions.RedditAPIException as e:
            logging.error(f"Error sending message to {recipient}: {e}")
            handle_rate_limit(e)

    # Functionality 3: Like a post
    def like_post(post_id):
        logging.info(f"Attempting to like post: {post_id}")
        try:
            post = reddit.submission(id=post_id)
            post.upvote()
            logging.info(f"Post liked: {post.title}")
        except praw.exceptions.RedditAPIException as e:
            logging.error(f"Error liking post {post_id}: {e}")
            handle_rate_limit(e)

    # Functionality 4: Post to a subreddit
    def post_to_subreddit(subreddit_name, title, content):
        logging.info(f"Attempting to post to subreddit: {subreddit_name}")
        try:
            reddit.subreddit(subreddit_name).submit(title=title, selftext=content)
            logging.info(f"Posted to {subreddit_name} with title: {title}")
        except praw.exceptions.RedditAPIException as e:
            logging.error(f"Error posting to subreddit {subreddit_name}: {e}")
            handle_rate_limit(e)

    # Example Usage
    reply_to_posts("test", limit=5)  # Reply to posts in subreddit 'test'
    send_direct_message("recipient_username", "Hello!", "This is an automated message.")  # Send a message
    like_post("post_id_here")  # Like a specific post
    post_to_subreddit("test", "Automated Post Title", "This is an automated post content.")  # Submit a post

except Exception as e:
    logging.error(f"Critical error: {e}")
