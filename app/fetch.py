import feedparser
import db

class Fetch():

    # Initialze the Fetch class with the feed url
    #   additionally, parse out the URL and get a parsed feed
    def __init__(self,feedURL):
        self.feedURL = feedURL
        self.parsedFeed = feedparser.parse(feedURL)

    # Return information about the feed itself
    def get_feed_details(self):
        
        thisFeed = self.parsedFeed['feed']

        # Declare an object
        obj = {}

        # If the required keys exist, add them

        obj['feed_url'] = self.feedURL

        obj['title'] 
        = obj['description'] 
        = obj['link'] 
        = ""

        if thisFeed.has_key('title'):
            obj['title'] = thisFeed['title']

        if thisFeed.has_key('subtitle'):
            obj['description'] = thisFeed['subtitle']

        if thisFeed.has_key('link'):
            obj['link'] = thisFeed['link']

        # Return the object
        return obj


    # Return a list of dictionaries of the entries in the feed
    def get_entries(self):

        # declare an empty entities list
        entries = []

        feed_id = db.get_feed_id(self.feedURL)

        # go through the list of entities present in the feed
        for entry in self.parsedFeed['entries']:

            # Declare an empty object
            obj = {}

            obj['feed_id'] = feed_id

            obj['title'] 
            = obj['description'] 
            = obj['link'] 
            = obj['guid'] 
            = obj['pubdate'] 
            = ""

            # If the keys exist, drop them in to the object
            if entry.has_key('title'):
                obj['title'] = entry['title']

            if entry.has_key('description'):
                obj['description'] = entry['description']

            if entry.has_key('link'):
                obj['link'] = entry['link']

            if entry.has_key('published'):
                obj['pubdate'] = entry['published']

            if entry.has_key('guid'):
                obj['guid'] = entry['guid']

            # append the created object to the list of entries
            entries.append(obj)

        # return the entries
        return entries
