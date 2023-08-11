import requests
import json
import praw


# The `RedditAPI` class provides methods to interact with the Reddit API, including retrieving hot
# posts from a subreddit and getting the top comments for a post.
class RedditAPI:
    def __init__(self, token, client_id, username, password):
        """
        The above function initializes a Reddit API client by obtaining an access token and setting up the
        necessary headers for authentication.

        :param token: The `token` parameter is the access token that is used for authentication when making
        requests to the Reddit API. It is obtained by making a POST request to the Reddit API's access token
        endpoint with the client ID and client secret as the basic authentication credentials, and the
        username and password as the request data
        :param client_id: The `client_id` parameter is a unique identifier for your application. It is
        obtained when you register your application with the Reddit API. You can get the `client_id` by
        creating a new application on the Reddit developer website
        :param username: The `username` parameter is the username of the Reddit account that you want to
        authenticate with
        :param password: The `password` parameter is the password for the Reddit account that you want to
        authenticate with
        """
        auth = requests.auth.HTTPBasicAuth(client_id, token)
        data = {'grant_type': 'password',
                'username': username,
                'password': password}

        headers = {'User-Agent': 'MyBot/0.0.1'}

        res = requests.post('https://www.reddit.com/api/v1/access_token',
                            auth=auth, data=data, headers=headers)

        TOKEN = res.json()['access_token']
        self.headers = {**headers, **{'Authorization': f"bearer {TOKEN}"}}

        # while the token is valid (~2 hours) we just add headers=headers to our requests
        requests.get('https://oauth.reddit.com/api/v1/me', headers=headers)

        self.reddit = praw.Reddit(
            client_id=client_id,
            client_secret=token,
            password=password,
            user_agent="testing",
            username=username,
        )

    def get_headers(self, subreddit) -> None:
        """
        The function `get_headers` sends a GET request to a specified subreddit and saves the response as a
        JSON file.

        :param subreddit: The `subreddit` parameter is the URL of the subreddit you want to make a request
        to. It should be a string representing the subreddit's URL
        """
        res = requests.get(subreddit,
                           headers=self.headers)

        with open("temp.json", "w") as outfile:
            json_obj = json.dumps(res.json(), indent=2)
            outfile.write(json_obj)

    def get_hot_posts(self, subreddit, limit):
        """
        The function `get_hot_posts` retrieves a specified number of hot posts from a given subreddit using
        the Reddit API.

        :param subreddit: The subreddit parameter is the name of the subreddit from which you want to
        retrieve the hot posts. For example, if you want to get the hot posts from the "python" subreddit,
        you would pass "python" as the value for the subreddit parameter
        :param limit: The `limit` parameter specifies the maximum number of hot posts to retrieve from the
        subreddit
        :return: an array of hot posts from the specified subreddit, limited to the specified limit.
        """
        sub = self.reddit.subreddit(subreddit)
        hot_posts = sub.hot(limit=limit)
        hot_posts_arr = [post for post in hot_posts]
        return hot_posts_arr

    def get_post_top_comments(self, post, limit):
        """
        The function `get_post_top_comments` retrieves the top comments for a given post on Reddit, up to a
        specified limit.

        :param post: The "post" parameter is an object representing a post on Reddit. It likely contains
        information such as the post's ID, title, content, author, etc
        :param limit: The "limit" parameter specifies the maximum number of top comments that should be
        returned
        :return: an array of the top comments for a given post, with the number of comments limited by the
        "limit" parameter.
        """
        submission = self.reddit.submission(post.id)
        submission.comments.replace_more(limit=50)
        comments = submission.comments.list()
        top_comments = sorted(
            comments, key=lambda comment: comment.score, reverse=True)[:limit]
        top_comments_arr = [comment for comment in top_comments]
        return top_comments_arr


if __name__ == "__main__":
    from secrets import REDDIT_API_TOKEN, REDDIT_API_CLIENT_ID, REDDIT_USERNAME, REDDIT_PASSWORD
    print("Executing Reddit_api_interactor.py")
    reddit_api = RedditAPI(
        REDDIT_API_TOKEN, REDDIT_API_CLIENT_ID, REDDIT_USERNAME, REDDIT_PASSWORD)
