#!/usr/bin/env python
import feedparser

if __name__ == "__main__":
    import urllib2
    import urllib
    url = "http://www.nyaa.se/?page=rss&cats=1_37&filter=1&term=[HorribleSubs]%20Hunter%20X%20Hunter%20720p"
    #url = "http://www.nyaa.se/?page=rss&cats=1_37&filter=1&term=[HorribleSubs] Hunter X Hunter 720p"
    #parsed_feeds = parse("rss_with_ampersand_link2.rss")
    #url = "nyaa.rss"
    url2 = urllib2.quote(url.encode("utf8"))
    print "url2:", url2
    print "unq:", urllib2.unquote(url2)
    #url = url2
    print "TYPE:", type(url)
    print "url:", url
    #print "url3:", urllib.urlencode(url)

    parsed_feeds = parse(url)
    print "parsed_feeds:", parsed_feeds

    for key in parsed_feeds["feed"].keys():
        print "key:", key

    if parsed_feeds["feed"].has_key("ttl"):
        print "TTL:", parsed_feeds["feed"]["ttl"]
    else:
        print "No TTL"

    for item in parsed_feeds['items']:
        #print "item:", item
        print "url:", item["link"]

