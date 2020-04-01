from django.shortcuts import render, get_object_or_404
from .models import Listing
from django.core.paginator import EmptyPage, Paginator, PageNotAnInteger


def index(request):
    # query all published listings sort by date
    listings = Listing.objects.all().order_by(
        '-list_date').filter(is_published=True)

    # pagination
    paginator = Paginator(listings, 6)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)

    context = {
        'listings': paged_listings
    }

    return render(request, 'listings/listings.html', context)


def listing(request, listing_id):
    # if id is invalid, go to 404 page
    listing = get_object_or_404(Listing, pk=listing_id)

    context = {
        'listing': listing
    }

    return render(request, 'listings/listing.html', context)


def search(request):

    # search options
    make_listings = Listing.objects.all().order_by('make')
    makes = []
    for listing in make_listings:
        if listing.make not in makes:
            makes.append(listing.make)

    body_listings = Listing.objects.all().order_by('body_style')
    bodies = []
    for listing in make_listings:
        if listing.body_style not in bodies:
            bodies.append(listing.body_style)

    fuel_listings = Listing.objects.all().order_by('fuel')
    fuels = []
    for listing in fuel_listings:
        if listing.fuel not in fuels:
            fuels.append(listing.fuel)

    transmission_listings = Listing.objects.all().order_by('transmission')
    transmissions = []
    for listing in transmission_listings:
        if listing.transmission not in transmissions:
            transmissions.append(listing.transmission)

    # all listings for search query
    queryset_list = Listing.objects.order_by('-list_date')

    # condition search
    if 'condition' in request.GET:
        condition = request.GET['condition']
        if condition:  # check if not an empty string
            # search condition, '__iexact' search for exact result
            queryset_list = queryset_list.filter(condition__iexact=condition)

    # make search
    if 'make' in request.GET:
        make = request.GET['make']
        if make:  # check if not an empty string
            queryset_list = queryset_list.filter(make__iexact=make)

    # body_style search
    if 'body_style' in request.GET:
        body_style = request.GET['body_style']
        if body_style:  # check if not an empty string
            queryset_list = queryset_list.filter(body_style__iexact=body_style)

    # fuel search
    if 'fuel' in request.GET:
        fuel = request.GET['fuel']
        if fuel:  # check if not an empty string
            queryset_list = queryset_list.filter(fuel__iexact=fuel)

    # price search
    if 'price' in request.GET:
        price = request.GET['price']
        if price:  # check if not an empty string
            queryset_list = queryset_list.filter(
                price__lte=price)  # search price, '__let' search for number and lower value

    # transmission search
    if 'transmission' in request.GET:
        transmission = request.GET['transmission']
        if transmission:
            queryset_list = queryset_list.filter(
                transmission__iexact=transmission)

    context = {
        'makes': makes,
        'bodies': bodies,
        'fuels': fuels,
        'transmissions': transmissions,
        'queryset_list': queryset_list,
        'values': request.GET  # to preserve search query on page
    }

    return render(request, 'listings/search.html', context)
