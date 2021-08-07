# Python-JavaScript---Blog

This web app is a dynamic and interactive portfolio application for owners(superusers) who wish to demonstrate their works/projects. The web application allows each visitor to choose between visiting as a guest or register and become a member so that they can like, share their own works with the owner. All types of users can leave comments/feedbacks on each project. Also, these interactions is helpful to get instant feedback on what type of works that would attract more visitors based on the likes. Since the design purpose is to mainly demonstrating the owner's work, so as to not create conflictions, there are two separate pages for shared projects and owners' for a better user experience.

## File Structure
- Final (default project files from Django when created) 
  - settings.py (with my installed apps and added urls)
  - urls.py (Registering all my app urls and media urls)
- media
  - Images (All uploaded images will be saved here)
- members (app created for users, for clearer site structuring)
  - templates
- registration
  - login.html (login pages for members)
  - register.html (register page for new member)
  - forms ( the registration form )
  - urls.py ( contains my url for register page )
  - views.py ( view of my registration page )
- portfolio ( main App )
- templates
  - category.html (filter projects with selected category)
  - comment.html (add a new comment to a project)
  - delete.html (a delete project page when author try to delete a project)
  - details.html (displays a project details)
  - edit.html (a page where the project author could update their shared projects) • home.html (default path, a welcoming page)
  - index.html (a page with all projects by me)
  - layout.html (the overall layout format for the web app)
  - manifesto.html (a page about me and personal statement)
  - new_category.html (allows a user to add a new category for all projects)
  - share.html (share project form where user can upload image)
  - shared_projects.html (a page with all projects shared by other users)
- admin.py (registered my models)
- forms.py (includes all forms created for portfolio app, to have a clean code structure)
- models.py (contains category, project, comment models)
- urls.py (all urls for portfolio app)
- views.py (have functional view and class view)
- requirement.txt (have extra Django installments)

## Getting Started

### Run App
1. Download the folder
2. In your terminal, `cd` into the mail directory.
3. Run `python manage.py makemigrations` mail to make migrations for the mail app.
4. Run `python manage.py migrate` to apply migrations to your database.
5. Run `python manage.py runserver` to start local host

### Managing Database
1. In your terminal, `cd` into the mail directory.
2. Run `python manage.py createsuperuser`, then follow the instructions 
3. Run `python manage.py runserver` to start local host
4. Open a Web browser and go to “/admin/” on your local domain – e.g., http://127.0.0.1:8000/admin/
