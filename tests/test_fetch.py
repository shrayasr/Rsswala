from app.utils.fetch import Fetch

def test_01_fetch_blank_feed():
    feed_url = ""
    feed_id = -1

    try:
        fetch = Fetch(feed_url)
        fetch.get_feed_details()
        fetch.get_entries(feed_id)
    except KeyError:
        assert True
    except Exception:
        assert False

def test_02_fetch_no_feed():
    feed_id = -1

    try:
        fetch = Fetch()
        fetch.get_feed_details()
        fetch.get_entries(feed_id)
    except KeyError:
        assert True
    except Exception:
        assert False

def test_03_fetch_bad_url():
    feed_id = -1
    feed_url = "www.shrayas.com"

    try:
        fetch = Fetch(feed_url)
        fetch.get_feed_details()
        fetch.get_entries(feed_id)
    except KeyError:
        assert True
    except Exception:
        assert False

def test_04_fetch_good_url():
    feed_id = -1
    feed_url = "http://techcrunch.com/feed/"

    fetch = Fetch(feed_url)
    feed_details = fetch.get_feed_details()
    feed_items = fetch.get_entries(feed_id)

    if feed_details and feed_items:
        assert True
    else:
        assert False
