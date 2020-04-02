# Carss Online AUto Dealer

A Python | Django Project

Live at: http://18.144.133.255/

![alt text](image.jpg)

### SUMMARY

Carss is an online auto dealer website where users can search and browse car listing and contact the sales advisor for test drives, and the company can manage its employees (sales advisors), car listings, users, messages through an admin system.

The project is written in Python 3.7 and Django 3.0, including six apps - accounts, advisors, carss, contacts, listings, and pages; three models with 1 one-to-many relationship.


### TECHNOLOGIES

- Front-End Technologies: HTML 5 | CSS 3 | JavaScript | jQuery | Bootstrap | Lightbox
- Back-End: Python 3.7 | Django 3.0 | Pillow
- Database: PostgreSQL


### FEATURES

1. The website uses Bootstrap themes and is **fully responsive**, with dynamic page titles and breadcrumb on different pages. Customized logo and favicon.

2. Implemented **template partials** including base.html, topbar, navbar with highlighted active selection, footer with dynamic year using JavaScript, and alerts.

3. The About Page features a seller of the month section, the selected advisor can be changed on the Advisor’s “is_mvp (an advisor attribute)” in the Admin Area.

4. The Search Form queries the listing database and renders results based on the search query. The Search Results Page preserves the **search query** on the search form. 

5. All Listings Page renders all “published (a listing attribute)” listings, ordered by “list_date (a listing attribute)”. Implemented page pagination on the page using Django **Paginator** Package

6. Single Listing Page renders all information about a car, listing images can be displayed by **Lightbox** package

7. The Test Drive Request Form is available on the single listing page. If the user is logged in, the form will prepopulate its information. Backend validation prevents duplicate requests, if the user had filed the request for the same listing before, form submission will fail, and return a customized error message to the user. Upon successful submission, an **automated confirmation email** will be sent to the user’s email, and the request information will be shown on the user’s dashboard, as well as the admin area for the admin users.

8. **Login and Register validation** include blank check, email authentication, password confirmation, and a duplicate username and email check. Failed validation will return the customized error messages to the user. Dynamic navbar items based on user login status. When a user is logged in, it will show the user’s dashboard and logout options, otherwise, it shows register and login.

9. **Customized Django Admin Area** styling, list display, list filter, search field.
