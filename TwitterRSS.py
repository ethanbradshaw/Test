from urllib.request import urlopen
import tweepy
from bs4 import BeautifulSoup

# Authenticate to Twitter
auth = tweepy.OAuthHandler("yHCc1LLldhFpcgvud540l4hxO", "CI0ptQy9ojtLDcNyJASEmffJRNow1yq1pE1EfPYvDIffTMSciN")
auth.set_access_token("711010595022217217-dhprBd3iJRxgGLj0LCrmBEMxuo20hKV", "niHzcU6OtXStxehLgIMhydvnVGnuffKZ6H9NrmLjU1EAS")

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
api.update_status(update(UPDATE_URL))
#Updates the RSS link


#Grabs newest update and tweets