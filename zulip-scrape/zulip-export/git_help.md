# #git help

> Git, the GitHub platform & our git workflow/tooling.

Exported from https://chat.zulip.org on 2026-10-19: 1,342 messages in 153 topics.

## workflow guide

*2016-10-11 to 2016-10-18 · 4 messages · [open in Zulip](https://chat.zulip.org/#narrow/channel/44-git-help/topic/workflow.20guide/with/35924)*

**Christie Koehler** · 2016-10-11 17:58 UTC

We are working on a git guide for new contributors. You can read it here: http://zulip-ck.readthedocs.io/en/1754-docs-add-git-workflow/git-guide.html

I would love feedback and I am happy to answer your git-related questions here.

**Christie Koehler** · 2016-10-17 23:58 UTC

The workflow guide is now live! http://zulip.readthedocs.io/en/latest/git-guide.html

**Tim Abbott** · 2016-10-18 00:51 UTC

yay!  :sagittarius: (the only emoji with "git" in its name, apparently)

**Sumana Harihareswara** · 2016-10-18 00:56 UTC

@Christie Koehler You mentioned that there were a few comments you hadn't addressed in this PR, about git config parameters and useful aliases and so on. Mind making an issue so we remember to follow up and add those?


## Useful git tips

*2016-10-16 to 2016-10-19 · 3 messages · [open in Zulip](https://chat.zulip.org/#narrow/channel/44-git-help/topic/Useful.20git.20tips/with/39439)*

**Sumana Harihareswara** · 2016-10-16 17:56 UTC

I just learned about `git log -S` which shows you changes that have added or removed a particular string -- e.g., `git log -S json_rules` to find changes that might have touched a variable named "json_rules". [Hat-tip to Steve Howell.](https://zulip.tabbott.net/#narrow/stream/test.20suites/subject/watch.20over.20my.20shoulder.20as.20I.20improve.20the.20linter/near/39375)

**Tim Abbott** · 2016-10-16 18:42 UTC

Yeah `git log -S` is awesome :)

**Sumana Harihareswara** · 2016-10-19 13:36 UTC

Steve's starting a [git tip of the day topic](https://zulip.tabbott.net/#narrow/stream/general/subject/git.20tip.20of.20the.20day)!


## can't reach GitHub

*2016-10-21 to 2016-11-02 · 6 messages · [open in Zulip](https://chat.zulip.org/#narrow/channel/44-git-help/topic/can.27t.20reach.20GitHub/with/44471)*

**Sumana Harihareswara** · 2016-10-21 13:05 UTC

Hmm - I'm having trouble connecting to github.com. And Twitter is [down for everyone, it seems](http://downforeveryoneorjustme.com/twitter.com), so I can't reach https://twitter.com/githubstatus . Still, [GitHub is not down for everyone](http://downforeveryoneorjustme.com/github.com) so I'm trying to investigate.

If I try to ping github.com, I get: "ping: unknown host github.com". If I ssh to another machine and ping github.com, that works. But if I use an SSH tunnel to proxy my browser through that machine, I still can't get to github.com. I can go to 192.30.253.113 which then tries to redirect me to https://github.com which still gives me "Firefox can't find the server at github.com" and which -- even when I disable HTTPS Everywhere -- tries to go specifically to https://github.com.

**Sumana Harihareswara** · 2016-10-21 13:16 UTC

It was an upstream DNS problem for GitHub. I haven't clicked on this link https://techcrunch.com/2016/10/21/many-sites-including-twitter-and-spotify-suffering-outage/ but I saw a preview via a Slack card/expansion:

> A number of popular sites and services are down right now for many users, including Twitter, SoundCloud, Spotify and Shopify. The cause appears to be a sweeping outage of DNS provider Dyn, as a result of a DDOS attack, according to a post on Hacker News. We’re tracking the outage and will let you know if we discover anything further about outage length, cause or sites affected. Other sites experiencing issues include Github, Airbnb, Reddit, Freshbooks, Heroku and Vox Media properties.

**Sumana Harihareswara** · 2016-11-02 18:03 UTC

@Tim Abbott Do we have a backup repo someplace that's not GitHub, that we could switch to following in the case of a prolonged GitHub outage? Like, git.zulip.org or GitLab?

**Tim Abbott** · 2016-11-02 18:05 UTC

Well, every Zulip developer has complete history on their laptop, and it takes a few hours to setup a GitLab or whatever server, so that's the default backup plan

**Tim Abbott** · 2016-11-02 18:05 UTC

While issues/PRs aren't included in that, I think we can probably count on GitHub to not permanently lose all that data

**Sumana Harihareswara** · 2016-11-02 18:06 UTC

Fair enough, thanks


## where was a commit merged from?

*2017-01-26 to 2017-01-26 · 5 messages · [open in Zulip](https://chat.zulip.org/#narrow/channel/44-git-help/topic/where.20was.20a.20commit.20merged.20from.3F/with/137861)*

**Sumana Harihareswara** · 2017-01-26 18:03 UTC

How can I tell that https://github.com/zulip/zulip/commit/7de45951e24d64cd99038bd8cab56c4cea3d6dd6 is related to https://github.com/zulip/zulip/pull/2417 ? What should I be looking for in order to find that connection?

**Tim Abbott** · 2017-01-26 18:04 UTC

There's no real way to tell

**Sumana Harihareswara** · 2017-01-26 18:12 UTC

So if an admin merges a single commit from a PR but leaves others unmerged, there is no way for us to find "here's a commit that used to be part of this PR but has already been merged" -- correct?

**Tim Abbott** · 2017-01-26 18:16 UTC

correct

**Sumana Harihareswara** · 2017-01-26 18:17 UTC

:\ thanks.


## getting merge commits out of a PR

*2017-03-17 to 2021-10-28 · 22 messages · [open in Zulip](https://chat.zulip.org/#narrow/channel/44-git-help/topic/getting.20merge.20commits.20out.20of.20a.20PR/with/172404)*

**Sumana Harihareswara** · 2017-03-17 16:28 UTC

@Jeremy Philemon hey, figured this might be a nicer place to talk about https://github.com/zulip/zulip/pull/4096 (rather than #**frontend** )

**Sumana Harihareswara** · 2017-03-17 16:29 UTC

To continue [the conversation](https://chat.zulip.org/#narrow/stream/frontend/topic/CSS.20Fix):

**Sumana Harihareswara** · 2017-03-17 16:29 UTC

so I'm looking at https://github.com/zulip/zulip/pull/4096/commits

**Sumana Harihareswara** · 2017-03-17 16:31 UTC

and I'm looking at https://zulip.readthedocs.io/en/latest/git-guide.html#keep-your-fork-up-to-date

**Sumana Harihareswara** · 2017-03-17 16:33 UTC

You said:

> I wanted to do an interactive rebase to squash the merge commits, but the merge commits weren't listed in the commit history so I went on and performed the normal rebase...

So when you run `git log` in your branch `regform-smaller-screen-responsive`, and compared to when you run `git log` in the master branch, the only two differences you see are "Fixed a linting error" and "Tweaked css to make registration form responsive on <495px screen width"?

**Tim Abbott** · 2017-03-17 17:27 UTC

It's not possible to squash merge commits; if you just do a `git rebase upstream/master` they will usually disappear, which is probably what you want.

**Sumana Harihareswara** · 2017-03-17 17:27 UTC

aha

**Sumana Harihareswara** · 2017-03-17 17:28 UTC

so I'm wondering whether the issue is a rebase in the wrong direction, or something

**Jeremy Philemon** · 2017-03-17 20:29 UTC

@Sumana Harihareswara I seem to have rebased it properly after following @Tim Abbott 's message! :D

**Sumana Harihareswara** · 2017-03-17 20:33 UTC

Apologies for getting the wrong end of the stick earlier, Jeremy

**Jeremy Philemon** · 2017-03-17 21:07 UTC

@Sumana Harihareswara That's alright :)

**Ayush Jain** · 2017-03-19 12:38 UTC

I also faced same problem but above solution worked, thanks

**Ngulefac Benazea** · 2021-10-26 21:33 UTC

Hello please I need help with this. I was told to open a PR for an issue I fixed and I did here https://github.com/zulip/zulip-mobile/pull/5078 , but now a merge commit was observed there and I have to fix the branch. Please what can I do ? 

I have never come across such. Neither have I seen clearly what to do online. Though I created a branch before doing my changes..so I don't know where a merge commit is form. Please help

**Greg Price** · 2021-10-26 21:36 UTC

Sure. Take a look at this section of our docs, which may help:
https://zulip.readthedocs.io/en/latest/git/troubleshooting.html#undo-a-merge-commit

**Greg Price** · 2021-10-26 21:37 UTC

Do also set up `gitk` or another graphical Git viewer, if you haven't already:
https://zulip.readthedocs.io/en/latest/git/setup.html#get-a-graphical-client

That will give you a better view of what's in your branch, and what happens as you make changes.

**Greg Price** · 2021-10-26 21:39 UTC

Hmm, also, looking at that PR it looks like you've already removed the merge commit! The new revision you pushed (commit 5b460300a, about 26 minutes ago), doesn't contain any merge commits.

**Greg Price** · 2021-10-26 21:40 UTC

I definitely recommend using a graphical Git viewer. It will help a lot in seeing exactly what's actually happening in your branch :smile:

**Ngulefac Benazea** · 2021-10-28 06:41 UTC

I push the changes to this same PR https://github.com/zulip/zulip-mobile/pull/5078
Please I'll really need more direction and help on how to resolve merge commits. The concept isn't still clear for me

**Chris Bobbe** · 2021-10-28 19:11 UTC

(@Ngulefac Benazea I've just moved your question here, from [here](https://chat.zulip.org/#narrow/stream/48-mobile/topic/.23M4851.2FMove.20top.20navigation.20bar.20into.20top.20left.20menu/near/1273379). :smile:)

**Chris Bobbe** · 2021-10-28 19:12 UTC

I don't see any merge commits in your current revision for #M5078, at zulip/zulip-mobile@5b460300a.

**Chris Bobbe** · 2021-10-28 19:14 UTC

We're happy to help with more specific problems you run into, and questions you have, while you try to follow Greg's advice above. This could help us improve our documentation. :smile:

**Ngulefac Benazea** · 2021-10-28 21:24 UTC

Alright Thank you @Chris Bobbe , I will follow your instruction here and on the PR comments to resolve the issues you pointed out


## git add

*2017-03-22 to 2017-03-22 · 5 messages · [open in Zulip](https://chat.zulip.org/#narrow/channel/44-git-help/topic/git.20add/with/177137)*

**Joshua Pan** · 2017-03-22 22:08 UTC

Discuss different options of `git add`, which ones you use, and why you use it

**Joshua Pan** · 2017-03-22 22:09 UTC

I usually use `git add -u` which updates all tracked files.

**Tim Abbott** · 2017-03-22 22:11 UTC

I use mostly that and `git add -p` if I want to split a file

**Joshua Pan** · 2017-03-22 22:11 UTC

I didn't know about `git add -p` until today, thanks to @Sumana Harihareswara. It's really useful

**Joshua Pan** · 2017-03-22 22:12 UTC

I should definitely go through more git command options and vim commands to improve my work productivity.


## reorder history

*2017-03-28 to 2017-03-29 · 5 messages · [open in Zulip](https://chat.zulip.org/#narrow/channel/44-git-help/topic/reorder.20history/with/180478)*

**Rishi Gupta** · 2017-03-28 23:23 UTC

For PRs with many commits, it can be somewhat confusing as a reviewer when you can't see them in the correct order on github. What would folks think of a tool that just rewrote the timestamps of all the commits on your branch between HEAD and master? E.g. the k'th parent of HEAD could have the timestamp `now() - k hours`.

**Steve Howell** · 2017-03-28 23:27 UTC

I'd be interested in that, since I don't think people generally care whether I did something at 3am in the morning vs. 4pm in the afternoon, as long as the basic timeframe is accurate.

**Tim Abbott** · 2017-03-29 19:19 UTC

Sigh, this is really just a bug in GitHub -- there's a simple topological sort algorithm that was just do this correctly.  There's a long sad thread where Anders is trying to convince the engineers at GitHub as well as random confused people of this.

**Tim Abbott** · 2017-03-29 19:19 UTC

I tend to just fetch the commits and read them in `gitk`; I think a tool of that form would be reasonable, but of course it's hard to make sure people use it.

**Steve Howell** · 2017-03-29 19:45 UTC

Yeah, likewise, most PRs are short enough that if they're out of order, it's not super confusing, and for longer ones, I tend to fetch them.


## looking through history

*2017-04-02 to 2017-04-02 · 1 messages · [open in Zulip](https://chat.zulip.org/#narrow/channel/44-git-help/topic/looking.20through.20history/with/183446)*

**Sumana Harihareswara** · 2017-04-02 14:51 UTC

`git grep idea` searches a code repository's code and comments for the word "idea", `git log --grep="idea"` searches the commit history for times we've used the word "idea" in a commit message, and `git blame codefile.py` shows you who last changed every line of that codefile, and when.

@Tejas Kasetty because of the recent conversation in #**frontend**


## collaborate on a branch

*2017-04-06 to 2017-04-06 · 1 messages · [open in Zulip](https://chat.zulip.org/#narrow/channel/44-git-help/topic/collaborate.20on.20a.20branch/with/185554)*

**Sumana Harihareswara** · 2017-04-06 16:01 UTC

[question](https://chat.zulip.org/#narrow/stream/documentation/topic/collaborate.20on.20a.20branch)


## submodules

*2017-04-10 to 2017-04-12 · 17 messages · [open in Zulip](https://chat.zulip.org/#narrow/channel/44-git-help/topic/submodules/with/187070)*

**Andrea  Longo** · 2017-04-10 16:27 UTC

The Swagger UI folks suggest using git submodules to get the code from their project for the Swagger API docs to work. The latest version no longer contains all the necessary dependancies when installed by npm because they assume you will be building it.

**Andrea  Longo** · 2017-04-10 16:27 UTC

They are reconsidering this based on feedback, but for the moment this is the situation.

**Andrea  Longo** · 2017-04-10 16:28 UTC

Are submodules something that would be reasonable to do for Zulip? It looks like it's possible to get a specific version (based on a tag) although I don't know all the details.

**Andrea  Longo** · 2017-04-10 16:31 UTC

My preference is to go back to the previous situation, where npm would install all the necessary stuff. Some other people agree, so perhaps that will happen. But if it doesn't, then I have to consider the submodules option. It seems like it would be complicated, as it would "sorta" add the other project's repo to Zulip's. I think.

**Andrea  Longo** · 2017-04-10 16:31 UTC

Any opinions on this?

**Andrea  Longo** · 2017-04-10 16:33 UTC

Here are some issues where this is being discussed:
[Plans for publishing package with built assets?](https://github.com/swagger-api/swagger-ui/issues/2758)
[swagger-editor-bundle file is not in npm](https://github.com/swagger-api/swagger-editor/issues/1235)

**Sumana Harihareswara** · 2017-04-10 21:50 UTC

@Steve Howell you have any opinions here? I don't know when Tim'll be back from his vacation to opine....

**Steve Howell** · 2017-04-10 22:03 UTC

I don't have experience using submodules, but I have heard that they are generally considered not worth the effort for most tasks.

**Andrea  Longo** · 2017-04-10 22:26 UTC

@Sumana Harihareswara @Steve Howell What I'm reading online is pretty much "Great for a few specific cases, a world of pain for anything else." The idea of embedding an unrelated repo into your own seems like it would confuse people not very familiar with the architecture.

**Andrea  Longo** · 2017-04-10 22:27 UTC

I hope they choose another option, one suggestion was a separate package of just the one directory needed for non-customized use.

**Andrea  Longo** · 2017-04-10 22:29 UTC

The've already broken up the previous single package into swagger-ui and swagger-client (and I've not figured out what purpose it serves.)

**Tim Abbott** · 2017-04-11 22:36 UTC

I'm pretty down on submodules, but I suppose they could be usable for something we only change with a provision.

**Tim Abbott** · 2017-04-11 22:36 UTC

The UI is terrible, and it often gets into states that are hard to debug unless you're an expert on them, which very few people are

**Boris Yankov** · 2017-04-11 22:40 UTC

Good intent behind submodules, but the tendency is in the exact opposite. Both Google and Facebook are using a mono-repo.

**Tim Abbott** · 2017-04-11 22:49 UTC

I actually the person was responsible for moving Dropbox to a monorepo

**Tim Abbott** · 2017-04-11 22:50 UTC

I think Google and Facebook are special cases, because they use Perforce and similar tools to avoid ever checking the whole thing out.  If you only have a few MLOC, it's actually better to just have a single Git repo.

**Andrea  Longo** · 2017-04-12 00:07 UTC

I'll monitor the situation. They seem interested in a solution that works similar to the old way, now that they know people were using it. I'm not super excited at the prospect of submodules either.


## git squash question

*2017-04-11 to 2017-04-11 · 6 messages · [open in Zulip](https://chat.zulip.org/#narrow/channel/44-git-help/topic/git.20squash.20question/with/187178)*

**Vaida Plankyte** · 2017-04-11 10:08 UTC

so i've been working on this PR: https://github.com/zulip/zulip/pull/4375
but i've been having problems with trying to squash the commits. i was working not on a separate branch but on master-- so my commits are a bit all over the place. i've tried `git rebase -i` and reordering the commits & squashing them into one, but then i am unable to push because `Updates were rejected because the tip of your current branch is behind its remote counterpart.` pulling the changes puts me back to my original situation. 
i've only used the basics of git up to now so this is really confusing to me! would appreciate help :)

**Vishnu KS** · 2017-04-11 10:10 UTC

Once you squash them appropriately use `git push origin master --force`. It should do the job :)

**Vaida Plankyte** · 2017-04-11 10:11 UTC

will try right now, thanks!!

**Vishnu KS** · 2017-04-11 10:11 UTC

The --force flag replaces the remote repo with your local repo.

**Vaida Plankyte** · 2017-04-11 10:18 UTC

worked, thanks a bunch VIshnu :D

**Vishnu KS** · 2017-04-11 10:18 UTC

Cool :)


## Checkout a PR locally

*2017-04-12 to 2017-04-12 · 2 messages · [open in Zulip](https://chat.zulip.org/#narrow/channel/44-git-help/topic/Checkout.20a.20PR.20locally/with/187668)*

**Akash** · 2017-04-12 20:01 UTC

`git fetch origin pull/123/head:123`
`git checkout 123`

```sh
function pullpr() {
	git fetch origin pull/$1/head:$1;
	git checkout $1;
}
```
use `pullpr 123` to check any PR locally..sometimes useful :)

**Akash** · 2017-04-12 20:07 UTC

Whopps..it should be in https://chat.zulip.org/#narrow/stream/git/subject/Useful.20git.20tips


## Reverting multiple commits  in a branch

*2017-04-16 to 2017-04-16 · 22 messages · [open in Zulip](https://chat.zulip.org/#narrow/channel/44-git-help/topic/Reverting.20multiple.20commits.20.20in.20a.20branch/with/188625)*

**Lalu Prasad Lenka** · 2017-04-16 06:29 UTC

I have an open PR [#134](https://github.com/zulip/zulip-electron/pull/134) in Zulip-electron, which is still under review.
I did a blunder :anguished: by directly opening a Pull request from my master branch.

Now I want to work on a different issue but if I create a new branch(for issue [#126](https://github.com/zulip/zulip-electron/issues/126)) it will have commits(related to PR [#134](https://github.com/zulip/zulip-electron/pull/134)) from my `origin master` which are not in Zulip-elelctron `upstream master` and  I don't want these commits because it  should not be in there in the PR for issue #126.

Any suggestions on how can I start working on a new branch for a different issue?

**Joshua Pan** · 2017-04-16 06:35 UTC

Easiest way is to push your master branch onto a new feature branch. close your current PR and open a new one.

**Joshua Pan** · 2017-04-16 06:36 UTC

Then reset --hard your master branch to upstream/master.

**Joshua Pan** · 2017-04-16 06:44 UTC

@Lalu Prasad Lenka Does that help?

**Lalu Prasad Lenka** · 2017-04-16 06:47 UTC

Thanks ! @Joshua Pan  
Yes closing the PR makes sense but I wanted to avoid that since I mentioned that PR in my GSoC proposal :confused: and it has a good amount of discussion and positive feedback in comments.

**Lalu Prasad Lenka** · 2017-04-16 06:48 UTC

Is there any way to  reset --hard my new feature_branch to upstream/master?

**Joshua Pan** · 2017-04-16 06:57 UTC

What do you mean reset --hard your new feature_branch? @Lalu Prasad Lenka

**Joshua Pan** · 2017-04-16 06:58 UTC

And just make sure to reference the new PR on your old PR. That should take care of any discrepancies.

**Joshua Pan** · 2017-04-16 06:59 UTC

Currently, what is on your new feature_branch?

**Lalu Prasad Lenka** · 2017-04-16 07:00 UTC

Currently my feature_branch is equal to `origin master`

**Joshua Pan** · 2017-04-16 07:00 UTC

Ohhh, I see what you are trying to do.

**Joshua Pan** · 2017-04-16 07:01 UTC

Keep the master branch with your PR.

**Joshua Pan** · 2017-04-16 07:01 UTC

Then create a new feature_branch and reset --hard to upstream/master.

**Joshua Pan** · 2017-04-16 07:01 UTC

Run the command `reset --hard upstream/master`.

**Lalu Prasad Lenka** · 2017-04-16 07:01 UTC

Exactly! @Joshua Pan

**Joshua Pan** · 2017-04-16 07:02 UTC

Yea, then the above commands should work. Tell me if they don't!

**Lalu Prasad Lenka** · 2017-04-16 07:08 UTC

I did this `git fetch upstream`
then `git reset --hard upstream/master`

It worked!
`git reset --hard upstream/master
HEAD is now at 85e7b33 Fixing travis test [WIP]
`


What should I do next to push these changes online?


`git push -f origin feature_branch`?

**Joshua Pan** · 2017-04-16 07:09 UTC

Yea, then it's just normal pushing feature_branch.

**Lalu Prasad Lenka** · 2017-04-16 07:14 UTC

Yayy!:grin::grin::grin::grin:
worked like a charm! 

Thanks a ton! @Joshua Pan  .
Now I can work on issue [#126](https://github.com/zulip/zulip-electron/issues/126).

**Joshua Pan** · 2017-04-16 07:14 UTC

No problem :)

**Akash** · 2017-04-16 18:28 UTC

@Joshua Pan thanks for helping him out :folded_hands:

**Joshua Pan** · 2017-04-16 21:42 UTC

@Akash Nimare no problem. My pleasure :)


## fetching someone's PR

*2017-04-21 to 2017-04-21 · 7 messages · [open in Zulip](https://chat.zulip.org/#narrow/channel/44-git-help/topic/fetching.20someone.27s.20PR/with/191228)*

**Sumana Harihareswara** · 2017-04-21 20:23 UTC

Was ssh'd into my Vagrant installation, which doesn't have my SSH credential on it. `tools/fetch-rebase-pull-request` gave me a public key error, but adding the remote, fetching, and then checking out the branch went fine. Did I do something wrong?

~~~
(zulip-venv)vagrant@vagrant-base-trusty-amd64:~/zulip$ cat .git/config 
[core]
	repositoryformatversion = 0
	filemode = true
	bare = false
	logallrefupdates = true
[remote "origin"]
	url = git@github.com:brainwane/zulip.git
	fetch = +refs/heads/*:refs/remotes/origin/*
[branch "master"]
	remote = origin
	merge = refs/heads/master
[remote "upstream"]
	url = git@github.com:zulip/zulip.git
	fetch = +refs/heads/*:refs/remotes/upstream/*
[gui]
	wmstate = normal
	geometry = 844x550+535+71 189 188
(zulip-venv)vagrant@vagrant-base-trusty-amd64:~/zulip$ tools/fetch-rebase-pull-request 4243
+ git diff-index --quiet HEAD
+ request_id=4243
+ remote=upstream
+ git fetch upstream pull/4243/head
Permission denied (publickey).
fatal: Could not read from remote repository.

Please make sure you have the correct access rights
and the repository exists.
(zulip-venv)vagrant@vagrant-base-trusty-amd64:~/zulip$ git remote add tommyip https://github.com/tommyip/zulip.git
(zulip-venv)vagrant@vagrant-base-trusty-amd64:~/zulip$ git fetch tommyip
remote: Counting objects: 261, done.
remote: Compressing objects: 100% (9/9), done.
remote: Total 261 (delta 203), reused 201 (delta 201), pack-reused 50
Receiving objects: 100% (261/261), 69.76 KiB | 0 bytes/s, done.
Resolving deltas: 100% (208/208), completed with 185 local objects.
From https://github.com/tommyip/zulip
 * [new branch]      arch_vis   -> tommyip/arch_vis
 * [new branch]      bot-howdoi -> tommyip/bot-howdoi
 * [new branch]      check-js-dep -> tommyip/check-js-dep
 * [new branch]      contrib_vis -> tommyip/contrib_vis
 * [new branch]      dedup_test -> tommyip/dedup_test
 * [new branch]      dockerize-bots -> tommyip/dockerize-bots
 * [new branch]      docs-admins -> tommyip/docs-admins
 * [new branch]      docs-keyboard-shortcut -> tommyip/docs-keyboard-shortcut
 * [new branch]      feature-highlight-bot -> tommyip/feature-highlight-bot
 * [new branch]      feature-limit-bot -> tommyip/feature-limit-bot
 * [new branch]      fix-popover -> tommyip/fix-popover
 * [new branch]      hot-fix    -> tommyip/hot-fix
 * [new branch]      lint-commit -> tommyip/lint-commit
 * [new branch]      master     -> tommyip/master
 * [new branch]      optimize-test-management -> tommyip/optimize-test-management
 * [new branch]      sort-import -> tommyip/sort-import
 * [new branch]      uglifyjs2  -> tommyip/uglifyjs2
 * [new branch]      unbundling-plotly -> tommyip/unbundling-plotly
 * [new branch]      vuejs      -> tommyip/vuejs
(zulip-venv)vagrant@vagrant-base-trusty-amd64:~/zulip$
~~~

**Sumana Harihareswara** · 2017-04-21 20:25 UTC

Currently we don't tell people to put their ssh credential onto the Vagrant guest in our dev env docs

**Joshua Pan** · 2017-04-21 20:29 UTC

Usually, I don't run any of my commands in my VM.

**Joshua Pan** · 2017-04-21 20:30 UTC

Except some of the `./tools/` commands that have to be in a VM.

**Tim Abbott** · 2017-04-21 20:35 UTC

Generally it's best to run Git commands outside the VM, for perf reasons if nothing else

**Tim Abbott** · 2017-04-21 20:36 UTC

This seems potentially hard to provide a better error message for.

**Sumana Harihareswara** · 2017-04-21 20:38 UTC

maybe edit https://zulip.readthedocs.io/en/latest/git-guide.html#fetch-a-pull-request-and-rebase to say "not in the vm"


## forcing local branch to match remote

*2017-05-31 to 2017-05-31 · 8 messages · [open in Zulip](https://chat.zulip.org/#narrow/channel/44-git-help/topic/forcing.20local.20branch.20to.20match.20remote/with/214874)*

**Andrea  Longo** · 2017-05-31 16:19 UTC

I have and old dev environment where I want to test something with the current version of a branch. The contents of the remote branch are correct, but when I try to update the local one I'm not getting the correct version. I've tried reset --hard and renaming/creating new but I still only get the old content.

**Andrea  Longo** · 2017-05-31 16:19 UTC

I could do it if I rebase, but I don't want to because it's got several annoying conflicts. And the remote branch already has that taken care of.

**Andrea  Longo** · 2017-05-31 16:20 UTC

How should this work? I don't understand why reset --hard didn't change anything.

**Robert Hönig** · 2017-05-31 16:22 UTC

With `reset --hard`, do you mean a `git fetch origin`, followed by a `git reset --hard origin/your-branch`?

**Andrea  Longo** · 2017-05-31 16:22 UTC

I did git fetch upstream, but yes.

**Andrea  Longo** · 2017-05-31 16:23 UTC

But now I've done it again with just git fetch and it works?

**Robert Hönig** · 2017-05-31 16:23 UTC

Cool :))

**Andrea  Longo** · 2017-05-31 16:29 UTC

Git has given me more trouble with multiple dev machines than other systems I've used. Like it doesn't seem to have a sense of designating an authoritative source. But I appear to have it now. Awesome.


## view old commit

*2017-06-03 to 2017-06-03 · 10 messages · [open in Zulip](https://chat.zulip.org/#narrow/channel/44-git-help/topic/view.20old.20commit/with/218177)*

**Abhijeet Kaur** · 2017-06-03 22:38 UTC

I have had half of my commits in a PR merged already (about a month back). I have the commit name: 78e5996877bb90766d51c087d6fb103042565b0b
I wish to look up the code that was merged in this commit (I think there was some unnecessary change there).

**Abhijeet Kaur** · 2017-06-03 22:39 UTC

Oh, posting it here, got me the link to the commit :relieved:

**Tommy Ip** · 2017-06-03 22:40 UTC

The commit is rebased so the SHA is no longer the same

**Abhijeet Kaur** · 2017-06-03 22:41 UTC

Ohh..!!

**Abhijeet Kaur** · 2017-06-03 22:41 UTC

I think then, I should just check up commit history with my author name. That would be a better option.

**Tommy Ip** · 2017-06-03 22:42 UTC

yeah
If you have the commit hash, you can use `git show <sha>` to view it locally

**Joshua Pan** · 2017-06-03 22:42 UTC

You'd have to grab that commit from your forked repo I think

**Joshua Pan** · 2017-06-03 22:42 UTC

(not from zulip/zulip)

**Tim Abbott** · 2017-06-03 22:44 UTC

Techniques like `git log --author=Abhijeet zerver/views/messages.py`  can find this sort of thing really fast

**Abhijeet Kaur** · 2017-06-03 22:47 UTC

Thank you, everyone! :)


## starting

*2017-06-09 to 2017-06-09 · 11 messages · [open in Zulip](https://chat.zulip.org/#narrow/channel/44-git-help/topic/starting/with/223370)*

**PDX Cloud Associates** · 2017-06-09 20:50 UTC

Hi I'm going to make my own dev server.  After I finish getting it set up, to start working on Zulip from this branch: djangopdx:may24-new-chggetuserfn   how do i do that?  I am assuming that i should not clone it.  I should pull it?  what is the exact git command ?

**Vishnu KS** · 2017-06-09 20:52 UTC

you should first clone your repository 
`git clone https://github.com/djangopdx/zulip`
Then you can checkout to your branch to start working on it.
`git checkout may24-new-chggetuserfn`

**PDX Cloud Associates** · 2017-06-09 20:53 UTC

got it thanks Vishnu

**Joshua Pan** · 2017-06-09 20:53 UTC

Does `git fetch origin` then `git checkout may24-new-chggetuserfn` work @Vishnu Ks ?

**Vishnu KS** · 2017-06-09 20:55 UTC

I am not sure whether he has already cloned the zulip repository or a fork

**PDX Cloud Associates** · 2017-06-09 20:55 UTC

nothing yet

**Vishnu KS** · 2017-06-09 20:55 UTC

@PDX Cloud Associates Then you should just follow the instructions I told :)

**PDX Cloud Associates** · 2017-06-09 20:59 UTC

thanks i'm going to make a ubuntu EC2 right now and follow the instructions then follow your instructions.

**Vishnu KS** · 2017-06-09 21:01 UTC

@PDX Cloud Associates It's not necessary to setup a remote dev environment. You can always run a vagrant machine on your computer.

**Vishnu KS** · 2017-06-09 21:01 UTC

http://zulip.readthedocs.io/en/latest/dev-overview.html

**PDX Cloud Associates** · 2017-06-09 21:17 UTC

@Vishnu Ks yes i know, thanks for that.  i feel more comfortable this way.


## deleted file problem

*2017-06-15 to 2017-06-15 · 15 messages · [open in Zulip](https://chat.zulip.org/#narrow/channel/44-git-help/topic/deleted.20file.20problem/with/228176)*

**Vaida Plankyte** · 2017-06-15 10:33 UTC

i have not made changes to `docs/code-of-conduct.md`, but i believe some changes have been made that have moved it around-- i can't figure out how to fix it as showing up as a deletion, as there seems to still be a file in upstream. help would be very appreciated :')
```
Vaida@DESKTOP-UV0SHQ7 MINGW64 ~/Github/zulip (master)
$ git fetch upstream
remote: Counting objects: 23, done.
remote: Compressing objects: 100% (10/10), done.
remote: Total 23 (delta 13), reused 14 (delta 12), pack-reused 1
Unpacking objects: 100% (23/23), done.
From https://github.com/zulip/zulip
   11a7a476d..7950f82f2  master     -> upstream/master

Vaida@DESKTOP-UV0SHQ7 MINGW64 ~/Github/zulip (master)
$ git rebase upstream/master
Cannot rebase: You have unstaged changes.
Please commit or stash them.

Vaida@DESKTOP-UV0SHQ7 MINGW64 ~/Github/zulip (master)
$ git status
On branch master
Your branch is ahead of 'origin/master' by 2 commits.
  (use "git push" to publish your local commits)
Changes not staged for commit:
  (use "git add/rm <file>..." to update what will be committed)
  (use "git checkout -- <file>..." to discard changes in working directory)

        deleted:    docs/code-of-conduct.md

no changes added to commit (use "git add" and/or "git commit -a")

Vaida@DESKTOP-UV0SHQ7 MINGW64 ~/Github/zulip (master)
$ git reset --hard upstream/master
HEAD is now at 7950f82f2 realm_emoji: Make sure that a deactivated realm emoji can't be used.

Vaida@DESKTOP-UV0SHQ7 MINGW64 ~/Github/zulip (master)
$ git status
On branch master
Your branch is ahead of 'origin/master' by 5 commits.
  (use "git push" to publish your local commits)
Changes not staged for commit:
  (use "git add/rm <file>..." to update what will be committed)
  (use "git checkout -- <file>..." to discard changes in working directory)

        deleted:    docs/code-of-conduct.md

no changes added to commit (use "git add" and/or "git commit -a")
```

**Robert Hönig** · 2017-06-15 10:38 UTC

Have you tried `git checkout -- docs/code-of-conduct.md`?

**Vaida Plankyte** · 2017-06-15 10:39 UTC

just tried it-- both that command and `git stash` still give me a `deleted:` after i run git status.

**Tim Abbott** · 2017-06-15 10:41 UTC

it changed from a file to a symlink.

**Tim Abbott** · 2017-06-15 10:41 UTC

@Vaida Plankyte are you on Windows?  On Windows, symlinks can't be created except by an administrator, and that could be involved

**Vaida Plankyte** · 2017-06-15 10:47 UTC

spot-on: wasn't running git BASH as an administrator. thanks!!

**Tim Abbott** · 2017-06-15 10:48 UTC

I wonder if there's a way we can make it more visibly a problem that one is not running as an administrator

**Tim Abbott** · 2017-06-15 10:49 UTC

I feel like that's the sources of >75% of Windows-specific development problems.

**Robert Hönig** · 2017-06-15 10:50 UTC

Agreed, I even set my terminal to start with administrative rights by default.

**Vaida Plankyte** · 2017-06-15 10:50 UTC

hm, we could emphasise parts of `git-guide.md` and the development install guide to mention the need to always run as administrator?

**Vaida Plankyte** · 2017-06-15 10:52 UTC

and point to how to set it up so it runs with administrative rights as @Robert Hönig inspired me to do :D

**Tim Abbott** · 2017-06-15 10:53 UTC

Yeah, we should explain that.  Probably should be in the "setup development" instructions for Windows as a called-out step.

**Tim Abbott** · 2017-06-15 10:53 UTC

(maybe needs to appear in both places with one as a link to the other)

**Vaida Plankyte** · 2017-06-15 10:54 UTC

i'll take care of that!

**Vaida Plankyte** · 2017-06-15 13:52 UTC

submitted #5408.


## fetch branch

*2017-06-19 to 2017-06-19 · 12 messages · [open in Zulip](https://chat.zulip.org/#narrow/channel/44-git-help/topic/fetch.20branch/with/231485)*

**Vaida Plankyte** · 2017-06-19 14:13 UTC

in the [docs](http://zulip.readthedocs.io/en/latest/git-guide.html#fetch-another-contributor-s-branch), the command given to check out someone's branch is `git checkout -b <username>-<branchname>`.  shouldn't it be `username/branchname`?

**Vaida Plankyte** · 2017-06-19 14:14 UTC

might also be useful to add the command `git checkout -b custombranchname username/branchname`, just to give people the option to rename the branch.

**Tommy Ip** · 2017-06-19 14:36 UTC

There is a script in `/tools`to fetch other's branches

**Vaida Plankyte** · 2017-06-19 14:46 UTC

ah, that too should be included. is it `tools/fetch-rebase-pull-request`?

**Tommy Ip** · 2017-06-19 14:46 UTC

yeah, I guess we should just replace the manual instruction to the script

**Vaida Plankyte** · 2017-06-19 14:48 UTC

i'd say it's important to keep the non-tools command, in case people run into problems such as not realising they're not inside the VM/they're not using vagrant/don't have ssh set up inside the VM

**Tommy Ip** · 2017-06-19 14:49 UTC

ok that's fair, i guess we should have them both in

**Vaida Plankyte** · 2017-06-19 14:49 UTC

cool! i'll PR it. am i correct with the fact that the dash should be replaced by a slash in the original code snippet?

**Tommy Ip** · 2017-06-19 14:51 UTC

yeah I think so

**Vaida Plankyte** · 2017-06-19 14:51 UTC

cool, thanks!

**Rohitt Vashishtha** · 2017-06-19 14:57 UTC

@Vaida Plankyte the scripts `tools/fetch-rebase-pull-request` and `tools/fetch-pull-request` do not need you to be in Vagrant environment. They just ensure that you don't have any uncommitted changes that could be overwritten.

**Vaida Plankyte** · 2017-06-19 15:00 UTC

oh, that is good to know, thanks!


## PR reviewability

*2017-07-12 to 2017-07-12 · 3 messages · [open in Zulip](https://chat.zulip.org/#narrow/channel/44-git-help/topic/PR.20reviewability/with/247967)*

**Elliott Jin** · 2017-07-12 03:18 UTC

Hi all, the Zulip git workflow results in a really clean commit history, but I've had some difficulty with code reviews because it's hard to see differences between versions of  a PR when you keep squashing / rebasing.

**Elliott Jin** · 2017-07-12 03:19 UTC

Do any of you do anything specific to make PRs easier to review?  I'm thinking "append-only while the PR is still being reviewed, then squash / rebase at the very end" is the way to go, but I'm curious if anyone has thoughts on this, or if Zulip already has a recommended way to handle this.

**Tim Abbott** · 2017-07-12 17:03 UTC

@Elliott Jin for a change that is likely to be merged as just one commit, one can certainly use that approach.  And for changes that will be several, usually the strategy is to (split out, if needed, and) merge any commits at the beginning of the branch that are correct and mergable early, to keep shrinking the size of the branch.


## unable to push

*2017-07-20 to 2017-07-20 · 3 messages · [open in Zulip](https://chat.zulip.org/#narrow/channel/44-git-help/topic/unable.20to.20push/with/254161)*

**Shubham Gupta** · 2017-07-20 10:47 UTC

I have created branch, add, commit (done), but when I type git push origin <branch> , its showing error

Its showing: git push origin final-tray-unread-messages
remote: Permission to zulip/zulip-electron.git denied to fragm3.
fatal: unable to access 'https://github.com/zulip/zulip-electron.git/': The requested URL returned error: 403

**Rohitt Vashishtha** · 2017-07-20 15:31 UTC

You are making a fundamental error here. You have to work on your fork and not the `zulip/ze` repo. You should read http://zulip.readthedocs.io/en/latest/git-guide.html#get-zulip-code for more info. However, where you stand, you should do this:

**Rohitt Vashishtha** · 2017-07-20 15:35 UTC

Using ze instead of zulip-electron. 

1. Fork the `zulip/ze` repository to your account as, say, `shubham/ze`.
2. Rename the `zulip/ze` remote to `upstream`. Run `git remote rename origin upstream`.
3. Add `shubham/ze` as new remote. Run `git remote add origin https://github.com/shubham/ze`.
4. Push to origin -> `shubham/ze` as you were pushing.
5. Go to github UI to create a PR back to `zulip/ze`.


## update fork

*2017-07-28 to 2023-11-27 · 12 messages · [open in Zulip](https://chat.zulip.org/#narrow/channel/44-git-help/topic/update.20fork/with/259007)*

**Matthias** · 2017-07-28 16:40 UTC

a long time ago I did a pull request and forked Zulip. Now I did another one and it says I'm 2600+ commits behind. How to I update it so that it's the same with zulip/zulip?

**Matthias** · 2017-07-28 16:41 UTC

And in case my fork differs in any way from the source how to I overwrite my changes?

**Tim Abbott** · 2017-07-28 17:09 UTC

@Matthias `git pull --rebase` will rebase your changes on top of the latest master.  zulip.readthedocs.io/en/latest/git-guide.html has some helpful guides and links :)

**Tim Abbott** · 2017-07-28 17:10 UTC

If you want to discard your local changes, you can use `git fetch; git reset --hard upstream/master` instead.

**Tim Abbott** · 2017-07-28 17:10 UTC

Usually, whenever you start writing new code, you want to create a new branch that's based off master so you don't end up 2600 commits behind.  The Git guide should help with specifics.

**Matthias** · 2017-07-29 07:53 UTC

so in a nutshell I definitely need git or a git client install on my PC, then log in to my account on github and use some commands to do it. I thought there was some button on the web interface as well

**Tim Abbott** · 2017-07-30 23:10 UTC

There may well be; I'd ask Google.  I don't use the GitHub web UI much, so don't really know the full scope of what it can do :)

**Joshua Pan** · 2017-07-30 23:16 UTC

GitHub UI doesn't allow you to do a lot of things. The handful of stuff is probably like adding/changing files, creating pull requests/issues. That's about it.

**Sujal Shah** · 2023-11-24 12:06 UTC

So , i was updating  my local machine repo because i was 140+ commit behind and i ran these commands and got an error:

1. (zulip-py3-venv) sujal@DESKTOP-7I7H17Q:~/zulip$ git fetch upstream
2. (zulip-py3-venv) sujal@DESKTOP-7I7H17Q:~/zulip$ git pull --rebase upstream main
3. (zulip-py3-venv) sujal@DESKTOP-7I7H17Q:~/zulip$ ./tools/run-dev
After this command i got an error :
```
Provisioning state check failed! This check compares
`var/provision_version` (currently (253, 1)) to the version in
source control (`version.py`), which is (254, 0), to see if you
likely need to provision before this command can run
properly

The branch you are currently on has added dependencies beyond
what you last provisioned. Your command is likely to fail
until you add dependencies by provisioning.

Do this: `./tools/provision`

If you really know what you are doing, use --skip-provision-check to run anyway.
```
OS: windows 10 
Using Wsl2 ubuntu

**Rohan Gudimetla** · 2023-11-24 12:30 UTC

Run ```./tools/provision``` as suggested, it will download the required packages , and then you'll be good to go.

**Sujal Shah** · 2023-11-24 12:55 UTC

i have to run every time ./tools/provision  when i am pulling changes from zulip/zulip?

**Tim Abbott** · 2023-11-27 04:59 UTC

Essentially yes. It depends on whether we've upgraded dependencies in important ways, but that happens at least once a week.


## corrupt repo

*2017-08-10 to 2017-08-10 · 4 messages · [open in Zulip](https://chat.zulip.org/#narrow/channel/44-git-help/topic/corrupt.20repo/with/265570)*

**Robert Hönig** · 2017-08-10 21:40 UTC

So I messed up some binary git files with a `sed` command. Now I am getting this error for any git command:
```
error: wrong index v2 file size in .git/objects/pack/pack-c7ce0345e8f6b0e4fb34232691d76eb3de42377d.idx
error: wrong index v2 file size in .git/objects/pack/pack-b2cbf8b5bd490163f5016b583d0c3fb133b140a1.idx
error: wrong index v2 file size in .git/objects/pack/pack-a268d27e05f0bd005ef1883f8db1ab7cda9f32c2.idx
error: wrong index v2 file size in .git/objects/pack/pack-a0a3b3199a0496a53de508070dbecc6de16a4137.idx
error: wrong index v2 file size in .git/objects/pack/pack-80e0b7ae171ed1d25fc2b2d912a873a8fcf4f289.idx
error: wrong index v2 file size in .git/objects/pack/pack-80ca676c649118fd14da759712eaa83ce8fb672e.idx
error: wrong index v2 file size in .git/objects/pack/pack-5d967742882c3a15c5867c0d1f3a0937ab15b03a.idx
error: wrong index v2 file size in .git/objects/pack/pack-57f1adfe3484d413dab4578c393d489c8a407268.idx
error: wrong index v2 file size in .git/objects/pack/pack-53db2ff03757a64180b965c6db8ed6eff42bd018.idx
error: wrong index v2 file size in .git/objects/pack/pack-1a795136f5ec0d9cac428a7a9295ea7eaf3d8f34.idx
error: wrong index v2 file size in .git/objects/pack/pack-0098439a76ca920a44e9733c0eab1730137837c3.idx
error: wrong index v2 file size in .git/objects/pack/pack-c7ce0345e8f6b0e4fb34232691d76eb3de42377d.idx
error: wrong index v2 file size in .git/objects/pack/pack-b2cbf8b5bd490163f5016b583d0c3fb133b140a1.idx
error: wrong index v2 file size in .git/objects/pack/pack-a268d27e05f0bd005ef1883f8db1ab7cda9f32c2.idx
error: wrong index v2 file size in .git/objects/pack/pack-a0a3b3199a0496a53de508070dbecc6de16a4137.idx
error: wrong index v2 file size in .git/objects/pack/pack-80e0b7ae171ed1d25fc2b2d912a873a8fcf4f289.idx
error: wrong index v2 file size in .git/objects/pack/pack-80ca676c649118fd14da759712eaa83ce8fb672e.idx
error: wrong index v2 file size in .git/objects/pack/pack-5d967742882c3a15c5867c0d1f3a0937ab15b03a.idx
error: wrong index v2 file size in .git/objects/pack/pack-57f1adfe3484d413dab4578c393d489c8a407268.idx
error: wrong index v2 file size in .git/objects/pack/pack-53db2ff03757a64180b965c6db8ed6eff42bd018.idx
error: wrong index v2 file size in .git/objects/pack/pack-1a795136f5ec0d9cac428a7a9295ea7eaf3d8f34.idx
error: wrong index v2 file size in .git/objects/pack/pack-0098439a76ca920a44e9733c0eab1730137837c3.idx
error: wrong index v2 file size in .git/objects/pack/pack-c7ce0345e8f6b0e4fb34232691d76eb3de42377d.idx
error: wrong index v2 file size in .git/objects/pack/pack-b2cbf8b5bd490163f5016b583d0c3fb133b140a1.idx
error: wrong index v2 file size in .git/objects/pack/pack-a268d27e05f0bd005ef1883f8db1ab7cda9f32c2.idx
error: wrong index v2 file size in .git/objects/pack/pack-a0a3b3199a0496a53de508070dbecc6de16a4137.idx
error: wrong index v2 file size in .git/objects/pack/pack-80e0b7ae171ed1d25fc2b2d912a873a8fcf4f289.idx
error: wrong index v2 file size in .git/objects/pack/pack-80ca676c649118fd14da759712eaa83ce8fb672e.idx
error: wrong index v2 file size in .git/objects/pack/pack-5d967742882c3a15c5867c0d1f3a0937ab15b03a.idx
error: wrong index v2 file size in .git/objects/pack/pack-57f1adfe3484d413dab4578c393d489c8a407268.idx
error: wrong index v2 file size in .git/objects/pack/pack-53db2ff03757a64180b965c6db8ed6eff42bd018.idx
error: wrong index v2 file size in .git/objects/pack/pack-1a795136f5ec0d9cac428a7a9295ea7eaf3d8f34.idx
error: wrong index v2 file size in .git/objects/pack/pack-0098439a76ca920a44e9733c0eab1730137837c3.idx
error: wrong index v2 file size in .git/objects/pack/pack-c7ce0345e8f6b0e4fb34232691d76eb3de42377d.idx
error: wrong index v2 file size in .git/objects/pack/pack-b2cbf8b5bd490163f5016b583d0c3fb133b140a1.idx
error: wrong index v2 file size in .git/objects/pack/pack-a268d27e05f0bd005ef1883f8db1ab7cda9f32c2.idx
error: wrong index v2 file size in .git/objects/pack/pack-a0a3b3199a0496a53de508070dbecc6de16a4137.idx
error: wrong index v2 file size in .git/objects/pack/pack-80e0b7ae171ed1d25fc2b2d912a873a8fcf4f289.idx
error: wrong index v2 file size in .git/objects/pack/pack-80ca676c649118fd14da759712eaa83ce8fb672e.idx
error: wrong index v2 file size in .git/objects/pack/pack-5d967742882c3a15c5867c0d1f3a0937ab15b03a.idx
error: wrong index v2 file size in .git/objects/pack/pack-57f1adfe3484d413dab4578c393d489c8a407268.idx
error: wrong index v2 file size in .git/objects/pack/pack-53db2ff03757a64180b965c6db8ed6eff42bd018.idx
error: wrong index v2 file size in .git/objects/pack/pack-1a795136f5ec0d9cac428a7a9295ea7eaf3d8f34.idx
error: wrong index v2 file size in .git/objects/pack/pack-0098439a76ca920a44e9733c0eab1730137837c3.idx
error: wrong index v2 file size in .git/objects/pack/pack-c7ce0345e8f6b0e4fb34232691d76eb3de42377d.idx
error: wrong index v2 file size in .git/objects/pack/pack-b2cbf8b5bd490163f5016b583d0c3fb133b140a1.idx
error: wrong index v2 file size in .git/objects/pack/pack-a268d27e05f0bd005ef1883f8db1ab7cda9f32c2.idx
error: wrong index v2 file size in .git/objects/pack/pack-a0a3b3199a0496a53de508070dbecc6de16a4137.idx
error: wrong index v2 file size in .git/objects/pack/pack-80e0b7ae171ed1d25fc2b2d912a873a8fcf4f289.idx
error: wrong index v2 file size in .git/objects/pack/pack-80ca676c649118fd14da759712eaa83ce8fb672e.idx
error: wrong index v2 file size in .git/objects/pack/pack-5d967742882c3a15c5867c0d1f3a0937ab15b03a.idx
error: wrong index v2 file size in .git/objects/pack/pack-57f1adfe3484d413dab4578c393d489c8a407268.idx
error: wrong index v2 file size in .git/objects/pack/pack-53db2ff03757a64180b965c6db8ed6eff42bd018.idx
error: wrong index v2 file size in .git/objects/pack/pack-1a795136f5ec0d9cac428a7a9295ea7eaf3d8f34.idx
error: wrong index v2 file size in .git/objects/pack/pack-0098439a76ca920a44e9733c0eab1730137837c3.idx
error: wrong index v2 file size in .git/objects/pack/pack-c7ce0345e8f6b0e4fb34232691d76eb3de42377d.idx
error: wrong index v2 file size in .git/objects/pack/pack-b2cbf8b5bd490163f5016b583d0c3fb133b140a1.idx
error: wrong index v2 file size in .git/objects/pack/pack-a268d27e05f0bd005ef1883f8db1ab7cda9f32c2.idx
error: wrong index v2 file size in .git/objects/pack/pack-a0a3b3199a0496a53de508070dbecc6de16a4137.idx
error: wrong index v2 file size in .git/objects/pack/pack-80e0b7ae171ed1d25fc2b2d912a873a8fcf4f289.idx
error: wrong index v2 file size in .git/objects/pack/pack-80ca676c649118fd14da759712eaa83ce8fb672e.idx
error: wrong index v2 file size in .git/objects/pack/pack-5d967742882c3a15c5867c0d1f3a0937ab15b03a.idx
error: wrong index v2 file size in .git/objects/pack/pack-57f1adfe3484d413dab4578c393d489c8a407268.idx
error: wrong index v2 file size in .git/objects/pack/pack-53db2ff03757a64180b965c6db8ed6eff42bd018.idx
error: wrong index v2 file size in .git/objects/pack/pack-1a795136f5ec0d9cac428a7a9295ea7eaf3d8f34.idx
error: wrong index v2 file size in .git/objects/pack/pack-0098439a76ca920a44e9733c0eab1730137837c3.idx
error: wrong index v2 file size in .git/objects/pack/pack-c7ce0345e8f6b0e4fb34232691d76eb3de42377d.idx
error: wrong index v2 file size in .git/objects/pack/pack-b2cbf8b5bd490163f5016b583d0c3fb133b140a1.idx
error: wrong index v2 file size in .git/objects/pack/pack-a268d27e05f0bd005ef1883f8db1ab7cda9f32c2.idx
error: wrong index v2 file size in .git/objects/pack/pack-a0a3b3199a0496a53de508070dbecc6de16a4137.idx
error: wrong index v2 file size in .git/objects/pack/pack-80e0b7ae171ed1d25fc2b2d912a873a8fcf4f289.idx
error: wrong index v2 file size in .git/objects/pack/pack-80ca676c649118fd14da759712eaa83ce8fb672e.idx
error: wrong index v2 file size in .git/objects/pack/pack-5d967742882c3a15c5867c0d1f3a0937ab15b03a.idx
error: wrong index v2 file size in .git/objects/pack/pack-57f1adfe3484d413dab4578c393d489c8a407268.idx
error: wrong index v2 file size in .git/objects/pack/pack-53db2ff03757a64180b965c6db8ed6eff42bd018.idx
error: wrong index v2 file size in .git/objects/pack/pack-1a795136f5ec0d9cac428a7a9295ea7eaf3d8f34.idx
error: wrong index v2 file size in .git/objects/pack/pack-0098439a76ca920a44e9733c0eab1730137837c3.idx
error: wrong index v2 file size in .git/objects/pack/pack-c7ce0345e8f6b0e4fb34232691d76eb3de42377d.idx
error: wrong index v2 file size in .git/objects/pack/pack-b2cbf8b5bd490163f5016b583d0c3fb133b140a1.idx
error: wrong index v2 file size in .git/objects/pack/pack-a268d27e05f0bd005ef1883f8db1ab7cda9f32c2.idx
error: wrong index v2 file size in .git/objects/pack/pack-a0a3b3199a0496a53de508070dbecc6de16a4137.idx
error: wrong index v2 file size in .git/objects/pack/pack-80e0b7ae171ed1d25fc2b2d912a873a8fcf4f289.idx
error: wrong index v2 file size in .git/objects/pack/pack-80ca676c649118fd14da759712eaa83ce8fb672e.idx
error: wrong index v2 file size in .git/objects/pack/pack-5d967742882c3a15c5867c0d1f3a0937ab15b03a.idx
error: wrong index v2 file size in .git/objects/pack/pack-57f1adfe3484d413dab4578c393d489c8a407268.idx
error: wrong index v2 file size in .git/objects/pack/pack-53db2ff03757a64180b965c6db8ed6eff42bd018.idx
error: wrong index v2 file size in .git/objects/pack/pack-1a795136f5ec0d9cac428a7a9295ea7eaf3d8f34.idx
error: wrong index v2 file size in .git/objects/pack/pack-0098439a76ca920a44e9733c0eab1730137837c3.idx
```
I tried following online instructions advising me to delete `.git/index` and run `git reset`, yet the latter results in the same error message.

**Tim Abbott** · 2017-08-10 21:41 UTC

@Robert Hönig unless you have special state in that Git repo, I'd recommend re-cloning

**Tim Abbott** · 2017-08-10 21:42 UTC

Sounds like you've corrupted your Git repo.

**Robert Hönig** · 2017-08-10 21:43 UTC

Okay, that's what I'm gonna go for then. At least I found out now about the `--binary-files=without-match` option...


## Add commits to PR

*2017-12-18 to 2017-12-20 · 17 messages · [open in Zulip](https://chat.zulip.org/#narrow/channel/44-git-help/topic/Add.20commits.20to.20PR/with/394671)*

**Akash** · 2017-12-18 15:06 UTC

Does anyone know how to -
a) Add commits to others PR? Like I want add few commits here - https://github.com/zulip/zulip-electron/pull/351
b) Modify the PR and merge like Tim did here #7504 :P

**Tommy Ip** · 2017-12-18 16:18 UTC

@Akash Nimare For b) I think you have to fetch the PR branch, do a `commit --amend`, push to upstream and then close the issue (this should keep the commit author the same).
For a) I don't think you can add commits to others PR

**Akash** · 2017-12-18 18:49 UTC

@Tommy Ip is this correct -
* `hub checkout https://github.com/zulip/zulip-electron/pull/351`
* Make changes
* `git push origin` (origin is - `origin  git@github.com:zulip/zulip-electron.git (push)`

**Tommy Ip** · 2017-12-18 18:50 UTC

Yeah looks right, never tried it though

**Bala G** · 2017-12-20 18:57 UTC

I have made changes and commited. How do i push or Make a PR?

**Tommy Ip** · 2017-12-20 19:00 UTC

Do you have an existing PR?

**Bala G** · 2017-12-20 19:20 UTC

@Tommy Ip  No. I  don't have existing PR.

**Tommy Ip** · 2017-12-20 19:21 UTC

Ok which task are you doing? You should probably open a new PR

**Bala G** · 2017-12-20 19:21 UTC

https://github.com/zulip/zulip/issues/4676

**Tommy Ip** · 2017-12-20 19:23 UTC

Ok yeah, open a PR with your branch

**Bala G** · 2017-12-20 19:25 UTC

ERROR: Permission to zulip/zulip.git denied

**Tommy Ip** · 2017-12-20 19:27 UTC

You need to push to your own fork (origin), since you don't have write access to upstream

**Balaji** · 2017-12-20 19:30 UTC

Can you paste your `git remote -v` output here?

**Bala G** · 2017-12-20 19:50 UTC

I have commited and pushed to my own fork. Now from Zulip code i have to raise PR right? It's comparing , PR doesn't made

**Bala G** · 2017-12-20 19:51 UTC

> Can you paste your `git remote -v` output here?
origin	https://github.com/fossbalaji/zulip.git (fetch)

**Akash** · 2017-12-20 20:01 UTC

@Bala G this is what you need to do -
* Go to - https://github.com/fossbalaji/zulip
[PR.png](https://chat.zulip.org/user_uploads/2/60/LVLiibS134SYbyKmK9AW8sMk/PR.png) 
* Click on **Pull request** then click on **create pull request** button
[PR2.png](https://chat.zulip.org/user_uploads/2/7f/KmmmdpVTeiZaxUWpEQUkgWqw/PR2.png)

**Bala G** · 2017-12-20 20:06 UTC

> @Bala G this is what you need to do - * Go to - https://github.com/fossbalaji/zulip [PR.png](https://chat.zulip.org/user_uploads/2/60/LVLiibS134SYbyKmK9AW8sMk/PR.png) * Click on **Pull request** then click on **create pull request** button [PR2.png](https://chat.zulip.org/user_uploads/2/7f/KmmmdpVTeiZaxUWpEQUkgWqw/PR2.png)
Thanks a lot yaar.


## How do i clean up my commits?

*2017-12-28 to 2022-09-29 · 8 messages · [open in Zulip](https://chat.zulip.org/#narrow/channel/44-git-help/topic/How.20do.20i.20clean.20up.20my.20commits.3F/with/413464)*

**Bala G** · 2017-12-28 12:47 UTC

I want to clean up my commits to PR . How do i do that?

**Shubham Dhama** · 2017-12-28 13:12 UTC

Here is a nice guide to help you with it, https://zulip.readthedocs.io/en/latest/git/fixing-commits.html , If you faced any problem in following this you can ask here.

**Bala G** · 2017-12-28 14:57 UTC

I am actually stuck in cleaning up my commits. after squash only one commit should be in PR or other previous commits also will be there?

**Tommy Ip** · 2017-12-28 14:58 UTC

Have you (force) push them?

**Bala G** · 2017-12-28 15:08 UTC

I did them .

**Karan Batavia** · 2022-09-29 10:35 UTC

Hello, I'm a new contributor here on zulip. I created my first pull request to fix an issue; after adding test coverage and keeping in sync with the upstream, my commit history looks unclean and one of the maintainers asked me to clean it before merging my changes. I don't know how to do that, if anyone could help me out, it'll be great. 

Pull request: https://github.com/zulip/zulip/pull/23054

Thanks!

**Anders Kaseorg** · 2022-09-29 10:38 UTC

A good starting point is our documentation on how to [examine and tidy your commit history](https://zulip.readthedocs.io/en/latest/git/using.html#examine-and-tidy-your-commit-history).

**Karan Batavia** · 2022-09-29 11:04 UTC

@Anders Kaseorg  I tried following that, but I cannot see the 3 commits I made on the 26th of September in the interactive rebase session, which is why I cannot drop or squash merge them.


## push.default (current vs upstream)

*2018-01-19 to 2018-01-19 · 4 messages · [open in Zulip](https://chat.zulip.org/#narrow/channel/44-git-help/topic/push.2Edefault.20.28current.20vs.20upstream.29/with/455480)*

**Pooja Gadige** · 2018-01-19 09:33 UTC

I've come across `git config --global push.default upstream` while glancing over my global configurations that I'd set for git a long long time ago. I'm feeling suspicious about this config piece. Does anyone think it may prove risky or yield something wrong in the process of contributing (especially pushing) code to any of the Zulip repositories?

**Rohitt Vashishtha** · 2018-01-19 09:35 UTC

It shouldn't be a more than a headache, I suppose. Since you won't have write access to the upstream repository, github will reject your pushes and you'll have to write `origin` as the remote after it fails.

**Joshua Pan** · 2018-01-19 09:35 UTC

@Pooja Gadige you don't have write access so don't worry :)

**Pooja Gadige** · 2018-01-19 09:39 UTC

that's a relief! thank you!


## checkout to branch

*2018-03-21 to 2018-03-21 · 5 messages · [open in Zulip](https://chat.zulip.org/#narrow/channel/44-git-help/topic/checkout.20to.20branch/with/545874)*

**Vishwesh Jainkuniya** · 2018-03-21 18:01 UTC

on `git status` I can't find anything uncommitted
```
Vishweshs-MacBook-Pro:zulip-mobile vishwesh$ git status
On branch issue-2039-1
nothing to commit, working tree clean
Vishweshs-MacBook-Pro:zulip-mobile vishwesh$ 
```
But whenever I tries to checkout to different branch, it says
```
Vishweshs-MacBook-Pro:zulip-mobile vishwesh$ git checkout master
error: The following untracked working tree files would be overwritten by checkout:
	src/autocomplete/AutoCompleteView.js
Please move or remove them before you switch branches.
Aborting
Vishweshs-MacBook-Pro:zulip-mobile vishwesh$ 
```
(I have renamed `AutoCompleteView.js ` to `AutocompleteView.js ` in my last commit of branch `issue-2039-1`)

**Tim Abbott** · 2018-03-21 18:10 UTC

@Vishwesh Jainkuniya this is probably because Macs have a case-insensitive filesystem.

**Tim Abbott** · 2018-03-21 18:10 UTC

I'm not entirely sure how to work around this, to be honest, since I don't develop on a Mac, but that might be helpful for googling...

**Vishwesh Jainkuniya** · 2018-03-21 18:11 UTC

okay! :+1:

**Vishwesh Jainkuniya** · 2018-03-21 18:14 UTC

For now it got fixed by `git config core.ignorecase true`


## pull request autoremove

*2018-03-31 to 2018-04-01 · 4 messages · [open in Zulip](https://chat.zulip.org/#narrow/channel/44-git-help/topic/pull.20request.20autoremove/with/552754)*

**Aswin G** · 2018-03-31 06:55 UTC

Hey @Vishwesh Jainkuniya when I undid my last commit so I could split the commit into two, it automatically closed my PR with the initial commit. Hence after the two new commits I had to send a new PR.
How can I stop the PR from automatically closing if I have to undo the commits in it and add new ones?

**Rohitt Vashishtha** · 2018-03-31 07:03 UTC

What exact steps did you take? Updating PRs is a simple act of pushing a new reference to a branch, usually, and whatever is in that branch is diffed against the base branch.

**Vishwesh Jainkuniya** · 2018-03-31 12:53 UTC

GitHub closes PR if there are no more commits on the top, i.e the branch becomes even to the branch to which you have made PR.

**Aswin G** · 2018-04-01 11:07 UTC

Yeah that's what happened, I had to split the only commit in my pull request, so I undid the commit with `git reset HEAD~1`and pushed that to my fork, which caused the PR to get closed. So when I made the new commits I had to send a new pull request.
I suppose the PR would not have been closed if I pushed changes from local to remote after I added the new commits.


## referencing issues in commits

*2018-04-06 to 2018-04-06 · 2 messages · [open in Zulip](https://chat.zulip.org/#narrow/channel/44-git-help/topic/referencing.20issues.20in.20commits/with/556093)*

**Ben Reeves** · 2018-04-06 17:54 UTC

Hi, if we have multiple commits that work towards fixing an issue, should we only put "Fixes #num" in the final commit message or in every message that works towards the fix?

**Rishi Gupta** · 2018-04-06 18:28 UTC

final commit


## split commit

*2018-07-27 to 2018-07-28 · 5 messages · [open in Zulip](https://chat.zulip.org/#narrow/channel/44-git-help/topic/split.20commit/with/619153)*

**Shubham Dhama** · 2018-07-27 14:29 UTC

```
Situation: I've five commits in the order: c1, c2, c3, c4, c5(HEAD) and many files are changed in this series of commit and
 but after doing the work I realised that I should split c3's changes into two commits so now the states should be like c1
, c2, c3' , c3, c4, c5. Originally c3 have changes in two files, say  A and B and I want to split c3 such that all the changes
 in B are in commit  c3'  after splitting, also luckily B isn't changed in any further commits(c4 and c5).

My simple solution is to: 

- copy changes in B file in c3
- rebase to edit c2 and paste those changes  
- commit (which results in c3')
- rebase --continue

And this is a very dumb solution, but while reviewing #9181 with Tim he followed a different solution which was perfect,
 and that made sense then and it was just like watching a video at 3x but now all I remember is just some file checkouts 
commands `git checkout <sha> <file name>` and some other commands but can't get remember exactly what process 
was that. Does this problem has a standard solution? @Tim Abbott can you share your method or anyone else
```

While writing this question I got the trick and here is the solution:
* Rebase to c2
* `git checkout <sha of c3> <file path>`
* commit
* voila!!

Just sharing :)

**Neil Pilgrim (neiljp)** · 2018-07-27 16:56 UTC

This is the approach I've seen mentioned before:
https://git-scm.com/docs/git-rebase.html#_splitting_commits

**Shubham Dhama** · 2018-07-27 18:12 UTC

yeah, this is helpful when we don't care about meta info of a commit as that would result in loss of meta info and commit message of the commit which we want to split.

**Neil Pilgrim (neiljp)** · 2018-07-28 06:22 UTC

That assumes that the commits are sufficiently independent?

**Shubham Dhama** · 2018-07-28 06:31 UTC

In the above situation changes in A is dependent on B(actually B has some new library function which is used in A) and further commits are independent of these changes. So I just extracted B in a separate commit before `c3` as `c3'`. I also used to do reset when the situation is complicated enough to copy paste but also I'm lazy to rewrite commit message :)


## disabling push to certain remotes

*2018-08-03 to 2018-08-04 · 3 messages · [open in Zulip](https://chat.zulip.org/#narrow/channel/44-git-help/topic/disabling.20push.20to.20certain.20remotes/with/624903)*

**Rohitt Vashishtha** · 2018-08-03 18:23 UTC

I knew that there were ways to set different push and pull URLs for remotes but I didn't know any usecase for them. Today, I thought and tried this:

`git remote set-url --push upstream invalid-url-here`.

Now, you have no chance of accidentally pushing anything to the upstream remote.

**Boris Yankov** · 2018-08-03 22:51 UTC

@Rohitt Vashishtha cool, I did exactly the same thing few days ago. I called the invalid url `DISABLED` :)

**Rohitt Vashishtha** · 2018-08-04 02:26 UTC

Hah, that's better at making the error easy to understand.


## set-upstream

*2018-09-01 to 2018-09-01 · 3 messages · [open in Zulip](https://chat.zulip.org/#narrow/channel/44-git-help/topic/set-upstream/with/640733)*

**Akash** · 2018-09-01 19:19 UTC

Is there any way to automatically set the upstream whenever you create a new branch? I have to use the following whenever I need to push -
 > git push --set-upstream origin branch-name

**Rohitt Vashishtha** · 2018-09-01 19:23 UTC

Try this: `git config --global push.default current`.

**Akash** · 2018-09-01 19:26 UTC

This worked, thanks :handshake:


## Automatically close issues

*2020-12-29 to 2021-01-24 · 9 messages · [open in Zulip](https://chat.zulip.org/#narrow/channel/44-git-help/topic/Automatically.20close.20issues/with/1089139)*

**Abhijeet Bodas** · 2020-12-29 11:45 UTC

Zulipbot currently writes a comment like-
[image.png](https://chat.zulip.org/user_uploads/2/79/Fqo5UDmnjCSIj23jJ-loEirv/image.png)

GitHub [supports closing](https://docs.github.com/en/free-pro-team@latest/github/managing-your-work-on-github/linking-a-pull-request-to-an-issue) issues automatically when you write "Fixes #XXXXX" in you PR description too (instead of the commit message).

So, why is writing "Fixes #XXXXX" in the commit message the recommended way of linking PRs? 
If this is done, GitHub writes a new line in the issue like 
```
   <username> added a commit to <username>/zulip that referenced this issue on <date>
```
 everytime the contributor force-pushes to update the PR. I feel this is kind-of spammy. 
If PR is linked from the PR description, such a message/text is shown only once in the GitHub issue.
What do folks here think about this?

**Neil Pilgrim (neiljp)** · 2020-12-30 00:46 UTC

Once a commit is merged then having a reference indicating if it fixed an issue remains useful, and there is no link from a commit to a PR. I agree it can be spammy but GitHub should probably fix that themselves instead.

**Anders Kaseorg** · 2020-12-30 01:40 UTC

It isn’t GitHub’s fault that some commits end up without a link to the PR. It happens when a commit is manually rebased outside of GitHub and pushed to `master` without first being pushed back to the PR.

**Anders Kaseorg** · 2020-12-30 01:42 UTC

If you

* use GitHub’s merge button, or
* use GitHub’s rebase-and-merge button, or
* use GitHub’s squash-and-merge button, or
* manually push a commit to `master` without rebasing it, or
* manually rebase a commit but push it back to the PR before pushing it to `master`,

the commit remains linked to the PR.

**Anders Kaseorg** · 2020-12-30 01:45 UTC

This is also the difference between PRs that end up in the “closed” state vs. the “merged” state.

**Anders Kaseorg** · 2020-12-30 01:50 UTC

And it’s why we have `tools/push-to-pull-request`. But I guess Tim isn’t in the habit of using that.

**Tim Abbott** · 2021-01-19 05:53 UTC

Maybe we should make `push-to-pull-request --merge`, to have it push to the PR and then merge it via rebase?  That would be useable for everything except cases where I'm only merging half the PR at a time (which is often, but probably 25% of the time).

**Anders Kaseorg** · 2021-01-22 18:58 UTC

#17103?

**Tim Abbott** · 2021-01-24 17:40 UTC

Seems to work for the "merge this entire PR" use case.


## Using fetch-pull-request

*2021-02-08 to 2021-02-08 · 5 messages · [open in Zulip](https://chat.zulip.org/#narrow/channel/44-git-help/topic/Using.20fetch-pull-request/with/1115062)*

**Sarthak Garg** · 2021-02-08 07:26 UTC

Could someone guide me on how to use `fetch-pull-request` to check out a PR locally?

**Sarthak Garg** · 2021-02-08 07:27 UTC

(I'm not even sure if it's responsible for doing so :sweat_smile:)

**Abhijeet Bodas** · 2021-02-08 07:29 UTC

If you run `./tools/fetch-pull-request <PR_number>`, the script will create new local branch with a name `review-<PR_number>` with the commits in that PR.

**Abhijeet Bodas** · 2021-02-08 07:34 UTC

https://zulip.readthedocs.io/en/latest/git/zulip-tools.html#fetch-a-pull-request-without-rebasing has some examples.

**Sarthak Garg** · 2021-02-08 07:41 UTC

Thanks!


## Github action temp. file not generating

*2021-02-11 to 2021-02-12 · 3 messages · [open in Zulip](https://chat.zulip.org/#narrow/channel/44-git-help/topic/Github.20action.20temp.2E.20file.20not.20generating/with/1116414)*

**Sarthak Garg** · 2021-02-11 14:07 UTC

I was working on making a workflow to check data consistency with the server regularly using Github actions.
1. I have a step in which a python script fetches and generates a temporary file, say `temp.py`. 
2. In the next step, another script converts fetched data in `temp.py` to a suitable format. Also `temp.py` is deleted in the process.

However, the Github action refuses to import the file `temp.py` in the second step.
A screenshot of the same is [error.jpg](https://chat.zulip.org/user_uploads/2/22/v-sFc8LaJXaqHzetQaPDcsxZ/error.jpg) 
Let me know if I am doing something wrong :)

**Tim Abbott** · 2021-02-12 00:53 UTC

@Sarthak Garg 😊 that sort of import error often is a PYTHONPATH issue; most likely you neglected to whatever step is needed to use the virtualenv in which dependencies were installed.

**Sarthak Garg** · 2021-02-12 09:18 UTC

Installing the dependencies with `pip install -e .` did the job :sweat_smile: 
Thanks for the help!


## Git Help

*2021-03-24 to 2023-10-03 · 9 messages · [open in Zulip](https://chat.zulip.org/#narrow/channel/44-git-help/topic/Git.20Help/with/1142040)*

**Gautam Arora (Gautam-Arora24)** · 2021-03-24 14:36 UTC

(deleted)

**Gautam Arora (Gautam-Arora24)** · 2021-03-24 14:42 UTC

Hello Everyone! I recently used ```git rm -f <file-name>``` command without any prior knowledge of what it does and end up deleting up a file from the index and the local repository. Now, if I add that file by copy-pasting its content, it will be added as a whole file in my next commit which I need to avoid. So, is there any way to avoid this addition of the whole file? Can I undo that ```git rm -f <file-name>``` command anyhow?

**Alex Dehnert** · 2021-03-24 15:27 UTC

Have you committed yet? If not, I think just recreating the file and using "git add" should leave you with no changes: ``` $ git status On branch master nothing to commit, working tree clean ```

If you've committed that change, but not anything further, putting the old contents back, and then running `git add` to add it, followed by `git commit --amend` will probably work. (`git commit --amend` means that instead of a new commit, it should modify the prior commit.)

If you've committed that change, and further ones, you can do something using `git rebase -i`.

(This is all assuming you know how to get the file contents from somewhere, which it sounds like you can, and doing so is convenient. If not, you may be able to pull it from history.)

**Gautam Arora (Gautam-Arora24)** · 2021-03-24 16:49 UTC

Thank you @Alex Dehnert Actually I tried using ```git reset --hard <commit-hash>``` and it worked for me!

**Alex Dehnert** · 2021-03-24 16:53 UTC

Ah, right, yes, that also makes sense.

**Alex Dehnert** · 2021-03-24 16:53 UTC

(I think that'll wipe out any other changes you made, but presumably in your case that was nothing, or at least was fine.)

**Alex Dehnert** · 2021-03-24 16:54 UTC

git does not, I think, particularly consistently have just one way to do a thing...

**Gautam Arora (Gautam-Arora24)** · 2021-03-24 16:57 UTC

(replying to Alex Dehnert)
> (I think that'll wipe out any other changes you made, but presumably in your case that was nothing, or at least was fine.)
Yes, Alex, I have no extra changes or commits in my git workflow so resetting hard worked for me. Otherwise, I should have tried the steps mentioned by you :)

**Utomobong Usoro 🎀** · 2023-10-03 08:40 UTC

Hello, please i have found a task to work on but it is already claimed. I want to collaborate with the contributor working on the project, I am using my vscode terminal and I keep getting this 

PS Microsoft.PowerShell.Core\FileSystem::\\wsl.localhost\Ubuntu\home\uty\zulip> git remote add itsadijmbt https://github.com/itsadijmbt/zulip.git
>> 
fatal: detected dubious ownership in repository at '//wsl.localhost/Ubuntu/home/uty/zulip'
To add an exception for this directory, call:

        git config --global --add safe.directory '%(prefix)///wsl.localhost/Ubuntu/home/uty/zulip'
PS Microsoft.PowerShell.Core\FileSystem::\\wsl.localhost\Ubuntu\home\uty\zulip> git fetch itsadijmbt
>>
fatal: detected dubious ownership in repository at '//wsl.localhost/Ubuntu/home/uty/zulip'
To add an exception for this directory, call:

        git config --global --add safe.directory '%(prefix)///wsl.localhost/Ubuntu/home/uty/zulip'
PS Microsoft.PowerShell.Core\FileSystem::\\wsl.localhost\Ubuntu\home\uty\zulip>


## navigating git blame

*2021-04-08 to 2021-04-08 · 11 messages · [open in Zulip](https://chat.zulip.org/#narrow/channel/44-git-help/topic/navigating.20git.20blame/with/1156904)*

**Wesley Aptekar-Cassels** · 2021-04-08 05:56 UTC

how do people navigate git blame? what i want is a way to see the current blame, then select a line, and jump to the blame for the commit just before that line was changed. right now, i do this manually, but that seems like a pain, i'm sure there's a better way.

what do other folks do for this? is there a git UI that runs on linux that handles this well?

**Wesley Aptekar-Cassels** · 2021-04-08 05:58 UTC

currently, my workflow is like:

```
git blame <filename>
git show <commit hash, copied from previous command>
git checkout <commit hash, copied from previous command>~
# repeat
```

**Anders Kaseorg** · 2021-04-08 06:01 UTC

`gitk` and `git gui blame` do exactly that.

**Wesley Aptekar-Cassels** · 2021-04-08 06:04 UTC

`git: 'gui' is not a git command. See 'git --help'.` — what do i need to install?

**Anders Kaseorg** · 2021-04-08 06:05 UTC

On Debian/Ubuntu, there are `gitk` and `git-gui` packages (also `git-all`).

**Anders Kaseorg** · 2021-04-08 06:06 UTC

`gitk` accepts most arguments you’d use with `git log`; `gitk --all` is particularly useful. Right-click a line in the diff for a menu with “Show origin of this line” or “Run gui blame on this line”.

**Wesley Aptekar-Cassels** · 2021-04-08 06:07 UTC

ahh, looks like it's `gitFull` on NixOS, will give it a spin :)

**Anders Kaseorg** · 2021-04-08 06:10 UTC

Oh right you’re a NixOS user too, yay. (`nix-index` can be helpful for these sorts of questions.)

**Greg Price** · 2021-04-08 06:18 UTC

For a bit of an indirect answer, a tool I'll commonly use for this purpose is `git log -L`. So `git log -L :funcName:path/to/file.js` will find the definition by that name in the file, and show me a log of the changes that touched those lines. Or `-L 123,147:path/to/file.js` for an arbitrary range of lines.

**Greg Price** · 2021-04-08 06:19 UTC

Other times I'll use `git log -S` to go straight to when some key bit was introduced, or removed.

**Greg Price** · 2021-04-08 06:22 UTC

This is also probably a good place to mention my (short) guide to reading Git history:
https://github.com/zulip/zulip-mobile/blob/master/docs/howto/git.md
which has `git log -S` and a few relatives, and also one weird trick that makes for very efficiently reading through `git log -p`.


## github ordering of commits?

*2021-04-08 to 2021-04-08 · 22 messages · [open in Zulip](https://chat.zulip.org/#narrow/channel/44-git-help/topic/github.20ordering.20of.20commits.3F/with/1156953)*

**Wesley Aptekar-Cassels** · 2021-04-08 07:09 UTC

i have a very strange thing happening. i have #M4608 open, which has four commits, that look like this in the github UI:

[.](https://chat.zulip.org/user_uploads/2/61/AVZid-__vswYim3MDDiJPXBy/0000-recent.png) 

however:

```
~/code/zulip-mobile$ git log --oneline | head -n 5
bb98b00a TopicItem: Show actionsheet on long-press.
3c9d9e84 TopicItem [nfc]: Make stream name required.
ba955b13 TopicList [nfc]: Pass stream name into TopicItem
5e5b54bc ZulipMobile [nfc]: Use just one `ActionSheetProvider`, here.
61891dbc webview: Mark messages as read when bottom comes into view
~/code/zulip-mobile$ git push --force wesleyac topicitem-longpress-actionsheet
Everything up-to-date
```

has anyone else seen this? why won't github let me push the reordered commits?

**Gautam Arora (Gautam-Arora24)** · 2021-04-08 07:11 UTC

Well, you can always reorder the commit using git rebase😅

**Wesley Aptekar-Cassels** · 2021-04-08 07:11 UTC

yes, i've done that. then when i push, github claims that they are up to date, is my problem...

**Gautam Arora (Gautam-Arora24)** · 2021-04-08 07:13 UTC

If you rebase, you always have to do force-push

**Wesley Aptekar-Cassels** · 2021-04-08 07:14 UTC

yes, i understand that. look at the last line — i have rebased, i force push, github claims "Everything up-to-date". note that the commit hashes in my `git log` and the ones on github are different, since the commits are ordered differently.

**Gautam Arora (Gautam-Arora24)** · 2021-04-08 07:15 UTC

Thinking...

**Wesley Aptekar-Cassels** · 2021-04-08 07:16 UTC

oh, i see, i'm in detached head, so it doesn't let me push to a branch :/

**Sarthak Garg** · 2021-04-08 07:36 UTC

You could checkout to a new branch from there and then push.

**Greg Price** · 2021-04-08 17:04 UTC

(replying to Wesley Aptekar-Cassels)
> oh, i see, i'm in detached head, so it doesn't let me push to a branch :/

`git push --force wesleyac @:topicitem-longpress-actionsheet` will do that

**Greg Price** · 2021-04-08 17:04 UTC

(Or I usually spell the `--force` as `+`: `git push wesleyac +@:topicitem-longpress-actionsheet`)

**Greg Price** · 2021-04-08 17:09 UTC

And I think what was happening isn't that it wouldn't let you push to a branch -- it's happy to do so when you specify the branch (as you did), but it's that the branch still had the same commits that were in the remote repo, because the branch didn't have the commits you were looking at. So:

> ``` ~/code/zulip-mobile$ git push --force wesleyac topicitem-longpress-actionsheet Everything up-to-date ```

it responded "yep, got it, the remote is already up to date with that branch".

**Wesley Aptekar-Cassels** · 2021-04-08 17:14 UTC

oh, right, i recall now that the syntax is `git push localbranch:remotebranch`. `@` being an alias for head, i presume. is `+` being `--force` a standard git feature? i assumed when i'd seen it before that it was github doing magic when parsing the branch name, but i realize now that git is parsing the `:` anyways, so i guess it's built in to git? (i habitually do `--force-with-lease` most of the time in any case, so it's not too much help, but good to know)

**Greg Price** · 2021-04-08 17:14 UTC

Here's a different tip, which could be helpful for spotting that's what's happening :smile: -- and also may save some typing:

(replying to Wesley Aptekar-Cassels)
> ``` ~/code/zulip-mobile$ git log --oneline | head -n 5 bb98b00a TopicItem: Show actionsheet on long-press. 3c9d9e84 TopicItem [nfc]: Make stream name required. ba955b13 TopicList [nfc]: Pass stream name into TopicItem 5e5b54bc ZulipMobile [nfc]: Use just one `ActionSheetProvider`, here. 61891dbc web …

Instead of piping to `head`, you can get the same effect by passing a limit to `git log` directly. If you do:
```
$ git log --oneline -5
26c8737d5 (HEAD -> master, upstream/master, upstream/HEAD) events tests: Add type-checking.
afbc9e7cb events: Switch to our `logging`, from `console`; mock properly in test.
d84cbc174 events [nfc]: Simplify out a `.apply`.
356f36fb6 events [nfc]: Pull out handleEvent as a function.
a70b88959 events: Catch exception for each event individually.
```
then by default it "decorates" the output with branch names.

Also you get color that way (I forget if this is default, but it's in [my gitconfig](https://gist.github.com/gnprice/5f71b63464a76bd7e0480f207b1bbff3)):
[image.png](https://chat.zulip.org/user_uploads/2/93/6WNGU9Dzh-DZTD6dle5si5Xt/image.png)

**Greg Price** · 2021-04-08 17:15 UTC

(replying to Wesley Aptekar-Cassels)
> oh, right, i recall now that the syntax is `git push localbranch:remotebranch`. `@` being an alias for head, i presume. is `+` being `--force` a standard git feature? i assumed when i'd seen it before that it was github doing magic when parsing the branch name, but i realize now that git is parsing …

Yep, `@` is a shorthand for `HEAD`. And yep, `+` there is a standard Git feature. It can also be used to apply `--force` to just one refspec, if you're pushing several different things in the same command.

**Greg Price** · 2021-04-08 17:17 UTC

Looks like there isn't a corresponding shorthand for `--force-with-lease`. Though for the use case of applying it to just one of several things you're pushing, it has its own (more regular) syntax `--force-with-lease=<refname>` or `--force-with-lease=<refname>:<expect>`.

**Greg Price** · 2021-04-08 17:30 UTC

Another different tip in an overlapping direction: a few years ago I adjusted my prompt so that it tells me key details of my Git status, when I'm inside a Git repo. You can see that in the screenshot above -- my prompt looks like this (plus some color):
```
greg@dark-matter:~/z/mobile (master u=) 
$ 
```

I've been quite happy with having that -- I type `git status` quite a lot less now.

The config for that is in my `~/.bashrc`, which is posted [here](https://gist.github.com/gnprice/ca70f86532b2ac75c3cc38db4d2da53d), has comments, and I'd encourage people to copy any or all of. The bits that control that particular feature are [here](https://gist.github.com/gnprice/ca70f86532b2ac75c3cc38db4d2da53d#file-bashrc-L116-L139) where it's mentioning GIT_PS1_etc and `__git_ps1`.

(You'll also need to source the `git-sh-prompt` script which is provided with Git. On a Debian or Ubuntu system, if you have the `git` package installed, `. /usr/lib/git-core/git-sh-prompt` anywhere in your `~/.bashrc` will do it. Not sure where NixOS puts it.)

**Tim Abbott** · 2021-04-08 18:33 UTC

I also highly recommend using `gitk --all` to understand the situation whenever you're confused about the state of a set of Git repositories and their relationship.

**Anders Kaseorg** · 2021-04-08 18:36 UTC

> Not sure where NixOS puts it.

I use `GIT_EXEC_PATH="$(git --exec-path)" && . "$GIT_EXEC_PATH/../../share/git/contrib/completion/git-prompt.sh"`.

(Alternatively, there’s the impure `. ~/.nix-profile/share/git/contrib/completion/git-prompt.sh`.)

**Greg Price** · 2021-04-08 19:09 UTC

(replying to Tim Abbott)
> I also highly recommend using `gitk --all` to understand the situation whenever you're confused about the state of a set of Git repositories and their relationship.

Yes, definitely this too.

The prompt, and `git log --oneline -10` or whatever, is super helpful for getting a quick routine picture, and I use them both constantly. (The particular `git log --oneline` command I type all the time is [my alias `git uv`](https://gist.github.com/gnprice/5f71b63464a76bd7e0480f207b1bbff3/168ea9aed0d61890987d0a222a69c862c38656f5#file-gitconfig-L33).) But as soon as you find you're confused about what's happening with the picture you're getting, it's really valuable to get a global picture with like `gitk --all HEAD`.

**Greg Price** · 2021-04-08 19:10 UTC

(The `HEAD` part ensures you see the commit you're currently on, if it's not part of any branch -- which I think would have been necessary in the case at the top of this thread, for example.)

**Greg Price** · 2021-04-08 19:11 UTC

And `gitk` is great on Linux but if you're on macOS or Windows another graphical client may be more convenient:
https://zulip.readthedocs.io/en/latest/git/setup.html#get-a-graphical-client

**Greg Price** · 2021-04-08 20:36 UTC

(Forked a thread to https://chat.zulip.org/#narrow/stream/44-git-help/topic/gitk.20on.20macOS.20and.20Windows/near/1157828 .)


## gitk on macOS and Windows

*2021-04-08 to 2021-04-28 · 24 messages · [open in Zulip](https://chat.zulip.org/#narrow/channel/44-git-help/topic/gitk.20on.20macOS.20and.20Windows/with/1157828)*

**Anders Kaseorg** · 2021-04-08 19:20 UTC

`gitk` works on macOS and Windows too. It might not be the prettiest application by modern standards, but I can’t imagine a better convenience than “it comes with Git”.

**Greg Price** · 2021-04-08 20:25 UTC

Cool. Maybe we should update that page, then?

I'm pretty sure at one point the story on macOS and Windows was that if you wanted to run `gitk`, you needed an X server, and that was getting to be an increasingly inconvenient thing to set up. But if it now just comes with Git and works out of the box, that's great.

**Greg Price** · 2021-04-08 20:28 UTC

Hmm, I think the story on macOS at least may still not be quite that convenient.

I have both the system Git in /usr/bin/git, and one installed from Homebrew in /usr/local/bin/git. And I don't seem to have a `gitk`. `brew install gitk` doesn't find anything, either.

**Anders Kaseorg** · 2021-04-08 20:31 UTC

Yeah okay, I tested with the default Git for Windows install but trusted the internet too much for macOS. Maybe `brew install git-gui`?

**Anders Kaseorg** · 2021-04-08 20:33 UTC

(I guess I should finish setting up my Mac enough to do zulip-desktop releases, and I’m probably going to want Homebrew…)

**Greg Price** · 2021-04-08 20:34 UTC

That does work!

I don't think I've ever used git-gui before. How do I get a `gitk`-like view from it?

**Greg Price** · 2021-04-08 20:34 UTC

(Just `git gui` gives me what looks like a UI to make a commit.)

**Anders Kaseorg** · 2021-04-08 20:34 UTC

I was conjecturing that `gitk` comes with the `git-gui` package.

**Greg Price** · 2021-04-08 20:35 UTC

Ah, I see.

Seems like it does! But then it gives me an error... I'll fork this thread and switch to the browser on that machine, and add details.

**Greg Price** · 2021-04-08 20:37 UTC

Here's the error:
```
zulip-mac:mobile greg$ gitk --all HEAD &
[2] 72030
zulip-mac:mobile greg$ Error in startup script: 58:103: execution error: Not authorized to send Apple events to System Events. (-1743)
    while executing
"exec osascript -e [format {
        tell application "System Events"
            set frontmost of processes whose unix id is %d to true
        end te..."
    invoked from within
"if {[tk windowingsystem] eq "aqua"} {
    exec osascript -e [format {
        tell application "System Events"
            set frontmost of processes ..."
    (file "/usr/local/bin/gitk" line 12292)

[2]+  Done                    gitk --all HEAD
```

**Anders Kaseorg** · 2021-04-08 20:37 UTC

Wow, how very Apple.

**Greg Price** · 2021-04-08 20:38 UTC

Likely related: the first time I tried starting `git gui` after installing it a few minutes ago, I got a system permissions prompt about if I wanted to let iTerm control the computer, and mentioning AppleScript.

I'd rather not, and was curious if things would work without that, so said no.

**Greg Price** · 2021-04-08 20:38 UTC

`git gui` itself seemed to work fine, though I've never used it before so don't know what might have been missing. But then yeah this.

**Greg Price** · 2021-04-08 20:40 UTC

Here's the relevant bit of `gitk`, it seems:
```
  12291 # on OSX bring the current Wish process window to front
  12292 if {[tk windowingsystem] eq "aqua"} {
  12293     exec osascript -e [format {
  12294         tell application "System Events"
  12295             set frontmost of processes whose unix id is %d to true
  12296         end tell
  12297     } [pid] ]
  12298 }

**Greg Price** · 2021-04-08 20:43 UTC

That's the only mention of `osascript` in that giant script.

I feel like it's a bug in `gitk` that on macOS it crashes if you don't give it a scary permission. Very likely it didn't use to be that way until some recent year's macOS release, and gitk just doesn't see enough development (especially macOS-specific development) to have fixed it.

But since that's the only mention, it's probably fine and I think the next thing I want to do is to say "OK, ok, you can have that permission" and see if it otherwise seems to work well.

**Anders Kaseorg** · 2021-04-08 20:46 UTC

Yeah, my experience getting patches into gitk has been slow because the maintainer works in a separate gitk tree that’s only occasionally merged into git.git.

**Greg Price** · 2021-04-08 20:46 UTC

Oof, that doesn't sound like it'd help.

**Anders Kaseorg** · 2021-04-08 20:47 UTC

Or at least that was true…wow, 10 years ago.

**Greg Price** · 2021-04-08 20:49 UTC

Hey, it works!
[Screen-Shot-2021-04-08-at-1.48.49-PM.png](https://chat.zulip.org/user_uploads/2/2/MJC_CYfgxaztNJTAHYjNhpdP/Screen-Shot-2021-04-08-at-1.48.49-PM.png)

**Greg Price** · 2021-04-08 20:49 UTC

FTR here's the bit of settings UI I had to go into to relent on the permissions question:
[Screen-Shot-2021-04-08-at-1.49.22-PM.png](https://chat.zulip.org/user_uploads/2/f1/tgeCurbgqpZaBXaEV9GyU6DE/Screen-Shot-2021-04-08-at-1.49.22-PM.png)

**Greg Price** · 2021-04-08 20:50 UTC

(found thanks to [this SE answer](https://apple.stackexchange.com/a/400054/284310))

**Greg Price** · 2021-04-08 20:53 UTC

OK, so it sounds like the story is:
* On Windows, you've already installed Git for Windows by the time you're thinking about this -- just run `gitk` and voilà. (Based on the testing you mentioned doing.)
* On macOS, `brew install git-gui` and then you'll have `gitk`.
  * There's a scary permissions prompt you'll have to accept for dumb reasons. If you say no, gitk won't start; you can change your answer to yes if you want; see this chat thread for details.

**Greg Price** · 2021-04-08 21:02 UTC

(Also it *looks* utterly ridiculous -- on Linux it just looks old-fashioned, but if you take a look at that screenshot from macOS it's this hilarious mashup with up-to-date Mac dropdowns and radio buttons sprinkled among the '90s-style Tk text fields, and some widgets that get the memo about dark mode while others don't. But hey, it does its job.)

**Tim Abbott** · 2021-04-28 18:41 UTC

@Greg Price can we add this documentation here? https://zulip.readthedocs.io/en/latest/git/setup.html#get-a-graphical-client


## append to earlier commit

*2021-06-07 to 2021-06-07 · 11 messages · [open in Zulip](https://chat.zulip.org/#narrow/channel/44-git-help/topic/append.20to.20earlier.20commit/with/1203140)*

**Wesley Aptekar-Cassels** · 2021-06-07 20:55 UTC

I often want to `git commit --amend` to a commit earlier in my history. I currently `git commit -m "squashme"`, then `git rebase -i upstream/master`, and edit the `pick` to `f`, and rearrange it, but that's sort of a pain. Is there a easy one-line way to squash current changes into a given ref?

**Anders Kaseorg** · 2021-06-07 21:21 UTC

Yeah, you can use `commit --fixup` and rebase with autosquash.

**Greg Price** · 2021-06-07 21:21 UTC

The feature that's aimed at helping automate this is `git commit --fixup OLDCOMMIT` plus `git rebase -i --autosquash`

**Greg Price** · 2021-06-07 21:23 UTC

Another feature which can be handy for writing the `--fixup` argument is `:/foo`, which searches commit messages:
https://manpages.debian.org/testing/git-man/gitrevisions.7.en.html

**Greg Price** · 2021-06-07 21:27 UTC

I find that that approach has enough small hiccups that I actually just mostly stick to `git commit -am 'fixup foo'` and plain `git rebase -i`. But definitely worth trying out for yourself.

(The silliest of them: you have to type out as far as `--autosq` before tab-completing, because there's also a `git rebase --autostash`.)

**Anders Kaseorg** · 2021-06-07 21:30 UTC

You can `git config --global rebase.autoSquash true` to get autosquash by default.

**Alex Vandiver** · 2021-06-07 22:16 UTC

I have a `git flat` which is aliased to `git  -c core.editor=: rebase -i` (and I have `rebase.autoSquash=true`) which I use after `git fixup` which is aliased to `git commit --fixup`, often with `:/foo`.

**Alex Vandiver** · 2021-06-07 22:17 UTC

So I often:
```
git fixup :/foo -a
git flat
```
...to fold a change into an earlier commit, without opening any editor.

**Greg Price** · 2021-06-07 22:55 UTC

Interesting. Do you use your `git flat` in other ways, or basically just for that use case?

It's kind of an entertaining hack or workaround, in that the nop editor setting *almost* cancels out the `-i`, so that it's almost like just saying `git rebase`… but more precisely it's like "`git rebase` but pretend I interacted". In particular, `--autosquash` only does anything if you're using `-i`.

**Alex Vandiver** · 2021-06-07 23:05 UTC

I ~only use it for flattening out autosqashes -- and yes, it is precisely because autosquash only kicks in for interactive rebases.

**Alex Vandiver** · 2021-06-07 23:05 UTC

But I may queue up multiple autosquash commits before flattening them out.


## git rebase restored deleted files

*2021-07-19 to 2021-07-19 · 10 messages · [open in Zulip](https://chat.zulip.org/#narrow/channel/44-git-help/topic/git.20rebase.20restored.20deleted.20files/with/1234282)*

**Akash Dhiman** · 2021-07-19 17:54 UTC

@Greg Price [wrote](https://github.com/zulip/zulip-mobile/pull/4757#issuecomment-882722824) in #M4757
> All looks good, except that it looks like send.js got revived in this one

I wonder why this happened, I followed the steps that @Greg Price listed [here](https://github.com/zulip/zulip-mobile/pull/4757#discussion_r670840304), I have had this happen to me once before as well where a commit which deletes a file misbehaved during rebase. (don't quite remember how exactly but I recall that it involved a deleted file and an edit in its previous commit during rebase.)

**Greg Price** · 2021-07-19 17:57 UTC

Hmm, yeah, sometimes the way Git's automatic merge handles those is less helpful than one would like.

The general solution is to check that the results are what you intended, so you can fix them when they're not. One command I very often do right after a rebase is `git diff @{1}` -- that tells me if the tree at the tip of the branch now is any different from what it was before the rebase.

**Greg Price** · 2021-07-19 17:57 UTC

Which for a lot of `rebase -i` rounds I expect to be empty, and if not then it still tells me if there's something I didn't intend.

**Greg Price** · 2021-07-19 18:02 UTC

OK, and trying out those steps I wrote in that comment, I see that the `git checkout @{2} .` line doesn't delete the file.

It would have *added*, or edited, any files that were present in that other commit. But it doesn't delete a file that isn't present there.

**Greg Price** · 2021-07-19 18:03 UTC

Aha, but `git restore` does do the right thing!

So I guess this is a good reason to do the modern thing and use `git restore`.

Instead of `git checkout @{2} .`, that command should be:
`git restore -s @{2} .`

**Notification Bot** · 2021-07-19 18:04 UTC

This topic was moved here from #**mobile-team>git rebase restored deleted files** by @Greg Price

**AkashDhiman (test)** · 2021-07-19 18:05 UTC

interesting! thanks for trying it out.

**Greg Price** · 2021-07-19 18:05 UTC

(I've just gone and made that edit to my comment, too, so it doesn't lead anyone astray in the future)

**Greg Price** · 2021-07-19 18:10 UTC

Some background is that `git checkout` is a command that's really about three different commands smashed together into an uneasy coexistence:
* It changes what branch you're on. (With an optional bonus feature of creating the branch to switch to.)
* It takes what's in the index, and updates the worktree to match -- IOW, it discards changes you haven't added to the index.
* It takes what's in some other commit (or some "tree-ish" in general), and updates both the index and the worktree to match that.

So it was long overdue for refactoring into some more coherent interface, and in a new version of Git in the last couple of years they added `git restore` as an attempt to do that.

**Greg Price** · 2021-07-19 18:12 UTC

I'd tried out `git restore` and then mostly gone back to using `git checkout`, because it usually felt like I was just typing out the same command except with `restore -s` replacing `checkout`, and `restore -s` is a bit more typing. But this is an important behavior difference, where they cleaned up the behavior while adding the new command!


## push-to-pull-request error

*2021-07-19 to 2021-07-20 · 15 messages · [open in Zulip](https://chat.zulip.org/#narrow/channel/44-git-help/topic/push-to-pull-request.20error/with/1234548)*

**Alya Abbott** · 2021-07-19 22:04 UTC

Hmm, am I doing something wrong?

```
(zulip-py3-venv) vagrant@vagrant:/srv/zulip$ ./tools/push-to-pull-request 19147
error: couldn't parse remote URL as GitHub repo: https://github.com/zulip/zulip.git
```

**Anders Kaseorg** · 2021-07-19 22:06 UTC

`push-to-pull-request` expects you to be pushing by SSH (not because you have to, just because that’s what it expects). Have you successfully used it before?

**Anders Kaseorg** · 2021-07-19 22:07 UTC

It’s possible you have it configured to work outside the Vagrant environment but not inside.

**Alya Abbott** · 2021-07-19 22:08 UTC

I haven't used it.

**Alya Abbott** · 2021-07-19 22:09 UTC

Outside, I need to figure out dependencies, I guess (on a Mac):

```
alya@wyndle zulip % ./tools/push-to-pull-request --help
error: not found: jq

push-to-pull-request requires the `jq` utility; you should install it.
Try:

  sudo apt install jq
alya@wyndle zulip % sudo apt install jq
Password:
The operation couldn’t be completed. Unable to locate a Java Runtime.
Please visit http://www.java.com for information on installing Java.
```

**Anders Kaseorg** · 2021-07-19 22:12 UTC

I don’t use it either myself; I would just run the manual equivalent:

`git push https://github.com/amanagr/zulip.git +@:landing_for_education`

**Alya Abbott** · 2021-07-19 22:33 UTC

Oh, hm, I guess I don't have permissions for that command. I can just make a new PR if that's going to be easiest.

**Greg Price** · 2021-07-19 22:40 UTC

(replying to Alya Abbott)
> Outside, I need to figure out dependencies, I guess (on a Mac): ``` … push-to-pull-request requires the `jq` utility; you should install it. Try: sudo apt install jq ```

I believe `brew install jq` will get you what you want.

**Greg Price** · 2021-07-19 22:43 UTC

I'm puzzled by that error. I hadn't expected there would be an `apt` command lying around on macOS!

But indeed, there's one on the Mac on my desk, too. It is not something you want, I think :smile:

**Greg Price** · 2021-07-19 22:46 UTC

And yeah, if you don't have the needed permissions on the repo, then a new PR might be easiest.

If you want to keep it in the same PR, the alternative would be to push a branch to your clone, and ask Aman to fetch that and push it to his existing PR.

**Anders Kaseorg** · 2021-07-19 22:46 UTC

(That message is just printed literally by `push-to-pull-request`, whether or not there’s an actual `apt`.)

**Greg Price** · 2021-07-19 23:00 UTC

(replying to Anders Kaseorg)
> (That message is just printed literally by `push-to-pull-request`, whether or not there’s an actual `apt`.)

Yeah -- I'm pretty sure I wrote that message :wink:

**Greg Price** · 2021-07-19 23:02 UTC

This is a script that's only really useful for maintainers, not most contributors -- as demonstrated by the permissions issue Alya saw when trying to run directly the command that it'd ultimately run to do its main work. For that reason I felt OK cutting some corners on assumptions about people's dev environments, where I wouldn't want to in a script for general Zulip-development use.

**Greg Price** · 2021-07-19 23:03 UTC

FTR I believe the script does work just fine on macOS, though (and I think @Chris Bobbe regularly uses it there), once you get `jq` installed from Homebrew or whatever.

**Alya Abbott** · 2021-07-20 06:41 UTC

Cool, thanks for the guidance!


## Can't push?

*2021-07-27 to 2021-07-27 · 6 messages · [open in Zulip](https://chat.zulip.org/#narrow/channel/44-git-help/topic/Can.27t.20push.3F/with/1239297)*

**Jore** · 2021-07-27 14:09 UTC

Hi everyone... Zulip is the first time I'm using `git` so please forgive the noobness, but I'm stuck at a stage trying to push a commit to Github where there's been changes upstream. I'm following the documentation from [here](https://zulip.readthedocs.io/en/latest/git/using.html#keep-your-fork-up-to-date) but run into this error: 
```
$ git push origin issue-19359 
To github.com:nooblag/zulip.git
 ! [rejected]              issue-19359 -> issue-19359 (fetch first)
error: failed to push some refs to 'git@github.com:nooblag/zulip.git'
hint: Updates were rejected because the remote contains work that you do
hint: not have locally. This is usually caused by another repository pushing
hint: to the same ref. You may want to first integrate the remote changes
hint: (e.g., 'git pull ...') before pushing again.
hint: See the 'Note about fast-forwards' in 'git push --help' for details
```
I'm scared to run `git pull` cos last time I think I did that (#18998) and I muddied up the commit with a merge commit from master (which was unwanted)...

Is this situation fixed by `git pull --rebase` and if so, does the documentation on this page need updating perhaps? Or am I doing something else wrong?

Thanks!

**Jore** · 2021-07-27 14:10 UTC

Screenshot would probably help too:
[Screenshot-from-2021-07-28-00-03-06.png](https://chat.zulip.org/user_uploads/2/54/v0qbCX0KyuHIbtB2GjDJZDXY/Screenshot-from-2021-07-28-00-03-06.png)

**Jore** · 2021-07-27 15:07 UTC

I got brave and ran `git pull --rebase` but it unforch didn't help...

**Dinesh Ch** · 2021-07-27 16:55 UTC

Doing a rebase changes the commit ID. Since the commit IDs on remote don't match with your local ones, git cannot push your commits. I think you can do a `git push -f`.

(feel free to correct me if I'm wrong)

**Alex Vandiver** · 2021-07-27 17:00 UTC

Yup, force-pushing is the right thing to do after you've made changes to one of your branches, or rebased it. https://zulip.readthedocs.io/en/latest/git/using.html#force-push-changes-to-github-after-you-ve-altered-your-history and the rest of that page may be helpful.

**Jore** · 2021-07-27 17:03 UTC

Okay great, thanks for that! I'll definitely give that a try next time. :big_smile:


## ✔ Cloning

*2021-08-18 to 2021-08-18 · 3 messages · [open in Zulip](https://chat.zulip.org/#narrow/channel/44-git-help/topic/.E2.9C.94.20Cloning/with/1247873)*

**Geo Jolly** · 2021-08-18 11:36 UTC

Is doing `git clone https://github.com/zulip/zulip-terminal.git` the same as `git clone git@github.com:zulip/zulip-terminal.git` ?
Does it matter if I do a PR?

**Ivan Gretsky** · 2021-08-18 11:47 UTC

Both will clone the same code. The 1st via https protocol and the 2nd via SSH. This won't matter for a PR.

**Notification Bot** · 2021-08-18 11:59 UTC

@Geo Jolly has marked this topic as resolved.


## ✔ Squashing only my commits

*2021-09-08 to 2021-09-08 · 6 messages · [open in Zulip](https://chat.zulip.org/#narrow/channel/44-git-help/topic/.E2.9C.94.20Squashing.20only.20my.20commits/with/1253583)*

**Parth Mittal** · 2021-09-08 14:42 UTC

So I need to squash all my commits to the PR into one commit. Referring to the docs, I switched to my feature branch. 
Then ran ```git rebase -i HEAD~4```
But this is also squashing commits made by others on the remote repo. I want to squash *only my commits*

**Tim Abbott** · 2021-09-08 16:57 UTC

@Parth Mittal you generally want `git rebase -i upstream/main` to only see your commits.

**Tim Abbott** · 2021-09-08 16:57 UTC

(`HEAD~4` just shows the last 4 commits, regardless of whether they're already merged to `main`)

**Parth Mittal** · 2021-09-08 17:13 UTC

Got it sir, thank you!

**Notification Bot** · 2021-09-08 17:22 UTC

@Parth Mittal has marked this topic as resolved.

**Greg Price** · 2021-09-08 18:58 UTC

You can also simplify things by having your branch's "upstream" be `upstream/main`.

You can make that the case for your current branch by saying `git branch -u upstream/main`. You can see the upstreams for all your branches by saying `git branch -vv`.

Once that's the case, if you say simply `git rebase -i`, it'll rebase just the commits that are specific to your branch.


## git error

*2021-10-07 to 2021-10-07 · 1 messages · [open in Zulip](https://chat.zulip.org/#narrow/channel/44-git-help/topic/git.20error/with/1263762)*

**Notification Bot** · 2021-10-07 19:07 UTC

This topic was moved by @Greg Price to #**development help>ReferenceError: document is not defined**


## Branch Ahead by X commits

*2021-10-15 to 2021-10-16 · 6 messages · [open in Zulip](https://chat.zulip.org/#narrow/channel/44-git-help/topic/Branch.20Ahead.20by.20X.20commits/with/1266936)*

**Vighnesh Kulkarni** · 2021-10-15 05:08 UTC

Hello everyone! This is my first time contributing to Zulip and I'm stuck with this git issuse:-

So, I forked and cloned the repo a few days ago, checked out to a new branch and made a commit in it.
Today I switched to main branch and did `git fetch` and `git rebase` as mentioned in the [documentation](https://zulip.readthedocs.io/en/latest/git/using.html#keep-your-fork-up-to-date) 
And now when I'm trying to checkout into the branch I had created before, it says `Your branch is ahead of 'origin/main' by 113 commits.` [zulip-git-help.png](https://chat.zulip.org/user_uploads/2/79/whBCHRxKO7d2elhteLZFgkV4/zulip-git-help.png)

Should I run this command next? :- `git push origin #19888-chevron-for-stream-selection`

Thanks!

**Greg Price** · 2021-10-15 20:15 UTC

@Vighnesh Kulkarni I think the very most helpful next step for you would be to set up a graphical Git client:
https://zulip.readthedocs.io/en/latest/git/setup.html#get-a-graphical-client
and take a look using that.

That will let you see a clear picture of what all the different branches in your repository look like, which will help a lot in seeing what to do. (It also lets you see exactly what the effect is of each command you try.)

**Greg Price** · 2021-10-15 20:15 UTC

From the style of your terminal, I'm guessing you're on Linux. In that case `gitk` is great. Try `gitk --all HEAD &` for a full picture.

**Greg Price** · 2021-10-15 20:20 UTC

What that message is specifically telling you is that your remote-tracking branch `origin/main` is 113 commits behind your local branch `main`.

If your `origin` remote is your own GitHub clone of Zulip, then `origin/main` is not something that you'll really use. You can always push to it to keep it up to date, but my recommendation would be to ignore it.

You can get Git to stop comparing your local branch to `origin/main`, and to instead tell you a more interesting comparison to `upstream/main`, by setting the "upstream" of the branch, like `git branch main --set-upstream-to upstream/main`. See [`git help branch`](https://manpages.debian.org/testing/git-man/git-branch.1.en.html).

**Greg Price** · 2021-10-15 20:23 UTC

Another thing happening in your log there is that your command `git checkout #19888-etc` had exactly the same effect as just `git checkout`, because `#` starts a comment in shell syntax.

You can see that in the `git branch` output, where your `main` branch is still selected. This is also something that a graphical Git client like `gitk` would help make visible for you.

You can always escape the `#` by enclosing it in single quotes: `'#'`. But it's probably a good idea to leave `#` out of the names of your branches, because it's a pain to escape it all the time.

**Vighnesh Kulkarni** · 2021-10-16 08:48 UTC

Ohhh it worked..Thanks a lot @Greg Price!!


## Squash commits in a branch

*2021-10-20 to 2021-10-20 · 4 messages · [open in Zulip](https://chat.zulip.org/#narrow/channel/44-git-help/topic/Squash.20commits.20in.20a.20branch/with/1269013)*

**Jume Brice NN** · 2021-10-20 15:15 UTC

Hello, I need help getting my branch commits, into a single commit (no merge commits)

**shlok (madrix01)** · 2021-10-20 15:27 UTC

You can refer to [here](https://zulip.readthedocs.io/en/latest/git/fixing-commits.html#squashing-commits). Is this what you looking for ?

**Jume Brice NN** · 2021-10-20 15:30 UTC

Thanks @shlok patel(madrix01)

**shlok (madrix01)** · 2021-10-20 15:30 UTC

Happy to help !!


## ✔ git setup error

*2021-10-26 to 2021-11-02 · 28 messages · [open in Zulip](https://chat.zulip.org/#narrow/channel/44-git-help/topic/.E2.9C.94.20git.20setup.20error/with/1272300)*

**Amanda E** · 2021-10-26 19:57 UTC

Does anyone know how to fix this error?  I've been finding the instructions to set up the dev environment in Windows 10 to be outdated, so maybe this has a new path?  Any ideas?  Below is the screenshot of the error and the link to the docs page.  Thank you in advance!

https://zulip.readthedocs.io/en/latest/development/setup-advanced.html#installing-directly-on-windows-10-with-wsl-2

[git-clone-error-code.JPG](https://chat.zulip.org/user_uploads/2/c1/-fvpJ_p3YMpv7ft1mCJxCyG4/git-clone-error-code.JPG)

**Amanda E** · 2021-10-26 20:00 UTC

This is step 6, but I'm not sure I completely understood step 5, so the problem could be there, also.

**Amanda E** · 2021-10-26 20:06 UTC

I also tried restarting my wsl, but go this error.  It successfully installed, but this doesn't work to restart it.

**Amanda E** · 2021-10-26 20:06 UTC

[tools-line-error.JPG](https://chat.zulip.org/user_uploads/2/d8/ScyBNXixh3uKutOq1mMboezj/tools-line-error.JPG)

**Greg Price** · 2021-10-26 21:21 UTC

It looks like you're hitting an error at the step of cloning your fork from GitHub.

For that step, the docs link here for more details:
https://zulip.readthedocs.io/en/latest/git/cloning.html#step-1b-clone-to-your-machine

This may be the line there that you want:
> Note: If you receive an error while cloning, you may not have [added your ssh key to GitHub](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account).

**Greg Price** · 2021-10-26 21:23 UTC

The next step, running `./tools/wsl/start_services`, can only work after you've successfully cloned the repo, because that's a script inside the Zulip repository.

**Amanda E** · 2021-10-27 15:03 UTC

Thanks, Greg.
Your answer sent me on the right track.  I also had to reconfigure my BIOS system to allow WSL, run Ubantu as an administrator, and go into github to fork the repo before pulling it.  The last one is obvious, I know, but since I was doing everything else from the command line, it wasn't obvious I had to switch over to the website for that part, and the documentation skipped it.

I pulled the repo using https.  I have a working ssh key, but it isn't recognized in wsl.  It seems to be a common problem, so I'm reading about it now.  It isn't a big deal, so if it is a complicated fix, I'll probably just use https instead.

Just FYI, installing wsl now automatically installs the latest version of Ubantu, so the instructions to go to the microstoft store and download it are somewhat confusing.  The instructions to add the ports in the config file was a hiccup because they came up automatically.   Also, I happened to know about vim, but some basic instruction on how to add/verify the node details in the vim editor would be helpful for many.   One last note, just as a heads up, it looks like windows 11 will be switching to a Hyper-V installation, which is similar but (of course) slightly different than both the current hyper-v for enterprise and the windows 10 installation. 

Thanks, again!

**Amanda E** · 2021-10-27 15:21 UTC

re: ssh key
It looks like it is possible to use the same key in wsl and Windows 10, but it is easier/less error prone to set up separate ssh keys for each.  Now that I've set up my wsl with https, it would be another step to switch them over to ssh, so for the moment, I'm going to stay with https for the moment.  
That's a possible documentation update, too, because it is easier to set up the separate key or create the secondary copy before setting up the git connections.

**Greg Price** · 2021-10-27 17:56 UTC

Thanks for all those detailed notes! We'd certainly appreciate a PR to make these updates and fixes to the instructions :smile:

**Greg Price** · 2021-10-27 17:58 UTC

(replying to Amanda E)
> The last one is obvious, I know, but since I was doing everything else from the command line, it wasn't obvious I had to switch over to the website for that part, and the documentation skipped it.

Mmm, yeah. It's described in the first step on this page:
https://zulip.readthedocs.io/en/latest/git/cloning.html
but those WSL instructions link straight to the second step (step 1b) and don't mention the first. That'd be good to adjust.

**Greg Price** · 2021-10-27 18:03 UTC

(replying to Amanda E)
> I pulled the repo using https. I have a working ssh key, but it isn't recognized in wsl. It seems to be a common problem, so I'm reading about it now. It isn't a big deal, so if it is a complicated fix, I'll probably just use https instead.

The way I'd recommend doing this is to generate an SSH key inside the WSL system, following the same steps as you'd do (following e.g. GitHub's instructions) on any Linux system that wasn't WSL.

I see some instructions on the web about sharing an SSH key between WSL and the Windows system outside it. Those look complicated, and there's no benefit to that. The normal recommended way to use SSH keys is to have a separate key generated on each machine you use; you can add as many SSH keys to GitHub (or other places you might SSH to) as you like.

... Ah, and I see in your last message that you reached the same conclusion :smile:

**Greg Price** · 2021-10-27 18:11 UTC

(replying to Amanda E)
> Also, I happened to know about vim, but some basic instruction on how to add/verify the node details in the vim editor would be helpful for many.

Oof, yeah. I wouldn't call for vim in a set of instructions like this. `nano` would be a better recommendation there (if it's installed by default, which I hope it is) -- it's an editor with a much more straightforward interface.

`nano` is the same editor I recommend setting up Git to use, for anyone who isn't already a regular user of either Emacs or vim.

**Amanda E** · 2021-10-27 18:50 UTC

I'd be glad to do a PR on these things.  It would be easy since I just went through them - but I'm not sure it would be enough for the Outreachy contribution period.  I had a crisis in my family, so I'm running late to complete a contribution.

You mentioned this page:   https://zulip.readthedocs.io/en/latest/git/cloning

I was working off of this page:  https://zulip.readthedocs.io/en/latest/development/setup-advanced.html#installing-directly-on-windows-10-with-wsl-2  This was the recommend setup instructions from this page: https://zulip.readthedocs.io/en/latest/development/setup-vagrant.html#windows-10

It is interesting that there are two different pages for the same thing.

As I mentioned before, I think I should probably go for something a little more for outreachy, but if I do com back to this later, what would the command line be in [step four](https://zulip.readthedocs.io/en/latest/development/setup-advanced.html#installing-directly-on-windows-10-with-wsl-2)?  It looks like this specifically calls for vim.

Thanks again.

**Greg Price** · 2021-10-27 19:41 UTC

Sure, no rush.

**Greg Price** · 2021-10-27 19:47 UTC

(replying to Amanda E)
> You mentioned this page: https://zulip.readthedocs.io/en/latest/git/cloning I was working off of this page: https://zulip.readthedocs.io/en/latest/development/setup-advanced.html#installing-directly-on-windows-10-with-wsl-2 This was the recommend setup instructions from this page: https://zulip.read …

I mentioned that git/cloning page because it's what those WSL instructions link to in step 6:
> Clone your fork of the Zulip repository and connecting the Zulip upstream repository:

where "Clone your fork of the Zulip repository" is a link.

I think those two pages have pretty different jobs: one of them goes into detail on the interaction with GitHub and getting a local clone of the repo, independent of what OS you're on, while the other is about setting up the development environment specifically on WSL. So the WSL instructions need to mention forking and cloning the repo and to give the key commands for it, but it's good for the detailed version of that to live on a different page (where it can be shared by the setup instructions for Vagrant and others.)

Definitely that reference in the WSL instructions can be made clearer, though. For one thing it could explicitly mention forking the Zulip repo, rather than just referring to "your fork" and implicitly expecting you've already done so.

**Greg Price** · 2021-10-27 19:50 UTC

(replying to Amanda E)
> if I do com back to this later, what would the command line be in [step four](https://zulip.readthedocs.io/en/latest/development/setup-advanced.html#installing-directly-on-windows-10-with-wsl-2)? It looks like this specifically calls for vim.

I'd just have it say
```
sudo nano /etc/rabbitmq/rabbitmq-env.conf
```
instead of the current
```
sudo vim /etc/rabbitmq/rabbitmq-env.conf
```

The one thing that requires besides making the edit is to fact-check that Nano is actually installed on your fresh WSL environment -- that if you type the `nano` version of that command, it successfully fires up a text editor for you (rather than an error about the command not being found.) I expect it is, but don't have a WSL environment handy to confirm.

**Amanda E** · 2021-10-27 20:14 UTC

nano comes up on my wsl.   I'll include that change if I come back to it.
Thanks for all your feedback.  I appreciate it.

**Notification Bot** · 2021-10-27 20:16 UTC

@Amanda E has marked this topic as resolved.

**Notification Bot** · 2021-10-27 20:16 UTC

@Amanda E has marked this topic as unresolved.

**Notification Bot** · 2021-10-27 20:16 UTC

@Amanda E has marked this topic as resolved.

**Amanda E** · 2021-10-29 22:11 UTC

@Greg Price  I've completed this pull request (#20103).  Thanks again for your help.

**Greg Price** · 2021-10-29 23:49 UTC

Thank you! I left some comments there.

**Amanda E** · 2021-11-01 02:16 UTC

@Greg Price  Updates and a couple of questions at PR #20103.

**Amanda E** · 2021-11-01 19:24 UTC

Everything should be good to go for PR 20103.  Let me know what you think.  Thanks again!

**Tim Abbott** · 2021-11-01 22:18 UTC

@Amanda E it looks like there's a failure in CI that you should investigate.

**Amanda E** · 2021-11-01 22:29 UTC

On it. 
Thanks!

**Amanda E** · 2021-11-02 00:15 UTC

@Tim Abbott  All checks pass now!

**Amanda E** · 2021-11-02 21:03 UTC

@Tim Abbott .  I received your note and will make sure to use the tools/build-docs next time.  Thanks for all your help!


## Creating a PR

*2021-10-29 to 2021-10-29 · 4 messages · [open in Zulip](https://chat.zulip.org/#narrow/channel/44-git-help/topic/Creating.20a.20PR/with/1273986)*

**Aryan Gurjar Banke** · 2021-10-29 16:07 UTC

I am new to Open source ,I am currently working on the issue #1087. After resolving the Padding problem, I did a commit form the VS code itself using there GUI but now I don't now how to raise a PR should it be raised from the forked repository or the official repository. Can someone please help

**Akash Dhiman** · 2021-10-29 16:15 UTC

Once you are satisfied with your commits, you should push your code to your remote repository i.e. your fork (it should be called origin by default in your git client if you cloned the fork), I think you can push the changes from vscode as well.

Once you do that head over to the official repository url or your fork url in your browser and you will see a prompt to make a PR at the top of the page.

A more comprehensive guide to make PR can be found here: https://docs.github.com/en/github/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request

Some zulip relevant things while making a PR can be found here: https://zulip.readthedocs.io/en/latest/git/pull-requests.html

**Aryan Gurjar Banke** · 2021-10-29 16:50 UTC

Thanks it helped, I have created my first PR :smiley:

**Aryan Gurjar Banke** · 2021-10-29 16:54 UTC

Thanks it helped, I have created my first PR :smiley:


## removing a commit

*2021-10-29 to 2021-11-03 · 14 messages · [open in Zulip](https://chat.zulip.org/#narrow/channel/44-git-help/topic/removing.20a.20commit/with/1274214)*

**Amanda E** · 2021-10-29 22:59 UTC

I accidentally pushed two commits to the wrong branch of my fork on GitHub.  I have also pushed them to the correct branch.  I have been reading the docs, but when I did `git rm <sha>`, it says `fatal: pathspec 'd456f4c0dd1d7c75bc507effa08d3676cb6c5501' did not match any files`  Stack overflow talks about a `git push -f ` with the last good commit - but I want to remove all of the commits.  Thoughts or pointers to a reference?  Thanks in advance.

**Greg Price** · 2021-10-29 23:28 UTC

Yeah, `git push -f` is the command that will do that.

A branch in Git points to some one commit at any given time. The commits that one thinks of as "in the branch" are then the commits that are part of the history of that commit -- its ancestors -- other than the commits that are also ancestors of the main branch.

So if you have the branch pointing to commit C, and you use `git push -f` to make it point instead to the grandparent of C, then the commits "in the branch" will consist of the grandparent's ancestors, and won't include C or its parent.

**Greg Price** · 2021-10-29 23:31 UTC

If you haven't already, I'd highly recommend setting up and using `gitk` or another graphical Git viewer:
https://zulip.readthedocs.io/en/latest/git/setup.html#get-a-graphical-client

That'll be very helpful for getting a picture of what's going on in your repository and the different branches in it, and seeing visually both the branches as pointers to (or labels on) specific commits, and then those commits' ancestors forming the commits that are "in" the branch.

**Amanda E** · 2021-11-01 02:22 UTC

Thank you for this explanation.  It is helpful.
I do have gitk set up.  I'm still on the steep part of it's learning curve, but I'm getting there.

**Greg Price** · 2021-11-01 17:41 UTC

Great!

**Amanda E** · 2021-11-03 16:10 UTC

I'm still struggling with these commits.
I ran `git push -f` a few days ago, and it seemed to work in the command line, but the commits were still on GitHub.  I didn't think much of this and continued working, which I can now see wasn't the best idea. 

Now my command line says
`git rebase upstream/main`
> ```bash First, rewinding head to replay your work on top of it... Applying: update: Update instructions for Windows 10 installation Using index info to reconstruct a base tree... M docs/development/setup-advanced.md Falling back to patching base and 3-way merge... Auto-merging docs/development/setup …
```
And GitHub says "This branch is 24 commits behind upstream and has commits which must be resolved.  Open a Pull request to fetch upstream and review changes or resolve conflicts."  (see screenshot)

I ran `git rebase -i HEAD~10` and marked drop on the commits which should be removed.  This didn't work.  It came back to a similar message to above.  I then ran it again and deleted the commits.  This also didn't work.

I also looked at what needed resolved in the files, but they are very outdated to the newly pulled file, so I'm not sure what to do with this.  I can get the corrected code and past it in, and then run `git rm/add` (from above), if that would help.

I have it pulled up on gitk, with screenshot below, but I'm not exactly sure how to use this information.

Thoughts?  Pointers?  Tips? 
Thanks in advance!

[24commits.JPG](https://chat.zulip.org/user_uploads/2/45/Zg0fJ6ZNnoC4BYNH3DnC0kAf/24commits.JPG) 
[gitk11.3.21.JPG](https://chat.zulip.org/user_uploads/2/22/cRWgSGa2QKqWC7UpcrtNV_lS/gitk11.3.21.JPG)

**Aman (amanagr)** · 2021-11-03 16:17 UTC

If you have the correct commits in your local branch, you should run `git pull --rebase upstream/main`, resolve the conflicts like the one you see above with `setup-advanced.md` file. Then when you are sure that your commit history looks fine locally and the changes are correct, do
`git push -f origin <branch name>`.

**Amanda E** · 2021-11-03 16:25 UTC

Thank you. 
I don't have the commits in my local file.  I used to have them, but deleted the feature branch after the pull request was completed.   I can copy the code off of the zulip/zulip repository and paste it in, save the file and then follow your instructions.  Would that work?

**Aman (amanagr)** · 2021-11-03 16:26 UTC

I don't understand, what are you trying to do?

**Amanda E** · 2021-11-03 16:30 UTC

I accidentally uploaded these to the wrong branch.  I put them on my main branch instead of the feature branch.  I then uploaded them to the feature branch and created a pull request.  The pull request was accepted, and I then deleted the feature branch.  Now these accidental commits are out of date with everything, and locking up the main branch.  GitHub won't let me do anything, including rebasing my fork of the zulip repo.

**Amanda E** · 2021-11-03 16:30 UTC

Does that make sense?

**Aman (amanagr)** · 2021-11-03 16:46 UTC

Oh! That's simple. Just do:
```
git fetch upstream
git checkout main
git reset --hard upstream/main
git push -f origin main (optional)
```

Your main branch doesn't matter in general.

**Amanda E** · 2021-11-03 16:47 UTC

Trying that now!

**Amanda E** · 2021-11-03 16:52 UTC

That worked!  Thank you so much!  I had spent hours trying to figure out how to do this! 
Have a great day!


## Linking PR to issue

*2021-10-30 to 2021-10-30 · 5 messages · [open in Zulip](https://chat.zulip.org/#narrow/channel/44-git-help/topic/Linking.20PR.20to.20issue/with/1274392)*

**Aryan Gurjar Banke** · 2021-10-30 06:13 UTC

I am trying to link my PR to the issue, But the link PR option is not getting clicked. So, can someone please tell me how to link my PR to the issue. Thank you!

**shlok (madrix01)** · 2021-10-30 11:17 UTC

@Aryan Gurjar Banke you can refer to the [github](https://docs.github.com/en/issues/tracking-your-work-with-issues/linking-a-pull-request-to-an-issue) documentation.

**Aryan Gurjar Banke** · 2021-10-30 11:20 UTC

I did saw the article there it is mentioned to click the link Pull Request and select over pull request, but for my case the link PR is not clickable.

**shlok (madrix01)** · 2021-10-30 11:37 UTC

You can add `Issue #200XX` in your PR message. It will automatically link issue to the PR

**Aryan Gurjar Banke** · 2021-10-30 15:26 UTC

Thanks it worked, I did Fixes zulip/zulip-desktop#1087 and it got linked.


## squashing fixup commits

*2021-10-30 to 2025-12-19 · 14 messages · [open in Zulip](https://chat.zulip.org/#narrow/channel/44-git-help/topic/squashing.20fixup.20commits/with/1274469)*

**Ngulefac Benazea** · 2021-10-30 20:26 UTC

Hello  @Chris Bobbe  please could you help me point out some of the commits that are related to each other here ? https://github.com/zulip/zulip-mobile/pull/5078  as pointed by @Greg Price .

**Greg Price** · 2021-11-01 17:35 UTC

(No need to @-mention; we'll see all messages on any relevant stream.)

Here's the commits in the PR:
```
ad3429d51 drawer: Add Drawer and drawer icon to top left
dec21ba1a fix: Resolving conflicts on android/build.gradle
74ff97a6f search icon:Send search icon to bottom navigation bar
1e6765211 drawer: Add organization name next to logo on drawer
5862496f2 real_name: Store real_name in redux
4a521f76e fix: Remove package-lock.json deleted package-lock.json since the project uses yarn and not npm Removed the uneanted chages made in android/build.gradle
3b48ad065 fix: Adjust formatting of code
```

Several of those commits are making fixes to previous commits in the PR. Instead, each commit should be a coherent change that's correct on its own. That means fixes like those should generally be squashed into the commits they fix.

Here's a docs section Chris linked to on the PR, which has pointers to more details about this and to how to fix it:
https://zulip.readthedocs.io/en/latest/git/using.html#examine-and-tidy-your-commit-history

**Ngulefac Benazea** · 2021-11-02 12:06 UTC

I just did some clean up on the commits. Please can you check those

**Greg Price** · 2021-11-02 18:08 UTC

Here's the commits on the PR now:
```
d1439cbcd drawer: Add Drawer and drawer icon to top left
d03c5750f fix: Remove package-lock.json deleted package-lock.json since the project uses yarn and not npm Removed the uneanted chages made in android/build.gradle
2e9d73993 fix: Adjust formatting of code
```

That's shorter, but there are still two commits that are fixing up a previous commit, which means the first commit isn't a coherent correct change on its own.

**Greg Price** · 2021-11-02 18:13 UTC

Also there are several different things going on, too much for one commit. Those should be separate so that each commit is doing a single coherent thing. Here's more on that idea:
https://zulip.readthedocs.io/en/latest/contributing/version-control.html

In the previous revision, the commit messages -- other than the fixup commits -- suggested a pretty reasonable separation of ideas:

```
ad3429d51 drawer: Add Drawer and drawer icon to top left
74ff97a6f search icon:Send search icon to bottom navigation bar
1e6765211 drawer: Add organization name next to logo on drawer
5862496f2 real_name: Store real_name in redux
```

Storing some new data from the server in Redux (here, the realm's name) is a good example of something to keep separate from a commit making major UI changes.

**Ayush khatri** · 2024-11-12 19:19 UTC

Someone please help, I want to commit just 1 of these, by mistake I committed 4 and now 4 is showing, what should I do?
[Screenshot (50).png](https://chat.zulip.org/user_uploads/2/86/036fVcurZ6skpQl4rt73GWWg/Screenshot-50.png)

**Tim Abbott** · 2024-11-12 20:00 UTC

https://zulip.readthedocs.io/en/latest/git/fixing-commits.html

**Notification Bot** · 2024-11-12 20:02 UTC

2 messages were moved here from #**git help>git checkout** by @Tim Abbott.

**Tim Abbott** · 2024-11-12 20:02 UTC

@Ayush khatri moved this to a more appropriate topic. Please pay attention to topics when asking questions.

**Khanak Khandelwal** · 2025-12-12 07:11 UTC

Hii , I have a doubt relating to squash 
I was asked to squash my fixup commits into the main commit. I did : 
git rebase -i HEAD~8 
since I had committed 8 times), then marked all commits as `s` except for 1, removed all the other commits, and pushed 
However, on GitHub, it shows:

> There isn’t anything to compare.
> 2e6356b1b363cf0c9711dbbb5c68f451a495decb and 4f5080d8b103023cb21a605485a65457dd361c46 are identical.

Why is this happening?

When I do:
`git log --oneline origin/main..HEAD`
It shows only:
`4f5080d8 (HEAD -> fix-empty-topic-list-2003, origin/fix-empty-topic-list-2003) topic_list: Add empty state placeholder for channels with no topics Fixes: #2003`

could you please help me ?

**Greg Price** · 2025-12-12 19:09 UTC

(replying to Khanak Khandelwal)
> When I do: `git log --oneline origin/main..HEAD` It shows only: `4f5080d8 (HEAD -> fix-empty-topic-list-2003, origin/fix-empty-topic-list-2003) topic_list: Add empty state placeholder for channels with no topics Fixes: #2003`

Looks like you've successfully produced a single commit.

**Greg Price** · 2025-12-12 19:10 UTC

> I was asked to squash my fixup commits into the main commit. I did : git rebase -i HEAD~8 since I had committed 8 times), then marked all commits as `s` except for 1, removed all the other commits, and pushed

And this sounds like a good way to do it.

**Greg Price** · 2025-12-12 19:12 UTC

(replying to Khanak Khandelwal)
> However, on GitHub, it shows: > There isn’t anything to compare. > 2e6356b1b363cf0c9711dbbb5c68f451a495decb and 4f5080d8b103023cb21a605485a65457dd361c46 are identical. Why is this happening?

Well, you haven't said what question you asked GitHub — what page you're looking at, or how you got there or what you did there. So it's hard to say much about what this answer from GitHub means.

(You also haven't said anything about what that commit 2e6356b1b363cf0c9711dbbb5c68f451a495decb might be.)

What did you do to get this response from GitHub, and what response did you expect?

**Khanak Khandelwal** · 2025-12-19 19:27 UTC

Sorry for the delayed response , The issue is resolved now. After rechecking, the squash was done correctly and the branch does contain a single commit on top of `main`, which is why GitHub showed “There isn’t anything to compare” at that point .


## Need help with PR

*2021-11-02 to 2024-10-29 · 23 messages · [open in Zulip](https://chat.zulip.org/#narrow/channel/44-git-help/topic/Need.20help.20with.20PR/with/1275289)*

**Efemena Esiri** · 2021-11-02 13:28 UTC

I'm trying to resolve the conflict on this PR.
What should I do next.. you can see the commit history 
https://github.com/zulip/zulip-mobile/pull/5073

**Greg Price** · 2021-11-02 18:05 UTC

Here's the instructions I gave originally:

(replying to Greg Price)
> It looks like the Git history in your branch is currently a bit complex, with a merge commit. We don't use merge commits in the Zulip project; for this change, we'll want just one commit. Take a look at our Git guide: https://zulip.readthedocs.io/en/latest/git/index.html and I highly recommend using …

What have you tried so far, and what were the results?

**Efemena Esiri** · 2021-11-03 20:35 UTC

To resolve the merge commit, I did a  revert on the commit
using 
```
git revert adb82375654c4b2e4e2cedd9941f328af169c4b5 -m 1
```
Where the hash is the merge commit from git log

**Greg Price** · 2021-11-03 22:06 UTC

I see. `git revert` adds a new commit on top, so that's not the thing you want -- all the previous commits are still there as part of that commit's ancestors, including the merge commits.

Have you set up a graphical Git viewer? What does it show you as the contents of your branch? That will help a lot in seeing the effects of the commands you try.

**Greg Price** · 2021-11-03 22:11 UTC

Then the goal is to make the branch into a single linear sequence of commits, with no merge commits, and where each commit makes sense on its own. More discussion here:
https://zulip.readthedocs.io/en/latest/contributing/version-control.html

In particular, there should be no commits that revert or fix up earlier commits in the branch, because that means the earlier commit didn't make sense on its own.

**Greg Price** · 2021-11-03 22:12 UTC

If you show a screenshot here of what you see in your graphical Git viewer (see above in this thread for links on how to set one up), that will help us see what you're seeing so that we can better help you figure things out.

**Efemena Esiri** · 2021-11-04 20:37 UTC

Help!!!  
I was able to resolve the commit to  two commit and do not reference any  unwanted commit or merge
https://github.com/Somena1/zulip-mobile/commits/Fix-split-screen

But along the line I ran a command as the GUI tool (SourceTree) was throwing an error
```git push -f --mirror ```
This ended up deleting the remote branch before pushing and closed the PR.
How do I re-open the PR?

**Greg Price** · 2021-11-04 22:32 UTC

I'd start by pushing the branch again.

**Greg Price** · 2021-11-04 22:32 UTC

If GitHub won't let you re-open the PR then, you can open a new one using the branch.

**Greg Price** · 2021-11-04 22:34 UTC

I think `git push --mirror` is not likely to be an option you want -- the things it's useful for aren't really in normal development workflows. For a normal development workflow, the default behavior of `git push` without `--mirror` is going to be closer.

**Greg Price** · 2021-11-04 22:35 UTC

A useful tool I'd recommend is `git push -n`, aka `git push --dry-run`. This will tell you what your `git push` command would have done, without actually doing it.

So for example if you were about to say `git push -f --mirror` but weren't sure exactly what it would do, you could run `git push -n -f --mirror`, and it'd tell you. That's helpful in experimenting with different forms of `git push` command.

**Greg Price** · 2021-11-04 22:38 UTC

But then more specifically, I recommend always saying explicitly what branch you want to push, unless you're very sure (like after testing with `-n`) what it would do.

So for example `git push origin +Fix-split-screen` will update that one branch to your new version of it, and do nothing else.

**Efemena Esiri** · 2021-11-04 23:45 UTC

Wow.. thank you, seems I won't be breaking my branch again.

**Efemena Esiri** · 2021-11-05 00:01 UTC

I've opened the PR here

https://github.com/zulip/zulip-mobile/pull/5104

**Shashank Singh** · 2021-12-03 07:11 UTC

Hello everyone! I was messing around with git and accidentally git pulled the Zulip remote repo which messed up the commit history. Is there a way I can squash 2 commits just using both commit IDs? I couldn't use git rebase -i HEAD because it won't show my very first commit in the local repo to begin with :) [PR#20232](https://github.com/zulip/zulip/pull/20232)

**Parth Mittal** · 2021-12-03 08:59 UTC

(replying to Shashank Singh)
> Hello everyone! I was messing around with git and accidentally git pulled the Zulip remote repo which messed up the commit history.
@Shashank Singh  Even I had git pulled. You can revert back to the last desired commit using [this doc](https://zulip.readthedocs.io/en/latest/git/troubleshooting.html?highlight=getting%20out%20of%20trouble#undo-a-merge-commit). Then you can have a look at [this](https://chat.zulip.org/#narrow/stream/49-development-help/topic/Best.20way.20to.20resolve.20merge.20conflicts.3F)

**Santam Roy Choudhury** · 2021-12-09 18:55 UTC

I need some help with my [PR](https://github.com/zulip/zulip/pull/20472) . I messed it up by previously pulling new changes from the master to this branch. I tried to rebase and delete all the commits from master and tried to force push . As it turns out, the PR got closed and currently I have no commits in it. Is there a way to reopen the PR and then push a new commit in it again?

**Tim Abbott** · 2021-12-09 19:38 UTC

@Santam Roy Choudhury sadly no; GitHub for some reason doesn't allow reopening a PR closed this way.  You can just a make a new one and link them; and then spend a bit more time learning `Git` to avoid this in the future.  (`gitk --all` can very much help avoid this)

**Tim Abbott** · 2021-12-09 19:38 UTC

You can find your commits using `git reflog`, if you lost track of them locally.

**Tim Abbott** · 2021-12-09 19:38 UTC

Check out of Git guide for reading that'll help you with this in the future.

**Chikezirim Orioha** · 2024-10-29 04:35 UTC

Please can someone check on this PR and help me with what I'm doing wrong #988

**Aditya Kasaudhan** · 2024-10-29 13:28 UTC

It looks like you referenced the wrong PR here.

**Lauryn Menard** · 2024-10-29 14:06 UTC

Looks like this is for the Zulip Flutter repository: #F988.


## error by command: tools/lint

*2021-11-02 to 2024-03-15 · 4 messages · [open in Zulip](https://chat.zulip.org/#narrow/channel/44-git-help/topic/error.20by.20command.3A.20tools.2Flint/with/1275391)*

**Axay Sagathiya** · 2021-11-02 17:13 UTC

gitlint   | fatal: ambiguous argument 'upstream/main..HEAD': unknown revision or path not in the working tree.
gitlint   | Use '--' to separate paths from revisions, like this:
gitlint   | 'git <command> [<revision>...] -- [<file>...]'



Can anyone help me with this ?

**Alex Vandiver** · 2021-11-02 17:37 UTC

This is happening because git can't find an `upstream/main` branch.

Did you follow the instructions at https://zulip.readthedocs.io/en/latest/git/cloning.html#step-1c-connect-your-fork-to-zulip-upstream ?

**Kirsty Williams** · 2024-03-15 02:19 UTC

Hi there! I've been having an issue with my pull request, I've tried fixing on my own but no luck so far. I'm using a windows 11 home device with a linux subsystem, and worked on the 
> Settings UI Panel Issue
However, when checks are run after upload i'm having both frontend and backend lint issues like this:
[image.png](https://chat.zulip.org/user_uploads/2/43/TY3YsahMVP5kuLqFGpCXNR6A/image.png)

Even though I haven't made any changes to these files.

**Anders Kaseorg** · 2024-03-15 05:41 UTC

If you want help, you’ll need to provide the complete error, not just the top half of one, and please provide it in a [Zulip code block](https://chat.zulip.org/help/code-blocks), not a screenshot.


## How to get fresh copy

*2021-11-04 to 2021-11-05 · 5 messages · [open in Zulip](https://chat.zulip.org/#narrow/channel/44-git-help/topic/How.20to.20get.20fresh.20copy/with/1276471)*

**Harsit Sinha** · 2021-11-04 11:37 UTC

I had set up the development area on vagrant and using the steps cloned the repository. I have not done any changes on my local system. Now when I use git status. I get this
[image.png](https://chat.zulip.org/user_uploads/2/a5/mhq-eFasLTO8yEi8S42x2_H4/image.png) 
Is there a way to get the latest copy . Should I again use git clone?

**Akash Dhiman** · 2021-11-04 11:44 UTC

This has nothing to do with how you have setup the development environment but rather the way your local clone is modified, the message says that your main branch of the local clone of the repo (the one in your machine) has 34 more commits than the one in origin/main.

This answer may help you further understand and change this: https://stackoverflow.com/questions/16288176/your-branch-is-ahead-of-origin-master-by-3-commits

**Harsit Sinha** · 2021-11-04 13:01 UTC

Thanks a lot. 
That means i should not worry about those 34 commits

**Greg Price** · 2021-11-04 22:41 UTC

That's right. It's also handy to change what comparison Git makes there, so that it tells you more useful information:
```
$ git branch --set-upstream-to upstream/main
```

Then Git will tell you about the comparison of your branch to `upstream/main`, which is much more interesting than `origin/main`. If you've cloned in the recommended way, then `origin` is your own fork and `upstream` is the upstream repo zulip/zulip where development goes to, so `upstream/main` is a useful thing to know how your branch compares to.

**Harsit Sinha** · 2021-11-05 06:36 UTC

That helps a lot, Thanks


## commit error during test

*2021-11-06 to 2021-11-07 · 3 messages · [open in Zulip](https://chat.zulip.org/#narrow/channel/44-git-help/topic/commit.20error.20during.20test/with/1277545)*

**Axay Sagathiya** · 2021-11-06 14:14 UTC

gitlint   | Commit 4602e8b61c:
gitlint   | 1: T7 Title does not match regex (^(.+:\ )?[A-Z].+\.$): "run prettier"
gitlint   | 
gitlint   | Commit 52f377ed59:
gitlint   | 1: T7 Title does not match regex (^(.+:\ )?[A-Z].+\.$): "hide square bracket around emoji"
gitlint   | 
gitlint   | Commit 35415c510d:
gitlint   | 1: T7 Title does not match regex (^(.+:\ )?[A-Z].+\.$): "fixed indentation"
gitlint   | 1: Z1 The first word in commit title should be in imperative mood ("fixed" -> "fix"): "fixed indentation"
gitlint   | 
gitlint   | Commit 46c5079233:
gitlint   | 1: T7 Title does not match regex (^(.+:\ )?[A-Z].+\.$): "Added name of status emoji in tooltip"
gitlint   | 1: Z1 The first word in commit title should be in imperative mood ("added" -> "add"): "Added name of status emoji in tooltip"
------------------------------------------------------------------------------------------------------------
I am getting the above text while testing. how can I resolve this?

**Manan Rathi** · 2021-11-06 14:22 UTC

Hi @Axay Sagathiya . I guess [this](https://zulip.readthedocs.io/en/latest/contributing/version-control.html#commit-messages) might help!

**Axay Sagathiya** · 2021-11-07 15:50 UTC

@Manan Rathi Thanks. it works.


## ssh key

*2021-11-16 to 2021-11-17 · 16 messages · [open in Zulip](https://chat.zulip.org/#narrow/channel/44-git-help/topic/ssh.20key/with/1282493)*

**Amanda E** · 2021-11-16 18:36 UTC

I have a "pebble in my shoe" problem.  It isn't the end of the world, but quite annoying none the less.  I can't get an ssh key for GitHub in WSL.   I can, of course, type in the personal authentication token each time, which is what I've been doing.  It is just difficult and annoying to type correctly.   It seems like I should be able to paste it into my Ubuntu terminal, but it doesn't allow me to.  I have double checked my settings and tried all the possible paste commands (^v, shift^v, ^ins).   Anyone know any special magic for this?

 I followed the [GitHub directions](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account) and have an ssh key on my machine (Windows 10), which works fine, but those directions won't work in the WSL terminal.  This produces a `id_ed25519.pub` key.  This is the type of key I need, but WSL can't access it.

I followed the [Ubuntu directions](https://ubuntu.com/tutorials/ssh-keygen-on-windows#3-key-generation-with-ubuntu-on-wsl) in WSL to create a key for the virtual machine, but it produces a `ssh-rsa` key, which isn't valid for GitHub. 

I tried a few ways to copy my .shh folder from my machine to WSL, but none were successful.  I didn't keep notes on those, so I can't list out those tries - sorry about that.

Any ideas, thoughts, work-arounds? 

Thanks in advance!

**Greg Price** · 2021-11-16 19:40 UTC

Have you tried following GitHub's directions for generating a key on Linux?
https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent

**Anders Kaseorg** · 2021-11-16 19:40 UTC

You can generate an ed25519 key with `ssh-keygen -t ed25519`.

Or, you can [connect](https://docs.microsoft.com/en-us/windows/wsl/tutorials/wsl-git#git-credential-manager-setup) WSL to the Windows Git Credential Manager and use https rather than ssh.

**Greg Price** · 2021-11-16 19:41 UTC

It's a shame that Ubuntu in 2021 is still telling you to generate an RSA key.

**Amanda E** · 2021-11-16 19:43 UTC

Trying those things now.

**Amanda E** · 2021-11-16 19:44 UTC

(replying to Greg Price)
> It's a shame that Ubuntu in 2021 is still telling you to generate an RSA key.
It uses the ssh generator in Windows to create the key for WSL - so it is a Windows 10 problem, not a Ubuntu problem...

**Greg Price** · 2021-11-16 19:45 UTC

It says:
> `ssh-keygen -t rsa`

That's a problem in that doc. `ssh-keygen` will generate the type of key you ask it to generate, and they're telling you to ask for RSA.

**Amanda E** · 2021-11-16 20:07 UTC

@Greg Price   That makes sense about the instructions.  It is easy for those things to fall through the cracks.

The WSL shell generated the correct kind of key, but  now it won't add to the ssh agent.


Here's the log of what I've tried.
```bash
(zulip-py3-venv) zulipdev2021@DESKTO:~$ eval "$(ssh-agent -s)
> Agent pid 59566
> ^C
(zulip-py3-venv) zulipdev2021@DESKTO:~$ sudo -s -H
[sudo] password for zulipdev2021:
root@DESKTO:/home/zulipdev2021# eval "$(ssh-agent -s)"
Agent pid 4928
root@DESKTO:/home/zulipdev2021# ssh-add ~/.ssh/id_ed25519
/root/.ssh/id_ed25519: No such file or directory
root@DESKTO:/home/zulipdev2021# cd/zulipdev2021@DESKTO:
bash: cd/zulipdev2021@DESKTO: No such file or directory
root@DESKTO:/home/zulipdev2021# exit
exit
(zulip-py3-venv) zulipdev2021@DESKTO:~$ ssh-add ~/.ssh/id_ed25519
Could not open a connection to your authentication agent.
(zulip-py3-venv) zulipdev2021@DESKTO:~$ exec shh-agent bash
-bash: exec: shh-agent: not found
(zulip-py3-venv) zulipdev2021@DESKTO:~$ exec shh-agent zsh
-bash: exec: shh-agent: not found
(zulip-py3-venv) zulipdev2021@DESKTO:~$ sudo -s -H
root@DESKTO:/home/zulipdev2021# eval "($ssh-agent -s)"
-agent: command not found
root@DESKTO:/home/zulipdev2021# eval "$(ssh-agent -s)
> Agent pid 59566
> ssh-add ~/ .ssh/id_ed25519
> exit
> ^C
root@DESKTO:/home/zulipdev2021# exit
exit
(zulip-py3-venv) zulipdev2021@DESKTO:~$ sudo -s -H
root@DESKTO:/home/zulipdev2021# eval "$(ssh-agent -s)
>
```

**Greg Price** · 2021-11-16 20:14 UTC

Several of those commands are missing a close-quote `"`. Without that, the next things you type are part of the string that's the argument to `eval`, which isn't what you want.

**Amanda E** · 2021-11-16 20:15 UTC

I'll try it again.  I'm sorry for making you spot my typo...

**Amanda E** · 2021-11-16 20:30 UTC

As can be seen below, this still wasn't working , so I decided to check for existing keys, in case the old rsa key was causing a problem.  It looks like I might actually have 28 ssh keys.  I'm not sure how I did that!  Do you know how to add any of these to GitHub?  I might need to delete all but one first?  How is that done?  The commands from the GitHub [page](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account) aren't working.


```bash
(zulip-py3-venv) zulipdev2021@DESKTO:~$ ssh-add ~/.ssh/id_ed25519
Could not open a connection to your authentication agent.
(zulip-py3-venv) zulipdev2021@DESKTO:~$ sudo -s -H
root@DESKTOhome/zulipdev2021# zulipdev2021
zulipdev2021: command not found
root@DESKTO:/home/zulipdev2021# eval "$(ssh-agent -s)"
Agent pid 11075
root@DESKTO:/home/zulipdev2021# ssh-add ~/.ssh/id_ed25519
/root/.ssh/id_ed25519: No such file or directory
root@DESKTO:/home/zulipdev2021# exit
exit
(zulip-py3-venv) zulipdev2021@DESKTO:~$ ls -al ~/.ssh
total 28
drwx------  2 zulipdev2021 zulipdev2021 4096 Nov 16 13:47 .
drwxr-xr-x 12 zulipdev2021 zulipdev2021 4096 Nov  3 13:30 ..
-rw-------  1 zulipdev2021 zulipdev2021  419 Nov 16 13:47 id_ed25519
-rw-r--r--  1 zulipdev2021 zulipdev2021  104 Nov 16 13:47 id_ed25519.pub
-rw-------  1 zulipdev2021 zulipdev2021 2622 Oct 31 16:24 id_rsa
-rw-r--r--  1 zulipdev2021 zulipdev2021  582 Oct 31 16:24 id_rsa.pub
-rw-r--r--  1 zulipdev2021 zulipdev2021 2210 Oct 26 14:44 known_hosts
(zulip-py3-venv) zulipdev2021@DESKTO:~$ cat ~/.ssh/ed_ed25519.pub
cat: /home/zulipdev2021/.ssh/ed_ed25519.pub: No such file or directory
```

**Anders Kaseorg** · 2021-11-16 20:37 UTC

`~` is your home directory, which changes when you use `sudo` to become `root`. In general, you should not use `sudo` unless the directions *actually tell you* to do that. It is used for specific purposes and is not a one-size-fits-all “make this work” command.

**Anders Kaseorg** · 2021-11-16 20:38 UTC

And you still have a typo: should be `id_ed25519.pub`, not `ed_ed25519.pub`.

**Amanda E** · 2021-11-16 20:42 UTC

@Anders Kaseorg 
In the instructions for starting the ssh agent in the middle of this [page](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent), it does say to use sudo.  

I'm sorry for the typo again. I think I've just been looking at the screen for too long today, and I need to be someplace else in about 20 minutes, so I'm just going to try again tomorrow.  
Thanks for all your help - and Greg, too.

**Amanda E** · 2021-11-17 16:56 UTC

Thank you, again for all your help!  I finally registered my ssh key!  Now I have to switch from https to ssh, but it is one major step done.

**Amanda E** · 2021-11-17 17:55 UTC

All set up and working!


## noop in rebase request

*2021-11-18 to 2021-11-19 · 5 messages · [open in Zulip](https://chat.zulip.org/#narrow/channel/44-git-help/topic/noop.20in.20rebase.20request/with/1283861)*

**Amanda E** · 2021-11-18 20:25 UTC

My local code for PR #20260 was completely lost when I tried to debug my dev environment.  (I don't know how.)
I couldn't just fetch it back out, because git said the branch was clean.  
After many attempts, I finally got the file back to where it needs to be and pushed it to the PR, but now when I try to clean up the mess of commits I made through an interactive rebase, the editor shows "noop" instead of the list of commits I can see on GitHub.  And yes, I have made sure I was on the correct branch.
Just in case it makes a difference, there is also a conflict, and the tests won't run.
Thank you in advance for any thoughts or help!

**Tim Abbott** · 2021-11-18 21:27 UTC

@Amanda E you can use `git reflog` to find past versions of code.

**Tim Abbott** · 2021-11-18 21:28 UTC

That said, if your goal is just to get your changes to a couple files, checking out a new branch based off main and then doing, `git checkout OLD_BRANCH_NAME PATH1 PATH2` and then making a new commit is probably the easiest answer.

**Tim Abbott** · 2021-11-18 21:29 UTC

You can then do `git push origin +NEW_BRANCH_NAME:OLD_BRANCH_NAME` to update your existing pull request from the new branch you created locally.

**Amanda E** · 2021-11-19 15:02 UTC

Thank you!  That worked. :tada:


## hung CodeQL test

*2021-11-19 to 2021-11-19 · 5 messages · [open in Zulip](https://chat.zulip.org/#narrow/channel/44-git-help/topic/hung.20CodeQL.20test/with/1284153)*

**Amanda E** · 2021-11-19 15:07 UTC

The CodeQL test is perpetually queued in PR #20260.  
It's been over half an hour and the rest of the tests are passing.
Thoughts?

**Aman (amanagr)** · 2021-11-19 15:18 UTC

Opened [#7190](https://github.com/github/codeql/issues/7190)

**Aman (amanagr)** · 2021-11-19 16:40 UTC

Just a bad deploy from them. [They are reverting it.](https://github.com/github/codeql/issues/7190#issuecomment-974228110)

**Amanda E** · 2021-11-19 17:44 UTC

Just FYI - They might still be fixing this, but right now there are two version of CodeQL running.  One which runs and one which is still queued.

**Tim Abbott** · 2021-11-19 19:33 UTC

Yeah we're just ignoring codeql while it's broken on GitHub's end.


## setup

*2021-11-22 to 2021-11-22 · 1 messages · [open in Zulip](https://chat.zulip.org/#narrow/channel/44-git-help/topic/setup/with/1285051)*

**Notification Bot** · 2021-11-22 07:07 UTC

This topic was moved by @Aman Agrawal (amanagr) to #**provision help>setup**


## ✔ squash commits with merge conflicts

*2021-12-02 to 2021-12-03 · 11 messages · [open in Zulip](https://chat.zulip.org/#narrow/channel/44-git-help/topic/.E2.9C.94.20squash.20commits.20with.20merge.20conflicts/with/1290116)*

**Parth Mittal** · 2021-12-02 19:17 UTC

I created some [commits](https://github.com/zulip/zulip/pull/19760/) in my feature branch which resulted in a merge conflict with the main branch. After resolving them, it creates a new commit for resolution of the conflict. How do I squash this commit now?
Do I ``` git fetch upstream``` and ``` git rebase upstream/my-feature-branch```?

**Greg Price** · 2021-12-02 19:41 UTC

(replying to Parth Mittal)
> After resolving them, it creates a new commit for resolution of the conflict.

Hmm, that isn't how conflict resolution normally goes.

I'd highly recommend taking a look at your branch with `gitk` or another graphical client:
https://zulip.readthedocs.io/en/latest/git/setup.html#get-a-graphical-client
That's very helpful for seeing a clear picture of what's happening, especially when doing a rebase or other operation where something happens that surprises you.

**Greg Price** · 2021-12-02 19:43 UTC

Ah, did you use `git merge` and end up with a merge commit?

We don't use merge commits, or `git merge`, in our workflow. Instead you always rebase your feature branch on top of upstream. See sample sets of commands here:
https://zulip.readthedocs.io/en/latest/git/using.html

**Parth Mittal** · 2021-12-03 04:10 UTC

(replying to Greg Price)
> Ah, did you use `git merge` and end up with a merge commit?
The conflict happened when I pushed the commits to my branch on remote. Github's interface prompted me to resolve conflicts by merging them.

**Greg Price** · 2021-12-03 06:48 UTC

I see. Yeah, that's unhelpful of GitHub.

Here's instructions for updating your PR correctly:
https://zulip.readthedocs.io/en/latest/git/using.html#keep-your-fork-up-to-date

**Greg Price** · 2021-12-03 06:49 UTC

To get rid of the merge commit, the simplest thing is to use `git reset --hard` to go to a version of your branch from just before the merge commit.

When you look at your repo with `gitk` or another graphical client as mentioned above, you'll be able to see exactly what commit comes before the merge commit and you can copy-paste that commit ID into a `git reset --hard` command.

**Parth Mittal** · 2021-12-03 07:30 UTC

(replying to Greg Price)
> To get rid of the merge commit, the simplest thing is to use `git reset --hard` to go to a version of your branch from just before the merge commit.
Yes I did this and it worked! @Yash RE  also helped me through it!

**Parth Mittal** · 2021-12-03 07:36 UTC

I first undo'ed' the merge commit using [this doc](https://zulip.readthedocs.io/en/latest/git/troubleshooting.html?highlight=getting%20out%20of%20trouble#undo-a-merge-commit). 
Then followed [this](https://chat.zulip.org/#narrow/stream/49-development-help/topic/Best.20way.20to.20resolve.20merge.20conflicts.3F) to rebase.

**Notification Bot** · 2021-12-03 07:36 UTC

@Parth Mittal has marked this topic as resolved.

**Parth Mittal** · 2021-12-03 08:53 UTC

Thanks @Greg Price !

**Greg Price** · 2021-12-03 18:23 UTC

Great -- glad you got it resolved, and thanks for following up with the details of what worked!


## ✔ git branching

*2021-12-08 to 2021-12-10 · 5 messages · [open in Zulip](https://chat.zulip.org/#narrow/channel/44-git-help/topic/.E2.9C.94.20git.20branching/with/1294131)*

**Parth Mittal** · 2021-12-08 10:43 UTC

I have finished working on a PR but it is yet to be merged. I wanted to work on another issue which is in this area only. 
Thus, I made a branch based of my previous branch (the yet to be merged one). Now, while making the new issue PR, the commits from both branches show up. Should I wait for the previous PR to get merged or make another branch based of main to work on the new issue?

**Aman (amanagr)** · 2021-12-08 10:49 UTC

In this case, I generally wait for my first PR ( if it is a big change ) to get its first review and then branch it to work on the next issue if it didn't get merged and mention that in the new and old PR.

**Tim Abbott** · 2021-12-08 15:43 UTC

Alternately if the changes are independent you can just make a new branch off main.

**Parth Mittal** · 2021-12-10 18:29 UTC

Well in that case, waiting seems to be the best option :smile:

**Notification Bot** · 2021-12-10 18:29 UTC

@Parth Mittal has marked this topic as resolved.


## messed commits by merge

*2022-01-11 to 2022-01-11 · 4 messages · [open in Zulip](https://chat.zulip.org/#narrow/channel/44-git-help/topic/messed.20commits.20by.20merge/with/1307957)*

**Axay Sagathiya** · 2022-01-11 06:50 UTC

I did commit my changes and raised PR.
after that, I did merge master with a my-issue branch.
after that, I did commit other changes and force pushed it.

now I wanted to hide the merge commit so I tried to rebase.
and here everything's been messed.

git log showing all those merged commits as my commit.

[Screenshot-from-2022-01-11-12-16-22.png](https://chat.zulip.org/user_uploads/2/cc/RoOa-7mMJJIi6Bgkb7Tcrfpg/Screenshot-from-2022-01-11-12-16-22.png) 
in this image, only the first commit is mine, and the rest of the many commits are merged from the master branch.

What should I do ?

**Greg Price** · 2022-01-11 17:32 UTC

It's hard to tell what's going on from that screenshot, partly because it's not clear what command you ran to get that output.

The first thing I'd recommend is to use `gitk` or another graphical Git viewer to look at your repository. That helps a lot in seeing what's happening:
https://zulip.readthedocs.io/en/latest/git/setup.html#get-a-graphical-client

**Greg Price** · 2022-01-11 17:33 UTC

For example `gitk --all HEAD &` will give you a view of everything that's in the repository. `gitk upstream.. &` will give you a view of everything that's in your current branch that isn't part of `upstream`'s default branch (i.e. `upstream/main`).

**Anders Kaseorg** · 2022-01-11 19:55 UTC

One thing we can tell from your screenshot is that the hashes of the upstream commits have changed. This indicates that you incorrectly rebased `upstream/main` onto your branch rather than the other way around. You shouldn’t do that, but the fix is simple: rebase your branch onto `upstream/main`. (See our [Git guide](https://zulip.readthedocs.io/en/latest/git/pull-requests.html#update-a-pull-request) for some suggested commands.)


## This branch cannot be rebased due to conflicts

*2022-01-14 to 2022-01-22 · 25 messages · [open in Zulip](https://chat.zulip.org/#narrow/channel/44-git-help/topic/This.20branch.20cannot.20be.20rebased.20due.20to.20conflicts/with/1310457)*

**Suman kumar** · 2022-01-14 18:48 UTC

I made a [PR](https://github.com/zulip/zulip-mobile/pull/5182) and it shows This branch cannot be rebased due to conflicts. I tried with this [link](https://zulip.readthedocs.io/en/latest/git/using.html#keep-your-fork-up-to-date) but it has not been resolved yet.

**Chris Bobbe** · 2022-01-14 18:53 UTC

Please carefully explain what you tried (specific commands that you ran), and what happened (specific error output, please) that led you to think it's not resolved.

**Chris Bobbe** · 2022-01-14 18:54 UTC

(Maybe try again if all of that isn't fresh on your mind. :smile:)

**Chris Bobbe** · 2022-01-14 18:56 UTC

These details are necessary for us to use our time to help you.

**Suman kumar** · 2022-01-14 19:35 UTC

[Screenshot-from-2022-01-15-00-59-45.png](https://chat.zulip.org/user_uploads/2/9c/Sedsa5VWNIssXfFDzCcv_pXB/Screenshot-from-2022-01-15-00-59-45.png) 
@Chris Bobbe here's a screenshot although nothing changed in the store.js file still it gives a conflict and at last, it gives everything is up to date. but on GitHub, it gives This branch cannot be rebased due to conflicts.

**Suman kumar** · 2022-01-14 19:37 UTC

here's a command which  i tried-
```
git fetch origin main
git rebase origin/main
git add src/boot/store.js
 git rebase --continue
git push -f origin copylinkStream(my feature branch name)

**Suman kumar** · 2022-01-14 22:45 UTC

Hii @Chris Bobbe I saw the link(https://zulip.readthedocs.io/en/latest/git/fixing-commits.html, https://zulip.readthedocs.io/en/latest/git/using.html#examine-and-tidy-your-commit-history)given by you but according to me it is related to the commit message.

**Suman kumar** · 2022-01-14 22:45 UTC

Can you point out in more detail/specifically, how to solved this with the link you provided?

**Greg Price** · 2022-01-18 19:12 UTC

If the `git rebase` output tells you there was a conflict in a file, then the commits you're rebasing do indeed have changes to that file.

**Greg Price** · 2022-01-18 19:14 UTC

The most important thing you'll need in order to sort out what's happening in your branch is to see clearly what exactly is in it. For that I highly recommend using `gitk` or another graphical Git viewer:
https://zulip.readthedocs.io/en/latest/git/setup.html#get-a-graphical-client

**Greg Price** · 2022-01-18 19:19 UTC

From a glance at your PR's page on GitHub, your branch contains a large number of commits that appear to be rebased versions of commits in main:
[image.png](https://chat.zulip.org/user_uploads/2/f0/h_TyUgwh9kxrOUCsB1Gkv1DU/image.png) 

That means that at some point you did something like rebasing main onto your branch, instead of vice versa.

Seeing what your branch actually looks like in `gitk` will help a lot in understanding what the commands you're running are doing and working out what to do.

**Suman kumar** · 2022-01-20 18:58 UTC

(replying to Greg Price)
> From a glance at your PR's page on GitHub, your branch contains a large number of commits that appear to be rebased versions of commits in main: [image.png](https://chat.zulip.org/user_uploads/2/f0/h_TyUgwh9kxrOUCsB1Gkv1DU/image.png) That means that at some point you did something like rebasing main onto your branch, ins …
Thanx for telling me about gitk it helps a lot to see what's happening.Although  I reverted my branch where it was merge in main branch but while doing git rebase it gives merge conflict in some file even though I didn't change anything in it.

**Greg Price** · 2022-01-20 19:14 UTC

If the `git rebase` output tells you there was a conflict in a file, then the commits you're rebasing do indeed have changes to that file.

You may not have edited that file in your editor and used `git commit` to make a commit that changes it. But nevertheless you have in your branch a commit that edits it. `gitk` can help you see what that commit is.

**Greg Price** · 2022-01-20 19:15 UTC

If you post details of concretely what you did and what you're seeing, people here may be able to help you figure out the things you're puzzled by. But it's not really possible to do that without more detail. I don't know what you tried to do that you're describing as "I reverted my branch where it was merge in main branch" -- clearly something in your repo isn't the way you expect it to be, and it's not possible to tell what without more specifics.

**Suman kumar** · 2022-01-20 20:36 UTC

[Screenshot-from-2022-01-21-02-04-05.png](https://chat.zulip.org/user_uploads/2/b1/hGu1oRubkRaXfbwW2Fa_bRRX/Screenshot-from-2022-01-21-02-04-05.png) [Screenshot-from-2022-01-21-02-04-27.png](https://chat.zulip.org/user_uploads/2/93/P34p63BaxxlEbY-1YZjGW1oT/Screenshot-from-2022-01-21-02-04-27.png).

**Suman kumar** · 2022-01-20 20:38 UTC

[Screenshot-from-2022-01-21-02-08-02.png](https://chat.zulip.org/user_uploads/2/1d/xoMmEowzGzCn_wsv8V-qjoWf/Screenshot-from-2022-01-21-02-08-02.png)

**Suman kumar** · 2022-01-20 20:45 UTC

command which i used for rebase-
```
git pull origin main --rebase
git add src/boot/store.js(merge conflict in this file)
git rebase --continue
git rebase --skip
```
Hope the above screenshot help to understand what's my problem/mistake.

**Greg Price** · 2022-01-20 20:48 UTC

Do take a look at our [community norms](https://zulip.com/development-community/#community-norms) for this server:
> When asking for help, provide the details needed for others to help you. For example, *include the full traceback in a code block (not a screenshot)*, a link to the code or a WIP PR you’re having trouble debugging, etc.

**Greg Price** · 2022-01-20 20:49 UTC

Your `gitk` screenshot (that part is fine as a screenshot, because it's graphical) shows you still have a number of commits that are versions of commits in `main`. Rebasing those on top of what's in `main` is going to have conflicts, because they're changing the same files as later commits in `main`.

**Greg Price** · 2022-01-20 20:50 UTC

For a first step, instead of `git pull --rebase`, use `git fetch` and `git rebase` separately, and use `gitk` in between to see what's happening. That will give you a clearer picture and more control.

**Greg Price** · 2022-01-20 20:52 UTC

Also is `origin` the correct remote you want there? Our convention is for the upstream repo to be called `upstream`.

If you have `origin` as the upstream repo, you can fix that with `git remote rename`.

**Greg Price** · 2022-01-20 20:52 UTC

Then once you've separated the fetch and rebase steps, try using `git rebase -i`. That will show you the full list of commits that you're rebasing.

**Greg Price** · 2022-01-20 20:53 UTC

You'll want to omit from that list all the commits that aren't your own changes, and are instead copies of commits in `main`.

**Greg Price** · 2022-01-20 20:54 UTC

Alternatively, instead of editing that list, you might find it easier to use `git cherry-pick` to build a new version of your branch up from scratch, taking just the individual commits from your existing branch that are actually your changes. `gitk` will be very helpful in seeing which those commits are.

**Suman kumar** · 2022-01-22 18:39 UTC

Thanx @Greg Price finally it resolved.


## messed up commit history

*2022-01-15 to 2022-01-15 · 3 messages · [open in Zulip](https://chat.zulip.org/#narrow/channel/44-git-help/topic/messed.20up.20commit.20history/with/1310630)*

**Yash** · 2022-01-15 18:58 UTC

Recently started contributing to open source and I think I have messed up some PR's. This is one of my [PR](https://github.com/zulip/zulip/pull/20650) and I have given the same commit messages to every commit, also some of the commits are unnecessary. I have two things to ask:
1. Is there anything I could do now (rewriting or squashing my commits history nd updating my PR)?
2. and what are the things to consider to avoid gitlint error when making commits (I always get this)?
Thanking everyone in advance.

**Alex Dehnert** · 2022-01-15 19:13 UTC

Addressing just the first point: you can use git rebase and force push to fix your commits. https://zulip.readthedocs.io/en/latest/git/using.html#examine-and-tidy-your-commit-history has some more details.

**Yash** · 2022-01-15 19:42 UTC

thank you so much for the help @Alex Dehnert, I think I get it now.


## pushing amended branch

*2022-01-24 to 2022-01-24 · 2 messages · [open in Zulip](https://chat.zulip.org/#narrow/channel/44-git-help/topic/pushing.20amended.20branch/with/1314864)*

**Rodrick Calvin Wamala** · 2022-01-24 15:51 UTC

Hello. I need help. I made a PR but was told to amend my commit message. On amending, the branch can't push. It says my branch can't update Updates rejected because the tip of your current branch is behind. Any recommendations?

**shlok (madrix01)** · 2022-01-24 15:57 UTC

Try 
```shell
git push -f origin <branch-name>
```


## ✔ Removing/avoiding merge commits

*2022-01-24 to 2022-01-29 · 4 messages · [open in Zulip](https://chat.zulip.org/#narrow/channel/44-git-help/topic/.E2.9C.94.20Removing.2Favoiding.20merge.20commits/with/1314948)*

**Raghav Luthra** · 2022-01-24 18:47 UTC

Whenever I sync my forked repository using the 'Fetch and merge' button on GitHub, a merge commit is pushed. Is there any preferred way to squash/remove these merge commits or avoid them altogether? So far I have managed with one or two solutions I found online like [this](https://stackoverflow.com/questions/33502205/how-to-delete-merge-commits) one, and I was wondering if there is a concrete solution for this.

**Tim Abbott** · 2022-01-24 20:46 UTC

@Raghav Luthra I don't recommend using those GitHub buttons; just use the command-line rebasing tools instead.

**Raghav Luthra** · 2022-01-25 10:14 UTC

All right. Thanks for the help.

**Notification Bot** · 2022-01-29 18:09 UTC

@Raghav Luthra has marked this topic as resolved.


## How to keep my git branch up to date?

*2022-02-28 to 2022-02-28 · 7 messages · [open in Zulip](https://chat.zulip.org/#narrow/channel/44-git-help/topic/How.20to.20keep.20my.20git.20branch.20up.20to.20date.3F/with/1336288)*

**Kai You** · 2022-02-28 20:24 UTC

Hi, I am new at working with such a big system, right now I am done with my work on my branch, so I double-checked and found out my branch is not up to date, and I want to keep it up to date so I can send a pull request with this doc https://zulip.readthedocs.io/en/latest/git/using.html#keep-your-fork-up-to-date
[截圖-2022-02-28-下午12.19.42.png](https://chat.zulip.org/user_uploads/2/cb/uCHiiYNM7aAEdogpUEQSH7I0/截圖-2022-02-28-下午12.19.42.png) 

I type "git fetch upstream", it shows the following
```terminfo
fatal: 'upstream' does not appear to be a git repository
fatal: Could not read from remote repository.
```

so right now I am stuck, I read the topic below it seems unrecommended to just using "Fetch upstream" button on Github, is there something I missed during viewing the doc?

**Anders Kaseorg** · 2022-02-28 21:00 UTC

The documentation assumes you have configured the `upstream` remote [as it describes](https://zulip.readthedocs.io/en/latest/git/cloning.html#step-1c-connect-your-fork-to-zulip-upstream).

**Kai You** · 2022-02-28 21:06 UTC

@Anders Kaseorg   Yes, I found the answer by reading more specifically into the doc, thanks !
But right now another problem is that I seems to merge when I tried to update my branch, here's the log history 
```terminfo
(zulip-py3-venv) vagrant@d7451d7b4bff:/srv/zulip$ git log --all --graph --oneline --decorate
*   64f5ceaba1 (HEAD -> issue-21265, ori
gin/issue-21265) Merge remote-tracking branch 'origin/issue-21265' into 
issue-21265
|\  
| * 275eb8bbcb popovers: Avatar border should be outside of the imag
e in full profile
* | bb107a8777 popovers: Avatar border should be outside of the imag
e in full profile
* | 9f89d7e069 (upstream/main, main)
 left_sidebar: Move "Recent topics" higher in the sidebar.
* | 98a05257ea (origin/main, origin/HEAD
) scripts: Print names of missing migrations in compatibility check.
| | * f17fa6867d (upstream/dependabot/npm_and_yarn
/url-parse-1.5.10) build(deps): bump url-parse from 1.5.4 to 1.5.10
| |/  
|/|   
* | cc5ac302ab docs: Add more metadata to GSoC project ideas and add
 ideas.
* | 7ddefc68cc settings: render_alert_words_ui -> rerender_alert_wor
ds_ui.
* | d6c00521b3 settings: Clean up muted_topics/users rendering logic
.
* | 5e49ddf4e1 settings: Add sorting feature for list of alert words
--More--
```

I am not sure is the status right now is  a good practice to submit a pull request, since I found the merge commit which are not supposed to happen according to the doc, so is their anything I missed ?

**Anders Kaseorg** · 2022-02-28 21:10 UTC

See the note about `git pull` in your first link.

**Kai You** · 2022-02-28 21:32 UTC

@Anders Kaseorg  sorry for not reading it thoroughlly, I delete my previous branch, and redo the step on the first link, right now the branch history look like this, do you think this is complete enough to submit a pull request ? or is there something else I should look for ?
```terminfo
* 331781a4ac (HEAD -> issue-21265, origi
n/issue-21265) popovers: Avatar border should be outside of the image in
 full profile
* 9f89d7e069 (upstream/main, origin/main, 
origin/HEAD, main) left_sidebar: Move "Recent topi
cs" higher in the sidebar.
* 98a05257ea scripts: Print names of missing migrations in compatibility c
heck.
| * f17fa6867d (upstream/dependabot/npm_and_yarn/url-par
se-1.5.10) build(deps): bump url-parse from 1.5.4 to 1.5.10
|/  
* cc5ac302ab docs: Add more metadata to GSoC project ideas and add ideas.
* 7ddefc68cc settings: render_alert_words_ui -> rerender_alert_words_ui.
* d6c00521b3 settings: Clean up muted_topics/users rendering logic.
* 5e49ddf4e1 settings: Add sorting feature for list of alert words.
* 27b985e868 recent_topics: Standardize format of last message time.
* c2a117c623 timerender_test: Directly use date object instead of timestam
p.
* 5ae178b39c recent_topics: Show loading indicator before fetching initial
 messages.
* 98c2038718 recent_topics: Position empty topic text independent of colum
ns.
* 62f4f3435f ci: Test upgrades from 4.10.
```

**Anders Kaseorg** · 2022-02-28 21:40 UTC

That looks fine. (Note that you can always submit a pull request and update it later, using a force push if necessary.)

**Kai You** · 2022-02-28 23:01 UTC

Thanks, I will look out for that !


## gitk selection bug

*2022-03-01 to 2022-03-01 · 4 messages · [open in Zulip](https://chat.zulip.org/#narrow/channel/44-git-help/topic/gitk.20selection.20bug/with/1337015)*

**Tim Abbott** · 2022-03-01 19:08 UTC

So I'm experiencing a strange bug with `gitk` where it seems to continuously be in selecting mode.  (i.e. just moving my mouse selects text). I'm on the latest Ubuntu PPA version, 2.35.  Anyone else experiencing this?

**Anders Kaseorg** · 2022-03-01 19:22 UTC

That makes more sense as a touchpad [driver bug](https://bugs.freedesktop.org/show_bug.cgi?id=98733) than a gitk bug.

Does it fix itself if you click on the gitk window?

**Tim Abbott** · 2022-03-01 19:58 UTC

No, I haven't figured out any way to fix it.

**Tim Abbott** · 2022-03-01 19:59 UTC

Ahh, that was the problem! Touching the laptop touchscreen was able to clear the state!


## git rewrite

*2022-03-14 to 2022-03-14 · 5 messages · [open in Zulip](https://chat.zulip.org/#narrow/channel/44-git-help/topic/git.20rewrite/with/1343951)*

**Sayam Samal** · 2022-03-14 13:31 UTC

Having pushed a commit to github, I see many as many as 330 changes in a file whereas I have just changed 2-3 lines of code. Any reason why this is happening? [Commit diffs](https://github.com/sayamsamal/zulip/commit/b017f19cfb91a7e3e437a5b27daec35d5d03cbb8) : look "settings_overlay.hbs"

I also get a message reading "git rewrite 87%".

**Greg Price** · 2022-03-14 17:23 UTC

It's telling you that those ilnes changed, because those lines changed.

One thing that appears to be happening is that a lot of those lines changed only by adding more indentation, i.e. more spaces at the beginning of the line. One thing you can do to get a clearer picture of what's happening in your commit is to pass the `-b` flag to `git log`: for example, `git log --stat -p -b`. That will treat those lines as having not changed, so you can focus on the lines that changed in a more interesting way.

**Greg Price** · 2022-03-14 17:23 UTC

Documentation on that flag here: https://git-scm.com/docs/git-log#Documentation/git-log.txt--b , or use `git help log` and search for "whitespace".

**Sayam Samal** · 2022-03-14 19:13 UTC

thank you for pointing it out, white spaces were indeed the reason why.
`git log --stat -p -b`, this is very handy indeed and will be using it from now on.

**Sayam Samal** · 2022-03-14 19:16 UTC

Also, found out that I could add `?w=1` to the end of the [commit diff page](https://github.com/zulip/zulip/pull/21408/commits/a34785d0b33d90919df651e89f08bba13edbd66e?w=1) to hide white-spaces.


## GitHub notifications

*2022-03-17 to 2022-03-18 · 6 messages · [open in Zulip](https://chat.zulip.org/#narrow/channel/44-git-help/topic/GitHub.20notifications/with/1347394)*

**Tim Abbott** · 2022-03-17 23:04 UTC

Is it possible to configure the GitHub notifications email address for a single repository, or only at the organization level?  I've found the latter setting but not the per-repository version, and want different configuration for zulip/zulip vs other projects like zulip/zulip-mobile.

**Greg Price** · 2022-03-17 23:44 UTC

As far as I've seen, only per organization (and only for organizations you're a member of, which is a gratuitous restriction I've often found frustrating.)

The workaround I've settled on for the latter issue, the fact that you can't do it for third-party organizations at all, is that I have a Gmail filter rule on my personal email (which is my default GitHub notification email address) which looks for all GitHub notifications from certain orgs and repos, archives them, marks as read, and forwards them to my zulip.com address.

**Greg Price** · 2022-03-17 23:45 UTC

If the destination you have for the zulip organization in general is in Gmail or another provider with a similar filter/forward feature, you could do the same thing.

**Greg Price** · 2022-03-17 23:47 UTC

The Gmail filter expression for notifications from, e.g., zulip/zulip-mobile, is `list:zulip-mobile.zulip.github.com`.

**Greg Price** · 2022-03-17 23:48 UTC

You can also compose them: `list:zulip.github.com -list:(zulip OR zulip-terminal).zulip.github.com` would match
* all GitHub notifications
* that are for some repo in the zulip org
* other than zulip/zulip or zulip/zulip-terminal .

**Tim Abbott** · 2022-03-18 00:11 UTC

Yeah, I'm experimenting with Alya's approach of having GitHub activity notifications go into a Zulip private stream, but I only want that for zulip/zulip.  So probably the right plan is to have things go directly to gmail and then forward just the zulip/zulip ones to the Zulip private stream via such a filter.


## git commit taking long time due to pre-commit hook

*2022-03-30 to 2022-04-04 · 12 messages · [open in Zulip](https://chat.zulip.org/#narrow/channel/44-git-help/topic/git.20commit.20taking.20long.20time.20due.20to.20pre-commit.20hook/with/1356199)*

**Christopher Chong** · 2022-03-30 16:02 UTC

Hi guys, everytime I do git commit the command takes super long (~2 mins) to finish running, where it is just stuck after showing this message `Running lint using vagrant...`. I guess the pre-commit hook is taking a long time, is there any way I can speed it up?

FYI I'm running my git command in zulip repo directory in my host machine, while my VSCode is editing the /srv/zulip inside vagrant.

**Greg Price** · 2022-03-30 17:48 UTC

That sounds awfully annoyingly slow, yikes!

**Greg Price** · 2022-03-30 17:49 UTC

Personally, my solution is to not enable the pre-commit hook. Even if it takes only a few seconds, that is way more friction than I want to have in the way of `git commit`.

One wants to be using `git commit` frequently when working in the Zulip project's style where a branch is often a long series of small commits.

**Greg Price** · 2022-03-30 17:54 UTC

One key thing the pre-commit hook does in order to try to avoid taking a super long time is that it tries to run the linter only on files that you've changed. If you want to debug why it's taking so long, one thing you could do is to find out what files it's passing to the linter.

For example, you could add this line for debugging:
```diff
diff --git a/tools/pre-commit b/tools/pre-commit
index 6c4d91a66..90661e93a 100755
--- a/tools/pre-commit
+++ b/tools/pre-commit
@@ -13,6 +13,7 @@ changed_files=()
 while read -r -d '' f; do
     changed_files+=("$f")
 done < <(git diff -z --cached --name-only --diff-filter=ACM)
+printf '%s\n' "${changed_files[@]}"
 if [ ${#changed_files} -eq 0 ]; then
     echo "No changed files to lint."
     exit 0
```

**Tim Abbott** · 2022-03-30 18:55 UTC

@Christopher Chong yikes, that certainly sounds like some sort of bug with how the pre-commit hook is being configured with Vagrant; it should only take a few seconds at most. The debugging step suggested by @Greg Price is the best next step.

**Christopher Chong** · 2022-04-02 06:24 UTC

@Greg Price @Tim Abbott  thanks so much for the help. I added the debug line and pre-commit only showed the file I edited. So it's probably due to vagrant ssh command. I have successfully fixed this by running `git commit` inside vagrant docker itself, which runs much faster compared to running `git commit` on my host machine.

**Greg Price** · 2022-04-04 21:15 UTC

Great, glad you have things working well!

Still puzzling if `vagrant ssh` is taking 2 minutes to work -- that could be good to debug.

**Greg Price** · 2022-04-04 21:16 UTC

It is normal for it to be annoyingly slow, unfortunately. For me it's about 1 second:
```
$ time vagrant ssh -- echo hi
hi

time: 1.083s wall (0.724s u, 0.306s s)
```

For that reason, I long ago added the following to my `~/.ssh/config` file:
```
Host zd
  HostName 127.0.0.1
  Port 2222
  User vagrant
  IdentityFile ~/z/zulip/.vagrant/machines/default/docker/private_key
```

so that I could skip running all Vagrant's slow Ruby code, and just say `ssh zd` to get the same effect much faster:
```
$ time ssh zd echo hi
hi

time: 0.129s wall (0.006s u, 0.004s s)

**Greg Price** · 2022-04-04 21:17 UTC

But 2 minutes is a rather more painful time to wait than 1 second is :smile:

**Tim Abbott** · 2022-04-04 22:26 UTC

Should we add a note on that tricky to our Vagrant docs?

**Tim Abbott** · 2022-04-04 22:27 UTC

(I'm not sure the `Vagrantfile` could safely set it up for you; I don't like the idea of a script writing to `~/.ssh/config` in any case)

**Anders Kaseorg** · 2022-04-04 22:27 UTC

There is a `vagrant ssh-config` command that outputs the `~/.ssh/config` snippet.


## ✔ Include django migration files in commit or not?

*2022-04-08 to 2022-04-08 · 2 messages · [open in Zulip](https://chat.zulip.org/#narrow/channel/44-git-help/topic/.E2.9C.94.20Include.20django.20migration.20files.20in.20commit.20or.20not.3F/with/1362617)*

**Raghav Luthra** · 2022-04-08 14:14 UTC

(deleted)

**Notification Bot** · 2022-04-08 14:56 UTC

@Raghav Luthra has marked this topic as resolved.


## Amend Commit Message

*2022-04-12 to 2022-04-12 · 3 messages · [open in Zulip](https://chat.zulip.org/#narrow/channel/44-git-help/topic/Amend.20Commit.20Message/with/1365060)*

**Vishal Sharma** · 2022-04-12 19:09 UTC

Hello, 

I have been asked to change the commit message [here](https://github.com/zulip/zulip-mobile/pull/5332), one way I know to do it is to use `--amend` and then force push the commit to my origin repo, and then create the PR will automatically connect with the existing PR. 

Is this the way in which Zulip works? OR should I confirm the steps in the PR discussion?

**Anders Kaseorg** · 2022-04-12 19:12 UTC

See [Examine and tidy your commit history](https://zulip.readthedocs.io/en/latest/git/using.html#examine-and-tidy-your-commit-history) in our documentation. (And there’s no need to @-mention individual developers—see our [community norms](https://zulip.com/development-community/#community-norms).)

**Vishal Sharma** · 2022-04-12 19:14 UTC

Okay. I'll take care in future discussions. Thank you for directing me to the documentation.


## ✔ unable to commit

*2022-04-20 to 2022-04-20 · 6 messages · [open in Zulip](https://chat.zulip.org/#narrow/channel/44-git-help/topic/.E2.9C.94.20unable.20to.20commit/with/1370437)*

**Cynthia Mamah** · 2022-04-20 05:08 UTC

Cynthia Mamah5:43 AM
I keep getting this error message on attempt to commit my changes "did not match any file(s) known to git"

below is my commit message that shows the error
git commit "Long "Person" type profile field spills out of input box (issue #21807)

Due to the error of type profile spilling out of input box,
This commit thereby fixes the issue

Fixes :#21828

**Cynthia Mamah** · 2022-04-20 05:08 UTC

Cynthia Mamah5:43 AM
I keep getting this error message on attempt to commit my changes "did not match any file(s) known to git"

below is my commit message that shows the error
git commit "Long "Person" type profile field spills out of input box (issue #21807)

Due to the error of type profile spilling out of input box,
This commit thereby fixes the issue

Fixes :#21828

**Cynthia Mamah** · 2022-04-20 05:18 UTC

below is my git status output

iamcynthiamamah@DESKTOP-0JR1QFC:~/zulip$ git status
On branch issue-21828-Cynthia
Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        modified:   static/styles/input_pill.css

**Aman (amanagr)** · 2022-04-20 05:19 UTC

Please stick to one topic for seeking help!

**Notification Bot** · 2022-04-20 05:19 UTC

@Aman Agrawal (amanagr) has marked this topic as resolved.

**Aman (amanagr)** · 2022-04-20 05:19 UTC

Discussion in https://chat.zulip.org/#narrow/stream/49-development-help/topic/unable.20to.20commit


## easier way to squash commits ?

*2022-04-28 to 2022-04-29 · 28 messages · [open in Zulip](https://chat.zulip.org/#narrow/channel/44-git-help/topic/easier.20way.20to.20squash.20commits.20.3F/with/1374906)*

**Adam Sah** · 2022-04-28 00:04 UTC

If I'm working in a simple branch off of `main`, and I have a stack of small commits that I want to roll into a ***one single*** commit, couldn't I simply do this to squash commits together?

1. git reset --soft origin/main
1. git commit -am "...commit message..."
1. git push -f

(obviously, this only works when all your changes fit into a single commit)

If this works, this seems much simpler for newbies and people working on small features and fixes.

**Greg Price** · 2022-04-28 00:12 UTC

Yep, that works! I regularly do something like that for squashing a handful of commits together.

**Greg Price** · 2022-04-28 00:13 UTC

Usually I use something like `git commit -ac main` or `git commit -ac main~2` to start from a particular existing commit's commit message, and also timestamp.

**Greg Price** · 2022-04-28 00:14 UTC

(but still with the editor to edit the commit message; `-C main` would reuse the commit message verbatim without popping up the editor)

**Greg Price** · 2022-04-28 00:15 UTC

In the case of the Zulip project, it's pretty common that we want a PR to be several commits, not just one. So one reason I think we wouldn't want to emphasize pointing people at those instructions, especially for newcomers to the project, is that we wouldn't want to make it seem like the normal thing or the easy path is to squash all your changes together. Often that's the right answer, especially for small PRs, but often it's not, even for small PRs.

**Anders Kaseorg** · 2022-04-28 00:18 UTC

It only works if your branch is a descendant of origin/main. If you’ve run a `git fetch` that updated origin/main, you might end up reversing those updates in your commit. This is obvious if you understand Git well, but not so obvious to new developers, so it’s probably not the way I would teach someone.

**Greg Price** · 2022-04-28 00:18 UTC

Also I don't think that's really a lot simpler to use than '`git rebase -i`, and change all but the first commit from "pick" to "squash".'

In particular for someone new to Git, the `git reset --soft` approach feels like it involves more working hands-on with Git at a lower level of abstraction -- it feels like it'd be easier for it to go awry and leave someone totally confused about what's happening.

**Greg Price** · 2022-04-28 00:18 UTC

For example, the way Anders just said while I was typing that :-)

**Adam Sah** · 2022-04-28 12:31 UTC

wow, thx for all this detail!  If you guys aren't prejudiced against it, I may propose a draft PR or tools/ script to provide newbs a gentler experience they can copy/paste (i.e. drop 10+ pages of docs to read).

background: I'm coming from experiences like Google & Postgres (i.e. large+old projects...), where new/junior developers don't think twice about source control and focused entirely on the code - newbs create their changes in a branch/diff/patch, go through rounds of reviews until they get an "lgtm" and then the branch gets pulled.

strawman **for newbs**:
1. idiot-proof "my first PR" copy/paste instructions, like the rest of the (awesome) zulip dev process!  (vagrant + manual testing incl auto-reload, unittesting, etc) Newbs shouldn't have to know about multiple commits or branches.
1. non-interactive command line like the rest of zulip - `git rebase -i` is interactive, and in fact my editor opened twice - one to pick/squash/etc and once to create a commit message. Each filled my screen with complex instructions. See below for details.
1. follow-on documentation that explains what to do when your PR contains multiple commits, when your PR isn't branched from main, etc.

---

Transcript of my experience with `git rebase -i`for the simple case where I made a small change to a unittest, and wanted to squash it in.

First, I run `git rebase -i` and then my editor opens:

```
pick ffee657e51 improve test

# Rebase 507240aa36..ffee657e51 onto 507240aa36 (1 command)
#
# Commands:
```
==> ??? where's the rest of the my commits in my branch?
==> ??? did I need to specify a commit hash?  if so, which one?
==> ??? why can't there just be a copy/paste command that does the right thing here?

So I run `git log` grab the commithash from the last merge from main and run `git rebase -i HASH`:
```
pick 507240aa36 Make it possible to send messages to unsubscribed streams.
pick ffee657e51 improve test

# Rebase ee0021de08..ffee657e51 onto ee0021de08 (2 commands)
#
# Commands:
# p, pick <commit> = use commit
# r, reword <commit> = use commit, but edit the commit message
# e, edit <commit> = use commit, but stop for amending
# s, squash <commit> = use commit, but meld into previous commit
# f, fixup [-C | -c] <commit> = like "squash" but keep only the previous
#                    commit's log message, unless -C is used, in which case
#                    keep only this commit's message; -c is same as -C but
#                    opens the editor
# x, exec <command> = run command (the rest of the line) using shell
# b, break = stop here (continue rebase later with 'git rebase --continue')
# d, drop <commit> = remove commit
# l, label <label> = label current HEAD with a name
# t, reset <label> = reset HEAD to a label
# m, merge [-C <commit> | -c <commit>] <label> [# <oneline>]
```
==> 11 different commands... ?!?!?!?!  do I use single letters or words? what arguments?

guessing, I try this:
```
pick 507240aa36 Make it possible to send messages to unsubscribed streams.
s ffee657e51 improve test
```

...and then my editor opens again?!?!?!?!  NOW what do I do ?!?!
```
 This is a combination of 2 commits.
# This is the 1st commit message:

Make it possible to send messages to unsubscribed streams.

Fixes #21433.

# This is the commit message #2:

improve test

# Please enter the commit message for your changes. Lines starting
# with '#' will be ignored, and an empty message aborts the commit.
#
# Date:      Wed Apr 27 19:26:04 2022 -0400
#
# interactive rebase in progress; onto ee0021de08
# Last commands done (2 commands done):
#    pick 507240aa36 Make it possible to send messages to unsubscribed streams.
#    squash ffee657e51 improve test
# No commands remaining.
# You are currently rebasing branch 'issue-21433--send-to-unsubd-stream' on 'ee0021de08'.
#
# Changes to be committed:
#       modified:   frontend_tests/node_tests/compose_validate.js
#       modified:   static/js/compose.js
#       modified:   static/js/compose_validate.js
#       modified:   static/styles/compose.css
#       modified:   static/templates/compose_not_subscribed.hbs
#       modified:   zerver/tests/test_message_send.py
#
# Untracked files:
#       TAGS
#
```

so I pick this:
```
# This is a combination of 2 commits.
# This is the 1st commit message:

Make it possible to send messages to unsubscribed streams.

Fixes #21433.

# Please enter the commit message for your changes. Lines starting
# with '#' will be ignored, and an empty message aborts the commit.
```
I then saved and because it wasn't obvious, I then ran `git log` to confirm that things looked right - and even then, I wasn't 100% sure that I had the changes from main.

note: this is the simplest case. When I ran rebase on multiple commits, things often went haywire if I didn't type everything perfectly. For example, when both main and my branch both had multiple commits, it wasn't easy/obvious which ones were mine vs main because rebase only shows the hash and commit message, not the author ([this is fixable](https://stackoverflow.com/questions/35851671/is-there-a-way-to-list-the-commits-author-in-git-rebase-i-interactive), but may conflict with the ability to change commit messages)

hope this helps! (sorry if distracting/annoying)

**Adam Sah** · 2022-04-28 12:40 UTC

(as another example, rebase -i gave me self-conflicts from two commits in my own branch, after I told it to squash the later commit into the earlier commit... I then had to examine the code carefully to know which to keep... yuck!)

```
asah@hadid:~/projects/zulip$ git diff
diff --cc zerver/tests/test_message_send.py
index 8bcbb2cef1,7345b6d22f..0000000000
--- a/zerver/tests/test_message_send.py
+++ b/zerver/tests/test_message_send.py
@@@ -1232,21 -1232,17 +1232,35 @@@ class MessagePOSTTest(ZulipTestCase)
              email_gateway: bool = False,
              mark_as_read: Sequence[int] = [],
          ) -> List[int]:
++<<<<<<< HEAD
 +            for send_request in send_message_requests_maybe_none:
 +                if send_request is not None:
 +                    if (
 +                        len(
 +                            Subscription.objects.filter(
 +                                user_profile_id=send_request.message.sender.id,
 +                                active=True,
 +                                recipient__type=Recipient.STREAM,
 +                                recipient__type_id=send_request.message.recipient.type_id,
 +                            ).values_list("user_profile_id", flat=True)
 +                        )
 +                        == 0
 +                    ):
 +                        raise Exception("not subscribed")
 +            raise Exception("is subscribed")
++=======
+             send_request = send_message_requests_maybe_none[0]
+             if send_request is None:
+                 raise Exception("no send request?!")
+             if Subscription.objects.filter(
+                 user_profile_id=send_request.message.sender.id,
+                 active=True,
+                 recipient__type=Recipient.STREAM,
+                 recipient__type_id=send_request.message.recipient.type_id,
+             ).exists():
+                 raise Exception("is subscribed")
+             raise Exception("not subscribed")
++>>>>>>> 650edc07c9 (Make it possible to send messages to unsubscribed streams.)

          with mock.patch(
              "zerver.actions.message_send.do_send_messages", side_effect=break_unsubscribed_send
```

(once that was resolved, I was still left with two commits and needed to rebase again...

```
asah@hadid:~/projects/zulip$ git log
commit 862883243faf9ebd45e4da7119fde1cd2f8d4e27 (HEAD -> issue-21433--send-to-unsubd-stream)
Author: Adam Sah <140002+asah@users.noreply.github.com>
Date:   Wed Apr 27 19:26:04 2022 -0400

    Make it possible to send messages to unsubscribed streams.

    Fixes #21433.

commit 507240aa360da88067fe69c2975543d1d3d1a453 (origin/issue-21433--send-to-unsubd-stream)
Author: Adam Sah <140002+asah@users.noreply.github.com>
Date:   Wed Apr 27 19:26:04 2022 -0400

    Make it possible to send messages to unsubscribed streams.

    Fixes #21433.

commit ee0021de084f7f8aa2c11de78c0df5c46ca5b12f (origin/main, origin/HEAD, main)
Author: Mateusz Mandera <mateusz.mandera@zulip.com>
Date:   Wed Apr 27 18:11:00 2022 +0200

    models: Change Stream.history_public_to_subscribers value to True.

    The default of a Stream is to be public - having
    history_public_to_subscribers default to False is inconsistent with
    that. The defaults on the model should generally be consistent.
```

(all I'm saying is that rebase -i adds a lot of complexity to an otherwise simple system)

**Tim Abbott** · 2022-04-28 17:16 UTC

I've for a long time wanted to build a little code lab that we can have contributors go through to learn how to do rebasing properly.

**Tim Abbott** · 2022-04-28 17:16 UTC

I continue to not have time for it, but I think it's one of the more meaningful things we could do to improve the productivity of the project.

**Tim Abbott** · 2022-04-28 17:18 UTC

https://github.com/zulip/zulip-gci/blob/master/tasks/2017/submit-a-pull-request.md is a very small thing we built 5 years ago in this directory for a program for high school students; not sure it has much use but figured I'd link it.

**Anders Kaseorg** · 2022-04-28 18:22 UTC

If `git rebase -i` showed you conflicts when you didn’t reorder or delete anything, it’s because the upstream branch moved and there really are conflicts—exactly the scenario I described above where the `git reset --soft` approach would have silently done the wrong thing.

**Anders Kaseorg** · 2022-04-28 18:26 UTC

I think maybe your issue there is that you were rebasing onto the wrong branch—in this case, an old version of the same commit. If you don’t have a good understanding of what Git selects as the default, you should always provide an argument to `git rebase -i`, such as `git rebase -i upstream/main`.

**Anders Kaseorg** · 2022-04-28 18:27 UTC

When there are conflicts, you’ll find them much easier to resolve if you [turn on the `diff3` style](https://blog.nilbus.com/take-the-pain-out-of-git-conflict-resolution-use-diff3/). (But in this case the right resolution would have been to `git rebase --abort` and try again with the correct argument.)

**Tim Abbott** · 2022-04-28 18:32 UTC

My other comment is that it's dramatically easier to self-debug things like this if you use `gitk --all` and refresh its state after every command. It often reveals situations like this, where one didn't ask for the rebase one thought one was asking for.

**Greg Price** · 2022-04-28 22:02 UTC

I agree with all of Anders's and Tim's thoughts above. I want to emphasize this one a bit:

(replying to Anders Kaseorg)
> When there are conflicts, you’ll find them much easier to resolve if you [turn on the `diff3` style](https://blog.nilbus.com/take-the-pain-out-of-git-conflict-resolution-use-diff3/).

by saying that this is a spot where the default is badly chosen -- you should definitely do `git config --global merge.conflictstyle diff3`, and it's regrettable that Git doesn't do it that way for everyone in the first place.

With the default behavior, it is completely impossible to resolve rebase (or merge) conflicts correctly without going and looking back at the history to work out what happened. (That blog post explains, with an example.) With `diff3`, once you learn to read what they're saying you can resolve most conflicts by looking purely at the conflict markers, which makes it very efficient to deal with them.

**Adam Sah** · 2022-04-29 01:06 UTC

thx!  takeaways:
- "my first PR" tutorial attempts welcome - adding to my list, though haha I'm more a customer than the expert!
- gitk (`brew install git-gui` on mac) can help visualize. FYI the font is *tiny* on my mac.
- `git config --global merge.conflictstyle diff3` ==> consider this for the tutorial?
- git rebase -i always get an argument and the choice isn't obvious  => more footguns...

(back to debugging hell - stack of non-obvious failed unittests from the latest merge from main... i.e. real conflicts in my branches...)

**Alex Vandiver** · 2022-04-29 01:10 UTC

There are other tools for MacOS which are a little prettier than gitk -- ISTR [gitx](https://gitx.frim.nl/seeit.html) being one of them.

**Neil Pilgrim (neiljp)** · 2022-04-29 01:11 UTC

I originally always used to do `git rebase -i HEAD~n` where n was how far back to go; these days I tend to keep up to date and always use main for comparison.

**Neil Pilgrim (neiljp)** · 2022-04-29 01:11 UTC

I use `tig` primarily.

**Alex Vandiver** · 2022-04-29 01:12 UTC

I set the upstream of  each branch when I start working on it, and `git rebase -i` automatically rebases onto that.

**Alex Vandiver** · 2022-04-29 01:13 UTC

http://git-scm.com/downloads/guis looks to have a full list of git GUIs

**Anders Kaseorg** · 2022-04-29 01:14 UTC

I often find `git rebase -i --keep-base upstream` useful, to avoid intermixing the two problems of adjusting my local commits and updating onto newer upstream commits.

**Alex Vandiver** · 2022-04-29 01:16 UTC

Oh, I didn't know about `--keep-base`!  That's handy.

**Adam Sah** · 2022-04-29 01:58 UTC

LOL none of us can agree... maybe not the ideal experience for new users ! :-)

**Anders Kaseorg** · 2022-04-29 02:10 UTC

Nobody ever accused Git of being the ideal experience for new users. But what you’re seeing here isn’t a disagreement. There are different ways of doing things with different tradeoffs on many conficting axes: brevity, generalizability, idiomaticity, memorability, prettiness, readability, safety, teachability, and understandability, to name a few.


## GitHub PR from commit

*2022-06-28 to 2022-06-29 · 7 messages · [open in Zulip](https://chat.zulip.org/#narrow/channel/44-git-help/topic/GitHub.20PR.20from.20commit/with/1398000)*

**Lauryn Menard** · 2022-06-28 16:12 UTC

As an aside, I've been using [Greg's tips](https://github.com/zulip/zulip-mobile/blob/main/docs/howto/git.md#reading-history) for searching git commit history, but I'd love to know how you then get from the commit to the PR.

**Anders Kaseorg** · 2022-06-28 16:22 UTC

I had to search for it manually. Back then PRs were being merged in a way that did not preserve GitHub’s association between the merged commits and the PR.

**Greg Price** · 2022-06-28 19:47 UTC

For completeness, because it's pretty inconspicuous in the GitHub UI, here's how you get from the commit to the PR when GitHub *does* know about the connection: on the commit page, there's a little link just below the description and above the author name and date.

E.g. on https://github.com/zulip/zulip/commit/aabbb2ad1 which is current main, it's the little gray "(#22328)": [image.png](https://chat.zulip.org/user_uploads/2/48/z694-vnaY1lnJMSs-QFHxquJ/image.png)

That should work on any zulip/zulip commit merged in recent years, and any zulip-mobile commit going back further.

**Greg Price** · 2022-06-28 19:53 UTC

(replying to Anders Kaseorg)
> Well, most silly CSS rules are written to (incompletely and over-broadly) cancel the effect of some other silly CSS rule, so it’s worth figuring out what the other one is.

I agree with this, but I suspect at this point that the easiest route might be to try deleting that rule, and see what changes and what looks wrong.

That might not give an answer to what the other rule was in 2017 when this one was added, because that other one might have been removed or fixed since then. But if it doesn't, then it probably doesn't matter.

**Greg Price** · 2022-06-29 21:38 UTC

(I just split this thread off from [here](https://chat.zulip.org/#narrow/stream/19-documentation/topic/Padding.20ordered.20list.20paragraphs/near/1397998).)

**Greg Price** · 2022-06-29 21:39 UTC

(And moved it to this stream; it's not actually about Git, but we don't have a `#github help` and this seems the best home for it.)

**Greg Price** · 2022-06-29 21:43 UTC

(replying to Greg Price)
> That should work on any zulip/zulip commit merged in recent years, and any zulip-mobile commit going back further.

I should qualify this more: this will work on *most* zulip/zulip commits merged in recent years, in particular almost all of them that were merged as part of merging the whole PR.

It still won't work in situations where part of a PR was merged while keeping the PR open, like [here](https://github.com/zulip/zulip/pull/22245#issuecomment-1165203485):
> I merged most of this as the series ending with 6400cd9

because GitHub doesn't have a way to know that those commits (like [6400cd9](https://github.com/zulip/zulip/commit/6400cd93eae150219f6ff43b10267fe077de6d9a) in this example) are from that PR.


## Run/Test an earlier version of codebase

*2022-08-15 to 2022-08-16 · 6 messages · [open in Zulip](https://chat.zulip.org/#narrow/channel/44-git-help/topic/Run.2FTest.20an.20earlier.20version.20of.20codebase/with/1419623)*

**Mounil Shah (mounilKshah)** · 2022-08-15 07:54 UTC

I had a doubt regarding situations where multiple (independent) commits are present in the PR. How can one shift the to an earlier version of the codebase, then test the code and shift back to the latest commit? 
I tried using `git reset HEAD^` for moving backwards one commit at a time and then running the code at that commit. And then using `git reset ORIG_HEAD` to return to the latest commit. But I am not sure if it is the best approach. This usually runs into some issues like `Unmerged files`.

**Neil Pilgrim (neiljp)** · 2022-08-15 16:35 UTC

Whether in your PR, non-pushed branch, or fetched PR, based on what you're mentioning I would suggest an interactive rebase, likely with an `edit` (or just `e`) next to the commit you want to change (or explore). I originally used to do that start from a position back down the stack of commits from `HEAD`, eg. `git rebase -i HEAD~2`, but these days I tend to just refer to `main` instead, assuming the branch is rebased to your local main. I assume you've used something like this before, but if you don't want to make or keep any changes then a `git rebase --abort` will get you back to your original position at the HEAD of the branch.

That said, if you want to ensure commits pass all linting and tests in zulip-terminal CI from a given commit up to HEAD, and your machine is fast enough, it's possible `tools/check-branch` will do what you want - with the proviso of the recent topic I posted in #**zulip-terminal** that `make check` was broken for me until a recent update.

**Greg Price** · 2022-08-15 23:57 UTC

(replying to Mounil Shah (mounilKshah))
> I tried using `git reset HEAD^` for moving backwards one commit at a time and then running the code at that commit. And then using `git reset ORIG_HEAD` to return to the latest commit. But I am not sure if it is the best approach. This usually runs into some issues like `Unmerged files`.

I typically use a variation of these. For those examples, if `main` is the name of my local branch, then:
`git checkout main^` to switch to an earlier commit in the branch for testing
`git checkout main` to switch back to the tip of the branch

**Greg Price** · 2022-08-16 00:00 UTC

The difference between those and the `git reset` version is that with `git reset`, you're modifying the actual branch in addition to changing what commit you're on and what files are in your working tree.

With a command like `git checkout main~3`, you're leaving the branch untouched, and only changing the latter two.

**Neil Pilgrim (neiljp)** · 2022-08-16 06:31 UTC

As long as you --abort the rebase (so as to not modify the branch) then I think the reason I find the interactive rebase good is that I can specifically pick (confirm) which commit I want, rather than figuring that out separately.

**Mounil Shah (mounilKshah)** · 2022-08-16 23:55 UTC

Thank you @Neil Pilgrim (neiljp) and @Greg Price for the suggestions!


## ✔ rebase not working in vagrant container

*2022-08-19 to 2022-08-19 · 5 messages · [open in Zulip](https://chat.zulip.org/#narrow/channel/44-git-help/topic/.E2.9C.94.20rebase.20not.20working.20in.20vagrant.20container/with/1421748)*

**Raghav Luthra** · 2022-08-19 16:37 UTC

I recently started using a vagrant environment with Ubuntu and  was trying to run an interactive rebase when I encountered this error:

```bash
(zulip-py3-venv) vagrant@70ddb9f64826:/srv/zulip$ git rebase -i HEAD~2
hint: Waiting for your editor to close the file... error: cannot run editor: No such file or directory
error: unable to start editor 'editor'
```

I don't get this error outside the vagrant container, but it becomes a problem when I'm trying to run tests in the middle of a rebase since I can't do `./tools/test-*` outside the container.

**Lauryn Menard** · 2022-08-19 17:06 UTC

Ubuntu/vagrant user here. I have two terminal windows open while working.

In one, I run `vagrant ssh` and provision (usually at the start of the day after rebasing main). That's where I run tests, lint and `tools/run-dev.py`.

The other one is in the directory for my cloned repository, but isn't in the virtual environment. And that's where I run git commands and any tools that don't require the virtual environment (e.g., `tools/fetch-rebase-pull-request`).

**Lauryn Menard** · 2022-08-19 17:07 UTC

So, when I want to do an interactive rebase, I run that command in my "git" terminal window, as I think of it. And then I can run tests or the dev server for that commit I'm looking at in the other terminal window.

**Raghav Luthra** · 2022-08-19 20:11 UTC

Thanks a lot!

**Notification Bot** · 2022-08-19 20:11 UTC

@Raghav Luthra has marked this topic as resolved.


## Regarding "help wanted" tag

*2022-08-26 to 2022-08-26 · 1 messages · [open in Zulip](https://chat.zulip.org/#narrow/channel/44-git-help/topic/Regarding.20.22help.20wanted.22.20tag/with/1425275)*

**Notification Bot** · 2022-08-26 00:34 UTC

This topic was moved to #**general>Regarding "help wanted" tag** by @Greg Price.


## Edited Old Commits, moved my edited commit

*2022-08-26 to 2022-10-07 · 18 messages · [open in Zulip](https://chat.zulip.org/#narrow/channel/44-git-help/topic/Edited.20Old.20Commits.2C.20moved.20my.20edited.20commit/with/1425575)*

**Eli Zevin** · 2022-08-26 19:13 UTC

I used `git rebase -i` to go and remove a file from an old commit,
I also used `git reset`, `git restore` and then finished the rebase. Now in git status that commit I was fixing has disappeared and the actual committed files ended up in someone elses commit which was the previous commit.

-why did this happen
-what should/can I do to fix this and bring those changes back to the original commit

**Greg Price** · 2022-08-26 19:16 UTC

(replying to Eli Zevin)
> and the actual committed files ended up in someone elses commit which was the previous commit.

That probably means you used something like `git commit --amend` at the start of the rebase.

**Greg Price** · 2022-08-26 19:17 UTC

That will take changes you currently have uncommitted, and apply them to the current head commit. Which is good when the current head commit is one of your commits you want to modify that way, but wasn't what you intended here.

Instead you wanted something like `git commit` without the `--amend`, which would make a new commit with the changes you currently have uncommitted.

**Greg Price** · 2022-08-26 19:18 UTC

The simplest way to fix it is probably to use the reflog to go back to your previous version of the branch, and then retry the rebase.

**Greg Price** · 2022-08-26 19:21 UTC

`git reflog` will show you the reflog.

`git reflog HEAD@{now}` will show it with timestamps, which can be helpful for reconstructing which entry corresponds to what thing you did.

That will show the commit ID for each version of your branch that's in the reflog. Then `git reset --hard` on that commit ID (e.g., `git reset --hard fa1efe1`) will return your branch to that version.

**Eli Zevin** · 2022-08-26 19:35 UTC

Thank you so much! This worked and helped!

**Eli Zevin** · 2022-08-26 19:43 UTC

second question, while I'm going back through this process of removing a few files from the old git commit. I've ran the `rebase -i` and selected to edit the exact commit in which I would like to remove the files. But while I'm on this commit, the git status says that everything is already pushed up.  Do I need to go back one more commit with `git reset --soft HEAD~1` and then make sure the changes dont get mixed into one?

**Greg Price** · 2022-08-26 19:56 UTC

Selecting to edit the commit you want to edit is correct.

It'll take you to that commit, so that commit is the current HEAD.

Then to edit it, you'll want to make the changes you want (just like you would for making a new commit); and then `git commit --amend`, to edit the current HEAD commit, instead of plain `git commit` which would make a new commit on top.

**Greg Price** · 2022-08-26 19:56 UTC

So e.g. `git rm some/file`, then `git commit --amend`.

**Eli Zevin** · 2022-08-26 20:07 UTC

gotcha, but on that commit it appears all those files for that commit are commited. So how would I remove a file from that commit if its already commited?

**Greg Price** · 2022-08-26 20:29 UTC

Well, first consider how you would make a new commit that removes it. That's a common operation in Git; you use `git rm`.

**Greg Price** · 2022-08-26 20:29 UTC

Then one way you could revise the commit so it doesn't add that file is:
* you make a new commit on top that removes the file;
* then you squash the commits together.

That's a perfectly reasonable way to make edits in general.

**Greg Price** · 2022-08-26 20:30 UTC

In this case you can also do it in fewer steps by using `git commit --amend` to edit the commit, instead of using `git commit` to make a new commit on top and then squashing that.

**Greg Price** · 2022-08-26 20:31 UTC

BTW if you aren't already, I'd highly recommend using a graphical Git browser like `gitk` to see what's happening in your repository / with your changes:
https://zulip.readthedocs.io/en/latest/git/setup.html#get-a-graphical-client

**Greg Price** · 2022-08-26 20:32 UTC

That can help a lot in acquiring a good feel of what's happening when you're in the middle of a rebase, what it means to edit a commit, and so on.

**Eli Zevin** · 2022-08-26 20:40 UTC

awesome thanks! Sorry I was thinking `git rm` removed from the staging area and not the commit. Got it all good now! 
Awesome I will check one out, (currently just using the Git Graph Vs Code extension) but I will look into those!

**Sayam Samal** · 2022-10-07 20:50 UTC

(replying to Greg Price)
> That probably means you used something like `git commit --amend` at the start of the rebase.
I have messed up so many times in something similar, while solving merge conflicts, where I would commit and amend, instead of just adding and continuing rebase. And I couldn't figure out what went wrong till a long time, I stopped doing it only when I read the helper messages from git.

**Sayam Samal** · 2022-10-07 20:51 UTC

I'm really glad to know that there's an actual solution to it with reflog, thanks a ton for this! Will save me hours in future.


## how to abandon a github issue

*2022-10-30 to 2022-10-31 · 3 messages · [open in Zulip](https://chat.zulip.org/#narrow/channel/44-git-help/topic/how.20to.20abandon.20a.20github.20issue/with/1457034)*

**Iano** · 2022-10-30 18:34 UTC

How do I unclaim an issue?

**Prakhar Pratyush** · 2022-10-30 18:42 UTC

(replying to Iano)
> How do I unclaim an issue?
You can use the unassign option on GitHub. It will be on the top-right side of the concerned issue page

**Notification Bot** · 2022-10-31 09:24 UTC

2 messages were moved here from #**documentation>"group-pm-with" search with multiple users** by @Lauryn Menard.


## how to git rebase so that...

*2022-11-04 to 2022-11-04 · 8 messages · [open in Zulip](https://chat.zulip.org/#narrow/channel/44-git-help/topic/how.20to.20git.20rebase.20so.20that.2E.2E.2E/with/1459277)*

**Leslie** · 2022-11-04 00:55 UTC

How do I perform a git rebase so that all the upstream updates don't show up in the compare view on GitHub? 

I tried `git pull upstream main` to update my local `main` branch, and then I switched over to my feature branch and did `git rebase main`.

**Josh Klar** · 2022-11-04 01:01 UTC

Hm, maybe an interactive rebase would help you identify what/why is being included? I also usually recommend specifying the remote alongside the branch: `git fetch upstream && git rebase -i upstream/main`. The text file that opens will provide instructions from there.

**Josh Klar** · 2022-11-04 01:01 UTC

https://github.com/MitMaro/git-interactive-rebase-tool may also be helpful for flows like that if you're not a fan of the text file based flow

**Leslie** · 2022-11-04 03:49 UTC

am dumb :face_palm:

anyone reviewing can just change the branch it's comparing against, so they can just switch the branch to compare upstream/main against mine

**Greg Price** · 2022-11-04 18:01 UTC

One step I highly recommend is to start using `gitk` or another graphical Git viewer:
https://zulip.readthedocs.io/en/latest/git/setup.html#get-a-graphical-client

**Greg Price** · 2022-11-04 18:01 UTC

So e.g. `gitk --all HEAD &` to see everything in the repo

**Greg Price** · 2022-11-04 18:02 UTC

That will give you a picture of what the structure of your branch looks like, how it relates to `upstream/main`, and how those change with the commands you use

**Greg Price** · 2022-11-04 18:04 UTC

In particular what I believe this will do:

(replying to Leslie)
> I tried `git pull upstream main` to update my local `main` branch

is, by default, to create a *merge* commit that combines `upstream/main` into whatever branch you currently have checked out. That's not something you want.


## Squashing commits

*2022-11-14 to 2024-01-10 · 30 messages · [open in Zulip](https://chat.zulip.org/#narrow/channel/44-git-help/topic/Squashing.20commits/with/1463489)*

**Isabella Carmo** · 2022-11-14 18:22 UTC

Hello! I'm actually working on this [PR](https://github.com/zulip/zulip/pull/23528) and I have to squash the 3rd commit to the 1st and 2nd commit. How can I do it? I believe that I can only squash the last two commits (3rd and 2nd) with the first one to have a single commit.

**Matt** · 2022-11-14 18:25 UTC

If you want to write a new commit message:
```
git reset --soft HEAD~3 && git commit
```
You can set ``3`` to however many commits you want to squash, but be careful!

**Aman (amanagr)** · 2022-11-14 18:28 UTC

Yeah, following Matt's approach, just separate the last commit into parts you want to squash into the first and second commit. Then do an interactive rebase using [`git rebase -i HEAD~3`.](https://git-scm.com/book/en/v2/Git-Tools-Rewriting-History#:~:text=The%20interactive%20rebase%20gives%20you,first%20one%20it%20will%20replay.)

**Aman (amanagr)** · 2022-11-14 18:28 UTC

(There maybe faster ways to do it, but I guess this is easier to understand)

**Isabella Carmo** · 2022-11-14 18:42 UTC

Sorry, but I'm a little confused now. How am I going to separate the last commit into two parts? And why would I need to make a `git reset --soft HEAD~3` and then a `git rebase -i HEAD~3`?

**Matt** · 2022-11-14 18:45 UTC

Don't to both, pick one. I almost always want to write a new commit message when I do a squash, so for me the ``reset --soft`` is simplest.

**Anders Kaseorg** · 2022-11-14 18:45 UTC

Squashing all three commits together is not the goal here.

**Aman (amanagr)** · 2022-11-14 18:49 UTC

Just do:
```
git reset HEAD~
git add (files for first commit)
git commit
git add (files for secondcommit)
git commit
```
then do the interactive rebase I mentioned in my previous message.

**Matt** · 2022-11-14 18:49 UTC

Apologies, please ignore my suggestion completely.

**Greg Price** · 2022-11-14 18:51 UTC

(replying to Aman (amanagr))
> Just do: ``` git reset HEAD~ git add (files for first commit) git commit git add (files for secondcommit) git commit ```

(To be a bit more explicit: this part is a set of instructions for splitting up the tip commit into two commits.)

**Isabella Carmo** · 2022-11-14 18:52 UTC

Oh, alright, but I just did a `git reset --soft HEAD~3`. Is there a way I can undo it?

**Greg Price** · 2022-11-14 18:53 UTC

A `git reset --soft HEAD@{1}` should do so.

**Greg Price** · 2022-11-14 18:54 UTC

I also would highly recommend using `gitk` or another graphical Git viewer to see what your repo looks like at each step. That's very helpful for getting a clear picture of what's happening.

**Greg Price** · 2022-11-14 18:55 UTC

(https://zulip.readthedocs.io/en/latest/git/setup.html#get-a-graphical-client)

**Neil Pilgrim (neiljp)** · 2022-11-14 19:01 UTC

One benefit of the interactive rebase is that you have the `--abort` option until you finish rebasing :)

**Isabella Carmo** · 2022-11-14 19:57 UTC

Thank you, guys! One more question, just to make it clear: Now I have these 4 commits: [image.png](https://chat.zulip.org/user_uploads/2/44/UL0_J51shiES3vPurWCwYH6j/image.png) . How could I squash them properly?

**Aman (amanagr)** · 2022-11-14 19:59 UTC

(replying to Aman (amanagr))
> Yeah, following Matt's approach, just separate the last commit into parts you want to squash into the first and second commit. Then do an interactive rebase using [`git rebase -i HEAD~3`.](https://git-scm.com/book/en/v2/Git-Tools-Rewriting-History#:~:text=The%20interactive%20rebase%20gives%20you,fir …
.

**Isabella Carmo** · 2022-11-14 20:02 UTC

But what should I do about the "css: Fix first commit"? Could you just leave it with `pick`?

**Lauryn Menard** · 2022-11-14 20:10 UTC

You can reorder the commits so that they are listed in the order you want. You'll just want to be sure that you're not creating any conflicts when you do so.

So, you can do a `git rebase -i HEAD~4`
```
pick hash-1 css: light theme
squash hash-4 css: fix first commit
pick hash-2 css: dark theme
squash hash-3 css: fix second commit
```

**Isabella Carmo** · 2022-11-14 20:16 UTC

I didn't know I could reorder just like that, thank you so much!

**Josh Klar** · 2022-11-14 21:19 UTC

(replying to Isabella Carmo)
> I didn't know I could reorder just like that, thank you so much!

Another tool you may find useful when doing rebases: https://github.com/MitMaro/git-interactive-rebase-tool. Just a cool lil UI to smooth over some of the UX quirks of the otherwise-`$EDITOR`-based flow

**Neil Pilgrim (neiljp)** · 2022-11-14 21:37 UTC

> https://github.com/MitMaro/git-interactive-rebase-tool

Looks like an interesting tool! There are many features listed there and I hope to take a look, but do you enjoy specific benefits over eg. `vim`?

**Josh Klar** · 2022-11-14 22:02 UTC

I don't personally use it, but mostly for the same reasons I still use (neo)vim itself: I found a workflow that worked before this tool existed and learning a new tool hasn't made the top of my TODO list any time recently among other priorities. I recommend it to folks not already familiar with doing a rebase manually in `vim`-et-al because various friends have had success with it, and the UX seems easier to grok than being thrown into `$EDITOR`

**Chris Bobbe** · 2022-11-16 04:22 UTC

(replying to Lauryn Menard)
> You can reorder the commits so that they are listed in the order you want. You'll just want to be sure that you're not creating any conflicts when you do so. So, you can do a `git rebase -i HEAD~4` ``` pick hash-1 css: light theme squash hash-4 css: fix first commit pick hash-2 css: dark theme squas …

There's a git config option that I find helpful for interactive rebases:

```
git config --add rebase.abbreviateCommands true
```

That means it'll give you

```
p 71abbbdd7 message_edit: Handle truncated topic resolution.
p 4210ab6c4 ifttt: Strengthen types using WildValue.
p f374498f3 papertrail: Strengthen types using WildValue.
p 8010d06f9 compatiblity: Delete obsolete compatibility code.
```

instead of

```
pick 71abbbdd7 message_edit: Handle truncated topic resolution.
pick 4210ab6c4 ifttt: Strengthen types using WildValue.
pick f374498f3 papertrail: Strengthen types using WildValue.
pick 8010d06f9 compatiblity: Delete obsolete compatibility code.
```

, so if you want to change a "pick" to a "fixup", for example, you don't have to delete the whole word "pick" before replacing it with an "f"; you just have to delete a "p". Saves some keystrokes. :smile:

**Temitayo Oyelade** · 2022-12-10 20:20 UTC

Hello, I was told to squash my commits so that I can have my PR reviewed and I was wondering if that means I should also squash the commits that involve syncing my fork. But within this merge includes other contributor's commits. On Git Desktop, it won't let me simply squash my own commits because of the times when I synced my fork. So should I simply squash all the commits and make the commit message reference my own changes, or is there another way to squash only my commits?

**Alex Vandiver** · 2022-12-12 15:00 UTC

@Temitayo Oyelade wrote:
> also squash the commits that involve syncing my fork

That sounds like you have a merge commit.  You should use `git fetch upstream; git rebase upstream/main` to "*rebase*" your commits to get them up to date with the main upstream's commits.

See https://zulip.readthedocs.io/en/latest/git/using.html#keep-your-fork-up-to-date and https://zulip.readthedocs.io/en/latest/git/using.html#examine-and-tidy-your-commit-history and most of that page in general.

**Josh Klar** · 2022-12-12 19:53 UTC

Additionally, if that rebase fails in a non-trivial way, or you still end up with extraneous commits in the log afterwards, look above in this topic at the discussion and instructions around interactive rebasing, which will let you hand-pick which commits are retained on the branch (generally by deleting any lines that aren't your own commits).

**Greg Price** · 2022-12-12 20:30 UTC

In particular I think this advice is highly relevant here:

> I also would highly recommend using `gitk` or another graphical Git viewer to see what your repo looks like at each step. That's very helpful for getting a clear picture of what's happening. (https://zulip.readthedocs.io/en/latest/git/setup.html#get-a-graphical-client)

**Swayam (swayam0322)** · 2024-01-10 13:13 UTC

how to squash commits in my PR #28516 i have been trying to rebase but it isn't working for some reason

**Prakhar Pratyush** · 2024-01-10 13:14 UTC

See: https://zulip.readthedocs.io/en/latest/git/fixing-commits.html#squashing-commits


## locally squash-merging contrib. with attribution+closing PR

*2022-11-22 to 2022-11-23 · 16 messages · [open in Zulip](https://chat.zulip.org/#narrow/channel/44-git-help/topic/locally.20squash-merging.20contrib.2E.20with.20attribution.2Bclosing.20PR/with/1468735)*

**Josh Klar** · 2022-11-22 21:58 UTC

(moving from DM with @Alex Vandiver ): Does anyone remember off-hand the correct way to ensure a manual and local fixup-rebase-merge flow closes the PR as merged (purple icon, not red)? Context being that I want to take a community pull request, squash and reword the commit history, and merge it.  I know I can retain commit author and timestamp with git's CLI and a standard amend/squash, I'm less sure how to appease GitHub's merge detection here. [GitHub's docs](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/incorporating-changes-from-a-pull-request/merging-a-pull-request) imply I can probably do it all in the GUI if I want to do a squash-merge, but also seem to indicate I may not be prompted for a squash commit message, which would defeat the purpose.

Backup plan, since the author of the pull request in question gave us write permission to their fork's branch, is to do a typical interactive rebase and force push, but I'd love to learn how to avoid that in cases like this if possible.

**Anders Kaseorg** · 2022-11-22 22:00 UTC

If you push your updated commits back to the PR (and wait a couple seconds for the PR page to update) before you push the commits upstream, GitHub will detect the PR as merged.

**Josh Klar** · 2022-11-22 22:00 UTC

(and my backup-backup plan is to stop nerd-sniping myself into doing this the right way, do the local rebase-squash-merge flow, and manually close the PR with a comment reading `Merged as abcde123, thanks!`)

**Josh Klar** · 2022-11-22 22:00 UTC

(replying to Anders Kaseorg)
> If you push your updated commits back to the PR (and wait a couple seconds for the PR page to update) before you push the commits upstream, GitHub will detect the PR as merged.
Ah, I see, so I *would* have to push to OP's fork then?

**Anders Kaseorg** · 2022-11-22 22:01 UTC

If you’d like a tool to help with this, we have `tools/push-to-pull-request --merge`.

**Josh Klar** · 2022-11-22 22:02 UTC

oh, that script is excellent. I'm working in docker-zulip right now, but I skimmed that script in `zulip` proper and it appears to do exactly what I was looking for, thank you!

**Greg Price** · 2022-11-22 22:02 UTC

(replying to Josh Klar)
> Ah, I see, so I *would* have to push to OP's fork then?

Yeah. The way GitHub determines that a push it just got represents a merge of a given PR seems to be simply that it includes the PR's branch in its ancestors.

**Greg Price** · 2022-11-22 22:03 UTC

The command I run all the time is
```
$ ../zulip/tools/push-to-pull-request PRNUMBER --merge
```

**Josh Klar** · 2022-11-22 22:04 UTC

Excellent. I'll give it a whirl and report back after I do the rebase.

**Greg Price** · 2022-11-22 22:04 UTC

I do that most often when working in zulip-mobile, but I spell it the same way even when in zulip/zulip for convenience in getting it from my shell history :smile:

**Josh Klar** · 2022-11-22 22:10 UTC

This and `reset-to-pull-request` are amazing, I actually had no idea GH provided inbound PR trees as refs in the target repo, for years I've been doing it the slow way (`git remote add soandso git@github.com:soandso/repo.git; git checkout soandso/weird-branch-name-inevitably`)

**Greg Price** · 2022-11-22 22:11 UTC

Yeah, real handy!

**Greg Price** · 2022-11-22 22:12 UTC

I forget how I first learned those existed. GH doesn't make them particularly discoverable.

Oh, might have been by using `git ls-remote` with the intention of seeing the branches -- that'll show the PR refs in there too.

**Anders Kaseorg** · 2022-11-22 22:14 UTC

I configure a remote this way:

```
[remote "origin"]
        url = https://github.com/zulip/zulip.git
        fetch = +refs/pull/*/head:refs/remotes/origin/pr/*
        fetch = +refs/heads/*:refs/remotes/origin/*
```

so that a plain `git fetch` brings in remote-tracking branches for all PRs.

**Tim Abbott** · 2022-11-23 16:46 UTC

GitHub these days has a CLI that offers some features of these scripts; we can potentially port to their thing but I don't see a clear benefit and it has the downside of needing to install an extra thing.

**Josh Klar** · 2022-11-23 19:20 UTC

(replying to Josh Klar)
> Excellent. I'll give it a whirl and report back after I do the rebase.
I forgot to do as promised and circle back to this: the reset and push to PR scripts are excellent time-savers and worked great over in docker-zulip land. Thanks for the pointers Anders & Greg! Especially enjoyed the pointers in their comments to set up pseudo-refs under `pr/*` prefixes, super useful.


## Invite resend

*2022-11-27 to 2022-11-29 · 6 messages · [open in Zulip](https://chat.zulip.org/#narrow/channel/44-git-help/topic/Invite.20resend/with/1469906)*

**Temitayo Oyelade** · 2022-11-27 00:57 UTC

Hello I have an issue claimed with ZulipBot, however the collaboration link is expired,  Is there a way I can get the link resent so I can hae proper access?

**Alex Vandiver** · 2022-11-28 18:40 UTC

@Temitayo Oyelade: I don't think the invitations expire.  You sure you don't see an invitation at https://github.com/zulip/zulip/invitations ?

**Alex Vandiver** · 2022-11-28 18:41 UTC

Oh, hm, they apparently do.  I wonder what controls the timeframe on that.

What's your Github username?

**Temitayo Oyelade** · 2022-11-28 22:33 UTC

(replying to Alex Vandiver)
> Oh, hm, they apparently do. I wonder what controls the timeframe on that. What's your Github username?
My username is otemitay

**Alex Vandiver** · 2022-11-28 22:38 UTC

@Temitayo Oyelade: You should have a new invite now.

**Temitayo Oyelade** · 2022-11-29 19:49 UTC

Got it! Thank you so much for the help!!


## git-sim tool

*2023-01-23 to 2023-01-23 · 1 messages · [open in Zulip](https://chat.zulip.org/#narrow/channel/44-git-help/topic/git-sim.20tool/with/1495248)*

**Josh Klar** · 2023-01-23 21:16 UTC

I haven't yet used this, but I came across https://initialcommit.com/blog/git-sim today and it looks like a slick contender to throw in our "sometimes you will benefit from a GUI" toolbelt.


## ✔ fetch-rebase-pull-request

*2023-01-25 to 2023-01-26 · 6 messages · [open in Zulip](https://chat.zulip.org/#narrow/channel/44-git-help/topic/.E2.9C.94.20fetch-rebase-pull-request/with/1496573)*

**Palash Baderia** · 2023-01-25 12:42 UTC

Hey everyone, While reviewing my PR #23899, @Aman (amanagr)  pushed a commit and suggested running `./tools/fetch-rebase-pull-request 23408` to fetch the latest changes locally. However, I changed the command to `./tools/fetch-rebase-pull-request 23899` since 23899 is my PR number. Doing so switched me to a new branch with the latest changes called `review-23899`. To continue further, should I open a PR from this new branch or is there a way to get back to the old PR with the latest changes and continue on the existing PR? Thanks.

**Aman (amanagr)** · 2023-01-25 12:56 UTC

You can reset your local branch to `review-23899` or use `./tools/push-to-pull-request 23899`.

**Palash Baderia** · 2023-01-26 01:14 UTC

Thank you so much. It worked for me to close this discussion with the solution so that others can discover it if they need it.
`git reset --hard origin/branch_id`

**Notification Bot** · 2023-01-26 01:14 UTC

@Palash Baderia has marked this topic as resolved.

**Neil Pilgrim (neiljp)** · 2023-01-26 01:26 UTC

For reference, it is my understanding that you should also be able to simply move the branches around by name using something like `git branch -m old new`.

For example, if you want to keep your old branch name, you can
- rename the original branch first (in case you want to refer to it, perhaps)
- then rename the new branch you just fetched using the tool, to the name of the branch you originally pushed

**Palash Baderia** · 2023-01-26 01:30 UTC

(replying to Neil Pilgrim (neiljp))
> For reference, it is my understanding that you should also be able to simply move the branches around by name using something like `git branch -m old new`. For example, if you want to keep your old branch name, you can - rename the original branch first (in case you want to refer to it, perhaps) - t …
That makes a lot of sense, I'll definitely give it a try in the future. Thank you for the suggestion!
That sounds


## ✔ revert old commits after being squashed

*2023-02-02 to 2023-02-06 · 5 messages · [open in Zulip](https://chat.zulip.org/#narrow/channel/44-git-help/topic/.E2.9C.94.20revert.20old.20commits.20after.20being.20squashed/with/1501400)*

**Palash Baderia** · 2023-02-02 17:23 UTC

@Aman (amanagr) I squashed all the commits into one using `git rebase -i Head~2` which included your commit and mine, and now I am not certain how to return to the previous commits. I searched a bit and discovered that using `git reflog` and `git reset --hard <SHA>` might work, but I'm not entirely sure. I'll give it a try. Is there any other method that can assist me with this?

**Aman (amanagr)** · 2023-02-02 17:24 UTC

`git reflog` is the way to go.

**Palash Baderia** · 2023-02-02 17:25 UTC

(replying to Aman (amanagr))
> `git reflog` is the way to go.
Great then, I will give it a try and update the PR soon.

**Palash Baderia** · 2023-02-04 00:10 UTC

(replying to Aman (amanagr))
> `git reflog` is the way to go.
Hey @Aman (amanagr) , I have reverted the commits so that there are now two separate commits, one from you and one from me. Could you please review the PR, Thanks. [PR LINK](https://github.com/zulip/zulip/pull/23899)

**Notification Bot** · 2023-02-06 23:09 UTC

@Palash Baderia has marked this topic as resolved.


## pull request

*2023-02-15 to 2025-01-24 · 43 messages · [open in Zulip](https://chat.zulip.org/#narrow/channel/44-git-help/topic/pull.20request/with/1508584)*

**Hardik Dharmani** · 2023-02-15 20:03 UTC

Hi,
I have created a pull request yesterday in zulip repo.
it is still open.
but I want to create another PR for another issue.
do I have to create another branch in my fork repo before committing changes?

**Palash Baderia** · 2023-02-15 20:22 UTC

(replying to Hardik Dharmani)
> Hi, I have created a pull request yesterday in zulip repo. it is still open. but I want to create another PR for another issue. do I have to create another branch in my fork repo before committing changes?
Hi @Hardik Dharmani , it's always recommended to create a new branch for each new issue. You should never work on your main branch. To create a new branch from the main branch, you can use this command. 
`git checkout -b <Issue Number>`
you can also refer this documentation. https://zulip.readthedocs.io/en/latest/git/using.html

**Hardik Dharmani** · 2023-02-16 07:51 UTC

(replying to Palash Baderia)
> (replying to Hardik Dharmani) ```quote Hi, I have created a pull request yesterday in zulip repo. it is still open. but I want to create another PR for another issue. do I have to create another branch in my fork repo before committing changes? ``` Hi @Hardik Dharmani , it's always recommended t …
Thanks :smile:

**Shashank Singh** · 2023-06-10 08:05 UTC

How do I remove thosa extra commits which gets into my PR whenever i squash and force push with lease my branch to make the commit history clean.
[Screenshot-2023-06-10-at-1.32.55-PM.png](https://chat.zulip.org/user_uploads/2/98/Rdx3wTXjcuUIED8ylqk6aMT4/Screenshot-2023-06-10-at-1.32.55-PM.png)

Due to that the no. of files I changed in my PR increases.

**Satyam Bansal** · 2023-06-10 14:50 UTC

@Shashank Singh  What I generally do when this happens is I tend to remove those commits from my branch using interactive rebase and then just force-push my changes. But be cautious when removing commits -- make sure to not delete yours.

I am not sure if this is the best solution but it works. :shrug: I would love to hear what other folks do to fix this.

**Lalit** · 2023-06-10 14:54 UTC

Yeah when I somehow mess up my commit history, I always rely on interactive rebase to tidy up my commit history!

**Anders Kaseorg** · 2023-06-11 18:12 UTC

You’re getting those extra commits when you rebase `upstream/main` onto your branch. You need to instead rebase your branch onto `upstream/main` (see [keep your fork up to date](https://zulip.readthedocs.io/en/latest/git/using.html#keep-your-fork-up-to-date)). You can recover from this mistake by rebasing your branch onto `upstream/main` again.

**Nimish Medatwal** · 2023-06-27 09:34 UTC

I was cleaning my git commits ( using reword and squash) and when i rebased them this happened .
[image.png](https://chat.zulip.org/user_uploads/2/40/65eahDE_H8e06fTWrmGFAQpO/image.png)
what should I do ?

**Satyam Bansal** · 2023-06-27 10:53 UTC

I would recommend using [interactive rebase](https://thoughtbot.com/blog/git-interactive-rebase-squash-amend-rewriting-history#interactive-rebase) to delete those extra commits and then you can force push to your origin branch.  

Also, read [this](https://chat.zulip.org/#narrow/stream/44-git-help/topic/pull.20request/near/1590891) message to see why it's happening.

**Nimish Medatwal** · 2023-06-27 22:43 UTC

(replying to Satyam Bansal)
> I would recommend using [interactive rebase](https://thoughtbot.com/blog/git-interactive-rebase-squash-amend-rewriting-history#interactive-rebase) to delete those extra commits and then you can force push to your origin branch. Also, read [this](https://chat.zulip.org/#narrow/stream/44-git-help/topi …

[image.png](https://chat.zulip.org/user_uploads/2/f5/4f_VgckLcx5RQBSmYlGBG13Q/image.png)
 Whenever i try using git rebase it shows always shows merge conflicts for every single file i've changed in the commit, has this ever happened to you?

**Junyao Chen** · 2023-07-01 12:10 UTC

Having conflicts means you need to solve conflict first before proceerding to make changes on merged codebase. In your IDE, you may  find those conflicting code blocks asking you how to accept conflicts from different sources

**Nimish Medatwal** · 2023-07-02 20:04 UTC

(replying to Junyao Chen)
> Having conflicts means you need to solve conflict first before proceerding to make changes on merged codebase. In your IDE, you may find those conflicting code blocks asking you how to accept conflicts from different sources

I solved that issue, Thank You

**Notification Bot** · 2023-10-13 01:57 UTC

4 messages were moved from this topic to #**development help>templates linter** by @Greg Price.

**Notification Bot** · 2023-10-16 17:36 UTC

5 messages were moved from this topic to #**development help>pnpm dupe** by @Greg Price.

**Notification Bot** · 2024-08-14 15:18 UTC

A message was moved from this topic to #**code review>pull request** by @Karl Stolley.

**Arpan** · 2024-09-16 15:44 UTC

[Screenshot (98).png](https://chat.zulip.org/user_uploads/2/c5/krS4IH5Y-VS8aGBJ0zEo6hkA/Screenshot-98.png)
[Screenshot (99).png](https://chat.zulip.org/user_uploads/2/d/_ckorfOvCd0hCLaq48tJq9C6/Screenshot-99.png)
2 days back i successfully make a push request and it also merged i see today . then i started to working on a another issue but when i do git pull today my today's commit showing on the old pr why is that . am i done something wrong . i am sorry but how can i do that right . please any one help me .

**Arpan** · 2024-09-16 15:45 UTC

make list item and map non nullable - the commit is for today's pr

**Arpan** · 2024-09-16 15:45 UTC

in panic i closed the issue 1st .

**Arpan** · 2024-09-16 15:47 UTC

do i need to make another branch for whenever i make a new contribution.

**Mateusz Mandera** · 2024-09-16 15:47 UTC

@Arpan Please post links to the pull requests rather than screenshot, that'll let us see directly what the situation there is

**Mateusz Mandera** · 2024-09-16 15:48 UTC

But in short yes, you need a new branch for each new PR

**Arpan** · 2024-09-16 15:49 UTC

thanks for the guidance . is this is the right way to post the link - https://github.com/zulip/zulip-flutter/pull/943

**Arpan** · 2024-09-16 15:50 UTC

what i have to do now i will do that.

**Arpan** · 2024-09-16 16:00 UTC

@Mateusz Mandera what i have to do now

**Arpan** · 2024-09-16 16:01 UTC

how can i change the today's commit in a new branch

**Pratik** · 2024-09-16 16:16 UTC

You could checkout to a new branch. Your current commits will get carried over to this new branch. Then you can just do interactive git rebase and drop a specific commit you wish.

**Arpan** · 2024-09-16 16:17 UTC

you mean if i create a new branch it automatically carried the the commit to the new branch

**Prakhar Pratyush** · 2024-09-16 16:36 UTC

Please read the [Git Guide](https://zulip.readthedocs.io/en/latest/git/index.html). That'll be helpful in the long run.

**Donald Nweyilobu** · 2024-10-12 17:54 UTC

The checks on my pull requests have passed. But I'm seeing somting saying 'This branch has conflicts that must be resolved'. so is it the contributors that resolve the conflicts or is it the one given write access? Also does anyone know how to compare files from a github repository to a local repository

**Mateusz Mandera** · 2024-10-12 18:01 UTC

@Donald Nweyilobu The contributor needs to resolve the conflicts, by rebasing the changes on top of of the current state of the `main` branch and push back to the PR. I recommend reading through our [git guide](https://zulip.readthedocs.io/en/latest/git/index.html) in general

**Donald Nweyilobu** · 2024-10-12 18:06 UTC

I've tried rebasing it. It keeps saying already up to date.

**Mateusz Mandera** · 2024-10-12 18:07 UTC

can  you link your pull request?

**Donald Nweyilobu** · 2024-10-12 18:08 UTC

I will as soon as I can

**Vishesh (NotVishesh)** · 2024-10-12 20:01 UTC

Make sure your  feature branch is up-to-date with the upstreams(Zulip) main branch, and then try to rebase it.
```
git fetch upstream
git rebase upstream/main
```
Helps a lot . but i recommend you to read the git guide https://zulip.readthedocs.io/en/latest/git/index.html

**Ayush khatri** · 2024-11-14 06:21 UTC

I have made a pull request and there is no response yet, why is this?

**Aman (whilstsomebody)** · 2024-11-14 09:56 UTC

You'll need to wait for some time; someone will review your PR. Also, when discussing a PR or issue, be sure to attach a link to it.

**Prakhar Pratyush** · 2024-11-14 11:16 UTC

[#32322](https://github.com/zulip/zulip/pull/32322)

Please fix the commit structure to get it ready for review.

You asked for help in #**GSoC>help squashing commits**  and #**git help>squashing fixup commits**. Did you try to read the docs and fix it as mentioned ?

**Nikhila Etikyala** · 2025-01-19 01:14 UTC

Hello, can someone help me with this error
[image.png](https://chat.zulip.org/user_uploads/2/5b/F0tiTAPsDBArxgF9jnDhliH4/image.png)

**Apoorva Pendse** · 2025-01-19 01:47 UTC

run `tools/lint --fix` on your local.

**Apoorva Pendse** · 2025-01-19 01:48 UTC

See [this](https://zulip.readthedocs.io/en/latest/testing/linters.html) for more details.

**Nikhila Etikyala** · 2025-01-19 02:01 UTC

Thank you @Apoorva Pendse

**Notification Bot** · 2025-01-22 04:42 UTC

17 messages were moved from this topic to #**mobile-dev-help>CI failures in #F1292** by @Greg Price.

**Notification Bot** · 2025-01-24 22:00 UTC

A message was moved from this topic to #**git help>updating PR** by @Greg Price.


## local branches

*2023-02-18 to 2023-02-21 · 7 messages · [open in Zulip](https://chat.zulip.org/#narrow/channel/44-git-help/topic/local.20branches/with/1509561)*

**Hardik Dharmani** · 2023-02-18 13:03 UTC

HI!
i created a branch x from y using git checkout -b x y  (x and y both are local branch, y created from fork)
now when I am making changes to x changes are also happening to y how to stop this?

**Lakshay Mittal** · 2023-02-18 14:04 UTC

Hello @Hardik Dharmani!  Are you committing the changes to the x branch? If you are not committing the changes to a branch and you are switching to another branch that does not contain conflicting changes, git will allow you to switch branches while preserving the state of the working copy.

**Lakshay Mittal** · 2023-02-18 14:09 UTC

It might look like the changes you are making to x are also happening to y but in reality, they are not made in anyone since you did not commit.

**Hardik Dharmani** · 2023-02-18 14:13 UTC

(replying to Lakshay Mittal)
> It might look like the changes you are making to x are also happening to y but in reality, they are not made in anyone since you did not commit.
but even when i committed changes to x they were committed to y also

**Lakshay Mittal** · 2023-02-18 15:04 UTC

That is strange, I do not have an answer for that. Can you share the commands you used (from start)? Maybe relevant terminal history.

**Neil Pilgrim (neiljp)** · 2023-02-18 17:00 UTC

You don't say which tools you're using to confirm what is happening, but various tools can help compare the state of different branches, whether very GUI tools, TUI tools like `tig`, or even those like `git range-diff`.

**Josh Klar** · 2023-02-21 18:55 UTC

This would be rather atypical - branches are refs under the hood, which point at a single commit. A single commit will always have the same parent(s) unless rebased to change, and so typically adding a commit to a base branch cannot impact the child branch (the history has *branched* at this point).

I've heard of folks trying to automate setups like that with CI and the likes, but nothing of the sort happens by default locally. Thirding the recommendation to use a visualization tool of some sort to show what your branch model looks like on disk currently, and perhaps also let us know if you're using any wrapper tools or plugins for Git (be that GitHub's desktop app, some Stacked PRs tool if applicable, whatever.


## git rebase to make branch up to date with main

*2023-03-03 to 2023-03-04 · 8 messages · [open in Zulip](https://chat.zulip.org/#narrow/channel/44-git-help/topic/git.20rebase.20to.20make.20branch.20up.20to.20date.20with.20main/with/1517512)*

**Sushmey** · 2023-03-03 06:33 UTC

Hi, I'm trying to make my PR branch up to date with the main. I'm running 
`git rebase upstream/main`
and then fix the merge conflicts and then my commits get added to the top of the main but the problem is that any other changes anyone else has done in the files I've made changes in get added as my commit. Like not even as a separate commit but inside my commit with the changes I've made. 

How do I rebase without adding this code?

**Lauryn Menard** · 2023-03-03 12:55 UTC

The documentation on [keeping your fork up to date](https://zulip.readthedocs.io/en/latest/git/using.html#keep-your-fork-up-to-date) should be helpful. And maybe double check you've got your [remote repositories set up](https://zulip.readthedocs.io/en/latest/git/cloning.html#step-1c-connect-your-fork-to-zulip-upstream) correctly for your fork?

**Lauryn Menard** · 2023-03-03 12:55 UTC

Here's my process in the command line when I'm starting to work on Zulip, every time:
1. Make sure I'm in my local `main` branch for my forked repository: `git status`
2. Fetch the upstream branch: `git fetch upstream`
3. Rebase my `main` branch: `git rebase upstream/main`
  - I'll note that because I always work on a feature branch, there are never any conflicts here.
4. Pull up the list of my local branches I've been working on: `git branch`
5. Go through the list to rebase all my branches, e.g. for feature branch `fix-typo-in-api-changelog`:
```git rebase upstream/main fix-typo-in-api-changelog```
  - Thanks go to @Greg Price for mentioning this shorthand at some point for rebasing feature branches.
  - As I do this, if there are conflicts I go through, in my IDE, and fix them, stage the updated files and do `git rebase --continue`. Sometimes I do this multiple times if the feature branch has a lot of commits that have conflicts with changes that have been merged with `upstream/main`.
  - The only conflicts that appear are in the files I changed on those feature branches, e.g. for `fix-typo-in-api-changelog`if I've only changed `api_docs/changelog.md`, then the only conflicts that should appear would be in that file. Therefore if other files were coming up in this process, that would be an indication that I had something set up incorrectly.
6. Finally, once all my local work is updated, I switch back to my `main` branch and push it to my fork's `origin` remote branch: `git push origin`, so that's kept up to date as well.

**Lauryn Menard** · 2023-03-03 12:55 UTC

Sometimes before doing the above, I'll skim through #**commits>zulip / main** here so that I know what conflicts to expect when I'm going through the above process.

**Lauryn Menard** · 2023-03-03 12:55 UTC

Also, if you get mixed up or overwhelmed while rebasing a branch, you can do `git rebase --abort` and start over on step 5 for that branch when you're ready, maybe after looking at the commit that was merged upstream that conflicts with your changes to really understand what needs to be fixed.

**Greg Price** · 2023-03-03 19:27 UTC

In addition to all of the helpful information @Lauryn Menard provided, one thought I'll add is that your symptom sounds like when you're handling merge conflicts, you may be producing incorrect resolutions.

Resolving Git merge conflicts is harder out of the box than it should be, but the good news is that with one setting and a bit of technique and practice, it can go a lot more smoothly. See this message and the rest of its thread:

(replying to Greg Price)
> One is that if you haven't already, you should definitely do `git config --global merge.conflictstyle diff3`. That is one setting that it's sad is not the default -- it is basically impossible to reliably and efficiently resolve rebase or merge conflicts without it. (Like, information-theoretically …

**Sushmey** · 2023-03-04 18:30 UTC

Thank you Lauryn for providing the wonderful list of steps to rebase. It'll be really useful since rebasing is such a common thing to do. I use a combination of GitHub desktop and the CLI so it's easier to visualise if the order of commits after rebasing is how I want.

**Sushmey** · 2023-03-04 18:37 UTC

You're right I am dealing with merge conflicts and since I'm using GitHub desktop I can see the conflicts. I've tried deleting the code which I've not written but then it deletes it from the whole commit only, meaning that code wouldn't be there only in the PR I'm pushing to.
I've tried to just delete the merge conflict markers and tried to tidy up the code but still it gets kind of difficult to keep track of what you've written and what someone else has.

I've successfully done a rebase once like a few months ago and I'm pretty sure I followed the [zulip docs](https://zulip.readthedocs.io/en/latest/git/using.html#keep-your-fork-up-to-date) but I can't figure out now what's going wrong.

I'll go through the thread you've sent and hopefully that solves it. Thanks Greg!


## permission denied

*2023-04-19 to 2023-04-19 · 6 messages · [open in Zulip](https://chat.zulip.org/#narrow/channel/44-git-help/topic/permission.20denied/with/1551472)*

**Neil Gupta** · 2023-04-19 20:32 UTC

Hello! My name is Neil and I am working on an open source issue:  https://github.com/zulip/zulip/issues/23692. I created a branch and have an implementation for this issue, however when I try to push and create a pull request git is not letting me. It is saying permission is denied. I have claimed this issue on github and have been identified as a collaborator. Any help on this would be great!

**Neil Gupta** · 2023-04-19 20:39 UTC

Hello! My name is Neil and I am working on an open source issue: https://github.com/zulip/zulip/issues/23692. I created a branch and have an implementation for this issue, however when I try to push and create a pull request git is not letting me. It is saying permission is denied. I have claimed this issue on github and have been identified as a collaborator. Any help on this would be great!

**Tim Abbott** · 2023-04-19 20:42 UTC

@Neil Gupta I'd recommend reading our [Git guide](https://zulip.readthedocs.io/en/latest/git/index.html) carefully -- it has advice for among other things, how to set up Git remotes for development.

**Tim Abbott** · 2023-04-19 20:42 UTC

My guess is you're trying to push not to your fork (which is where one pushes to create a pull request), but to the official zulip/zulip repository, which you don't have permission to do.

**Tim Abbott** · 2023-04-19 20:50 UTC

@Neil Gupta I replied to the copy of this question in #**general>permissions**; I guess I'll move that copy here. But please follow our community guidelines and don't re-ask the same question in multiple places.

**Notification Bot** · 2023-04-19 20:51 UTC

3 messages were moved here from #**general>permissions** by @Tim Abbott.


## ✔ Merge conflict while rebasing

*2023-04-20 to 2023-04-20 · 2 messages · [open in Zulip](https://chat.zulip.org/#narrow/channel/44-git-help/topic/.E2.9C.94.20Merge.20conflict.20while.20rebasing/with/1551875)*

**Syed Rafat** · 2023-04-20 09:05 UTC

[Screenshot-49.png](https://chat.zulip.org/user_uploads/2/81/NR0cEVM_H4lSMyaPwx3CSpFN/Screenshot-49.png)
I am stuck here, I was trying to squash 3 commits together and the interactive rebase got stuck in merge conflict. What should I do here?

**Notification Bot** · 2023-04-20 11:17 UTC

@Syed Rafat has marked this topic as resolved.


## ✔ git pulled all other commits into feature branch

*2023-05-08 to 2023-05-08 · 5 messages · [open in Zulip](https://chat.zulip.org/#narrow/channel/44-git-help/topic/.E2.9C.94.20git.20pulled.20all.20other.20commits.20into.20feature.20branch/with/1563395)*

**Syed Rafat** · 2023-05-08 12:16 UTC

I could not push to origin/ feature branch because it was showing that my feature branch was ahead for some reason. So I pulled from origin and then pushed, but it merged all the latestt commit to the feature branch?

What should I do now? Should I just delete the pull request and start another again? This time fixing everything as it should be with the rebase workflow?

**Syed Rafat** · 2023-05-08 12:21 UTC

[Screenshot-52.png](https://chat.zulip.org/user_uploads/2/a4/rkkpyi9PpIc813bSxIWajk3H/Screenshot-52.png)

**Notification Bot** · 2023-05-08 12:31 UTC

@Syed Rafat has marked this topic as resolved.

**Syed Rafat** · 2023-05-08 12:34 UTC

I was able to fix this by reseting the last commit with
`git reset --hard HEAD^`
then  `git rebase upstream/main`
then `git push --force origin mark-read-for-private-narrow`  which overwrote commit history to the remote origin

**Syed Rafat** · 2023-05-08 12:35 UTC

Just leaving it here if anyone needs it.


## Permission denied - committing someone else's PR.

*2023-06-20 to 2023-06-21 · 6 messages · [open in Zulip](https://chat.zulip.org/#narrow/channel/44-git-help/topic/Permission.20denied.20-.20committing.20someone.20else.27s.20PR.2E/with/1595830)*

**Palash Baderia** · 2023-06-20 17:59 UTC

I recently worked on moving this PR #22903 forward. To do so, I followed the [zulip-guide](https://zulip.readthedocs.io/en/latest/git/collaborate.html) on collaborating with others. However, when pushing the changes to the PR, I encountered this issue:

```shell
git push yogesh-sirsat yogesh-sirsat/emtpy_field_choices

remote: Permission to yogesh-sirsat/zulip.git denied to palashb01.
fatal: unable to access 'https://github.com/yogesh-sirsat/zulip.git/': The requested URL returned error: 403
```

**Lalit** · 2023-06-20 18:00 UTC

You can't push code to someone else's repo directly unless you are a maintainer.

**Lalit** · 2023-06-20 18:01 UTC

So either you should raise a new PR with your changes or open a PR in the fork of `yogesh-sirsat`.

**Palash Baderia** · 2023-06-20 18:02 UTC

~~Could you please elaborate on what you mean by "in the fork of"?~~

**Palash Baderia** · 2023-06-20 18:03 UTC

okay got it, thanks :)

**Neil Pilgrim (neiljp)** · 2023-06-21 07:34 UTC

Also of note are the scripts right at the bottom of that page; after fetching the branch locally you can rename it to whatever you like, as with the other approach.


## ✔ commit message

*2023-09-03 to 2023-09-04 · 2 messages · [open in Zulip](https://chat.zulip.org/#narrow/channel/44-git-help/topic/.E2.9C.94.20commit.20message/with/1634818)*

**Shashank Singh** · 2023-09-03 20:11 UTC

Can anyone tell me what is the format to add period in my commit message.
[Screenshot-2023-09-03-at-6.39.20-PM.png](https://chat.zulip.org/user_uploads/2/e5/SaIzp9pvpwan2QlLQGpkLxOe/Screenshot-2023-09-03-at-6.39.20-PM.png)
As i was recently advised to update my commit message. 
Specifically what is the format of adding period and giving suggestion credits in my commit message.

**Notification Bot** · 2023-09-04 05:04 UTC

@Shashank Singh has marked this topic as resolved.


## refactoring pull request

*2023-09-23 to 2023-09-27 · 3 messages · [open in Zulip](https://chat.zulip.org/#narrow/channel/44-git-help/topic/refactoring.20pull.20request/with/1646043)*

**Sudip Bose** · 2023-09-23 19:40 UTC

Is it a good idea to show all of the commits made up until now in a pull request. I needed to refactor my PR. after pushing changes to my working branch I can see in the files-changes tab 639 files changed, while in fact I only changed one file. It actually showing all of the commits. So is it a good idea to show that? If not can I further refactor it?

**Tim Abbott** · 2023-09-24 22:51 UTC

@Sudip Bose check out the PR sections in https://zulip.readthedocs.io/en/latest/git/index.html, but I'm guessing you somehow rebased `main` onto your code, rather than the other way around.

**Sudip Bose** · 2023-09-27 17:48 UTC

(replying to Tim Abbott)
> @Sudip Bose check out the PR sections in https://zulip.readthedocs.io/en/latest/git/index.html, but I'm guessing you somehow rebased `main` onto your code, rather than the other way around.

Thanks Tim for helping me out! 
I have fixed it.


## Project Clone Issue

*2023-10-04 to 2023-12-25 · 13 messages · [open in Zulip](https://chat.zulip.org/#narrow/channel/44-git-help/topic/Project.20Clone.20Issue/with/1654228)*

**rinwa** · 2023-10-04 01:06 UTC

[image.png](https://chat.zulip.org/user_uploads/2/e0/CfZGW4UjUO-m3Y_ey36ARj8E/image.png)
 I keep getting this error message when i try to clone the zulip project locally. I've tried adding private ssh-keys it didn't

**Ndifon Titiana Sih** · 2023-10-04 01:27 UTC

Am having same issues I have changed ssh key and public keys numerous times nothing yet

**Esther Anierobi** · 2023-10-06 14:28 UTC

[Quoting…]

Hi Nidfon, have you been able to resolve it?

**Karl Stolley** · 2023-10-06 14:48 UTC

@Ndifon Titiana Sih, what's the contents of your `.ssh/` directory? run `la -la ~/.ssh/`

**Ndifon Titiana Sih** · 2023-10-06 15:19 UTC

Thank you @Esther Anierobi @Karl Stolley  
I fixed that already , Right now i have problems starting my development environment.
when i run "vagrant plugin install vagrant-vbguest" it installs quite alright , and when i further run "vagrant up --provider=virtualbox" i start getting the following errors.  Am working with windows
[image.png](https://chat.zulip.org/user_uploads/2/29/eBoXBnXpDknI6NN5Yti1tqkq/image.png)
 I have turned on virtualization and hyper-v , i also tried using oracle virtual box but it didn't work out . 
Any idea how i can resolve this?

**Chisom** · 2023-10-06 15:24 UTC

Hi, Ndifon, I use Windows too but I didn't go the vagrant way during my setup

**Esther Anierobi** · 2023-10-06 15:29 UTC

(replying to Ndifon Titiana Sih)
> Thank you @Esther Anierobi @Karl Stolley I fixed that already , Right now i have problems starting my development environment. when i run "vagrant plugin install vagrant-vbguest" it installs quite alright , and when i further run "vagrant up --provider=virtualbox" i start getting the followi …

Okay Ndifon, I had similar error before though I'm using mac.
But what I did was open my virtualbox GUI and it run perfectly.
check discussions  in "Outreachy > development environment help" I know someone has same error with windows.

**Karl Stolley** · 2023-10-06 16:36 UTC

I'm not a Windows user, but I'd start by doing the things described in those error messages.

**Ndifon Titiana Sih** · 2023-10-06 22:01 UTC

I will keep trying them

**Notification Bot** · 2023-11-30 15:19 UTC

2 messages were moved from this topic to #**provision help>Docker issue** by @Karl Stolley.

**Jayant Pranjal** · 2023-12-06 17:26 UTC

[image.png](https://chat.zulip.org/user_uploads/2/8f/uljVhSWYFDKxmNo12Dn48ani/image.png)


Can someone help me with it??

**Aman (amanagr)** · 2023-12-06 17:32 UTC

You need to setup your ssh key correctly. Search online for it.

**Notification Bot** · 2023-12-25 03:27 UTC

3 messages were moved from this topic to #**provision help>activate not working** by @Greg Price.


## Github Actions

*2023-10-18 to 2023-10-18 · 1 messages · [open in Zulip](https://chat.zulip.org/#narrow/channel/44-git-help/topic/Github.20Actions/with/1664692)*

**Notification Bot** · 2023-10-18 16:35 UTC

This topic was moved to #**development help>curl error in  CI** by @Greg Price.


## Cleaning up commit history

*2023-10-20 to 2023-10-20 · 5 messages · [open in Zulip](https://chat.zulip.org/#narrow/channel/44-git-help/topic/Cleaning.20up.20commit.20history/with/1666057)*

**Aditya Kale** · 2023-10-20 13:53 UTC

:wave: there. I am a beginner both in open source as well as Zulip, so if this issue looks very trivial I apologize in advanced
I created a pull request https://github.com/zulip/zulip/pull/27199 which was able to pass all the tests but I am not able to understand on how to  cleanup commit history. Also I looked up the documentation but was unable to understand anything worthwhile.

**Sol** · 2023-10-20 14:10 UTC

hello you would be able to do that with the `git rebase` command. In your case, assuming on the correct branch `git rebase -i HEAD~2` will allow you to edit the two last commits

**Notification Bot** · 2023-10-20 14:14 UTC

This topic was moved here from #**issues>Cleaning up commit history** by @Karl Stolley.

**Aditya Kale** · 2023-10-20 14:37 UTC

Actually I did that and changed the first commit from something which was above 30 characters to `Change file name from display_settings.js to display_preferences.js`
It was only after that I created an issue. Rather than git rebase, I think I don't know how to write a good commit title so I asked for help on what should be improved.

**Esther Anierobi** · 2023-10-20 15:05 UTC

Hi Aditya, here is a link for writing a good commit:[commit discipline](https://zulip.readthedocs.io/en/latest/contributing/commit-discipline.html)


## Tests not running on github

*2023-11-30 to 2023-11-30 · 7 messages · [open in Zulip](https://chat.zulip.org/#narrow/channel/44-git-help/topic/Tests.20not.20running.20on.20github/with/1692087)*

**Nimish Medatwal** · 2023-11-30 06:34 UTC

Tests are not running on pr #27841. I thought maybe rebasing and pushing code again will fix the issue but it didn't. Can anyone explain why is this happening ? Also zulipbot keeps adding `has conflict` tag cause I renamed two help files. How can I prevent that from happening ?
[image.png](https://chat.zulip.org/user_uploads/2/3d/MtTwjZ6zijvaqoBwPaR8Hlex/image.png)
[image.png](https://chat.zulip.org/user_uploads/2/4/CHS5nk8bAR9raHTNqv8S74zP/image.png)

**Anders Kaseorg** · 2023-11-30 06:54 UTC

zulipbot is correct—you really do need to follow its instructions and rebase your PR on `upstream/main`.

**Nimish Medatwal** · 2023-11-30 06:56 UTC

(replying to Anders Kaseorg)
> zulipbot is correct—you really do need to follow its instructions and rebase your PR on `upstream/main`.

I just did that, it removed the `has conflict` tag , then added the tag again.

**Anders Kaseorg** · 2023-11-30 06:56 UTC

I just checked. Your branch is 281 commits behind `upstream/main`.

**Anders Kaseorg** · 2023-11-30 06:57 UTC

And there really are conflicts that you’re going to resolve manually when you rebase it.

**Anders Kaseorg** · 2023-11-30 07:00 UTC

Your push 39 minutes ago did not advance the base commit, which is still from a week ago (and this was quite a busy week).

**Nimish Medatwal** · 2023-11-30 07:02 UTC

(replying to Anders Kaseorg)
> Your push 39 minutes ago did not advance the base commit, which is still from a week ago (and this was quite a busy week).

Okay got it, thank you.


## Issue with rebase

*2023-12-01 to 2023-12-10 · 6 messages · [open in Zulip](https://chat.zulip.org/#narrow/channel/44-git-help/topic/Issue.20with.20rebase/with/1692661)*

**Tuba Mouqeem** · 2023-12-01 02:39 UTC

I am trying to rebase my main branch but this error is occurring again and again
[git-issue.png](https://chat.zulip.org/user_uploads/2/5c/MFYzyr4Sax_BMFIKIz_xL9Se/git-issue.png)

**Aman (amanagr)** · 2023-12-01 02:55 UTC

Your git cache is likely disturbed you can likely find solutions to reset it online.

**Tuba Mouqeem** · 2023-12-01 02:56 UTC

Thanks, okay let me do it first

**Tuba Mouqeem** · 2023-12-10 01:55 UTC

@Aman (amanagr) I have tried to solve it but still facing this issue 
[image.png](https://chat.zulip.org/user_uploads/2/88/mDi1WfYWoNtYtjb91BxgVmsI/image.png) 
[image.png](https://chat.zulip.org/user_uploads/2/f8/8NRqgHhz4fIrnJCvp7Y2xCUA/image.png)

**Aman (amanagr)** · 2023-12-10 04:02 UTC

Use WSL terminal please.

**Tuba Mouqeem** · 2023-12-10 13:38 UTC

@Aman (amanagr) yeah i tried it and it worked thanks


## How to use a piece of code that is shared across two PRs?

*2023-12-10 to 2023-12-10 · 5 messages · [open in Zulip](https://chat.zulip.org/#narrow/channel/44-git-help/topic/How.20to.20use.20a.20piece.20of.20code.20that.20is.20shared.20across.20two.20PRs.3F/with/1699028)*

**Sayam Samal** · 2023-12-10 05:29 UTC

So, while working on #27815, I have introduced a global CSS variable `--popover-menu-min-width. Now I also want to use this variable in my other PR #28092. What's the best way to do this?

**Sayam Samal** · 2023-12-10 05:30 UTC

Include the same code twice, and solve merge conflicts if they arise? Cherry-pick? Rebase? I haven't encountered this case before, hence the confusion.

**Aman (amanagr)** · 2023-12-10 05:34 UTC

Just rebase the new PR on the old PR.

**Sayam Samal** · 2023-12-10 05:36 UTC

Excuse my confusion, but what happens if only the newer PR is the one that needs to be merged first?

**Aman (amanagr)** · 2023-12-10 07:33 UTC

Just mention about the common commits in the new PR.


## Test failed in PR

*2023-12-29 to 2024-06-24 · 5 messages · [open in Zulip](https://chat.zulip.org/#narrow/channel/44-git-help/topic/Test.20failed.20in.20PR/with/1710638)*

**Joydeep Bhattacharjee** · 2023-12-29 08:48 UTC

I have created a PR [28379](https://github.com/zulip/zulip/pull/28379) but unfortunately some lint test failed. What should be the steps I follow now to create the PR again.

**Anders Kaseorg** · 2023-12-29 09:07 UTC

Do not create another PR; [update the existing one](https://zulip.readthedocs.io/en/latest/git/pull-requests.html#update-a-pull-request).

**Joydeep Bhattacharjee** · 2023-12-29 10:34 UTC

After I fix my test  as per the [commit discipline](https://zulip.readthedocs.io/en/latest/contributing/commit-discipline.html) I should not write a new commit message but edit the old one with `--ammend`. So if I do that I've to force push to my origin (the one I forked). Is it okay to do that? Also if I do that will it update the pull request as well?

**Anders Kaseorg** · 2023-12-29 19:29 UTC

Yes.

**Notification Bot** · 2024-06-24 14:18 UTC

A message was moved from this topic to #**development help>Failing puppeteer test in #29584** by @Lauryn Menard.


## reusing branches

*2024-01-05 to 2024-01-05 · 1 messages · [open in Zulip](https://chat.zulip.org/#narrow/channel/44-git-help/topic/reusing.20branches/with/1714366)*

**Alex Vandiver** · 2024-01-05 19:48 UTC

@Rohan Gudimetla [said](https://chat.zulip.org/#narrow/stream/378-api-design/topic/pinning.20topics.20of.20a.20stream/near/1714362):
> Sorry regarding opening a new PR. Due to some confusion, my previous PR reused an existing endpoint, and I lost track of the changes to make it follow a new endpoint as per feedback. Hence, I had to use a duplicate branch and open a separate PR.

It's always possible to update your local git repo to put entirely new commits on an old branch.

For example, it looks like your old branch was named `iss-19483`.  If you wanted to drop all of your local commits and start fresh on that branch:
```shell
git fetch upstream
git checkout iss-19483
git reset --hard upstream/main
# ... work
git commit
# ... work
git commit
git push -f
```

If you wanted to leave that old branch around while trying a new version:
```shell
git fetch upstream
git checkout -b new-version upstream/main
# ... work
git commit
# ... work
git commit

# OK, satisfied with the new version, switch the old branch to it!
git checkout iss-19483
git reset --hard new-version
git push -f
```


## Commit message

*2024-01-08 to 2025-01-13 · 44 messages · [open in Zulip](https://chat.zulip.org/#narrow/channel/44-git-help/topic/Commit.20message/with/1715248)*

**Tuba Mouqeem** · 2024-01-08 05:36 UTC

I was trying to fix commit message and during this process i used git rebase command to make  my existing PR up to date now it is showing 454 commit messages, how fix it? Should i make new PR?
[image.png](https://chat.zulip.org/user_uploads/2/d0/rjjWZk9j35OQ3OwMcgBQnXwR/image.png)

**Aman (amanagr)** · 2024-01-08 05:46 UTC

Reset your PR to `upstream/main` and cherry-pick the commits you want.

**Tuba Mouqeem** · 2024-01-08 06:01 UTC

I tried to find my own commit, but my commit is not showing.  It was starting with commit summary "notifications: "
[image.png](https://chat.zulip.org/user_uploads/2/aa/R8sYsXr45-PC5uuBmh6tugl9/image.png)

**Greg Price** · 2024-01-08 19:06 UTC

This symptom typically comes from rebasing upstream/main onto your branch. Instead, you want to rebase your branch onto upstream/main. See our docs: https://zulip.readthedocs.io/en/latest/git/using.html#keep-your-fork-up-to-date

**Greg Price** · 2024-01-08 19:09 UTC

Use a graphical Git viewer like `gitk` to help see what's happening:
https://zulip.readthedocs.io/en/latest/git/setup.html#get-a-graphical-client

**Greg Price** · 2024-01-08 19:10 UTC

There's no need to make a new PR (and doing so won't help). Once your branch is fixed, you can just push back to your existing PR to update it.

**Tuba Mouqeem** · 2024-01-08 21:20 UTC

Thank you for the help

**Tuba Mouqeem** · 2024-01-08 22:50 UTC

@Greg Price i tried gitk and unable to find there also. It seems my commit message has deleted there is no history of it, can i make new branch and make new PR on that?
[image.png](https://chat.zulip.org/user_uploads/2/ee/RwwgTQ3rBiwslxvDeFAGjVHB/image.png)

**Greg Price** · 2024-01-08 22:54 UTC

You can find your previous commit in the reflog:
https://zulip.readthedocs.io/en/latest/git/troubleshooting.html

**Greg Price** · 2024-01-08 22:55 UTC

The best strategy is probably to use the reflog to get back to where you were before you did the rebase. Then try again, and this time rebase your branch onto upstream/main.

**Greg Price** · 2024-01-08 22:55 UTC

Also there's generally no need to @-mention core contributors here — see our community norms:
https://zulip.com/development-community/#getting-help

**Tuba Mouqeem** · 2024-01-08 23:38 UTC

Thanks for mentioning it, i will follow these rules

**Gaurav Kushwaha** · 2025-01-08 17:05 UTC

Hello,
I was having some confusion regarding commit messages.

PR: [#1213](https://github.com/zulip/zulip-flutter/pull/1213#issuecomment-2576558500) 

Here, I made some changes but the commit messages are not proper which I am not getting what should be a proper commit message. Please tell what commit messages that I should keep while rebasing.

Here are the changes:
- I updated `DesignVariables` constant values based on their values in figma design.
- I updated `MessageListTheme` constant values based on their values in figma design.

Thank You.

**Apoorva Pendse** · 2025-01-08 17:21 UTC

[I think you can remove this](https://github.com/zulip/zulip-flutter/pull/1213/commits/3af0d2eda2fe7393470979bc1faf41b703ba1c32#:~:text=%2D%20I%20have%20dropped%20some%20%60merge%60%20commits%20of%20%60zulip%3Amain%60%20into%20%60TweakDarkTheme%60.%0A%2D%20So%2C%20I%20have%20dropped%20to%20later%20again%20rebase%20(squash)%20them.%0A%2D%20I%20am%20using%20rebase%20first%20time%2C%20sorry%20if%20I%20have%20done%20something%20wrong.)

**Apoorva Pendse** · 2025-01-08 17:21 UTC

Just explain the part of the code you've changed and why, no need to use "I".

**Apoorva Pendse** · 2025-01-08 17:22 UTC

See this [example commit message](https://github.com/zulip/zulip/commit/4869e1b0b2bc6d56fcf44b7d0e36ca20f45d0521) in the [commit discipline documentation](https://zulip.readthedocs.io/en/latest/contributing/commit-discipline.html#examples-of-good-commit-messages).

**Apoorva Pendse** · 2025-01-08 17:23 UTC

Attach the issue number your commit fixes as the last paragraph of your commit message.
```Fixes #973.``` in your case.

**Apoorva Pendse** · 2025-01-08 17:24 UTC

It might also be a good idea to attach the CZO link where the colors were discussed in the commit description.

**Apoorva Pendse** · 2025-01-08 17:26 UTC

For gaining better idea, see the merged commits of the other contributors  here: https://github.com/zulip/zulip-flutter/commits/.
The [latest merged commit](https://github.com/zulip/zulip-flutter/commit/0b90e421dbff8b35fee3e8768cbf0e6d2f0cccba) is also a good example of what is expected.

**Apoorva Pendse** · 2025-01-08 17:28 UTC

Also try following the [formatting guide](https://zulip.readthedocs.io/en/latest/contributing/commit-discipline.html#formatting-guidelines) AMAP.

**Gaurav Kushwaha** · 2025-01-08 20:21 UTC

(replying to Apoorva Pendse)
> For gaining better idea, see the merged commits of the other contributors here: https://github.com/zulip/zulip-flutter/commits/. The [latest merged commit](https://github.com/zulip/zulip-flutter/commit/0b90e421dbff8b35fee3e8768cbf0e6d2f0cccba) is also a good example of what is expected.

Thank you for your help.
I think this should be my commit message.

------
theme: Update theme variables for dark theme

This change updates the dark theme variables in `DesignVariables` and 
`MessageListTheme` acc. to their values in [Figma design](https://www.figma.com/design/1JTNtYo9memgW7vV6d0ygq/Zulip-Mobile?node-id=4514-33396&t=bMNXsr5LwkrHz4dp-1).
CZO Discussion: https://chat.zulip.org/#narrow/stream/137-feedback/topic/design.20feedback/near/1950672

Fixes: #973
------

Is it fine now?

**Gaurav Kushwaha** · 2025-01-08 20:25 UTC

[Screenshot from 2025-01-09 01-51-32.png](https://chat.zulip.org/user_uploads/2/c7/AKDDl_wCIdNn1-9uwkB1ik5t/Screenshot-from-2025-01-09-01-51-32.png)

Also, like when I am rebasing for editing the commit message.
After changing `pick` to `edit`. 
How do I add the description of the commit in that line along with the title?

**Apoorva Pendse** · 2025-01-08 20:28 UTC

(replying to Gaurav Kushwaha)
```
Is it fine now?
````
Yes, LGTM.

**Apoorva Pendse** · 2025-01-08 20:29 UTC

(replying to Gaurav Kushwaha)
> Also, like when I am rebasing for editing the commit message.


You can just use `git commit --amend` to edit the commit message of your latest commit.

**Apoorva Pendse** · 2025-01-08 20:33 UTC

(replying to Gaurav Kushwaha)
> After changing `pick` to `edit`. How do I add the description of the commit in that line along with the title?
You can use `reword` instead of `edit `

**Aman (whilstsomebody)** · 2025-01-09 07:58 UTC

(replying to Gaurav Kushwaha)
> [Screenshot from 2025-01-09 01-51-32.png](https://chat.zulip.org/user_uploads/2/c7/AKDDl_wCIdNn1-9uwkB1ik5t/Screenshot-from-2025-01-09-01-51-32.png) Also, like when I am rebasing for editing the commit message. After changing `pick` to `edit`. How do I add the description of the commit in that line along with the title?

See, each line in a commit can have max of 72 chars. So the first 72(or fewer) chars of the first line are included as the commit summary and  rest goes to the description block.

For example;

```
name: This is my name.
My name us so and so.

```

In this example, the first line serves as commit summary and the second line is the description.

Lets take another example;

```
introduction: This is my name, this is my work, this is my address. this is my car .
Description of intro goes here.

```
Since the first line has more than 72 chars, so this commit will appear as follows:

```
introduction: This is my name, this is my work, this is my address. thi...
s is my car.
Description of intro goes here.

```
In conclusion, after 72 characters on the first line, everything is included in the description. 
I hope this is clear.

**Gaurav Kushwaha** · 2025-01-09 10:16 UTC

Thank you ,
I understood the commit structure and some useful tips from both of you like not to use `I`.

**Apoorva Pendse** · 2025-01-09 10:18 UTC

Happy to help :octopus:

**Gaurav Kushwaha** · 2025-01-09 10:38 UTC

Just one more thing, 
Like if I am rebasing to restructure 4 commits in one of my PR.

There I wanna squash 3 commits with a new title and description to it's message and also add description to my 4th commit message.
[Screenshot from 2025-01-09 15-54-44.png](https://chat.zulip.org/user_uploads/2/c1/Xy2J12KioAqW8a_GTPqeudQB/Screenshot-from-2025-01-09-15-54-44.png)

Here, what is happening after changing `pick` to `squash` for first three and `pick` to `reword` in last commit, it is asking for a new commit message for the squashed commits (-**). 
But after entering the commit message for squash commit (acc. to me), I force pushed the changes.
And what I am seeing is that I have pushed a commit with all 4 commits merged into a single one and the message that I am seeing is the message I added for squash (here **).

**Gaurav Kushwaha** · 2025-01-09 10:39 UTC

That means my 4 commits that I wanted to squash (first three) and reword (last one), was pushed as a single commit with the message I added for squash.

**Aman (whilstsomebody)** · 2025-01-09 10:41 UTC

So, if you want to squash first three commits, just change the pick for the second and third only.

**Aman (whilstsomebody)** · 2025-01-09 10:42 UTC

This will first squash the first and second  at first then make a single commit for the two, then move to squash the resultant with the third one.

**Gaurav Kushwaha** · 2025-01-09 10:45 UTC

(replying to Aman (whilstsomebody))
> So, if you want to squash first three commits, just change the pick for the second and third only.

I want to squash first three and change commit message of last one. Totally there are 4 commits and all are pushed ones.

**Aman (whilstsomebody)** · 2025-01-09 10:46 UTC

Umm, not clearly understanding what you want to ask.

**Apoorva Pendse** · 2025-01-09 10:48 UTC

```
pick a
squash b
squash c
reword d
```
Should do what you want, if I understand your message correctly

**Gaurav Kushwaha** · 2025-01-09 10:48 UTC

In that screenshot, 
1) I want to squash these commits into a single one with a single commit message.
```
pick 1f412295 Same user messages undistinguishable issue is resolved now.
pick 7629b01d Shifted from Container to DecoratedBox
pick 5bf999b2 pressedTint updated for both themes
```

2) I want to change commit message and add description to this commit.
```
pick 0794bb07 test: Added tests for above commits
```

**Aman (whilstsomebody)** · 2025-01-09 10:48 UTC

(replying to Apoorva Pendse)
> ``` pick a squash b squash c reword d ``` Should do what you want, if I understand your message correctly
yeah this is right. This is what I am saying

**Aman (whilstsomebody)** · 2025-01-09 10:49 UTC

(replying to Gaurav Kushwaha)
> In that screenshot, 1) I want to squash these commits into a single one with a single commit message. ``` pick 1f412295 Same user messages undistinguishable issue is resolved now. pick 7629b01d Shifted from Container to DecoratedBox pick 5bf999b2 pressedTint updated for both themes ``` 2) I want to …


So, just change pick to squash(s) for second and third only. Change pick to reword(r) for the last one. Thats it.

**Gaurav Kushwaha** · 2025-01-09 10:56 UTC

(replying to Aman (whilstsomebody))
> yeah this is right. This is what I am saying

Okay, after this;
I added a commit message to complete my rebase. 
Now, this message will be for my squashed commits or reword commit. 
This is what I was asking.

**Aman (whilstsomebody)** · 2025-01-09 11:00 UTC

You will be taken to the commit edit terminal thrice in the process.

Will squashing first and second 
then for the resultant of first and second and third.
In the squashing process, the terminal will display the commit messages from botht he commits to be squashed, you can either select one and comment the other or comment both and write a new message.

After this, the third time you will taken to commit edit termnal for reword. Here you will be displayed a single commit only which you can edit.

**Gaurav Kushwaha** · 2025-01-09 12:12 UTC

Thank u once again. I finally understood the rebase practically.

**Gaurav Kushwaha** · 2025-01-13 00:40 UTC

What commit message should I use for resolving merge conflicts?

**Gaurav Kushwaha** · 2025-01-13 00:42 UTC

Or I should use rebase instead of pushing a new commit?

**Apoorva Pendse** · 2025-01-13 01:20 UTC

(replying to Gaurav Kushwaha)
> Or I should use rebase instead of pushing a new commit?

Yes.


## ✔ already a rebase-apply directory

*2024-01-26 to 2024-01-28 · 12 messages · [open in Zulip](https://chat.zulip.org/#narrow/channel/44-git-help/topic/.E2.9C.94.20already.20a.20rebase-apply.20directory/with/1726695)*

**Shashank Singh** · 2024-01-26 08:10 UTC

I stopped a branch rebase in the very middle and now I am unable to abort it. 
I want to squash my commits using interactive rebasing but the previous rebase can't be aborted. 
[Screenshot-2024-01-26-at-1.39.39PM.png](https://chat.zulip.org/user_uploads/2/c0/59WhFgUcsxCOyDzZIwI1D5hO/Screenshot-2024-01-26-at-1.39.39PM.png)
Can anyone help me with this?

**Notification Bot** · 2024-01-26 08:28 UTC

[A message](https://chat.zulip.org/#narrow/stream/44-git-help/topic/already.20a.20rebase-apply.20directory/near/1726695) was moved here from #**git help>how to git rebase so that...** by @Greg Price.

**Greg Price** · 2024-01-26 08:29 UTC

Is there any state you want to keep from the old rebase?

If not, that first error message has a suggestion for what to do.

**Shashank Singh** · 2024-01-26 10:15 UTC

(replying to Greg Price)
> Is there any state you want to keep from the old rebase? If not, that first error message has a suggestion for what to do.

No , I don't.
I'm just unsure whether I should use ```rm -fr ".git/rebase-apply"``` because the ```git rebase --abort``` always worked fine.

**Shashank Singh** · 2024-01-26 10:23 UTC

Thanks Greg , I just forcefully aborted the rebase using ```git rebase --quit```.

**Greg Price** · 2024-01-26 20:22 UTC

Cool, glad you got things working.

**Greg Price** · 2024-01-26 20:24 UTC

Rereading what `git rebase --abort` printed in your original output, it looks like it may be that the `git rebase --abort` actually already successfully ended the rebase.

The only thing it prints is labeled "warning", not "error". And it's saying that it doesn't find the file that would tell it which branch to reset you to.

**Greg Price** · 2024-01-26 20:25 UTC

The only(*) difference between `--abort` and `--quit`, according to the documentation, is that `--abort` resets you to your original branch:

```
       --abort
           Abort the rebase operation and reset HEAD to the
           original branch. If <branch> was provided when the
           rebase operation was started, then HEAD will be reset
           to <branch>. Otherwise HEAD will be reset to where it
           was when the rebase operation was started.

       --quit
           Abort the rebase operation but HEAD is not reset back
           to the original branch. The index and working tree are
           also left unchanged as a result. If a temporary stash
           entry was created using --autostash, it will be saved
           to the stash list.
```
(that's from `git help rebase`; some formatting lost)

**Greg Price** · 2024-01-26 20:26 UTC

(*) there's one other difference which applies only if you've used the unusual option `--autostash`

**Greg Price** · 2024-01-26 20:27 UTC

So in other words the output you got from `--abort` suggests that it already did exactly the same job as `--quit` would do.

**Shashank Singh** · 2024-01-27 05:45 UTC

Ohh that's cool , didn't know rebase got so many secrets behind it.

**Notification Bot** · 2024-01-28 19:29 UTC

@Shashank Singh has marked this topic as resolved.


## #27841

*2024-01-28 to 2024-01-28 · 2 messages · [open in Zulip](https://chat.zulip.org/#narrow/channel/44-git-help/topic/.2327841/with/1727582)*

**Nimish Medatwal** · 2024-01-28 15:59 UTC

I've rebased and resolved conflicts in #27841 but zulipbot hasn't removed the `has conflict` tag, can someone please remove it manually.

**Tim Abbott** · 2024-01-28 23:49 UTC

Fixed.


## modified message without modifying the files

*2024-02-03 to 2024-02-05 · 11 messages · [open in Zulip](https://chat.zulip.org/#narrow/channel/44-git-help/topic/modified.20message.20without.20modifying.20the.20files/with/1731337)*

**Pratik Goud** · 2024-02-03 10:13 UTC

[image.png](https://chat.zulip.org/user_uploads/2/bf/gEztQauePf2VaXBG4RZRQiSf/image.png)

Hi @Alya Abbott 
I haven't modified any of the files but still the output of command "git status" shows as modified.
How should I tackle this?
I have freshly created a new dev env.

**Pratik Goud** · 2024-02-03 10:18 UTC

[image.png](https://chat.zulip.org/user_uploads/2/e4/91zVVS1OjsbJ-TW2qZ1rzJZn/image.png)

This is the output of "git diff" command.

**Arjun C 🪲** · 2024-02-03 17:52 UTC

(replying to Pratik Goud)
> [image.png](https://chat.zulip.org/user_uploads/2/e4/91zVVS1OjsbJ-TW2qZ1rzJZn/image.png) This is the output of "git diff" command.
Looks like the change is in the number of lines or context and not the content of the file. Maybe some white space changes
try this command to  ignore whitespace changes
```
git diff -w
```

**Pratik Goud** · 2024-02-04 03:51 UTC

Thanks @Arjun C 🪲 for checking.
"git diff -w" is still giving me the same output.
`-../CODE_OF_CONDUCT.md`: This line shows the content that was present in the old version of the file and has been removed. The `-` sign indicates the removal.

**Arjun C 🪲** · 2024-02-04 05:00 UTC

strange, how do other files get affected while creating an env. Did you find any fix?

**Pratik Goud** · 2024-02-04 06:51 UTC

No.I didn't find any fix

**Pratik Goud** · 2024-02-04 06:52 UTC

All this files are symlinks.

**Greg Price** · 2024-02-05 21:13 UTC

@Pratik Goud Please see our community norms:
https://zulip.com/development-community/#getting-help
In particular use a code block rather than a screenshot, and there's generally no need to @-mention core contributors.

**Greg Price** · 2024-02-05 21:15 UTC

From that `git diff` output, it looks like what's happened is that a number of symlinks were modified so that they point to an empty path.

You should be able to undo the changes, and get back to the version that's in the Git repo, with `git reset --hard`.

**Greg Price** · 2024-02-05 21:16 UTC

That leaves the question of how the change happened, and how to prevent it.

What OS are you using?

**Greg Price** · 2024-02-05 21:16 UTC

And does it happen again after you use `git reset --hard` to reset things?


## applying migrations

*2024-02-03 to 2024-02-05 · 4 messages · [open in Zulip](https://chat.zulip.org/#narrow/channel/44-git-help/topic/applying.20migrations/with/1731447)*

**Shashank Singh** · 2024-02-03 20:16 UTC

I did some changes in the models and views of my issue branch and applied migrations. But i got some errors so I reverted those changes. 
But now when I run the environment , I still get the same error.
Even if I change the branch , the problem remains.

Does doing ```git restore``` not completely restores previous changes?
If that is so how can I completely revert back to normal case ?
Also does applying migrations in one branch effect the database for different branches as well?

**Prakhar Pratyush** · 2024-02-05 09:49 UTC

> Does doing `git restore` not completely restores previous changes?

It discards changes made in files.

**Prakhar Pratyush** · 2024-02-05 09:49 UTC

> If that is so how can I completely revert back to normal case ?

I prefer: `/tools/rebuild-dev-database`

We can also use [reversing migration](https://docs.djangoproject.com/en/3.2/topics/migrations/#reversing-migrations). This is important:
"A migration is irreversible if it contains any irreversible operations. Attempting to reverse such migrations will raise `IrreversibleError`:"

**Prakhar Pratyush** · 2024-02-05 09:50 UTC

> Also does applying migrations in one branch effect the database for different branches as well?

Yes


## make remote repository same as original repository

*2024-02-11 to 2024-03-07 · 20 messages · [open in Zulip](https://chat.zulip.org/#narrow/channel/44-git-help/topic/make.20remote.20repository.20same.20as.20original.20repository/with/1735564)*

**Ankit Suryawanshi** · 2024-02-11 14:53 UTC

Some files in my repository is showing modified. But I don't want to make any changes and make my remote repository exactly similar to zulip's original repository. How can I do? can anyone please help

**Varun** · 2024-02-11 18:11 UTC

You can stash your changes using `git stash` .This will stash your local uncommited changes which you can re-apply later using `git stash pop`(which I am guessing you don't want). Then `git fetch upstream` and `git rebase upstream/main`  to  rebase your **local** repo branch against zulip's `main`.
Finally `git push origin main` to make your remote branch up-to-date with `zulip/main`. This is what works for me.

**Ankit Suryawanshi** · 2024-02-12 09:12 UTC

I followed your steps @Varun Singh(LaPulgaaa) . But even now some files have M written adjacent to them. Why?
[image.png](https://chat.zulip.org/user_uploads/2/d8/qZpJ-akXm-DTCLtBdzOD8B7j/image.png)

**Prakhar Pratyush** · 2024-02-12 10:35 UTC

* Step 1: `git restore .`
* Step 2: See [Keep your fork up to date](https://zulip.readthedocs.io/en/latest/git/using.html#keep-your-fork-up-to-date)

**Ankit Suryawanshi** · 2024-02-13 08:43 UTC

still there are these files showing
[image.png](https://chat.zulip.org/user_uploads/2/66/OU1tcepMFDKDSN1Snxoh2Jvq/image.png)
Even after discarding them, they are reappearing again and again 
and backend test is also failing
[image.png](https://chat.zulip.org/user_uploads/2/ac/5bWEGZebBa3mjIwVhptNsl09/image.png)

**Varun** · 2024-02-13 12:55 UTC

Are you in the project's(zulip) `root` directory while writting those commands.
 I'd use `git reset --hard` to undo all the changes. It will discard all changes and take your branch to the last commit . But I think advice of someone more seasoned with git would be better than mine.

**Greg Price** · 2024-02-13 17:41 UTC

Along the lines of what @Varun Singh(LaPulgaaa) said, it's helpful to show the commands you're running and the output they produce. You can do that with a Zulip code block, rather than a screenshot, to make it easier to read.

**Greg Price** · 2024-02-13 17:42 UTC

If unwanted changes are appearing after you use `git reset --hard` or `git restore .` or `git stash` to clear them away, then you'll want to identify what's causing them so you can get it to stop.

**Greg Price** · 2024-02-13 17:43 UTC

Two questions to answer that would help with that are:
* When does it seem to happen? What are you doing immediately before the changes appear?
* What do the changes look like? For this, `git diff` is a good tool.

**Ankit Suryawanshi** · 2024-02-14 03:08 UTC

I am not doing anything and they are reappearing without doing anything.

Can I remove my forked repository and fork it again?

I think that would be better because I tried all these commands. 

Even after running upstream and merging backend tests are failing continuously.

Should I fork it again?

**Greg Price** · 2024-02-14 04:37 UTC

If you're seeing unwanted changes in your local working tree, then it's unlikely that that has anything to do with your forked repository on GitHub.

If you look at what the changes are, that will help make it possible to identify what might be causing them.

**Ankit Suryawanshi** · 2024-02-14 06:27 UTC

[image.png](https://chat.zulip.org/user_uploads/2/ab/VmFYdQ6T8xbMQIiGVEAgXLcF/image.png)
[image.png](https://chat.zulip.org/user_uploads/2/a0/7uyC96DP2xDYkU5jTisEma2h/image.png)
[image.png](https://chat.zulip.org/user_uploads/2/8a/WGnAPoHAWIXROfv0AVWt7FSh/image.png)

**Ankit Suryawanshi** · 2024-02-14 13:14 UTC

any response @Greg Price @Varun Singh(LaPulgaaa)

**Greg Price** · 2024-02-14 19:34 UTC

Please do read our community guidelines. In addition to this point I mentioned above:

(replying to Greg Price)
> You can do that with a Zulip code block, rather than a screenshot, to make it easier to read.

there's an important point there about @-mentions.

**Greg Price** · 2024-02-14 19:35 UTC

The `git status` output in your second screenshot is telling you there are untracked extra files in your working tree, but no modifications to any existing files.

If you don't want those files, you can delete them. A Git command for that would be `git clean -id`, but you can also just delete them in whatever way you like for deleting files.

**Ankit Suryawanshi** · 2024-02-15 03:08 UTC

I have deleted that file but still the issue continues

**Greg Price** · 2024-02-15 04:17 UTC

OK.

If you'd like help with figuring out the issue you're seeing, a key ingredient in making it possible for people to help will be to give more details:

(replying to Greg Price)
> Along the lines of what @Varun Singh(LaPulgaaa) said, it's helpful to show the commands you're running and the output they produce.

In particular it's not clear what you mean when you say "the issue continues" — are you seeing unexpected changed files? (If so, what do `git status` and `git diff` say?) Or do you no longer have any unexpected changes or extra files, but tests are failing? (If so, what command are you running and what does it output?)

**Ankit Suryawanshi** · 2024-02-15 05:11 UTC

issue means when i am running git status it is showing nothing to commit morking tree clean but on vs code 'M' is written adjacent to some files.

And on running ./tools/backend-test, sometimes it is giving 1 error or 2 errors.

**rinwa** · 2024-03-07 03:23 UTC

@Ankit Suryawanshi Hi first the approach to this kind of issue is to first sit back clear your head and look at the state of vscode, figure out what you want as an outcome then we can figure out what can get you to your desired outcome.

**rinwa** · 2024-03-07 03:25 UTC

Some of your explanations are somewhat hard to understand. I can't figure out how to help or what to help with.


## ✔ authenticity can't be established when push

*2024-03-01 to 2024-03-01 · 10 messages · [open in Zulip](https://chat.zulip.org/#narrow/channel/44-git-help/topic/.E2.9C.94.20authenticity.20can.27t.20be.20established.20when.20push/with/1749073)*

**Bedo Khaled** · 2024-03-01 01:37 UTC

When i try to push my local commits to **Origin** (my fork of Zulip) I get the following **prompt** which is new to me, I don't know what does it mean or is it safe to continue or not.
```
The authenticity of host 'github.com (140.82.121.4)' can't be established.
ECDSA key fingerprint is **********************.
Are you sure you want to continue connecting (yes/no/[fingerprint])? no

```

when i try the following command "git remote show origin" it gives me the same prompt above

**Greg Price** · 2024-03-01 01:47 UTC

What have you tried so far for searching for information about that message?

**Bedo Khaled** · 2024-03-01 02:03 UTC

turns out that Google gemini is not so bad :laughing:  here its response :
```
The message you're encountering is related to Git's security measures when connecting to a remote repository, typically hosted on platforms like GitHub. Here's a breakdown of the message and what you should do:

Breakdown:

"The authenticity of host 'github.com (140.82.121.3)' can't be established.": This warning signifies that Git cannot verify the identity of the server you're trying to connect to (github.com).
"ECDSA key fingerprint is SHA256:*************": This line displays the fingerprint of the public key used by the server for its identification. Each server has a unique fingerprint, similar to a digital signature.
"Are you sure you want to continue connecting (yes/no/[fingerprint])?": This prompt asks for your confirmation before proceeding.
What to do:

Verify the fingerprint: You can compare the displayed fingerprint with the official fingerprint of the remote repository you're trying to connect to. For GitHub, the official fingerprint can be found on their https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/githubs-ssh-key-fingerprints page.

Make an informed decision:

If the fingerprints match:
Type yes to proceed with the connection. This confirms that you trust the server and are willing to connect despite the lack of automatic verification.
If the fingerprints don't match:
Do not proceed! This inconsistency indicates a potential security risk. Investigate further and troubleshoot the issue before attempting to connect.
Additional considerations:

This prompt might appear for the first time you connect to a specific remote repository. Once you confirm the fingerprint and connect successfully, Git will usually remember it for future connections, avoiding the prompt unless the fingerprint changes on the server side.
If you encounter this message frequently, consider setting up SSH keys for authentication, which can provide a more secure and convenient way to connect to remote repositories without relying on manual confirmation prompts.

```

**Bedo Khaled** · 2024-03-01 02:11 UTC

I just had to compare the **ECDSA key fingerprint** in the prompt (which is not a secret as i thought) with
 Github public key fingerprint for **ECDSA**

**Greg Price** · 2024-03-01 02:12 UTC

Indeed. And that link https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/githubs-ssh-key-fingerprints is helpful.

There's actually a better option than comparing the fingerprints yourself. The prompt says "(yes/no/[fingerprint])". What that's hinting is that instead of saying "yes" or "no", you can paste in the fingerprint you're expecting. Then that makes it the computer's job to compare it to the actual fingerprint.

**Bedo Khaled** · 2024-03-01 02:14 UTC

ok, now everything is clear the issue was that i was trying to push from the linux container (Vagrant Setup) which is isolated from the rest of my system where i keep my SSH keys, just had to push from another terminal which doesn't have **(zulip-py3-venv)**

**Bedo Khaled** · 2024-03-01 02:15 UTC

> There's actually a better option than comparing the fingerprints yourself. The prompt says "(yes/no/[fingerprint])". What that's hinting is that instead of saying "yes" or "no", you can paste in the fingerprint you're expecting. Then that makes it the computer's job to compare it to the actual finge …
Correct !

**Greg Price** · 2024-03-01 02:17 UTC

One inaccuracy in that response is that it isn't really a security measure taken by Git, but rather by SSH.

SSH is the transport protocol that Git is using in this case to talk to GitHub. It's also used more generally, unrelated to Git, for logging into remote servers.

**Bedo Khaled** · 2024-03-01 02:21 UTC

Yes, I never take AI reponses for granted, but they are still helpful like in this situation

**Notification Bot** · 2024-03-01 03:46 UTC

@Bedo Khaled has marked this topic as resolved.


## many commits in my PR

*2024-03-05 to 2024-03-06 · 59 messages · [open in Zulip](https://chat.zulip.org/#narrow/channel/44-git-help/topic/many.20commits.20in.20my.20PR/with/1752561)*

**Bedo Khaled** · 2024-03-05 23:34 UTC

**Urgent !**
i have pushed the last commit i made localy to Origin (my zulip fork) and this happened in my [pr](https://github.com/zulip/zulip/pull/29144)

**Bedo Khaled** · 2024-03-05 23:34 UTC

Many commits are added from other contributors !

**Bedo Khaled** · 2024-03-05 23:43 UTC

**Here are the exact commands i ran  in order**  :

1. `git fetch upstream`
2. commit my staged changes.
3.  `git rebase upstream/main` with the following msg :
> First, rewinding head to replay your work on top of it... Applying: portico: Add keyboard accessibility for show/hide password icon. Applying: portico: Remove preventDefault() from keyup listener. Applying: portico: Add test for keyup event. Applying: portico: Change keyup event to keydown.
4. `git status` with the following **important** msg :
> On branch main Your branch and 'origin/main' have diverged, and have 94 and 3 different commits each, respectively. (use "git pull" to merge the remote branch into yours) nothing to commit, working tree clean
5. tried to push, but it failed with the following : 
> error: failed to push some refs to 'git@github.com:abdelrahman725/zulip.git' hint: Updates were rejected because the tip of your current branch is behind hint: its remote counterpart. Integrate the remote changes (e.g. hint: 'git pull ...') before pushing again.
6. `git pull`with the following : 
> First, rewinding head to replay your work on top of it... Applying: Revert "copy_and_paste: Fix formatting of code pasted from VS Code." Applying: docs: Fix broken Markdown links from recent reorganization. **Applying other commits.....**
 7. `git status` : 
> On branch main Your branch is ahead of 'origin/main' by 91 commits.
8. finally did a `git push`

**Bedo Khaled** · 2024-03-05 23:45 UTC

now the PR is totally messed up, i don't know what happened !

**Bedo Khaled** · 2024-03-05 23:45 UTC

**I'm really sorry for that hussle**

**Bedo Khaled** · 2024-03-05 23:50 UTC

Current state of my fork :
[Screenshot-from-2024-03-06-01-49-34.png](https://chat.zulip.org/user_uploads/2/a0/VInOzru4QTENiE-_TRoxxawg/Screenshot-from-2024-03-06-01-49-34.png)

**Greg Price** · 2024-03-06 01:43 UTC

It looks like your branch has
* some commits of yours
* then a bunch of recent commits from upstream, but rebased onto those first commits of yours
* then another commit of yours.

**Greg Price** · 2024-03-06 01:43 UTC

This is a good time to try out `gitk` or another graphical Git viewer:
https://zulip.readthedocs.io/en/latest/git/setup.html#get-a-graphical-client

That will help a lot in giving you a picture of what's going on in your repository.

**Greg Price** · 2024-03-06 01:44 UTC

(In particular try `gitk --all HEAD`, to see everything.)

**Greg Price** · 2024-03-06 01:45 UTC

The good news is that this will be pretty easy to clean up by rebasing your branch onto upstream. Seeing a picture with a graphical viewer will help you see what the right commands to try for that are — what you want to rebase on top of what.

**Bedo Khaled** · 2024-03-06 01:46 UTC

and can my PR be fixed ? that's to get rid of all those commit ?

**Greg Price** · 2024-03-06 01:46 UTC

Yeah, like I said — by rebasing onto upstream

**Greg Price** · 2024-03-06 01:46 UTC

No, it's never necessary to close the existing PR and open a new one for something like this

**Greg Price** · 2024-03-06 01:47 UTC

(that is, for any kind of fixing up of the Git state)

**Greg Price** · 2024-03-06 01:47 UTC

Just get the Git branch into the desired state — which you'd have to do anyway for a new PR — and then push that to the PR branch

**Greg Price** · 2024-03-06 01:48 UTC

One key fact in how rebasing will clean this up is that when you rebase a branch on top of a branch that already has equivalents to some of the same commits — for example, when you rebase your current branch atop upstream, which already has many of those changes — the redundant commits will just get dropped. Which is exactly what you want here.

**Bedo Khaled** · 2024-03-06 01:50 UTC

> when you rebase your current branch atop upstream
and that's what i should do right ?

**Greg Price** · 2024-03-06 01:50 UTC

Right

**Greg Price** · 2024-03-06 01:52 UTC

So a graphical Git viewer like `gitk` should be helpful for seeing what's happening, and then rebasing onto upstream should clean this branch up.

Then going into the root causes a bit:

From the `git status` output you helpfully included above, it sounds like you have a branch with its upstream (the branch `git status` reports those "ahead"/"diverged"/etc. commit counts relative to) set to `origin/main`. Which it sounds like is your own fork, rather than to `upstream/main`, meaning the main Zulip repository.

I think that was a key step in how your branch got into this state. You rarely want to be rebasing changes from elsewhere onto your own branches — instead you want to be rebasing your branch onto `upstream/main`. And the "upstream" used by `git status` is the same one that some commands like `git pull` will use for rebasing your changes onto.

**Greg Price** · 2024-03-06 01:53 UTC

So when `git status` is telling you about where you are relative to `origin/main`, that's something you should fix. (Given that you're using `origin` to mean your own fork and not the main upstream Zulip repo.) It should be `upstream/main` instead.

**Greg Price** · 2024-03-06 01:53 UTC

You can fix that with `git branch -u` — see `git help branch` for docs.

**Bedo Khaled** · 2024-03-06 01:53 UTC

so what was wrong with step 3 i made above ? which was rebasing

**Greg Price** · 2024-03-06 01:54 UTC

I think probably step 3 was fine, and it was step 6 that made the branch look like this.

That's because step 3 was explicitly pointing at `upstream/main` as the place to rebase onto, but step 6 was implicitly using the branch's "upstream" — and as discussed above, that was `origin/main` which isn't what you want.

**Greg Price** · 2024-03-06 01:56 UTC

The next time you do a similar rebase, I highly recommend having `gitk --all HEAD`, or a similar graphical Git viewer, open while you do it. (And hit refresh in that viewer after each step.)

That will help a lot in giving you a picture of what the commands are doing, and building your mental model of what they all do.

**Bedo Khaled** · 2024-03-06 01:56 UTC

> but step 6 was implicitly using the branch's "upstream"
Yes i should have pulled from Origin (my fork) and not upstream which is the original zulip repo, is that right ?

**Greg Price** · 2024-03-06 01:58 UTC

Other way around, if I'm understanding you right:
* You always want to rebase atop `upstream/main`, not `origin/main`.
* The `git pull` command, with no further arguments, rebases onto the branch's own configured "upstream". For your branch, that's currently `origin/main`, so the wrong thing happened.

**Greg Price** · 2024-03-06 01:58 UTC

(this is a bit confusing to describe because your branch has "an upstream" that's part of the branch's own config, but `upstream` is also the name of one of your remotes)

**Bedo Khaled** · 2024-03-06 02:04 UTC

this is the output of `git remote -v` : 
> origin git@github.com:abdelrahman725/zulip.git (fetch) origin git@github.com:abdelrahman725/zulip.git (push) upstream https://github.com/zulip/zulip.git (fetch) upstream https://github.com/zulip/zulip.git (push)

**Bedo Khaled** · 2024-03-06 02:04 UTC

origin is my fork, and upstream is the original repo for Zulip

**Bedo Khaled** · 2024-03-06 02:04 UTC

i shoud have pulled from origin instead right ?

**Bedo Khaled** · 2024-03-06 02:07 UTC

I'm will install now `gitk` should i install it in the **Vagrant container** (zulip dev env) or my machine ?

**Greg Price** · 2024-03-06 02:07 UTC

On your machine is probably more convenient

**Greg Price** · 2024-03-06 02:08 UTC

It's a graphical application, which may be annoying to get working from inside Vagrant

**Bedo Khaled** · 2024-03-06 02:29 UTC

> i shoud have pulled from origin instead right ?
Sorry This wrong, this what actuallly caused the problem.

**Bedo Khaled** · 2024-03-06 02:39 UTC

ok now i have rebased on upstream `git rebase upstream/main`
when i do `git status` now :
> Your branch and 'origin/main' have diverged, and have 94 and 94 different commits each, respectively. (use "git pull" to merge the remote branch into yours)

**Bedo Khaled** · 2024-03-06 02:39 UTC

since my local brach is in the correct state, my `Origin` is the one that should be the same as my local branch right ? should i force push to Origin ?

**Bedo Khaled** · 2024-03-06 03:01 UTC

> So when `git status` is telling you about where you are relative to `origin/main`, that's something you should fix. (Given that you're using `origin` to mean your own fork and not the main upstream Zulip repo.) It should be `upstream/main` instead.
You mean git status should give me info about `upstream` instead of `Origin` ?

**Greg Price** · 2024-03-06 03:05 UTC

(replying to Bedo Khaled)
> You mean git status should give me info about `upstream` instead of `Origin` ?

Right, exactly.

**Greg Price** · 2024-03-06 03:07 UTC

(replying to Bedo Khaled)
> ok now i have rebased on upstream `git rebase upstream/main`

Perfect.

> when i do `git status` now : ```quote Your branch and 'origin/main' have diverged, and have 94 and 94 different commits each, respectively. (use "git pull" to merge the remote branch into yours) ```

Yeah, that's what it will look like after you have the branch all fixed.

It's not as informative as it could be, because ideally it would be telling you about the status relative to `upstream/main` instead. You can fix that with `git branch -u` as mentioned above.

**Greg Price** · 2024-03-06 03:08 UTC

(Doing that would both make `git status` more helpful, and also make `git pull` and `git rebase` do the right thing by default.)

**Bedo Khaled** · 2024-03-06 03:08 UTC

ok now how to actually fix the PR, should i force the local changes to be pushed to Origin?

**Greg Price** · 2024-03-06 03:09 UTC

(replying to Bedo Khaled)
> should i force push to Origin ?

You should force-push to your PR branch.

Looking at #29144, it looks like that's `main` in your GitHub fork: 
[image.png](https://chat.zulip.org/user_uploads/2/6/IuLjbMYEYcdJSs51uMhMFr4a/image.png)

**Greg Price** · 2024-03-06 03:09 UTC

i.e. `origin/main` in terms of your local repository.

**Bedo Khaled** · 2024-03-06 03:10 UTC

yes

**Greg Price** · 2024-03-06 03:10 UTC

For your next PR, it'll be better to use a branch other than `main`. See advice here:
https://zulip.readthedocs.io/en/latest/git/pull-requests.html

**Greg Price** · 2024-03-06 03:10 UTC

(No need to try to change that for this PR, though)

**Bedo Khaled** · 2024-03-06 03:10 UTC

Ok

**Greg Price** · 2024-03-06 03:11 UTC

One reason that's a good idea is that it'll help make the kind of confusion that happened here less likely :smile:

**Bedo Khaled** · 2024-03-06 03:11 UTC

`git push --force` will do right

**Greg Price** · 2024-03-06 03:12 UTC

Yeah, `--force` will make it a force-push.

Personally I always add an argument after `git push` to say explicitly what I want to push and where.

**Bedo Khaled** · 2024-03-06 03:12 UTC

push by default pushes to `origin`, since i can not push directoy to `upstream`

**Greg Price** · 2024-03-06 03:12 UTC

You can also add `-n` to any `git push` command, and it'll print out what it would do instead of actually doing it

**Greg Price** · 2024-03-06 03:12 UTC

Right, you'll always be pushing to some branch on `origin`, i.e. in your own GitHub fork.

**Bedo Khaled** · 2024-03-06 03:13 UTC

My PR is now fixed and cleared from all those previous commits !!! :tada:

**Bedo Khaled** · 2024-03-06 03:13 UTC

Thank you so much Greg !!

**Greg Price** · 2024-03-06 03:13 UTC

You're welcome!

**Bedo Khaled** · 2024-03-06 03:14 UTC

You were very helpful and kind answering with detailed explanation

**Greg Price** · 2024-03-06 03:14 UTC

Great, glad it was helpful

**Greg Price** · 2024-03-06 03:14 UTC

Hopefully `gitk` will keep helping you in the future, too.


## ✔ force push vs new commit

*2024-03-21 to 2024-07-09 · 10 messages · [open in Zulip](https://chat.zulip.org/#narrow/channel/44-git-help/topic/.E2.9C.94.20force.20push.20vs.20new.20commit/with/1762865)*

**Aditya Bajaj** · 2024-03-21 04:00 UTC

Hello! What is the convention on amending and force pushing to a branch in your fork (safe to force push over any changes you added yourself) vs adding a new commit to fix something like running the linter that you missed out on doing before committing previous changes.

I see a lot of other PRs in the repo with force pushes/amends: I understand that this is safe and keeps history clean but I just wanted to double check since I think amends and force pushing makes a PR harder to review and navigate. Any insight would be appreciated, Thanks!

**Greg Price** · 2024-03-21 04:15 UTC

Amending existing commits, and other forms of force-pushing, does unfortunately make GitHub's web UI less helpful for reviewing revisions to a PR. In the Zulip project we do that anyway, because it's part of how we get a nice readable Git history in the end.

**Greg Price** · 2024-03-21 04:16 UTC

The main thing we do to mitigate that when reviewing is we fetch the PR branch, and use Git locally to see the changes. We have a couple of scripts in `tools/` that help for fetching it, in particular `tools/reset-to-pull-request`. Here's some discussion of how you can use the results of that:
https://chat.zulip.org/#narrow/stream/121-GSoC-Mentors/topic/review.20tips/near/899664

**Aditya Bajaj** · 2024-03-21 04:28 UTC

Thanks for the quick help @Greg Price :)

**Tanmay Kumar (tnmkr)** · 2024-03-21 04:36 UTC

(replying to Greg Price)
> https://chat.zulip.org/#narrow/stream/121-GSoC-Mentors/topic/review.20tips/near/899664

I think this is a private stream. Can't access it.

**Notification Bot** · 2024-03-21 09:52 UTC

@Aditya Bajaj has marked this topic as resolved.

**Greg Price** · 2024-03-22 01:36 UTC

(replying to Tanmay Kumar (tnmkr))
> I think this is a private stream. Can't access it.

Ooh sorry, thanks. I guess now that I reread the stream's name, that's unsurprising.

**Greg Price** · 2024-03-22 01:38 UTC

Here's a series of messages I sent there myself (back in 2020-06), which are what I most wanted to point to:

> The thing I do all the time to make use of the reflog is a command like: ``` $ git range-diff @{u}..pr/4133@{{1,0}} ``` just changing the PR number. There's two different things that braces `{}` are doing there -- the ones with a comma between are shell notation, so the shell expands that to: ``` $ …

> So all told that works out to mean "take the previous version (that I fetched locally) of this branch, and the current version, and compare the branches." Sometimes I'll change it to `…@{{2,0}}` or `…@{{2,1}}` or something to compare previous versions; the most common case of that is if there was a …

> I'll also sometimes do a plain `git diff` between the ends of the (old and new) branches. That could be as simple as ``` $ git diff pr/12345@{{1,0}} ``` but that can be noisy if the branch was rebased. One way to filter that out that's usually pretty effective is to limit to the files that were chan …

[…]

> This discussion is kind of making me think there should be a script that does the "fetch to `pr/12345`" part without the reset part. The reset part isn't a great fit for everyone's workflows -- and I'm not sure everyone necessarily should be using the workflow it works great for, even though it's a …

**Greg Price** · 2024-03-22 01:43 UTC

One update, as I reread those: the command I now use all the time is a slight variation on the above, namely
```
$ git range-diff origin pr/4133@{{1,0}}
```

That involves the same two different things that braces `{}` are doing, one for the shell to interpret and one for Git. But
* `git range-diff` takes a convenient three-argument form; `git range-diff A B C` is equivalent (IIUC) to `git range-diff A..B A..C`.
* I've shifted to usually typing `origin` explicitly rather than `@{u}`.

  I think one reason I used to use `@{u}` was that I find the word "upstream" just a little slow to type, thanks to lots of consecutive letters on the same hand (in a QWERTY layout). Sometime since 2020 I switched back to using the name `origin` for the remote pointing at the upstream repository, rather than `upstream`, and `origin` I can type very quickly :smile:

**Greg Price** · 2024-07-09 18:44 UTC

For cross-reference, I just wrote a bit more about `git range-diff` here:
https://chat.zulip.org/#narrow/stream/243-mobile-team/topic/code.20reviews/near/1852971


## ✔ E: Package 'libmagic1' has no installation candidate

*2024-03-31 to 2024-03-31 · 1 messages · [open in Zulip](https://chat.zulip.org/#narrow/channel/44-git-help/topic/.E2.9C.94.20E.3A.20Package.20.27libmagic1.27.20has.20no.20installation.20candidate/with/1771050)*

**Notification Bot** · 2024-03-31 03:40 UTC

This topic was moved to #**development help>✔ E: Package 'libmagic1' has no installation candidate** by @Greg Price.


## cleaning PR commit history

*2024-04-04 to 2024-04-05 · 3 messages · [open in Zulip](https://chat.zulip.org/#narrow/channel/44-git-help/topic/cleaning.20PR.20commit.20history/with/1774835)*

**Kirsty Williams** · 2024-04-04 15:53 UTC

Hi there! I'm need help cleaning up my PR commit history: [](https://github.com/zulip/zulip/pull/29324)
 I read the documents provided by Zulip along with my own research, however, I'm worried about losing important data if I rebase, and all my commits are not shown when I'm attempting to 'squash' instead of deleting. What is the best way to resolve so that my commit can be properly prepped for merge?
P.S I'm using WSL2 on a Windows 11 Home device

**Karl Stolley** · 2024-04-05 13:50 UTC

If you’re worried about losing data, I suggest creating as many temporary branches as you like from your working branch, and giving yourself the opportunity to learn and make mistakes with rebasing.

**Kirsty Williams** · 2024-04-05 16:03 UTC

Okay, thank you :+1:


## Organizing  my commits for PR #598

*2024-04-05 to 2024-04-09 · 13 messages · [open in Zulip](https://chat.zulip.org/#narrow/channel/44-git-help/topic/Organizing.20.20my.20commits.20for.20PR.20.23598/with/1775525)*

**satyam pokharna** · 2024-04-05 02:28 UTC

Help needed 

what kind of git commands i can use to organize my commits ?

**Prakhar Pratyush** · 2024-04-05 03:23 UTC

You can spend some time reading https://zulip.readthedocs.io/en/latest/git/index.html

That'd be very helpful.

**satyam pokharna** · 2024-04-05 08:34 UTC

[image.png](https://chat.zulip.org/user_uploads/2/40/D5bmG6oySbvr8a-Alkx2st5K/image.png)
[image.png](https://chat.zulip.org/user_uploads/2/6a/KDwyr4CR50KMfAMtM9s4XH7V/image.png)
what should i do in this situation? should i rebase or drop my commits and then make a new one

**Greg Price** · 2024-04-05 16:23 UTC

From those screenshots it's not clear what problem you're trying to solve. "9 commits ahead of main" means there are 9 commits in your branch, which can be appropriate depending on the commits.

**Greg Price** · 2024-04-05 16:24 UTC

For what the sequence of commits should look like, see the Zulip Git style guide:
https://zulip.readthedocs.io/en/latest/contributing/commit-discipline.html

**satyam pokharna** · 2024-04-05 16:27 UTC

so after making new commits according to the guideline , should i keep the older ones as they are?

**satyam pokharna** · 2024-04-05 16:30 UTC

because some commits has the wrong logic which i have corrected and then again committed it according to the review

**satyam pokharna** · 2024-04-05 16:31 UTC

or should i make a new PR

**Greg Price** · 2024-04-05 16:33 UTC

There's never a need to close a PR and make a new one for a revision of the same changes — once you have the branch in the shape you want, you can always push the new revision to the existing PR

**Greg Price** · 2024-04-05 16:34 UTC

Getting the branch in the right shape will involve revising the existing commits. See the Git style guide linked above, and the discussion of `git rebase` there.

**Kirsty Williams** · 2024-04-09 15:53 UTC

Hey! I just fixed this myself. Checkout this [StackOverflow answer](https://stackoverflow.com/questions/33502205/how-to-delete-merge-commits)
Goodluck :+1:

**satyam pokharna** · 2024-04-09 16:07 UTC

Thanks @Kirsty Williams

**satyam pokharna** · 2024-04-09 16:07 UTC

Thanks @Kirsty Williams


## cleaning commits that reference an issue

*2024-04-22 to 2024-04-22 · 2 messages · [open in Zulip](https://chat.zulip.org/#narrow/channel/44-git-help/topic/cleaning.20commits.20that.20reference.20an.20issue/with/1785353)*

**Bedo Khaled** · 2024-04-22 13:23 UTC

in [Provide an internal function to deactivate multiple users more efficiently](https://github.com/zulip/zulip/issues/19490) you can see the following :
[Screenshot-from-2024-04-22-15-18-41.png](https://chat.zulip.org/user_uploads/2/a3/nP9ISFvui71zsOXHX-HQrX_P/Screenshot-from-2024-04-22-15-18-41.png)

That results from me amending the commit, that is force push to my origin and hence to the PR, the PR itself is clean with one commit that will be merged in the future.

But all these commits in the above image is really **ugly** and redundant since we should only care about the last one,
Is there away to clean all these commits and make them one, since i probably will keep amending the commit?

**Alex Vandiver** · 2024-04-22 15:02 UTC

No.  This is just GitHub's UI being noisy; there isn't anything to be done about it.  Keeping the overall commit history clean is much more important than keeping GH's PR or issue view clean.


## ✔ Remove other contributors commit from PR#619

*2024-04-22 to 2024-04-25 · 7 messages · [open in Zulip](https://chat.zulip.org/#narrow/channel/44-git-help/topic/.E2.9C.94.20Remove.20other.20contributors.20commit.20from.20PR.23619/with/1785381)*

**satyam pokharna** · 2024-04-22 14:38 UTC

[image.png](https://chat.zulip.org/user_uploads/2/2e/AHG4tJGxvFtjWVp1bcWN632k/image.png)
**After merging my feature branch with `main` and committing my changes, I  included commits from other contributors in pull request #619. How can I remove these unwanted commits from my PR?**

**Alex Vandiver** · 2024-04-22 15:03 UTC

That's because you merged `main` into your branch, rather than rebasing.  See https://zulip.readthedocs.io/en/stable/git/using.html#keep-your-fork-up-to-date

**satyam pokharna** · 2024-04-22 15:14 UTC

so what should I do next , should I drop the other commits ?

**Alex Vandiver** · 2024-04-22 15:22 UTC

You can follow those instructions.  Rebasing will drop the other commits automatically.

**satyam pokharna** · 2024-04-22 15:23 UTC

thanks for the help

**satyam pokharna** · 2024-04-22 18:50 UTC

after running  **git rebase upstream/main**  the project is getting updated to the very first commit of the flutter repo

**Notification Bot** · 2024-04-25 18:11 UTC

@satyam pokharna has marked this topic as resolved.


## Diverged local main

*2024-04-25 to 2024-04-25 · 22 messages · [open in Zulip](https://chat.zulip.org/#narrow/channel/44-git-help/topic/Diverged.20local.20main/with/1787785)*

**satyam pokharna** · 2024-04-25 18:31 UTC

[image.png](https://chat.zulip.org/user_uploads/2/5d/LnCF6JTY4v7hWk4P5A5_72fB/image.png)
[image.png](https://chat.zulip.org/user_uploads/2/89/CVmkOg8rbNll360cKDdeQddX/image.png)
My local main branch has got diverted from the origin main. How to set the head of local main to latest commit of flutter project

**Greg Price** · 2024-04-25 18:46 UTC

The first screenshot there appears to be for a zulip/zulip repository, while the second looks like zulip-flutter.

**Greg Price** · 2024-04-25 18:46 UTC

Are they from the same local repository of yours? What did you do to produce each of the two screenshots?

**satyam pokharna** · 2024-04-25 18:57 UTC

When I was trying to commit my work, it showed me a message saying, "Your HEAD is behind." That's why I used the command `git reset HEAD`. After running this command, my local Flutter files were changed to backend Python files.   

I then used Git in Android Studio to view the branch, and as a result, I received the image.

**Greg Price** · 2024-04-25 19:07 UTC

(replying to satyam pokharna)
> When I was trying to commit my work, it showed me a message saying, "Your HEAD is behind." That's why I used the command `git reset HEAD`.

Do you still have open the terminal where you got that message, and ran that command? Pasting that terminal history here, in a Zulip code block, would help a lot in being able to pin down just what happened.

**satyam pokharna** · 2024-04-25 19:09 UTC

I encountered the issue Two days ago, and since then, I've been trying various commands to fix it myself by referring to the documentation, but I haven't been able to resolve it.

**Greg Price** · 2024-04-25 19:44 UTC

OK. In general, if at a certain point your tree gets into a state that you don't understand, it's a good idea to go and try to preserve the details of exactly what just happened — the exact commands you ran, and their exact output, starting from just before things became surprising.

After all, by hypothesis, there's something you don't yet understand about what just happened. That means that any summary you have from memory is likely to be inaccurate. Having an exact written record helps a lot when going back and trying to work things out, e.g. after reading some more documentation.

**Greg Price** · 2024-04-25 19:46 UTC

In particular the key command probably wasn't quite `git reset HEAD`. That command won't change `main` (or any other branch) to any different commit from the one it's already at. It also won't change the files in your tree.

(Instead the only thing it changes is the "index", which is a Git concept that you see reflected in `git status` and affects the behavior of `git commit` among others.)

**Greg Price** · 2024-04-25 19:46 UTC

What does `git remote -v` say? It sounds like you may have a mix of some remotes pointing to versions of zulip/zulip and others pointing to versions of zulip-flutter.

**satyam pokharna** · 2024-04-25 19:48 UTC

[image.png](https://chat.zulip.org/user_uploads/2/63/7KII0linH45R1y1N0fwHElNr/image.png)

**Greg Price** · 2024-04-25 19:49 UTC

Please use a Zulip code block — that makes this sort of output more readable.

**satyam pokharna** · 2024-04-25 19:51 UTC

```
PS C:\Users\Satyam\Desktop\zulip_3\zulip-flutter> git remote -v
origin  https://github.com/satyam372/zulip-flutter.git (fetch)
origin  https://github.com/satyam372/zulip-flutter.git (push)
upstream        https://github.com/zulip/zulip.git (fetch)
upstream        https://github.com/zulip/zulip.git (push)

```

**Greg Price** · 2024-04-25 19:52 UTC

Yeah, so `origin` is your GitHub fork of zulip-flutter, but `upstream` is zulip/zulip

**satyam pokharna** · 2024-04-25 19:52 UTC

yes . is that the issue?

**satyam pokharna** · 2024-04-25 19:55 UTC

currently i have used   **git remote set-url origin https://github.com/satyam372/zulip-flutter.git** this command and I am trying to rebase and solve the merge conflict and it is geeting updates as i solve the conflict

**Greg Price** · 2024-04-25 20:01 UTC

Generally you don't ever want commits from two separate codebases in the same Git repo. (Git itself handles that without a hitch, but it's not a situation that's helpful for any normal development workflow.)

That also means you don't want remotes that are for separate codebases. Instead you want all your remotes in a given repo to be different versions of the same codebase. For fetching commits from different codebases, use `git clone` to make a separate local repository for each codebase.

**Greg Price** · 2024-04-25 20:02 UTC

I'm not sure what merge conflict you mean, or what you're rebasing. But if you're trying to rebase commits from zulip/zulip atop zulip-flutter, then that isn't likely to be productive.

**satyam pokharna** · 2024-04-25 20:04 UTC

I am trying to rebase my origin/main into my local main

**Anders Kaseorg** · 2024-04-25 20:08 UTC

You just set your `origin` to a fork of zulip-flutter.git (the new mobile client), and your local main is from zulip.git (the server). These two repositories have nothing in common. It does not make sense to rebase one onto the other.

**satyam pokharna** · 2024-04-25 20:11 UTC

what can I do to address this issue? should I use git clone and make a new copy of project.

**Anders Kaseorg** · 2024-04-25 20:20 UTC

You ran a bizarre `git remote set-url` command to mix incompatible repositories together and got bizarre results. To avoid issues that result from running bizarre commands, don’t run bizarre commands. I don’t know what else to tell you.

**satyam pokharna** · 2024-04-25 20:40 UTC

I apologize for any confusion or inconvenience caused by my mistake. Could you please provide guidance on how to address the current situation ?


## stacking PRs

*2024-06-26 to 2024-06-27 · 7 messages · [open in Zulip](https://chat.zulip.org/#narrow/channel/44-git-help/topic/stacking.20PRs/with/1838994)*

**Zixuan James Li** · 2024-06-26 17:20 UTC

What's your general workflow when stacking PR on top of another?
Let's say C relies on B and B relies A, what I currently do is just:
- Update the branch, let's say A, with `git commit --fixup`
- Rebase B onto A with `git rebase --onto`, resolve conflicts
- Rebase C onto B with `git rebase --onto`, resolve conflicts

I guess there are many ways to do it, and I would love to know other people's workflow.

**Tim Abbott** · 2024-06-26 21:42 UTC

That's roughly what I do. 

That said, generally we aim to avoid ending up in a state where one needs to stack PRs, though; either not starting work on B/C until A is merged, or having a single PR with all the commits for A/B/C and instead just extracting prefixes when they are ready to merge, like in #30584.

**Tim Abbott** · 2024-06-26 21:43 UTC

With a lot of the effort towards avoiding it being to try to prioritize for reviews/merging work that will need other things stacked on it in the near future.

**Greg Price** · 2024-06-26 23:54 UTC

(replying to Tim Abbott)
> or having a single PR with all the commits for A/B/C and instead just extracting prefixes when they are ready to merge, like in #30584

Yeah, I think my own preference as a reviewer is different — because GitHub's UX degrades rapidly as a thread gets longer (and things start disappearing behind "hidden" links), I prefer to have a separate PR thread for each phase.

**Greg Price** · 2024-06-27 00:01 UTC

As an author, my workflow is basically the same one described above.

One helpful shell feature I use to make those `git rebase --onto` commands a bit more convenient to type is [brace expansion](https://www.gnu.org/software/bash/manual/bash.html#Brace-Expansion):
```
$ echo foo{bar,baz}
foobar foobaz
```

So e.g. if I'm doing the steps
* Revise branch A, whose name let's say is `pr-amazing-albatross`
* Push the new A: `git push me +@:pr-amazing-albatross`
* Rebase B onto the new A with `git rebase --onto`

then the way I'll spell that latter command is
```
$ git rebase --onto me/pr-amazing-albatross@{{0,1}} me/pr-bodacious-barracuda
```

which saves having to type out the name `me/pr-amazing-albatross` twice.

**Greg Price** · 2024-06-27 00:03 UTC

(There are two different syntaxes that braces `{}` are being used for in that command — one is the shell feature of brace expansion, expanding `{0,1}` to `0` and `1`, and the other layer is Git interpreting `@{0}` and `@{1}` to get commits from the reflog. See [previous discussion here](https://chat.zulip.org/#narrow/stream/44-git-help/topic/.E2.9C.94.20force.20push.20vs.20new.20commit/near/1763867) in a slightly different context.)

**Greg Price** · 2024-06-27 00:09 UTC

(replying to Tim Abbott)
> That said, generally we aim to avoid ending up in a state where one needs to stack PRs, though; either not starting work on B/C until A is merged

I definitely agree this is a useful tactic, though.

Also a variation on it: leave B/C as just a single branch on top of A, not yet split up into the PRs they'll become, until A is merged. (Could still post it as a draft PR for feedback, which could turn into the PR for B later.) That way there's only one layer of `git rebase --onto` to do.

(Often the later work does inform the earlier work, which is why just not starting on B/C often isn't a helpful option.)

I usually apply that latter tactic, so that there's at most one layer of `git rebase --onto` to be done after updating a PR.


## ✔ git rebase issue

*2024-08-09 to 2024-08-09 · 9 messages · [open in Zulip](https://chat.zulip.org/#narrow/channel/44-git-help/topic/.E2.9C.94.20git.20rebase.20issue/with/1915321)*

**Aditya Chaudhary** · 2024-08-09 19:55 UTC

While using git rebase -i HEAD~4. 
I expect the latest 4 commit to come but the whole commit list is coming. Is there any mistake im doing here ? 

```
git log --oneline
527542728e (HEAD -> branch-msg-notification, origin/branch-msg-notification) linter: Fix the issue for linter in unread.ts
b6db55ee13 linter: Fix the linter issue for the unread.ts
206ef6ef37 Merge branch 'main' of https://github.com/userAdityaa/zulip into branch-msg-notification
10787dd235 linter: Fix the linter issue for the code
cef6b632f1 notification_settings: Fix the closing of notification after mark as read
de35f44624 (origin/main, origin/HEAD, main) zulip_updates: Mention default for send navigation.
4351cc5914 thumbnail: Move get_image_thumbnail_path and split_thumbnail_path.
d474600056 tests: Remove a nonsensical no-op vimeo test.
424f3dd503 tests: Break up and reorganize test_markdown.py.
```

**Notification Bot** · 2024-08-09 20:04 UTC

This topic was moved here from #**issues>git rebase issue** by @Greg Price.

**Greg Price** · 2024-08-09 20:06 UTC

The key thing you can do to handle this and prevent it is to use `gitk` or another graphical Git viewer to see what's going on in your repository:
https://github.com/zulip/zulip-mobile/blob/main/docs/howto/git.md#graphical-client

**Greg Price** · 2024-08-09 20:08 UTC

One thing I notice in your output above is that there's a merge commit. That can mean the commits that are in HEAD but not in HEAD~4 are more than just four commits — if for example HEAD~2 is a merge commit, then all the commits that merge pulled in (and that aren't part of the ancestry of HEAD~4) will be included too.

**Greg Price** · 2024-08-09 20:08 UTC

Again, `gitk` or another graphical Git viewer will be an excellent way to see what's going on there.

**Aditya Chaudhary** · 2024-08-09 20:20 UTC

(replying to Greg Price)
> One thing I notice in your output above is that there's a merge commit. That can mean the commits that are in HEAD but not in HEAD~4 are more than just four commits — if for example HEAD~2 is a merge commit, then all the commits that merge pulled in (and that aren't part of the ancestry of HEAD~4) w …

Yes, this is only the case. Is there any way to resolve this ?

**Aditya Chaudhary** · 2024-08-09 20:23 UTC

For more better picture this is the case: 

```
 git log --oneline --graph --decorate
* 527542728e (HEAD -> branch-msg-notification, origin/branch-msg-notification) linter: Fix the issue for linter in unread.ts
* b6db55ee13 linter: Fix the linter issue for the unread.ts
*   206ef6ef37 Merge branch 'main' of https://github.com/userAdityaa/zulip into branch-msg-notification
|\  
| * de35f44624 (origin/main, origin/HEAD, main) zulip_updates: Mention default for send navigation.
| * 4351cc5914 thumbnail: Move get_image_thumbnail_path and split_thumbnail_path.
| * d474600056 tests: Remove a nonsensical no-op vimeo test.
| * 424f3dd503 tests: Break up and reorganize test_markdown.py.
| * ecdf5713c2 tests: Factor out ZulipVerboseEqualTest class, and use more. 
```

**Greg Price** · 2024-08-09 20:38 UTC

Probably the first thing to do is to get rid of the merge by rebasing your changes atop main: just `git rebase` will do it if you have the branch upstream set correctly, or `git rebase origin/main` to be more explicit

**Notification Bot** · 2024-08-09 20:55 UTC

@Aditya Chaudhary has marked this topic as resolved.


## git reset older commits without reseting newer ones

*2024-08-10 to 2024-08-11 · 6 messages · [open in Zulip](https://chat.zulip.org/#narrow/channel/44-git-help/topic/git.20reset.20older.20commits.20without.20reseting.20newer.20ones/with/1916063)*

**Khader Khudair** · 2024-08-10 10:17 UTC

You can see in my pr [#F779](https://github.com/zulip/zulip-flutter/pull/779) @Greg Price  has pushed new commits on top of the existing ones. 
Normally, I'd `git reset` my commits and fix them and recommit them one by one. I wonder is there any other way that can help avoiding to reset Greg's commits?

**Mateusz Mandera** · 2024-08-11 19:04 UTC

Not sure if I understand the issue correctly, I may be missing why you need to `reset` your commits. But ordinarily this sounds like something where you should  use an interactive rebase  (`git rebase -i`) and mark the commits you want to fix for `edit`. And the rebase will take you commit-by-commit allowing you to amend the individual commits that need changes. https://zulip.readthedocs.io/en/latest/git/fixing-commits.html#fixing-older-commits mentions this

**Mateusz Mandera** · 2024-08-11 19:08 UTC

Or you could do whatever your usual flow is on a branch with Greg's commits removed, and then when you're done `cherry-pick` them onto this new branch.

(using the current commit SHAs in the PR):
```
git cherry-pick 463e270108f6acb4d8ad3da14d0cf5c884d3adc3 4f6283ee4df05f4d216aea748f560a09e6932a6c fab52eff8ec31c4de1c94694b99c1d2fdcb1f9f8
```

**Greg Price** · 2024-08-11 19:35 UTC

Yeah, the tool I'd recommend for this in general (including when it's all your own changes) is `git rebase -i`.

In addition to the section @Mateusz Mandera linked, the other section on this in our docs is here:
https://zulip.readthedocs.io/en/latest/git/using.html#examine-and-tidy-your-commit-history
It links to the upstream git-rebase doc:
https://git-scm.com/docs/git-rebase
as well as a tutorial from GitHub which may be helpful:
https://docs.github.com/en/get-started/using-git/using-git-rebase-on-the-command-line

**Greg Price** · 2024-08-11 19:43 UTC

(And that `git cherry-pick` solution will also work, if you find it easier to mostly stick to your existing approach for the moment. But in that case I definitely still recommend starting to experiment with `git rebase -i` afterward — I think you'll find it simplifies things a lot when revising a branch.)

**Greg Price** · 2024-08-11 19:45 UTC

The other thing I'd recommend alongside that is to use `gitk` or another graphical Git viewer to see your branch, and especially to see both the old and new versions when you're making a revision (either with `git rebase -i`, or with `git reset` and `git commit`):
https://github.com/zulip/zulip-mobile/blob/main/docs/howto/git.md#graphical-client


## git-delta

*2024-08-21 to 2024-09-04 · 5 messages · [open in Zulip](https://chat.zulip.org/#narrow/channel/44-git-help/topic/git-delta/with/1928454)*

**Zixuan James Li** · 2024-08-21 19:42 UTC

Has anyone used [git-delta](https://github.com/dandavison/delta) before? It offers syntax highlighting for the git pager and seems to be pretty customizable as well.

**Zixuan James Li** · 2024-08-21 19:42 UTC

I think it doesn't support `git range-diff`, though.

**Greg Price** · 2024-08-21 20:09 UTC

I haven't. You could try it out!

**Alex Vandiver** · 2024-09-04 16:08 UTC

@Zixuan James Li:  Have you been using it?  Any thoughts on it?

**Zixuan James Li** · 2024-09-04 16:16 UTC

I think I didn't end up relying on its syntax highlighting feature in particular. I'm mostly for the aesthetics when I use `git log --stat -p` (very tweakable with with some git configs).

I found it easier to  see the file headings than the default, and I appreciate its highlight markers for in-line changes. In general just makes things easier for my eyes.


## build coq project

*2024-09-09 to 2024-09-09 · 2 messages · [open in Zulip](https://chat.zulip.org/#narrow/channel/44-git-help/topic/build.20coq.20project/with/1938560)*

**Zhanquen** · 2024-09-09 14:02 UTC

I encounter a problem while I am downloading a coq project. Thanks if someone can offer a help
For OS I use Mac Pro.
I deleted the local repository and did git clone on my root, then tried make all but an error occurred. Due to this, I can't open the libraries in the project due to mistake of coqide. 
[image.png](https://chat.zulip.org/user_uploads/2/31/SJLViI36kNdgXYNU7cODgo7y/image.png)
Although the error occurred only after I had deleted the repository, I have my nix reinstalled with help of https://github.com/coq-community/coq-nix-toolbox?tab=readme-ov-file, so as coqide.
In addition, the project itself doesn't contain error because before I used it normally.

**Tim Abbott** · 2024-09-09 15:32 UTC

I think you meant to ask in https://coq.zulipchat.com, not this Zulip instance (for the development of Zulip itself).


## editing hunk

*2024-09-27 to 2024-09-30 · 18 messages · [open in Zulip](https://chat.zulip.org/#narrow/channel/44-git-help/topic/editing.20hunk/with/1950266)*

**Zixuan James Li** · 2024-09-27 20:59 UTC

`git add -i` is a neat feature that offers a range of interactive tools for staging/unstaging changes. Among them, there is this `patch` option that allows you to add changes by hunks.

**Zixuan James Li** · 2024-09-27 21:00 UTC

Sometimes it might be useful to decide what part of the working tree belongs to the commit at the file level, and a plain `git add` would be more than sufficient.

**Karl Stolley** · 2024-09-27 21:00 UTC

Also `git add -p` will get you straight into that mode. A related inverse action is `git restore -p`, which let's you remove hunks.

**Zixuan James Li** · 2024-09-27 21:00 UTC

But in case you need a granularity level by lines, the `patch` option becomes useful.

**Zixuan James Li** · 2024-09-27 21:01 UTC

(replying to Karl Stolley)
> Also `git add -p` will get you straight into that mode. A related inverse action is `git restore -p`, which let's you remove hunks.

TIL. That's pretty neat!

**Karl Stolley** · 2024-09-27 21:01 UTC

It's pretty indispensable!

**Zixuan James Li** · 2024-09-27 21:01 UTC

The one thing that I'm wondering about, is how you generally approach to editing hunks. This is one of the options you have when `patch`ing changes.

**Zixuan James Li** · 2024-09-27 21:02 UTC

The quick guide that appears at the bottom of your hunk when you enter this mode makes it seem easy:

```bash
# ---
# To remove '-' lines, make them ' ' lines (context).
# To remove '+' lines, delete them.
# Lines starting with # will be removed.
# If the patch applies cleanly, the edited hunk will immediately be marked for staging.
# If it does not apply cleanly, you will be given an opportunity to
# edit again.  If all lines of the hunk are removed, then the edit is
# aborted and the hunk is left unchanged.
```

**Zixuan James Li** · 2024-09-27 21:04 UTC

However, it seems more than that. Because if I just follow the instructions there, there are still chances that the edit cannot be applied cleanly.

**Zixuan James Li** · 2024-09-27 21:08 UTC

This seems to happen when I do something semi-complicated, such as removing both `+` and `-` lines at the same time.

**Zixuan James Li** · 2024-09-27 21:10 UTC

I guess I also need to update the line numbers at the top too, but this makes me feel that there might be a better workflow for hunk editing.

**Greg Price** · 2024-09-27 21:51 UTC

Yeah, I use `git add -p` regularly, as well as the related `git checkout -p` (which is very similar to `git restore -p`). Very useful!

**Greg Price** · 2024-09-27 21:54 UTC

I've found its "edit" mode to be pretty finicky. I'm sure if I really thought through it carefully I could reliably make it work — but at that point it always feels like more effort than it would be to just edit the file directly in the tree, after either taking the whole hunk or none of it.

I occasionally still use the "edit" mode when the edit I want to make is very simple so that I'm confident I can do it accurately without thinking hard.

**Greg Price** · 2024-09-27 21:56 UTC

(replying to Zixuan James Li)
> I guess I also need to update the line numbers at the top too, but this makes me feel that there might be a better workflow for hunk editing.

(I don't *think* the failures to apply cleanly will be about the line numbers, though.)

**Tim Abbott** · 2024-09-27 21:57 UTC

I use the "split" feature of `git add -p` pretty often, when its hunks are too large.

**Zixuan James Li** · 2024-09-27 23:10 UTC

Yeah, editing the file directly is a good workaround. I currently just rely on my editor's undo queue to make temporary changes for staging when it becomes tricky.

**Mateusz Mandera** · 2024-09-27 23:14 UTC

I didn't try figuring out `git`'s  built-in UX for working with hunks, but I found vscode's functionality for it super good. In the terminal,  `lazygit`'s flow for this has been  pretty okay too.

**Puneeth Chaganti** · 2024-09-30 04:05 UTC

I use `magit` from within Emacs to do this. And it works quite well too.


## dif

*2024-10-12 to 2024-10-15 · 5 messages · [open in Zulip](https://chat.zulip.org/#narrow/channel/44-git-help/topic/dif/with/1960940)*

**Donald Nweyilobu** · 2024-10-12 08:16 UTC

i want to use git diff to compare files from a remote repositoy ro my local repository. the file is test\widgets\theme_test.dart. does anyone know how?

**Karl Stolley** · 2024-10-14 15:23 UTC

Sure. First you want to run `git fetch` on the remote you're looking to compare. From your working branch, you'd then run:

```
$ git diff some-remote/some-branch test/widgets/theme_test.dart
```

**Greg Price** · 2024-10-15 21:10 UTC

@Donald Nweyilobu In addition to @Karl Stolley's direct answer to your question, I highly recommend setting up and using `gitk` or another graphical Git viewer.

That will help a lot for you to see what's going on in your repository, including how your commits relate to each other and to the upstream commits. Among other things it'll help you identify what you should pass for `some-remote/some-branch` in the example command Karl gave.

**Donald Nweyilobu** · 2024-10-15 23:35 UTC

I am using git kraken.  It was how I was able to see my error.
Of theme and Design variables.

**Greg Price** · 2024-10-15 23:49 UTC

Cool, that should help.

Seeing this thread again, I see I forgot to post the links to our docs I meant to include:
https://github.com/zulip/zulip-mobile/blob/main/docs/howto/git.md#graphical-client
https://zulip.readthedocs.io/en/latest/git/setup.html#get-a-graphical-client


## commit history

*2024-10-17 to 2024-10-25 · 15 messages · [open in Zulip](https://chat.zulip.org/#narrow/channel/44-git-help/topic/commit.20history/with/1963843)*

**Donald Nweyilobu** · 2024-10-17 07:00 UTC

[commit history.PNG](https://chat.zulip.org/user_uploads/2/d8/XjvdU0G_VP7ra8SSuUPvCxCy/commit-history.PNG)
[tool check 1.PNG](https://chat.zulip.org/user_uploads/2/91/-mWcw6AMKYeaQo9tnq5kO7x3/tool-check-1.PNG)
[tool check 2.PNG](https://chat.zulip.org/user_uploads/2/30/14x_6ii_tyW6njn4LeZTXitU/tool-check-2.PNG)
[tool check.PNG](https://chat.zulip.org/user_uploads/2/e3/yZSe4YPJl7oPsoT-XUdejLNf/tool-check.PNG)

i was told that mu commit history was unclean and that not all of the commits passes but according to these screensshots and this link to my oull request. That doesn'tr seem to be the case. Except there's something I'm not seeing?

**Aman (amanagr)** · 2024-10-17 07:08 UTC

We can help if you link your pull request and the exact error message.

**Donald Nweyilobu** · 2024-10-17 09:16 UTC

That's the thing. There I don't see any errors, but greg says that my commits didn't pass the tets. He also said my commit history was broke, but i viewed it with Git Kraken and it seems fine to me.

**Donald Nweyilobu** · 2024-10-17 09:17 UTC

https://github.com/zulip/zulip-flutter/pull/991. here is the link to my pull request. If  you see anything wrong please tell me, but i don't.

**Aman (amanagr)** · 2024-10-17 09:39 UTC

He means that each commit should pass the test without the later commits. Also, the commit message don't follow our https://zulip.readthedocs.io/en/latest/contributing/commit-discipline.html

**Donald Nweyilobu** · 2024-10-17 11:09 UTC

Okay, thanks. Did you check the link to my pull request

**Donald Nweyilobu** · 2024-10-17 11:12 UTC

Because I think I did follow the commit rules as best as I did. What did I
do wrong. I followed the naming convention of the commits. I made sure my
tasks were minimal in every commit. And I removed every error and unused
imports. So what did I do wrong?

**Anders Kaseorg** · 2024-10-17 19:02 UTC

As an obvious example of something that breaks the rules: you have a commit “test: Add widget tests for custom themes in theme_test.dart” that uses the `get` package, *followed* by a commit “chore: Add get dependency to the project” that provides the `get` package. The former commit won’t work without the latter, so you need to reorder the latter commit before the former.

Greg told you “it's broken after the first commit (and in fact stays broken until near the end)”, so that must not be the only such problem.

**Donald Nweyilobu** · 2024-10-17 19:05 UTC

Thank you.

**Anders Kaseorg** · 2024-10-17 19:06 UTC

Putting all changes in the right order is important both for human readability, and for the ability to use [`git bisect`](https://git-scm.com/docs/git-bisect) to diagnose bugs.

**Greg Price** · 2024-10-17 21:03 UTC

Yep, all of the above.

If you check out any of the previous commits in your branch and run `tools/check`, if the Git history in your branch is clean then it should pass. If it doesn't pass, then that's something that needs to be fixed. (Even if it does pass when you check out the tip commit of your branch.)

**Brynly Mitchell** · 2024-10-25 00:57 UTC

Hi, I've been asked to clean up my branch's commit history and was wondering how to go about this. 
My first commit fails as my second commit fixes the tests, should these commits be combined?
And how do I go about undoing accidental changes I made in earlier commits? Should my commit messages also be revised?

**Greg Price** · 2024-10-25 01:05 UTC

Yes, if one change breaks tests and another fixes them, those should go in the same commit. See our guide here:
https://zulip.readthedocs.io/en/latest/contributing/commit-discipline.html#each-commit-must-be-coherent

**Greg Price** · 2024-10-25 01:05 UTC

For the mechanics of fixing up earlier commits, you'll want `git rebase -i`. Some resources here:
https://zulip.readthedocs.io/en/latest/git/using.html#examine-and-tidy-your-commit-history

**Brynly Mitchell** · 2024-10-25 01:32 UTC

thanks


## undo merge

*2024-10-28 to 2024-10-29 · 39 messages · [open in Zulip](https://chat.zulip.org/#narrow/channel/44-git-help/topic/undo.20merge/with/1970892)*

**Arpan** · 2024-10-28 05:23 UTC

now how can i unmerge this from my local project.. and make all this things right

**Arpan** · 2024-10-28 05:28 UTC

i know i understand things a little late but i have interst in coding that why i just wanted to contribute in zulip flutter i..if i have to read or code for 18 hours i dont have any problem i just wanted to contribute

**Arpan** · 2024-10-28 05:30 UTC

i tried  `git reset` but it didn't help any way

**Arpan** · 2024-10-28 05:54 UTC

after that git merge message it showing like this 
[Screenshot (108).png](https://chat.zulip.org/user_uploads/2/47/8HlKB7gxyxKuW7DGIL7QQuHh/Screenshot-108.png)

**Arpan** · 2024-10-28 05:56 UTC

i read also undo the merge commit but i didn't understand ...

**Greg Price** · 2024-10-28 06:26 UTC

(replying to Arpan)
> i read also undo the merge commit but i didn't understand ...

Do you mean this section of our docs?
https://zulip.readthedocs.io/en/latest/git/troubleshooting.html#undo-a-merge-commit

That's a good one to be looking at. If you can ask a specific question about what it is you don't understand there (or even explain the parts you do understand), that might make it possible for someone to help.

**Greg Price** · 2024-10-28 06:26 UTC

Also for questions about using Git, #**git help** is a better channel to ask in — that way there are more people who might answer.

**Arpan** · 2024-10-28 06:29 UTC

yes i read that doc ... i want to ask about the problem in my local project shows ...

**Arpan** · 2024-10-28 06:30 UTC

i want to make that right and want to contribute

**Arpan** · 2024-10-28 06:32 UTC

as in that doc says we can use `git reset` ..i use that but the error are not going...

**Prakhar Pratyush** · 2024-10-28 06:42 UTC

> after succesfully upgrade the pigeon i tried to push the code but it shows me like this and telling to do git pull so i did git pull

`git pull` is `git fetch` followed by `git merge`. 

The zulip [doc mentions](https://zulip.readthedocs.io/en/stable/git/overview.html#quick-start-how-zulip-uses-git-and-github):
> We use a **[rebase](https://git-scm.com/book/en/v2/Git-Branching-Rebasing)-oriented workflow.** We do not use merge commits. This means you should use `git fetch` followed by `git rebase` rather than `git pull` (or you can use `git pull --rebase`).

**Prakhar Pratyush** · 2024-10-28 06:44 UTC

> as in that doc says we can use `git reset` ..i use that but the error are not going...

Did you follow [all the steps mentioned here](https://zulip.readthedocs.io/en/latest/git/troubleshooting.html#undo-a-merge-commit) ?

**Arpan** · 2024-10-28 06:54 UTC

no that time i didn't follow all the steps .. i just did `git reset` .. i didn't understand what happend that time and get scared and i did `git reset` ....but nothing chnages .

**Prakhar Pratyush** · 2024-10-28 07:34 UTC

What's the output of `git status`and `git log` ?

**Arpan** · 2024-10-28 08:05 UTC

`git status` said - 
```On branch test
Your branch is ahead of 'origin/main' by 116 commits.
  (use "git push" to publish your local commits)

nothing to commit, working tree clean

```

**Arpan** · 2024-10-28 08:06 UTC

and `git log` - 
```commit e008fd47f90e0805b4bd8d809230ba34d7c64b6c (HEAD -> test)
Merge: f419beb 6aaf506
Author: Arpan Mondal <arpanmondal572@gmail.com>
Date:   Sun Oct 27 11:42:26 2024 +0530

    Merge branch 'test' of https://github.com/ArpanMondalGITHUB/zulip-flutter into test

commit f419beb5262ef7a8f40fbadd170da1ea6db5ba15
Author: Arpan Mondal <arpanmondal572@gmail.com>
Date:   Sun Oct 27 11:38:43 2024 +0530
:

```

**Prakhar Pratyush** · 2024-10-28 08:16 UTC

> Did you follow [all the steps mentioned here](https://zulip.readthedocs.io/en/latest/git/troubleshooting.html#undo-a-merge-commit) ?

Follow the steps mentioned here. 

Then read [Using Git as you work](https://zulip.readthedocs.io/en/latest/git/using.html)

**Arpan** · 2024-10-28 13:37 UTC

as you said to follow the steps i read that and try to follow ..but didn't understand which commit hash i have to do `git reset --hard the hash`

**Arpan** · 2024-10-28 13:38 UTC

i did `git reflog` and it gives me this -

**Arpan** · 2024-10-28 13:38 UTC

```e008fd4 (HEAD -> test) HEAD@{0}: reset: moving to HEAD
e008fd4 (HEAD -> test) HEAD@{1}: pull origin test: Merge made by the 'ort' strategy.
f419beb HEAD@{2}: commit: fix: made List and Map items non-nullable and update the pigeon successfully
756371a HEAD@{3}: reset: moving to HEAD
756371a HEAD@{4}: reset: moving to HEAD
756371a HEAD@{5}: checkout: moving from main to test

```

**Arpan** · 2024-10-28 13:39 UTC

should i have to do`git reset --hard` this - 
````e008fd4 (HEAD -> test) HEAD@{1}: pull origin test: Merge made by the 'ort' strategy.`

```

**Arpan** · 2024-10-28 13:42 UTC

i am trying to understand from that time you tell me ...

**Arpan** · 2024-10-28 13:44 UTC

but here the HEAD{0} AND HEAD{1} hash is same 
```PS C:\Users\Arpan Mondal\test\zulip-flutter> git reflog
e008fd4 (HEAD -> test) HEAD@{0}: reset: moving to HEAD
e008fd4 (HEAD -> test) HEAD@{1}: pull origin test: Merge made by the 'ort' strategy.
f419beb HEAD@{2}: commit: fix: made List and Map items non-nullable and update the pigeon successfully
756371a HEAD@{3}: reset: moving to HEAD
756371a HEAD@{4}: reset: moving to HEAD
756371a HEAD@{5}: checkout: moving from main to test

```

**Arpan** · 2024-10-28 15:28 UTC

what should i do

**Prakhar Pratyush** · 2024-10-29 03:13 UTC

`git reset --hard f419beb`

**Arpan** · 2024-10-29 03:16 UTC

okay

**Arpan** · 2024-10-29 03:20 UTC

yes all the error are gone ....

**Arpan** · 2024-10-29 03:23 UTC

now i can do? `git push origin test`

**Arpan** · 2024-10-29 03:23 UTC

my branch shows it have 3 commit ..

**Arpan** · 2024-10-29 03:24 UTC

```Date:   Fri Oct 25 11:36:51 2024 +0530

PS C:\Users\Arpan Mondal\test\zulip-flutter> git status
On branch test
Your branch is ahead of 'origin/main' by 3 commits.
  (use "git push" to publish your local commits)

nothing to commit, working tree clean

```

**Arpan** · 2024-10-29 03:25 UTC

now what i have to do?

**Prakhar Pratyush** · 2024-10-29 03:31 UTC

Please read [Using Git as you work](https://zulip.readthedocs.io/en/latest/git/using.html) and related docs to understand "now what i have to do". Understanding git is important to contribute to the project.

**Arpan** · 2024-10-29 03:39 UTC

i should use this ?
```git checkout feature-branch
Switched to branch 'feature-branch'

$ git rebase upstream/main

$ git push origin feature-branch```

**Arpan** · 2024-10-29 03:41 UTC

because i have a feature branch named test

**Notification Bot** · 2024-10-29 04:12 UTC

34 messages were moved here from #**mobile-dev-help>Pigeon upgrade** by @Greg Price.

**Greg Price** · 2024-10-29 04:13 UTC

I've moved this part of the thread to #**git help** because it's about using Git and not about the mobile codebase in particular. (Thanks @Prakhar Pratyush for answering questions in this thread today!)

**Arpan** · 2024-10-29 04:13 UTC

when i did 
```  test
PS C:\Users\Arpan Mondal\test\zulip-flutter> git fetch upstream
fatal: 'upstream' does not appear to be a git repository
fatal: Could not read from remote repository.

Please make sure you have the correct access rights
and the repository exists.

```

**Arpan** · 2024-10-29 04:14 UTC

what i have to write other than upstream

**Greg Price** · 2024-10-29 04:15 UTC

I'll echo @Prakhar Pratyush's advice [above](https://chat.zulip.org/#narrow/channel/44-git-help/topic/undo.20merge/near/1971540):
> Please read [Using Git as you work](https://zulip.readthedocs.io/en/latest/git/using.html) and related docs to understand "now what i have to do". Understanding git is important to contribute to the project.


## git checkout

*2024-10-31 to 2024-11-01 · 6 messages · [open in Zulip](https://chat.zulip.org/#narrow/channel/44-git-help/topic/git.20checkout/with/1973172)*

**Kurosaki** · 2024-10-31 04:54 UTC

Hey guys, Noob question. Why do my changes in the `testing-dev` branch reflect in the `main` branch? Did I miss something?
[image.png](https://chat.zulip.org/user_uploads/2/f0/c3SdQ_EIdSY86UBAgC0bSfAN/image.png)

**Aman (whilstsomebody)** · 2024-10-31 06:32 UTC

You might have checked out from the feature-branch to main without staging or stashing your changes.
Git usually gives warning, but sometimes this issue occurs.
You can simple revert those changes in the main.

**Kurosaki** · 2024-10-31 11:07 UTC

(replying to Aman (whilstsomebody))
> You might have checked out from the feature-branch to main without staging or stashing your changes. Git usually gives warning, but sometimes this issue occurs. You can simple revert those changes in the main.

Thanks, i just wanted to clarify that.

**Greg Price** · 2024-11-01 01:56 UTC

The changes you're referring to are changes that weren't part of any commit. That means they weren't "in the `testing-dev` branch" or any other branch.

**Greg Price** · 2024-11-01 01:58 UTC

Take a look at `git help checkout`.

       git checkout [<branch>]
           […]
           Local modifications to the files in the working tree are kept, so that
           they can be committed to the <branch>.

So those modifications were kept.

**Kurosaki** · 2024-11-01 06:40 UTC

(replying to Greg Price)
> The changes you're referring to are changes that weren't part of any commit. That means they weren't "in the `testing-dev` branch" or any other branch.

Thanks Greg, now this gives me a lot of clarity.


## ✔ Links get broken on wrapping.

*2024-11-14 to 2024-11-15 · 3 messages · [open in Zulip](https://chat.zulip.org/#narrow/channel/44-git-help/topic/.E2.9C.94.20Links.20get.20broken.20on.20wrapping.2E/with/1981147)*

**Aman (whilstsomebody)** · 2024-11-14 10:04 UTC

When I try to add a link, it often exceeds the 72-character per line limit, so I attempt to wrap it to another line, but the link gets broken when I do so. Could someone tell me how to fix this?

**Prakhar Pratyush** · 2024-11-14 16:06 UTC

> * Your commit message should be line-wrapped to about 68 characters per line, but no more than 70, so that your commit message will be easy to read in `git log` in a normal terminal. (It’s OK for links to be longer – ignore `gitlint` when it complains about them.)

[Docs](https://zulip.readthedocs.io/en/latest/contributing/commit-discipline.html#formatting-guidelines)

**Notification Bot** · 2024-11-15 05:31 UTC

@Aman (whilstsomebody) has marked this topic as resolved.


## ✔ Increasing efficiency with zulip git workflow

*2024-11-30 to 2024-12-02 · 8 messages · [open in Zulip](https://chat.zulip.org/#narrow/channel/44-git-help/topic/.E2.9C.94.20Increasing.20efficiency.20with.20zulip.20git.20workflow/with/1990558)*

**Apoorva Pendse** · 2024-11-30 14:43 UTC

I wanted to know from some of the experienced folks, that how do you deal with having to restructure your commits as per feedback.

My current workflow is pull --rebase upstream main
Then reset soft to the latest upstream commit, when the changes I'll be making will cause some disruption of the commits on the local, such that I would have to redo them, which is generally most of the times.

Make changes and git add -p the changes to make commits reflect to a single idea.

Right now, making changes is less time consuming than crafting commits.

Just wanted to know if there is a better way to do this, or any suggestions from you guys.
Thanks

**Aman (amanagr)** · 2024-12-02 06:12 UTC

Looks like you are having trouble resolving merge conflicts. Reading the commit which broke your changes could help other than carefully reading the conflict diff.

**Apoorva Pendse** · 2024-12-02 06:12 UTC

No I do not have any merge conflicts

**Apoorva Pendse** · 2024-12-02 06:16 UTC

@Aman (amanagr), the question was about being efficient with the git workflow when dealing with some minor suggestions that make you restructure your commits from the start

eg : I made 3 commits for some issue
A core maintainer then points some one liner change which was related to the first commit.
I basically have to reset all the commits in my local and make them from scratch.

This has happened a handful of times in the last week which is why I raised this question wondering if there is a better/efficient way to do this.

**Aman (amanagr)** · 2024-12-02 06:17 UTC

Yeah, you can use interactive rebase to navigatie to your first commit and apply changes to the code and then amend them to the first commit.

**Apoorva Pendse** · 2024-12-02 06:18 UTC

Sure, I will try that :thumbs_up: 
Thanks

**Aman (amanagr)** · 2024-12-02 06:18 UTC

Read https://zulip.readthedocs.io/en/stable/git/using.html#examine-and-tidy-your-commit-history

**Notification Bot** · 2024-12-02 11:14 UTC

@Apoorva Pendse has marked this topic as resolved.


## Regarding Open Source Community Guidelines

*2024-12-12 to 2024-12-12 · 5 messages · [open in Zulip](https://chat.zulip.org/#narrow/channel/44-git-help/topic/Regarding.20Open.20Source.20Community.20Guidelines/with/2001227)*

**Gaurav Kushwaha** · 2024-12-12 16:41 UTC

Hello,
I am a new contributor, and today I picked up my first issue but it is still not assigned to me.

So, I was having a slight doubt regarding the guidelines that is it allowed to open PR if the issue isn't assigned to you.
Since, I have already resolved it, so I wanted open raise the PR.

**Gaurav Kushwaha** · 2024-12-12 16:41 UTC

Issue: https://github.com/zulip/zulip-flutter/issues/1142

**Gaurav Kushwaha** · 2024-12-12 16:42 UTC

@Chris Bobbe

**Chris Bobbe** · 2024-12-12 22:36 UTC

I responded on the issue.

**Chris Bobbe** · 2024-12-12 22:37 UTC

Oh I see; you have a PR ready to send? Please send it if it's ready for a review (follows our Git style, etc.)


## reorder commits

*2024-12-18 to 2024-12-20 · 14 messages · [open in Zulip](https://chat.zulip.org/#narrow/channel/44-git-help/topic/reorder.20commits/with/2008844)*

**billy** · 2024-12-18 19:35 UTC

@Chris Bobbe Hello there, I have attempted to reorder the commits and resolved the confusing conflicts. But before proceeding, can you verify this here: https://github.com/tomlin7/zulip-flutter/commits/testing-rebase/

**Chris Bobbe** · 2024-12-18 19:41 UTC

That looks almost right to me :smile: but the commit that adds the new menu button—

```
e7c1d59  nav: Add an About Zulip button to the main menu
```

—is still using `Icons.info`; it should use the new `ZulipIcons.info` instead (the icon you added in the prep commit).

**billy** · 2024-12-18 19:50 UTC

That is right! thanks for pointing it out. I lost the changes because that change was amended to `icon` commit. 
I have amended that change to `nav` commit and pushed. It looks like I'm good to proceed now! tests are also passing

**Greg Price** · 2024-12-18 20:39 UTC

One thing I routinely do after a `rebase -i` is that I'll compare the revised version of the branch to the previous one. For example, just after rebasing:
```
$ git diff --stat -p @{1}
```
which compares to the previous value of the current branch.

Or as a step before pushing the revised branch:
```
$ git diff --stat -p me/dev-whatever
$ git push me +@:dev-whatever
```

**Greg Price** · 2024-12-18 20:40 UTC

That's helpful because it catches this kind of situation, where a change was accidentally lost as part of reordering some commits.

**Greg Price** · 2024-12-18 20:42 UTC

More fully, the sequence of commands I routinely do after rewriting a branch with `git rebase -i` is:
```
$ git diff --stat -p me/dev-whatever
$ git range-diff origin me/dev-whatever @
$ git push me +@:dev-whatever
```

The `git range-diff` command is a bit more complex to read the output of — it's comparing the old and new sequences of changes, so it's diffs of diffs — but it's a second and more detailed way to confirm that the revisions are what I intended.

**billy** · 2024-12-19 06:05 UTC

@Greg Price that is very helpful, but since I'm using the GUI merge editor, the conflict resolving part becomes easier!
I prefer using vscode for viewing diff, terminal is a bit too hard.

**Greg Price** · 2024-12-19 06:22 UTC

Cool. Does VS Code have a way to compare the tree at one commit with the tree at another? Like the `git diff` commands I mentioned above.

**Greg Price** · 2024-12-19 06:23 UTC

Even with a helpful tool, you'll sometimes have oversights, particularly when merge conflicts are more complex. So it's useful to be able to check your work by comparing the final results.

**Apoorva Pendse** · 2024-12-19 08:55 UTC

(replying to Greg Price)
> One thing I routinely do after a `rebase -i` is that I'll compare the revised version of the branch to the previous one. For example, just after rebasing: `$ git diff --stat -p @{1}`
This is really helpful, thanks for sharing @Greg Price !

**Apoorva Pendse** · 2024-12-19 08:58 UTC

(replying to Greg Price)
> Cool. Does VS Code have a way to compare the tree at one commit with the tree at another? Like the `git diff` commands I mentioned above.

[image.png](https://chat.zulip.org/user_uploads/2/16/_JYr3ZoLCW7r25FNl_j9ofwr/image.png)
Yes, it does show diffs like the one in the img, not sure if it is possible to inspect diffs wrt reflog.

**billy** · 2024-12-19 09:31 UTC

(replying to Greg Price)
> Even with a helpful tool, you'll sometimes have oversights, particularly when merge conflicts are more complex. So it's useful to be able to check your work by comparing the final results.

Sure yeah, every GUI-based git wrapper has its limitations of course. Sometimes it slows you down at the cost of showing a clear picture of what is happening. VSC alone doesn't do much, but as mentioned by @Apoorva Pendse Gitlens helps a lot, it's literally a Gitkraken running inside your editor! 

Diff can be configured, but not as quickly or versatile as the git diff command
[image.png](https://chat.zulip.org/user_uploads/2/2d/ZujSMcQfxafmO3I0XBQVV9E-/image.png)

**Apoorva Pendse** · 2024-12-19 10:01 UTC

(replying to billy)
> Diff can be configured, but not as quickly or versatile as the git diff command

Thanks for sharing billy :thumbs_up: , 

BTW you can use silent mentions for core team by adding an underscore between `@` and `*` 
Example: `@Greg Price` instead of `@Greg Price`.
So it causes them fewer notifications and less trouble in cases where you don't need their immediate attention.

See 
- https://zulip.com/development-community/#getting-help.
- https://zulip.com/help/mention-a-user-or-group#silently-mention-a-user

**Greg Price** · 2024-12-20 04:38 UTC

(replying to billy)
> Diff can be configured, but not as quickly or versatile as the git diff command [image.png](https://chat.zulip.org/user_uploads/2/2d/ZujSMcQfxafmO3I0XBQVV9E-/image.png)

Great. Yeah, if you find it's more convenient for you to compare the tip of your new revision with the tip of the previous revision by using that than by using `git diff`, then whatever works is good.

The key is just to have some way that you reread your changes, using whichever tool does the job for you, so as to check your work.


## undo rename

*2024-12-20 to 2024-12-20 · 1 messages · [open in Zulip](https://chat.zulip.org/#narrow/channel/44-git-help/topic/undo.20rename/with/2010848)*

**Notification Bot** · 2024-12-20 04:06 UTC

This topic was moved to #**development help>"typing" module shadowed** by @Greg Price.


## make git blame show actual authors in a single commit.

*2025-01-02 to 2025-01-03 · 11 messages · [open in Zulip](https://chat.zulip.org/#narrow/channel/44-git-help/topic/make.20git.20blame.20show.20actual.20authors.20in.20a.20single.20commit.2E/with/2023206)*

**Apoorva Pendse** · 2025-01-02 03:03 UTC

Is there a way to do this while adding changes from different authors into a single commit?
I wanted to do that for [this commit](https://github.com/zulip/zulip/pull/32864/commits/b3f4019425548221911bb3b4356483039f36dd58).
What I've tried:
1. soft resetting the commit, unstaging everything followed by `git add -p`ing  my chunks and committing them, followed by staging @Nehal Sharma's code and `git commit --amend --author=<details>`, but seems like it only retains the amended author as the author for all the lines.
2. Interactive rebase on our resp. changes split into 2 different commits and squashing them. This just ends up having git blame show me as the author for everything.

**Greg Price** · 2025-01-02 04:31 UTC

Git has only a single "author" field per commit.

There is a convention for crediting additional authors in the commit message, with "Co-authored-by:". Details here:
https://zulip.readthedocs.io/en/latest/contributing/continuing-unfinished-work.html#credit-prior-work-in-your-commit-history

**Greg Price** · 2025-01-02 04:32 UTC

Some software understands that convention, so it's helpful to use it.

**Greg Price** · 2025-01-02 04:34 UTC

`git blame` might not. But `git blame` is a very noisy tool for identifying authorship anyway — it tells you who last touched a given line, and that's often someone who did a broad refactor rather than someone it'd make sense to describe as an author of that piece of code.

**Greg Price** · 2025-01-02 04:39 UTC

When you want to find out who wrote some code (and when, and what their commit message said about why), the technique I find much more effective is to use `git log -p`.

The key is to (a) use some of its handy features for narrowing down which commits you see, and then (b) use my "secret" for giving you basically a keybinding meaning "next commit". Then you can very efficiently skip past any remaining commits that are boring (because they're unrelated refactors, for example) to find the one or two commits that really introduced the relevant logic.

Details on that "secret", and some other tips for reading Git history, are here:
https://github.com/zulip/zulip-mobile/blob/main/docs/howto/git.md#reading-history

**Apoorva Pendse** · 2025-01-02 05:14 UTC

(replying to Greg Price)
> There is a convention for crediting additional authors in the commit message, with "Co-authored-by:". Details here:

Yes, I did go through that.
But I thought that having some way to know the exact lines last touched by someone would be better to demonstrate what the individual contributions were. 

```spoiler I wrote this little script to check the diff blame for a commit
But it is basically useless, since 

(replying to Greg Price)
> Git has only a single "author" field per commit.
```bash
#!/usr/bin/env bash

max_length=10

if ! git rev-parse --is-inside-work-tree > /dev/null 2>&1; then
  echo "Error: This script must be run inside a Git repository."
  exit 1
fi

if [ -z "$1" ]; then
  echo "Error: You need to pass a commit hash as the first argument."
  exit 1
fi

input_hash=$1

# Get the first 10 characters of the commit hash
commit_hash=$(git rev-parse --short=10 "$input_hash")

echo "Using commit hash: $commit_hash"

git show "$commit_hash" --name-only --pretty=format: | while read -r file; do
  echo "Blaming file: $file"
  
  git blame "$file" | grep "$commit_hash" || echo "Failed to blame file: $file"
done | less
```

```

[In my case](https://github.com/zulip/zulip/pull/32864/commits/b3f4019425548221911bb3b4356483039f36dd58), I wrote/modified a handful of lines whereas the bulk of the work was done by @Nehal Sharma.

**Apoorva Pendse** · 2025-01-02 05:18 UTC

(replying to Greg Price)
> Details on that "secret", and some other tips for reading Git history, are here: https://github.com/zulip/zulip-mobile/blob/main/docs/howto/git.md#reading-history
Oooh, that's pretty neat.
I used a variation of this where I used the year / month as the pattern to skim through the commits.

**Greg Price** · 2025-01-02 22:00 UTC

(replying to Apoorva Pendse)
> Yes, I did go through that. But I thought that having some way to know the exact lines last touched by someone would be better to demonstrate what the individual contributions were.

Yeah, there isn't a mechanism for that. Even if there were, I think "line was last touched by" wouldn't be a great way to express people's contributions, for the same reason `git blame` isn't.

Instead, I think the way to express that is with a bit of text in the commit message.

**Greg Price** · 2025-01-02 22:01 UTC

> [In my case](https://github.com/zulip/zulip/pull/32864/commits/b3f4019425548221911bb3b4356483039f36dd58), I wrote/modified a handful of lines whereas the bulk of the work was done by @Nehal Sharma.

Concretely, I'd express this by:
* @Nehal Sharma as the author;
* yourself in a Co-authored-by: line;
* and then, optionally, a sentence in the commit message briefly saying which parts you did.

**Apoorva Pendse** · 2025-01-03 02:20 UTC

(replying to Greg Price)
> * and then, optionally, a sentence in the commit message briefly saying which parts you did.

Something like [this](https://github.com/zulip/zulip-flutter/commit/c02d947e74adba3848faba259c69ee3e3f658ffe#:~:text=%5Bgreg%3A%20rewrote%20comment%5D
)?

**Greg Price** · 2025-01-03 03:34 UTC

> [greg: rewrote comment]

Yeah, that's the form I sometimes use when I make significant changes to a commit just before merging it. (More often I make small changes and don't remark on them in the commit message at all.) I think @Tim Abbott uses a similar form and I borrowed it from him.

I'd actually recommend a different form, though: just a short paragraph of normal prose, saying that Nehal wrote most of the code and Apoorva wrote such-and-such parts (or whatever the right details are).


## Checks Failing Issues

*2025-01-22 to 2025-01-22 · 1 messages · [open in Zulip](https://chat.zulip.org/#narrow/channel/44-git-help/topic/Checks.20Failing.20Issues/with/2053282)*

**Notification Bot** · 2025-01-22 04:39 UTC

This topic was moved to #**mobile-dev-help>Checks Failing Issues** by @Greg Price.


## squash-merges

*2025-01-22 to 2025-01-27 · 23 messages · [open in Zulip](https://chat.zulip.org/#narrow/channel/44-git-help/topic/squash-merges/with/2053531)*

**Lakshya Goel** · 2025-01-22 10:18 UTC

Hello everyone, 
I am wondering about the reason behind force-pushing every time we make changes to our PRs. I suppose it is to maintain a clean commit history that follows the [commit discipline](https://zulip.readthedocs.io/en/latest/contributing/commit-discipline.html). I was thinking, what if we use squash commits instead? This would allow contributors to push changes directly, and at the time of merging, we could squash them all into a single commit with a valid commit message. This approach would maintain a clear commit history and also enable us to track progress more effectively, wouldn’t it? 
Happy to hear your thoughts on this as well!

**Prakhar Pratyush** · 2025-01-22 10:37 UTC

Are you suggesting pushing your changes as "update 1", "update 2" and so on (all of which belongs to one commit but the work was completed in chunks and small commits  were made + pushed to not lose your changes locally) ? And finally squashing them into one commit before review ?

**Lakshya Goel** · 2025-01-22 10:41 UTC

At the time of review as well if some changes have been suggested then we usually forced push it for maintaining a clear commit history. Can't we just keeps on changing things with adding a new commit for each change we made after review. And finally at the time of merging all of the commits can be squashed into a single one.

**Prakhar Pratyush** · 2025-01-22 10:58 UTC

Suppose a PR has 5 commits, some changes were suggested to make in the 3rd commit. Now if we add 1 commit per review comment, it'd be difficult for the reviewer to review -- "Whether these 4 new commits (for suggested change s during review) would be fine to squashed with the 3rd commit" type of overhead to think about. And a lot of complexity I can think of... 

The contributor will be fixing the commit history anyways before the PR is ready to merge, so it makes sense to present the PR in a way which we as a contributor think is good to merge in the present state. This will save multiple review cycles and easier to review.

There are other ways to see what changed since the last push.

**Lakshya Goel** · 2025-01-22 13:10 UTC

Hmm, I see how it could increase the complexity for the reviewer. However, what if, instead of reviewing commit by commit, the reviewer evaluates the changes collectively, considering all the commits together or just focusing on the latest commit? For each review cycle, the contributor could add a new commit addressing the suggestions of all the comments, and during the next review, the reviewer could again look at the changes collectively. This way, the focus remains on the overall changes rather than individual commits, streamlining the review process. What do you think?

**Apoorva Pendse** · 2025-01-22 13:21 UTC

(replying to Lakshya Goel)
> the reviewer could again look at the changes collectively

Not convenient.

**Anders Kaseorg** · 2025-01-22 14:44 UTC

Commit discipline (one commit per logical change) is important not just for pre-merge review, but also for post-merge archaeology—it’s important that tools like `git log` and `git bisect` give clear straightforward answers, rather than following the twisty path through all the known-wrong versions created during the PR’s development.

**Greg Price** · 2025-01-22 23:00 UTC

Keeping the known-wrong versions created during a PR's development out of the merged history is important for the reasons @Anders Kaseorg said. That criterion is one that's also accomplished by the squash-merge workflow discussed at the top of this thread, though, where the whole PR becomes one commit in the merged history.

**Greg Price** · 2025-01-22 23:01 UTC

There is a real trade-off we make with our current workflow: GitHub's review interface does not support it well.

When a PR is revised by only pushing new commits on top, GitHub provides an easy way to see the changes from one revision to the next. When the PR branch is force-pushed, GitHub just about memory-holes the previous revisions — it's annoying and sometimes impossible to see the old commits at all, and there's no way to get (within the GItHub web interface) a diff from the old revision to the new one.

**Greg Price** · 2025-01-22 23:03 UTC

The major thing we gain from our current workflow, compared to a squash-merge workflow, is that it's possible to have multiple commits reviewed together in a single PR.

In particular that makes it possible to split a change up into a series of small refactoring commits, and/or into different logical areas of what needs to change, like we describe here:
https://zulip.readthedocs.io/en/latest/contributing/commit-discipline.html#commits-should-generally-be-minimal

and at the same time not incur the overhead of having 3 or 6 or 20 separate PRs for such a series.

**Greg Price** · 2025-01-22 23:07 UTC

So with our current workflow, the GitHub web app doesn't support review as well as it should. Here's a thread last year where I wrote about how we handle that:

(replying to Greg Price)
> The main thing we do to mitigate that when reviewing is we fetch the PR branch, and use Git locally to see the changes. We have a couple of scripts in `tools/` that help for fetching it, in particular `tools/reset-to-pull-request`. Here's some discussion of how you can use the results of that: […]

(and see details in later messages of that thread)

**Notification Bot** · 2025-01-22 23:07 UTC

This topic was moved here from #**git help>Commit style** by @Greg Price.

**Tim Abbott** · 2025-01-22 23:40 UTC

(replying to Greg Price)
> When the PR branch is force-pushed, GitHub just about memory-holes the previous revisions — it's annoying and sometimes impossible to see the old commits at all, and there's no way to get (within the GItHub web interface) a diff from the old revision to the new one.
GitHub does have a very limited way of seeing the diff, via the "Compare" links, but they are quite hard to use if the PR was rebased onto a new `upstream/main`, since that Compare feature doesn't make use of fancier Git branch comparison techniques.

**Anders Kaseorg** · 2025-01-22 23:41 UTC

What I try to do when I edit my own PR is rebase it *using the same base* that it was based on before, unless I have a reason to change it (such as a merge conflict with newer upstream commits). That way the GitHub compare links work.

**Tim Abbott** · 2025-01-22 23:41 UTC

I'd also like to emphasize a few core things about a large software project, just for the pre-merge review use case:
- The time of the core maintainers for the project is a much more limited resource than that of other contributors, because it's very very hard to train more people who understand enough about the project to carefully review complex changes.
- It is very often the case that it stakes 10x as much time to carefully review a complex PR that is 1000 lines of changes compared to one that is written as a careful series of 12 commits that each do one coherent thing cleanly. 

In practice, I don't think I would be able to review nearly the volume of changes that I can without our policies. Well, I would if I basically stopped trying to check anything.

**Tim Abbott** · 2025-01-22 23:42 UTC

(replying to Anders Kaseorg)
> What I try to do when I edit my own PR is rebase it *using the same base* that it was based on before, unless I have a reason to change it (such as a merge conflict with newer upstream commits). That way the GitHub compare links work.

Yes, the other thing that can work is to first rebase onto `upstream/main`, then push that, and then make your changes and push those again, so it generates two "Compare" links, one of which is just a clean rebase.

**Greg Price** · 2025-01-23 00:06 UTC

Hmm interesting. I guess I never use those "Compare" links. I should try them some.

**Greg Price** · 2025-01-23 00:09 UTC

(replying to Anders Kaseorg)
> What I try to do when I edit my own PR is rebase it *using the same base* that it was based on before, unless I have a reason to change it (such as a merge conflict with newer upstream commits). That way the GitHub compare links work.

I actually find this practice helpful even though I haven't been using the compare links. (So those provide an added reason to keep the same base.) Keeping the same base means that plain `git diff` works well between the revisions of the branch — and though my primary tool for re-reviews is `git range-diff` (which generally works even when there's a new base), that command is fairly limited in the ways you can control how it does the diff, so when the changes in the revision are complex I often end up reaching for `git diff`.

**Greg Price** · 2025-01-23 00:13 UTC

I think the advice we tend to give new contributors is to do the opposite: to constantly rebase onto the latest main.

Rebasing onto latest is also what naturally happens if you do `git rebase -i` (and have fetched recently) and don't add `--keep-base`.

So between those factors, I think it's currently pretty uncommon for people to keep the same base when they revise their PRs, unless they're just never fetching. Possibly we should change our advice to encourage people to do it.

**Tim Abbott** · 2025-01-23 06:06 UTC

I find keeping the same base is not very practical in zulip/zulip; the rate of changes where your PR will break if not rebased is fairly high. Not just merge conflicts, but large across the codebase refactors.

**Tim Abbott** · 2025-01-23 06:07 UTC

Also, if you have several PRs you're maintaining, you want them to largely have the same base, since that makes the development environment re-provisioning costs a lot lower. And the only way to try to arrange that is to keep them all rebased on the latest `main`, at least as you touch them.

**Lakshya Goel** · 2025-01-23 14:42 UTC

(replying to Greg Price)
> There is a real trade-off we make with our current workflow: GitHub's review interface does not support it well.
Thank you for the insights, @Greg Price! 
I appreciate your perspective on the trade-offs between our current workflow and the squash-merge approach. I agree that the problem with GitHub's review interface not supporting our current method well is a significant concern. The complexity of reviewing large PRs can indeed be overwhelming, and so I thought of  utilizing  squashed commits for a cleaner and more manageable review process. 
However, I now understand the overhead that switching to a squash-commit strategy might cause.

**Notification Bot** · 2025-01-27 13:46 UTC

15 messages were moved from this topic to #**git help>CodeRabbit** by @Apoorva Pendse.


## CodeRabbit

*2025-01-23 to 2025-01-27 · 16 messages · [open in Zulip](https://chat.zulip.org/#narrow/channel/44-git-help/topic/CodeRabbit/with/2056069)*

**Lakshya Goel** · 2025-01-23 14:47 UTC

(replying to Tim Abbott)
> I'd also like to emphasize a few core things about a large software project, just for the pre-merge review use case: - The time of the core maintainers for the project is a much more limited resource than that of other contributors, because it's very very hard to train more people who understand eno …

Thank you for highlighting these critical points about our review process. I completely agree that the time and expertise of our core maintainers are invaluable resources, and the complexity of reviewing large PRs can be a significant bottleneck.

Given the challenges you've mentioned, particularly with reviewing complex changes that involve extensive lines of code, what if we employ some of the AI tools for the same . Many open-source repositories are successfully using tools like **[CodeRabbit](https://www.coderabbit.ai/)** (I am not aware about any other, happy to know if there are some other tools also ), which can significantly reduce the workload of the review process.

**Lakshya Goel** · 2025-01-23 14:51 UTC

Employing such tools may pace up our review process and manage the volume of pending PRs more effectively. This would not only help in keeping our project moving forward but also allow maintainers to focus on more critical aspects of the review.

**Lakshya Goel** · 2025-01-23 14:51 UTC

I’d love to hear your thoughts on this approach and whether we can explore integrating such tools into our process!

**Tim Abbott** · 2025-01-24 20:31 UTC

I've not tried CodeRabbit, but I don't think it could possibly help solve the core problem that a well-constructed PR branch solves, which is that we want any change we merge to the main branch to be read and understood by a maintainer in fully, and that is very time-consuming if changes are not organized in a readable fashion.

**Lakshya Goel** · 2025-01-26 17:28 UTC

(replying to Tim Abbott)
> I don't think it could possibly help solve the core problem that a well-constructed PR branch solves

I completely understand and agree with your perspective, a well-constructed and organized PR is undoubtedly critical for maintaining the quality of the codebase.

**Lakshya Goel** · 2025-01-26 17:29 UTC

(replying to Tim Abbott)
> I've not tried CodeRabbit

But still I believe CodeRabbit can be a valuable tool in supporting our review process. It’s not meant to replace the thorough judgment of a maintainer but rather to complement it. Along with reviewing the PRs (potential issues, inconsistencies, or even adherence to style guidelines), it also summarize the changes and make some flowcharts as well for the changes.

**Lakshya Goel** · 2025-01-26 17:29 UTC

Moreover the thing is  it's free for open-source repos, so we may try it for with no cost. What if we give it a try and see whether it can make a meaningful difference in managing our reviews?

Looking forward to hearing your thoughts!

**Apoorva Pendse** · 2025-01-26 17:47 UTC

Looks interesting. I guess NextUI uses it.

**Apoorva Pendse** · 2025-01-26 17:47 UTC

[Yup](https://github.com/heroui-inc/heroui#:~:text=last%20month-,.coderabbit.yaml,-feat%3A%20new%20gitflow)

**Lakshya Goel** · 2025-01-26 17:57 UTC

Yes, Also Palisadoes Foundation, talawa uses the same [see](https://github.com/PalisadoesFoundation/talawa-admin/pull/3433)

**Greg Price** · 2025-01-26 22:31 UTC

I looked at a few PRs where CodeRabbit had commented in those two repos. It sure does write a lot of text.

I'm not sure that text is helpful, though. In particular, I saw a handful of review comments it made, all of them nits... and all of them were ignored by the authors and maintainers, who merged the PRs without making any of the suggested changes. Maybe some of the suggestions were good, I don't know, but it didn't seem like the people working on those projects were convinced.

**Greg Price** · 2025-01-26 22:34 UTC

I think one ingredient that would help in making a case this can be useful would be to see a couple of PRs where it seemed to actually improve things.

**Greg Price** · 2025-01-26 22:42 UTC

I do think there's potential for an AI to give a useful first code review on PRs from new contributors. There's a lot of kinds of comments we frequently make that might be in range for an AI at this point. I'd be a little surprised if anyone's quite gotten that into a working product yet, but it'd be interesting to know if someone has.

**Greg Price** · 2025-01-26 22:52 UTC

On the other hand I doubt we'd find value in the part where it writes a long summary of what's in the PR. The reviewer is going to be reading the actual PR anyway. And we can't trust a summary like that — it's going to very frequently get some things wrong — so it's not clear how we'd make use of it short of fact-checking it all, which sounds like a lot of work.

**Apoorva Pendse** · 2025-01-27 01:10 UTC

It does give some useful suggestions.
See [this](https://github.com/heroui-inc/heroui/pull/4653#discussion_r1929694615) for example.

I agree that initial summary is just too much text.

**Notification Bot** · 2025-01-27 13:46 UTC

15 messages were moved here from #**git help>squash-merges** by @Apoorva Pendse.


## updating PR

*2025-01-24 to 2025-01-25 · 5 messages · [open in Zulip](https://chat.zulip.org/#narrow/channel/44-git-help/topic/updating.20PR/with/2060308)*

**Arya Singh** · 2025-01-24 21:58 UTC

Hi Everyone

https://github.com/zulip/zulip-flutter/pull/1230

This is my PR, I am having trouble passing the ci as well as rebasing it.

tried running 
```sh
git push origin +feat/compose
```

still facing issues, if possible kindly help. thanks

**Notification Bot** · 2025-01-24 22:00 UTC

[A message](https://chat.zulip.org/#narrow/channel/44-git-help/topic/updating.20PR/near/2060308) was moved here from #**git help>pull request** by @Greg Price.

**Greg Price** · 2025-01-24 22:01 UTC

What are you seeing, and how does it differ from what you expect?

**Apoorva Pendse** · 2025-01-25 02:43 UTC

After reviewing your comments on the PR, 
I believe going through how git rebase works might be a good investment for you.

**Aman (whilstsomebody)** · 2025-01-25 04:49 UTC

@Arya Singh , Also consider reading the git guide. If you still face problems, feel free to reach us.


## rebase issue

*2025-02-06 to 2025-02-06 · 11 messages · [open in Zulip](https://chat.zulip.org/#narrow/channel/44-git-help/topic/rebase.20issue/with/2081008)*

**Saini Abhishek** · 2025-02-06 12:15 UTC

Hello, I tried rebasing my current working branch from the main, but it seems like it is rebasing from the forked branch. How can I rebase from the upstream?
Thanks

**Aman (whilstsomebody)** · 2025-02-06 12:18 UTC

git fetch upstream
git rebase upstream/main

**Aman (whilstsomebody)** · 2025-02-06 12:18 UTC

set the upstream to the repo of the organizaton.

**Aman (whilstsomebody)** · 2025-02-06 12:19 UTC

fetch command should be ran in the main branch

**Saini Abhishek** · 2025-02-06 12:20 UTC

thanks for the help
git remote add upstream <organization_repo_url>

will this command set the upstream?

**Aman (whilstsomebody)** · 2025-02-06 12:20 UTC

yupz

**Aman (whilstsomebody)** · 2025-02-06 12:21 UTC

Use git remote -v to check if upstream is already set.

**Saini Abhishek** · 2025-02-06 12:29 UTC

okay

**Saini Abhishek** · 2025-02-06 12:31 UTC

It worked. Thanks

**Aman (whilstsomebody)** · 2025-02-06 12:31 UTC

If you have followed the documentation properly, then youo must have set it already.

**Saini Abhishek** · 2025-02-06 12:31 UTC

yeah, the upstream was already set. The main issue was arising when I was rebasing it.


## ✔ commit history for PR

*2025-02-10 to 2025-02-11 · 8 messages · [open in Zulip](https://chat.zulip.org/#narrow/channel/44-git-help/topic/.E2.9C.94.20commit.20history.20for.20PR/with/2084296)*

**Brynly Aneirin** · 2025-02-10 07:18 UTC

Hi, so I'm working on pull request [#F1017](https://github.com/zulip/zulip-flutter/pull/1017) focused on making the dialogs platform specific. A new  type of dialog has been introduced with the addition of the function `showSuggestedDialogAction` since I began work on the PR.  Should I adapt this new function in a seperate commit? And should the new tests I've written go into their own commit, with all tests in one commit?
Lastly, I'm confused as to how to rebase onto these external changes whilst keeping a clean commit history.

Thanks.

**Maneesh Shukla** · 2025-02-10 11:02 UTC

For syncing external changes, you should:
- git switch main
- git fetch upstream
- git rebase upstream/main
- git push origin main

Then, checkout to your feature branch:
- git switch feature-branch
- git rebase upstream/main  (resolve the conflicts that arise)
- git push origin feature-branch --force

**Maneesh Shukla** · 2025-02-10 11:03 UTC

You should add tests in the same commit as the new code they are testing. There is no need to write tests in a separate commit.

**Greg Price** · 2025-02-10 20:47 UTC

Handling the new function could go in either a separate commit or the same one. If you're unsure, try making it a separate commit — it's generally easier to squash commits later on than to split them.

**Greg Price** · 2025-02-10 20:50 UTC

The steps @Maneesh Shukla gave are good except I would skip the first half, about main. It's not necessary to update the main branch of your fork repo; I don't think I've pushed to mine in years.

**Maneesh Shukla** · 2025-02-10 20:54 UTC

Thanks, @Greg Price, for this info, as every time I fetch some changes, I rebase my main branch first, then rebase my feature branch. :smiling_face_with_tear:

**Brynly Aneirin** · 2025-02-10 22:09 UTC

Alright thanks both of you much appreciated

**Notification Bot** · 2025-02-11 01:00 UTC

@Brynly Aneirin has marked this topic as resolved.


## granularity of commits

*2025-02-10 to 2025-02-10 · 4 messages · [open in Zulip](https://chat.zulip.org/#narrow/channel/44-git-help/topic/granularity.20of.20commits/with/2084458)*

**Chinmay Ajith** · 2025-02-10 12:17 UTC

I am working on #F800 and I have made changes to the following files, all related to managing the names of archived channels.
- `compose_box.dart`- shows the "no permission" error banner if the stream is archived.
- `inbox.dart` - append " (archived)" to the end of the stream name
- `message_list.dart` - append " (archived)" to the end of the stream name
- `subscription_list.dart` - filter out the archived channels from the list
and their related tests. 

What would be the apt commit message for these changes? I went through the commit history of each of these files and still wasn't able to figure it out. My doubt is should each of these files be committed with a single message like 
`archived_channels: Add archived channel label and update related components`

or should each file have a separate commit according to the widgets like `compose: ...` or `inbox: ...` etc.

**Apoorva Pendse** · 2025-02-10 12:24 UTC

>Never mix multiple changes together in a single commit, but it’s great to include several related changes, each in their own commit, in a single pull request

 [1](https://zulip.readthedocs.io/en/latest/contributing/commit-discipline.html#write-a-clean-commit-history)

**Greg Price** · 2025-02-10 20:53 UTC

If some of those changes involve any interesting logic of their own (distinct from what the others are doing), it'd be good to make them separate commits.

For a recent fairly complex example, see #F1297 by @Zixuan James Li implementing "general chat".

**Notification Bot** · 2025-02-10 21:28 UTC

3 messages were moved here from #**git help>commit message** by @Greg Price.


## commit message

*2025-02-10 to 2025-02-10 · 1 messages · [open in Zulip](https://chat.zulip.org/#narrow/channel/44-git-help/topic/commit.20message/with/2085028)*

**Notification Bot** · 2025-02-10 21:28 UTC

3 messages were moved from this topic to #**git help>granularity of commits** by @Greg Price.


## Zulip CI workflow run failed

*2025-03-23 to 2025-03-24 · 5 messages · [open in Zulip](https://chat.zulip.org/#narrow/channel/44-git-help/topic/Zulip.20CI.20workflow.20run.20failed/with/2132935)*

**Sagar Gupta** · 2025-03-23 18:23 UTC

I was creating a PR but its failed zulip ci workflow. Its my first ever PR so I am not sure what went wrong or how to solve it. Can anyone guide me to materials answering this issue or tell me how to tackle it? I already went through git-guide - https://zulip.readthedocs.io/en/latest/git/pull-requests.html and this doc -  https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request-from-a-fork . (As embedded links doesn't seem to work for me, so i am putting full url)
[image.png](https://chat.zulip.org/user_uploads/2/2d/lEKVfiXIAUt359U4HohGCDjs/image.png)

**Sagar Gupta** · 2025-03-24 02:55 UTC

Just bumping it again as it has been some time since I asked this. @Harsh Bansal or @Apoorva Pendse, do you happen to know what went wrong here?

**Prakhar Pratyush** · 2025-03-24 03:30 UTC

PR link ?

**Sagar Gupta** · 2025-03-24 04:24 UTC

https://github.com/zulip/zulip/pull/34134

**Prakhar Pratyush** · 2025-03-24 04:28 UTC

You can click on the individual "Jobs" in the left sidebar to understand the failures.
* Backend test and Capitalization of string is failing.


## TROUBLES WITH SSH

*2025-04-07 to 2025-04-07 · 4 messages · [open in Zulip](https://chat.zulip.org/#narrow/channel/44-git-help/topic/TROUBLES.20WITH.20SSH/with/2147528)*

**Elena Molero** · 2025-04-07 18:09 UTC

Hi, I am trying to fork the repo but I get an error, I think it is because of the part of the ssh agent. I have tried also with github desktop. Could you help me? 
[image.png](https://chat.zulip.org/user_uploads/2/72/IpxxKkmGocitBHiuy2rFvT9g/image.png)

**Apoorva Pendse** · 2025-04-07 18:16 UTC

Have you added your public key at https://github.com/settings/keys?

**Apoorva Pendse** · 2025-04-07 18:19 UTC

Also, it is recommended to setup Zulip on the WSL filesystem.

**Apoorva Pendse** · 2025-04-07 18:21 UTC

See [this guide](https://zulip.readthedocs.io/en/latest/development/setup-recommended.html#step-0-set-up-git-github) for more info.


## commit workflow

*2025-09-30 to 2025-09-30 · 2 messages · [open in Zulip](https://chat.zulip.org/#narrow/channel/44-git-help/topic/commit.20workflow/with/2268116)*

**MJ3340** · 2025-09-30 09:16 UTC

Hello Everyone this is Mritunjay Tiwari, I have recently started contributing to zulip-flutter and I am bit confused with the way flutter deal with commit and what it consider a "clean commit history". It would be very helpful if someone could explain. I have understood rebasing of main not merging. But I am not able to get context of clean commit history. Here is the pull request link: #F1879

**Karl Stolley** · 2025-09-30 11:21 UTC

Have you read the Zulip [Git guide](https://zulip.readthedocs.io/en/latest/git/index.html)? It includes a lot of useful guidance, including how to [tidy your commit history](https://zulip.readthedocs.io/en/latest/git/using.html#examine-and-tidy-your-commit-history).


## ✔ single pr closes multiple issue description type

*2025-11-01 to 2025-11-01 · 8 messages · [open in Zulip](https://chat.zulip.org/#narrow/channel/44-git-help/topic/.E2.9C.94.20single.20pr.20closes.20multiple.20issue.20description.20type/with/2289849)*

**MJ3340** · 2025-11-01 07:19 UTC

Is this the correct way in zulip commit style to link multiple issue to close in a commit message of a PR?

> home: Add label to bottom navbar icons Fixes #1857. Fixes #1960.

**Prakhar Pratyush** · 2025-11-01 07:41 UTC

If two issues are open for the same thing, we close one of them as duplicate.

**Prakhar Pratyush** · 2025-11-01 07:41 UTC

#1857 is already closed; 1960 too.

I guess those were just random numbers as an example.

**MJ3340** · 2025-11-01 07:47 UTC

(replying to Prakhar Pratyush)
> #1857 is already closed; 1960 too. I guess those were just random numbers as an example.

These are the actual issue links for reference!

> home: Add label to bottom navbar icons Fixes #F1857. Fixes #F1960.

**MJ3340** · 2025-11-01 07:49 UTC

Also those are 2 separate issues (maybe separated to organize them in some way i.e the semantics one), but solving one solves other indirectly.

**Prakhar Pratyush** · 2025-11-01 07:56 UTC

Yeah, that's fine.

**MJ3340** · 2025-11-01 07:57 UTC

(replying to Prakhar Pratyush)
> Yeah, that's fine.

Thanks for clarifying.

**Notification Bot** · 2025-11-01 07:57 UTC

@Mritunjay Tiwari has marked this topic as resolved.


## having issue with recent commit in zulip-flutter

*2026-01-16 to 2026-01-16 · 2 messages · [open in Zulip](https://chat.zulip.org/#narrow/channel/44-git-help/topic/having.20issue.20with.20recent.20commit.20in.20zulip-flutter/with/2354697)*

**Ashutosh Khadse** · 2026-01-16 04:47 UTC

@Greg Price  You can see that the branch is up-to-date and not changed or committed ahead, but the CI is failing. I do not understand that  
[Screenshot 2026-01-16 at 10.13.22 AM.png](https://chat.zulip.org/user_uploads/2/c4/fJlZhNY-CgM9lITyWkf1vpkJ/Screenshot-2026-01-16-at-10.13.22AM.png)
[Screenshot 2026-01-16 at 10.12.50 AM.png](https://chat.zulip.org/user_uploads/2/d3/AHh2FAU3zDTnS5vlIZEYEbEW/Screenshot-2026-01-16-at-10.12.50AM.png)

I also reran the CI

**Ashutosh Khadse** · 2026-01-16 05:35 UTC

Also I am getting this 
Analyzing zulip-flutter...                                              

warning • The annotation 'override' can only be used on fields, getters,
       methods, or setters • lib/api/model/submessage.dart:266:4 •
       invalid_annotation_target
warning • The annotation 'override' can only be used on fields, getters,
       methods, or setters • lib/api/model/submessage.dart:287:4 •
       invalid_annotation_target
warning • The annotation 'override' can only be used on fields, getters,
       methods, or setters • lib/api/model/submessage.dart:313:4 •
       invalid_annotation_target

3 issues found. (ran in 7.6s)

But I checked there are no changes in the main and this main submessage.dart file


## Doubt regarding #F2119

*2026-02-08 to 2026-02-08 · 3 messages · [open in Zulip](https://chat.zulip.org/#narrow/channel/44-git-help/topic/Doubt.20regarding.20.23F2119/with/2373506)*

**Ruhaan S** · 2026-02-08 18:37 UTC

@Rajesh Malviya 
https://github.com/zulip/zulip-flutter/pull/2119/changes/160589d91aa85a0f3f63483aee4e8878624f8daa#r2779595933
Just to clarify: When splitting the commits, I only keep code changes related to UserMention widget renaming in the second nfc commit, right? So changing the type of parameter from UserMentionNode to MentionNode in the widget will still happen in the first commit, right?

**Rajesh Malviya** · 2026-02-08 18:39 UTC

Correct.

**Rajesh Malviya** · 2026-02-08 18:45 UTC

Also sorry for not being clear in that comment, what I meant was that if you have question on regarding how to split those commits using `git`, you should ask that here. (The above question probably belongs in that github thread or in #**mobile-dev-help** :slight_smile:.)


## long commit summary

*2026-02-15 to 2026-02-15 · 4 messages · [open in Zulip](https://chat.zulip.org/#narrow/channel/44-git-help/topic/long.20commit.20summary/with/2380793)*

**Apoorva Pendse** · 2026-02-15 13:39 UTC

88c326c27f7c8709c50a806cc3a4276ed3e21eaf has an absurdly long commit summary.
This was probably an accident.
```
58d43d1608 apps: Prefer Intel macOS download when amd64 architecture is detected
88c326c27f apps: Prevent download page flicker during initialization Hide the apps download hero content until all dynamic state is computed, then reveal it o
nce update_page() completes. This avoids briefly showing incorrect or partially-initialized download links during page load
236868b971 help: Fix typo in image preview settings documentation.
```

I’m not sure if there’s a simple way to avoid this, given that we don’t run `gitlint` in CI for other pragmatic reasons.

**Apoorva Pendse** · 2026-02-15 13:42 UTC

The weird part is GH UI displays the commit  as if it does have the extra newline between the summary and the description.

**Tim Abbott** · 2026-02-15 16:38 UTC

Yeah, it's a GitHub bug that it doesn't display these correctly.

**Tim Abbott** · 2026-02-15 16:38 UTC

I noticed this one a couple seconds after merging and didn't think it worth a force-push.

