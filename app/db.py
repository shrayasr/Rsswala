import conf
import MySQLdb

db = MySQLdb.connect(user=conf.MYSQL_USER,passwd=conf.MYSQL_PASS,db=conf.MYSQL_DB,charset='utf8')

# insert a new feed data
def create_new_feed(data):
    c = db.cursor()

    c.execute("""INSERT INTO 
        feeds(feed_url,title,description,link)
        VALUES(%s,%s,%s,%s)""",
        (
          data['feed_url']
          ,data['title']
          ,data['description']
          ,data['link']
        )
        )

    db.commit()

    return c.lastrowid

# add new items for a feed
def add_new_item(items):
    c = db.cursor()

    print items[0]['pubdate']

    c.executemany("""INSERT INTO 
        items(feed_id,title,description,link,guid,pubdate)
        VALUES(%s,%s,%s,%s,%s,%s)""",
        [(
          item['feed_id']
          ,item['title']
          ,item['description']
          ,item['link']
          ,item['guid']
          ,item['pubdate']
         ) for item in items])

    db.commit()

# get the feed_id of an existing feed_id
def get_feed_id(feed_url):
    c = db.cursor()
    c.execute("SELECT id FROM feeds WHERE feed_url = %s",(feed_url,))

    return c.fetchone()[0]
