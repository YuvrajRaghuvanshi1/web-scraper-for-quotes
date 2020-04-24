from .models import  Quotes  
from django.views.generic import ListView
from bs4 import BeautifulSoup as Bsoup
import requests
from django.db.models import Q
from django.shortcuts import render, redirect

requests.packages.urllib3.disable_warnings()    
def scrape(request):
    session = requests.Session()
    session.headers = {"User-Agent": "Googlebot/2.1 (+http://www.google.com/bot.html)"}
    instance=Quotes.objects.all()
    instance.delete()
    i=1
    for i in range(1,4):
      url='https://www.goodreads.com/quotes?page='+str(i)
      source= requests.get(str(url)).content
      soup=Bsoup(source,'lxml')
      articles=soup.find_all('div',class_='quoteText')
      for article in  articles:
          #main = article.find('a')
          #link = main['href']
          #image_src = main.find('img')['src']
          text= article.text
          new_quote=Quotes()
          new_quote.quote=text
          #new_quote.image=image_src
          if len(new_quote.quote)<=255:
            new_quote.save()
    return redirect('../')

def home_list(request):
    headlines = Quotes.objects.all()
    context = {
        'object_list': headlines,
    }
    return render(request, "home.html", context)


def search(request)    :
  if request.method == 'GET':
        query= request.GET.get('q')

        submitbutton= request.GET.get('submit')

        if query is not None:
            lookups= Q(quote__icontains=query)

            results= Quotes.objects.filter(lookups).distinct()

            context={'results': results,
                     'submitbutton': submitbutton}

            return render(request, 'home.html', context)

        else:
            return render(request, 'home.html')

  else:
        return render(request, 'home.html')




