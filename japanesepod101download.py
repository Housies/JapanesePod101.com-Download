from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import urllib
from time import sleep
import re
import os

#this number determines which season the script starts from
number = int(raw_input('Season to start from (starts at 0): '))

#this number is used to name audio dialog files for the flashcards
count = int(raw_input('If continuing from previous attempt, put the count here. Otherwise, put 0: '))

#name of hiragana Anki flashcards file. It will be created in the same directory as the script. If the file exists it will add the lines to it
out_file = 'HIRAGANACARDS.txt'

#name of kanji Anki flashcards file. It will be created in the same directory as the script. If the file exists it will add the lines to it
out_file1 = 'KANJICARDS.txt'

#name of file with list of URLs that failed to load, plus the count. It will be created in the same directory as the script.
out_file2 = 'FAILLIST.txt'

#put your username on this line
username = 'USERNAME'

#put your password on this line
password = 'PASSWORD'

#full path of the location for flashcard audio
vocabdir = 'LOCATION'

#full path of the location for audio tracks
root = 'LOCATION'

#number of flashcards to create before giving up
limit = 50

#number of attempts to download a file or load page source before giving up
limit1 = 5

#maximum number of iterations of the loop to check if a URL has loaded
limit2 = 240

#maximum number of times to attempt to load a URL
limit3 = 1

def load(url):
    global source, resume2
    resume2 = True
    for n in range(limit3):
        try:
            driver.get(url)
        except:
            print 'URL load failed'
            print url
            with open(out_file2, "a") as myfile:
                myfile.write(url)
                myfile.write('\n')
            resume2 = False
            continue
        resume1 = True
        for n in range(limit1):
            try:
                prevsource = driver.page_source
                break
            except:
                t = '%s incomplete' % url
                print "Page didn't load completely", url
                with open(out_file2, "a") as myfile:
                    myfile.write(t)
                    myfile.write('\n')
                if n == limit1 - 1:
                    print 'Limit reached, giving up'
                    resume1 = False
        if resume1 == False:
            resume2 = False
            continue
        count2 = 0
        sleep(0.5)
        for n in range(limit1):
            try:
                source = driver.page_source
                break
            except:
                t = '%s incomplete' % url
                print "Page didn't load completely", url
                with open(out_file2, "a") as myfile:
                    myfile.write(t)
                    myfile.write('\n')
                if n == limit1 - 1:
                    print 'Limit reached, giving up'
                    resume1 = False
        if resume1 == False:
            resume2 = False
            continue
        while source not in prevsource:
            count2 = count2 + 1
            for n in range(limit1):
                try:
                    prevsource = driver.page_source
                    break
                except:
                    t = '%s incomplete' % url
                    print "Page didn't load completely", url
                    with open(out_file2, "a") as myfile:
                        myfile.write(t)
                        myfile.write('\n')
                    if n == limit1 - 1:
                        print 'Limit reached, giving up'
                        resume1 = False
                        break
            sleep(0.5)
            for n in range(limit1):
                try:
                    source = driver.page_source
                    break
                except:
                    t = '%s incomplete' % url
                    print "Page didn't load completely", url
                    with open(out_file2, "a") as myfile:
                        myfile.write(t)
                        myfile.write('\n')
                    if n == limit1 - 1:
                        print 'Limit reached, giving up'
                        resume1 = False
                        break
            if count2 == limit2:
                t = '%s incomplete' % url
                print "Page didn't load completely", url
                with open(out_file2, "a") as myfile:
                    myfile.write(t)
                    myfile.write('\n')
                break
                resume1 = False
        if resume1 == False:
            resume2 = False
