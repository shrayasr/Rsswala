import os
from nose import with_setup

from app.utils.opml import OpmlParser

def setup_blank_xml():
    xml = """<?xml version="1.0" encoding="UTF-8" ?>
             <opml version="1.0"></opml>"""

    with open("test.xml","w") as f:
        f.write(xml)

def setup_good_xml_no_nest():
    xml = """<?xml version="1.0" encoding="UTF-8" ?>
             <opml version="1.0">
             <body>
             <outline text="Hack Education" title="Hack Education" type="rss" xmlUrl="http://feeds.feedburner.com/HackEducation" htmlUrl="http://www.hackeducation.com/" />
             <outline text="Hacker News" title="Hacker News" type="rss" xmlUrl="http://news.ycombinator.com/rss" htmlUrl="https://news.ycombinator.com/" />
             <outline text="HackerStreet.India" title="HackerStreet.India" type="rss" xmlUrl="http://hackerstreet.in/rss" htmlUrl="http://hackerstreet.in/" />
             <outline text="John Resig" title="John Resig" type="rss" xmlUrl="http://feeds.feedburner.com/JohnResig" htmlUrl="http://ejohn.org" />
             <outline text="Lonely Proton" title="Lonely Proton" type="rss" xmlUrl="http://lonelyproton.com/feed/" htmlUrl="http://lonelyproton.com" />
             </body></opml>"""

    with open("test.xml","w") as f:
        f.write(xml)

def setup_good_xml_nest():
    xml = """<?xml version="1.0" encoding="UTF-8" ?>
             <opml version="1.0">
             <body>
             <outline text="Hack Education" title="Hack Education" type="rss" xmlUrl="http://feeds.feedburner.com/HackEducation" htmlUrl="http://www.hackeducation.com/" />
             <outline text="Hacker News" title="Hacker News" type="rss" xmlUrl="http://news.ycombinator.com/rss" htmlUrl="https://news.ycombinator.com/" />
             <outline text="HackerStreet.India" title="HackerStreet.India" type="rss" xmlUrl="http://hackerstreet.in/rss" htmlUrl="http://hackerstreet.in/" />
             <outline text="John Resig" title="John Resig" type="rss" xmlUrl="http://feeds.feedburner.com/JohnResig" htmlUrl="http://ejohn.org" />
             <outline text="Lonely Proton" title="Lonely Proton" type="rss" xmlUrl="http://lonelyproton.com/feed/" htmlUrl="http://lonelyproton.com" />
             <outline title="blogger-following" text="blogger-following">
             <outline text="BAC Club Diary" title="BAC Club Diary" type="rss" xmlUrl="http://b-a-c-clubdiary.blogspot.com/feeds/posts/default" htmlUrl="http://b-a-c-clubdiary.blogspot.com/" />
             <outline text="Back to the Basics" title="Back to the Basics" type="rss" xmlUrl="http://blogofvk.blogspot.com/feeds/posts/default" htmlUrl="http://blogofvk.blogspot.com/" />
             </outline>
             </body></opml>"""

    with open("test.xml","w") as f:
        f.write(xml)

def teardown_xml():
    os.remove("test.xml")


def test_opml_no_xml():

    try:
        opml = OpmlParser()
    except KeyError:
        assert True
    except Exception:
        assert False

@with_setup(setup_blank_xml, teardown_xml)
def test_opml_blank_xml():

    try:
        opml = OpmlParser("test.xml")
        feed_urls = opml.parse()

    except Exception as e:
        if e.message.upper() == "MALFORMED XML":
            assert True
        else:
            assert False

@with_setup(setup_good_xml_no_nest, teardown_xml)
def test_opml_good_xml_no_nest():
    
    try:
        opml = OpmlParser("test.xml")
        feed_urls = opml.parse()

        if len(feed_urls) == 5:
            assert True
        else:
            assert False

    except Exception as e:
        print e
        assert False

@with_setup(setup_good_xml_nest, teardown_xml)
def test_opml_good_xml_nest():
    
    try:
        opml = OpmlParser("test.xml")
        feed_urls = opml.parse()

        if len(feed_urls) == 7:
            assert True
        else:
            assert False

    except Exception as e:
        print e
        assert False
