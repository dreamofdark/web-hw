from django.db import models

from django.contrib.auth.models import User

# Create your models here.


class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user_profile')
	avatar = models.ImageField(upload_to='%Y/%m/%d', default='default.jpg')

	def __str__(self):
		return self.user.username

class Tag(models.Model):
	label = models.CharField(max_length=25)

	def __str__(self):
		return self.label

	class Meta:
		ordering = ('label',)

class QuestionManager(models.Manager):
	def get_new(self):
		return self.order_by('-date')
	def get_top(self):
		return self.order_by('-rating')
	def get_with_tag(self,tag):
		return self.filter(tags__label__iexact=tag).order_by('-date')
	def get(self, id):
		return self.filter(id__exact=id)[0]

class Question(models.Model):
	title = models.CharField(max_length=50)
	text = models.TextField()
	tags = models.ManyToManyField(Tag)
	rating = models.IntegerField(default = 0)
	author = models.ForeignKey(Profile, on_delete=models.CASCADE)
	date = models.DateTimeField(auto_now_add=True)
	objects = QuestionManager()

	def __str__(self):
		return self.title

	class Meta:
		ordering = ('id',)

class AnswerManager(models.Manager):
	def get_answer(self,question_id):
		return self.filter(question__id__exact=question_id).order_by('-rating','-date')


class Answer(models.Model):
	text = models.TextField()
	author= models.ForeignKey(Profile, on_delete=models.CASCADE)
	question = models.ForeignKey(Question, on_delete=models.CASCADE)
	rating = models.IntegerField(default = 0)
	date = models.DateTimeField(auto_now_add=True)
	correct = models.BooleanField(default=False) 
	objects = AnswerManager()

class Like(models.Model):
	like_type = models.IntegerField(default=0)
	user = models.ForeignKey(Profile, on_delete=models.DO_NOTHING)

	class Meta():
		abstract = True

class QuestionLike(Like):
	question = models.ForeignKey(Question, on_delete=models.CASCADE)

class AnswerLike(Like):
	answer = models.ForeignKey(Answer, on_delete=models.CASCADE)







