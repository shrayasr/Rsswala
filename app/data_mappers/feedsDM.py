import MySQLdb

from instance import conf as config
from app import app
from app.model.feed import Feed
from app.model.item import Item
from app.utils.fetch import Fetch
from app.utils.commons import Commons

class UserDM():

    def __init__(self):

        self.db = MySQLdb.connect(user=config.MYSQL_USER,
                                  passwd=config.MYSQL_PASS, db=config.MYSQL_DB,
                                  charset='utf8')

    def get_feed_id(self, feed_url):

        c = self.db.cursor()
        feed_id = None

        try:
            c.execute("SELECT id FROM feeds WHERE feed_url = %s",(feed_url,))

            feed_id = -1
            if c.rowcount > 0:
                feed_id = c.fetchone()[0]

            return feed_id

        except Exception as e:
            print "Error while getting feed_id"
            print e

        finally: 
            c.close()
            return feed_id

    def subscribe(self, user_id, feed_url):

        feed_id = None

        try:
            feed_id = self.get_feed_id(feed_url)

            if feed_id < 0:
                fetch_engine = Fetch(feed_url)
                feed_data = feed_engine.get_feed_details()
                feed_id = self.create_new_feed(feed_data)
                feed_entries = feed_engine.get_entries(feed_id)
                self.populate_items(feed_entries)
                self.add_user_to_feed(user_id, feed_id)

        except Exception as e:
            print "Error while subscribing user to feed"
            print e

        finally:
            return feed_id

    def populate_items(self, feed_entries):

        c = self.db.cursor()
        items_added = len(feed_entries)

        try:
            c.executemany("""INSERT IGNORE INTO 
                items(feed_id,title,description,link,guid,guid_hash,pubdate)
                VALUES(%s,%s,%s,%s,%s,%s,%s)""",
                [(
                     feed_entry['feed_id']
                    ,feed_entry['title']
                    ,feed_entry['description']
                    ,feed_entry['link']
                    ,feed_entry['guid']
                    ,feed_entry['guid_hash']
                    ,feed_entry['pubdate']
                    ) for feed_entry in feed_entries])

            self.db.commit()

        except Exception as e:
            print "Error while adding items to feed"
            print e
            items_added = None

        finally:
            c.close()
            return items_added


    def create_new_feed(self, feed_data):

        c = self.db.cursor()
        feed_id = -1

        try:
            c.execute("""INSERT INTO 
                feeds(feed_url,title,description,link)
                VALUES(%s,%s,%s,%s)""",
                (
                     feed_data['feed_url']
                    ,feed_data['title']
                    ,feed_data['description']
                    ,feed_data['link']
                    )
                )

            self.db.commit()
            feed_id = c.lastrowid

        except Exception as e:
            print "Error when creating a new feed"
            print e

        finally:
            c.close()
            return feed_id
