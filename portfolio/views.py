from django.shortcuts import render
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Project, Category, Comment
from .forms import ShareForm, EditForm, CommentForm
from django.urls import reverse_lazy
from django.http import JsonResponse
from django.http import HttpResponse

# pycode style command
# pycodestyle portfolio/views.py --max-line-length=120


# Using Capital letter here to keep the foramt consistant in urls.py
def HomeView(request):
    return render(request, "home.html")


def ManifestoView(request):
    categories = Category.objects.all()
    return render(request, "manifesto.html", {"categories": categories})


def CategoryView(request, category):
    categories = Category.objects.all()
    projects = Project.objects.filter(category=category)
    length = len(projects)
    return render(
        request, "category.html", {
            "category": category,
            "categories": categories,
            "projects": projects,
            "length": length
        })


@csrf_exempt
def Like(request, project_id):
    if request.method == "PUT":
        project = Project.objects.get(pk=project_id)
        liked_projects = project.likes.all()
        if request.user in liked_projects:
            # click twice to undo liking a post
            project.likes.remove(request.user)
        else:
            project.likes.add(request.user)
        project.save()
        return JsonResponse({"likes": project.likes.count()})


def SharedProjectView(request):
    superuser = User.objects.filter(is_superuser=True).first()
    projects = Project.objects.exclude(author=superuser)
    categories = Category.objects.all()

    return render(request, "shared_projects.html", {
        "projects": projects,
        "categories": categories
    })


class IndexView(ListView):
    model = Project
    template_name = 'index.html'
    ordering = ['-timestamp']

    def get_context_data(self, *args, **kwargs):
        categories = Category.objects.all()
        context = super(IndexView, self).get_context_data(*args, **kwargs)
        context["categories"] = categories
        return context


class ProjectDetailView(DetailView):
    model = Project
    template_name = 'details.html'

    def get_context_data(self, *args, **kwargs):
        categories = Category.objects.all()
        context = super(ProjectDetailView,
                        self).get_context_data(*args, **kwargs)
        context["categories"] = categories
        return context


class ShareProjectView(CreateView):
    model = Project
    form_class = ShareForm
    template_name = 'share.html'

    # other ways to control fields showing on the page #
    # fields = '__all__'
    # fields = ('title','content')

    def get_context_data(self, *args, **kwargs):
        categories = Category.objects.all()
        context = super(ShareProjectView,
                        self).get_context_data(*args, **kwargs)
        context["categories"] = categories
        return context


class CommentView(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'comment.html'
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        form.instance.project_id = self.kwargs['pk']
        return super().form_valid(form)


class AddCategoryView(CreateView):
    model = Category
    fields = '__all__'
    template_name = 'new_category.html'


class EditProjectView(UpdateView):
    model = Project
    form_class = EditForm
    template_name = 'edit.html'


class DeleteProjectView(DeleteView):
    model = Project
    template_name = 'delete.html'
    success_url = reverse_lazy('index')
