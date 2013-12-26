from django.contrib.syndication.views import Feed
from django.utils import feedgenerator
from btlib.models import *


class Feed(Feed):
    feed_type = feedgenerator.Rss201rev2Feed
    title = "Baka Tsuki Library"
    link = "/"
    description = "Updates"

    def items(self):
        return Novel.objects.order_by('-id')[:25]

    def item_title(self, item):
        return item.novel.name + " - " + str(item.number) + " - " + item.name

    def item_categories(self, item):
        return item.novel.genre.all()

    def item_pubdate(self, item):
        return item.created

    def item_description(self, item):
        return item.synopsis

    # item_link is only needed if NewsItem has no get_absolute_url method.
    def item_link(self, item):
        return item.get_absolute_url()


class AtomVolumeFeed(Feed):
    feed_type = feedgenerator.Atom1Feed