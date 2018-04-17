from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render

from questions.models import Profile, Tag, Question, Answer

# Create your views here.

# questions = []
# for i in range(1,10):
#     questions.append({
#         'title': 'title' + str(i),
#         'id': i, 
#         'text': ('user' + str(i) + ' wants to ask one question and answer') * i * 2,
#         'user': 'user' + str(i),
#         'rating': i*8+4,
#         'tags':[str(i) + 'code', str(i) + 'work', str(i) + 'sleep' ],
#     })

tags_list1 = ['python','googlej','poka', 'work', 'code', 'SQL', 'mail', 'TechnoPark']


# def user_form(request):
# 	r_d = {
# 	'form': form
# 	}

tags_list = Tag.objects.all()

def index(request):
	authentificated = True
	type_page = 'index'

	questions = Question.objects.get_new()
	
	questions_on_page = paginate(request,questions,20)
	return render(request,'index.html',{'questions':questions_on_page, 'authentificated': authentificated, 'page_type':type_page, 'tags': tags_list})

def ask(request):
	return render(request,'ask.html')

def user_settings(request):
	return render(request,'settings.html')

def logout(request):
	authentificated = False
	type_page = 'index'
	return render(request,'index.html',{'questions':questions, 'authentificated': authentificated, 'page_type':type_page, 'tags': tags_list})

def signup(request):
	return render(request,'signup.html')

def login(request):
	return render(request,'login.html')

def question(request,id_question):
	answers = Answer.objects.get_answer(id_question)
	question = Question.objects.get(id_question)
	return render(request,'question.html',
		{'tags': tags_list,'answers':paginate(request,answers,30), 'question':question})


def tags(request,tag):
	authentificated = True
	type_page = 'tags'
	questions = Question.objects.get_with_tag(tag)
	questions_on_page = paginate(request,questions,20)
	return render(request,'index.html',{'questions':questions_on_page, 'authentificated': authentificated, 'page_type':type_page, 'tags': tags_list, 'tag':tag})

def hot(request):
	authentificated = True
	type_page = 'hot'
	questions = Question.objects.get_top()
	questions_on_page = paginate(request,questions,20)
	return render(request,'index.html',{'questions':questions_on_page, 'authentificated': authentificated, 'page_type':type_page, 'tags': tags_list})


def paginate(request, object_list, on_page):
	paginator = Paginator(object_list, on_page)
	page = request.GET.get('page')
	return paginator.get_page(page)

