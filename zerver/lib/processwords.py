#!/usr/bin/env python3

from nltk.stem import PorterStemmer
import math
import re

ps = cw = sw = aliases = None
pwloaded = False

wordbreak = "pwwdbk"

cw_words = '''
unclear unhelpful anecdotally risky
mattgroh zulip github.com
'''

sw_words = '''
    i'm     i'll     i'd    i've
 you're   you'll   you'd  you've
           he'll    he'd            he's
          she'll   she'd           she's
           it'll    it'd            it's
  we're    we'll    we'd   we've
they're  they'll  they'd they've
         that'll  that'd that've  that's
          who'll   who'd  who've   who's
what're  what'll  what'd          what's
        where'll where'd         where's
         when'll  when'd          when's
          why'll   why'd           why's
          how'll   how'd           how's
        there'll there'd there've there's
         here'll here'd here've here's
it's
let's
isn't aren't wasn't weren't haven't hasn't hadn't won't wouldn't
don't doesn't didn't can't couldn't shouldn't mightn't mustn't
would've should've could've might've must've
c'mon

mon tue tues wed weds thu thur thurs fri sat sun
monday tuesday wednesday thursday friday saturday sunday
jan feb mar apr may jun jul aug sep oct nov dec
sorry nit said yet would
pls lol lolz fyi ha haha hah ah
image image.png image.jpg twitter.com
png jpg mp3 see top
2^22
threadgill sah ghausi dekorte
discussion forecast.chat
youtube reddit http
geos tech macro misc wild
2021 2022 2023 2024
yeah yea yah
know going think mises happen leak kind okay 
people thing like really mean actual look want time well talk
interest something year could make much market even sort come seem say
work print also money question start case right point good maybe take
around need still reason back problem world power bank call rate system
basic long virusmove data first death many pretty risk might state
invest idea thought vaccine sure price give use comment great effect
little less part probably feel course real another asset whale number
enough stream whatever example
'''

alias_words = '''
u.s US
u.s.a US
covid-19 covid
covid19 covid
coronavirus covid
russia's russia
russian russia
russians russia
'''

def processwords(text):
    global pwloaded, ps, cw, sw, aliases
    if not pwloaded:
        ps = PorterStemmer()

        cw = {}
        lineno = 0
        with open('zerver/lib/google-10000-english-usa.txt') as fh:
            while True:
                commonword = fh.readline()
                if not commonword:
                    break
                lineno += 1
                commonword = commonword.lower().strip()
                if commonword not in cw:
                    cw[commonword] = lineno
                stem = ps.stem(commonword)
                if stem not in cw:
                    cw[stem] = lineno
        print(f"found {len(cw)} common words.")
        for word in cw_words.strip().split():
            stem = ps.stem(word)
            if stem not in cw:
                cw[stem] = 1
            if word not in cw:
                cw[word] = 1

        sw = {}
        with open('zerver/lib/stopwords.txt') as fh:
            while True:
                stopword = fh.readline()
                if not stopword:
                    break
                stopword = stopword.lower().strip()
                sw[ps.stem(stopword)] = True
        sw.update({ps.stem(word):True for word in sw_words.strip().split()})
        print(f"found {len(sw)} stopwords.")

        aliases = dict(item.split() for item in alias_words.strip().split("\n"))
        print(f"found {len(aliases)} aliases.")
        pwloaded = True

    text = text.replace("\n", "").replace("\r", "")
    singlewords = []
    bigrams = []
    lastword = ""
    text = re.sub(r'@mention just signed up for Zulip.+?[(]total: [0-9]+[)]', '', text)
    knownwords = {}
    for word in re.split(r'[\s/\\]', text):
        if len(word) < 4 or len(word) > 12:
            continue
        word = word.lower()
        word = word.strip()
        # skip @mentions and #mentions
        if re.search(r'^(@|#)', word):
            continue
        word = re.sub(r'[^a-z0-9]+$', '', word)
        word = re.sub(r'^[^a-z0-9]+', '', word)
        # skip URLs
        if re.search(r'^https?://', word):
            continue
        word = aliases.get(word, word)
        stem = ps.stem(word)
#        print(f'{word} => {stem}')
        if stem in sw or word in sw:
#            print("ignoring {stem} / {word}: sw")
            continue
        if word == wordbreak:
            lastword = ""
#            print("ignoring {stem} / {word}: wordbreak")
            continue
        if (word in knownwords or 
            (len(word) >= 4 and len([c for c in word if c.isalpha()]) > 2)):
            knownwords[word] = True
            laststem = ps.stem(lastword)
            if lastword != "" and laststem != stem:
                bigram = lastword + " " + word
                # too much punctuation - no bigram for you
                if len([c for c in bigram if not c.isalnum()]) > 2:
                    continue
                if lastword != "" and (stem not in cw or laststem not in cw):                    
                    bigrams.append(bigram)
                    if stem not in cw:
                        bigrams.append(bigram)
                    if laststem not in cw:
                        bigrams.append(bigram)
            lastword = word
        # too much punctuation
        if len([c for c in word if not c.isalnum()]) > 1:
#            print("ignoring {stem} / {word}: 2+ puncts")
            continue
        singlewords.append(word)
    print(f"scanned {len(singlewords)} single words and {len(bigrams)} bigrams.")

    freq = {}
    for i, word in enumerate(singlewords):
        stem = ps.stem(word)
        key = stem if stem in freq else word
        # penalize older posts / boost more recent posts
        freq[key] = freq.get(key, 0.0) + math.log2(i+1) / math.log2(len(singlewords))
    
    for key in freq:
        if key in cw:
            freq[key] = freq[key] * (math.log(cw[key]) / math.log(10000))
#            print(f'{key} => {(math.log(cw[key]) / math.log(10000))}')
    top20 = dict(sorted(freq.items(), key=lambda r: r[1])[-100:])
    #print(top20)
    
    bgfreq = {}
    for keyword in bigrams:
        word1, word2 = keyword.split()
        if word1 in top20 and word2 in top20:
            freq[word1] += 1
            freq[word2] += 1
            continue
        rev = f"{word2} {word1}"
        if rev in bgfreq:
            bgfreq[rev] = bgfreq.get(rev, 0) +1
        else:
            bgfreq[keyword] = bgfreq.get(keyword, 0) +1
    
    for bigram, bgcnt in bgfreq.items():
        word1, word2 = bigram.split()
        wf1 = freq.get(word1, 0)
        wf2 = freq.get(word2, 0)
        if wf1 + wf2 < bgcnt:
            freq[bigram] = freq.get(bigram, 0) + bgcnt

    return freq


if __name__ == "__main__":
    # fetch alltext.txt from production /tmp/alltext.txt
    with open('alltext.txt') as fh:
        text = ""
        while True:
            line = fh.readline()
            if not line:
                break
            text += line
        freq = processwords(text)
        print('\n'.join(
            [ f"{v:3} {k}" for k,v in
              sorted(freq.items(), key=lambda r: r[1], reverse=True) ]
        ))

