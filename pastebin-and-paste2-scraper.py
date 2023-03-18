# Fully working link scraper for pastebin.com and paste2.org
# Works only for Static webpages.

import requests
import re

url = "https://paste2.org/JZ6U2EaD"  # paste2.com example
# url = "https://pastebin.com/CzNhsbVf"  # pastebin.com example

raw_rows = [link.strip() for link in requests.get(url).text.split("\n")]

# Empty list of tuples for URLs
all_urls_list = []

# Regex pattern for all links:
URL_REGEX = r"""((?:(?:https|ftp|http)?:(?:/{1,3}|[a-z0-9%])|[a-z0-9.\-]+[.](?:com|org|uk)/)(?:[^\s()<>{}\[\]]+|\([^\s()]*?\([^\s()]+\)[^\s()]*?\)|\([^\s]+?\))+(?:\([^\s()]*?\([^\s()]+\)[^\s()]*?\)|\([^\s]+?\)|[^\s`!()\[\]{};:'".,<>?«»“”‘’])|(?:(?<!@)[a-z0-9]+(?:[.\-][a-z0-9]+)*[.](?:com|uk|ac)\b/?(?!@)))"""

# Load all filehosts for filtering:
filename = "filehosts.txt"
with open(filename, "r") as file:
    filehosts = file.readlines()
    filehosts = [x.strip() for x in filehosts]

print(filehosts)

# Matching only filehost links
matching = [s for s in raw_rows if any(xs in s for xs in filehosts)]

for string in matching:
    urls = re.findall(URL_REGEX, string)
    all_urls_list.append(urls)

# Convert list of lists into a list:
urls_list = [item for t in all_urls_list for item in t]

# Removing duplicates (if they exists)
urls_no_dupes = list(dict.fromkeys(urls_list))

print(urls_no_dupes)
