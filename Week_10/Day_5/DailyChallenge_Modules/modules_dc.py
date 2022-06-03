import requests
import time

urls = {'Google': 'https://www.google.com/',
       'GitHub': 'https://github.com/',
       'YouTube': 'https://www.youtube.com/',
       'StackOverflow': 'https://stackoverflow.com/'}


def time_counter(name, url):
    start = time.time()
    requests.get(url)
    end = time.time()
    time_taken = round(end - start, 4)
    print(f'{name} takes {time_taken} sec to load page.')


for key, value in urls.items():
    time_counter(key, value)