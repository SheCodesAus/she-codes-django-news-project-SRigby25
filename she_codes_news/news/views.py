from django.views import generic
from django.urls import reverse_lazy, reverse
from .models import NewsStory
from .forms import StoryForm
from django.views.generic import UpdateView, DeleteView

class IndexView(generic.ListView):
    template_name = 'news/index.html'
    

    def get_queryset(self):
        '''Return all news stories.'''
        return NewsStory.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['latest_stories'] = NewsStory.objects.all().order_by('-pub_date')[:4]
        context['all_stories'] = NewsStory.objects.all()
        return context
         
class StoryView(generic.DetailView):
    model = NewsStory
    template_name = 'news/story.html'
    context_object_name = 'story'

class AddStoryView(generic.CreateView):
    form_class = StoryForm
    context_object_name = 'storyForm'
    template_name = 'news/createStory.html'
    success_url = reverse_lazy('news:index')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class UpdateStoryView(UpdateView):
    model = NewsStory
    template_name = 'news/createStory.html'
    fields = ['title', 'content', 'image', 'catergory']

    def get_success_url(self):
        story_id = self.object.id
        return reverse ('news:story', kwargs={'pk': story_id},)

class CatergoryView(generic.ListView):
    template_name = 'news/catergory.html'
    context_object_name = 'storys'

    def get_queryset(self):
        '''Return all news stories.'''
        return NewsStory.objects.filter(catergory=self.kwargs["catergory"])


class DeletePostView(DeleteView):
    model = NewsStory
    template_name = 'news/delete_post.html'
    success_url = reverse_lazy('news:index')

class AuthorView(generic.ListView):
    template_name = 'news/userstorys.html'
    context_object_name = 'storys'

    def get_queryset(self):
        '''Return all news stories.'''
        return NewsStory.objects.filter(author=self.kwargs["author"])