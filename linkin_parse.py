# linkinParkway
# so titled because I've always despised the series of phonemes that make up the atrocious word 'LinkdIn' *shudder*
# and also, avoiding SEO. :D 
import os
from bs4 import BeautifulSoup
from selenium import webdriver
import requests
from lxml import html
# --- #
import csv
import time

def getCurJob(soup):
	p = soup.find_all('p', class_='title')
	return tx(p)

# <my own shamelessly reused code from glvssdoor-scrvper>
def decode(thing):
	try:
		return u''.join(thing).encode(u'utf-8').strip()
	except (UnicodeDecodeError, UnicodeEncodeError, TypeError):
		return thing

def tx(t):
	try:
		x = t.contents[0].strip(" \n")
		return x
	except (AttributeError, IndexError):
		x = ''
	return x
# </my own shamelessly reused code from glvssdoor-scrvper>


if __name__ == '__main__':

	# the cookies.
	cukie = [{u'domain': u'.linkedin.com', u'name': u'lang', u'value': u'"v=2&lang=en-us"', u'expiry': None, u'path': u'/', u'httpOnly': False, u'secure': False}, {u'domain': u'.linkedin.com', u'name': u'bcookie', u'value': u'"v=2&795eea1c-9100-4a08-836c-f4e80ca9bf54"', u'expiry': 1512159247, u'path': u'/', u'httpOnly': False, u'secure': False}, {u'domain': u'.www.linkedin.com', u'name': u'bscookie', u'value': u'"v=1&2015120208363494695453-3519-4047-859a-530c87aaf5dbAQEL22OcDDzNcQf506Wuw33EtOFB9Gx_"', u'expiry': 1512159247, u'path': u'/', u'httpOnly': True, u'secure': True}, {u'domain': u'www.linkedin.com', u'name': u'L1c', u'value': u'3d5be962', u'expiry': None, u'path': u'/', u'httpOnly': False, u'secure': False}, {u'domain': u'www.linkedin.com', u'name': u'L1e', u'value': u'a98019b', u'expiry': None, u'path': u'/', u'httpOnly': False, u'secure': False}, {u'domain': u'.linkedin.com', u'name': u'_ga', u'value': u'GA1.2.2128523357.1449045397', u'expiry': 1512117396, u'path': u'/', u'httpOnly': False, u'secure': False}, {u'domain': u'.linkedin.com', u'name': u'_gat', u'value': u'1', u'expiry': 1449045996, u'path': u'/', u'httpOnly': False, u'secure': False}, {u'domain': u'.www.linkedin.com', u'name': u'sl', u'value': u'"v=1&IWpdY"', u'expiry': 1456821403, u'path': u'/', u'httpOnly': False, u'secure': False}, {u'domain': u'.www.linkedin.com', u'name': u'JSESSIONID', u'value': u'"ajax:7939485161767611347"', u'expiry': 1456821403, u'path': u'/', u'httpOnly': False, u'secure': True}, {u'domain': u'.www.linkedin.com', u'name': u'li_at', u'value': u'AQEDARaFT1wFKxuDAAABUWHWKEEAAAFRYkQFQUsAE0kieDkemVA0irMoDRYsOFLpXrre0LguAck8dMq5CO7ZXqo3l-kfeOK3PvqL_aqtTgzYnHWGcTExGWnSFPTknQQBwjX4jro4vhIsC4z4T3tYnOk1', u'expiry': 1456821403, u'path': u'/', u'httpOnly': True, u'secure': True}, {u'domain': u'.linkedin.com', u'name': u'liap', u'value': u'true', u'expiry': 1456821403, u'path': u'/', u'httpOnly': False, u'secure': False}, {u'domain': u'.linkedin.com', u'name': u'lidc', u'value': u'"b=LB56:g=311:u=29:i=1449045403:t=1449124645:s=AQG25PXWFyi7c-sLb-l7gUxkEAAZ2kv-"', u'expiry': 1449124645, u'path': u'/', u'httpOnly': False, u'secure': False}, {u'domain': u'.linkedin.com', u'name': u'RT', u'value': u's=1449045403897&r=https%3A%2F%2Fwww.linkedin.com%2Fuas%2Flogin%3Fgoback%3D%252Enppvan_franceshaugen%26trk%3Dhb_signin', u'expiry': 1449046003, u'path': u'/', u'httpOnly': False, u'secure': False}, {u'domain': u'www.linkedin.com', u'name': u'oz_props_fetch_size1_undefined', u'value': u'undefined', u'expiry': 1449056206, u'path': u'/', u'httpOnly': False, u'secure': False}, {u'domain': u'www.linkedin.com', u'name': u'wutan', u'value': u'G1sF3mqWrPKaQXpg/beISgA+sPffI+WvPW7rwLzTPBU=', u'expiry': None, u'path': u'/', u'httpOnly': False, u'secure': False}, {u'domain': u'www.linkedin.com', u'name': u'share_setting', u'value': u'PUBLIC', u'expiry': None, u'path': u'/', u'httpOnly': False, u'secure': False}, {u'domain': u'.linkedin.com', u'name': u'_lipt', u'value': u'0_1p9HKGNR_4Z-8O0u-XB4h8HpSrjga4XLQEm8-LYj2YMPVdzhRLvlUqHg8B_NMzZx5ArqxUA3nBxYekuQWrFA1Pk_oqUUzQraA1slDP4O1DqnjJAtfdpS_MGJ14HJuANDW4efVt8btHncsAty1ECeARv62Nk-HxjjTidQA1mcowHDQTNyPGmikSurwbiuL3PdDFEkAZ-N8q9-jfgchdWLqOxlGz1HEHs2z-hYG8G3aL3HVsIlV9R0vN_j6j-GZ5ULWTvIwRl-k1UcQZ9BmsTpgO', u'expiry': 1451637407, u'path': u'/', u'httpOnly': False, u'secure': False}, {u'domain': u'.linkedin.com', u'name': u'sdsc', u'value': u'1%3A1SZM1shxDNbLt36wZwCgPgvN58iw%3D', u'expiry': None, u'path': u'/', u'httpOnly': True, u'secure': False}, {u'domain': u'www.linkedin.com', u'name': u'visit', u'value': u'"v=1&M"', u'expiry': 1512117407, u'path': u'/', u'httpOnly': False, u'secure': False}]

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

	time.sleep(3)

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

	time.sleep(2)

	# the url (pronounced 'earl'):
	# TODO: ask for UID instead of having this hard-coded
	print 'Retrieving Earl.'
	earl = 'http://linked{0}n.com/in/franceshaugen'.format('i') # breaking this up --> Interested Parties can't search their own company name on GitHub and find this script
	
	# get page source:
	print 'Acquiring sauce.'

	# this next bit is kind of fun
	# the first part adds options to the Chrome driver,
	# which then lets us manipulate its cookies
	# in an SQLite3 db at userdir/Default/Cookies.
	o = webdriver.ChromeOptions()
	o.add_argument("--user-data-dir=userdir")
	c = webdriver.Chrome(chrome_options=o)

	# get the goods from Earl
	c.get(earl)
	sauce = decode(ff.page_source)
	# cooks = decode(ff.get_cookies())
	c.close()
	# print cooks # but are there TOO MANY?...
	
	# make some soup with the delicious sauce
	print 'Brewing delicious soup.'
	soup = BeautifulSoup(sauce, 'html.parser')
	# get our hands dirty
	print 'Entering the Matrix.'
	getCurJob(soup)