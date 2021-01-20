from django.db import models
from snippets.functions import whole_thing, get_similarity_score, get_total_score

# Create your models here.
class Snippet(models.Model):
	string_1 = models.TextField()
	string_2 = models.TextField()
	similarity = models.FloatField(null=True,blank=True)

	def __str__(self):
		return f'{self.similarity}'

	def save(self, *args, **kwargs):
		one,one_n = whole_thing(self.string_1)
		two,two_n = whole_thing(self.string_2)
		single_score = get_similarity_score(one,two)
		ngram_score = get_similarity_score(one_n,two_n)
		self.similarity = get_total_score(single_score,ngram_score)
		
		super(Snippet, self).save(*args, **kwargs)








