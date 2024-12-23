class SocialMediaAccount:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def login(self):
        print(f"{self.username} logged in.")

    def post(self):
        print(f"{self.username} posted something.")

class InstagramAccount(SocialMediaAccount):
    def __init__(self, username, password, number_of_followers):
        super().__init__(username, password)
        self.number_of_followers = number_of_followers

    def share_story(self):
        print(f"{self.username} shared a story.")

class TwitterAccount(SocialMediaAccount):
    def __init__(self, username, password, number_of_tweets):
        super().__init__(username, password)
        self.number_of_tweets = number_of_tweets

    def tweet(self):
        print(f"{self.username} tweeted something.")

instagram_account = InstagramAccount("user123", "password123", 1500)
twitter_account = TwitterAccount("user456", "password456", 500)

instagram_account.login()
instagram_account.share_story()
twitter_account.login()
twitter_account.tweet()




