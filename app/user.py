import db
from fetch import Fetch

class User():

    def __init__(self,mail="foo@bar.com"):
        self.uid = db.get_user_id(mail)

        if self.uid < 0 :
            self.uid = db.create_new_user(mail)

    def subscribe_to_feed(self,feed_url):
        feed_id = db.get_feed_id(feed_url) 

        if feed_id < 0 :
            feed_fetch = Fetch(feed_url)
            feed_id = db.create_new_feed(feed_fetch.get_feed_details())
            db.add_new_item(feed_fetch.get_entries())

        user_feed_id = db.add_user_to_feed(self.uid,feed_id)

        return user_feed_id

    def refresh_all_items(self):

        items = db.get_all_feed_user_items(self.uid)
        return items

    def refresh_feed_items(self,feedid):

        items = db.get_one_feed_user_items(self.uid,feedid)
        return items

    def mark_item(self,item_id,read=True):

        return_id = -1

        if read == True : 
            return_id = db.add_read_item(self.uid,item_id)
        else:
            return_id = db.delete_read_item(self.uid,item_id)

        return return_id

