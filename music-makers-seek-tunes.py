# https://stackoverflow.com/a/55804977

import tweepy

user_name = "@ThatKevinSmith"
tweet_id = "1461361593564811278"

replies = tweepy.Cursor(
    api.search, q="to:{}".format(user_name), since_id=tweet_id, tweet_mode="extended"
).items()
while True:
    try:
        reply = replies.next()
        if not hasattr(reply, "in_reply_to_status_id_str"):
            continue
        if reply.in_reply_to_status_id == tweet_id:
            logging.info("reply of tweet:{}".format(reply.full_text))

    except tweepy.RateLimitError as e:
        logging.error("Twitter api rate limit reached".format(e))
        time.sleep(60)
        continue

    except tweepy.TweepError as e:
        logging.error("Tweepy error occured:{}".format(e))
        break

    except StopIteration:
        break

    except Exception as e:
        logger.error("Failed while fetching replies {}".format(e))
        break