def loadrefresh(url):
    global source, resume2
    resume2 = True
    for n in range(limit3):
        try:
            driver.get(url)
            driver.refresh()
        except:
            print 'URL load failed'
            print url
            with open(out_file2, "a") as myfile:
                myfile.write(url)
                myfile.write('\n')
            resume2 = False
            continue
        resume1 = True
        for n in range(limit1):
            try:
                prevsource = driver.page_source
                break
            except:
                t = '%s incomplete' % url
                print "Page didn't load completely", url
                with open(out_file2, "a") as myfile:
                    myfile.write(t)
                    myfile.write('\n')
                if n == limit1 - 1:
                    print 'Limit reached, giving up'
                    resume1 = False
        if resume1 == False:
            resume2 = False
            continue
        count2 = 0
        sleep(0.5)
        for n in range(limit1):
            try:
                source = driver.page_source
                break
            except:
                t = '%s incomplete' % url
                print "Page didn't load completely", url
                with open(out_file2, "a") as myfile:
                    myfile.write(t)
                    myfile.write('\n')
                if n == limit1 - 1:
                    print 'Limit reached, giving up'
                    resume1 = False
        if resume1 == False:
            resume2 = False
            continue
        while source not in prevsource:
            count2 = count2 + 1
            for n in range(limit1):
                try:
                    prevsource = driver.page_source
                    break
                except:
                    t = '%s incomplete' % url
                    print "Page didn't load completely", url
                with open(out_file2, "a") as myfile:
                    myfile.write(t)
                    myfile.write('\n')
                    if n == limit1 - 1:
                        print 'Limit reached, giving up'
                        resume1 = False
                        break
            sleep(0.5)
            for n in range(limit1):
                try:
                    source = driver.page_source
                    break
                except:
                    t = '%s incomplete' % url
                    print "Page didn't load completely", url
                    with open(out_file2, "a") as myfile:
                        myfile.write(t)
                        myfile.write('\n')
                    if n == limit1 - 1:
                        print 'Limit reached, giving up'
                        resume1 = False
                        break
            if count2 == limit2:
                t = '%s incomplete' % url
                print "Page didn't load completely", url
                with open(out_file2, "a") as myfile:
                    myfile.write(t)
                    myfile.write('\n')
                break
                resume1 = False
        if resume1 == False:
            resume2 = False

postfix1 = '#lc_transcript'
postfix2 = '#lc_vocabulary_list'
audioprefix = 'http://www.japanesepod101.com'
lessonsdir = '/lessons'
bonusdir = '/bonus tracks'
reviewsdir = '/review tracks'
dialogsdir = '/dialog tracks'
grammarsdir = '/grammar tracks'
url = 'http://www.japanesepod101.com'
try:
    os.makedirs(root)
except:
    pass
try:
    os.makedirs(vocabdir)
except:
    pass
