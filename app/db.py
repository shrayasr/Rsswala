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

    feed_id = -1
    if c.rowcount > 0:
        feed_id = c.fetchone()[0]

    return feed_id

def get_user_id(mail):
    c = db.cursor()
    c.execute("SELECT id FROM users WHERE mail = %s",(mail,))

    uid = -1
    if c.rowcount > 0:
        uid = c.fetchone()[0]

    return uid

def create_new_user(mail):
    c = db.cursor()
    c.execute("INSERT INTO users(mail) VALUES(%s)",(mail,))

    db.commit()

    return c.lastrowid

def add_user_to_feed(uid,feed_id):
    c = db.cursor()
    c.execute("INSERT INTO user_feeds(user_id,feed_id) VALUES(%s,%s)",(uid,feed_id))

    db.commit()

    return c.lastrowid

def delete_read_item(uid,item_id):
    c = db.cursor()
    c.execute("DELETE FROM user_read_items WHERE user_id = %s AND item_id = %s",(uid,item_id))

    db.commit()

    return 1 # TODO return false also

def add_read_item(uid,item_id):
    c = db.cursor()
    c.execute("INSERT INTO user_read_items(user_id,item_id) VALUES(%s,%s)",(uid,item_id))

    db.commit()

    return c.lastrowid # TODO return false also

