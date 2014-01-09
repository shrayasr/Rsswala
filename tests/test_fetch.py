from app.fetch import Fetch

def test_create_fetch_obj_empty_args():
    try:
        f = Fetch()
    except KeyError:
        assert True
    except Exception:
        assert False

def test_create_fetch_obj_blank_url():
    try:
        f = Fetch('')
    except KeyError:
        assert True
    except Exception:
        assert False

def test_create_fetch_obj_good_url():
    try:
        GOOD_URL='http://techcrunch.com/feed/'
        f = Fetch(GOOD_URL)
        obj = f.get_feed_details()

        if obj['feed_url'] != None and obj['title'] != None and \
            obj['description'] != None and obj['link'] != None:
            assert True
        else:
            assert False
    except Exception:
        assert False
