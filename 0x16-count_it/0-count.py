#!/usr/bin/python3

'''
recursive function that queries the Reddit API,
parses the title of all hot articles,
and prints a sorted count of given keywords
'''

from collections import Counter, defaultdict
import re
import requests


def count_words(subreddit, word_list, res=defaultdict(int), after=None):
    ''' Counting the words in subreddit '''
    ag = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6)\
            AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132i\
            Safari/537.36"
    headers = {"User-Agent": ag}
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    if after:
        url += '?after={}'.format(after)
    try:
        r = requests.get(url, headers=headers, allow_redirects=False).json()
        titles = r.get('data').get('children')
        for x in titles:
            c = Counter(x.get('data').get('title').lower().split(' '))
            for wrd in word_list:
                if wrd.lower() in c:
                    res[wrd] += c.get(wrd.lower())
        after = r.get('data').get('after')
        if after:
            return count_words(subreddit, word_list, res, after)
        sort_first = sorted(res.items(), key=lambda x: x[0])
        for k, v in sorted(sort_first, key=lambda x: x[1], reverse=True):
            print('{}: {}'.format(k, v))
    except:
        return
