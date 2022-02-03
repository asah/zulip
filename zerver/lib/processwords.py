#!/usr/bin/env python3

from nltk.stem import PorterStemmer
import re

ps = PorterStemmer()

cw = {}
with open('zerver/lib/google-10000-english-usa.txt') as fh:
    while commonword := fh.readline():
        commonword = commonword.lower().strip()
        cw[ps.stem(commonword)] = True
print(f"found {len(cw)} common words.")
cw.update({ps.stem(word):True for word in '''
unclear unhelpful anecdotally risky
mattgroh zulip github.com
'''.strip().split()})


sw = {}
with open('zerver/lib/stopwords.txt') as fh:
    while stopword := fh.readline():
        stopword = stopword.lower().strip()
        sw[ps.stem(stopword)] = True
sw.update({ps.stem(word):True for word in '''
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
'''.strip().split()})
print(f"found {len(sw)} stopwords.")

aliases = dict(item.split() for item in '''
u.s US
u.s.a US
covid-19 covid
covid19 covid
'''.strip().split("\n"))
print(aliases)

def processwords(text):
    text = text.replace("\n", "").replace("\r", "")
    singlewords = []
    bigrams = []
    lastword = ""
    text = re.sub(r'@mention just signed up for Zulip.+?[(]total: [0-9]+[)]', '', text)
    for word in re.split(r'[\s/\\]', text):
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
        # skip wasn't etc.
        if re.search(r'^[a-z]{2,6}n\'t$', word):
            continue
        word = aliases.get(word, word)
        stem = ps.stem(word)
        if stem in sw:
            continue
        if word == "wordbreak":
            lastword = ""
            continue
        if len(word) >= 4 and len([c for c in word if c.isalpha()]) > 2:
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
            continue
        if len(word) <= 4 or stem in cw:
            continue
        singlewords.append(word)

    freq = {}
    for word in singlewords:
        stem = ps.stem(word)
        if stem in freq:
            freq[stem] = freq.get(stem, 0) +1
        else:
            freq[word] = freq.get(word, 0) +1
    
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
        while line := fh.readline():
            text += line
        freq = processwords(text)
        print('\n'.join(
            [ f"{v:3} {k}" for k,v in
              sorted(freq.items(), key=lambda r: r[1], reverse=True) ]
        ))

