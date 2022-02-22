# Podcast Saver

## How to
Install requirements.txt 

```
pip install -r requirements.txt
```

Set a cronjob to let the script run in specific periods, e.g. every 10 days.

```
crontab -e
```

```
0 0 */30 * * /usr/bin/python <path-to-script>/podcast.py
```

## Set the main link
In podcast.py set the main page link for the page to scrape and change if needed