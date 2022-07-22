from sys import stdout
from django.core.management.base import BaseCommand, CommandError
import feedparser
from dateutil import parser

from rss.models import Actual,Newest,News,Show,Sport,Tech,Lifestyle,Viral


URLS = {'actual': 'https://www.24sata.hr/feeds/aktualno.xml',
        'newest': 'https://www.24sata.hr/feeds/najnovije.xml',
        'news': 'https://www.24sata.hr/feeds/news.xml',
        'show': 'https://www.24sata.hr/feeds/show.xml',
        'sport': 'https://www.24sata.hr/feeds/sport.xml',
        'lifestyle': 'https://www.24sata.hr/feeds/lifestyle.xml',
        'tech': 'https://www.24sata.hr/feeds/tech.xml',
        'viral': 'https://www.24sata.hr/feeds/fun.xml'  
}

MODEL_NAMES = { 'actual': Actual,
                'newest': Newest,
                'news': News,
                'show': Show,
                'sport': Sport,
                'lifestyle': Lifestyle,
                'tech': Tech,
                'viral': Viral, 
                }

class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('feed',choices=URLS.keys())
    
    def handle(self, *args, **options):
        arg = options['feed']
        
        if not arg in URLS.keys():
            raise CommandError('Argument must be some of these: {}',format(URLS.keys()))
        url = URLS.get(arg,False)
        if not url:
            raise CommandError('There is no valid URL supplied for this argument')
        Obj = MODEL_NAMES.get(arg,False)
        if not Obj:
            raise CommandError('There is no valid model supplied for this argument')
        feed = feedparser.parse(url)
        for item in feed.entries:
            link = item.summary_detail['value'].split('src="')[1].split('"')[0] 
            # constraint to restrict creation of same objects
            if not Obj.objects.filter(guid=item.guid).exists():
                if item.author_detail.name is not None:
                    creator_name = item.author_detail.name
                record = Obj(
                        name = item.title,
                        text = item.description.split('/>')[-1],
                        url_adress = item.link,
                        guid = item.guid,
                        category = item.category,
                        creator_name = creator_name,
                        pub_date = parser.parse(item.published), # datum nije bilo dovoljno uzeti iz xml-a, django trazi drugaciji oblik -> YYYY-MM-DD HH:MM[:ss[.uuuuuu]][TZ]
                        image_url = link,
                        
                    )
                record.save()
        self.stdout.write('SUCCESFUL!!')
