from app import app
from app.utils.commons import Commons

class Item():

    def __init__(self, feed_id, title=None, description=None, link=None, 
                 guid=None, guid_hash=None, pubdate=None, uid=None):
        self.uid = uid
        self.feed_id = feed_id
        self.title = title 
        self.description = description
        self.link = link
        self.guid = guid
        self.guid_hash = guid_hash
        self.pubdate = pubdate

    def __str__(self):
        return {
                "id":self.uid,
                "feed_id":self.feed_id,
                "title":self.title,
                "description":self.description,
                "link":self.link,
                "guid":self.guid,
                "pubdate":self.pubdate
                }

