from django.shortcuts import render
from listings.models import Listing
from advisors.models import Advisor


def index(request):

    # get the 3 latest listings
    listings = Listing.objects.order_by(
        '-list_date').filter(is_published=True)[:3]

    # query for search options
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

    context = {
        'listings': listings,
        'makes': makes,
        'bodies': bodies,
        'fuels': fuels,
        'transmissions': transmissions
    }

    return render(request, 'pages/index.html', context)


def about(request):
    # get all advisors
    advisors = Advisor.objects.all()

    # get mvp
    mvp_advisor = Advisor.objects.all().filter(is_mvp=True)

    context = {
        'advisors': advisors,
        'mvp_advisor': mvp_advisor
    }

    return render(request, 'pages/about.html', context)
