import conf
import MySQLdb
import datetime

db = MySQLdb.connect(user=conf.MYSQL_USER,passwd=conf.MYSQL_PASS,
        db=conf.MYSQL_DB,charset='utf8')

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

    c.executemany("""INSERT IGNORE INTO 
        items(feed_id,title,description,link,guid,guid_hash,pubdate)
        VALUES(%s,%s,%s,%s,%s,%s,%s)""",
        [(
            item['feed_id']
            ,item['title']
            ,item['description']
            ,item['link']
            ,item['guid']
            ,item['guid_hash']
            ,item['pubdate']
            ) for item in items])

    db.commit()

# feed: get the id of an existing url
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

def get_one_feed_user_items(uid,feedid):
    c = db.cursor()
    c.execute("""SELECT * from items where feed_id = %s and id not in 
            (select item_id from user_read_items where user_id = %s)""",
            (feedid,uid,))

    items = []
    if c.rowcount > 0:
        while True:
            row = c.fetchone()
            if row == None:
                break

            item = {
                    "item_id":row[0],
                    "feed_id":row[1],
                    "title":row[2],
                    "desc":row[3],
                    "link":row[4],
                    "guid":row[5],
                    "pubdate":str(row[6])
                    }

            items.append(item)

    return items

def get_all_feed_user_items(uid):
    c = db.cursor()
    c.execute("""SELECT 
            i.id AS id, i.title AS title, i.link AS link, f.title AS feed_title, f.id AS feed_id
            FROM items i 
            JOIN feeds f 
            ON f.id = i.feed_id 
            JOIN user_feeds uf 
            ON uf.feed_id = f.id 
            LEFT OUTER JOIN user_read_items uri 
            ON uri.item_id = i.id 
            WHERE uf.user_id = %s 
            AND uri.item_id is NULL
            ORDER BY i.feed_id,i.pubdate DESC
            """,(uid,))

    items = []
    prev_feed = -1
    if c.rowcount > 0:
        while True:
            row = c.fetchone()
            if row == None:
                break

            feed_id = row[4]
            item_data = {                    
                    "item_id":row[0],
                    "title":row[1],
                    "link":row[2]
                    }
            
            if prev_feed != row[4]:
                feed_data = {
                        "title": row[3],
                        "item_data": [item_data]
                        }
                items.append(feed_data)
                prev_feed = row[4]
            else:
                items[-1]["item_data"].append(item_data)

    return items

def get_feed_list(uid):
    c = db.cursor()
    c.execute("""select * from feeds as f inner join user_feeds as uf on f.id =
            uf.feed_id where uf.`user_id` = %s""",(uid,))

    feeds = []
    if c.rowcount > 0:
        while True:
            row = c.fetchone()
            if row == None:
               break

            feed = {
                    "feed_id"   :row[0],
                    "feed_url"  :row[1],
                    "title"     :row[2],
                    "desc"      :row[3],
                    "link"      :row[4]
                    }

            feeds.append(feed)

    return feeds


def create_new_user(mail):
    c = db.cursor()
    c.execute("INSERT INTO users(mail) VALUES(%s)",(mail,))

    db.commit()

    return c.lastrowid

def add_user_to_feed(uid,feed_id):
    c = db.cursor()
# insert ignores if user is already part of a feed
    c.execute("INSERT IGNORE INTO user_feeds(user_id,feed_id) VALUES(%s,%s)",
            (uid,feed_id))

    db.commit()

    return c.lastrowid

def delete_read_item(uid,item_id):
    c = db.cursor()
    c.execute("DELETE FROM user_read_items WHERE user_id = %s AND item_id = %s",
            (uid,item_id))

    db.commit()

    return 1 # TODO return false also

def add_read_item(uid,item_id):
    c = db.cursor()
    c.execute("INSERT INTO user_read_items(user_id,item_id) VALUES(%s,%s)",
            (uid,item_id))

    db.commit()

    return c.lastrowid # TODO return false also

