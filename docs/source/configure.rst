Configure Twitterwatch
======================

As a prerequisite to use Twitterwatch, you need a Twitter app. Log in Twitter, go to https://apps.twitter.com, create an app and generate the access token.

In order to configure Twitterwatch, you need to create a twitterwatch.ini file (or any name you prefer, finishing with the extension .ini) with the following parameters::

    [twitter]
    consumer_key=ml9jaiBnf3pmU9uIrKNIxAr3v
    consumer_secret=8Cmljklzerkhfer4hlj3ljl2hfvc123rezrfsdctpokaelzerp
    access_token=213416590-jgJnrJG5gz132nzerl5zerwi0ahmnwkfJFN9nr3j
    access_token_secret=3janlPMqDKlunJ4Hnr90k2bnfk3jfnwkFjeriFZERj32Z

    [schedule]
    check_interval=60

    [mail]
    host=localhost
    from=admin@myserver.org
    to=foo@mylaptop.org

For the [twitter] section:

- consumer_key: the Twitter consumer key (see your apps.twitter.com webpage)
- consumer_secret: the Twitter consumer secret key (see your apps.twitter.com webpage)
- access_token: the Twitter access token key (see your apps.twitter.com webpage)
- access_token_secret: the Twitter access token secret key (see your apps.twitter.com webpage)

For the [mail] section:

- host: the name of the mail server to connect with SMTP
- from: mail address sending the email alerts
- to: mail address of the recipient of the email alerts
