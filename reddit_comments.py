import praw
import csv
import re

def redditAuthenticate():
    #Authentication
    clientId = ""
    clientSecret = ""
    password = ''
    username = ''
    reddit = praw.Reddit(
        client_id=clientId,
        client_secret=clientSecret,
        password=password,
        user_agent='',
        username=username
    )
    return reddit


def main():
    dest_handle = csv.writer(open('.../dest.csv', 'w'))
    dest_handle.writerow(['News Article', 'Comments'])
    redditHandle = redditAuthenticate()
    submission_id = []
    for submission in redditHandle.subreddit('news').stream.submissions():
        dest_handle.writerow([submission.title])
        submission.comments.replace_more(limit = 0)
        
        for top_level_comment in submission.comments:
            print (top_level_comment.body)
            dest_handle.writerow(['', top_level_comment.body])        


if __name__ == '__main__':
    main()
