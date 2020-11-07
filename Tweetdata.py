
def extractdata(user_scname,tweets):
    user= api.get_user(user_scname)
    print("### USER DETAILS####")
    print("User Name: "+ user.name)
    print("User Screen Name: "+ user.screen_name)
    print("User Description: "+user.description)
    print("##############################")
    data = api.user_timeline(user.id)
    tweets_for_csv=[tweet.text for tweet in data]
    for i in tweets_for_csv:
        tweets.append(i)    