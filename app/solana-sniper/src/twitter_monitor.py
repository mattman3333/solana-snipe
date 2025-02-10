import tweepy
import logging
import os
import time
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('logs/app.log'),
        logging.StreamHandler()
    ]
)

class TwitterMonitor:
    def __init__(self):
        self.auth = self._authenticate()
        self.api = tweepy.API(self.auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
        self.stream = None

    def _authenticate(self):
        """Authenticate with Twitter API."""
        try:
            auth = tweepy.OAuth1UserHandler(
                os.getenv("TWITTER_API_KEY"),
                os.getenv("TWITTER_API_SECRET_KEY"),
                os.getenv("TWITTER_ACCESS_TOKEN"),
                os.getenv("TWITTER_ACCESS_TOKEN_SECRET"),
            )
            return auth
        except Exception as e:
            logging.error(f"Authentication failed: {e}")
            raise

    def start_monitoring(self, accounts, callback):
        """Start monitoring specified Twitter accounts."""
        try:
            listener = TwitterStreamListener(callback)
            self.stream = tweepy.Stream(auth=self.api.auth, listener=listener)
            self.stream.filter(follow=[str(account) for account in accounts])
        except Exception as e:
            logging.error(f"Failed to start monitoring: {e}")
            raise

class TwitterStreamListener(tweepy.Stream):
    def __init__(self, callback):
        super().__init__()
        self.callback = callback

    def on_status(self, status):
        """Called when a new tweet is posted."""
        try:
            self.callback(status.text)
        except Exception as e:
            logging.error(f"Failed to process tweet: {e}")
            raise