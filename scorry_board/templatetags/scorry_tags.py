from django import template

from scorry_board.models import News

register = template.Library()


@register.inclusion_tag("includes/news.html")
def news_block():
    try:
        news = News.objects.all().order_by('create_date').reverse()
    except News.DoesNotExist:
        news = []
    return {"news_list": news}

