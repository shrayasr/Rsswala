from app.utils.fetch import Fetch

def test_fetch_blank_feed():
    feed_url = ""
    feed_id = -1

    try:
        fetch = Fetch(feed_id,feed_url)
    except KeyError:
        assert True
    except Exception:
        assert False

def test_fetch_no_feed():
    feed_id = -1

    try:
        fetch = Fetch(feed_id)
    except KeyError:
        assert True
    except Exception:
        assert False

def test_fetch_bad_url():
    feed_id = -1
    feed_url = "www.shrayas.com"

    try:
        fetch = Fetch(feed_id,feed_url)
    except KeyError:
        assert True
    except Exception:
        assert False

def test_fetch_good_url():
    feed_id = -1
    feed_url = "http://techcrunch.com/feed/"

    fetch = Fetch(feed_id,feed_url)

    if fetch.feed and fetch.items:
        assert True
    else:
        assert False
