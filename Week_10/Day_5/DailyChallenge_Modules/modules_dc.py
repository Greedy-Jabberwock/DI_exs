import requests
import time

urls = {'Google': 'https://www.google.com/',
       'GitHub': 'https://github.com/',
       'YouTube': 'https://www.youtube.com/',
       'StackOverflow': 'https://stackoverflow.com/'}

for key, value in urls.items():
    start = time.time()
    response = requests.get(value)
    end = time.time()
    time_taken = round(end - start, 4)
    print(f'{key} takes {time_taken} sec to load page.')