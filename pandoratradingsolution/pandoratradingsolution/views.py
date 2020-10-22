from collections import Counter
import logging

from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.views import View
from django.contrib.flatpages.models import FlatPage
from django.contrib.sites.shortcuts import get_current_site
from django.shortcuts import get_object_or_404
from django.utils.safestring import mark_safe
from django.views.decorators.clickjacking import xframe_options_exempt

from pandoratradingsolution import settings
from integrations import api_google
from dailyAnalysis.models import Post
from .form import ContactForm
import marketDictionary.models as md
import predictions.models as post_model

@xframe_options_exempt
def mainpage(request):
    post_list = Post.objects.order_by('-date_analysis')[:30]

    context = {'post_list': post_list}

    return render(request, 'pandoratradingsolution/ms_index.html', context)

def handler404(request, exception):
    return render(request, 'pandoratradingsolution/error404.html', status=404)

def handler500(request):
    return render(request, 'pandoratradingsolution/error500.html', status=500)

def about(request):
    return render(request, 'pandoratradingsolution/ms_about.html')

def coming(request):
    return render(request, 'pandoratradingsolution/ms_coming.html')

def search(request):
    results = api_google.search(request.GET['q'])

    logging.config.dictConfig(settings.dictLogConfig)
    logger = logging.getLogger("google_api")
    logger.info('IP:{0}|Search_text:{1}'.format(request.META.get('REMOTE_ADDR'), request.GET['q']))

    if results['searchInformation']['totalResults'] == '0':
        context = {'q': results['queries']['request'][0]['searchTerms'],
                   'total_results': results['searchInformation']['totalResults'],
                   'results': ''}
    else:
        context = {'q': results['queries']['request'][0]['searchTerms'],
                   'total_results': results['searchInformation']['totalResults'],
                    'results': results['items']
                    }

    return render(request, 'pandoratradingsolution/ms_search.html', context=context)

def flatpage(request, url):
    if not url.startswith('/'):
        url = '/' + url
    site_id = get_current_site(request).id
    f = get_object_or_404(FlatPage, url=url, sites=site_id)

    f.title = mark_safe(f.title)
    f.content = mark_safe(f.content)

    context = {'flatpage': f}
    context.update(get_navbar_stat())
    return render(request, 'flatpages/default.html', context=context)

class EContactsView(View):
    template_name = 'pandoratradingsolution/ms_contact.html'

    # В случае get запроса, мы будем отправлять просто страницу с контактной формой
    def get(self, request, *args, **kwargs):
        context = {}
        context['contact_form'] = ContactForm()

        return render(request, template_name=self.template_name, context=context)

    def post(self, request, *args, **kwargs):
        context = {}

        form = ContactForm(request.POST)

        # Если не выполнить проверку на правильность ввода данных,
        # то не сможем забрать эти данные из формы... хотя что здесь проверять?
        if form.is_valid():
            email_subject = 'PTS : Сообщение с сайта через контактную форму с темой: {0}'.format(form.cleaned_data['subject'])
            email_body = "С сайта отправлено новое сообщение\n\n" \
                         "Имя отправителя: %s \n" \
                         "E-mail отправителя: %s \n\n" \
                         "Тема: %s \n\n" \
                         "Сообщение: \n" \
                         "%s " % \
                         (form.cleaned_data['name'], form.cleaned_data['email'], form.cleaned_data['subject'], form.cleaned_data['message'])

            # и отправляем сообщение
            send_mail(email_subject, email_body, settings.EMAIL_HOST_USER, settings.EMAIL_TARGET, fail_silently=False)
            context = {'send_success': True}

        return render(request, template_name=self.template_name, context=context)

# Additional funcs
def get_navbar_stat():
    post_all = Post.objects.all().order_by('-date_analysis')
    post_count = len(post_all)
    pred_count = len(post_model.Prediction.objects.all())

    d_list = []
    for p in post_all:
        d_list.append(p.date_analysis.replace(day=1))
    post_counter = list(Counter(d_list).items())

    ticker_list = md.Ticker.objects.all()

    context = {'post_count': post_count,
               'pred_count': pred_count,
               'post_counter': post_counter,
               'ticker_list': ticker_list}

    return context