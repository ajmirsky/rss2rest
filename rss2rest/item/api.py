from tastypie.resources import ModelResource
from item.models import FeedItem


class FeedItemResource(ModelResource):
    class Meta:
        queryset = FeedItem.objects.all()
        resource_name = 'feed_item'