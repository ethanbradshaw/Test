from urllib.request import urlopen
import tweepy
from bs4 import BeautifulSoup

# Authenticate to Twitter
auth = tweepy.OAuthHandler("", "")
auth.set_access_token("", "")

# Create API object
api = tweepy.API(auth, wait_on_rate_limit=True,
    wait_on_rate_limit_notify=True)


#Gets RSS Feed and sorts
def update(xml_update_url):
    parse_xml_update_url = urlopen(xml_update_url)
    xml_page = parse_xml_update_url.read()
    parse_xml_update_url.close()

    soup_page = BeautifulSoup(xml_page, "xml")
    update_list = soup_page.findAll("item")
    for getfeed in update_list:
        print("\n")
        print(getfeed.title.text)
        print(getfeed.link.text)
        print(getfeed.pubDate.text)


UPDATE_URL = "https://blog.counter-strike.net/index.php/category/updates/feed/"
update(UPDATE_URL)

#Grabs newest update and tweets
