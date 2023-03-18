# **Pastebin and Paste2 Scraper for Filehosts links**

![Pastebin logo](/img/pastebin_logo.PNG)
![Paste2 logo](/img/paste2_logo.JPG)

</br>This is a Python script for web scraping filehosts links from pastebin [pastebin.com](https://pastebin.com) and [paste2.org](https://paste2.com) by using 'requests' library and 'regex' for recognizing URLs, so it's very fast! :)
</br>Install 'requests':
```
pip install requests
```
Filehosts are saved into filehosts.txt, and I had a few of them:
```
filecrypt.cc
safelinking.net
multiup.org
keeplinks.org
```
You can add more according to your needs.

### **Short description how it works:**
- Basicly, we are using requests we to retrieve all the text from url
- We are using Regex pattern to recognize urls from text
- From filehosts.txt we are loading all strings for maching only those links which are containing filehost
- At the end, we print only recognized (filehosts) links.
