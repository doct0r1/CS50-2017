from cgitb import text

import nltk
import self as self     # this module didn't used

"""takes one command argument and check if the word is positive, negative or natural
	TODO: 1) iterate over tokens 
		  2) check if it's positive or negative
		  3) return score"""


class Analyzer:
	"""Implements sentiment analysis."""

	def __init__(self, positives, negatives):
		"""Initialize Analyzer."""

		# TODO
		self.positiveSet = set()
		file = open(positives, "r")

		for line in file:
			if not line.startswith(';'):
				self.positiveSet.add(line.rstrip("\n"))
		file.close()

		self.negativeSet = set()
		file = open(negatives, "r")

		for line in file:
			if not line.startswith(';'):
				self.negativeSet.add(line.rstrip("\n"))
		file.close()

	def analyze(self, text):
		"""Analyze text for sentiment, returning its score."""

		# TODO
		tokenizer = nltk.tokenize.TweetTokenizer()
		tokens = tokenizer.tokenize(text)
		sum = 0
		for word in tokens:
			if word.lower() in self.positiveSet:
				sum += 1
			elif word.lower() in self.negativeSet:
				sum -= 1
			else:
				continue

		return sum
