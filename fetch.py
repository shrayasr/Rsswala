import feedparser

class Fetch():

    # Initialze the Fetch class with the feed url
    #   additionally, parse out the URL and get a parsed feed
    def __init__(self,feedURL):
        self.feedURL = feedURL
        self.parsedFeed = feedparser.parse(feedURL)

    # Return information about the feed itself
    def getFeedDetails(self):
        
        thisFeed = self.parsedFeed['feed']

        # Declare an object
        obj = {}

        # If the required keys exist, add them
        #   else, throw out a blank

        obj['feed_url'] = self.feedURL

        if thisFeed.has_key('title'):
            obj['title'] = thisFeed['title']
        else:
            obj['title'] = ""

        if thisFeed.has_key('subtitle'):
            obj['description'] = thisFeed['subtitle']
        else:
            obj['description'] = ""

        if thisFeed.has_key('link'):
            obj['link'] = thisFeed['link']
        else:
            obj['link'] = ""

        # Return the object
        return obj


    # Return a list of dictionaries of the entries in the feed
    def getEntries(self):

        # declare an empty entities list
        entries = []

        # go through the list of entities present in the feed
        for entry in self.parsedFeed['entries']:

            # Declare an empty object
            obj = {}

            # If the keys exist, drop them in to the object
            #   Else, throw out a blank string
            if entry.has_key('title'):
                obj['title'] = entry['title']
            else:
                obj['title'] = ""

            if entry.has_key('description'):
                obj['description'] = entry['description']
            else:
                obj['description'] = ""

            if entry.has_key('link'):
                obj['link'] = entry['link']
            else:
                obj['link'] = ""

            if entry.has_key('published'):
                obj['pubdate'] = entry['published']
            else:
                obj['pubdate'] = ""

            if entry.has_key('guid'):
                obj['guid'] = entry['guid']
            else:
                obj['guid'] = ""

            # append the created object to the list of entries
            entries.append(obj)

        # return the entries
        return entries
