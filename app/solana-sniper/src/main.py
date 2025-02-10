import logging
from src.twitter_monitor import TwitterMonitor
from src.snipe_mechanism import SnipeMechanism

def process_tweet(tweet_text):
    try:
        sniper = SnipeMechanism()
        sniper.execute_buy_order(tweet_text)
    except Exception as e:
        logging.error(f"Failed to process tweet: {e}")

if __name__ == "__main__":
    try:
        accounts = ["123456789"]  # Replace with actual Twitter account IDs
        monitor = TwitterMonitor()
        monitor.start_monitoring(accounts, process_tweet)
    except Exception as e:
        logging.error(f"Application failed: {e}")