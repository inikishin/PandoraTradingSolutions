import re

from django.db import models
import marketDictionary.models as md
from django.conf import settings


class AnalysisType(models.Model):
    type_name = models.CharField(max_length=100)

    def __str__(self):
        return self.type_name

# markdowns for texfields
# https://pocoz.gitbooks.io/django-v-primerah/rasshirenie-prilozheniya-blog/sozdanie-kastomizirovannyh-shablonov-tegov-i-filtrov/sozdanie-filtrov-shablonizatora-django.html
# https://daringfireball.net/projects/markdown/basics


class Post(models.Model):
    analysis_type = models.ForeignKey(AnalysisType, on_delete=models.CASCADE)
    ticker = models.ForeignKey(md.Ticker, on_delete=models.CASCADE)
    date_analysis = models.DateField()
    post_img = models.TextField()
    post_description = models.TextField()
    header = models.TextField()
    content = models.TextField()
    slug = models.SlugField(max_length=250, unique_for_date='date_analysis')
    slug_url = models.SlugField(default='')
    created = models.DateTimeField(auto_now_add=True)
    sig_elder = models.IntegerField(default=0)
    sig_channel = models.IntegerField(default=0)
    sig_DivBar = models.IntegerField(default=0)
    sig_NR4ID = models.IntegerField(default=0)
    sig_breakVolatility = models.IntegerField(default=0)
    sig_elder_proba = models.FloatField(default=0)
    sig_channel_proba = models.FloatField(default=0)
    sig_DivBar_proba = models.FloatField(default=0)
    sig_NR4ID_proba = models.FloatField(default=0)
    sig_breakVolatility_proba = models.FloatField(default=0)

    def __str__(self):
        return self.ticker.short_name + '_' + str(self.date_analysis)

    def get_absolute_url(self):
        return "/dailyanalysis/{0}/".format(self.slug_url)

    def get_description_for_signal(self, signal=''):
        if signal == 'weekly':
            descr_indx = 0
            img_str = 'weekly'
        elif signal == 'daily':
            descr_indx = 1
            img_str = '_daily_'
        elif signal == 'elder':
            descr_indx = 2
            img_str = 'elder'
        elif signal == 'channel':
            descr_indx = 3
            img_str = 'channel'
        elif signal == 'divbar':
            descr_indx = 4
            img_str = 'divbar'
        elif signal == 'volatility':
            descr_indx = 5
            img_str = 'volatility'
        else:
            descr_indx = 0
            img_str = 'weekly'

        signal_descriptions = re.findall(r"###[\D\d][^\[!]+", self.content)  # регулярка для всех описаний
        signal_descriptions_clear = []
        for d in signal_descriptions:
            if '###Содержание' not in d:
                d = re.sub(r'###[\D\d]+\}', '', d)  # Сделать реплейс этих значений
                d = re.sub(r'<[\D\d]+>', '', d)  # Сделать реплейс этих значений
                signal_descriptions_clear.append(d)
        sig_descr = signal_descriptions_clear[descr_indx].strip()

        img_links = re.findall(r'\[[\D]+\]\([media]{5}[A-z0-9\/.\)-]+', self.content)  # регулярка для всех ссылок
        img = ''
        for l in img_links:
            if img_str in l:
                img = l.split('(media_url/')[1][:-1] # возвращаем без закрывающей скобки
        return {'description': sig_descr,
                'img': img}

    def get_overview(self):
        if self.post_description != '' and self.post_img != '':
            return {'description': self.post_description,
                    'img': 'dailyAnalysis/' + self.post_img}

        # TODO: убрать весь код ниже и связанную функцию, после заполнения на сайте для всех статей post_img и post_description
        if self.sig_elder > 0:
            return self.get_description_for_signal(signal='elder')
        elif self.sig_channel > 0:
            return self.get_description_for_signal(signal='channel')
        elif self.sig_DivBar > 0:
            return self.get_description_for_signal(signal='divbar')
        elif self.sig_NR4ID > 0:
            return self.get_description_for_signal(signal='volatility')
        elif self.sig_breakVolatility > 0:
            return self.get_description_for_signal(signal='volatility')
        else:
            return self.get_description_for_signal(signal='daily')