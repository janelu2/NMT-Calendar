from bs4 import BeautifulSoup
import requests
from NMTevent import NMTevent


def create_soup(url):
    """Returns a BeautifulSoup obj for any given url"""
    page = requests.get(url)
    html = page.content
    soup = BeautifulSoup(html, "lxml")
    return soup


def find_date(event_link):
    """This function finds the date +  time of an event given the link to
    the calendar event. This is done because there are no dates on the calendar"""
    temp_soup = create_soup(event_link)
    div = temp_soup.find('div', attrs={'class': 'jcl_event_right jcl_right'}).find_all('div')[0]
    date_info = str(div.text).split(' ', 1)[1]
    return date_info

# this is a temporary way to loop and create a bunch of event objects stored in an array
events = []
calendar_soup = create_soup('http://www.nmt.edu/nmt-calendar')
for row in calendar_soup.find_all('div', attrs={"class": "eventmiddle"}):
    event_link = "http://www.nmt.edu" + str(row.a['href'])
    new_event = NMTevent(row, event_link, find_date(event_link))
    events.append(new_event)
    new_event.pretty()

# pls ignore this, simply something to remember:
# for a in soup.findAll('a', title=True):
#    print "Found this: ", a['title']