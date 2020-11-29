from django.contrib.syndication.views import Feed
from django.template.defaultfilters import truncatewords
from .models import * #Post is model
from django.urls import reverse

# context in feeds is "obj"

class LatestPostsFeed(Feed):
    title = "My blog"
    link = ""
    description = "New posts of my blog."
    #description_template = "feeds/articles.html"

    def items(self):
        return #Post.objects.filter(status=1)

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return truncatewords(item.content, 30)
    
    #def get_context_data(self, **kwargs):
    #    context = super().get_context_data(**kwargs)
    #    context['foo'] = 'bar'
    #    return context

    # Only needed if the model has no get_absolute_url method
    # def item_link(self, item):
    #     return reverse("post_detail", args=[item.slug])