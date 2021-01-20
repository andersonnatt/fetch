def strip_sentences(string):
	'''Takes string as argument and removes whitespace and changes
	case to lower, returning a string.'''
	result=string.strip().lower()
	return result

def remove_special_characters(string):
	'''Takes string as argument and removes special characters and numbers.
	Returns a list of each word in the string.'''
	chars_to_remove = [',','<','@','#','&','$','%','*',':','?','!','.','0','1','2','3','4','5','6','7','8','9']
	for char in chars_to_remove:
		string = string.replace(char,'')
	return string.split(' ')

def replace_contractions(word_list):
	'''Takes in list of words as argument and replaces common contractions based
	on those represented in the contraction_dict.  Returns list of words, with
	those contractions replaced with full text.'''
	contraction_dict = {
		"n't":"not",
		"'s":"is",
		"'m":"am",
		"'re":"are",
		"'ll":"will",
		"'d":"would",
		"'ve":"have"
	}
	result = []
	for word in word_list:
		if "'" in word:
			for contraction in contraction_dict:
				if contraction in word:
					first = word.replace(contraction,'')
					second = contraction_dict.get(contraction)
					result.append(first)
					result.append(second)
		else:
			result.append(word)
	return result

def remove_stop_words(string_as_list):
	'''Takes in list of words as agrument and removes those that occur in
	the stop_words list in the function.  These words are not heavily weighted
	in the English language and can contribute to noise in similarity study.'''
	stop_words = ['ourselves', 'hers', 'between', 'yourself', 'but', 'again', 'there', 'about', 'once', 'during', 'out', 'very', 'having', 'with', 'they', 'own', 'an', 'be', 'some', 'for', 'do', 'its', 'yours', 'such', 'into', 'of', 'most', 'itself', 'other', 'off', 'is', 's', 'am', 'or', 'who', 'as', 'from', 'him', 'each', 'the', 'themselves', 'until', 'below', 'are', 'we', 'these', 'your', 'his', 'through', 'don', 'nor', 'me', 'were', 'her', 'more', 'himself', 'this', 'down', 'should', 'our', 'their', 'while', 'above', 'both', 'up', 'to', 'ours', 'had', 'she', 'all', 'no', 'when', 'at', 'any', 'before', 'them', 'same', 'and', 'been', 'have', 'in', 'will', 'on', 'does', 'yourselves', 'then', 'that', 'because', 'what', 'over', 'why', 'so', 'can', 'did', 'not', 'now', 'under', 'he', 'you', 'herself', 'has', 'just', 'where', 'too', 'only', 'myself', 'which', 'those', 'i', 'after', 'few', 'whom', 't', 'being', 'if', 'theirs', 'my', 'against', 'a', 'by', 'doing', 'it', 'how', 'further', 'was', 'here', 'than']
	result = []
	for word in string_as_list:
		if word not in stop_words:
			result.append(word)
	return result

def wordbank_freq(list_of_words):
	'''Takes in list of words as argument and creates a dictionary with keys
	of unique words from list and values of number of occurences.  This
	dictionary is the output.'''
	result = {}
	for word in list_of_words:
		if word in result:
			result[word] = result[word] + 1
		else:
			result[word] = 1
	return result

def freq_dict(original_dict):
	'''Takes dictionary of words and number of occurences as argument.  The
	output is a similar dictionary, though instead of occences it shows
	a percentage of total string represented by word that is the key.'''
	total = sum(original_dict.values())
	final = {}
	for i in original_dict:
		final[i] = original_dict[i]/total
	return final

def ngram_freq(list_of_words):
	'''Takes in a list of words, where each item is two words separated by a space.
	This list is then made into a dictionary where keys are unique two word items
	and values are the number of occurences in the entire list.'''
	result = {}
	for i in range(0,len(list_of_words)-1):
		temp = ' '.join(list_of_words[i:i+2])
		if temp in result:
			result[temp] = result[temp] + 1
		else:
			result[temp] = 1
	return result

def whole_thing(string):
	'''Takes in string as argument and uses the above functions to return
	2 dictionaries with keys being word(s) and values being their % of
	occurence in the original string'''
	result = strip_sentences(string)
	result = remove_special_characters(result)
	result = replace_contractions(result)
	result = remove_stop_words(result)
	result2 = result
	result = wordbank_freq(result)
	result = freq_dict(result)
	result2 = ngram_freq(result2)
	result2 = freq_dict(result2)
	return result,result2

def get_similarity_score(one,two):
	'''Takes in 2 dictionaries where keys are word(s) and values are % of
	occurence in original string as arguments.  Looping through each key,
	if present in both dictionaries, the lesser value is added to the 
	score which starts at 0.  This score is then returned.'''
	score = 0
	for key in one:
		if key in two:
			if one.get(key) > two.get(key):
				score+=two.get(key)
			else:
				score+=one.get(key)
	return score

def get_total_score(one,two):
	'''Takes in two scores that are between 0 and 1 as arguments.  These 
	scores are weighted evenly and an overall score is returned.'''
	return (one * 0.5) + (two * 0.5)
