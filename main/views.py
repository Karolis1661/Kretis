from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.urls import reverse

from main.models import Article, ArticleCategory, ClientRequest, Projects
from .forms import UserRequest, WebForm, EshopForm, DesignForm


def get_clients(request):
    client_logos = []
    for e in Projects.objects.all():
        client_logos.append(e.company_logo.url)

    return client_logos


def portfolio_images(request):
    portfolio_img = []
    for e in Projects.objects.all():
        portfolio_img.append(e.intro_image.url)

    return portfolio_img


def home_page(request):
    """Display articles, project covers"""

    articles = Article.objects.order_by('date')

    # display only first 3 articles on home page
    paginator = Paginator(articles, 3)
    page_number = request.GET.get('page')
    home_articles = paginator.get_page(page_number)

    clients = get_clients(request)
    port_img = portfolio_images(request)
    context = {'home_articles': home_articles, 'clients': clients, 'port_img': port_img}

    return render(request, 'main/pages/home.html', context)


def single_article(request, url):
    single = Article.objects.get(url=url)
    articles = Article.objects.order_by('date')
    paginator = Paginator(articles, 6)
    page_number = request.GET.get('page')
    single_articles = paginator.get_page(page_number)
    clients = get_clients(request)
    context = {'single': single,
               'single_articles': single_articles,
               'clients': clients}
    return render(request, 'main/pages/single_article.html', context)


def articles(request):

    a_articles = Article.objects.order_by('date')

    paginator = Paginator(a_articles, 3)
    page_number = request.GET.get('page')
    all_articles = paginator.get_page(page_number)

    if 'q' in request.GET:
        search_term = request.GET['q']
        all_articles = a_articles.filter(Q(category__category__icontains=search_term))
    clients = get_clients(request)
    context = {'all_articles': all_articles,
               'clients': clients}
    return render(request, 'main/pages/articles.html', context)


def websites(request):
    clients = get_clients(request)
    context = {'clients': clients}
    return render(request, 'main/pages/websites.html', context)


def e_shop(request):
    clients = get_clients(request)
    context = {'clients': clients}
    return render(request, 'main/pages/e_shop.html', context)


def design(request):
    clients = get_clients(request)
    context = {'clients': clients}
    return render(request, 'main/pages/design.html', context)


def contacts(request):

    if request.method != 'POST':
        # no data submitted, create blank form
        user_data = UserRequest()
    else:
        # post data submitted, process data
        user_data = UserRequest(request.POST)
        if user_data.is_valid():
            new_post = user_data.save(commit=False)
            new_post.save()
            return HttpResponseRedirect(reverse('home_page'))

    clients = get_clients(request)
    context = {'user_data': user_data,
               'clients': clients}
    return render(request, 'main/pages/contacts.html', context)


def calculator(request):

    if request.method != 'POST':
        # no data submitted, create blank form
        form = WebForm(label_suffix='')
        e_form = EshopForm(label_suffix='')
        d_form = DesignForm(label_suffix='')
    else:
        # post data submitted, process data
        form = WebForm(request.POST, label_suffix='')
        e_form = EshopForm(request.POST, label_suffix='')
        d_form = DesignForm(request.POST, label_suffix='')

        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.save()
            return HttpResponseRedirect(reverse('home_page'))

        if e_form.is_valid():
            new_post = e_form.save(commit=False)
            new_post.save()
            return HttpResponseRedirect(reverse('home_page'))

        if d_form.is_valid():
            new_post = d_form.save(commit=False)
            new_post.save()
            return HttpResponseRedirect(reverse('home_page'))

    clients = get_clients(request)
    context = {'form': form,
               'e_form': e_form,
               'd_form': d_form,
               'clients': clients}
    return render(request, 'main/pages/calculator.html', context)


def projects(request):
    projects = Projects.objects.order_by('date')
    clients = get_clients(request)
    context = {'projects': projects,
               'clients': clients}
    return render(request, 'main/pages/projects.html', context)


def single_project(request, client):
    single = Projects.objects.get(client=client)
    projects = Projects.objects.all()

    # display only first 3 articles on home page

    paginator = Paginator(projects, 1)
    page_number = request.GET.get(client)
    all_projects = paginator.get_page(page_number)

    clients = get_clients(request)
    context = {'single': single,
               'clients': clients,
               'all_projects': all_projects}
    return render(request, 'main/pages/single_project.html', context)
