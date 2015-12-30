### Twitterwatch 

Twitterwatch watches a user timeline in order to check if tweets are tweeted on a regular schedule.

### Quick Install

* Install Twitterwatch from PyPI

        # pip3 install twitterwatch

* Install Twitterwatch from sources    
  *(see the installation guide for full details)
  [Installation Guide](http://twitterwatch.readthedocs.org/en/latest/install.html)*
  

        # tar zxvf twitterwatch-0.1.tar.gz
        # cd twitterwatch
        # python3.4 setup.py install
        # # or
        # python3.4 setup.py install --install-scripts=/usr/bin

### Use Twitterwatch

* Create or modify twitterwatch.ini file in order to configure Twitterwatch:

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

* Launch Twitterwatch

        $ twitterwatch /path/to/twitterwatch.ini

### Authors

Carl Chenet <chaica@ohmytux.com>

### License

This software comes under the terms of the GPLv3+. See the LICENSE file for the complete text of the license.
