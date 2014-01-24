import feedparser
import hashlib
from time import strftime

from app.models.feed import Feed
from app.models.item import Item


class Fetch():

    # Initialze the Fetch class with the feed url
    def __init__(self, feed_url=None):

        # If you are trying to be a smartass,
        # throw an exception
        if feed_url == None or len(feed_url.strip()) == 0:
            raise KeyError('Please supply a feedURL')

        # Some defaults
        self.feed_url = feed_url
        self.feed = None
        self.items = []

        # Perform a parse.
        self.parsed_feed = feedparser.parse(self.feed_url)

        # Check the parse and throw error if necessary
        if self.parsed_feed['bozo'] == 1:
            raise KeyError('Bad URL')

    # Return information about the feed itself
    def get_feed_details(self):

        thisFeed = self.parsed_feed['feed']

        self.feed = Feed(self.feed_url)

        if thisFeed.has_key('title'):
            self.feed.title = thisFeed['title']

        if thisFeed.has_key('subtitle'):
            self.feed.description = thisFeed['subtitle']

        if thisFeed.has_key('link'):
            self.feed.link = thisFeed['link']

        return self.feed


    # Return a list of dictionaries of the entries in the feed
    def get_entries(self, feed_id):

        # Store the feed_id
        self.feed_id = feed_id

        # go through the list of entities present in the feed
        for entry in self.parsed_feed['entries']:

            # Create an item object
            item = Item(self.feed_id)

            # If the keys exist, drop them in to the object
            if entry.has_key('title'):
                item.title = entry['title']

            if entry.has_key('description'):
                item.description = entry['description']

            if entry.has_key('link'):
                item.link = entry['link']

            if entry.has_key('published'):
                # convert the datetime to mysql format
                pub_datetime = entry['published_parsed']
                item.pubdate = strftime('%Y-%m-%d %H:%M:%S',pub_datetime)

            # guid is a part of the newer rss specification,
            # it doesn't exists we'll just use a link
            if entry.has_key('guid'):
                item.guid = entry['guid']
            else:
                item.guid = item.link

            # the hash of the guid is used to check for duplicates
            item.guid_hash = hashlib.md5(item.guid).hexdigest()

            # append the created object to the list of entries
            self.items.append(item)

        return self.items

