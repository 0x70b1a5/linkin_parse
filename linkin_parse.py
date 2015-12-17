# so titled because I've always despised the series of phonemes that make up the atrocious word 'LinkdIn' *shudder*
# and also, avoiding SEO. 
from bs4 import BeautifulSoup
from selenium import webdriver
import requests
from lxml import html
# --- #
import os
import csv
import time
import pdb

def getCurJob(soup):
	try: 
		p = soup.find_all('p', class_='title', dir='ltr')[0]
	except (IndexError, AttributeError):
		print "Failed to acquire target's current job."
	return tx(p)

def getPastJobs(soup):
	pastjobs_a = soup.find_all('header')
	past_jobs_html = decode(BeautifulSoup(pastjobs_a.contents).prettify())
	return past_jobs_html

# <shamelessly reused code from glvssdoor-scrvper>
def decode(thing):
	try:
		thing = u''.join(thing).encode(u'utf-8').strip()
	except (UnicodeDecodeError, UnicodeEncodeError, TypeError):
		print "Tried and failed to decode {}".format(thing)
	return thing

def tx(t):
	try:
		x = t.contents[0].strip(" \n")
		return x
	except (AttributeError, IndexError):
		return t
# </shamelessly reused code from glvssdoor-scrvper>

if __name__ == '__main__':

	print '''
	+---------------------------------+
	|                                 |
	| ARE YOU SURE YOU WANT TO GET ON |
	|      --------  ----  -----      |
	|   -- MERKLE'S  WILD  RIDE? --   |
	|      --------  ----  -----      |
	|                                 |
	|     <YES>         ==> <NO>      |
	|                                 |
	+---------------------------------+
	'''

	# time.sleep(3)

	print '''
	+---------------------------------+
	|                                 |
	|             TOO BAD!            |
	|                                 |
	|     DEATH COMES FOR US ALL,     |
	|         AS DOES MERKLE.         |
	|                                 |
	|   IT WAS NICE NOT KNOWING YOU.  |
	|                                 |
	+---------------------------------+
	'''

	# time.sleep(3)

	# the url (pronounced 'earl'):
	# TODO: ask for UID instead of having this hard-coded
	print 'Retrieving Earl.'
	# earl = 'http://l{0}nked{0}n.com/{0}n/franceshaugen'.format('i') # breaking this up --> Interested Parties can't search their own company name on GitHub and find this script

	# for now, read from file instead
	f=os.getcwdu()+'/page.html'
	soup = BeautifulSoup(open(f,'w'), 'html.parser')

	# get page source:
	print 'Acquiring sauce.'

	# # initialize webdriver
	# ff = webdriver.Firefox()

	# # log in to the dummy account
	# ff.get('http://l{0}nked{0}n.com/uas/log{0}n'.format('i'))
	# lie = ff.find_element_by_id("session_key-login")
	# lie.send_keys('cron.jobber@yandex.com')
	# time.sleep(1)
	# fib = ff.find_element_by_id("session_password-login")
	# fib.send_keys('passpass\r')
	# time.sleep(5)

	# # get the goods from Earl
	# ff.get(earl)
	# time.sleep(3)

	# # get the source
	# sauce = decode(ff.page_source)
	# ff.close()
	
	# make some soup with the delicious sauce
	print 'Brewing delicious soup.'
	# soup = BeautifulSoup(sauce, 'html.parser')
	# get our hands dirty
	print 'Entering the Matrix.'
	pdb.set_trace()

	with open(os.getcwdu()+"/results.txt", 'w') as out_f:
		file.write(getCurJob(soup))
		file.write(getPastJobs(soup))