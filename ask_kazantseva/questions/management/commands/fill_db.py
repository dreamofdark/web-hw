from django.core.management.base import BaseCommand, CommandError
from questions.models import Profile, Tag, Question, Answer, User

class Command(BaseCommand):
	help =''

	def execute(*args, **options):
		for i in range(7):
			user = User.objects.create(username='New User{0}'.format(i), password='qwe456788')
			profile = Profile.objects.create(user=user)

		for i in range(10):
			tag = Tag.objects.create(label='topTag{0}'.format(i))

		for i in range(47):
			user = Profile.objects.get(user__username='New User{0}'.format(i%7))
			quest = Question.objects.create(
				title = "This is question {0}".format(i),
				text = "Some text in question {0}. ".format(i) * 7,
				rating = 5 * i - 8,
				author = user
				)

			for j in range(3):
				onetag = Tag.objects.get(label='topTag{0}'.format((i+j)%10))
				quest.tags.add(onetag)

			for a in range(17):
				user_answ = Profile.objects.get(user__username='New User{0}'.format((i + 3) % 7))
				answer = Answer.objects.create(
					text = "the perfect answer here {0}. ".format(a) * 4,
					author = user_answ,
					question = quest,
					rating = i - a
					)
		