driver = webdriver.Firefox()
driver.get(url)
driver.find_element_by_link_text('Sign in').click()
#this pause is to wait for the sign in box to appear
sleep(5)
inputElement = driver.find_element_by_name('amember_login')
inputElement.send_keys(username)
inputElement = driver.find_element_by_name('amember_pass')
inputElement.send_keys(password)
inputElement.submit()
url = 'http://www.japanesepod101.com/index.php?cat=Introduction'
load(url)
urls = re.findall(r'						<a href="?([^\'" >]+)', driver.page_source)
for url in urls[number:]:
    load(url)
    if resume2 == False:
        continue
    season = driver.title[17:]
    lessonseasondir = '%s%s/%s' % (root, lessonsdir, season)
    bonusseasondir = '%s%s/%s' % (root, bonusdir, season)
    reviewseasondir = '%s%s/%s' % (root, reviewsdir, season)
    dialogseasondir = '%s%s/%s' % (root, dialogsdir, season)
    grammarseasondir = '%s%s/%s' % (root, grammarsdir, season)
    os.makedirs(lessonseasondir)
    os.makedirs(bonusseasondir)
    os.makedirs(reviewseasondir)
    os.makedirs(dialogseasondir)
    os.makedirs(grammarseasondir)
    resume1 = True
    for n in range(limit1):
        try:
            source = driver.page_source
            break
        except:
            t = '%s incomplete' % url
            print "Page didn't load completely", url
            with open(out_file2, "a") as myfile:
                myfile.write(t)
                myfile.write('\n')
            if n == limit1 - 1:
                print 'Limit reached, giving up'
                resume1 = False
    if resume1 == False:
        print 'Failed to load season'
        print url
        with open(out_file2, "a") as myfile:
            myfile.write(url)
            myfile.write('\n')
        continue
    seasonurls = re.findall(r'rel="bookmark" href="?([^\'" >]+)', source)
    for ourl in seasonurls:
        load(ourl)
        if resume2 == False:
            continue
        resume1 = True
        for n in range(limit1):
            try:
                source = driver.page_source
                break
            except:
                t = '%s incomplete' % ourl
                print "Page didn't load completely", ourl
                with open(out_file2, "a") as myfile:
                    myfile.write(t)
                    myfile.write('\n')
                if n == limit1 - 1:
                    print 'Limit reached, giving up'
                    resume1 = False
        if resume1 == False:
            continue
        audiourls = re.findall(r'" data-mode="audio" data-url="?([^\'" >]+)', source)
        for t in audiourls:
            t1 = t
            while '/' in t1:
                t1 = t1[t1.find('/') + 1:]
            if 'bonus' in t:
                dldir = '%s/%s' % (bonusseasondir, t1)
                for n in range(limit1):
                    try:
                        urllib.urlretrieve (t, dldir)
                        break
                    except:
                        print 'Download failed'
                        print t, dldir
                        with open(out_file2, "a") as myfile:
                            myfile.write(t)
                            myfile.write('\n')
                            myfile.write(dldir)
                            myfile.write('\n')
                        sleep(10)
                        if n == limit1 - 1:
                            print 'Limit reached, giving up'
            elif 'review' in t:
                dldir = '%s/%s' % (reviewseasondir, t1)
                for n in range(limit1):
                    try:
                        urllib.urlretrieve (t, dldir)
                        break
                    except:
                        print 'Download failed'
                        print t, dldir
                        with open(out_file2, "a") as myfile:
                            myfile.write(t)
                            myfile.write('\n')
                            myfile.write(dldir)
                            myfile.write('\n')
                        sleep(10)
                        if n == limit1 - 1:
                            print 'Limit reached, giving up'
            elif 'dialog' in t:
                dldir = '%s/%s' % (dialogseasondir, t1)
                for n in range(limit1):
                    try:
                        urllib.urlretrieve (t, dldir)
                        break
                    except:
                        print 'Download failed'
                        print t, dldir
                        with open(out_file2, "a") as myfile:
                            myfile.write(t)
                            myfile.write('\n')
                            myfile.write(dldir)
                            myfile.write('\n')
                        sleep(10)
                        if n == limit1 - 1:
                            print 'Limit reached, giving up'
            elif 'grammar' in t:
                dldir = '%s/%s' % (grammarseasondir, t1)
                for n in range(limit1):
                    try:
                        urllib.urlretrieve (t, dldir)
                        break
                    except:
                        print 'Download failed'
                        print t, dldir
                        with open(out_file2, "a") as myfile:
                            myfile.write(t)
                            myfile.write('\n')
                            myfile.write(dldir)
                            myfile.write('\n')
                        sleep(10)
                        if n == limit1 - 1:
                            print 'Limit reached, giving up'
            else:
                dldir = '%s/%s' % (lessonseasondir, t1)
                for n in range(limit1):
                    try:
                        urllib.urlretrieve (t, dldir)
                        break
                    except:
                        print 'Download failed'
                        print t, dldir
                        with open(out_file2, "a") as myfile:
                            myfile.write(t)
                            myfile.write('\n')
                            myfile.write(dldir)
                            myfile.write('\n')
                        sleep(10)
                        if n == limit1 - 1:
                            print 'Limit reached, giving up'
        url = '%s%s' % (ourl, postfix2)
        resume2 = loadrefresh(url)
        if resume2 == False:
            continue
        n = source.find('<td class="cell-checkbox">')
        resume = True
        count1 = 0
        while resume == True:
            count1 = count1 + 1
            n1 = source.find('<td class="cell-checkbox">', n + 26)
            if n1 == -1 or count1 >= limit:
                n1 = len(source)
                resume = False
            kana = re.findall(r'<span class="kana">?([^\<>]+)', source[n:n1])
            kanji = re.findall(r'<span class="term">?([^\<>]+)', source[n:n1])
            english = re.findall(r'<span class="english">?([^\<>]+)', source[n:n1])
            audio = re.findall(r'data-url="?([^\'"<>]+)', source[n:n1])
            if len(kana) > 0 and len(kanji) > 0 and len(english) > 0 and len(audio) > 0:
                vocabdldir = '%s%s' % (vocabdir, audio[0][62:])
                for n in range(limit1):
                    try:
                        urllib.urlretrieve (audio[0], vocabdldir)
                        break
                    except:
                        print 'Download failed'
                        print audio[0], vocabdldir
                        with open(out_file2, "a") as myfile:
                            myfile.write(audio[0])
                            myfile.write('\n')
                            myfile.write(vocabdldir)
                            myfile.write('\n')
                        sleep(10)
                        if n == limit1 - 1:
                            print 'Limit reached, giving up'
                t = '<span style="font-family: Liberation Sans; font-size: 40px;  ">%s</span>	<span style="font-family: Liberation Sans; font-size: 40px;  "><br>%s<br>[sound:%s]</span>	%s vocabulary English>Japanese' % (english[0], kana[0], audio[0][62:], driver.title[17:].replace(' ', '_'))
                with open(out_file, "a") as myfile:
                    myfile.write(t.encode('utf-8'))
                    myfile.write('\n')
                t = '<span style="font-family: Liberation Sans; font-size: 40px;  ">%s</span>	<span style="font-family: Liberation Sans; font-size: 40px;  "><br>%s<br>[sound:%s]</span>	%s vocabulary English>Japanese' % (english[0], kanji[0], audio[0][62:], driver.title[17:].replace(' ', '_'))
                with open(out_file1, "a") as myfile:
                    myfile.write(t.encode('utf-8'))
                    myfile.write('\n')
            n = n1
        url = '%s%s' % (ourl, postfix1)
        loadrefresh(url)
        if resume2 == False:
            continue
        n = source.find('<span class="lesson-container-tab ill-savonlinna ill-ease-color">All</span>')
        n1 = source.find('<div style="display: none;" class="lesson-lbl-transcript">')
        kanji = re.findall(r'<td class="ctext"><span class="clickable">?([^\<>]+)', source[n:n1])
        audio = re.findall(r'<span data-type="audio/mp3" data-url="?([^\'"<>]+)', source[n:n1])
        n = n1
        n1 = source.find('<div style="display: none;" class="lesson-lbl-transcript">', n + 58)
        english = re.findall(r'<td class="ctext"><span class="clickable">?([^\<>]+)', source[n:n1])
        n = source.find('<div style="display: none;" class="lesson-lbl-transcript">', n1 + 58)
        kana = re.findall(r'<td class="ctext"><span class="clickable">?([^\<>]+)', source[n:])
        for k, a, e, h in zip(kanji, audio, english, kana):
            count = count + 1
            z = 7 - len(str(count))
            audioname = '%s%s.mp3' % ('0' * z, count)
            vocabdldir = '%s%s' % (vocabdir, audioname)
            audiourl = '%s%s' % (audioprefix, a)
            for n in range(limit1):
                try:
                    urllib.urlretrieve (audiourl, vocabdldir)
                    break
                except:
                    print 'Download failed'
                    print audiourl, vocabdldir
                    with open(out_file2, "a") as myfile:
                        myfile.write(audiourl)
                        myfile.write('\n')
                        myfile.write(vocabdldir)
                        myfile.write('\n')
                    sleep(10)
                    if n == limit1 - 1:
                        print 'Limit reached, giving up'
            t = '<span style="font-family: Liberation Sans; font-size: 40px;  ">%s</span>	<span style="font-family: Liberation Sans; font-size: 40px;  "><br>%s<br>[sound:%s]</span>	%s dialogue Japanese_text>English' % (h, e, audioname, driver.title[17:].replace(' ', '_'))
            with open(out_file, "a") as myfile:
                myfile.write(t.encode('utf-8'))
                myfile.write('\n')
            t = '<span style="font-family: Liberation Sans; font-size: 40px;  ">Listen.[sound:%s]</span>	<span style="font-family: Liberation Sans; font-size: 40px;  "><br>%s<br>%s</span>	%s dialogue Japanese_audio>English' % (audioname, h, e, driver.title[17:].replace(' ', '_'))
            with open(out_file, "a") as myfile:
                myfile.write(t.encode('utf-8'))
                myfile.write('\n')
            t = '<span style="font-family: Liberation Sans; font-size: 40px;  ">%s</span>	<span style="font-family: Liberation Sans; font-size: 40px;  "><br>%s<br>[sound:%s]</span>	%s dialogue Japanese_text>English' % (k, e, audioname, driver.title[17:].replace(' ', '_'))
            with open(out_file1, "a") as myfile:
                myfile.write(t.encode('utf-8'))
                myfile.write('\n')
            t = '<span style="font-family: Liberation Sans; font-size: 40px;  ">Listen.[sound:%s]</span>	<span style="font-family: Liberation Sans; font-size: 40px;  "><br>%s<br>%s</span>	%s dialogue Japanese_audio>English' % (audioname, k, e, driver.title[17:].replace(' ', '_'))
            with open(out_file1, "a") as myfile:
                myfile.write(t.encode('utf-8'))
                myfile.write('\n')
print 'Count: %s' % count
with open(out_file2, "a") as myfile:
    myfile.write(str(count))
    myfile.write('\n')
