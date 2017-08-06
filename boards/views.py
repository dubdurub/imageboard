from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader
from .models import *
from .forms import Postform
from django.utils import timezone
test=1
def kekes(request):
	if request.method == 'POST':
		form = Postform(request.POST, request.FILES)
		if form.is_valid():
			thr=thread(board_id=1)
			thr.save()
			posteque=Post(thread_id=thr.ID,
						text=form.cleaned_data['text'],
						img=request.FILES['image'],
						published_date=timezone.now())
			posteque.save()
	else:
		form = Postform()
	posts=[]	#Создание списка для хранения постов
	posts_sequence=Post.objects.order_by('-ID')	#Сортировка постов в порядке убывания 
	thread_sequence=[]	#Создание списка тредов, для последующей сортировки по последним постам
	for o in posts_sequence:	#Добавление ID тредов в список по последним постам
		if thread_sequence.count(o.thread_id)<1:
			thread_sequence.append(o.thread_id) 
	for j in thread_sequence: # Перебор постов в отсортированных тредах
		temp_posts=[] #Временный список для хранения постов
		thread_posts=Post.objects.filter(thread_id__exact=j) #Выбор постов по thread_id
		temp_posts.append(thread_posts[0]) #Добавление в список заглавного (ОП) поста
		if thread_posts.count() >3:
			latest_posts=thread_posts.filter()[:3] #Отображение 3-ех последних постов треда, если в треде более 3-х постов
			for k in latest_posts:
				temp_posts.append(k)
		else: 
			for k in thread_posts:
				if k != thread_posts[0]:
					temp_posts.append(k)
		posts.append(temp_posts)
	context = {
		'posts': posts, 
		'form': form,
	}
	return render(request,'boards/index.html',context)
def open_thread(request, op_id):
	op_post= get_object_or_404(Post, pk=op_id)
	posts_thread=Post.objects.filter(thread_id__exact=op_post.thread_id)
	context={'op_post': op_post,
			'posts_thread': posts_thread}
	return render(request, 'boards/open_thread.html', context)