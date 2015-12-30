Configure Twitterwatch
======================

As a prerequisite to use Twitterwatch, you need a Twitter app. Log in Twitter, go to https://apps.twitter.com, create an app and generate the access token.

In order to configure Twitterwatch, you need to create a twitterwatch.ini file (or any name you prefer, finishing with the extension .ini) with the following parameters::

    [twitter]
    screen_name_of_the_user_to_watch=journalduhacker
    consumer_key=ml9jaiBnf3pmU9uIrKNIxAr3v
    consumer_secret=8Cmljklzerkhfer4hlj3ljl2hfvc123rezrfsdctpokaelzerp
    access_token=213416590-jgJnrJG5gz132nzerl5zerwi0ahmnwkfJFN9nr3j
    access_token_secret=3janlPMqDKlunJ4Hnr90k2bnfk3jfnwkFjeriFZERj32Z

    [schedule]
    check_interval=60

For the [twitter] section:

- screen_name_of_the_user_to_watch: the screen_name of the user to watch (in @carl_chenet, it's carl_chenet)
- consumer_key: the Twitter consumer key (see your apps.twitter.com webpage)
- consumer_secret: the Twitter consumer secret key (see your apps.twitter.com webpage)
- access_token: the Twitter access token key (see your apps.twitter.com webpage)
- access_token_secret: the Twitter access token secret key (see your apps.twitter.com webpage)
