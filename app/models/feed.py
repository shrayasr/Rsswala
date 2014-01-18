from app import app
from app.utils.commons import Commons

class Feed():

    def __init__(self, feed_url, title=None, description=None, link=None, uid=None):
        self.uid = uid
        self.feed_url = feed_url
        self.title = title 
        self.description = description
        self.link = link

    def __str__(self):
        return {
                "id":self.uid,
                "feed_url":self.feed_url,
                "title":self.title,
                "description":self.description,
                "link":self.link
                }

