# #tools

> Making Zulip easier & more robust for development + deployment

Exported from https://chat.zulip.org on 2026-10-19: 3,169 messages in 113 topics.

## intro

*2016-08-01 to 2018-03-30 · 5 messages · [open in Zulip](https://chat.zulip.org/#narrow/channel/18-tools/topic/intro/with/10039)*

**Steve Howell** · 2016-08-01 17:24 UTC

This is a good place to discuss Zulip issues that aren't directly related to creating new features for users, but instead allow us to make Zulip easier and more robust for development and deployment.  Examples:
* linters like mypy, pyflake, etc. and the home grown stuff we've built on top of it
* provisioning virtual environments
* troubleshooting test failures

**Tim Abbott** · 2016-08-01 17:26 UTC

My goal is for Zulip to have the best tools of basically any project, since they have such a huge impact on productivity.  I'm a huge fan of having tools that are fast, precise, and eliminate whole categories of problems

**Sumana Harihareswara** · 2016-08-01 17:27 UTC

@Tim Abbott I was just thinking during my morning jog today how much I appreciated your near-fanatical respect & reverence for this practice

**Rohitt Vashishtha** · 2018-03-30 20:57 UTC

Hey. I've use eslint to autofix JS a couple of times, and I'll just tell you what I did without actually encouraging that.

In 'tools/lint', find the line where we call eslint in a subprocess. Add the argument '--fix' to it. Now, run tools/lint and then remove that argument.

Note: use this only for changes where you notice that all of them are minor spacing issues or missing semicolon etc. Not for complex issues with formatting where there *might* be breaking changes. Also, carefully check that nothing unwanted was changed.

**Armaan Ahluwalia** · 2018-03-30 21:33 UTC

> In 'tools/lint', find the line where we call eslint in a subprocess. Add the argument '--fix' to it. Now, run tools/lint and then remove that argument.
Thanks @Rohitt Vashishtha  that worked well. :)


## html/css cross-checker

*2016-08-01 to 2016-08-02 · 5 messages · [open in Zulip](https://chat.zulip.org/#narrow/channel/18-tools/topic/html.2Fcss.20cross-checker/with/10049)*

**Steve Howell** · 2016-08-01 17:27 UTC

Hi folks, I am currently working on an HTML/CSS cross checker that basically makes sure that any CSS styles we define are likely to be rendered by one of our HTML templates.

**Steve Howell** · 2016-08-01 17:28 UTC

This is partly based on a home grown HTML parser in `tools/check-templates` that knows how to deal with Django and handlebars tags.  I'm cleaning up that code as we speak.

**Steve Howell** · 2016-08-01 20:15 UTC

#1511

**Steve Howell** · 2016-08-02 18:31 UTC

This gets one step closer to cross checking css/html:

```
$ ./tools/html-grep '.modal-body' label form divtemplates/zerver/invite_user.html 12
    div(.modal,hide)(#invite-user) form(.form-horizontal)(#invite_user_form) div(.modal-body) div(.control-group) label(.control-label)

templates/zerver/invite_user.html 24
    div(.modal,hide)(#invite-user) form(.form-horizontal)(#invite_user_form) div(.modal-body) div(.control-group) label(.control-label)

templates/zerver/stream_creation_prompt.html 13
    div(.modal,hide)(#stream-creation) form(.form-inline)(#stream_creation_form) div(.modal-body) div(#make-invite-only) label(.radio) span(.icon-vector-globe)

templates/zerver/stream_creation_prompt.html 18
    div(.modal,hide)(#stream-creation) form(.form-inline)(#stream_creation_form) div(.modal-body) div(#make-invite-only) label(.radio) span(.icon-vector-lock)

templates/zerver/stream_creation_prompt.html 24
    div(.modal,hide)(#stream-creation) form(.form-inline)(#stream_creation_form) div(.modal-body) div(#announce-new-stream) label(.checkbox)

templates/zerver/stream_creation_prompt.html 32
    div(.modal,hide)(#stream-creation) form(.form-inline)(#stream_creation_form) div(.modal-body) div(.control-group) label(.control-label) b
```

**Steve Howell** · 2016-08-02 18:31 UTC

(not pushed yet)


## provisioning issues

*2016-08-01 to 2016-08-01 · 15 messages · [open in Zulip](https://chat.zulip.org/#narrow/channel/18-tools/topic/provisioning.20issues/with/10119)*

**Sumana Harihareswara** · 2016-08-01 17:43 UTC

ok, will put some troubleshooting stuff here

**Sumana Harihareswara** · 2016-08-01 17:44 UTC

http://pastebin.com/QhXd4S4c

**Sumana Harihareswara** · 2016-08-01 17:45 UTC

current date: Mon Aug  1 13:45:00 EDT 2016

date that this vagrant step is stuck on: timestamped Aug 01 13:27:38

**Sumana Harihareswara** · 2016-08-01 17:46 UTC

Tim notes this is related to https://github.com/zulip/zulip/issues/1461

**Tim Abbott** · 2016-08-01 17:47 UTC

Oh, I bet your thing finished successfully but `ts` didn't quit properly

**Sumana Harihareswara** · 2016-08-01 17:48 UTC

Oh! Is it reasonably safe to control-C out?

**Tim Abbott** · 2016-08-01 17:56 UTC

yes

**Tim Abbott** · 2016-08-01 17:56 UTC

Actually basically all of our tools are safe to `ctrl-C` out and rerun them (this property is called being `idempotent`, and I think is super important for scripts because it also means you don't have to do anything crazy if there's an error)

**Sumana Harihareswara** · 2016-08-01 18:00 UTC

@Tim Abbott I know about idempotence -- I hadn't realized we are hard-core about our tools being idempotent. That is cheering!

I control-C'd out, re-ran it, and once more got stuck at
`Aug 01 13:58:52 ==> default: Using cached version of node_modules`

**Tim Abbott** · 2016-08-01 18:00 UTC

Did you rerun under `ts`?

**Tim Abbott** · 2016-08-01 18:00 UTC

`ts` isn't the best tool -- it often has this sort of hang-on-finish problem

**Sumana Harihareswara** · 2016-08-01 18:01 UTC

I did. If you want to suggest an alternative that gives more granular timing data than prepending `time`, I'm game

**Tim Abbott** · 2016-08-01 18:02 UTC

Really the output from one where it hangs is fine

**Tim Abbott** · 2016-08-01 18:02 UTC

0 time passes after that `npm` output line anyway

**Sumana Harihareswara** · 2016-08-01 18:03 UTC

yup. verified. Will put that in the issue @Tim Abbott


## issue labels

*2016-08-02 to 2016-08-02 · 2 messages · [open in Zulip](https://chat.zulip.org/#narrow/channel/18-tools/topic/issue.20labels/with/10636)*

**Tim Abbott** · 2016-08-02 22:10 UTC

@Steve Howell do you think we should add an issue label for tooling?

**Steve Howell** · 2016-08-02 22:17 UTC

Yeah, I think that makes sense.


## mypy unittest

*2016-08-03 to 2016-08-03 · 20 messages · [open in Zulip](https://chat.zulip.org/#narrow/channel/18-tools/topic/mypy.20unittest/with/10930)*

**Steve Howell** · 2016-08-03 17:52 UTC

I get the following errors from mypy when using unittest:

```
tools/test-tools:6: error: Module has no attribute 'TestLoader'
tools/test-tools:24: error: "TextTestRunner" has no attribute "run"
```

**Tim Abbott** · 2016-08-03 17:53 UTC

This could be because of an issue with the stubs for `unittest`

**Tim Abbott** · 2016-08-03 17:54 UTC

The stubs are here:
`/srv/zulip-py3-venv/lib/mypy/typeshed/stdlib/2.7/unittest.pyi`

**Tim Abbott** · 2016-08-03 17:55 UTC

And do look distinctly unfinished

**Steve Howell** · 2016-08-03 17:55 UTC

Should I just `# type: ignore`it for now?

**Tim Abbott** · 2016-08-03 17:55 UTC

You should `type: ignore` for now

**Tim Abbott** · 2016-08-03 17:56 UTC

I'd also encourage reporting an issue in https://github.com/python/typeshed/issues so that upstream knows this stuff is broken

**Tim Abbott** · 2016-08-03 17:56 UTC

So that it'll actually get fixed eventually

**Tim Abbott** · 2016-08-03 17:56 UTC

Usually we keep track of these by writing it as `# type: ignore # https://github.com/python/typeshed/issues/123` to make it easy to keep track of the issue

**Steve Howell** · 2016-08-03 17:56 UTC

I'm building all the boilerplate for running tests on `tools/lib`.  About to submit a PR.  For now I'm using `unittest`, but we might eventually want to use one of the more modern tests runners for non-Django stuff.

**Steve Howell** · 2016-08-03 17:57 UTC

Do you have any inside info on whether they already know about this issue?

**Tim Abbott** · 2016-08-03 17:58 UTC

They do all their work in the public bug tracker

**Tim Abbott** · 2016-08-03 17:58 UTC

So I'd guess they don't, since I don't see it there

**Steve Howell** · 2016-08-03 17:58 UTC

https://github.com/python/typeshed/issues/372 is probably in the ballpark.

**Tim Abbott** · 2016-08-03 17:59 UTC

yeah you could consider posting on that issue

**Tim Abbott** · 2016-08-03 17:59 UTC

Stub issues are usually a quick fix if you know how to write stubs, so usually for things like this when I run into them I just submit a quick PR fixing the issue

**Steve Howell** · 2016-08-03 18:01 UTC

ok, I'm already in kind of a rabbit hole, so I prolly won't write a stub, but I'll post those two lines to the ticket and mention 372 in my ignore comment

**Tim Abbott** · 2016-08-03 18:01 UTC

yep, sounds good

**Tim Abbott** · 2016-08-03 18:01 UTC

You need the `type: ignore` anyway until they merge their stuff

**Tim Abbott** · 2016-08-03 18:01 UTC

So the typeshed stuff always is effectively a follow-on cleanup project when I do it


## testing tools/lib

*2016-08-03 to 2016-08-03 · 31 messages · [open in Zulip](https://chat.zulip.org/#narrow/channel/18-tools/topic/testing.20tools.2Flib/with/10951)*

**Steve Howell** · 2016-08-03 18:34 UTC

I just submitted https://github.com/zulip/zulip/pull/1534 for adding unit tests to tools/lib.  It includes two really tiny tests to make sure it works, but then it's all boilerplate.  I would love to move this code to something like `nose` if we could.

**Tim Abbott** · 2016-08-03 18:34 UTC

yay

**Tim Abbott** · 2016-08-03 18:34 UTC

what are the things you want from `nose` that aren't present already?

**Tim Abbott** · 2016-08-03 18:35 UTC

Also, what are your thoughts on whether we'll want to integrate this with the Django `test-backend` so we can run just e.g. `test-backend tools`

**Tim Abbott** · 2016-08-03 18:35 UTC

Or whether we'll want this to be its own line item in e.g. `tools/test-all`

**Steve Howell** · 2016-08-03 18:36 UTC

mostly better discovery...I'm not advocating for `nose` specifically...this is more of a query to others who might want to "modernize" away from unittest, if even only to unittest2

**Steve Howell** · 2016-08-03 18:38 UTC

Reasons to integrate tightly with test-backend: don't reinvent wheels on making output nicer, getting coverage reports

Reason not to integrate: SO much faster!

I think being able to run tests quickly trumps all the other concerns, so I'd have it as its own line item in `tools/test-all`

**Tim Abbott** · 2016-08-03 18:38 UTC

`test-backend` startup actually we can make 3x faster with a fairly small change

**Tim Abbott** · 2016-08-03 18:39 UTC

I have notes on how to do this in an open issue

**Tim Abbott** · 2016-08-03 18:39 UTC

basically the problem is it shells out to a new Django process twice

**Tim Abbott** · 2016-08-03 18:39 UTC

And Django has a slow startup to import all its stuff

**Steve Howell** · 2016-08-03 18:39 UTC

Yeah, I guess one more reason to keep things separate it's rare that you're working on both at the same time.

**Tim Abbott** · 2016-08-03 18:40 UTC

yeah

**Steve Howell** · 2016-08-03 18:40 UTC

I don't like the way `unittest` formats its test output, but that takes about two seconds to get used to if you're working on the `tools/lib` code.  I haven't tried to get a coverage report yet, but I can't imagine that's an insurmountable task.

**Tim Abbott** · 2016-08-03 18:41 UTC

Coverage data is super easy to produce

**Tim Abbott** · 2016-08-03 18:41 UTC

The only interesting bit will be merging it with the `test-backend` one so that we get a single overall coverage report

**Tim Abbott** · 2016-08-03 18:41 UTC

Also probably a standard tool just does it though

**Steve Howell** · 2016-08-03 18:42 UTC

`test-tools` runs in 300ms real time on my slow laptop...that makes me very happy (granted there are only two tests running so far)

**Steve Howell** · 2016-08-03 18:43 UTC

The codebases are pretty disjoint; I'm not sure we'd even want it all in the same coverage report, much less need it.

**Tim Abbott** · 2016-08-03 18:43 UTC

Well, with things like `coveralls`, it's kinda annoying to have more than one :)

**Steve Howell** · 2016-08-03 18:43 UTC

Ha, I didn't think of that.

**Tim Abbott** · 2016-08-03 18:43 UTC

arguably we should ditch coveralls as a mediocre tool, but it is nice to have something filling that role

**Tim Abbott** · 2016-08-03 18:43 UTC

and I'm not aware of credible alternatives

**Steve Howell** · 2016-08-03 18:45 UTC

Yeah, I've never done work to build coverage systems, I've only used them, so I don't have much to offer there.

**Steve Howell** · 2016-08-03 18:45 UTC

s/build/integrate/

**Steve Howell** · 2016-08-03 18:48 UTC

So my #1 concern is getting on to writing the actual unit tests, haha.  This was a good discussion on how to run them, but I think for now we can probably live with `unittest`.  If somebody shows interest in modernizing them or integrating them better with our backend tests, I'm all for it.  I'd love to keep the loadup time under a second, but that's not a hard constraint.

**Tim Abbott** · 2016-08-03 18:48 UTC

agreed

**Tim Abbott** · 2016-08-03 18:48 UTC

I'd love to get the loadup time for all our tests under 1s, it has a huge impact on iteration speed :)

**Steve Howell** · 2016-08-03 18:48 UTC

absolutely

**Steve Howell** · 2016-08-03 18:51 UTC

Sorry, I only now just read your comments on the ticket.  Getting this into Travis is definitely a big deal.  I think for the bare minimum concern--make sure tests don't fail--that will be ready when I submit the final draft of the PR (basically one line of code).  Getting more advanced Travis integration (coverage) will be more of a challenge.

**Tim Abbott** · 2016-08-03 19:03 UTC

yep makes sense


## testing functions that read files

*2016-08-03 to 2016-08-04 · 4 messages · [open in Zulip](https://chat.zulip.org/#narrow/channel/18-tools/topic/testing.20functions.20that.20read.20files/with/11118)*

**Steve Howell** · 2016-08-03 23:34 UTC

What's our preferred pattern for testing functions that open files?  I can either write a temp file, write to var, use some third party mock, or make my own lightweight stub.

**Steve Howell** · 2016-08-03 23:35 UTC

(For the function I'm testing, I'm confident in its ability to read files, so I just want to get past the first line of code that does `text = open(fn).read()`.)

**Steve Howell** · 2016-08-03 23:37 UTC

We use StringIO as a stand in for file pointers, but that doesn't seem to address my use case.

**Steve Howell** · 2016-08-04 00:04 UTC

I worked around this mostly, so it's not urgent.  (I still need to figure out something to get line coverage.)


## test-js-with-node

*2016-08-04 to 2022-01-06 · 55 messages · [open in Zulip](https://chat.zulip.org/#narrow/channel/18-tools/topic/test-js-with-node/with/11141)*

**Steve Howell** · 2016-08-04 16:17 UTC

@Tomasz Kolek @Tim Abbott I think we may have regressed test-js-with-node to not have the correct exit code on failure.  We probably don't need a prominent failure message, as the failures are usually obvious, or maybe there's a shell way to echo/exit-1 idiomatically, and we can keep the message.

To repro:

`$ ./tools/test-js-with-node server_events.js && echo 'what?'`

**Tim Abbott** · 2016-08-04 16:20 UTC

hmm, yeah, basically we need to do `|| failed=1` and check that variable

**Steve Howell** · 2016-08-04 16:20 UTC

My vote would be to simplify it.

**Tim Abbott** · 2016-08-04 16:20 UTC

or `|| (echo error; exit 1)`

**Tim Abbott** · 2016-08-04 16:21 UTC

anyway I'm fine with any solution but we should fix quickly, since I bet this means CI won't catch Node failures

**Steve Howell** · 2016-08-04 16:22 UTC

agreed

**Steve Howell** · 2016-08-04 16:22 UTC

or just be careful not to merge anything that's not clearly non-js-related

**Steve Howell** · 2016-08-04 16:23 UTC

nm, pull requests will still come in

**Tim Abbott** · 2016-08-04 16:23 UTC

yeah

**Tim Abbott** · 2016-08-04 16:23 UTC

I can manually rerun tests for a while, but it's a pain

**Tim Abbott** · 2016-08-04 16:23 UTC

We could revert, but this seems like something one could fix forward quickly

**Steve Howell** · 2016-08-04 16:24 UTC

I vote revert due to time zone differences.

**Steve Howell** · 2016-08-04 16:25 UTC

Then Tomasz can weigh in and make the fix.

**Tim Abbott** · 2016-08-04 16:27 UTC

Eh how about I just merge changing the error echoes to `(echo "FAIL - Test(s) failed"; exit 1)`

**Tim Abbott** · 2016-08-04 16:27 UTC

Just verified that fixes the problem

**Tim Abbott** · 2016-08-04 16:27 UTC

then we can simplify later

**Tim Abbott** · 2016-08-04 16:28 UTC

Hmm, our istanbul config could be improved.  We install it at `node_modules/.bin/istanbul`, but it's not in PATH

**Tim Abbott** · 2016-08-04 16:29 UTC

OK merged a fix

**Tim Abbott** · 2016-08-04 16:30 UTC

It's probably still worth someone working on cleaning it up, since the code is now a bit verbose and duplicated

**Steve Howell** · 2016-08-04 16:32 UTC

was there an issue on this originally, or just a pr?

**Tim Abbott** · 2016-08-04 16:34 UTC

an issue and a PR

**Steve Howell** · 2016-08-04 16:34 UTC

huh, your path might not be typical

```
(zulip-venv)vagrant@vagrant-ubuntu-trusty-64:/srv/zulip$ which istanbul
/usr/bin/istanbul
```

**Tim Abbott** · 2016-08-04 16:34 UTC

#1489

**Tim Abbott** · 2016-08-04 16:34 UTC

So the story is that we install it via `npm install` in `package.json`

**Tim Abbott** · 2016-08-04 16:35 UTC

We also seem to document `sudo npm install -g istanbul`, which I think puts it in `/usr/bin`, but it's installed via `packages.json` on everyone's system

**Tim Abbott** · 2016-08-04 16:35 UTC

I bet you have it in both places, and we should remove the docs telling people to install it via `npm install -g istanbul`

**Steve Howell** · 2016-08-04 16:36 UTC

yep, I do

**Steve Howell** · 2016-08-04 16:38 UTC

I reopened #1489.

**Steve Howell** · 2016-08-04 16:39 UTC

The istanbul thing should be a new ticket, correct?

**Tim Abbott** · 2016-08-04 16:39 UTC

well, I merged the PATH fix, but you mean the docs thing?  I'll just fix that now too

**Steve Howell** · 2016-08-04 16:39 UTC

ok, I reopened #1489 to clean up the code

**Tim Abbott** · 2016-08-04 16:39 UTC

Seems like a small enough problem that it's faster to fix than write the ticket

**Tim Abbott** · 2016-08-04 16:39 UTC

sounds good re: the code cleanup

**Steve Howell** · 2016-08-04 16:39 UTC

fair enough

**Tim Abbott** · 2016-08-04 16:40 UTC

And documentation fix tickets sometimes end up lingering :)

**Steve Howell** · 2016-08-04 16:40 UTC

haha

**Steve Howell** · 2016-08-04 16:40 UTC

aside: For doc changes that are purely for development (not production setup), I think we just push those aggressively to get eyeballs on them and avoid confusion.

**Tim Abbott** · 2016-08-04 16:41 UTC

yeah

**Tomasz Kolek** · 2016-08-08 20:55 UTC

@Tim Abbott  @Steve Howell Guys, sorry for the delay. I'd got a little break.
I created PR with cleanup - please take a look
[#1569](https://github.com/zulip/zulip/pull/1569)

**Steve Howell** · 2016-08-08 21:01 UTC

I added a few notes.  Seems like an improvement to me, thanks for following up on this.

**Yash RE** · 2022-01-03 15:25 UTC

I've been working on `tools: Run node_tests with coverage in parallel through node.js.` (#20280) and I'm kinda stuck and confused. What I'm trying to do is fix the regression described in the edit for [#20280 (comment)](https://github.com/zulip/zulip/pull/20280#issuecomment-979284913).
One thing that confuses me is [that this CI failure](https://github.com/zulip/zulip/runs/4691762729?check_suite_focus=true) is correct, but it's not what I see when running `./tools/test-js-with-node --coverage` locally.

I'm slightly suspicious that this might be a nyc thing, but I tried to minimally reproduce with this repl https://replit.com/join/njuvccqnxi-internetpersona, which replaces the test file runner with a number counter but I do not see the same bug and I'm not sure what's different...

**Tim Abbott** · 2022-01-03 20:19 UTC

@Steve Howell (showell) may be best equipped to help with this.

**Steve Howell** · 2022-01-05 16:50 UTC

I have had surprisingly little experience with the `--coverage` option for `test-js-with-node`, whether it was the original `istanbul` features or the more modern `nyc` usage.

**Steve Howell** · 2022-01-05 16:51 UTC

I tried at one point to understand how `nyc` aggregated results, but the documentation was a bit too opaque for me to grok in the time I had allotted myself.

**Steve Howell** · 2022-01-05 16:53 UTC

I do think we should avoid parallelization by default when running coverage until it's rock solid.

There a couple know annoyances with the `--coverage` option.  It seems to mess up strack traces.  And you can't control-C out of it.  Neither nuisance has never been severe enough to me to motivate me to try to fix them, so I am sorry I don't have more useful info to provide.

**Yash RE** · 2022-01-05 17:15 UTC

Well, one thing that would help me is if someone could validate that the whole `const has_exited = new Map();` is an appropriate way to do things. I do not have much experience with node.js `child_process`...

**Steve Howell** · 2022-01-05 17:33 UTC

I like the idea of moving all the parallelization code to node.

**Steve Howell** · 2022-01-05 17:36 UTC

I believe at some point I actually did the reverse--i.e. moved some test-runner logic from JS to Python--but it was mostly because I was more fluent in Python (and wasn't happy with the prior JS code).

**Tim Abbott** · 2022-01-05 21:06 UTC

Ultimately if we're going to spend serious investment on this, we probably want to just debug why `jest` is so slow and then migrate to that as a test runner.  https://github.com/zulip/zulip/pull/13374 is work towards that which we decided was too much of a performance regression at the time.

**Greg Price** · 2022-01-05 21:10 UTC

Speaking from our experience on zulip-mobile, Jest is great and I think y'all will be happy to have moved to it (after resolving the perf regression.)

**Greg Price** · 2022-01-05 21:12 UTC

Might be worth bumping https://github.com/facebook/jest/issues/9554 (which Anders filed based on that PR). Seems like it ought to be fixable in principle.

**Greg Price** · 2022-01-05 21:12 UTC

(and the maintainer was interested, but it evidently fell off his plate)

**Greg Price** · 2022-01-05 22:24 UTC

Speaking of Jest being great, one example that I happened to see today:

(replying to Anders Kaseorg)
> `console.log` works in the Node tests. Make sure you added it to the right file and that it’s before the failure. Note that if you’re running multiple tests, the output might be interleaved with other tests due to parallelism.

Jest solves this problem:
https://jestjs.io/blog/2016/09/01/jest-15#buffered-console-messages

**Steve Howell** · 2022-01-06 23:53 UTC

I just wanted to enumerate the known issues with the current test runner that have recently been discussed, to make sure I'm not missing anything:
* you get bad stack traces with `--coverage` option
* control-c doesn't work with `--coverage` option
* you can't parallelize with `--coverage`
* we haven't finalized our policy for console buffering with `--parallel`
* we don't seem to get a massive speedup when running `--parallel`

**Steve Howell** · 2022-01-06 23:57 UTC

see also #**automated testing>node tests parallel**


## snippet

*2016-08-06 to 2016-08-08 · 2 messages · [open in Zulip](https://chat.zulip.org/#narrow/channel/18-tools/topic/snippet/with/11551)*

**Steve Howell** · 2016-08-06 15:14 UTC

For tooling, we often need to identify a line of code .  Our primary use case is to exclude it from some overly zealous lint rule, but we may also have future tooling that hunts out things like jQuery adding a class tag.  I would like to propose a convention of `# snippet: snippet_identifier` for lines of code that we want to name for tools.  The `snippet_identifier` would have to be unique within the source file, and it should look like an identifier (alphas, underscore, no spaces, etc.).

**Tim Abbott** · 2016-08-08 17:47 UTC

Seems reasonable to me


## travis

*2016-08-09 to 2016-08-09 · 11 messages · [open in Zulip](https://chat.zulip.org/#narrow/channel/18-tools/topic/travis/with/11865)*

**Steve Howell** · 2016-08-09 16:30 UTC

I assume this is due to some migration prep:
"CRITICAL:root:Unsupported platform: Ubuntu precise"

**Steve Howell** · 2016-08-09 16:30 UTC

(my PR build failed just now)

**Tim Abbott** · 2016-08-09 16:32 UTC

No...

**Tim Abbott** · 2016-08-09 16:32 UTC

We in theory declare in travis CI that we want Trusty

**Tim Abbott** · 2016-08-09 16:32 UTC

I bet that's some Travis CI infrastructure problem

**Tim Abbott** · 2016-08-09 16:32 UTC

where some of their machines are tagged for the wrong cluster or something

**Steve Howell** · 2016-08-09 16:35 UTC

Ah, ok.

**Steve Howell** · 2016-08-09 16:35 UTC

I am about to update that PR fairly soon, anyway, so it's not a big issue for me.

**Tim Abbott** · 2016-08-09 16:35 UTC

Cool.  I wish Travis CI were a less flaky system

**Tim Abbott** · 2016-08-09 16:36 UTC

I spent all this time at Dropbox making the CI system not have all these nondeterministic failures that have nothing to do with the code being tested, but then back in the external world, the problems return ;)

**Steve Howell** · 2016-08-09 19:59 UTC

Heh, another error: "Error: Could not start Service[rabbitmq-server]"


## mypy

*2016-08-09 to 2017-01-25 · 124 messages · [open in Zulip](https://chat.zulip.org/#narrow/channel/18-tools/topic/mypy/with/11962)*

**Steve Howell** · 2016-08-09 19:18 UTC

So I was under the impression that you could pass a list of file names to `run-mypy`, but it seems very flaky at reporting errors when you do that.

**Tim Abbott** · 2016-08-09 19:20 UTC

if you pass a list of filenames, it only checks those files

**Tim Abbott** · 2016-08-09 19:20 UTC

So it won't catch consistency issues with other parts of the project

**Steve Howell** · 2016-08-09 19:26 UTC

It seems flakier than that--it seems to report different things in consecutive calls.  (I'm not 100% sure I'm not screwing up something else, though.)

**Tim Abbott** · 2016-08-09 19:28 UTC

I think it's pretty deterministic

**Tim Abbott** · 2016-08-09 19:28 UTC

But yeah, I've found the experience of running it on a single file to often miss things

**Steve Howell** · 2016-08-10 23:36 UTC

Ugh, this keeps happening to me during interactive rebases, when it's least convenient:

```
Using mypy from /srv/zulip-py3-venv/bin/mypy
zerver/lib/export.py: error: Duplicate module named 'zerver.lib.export'
```

**Tim Abbott** · 2016-08-10 23:37 UTC

interesting

**Tim Abbott** · 2016-08-10 23:37 UTC

Can you do a `find | grep export.py` ?

**Tim Abbott** · 2016-08-10 23:37 UTC

My guess is somehow there's a `export.pyc` leak or something

**Tim Abbott** · 2016-08-10 23:38 UTC

(actually, I have no idea why that would cause that outcome)

**Steve Howell** · 2016-08-10 23:38 UTC

```
$ find . | grep export.py
./zerver/lib/export.py
./zerver/lib/export.pyc
./zerver/management/commands/export.py
./zerver/management/commands/export.pyc
```

**Tim Abbott** · 2016-08-10 23:38 UTC

can you try removing the `.pyc` files and seeing if it fixes it?

**Steve Howell** · 2016-08-10 23:38 UTC

yeah, trying now...

**Steve Howell** · 2016-08-10 23:39 UTC

ha, that seemed to fix it, thx!

**Steve Howell** · 2016-08-10 23:39 UTC

Maybe we should have run-mypy aggressively remove .pyc files, huh?

**Tim Abbott** · 2016-08-10 23:40 UTC

no, I suspect there's some sort of mypy bug here; it shouldn't be parsing .pyc files regardless

**Steve Howell** · 2016-08-10 23:41 UTC

I'm just saying to work around the bug for now.  Although I guess that would be painful for the normal case.

**Tim Abbott** · 2016-08-10 23:41 UTC

right, it actually takes time to recompile them all

**Steve Howell** · 2016-08-10 23:41 UTC

I'm personally fine with the workaround, just worried about future folks.

**Tim Abbott** · 2016-08-10 23:42 UTC

@Reid Barton have you ever seen issues like this with mypy before?

**Tim Abbott** · 2016-08-10 23:42 UTC

mypy is a pretty fast-moving project, so ideally we'd just debug and get it fixed :)

**Steve Howell** · 2016-08-10 23:43 UTC

fair enough

**Steve Howell** · 2016-08-10 23:57 UTC

Huh, got it again, and this time removing .pyc files didn't help.

**Steve Howell** · 2016-08-11 00:01 UTC

And when I finish rebasing, mypy starts working again.  I wonder if mypy is sensitive to some artifact of rebasing.  I don't have a theory on why that would be.

**Tim Abbott** · 2016-08-11 00:02 UTC

That's quite strange -- it's not like we moved the files

**Tim Abbott** · 2016-08-11 00:02 UTC

Just to understand -- are you running `mypy` on each commit as you rebase, or e.g. running it in a loop on the side while doing the rebase?

**Steve Howell** · 2016-08-11 00:03 UTC

I could see it somehow being related to "export," i.e. mypy has a concept of exporting symbols or something.  But not rebase.

**Steve Howell** · 2016-08-11 00:03 UTC

I just rebase -i, choose "e" for edit, then manually run at the command line.

**Steve Howell** · 2016-08-11 00:04 UTC

If you want to try to repro, you can probably do something like rebase -i HEAD^^^^^^^^^^ on master and try to edit one of the export commits.

**Tim Abbott** · 2016-08-11 00:05 UTC

I'm a little busy right now to do that myself

**Steve Howell** · 2016-08-11 00:05 UTC

no worries

**Steve Howell** · 2016-08-11 00:06 UTC

Right now my theory is that this is somehow unique to "export" and git is just somehow a strange aggravating factor.

**Steve Howell** · 2016-08-11 00:10 UTC

/me considers just renaming the library to export_import.py

**Tim Abbott** · 2016-08-11 00:11 UTC

haha yeah do you think the problem is because we have two `export.py` files?

**Steve Howell** · 2016-08-11 00:13 UTC

yeah, could be, although it can't be the only place we have dup names, can it?  Maybe it's a good policy to avoid dup names, anyway, just for the minor productivity boost you get when trying to open a file in your editor.

**Steve Howell** · 2016-08-11 00:15 UTC

(I'm being slightly facetious, because I think it's actually useful to have parallel names in some cases.)

**Steve Howell** · 2016-08-11 00:17 UTC

also, interactive rebase is overrated anyway, (`git checkout HEAD^^^ && git checkout -b tmp` * 42) for the win

**Steve Howell** · 2016-08-11 00:19 UTC

(and now I'm being 95% facetious...but not 100%)

**Reid Barton** · 2016-08-11 02:32 UTC

Weird

**Steve Howell** · 2016-08-11 02:36 UTC

Indeed.

**Reid Barton** · 2016-08-11 02:39 UTC

Are you using mypy's incremental mode?

**Reid Barton** · 2016-08-11 02:40 UTC

Then this would possibly almost make sense

**Reid Barton** · 2016-08-11 02:40 UTC

Or maybe it's somehow an issue outside of mypy proper
like, zulip's mypy script has some find to produce the list of files and the order of that list could definitely affect the outcome

**Steve Howell** · 2016-08-11 02:42 UTC

https://github.com/zulip/zulip/blob/master/tools/run-mypy

**Reid Barton** · 2016-08-11 02:43 UTC

oh, the list of files even goes through a dict it looks like

**Reid Barton** · 2016-08-11 02:43 UTC

so the order could be sensitive to stuff

**Steve Howell** · 2016-08-11 02:45 UTC

yeah, it's probably worthwhile to make the list of file semi-deterministic...I am still grok-ing the script

**Reid Barton** · 2016-08-11 02:45 UTC

I've never noticed mypy behave nondeterministically when given the same ordered list of files, so I'm going to claim that probably the order of the list is changing and that's the issue, since it looks plausible

**Steve Howell** · 2016-08-11 02:46 UTC

It would make sense that being in a rebase would change the order of files that lister found.

**Steve Howell** · 2016-08-11 02:46 UTC

I mean, I think, I'm just guessing.

**Reid Barton** · 2016-08-11 02:47 UTC

Right, it also seems plausible that the order of the output of `lister.list_files` could depend on the order on disk of files in a directory and stuff

**Steve Howell** · 2016-08-11 02:49 UTC

yeah, which would definitely be perturbed by doing a rebase, I'm guessing

**Steve Howell** · 2016-08-11 02:50 UTC

I'm kind of at the end of my day, but tomorrow I'll look into making run-mypy more deterministic, at least in terms of sorting the files.

**Steve Howell** · 2016-08-11 02:51 UTC

Reid, what percentage chance do you think that the name "export" has some sort of subtle collision with mypy?  My estimate is about 10%.

**Reid Barton** · 2016-08-11 02:52 UTC

Yeah I think just sorting the file list before passing it to mypy is a good idea. Or if you remove all import cycles then mypy should probably be deterministic also :)

**Reid Barton** · 2016-08-11 02:53 UTC

Quite low, there aren't any interesting matches for export in either mypy or typeshed

**Steve Howell** · 2016-08-11 02:54 UTC

FWIW export.py doesn't have any circular dependency issues that I'm aware of.  It's purely a consumer to everything, except, well, um, the management command with the same module name.  (But to my original point, it doesn't do anything strange.)

**Reid Barton** · 2016-08-11 02:55 UTC

Even if it just indirectly imports a cycle that is involved in a cycle, that often causes problems

**Reid Barton** · 2016-08-11 02:55 UTC

er, a module that is involved in a cycle

**Steve Howell** · 2016-08-11 02:55 UTC

One thing that is fairly unique to `export.py` in the Zulip codebase is that I define custom types:

```
  30 # Custom mypy types follow:
  31 Record = Dict[str, Any]
  32 TableName = str
  33 TableData = Dict[TableName, List[Record]]
  34 Field = str
  35 Path = text_type
  36 Context = Dict[str, Any
```

**Reid Barton** · 2016-08-11 02:56 UTC

Oh, looking at the original error again, it is still kind of weird, hmm

**Reid Barton** · 2016-08-11 02:57 UTC

Could it be in the list of files twice?

**Steve Howell** · 2016-08-11 02:57 UTC

ha, yeah, like some strange lister bug, or some bug in the way we call lister?

**Reid Barton** · 2016-08-11 02:57 UTC

That would cause that error but I don't see yet why it would happen

**Reid Barton** · 2016-08-11 02:57 UTC

right

**Reid Barton** · 2016-08-11 02:58 UTC

or, like, does git store copies of the files involved in a rebase under `.git` somewhere

**Steve Howell** · 2016-08-11 02:58 UTC

Interesting, that seems like the most plausible explanation--we are actually feeding it duplicate files.  Looking at the code again...

**Steve Howell** · 2016-08-11 03:03 UTC

I am not totally convinced that files_dict['py'] doesn't have duplicates.

**Steve Howell** · 2016-08-11 03:06 UTC

What the heck is up with the first "not" here?

```
python_files = [fpath for fpath in files_dict['py']
                if not fpath.endswith('.py') or fpath + 'i' not in pyi_files]
```

**Steve Howell** · 2016-08-11 03:10 UTC

Huh, it's apparently related to our --scripts-only option.  I wish we just suffixed all of our Python files with `.py`.  I have had a bunch of broken builds due to not running `--scripts-only' on our `run-mypy` script.

**Reid Barton** · 2016-08-11 03:11 UTC

`use_shebang` makes the lister put things that look like python scripts into `files_dict['py']`?

**Steve Howell** · 2016-08-11 03:16 UTC

I think so.

**Steve Howell** · 2016-08-11 03:18 UTC

But my analysis could be a total red herring.  My circumstantial theory would be more plausible if we had a script named `export`, but we don't.  I should probably stop theorizing on this tonight and take a fresh look at it in the morning.

**Tim Abbott** · 2016-08-11 04:37 UTC

Yeah, the `--scripts-only` thing is kinda a mess; it's all a workaround for the fact that mypy only lets you have one "__main__" per invocation, which is totally something worth fixing.  We have to do `--scripts-only` only in CI because it's super slow.

**Steve Howell** · 2016-08-11 04:43 UTC

Ah, that makes sense.

**Steve Howell** · 2016-08-18 17:51 UTC

For contextmanagers, do we want to use `Generator[None, None, None]` still?  If so, what do the three Nones represent?

**Tim Abbott** · 2016-08-18 18:04 UTC

I think we don't need that anymore

**Tim Abbott** · 2016-08-18 18:05 UTC

I think it can now just be annotated as a function that returns an iterable

**Tim Abbott** · 2016-08-18 18:05 UTC

Those annotations are a relic from mypy as of January

**Steve Howell** · 2016-08-18 18:20 UTC

Ok, I couldn't find a good example of the new way.  I'll probably just use the None/None/None for now on the assumption we'll sweep these some day.  We might want a specific type that we create for "generators," even if it's really just an iterator from mypy's perspective.  (Just to make the "type" statements work as a form of documentation.)

**Tim Abbott** · 2016-08-18 18:27 UTC

Oh the new way is just `-> Iterable[str]` or whatever

**Steve Howell** · 2016-08-18 18:30 UTC

that makes sense for real generators; I'm talking about context managers

**Steve Howell** · 2016-08-18 18:30 UTC

not that context managers aren't "real"

**Steve Howell** · 2016-08-18 18:31 UTC

I misspoke a few messages back, I meant to say "context managers" instead of "generators."

**Tim Abbott** · 2016-08-18 18:33 UTC

oh I see

**Tim Abbott** · 2016-08-18 18:34 UTC

Yeah unfortunately I've forgotten what the three arguments to `Generator` are.  I bet it's in the PEP-484 spec though

**Tim Abbott** · 2016-08-18 18:34 UTC

https://www.python.org/dev/peps/pep-0484/#annotating-generator-functions-and-coroutines

**Steve Howell** · 2016-08-18 18:41 UTC

huh, that works for me

**Steve Howell** · 2016-08-18 18:42 UTC

huh, they do have a ContextManager mentioned in the PEP, apparently

**Steve Howell** · 2016-08-18 18:48 UTC

#1648 for the sweep

**Steve Howell** · 2016-09-11 15:31 UTC

@Tim Abbott Do we have a standard way to check for generic Django models in Django?

**Tim Abbott** · 2016-09-11 17:28 UTC

Not really; I bet there is some class like Manager deep in Django one can use, but it's possible one should just use Type (for a generic class, not a class instance) or Any for it.

**Steve Howell** · 2016-09-11 18:19 UTC

Is there a reason `test_upload.py` is still in the exclude list?

**Tim Abbott** · 2016-09-11 23:34 UTC

@Steve Howell probably not; the test files started out all in the exclude list because test files tend to do more questionable stuff, and we've been moving them off steadily.  Annotating them is super easy since 90% of the functions are `() -> None` as their type; the hard part is just dealing with the monkey-patching (or whatever) that tests do

**Steve Howell** · 2016-09-11 23:45 UTC

Cool.  I'm kind of done with mypy for today, but during Tuesday's testing sprint I'll see what low hanging fruit still remains there.  I asked about `test_upload.py` in particular, because it actually looks like it's 90% annotated.

**Tim Abbott** · 2016-09-11 23:47 UTC

interesting

**Steve Howell** · 2016-09-11 23:48 UTC

966375d74c5a5cc94260cc3c327c86a28e7ef423

**Tim Abbott** · 2016-09-11 23:51 UTC

cool, yeah, looks like I screwed up and didn't move it off the bad list :)

**Steve Howell** · 2016-09-11 23:53 UTC

One of these days we should probably have a linter sprint where all we do is sweep exclude lists, haha.  (Sweep for both excludes that are obsolete or that are easier to fix now.)

**Steve Howell** · 2016-09-12 00:51 UTC

@Tim Abbott I can't remember why I decided to use text_type instead of str for path-like variables, but it's proven to be painful.  Do you remember any of our prior discussions on this?  I'm about to re-submit a PR where I just make it str.

**Tim Abbott** · 2016-09-12 15:33 UTC

We're now done to just these things not in the big files (api/zulip/__init__.py, zerver/views/messages.py) missing annotations :)
```
tools/lib/template_parser.py: note: In function "tokenize":
tools/lib/template_parser.py:27: error: Function is missing a type annotation
tools/tests/test_template_parser.py: note: In member "_assert_validate_error" of class "ParserTest":
tools/tests/test_template_parser.py:19: error: Function is missing a type annotation
tools/tests/test_css_parser.py: note: In member "_assert_error" of class "ParserTestSadPath":
tools/tests/test_css_parser.py:121: error: Function is missing a type annotation
```

**Tim Abbott** · 2016-09-12 15:34 UTC

OK well I lied since I hadn't pushed yet, but we are now! :)

**Tim Abbott** · 2016-09-12 15:50 UTC

Alright just did `messages.py` :)

**Tim Abbott** · 2016-09-12 15:51 UTC

@Steve Howell I think this is the issue with `test_upload.py`
```
zerver/tests/test_upload.py: note: In member "test_rest_endpoint" of class "FileUploadTest":
zerver/tests/test_upload.py:51: error: Property "name" defined in "StringIO" is read-only
```

**Steve Howell** · 2016-09-12 15:54 UTC

Was that on my list?  I don't remember that one.

**Tim Abbott** · 2016-09-12 15:54 UTC

No, but you were asking me what the story was with `test_upload.py` being mostly annotated but not having mypy running on it

**Steve Howell** · 2016-09-12 15:55 UTC

Ah, got it.

**Tim Abbott** · 2016-09-12 15:55 UTC

OK having excluded `api/zulip/__init__.py`, we're now down to just these:
```
$ ./tools/run-mypy --disallow-untyped-defs 
tools/lib/template_parser.py: note: In function "tokenize":
tools/lib/template_parser.py:27: error: Function is missing a type annotation
tools/tests/test_template_parser.py: note: In member "_assert_validate_error" of class "ParserTest":
tools/tests/test_template_parser.py:19: error: Function is missing a type annotation
tools/tests/test_css_parser.py: note: In member "_assert_error" of class "ParserTestSadPath":
tools/tests/test_css_parser.py:121: error: Function is missing a type annotation
```

**Tim Abbott** · 2016-09-12 15:56 UTC

I guess I'll just try to do those right now :)

**Steve Howell** · 2016-09-12 15:56 UTC

@Gordon P. Hemsley and I were both in that code yesterday, but I merged his major change, which is to split out a new module, so, yeah, I'd just go for it.

**Steve Howell** · 2016-09-12 15:58 UTC

For the css parser there are a couple places we use `cast` in the tests to appease mypy.  (It actually makes the tests read a little more clearly as a side benefit.)

**Tim Abbott** · 2016-09-12 16:12 UTC

OK we're now at 100%, I'm testing https://github.com/timabbott/zulip/tree/enforce-mypy for moving it to enforcing

**Tim Abbott** · 2016-09-12 16:12 UTC

I think once we do that, we should probably kill the mypy/coveralls integration, right?

**Tim Abbott** · 2016-09-12 16:12 UTC

Since that will just sit at 100% and not be interesting at all

**Steve Howell** · 2016-09-12 16:13 UTC

seems sensible

**Sumana Harihareswara** · 2016-09-12 16:14 UTC

@Tim Abbott just to be clear, once you turn on this enforcement mechanism, there's no way that we could ever slip into coverage under 100%? then yes, but make sure you take a screenshot before you kill the integration, so we can bask and put it in blog posts and whatnot :)

**Tim Abbott** · 2016-09-12 16:15 UTC

well, someone could, but it would make Travis CI fail :)

**Tim Abbott** · 2016-09-20 05:56 UTC

@Eklavya Sharma thanks to Guido, the `tools/run-mypy --scripts-only` option is now super fast and takes 3 like seconds to run :)

**Tim Abbott** · 2016-09-20 05:57 UTC

(The new setup is a lot nicer than the hack we had to run it individually on all the scripts)

**Steve Howell** · 2017-01-25 01:12 UTC

I'm getting these errors on master.  Is there a way to hard-reset mypy?

~~~
(zulip-venv)vagrant@vagrant-base-trusty-amd64:/srv/zulip$ ./tools/run-mypy 
Using mypy from /srv/zulip-py3-venv/bin/mypy
zproject/local_settings.py:13: error: INTERNAL ERROR -- please report a bug at https://github.com/python/mypy/issues
zproject/local_settings.py:13: note: please use --show-traceback to print a traceback when reporting a bug

**Steve Howell** · 2017-01-25 01:16 UTC

`./tools/run-mypy --py3` works

**Tim Abbott** · 2017-01-25 03:47 UTC

`rm -rf var/mypy-cache` works.  I reported it upstream yesterday

**Sampriti Panda** · 2017-01-25 15:31 UTC

Yeah that worked for me too.


## export tool

*2016-08-11 to 2016-08-11 · 3 messages · [open in Zulip](https://chat.zulip.org/#narrow/channel/18-tools/topic/export.20tool/with/12618)*

**Steve Howell** · 2016-08-11 13:56 UTC

@Tim Abbott Does it make sense to create a `/tmp/zulip-export-latest` soft link?

**Tim Abbott** · 2016-08-11 15:57 UTC

yeah, that could be a nice workflow convenience

**Steve Howell** · 2016-08-11 17:38 UTC

When we export a single user, it seems like we might be exporting non-stream-related subscriptions and recipients, without connecting them to anything.  (I think).  Does that make sense?


## git pre-commit

*2016-08-15 to 2016-09-06 · 312 messages · [open in Zulip](https://chat.zulip.org/#narrow/channel/18-tools/topic/git.20pre-commit/with/14562)*

**Christie Koehler** · 2016-08-15 21:32 UTC

I'm trying to understand why there's an OR in the git pre-commit script here https://github.com/zulip/zulip/blob/master/tools/pre-commit

**Christie Koehler** · 2016-08-15 21:33 UTC

`tools/lint-all` seems to return the correct bash exit code. e.g. 0 for success and 1 for failure

**Tim Abbott** · 2016-08-15 21:34 UTC

because the intent is to have it just provide an error in the terminal, but still make the commit

**Christie Koehler** · 2016-08-15 21:34 UTC

and that seems to get reversed with the ||?

**Tim Abbott** · 2016-08-15 21:34 UTC

empirically, it's super annoying if it doesn't make the commit :)

**Christie Koehler** · 2016-08-15 21:34 UTC

oh

**Tim Abbott** · 2016-08-15 21:34 UTC

`|| true` just means "always succeed" in shell :)

**Christie Koehler** · 2016-08-15 21:34 UTC

yes, which is not what I would expect from this pre-commit hook

**Christie Koehler** · 2016-08-15 21:35 UTC

which is why I was confused.

**Christie Koehler** · 2016-08-15 21:35 UTC

e.g I would want to fix my whitespace errors before committing bc if I don't, I have to rebase to squash the commits

**Christie Koehler** · 2016-08-15 21:36 UTC

thanks for clarifying. I have this working via vagrant now

**Christie Koehler** · 2016-08-15 21:37 UTC

except for displaying the error

**Tim Abbott** · 2016-08-15 21:39 UTC

ahh, see I'd just use `git commit --amend` for the fixup

**Tim Abbott** · 2016-08-15 21:39 UTC

No need to make a new commit

**Christie Koehler** · 2016-08-15 22:01 UTC

it'd still be my preference for the commit not to go through

**Tim Abbott** · 2016-08-15 22:01 UTC

Well, maybe we should make that configurable :)

**Christie Koehler** · 2016-08-15 22:01 UTC

but regardless, it's confusing as it b/c if you get the commit working via vagrant, which is fairly easy, the message doesn't display

**Christie Koehler** · 2016-08-15 22:02 UTC

so you don't know about whitespace issues, for example, until CI fails

**Tim Abbott** · 2016-08-15 22:02 UTC

yeah

**Christie Koehler** · 2016-08-15 22:02 UTC

I get wanting the commit to go through no matter what, so now that I know that's intended behavior, I'm working on capturing the message

**Tim Abbott** · 2016-08-15 22:02 UTC

My theory is we should make the `pre-commit` hook smart in that if you are outside the guest, it will automatically do it via Vagrant

**Christie Koehler** · 2016-08-15 22:02 UTC

right now I'm just working to make a pre-commit hook that works via vagrant

**Tim Abbott** · 2016-08-15 22:03 UTC

cool, yeah should be easy to modify that to auto-detect

**Tim Abbott** · 2016-08-15 22:03 UTC

once we have it

**Christie Koehler** · 2016-08-15 22:05 UTC

it's running vagrant and outside of the guest, right?

**Christie Koehler** · 2016-08-15 22:05 UTC

I'm guessing these hooks already work for folks as-is who aren't using vagrant

**Tim Abbott** · 2016-08-15 22:06 UTC

right

**Tim Abbott** · 2016-08-15 22:06 UTC

yeah I can make that case work for you, since that's how I do development

**Tim Abbott** · 2016-08-15 22:06 UTC

So don't worry about it

**Tim Abbott** · 2016-08-15 22:06 UTC

will likely be <5 line change, but easier to be done by someone with the right test setup

**Tim Abbott** · 2016-08-15 22:06 UTC

I guess actually running inside vagrant will be the same experience as the no-vagrant

**Tim Abbott** · 2016-08-15 22:07 UTC

so maybe you can test easily, actually :)

**Christie Koehler** · 2016-08-15 22:07 UTC

I don't think it is

**Christie Koehler** · 2016-08-15 22:07 UTC

because git isn't setup inside vagrant

**Christie Koehler** · 2016-08-15 22:07 UTC

isn't set up with your user info and such

**Christie Koehler** · 2016-08-15 22:08 UTC

e.g. I can't commit from within vagrant without configuring git there

**Tim Abbott** · 2016-08-15 22:09 UTC

oh yeah, but you can just configure git inside temporarily to test

**Christie Koehler** · 2016-08-15 22:10 UTC

right, but I'm trying to adapt the precommit script to work with vagrant workflow

**Tim Abbott** · 2016-08-15 22:10 UTC

yeah

**Tim Abbott** · 2016-08-15 22:10 UTC

What I'm saying is you can test the non-vagrant workflow using your vagrant guest

**Christie Koehler** · 2016-08-15 22:11 UTC

yes, or any of the other non-vagrant machines I have setup to work with Zulip

**Christie Koehler** · 2016-08-15 22:11 UTC

I expect that's already working well

**Christie Koehler** · 2016-08-15 22:11 UTC

once you configure git

**Tim Abbott** · 2016-08-15 22:13 UTC

yeah

**Tim Abbott** · 2016-08-15 22:13 UTC

this is just to test if you broke it :)

**Tim Abbott** · 2016-08-15 22:13 UTC

when you're done

**Christie Koehler** · 2016-08-15 22:18 UTC

yes, indeed

**Christie Koehler** · 2016-08-15 22:18 UTC

sorry bash makes me irritable

**Christie Koehler** · 2016-08-15 22:19 UTC

And I haven't been able to think of a good way to automatically determine if you're using vagrant or not. Maybe a vagrant status or look for the processes or something?

**Christie Koehler** · 2016-08-16 00:41 UTC

Does anyone know why this works when I run it manually `.git/hooks/pre-commit` but not when I try to run `git commit`? http://cdn.subfictional.com/dropshare/pb-0wIEodiVcj.txt

**Christie Koehler** · 2016-08-16 00:41 UTC

I am not understanding something about the way git runs these hooks

**Steve Howell** · 2016-08-16 00:47 UTC

What's the error?  I have definitely seen strange mypy results when in git rebases, so it wouldn't surprise me for mypy to act strangely in a git pre-commit hook.  Most of the other lint stuff is fairly straightforward in nature, so that would surprise me.

**Christie Koehler** · 2016-08-16 00:59 UTC

@Steve Howell the error is nothing is printed

**Christie Koehler** · 2016-08-16 00:59 UTC

ideally any linter errors would echo on screen

**Steve Howell** · 2016-08-16 01:13 UTC

is there is anything in the pre-commit hook that looks like it might suppress output?

**Christie Koehler** · 2016-08-16 01:28 UTC

@Steve Howell not in the hook itself. there's output if I run it manually, just not when it's invoked by git upon committing

**Steve Howell** · 2016-08-16 01:58 UTC

Hmmmm.

**Steve Howell** · 2016-08-16 02:03 UTC

I guess one little thing to check is to try install a git-commit hook that prints an obvious error regardless of what you check in, just to understand better how the hooks work.  Maybe the hooks annoyingly redirect error output to some file under `.git.`.

**Steve Howell** · 2016-08-16 14:15 UTC

I was able to reproduce the problem @Christie Koehler reported about 12 hours ago.  I think it has something to do with how stderr gets piped through vagrant ssh and/or git.  I can take tools/lint-all out of the equation and get funny results with this vcmd: `vcmd='echo "HELLO WORLD"; pwd; >&2 echo "simulate error"'`
Depending on whether I run the shell script directly or invoke it directly as a pre-commit hook, the stderr part of that shows up in different places.

**Tim Abbott** · 2016-08-16 15:00 UTC

If `vagrant ssh` is causing problems, one can just `ssh` to the IP address of the Vagrant geust

**Tim Abbott** · 2016-08-16 15:01 UTC

Which can be faster anyway

**Steve Howell** · 2016-08-16 15:03 UTC

yeah, this is crazy flaky

**Steve Howell** · 2016-08-16 15:04 UTC

is the guest just 127.0.0.1?

**Tim Abbott** · 2016-08-16 15:05 UTC

`$ vagrant ssh-config` I think tells you

**Steve Howell** · 2016-08-16 15:15 UTC

Hmmm, I think I'm in vagrant now via ssh, but the lint-all script isn't able to import stuff.

**Steve Howell** · 2016-08-16 15:18 UTC

```
$ cat .git/hooks/pre-commit
#!/bin/sh
vcmd='(cd /srv/zulip && pwd && ./tools/lint-all $(git diff --cached --name-only --diff-filter=ACM))'
identity=/Users/showell/zulip/.vagrant/machines/default/virtualbox/private_key
ssh -p 2222 -i "$identity" vagrant@127.0.0.1  "$vcmd"

 $ .git/hooks/pre-commit
/srv/zulip
ImportError: No module named typing
You need to run the Zulip linters inside a Zulip dev environment.
If you are using Vagrant, you can `vagrant ssh` to enter the Vagrant guest.
```

**Steve Howell** · 2016-08-16 15:26 UTC

Also, if I use vanilla ssh to get into a vagrant shell, I can run the command; I just can't pass in the command on the command line and have its environment be what I want.

**Tim Abbott** · 2016-08-16 15:40 UTC

try passing `-t` to ssh

**Steve Howell** · 2016-08-16 15:41 UTC

heh, that works

**Tim Abbott** · 2016-08-16 15:41 UTC

I think our code to source the virtualenv (which is what that check is for) is in the bash scripts that only run if it's making a terminal

**Steve Howell** · 2016-08-16 15:42 UTC

@Christie Koehler You will need to s/showell/whatever/ here:

```
$ cat .git/hooks/pre-commit
#!/bin/sh
vcmd='source /home/vagrant/.bash_profile && cd /srv/zulip && pwd && ./tools/lint-all $(git diff --cached --name-only --diff-filter=ACM)'
identity=/Users/showell/zulip/.vagrant/machines/default/virtualbox/private_key
ssh -t -p 2222 -i "$identity" vagrant@127.0.0.1 $vcmd
```

**Steve Howell** · 2016-08-16 15:43 UTC

/me wants the last hour of his life back now.

**Steve Howell** · 2016-08-16 15:48 UTC

Oh, wait, if I run through the hook, now I get this: Pseudo-terminal will not be allocated because stdin is not a terminal.

**Tim Abbott** · 2016-08-16 15:48 UTC

ok well then probably you need to manually source the venv inside the script

**Steve Howell** · 2016-08-16 15:49 UTC

I do.

**Tim Abbott** · 2016-08-16 15:49 UTC

oh

**Steve Howell** · 2016-08-16 15:49 UTC

oh, gotcha

**Steve Howell** · 2016-08-16 15:49 UTC

just the venv part?

**Tim Abbott** · 2016-08-16 15:49 UTC

Or, actually, for `lint-all` in particular, we could have `lint-all` auto-source it for you

**Tim Abbott** · 2016-08-16 15:50 UTC

e.g. do `import scripts.lib.setup_path_on_import` inside a try/except clause

**Tim Abbott** · 2016-08-16 15:50 UTC

See `puppet/zulip/files/postgresql/process_fts_updates` for an example

**Steve Howell** · 2016-08-16 15:51 UTC

is that ok to do if you're already inside a venv?

**Tim Abbott** · 2016-08-16 15:52 UTC

should be

**Tim Abbott** · 2016-08-16 15:52 UTC

might waste a bit of time though, so could be worth checking :)

**Steve Howell** · 2016-08-16 16:01 UTC

So, this is kind of confusing, but the original problem was always about getting terminal output.  Going to vanilla ssh instead of vagrant ssh allowed us to hone in on pseudo-terminals being the issue, but then the problem is you still can't use `-t` inside of  a git hook.

**Steve Howell** · 2016-08-16 16:12 UTC

I am throwing in the towel on this for now.  Here is a script that has the same behavior as the original one @Christie Koehler posted.  It successfully sets the return code to 1, but it doesn't show terminal output.  This version removes the variable of `vagrant ssh` being the problem:

```
#!/bin/sh
vcmd='source /srv/zulip-venv/bin/activate && cd /srv/zulip && ./tools/lint-all $(git diff --cached --name-only --diff-filter=ACM)'
identity=/Users/showell/zulip/.vagrant/machines/default/virtualbox/private_key
ssh -p 2222 -i "$identity" vagrant@127.0.0.1 $vcmd
``

**Christie Koehler** · 2016-08-16 16:41 UTC

@Steve Howell thank you so much for working on this

**Steve Howell** · 2016-08-16 16:43 UTC

no prob, sorry I couldn't get to a solution...if you get really stuck on this, I have thought about a hackier workflow where we maybe run tools/lint-all ourselves, but the git hook could identify that we haven't run it in the last minute or so...would require prolly a one-line tweak to lint-all

**Christie Koehler** · 2016-08-16 16:44 UTC

or if what we want to see is the output, it could be written to a temp file and probably ready in by the git hook

**Christie Koehler** · 2016-08-16 16:44 UTC

So the issue has to do with pseudo terminals and not being able to use them in git hooks?

**Steve Howell** · 2016-08-16 16:48 UTC

yeah, I tried the temp file approach, and I couldn't get it to work, because I think there was still some funkiness related to the pseudo-terminal, but I could imagine a special command line argument to lint-all that tells it to write simple output to a file; of course, this is complicated by the fact that lint-all itself launches several subprocesses

**Christie Koehler** · 2016-08-16 16:59 UTC

I wonder if it would be possible to redirect to /dev/tty

**Steve Howell** · 2016-08-16 17:01 UTC

Interesting, yeah, that's worth a shot.  (I don't know much about how Unix terminals work, sadly.)  What I'm going to do as a first cut is abstract sys.stdout a little bit in tools/lint-all.  I'll ping you once I put up the PR.  Then from there we can try to have option(s) to either redirect to tty and/or redirect to a file.

**Christie Koehler** · 2016-08-16 17:02 UTC

okay

**Steve Howell** · 2016-08-16 17:02 UTC

Shouldn't take me more than 5 minutes, so you'll probably hear from me in about half an hour. ;)

**Christie Koehler** · 2016-08-16 17:02 UTC

sounds good!

**Christie Koehler** · 2016-08-16 17:34 UTC

I just thought to test another script in `/tools/`. I get output from `test-backend`.

**Christie Koehler** · 2016-08-16 17:34 UTC

So now I'm working if lint-all is doing something odd with stderr/stdout or redirection.

**Steve Howell** · 2016-08-16 17:36 UTC

Yes, lint-all writes directly to sys.stdout and has many subprocesses.  For pyflakes in particular, it uses subprocess.Popen with pipe redirection.

**Steve Howell** · 2016-08-16 17:37 UTC

anyway, #1631 is out there now

**Steve Howell** · 2016-08-16 17:38 UTC

oops, missed one call to sys.stdout, about to re-push, but you can look at it now to get the idea of where I'm going

**Steve Howell** · 2016-08-16 17:40 UTC

ok, re-pushed

**Christie Koehler** · 2016-08-16 17:44 UTC

@Steve Howell So you've changed it so that each of the tests instead of writing directly to stdout, write to outfile?

**Christie Koehler** · 2016-08-16 17:45 UTC

Does it make sense that /dev/tty would exist before running `lint-all` but not after? In the same vagrant ssh session?

**Steve Howell** · 2016-08-16 17:46 UTC

No, all I've done is make it easy to hack on lint-all.

**Steve Howell** · 2016-08-16 17:47 UTC

If you go to the `output-redirected` context manager, you can experiment with opening dev/tty instead of return sys.stdout as the object that supports "write" calls in all the other places.

**Christie Koehler** · 2016-08-16 17:47 UTC

gotcha

**Steve Howell** · 2016-08-16 17:48 UTC

I'm happy to try it on my end if you want.  Just let me know either way.

**Christie Koehler** · 2016-08-16 17:59 UTC

@Steve Howell Thanks. I'm taking a look now.

**Steve Howell** · 2016-08-16 18:09 UTC

Sounds good, let me know if you have any questions or want me to try out anything on my side.

**Christie Koehler** · 2016-08-16 19:07 UTC

I've narrowed it down to the pyflakes checker by turning on verbose output. This is probably unsurprising thought.

**Steve Howell** · 2016-08-16 19:14 UTC

Cool, keep me posted!

**Christie Koehler** · 2016-08-16 19:21 UTC

I'm having trouble understanding this line: https://github.com/zulip/zulip/blob/master/tools/lint-all#L74

**Christie Koehler** · 2016-08-16 19:22 UTC

that is, why a PIPE instead of handle to the existing out_file?

**Steve Howell** · 2016-08-16 19:27 UTC

two reasons, I think:
* we are trying to collect both stdout/stderr
* we need to post-process the output to quiet down pyflakes for things that we don't consider to be real errors

**Steve Howell** · 2016-08-16 19:28 UTC

I would argue there's some merit in just sweeping the code for some things, like unused imports, but that's a substantial project.

**Steve Howell** · 2016-08-16 19:29 UTC

It's also possible that pyflakes has become more configurable in terms of turning off those errors since we originally wrote that code.

**Steve Howell** · 2016-08-16 19:30 UTC

You can run with the --full option to see the scope of what we're filtering out from the pyflakes output.

**Steve Howell** · 2016-08-16 19:34 UTC

I get 1099 lines when I turn on --full.  So, yeah, a big project.  I'm personally a big fan of cleaning up unused import statements, as it can be a big help in splitting up modules to know what your true dependencies are.  But there are definitely convenience sacrifices if you buy into that discipline.

**Tim Abbott** · 2016-08-16 19:34 UTC

yeah, also pyflakes doesn't know about mypy annotations, so its output can be wrong

**Tim Abbott** · 2016-08-16 19:34 UTC

This is an issue that will go away on python 3

**Christie Koehler** · 2016-08-16 19:36 UTC

The wanting to collect stdout and stderr I understand. Is that not possible with a file handle? Why does it need to be a pipe?

**Steve Howell** · 2016-08-16 19:38 UTC

a pipe kinda is a file handle

**Steve Howell** · 2016-08-16 19:38 UTC

I mean not even kinda.

**Steve Howell** · 2016-08-16 19:40 UTC

Everything in Unix is either a file handle or a cryptic two-letter/three-letter command. ;)

**Christie Koehler** · 2016-08-16 19:44 UTC

Right

**Christie Koehler** · 2016-08-16 19:49 UTC

From the docs - "PIPE indicates that a new pipe to the child should be created. With the default settings of None, no redirection will occur; the child’s file handles will be inherited from the parent."

**Christie Koehler** · 2016-08-16 19:50 UTC

Why are the file handles from the parent not suitable for capturing stdout and stderr of pyflakes in this case?

**Steve Howell** · 2016-08-16 19:50 UTC

(And the reason to use pipes is to avoid creating permanent files, which would be subject to errors like mistakenly reading an obsolete file or not being in a suitable directory.)

**Christie Koehler** · 2016-08-16 19:52 UTC

I am not saying this is wrong, I am just trying to understand why the output collection breaks right here when run through a shell

**Steve Howell** · 2016-08-16 19:52 UTC

um, not sure I completely understand your question, but maybe this is the answer: the parent process has a bunch of stdout completely unrelated to pyflakes; the parent is only interested in post-processing pyflakes output, not jslint

**Christie Koehler** · 2016-08-16 19:52 UTC

yes, that explanation makes sense.

**Steve Howell** · 2016-08-16 19:53 UTC

Yeah, don't worry, questions are good here.  There is reasoning behind the way it's currently written, but that reasoning may be completely broken, haha

**Christie Koehler** · 2016-08-16 19:53 UTC

okay, so I understand not inheriting the parent's file handles

**Christie Koehler** · 2016-08-16 19:54 UTC

why use a pipe vs new file handles specific to this child processes?

**Steve Howell** · 2016-08-16 19:54 UTC

Cool.  Have you tried re-pointing this to dev/tty yet?

**Christie Koehler** · 2016-08-16 19:55 UTC

I stopped focusing on that when I realized that the output was breaking at this pyflakes code

**Steve Howell** · 2016-08-16 19:55 UTC

So we could just have the child write to output files in the "real" file system, but I think I address that in my earlier comment (does the dir exist?  is some other lint-all gonna overwrite it?)

**Christie Koehler** · 2016-08-16 19:56 UTC

and so I'm trying to understand what's happening with the childprocesses and the terminal output

**Christie Koehler** · 2016-08-16 19:57 UTC

is there only one stdout and stderr handles available at a time?

**Steve Howell** · 2016-08-16 19:57 UTC

So I think you were actually on the right track with dev/tty, but you are not wrong to focus on pyflakes either.  I think the pipes-based approach to capturing pyflakes output might somehow be aggravating some issue with a pseudo-terminal not being available.

**Christie Koehler** · 2016-08-16 19:58 UTC

I suspect it's the whole issue

**Christie Koehler** · 2016-08-16 19:58 UTC

because when I run the git hook with -v I get output outside of the vagrant VM until pyflakes

**Christie Koehler** · 2016-08-16 19:58 UTC

and then squat

**Steve Howell** · 2016-08-16 19:59 UTC

Yeah, so don't quote me rigorously on this, but basically every Unix process loads with file handles to stderr/stdin/stdout, and 90% of the time they come from a shell-like process that sets up those file handles to be what you prosaically think of as input/output/error, but the other 10% of the time the parent is re-plugging your stdin to some non-shell's stdout.  The classic example is Unix pipeline chains: `cat foo.txt | sort | uniq -c | grep bar`

**Christie Koehler** · 2016-08-16 20:01 UTC

Another odd thing I noticed is that if you use `file /dev/tty && /srv/zulip/tools/lint-all && file /dev/tty` as your vagrant command, you get nothing for the second file /dev/tty

**Steve Howell** · 2016-08-16 20:01 UTC

Behind the scenes bash is configuring the stdout of `cat` to be the stdin of `sort`.

**Steve Howell** · 2016-08-16 20:02 UTC

yeah, I think your observation about /dev/tty gets to the heart of the matter...we are getting into some strange universe where "terminal" is no longer a concept and processes can only write to files

**Christie Koehler** · 2016-08-16 20:02 UTC

I also found this https://docs.python.org/2.7/library/subprocess.html#subprocess.Popen.communicate

**Christie Koehler** · 2016-08-16 20:02 UTC

which we're not using. Not sure if this is related or not

**Steve Howell** · 2016-08-16 20:03 UTC

But I think it's more about fixing `lint-all` than fixing how `lint-all` talks to `pyflakes`, if that makes any sense.

**Steve Howell** · 2016-08-16 20:04 UTC

So, yeah, the Python way of managing processes has completely evolved over time, so I wouldn't completely rule that out as a factor.  Having said that...

**Steve Howell** · 2016-08-16 20:05 UTC

I think it's worthwhile to patch lint-all so that it just writes to an output file.  Then git hooks can just display the output from the output file.  And I'd bet with 65% confidence that we wouldn't need to address the way that lint-all talks to pyflakes if we got that working.

**Christie Koehler** · 2016-08-16 20:06 UTC

As long as the same issue doesn't cause problems with writing to the file,  yeah.

**Steve Howell** · 2016-08-16 20:07 UTC

I think the strange boundary is really between git/vagrant and lint-all, not pyflakes.  But I wouldn't bet my first born on it.

**Christie Koehler** · 2016-08-16 21:09 UTC

haha

**Christie Koehler** · 2016-08-16 21:10 UTC

I changed it to use communicate() and now the logging output doesn't stop with pyflakes, but neither are the pyflakes messages displayed

**Christie Koehler** · 2016-08-16 21:10 UTC

so now maybe I think @Steve Howell was on to something

**Christie Koehler** · 2016-08-16 21:17 UTC

logger shows output via vagrant/ssh

**Steve Howell** · 2016-08-16 22:02 UTC

So lint-all fails fast, so what might be happening is that you perturbed which subprocess finishes first.

**Steve Howell** · 2016-08-16 22:04 UTC

hmmm...I take that back...it waits for all subprocesses...but I'm curious what logging normally follows the pyflakes output

**Steve Howell** · 2016-08-16 22:04 UTC

are you running with `--verbose`?

**Christie Koehler** · 2016-08-16 23:08 UTC

yes, I'm generally running with --verbose

**Christie Koehler** · 2016-08-16 23:10 UTC

and if I write using `logging.info`I see output when running lint-all via vagrant

**Christie Koehler** · 2016-08-16 23:11 UTC

(I don't see the same output via sys.stdout.write)

**Christie Koehler** · 2016-08-16 23:11 UTC

one thing I discovered is that the call to sys.exit causes vagrant to return right away, even if you have more in your command

**Steve Howell** · 2016-08-16 23:15 UTC

Yeah, that's strange, but your observation seems consistent with what we're seeing.  Basically, at the first sign of trouble, something is exiting before showing us the symptoms.  On the other hand, I was able to repro this using regular ssh instead of vagrant ssh.  (That doesn't completely exonerate vagrant, though.)  Also, somehow git is part of the problem here.

**Steve Howell** · 2016-08-16 23:16 UTC

What happens if you just redirect to a file at the tools/lint-all level?

**Christie Koehler** · 2016-08-16 23:21 UTC

@Steve Howell It doesn't get that far

**Christie Koehler** · 2016-08-16 23:22 UTC

either that or I am confused about my paths; let me try again

**Christie Koehler** · 2016-08-16 23:23 UTC

I was confused about my paths.

**Christie Koehler** · 2016-08-16 23:23 UTC

It created the file, but there's only a bit of whitespace in it

**Steve Howell** · 2016-08-16 23:25 UTC

even if you run it locally, and not through the hook?

**Steve Howell** · 2016-08-16 23:26 UTC

Let me try something on my end...

**Christie Koehler** · 2016-08-16 23:27 UTC

@Steve Howell yeah, running it within Vagrant and outside of Vagrant yields the same results

**Steve Howell** · 2016-08-16 23:28 UTC

can you send me the diff for writing-to-file in lint-all?

**Christie Koehler** · 2016-08-16 23:31 UTC

@Steve Howell I may have mis-understood what you meant. I just did `tools/lint-all >lint.log`

**Christie Koehler** · 2016-08-16 23:34 UTC

I haven't quite figured out how to redirect all of the scripts output from sys.stdout

**Steve Howell** · 2016-08-16 23:36 UTC

no, I'm thinking of having lint-all write directly to a file, so that it doesn't have to deal with any jankiness of the file descriptor that's being passed in to it as stdout

**Christie Koehler** · 2016-08-16 23:41 UTC

@Steve Howell To be clear, you mean replacing the sys.std.write statements, right?

**Steve Howell** · 2016-08-16 23:49 UTC

yeah, let me post my next fix to the PR...it doesn't fix anything yet, but it will clarify what I'm talking about...I am starting to think the problem now is actually the fork in `run_parallel()`...poking @Tim Abbott

**Steve Howell** · 2016-08-16 23:52 UTC

So `run_parallel` forks off child processes to run some test code in parallel.  (These are child process of lint-all itself, not launching new subprocesses.)  I think there is something happening to file descriptors when we fork there.

**Christie Koehler** · 2016-08-16 23:59 UTC

@Steve Howell That's the code I've been looking at too

**Christie Koehler** · 2016-08-17 00:00 UTC

was reading through p ython docs trying to understand when you are to use os.fork() and when to use subproccess

**Christie Koehler** · 2016-08-17 00:00 UTC

I think one of the processes is writing to screen and then failing before the redirect can complete...maybe?

**Christie Koehler** · 2016-08-17 00:01 UTC

I want a call stack diagram for lit-all.

**Steve Howell** · 2016-08-17 00:02 UTC

So I'd start at the top with the functions with @lint decorator.  They get put into a list that `run_parallel` processes.

**Steve Howell** · 2016-08-17 00:05 UTC

Long story short, forking off a bunch of child processes and having them all write to the same file descriptor is asking for trouble.

**Steve Howell** · 2016-08-17 00:06 UTC

even if it's stdout

**Christie Koehler** · 2016-08-17 00:06 UTC

yeah

**Christie Koehler** · 2016-08-17 00:07 UTC

using logger.warn or logger.info works in the few places I've tried it, but I don't know what the implications of swtiching to that are

**Christie Koehler** · 2016-08-17 00:07 UTC

I like it because it works and it's already there

**Christie Koehler** · 2016-08-17 00:14 UTC

oh my god

**Sumana Harihareswara** · 2016-08-17 00:15 UTC

/me listens to the latest iteration of this saga -- which is probably worth a conference talk or podcast ep all on its own

**Christie Koehler** · 2016-08-17 00:15 UTC

I figured it out.

**Christie Koehler** · 2016-08-17 00:16 UTC

I added a `sys.stdout.flush()` before the `os._exit` call in `run_parallel()`

**Christie Koehler** · 2016-08-17 00:16 UTC

that's it. that's all it needed

**Christie Koehler** · 2016-08-17 00:17 UTC

now it displays the output when run via vagrant and actually writes to a file when redirected

**Steve Howell** · 2016-08-17 00:18 UTC

Heh, yeah, I have that in my branch now, and it seems to fix it.

**Steve Howell** · 2016-08-17 00:19 UTC

we should probably flush after every single write

**Christie Koehler** · 2016-08-17 00:19 UTC

or at least when the processes are handed off

**Christie Koehler** · 2016-08-17 00:20 UTC

well lint-all is probably the zulip code I know best now

**Steve Howell** · 2016-08-17 00:22 UTC

haha

**Christie Koehler** · 2016-08-17 00:22 UTC

thanks for working with me on that one @Steve Howell !

**Christie Koehler** · 2016-08-17 00:22 UTC

so many red herrings!

**Steve Howell** · 2016-08-17 00:22 UTC

indeed

**Christie Koehler** · 2016-08-17 00:23 UTC

I do think lint-all could be improved a lot.

**Christie Koehler** · 2016-08-17 00:23 UTC

But of course I have opinions about it after spending a day with it. ;)

**Sumana Harihareswara** · 2016-08-17 00:23 UTC

@Christie Koehler I want to learn everything you know, but, like, via a doc or a talk

**Steve Howell** · 2016-08-17 00:23 UTC

yeah, it's really hacky...everything executes at the top level in Python, so namespaces are messy, which gets crazy when you start forking

**Sumana Harihareswara** · 2016-08-17 00:23 UTC

(about `lint-all` specifically)

**Sumana Harihareswara** · 2016-08-17 00:24 UTC

or via code comments

**Christie Koehler** · 2016-08-17 00:24 UTC

first step might be code comments

**Christie Koehler** · 2016-08-17 00:24 UTC

## this code made christie cry

**Christie Koehler** · 2016-08-17 00:24 UTC

## this code made christie yell at her dogs

**Christie Koehler** · 2016-08-17 00:24 UTC

j/k

**Sumana Harihareswara** · 2016-08-17 00:24 UTC

/me offers tea and a nice vegan gluten-free snack

**Steve Howell** · 2016-08-17 00:24 UTC

Usually my dogs yell at me

**Sumana Harihareswara** · 2016-08-17 00:24 UTC

:tea: :dog_face: :cookie:

**Tim Abbott** · 2016-08-17 00:27 UTC

I see, so it turns out to be a subtle mistake I made writing `run_parallel` like 3 years ago.  Nice :)

**Steve Howell** · 2016-08-17 00:28 UTC

ok, I think we should push #1631 with approval from @Tim Abbott, but then one of should take on a project to clean up how we multiplex all the errors from the subprocesses...flush() is a big help, but there are still possible races

**Christie Koehler** · 2016-08-17 00:28 UTC

https://github.com/christi3k/zulip/commit/37feb29991daa910ef2911bfd7ea1fa9359dfc55

**Christie Koehler** · 2016-08-17 00:29 UTC

yeah, I wouldn't be surprised if there are other gotchas

**Steve Howell** · 2016-08-17 00:29 UTC

@Tim Abbott I was in on that decision, too!

**Christie Koehler** · 2016-08-17 00:29 UTC

It's all good, @Tim Abbott , I got to have an excuse to deep dive into all sorta of things.

**Christie Koehler** · 2016-08-17 00:30 UTC

like bash redirection. psuedo-terminals, and multiprocesss python

**Christie Koehler** · 2016-08-17 00:30 UTC

this is all so I can automatically run the linter upon commit because otherwise I forget

**Tim Abbott** · 2016-08-17 00:30 UTC

This only sorta works, but:

!avatar(christie@authenticengine.com)
:octopus:

**Christie Koehler** · 2016-08-17 00:31 UTC

haha

**Tim Abbott** · 2016-08-17 00:31 UTC

I think if we did some tweaking to the size of `!avatar(email)` we could make that look good

**Tim Abbott** · 2016-08-17 00:31 UTC

Ooh, just found a render ordering bug

**Tim Abbott** · 2016-08-17 00:32 UTC

`avatar` should not be able to escape like that

**Christie Koehler** · 2016-08-17 00:32 UTC

did you put that in backticks?

**Tim Abbott** · 2016-08-17 00:33 UTC

yeah

**Tim Abbott** · 2016-08-17 00:33 UTC

it's a markdown parser bug

**Tim Abbott** · 2016-08-17 00:35 UTC

have a fix already, guess I should add some tests too though

**Steve Howell** · 2016-08-17 00:37 UTC

@Christie Koehler Can you submit a PR for your one-line flush() fix?  I have some ideas on cleaning this up a bit, but this script is actually pretty robust for typical uses, and if your flush() fix fixes your issue, I think we can punt on deeper cleanup for a while.

**Christie Koehler** · 2016-08-17 00:38 UTC

@Steve Howell yeah I was going to wait for CI to complete, but it's a small change so I went ahead

**Christie Koehler** · 2016-08-17 00:38 UTC

https://github.com/zulip/zulip/pull/1637

**Steve Howell** · 2016-08-17 00:47 UTC

I'll create a PR for deeper cleanup...

**Steve Howell** · 2016-08-17 00:52 UTC

#1638

**Steve Howell** · 2016-08-17 00:52 UTC

@Christie Koehler In your PR you might want to flush stderr for good measure.

**Christie Koehler** · 2016-08-17 00:52 UTC

@Steve Howell I was literally just realizing that.

**Steve Howell** · 2016-08-17 00:52 UTC

haha gmta

**Steve Howell** · 2016-08-17 00:54 UTC

@Sumana Harihareswara #1638 is a great project for somebody who wants to get their feet wet on something pretty core to Zulip but not directly user-impacting

**Christie Koehler** · 2016-08-17 00:57 UTC

Here's the python documentation for `os._exit(n)`: "Exit the process with status n, without calling cleanup handlers, flushing stdio buffers, etc."

**Christie Koehler** · 2016-08-17 00:57 UTC

I feel like they could help you out a bit more there.

**Steve Howell** · 2016-08-17 01:02 UTC

Huh, maybe we should be calling `sys.exit()` instead?

**Christie Koehler** · 2016-08-17 01:17 UTC

No, I think it's the right thing to use with child processes from .fork()

**Christie Koehler** · 2016-08-17 01:17 UTC

"Note The standard way to exit is sys.exit(n). _exit() should normally only be used in the child process after a fork()."

**Sumana Harihareswara** · 2016-08-17 01:18 UTC

@Steve Howell thanks for the heads-up!

**Sumana Harihareswara** · 2016-08-17 01:19 UTC

@Steve Howell add `help wanted`?

**Steve Howell** · 2016-08-17 01:26 UTC

ah, good point @Christie Koehler ... @Sumana Harihareswara yep, looks like somebody already added it

**Sumana Harihareswara** · 2016-08-17 01:27 UTC

Cool :thumbsup:

**Steve Howell** · 2016-08-17 01:31 UTC

It's too bad there's not something higher-level than os._exit that isn't as big-hammer as sys.exit().  Maybe we should just thread all the parallel linters, though, and then we could have an easy thread-lock to write output (at least for the local stuff).

**Christie Koehler** · 2016-08-17 20:30 UTC

progress! https://github.com/christi3k/zulip/blob/improve-pre-commit-hook/tools/pre-commit

**Christie Koehler** · 2016-08-17 20:31 UTC

I'm still working on the best way to determine whether or not you're actively using vagrant for the zulip dev

**Tim Abbott** · 2016-08-17 20:38 UTC

just test if the current user is called `vagratn`

**Christie Koehler** · 2016-08-17 20:42 UTC

@Tim Abbott that would tell me if I'm in the vagrant VM, which is not what I'm testing for

**Christie Koehler** · 2016-08-17 20:42 UTC

i'm testing if I'm my normal user AND using vagrant

**Christie Koehler** · 2016-08-17 20:42 UTC

or if I'm just my regular user but I've done a manual setup for zulip dev

**Tim Abbott** · 2016-08-17 20:42 UTC

ahh, whether you have a vagrant guest?  Checking whether there's a `.vagrant` file in the Zulip repo is pretty good

**Christie Koehler** · 2016-08-17 20:42 UTC

I think I got it though

**Tim Abbott** · 2016-08-17 20:43 UTC

I would probably add an exclusion for if you're inside a Zulip virtualenv, since that would suggest that you have a Vagrant guest but don't use it normally

**Christie Koehler** · 2016-08-17 20:43 UTC

when is that .vagrant directory created?

**Tim Abbott** · 2016-08-17 20:44 UTC

it's created by `vagrant up`

**Tim Abbott** · 2016-08-17 20:44 UTC

Stores Vagrant metadata about your Vagrant environment

**Christie Koehler** · 2016-08-17 20:46 UTC

I have a zulip checkout with that directory and the only vagrant command i've done is `vagrant status`

**Tim Abbott** · 2016-08-17 20:46 UTC

OK, so maybe every vagrant command also creates it :)

**Tim Abbott** · 2016-08-17 20:46 UTC

probably doesn't matter

**Christie Koehler** · 2016-08-17 20:46 UTC

the approach I have now is to do `vagrant status` and proceed with the vagrant version of the linter if the result is anything but 'not created'

**Tim Abbott** · 2016-08-17 20:47 UTC

Fundamentally, I think a correct algorithm is this:

* if we're in a virtualenv, just run the command
* if we're not, and there's a .vagrant file, try to use `vagrant ssh`

**Tim Abbott** · 2016-08-17 20:48 UTC

(the first case covers the "you're the vagrant user" case)

**Christie Koehler** · 2016-08-17 20:49 UTC

there's no way the user would be in a virtualenv any other way?

**Christie Koehler** · 2016-08-17 20:57 UTC

e.g they are working on multiple projects. I'm looking through docs now.

**Christie Koehler** · 2016-08-18 01:12 UTC

I :heart: this update git hook

**Christie Koehler** · 2016-08-18 01:14 UTC

Would love to have a few others test it, esp those not using vagrant for their Zulip dev environment. https://github.com/zulip/zulip/pull/1643

**Christie Koehler** · 2016-08-18 19:11 UTC

ugh I just remembered we also have a docker setup

**Tim Abbott** · 2016-08-18 19:12 UTC

I think it's fine for this to not be tested/implemented for docker

**Tim Abbott** · 2016-08-18 19:12 UTC

I don't think it's used heavily

**Tim Abbott** · 2016-08-18 19:12 UTC

People who use it can contribute support for it if needed

**Christie Koehler** · 2016-08-18 19:12 UTC

okay

**Tim Abbott** · 2016-08-18 19:13 UTC

better to ship the thing for the majority of users, for this at least

**Christie Koehler** · 2016-08-18 19:13 UTC

I'd like to keep up with how docker works but there's only so much time in the day!

**Christie Koehler** · 2016-08-18 19:13 UTC

plus I got annoyed when the required you to sign an NDA to try their beta

**Christie Koehler** · 2016-08-18 19:13 UTC

yeah, and the commit hooks are something you have to specifically enable

**Sumana Harihareswara** · 2016-08-29 19:45 UTC

Thanks to @Christie Koehler for writing up https://subfictional.com/2016/08/27/pythons-os-fork-subprocess-and-the-case-of-the-missing-output/

**Christie Koehler** · 2016-08-29 19:45 UTC

@Sumana Harihareswara you're welcome! I hope it was useful

**Christie Koehler** · 2016-08-29 19:46 UTC

Was thinking I should put some of the explanation into lint-all as comments

**Sumana Harihareswara** · 2016-08-29 19:48 UTC

@Christie Koehler I will defer to others on this matter but I think your explanation will be helpful to future archaeologists. And I learned about `shopt`

**Tim Abbott** · 2016-09-06 17:44 UTC

@Christie Koehler maybe it's worth adding a link to that blog post in the comments of the relevant code?

**Tim Abbott** · 2016-09-06 17:45 UTC

Oh, I see you had that idea as well.  I think it's a good one :)

**Christie Koehler** · 2016-09-06 17:46 UTC

Cool, I will do that today.

**Christie Koehler** · 2016-09-06 17:46 UTC

I've also been thinking about way sto refactor the linter, but not sure how high a priority that is.

**Steve Howell** · 2016-09-06 17:53 UTC

For the linter it would be nice to at least move all the "data" stuff out to its own file (probably still built with Python).    All the pattern/description rules make it hard to scan the program for the higher level stuff going on.

**Tim Abbott** · 2016-09-06 17:54 UTC

+1 to doing that

**Christie Koehler** · 2016-09-06 17:54 UTC

Indeed, that's probably a good place to start.

**Christie Koehler** · 2016-09-06 17:54 UTC

Also want to revisit the concurrency model and see if there's a better way to do that.

**Steve Howell** · 2016-09-06 17:58 UTC

One thing on the concurrency stuff is that it would be about 10 lines of code to add the ability to just run one of the lint types, which can be useful when you're doing iterative development.  Although for some of the sub-options you can already call a full process.  Maybe for consistency it would be to have ./tools/custom-checks.

**Steve Howell** · 2016-09-06 17:58 UTC

What were you thinking in terms of addressing the concurrency stuff?

**Tim Abbott** · 2016-09-06 18:00 UTC

+1 to Steve's thought -- I don't think the concurrency stuff is really a problem

**Tim Abbott** · 2016-09-06 18:00 UTC

Though I do think it would be not crazy to eventually refactor lint-all to have a generic linter framework (supporting parallelism and all) + a Python script configuration file that defines how the linter framework works for Zulip

**Tim Abbott** · 2016-09-06 18:01 UTC

And then we could eventually spin the Zulip linter framework out as its own reusable project

**Steve Howell** · 2016-09-06 18:07 UTC

I think the low hanging fruit is to extract the custom-checks stuff and the pyflakes wrapper into their own tools.  That way lint-all is really just dispatching a bunch of other scripts, usually in parallel, and de-duplicating some of the logic around finding your git files.

**Christie Koehler** · 2016-09-06 18:08 UTC

I don't think the concurrency stuff is a problem, exactly. Mostly I think lint-all could be refactored to: a) be more readable, b) be more extensible and flexible, c) use more up to date python concurrency features.

**Christie Koehler** · 2016-09-06 18:08 UTC

Yeah, that makes sense to me.

**Steve Howell** · 2016-09-06 18:09 UTC

I am not sure how hard it is to extend, though, I guess is where I'm having the disconnect.  I added the CSS linter recently, and it was basically just dropping this into the code:

```
        @lint
        def css():
            # type: () -> int
            result = subprocess.call(['tools/check-css'])
            return result
```

**Christie Koehler** · 2016-09-06 18:10 UTC

Yes, but first you have to read though that whole file and understand how it works.

**Steve Howell** · 2016-09-06 18:11 UTC

Yeah, but that's mostly all the clutter from the custom checks.

**Christie Koehler** · 2016-09-06 18:11 UTC

Agreed, taking care of the low-handing fruit you identified will go a long way.

**Steve Howell** · 2016-09-06 18:12 UTC

276 lines of clutter, to be precise

**Steve Howell** · 2016-09-06 18:13 UTC

I think it's always worthwhile to evolve this tool, since it's pretty essential to everyday Zulip stuff, so to answer your original question, I would consider it somewhat of a priority.  Also, once you dig into the code a bit more, you may finid yourself wanting to do things like speed it up, remove some obsolete lint rules, etc., which would also be valuable.


## lint-all

*2016-08-18 to 2016-08-18 · 6 messages · [open in Zulip](https://chat.zulip.org/#narrow/channel/18-tools/topic/lint-all/with/15998)*

**Steve Howell** · 2016-08-18 19:04 UTC

#1647 is read to merge, pending review.  It shows red due to coverage.  We'll eventually address that by moving some code into tools/lib.

**Tim Abbott** · 2016-08-18 19:05 UTC

k

**Tim Abbott** · 2016-08-18 19:06 UTC

am on a roll working on Acrefoot's docs

**Tim Abbott** · 2016-08-18 19:06 UTC

So will review once that's done :)

**Steve Howell** · 2016-08-18 19:06 UTC

sgtm

**Steve Howell** · 2016-08-18 19:53 UTC

#1645 is also ready to merge, but like #1647, it shows red due to coverage.  I actually added tests in #1645, but the tools tests don't count toward coverage stats yet for Travis.


## automated HTML cleanup

*2016-08-26 to 2016-08-26 · 32 messages · [open in Zulip](https://chat.zulip.org/#narrow/channel/18-tools/topic/automated.20HTML.20cleanup/with/19843)*

**Steve Howell** · 2016-08-26 21:59 UTC

@Tim Abbott

**Tim Abbott** · 2016-08-26 21:59 UTC

yep?

**Steve Howell** · 2016-08-26 21:59 UTC

So one component of an HTML sweep is locking down the linters.

**Steve Howell** · 2016-08-26 22:00 UTC

I guess only one linter's involved here, check-templates.

**Steve Howell** · 2016-08-26 22:00 UTC

It only looks for consistent indentation between start and end; it has no notion of nesting levels or 4-space preferences.

**Steve Howell** · 2016-08-26 22:01 UTC

Neither's that hard to build; they just weren't worth the effort when so much of our HTML would have failed the checks.

**Steve Howell** · 2016-08-26 22:02 UTC

Also, the linter's would need some clarity on when no-indent is allowed, like for #if.

**Steve Howell** · 2016-08-26 22:02 UTC

In theory, it wouldn't be that difficult to just turn the linter into a pretty-printer.

**Steve Howell** · 2016-08-26 22:03 UTC

the linter guts, I mean

**Steve Howell** · 2016-08-26 22:06 UTC

if we did a fully automated pretty-print, I think there's some risk of the machine missing some edge case where the human knows how to wrap a tag more prettily, but that's only a dev-facing nuisance

**Tim Abbott** · 2016-08-26 22:08 UTC

If we wrote the pretty-printer, we could do some cross-checking to confirm it makes sense.

**Tim Abbott** · 2016-08-26 22:09 UTC

E.g. I could imagine doing a `M-x indent-region`, add that to index, and then run pretty-printer, to see what differs

**Steve Howell** · 2016-08-26 22:11 UTC

if we're pretty confident that M-x just works, then maybe we just do that, and then on the automated side, maybe have the linter dig a little deeper on things like wrapped tags.

**Steve Howell** · 2016-08-26 22:11 UTC

47 templates

**Steve Howell** · 2016-08-26 22:11 UTC

We're talking just Django-side for now, right?

**Tim Abbott** · 2016-08-26 22:13 UTC

yeah

**Tim Abbott** · 2016-08-26 22:13 UTC

handlebars has more churn and thus seems better to do second

**Steve Howell** · 2016-08-26 22:14 UTC

agreed, and I think the 2-vs.-4 debate is a little more blurry there

**Tim Abbott** · 2016-08-26 22:14 UTC

yeah

**Steve Howell** · 2016-08-26 22:17 UTC

how long would it take you to just sweep all 47?  and then, what do you think the odds are that most of them are good, in which case maybe we do some quick automated triage first?

**Steve Howell** · 2016-08-26 22:18 UTC

wow, I just randomly opened like 4 in a row that were bad, so I don't think triaging would help M-x much

**Steve Howell** · 2016-08-26 22:19 UTC

and, otoh, they don't seem too barbaric in terms of wrapping, which maybe is telling us to automate the indenting

**Steve Howell** · 2016-08-26 22:22 UTC

this is my favorite commit of all time, haha: https://github.com/zulip/zulip/commit/f78966d30613a44ad75b940a593abd6f615680fa

**Tim Abbott** · 2016-08-26 22:27 UTC

hahaha :)

**Steve Howell** · 2016-08-26 22:28 UTC

One pain point in the rebase case is that you'd need to revert the linter lockdowns too if you're in the weeds of a messy rebase.

**Steve Howell** · 2016-08-26 22:28 UTC

But I still think we can manage that reactively.

**Steve Howell** · 2016-08-26 22:29 UTC

I'm leaning more toward full automation.

**Tim Abbott** · 2016-08-26 22:29 UTC

yeah this seems like something where full automation (generating 1 commit per thing) is probably worth it

**Steve Howell** · 2016-08-26 22:30 UTC

I can get it all scripted on a branch, we can maybe run off my branch for a day on tzn, then go back to regular master, and wait for dust to settle on PRs, then do it for real.  Something like that.

**Tim Abbott** · 2016-08-26 22:30 UTC

So it can be just "fix-whitespace <path>" as the process for cleaning one once there aren't open PRs touching it

**Steve Howell** · 2016-08-26 22:31 UTC

or even just a fix-all-47 script that we run right after we release 1.4.1 or something

**Steve Howell** · 2016-08-26 22:31 UTC

and we try to keep the focus in 1.4 on getting stale PRs to master


## general code cleanup

*2016-08-26 to 2016-09-12 · 225 messages · [open in Zulip](https://chat.zulip.org/#narrow/channel/18-tools/topic/general.20code.20cleanup/with/19881)*

**Steve Howell** · 2016-08-26 22:33 UTC

On a related note, I am still hoping to persuade you to have a 1.5 branch that has some pretty major cleanup, and then we just have some small pain of applying 1.4.0..1.4.1 to 1.5

**Steve Howell** · 2016-08-26 22:34 UTC

or more likely 1.4.1...1.4.2

**Steve Howell** · 2016-08-26 22:35 UTC

we freeze 1.4.1 and do some things like compress migrations, sweep whitespace, sweep subject/topic/etc. on 1.5.0 and let it bake on tzn for a week

**Tim Abbott** · 2016-08-26 23:24 UTC

Yeah, I'm still feeling the "every week we do a big migration on master all targeted at our next release" approach

**Tim Abbott** · 2016-08-26 23:24 UTC

OK, we may do a 1.4.1 if we find something super serious we need to put out

**Tim Abbott** · 2016-08-26 23:25 UTC

But I'd rather, for each of the things in the list of larger migrations we want to do, come up with a plan for how to do that migration efficiently in master

**Tim Abbott** · 2016-08-26 23:26 UTC

For the database stuff, I want to start with moving `pub_date` to `timestamp` for the Message table, because that's a migration that I think I can do end-to-end in a day or two (complete with testing with a restored-from-backups copy of the zulipchat.com data set) to figure out a good process for doing large-scale migrations with the message table

**Tim Abbott** · 2016-08-26 23:26 UTC

And then once we've done that and worked out all the issues, we can start doing any other cleanups we feel are valuable

**Tim Abbott** · 2016-08-26 23:26 UTC

So, I agree the next major release should be 1.5 and we should be willing to do major cleanup, I just don't want to have 2 large branches :)

**Tim Abbott** · 2016-08-26 23:27 UTC

(I also think we should keep master releaseable as we go)

**Tim Abbott** · 2016-08-26 23:28 UTC

I think with almost any major change we want to do, we can do refactoring in master up front that makes the actual risky change a <100 line patch that we can test, rebase, and verify carefully

**Steve Howell** · 2016-08-26 23:49 UTC

So, for things like s/subject/topic/ and clean-up-all-templates, that's where I think it's hard to contain the risk to a nice < 100 line patch.

**Steve Howell** · 2016-08-26 23:50 UTC

There are things that aren't really risky inherently, they're just sweeping in nature.

**Steve Howell** · 2016-08-26 23:52 UTC

so for something like s/subject/topic/,  you make it the very first thing in a new release, and you have all people develop in the post-subject world...then the only thing that happens on the old release is small stuff

**Tim Abbott** · 2016-08-26 23:53 UTC

yeah, maybe for some things that are more syntactical it could be larger than 100 lines, but it's not going to be 100 lines of interesting stuff

**Steve Howell** · 2016-08-26 23:53 UTC

But I think the core of what I'm asking for isn't really to have two branches, it's to consolidate some of the sweep-the-code tasks together

**Tim Abbott** · 2016-08-26 23:54 UTC

I see.  I think to some extent I've already been running a process where when I'm getting ready to do a release I stop merging risky things until the release is out

**Tim Abbott** · 2016-08-26 23:54 UTC

that's basically been the last 2 weeks (and is part of why subdomains isn't fully merged)

**Steve Howell** · 2016-08-26 23:54 UTC

Here's an example issue.  Assume that sweep-whitespace wasn't fully automatic, nor subject-topic (which totally isn't automatic).  If you do subject-topic on one branch X and I do whitespace on branch Y, and we're both deadlocked, we're gonna have rebase hell.

**Tim Abbott** · 2016-08-26 23:55 UTC

So, release out, we're now in "sweeping changes are good" again :)

**Tim Abbott** · 2016-08-26 23:55 UTC

yeah, I see what you mean.  My perspective is that we should maybe be disciplined about avoiding having sweeping branches survive more than a week.

**Tim Abbott** · 2016-08-26 23:55 UTC

By which I mean, only start doing such a sweeping branch (or at least parts that may not be able to merge until a lot of care is taken) when we have the time allocated to finish them

**Steve Howell** · 2016-08-26 23:55 UTC

Cool.  And I think you're starting to flesh out the DB plan.  I think there are probably a list of things where the risk factors are all kind of similar.

**Tim Abbott** · 2016-08-26 23:56 UTC

But I think it's fine to have a few of these running somewhat in parallel, as long as we're strategic about the ordering.

**Steve Howell** · 2016-08-26 23:56 UTC

Yeah, that's actually exactly what I'm asking for!

**Tim Abbott** · 2016-08-26 23:56 UTC

E.g., one person could be working on redoing our tests to use different users while someone else is working on the first part of the message schema

**Steve Howell** · 2016-08-26 23:56 UTC

Some of them are hard to parallelize is kind of what I'm saying.

**Tim Abbott** · 2016-08-26 23:57 UTC

(or maybe a better example would be tests + templates)

**Tim Abbott** · 2016-08-26 23:57 UTC

Because they churn different parts of the codebase

**Tim Abbott** · 2016-08-26 23:57 UTC

We just need to coordinate these things

**Steve Howell** · 2016-08-26 23:57 UTC

Yeah, that's fair.

**Steve Howell** · 2016-08-26 23:58 UTC

Realistically they're gonna happen mostly serially anyway, because there are only so many active people on the project that have enough context to do them.

**Steve Howell** · 2016-08-26 23:59 UTC

#1623 lists most of the cleanup tasks I could think of off the top of my head--some were more speculative in nature than others, though

**Tim Abbott** · 2016-08-27 00:01 UTC

Yeah so python3 is basically done; we're down to a few small bugs at this point.

**Steve Howell** · 2016-08-27 00:01 UTC

Another set of changes for us to consider getting to sooner than later are user-facing things like "streams vs. channel" nomenclature.  If we can get ahead of the curve on those, we only have 14 sites or so to disrupt, vs. doing it a year from now.

**Tim Abbott** · 2016-08-27 00:01 UTC

I was planning to just kill /api/v1/send_message after bugging the one entity I know is still using it that it's being desupported

**Tim Abbott** · 2016-08-27 00:01 UTC

yeah agreed

**Tim Abbott** · 2016-08-27 00:02 UTC

Anyway I think that list is pretty good for what to be thinking about

**Tim Abbott** · 2016-08-27 00:02 UTC

I'd love to start just picking off 1-2 every week

**Steve Howell** · 2016-08-27 00:03 UTC

ok, anyway, back to the original topic of HTML cleanup, I think that's something where I can make some headway next week...one thing I thought of is maybe trying to get the template tests complete as part of the same effort

**Tim Abbott** · 2016-08-27 00:16 UTC

yeah the template test project would be a great one to finish

**Tim Abbott** · 2016-08-27 00:16 UTC

Especially since e.g. subdomains will be changing a lot of templates

**Steve Howell** · 2016-08-27 00:17 UTC

There's not much churn in the JS code at this point, correct?

**Tim Abbott** · 2016-08-27 00:19 UTC

Not too much.  A few large PRs related to it, but that's kinda different

**Tim Abbott** · 2016-08-27 00:19 UTC

One project that we could do quickly and enjoy would be finishing off zulip.js

**Tim Abbott** · 2016-08-27 00:19 UTC

Maybe worth making a central hit list of refactoringy cleanups we want to do

**Tim Abbott** · 2016-08-27 00:19 UTC

e.g. eliminate zulip.js, template whitespace, use example.com in tests, etc.

**Tim Abbott** · 2016-08-27 00:20 UTC

and we can try to hit a few every week

**Steve Howell** · 2016-08-27 00:20 UTC

Are there any subtleties there in terms of loading order?  I don't have a good grasp on JS startup.

**Tim Abbott** · 2016-08-27 00:20 UTC

zprojects/settings.py has the loading order

**Tim Abbott** · 2016-08-27 00:20 UTC

but basically it's not too hard to get right.

**Steve Howell** · 2016-08-27 00:21 UTC

alright, maybe paper is the best tool for this, huh?  better than github, at least

**Tim Abbott** · 2016-08-27 00:21 UTC

yeah, could imagine doing a central GitHub issue with checkboxes

**Tim Abbott** · 2016-08-27 00:22 UTC

but paper is probably a better workflow

**Steve Howell** · 2016-08-27 00:23 UTC

yeah, I think it's helpful to slice and dice...the other way of doing it would be an orphaned .md file under git control, where we can back-and-forth a bit on priorities via commits, but that might be slightly heavy

**Steve Howell** · 2016-08-27 00:24 UTC

kinda a subset of roadmap.md

**Steve Howell** · 2016-08-27 00:25 UTC

rock, scissors, paper to decide, haha?

**Steve Howell** · 2016-08-27 00:27 UTC

https://paper.dropbox.com/doc/Code-cleanup-tasks-G6VVavGbgriCvukAP81ha

**Tim Abbott** · 2016-08-27 00:38 UTC

A lot of those have open issues, BTW (roadmap technical debt section will find some)

**Steve Howell** · 2016-08-27 00:59 UTC

cool, about to fork the last part of this traffic to "code cleanup" for searchability (it's not really tools any more, but whatever)

**Gordon P. Hemsley** · 2016-08-29 02:09 UTC

I've filed two PRs that kinda fall into the category of general code cleanup

**Gordon P. Hemsley** · 2016-08-29 02:09 UTC

https://github.com/zulip/zulip/pull/1729

**Gordon P. Hemsley** · 2016-08-29 02:09 UTC

https://github.com/zulip/zulip/pull/1730

**Steve Howell** · 2016-08-29 02:38 UTC

Are you sure you are handling the case of `<foo>x`?  That's what the state.depth check is for. (I am only skimming the code, so I may just be missing something you fixed, or I might be mis-remembering something.)

**Steve Howell** · 2016-08-29 02:46 UTC

BTW if you are interested in further hacking on template_parser.py and further code cleanup, I have the perfect project for you! We are gonna try to clean up all the indentation in the Django templates to four-space templates. I can help you with it if you want to take it on. If not, no sweat!

**Gordon P. Hemsley** · 2016-08-29 04:58 UTC

Hmm, you may be right about <foo>x. I'll have to trace that path again.

**Gordon P. Hemsley** · 2016-08-29 05:49 UTC

Yup, `state.depth` is non-zero if there are unclosed tags. I've updated the check and added another test.

**Gordon P. Hemsley** · 2016-08-29 05:51 UTC

And sure, I'm interested in hearing more about the project.

**Gordon P. Hemsley** · 2016-08-29 12:50 UTC

I have to say, though, this coverage calculator is rather naive.

**Gordon P. Hemsley** · 2016-08-29 12:50 UTC

it doesn't check branch points

**Gordon P. Hemsley** · 2016-08-29 12:50 UTC

it only checks lines

**Gordon P. Hemsley** · 2016-08-29 12:50 UTC

which can be very misleading

**Gordon P. Hemsley** · 2016-08-29 12:51 UTC

and can result in unknowingly undertested code

**Steve Howell** · 2016-08-29 13:52 UTC

Yeah, we take the coverage reports with a grain of salt.  We also do a fair amount of end-to-end testing, which can generate a lot of superficial coverage of code without precisely targeting some of the deeper methods.

**Steve Howell** · 2016-08-29 13:54 UTC

So for the project I mentioned last night, we basically want to clean up all of our Django templates to be 4-space indents.  Part of our proposed process for making that happen is to make template_parser more strict about formatting.  Right now it checks whether tags match, but it doesn't enforce anything about deeply they are indented.

Also, in order to fix the templates, we might try to use some of he code from template_parser to aid in the pretty printing.

**Gordon P. Hemsley** · 2016-08-30 22:05 UTC

Part of the reason I mentioned the coverage problem is because I've seen a Perl coverage calculator that was much more thorough in its analysis, checking each branch of a conditional and such.

**Gordon P. Hemsley** · 2016-08-30 22:05 UTC

And I thought surely this can't be all there is for Python

**Steve Howell** · 2016-08-30 22:44 UTC

JS also has tools that do branch coverage.  I'm not sure what the state of the world of Python coverage tools is.  We're still far away from 100% line coverage that branch coverage isn't a big priority.

**Gordon P. Hemsley** · 2016-08-30 22:45 UTC

hmm, I suppose

**Steve Howell** · 2016-08-30 22:46 UTC

I mean it would be nice--don't get me wrong--just not on the top of the list.

**Gordon P. Hemsley** · 2016-08-30 22:46 UTC

Just wanted to make sure that it was known that 100% line coverage didn't actually mean 100% coverage.

**Gordon P. Hemsley** · 2016-08-30 22:47 UTC

And also, it makes it harder to write tests if you're not sure if you're covering everything.

**Gordon P. Hemsley** · 2016-08-30 22:47 UTC

But then again, maybe I'm just thorough.

**Gordon P. Hemsley** · 2016-08-30 22:50 UTC

how strict are the word-wrap rules for commit messages?

**Gordon P. Hemsley** · 2016-08-30 22:52 UTC

ah nevermind, I'll just listen to them

**Steve Howell** · 2016-08-30 22:52 UTC

http://zulip.readthedocs.io/en/latest/version-control.html#commit-messages

**Gordon P. Hemsley** · 2016-08-30 22:53 UTC

well yes, those are the rules I'm referring to

**Steve Howell** · 2016-08-30 22:55 UTC

They are human-enforced, and this week is the human is most likely me.  We are talking about maybe automating a little bit of the commit-message guidelines.

**Gordon P. Hemsley** · 2016-08-30 23:02 UTC

alright, I've updated the PR: https://github.com/zulip/zulip/pull/1730

**Steve Howell** · 2016-08-30 23:03 UTC

looking now, but gotta restart my browser, back in a bit

**Gordon P. Hemsley** · 2016-08-30 23:05 UTC

oh, apparently adding branch coverage is merely a configuration change

**Gordon P. Hemsley** · 2016-08-30 23:05 UTC

https://coverage.readthedocs.io/en/coverage-4.1/config.html#run

**Gordon P. Hemsley** · 2016-08-30 23:06 UTC

or passing in `--branch`

**Gordon P. Hemsley** · 2016-08-30 23:06 UTC

that seems easy enough

**Steve Howell** · 2016-08-30 23:07 UTC

Good to know.

**Gordon P. Hemsley** · 2016-08-30 23:09 UTC

or adding `branch=True` to a `Coverage()` call

**Gordon P. Hemsley** · 2016-08-30 23:10 UTC

that's enlightening

**Gordon P. Hemsley** · 2016-08-30 23:11 UTC

I wonder why that's not the default

**Steve Howell** · 2016-08-30 23:14 UTC

I think sometimes it's really tough to get 100% branch coverage, but 100% line coverage is more achievable, so pragmatic considerations come into play.

**Gordon P. Hemsley** · 2016-08-30 23:14 UTC

shrug

**Steve Howell** · 2016-08-30 23:14 UTC

I mean, even if you get 100% branch coverage, that's still not 100% universe-of-possible-inputs coverage.

**Gordon P. Hemsley** · 2016-08-30 23:14 UTC

true

**Gordon P. Hemsley** · 2016-08-30 23:15 UTC

I dunno, I guess I just don't see line coverage as a particularly helpful metric

**Steve Howell** · 2016-08-30 23:16 UTC

I think the end game for us is to have some kind of staged policy:
* a module that's not 100% covered can be exempt if we know it's really old, stable code
* once we get 100% line coverage on something, enforce no regressions in line coverage
* once we start getting a lot modules up to 100% line coverage, raise the bar to branch coverage

**Gordon P. Hemsley** · 2016-08-30 23:16 UTC

hmm

**Gordon P. Hemsley** · 2016-08-30 23:17 UTC

well, each separate testing file calls `Coverage()` on its own

**Gordon P. Hemsley** · 2016-08-30 23:17 UTC

so any change doesn't have to be across the board

**Steve Howell** · 2016-08-30 23:17 UTC

for us it's really helpful, because in order to get 100% coverage on our views, you have to eventually write tests that force negative HTTP responses

**Gordon P. Hemsley** · 2016-08-30 23:17 UTC

ah, hmm

**Gordon P. Hemsley** · 2016-08-30 23:18 UTC

I guess I'm narrowly scoped to these commandline scripts at the moment

**Steve Howell** · 2016-08-30 23:18 UTC

yeah, as of about three weeks ago, we had no tests on those at all, but they also hadn't changed in 3 years, because they were doing a fairly simple job until I started mucking with them recently

**Gordon P. Hemsley** · 2016-08-30 23:18 UTC

:)

**Gordon P. Hemsley** · 2016-08-30 23:18 UTC

I noticed that after I dove in

**Steve Howell** · 2016-08-30 23:19 UTC

So for your fourth commit, would you mind amending the message just a bit?  I think you can simply say "Clean up end-tag handling in template parsing" and possibly elaborate in the message itself.

**Steve Howell** · 2016-08-30 23:20 UTC

All four commits are awesome, by the way.  Much appreciated.

**Gordon P. Hemsley** · 2016-08-30 23:20 UTC

yeah, I wasn't sure how detailed the commit messages need to be, because I'm not familiar with the codebase

**Gordon P. Hemsley** · 2016-08-30 23:21 UTC

I just found a ticket that seemed doable and it led me to these tools

**Steve Howell** · 2016-08-30 23:21 UTC

Cool deal.  Yeah, basically we want the first line to be concise and scannable, and then after that as much detail as you think it warrants.

**Gordon P. Hemsley** · 2016-08-30 23:22 UTC

uh oh, did I break a test?

**Gordon P. Hemsley** · 2016-08-30 23:22 UTC

I don't understand how to read coveralls

**Steve Howell** · 2016-08-30 23:23 UTC

I think that's just a byproduct of our coveralls check being kind of stupid when it comes to changes that only affect tools.

**Steve Howell** · 2016-08-30 23:24 UTC

I can push your changes despite that.

**Gordon P. Hemsley** · 2016-08-30 23:24 UTC

alright, cool

**Gordon P. Hemsley** · 2016-08-30 23:24 UTC

lemme fix that commit message

**Tim Abbott** · 2016-09-06 17:45 UTC

@Gordon P. Hemsley I just got back from my trip and saw your work on testing our scripts -- awesome, thanks for doing that!

**Gordon P. Hemsley** · 2016-09-09 20:09 UTC

@Tim Abbott you're welcome :)

**Gordon P. Hemsley** · 2016-09-09 20:09 UTC

more to come

**Gordon P. Hemsley** · 2016-09-11 05:07 UTC

@Steve Howell re https://github.com/zulip/zulip/commit/0f8d014096aac93f51dc4db989a199feabb94f4d

**Gordon P. Hemsley** · 2016-09-11 05:07 UTC

Was there a reason you put `HtmlTreeBranch` and its related functions in template_parser instead of html_grep?

**Gordon P. Hemsley** · 2016-09-11 05:08 UTC

(template_parser doesn't actually use any of it)

**Steve Howell** · 2016-09-11 13:51 UTC

I think `HtmlTreeBranch` is general purpose, so it doesn't make sense to bury in `html_grep.py`, which is really only intended to implement the optimized Grepper class that loads up a big dictionary to handle multiple searches.  On the other hand, I see your point that it looks kind of funny to have the code in template_parser.py now when nobody's using it yet.  One thing to consider is to split out a third module called `html_branches.py` or something like that.  Under the hood the grep code code eventually calls tokenize(), so splitting out a third module won't really break any dependencies for the grepper, but it would make the parser  module slimmer for its main use case, which is linting.

**Gordon P. Hemsley** · 2016-09-11 14:52 UTC

Alright, I think I'm gonna do that. There are some other adjustments I'm going to make to it, too, to make it play nicer with testing.

**Gordon P. Hemsley** · 2016-09-11 14:54 UTC

Out of curiosity, do we have a linter for Python code? We seem to have a lot of inconsistencies.

**Steve Howell** · 2016-09-11 14:54 UTC

We use `pyflakes` for Python linting.

**Gordon P. Hemsley** · 2016-09-11 14:55 UTC

"Pyflakes makes a simple promise: it will never complain about style"

**Gordon P. Hemsley** · 2016-09-11 14:55 UTC

"If you like Pyflakes but also want stylistic checks, you want flake8, which combines Pyflakes with style checks against PEP 8 and adds per-project configuration ability."

**Steve Howell** · 2016-09-11 15:00 UTC

Our big push on the Python front now is `mypy`.  There are some style inconsistencies in the code, but we mostly check for human readability via code review.

**Steve Howell** · 2016-09-11 15:01 UTC

Before refactoring the HTML grep stuff, it might be helpful to try using it with a couple different searches and get some timings on it, and maybe stash off the output.

**Gordon P. Hemsley** · 2016-09-11 15:02 UTC

My change is really just limited to abstracting out the dependency on file loading

**Steve Howell** · 2016-09-11 15:04 UTC

Cool, you still might want a before/after test.

**Gordon P. Hemsley** · 2016-09-11 15:31 UTC

What's better, multiple small PRs or one big PR?

**Steve Howell** · 2016-09-11 15:32 UTC

small for review, then we can always squash them before merging

**Steve Howell** · 2016-09-11 15:33 UTC

Also, you are welcome to submit draft PRs for early review.

**Gordon P. Hemsley** · 2016-09-11 15:34 UTC

well my question is really, should I create a PR now and wait for it to be merged, or just keep working on the same branch and create a PR with a large number of commits later?

**Steve Howell** · 2016-09-11 15:36 UTC

Keep working on the same branch.  If you get early commits submitted that we think are ready to merge, we will just merge them and have you rebase.   Occasionally, if a PR starts getting really cluttered, we'll open a new PR with a new branch, but we're pretty used to managing it all as one branch.

**Gordon P. Hemsley** · 2016-09-11 15:36 UTC

so create the PR early (now)?

**Steve Howell** · 2016-09-11 15:37 UTC

yeah, and just flag it as wip

**Gordon P. Hemsley** · 2016-09-11 15:38 UTC

actually, come to think of it, these two things aren't all that related after all

**Gordon P. Hemsley** · 2016-09-11 15:39 UTC

https://github.com/zulip/zulip/pull/1773

**Steve Howell** · 2016-09-11 15:39 UTC

looking now

**Steve Howell** · 2016-09-11 15:43 UTC

awesome, about to merge

**Gordon P. Hemsley** · 2016-09-11 15:43 UTC

cool

**Steve Howell** · 2016-09-11 15:53 UTC

One thing that would be helpful is if you could sweep the tools/lib and tools/test code for missing mypy annotations.  I think there are only a few missing.  I'd fix them myself, but they may churn a bit if you extract out some of the html stuff to its own file.

**Gordon P. Hemsley** · 2016-09-11 15:53 UTC

alright, I'll look into it

**Steve Howell** · 2016-09-11 15:54 UTC

We are also getting this error:

```

tools/tests/test_css_parser.py: note: In member "test_no_semicolon" of class "ParserTestHappyPath":
tools/tests/test_css_parser.py:59: error: Some element of union has no attribute "declaration_block"
```

**Gordon P. Hemsley** · 2016-09-11 15:55 UTC

what's generating that?

**Steve Howell** · 2016-09-11 15:55 UTC

`./tools/run-mypy --py3`

**Gordon P. Hemsley** · 2016-09-11 15:55 UTC

hmm, ok

**Steve Howell** · 2016-09-11 15:56 UTC

It runs in Travis, but not in lint-all, just because it's kinda slow.

**Gordon P. Hemsley** · 2016-09-11 15:56 UTC

gotcha

**Steve Howell** · 2016-09-11 15:56 UTC

https://travis-ci.org/zulip/zulip/jobs/159127987

**Steve Howell** · 2016-09-11 15:57 UTC

You have to work around it with cast().

**Gordon P. Hemsley** · 2016-09-11 15:57 UTC

ah, I see

**Gordon P. Hemsley** · 2016-09-11 15:57 UTC

I was wondering what the purpose of that was

**Gordon P. Hemsley** · 2016-09-11 15:58 UTC

I'll fix that in a moment

**Steve Howell** · 2016-09-11 15:58 UTC

sounds good

**Steve Howell** · 2016-09-11 16:06 UTC

I'm gonna back your changes out from master.  I should have waited for Travis to finish before pushing them.  Still on my first cup of coffee.

**Gordon P. Hemsley** · 2016-09-11 16:06 UTC

sure

**Steve Howell** · 2016-09-11 16:09 UTC

I didn't close the PR yet, so you should be able to rebase the mypy cast thing on to your first change and force-push your branch again.

**Gordon P. Hemsley** · 2016-09-11 16:09 UTC

ok

**Gordon P. Hemsley** · 2016-09-11 16:46 UTC

@Steve Howell Alright, fixed the commit and force pushed.

**Gordon P. Hemsley** · 2016-09-11 16:49 UTC

https://travis-ci.org/zulip/zulip/jobs/159136880

**Gordon P. Hemsley** · 2016-09-11 17:06 UTC

hmm... it seems we have screwed up the history with all these force pushes

**Gordon P. Hemsley** · 2016-09-11 17:07 UTC

I guess you did a rebase or something?

**Steve Howell** · 2016-09-11 17:08 UTC

yeah, I pushed your original set, then force-pushed HEAD^^^, then pushed your new set

**Gordon P. Hemsley** · 2016-09-11 17:09 UTC

well I force-pushed my branch to clean up my local history, and now the PR is empty

**Gordon P. Hemsley** · 2016-09-11 17:09 UTC

(and got automatically closed)

**Steve Howell** · 2016-09-11 17:10 UTC

yeah, I believe that's what should actually happen, since you should now see your 3 commits on master

**Gordon P. Hemsley** · 2016-09-11 17:11 UTC

well yeah, it just means you can't go back to the PR to see the commits that were involved

**Tim Abbott** · 2016-09-11 17:31 UTC

yeah, GitHub's UI does a lot of things that aren't right for our workflow.  Probably the most embarrassing is that they sort commits in the PR display by creation time, not by the order they actually appear in the branch, which is super confusing (any easy for them to fix -- just change the sort order to be topological rather than by timestamp)

**Tim Abbott** · 2016-09-11 17:33 UTC

One of the things that makes me sad about using a proprietary tool; there's a bug report that a friend filed with a clear explanation of the issue and clear advice on how to fix the issue, and it seems structurally clear it's strictly an improvement to something a lot of people complain about, but workflow improvements in general are not a priority for GitHub right now, so they aren't going to ever fix it.

**Gordon P. Hemsley** · 2016-09-11 18:27 UTC

https://github.com/zulip/zulip/pull/1775

**Gordon P. Hemsley** · 2016-09-11 18:30 UTC

sigh

**Gordon P. Hemsley** · 2016-09-11 18:30 UTC

heisenberg test failures

**Steve Howell** · 2016-09-11 18:31 UTC

pgroonga?

**Gordon P. Hemsley** · 2016-09-11 18:31 UTC

no, mypy

**Gordon P. Hemsley** · 2016-09-11 18:31 UTC

apparently I failed to run it with the code in its current state

**Steve Howell** · 2016-09-11 18:34 UTC

Oh yeah, I've run into that.  So mypy is still kinda beta.  I've had trouble running it against a single file and getting it to report errors consistently.

**Gordon P. Hemsley** · 2016-09-11 18:34 UTC

oh, no, this is human error

**Gordon P. Hemsley** · 2016-09-11 18:34 UTC

I kept changing the code, and forgot to rerun

**Gordon P. Hemsley** · 2016-09-11 18:37 UTC

I'm also running into module import syntax issues

**Gordon P. Hemsley** · 2016-09-11 18:37 UTC

different scripts require different imports

**Steve Howell** · 2016-09-11 18:43 UTC

So what happens if you run html_grep now and one of the files is unparsable?  Will it report the filename in the error output?

**Gordon P. Hemsley** · 2016-09-11 18:43 UTC

Did it do that before?

**Steve Howell** · 2016-09-11 18:49 UTC

Huh, I guess not.  We might want to call validate() in html_tag_tree() some day in the future, because the grep results are gonna be kind of broken if your HTML is messed up.

**Gordon P. Hemsley** · 2016-09-11 18:50 UTC

Alright, well, I've pushed the update to fix the errors. Testing is running now, but it looks like it'll be good.

**Gordon P. Hemsley** · 2016-09-11 18:54 UTC

It also comes with 99% test coverage, and I believe the remaining 1% is a bug in the code.

**Steve Howell** · 2016-09-11 18:54 UTC

For a fairly big code move like this, I would make the commit message include detail on anything that you changed apart from trivial stuff like moving code from file to file or adjusting imports.

**Gordon P. Hemsley** · 2016-09-11 18:55 UTC

I tried to avoid changing anything. I think the only significant thing I changed was the signature for html_branches(), which is only used by html_grep. Do you want me to notate that?

**Steve Howell** · 2016-09-11 18:56 UTC

yes, please...what was the bug?

**Gordon P. Hemsley** · 2016-09-11 18:56 UTC

the reason I changed it?

**Gordon P. Hemsley** · 2016-09-11 18:56 UTC

or do you mean with the test coverage?

**Steve Howell** · 2016-09-11 18:57 UTC

whatever you meant by the "1%" thing

**Gordon P. Hemsley** · 2016-09-11 18:57 UTC

There is a check that will always be true because it's already guarded against elsewhere

**Steve Howell** · 2016-09-11 18:58 UTC

can we turn it into an assertion then?

**Gordon P. Hemsley** · 2016-09-11 18:58 UTC

in `html_tag_tree`

**Gordon P. Hemsley** · 2016-09-11 18:58 UTC

we could, sure

**Gordon P. Hemsley** · 2016-09-11 18:58 UTC

I didn't do anything to it in this commit

**Steve Howell** · 2016-09-11 18:58 UTC

oh, I see, it's just not testable yet is what you're saying

**Steve Howell** · 2016-09-11 18:59 UTC

which check?

**Gordon P. Hemsley** · 2016-09-11 18:59 UTC

yeah, it's just that the False branch will never be followed

**Gordon P. Hemsley** · 2016-09-11 18:59 UTC

`if not is_special_html_tag(token.s, token.tag):`

**Gordon P. Hemsley** · 2016-09-11 19:00 UTC

since special html tags get a kind of `html_special`, that will never be false

**Steve Howell** · 2016-09-11 19:00 UTC

oh, that is a bug

**Steve Howell** · 2016-09-11 19:01 UTC

the way we treat special tags got upstreamed to the tokenizer, and I must have forgotten to fix that code

**Steve Howell** · 2016-09-11 19:02 UTC

The code still probably works, but it can now be simplified to a flat if/elif with just three cases.

**Gordon P. Hemsley** · 2016-09-11 19:03 UTC

well, one thing at a time

**Steve Howell** · 2016-09-11 19:03 UTC

yeah, I agree, one thing at a time

**Gordon P. Hemsley** · 2016-09-11 19:04 UTC

alright, commit message updated

**Steve Howell** · 2016-09-11 20:40 UTC

Cool, I just pushed your changes as well as a small change to remove the `is_special_html_tag` dead code.

**Gordon P. Hemsley** · 2016-09-11 21:35 UTC

that brings html_branches to 100% coverage

**Gordon P. Hemsley** · 2016-09-11 21:35 UTC

though you forgot to remove it from the import

**Sumana Harihareswara** · 2016-09-11 23:01 UTC

@Tim Abbott How long ago did your friend file that bug report, about how GitHub should sort the commits (in pull request display) topologically rather than by creation timestamp? I could ping a couple people I know at GitHub who are working on making GitHub better for FLOSS maintainers, in case another voice helps. I know it's somewhat unlikely, but it might help.

**Tim Abbott** · 2016-09-11 23:31 UTC

https://github.com/isaacs/github/issues/386 is the relevant issue thread; Anders Kaseorg is the friend.

**Sumana Harihareswara** · 2016-09-12 02:07 UTC

cool, thanks


## python coding standards

*2016-09-12 to 2016-09-12 · 72 messages · [open in Zulip](https://chat.zulip.org/#narrow/channel/18-tools/topic/python.20coding.20standards/with/23249)*

**Gordon P. Hemsley** · 2016-09-12 01:27 UTC

mypy type declarations require including classes in a file that are used in type declarations, even if they aren't used directly in any code. This will directly conflict with any tool (like flake8) that reports on imports that aren't used. I'd like to propose that we list all type-specific imports separately, before any code-related imports.

**Gordon P. Hemsley** · 2016-09-12 01:27 UTC

For example, undoing the change that was made here: https://github.com/zulip/zulip/commit/98ac51d07deedf7add50713002b09d002b63b077

**Gordon P. Hemsley** · 2016-09-12 01:29 UTC

Put another way, PEP 8 lists the order that imports should occur: http://legacy.python.org/dev/peps/pep-0008/#imports

**Gordon P. Hemsley** · 2016-09-12 01:30 UTC

I propose adding to that list:
*   **Imports for future-proofing (`__future__`, `six`, etc.)**
*   **Imports for types (`typing`, classes only required for `mypy`)**
*   standard library imports
*   related third party imports
*   local application/library specific imports

**Gordon P. Hemsley** · 2016-09-12 01:35 UTC

I'd also like to discuss the ramifications of requiring the `from` syntax for imports, which requires explicit enumeration of every class/function, and which brings everything into the current "namespace" scope

**Steve Howell** · 2016-09-12 02:00 UTC

Regarding mypy, we are kind of on the bleeding edge of its evolution, so I think there are some things now that now appear kind of hacky that will improve over time, like they may figure out a better solution for annotating types that aren't otherwise imported.

**Steve Howell** · 2016-09-12 02:08 UTC

If we were to eliminate the "from" syntax, we wouldn't completely eliminate the chance of name collisions.  Our module names tend to be short--export, import, upload, streams, messages.  Our function names tend to be longer and more descriptive.  The "from" syntax, while polluting the module namespace, does have advantages--it makes most of the code more brief, and it makes you explicitly declare your dependencies.

**Steve Howell** · 2016-09-12 02:26 UTC

If you look at our git logs and search for "fix" you will see the kind of problems that have tended to plague Zulip in the past, and namespace collisions is really not one of them.  We have all kinds of problems with fiddly CSS, plus more high-level system stuff like dealing with third-party systems like jquery/tornado/rabbitmq/pgroonga, things that only break in Vagrant, etc.  Caching, of course, is always complicated, and we occasionally have idempotency-related bugs.  Both of our upgrade issues were essentially caused by re-arranging directory structures, which were positive changes, but hard to test.

**Steve Howell** · 2016-09-12 02:41 UTC

It's also interesting to look at the currently open bugs: https://github.com/zulip/zulip/issues?utf8=%E2%9C%93&q=is%3Aissue%20is%3Aopen%20label%3Abug

**Tim Abbott** · 2016-09-12 05:14 UTC

Yeah, I can't think of a time we've had a problem with namespace collision.

re: mypy type declarations, it's worth noting that the problem will in some sense go away when we move to Python 3 only and start using the nicer Python 3 type syntax, since the type-related imports will actually be required.

**Tim Abbott** · 2016-09-12 05:15 UTC

(Since with the Python 3 typing syntax, the types are accessible at runtime)

**Tim Abbott** · 2016-09-12 05:19 UTC

Back to the topic of the `from` import syntax, one problem you get fairly quickly the other way is that code gets really verbose really fast (it's very hard to avoid most lines needing to be wrapped, which makes code harder to read).  If you look at large Python codebases (Django, Flask, SQLAlchemy are the 3 I sampled just now), they largely use the `from` style that Zulip is using, and I think for good reason.

**Tim Abbott** · 2016-09-12 05:20 UTC

I would be generally on board for the project of reordering/reorganizing our imports to match the PEP 8 standard ordering, though I would much prefer to do that after a coordinated effort to merge open PRs, to minimize the cost in terms of rebase pain for merging those PRs eventually.

**Tim Abbott** · 2016-09-12 05:23 UTC

FYI, `pyflakes` (The linter we already use) reports on unused imports, and you can see them with `tools/lint-all --full`.  We do periodic batch purges of extraneous stuff using that option, which I find to be a pretty efficient balance in terms of avoiding clutter from too many unnecessary imports (which are mostly harmless) without making every contributor have to remove imports all the time to get their code to pass the linter.

**Tim Abbott** · 2016-09-12 05:24 UTC

(though I suppose the addition of mypy has made that approach now useless/painful)

**Tim Abbott** · 2016-09-12 05:25 UTC

My hope is that we'll just move to full python 3 soon; our entire test suite passes on Python 3 and has for months, so we just need to do production testing to support Python 3 in production; and then not too long after we should be able to drop Python 2...

**Gordon P. Hemsley** · 2016-09-12 22:28 UTC

@Tim Abbott `flake8` is a wrapper around `pyflakes` as well as `pycodestyle` and `mccabe`, so I would expect overlap.

**Tim Abbott** · 2016-09-12 22:29 UTC

yeah, makes sense

**Gordon P. Hemsley** · 2016-09-12 22:29 UTC

FWIW, I don't consider having to remove unused imports as a particularly high burden

**Steve Howell** · 2016-09-12 22:29 UTC

We should definitely do an imports sweep some time soon.  I think we can probably have a "remove cruft sprint" sometime soon.

**Gordon P. Hemsley** · 2016-09-12 22:30 UTC

my intent was to run flake8 on tools/ and clean up all that it reports in a single commit

**Gordon P. Hemsley** · 2016-09-12 22:31 UTC

I was also gonna take care of the missing type defs, but I guess that's taken care of now?

**Tim Abbott** · 2016-09-12 22:31 UTC

yep all done :)

**Tim Abbott** · 2016-09-12 22:32 UTC

Cool, let me take a look at the flake8 output

**Tim Abbott** · 2016-09-12 22:32 UTC

I would consider doing a cleanup for this: `$ flake8 tools/  | grep -v E501 | grep -v E302 | grep -v F401`

**Steve Howell** · 2016-09-12 22:33 UTC

The next big thing with the tools code is to pretty-print all the HTML and then lock down the linters.  After that, the next big thing is CSS cleanup, but there are more moving parts there in terms of people/decisions.  All the stuff that @Gordon P. Hemsley has done recently sets the stage perfectly for ramping up our tooling.  We have virtually 100% coverage plus better organized code.

**Gordon P. Hemsley** · 2016-09-12 22:34 UTC

@Tim Abbott `python3 -m flake8 --max-line-length=120 --exclude deprecated tools/` is what I was using

**Gordon P. Hemsley** · 2016-09-12 22:34 UTC

@Steve Howell FYI, html_grep is missing tests

**Steve Howell** · 2016-09-12 22:34 UTC

Gordon, do you have any thoughts on making the tools test runner stuff better?

**Gordon P. Hemsley** · 2016-09-12 22:35 UTC

`test-tools`? better how?

**Steve Howell** · 2016-09-12 22:36 UTC

The html_grep stuff is definitely a work in progress.

**Steve Howell** · 2016-09-12 22:37 UTC

Re `test-tools` it doesn't allow us to just run one test, and the output is crappy out-of-the-box unittest kind of stuff where if a test fails you have to scroll up to see the actual output if you do any kind of print debugging.

**Gordon P. Hemsley** · 2016-09-12 22:37 UTC

ah

**Gordon P. Hemsley** · 2016-09-12 22:37 UTC

I'd have to think about that

**Steve Howell** · 2016-09-12 22:38 UTC

It's not a super easy problem, so, yeah, think about it. :)  It's not urgent; it's still mostly a nuisance for now, because the tests run super fast, and print debugging is kinda lame.

**Tim Abbott** · 2016-09-12 22:38 UTC

OK, I would probably also consider not doing:
* E302 (the entire codebase uses 1 blank line between defs, and I want to think about it more before changing part of it to work differently), 
* F401 (because of mypy false positives)
* E261 (because it seems most of the things it flags are type comments, where I think our 1-space style is standard)

some of the others random things it flags are probably also going to have to stay for various reasons (e.g. imports later in the file because we need to have code to update `sys.path` to find them)

**Tim Abbott** · 2016-09-12 22:39 UTC

(you can just use `--ignore=E302`, for example, to exclude a rule)

**Gordon P. Hemsley** · 2016-09-12 22:39 UTC

FYI, the stuff it checks for are listed in PEP8

**Steve Howell** · 2016-09-12 22:43 UTC

/me remembers the days before PEP8 when he had to sew his own clothes and could notate years with two digits

**Tim Abbott** · 2016-09-12 22:43 UTC

I'm aware the linter is based on PEP8, however, PEP8 is not perfect.  For example, as I mentioned, putting all the imports at the top of the file doesn't work for certain scripts that need to update `sys.path` inside the script.

The mypy thing comes from: https://github.com/python/mypy/blob/master/docs/source/cheat_sheet.rst

**Tim Abbott** · 2016-09-12 22:44 UTC

I do think we should try to avoid differing from PEP-8 except where there's a good reason

**Gordon P. Hemsley** · 2016-09-12 22:45 UTC

if you're mentioning the cheat sheet in reference to spaces before inline comments, I'll note that document is not internally consistent

**Tim Abbott** · 2016-09-12 22:46 UTC

yeah.  It's possible we should just submit a PR to update that cheat sheet to 2-spaces and move our codebase to 2-spaces.  But I guess my larger issue is that I kinda want to avoid different corners of the codebase all having randomly different Python styles

**Gordon P. Hemsley** · 2016-09-12 22:46 UTC

I think it already does, that's why I brought it up in the first place ;)

**Tim Abbott** · 2016-09-12 22:47 UTC

So for a few big things that I happen to know the entire codebase has a fairly consistent convention (E302 and E261 being the main ones), I'd prefer to avoid migrating one portion at a time.

**Tim Abbott** · 2016-09-12 22:48 UTC

Our codebase is still small enough that one can do big migrations for things like this, and I'd rather do the big migration to make things consistent than do the slow-churn-over-2-years thing that a lot of projects do for style things

**Gordon P. Hemsley** · 2016-09-12 22:49 UTC

sure

**Gordon P. Hemsley** · 2016-09-12 22:49 UTC

and I'm not suggesting that we enforce flake8 output

**Gordon P. Hemsley** · 2016-09-12 22:49 UTC

merely use it as a guide

**Gordon P. Hemsley** · 2016-09-12 22:49 UTC

it does have bugs, anyway

**Gordon P. Hemsley** · 2016-09-12 22:50 UTC

I filed this, for example: https://github.com/PyCQA/pycodestyle/issues/571

**Tim Abbott** · 2016-09-12 22:50 UTC

yeah

**Tim Abbott** · 2016-09-12 22:51 UTC

Some of its rules aren't spammy, but I'd be happy to lock down in CI any that demonstrably basically aren't (by not having false positives on our codebase)

**Tim Abbott** · 2016-09-12 22:52 UTC

Which one can do with `flake8 --select` I guess

**Gordon P. Hemsley** · 2016-09-12 22:52 UTC

see https://pycodestyle.readthedocs.io/en/latest/intro.html#error-codes for the list

**Tim Abbott** · 2016-09-12 22:53 UTC

Cool

**Steve Howell** · 2016-09-12 22:53 UTC

I'd like to reiterate one big-picture thing.  Our Python code, while not perfect, is probably the least of Zulip's problems.  We have way grosser problems with things like CSS (organization), templates (formatting), and JS (structure).  So we should all apply our talents to the most leveraged problems.

**Gordon P. Hemsley** · 2016-09-12 22:54 UTC

@Tim Abbott Ooh, and the section above shows how to use a config file to set parameters

**Tim Abbott** · 2016-09-12 22:55 UTC

Agreed with that :).  I also don't want to applying stop energy to doing python code style consistency work, since it does have value; but I would encourage using a systematic approach to make it easy to code review (e.g. fix only 1 rule in a give commit so you can review a bunch of self-similar stuff together), and I would probably skip any rule that has a ton of violations like this in the codebase overall without chatting about it:
```
$ flake8 --select=E302 ./ | wc
   1570   12560  115372
```
since we'll want to think hard about whether or not it's worth doing such a migration and if so, how to do it without making merge conflicts galore.

**Tim Abbott** · 2016-09-12 22:56 UTC

I'd love to have us put together a little config file and framework that provides a clear process for adding another one of those rules and locking it down (if the rule seems good)

**Tim Abbott** · 2016-09-12 22:57 UTC

Since then we can have a pretty fast repeatable process for clearing things out

**Gordon P. Hemsley** · 2016-09-12 22:57 UTC

```
$ python3 -m flake8 --max-line-length=120 --exclude=deprecated --ignore=E302,E261,F401 --statistics -qq | sort -nr
667   E251 unexpected spaces around keyword / parameter equals
318   E501 line too long (121 > 120 characters)
220   E128 continuation line under-indented for visual indent
135   E402 module level import not at top of file
114   E241 multiple spaces after ','
112   E126 continuation line over-indented for hanging indent
110   E221 multiple spaces before operator
```

**Steve Howell** · 2016-09-12 22:58 UTC

Another big-picture thing to think about that's only in the scope of Python is that our problems there are also mostly structural.  We have some pretty big Python modules that could be split up.  Splitting up Python modules is a non-trivial task, so there might be tooling opportunities there.

**Gordon P. Hemsley** · 2016-09-12 23:00 UTC

(the `--statistics` parameter is a little flawed, as it only prints the first occurrence of a variable error description)

**Gordon P. Hemsley** · 2016-09-12 23:01 UTC

fun fact: you can use an error prefix to get all the errors under it

**Gordon P. Hemsley** · 2016-09-12 23:01 UTC

e.g. `--select=E2`

**Tim Abbott** · 2016-09-12 23:02 UTC

nice

**Gordon P. Hemsley** · 2016-09-12 23:03 UTC

E7 is probably a good one to enforce

**Tim Abbott** · 2016-09-12 23:04 UTC

yeah most of those sound bad

**Gordon P. Hemsley** · 2016-09-12 23:05 UTC

also, there appears to be a bug where `--select` will still include `F` unless you explicitly `--ignore=F`

**Tim Abbott** · 2016-09-12 23:06 UTC

I guess we'll get some opportunities to report a bunch of bugs in that ecosystem.  Probably good for them :)

**Gordon P. Hemsley** · 2016-09-12 23:06 UTC

yeah


## pretty printer

*2016-09-12 to 2016-09-12 · 2 messages · [open in Zulip](https://chat.zulip.org/#narrow/channel/18-tools/topic/pretty.20printer/with/23283)*

**Steve Howell** · 2016-09-12 11:20 UTC

@Tim Abbott @Gordon P. Hemsley I have started to work on the HTML pretty printer.  Here's an early look:

https://github.com/zulip/zulip/pull/1778/files

I need to add handling for template tags and package up a tool.

**Tim Abbott** · 2016-09-12 14:50 UTC

cool!


## generic code cleanup engine

*2016-09-12 to 2016-09-13 · 41 messages · [open in Zulip](https://chat.zulip.org/#narrow/channel/18-tools/topic/generic.20code.20cleanup.20engine/with/23581)*

**Steve Howell** · 2016-09-12 23:36 UTC

@Gordon P. Hemsley @Tim Abbott 
For some of the code cleanup that we're about to do-things like PEP8 and template indentation--it would be nice to have an engine that does this:
- make sure your git branch is clean
- run a cleanup tool against one file at a time, overwriting the file as needed
- check in the change to your branch
- continue on to the next file

**Gordon P. Hemsley** · 2016-09-12 23:37 UTC

you mean cleaning things up automatically?

**Steve Howell** · 2016-09-12 23:37 UTC

Yeah, one file at a time.

**Gordon P. Hemsley** · 2016-09-12 23:37 UTC

hmm

**Gordon P. Hemsley** · 2016-09-12 23:38 UTC

I wonder how tough that would be

**Tim Abbott** · 2016-09-12 23:38 UTC

I think that approach is definitely right for template indentation

**Tim Abbott** · 2016-09-12 23:38 UTC

And the `git` tools are pretty easy to script, you can probably do it in a (200 character) shell 1-liner.

**Steve Howell** · 2016-09-12 23:38 UTC

I think it makes sense for some PEP8 things as well, like the number of empty lines between defs definitely doesn't require human intervention.

**Tim Abbott** · 2016-09-12 23:38 UTC

Would probably be worth making a reusable tool instead of said shell 1-liner though :)

**Tim Abbott** · 2016-09-12 23:39 UTC

Yeah, if we were to do the empty line piece with a tool, I'd want that.  For the things with <100 violations, would probably just do 1 commit

**Tim Abbott** · 2016-09-12 23:39 UTC

The advantage of the tool is one can resolve merge conflicts by just running the tool on the branch to rebase.

**Steve Howell** · 2016-09-12 23:40 UTC

Yeah, I think the tooling would be easy for a computer, fiddly for a human.  So, yeah, the tool could have an option to be file-granular or just do it all in one big bang.

**Gordon P. Hemsley** · 2016-09-12 23:40 UTC

python would be "easy" to script into a style enforcer, since it's defined by context-free rules

**Gordon P. Hemsley** · 2016-09-12 23:41 UTC

something like this: https://pypi.python.org/pypi/PythonTidy/

**Gordon P. Hemsley** · 2016-09-12 23:41 UTC

but more modern

**Gordon P. Hemsley** · 2016-09-12 23:43 UTC

probably would be easier to use this: https://docs.python.org/3/library/tokenize.html

**Steve Howell** · 2016-09-12 23:44 UTC

I don't want to turn over **too** much control to the tools on formatting.  Here's an example where I'd defer to the human (and I didn't write this code afaik):

```
358             if len(subscriptions) == 1:
359                 msg = ("Hi there!  We thought you'd like to know that %s just "
360                        "subscribed you to the%s stream [%s](%s)."
361                        % (user_profile.full_name,
362                           " **invite-only**" if private_streams[subscriptions[0]] else "",
363                           subscriptions[0],
364                           stream_link(subscriptions[0]),
365                         ))
```

**Gordon P. Hemsley** · 2016-09-12 23:45 UTC

what do you think a computer would do with that?

**Steve Howell** · 2016-09-12 23:46 UTC

Heh, I don't know.

**Steve Howell** · 2016-09-12 23:46 UTC

It might be a good litmus test.

**Steve Howell** · 2016-09-12 23:47 UTC

It was just the first random scrap of code I found where some human obviously was fiddly about the formatting.

**Gordon P. Hemsley** · 2016-09-12 23:47 UTC

what file was that?

**Steve Howell** · 2016-09-12 23:48 UTC

`zerver/views/streams.py`

**Gordon P. Hemsley** · 2016-09-12 23:48 UTC

flake8 has no problems with those lines

**Steve Howell** · 2016-09-12 23:48 UTC

Without even doing `git blame`, I know I didn't write it, because I have different formatting biases, but there's a human element to the code that is refreshing.

**Steve Howell** · 2016-09-12 23:49 UTC

That's good to know!

**Gordon P. Hemsley** · 2016-09-12 23:49 UTC

now, lines 349 and 376 are a different story :P

**Gordon P. Hemsley** · 2016-09-12 23:49 UTC

(the closest lines with issues)

**Steve Howell** · 2016-09-12 23:50 UTC

Yeah.

**Gordon P. Hemsley** · 2016-09-12 23:51 UTC

oh wait

**Gordon P. Hemsley** · 2016-09-12 23:51 UTC

hmm

**Gordon P. Hemsley** · 2016-09-12 23:51 UTC

we're looking at different copies of the file

**Gordon P. Hemsley** · 2016-09-12 23:52 UTC

line 349 in my file is the closing parentheses (line 365 in yours)

**Steve Howell** · 2016-09-12 23:52 UTC

The ideal code formatter for me wouldn't adjust every line of code to its concept of the perfect canonical style; it would just clean up obvious errors.  But I'd be somewhat open-minded to a more tyrannical regime where the computer just formatted the code and we didn't have to think about it.

**Steve Howell** · 2016-09-12 23:52 UTC

oh yeah, sorry, I was on a branch, back on master now, so we're on the same page

**Gordon P. Hemsley** · 2016-09-12 23:53 UTC

but yeah, something tyrannical is what I'm pondering

**Steve Howell** · 2016-09-12 23:57 UTC

`zerver/views/__init__.py` is 1238 lines long.  It would be a great litmus test for some kind of automated tools cleanup.  I'd say if it changes more than, say, 50 non-whitespace lines, it's probably too tyrannical.  If it changes more than 5 or 6 lines of code where we all just go "yuck," it's too tyrannical.  But if it passes both the prior tests, I think we should be open-minded.

**Steve Howell** · 2016-09-13 00:01 UTC

I could deal with a small yuck factor in the name of consistency, since you can usually work around yuck-type of rules with a tiny bit of cleverness.

**Gordon P. Hemsley** · 2016-09-13 00:03 UTC

I am intrigued by this idea

**Steve Howell** · 2016-09-13 00:10 UTC

I think it would be worthwhile for you to explore.  Although I will also remind you that there are lower hanging fruit, like the templates, which are way more badly in need of cleanup.

**Steve Howell** · 2016-09-13 00:11 UTC

But it would be nice to at least have a data point on the PEP8 stuff, even if we are reluctant to act on it right away.  (You've already given some useful data points, but maybe applied to one file it will be easier to grok.)


## linter

*2016-10-21 to 2018-03-30 · 30 messages · [open in Zulip](https://chat.zulip.org/#narrow/channel/18-tools/topic/linter/with/44624)*

**Deeksha Aruloli** · 2016-10-21 18:43 UTC

@Tim Abbott Could you please check #2098 and kindly guide me as to why the "checks failed" ?

**Sumana Harihareswara** · 2016-10-21 18:44 UTC

@Deeksha Aruloli can you click through to Travis CI and see https://travis-ci.org/zulip/zulip/builds/169577227 ... no you can't because of the global DNS problem happening right now

**Sumana Harihareswara** · 2016-10-21 18:44 UTC

@Deeksha Aruloli have you tried running the linter locally?

**Tim Abbott** · 2016-10-21 18:45 UTC

My guess is the tests will fail in Travis CI since we use GitHub there.  Probably not your fault.

**Sumana Harihareswara** · 2016-10-21 18:46 UTC

@Deeksha Aruloli If you run the linter locally (on your branch) and the tests pass, then don't worry about GitHub/Travis CI errors right now -- they're probably a false positive because of the DNS problems that are affecting a lot of websites right now

**Deeksha Aruloli** · 2016-10-21 19:17 UTC

I seem to be having issues in opening the Dev environment. Worked fine all this while. Could I please check and come back by tomorrow morning as the Internet is very shaky right now :(

**Sumana Harihareswara** · 2016-10-21 19:19 UTC

@Deeksha Aruloli of course that's fine -- are you asking permission?

**Deeksha Aruloli** · 2016-10-21 19:22 UTC

well, I really wanted to work on this and wrap it up tonight but seems like the Internet connection isn't favoring me. :grimacing:

**Tim Abbott** · 2016-10-21 19:24 UTC

If lint-all works locally and you didn't change anything not in the linter, the tests will almost certainly pass in Travis CI; so probably you're good and should just not worry about the Travis CI output (I'll deal when I merge it).

**Sumana Harihareswara** · 2016-10-21 19:26 UTC

Yeah. Go rest. :)

**Deeksha Aruloli** · 2016-10-21 19:26 UTC

@Tim Abbott  Just a doubt here. What could have possibly gone wrong when `vagrant up` was running but my Internet connection goes off. And when I run it again, it says it's "up-to-date" but doesn't open the Zulip env.

**Steve Howell** · 2016-10-21 19:32 UTC

@Deeksha Aruloli This is possibly unrelated to your problem, but my vagrant seems to spontaneously shut down after a day or two of use, and I've never gotten to the bottom of why it happens.  I can usually just restart it, but it's kind of a nuisance.

**Deeksha Aruloli** · 2016-10-21 19:33 UTC

@Steve Howell Oh. I am trying to run provision within the guest hoping it will fix the issue ( as it did so before ) :D

**Tim Abbott** · 2016-10-21 19:49 UTC

@Steve Howell that may be something where you want to switch Vagrant versions -- they seem to have occasional problems like that on Mac that are version-dependent.  I think @Brock Whittaker said he switched versions recently and that stopped happening?  If so we should document that version and maybe send out an email PSA...

**Steve Howell** · 2016-10-21 19:51 UTC

yeah...I might not be able to give great feedback here, since I'm in the process of cutting over to a new laptop with a new OS

**Deeksha Aruloli** · 2016-10-22 06:14 UTC

@Sumana Harihareswara  @Tim Abbott I ran lint locally, and seems to work correct. How shall I go about now?

**Deeksha Aruloli** · 2016-10-22 06:15 UTC

@Steve Howell  Got the environment up again , by running provision.py within the guest. :)

**Sumana Harihareswara** · 2016-10-22 08:47 UTC

@Deeksha Aruloli Move on to the next issue that you want to work on.

**Sumana Harihareswara** · 2016-10-22 08:48 UTC

And maybe leave a comment on the GitHub pull request #2098 saying "I ran the linters locally and they work."

**Deeksha Aruloli** · 2016-10-22 09:52 UTC

Will do so @Sumana Harihareswara . Thank you.

**Deeksha Aruloli** · 2016-10-22 17:35 UTC

@Tim Abbott My pull request, #2098 is ready for review now.

**Armaan Ahluwalia** · 2018-03-30 20:29 UTC

Hi. I was wondering if anyone here has had any successes with autofixing based off of eslintrc or editorconfig on the frontend of the project. Thanks!

**Armaan Ahluwalia** · 2018-03-30 20:31 UTC

Hi. I was wondering if anyone here has had any successes with autofixing based off of eslintrc or editorconfig on the frontend of the project. Thanks!

**Tim Abbott** · 2018-03-30 20:32 UTC

@Armaan Ahluwalia you can edit topics to fix a message you sent to the wrong place :)

**Armaan Ahluwalia** · 2018-03-30 20:32 UTC

ah thanks!

**Tim Abbott** · 2018-03-30 20:32 UTC

eslintrc doesn't cover every bit of linting we do (e.g. doesn't check CSS, etc.) but I know some people use editors that autofix their code.

**Armaan Ahluwalia** · 2018-03-30 20:34 UTC

Was just wondering if anyone had any luck with this. My efforts have been rather unsuccessful

**Armaan Ahluwalia** · 2018-03-30 20:35 UTC

FYI: Im using atom

**Armaan Ahluwalia** · 2018-03-30 20:43 UTC

> eslintrc doesn't cover every bit of linting we do (e.g. doesn't check CSS, etc.) but I know some people use editors that autofix their code.
Understood. Might be useful to add a minimal stylelint config file which would allow editors to automatically lint them?

**Tim Abbott** · 2018-03-30 20:54 UTC

Yeah, not a bad idea.  Open an issue for adding one?


## dh-virtualenv

*2016-10-26 to 2016-10-26 · 7 messages · [open in Zulip](https://chat.zulip.org/#narrow/channel/18-tools/topic/dh-virtualenv/with/46361)*

**Christie Koehler** · 2016-10-26 20:23 UTC

have we ever explored using dh-virtualenv?  https://github.com/spotify/dh-virtualenv I learned about it from this blog post https://nylas.com/blog/packaging-deploying-python/

**Christie Koehler** · 2016-10-26 20:23 UTC

Which caught my eye because I think we have similar challenges with deployment.

**Steve Howell** · 2016-10-26 20:29 UTC

Not to my knowledge.  It seems to solve a problem that I have been thinking about in terms of deploying bots.   I want to make it simple for people to write a bot that they run on their laptops for a few days, then move it out to hosting.  I looked very briefly deeply into things like docker/heroku as well as more lightweight stuff like fabfile.

**Steve Howell** · 2016-10-26 20:49 UTC

Are you thinking about this mainly for production, or mainly for dev, or a little bit of both?

For production, I'm wondering if we include dependencies in our tarball already, at least for upgrades.

For development, I think the debian approach is kind of intriguing.  It would be impractical to build a debian package for every pull request, but I don't think it would be unreasonable to build a new debian package every time we touch dependencies.  We are already trying to roll out a discipline of bumping up provisioning version numbers and being mindful of provisioning upgrades.

**Christie Koehler** · 2016-10-26 20:51 UTC

To start, for development.

**Steve Howell** · 2016-10-26 20:56 UTC

I know we've fixed some glitches in our provisioning recently, but I would definitely be up for exploring the following approaches for making dev-provisioning more easy:
* build a big tarball for the 3 or 4 major platforms
* hand-build a debian package
* use something like dh-virtualenv

We could probably have Travis do this mostly offline.  Not a trivial undertaking, but it's solving a problem that impacts thousands of people, so worth thinking about.

**Tim Abbott** · 2016-10-26 21:09 UTC

An image-based system could definitely be more reliable/consistent, but at the cost of being fast to iterate on locally.  We sorta basically do something like what they describe with our production release tarballs.


## pep8

*2016-11-09 to 2016-11-14 · 9 messages · [open in Zulip](https://chat.zulip.org/#narrow/channel/18-tools/topic/pep8/with/51344)*

**Tim Abbott** · 2016-11-09 23:15 UTC

Man, the pep8 linter is really slow!

**Tim Abbott** · 2016-11-09 23:22 UTC

@Gordon P. Hemsley FYI we now have the pep8 linter integrated into Zulip via `lint-all --pep8`, with clean-passing output

**Tim Abbott** · 2016-11-09 23:23 UTC

we're thinking of making a fun Google Code-In project for the high school students to fix most of the issues it reports :)

**Steve Howell** · 2016-11-09 23:23 UTC

Do you think it's just a slow implementation, or is it doing some complicate cross-module checks that pyflakes doesn't handle?

**Tim Abbott** · 2016-11-09 23:23 UTC

I kinda want to spend some time figuring out why the tool is so slow, though; it seems like it could benefit from optimization

**Tim Abbott** · 2016-11-09 23:23 UTC

It's mostly whitespace stuff, so I think it's probably just a slow implementation

**John Vandenberg** · 2016-11-14 15:59 UTC

Is it using the new `pycodestyle`, or the old `pep8`?
Is it traversing a build directory, or a hidden directory like `.tox`?

**Tim Abbott** · 2016-11-14 21:22 UTC

@John Vandenberg we're using `pycodestyle`; and to see how we're running it, read `tools/lint-all` and search for `pep8`.

**Tim Abbott** · 2016-11-14 21:23 UTC

I think it's just traversing the main source directory for the repo


## duplicate HTML IDs

*2016-12-28 to 2017-01-14 · 129 messages · [open in Zulip](https://chat.zulip.org/#narrow/channel/18-tools/topic/duplicate.20HTML.20IDs/with/107757)*

**Tim Abbott** · 2016-12-28 00:55 UTC

@Steve Howell would it be easy to make your HTML processors lint for https://github.com/zulip/zulip/issues/2950 ?

**Tim Abbott** · 2016-12-28 00:55 UTC

That's the second bug of that form that I've run into in the last month or two :)

**Steve Howell** · 2016-12-28 15:17 UTC

Yeah, the HTML processors can already pull out ids and classes.  It wouldn't catch every case of this bug (people could slyly create ids with template variables), but it would catch some.  I think we should also remember our `expectOne()` helper.

**Tim Abbott** · 2016-12-28 17:30 UTC

Well the problem in this case was actually CSS that accidentally applied to things it didn't intend to; I'm not sure expectOne would have caught it

**Tim Abbott** · 2016-12-28 17:30 UTC

OK, I think that sort of basic duplicate detection linting seems like a worthwhile project.

**Steve Howell** · 2016-12-28 18:47 UTC

I'm hoping to eventually get a student interested in that code, as it's challenging in some way but it doesn't get you into ugly legacy stuff.  A few months ago Gordon put some really good test coverage on it, but he seems to have gotten busy with other stuff.

**Tommy Ip** · 2016-12-28 19:01 UTC

What should the program do?

**Steve Howell** · 2016-12-28 20:28 UTC

We have programs that scan all of our templates looking for indentation bugs.  We could also have them look for things like duplicate ids.  Gotta run, but I will try to describe in more detail if you catch me online later.

**Brock Whittaker** · 2016-12-29 18:53 UTC

I already have a script that does this in browser which can be useful, but the issue with templates generating them dynamically is actually a really huge issue.

**Brock Whittaker** · 2016-12-29 19:23 UTC

List of (probably) all ID collisions in the Zulip front-end.

```javascript
{
    "collisions": [
        {
            "id": "name_change_container",
            "count": 1045,
            "node": "<div className='input-group' id='name_change_container'></div>"
        },
        {
            "id": "full_name",
            "count": 1045,
            "node": "<input className='' id='full_name'></input>"
        },
        {
            "id": "admin-user-list",
            "count": 1,
            "node": "<div className='settings-section' id='admin-user-list'></div>"
        },
        {
            "id": "organization-settings",
            "count": 1,
            "node": "<div className='settings-section' id='organization-settings'></div>"
        },
        {
            "id": "deactivation_user_modal_label",
            "count": 1,
            "node": "<h3 className='' id='deactivation_user_modal_label'></h3>"
        },
        {
            "id": "108950",
            "count": 1,
            "node": "<div className='message_edit_form' id='108950'></div>"
        },
        {
            "id": "timerender503",
            "count": 1,
            "node": "<span className='hide-date' id='timerender503'></span>"
        },
        {
            "id": "109847",
            "count": 2,
            "node": "<div className='message_row include-sender last_message  selectable_row' id='109847'></div>"
        },
        {
            "id": "109868",
            "count": 1,
            "node": "<div className='message_edit_form' id='109868'></div>"
        },
        {
            "id": "fmt_help_table",
            "count": 1,
            "node": "<table className='table table-striped table-condensed table-rounded table-bordered' id='fmt_help_table'></table>"
        }
    ],
    "total_collisions": 2099
}
```

**Tim Abbott** · 2016-12-29 19:40 UTC

The first two with 1045 entries are both in `static/templates/admin_user_list.handlebars`.  @Brock Whittaker do you want to take care of fixing these?

**Brock Whittaker** · 2016-12-29 21:21 UTC

PR submitted.

**Aditya Bansal** · 2017-01-05 21:44 UTC

@Tim Abbott @Steve Howell 
I read the discussion in this issue https://github.com/zulip/zulip/issues/2950 and thought of to take a look
so i read the `html_branches.py` file and modified it to return a list of id's which appeared more than once in a given html. could you please guide me futher on this

**Steve Howell** · 2017-01-05 21:50 UTC

I would start the discussion by submitting a "wip" (work in progress) PR with what you have so far.   I think we want to prevent duplicate ids across files, not just within them.

**Aditya Bansal** · 2017-01-05 21:55 UTC

ohk
i will submit a WIP and we can discuss further there
Actually i wanted to ask before submitting WIP since some other guy in the issues said to take it up. So i thought it would be better to ask

**Steve Howell** · 2017-01-05 21:58 UTC

It was good to ask, but at this point I'm not sure the other person is still around, and even if they are, it will be good to have your PR, so they can see your thought process on this.  Thanks for taking this on!

**Aditya Bansal** · 2017-01-05 22:05 UTC

ohk i will open up a WIP 
thanks for giving a direction

**Aditya Bansal** · 2017-01-06 15:44 UTC

@Steve Howell
Please review this https://github.com/zulip/zulip/pull/3139

**Steve Howell** · 2017-01-06 15:57 UTC

Thanks for the PR!  I added a few comments.  If you catch me online today, I'm happy to discuss over chat, or you can also add comments on the PR, of course.

**Steve Howell** · 2017-01-06 16:04 UTC

@Aditi Gupta You may want to look at the Grepper class here: https://github.com/zulip/zulip/blob/master/tools/lib/html_grep.py#L18

It is somewhat related to what you're doing.

Also, we will eventually want automated unit tests--look at `tools/tests` to find examples.

**Aditya Bansal** · 2017-01-06 16:16 UTC

@Steve Howell 
Thanks for reviewing my PR
I will make the suggested changes 
About the position where we collect the id's to build dictionary
Would it not be better that we do that in `html_branches` function if we want to leave `get_tag_info` function unchanged 
Since the `html_branches` function returns the List of objects of `HtmlTreeBranch` class which doesn't posses information about id's.

**Steve Howell** · 2017-01-06 16:28 UTC

For this we might not even want `html_branches()` to be part of the mix.

**Steve Howell** · 2017-01-06 16:29 UTC

We can probably just call `tokenize()` to get the tokens (see `html_tag_tree` for an example usage), and then call `get_tag_info()` to get the ids.

**Aditya Bansal** · 2017-01-06 17:31 UTC

ohk
That could be done. I will get to it now.
Actually i thought that i might be saving some computation by collecting id's in those functions only so that we may not be parsing same html again and again.

**Steve Howell** · 2017-01-06 17:57 UTC

I wouldn't worry about that.  On my VM we can parse all of our HTML in less than a second, and we don't expect our HTML to grow too much.

**Steve Howell** · 2017-01-06 17:58 UTC

The only places where we'll need to start optimizing is when we do complex things like checking HTML tags vs. CSS tags--that's why the Grepper is there, for example.  But for this id check, I just want to keep things simple for now.

**Aditya Bansal** · 2017-01-06 18:12 UTC

ohk I have pushed a commit 
Please review it

**Steve Howell** · 2017-01-06 18:31 UTC

I think we  want to call tokenize() directly, as a I suggested a few messages back.

There are also some naming convention things--check_Dupid, for example.  The Zulip convention is more like "check_for_dup_ids".

**Aditya Bansal** · 2017-01-06 18:34 UTC

ohk i misunderstood 
I will make changes. Missed out that naming convention again. Will take care in future

**Aditya Bansal** · 2017-01-06 20:57 UTC

@Steve Howell 
I made the changes. Using `tokenize ()` was a great suggestion. It simplified the code.
Please review my commit.

**Steve Howell** · 2017-01-06 22:13 UTC

Hi @Aditya Bansal A quick tip--if you want a quick review, it helps to put the PR in your message, like #3139, just to save your reviewer (me, haha) a little time.

**Steve Howell** · 2017-01-06 22:14 UTC

It's looking much better!  Have you used `defaultdict(list)` before?  It can save you a couple lines of code where you have to check if a key is in the dictionary.

**Aditya Bansal** · 2017-01-07 07:04 UTC

I will take care to put in the PR in messages from now on. 
For the `defaultdict(list)` i never did used it before but i just learned to and updated the code with changes.
Here it is [#3139](https://github.com/zulip/zulip/pull/3139)

**Aditya Bansal** · 2017-01-09 15:44 UTC

Hey @Steve Howell I made simplifications to the templates list by leaving out base.html. Also fixed those coding convention issues in this [#3139](https://github.com/zulip/zulip/pull/3139). I had a query about need of sorting templates list.
Also i was thinking of making unit tests for the function. In regard of unit tests i wanted to ask if i should return in someway the entire content (by appending to an empty string everything function outputs) that was printed or should there be some other approach followed to make tests.
Currently duplicates are printed to console when they are detected. There are duplicate id's in a number of files currently.

**Steve Howell** · 2017-01-09 15:51 UTC

We sort the templates just to make the output predictable.  It's inexpensive to sort them, so I'd leave that in.

**Aditya Bansal** · 2017-01-09 15:52 UTC

yes, just wanted to understand its meaning there.

**Steve Howell** · 2017-01-09 15:54 UTC

For unit testing, you can change check_for_duplicate_ids to return a list of strings describing the errors, and then actually print the errors in `check-templates`.

**Steve Howell** · 2017-01-09 15:55 UTC

Do you have examples of duplicate ids?  You should research a few to see if you think they are legitimate issues or due to some flaw in the way that we search for duplicates.

**Aditya Bansal** · 2017-01-09 16:08 UTC

i was thinking of trying to make some up.
Firstly i was thinking to look onto the duplicates that are being already reported and probably keep some cases separately in files so i can use them as test cases.
Wouldn't that be right. Or should i try to make cases with varying places where duplicates occur.
for example:
`<p id="someid">
....
<span id="someid"></span></p>` 
with sameid being in one file and then similar id's being in other files too.

**Steve Howell** · 2017-01-09 16:35 UTC

For your test cases I would just use fake data in small representative HTML snippets.

**Aditya Bansal** · 2017-01-09 16:36 UTC

so should i place such data in separate files under a new directory in tests folder

**Steve Howell** · 2017-01-09 16:36 UTC

Now that your code is in pretty good shape, your biggest focus might be to track down the actual duplicates that are being reported, so we can get to the bottom of what is causing them (and fix any that are broken).  Then we can come back to testing, I think.

**Steve Howell** · 2017-01-09 16:37 UTC

We have a `fixtures` directory that we use for test data.

**Steve Howell** · 2017-01-09 16:38 UTC

Hmmm.  Let's just make a new directory as you propose, under `tools/tests` for the sample data.

**Aditya Bansal** · 2017-01-09 16:40 UTC

ohk i will move forward with that and yeah maybe i must first take a look onto the duplicates being reported first.

**Steve Howell** · 2017-01-09 16:45 UTC

Sounds good!

**Aditya Bansal** · 2017-01-10 21:34 UTC

@Steve Howell 
While looking through duplicates being reported i found some weird id being parsed ("}}"). Such id didn't existed in the files and was a issue of `get_tag_info` function within `html_branches.py`.
`get_tag_info` functions uses `lst += g.split()` which i believe it does to convert string to list.
I believe that needs to be changed since parsing ids with template variable may have spaces and get broken up while being inserted to ids list for a token. 
What do you say

**Steve Howell** · 2017-01-10 21:52 UTC

That sounds like a bug!  If there's an easy fix, we should just make it and add some tests for it.  Can you excerpt a little more of the template for context?  I'm wondering if the template is formatted funny.  I suspect it's more about the parser just being a little naive.

**Aditya Bansal** · 2017-01-10 21:55 UTC

template that we are looking at is `templates/analytics/activity.html` (Line 41 ) and `templates/zerver/register.html` (Line 126)
Actually the problem is id's here are given using template variables.

**Aditya Bansal** · 2017-01-10 21:59 UTC

everything works fine till get_tag_info function extracting id using regex.
but when this id is inserted to the list in that function syntax like 
`lst += g.split()` is used. since g is a string and ideally for id's g.split would have returned a list with only one string that was same as `g`. But in case of id's with template variables that id gets split up on space.
it should be replaced with `lst += [g] ` and i believe everything would be fine then.

**Steve Howell** · 2017-01-10 22:00 UTC

I think we actually want to treat "{{ name|slugify }}" as the entire name of the id, which probably requires a little more intelligence in our parser.

**Steve Howell** · 2017-01-10 22:02 UTC

I would be ok putting a temporary hack in the parser to just ignore any id or class attribute that has "{{" in it, for now.

**Aditya Bansal** · 2017-01-10 22:05 UTC

actually id is extracted in get_tag_info function in `html_branches.py`.
If we replace `lst += g.split()` with `lst += [g]` it should give us id as we want i.e. treat `id={{ name|slugify }}`.

**Aditya Bansal** · 2017-01-10 22:12 UTC

currently if we say `g` to hold string `{{ name|slugify }}` then `g.split()` is added to `lst`.
It seems like a shortcut way of generating list of string to me. In case we are sure that `g` won't have spaces in it.

**Steve Howell** · 2017-01-10 22:17 UTC

Calling `split` makes sense for classes, since in HTML you can do this:

~~~ html
<div class="book red clickable">

**Steve Howell** · 2017-01-10 22:17 UTC

In that case you're really dealing with three separate classes.  It doesn't make as much sense for `id`, since it's rare you give more than one id to an element.

**Aditya Bansal** · 2017-01-10 22:19 UTC

yeah i wasn't thinking about classes.

**Aditya Bansal** · 2017-01-10 22:41 UTC

A linear traversal on the ids with replacing spaces that are outside {{ anything here }} with a # and then splitting using # as delimiter. How do you find this approach.?
Also i looked onto other duplicates and it looks like they are no problems till now. What should i do with the duplicates which are not actually broken?

**Steve Howell** · 2017-01-10 23:39 UTC

I think we can parse it more robustly by just doing a char-by-char parse.  If you see "{{" keep eating chars till the end of "}}"; if you see anything else, eat characters up to the space.  You can probably drive this with automated tests.

**Steve Howell** · 2017-01-10 23:40 UTC

For dealing with the "false" errors, we have two choices:
* temporarily create some hacky code to make exceptions for those token
* just go ahead and fix how we parse the ids and classes

There's no huge rush on this, so I'd play around with parsing the ids/classes.

**Aditya Bansal** · 2017-01-11 19:14 UTC

Hey @Steve Howell I moved forward with the option of fixing how we parse ids/classes and implemented a new method in `html_branches` called `split_for_id_and_class` which performs splits now. Also added basic unit test case for this method.
I had also added very basic unit test for the duplicate id detection previously and modified `check_templates` to ignore test data directory. Here are the new commits [#3139](https://github.com/zulip/zulip/pull/3139). Please review them.

Also for the duplicates being reported now none of them seems to me like broken. What i mean to say is that duplicate id's have been used in various places but none of them is causing any problem right now. 
For example : The first duplicate being reported is some thing like this
```Duplicate ID(s) detected :Id 'api-example-tabs' present at following files: 
Line 35:templates/zerver/api.html
Line 16:templates/zerver/api_endpoints.html```
Here same id is being used for nav tabs but it doesn't break anything.
so what should be done with such cases since these are valid duplicate ids but aren't currently causing problem.

**Steve Howell** · 2017-01-11 20:49 UTC

We can exempt the API endpoints, I guess, since they're not really part of the core app.  Ideally even for that case we'd create some sort of partial template to de-duplicate the logic.

**Steve Howell** · 2017-01-11 21:08 UTC

I added several comments to the PR, mostly dealing with stylistic stuff.

**Aditya Bansal** · 2017-01-11 21:14 UTC

I will read the comments and try improve. 
Here are all the [duplicates](http://paste.ubuntu.com/23783591/) being reported. I made some comments on each showing what i think of them.

**Aditya Bansal** · 2017-01-11 21:17 UTC

I would first like to clear meaning of partial templates. Does it means having a template which will then be included in another template?

**Sampriti Panda** · 2017-01-11 21:19 UTC

Yeah, mainly that.

**Sampriti Panda** · 2017-01-11 21:20 UTC

You can use every template on it's own actually.

**Sampriti Panda** · 2017-01-11 21:20 UTC

But a "partial template" means including another template inside the current one.

**Aditya Bansal** · 2017-01-11 21:28 UTC

ohk
I will think about use of partial templates here.

**Steve Howell** · 2017-01-11 21:29 UTC

@Brock Whittaker @Tim Abbott Here is a preliminary list of duplicate IDs from @Aditya Bansal http://paste.ubuntu.com/23783591/  Let us know if anything looks unexpected or kind of alarming for the upcoming release.

**Steve Howell** · 2017-01-11 21:30 UTC

Here is a case of duplicates where we could do a pretty simple fix:

~~~

Duplicate ID(s) detected :Id 'fmt_help_table' present at following files: -->used for same purpose of labeling table in help
Line 9:templates/zerver/markdown_help.html
Line 8:templates/zerver/search_operators.html

**Steve Howell** · 2017-01-11 21:32 UTC

Those are totally copy/paste, and I grepped the code, and we don't have any JS/CSS that uses the ids, so we could just remove them.

**Steve Howell** · 2017-01-11 21:42 UTC

@Aditya Bansal In the interest of getting this merged, I would be fine if you just created a list of these 15 ids or so in your program:

~~~ py
# TODO: Clean up the these cases in the real code
IGNORE_IDS = [
    'api-example-tabs',
   'errors',
   ...
]

if id in IGNORE_IDS:
   # print it
else:
   # add it to the list of bad_ids

if bad_ids:
    sys.exit(1)
~~~

**Aditya Bansal** · 2017-01-11 21:44 UTC

in context to previous message: `zulip.css` uses id `fmt_help_table` to apply `table-layout: fixed;`

**Steve Howell** · 2017-01-11 21:46 UTC

Oh, I missed that in the grep.  Need a bigger font, haha.

**Steve Howell** · 2017-01-11 21:46 UTC

Let me do a quick PR for that.

**Steve Howell** · 2017-01-11 21:53 UTC

https://github.com/zulip/zulip/pull/3238

**Tim Abbott** · 2017-01-11 22:00 UTC

Merged

**Steve Howell** · 2017-01-11 22:03 UTC

thx :)

**Aditya Bansal** · 2017-01-11 22:09 UTC

@Steve Howell What is the expected behaviour in case we add list of ids currently being reported? Like according to the sample code ignored id's gets printed and id's that are new duplicates make code to exit without printing anything. 
Should not that be something like this:
bad id's gets printed and then a exit and nothing done for ignored_ids.

**Steve Howell** · 2017-01-11 22:16 UTC

For ignored ids, we should probably do something like`logging.warn`.

What I'm try to say is that we only exit with a bad return code (`sys.exit(1)`) if we get new bad ids.  And we should print those as well.

My code above is not precise, just giving you the idea of what to do.

**Aditya Bansal** · 2017-01-11 22:16 UTC

ohk i will improvise on that

**Brock Whittaker** · 2017-01-11 22:17 UTC

The only concerning ones are the `#fmt_help_table` IDs colliding because as far as I can see, none of the other IDs will be on the same page at one time.

**Aditya Bansal** · 2017-01-11 22:18 UTC

yeah none other are on same page at a time

**Steve Howell** · 2017-01-11 23:36 UTC

@Brock Whittaker We just fixed fmt_help_table, so it sounds like we're good for now?

https://github.com/zulip/zulip/commit/48e68791e8d2e388225418a8baca399271025895

**Brock Whittaker** · 2017-01-12 00:31 UTC

I think the rest looks fine, yeah!

**Aditya Bansal** · 2017-01-12 14:13 UTC

Hi @Steve Howell I have pushed in more commits to [#3139](https://github.com/zulip/zulip/pull/3139) to implement changes suggested. Hope i may have improved upon naming conventions this time. Also added the ignore able ids list and made changes to printing statements so as to always print bad ids after the warning type ignore able id's so that users may be able to follow and debug easily. Please review.
I do not know why the travis CI has not started yet it has been almost 42 mins.

**Steve Howell** · 2017-01-12 15:06 UTC

Nice work!  Travis has been getting backlogged a lot lately; sorry about that.   I taking a quick look at it now, but I am a bit behind on some other PRs.

**Aditya Bansal** · 2017-01-12 15:50 UTC

ohk i saw the comments i will resolve the issues.

**Aditya Bansal** · 2017-01-12 16:31 UTC

I have squashed the commits into one here in [#3139](https://github.com/zulip/zulip/pull/3139). 
Also changed it to use `foo.items()` instead of `iteritems(foo)`

**Aditya Bansal** · 2017-01-12 20:43 UTC

Hey @Steve Howell  if you have made up with the other PRs could you please take a look at this[#3139](https://github.com/zulip/zulip/pull/3139).
Also i wanted to ask a question about your commit [here](https://github.com/zulip/zulip/commit/5ec0bc121319f1402249fc3f500a052e780c9f60). Here you moved import statement to `if False`
If i understand it correctly then that import will never execute then why not remove it entirely?

**Steve Howell** · 2017-01-12 21:02 UTC

That's a special hack for mypy, our static type checker, to be able to work.

**Steve Howell** · 2017-01-12 21:08 UTC

Cool, I'll look at it again within the hour, most likely.

**Aditya Bansal** · 2017-01-12 21:09 UTC

No problem although i still don't follow the hack much. Maybe reading run-mypy code could help me

**Steve Howell** · 2017-01-12 21:13 UTC

That won't help too much, actually.

**Steve Howell** · 2017-01-12 21:14 UTC

Basically, a static analyzer wants to be able to read all your Python code and infer import dependencies to see how everything is connected, but those things aren't really needed at runtime, and they can often cause complications like circular run-time dependencies, so you can hide them with `if False:` from actual Python, but mypy will still see them.

**Steve Howell** · 2017-01-12 21:15 UTC

Here's a good intro to mypy, written by our own @Tim Abbott : http://blog.zulip.org/2016/10/13/static-types-in-python-oh-mypy/

**Aditya Bansal** · 2017-01-12 21:18 UTC

ohk so mypy can look beyond that `if False:`
I will read the intro now. Thanks for the explanation and link

**Steve Howell** · 2017-01-12 21:58 UTC

No prob!  Regarding your PR I think the last step is to try it out with ./tools/lint-all.  We don't want `lint-all` to be very noisy if there aren't actual problems, so we probably want `check-templates` to also be quiet by default.  But we should have a way for `check-templates` to be verbose when we're looking for all dups, including ones in the IGNORE list.  Make sense?

**Aditya Bansal** · 2017-01-12 23:02 UTC

Totally 
I will work on that

**Aditya Bansal** · 2017-01-13 21:29 UTC

Hey @Steve Howell  I made some changes so that the ignored ids are analysed conditionally only.
I added a `--complete` argument to lint-all so that could control the complete scan for ids.
Here [#3139](https://github.com/zulip/zulip/pull/3139) it is. Please review. 
I also thought of adding it under the `--full` argument but that also controlled other stuff and that led to quite a messy output for trying to find out cases of ignored duplicate id's so i thought it would be better to create a new argument.
`--complete` might not be a very good arg so we might change it it `--alldup` whats your thought?

**Steve Howell** · 2017-01-13 21:29 UTC

I like `--alldup`.

**Aditya Bansal** · 2017-01-13 21:30 UTC

ohk i change it then wait a min

**Steve Howell** · 2017-01-13 21:33 UTC

sounds good

**Aditya Bansal** · 2017-01-13 21:40 UTC

done [#3139](https://github.com/zulip/zulip/pull/3139)

**Steve Howell** · 2017-01-13 22:20 UTC

Testing it now.  I think the last thing to address is making your commit message a little more concise.

**Steve Howell** · 2017-01-13 22:21 UTC

Some guidelines for the commit message are here: https://zulip.readthedocs.io/en/latest/version-control.html#commit-messages

**Steve Howell** · 2017-01-13 22:24 UTC

Oh, and you can undo your changes from `lint-all`.  I think we only need that `--all-dups` option if you're running `check-templates` directly.

**Aditya Bansal** · 2017-01-13 22:39 UTC

yes i will make the commit concise now. I thought it would be better to get a review first if that was ready for merge.
ohk i will remove those args from lint-all

**Steve Howell** · 2017-01-13 22:45 UTC

Thanks!

**Aditya Bansal** · 2017-01-13 23:46 UTC

i have made the changes and linted up the commit message 
Here [#3139](https://github.com/zulip/zulip/pull/3139) 
Please review

**Steve Howell** · 2017-01-14 00:14 UTC

Can you add a period to the end of the title line?  (This is part of our standard, although we sometimes enforce it laxly.)

Also, all lines in your commit message should be < 80 chars, because lots of tools won't wrap them for you (including github--you'll see what I mean if you look there).

**Steve Howell** · 2017-01-14 00:16 UTC

Also, it looks like the last paragraph of the commit is left over from a squash--you can just remove it, please.

**Aditya Bansal** · 2017-01-14 00:21 UTC

ohk i forgot the period after the first line. I almost specially checked it in entire commit. But missed it. I don't know why lines are going beyond 80 chars. i put new lines while committing in a 79X22 terminal window. Let me have a look at that.

**Aditya Bansal** · 2017-01-14 00:26 UTC

done have a look [#3139](https://github.com/zulip/zulip/pull/3139)

**Steve Howell** · 2017-01-14 00:30 UTC

It still looks like this:

[pasted image](https://chat.zulip.org/user_uploads/2/4d/ZzmeuhZYEDVvQ0nb50KW7ozO/pasted_image.png)

**Steve Howell** · 2017-01-14 00:33 UTC

it might be 76 chars

**Steve Howell** · 2017-01-14 00:34 UTC

I would also put blank lines between your paragraphs.

**Aditya Bansal** · 2017-01-14 00:35 UTC

let me see, i find this strange the character thing.

**Aditya Bansal** · 2017-01-14 00:36 UTC

ohk char limit is 76 chars i see

**Aditya Bansal** · 2017-01-14 00:41 UTC

i guess this is varying with screens as well
i looked at github and it didn't wrapped after detect in first line but in your screen it does.

**Steve Howell** · 2017-01-14 00:41 UTC

interesting

**Aditya Bansal** · 2017-01-14 00:41 UTC

anyways lets limit to 65 chars

**Steve Howell** · 2017-01-14 00:43 UTC

good idea :)

**Aditya Bansal** · 2017-01-14 00:56 UTC

its done [#3139](https://github.com/zulip/zulip/pull/3139)

**Steve Howell** · 2017-01-14 01:00 UTC

Merged!  Thanks for doing this!

**Aditya Bansal** · 2017-01-14 01:10 UTC

Thanks for guiding me through out. I loved working on the issue. Will find some new one, got any suggestions.

**Steve Howell** · 2017-01-14 12:17 UTC

You're welcome!  We have some other  similar issues, like this one:

https://github.com/zulip/zulip/issues/1659

Here are all the issues with the "tooling" label:

https://github.com/zulip/zulip/labels/area%3A%20tooling

**Aditya Bansal** · 2017-01-14 14:01 UTC

ohk let me take a look


## shubham808

*2016-12-31 to 2017-01-12 · 6 messages · [open in Zulip](https://chat.zulip.org/#narrow/channel/18-tools/topic/shubham808/with/111177)*

**Shubham Shukla** · 2016-12-31 06:10 UTC

i want to request a remote dev instance

**Tomasz Kolek** · 2016-12-31 06:38 UTC

Here you are:
```
------
Your remote Zulip dev server has been created!

- Connect to your server by running
  `ssh zulipdev@shubham808.zulipdev.org` on the command line 
  (Terminal for macOS and Linux, Bash for Git on Windows).
- There is no password; your account is configured to use your ssh keys.
- Once you log in, you should see `(zulip-venv) ~$`.
- To start the dev server, `cd zulip` and then run `./tools/run-dev.py`.
- While the dev server is running, you can see the Zulip server in your browser at http://shubham808.zulipdev.org:9991.

See [Developing remotely](http://zulip.readthedocs.io/en/latest/dev-remote.html) for tips on using the remote dev instance and [Git & GitHub Guide](http://zulip.readthedocs.io/en/latest/git-guide.html) to learn how to use Git with Zulip.
------
```

**Shubham Shukla** · 2016-12-31 06:40 UTC

thanks @Tomasz Kolek

**Shubham Shukla** · 2016-12-31 06:52 UTC

i am getting a could not resolve hostname shubham808.zulipdev.org

**Sumana Harihareswara** · 2017-01-12 00:00 UTC

@Shubham Shukla Did you end up being able to solve this problem?

**Shubham Shukla** · 2017-01-12 10:45 UTC

yup i did solve it


## linters

*2016-12-31 to 2017-03-27 · 419 messages · [open in Zulip](https://chat.zulip.org/#narrow/channel/18-tools/topic/linters/with/111499)*

**Tim Abbott** · 2016-12-31 17:40 UTC

Is there a Python linter tool that supports checking for passing too many positional arguments (and thus covering the first keyword argument)?  That's a common bad pattern in Python code that we'd like to ban from the codebase, but I'm not sure there's a checker that will look for it.

**Lasse Schuirmann** · 2016-12-31 17:42 UTC

I think PyLInt does that.

**Lasse Schuirmann** · 2016-12-31 17:46 UTC

@Tim Abbott  I don't see anything else relevant on https://github.com/coala/bear-docs/blob/master/README.rst#python and we have most tools integrated in coala. If pylint doesn't suit your needs you could probably very easy hack up something very simple [using this](http://coala.io/writingbears)

**Tim Abbott** · 2016-12-31 17:47 UTC

Do you know which pylint rule does it?  It has a lot of spammy issues (e.g. it seems to be unable to handle decorators that change the arguments list) so it's a bit hard to sort through the output for this

**Lasse Schuirmann** · 2016-12-31 17:48 UTC

`too-many-arguments`

**Lasse Schuirmann** · 2016-12-31 17:48 UTC

see http://pylint-messages.wikidot.com/all-codes

**Tim Abbott** · 2016-12-31 17:49 UTC

too-many-arguments isn't right; that one is about having more than 5 arguments

**Tim Abbott** · 2016-12-31 17:50 UTC

I want cases where a function is called with more positional arguments than it accepts, which is a bit subtler

**Tim Abbott** · 2016-12-31 17:51 UTC

So maybe we need to go the Bear route?

**Lasse Schuirmann** · 2016-12-31 17:54 UTC

if pylint doesn't have it that's probably the fastest thing if you want decent usability with being able to ignore things and stuff

**Lasse Schuirmann** · 2016-12-31 17:54 UTC

the alternative is to hack together a grep which is about the same amount of work but you get worse usability

**Lasse Schuirmann** · 2016-12-31 17:54 UTC

but anyway disclaimer, I created coala

**Tim Abbott** · 2016-12-31 17:54 UTC

this seems a bit much for grep, since you need to cross-check the definition against the caller

**Tim Abbott** · 2016-12-31 17:55 UTC

We have a nearly 600 line script that runs all of our linters in parallel and has tons of regular expressions for common things (e.g. strings not tagged for translation in contexts where they should always be, etc.)

**Lasse Schuirmann** · 2016-12-31 17:56 UTC

that sounds like you have a hacked together version of coala there :P

**Tim Abbott** · 2016-12-31 17:56 UTC

But we sometimes run into things where grep doesn't cut it; seems like playing with coala should be a good choice for that

**Lasse Schuirmann** · 2016-12-31 17:56 UTC

coala does parallelization and caching etc.

**Lasse Schuirmann** · 2016-12-31 17:56 UTC

so it's basically made for what you do with your 600 line script IIUC

**Tim Abbott** · 2016-12-31 17:56 UTC

Yeah, we call into like 5 third-party linters for different stuff like puppet, etc., :)

**Lasse Schuirmann** · 2016-12-31 17:56 UTC

but if you intend to do it, ping us on coala.io/chat there'll be people helping you

**Lasse Schuirmann** · 2016-12-31 17:57 UTC

yep coala has a lot of those already and it takes like 15 mins integrating a new one

**Lasse Schuirmann** · 2016-12-31 17:57 UTC

fun story, I live coded one in 15 mins at a conference, got it released in the evening ;)

**Tim Abbott** · 2016-12-31 17:57 UTC

awesome :)

**Lasse Schuirmann** · 2016-12-31 17:57 UTC

ok gotta go, see ya around!

**Tim Abbott** · 2016-12-31 17:57 UTC

I definitely want to check it out when I have some free time (haha; we have 150 open PRs right now)

**Tim Abbott** · 2016-12-31 17:57 UTC

See ya at PyCon or something! :)

**Reid Barton** · 2017-01-07 23:19 UTC

@Tim Abbott I forget whether you are using python 3 yet, but it has a syntax `def f(a, b, *, c=1)` that prevents positional arguments from bleeding into the function's formal keyword arguments

**Reid Barton** · 2017-01-07 23:20 UTC

Also this seems like something mypy perhaps should (optionally?) catch, even if the function isn't defined using `*`

**Tim Abbott** · 2017-01-09 00:35 UTC

interesting, yeah, that seems like a good use case for mypy

**Tim Abbott** · 2017-01-09 00:35 UTC

Definitely should be an option since people have different philosophies on it

**sinwar** · 2017-01-09 03:46 UTC

after pull upstream master ```./tools/lint-all``` is showing 
```
Line too long (121) at docs/chinese.md line 63: 曾经使用的翻译有“群组”、“主题”、“版块”，还有“栏目”。现在选择的“频道”灵
Line too long (121) at docs/chinese.md line 167: 译有“错误”、“非法”、“不合法”；为保持一致的习惯，这里统一翻译为“不正确”。
Line too long (127) at docs/russian.md line 3: Вот некоторые правила, которых стоит придерживаться для поддержания
Line too long (122) at docs/russian.md line 4: качества перевода. Они продиктованы опытом - собственным и коллег,
Line too long (122) at docs/russian.md line 10: * Избегайте IT-жаргонизмы и кальки. Например, не приватный, а личный.
Line too long (122) at docs/russian.md line 11: * Фразы должны правильно читаться и передавать исходный смысл. Для
Line too long (125) at docs/russian.md line 13: * Вместо изобретения собственных терминов, используйте устоявшиеся

```

**sinwar** · 2017-01-09 03:48 UTC

I don't know russian or chinese so please check it out

**sinwar** · 2017-01-09 03:48 UTC

and break the lines

**Tim Abbott** · 2017-01-09 06:46 UTC

Oh, this is a Python 2 vs. 3 encoding issue; I'll fix this momentarily

**Tim Abbott** · 2017-01-09 06:46 UTC

Those lines are a perfectly reasonable length, but characters are being double and triple counted

**Tim Abbott** · 2017-01-09 06:48 UTC

Fix merged

**Aditya Bansal** · 2017-01-18 18:10 UTC

Hi @Steve Howell.
This is in reference to this issue [#1659](https://github.com/zulip/zulip/issues/1659), [#1661](https://github.com/zulip/zulip/issues/1661) and This PR of your's [#1778](https://github.com/zulip/zulip/pull/1778) 
I was trying to follow the discussion and discovered that there is no 2 space indents in zulip.css (Must have got fixed along the way). Also i was trying to figure out what was to be done for the PR [#1778](https://github.com/zulip/zulip/pull/1778).
I read the code and i believe you implemented the entire functionality. Please could you provide some more information on this.

**Steve Howell** · 2017-01-18 21:10 UTC

@Aditya Goyal I think #1778 is probably in pretty good shape.  I think I just got too busy to follow up on getting it reviewed and testing it out on some of our actual templates.

If you want to take this over, I would try running the tool against a couple individual files and make sure the results seem fine to you, and I'd submit a small PR with one commit per template cleanup for maybe 3 or 4 templates.

Once we get that signed off on, we probably want to have it automatically run against all of our templates.  And then, finally, we can tighten up the linter.

**Aditya Bansal** · 2017-01-19 18:38 UTC

@Steve Howell  I believe you were trying to mention me here.
I tried running the tool against a handlebar `actions_popover_content` in `static/templates` and i believe there might be modifications needed to tool itself. I believe we might wanna put in some if conditions dealing with handlebar start and end tags.
like for this line `{{#tr message}}Unmute the topic <b>__subject__</b>{{/tr}}`(line 36) offset would be set negative and resulting pretty_line would be `e the topic <b>__subject__</b>{{/tr}}` which is in correct.

**Aditya Bansal** · 2017-01-19 18:39 UTC

Am i in right direction with handlebar start and end tags to be dealt?

**Steve Howell** · 2017-01-19 18:45 UTC

Ah, yeah, that makes sense.  Yep, we need to handle those.

**Aditya Bansal** · 2017-01-19 18:46 UTC

ohk i will move forward to make modifications then.

**Steve Howell** · 2017-01-19 18:50 UTC

I'm kind of surprised we are getting negative offsets there, to be honest.  What happens to the line before that?

**Aditya Bansal** · 2017-01-19 18:52 UTC

actually if we look at this 
```
<li>
    <a href="#" class="popover_unmute_topic" data-msg-stream="{{message.stream}}" data-msg-topic="{{message.subject}}">
      <i class="icon-vector-eye-open"></i>
      {{#tr message}}Unmute the topic <b>__subject__</b>{{/tr}}
    </a>
  </li>
```

**Aditya Bansal** · 2017-01-19 18:53 UTC

we will see that `<li>` tag should get a intent of 4 and then `<a>` tag should get a intent of 8 and `<i>` onwards a intent of 12

**Steve Howell** · 2017-01-19 18:54 UTC

That should lead us to a positive offset.

**Aditya Bansal** · 2017-01-19 18:54 UTC

so what happens is when <b> tag is scanned the last tag in stack is <i>

**Steve Howell** · 2017-01-19 18:56 UTC

The `</i>` should have popped that off the stack.

**Aditya Bansal** · 2017-01-19 19:00 UTC

yes you are right 
i said it wrong 
like for <i> the intent is 12
so should be for the next line 
but in next line scanner see <b> tag

**Steve Howell** · 2017-01-19 19:01 UTC

Ah...so the problem here is block tags that have non-whitespace stuff in front of them.

**Steve Howell** · 2017-01-19 19:02 UTC

That's gonna be a problem for `<b>` even when it's not inside a handlebars block.

**Aditya Bansal** · 2017-01-19 19:02 UTC

yeah that's the problem

**Steve Howell** · 2017-01-19 19:03 UTC

So, before adding the handlebars stuff, I'd try to write a really simple test that causes "foo<b>bar</b>" to fail, then make the fix for that, which involves figuring out that an HTML token is not the start of a line.

**Aditya Bansal** · 2017-01-19 19:06 UTC

ohk i will think about how to do that and then try that out.

**Andrea  Longo** · 2017-01-20 23:41 UTC

A different lint question, why would something in an excluded directory get checked? I know the exclude is working, because there's a bunch more stuff in Swagger UI that doesn't pass and isn't getting flagged. But it finds this file?
```
+./tools/lint-all --pep8
Traceback (most recent call last):
  File "tools/check-templates", line 149, in <module>
    check_our_files()
  File "tools/check-templates", line 44, in check_our_files
    check_html_templates(by_lang['html'], args.modified, args.all_dups)
  File "tools/check-templates", line 137, in check_html_templates
    validate(fn=fn, check_indent=(fn not in bad_files))
  File "/home/travis/build/zulip/zulip/tools/lib/template_parser.py", line 203, in validate
    state.matcher(token)
  File "/home/travis/build/zulip/zulip/tools/lib/template_parser.py", line 191, in f
    ''' % (fn, problem, start_token.s, start_line, start_col, end_tag, end_line, end_col))
lib.template_parser.TemplateParserException: 
                    fn: static/swagger/index.html
                    Mismatched tag.
                    start:
                        <head>
                        line 3, col 1
                    end tag:
                        script
                        line 30, col 64
```

**Tim Abbott** · 2017-01-20 23:43 UTC

We have 7 linters that run in parallel.  `check-templates` is a different one from the regex ones

**Andrea  Longo** · 2017-01-21 00:04 UTC

So is there more than one place to exclude files?

**Andrea  Longo** · 2017-01-21 00:08 UTC

There's another `EXCLUDED_FILES` in check-templates. There's only `tools/tests/test_template_data` there however.

**Steve Howell** · 2017-01-21 00:10 UTC

Yep, individual tools sometimes have their own custom ways of excluding stuff.

**Steve Howell** · 2017-01-21 00:12 UTC

Is`swagger/index.html` coming from swagger?  If so, we can exclude it from our template checking.  If not, we should just clean up its indentation.

**Andrea  Longo** · 2017-01-21 00:12 UTC

It's from Swagger UI. It would be trivial to change, but then this will happen again (presumably) next time it's updated.

**Andrea  Longo** · 2017-01-21 00:12 UTC

And it's in a directory that is already excluded.

**Steve Howell** · 2017-01-21 00:13 UTC

Ok, then I think we're fine to just exclude it from our template checks.

**Andrea  Longo** · 2017-01-21 00:14 UTC

Ok, I'll do that then. Seemed odd.

**Aditya Bansal** · 2017-01-22 17:33 UTC

Hey @Steve Howell .
So I made the changes you suggested. Here is the PR [#3428](https://github.com/zulip/zulip/pull/3428). Please take a look.
Also should I start cleaning up the handlebar templates as you suggested to do.

**Steve Howell** · 2017-01-22 21:03 UTC

yeah, you can start cleaning up the templates before your change gets reviewed and merged...I would strive to have one commit per template

**Aditya Bansal** · 2017-01-24 21:57 UTC

I cleaned up some templates using the tool and pushed commits. Take a look on them [here](https://github.com/zulip/zulip/pull/3428).

**Aditya Bansal** · 2017-01-24 22:15 UTC

@Steve Howell I wanted to ask about the behaviour of tool on something like this 
```
<div>
    <div>
    {{t "foobar"}}
    </div>
</div>
```
Since `{{t` isn't detected as a tag so is not indented.

**Steve Howell** · 2017-01-24 22:20 UTC

Hmmm...it seems like the tool is  re-indenting the blocks, but not the "insides" of the blocks.

**Aditya Bansal** · 2017-01-24 22:21 UTC

yeah actually it re-indents every token and assumes everything inside it's scope is already indented.

**Aditya Bansal** · 2017-01-24 22:23 UTC

so what should be the behaviour here,
Like should i try to modify the tool to indent stuff?

**Steve Howell** · 2017-01-24 22:29 UTC

Thinking...

**Steve Howell** · 2017-01-24 22:30 UTC

It's not the end of the world if the most inner blocks don't get fixed in this pass, but it shouldn't be super hard to just make it work like I think we both expect it to work here.

**Steve Howell** · 2017-01-24 22:32 UTC

One thing that is sort of unrelated, but sort of is, is that I still think we should treat a line like "foo<b>yo</b>" as being essentially raw text and **not** being a block.

**Steve Howell** · 2017-01-24 22:33 UTC

Back to the original issue, when we get to an HTML end tag, I think we pretty easily know that we don't have any "blocks" inside, i.e. we are essentially a "leaf" block.  And then for that case, we can write different code to re-indent the inner stuff.

**Steve Howell** · 2017-01-24 22:36 UTC

There are some slightly tricky edge cases, because we should allow code like this:

~~~ html
<div class="red" 
    id=7>
    Here is a button: <button class="send-button"
                 id=7>
</div>

**Steve Howell** · 2017-01-24 22:37 UTC

Not the best example---the above code is pretty darn ugly--but there are places where you want tags to span multiple lines.

**Sampriti Panda** · 2017-01-24 22:40 UTC

In multi line tags, I think it's best to have the arguments aligned with the previous lines arguments.

**Sampriti Panda** · 2017-01-24 22:40 UTC

so like id would start where class started.

**Sampriti Panda** · 2017-01-24 22:40 UTC

But maybe that would be difficult to do.

**Steve Howell** · 2017-01-24 22:51 UTC

Yeah, my philosophy here it to preserve the style that the original coder used and only fix the indent.

**Aditya Bansal** · 2017-01-24 22:54 UTC

Actually only fixing the leaf block separately might not work since we may have case like
```
<div>
{{ stuff here }}
  <div>
      ...
   </div>
</div>
```
so here the leaf node will be inner div but `{{ stuff here }} ` won't get indent correction

**Steve Howell** · 2017-01-25 00:14 UTC

yeah, that's where things get a bit tricky...what we might want to do this is this at the end of a block that is five levels deep:
* make sure first and last line are indented by 20 spaces
* make sure all other lines are indented by **at least** 24 spaces, but otherwise respect the existing indentation

**Aditya Bansal** · 2017-01-26 21:39 UTC

Hey @Steve Howell .
I tried out something though not what you suggested. Here is the [PR](https://github.com/zulip/zulip/pull/3428) with some new commits.
What I did is something like this 
Added capability to indent lines with right indents.
If multi line tags exit then we indent the new lines as would have been done with any other sub part of a block
something like this 
```
<div class="red" 
id=7>
    Here is a button: <button class="send-button"
                 id=7>
                                       </button>
</div>
```
Would turn into 
```
<div class="red" 
    id=7>
    Here is a button: <button class="send-button"
                                           id=7>
                                       </button>
</div>
```
I believe for the timing we can have multi line tags also have 4-space indents.
Also the code structure has some kind of repetition of code but I thought of getting some review first before i spent time refactoring more to remove repetition.

**Aditya Bansal** · 2017-01-26 21:42 UTC

Also I added a exception for `pre` html tag since it retains formatting of the html involved inside.

**Steve Howell** · 2017-01-26 21:45 UTC

l agree with the '<pre>' tag exception.  I'm not sure how I feel about the right indents.

One comment related to the PR that is not related to your most recent changes:  can you put the GOOD and BAD side by side for each of the test fixtures?

**Aditya Bansal** · 2017-01-26 21:48 UTC

you mean one after the other in the test cases?

**Steve Howell** · 2017-01-26 21:49 UTC

yep :)

**Aditya Bansal** · 2017-01-26 21:50 UTC

yeah i can do that

**Aditya Bansal** · 2017-01-26 21:53 UTC

done [here](https://github.com/zulip/zulip/pull/3428)

**Steve Howell** · 2017-01-26 21:58 UTC

Thanks!  Let me give you another test case...

**Aditya Bansal** · 2017-01-26 21:58 UTC

For the indents part i believe i didn't explained very much.
So in that part what i did is that whenever we have a new block we record the indent at which it.
```.html
    foobar<div>
          text in here
          </div>
```
So in the above when we apply correct indent it becomes something like this
```.html
    foobar<div>
               text in here
          </div>
```
So the text here part gets indented with respect to div with 4 space indent.

**Steve Howell** · 2017-01-26 22:01 UTC

Hopefully we don't have input HTML that is quite that bad, but it's still a reasonable thing to test.

**Steve Howell** · 2017-01-26 22:02 UTC

But here's what I think will be a more common case that we want to get right:

~~~ html
<div>
  foo 
  <p>hello</p>
  bar 
</div>

<div>
    foo 
    <p>hello</p>
    bar 
</div>

**Aditya Bansal** · 2017-01-26 22:02 UTC

no actually the example i sent is not what i wanted to

**Aditya Bansal** · 2017-01-26 22:02 UTC

something is wrong, like i put in spaces and it rendered it differently.

**Tim Abbott** · 2017-01-26 22:03 UTC

Using view source, it looks consistent with what you typed?

[pasted image](https://chat.zulip.org/user_uploads/2/ee/DagRF6fzjoNzaChjAKaQbrLu/pasted_image.png)

**Aditya Bansal** · 2017-01-26 22:05 UTC

actually i was hoping it to have 'text in here' just below div part

**Aditya Bansal** · 2017-01-26 22:06 UTC

Like if we put in equal space then why did closing div tag move far from where it was placed.

**Aditya Bansal** · 2017-01-26 22:11 UTC

@Steve Howell I added the test case you gave me to unit tests and pushed the changes [here](https://github.com/zulip/zulip/pull/3428).
On my local setup i believe it passes.

**Steve Howell** · 2017-01-26 22:18 UTC

https://github.com/zulip/zulip/pull/3428/files#r98105566

**Aditya Bansal** · 2017-01-26 22:18 UTC

Ohk I get what tim wanted to say. Yeah that was consistent with what i typed, i didn't actually count the spaces.

**Aditya Bansal** · 2017-01-26 22:23 UTC

That was a mistake steve. I intended to have 
`info['offset']` in place of `offset` in there.

**Steve Howell** · 2017-01-26 22:28 UTC

No worries, that's what I'm here for. :)

**Steve Howell** · 2017-01-26 22:31 UTC

I think the next steps are this:
* Keep cleaning up your code, as you mentioned you felt there were a few things you could de-duplicate.
* Add a few more minimal tests cases, even if they're slightly overlapping.
* Re-run the tool against the templates that are currently in your PR.
* We'll have some other folks look at the diffs for the templates and make sure they don't spot anything that we have overlooked.

**Aditya Bansal** · 2017-01-26 22:36 UTC

yeah will do that 
For the cleaning up the code part, I may need to change the structure entirely 
Like what i had in mind was to start the looping on lines from the start instead of looping on tokens and keep a token list to see through as we move down the lines as use tokens to do the same block thing with help of stack.
I don't know what i will end up with kind of have a vague picture of what it would be like. I go on with that and will show you what I had in mind.

**Steve Howell** · 2017-01-26 22:41 UTC

Ok, sounds interesting!

**Aditya Bansal** · 2017-02-02 18:10 UTC

Hey @Steve Howell 
I ran the tool again on the templates in the [PR](https://github.com/zulip/zulip/pull/3428) and found this issue
```
{{#if author}}
    <span class="emoji_author">{{author.full_name}}</span>
    {{else}}
    <span class="emoji_author">Unknown Author</span>
{{/if}}
```
But the Expected should be 
```
{{#if author}}
    <span class="emoji_author">{{author.full_name}}</span>
{{else}}
    <span class="emoji_author">Unknown Author</span>
{{/if}}
```
I wanted to ask whether should i add a conditional exception for that?

**Steve Howell** · 2017-02-02 18:58 UTC

Interesting...yeah, "else" is kind of tricky for these kind of tools.  There might not  be a super elegant way to handle "else", so it's fine if we need to special-case this somehow.

**Aditya Bansal** · 2017-02-02 19:00 UTC

ohk then i add it as special case.

**Aditya Bansal** · 2017-02-07 20:13 UTC

Hey @Steve Howell 
I fixed a case that i found out in the pretty_print
Basically nested tags in a single line where causing some issue.
Here is the updated [PR](https://github.com/zulip/zulip/pull/3428).

**Steve Howell** · 2017-02-07 20:50 UTC

Cool!   Do you feel like we're getting close enough where we can maybe do a big commit fixing all the handlebars templates, but not actually pushing out the tool, and then we'll merge that and see if we can get any problems with the newly formatted templates?

We just released 1.5.1, so we can be a bit more aggressive now about making changes.

**Aditya Bansal** · 2017-02-07 20:58 UTC

I feel like so as i couldn't think of some other test case where failure might occur.
So yaa a commit with all handlebar templates indented should be the way to go.
Should i run the tool on all handlebar templates and make a new PR with them?
If anything more occurs with templates, tool could be updated accordingly.

**Steve Howell** · 2017-02-07 20:59 UTC

yep, sounds good

**Steve Howell** · 2017-02-07 21:00 UTC

If all goes well with the handlebars templates, then we'll do Django after that.

**Tim Abbott** · 2017-02-07 21:01 UTC

In terms of merging things, I'll want to be strategic about reindenting first the templates that don't have open PRs to avoid unnecessary merge conflicts

**Tim Abbott** · 2017-02-07 21:02 UTC

I guess actually it'd be pretty cool to build a tool for figuring this out to help advice big refactorings in general -- basically fetches the diffstats of all open PRs and then shows you which files are totally safe and which PRs are most at risk (so you can try to work them out)

**Aditya Bansal** · 2017-02-07 21:07 UTC

i am getting the idea about what you are saying @Tim Abbott 
Infact i was first going to ask about the existence of such a tool. 
I will try out and see if some small python script could help me out and then we can talk about turning it into a tool.

**Tim Abbott** · 2017-02-07 21:22 UTC

As a sidenote, I just added the `pep8` linter to how `lint-all` gets run in the pre-commit hook, since there's no performance reason not to

**Steve Howell** · 2017-02-07 22:40 UTC

The other approach here is to make a single commit for each template, and then we can revert formatting changes for particular templates if needed to facilitate merging old PRs.

**Tim Abbott** · 2017-02-07 22:40 UTC

yeah that's probably the expedient approach :)

**Steve Howell** · 2017-02-07 22:41 UTC

But I also like the find-old-PRs tooling approach, and none of this beautification is super urgent.

**Aditya Bansal** · 2017-02-13 00:13 UTC

Hey @Steve Howell @Tim Abbott 
I made a new PR with handlebar templates which are not currently in any of the PR's as the approach @Tim Abbott  suggested. Here is the new [PR](https://github.com/zulip/zulip/pull/3658). Please take a look.
Also I wrote a small tool to figure out files in any directory to find out which are at risk and which are safe to merge in sense Tim talked about. Here is the [tool](https://github.com/adnrs96/TinglingGit).

**Tim Abbott** · 2017-02-13 00:25 UTC

Awesome!

**Tim Abbott** · 2017-02-13 00:25 UTC

I'd love to check in the tool as well, since I think we'll want to use it for other refactorings in the future :)

**Tim Abbott** · 2017-02-13 00:26 UTC

Stylistically, we haven't been indenting handlebars conditionals, so:
```
+                {{#if subscribed}}
+                    Unsubscribe
+                {{else}}
+                    Subscribe
+                {{/if}}
```

I'd prefer to be
```
+                {{#if subscribed}}
+                Unsubscribe
+                {{else}}
+                Subscribe
+                {{/if}}
```

**Aditya Bansal** · 2017-02-13 00:26 UTC

I Intent to improve the tool more since its quite slow right now.

**Tim Abbott** · 2017-02-13 00:27 UTC

I'll look to see if anything else should be different

**Aditya Bansal** · 2017-02-13 00:28 UTC

Does that mean that none of handlebar tags should be indented to further deeper level?

**Tim Abbott** · 2017-02-13 00:28 UTC

That's my preference; it's the style we've been trying to use

**Tim Abbott** · 2017-02-13 00:28 UTC

If you don't do that, then things get super deep

**Tim Abbott** · 2017-02-13 00:30 UTC

I would consider making an exception for places where we might have multiple layers of handlebars tags, e.g.
```
+            {{#each message_containers}}
+                {{#with this}}
+                    {{partial "single_message" "use_match_properties" ../../../../use_match_properties "table_name" ../../../../table_name}}
+                {{/with}}
+            {{/each}}
```

**Aditya Bansal** · 2017-02-13 00:33 UTC

I will add an exception for multiple layers then and remove indenting to further levels in handlebar tags in general.

**Tim Abbott** · 2017-02-13 00:39 UTC

sounds good!

**Steve Howell** · 2017-02-13 16:01 UTC

Aditya, I'm online now if you have any questions about the tooling stuff.  It seems like you're continuing to make great progress!

**Aditya Bansal** · 2017-02-13 16:45 UTC

I am actually just going to start working on it. Currently i guess i have a idea about what might be needed to be done for the handlebar stuff. I try it out and let you know if i run into some trouble. 
Regarding the tool to determine possible merge conflicts i try to make it use async calls to github api so that it may speed up the tool a little bit, currently its super slow. But i had doubts about how should the output be generated.
For example 
 * tool should analyse all the files in the current directory from where it was run and display stuff.
 * tool should accept some kind of input in args possibly file name for which result should be displayed.
 * tool should accept a path in args and for it tool analyses all files.

Currently i have the first option used for the tool. And files which are in none of the PR's are output in green and others in red.
Will like your views on it.

**Aditya Bansal** · 2017-02-14 22:28 UTC

Hey @Steve Howell @Tim Abbott 
I moved a little bit forward on the issue. I have updated the PR[#3658](https://github.com/zulip/zulip/pull/3658) for template cleanup with new commit. Now it does something like this with handlbar tags.
```
+                {{#if subscribed}}
+                Unsubscribe
+                {{else}}
+                Subscribe
+                {{/if}}
``` 
and for nested handlebars something like this
```
+            {{#each message_containers}}
+            foobar
+            {{#with this}}
+                {{partial "single_message" "use_match_properties" ../../../../use_match_properties "table_name" ../../../../table_name}}
+            {{/with}}
+            morecontent
+            {{/each}}
```

**Aditya Bansal** · 2017-02-14 22:29 UTC

Also i have updated the PR[#3428](https://github.com/zulip/zulip/pull/3428) with new commit for changes in pretty_print tool.
Please take a look.

**Steve Howell** · 2017-02-14 23:47 UTC

Things are looking pretty good.  Can you create one squashed commits for everything directly related to the tool?

**Aditya Bansal** · 2017-02-14 23:48 UTC

Like including the handlebar cleanup as well?

**Aditya Bansal** · 2017-02-14 23:51 UTC

or the tooling alone and keeping handlebar cleanup in a separate PR as it is now.

**Steve Howell** · 2017-02-15 00:01 UTC

keep the handlebar cleanup separate

**Steve Howell** · 2017-02-15 00:01 UTC

but the tool+tests can be one commit

**Aditya Bansal** · 2017-02-15 00:02 UTC

ohk i will then drop the commits which cleaned up 4 templates for testing purpose

**Aditya Bansal** · 2017-02-15 00:45 UTC

I have squashed the commits [here](https://github.com/zulip/zulip/pull/3428). Nothing big but wanted to ask should I squash all the commits into your commit or keep two commits as i have currently done. Also, I mentioned your old PR in commit message in hopes that it automatically closes that when merged. Is that fine thing to do?

**Steve Howell** · 2017-02-15 01:13 UTC

You can squash my commit into yours and just mention my name in the commit message as having helped with it.

It looks like there's a stray template in the PR.

**Aditya Bansal** · 2017-02-15 05:21 UTC

Here i have updated the [PR](https://github.com/zulip/zulip/pull/3428).
Yeah there was a left out template in PR previously, I must have missed out.

**Steve Howell** · 2017-02-15 05:33 UTC

Can you make the first line of the commit message be...

~~~
tools: Create HTML pretty printer.

**Aditya Bansal** · 2017-02-15 05:35 UTC

sure, done

**Steve Howell** · 2017-02-15 05:37 UTC

I'm about to go to bed, but I will try to get this merged tomorrow assuming Travis passes.

**Aditya Bansal** · 2017-02-15 05:43 UTC

No worries.
Thanks for the help and reviewing.

**Steve Howell** · 2017-02-15 15:40 UTC

I just merged the tool.  The next step is to merge a few of the templates after applying the tool to it.  Ideally we'd have a  single commit for each template.

**Tim Abbott** · 2017-02-15 16:09 UTC

Yay, this is exciting :)

**Aditya Bansal** · 2017-02-15 16:25 UTC

ahh i guess some improvement to tool might be needed to incorporate this case pointed out by Tim here https://github.com/zulip/zulip/pull/3658#pullrequestreview-21930210
I try incorporate the case in tool and then will apply it to some templates.

**Tim Abbott** · 2017-02-15 16:30 UTC

yeah, we'll probably find a subtle issue like that or two as we review the reformatting of the templates :)

**Aditya Bansal** · 2017-02-15 16:33 UTC

So should i first apply the tool and update the templates cleanup PR?

**Aditya Bansal** · 2017-02-15 16:34 UTC

with single commit per template because otherwise currently in this [PR](https://github.com/zulip/zulip/pull/3658) most recent code of tool was used.

**Steve Howell** · 2017-02-15 16:43 UTC

yep, I'd fix up the tool first, and then start applying changes to the templates...we may have a little minor churn here, as you may find some edge cases you missed, but that's a normal part of the process

**Aditya Bansal** · 2017-02-15 17:14 UTC

On it.

**Aditya Bansal** · 2017-02-15 20:35 UTC

I have updated the Handlebar cleanup [PR#3658](https://github.com/zulip/zulip/pull/3658) with new commits with one commit per template after fixing the html singleton tags issue in the pretty printing tool. I have updated the tool as well but I am not sure where to push changes in the tool, should I push it in the [PR#3428](https://github.com/zulip/zulip/pull/3428) which got merged or create  a new one?

**Aditya Bansal** · 2017-02-15 21:07 UTC

Also the templates that i have included in the PR are only those which are not currently present in any of the open PR's. 
These templates were determined by the kind of tool Tim suggested to develop for the purpose. Here is the link to the [tool](https://github.com/adnrs96/TinglingGit). I believe the tool is now somewhat usable in basic terms. Would like your review on it.

**Steve Howell** · 2017-02-15 21:11 UTC

You can put your tool changes on to #3658 at this point.  I'm not sure what we want to do with your git tool.  There's some merit in leaving it as a separate project.

**Aditya Bansal** · 2017-02-15 21:14 UTC

Actually @Tim Abbott  had a view that it could be useful in big refactoring.

**Aditya Bansal** · 2017-02-15 21:17 UTC

I have kind of used a hack to incorporate singleton html tags. I have updated the [PR](https://github.com/zulip/zulip/pull/3658) with the commit concerning update in pretty printing tool.

**Steve Howell** · 2017-02-15 22:24 UTC

I guess I don't understand why singletons can't be treated just like ordinary text.

**Aditya Bansal** · 2017-02-16 09:41 UTC

They can be and they were being treated like that only in the commit that got merged but later on this case was found.
```
-  <label class="checkbox">
 -    <input type="checkbox" name="stream" value="{{name}}"
 -           {{#unless invite_only}}checked="checked"{{/unless}} /> {{name}}
 -    {{#if invite_only}}<i class="icon-vector-lock"></i>{{/if}}
 -  </label>
```

**Aditya Bansal** · 2017-02-16 09:41 UTC

In this case if we treat the singleton's like normal text no doubt they get indented but since the singleton has a line span of more than 1 it will get indented like this.
```
-  <label class="checkbox">
 -      <input type="checkbox" name="stream" value="{{name}}"
 -      {{#unless invite_only}}checked="checked"{{/unless}} /> {{name}}
 -      {{#if invite_only}}<i class="icon-vector-lock"></i>{{/if}}
 -  </label>
```
Observe the indent of the 3rd line it starts from where the input tag is starting although the input tag is not closed yet. I guess the expected behaviour here is to have at least some extra indent in the 3rd line so as to display that input tag is not over. So i added a kind of a hack to make that happen by respecting whatever indent there was already present in the continuation line of the input tag.

**Aditya Bansal** · 2017-02-16 09:44 UTC

This indenting in case of multi line span of tags is taken care of for other tags with a ending tag automatically since these line are treated as text and get indented, since we indent all text between starting and ending tags.

**Steve Howell** · 2017-02-16 15:29 UTC

Interesting...I am guessing that part of the problem here is that `{{#unless}}` is a handlebars tag.  I think instead of your hack to the pretty printer, we should just change the parser in one of two ways:
* We can have the parser ignore handlebars tags inside of singleton tags.  This makes us a bit blind to possible errors there, but it simplifies pretty printing.
* We can have the parser emit the `html_singleton_end` tag for us.  This may require some tiny tweaks to our other tools, but I don't think it would be so bad.

I'm more inclined to the first option for now.

**Aditya Bansal** · 2017-02-16 15:36 UTC

I believe `{{#unless}}` being a handlebar tag here could not be a problem. Since when we tokenize, anything within a tag itself isn't tokenized

**Aditya Bansal** · 2017-02-16 15:37 UTC

what i mean to say is that when we say this 
``` 
<input type="checkbox" name="stream" value="{{name}}"
        {{#unless invite_only}}checked="checked"{{/unless}} />
```
to be a tag then our template parser doesn't recognise `{{#unless}}` as a handlebar tag

**Steve Howell** · 2017-02-16 15:57 UTC

Ok, then maybe the problem here is that we are generally too opinionated about indenting text that is not in a "pre" tag?  The original strategy was just to nudge text over.   I guess some of the other issues make that tricky to go back to.

**Aditya Bansal** · 2017-02-16 16:11 UTC

The problem with just nudging text over was that the indentation would not be rightly done. For example
```
<div>
  foobar
  <div>
    test
  </div>
</div>
```

**Aditya Bansal** · 2017-02-16 16:12 UTC

Would have become 
```
<div>
  foobar
    <div>
      text
    </div>
</div>
```

**Aditya Bansal** · 2017-02-16 16:12 UTC

Observe the `foobar` with only 2 space indent and same is with `text`

**Steve Howell** · 2017-02-16 16:16 UTC

Well, we could nudge thus pretty easily, but then the problem was identifying the continuation lines, correct?

**Aditya Bansal** · 2017-02-16 16:23 UTC

identifying the continuation lines? I meant that problem while just nudging text over was if text inside some tag was at some wrong indent level, it remained like that.

**Aditya Bansal** · 2017-02-16 16:35 UTC

If you meant by continuation lines, multiple line tag definitions then, nudging would have saved the original indent for tag continuation but text would not be indented right but if we indent text right like now we are doing original indent of tag's continuation line is lost and we indent that too a 4 spaces.

**Aditya Bansal** · 2017-02-16 16:46 UTC

The core of problem here according to me is that the code is designed in such a way that it indents tags such that tags have a opening and ending tag. But since we came across a singleton tag which isn't supposed to have a body but may have multiple line tag itself things cause problem since we were handling such cases for other tags replying on fact they have a closing tag but now there isn't one. So the possible solution according to me here was 
* Add a singleton_end tag dynamically into tokens list (that's the hack) when we find a singleton tag so as to just nudge the lines between start and end of singleton tag.
* Modify template parser to output tokens with more information about starting and ending line of a tag so as to exactly figure out line from which body starts.

**Steve Howell** · 2017-02-16 16:54 UTC

I think I favor the approach of having the template parser produce more useful info.

**Steve Howell** · 2017-02-16 16:56 UTC

It's kind of lame that the template parser only stores the start line/column.  I don't think that would be too hard to fix.

**Aditya Bansal** · 2017-02-16 16:57 UTC

In that case as well we will need to deal with singleton tags specially in the pretty printing tool.

**Aditya Bansal** · 2017-02-16 16:57 UTC

yaa it shouldn't be hard to fix

**Aditya Bansal** · 2017-02-16 16:58 UTC

i guess i should try change template parser then, right?

**Steve Howell** · 2017-02-16 17:00 UTC

I would at least look at it to see how easy you think it is to fix.

**Steve Howell** · 2017-02-16 17:01 UTC

I'm still thinking about this.  On the one hand, if we're going to fix this, we should probably take the time to really make it right.  On the other hand, multi-line singleton tags are pretty rare, and we might want to just do something pragmatic to handle them.

**Steve Howell** · 2017-02-16 17:02 UTC

A good data point here would be to know how many of our templates have these multi-line singleton tags.

**Aditya Bansal** · 2017-02-16 17:02 UTC

i guess i can get a number, wait

**Steve Howell** · 2017-02-16 17:20 UTC

Just to enumerate a bunch of options:
* just use your hack, which may be fine
* use most of your hack, but have the parser populate something like a line_span or an end_line in the Token object (which could help other future tools)
* make the parser actually produce html_singleton_end tokens (and possibly even validate the handlebars stuff within it)

We could also change our approach to singleton tokens somehow:
* just make the template checker enforce that singleton tokens have to fit on one line (and we'll fix any existing cases)
* figure out a better way to handle things like "checked" fields without complex template logic (probably a non-starter, but I'm brainstorming)

**Aditya Bansal** · 2017-02-16 17:30 UTC

/srv/zulip/static/templates/alert_word_settings_item.handlebars 1
/srv/zulip/static/templates/stream_member_list_entry.handlebars 1
/srv/zulip/static/templates/invite_subscription.handlebars 1
/srv/zulip/static/templates/subscription_creation_form.handlebars 1
/srv/zulip/static/templates/single_message.handlebars 1
/srv/zulip/static/templates/subscription_table_body.handlebars 2
/srv/zulip/static/templates/compiled.js 68
/srv/zulip/static/templates/new_stream_users.handlebars 1
Total appearance 76

**Aditya Bansal** · 2017-02-16 17:37 UTC

This includes only cases where singleton's are multiple line spanned.

**Steve Howell** · 2017-02-16 17:37 UTC

compiled.js doesn't count :)

**Aditya Bansal** · 2017-02-16 17:38 UTC

yeah did a listdir() so ...

**Steve Howell** · 2017-02-16 17:40 UTC

I think there are enough of these that I don't want to force them to be one line, so that rules out one of my options.

**Steve Howell** · 2017-02-16 17:42 UTC

I'm starting to like your hack, but maybe we can have the parser report how many lines a token spans.

**Aditya Bansal** · 2017-02-16 17:43 UTC

yeah we can do that, I believe stuff from my hack could be transferred into parser to do that.

**Aditya Bansal** · 2017-02-16 17:43 UTC

Although I am curious about what did you meant by `"checked" fields`.

**Steve Howell** · 2017-02-16 17:43 UTC

Sounds good.

**Aditya Bansal** · 2017-02-16 17:45 UTC

Like could you please give some more info on the last option you suggested.

**Steve Howell** · 2017-02-16 17:46 UTC

I didn't have a concrete idea on the "checked" fields, but I was thinking something like a partial that we use for certain types of input fields, and then we could exempt those partials from our checks.   Or maybe we do more logic in JS/jQuery to simplify the template.  But I think there are too many places to fix for that to be practical, and those solutions would be overkill for a pretty small nuisance in our pretty printer.

**Aditya Bansal** · 2017-02-16 18:31 UTC

I too feel that to be a overkill
About the template parser modification, should I make the parser output an extra tag for html_singleton_end token just after the html_singleton with almost same info and just changing the line of token using line span?

**Aditya Bansal** · 2017-02-16 18:31 UTC

I am currently adding a line_span field

**Steve Howell** · 2017-02-16 18:35 UTC

I think either or both is ok.  We probably want line_span for future uses as well as what you're doing.  I can also see having the parser emit a dummy html_singleton_end token for convenience that most tools will just ignore, but which the pretty printer can use.

**Aditya Bansal** · 2017-02-16 18:43 UTC

I would go with both

**Aditya Bansal** · 2017-02-16 19:49 UTC

I have updated the [PR](https://github.com/zulip/zulip/pull/3658/) with new commits. Please take a look.

**Steve Howell** · 2017-02-16 19:59 UTC

I think you can simplify the html_singleton_end() hack by doing it after the call to `advance` and using state.line and state.col.  You probably also want to add a comment explaining that it's kind of a pseudo tag for convenience.

**Steve Howell** · 2017-02-16 20:00 UTC

(within the template parser)

**Aditya Bansal** · 2017-02-16 20:06 UTC

ohh yes!!! I overlooked `advance`.

**Aditya Bansal** · 2017-02-16 20:41 UTC

Done updating [PR](https://github.com/zulip/zulip/pull/3658/).

**Steve Howell** · 2017-02-16 20:59 UTC

This one looks kind of funny:

https://github.com/adnrs96/zulip/blob/5bc4db4ea0b8c1ddf6499d8c5484083a12e42fcf/static/templates/message_group.handlebars

**Aditya Bansal** · 2017-02-16 21:49 UTC

Yeah missed on that in logic resulting in staircase effect.

**Aditya Bansal** · 2017-02-16 21:50 UTC

updated [PR](https://github.com/zulip/zulip/pull/3658/) with new commit.

**Steve Howell** · 2017-02-16 21:54 UTC

The code change looks good, but we probably want a test for that.

**Aditya Bansal** · 2017-02-16 21:56 UTC

Yeah i was thinking to add one first, anyways will do right away.

**Steve Howell** · 2017-02-16 21:57 UTC

@Tim Abbott I was hoping to merge the first four commits here: https://github.com/zulip/zulip/pull/3658/commits

I think it's useful at this point to get the ball rolling a bit on the HTML cleanup.

**Aditya Bansal** · 2017-02-16 22:02 UTC

Added a test case for the staircase effect and updated the PR

**Steve Howell** · 2017-02-16 22:06 UTC

Can you clean up the commit message here?

https://github.com/zulip/zulip/pull/3658/commits/d357540480c5fcf01c6c714e4f6935789cd875f8

**Steve Howell** · 2017-02-16 22:07 UTC

In the first line of the commit message, you can be more concise by removing filler words like "Add the ability to."

**Aditya Bansal** · 2017-02-16 22:08 UTC

on it

**Steve Howell** · 2017-02-16 22:08 UTC

It's a bit of an art to squeeze as much info into 65 characters or so, but it really does help when people are looking at the logs.  You can be more verbose in the following paragraphs to elaborate on the details.

**Aditya Bansal** · 2017-02-16 22:26 UTC

yeah i agree its quite a art.
I have updated the [PR](https://github.com/zulip/zulip/pull/3658) and kind of cleaned up the commit message.

**Tim Abbott** · 2017-02-16 22:39 UTC

OK looking at these

**Tim Abbott** · 2017-02-16 22:41 UTC

I don't see any problematic renderings through 4a93a7e9d59c60b97e8bc9c54899ccb4a0c38481

**Tim Abbott** · 2017-02-16 22:41 UTC

Is there a reason you said "first four" and not more @Steve Howell ?

**Steve Howell** · 2017-02-16 22:42 UTC

I'd be up for merging at least four of the templates. :)   But probably not all of them right away.

**Tim Abbott** · 2017-02-16 22:45 UTC

Yeah I just read through them all, and most seem great on casual reading; I think I'll merge that subset to make it easier for focus on the things that we need to work more on the tool for

**Steve Howell** · 2017-02-16 22:45 UTC

Sounds good!

**Tim Abbott** · 2017-02-16 22:46 UTC

I guess there are a total of ~20 such commits, merged!

**Steve Howell** · 2017-02-16 22:48 UTC

Awesome!

**Steve Howell** · 2017-02-16 22:57 UTC

Aditya, how do you feel about letting these changes sit on master for a couple days, just to see if we discover any issues with them?  Meanwhile if you want to work on other stuff, I have some ideas, or maybe you have other things you were looking at.

**Aditya Bansal** · 2017-02-16 23:00 UTC

Yeah i was about to ask about workflow for finding possible issues. I am fine with letting it on master.
I would love to hear ideas about other stuff i could work upon.

**Aditya Bansal** · 2017-02-16 23:04 UTC

But firstly i would like to thank you and Tim for helping me and reviewing my PR.

**Steve Howell** · 2017-02-16 23:13 UTC

You're welcome, first of all! :)  And thanks for all your work.

**Steve Howell** · 2017-02-16 23:15 UTC

One thing that we have currently is a backlog of PRs that need to be reviewed, so we are trying to encourage all contributors who have had a few of their own commits merged to help look at PRs.  You probably have a feel for what we look for, based on some of my comments on your PRs.  Basically, things like this:
* commit messages
* overall design
* clear variable names
* simply asking questions where you find the code confusing

**Steve Howell** · 2017-02-16 23:16 UTC

Also, for a coding thing, we have an issue open to improve our message handling for the check-templates tools in certain cases.

**Steve Howell** · 2017-02-16 23:16 UTC

For some errors we are good about reporting line numbers, but in other cases our messages aren't helpful.

**Steve Howell** · 2017-02-16 23:20 UTC

see https://github.com/zulip/zulip/pull/2859 for an attempt at cleaning up the errors...I think your deeper knowledge of the parser will lead to a better approach

**Aditya Bansal** · 2017-02-16 23:23 UTC

I will surly have a look.

**Tim Abbott** · 2017-02-17 00:09 UTC

A few other follow-up things we can do on template formatting:
* Doing the same sort of indentation work on the templates/zerver/ templates.
* Doing another round of merging template changes, targeting things where conflicting PRs have small conflict diffstats (even if nonzero)

**Steve Howell** · 2017-02-17 00:52 UTC

Another thing to do is find the PRs where there may be merge conflicts and do a quick comment asking the author what the status is and giving them a heads up about upcoming changes.

**Tim Abbott** · 2017-02-17 02:02 UTC

Also if there's a handy list, we could potentially focus on merging those PRs

**Aditya Bansal** · 2017-02-17 16:48 UTC

static/templates/stream_sidebar_actions.handlebars [PR#1432](https://github.com/zulip/zulip/pull/1432)
static/templates/subscription_settings.handlebars [PR#3676](https://github.com/zulip/zulip/pull/3676) [PR#3479](https://github.com/zulip/zulip/pull/3479) [PR#3512](https://github.com/zulip/zulip/pull/3512)
static/templates/subscription_table_body.handlebars [PR#3512](https://github.com/zulip/zulip/pull/3512)
static/templates/user_presence_rows.handlebars [PR#850](https://github.com/zulip/zulip/pull/850)
static/templates/message_reaction.handlebars [PR#3573](https://github.com/zulip/zulip/pull/3573)
static/templates/user_presence_row.handlebars [PR#850](https://github.com/zulip/zulip/pull/850)
static/templates/change_stream_privacy.handlebars [PR#3512](https://github.com/zulip/zulip/pull/3512)
static/templates/recipient_row.handlebars [PR#2973](https://github.com/zulip/zulip/pull/2973)
static/templates/subscription_type.handlebars [PR#1122](https://github.com/zulip/zulip/pull/1122) [PR#1432](https://github.com/zulip/zulip/pull/1432)
static/templates/stream_sidebar_row.handlebars [PR#1432](https://github.com/zulip/zulip/pull/1432) [PR#2973](https://github.com/zulip/zulip/pull/2973)
static/templates/admin_tab.handlebars [PR#3349](https://github.com/zulip/zulip/pull/3349)
static/templates/stream_member_list_entry.handlebars [PR#1122](https://github.com/zulip/zulip/pull/1122)
static/templates/user_sidebar_actions.handlebars [PR#850](https://github.com/zulip/zulip/pull/850)
static/templates/message_edit_form.handlebars [PR#3337](https://github.com/zulip/zulip/pull/3337)
static/templates/single_message.handlebars [PR#2973](https://github.com/zulip/zulip/pull/2973)
static/templates/subscription.handlebars [PR#1122](https://github.com/zulip/zulip/pull/1122) [PR#1432](https://github.com/zulip/zulip/pull/1432)
static/templates/settings_tab.handlebars [PR#1747](https://github.com/zulip/zulip/pull/1747) [PR#382](https://github.com/zulip/zulip/pull/382)
static/templates/tutorial_message.handlebars [PR#3420](https://github.com/zulip/zulip/pull/3420)
static/templates/email_address_hint.handlebars [PR#3420](https://github.com/zulip/zulip/pull/3420)
static/templates/admin_user_list.handlebars [PR#2792](https://github.com/zulip/zulip/pull/2792) [PR#2899](https://github.com/zulip/zulip/pull/2899) [PR#3424](https://github.com/zulip/zulip/pull/3424)
static/templates/actions_popover_content.handlebars [PR#632](https://github.com/zulip/zulip/pull/632) [PR#1204](https://github.com/zulip/zulip/pull/1204) [PR#3366](https://github.com/zulip/zulip/pull/3366)
static/templates/subscription_setting_icon.handlebars [PR#1432](https://github.com/zulip/zulip/pull/1432)
static/templates/stream_privacy.handlebars [PR#2973](https://github.com/zulip/zulip/pull/2973)
static/templates/bot_avatar_row.handlebars [PR#2792](https://github.com/zulip/zulip/pull/2792)

**Aditya Bansal** · 2017-02-17 16:50 UTC

These are the PR's which have changes to these templates. I haven't made tool accurate enough too tell how big are the changes yet (frankly not thought of how could that be done).

**Steve Howell** · 2017-02-17 17:17 UTC

@Tim Abbott I am thinking a reasonable cutoff here might be < 2800 for PR number where we assume they're already gonna have major rebase work or the PR is likely to be abandoned, so we can just have Aditya clean up templates referenced by the old PRs.  Thoughts?

**Steve Howell** · 2017-02-17 17:22 UTC

A fair number of these are from krtkmj.

**Tim Abbott** · 2017-02-17 18:52 UTC

I was thinking of doing something cool with how big the changes are, and basically any template with not a lot of total lines of changes would be clear; and we'd try to investigate whether we can push for merging any PRs that are keeping it stuck

**Tim Abbott** · 2017-02-17 18:53 UTC

I'm actually in the process of trying to merge a lot of these PRs that have things stuck

**Tim Abbott** · 2017-02-17 18:53 UTC

So possibly we can just sorta reformat as we go

**Aditya Bansal** · 2017-02-22 23:32 UTC

Hey @Tim Abbott @Steve Howell 
I have made a new [PR](https://github.com/zulip/zulip/pull/3764) in which we cleanup the Django templates located here `/templates/zerver/` to use 4 space indents. This contains all templates which didn't posed any possible merge conflicts with any of the open PR's currently. I have updated [PR#3658](https://github.com/zulip/zulip/pull/3658) with updates to pretty_print tool so support Django cleanup as well.  Also here is a list of templates which have open PR's to.

**Aditya Bansal** · 2017-02-22 23:32 UTC

templates/zerver/left-sidebar.html [PR#3579(+6-0)](https://github.com/zulip/zulip/pull/3579)
templates/zerver/compose.html [PR#3118(+1-2)](https://github.com/zulip/zulip/pull/3118) [PR#2721(+1-0)](https://github.com/zulip/zulip/pull/2721) [PR#2973(+6-6)](https://github.com/zulip/zulip/pull/2973) [PR#3023(+2-1)](https://github.com/zulip/zulip/pull/3023)
templates/zerver/login.html [PR#1747(+7-2)](https://github.com/zulip/zulip/pull/1747)
templates/zerver/navbar.html [PR#2379(+1-0)](https://github.com/zulip/zulip/pull/2379) [PR#2973(+31-39)](https://github.com/zulip/zulip/pull/2973)
templates/zerver/register.html [PR#3690(+1-0)](https://github.com/zulip/zulip/pull/3690) [PR#3007(+3-0)](https://github.com/zulip/zulip/pull/3007)
templates/zerver/keyboard_shortcuts.html [PR#3715(+8-7)](https://github.com/zulip/zulip/pull/3715) [PR#2292(+8-0)](https://github.com/zulip/zulip/pull/2292) [PR#2854(+4-0)](https://github.com/zulip/zulip/pull/2854)
templates/zerver/index.html [PR#2292(+1-0)](https://github.com/zulip/zulip/pull/2292) [PR#3023(+1-0)](https://github.com/zulip/zulip/pull/3023)
templates/zerver/home.html [PR#2089(+2-0)](https://github.com/zulip/zulip/pull/2089) [PR#3002(+2-0)](https://github.com/zulip/zulip/pull/3002) [PR#749(+5-0)](https://github.com/zulip/zulip/pull/749)
templates/zerver/subscriptions.html [PR#1954(+1-0)](https://github.com/zulip/zulip/pull/1954)
templates/zerver/right-sidebar.html [PR#3718(+6-1)](https://github.com/zulip/zulip/pull/3718) [PR#2973(+2-8)](https://github.com/zulip/zulip/pull/2973)
templates/zerver/settings_overlay.html [PR#3748(+2-0)](https://github.com/zulip/zulip/pull/3748)
templates/zerver/base.html [PR#3330(+3-0)](https://github.com/zulip/zulip/pull/3330)

**Aditya Bansal** · 2017-02-22 23:32 UTC

The list also depicts some sort of idea about how big are the changes to files in those open PR's using number of lines added or deleted. 
Here is a similar list for handlebar templates we were talking about last time. Although i already posted a list for these but this one also gives an idea about size of changes in those PR's.

**Aditya Bansal** · 2017-02-22 23:32 UTC

static/templates/stream_sidebar_actions.handlebars [PR#1432(+19-9)](https://github.com/zulip/zulip/pull/1432)
static/templates/subscription_settings.handlebars [PR#3676(+1-0)](https://github.com/zulip/zulip/pull/3676) [PR#3479(+4-4)](https://github.com/zulip/zulip/pull/3479) [PR#3512(+6-10)](https://github.com/zulip/zulip/pull/3512)
static/templates/subscription_table_body.handlebars [PR#3512(+27-0)](https://github.com/zulip/zulip/pull/3512)
static/templates/user_presence_rows.handlebars [PR#850(+5-1)](https://github.com/zulip/zulip/pull/850)
static/templates/admin_emoji_list.handlebars [PR#3748(+2-0)](https://github.com/zulip/zulip/pull/3748)
static/templates/user_presence_row.handlebars [PR#850(+1-1)](https://github.com/zulip/zulip/pull/850)
static/templates/change_stream_privacy.handlebars [PR#3512(+0-11)](https://github.com/zulip/zulip/pull/3512)
static/templates/recipient_row.handlebars [PR#2973(+59-46)](https://github.com/zulip/zulip/pull/2973)
static/templates/subscription_type.handlebars [PR#1122(+1-0)](https://github.com/zulip/zulip/pull/1122) [PR#1432(+1-1)](https://github.com/zulip/zulip/pull/1432)
static/templates/stream_sidebar_row.handlebars [PR#1432(+8-2)](https://github.com/zulip/zulip/pull/1432) [PR#2973(+9-6)](https://github.com/zulip/zulip/pull/2973)
static/templates/admin_tab.handlebars [PR#3349(+24-8)](https://github.com/zulip/zulip/pull/3349)
static/templates/stream_member_list_entry.handlebars [PR#1122(+1-0)](https://github.com/zulip/zulip/pull/1122)
static/templates/user_sidebar_actions.handlebars [PR#850(+6-0)](https://github.com/zulip/zulip/pull/850)
static/templates/message_edit_form.handlebars [PR#3337(+3-0)](https://github.com/zulip/zulip/pull/3337)
static/templates/single_message.handlebars [PR#2973(+1-2)](https://github.com/zulip/zulip/pull/2973)
static/templates/subscription.handlebars [PR#1122(+2-0)](https://github.com/zulip/zulip/pull/1122) [PR#1432(+13-0)](https://github.com/zulip/zulip/pull/1432)
static/templates/settings_tab.handlebars [PR#1747(+1-0)](https://github.com/zulip/zulip/pull/1747) [PR#382(+11-0)](https://github.com/zulip/zulip/pull/382)
static/templates/tutorial_message.handlebars [PR#3420(+1-1)](https://github.com/zulip/zulip/pull/3420)
static/templates/email_address_hint.handlebars [PR#3420(+3-3)](https://github.com/zulip/zulip/pull/3420)
static/templates/admin_user_list.handlebars [PR#2792(+16-5)](https://github.com/zulip/zulip/pull/2792) [PR#2899(+21-14)](https://github.com/zulip/zulip/pull/2899) [PR#3424(+2-6)](https://github.com/zulip/zulip/pull/3424)
static/templates/actions_popover_content.handlebars [PR#632(+2-3)](https://github.com/zulip/zulip/pull/632) [PR#3366(+39-43)](https://github.com/zulip/zulip/pull/3366)
static/templates/subscription_setting_icon.handlebars [PR#1432(+8-2)](https://github.com/zulip/zulip/pull/1432)
static/templates/message_edit_history.handlebars [PR#3747(+10-2)](https://github.com/zulip/zulip/pull/3747)
static/templates/stream_privacy.handlebars [PR#2973(+2-0)](https://github.com/zulip/zulip/pull/2973)
static/templates/bot_avatar_row.handlebars [PR#2792(+10-0)](https://github.com/zulip/zulip/pull/2792)

**Steve Howell** · 2017-02-22 23:45 UTC

Looks great!  One template that might need some manual followup is markdown_help.html.  I think the automatic changes are definitely an improvement, but the original template had some strange formatting.

**Steve Howell** · 2017-02-22 23:47 UTC

Does your tool have way to report which files have good format?  (basically, you can either do a diff at the end or count lines changes as part of the tool itself)  We might want to see if some of the handlebars-related PRs are no longer open for some of the templates that we were holding off on before (but we want to exclude files that have already been fixed).

**Aditya Bansal** · 2017-02-22 23:51 UTC

Yeah i totally forgot to remove files that have been fixed already. Let me see if there is some way to automatically remove files which were fixed already.

**Tim Abbott** · 2017-02-22 23:58 UTC

Cool.  I'm really excited about your tool, BTW; I think we can use is to make our main remaining PEP8 migration painless (switching to two spaces between code and an inline comment)

**Aditya Bansal** · 2017-02-23 01:25 UTC

I have updated the [PR#3764](https://github.com/zulip/zulip/pull/3764) fixing the issue with `markdown_help.html` and one another issue with django tags.  I have updated the tool as well in this [PR#3658](https://github.com/zulip/zulip/pull/3658).

**Aditya Bansal** · 2017-02-23 01:33 UTC

Also i wanted to get review on this [PR#3742](https://github.com/zulip/zulip/pull/3742) improving error messages from our template parser.

**Steve Howell** · 2017-02-23 01:38 UTC

#3742 looks great!  I'm running tests locally and then will merge.  I think Tim should take a quick peek at the other two before we merge.  Thanks for the quick fixes!

**Steve Howell** · 2017-02-23 01:40 UTC

#3742 has been merged

**Aditya Bansal** · 2017-02-23 01:40 UTC

I again forgot to mention regarding the handlebar file list having PR's open to only 
static/templates/admin_emoji_list.handlebars [PR#3748(+2-0)](https://github.com/zulip/zulip/pull/3748)
Has been merged from the list mentioned above.

**Steve Howell** · 2017-02-23 01:46 UTC

Can you rebase #3658 against the latest copy of master and clean up the commits a bit?

**Aditya Bansal** · 2017-02-23 01:47 UTC

of course.

**Aditya Bansal** · 2017-02-23 02:02 UTC

Done.

**Tim Abbott** · 2017-02-23 04:29 UTC

I'm working through merging these; this is great

**Tim Abbott** · 2017-02-23 04:29 UTC

There's a few that I'm holding back because I know Brock has some not-yet-opened PRs on them (hello.html, features.html, apps.html, integrations.html); we can do those as soon as that work is merged

**Tim Abbott** · 2017-02-23 04:30 UTC

In #3764, the `accounts_html.html` one seems to have a few funny things around the `footer_padder`

**Tim Abbott** · 2017-02-23 04:30 UTC

Same issue with `accounts_send_confirm`; I think it's just that the `</div>`s are in the wrong spot

**Tim Abbott** · 2017-02-23 04:33 UTC

`authors.html` seems like a fairly messy one; probably a good test case for the indentation logic being a bit off :)

**Tim Abbott** · 2017-02-23 04:36 UTC

It looks like the templates that don't use Jinja2 conditionals are fine, so I merged a few of those

**Tim Abbott** · 2017-02-23 04:38 UTC

I think it might just be 2 bugs:
* The Jinja2 logic statements are having the thing inside them indented unconditionally, which produces deep nesting
* Some closing tags immediately after Jinja2 logic statements close seem to have the wrong offset

**Tim Abbott** · 2017-02-23 04:38 UTC

I'll let you track these down @Aditya Bansal; thanks again for doing this!  I'm really excited that we're finally going to have sanity in our templates :)

**Aditya Bansal** · 2017-02-23 13:25 UTC

thanks for reviewing this, let me take a look on what's wrong here.

**Aditya Bansal** · 2017-02-24 17:43 UTC

ohk i had this fixed and updated the [PR#3764](https://github.com/zulip/zulip/pull/3764) with new commits. Also i updated the tool and pushed a commit in [PR#3658](https://github.com/zulip/zulip/pull/3658). 
For the topic_edit_form.handlebars I didn't remove the extra space in comment area but fixed the issue of indenting to a deeper level on tags which are commented out.

**Steve Howell** · 2017-02-24 17:54 UTC

Looks good...we should add test coverage for the new template parsing stuff you did.

**Aditya Bansal** · 2017-02-24 17:55 UTC

yeah the tags in comments thing. On it.

**Aditya Bansal** · 2017-02-24 19:43 UTC

done adding test's. Updated the [PR#3658](https://github.com/zulip/zulip/pull/3658).

**Aditya Bansal** · 2017-03-12 14:16 UTC

Hey @Steve Howell 
Since the tooling for pretty_print has been merged now, i had been working on making having pretty_print tool being used to check indents in testing phase, i.e. the lint-all part. But i have ran into a choice which  i would like to have your views upon.
Since we are going to have the files pretty_print automatically we would want the tool to show the user the lines where the indents are not matching our 4 space standard. For this how should we proceed
* Make use of diff command in the same way done in check-css.
```
print('BOO! %s broken' % (fn,))
        open('foo.txt', 'w').write(section_list.text())
        os.system('diff %s foo.txt' % (fn,))
        sys.exit(1)
```
* Iterate over the list comparing lines and output lines with difference.

So which is more preferable here?

**Steve Howell** · 2017-03-12 14:17 UTC

Let's try the `diff` approach first. :)

**Aditya Bansal** · 2017-03-12 14:18 UTC

ohk

**Steve Howell** · 2017-03-12 14:18 UTC

BTW that "BOO!" in the current message is a bit informal, haha.  I think I wrote that and forgot to clean up the error message before checking in.

**Aditya Bansal** · 2017-03-12 14:19 UTC

I will do that, I am working on 4 space indents in CSS as well.

**Aditya Bansal** · 2017-03-12 14:20 UTC

I meant i will clean up the message

**Steve Howell** · 2017-03-12 14:24 UTC

sounds good!

**Aditya Bansal** · 2017-03-13 15:14 UTC

The linter now can automatically enforce 4 space indents with a exception list. But i have stumbled upon a mypy issue which seems like new for me (maybe some thing with those typeshed things i read in some issues and all).
`./tools/run-mypy --py3` gives the following error.
``` 
tools/lib/pretty_print.py:264: error: No overload variant of "write" of "BinaryIO" matches argument types [builtins.str]
```
Here is a [PR#4044](https://github.com/zulip/zulip/pull/4044) which has the code for automatic linting.

**Steve Howell** · 2017-03-13 15:36 UTC

I tried googling, and I couldn't find a good answer on the NamedTemporaryFile.  You could do `# type: ignore`, but I'd consider just using a real file here in the `var` directory.  It's not the end of the world if the `var` directory is cluttered, and experienced users of your tool may choose to just take the re-formatted copy and overwrite their version.  Or they may want to open the "good" version in the editor to see what's up.

**Aditya Bansal** · 2017-03-13 15:40 UTC

yeah using the file to see the good version is a nice case. I should have thought of it. Anyways i like to go with file now.

**Steve Howell** · 2017-03-13 15:47 UTC

Sounds good.  We should probably report the mypy error, too, but we can wait till Tim comes online for that.

**Tim Abbott** · 2017-03-13 17:59 UTC

I think this is an annotation or Python 3 bug, not a mypy bug.  `BinaryIO.write` expected to be passed a `bytes`

**Tim Abbott** · 2017-03-13 17:59 UTC

And you're passing it a `str`, which in Python 2 is a bytes and in Python 3 is a unicode

**Tim Abbott** · 2017-03-13 18:00 UTC

So either we need to call `zerver.str_utils.force_bytes` (which does nothing on Python 2 and encodes it on python 3) if i actually returns `str`, or something else

**Aditya Bansal** · 2017-03-14 11:28 UTC

Yes agreed Tim. 
I still would like to go ahead and write to a actual file to gain the benefits Steve mentioned. This solves the mypy error as well, might be the case that `write` function must be having definition to deal with different meanings of `str` in py2 and py3.  Updated the [PR#4044](https://github.com/zulip/zulip/pull/4044).
( I was not able to make an import to `zerver.lib.str_utils` to import `force_bytes` from `tools/lib/pretty_print`. Is there a simple way to do so, i mean import stuff from under `zerver package` to `tools package`?)

**Aditya Bansal** · 2017-03-14 14:12 UTC

Just created [PR#4062](https://github.com/zulip/zulip/pull/4062) to address 4 space indents in CSS. This PR currently has an extra commit from [PR#4044](https://github.com/zulip/zulip/pull/4044) which was also modifying pretty_print. I didn't wanted to have a merge conflict later on, so i added the extra commit so that i could get it reviewed and will later rebase it.

**Steve Howell** · 2017-03-14 14:17 UTC

For the CSS pretty printer, I actually had a different approach in mind.  Unlike our HTML templates, which have lots of anomalies and places where we want to respect the human's original formatting decision, for CSS we can have a pretty canonical representation and say "there's one right way to format this."  Also, the CSS parser is more of a full parser.  So my approach to the CSS pretty printer would be to simply smash all the tokens back together, adjusting whitespace as needed according to the depth of the token.

**Steve Howell** · 2017-03-14 14:21 UTC

If you look at `tools/check-css`, for example, you'll see a call to section_list.text() that re-builds the CSS from raw tokens.  We could modify that to take in an indent count, and then just make the various text() methods be whitespace-aware.

**Aditya Bansal** · 2017-03-14 14:23 UTC

Let me have a look.

**Steve Howell** · 2017-03-14 14:32 UTC

Actually, the approach I am suggesting is a little more than "smashing all tokens together."  It's more like have each token of the CSS recursively represent itself.

**Aditya Bansal** · 2017-03-14 14:39 UTC

From what i am understanding is that you are saying to do something like this:
```
body, html,
    .app-main,
    .header-main {
        min-width: 350px;
    }
```
Becomes this:
```
body,html,.app-main,.header-main{min-width:350px;}
```

**Aditya Bansal** · 2017-03-14 14:40 UTC

and then we start to make a parse over it to reconstruct the css in format we have specified as a standard.

**Steve Howell** · 2017-03-14 14:52 UTC

Not exactly.

**Steve Howell** · 2017-03-14 14:52 UTC

I'm saying that we already do a full parse (see check-css), and then we have each object represent itself properly.

**Steve Howell** · 2017-03-14 14:54 UTC

You can already see this action if you modify the CSS to have, for example, a missing semicolon at the end of a line.  Here is an example of how an object currently represents itself:

~~~ py
353 class CssDeclaration(object):
354     def __init__(self, tokens, pre_fluff, post_fluff, css_property, css_value, semicolon):
355         # type: (List[Token], str, str, str, CssValue, bool) -> None
356         self.tokens = tokens
357         self.pre_fluff = pre_fluff
358         self.post_fluff = post_fluff
359         self.css_property = css_property
360         self.css_value = css_value
361         self.semicolon = semicolon
362 
363     def text(self):
364         # type: () -> str
365         res = ''
366         res += self.pre_fluff
367         res += self.css_property
368         res += ':'
369         res += self.css_value.text()
370         if self.semicolon:
371             res += ';'
372         res += self.post_fluff
373         return res

**Steve Howell** · 2017-03-14 14:55 UTC

Actually, the text() method only adds the semicolon if it was already in the original text, but we could remove the `if` on line 370 to enforce that every declaration ends in a semicolon.

**Aditya Bansal** · 2017-03-14 15:00 UTC

yes i took a look at it. I believe fluff is not much clear to me. Does fluff has spaces which are present around in the css.
pre_fluff -> space before
post_fluff -> space after ?
in this case adjustment to pre-fluff should be done to have proper indents in i guess?

**Steve Howell** · 2017-03-14 15:04 UTC

Yeah, the pre_fluff/post_fluff stuff is the ugly bit here.  We could try to tackle this as follows:
* Clean up the parser so that when we have pre_fluff vs. post_fluff is a little more consistent.
* Make our CSS itself more consistent about whitespace/commenting.
* Have the text methods do a little more logic to clean up the "fluff" parts.

**Aditya Bansal** · 2017-03-14 15:04 UTC

ohk i guess i get what you wanna say.
we want to modify this representation to have field which stands for indent and insert that much indent to css element

**Steve Howell** · 2017-03-14 15:06 UTC

I think we mostly handle indent recursively.  For the parent, have the children format themselves with no indent, and then indent all the children from the parent.  And likewise for the grandparent.

**Steve Howell** · 2017-03-14 15:07 UTC

It's possible that we won't even need to explicitly track "depth."  It will just work out from each parent indenting their children elements by 4 spaces, with perhaps a few minor complications related to comments.

**Steve Howell** · 2017-03-14 15:08 UTC

We basically do a depth-first traversal of all nodes and have each node render itself.

**Steve Howell** · 2017-03-14 15:10 UTC

I'm about to send you a PR for the semicolon fix.  Do you intend to be online for a while?

**Aditya Bansal** · 2017-03-14 15:12 UTC

yeah i am online.

**Steve Howell** · 2017-03-14 15:21 UTC

see #4063

**Aditya Bansal** · 2017-03-14 15:27 UTC

it inserted the `;` after every property value pair.
So we want to have it in such a way that every property value pair is indented automatically like the semi-colon was enforced.

**Aditya Bansal** · 2017-03-14 15:29 UTC

But don't we need to keep track of depth then like if its depth first traversal the last node would be rendered so we will need to know how deep we have gone?

**Aditya Bansal** · 2017-03-14 15:31 UTC

ohk it won't.

**Steve Howell** · 2017-03-14 15:31 UTC

yep :)

**Steve Howell** · 2017-03-14 15:32 UTC

Let me push out one more fix that works at the "leaf" level, and then I'll put it in your good hands. :)

**Steve Howell** · 2017-03-14 15:33 UTC

I suspect there will be some minor challenges with long CSS comments, but you should feel empowered to enforce some style conventions as needed and just clean up the existing CSS.

**Aditya Bansal** · 2017-03-14 15:33 UTC

but don't we need to have a indent dynamic in nature. Like pretty_print had a option of num_spaces being passed?
or we want it to be 4 space indented only? Like no - flexibilty.

**Steve Howell** · 2017-03-14 15:35 UTC

I would argue for not having flexibility here.  Realistically, we're always going to want 4-space indents.  And it wouldn't be hard to patch that in later.

**Steve Howell** · 2017-03-14 15:37 UTC

Ok, I just pushed out a new commit to #4063.

**Steve Howell** · 2017-03-14 15:37 UTC

oops, I need to fix a test, so it will be a while till I merge this

**Aditya Bansal** · 2017-03-14 15:43 UTC

no problem. I will have some dinner till then :)
BTW this space standard for value's is nice.

**Steve Howell** · 2017-03-14 16:02 UTC

Ok, I will merge #4063 once Travis finishes.

**Aditya Bansal** · 2017-03-17 14:29 UTC

I have updated this with new commit's [PR#4062](https://github.com/zulip/zulip/pull/4062).
There is a list of safe css files to merge while avoiding merge conflicts.
Here is the list of safe files.

static/styles/landing-page.css
static/styles/thirdparty-fonts.css
static/styles/pygments.css
static/styles/fonts.css
static/styles/activity.css
static/styles/overlay.css

**Aditya Bansal** · 2017-03-17 14:30 UTC

Other files would be held due to these.

static/styles/reactions.css [PR#3382(+24-0)](https://github.com/zulip/zulip/pull/3382)
static/styles/media.css [PR#2089(+9-0)](https://github.com/zulip/zulip/pull/2089) [PR#3265(+15-10)](https://github.com/zulip/zulip/pull/3265) [PR#3996(+20-7)](https://github.com/zulip/zulip/pull/3996) [PR#2973(+4-4)](https://github.com/zulip/zulip/pull/2973) [PR#4083(+63-23)](https://github.com/zulip/zulip/pull/4083) [PR#3002(+9-0)](https://github.com/zulip/zulip/pull/3002)
static/styles/subscriptions.css [PR#3676(+7-0)](https://github.com/zulip/zulip/pull/3676) [PR#3996(+8-6)](https://github.com/zulip/zulip/pull/3996) [PR#2973(+0-2)](https://github.com/zulip/zulip/pull/2973)
static/styles/compose.css [PR#3118(+16-19)](https://github.com/zulip/zulip/pull/3118) [PR#2721(+2-1)](https://github.com/zulip/zulip/pull/2721) [PR#2973(+2-2)](https://github.com/zulip/zulip/pull/2973)
static/styles/right-sidebar.css [PR#2128(+213-0)](https://github.com/zulip/zulip/pull/2128) [PR#2973(+11-4)](https://github.com/zulip/zulip/pull/2973)
static/styles/stats.css [PR#4107(+21-10)](https://github.com/zulip/zulip/pull/4107)
static/styles/components.css [PR#2973(+16-0)](https://github.com/zulip/zulip/pull/2973)
static/styles/settings.css [PR#4098(+7-1)](https://github.com/zulip/zulip/pull/4098) [PR#2172(+5-0)](https://github.com/zulip/zulip/pull/2172) [PR#3349(+11-2)](https://github.com/zulip/zulip/pull/3349) [PR#2899(+4-0)](https://github.com/zulip/zulip/pull/2899) [PR#2973(+0-1)](https://github.com/zulip/zulip/pull/2973)
static/styles/portico.css [PR#4096(+15-1)](https://github.com/zulip/zulip/pull/4096) [PR#3835(+17-0)](https://github.com/zulip/zulip/pull/3835)
static/styles/left-sidebar.css [PR#2973(+58-43)](https://github.com/zulip/zulip/pull/2973) [PR#3579(+20-0)](https://github.com/zulip/zulip/pull/3579)
static/styles/informational-overlays.css [PR#4023(+1-1)](https://github.com/zulip/zulip/pull/4023)
static/styles/drafts.css [PR#2973(+6-8)](https://github.com/zulip/zulip/pull/2973)
static/styles/zulip.css [PR#3337(+17-0)](https://github.com/zulip/zulip/pull/3337) [PR#2128(+0-215)](https://github.com/zulip/zulip/pull/2128) [PR#3747(+7-0)](https://github.com/zulip/zulip/pull/3747) [PR#3787(+24-0)](https://github.com/zulip/zulip/pull/3787) [PR#2292(+12-4)](https://github.com/zulip/zulip/pull/2292) [PR#3330(+9-0)](https://github.com/zulip/zulip/pull/3330) [PR#2379(+22-0)](https://github.com/zulip/zulip/pull/2379) [PR#1432(+1-1)](https://github.com/zulip/zulip/pull/1432) [PR#2973(+378-263)](https://github.com/zulip/zulip/pull/2973) [PR#4083(+225-156)](https://github.com/zulip/zulip/pull/4083)

**Steve Howell** · 2017-03-17 15:57 UTC

Wow!  I guess our current CSS is kind of a mess in terms of indentation.   A couple suggestions:
* I think we should try to de-duplicate some of the pre-fluff/post-fluff logic in the various text() methods.
* We may want to handle multi-line comments slightly more intelligently, allowing for an extra three spaces of indent after the first line.

~~~ css
/* This is 
   a multiline
   comment. */

**Steve Howell** · 2017-03-17 15:58 UTC

@Brock Whittaker @Tim Abbott Is there any chance we can sweep some of the PRs above to try to get them merged?

**Aditya Bansal** · 2017-03-17 16:05 UTC

yeah i too thought of that. I could try de-duplicate some of the code but actually the code might have some minor changes in places which might make it kind of messy while de-duplicating itself.
Although i am going to try it now.
the multi-line comments can definitely be improved. I will do it.

**Steve Howell** · 2017-03-17 16:31 UTC

Even if you have to extract a few mostly-similar functions to deal with whitespace/comments, and you can't get one nice perfect function that handles all cases, it's probably worth the effort, as you can write tests more directly against the helpers, and we can also group all the whitespace-handling stuff near each other in the file.

**Tim Abbott** · 2017-03-17 17:21 UTC

How big are the reindentation diffs?  It seems possible to me that most of those PRs wouldn't actually merge conflict.

**Tim Abbott** · 2017-03-17 17:24 UTC

Also, several of the conflicts are with parts of PRs that are already merged; I close #2128 for that reason.

**Steve Howell** · 2017-03-17 17:49 UTC

It's possible that we should be aggressive on the re-indentation here.  Unlike with code, merge conflicts in CSS aren't likely to introduce subtle logic errors if somebody messes up the rebase.

**Tim Abbott** · 2017-03-17 17:58 UTC

Yeah I think I'm going to do a bit of testing here, but I think we can just merge most of these since unlike HTML, in most cases these change like 5 lines in the file, not every line :)

**Tim Abbott** · 2017-03-17 18:01 UTC

I just merged the 4 simplest ones.  I agree with Steve's feedback about multiline comments; it looks like we could merge a lot more if that was resolved.

**Tim Abbott** · 2017-03-17 18:01 UTC

My expectation is that with the exception of maybe zulip.css, we can probably just merge all of these ones we're happy with the formatting.

**Aditya Bansal** · 2017-03-17 18:02 UTC

let me work on it. Also i wanted feedback on formatting of `pygments.css`.

**Aditya Bansal** · 2017-03-17 18:03 UTC

actually i put in a kind of rule of have something like this always
selector {
body
}

**Aditya Bansal** · 2017-03-17 18:03 UTC

instead of 
selector { body }

**Aditya Bansal** · 2017-03-17 18:04 UTC

[diff](https://github.com/zulip/zulip/pull/4062/files#diff-035dbf457ff3bc89be2de33fea914285) here is a diff of the file

**Tim Abbott** · 2017-03-17 18:07 UTC

I think just excluding pygments.css is probably reasonable, since I think for its specialized circumstances its formatting is pretty reasonable

**Steve Howell** · 2017-03-17 18:08 UTC

I like the pygments.css re-formatting.  Maybe in a vacuum, I'd leave pygments.css alone, but I think for overall consistency we should avoid its all-on-one-line styling.

**Steve Howell** · 2017-03-17 18:10 UTC

And I don't think the original format is vastly superior to the automatic formatting.  It's true that you need to scroll more now, but it's more readable IMHO.

**Aditya Bansal** · 2017-03-17 18:10 UTC

And actually it would be difficult for leaving out `pygments.css` from indents test without leaving it out from the css test being run until now, since the upgrade to the css parser won't allow it.

**Steve Howell** · 2017-03-17 18:12 UTC

Yep, good point.  @Tim Abbott For context, the way our CSS linter works is that we re-format the entire file, which includes not just indentation but also things like trailing semi-colons, and then complain if re-formatting creates a diff.  So it's hard to do piecemeal linting with our current architecture.

**Tim Abbott** · 2017-03-17 18:17 UTC

OK, makes sense

**Tim Abbott** · 2017-03-17 18:17 UTC

I'm probably fine with reformatting pygments given that.  We've changed it once in 3 years, so not a heavily modified file :)

**Steve Howell** · 2017-03-17 18:30 UTC

So, @Aditya Bansal @Tim Abbott let me just summarize a few decisions here:
* It's ok to re-format pygments.css.
* We should fix the commenting.  (sounds like you're on it)
* We will push everything but zulip.css when you're ready (unless you discover another module has a huge diff).
* We'll rely on people with existing PRs to just rebase as needed (and we don't expect major churn here).

**Tim Abbott** · 2017-03-17 18:31 UTC

yeah and possibly after the commenting changes zulip.css may be pushable; basically anything where we're changing <10 lines is clearly not going to be a big merge conflict problem.

**Steve Howell** · 2017-03-17 18:31 UTC

@Tim Abbott For zulip.css, since there's not tremendous urgency here, it might be nice to try to sweep a few of the PRs that it touches before the final indentation cleanup.  Not just for this, but as PRs get stale, the CSS might become outdated.

**Tim Abbott** · 2017-03-17 18:33 UTC

Yeah, we may do something where we merge chunks or whatever for that.  We can figure it out once the rest are happy

**Tim Abbott** · 2017-03-17 18:33 UTC

Specifically worried about just #2973 and #4083.

**Aditya Bansal** · 2017-03-18 05:13 UTC

I have updated the [PR#4062](https://github.com/zulip/zulip/pull/4062) with new commits.
I have reduced duplication substantially
(Although i thought it would create a mess but to my surprise it was really easy to do.)
The comments are now handled in a better way.
Only one thing that i know of is not being tackled.
If we have something like this: 
```
body { /*  multi-line comment starting here
.... */
body content
}
```

**Aditya Bansal** · 2017-03-18 05:13 UTC

It would be made into 
```
body {    /* multi-line comment starting here
.... */
    body content
}
```

**Aditya Bansal** · 2017-03-18 05:14 UTC

notice the 4 space indent before starting of multi-line comment and  `{`.
This is due to architecture we currently have for our parser.

**Aditya Bansal** · 2017-03-18 05:15 UTC

Although currently there are no such cases in our code.

**Steve Howell** · 2017-03-18 05:26 UTC

I think we can safely ignore that case.  If somebody starts the comment after the opening curly, they'll get a dubious recommendation on how to fix it, but hopefully they'll just work around it by moving the comment to the next line.

**Steve Howell** · 2017-03-18 05:28 UTC

We probably want to exempt thirdparty-fonts.css.

**Steve Howell** · 2017-03-18 05:41 UTC

One more thing is we probably want to keep 100% coverage on the CSS parser, if possible.

**Aditya Bansal** · 2017-03-18 05:48 UTC

Let me try add some tests for the new functions.

**Tim Abbott** · 2017-03-18 15:06 UTC

I merged a few of these; a few things we may not want to reindent:
* thirdparty-fonts.css -- I think that's just a third-party file from Font Awesome and we shouldn't be touching it.  Probably should move it to `static/third` for clarity.
* zulip.css -- this looks a lot better.  But some of the comment changes near the bottom seem off

**Aditya Bansal** · 2017-03-18 15:17 UTC

```
.modal {
    overflow: hidden;
    margin-top: 0;
    top: 5%;
    outline: 0; /* Bootstrap uses tabindex=-1 on modals for focus and ESC handling,
    so avoid the outline it causes */
}
```
Is this you are referring to?

**Tim Abbott** · 2017-03-18 15:21 UTC

yeah

**Tim Abbott** · 2017-03-18 15:21 UTC

Also these guys look weird and we should probably edit manually to remove the leading `*`s 
```
 .loading_indicator_text {
     /* If you change these, make sure to adjust the constants in
-     * loading.make_indicator as well */
+    * loading.make_indicator as well */
```

**Steve Howell** · 2017-03-18 15:25 UTC

Yep, @Aditya Bansal, for some of the  stranger comments, what I would do is this:
* run your tool and find strange comments
* get a clean checkout
* just manually clean up the comment in a small diff
* run your tool again to make sure the tool likes it

**Steve Howell** · 2017-03-18 15:28 UTC

Also, don't be afraid to remove comments that are more confusing than helpful.  I believe most of the comments in the CSS are basically ignored, anyway.

**Aditya Bansal** · 2017-03-18 15:29 UTC

ohk actually i wanted to ask about comments like this
```
outline: 0; /* content here
content here */
```

**Steve Howell** · 2017-03-18 15:30 UTC

For those I'd be inclined to switch to this style:

~~~
/* make it blue */
color: blue;
~~~

**Steve Howell** · 2017-03-18 15:30 UTC

or just make the comments more terse

**Steve Howell** · 2017-03-18 15:32 UTC

or for longer stuff

~~~ css
/* make it show
   blue because of some silly web thing */
color: blue;

**Aditya Bansal** · 2017-03-18 15:33 UTC

ohk so like we can have linter put in a `\n` before every comment starting the same line as of the
`propery: value;`

**Aditya Bansal** · 2017-03-18 15:35 UTC

Such a thing would make 
```
color: blue; /* blue color */
width: 100px;
```
To be like this:
```
color: blue;
/* blue color */
width: 100px;
```

**Tim Abbott** · 2017-03-18 15:35 UTC

Well, but we want the comment before, not after

**Aditya Bansal** · 2017-03-18 15:35 UTC

although this might be vague.

**Tim Abbott** · 2017-03-18 15:35 UTC

So probably we should just fix these by hand; there's only a few of them

**Aditya Bansal** · 2017-03-20 20:08 UTC

Updated the [PR#4062](https://github.com/zulip/zulip/pull/4062) with new commit. 
Now the tooling is little bit modified to put an '\n' at end of comments such as this 
```
color: blue; /* blue 
color */
width: 100px;
```
To make it like this
```
color: blue;
/* blue color */
width: 100px;
```
Now this will force the programmer to put comments in the position we prefer to be a standard.
Manually updated the comment's in `zulip.css` to make them look how we wanted.
Also moved the `thirdparty-fonts.css` to  `third` folder.

**Steve Howell** · 2017-03-20 20:16 UTC

The comment should be above the declaration, though, which I know is more tricky.  This is why I think you should just manually fix these.

**Aditya Bansal** · 2017-03-20 20:17 UTC

actually i manually fixed that.

**Aditya Bansal** · 2017-03-20 20:18 UTC

I meant to say that now tool would put in a new line character and won't let test's pass unless any new comment's are put in the right way.

**Aditya Bansal** · 2017-03-20 20:18 UTC

also it would leave alone comments like this
` width: 100px; /* comment */`. Only put in new line for multi line comments.

**Steve Howell** · 2017-03-20 20:19 UTC

ok

**Aditya Bansal** · 2017-03-20 20:22 UTC

wait, it just clicked me. I guess i might be able to make it come before as well. Let me try it out.

**Aditya Bansal** · 2017-03-20 20:23 UTC

no. It would mess things up.

**Aditya Bansal** · 2017-03-21 20:12 UTC

So currently i added two functions handling post and pre fluff separately. We might be able to handle the case we had been discussing if we add another function which in return calls pre and post fluff handlers and deals with possible interaction between them. Should i proceed with this way or is it good the way it is right now?

**Steve Howell** · 2017-03-21 20:17 UTC

I think our pre-fluff and post-fluff handling can be dumb, and we just need to manually fix some of our existing CSS as a one-time effort.  People rarely add comments to CSS, so I'm not super concerned about us being too particular for future code.  We just want the one-time indentation cleanup to not choke too much on them.

**Aditya Bansal** · 2017-03-21 20:24 UTC

In that case i would like to update you about this [PR#4062](https://github.com/zulip/zulip/pull/4062), in case there is a confusion about its status (I felt there might be one, might be silly of me to feel like that). I have updated this already to have CSS fixed manually for the comment's case.

**Steve Howell** · 2017-03-21 20:29 UTC

That looks good to me!  I'm sorry, I've been kind of busy lately, so I've probably not tracked this conversation as carefully as I would like to.  @Tim Abbott Can you give a :thumbs_up: to merge Aditya's changes in #4062? I feel like there may be some room to simplify the last commit there, but we can do that after cleaning up the CSS.

**Steve Howell** · 2017-03-21 20:29 UTC

(we could merge the last commit too, and just make an issue to try to simplify that code)

**Aditya Bansal** · 2017-03-21 20:41 UTC

yeah i understand. I didn't mean to bombard you with this, i thought you might have thought from the conversation that i am yet to update the PR.
Thanks for reviewing this.

**Tim Abbott** · 2017-03-21 20:42 UTC

Yeah this looks great, merged

**Aditya Bansal** · 2017-03-21 20:46 UTC

Thanks for merging.
I am afraid that i can't think of any direct way yet to simplify that code. Should i open a follow-up issue for this?

**Tim Abbott** · 2017-03-21 20:47 UTC

I think if the issue isn't actionable, we shouldn't bother opening an issue for it

**Steve Howell** · 2017-03-21 21:50 UTC

I think it's actionable, although I don't have time now to explain the simplifications.  In short, now that we have reasonable CSS, we can make the whitespace handling a bit more canonical, so that any strange placement of whitespace causes a diff and causes the linter to fail.

**Aditya Bansal** · 2017-03-22 07:55 UTC

I believe that has been done somewhat. Like for any case like having white space after `{ ` and no text or comment in same line, linter would remove such a white space. Also any white spaces at ends of statements are removed which doesn't feel needed. If we have new lines with no text in them and just for vertical spacing purpose, stray white spaces in such lines is also removed.
If this was not what you were saying i would be happy to catch you online sometime later (when you might have a lighter schedule) to discuss this.

**Aditya Bansal** · 2017-03-26 18:01 UTC

I have been meaning to catch up with you Steve on this one.
(only if you have a lighter schedule now)

**Steve Howell** · 2017-03-26 18:46 UTC

Kinda busy now, but one suggestion that I have is to see if every conditional in your code is captured by test.  If any of them aren't tests, and deal with edge-case-y kind of stuff, maybe see if you can simplify the code without having to fix too much of our existing CSS.

**Aditya Bansal** · 2017-03-26 19:21 UTC

ohk i will try to do that and do another round of analysis on code to see if i could do something to simplify.

**Steve Howell** · 2017-03-26 19:45 UTC

This method also seems like it could be cleaned up somehow:

~~~ css
418     def text(self):
419         # type: () -> str
420         res = ''
421         for i, sel in enumerate(self.selectors):
422             sel_list_render = sel.text()
423             if i != 0 and sel_list_render[0] != '\n':
424                 res += ' '
425             res += sel_list_render
426             if i != len(self.selectors) - 1:
427                 res += ','
428         if res[-1] != ' ' and res[-1] != '\n':
429             res += ' '
430         return res

**Steve Howell** · 2017-03-26 19:47 UTC

The selector list shouldn't need to put out a trailing space, for example; let the node above it handle that.

**Steve Howell** · 2017-03-26 20:03 UTC

I am looking into the above code now.

**Steve Howell** · 2017-03-26 20:32 UTC

ok, see #4326

**Aditya Bansal** · 2017-03-26 20:55 UTC

ohk i had a look and this makes sense. I now understand what you were trying to say was that concept of pre and post fluff for the selectors is useless in general practice since we might not want to have comments among the selector's list in our standard.

**Aditya Bansal** · 2017-03-26 21:07 UTC

Although i am not so sure about the commit ensuring the bracket's position. I believe i must have got the initial purpose of this task wrong. I believed we wanted to pretty print CSS to our standard format. But from the commit it seems like that we actually want to just raise a diff if there is a difference from our standard.

**Aditya Bansal** · 2017-03-26 21:15 UTC

But if we want to treat it as a pretty printer i believe the changes in first commit might not be good since one can get the checker to accept CSS by adding a extra space in front of `{` rather than following our standard.
Like if we think about a new developer who is not acquainted to our standard and reads the diff which was resulting from 
`zulip.css` having this
```
input[type="color"]
{		
      font-size: inherit;
      height: 1.4em;
}
```

**Aditya Bansal** · 2017-03-26 21:16 UTC

diff is here
```
static/styles/zulip.css seems to be broken:
267c267
< {
---
>  {
```
one might be tempted to just add that extra space rather than remove new line and put it after last selector.

**Aditya Bansal** · 2017-03-26 21:17 UTC

Putting that extra space will make the checker pass the CSS.

**Steve Howell** · 2017-03-26 21:26 UTC

I think we want to be strict here.  If anybody looks at our CSS for just a little bit, they'll see we always hang the brace on the end of the line, and we do that in JS as well, I might add.  So somebody may have a one-time head scratcher if they are oblivious to the way the rest of the code is formatted, but I think that's normal.

**Steve Howell** · 2017-03-26 21:28 UTC

And, if you try doing the "wrong" fix on my branch, I think you'll see that the linter still complains.

**Aditya Bansal** · 2017-03-26 21:34 UTC

I guess it doesn't. I tried it out with [1141d17](https://github.com/zulip/zulip/pull/4326/commits/1141d175feded3025cc14d4dfb28f427068adaab). Since the changes weren't much i manually added them on my branch and linter did complain first but when i added an extra space it didn't complained.

**Aditya Bansal** · 2017-03-26 21:43 UTC

Ditching the post -fluff part of the selector list should have made the linter complain on your branch. I didn't tested it out with both the commits.

**Aditya Bansal** · 2017-03-26 21:47 UTC

'made linter not complain' is what i meant to say above.

**Steve Howell** · 2017-03-26 21:49 UTC

It might be the second commit that completely locks this down.

**Aditya Bansal** · 2017-03-26 21:49 UTC

yeah it is

**Aditya Bansal** · 2017-03-26 21:51 UTC

i guess both together does the job flawlessly. Shouldn't be they squashed into one in such a case?

**Steve Howell** · 2017-03-26 22:14 UTC

I think the first commit is still "correct" on its own.  It might not be as locked down as we like, but we had loopholes before that fix.

**Aditya Bansal** · 2017-03-26 22:28 UTC

Loophole being the complexity?

**Steve Howell** · 2017-03-26 22:47 UTC

no, loophole being that we probably still had some ways to get funny looking CSS through the linter

**Aditya Bansal** · 2017-03-27 05:15 UTC

yeah the case of having '{' on next line.

**Aditya Bansal** · 2017-03-27 05:22 UTC

i guess i was too sleepy when i asked that. :sleepy:


## making ssh key persist across logins

*2017-01-03 to 2017-01-03 · 2 messages · [open in Zulip](https://chat.zulip.org/#narrow/channel/18-tools/topic/making.20ssh.20key.20persist.20across.20logins/with/114106)*

**Andrea  Longo** · 2017-01-03 18:28 UTC

I don't know why I seem to be the only person with this problem, or why suddenly I have to add my key with every login and not just after provision, but I found a solution that's working on my Ubuntu box: install keychain
https://www.cyberciti.biz/faq/ubuntu-debian-linux-server-install-keychain-apt-get-command/

**Andrea  Longo** · 2017-01-03 18:29 UTC

Now I should only have to dig up my passphrase only after reboots. It survives provision as well as shell logout.


## shell in vm

*2017-01-04 to 2017-01-05 · 19 messages · [open in Zulip](https://chat.zulip.org/#narrow/channel/18-tools/topic/shell.20in.20vm/with/115663)*

**Vishnu KS** · 2017-01-04 20:52 UTC

Does everyone use the default bash shell when inside vagrant? Or do you install your favorite shell?

**Tim Abbott** · 2017-01-04 20:52 UTC

I use bash in general :)

**Tim Abbott** · 2017-01-04 20:53 UTC

I do think we should think about having a way to add hooks/configure to make provisioning auto-install certain packages inside for folks who want that, so that destroying your Vagrant guest doesn't lose all your favorite customizations

**Vishnu KS** · 2017-01-04 20:55 UTC

Yeah! I keep ending up reinstalling oh-my-zsh every time after I recreate the VM.

**Vishnu KS** · 2017-01-04 20:57 UTC

@Tim Abbott You  tried oh-my-zsh before?

**Tim Abbott** · 2017-01-04 20:58 UTC

I have only used zsh, not oh-my-zsh :)

**Tim Abbott** · 2017-01-04 20:59 UTC

I think we can probably implement this as a config file (or shell script?) that the user can place at some .gitignored path in their Zulip repo

**Vishnu KS** · 2017-01-04 20:59 UTC

Okay. It's nice. You should check it out sometimes. :)

**Tim Abbott** · 2017-01-04 20:59 UTC

And provision.py can just check if that file exists and if so, call it

**Vishnu KS** · 2017-01-04 20:59 UTC

Yeah. That's a good idea.

**Tim Abbott** · 2017-01-04 21:00 UTC

I encourage opening an issue for this idea and then claiming it :)

**Vishnu KS** · 2017-01-04 21:00 UTC

Yeah. Will do now. :)

**Tommy Ip** · 2017-01-04 21:04 UTC

Oh-my-zsh/zsh is awesome  :+1:

**Vishnu KS** · 2017-01-05 12:29 UTC

I think I am going to do this with the help of a shell script. Users can create a file called `custom_provision_script.sh` which would be run after the main provision.

**Vishnu KS** · 2017-01-05 12:31 UTC

Does that sounds good?

**Alicja Raszkowska** · 2017-01-05 13:42 UTC

I'm using a lot of bash aliases extensively and haven't found a good way of using them in vagrant too - can that be a part of a setup, e.g. a user `.bashrc` could be loaded?

**Alicja Raszkowska** · 2017-01-05 13:46 UTC

there can be obviously some problems with aliases between OSX and Linux, I had to adjust my `.bashrc` a bit for Linux, so this could be loaded from a file the user points to

**Tommy Ip** · 2017-01-05 13:48 UTC

Maybe we should provide a few templates so users can just adjust it to their preference?

**Vishnu KS** · 2017-01-05 14:16 UTC

Yeah. We can probably add some basic commands like loading the bashrc file in the script. (They would be commented out by default).


## tools/review

*2017-01-06 to 2017-01-06 · 3 messages · [open in Zulip](https://chat.zulip.org/#narrow/channel/18-tools/topic/tools.2Freview/with/117313)*

**Steve Howell** · 2017-01-06 17:11 UTC

I am starting to think about writing a `tools/review` script in Python that will be a more advanced version of `./tools/fetch-rebase-pull-request`.   Probably the most immediate thing I'll do is just make it so that I can run it fearlessly--if I have any code checked out, or if I'm on a feature branch, it should not do anything except tell me my current status.

And then I'm thinking of future bells and whistles...

**Tim Abbott** · 2017-01-06 17:11 UTC

sounds great to me!

**Steve Howell** · 2017-01-06 17:16 UTC

Some ideas:
* use the Github API to pull down some metadata, like maybe the number of comments and whether Tim has reviewed it yet
* if somebody's EDITOR environment variable is set to "vim," fire up vim with the affected files (and other folks could extend it for their favorite editors)
* send a message to Zulip saying "Steve has locally fetched PR #5555"


## creating a text file with no end of line

*2017-01-14 to 2017-01-14 · 2 messages · [open in Zulip](https://chat.zulip.org/#narrow/channel/18-tools/topic/creating.20a.20text.20file.20with.20no.20end.20of.20line/with/127664)*

**Andrea  Longo** · 2017-01-14 03:18 UTC

I needed a test fixture without a linefeed at the end, so instead of shuffling something over from my laptop with the proper hex editor, I did this in a shell:
```
$ echo -n my_no_a0_data > myfile
$ od -t x1 myfile
0000000 6d 79 5f 6e 6f 5f 61 30 5f 64 61 74 61
0000015
```

**Andrea  Longo** · 2017-01-14 03:19 UTC

I know, I know, it isn't a "text file" if it doesn't have the linefeed. But it worked.


## message received by server

*2017-01-14 to 2017-03-11 · 272 messages · [open in Zulip](https://chat.zulip.org/#narrow/channel/18-tools/topic/message.20received.20by.20server/with/127933)*

**Mahim Goyal** · 2017-01-14 14:20 UTC

I was wondering as to how can I find out if a message has been received by the server or not? Related to issue https://github.com/zulip/zulip/issues/3212

**Steve Howell** · 2017-01-14 14:27 UTC

On the browser side, the server will send you an event when the message got received.  If you look at our local echo code path (see `echo.js` and `message_store.js`) you can probably grok how this works.   Look at `static/js/server_events.js` as well, near line 277.

As Tim says, we probably want to set a 15s timeout and then see if the message in question has not been "reified."

**Mahim Goyal** · 2017-01-14 14:53 UTC

Ok, I will look into it.

**Tim Abbott** · 2017-01-14 20:00 UTC

@Mahim Goyal mechanically, we'd probably have the `reify` function call `clearTimeout()` on the relevant object to cancel it

**Mahim Goyal** · 2017-01-14 21:37 UTC

I went through the files. But I got stuck as to how can I make the server down or something similar while testing some of my code.

**Steve Howell** · 2017-01-14 21:45 UTC

You can trace the code from JS.  See what JS posts to send a message.  Then look that up in `zproject/urls.py`.  Then find the back end view it points to.  Finally insert something like `time.sleep(20)` to make the view sleep for 20 seconds before returning.

**Mahim Goyal** · 2017-01-14 23:12 UTC

Thanks

**Mahim Goyal** · 2017-01-15 16:54 UTC

@Steve Howell I went through the  `compose.js` file and found this `function send_message(request)`. In this function I got to this `echo.try_deliver_locally(request);`,  while tracing through it I finally ended up at `function insert_new_messages(messages)` .  This is where I got confused. As far as I understood here we are only trying to insert the message into the message list. I think the function handling the contact with the server is `function process_from_server(messages)`. Am I in the right direction so far? Please let me know if these are amateur doubts, I will try to work harder before raising any queries in future.

**Steve Howell** · 2017-01-15 17:04 UTC

These are fair questions to ask--it's a tricky code path.

**Steve Howell** · 2017-01-15 17:05 UTC

At some point in the send_message() call, we do actually render the message.  Let me look myself...

**Steve Howell** · 2017-01-15 17:11 UTC

in `message_store.js`, `insert_new_messages` calls  `add_messages`, which calls `msg_list.add_messages`, which takes you to `message_list.js`

Then the `add_messages` function there eventually calls rendering code.

**Steve Howell** · 2017-01-15 17:18 UTC

It is probably important to set a timeout here regardless of whether we render the message as part of local echo, because if I send a message, and it times out, I probably want to know about it.  But then if we had happened to render the message, there will be an additional step of removing it from the view.   You may want to start with the message_list.js code here and build up some building blocks, if they don't already exist.  You may need to build a function that lets you pass in a message id to a message list and ask it to remove the message from the list and re-rerender.  It's probably worth investing the time to just read all 645 lines of that file.  You don't need to understand every detail of how that module works, but you'll want a big picture view of it.

**Mahim Goyal** · 2017-01-15 18:08 UTC

Thank you Steve, that was very helpful.

**Steve Howell** · 2017-01-15 18:10 UTC

no prob :smile_cat:

**Mahim Goyal** · 2017-01-22 03:01 UTC

@Steve Howell  I went through the file but saw that add_messages is locally rendering the message. It is not sending it to the server. I couldn't find any specific criteria which was not changing when the server is not contacted. But while testing in server down conditions, I saw that  the messages are not time punched. We could use that as the identifying character if the message was sent to server or not. Is this right?

**Tim Abbott** · 2017-01-22 03:29 UTC

correct, we intentionally don't mark timestamps on messages until they are acknowledged by the server

**Mahim Goyal** · 2017-01-22 07:44 UTC

@Tim Abbott  @Steve Howell  I have created a wip PR #3419 , it will show an alert if message is not received by server. Let me know if its fine till here.

**Steve Howell** · 2017-01-22 14:00 UTC

@Mahim Goyal The current fix is simple, but not super precise about which message failed.  I think we want a little more sophistication about connecting msg_server_status to a particular message.  For example, with your current implementation, I believe I could send message #1, and message #1 never gets processed, but then send message #2, which does get processed, and I'd never know about an error.

**Mahim Goyal** · 2017-01-24 06:32 UTC

@Steve Howell  It would be great if you could take a look at wip #3419 again.

**Steve Howell** · 2017-01-24 15:34 UTC

Hi @Mahim Goyal, thanks for the follow up.  I think you want msg_server_status[local_id], not msg_server_status.local_id.  They mean different things in JS! :)

**Steve Howell** · 2017-01-24 15:36 UTC

~~~ js
(zulip-venv)vagrant@vagrant-base-trusty-amd64:/srv/zulip$ node
> hsh = {};
{}
> local_id = 5
5
> hsh[local_id] = "five"
'five'
> local_id = 6
6
> hsh[local_id] = 
... "six"
'six'
> hsh.local_id = "foo"
'foo'
> hsh
{ '5': 'five', '6': 'six', local_id: 'foo' }

**Mahim Goyal** · 2017-01-24 16:10 UTC

Oh I intended to make a dictionary, stackoverflow gave me that. I will update then and revert back.

**Steve Howell** · 2017-01-24 16:13 UTC

Sounds good!

**Steve Howell** · 2017-01-24 16:39 UTC

Hi @Mahim Goyal, another thing we'll want to do with this change is add some node tests for it.  I'm asking @Tommy Ip to help you here, and I'll also be online for most of the next hour or so.

**Steve Howell** · 2017-01-24 16:40 UTC

@Mahim Goyal, can you take a moment to explain the context of this change to Tommy?

**Mahim Goyal** · 2017-01-24 16:40 UTC

Yes sure.

**Mahim Goyal** · 2017-01-24 16:44 UTC

So here we are trying to notify the user if the message sent was captured by the server or not. We wait for 15s before checking this.  Then send the notification. I have completed this part. Next we want is to remove the message from the message list. I am currently working on this.

**Tommy Ip** · 2017-01-24 16:45 UTC

Ok, is the PR #3419?

**Mahim Goyal** · 2017-01-24 16:45 UTC

Yes

**Tommy Ip** · 2017-01-24 16:46 UTC

When you say `remove the message from the message list`, do you mean delete a message if it was not received by the server?

**Mahim Goyal** · 2017-01-24 16:47 UTC

Yes.

**Mahim Goyal** · 2017-01-24 16:47 UTC

I think it is better to do it this way now.

**Mahim Goyal** · 2017-01-24 16:48 UTC

Maybe later on we can save the message and ask the user to retry sending the message.

**Tommy Ip** · 2017-01-24 16:48 UTC

Alright. So I guess Steve wants you to write a unittest for the current code before moving on ?

**Mahim Goyal** · 2017-01-24 16:50 UTC

Yes thats right

**Tommy Ip** · 2017-01-24 16:51 UTC

Right, lets start! Firstly, do you have much experience with unit testing in general? Don't worry if not, we can go through it step by step.

**Mahim Goyal** · 2017-01-24 16:51 UTC

This is new to me.

**Tommy Ip** · 2017-01-24 16:54 UTC

Ok, so there are two type of tests in Zulip (and in most projects), Unit-test and integration test. Unit-test tests a unit of code (a function most of the time) by giving it a input and check if the output is correct. Integration test tests multiple layers of the software, but don't worry about that for now.

**Mahim Goyal** · 2017-01-24 16:56 UTC

Fine

**Tommy Ip** · 2017-01-24 16:57 UTC

Before we write any tests, lets try to run the tests to see what it is like. Do you have a development environment? Like a vagrant instance?

**Mahim Goyal** · 2017-01-24 16:58 UTC

Yes I have my development environment

**Tommy Ip** · 2017-01-24 16:59 UTC

ok, you can invoke the `node` unit test by entering this command in the root directory: `$ ./tools/test-js-with-node`

**Mahim Goyal** · 2017-01-24 17:00 UTC

Ok, let me try.

**Mahim Goyal** · 2017-01-24 17:02 UTC

Yes, the tests are running.

**Tommy Ip** · 2017-01-24 17:02 UTC

The tests should pass, and in that case lets start writing some unit test if you don't have any question about that.

**Mahim Goyal** · 2017-01-24 17:03 UTC

Yes, the tests have passed.

**Mahim Goyal** · 2017-01-24 17:03 UTC

Yes we can go on

**Tommy Ip** · 2017-01-24 17:04 UTC

Let me have a quick look at the code

**Mahim Goyal** · 2017-01-24 17:04 UTC

Sure

**Tommy Ip** · 2017-01-24 17:08 UTC

Hmm I am a bit confused as to what line 595 - 601 do

**Mahim Goyal** · 2017-01-24 17:11 UTC

`msg_server_status`stores whether a message was 'received' by the server or it 'failed'. We give a 10s timeout(for testing purpose, later on it has to be made to 15s) before checking the message status.

**Tommy Ip** · 2017-01-24 17:11 UTC

Is `alert(request.content);` just temporary?

**Mahim Goyal** · 2017-01-24 17:11 UTC

For notification I have used `alert`

**Mahim Goyal** · 2017-01-24 17:11 UTC

Yes, Thats right

**Mahim Goyal** · 2017-01-24 17:12 UTC

That basically just displays the content of message, so we know which message was undelivered.

**Mahim Goyal** · 2017-01-24 17:14 UTC

And then to save memory the item in `msg_server_status`is deleted

**Tommy Ip** · 2017-01-24 17:15 UTC

Alright. The unit test in Zulip just uses barebone Javascript assert statements, so there isn't any fancy framework. A unit test example:
```.js
// My function
function add_two_numbers(a, b) {
    return a + b;
}

// Unit test
function test_add_two_numbers() {
    assertEqual(add_two_numbers(1, 1), 2);
}
```
That's it!

**Mahim Goyal** · 2017-01-24 17:16 UTC

Ok, so we pre-define some test cases for which it has to pass.

**Tommy Ip** · 2017-01-24 17:16 UTC

Yes that's right!

**Tommy Ip** · 2017-01-24 17:16 UTC

assertEqual just check if the first argument is the same as the second, if not, the test fails

**Mahim Goyal** · 2017-01-24 17:17 UTC

Ok

**Mahim Goyal** · 2017-01-24 17:18 UTC

How can we test if a message was undelivered in our case.

**Mahim Goyal** · 2017-01-24 17:19 UTC

Like in what way can we simulate server unreachable king of a situation.

**Tommy Ip** · 2017-01-24 17:21 UTC

The general solution is to simply set `msg_server_status.local_id` to False, and then check if the notice popup. And then set it to True, and then see if the notice still popup

**Mahim Goyal** · 2017-01-24 17:23 UTC

I get it, but won't that provide only the test scenario of server online conditions?

**Tommy Ip** · 2017-01-24 17:26 UTC

Oh sorry, what does `msg_server_status[local_id]` represent?

**Mahim Goyal** · 2017-01-24 17:29 UTC

It represents the state of message with given  ` local_id `. It is initially set to `failed`and then when the server is finally contacted it is set to `received`. So if after the given time if it still is `failed`, it means that the message was not sent to server.

**Tommy Ip** · 2017-01-24 17:32 UTC

Yeah I think we should be fine just setting msg_server_status[local_id] to false in this case

**Tommy Ip** · 2017-01-24 17:33 UTC

@Steve Howell Since the time out is 10s/15s, wouldn't that slow down the node tests?

**Steve Howell** · 2017-01-24 17:34 UTC

We need to stub setTimeout.

**Tommy Ip** · 2017-01-24 17:34 UTC

oh ok

**Steve Howell** · 2017-01-24 17:34 UTC

That's the tricky piece here. :)

**Mahim Goyal** · 2017-01-24 17:35 UTC

Ok, I think I will start writing the function.

**Tommy Ip** · 2017-01-24 17:36 UTC

Yeah, I think you should put the test in maybe node_tests/sever_events.js?

**Tommy Ip** · 2017-01-24 17:36 UTC

Not sure about that though

**Steve Howell** · 2017-01-24 17:37 UTC

We should create a new file for testing `compose.js`.

**Mahim Goyal** · 2017-01-24 17:37 UTC

Ok I will get started on that.

**Tommy Ip** · 2017-01-24 17:38 UTC

Right, Mahim, you can have a look at the other tests to see how to import and set the necessary files/settings

**Mahim Goyal** · 2017-01-24 17:39 UTC

Ok

**Mahim Goyal** · 2017-01-24 18:29 UTC

Is this a possible syntax to check a variables value in a function `assert.equal(compose.msg_server_status[local_id], "failed");`

**Mahim Goyal** · 2017-01-24 18:31 UTC

given its a global var

**Sampriti Panda** · 2017-01-24 18:33 UTC

Yes.

**Mahim Goyal** · 2017-01-24 18:40 UTC

thanks

**Mahim Goyal** · 2017-01-24 18:50 UTC

Please take a look at this @Steve Howell 
```
var compose = require("js/compose.js");

(function test_msg_server() {
	// Increased timeout to 15s so as to not run before 
	// the actual timeout processes.
	setTimeout(function() {
        assert.equal(compose.msg_server_status[local_id], "failed");
	},15000);
}());
```

**Steve Howell** · 2017-01-24 18:53 UTC

You'll need to actually create a stubbed out version of setTimeout rather than using the real function.

**Steve Howell** · 2017-01-24 18:54 UTC

You can so something like `global.patch_builtin('setTimeout', function (f, interval) {f();})`.

**Mahim Goyal** · 2017-01-24 18:56 UTC

Ok, on it.

**Steve Howell** · 2017-01-24 19:04 UTC

You'll probably a little more sophisticated, like this:

~~~ js
var callback;

global.patch_builtin('setTimeout', function (f, interval) {
    assert.equal(interval, 15000);
    callback = f;
});

do_some_stuff();
// make some assertions

// simulate the timeout expiring
callback();

// do more stuff

**Sampriti Panda** · 2017-01-24 19:05 UTC

You used the wrong comment syntax :P

**Steve Howell** · 2017-01-24 19:05 UTC

And then in another test simulate a different timing sequence, where you call `callback()` **before** you simulate message arrival.

**Steve Howell** · 2017-01-24 19:05 UTC

thanks, @Sampriti Panda (fixed!)

**Mahim Goyal** · 2017-01-25 13:58 UTC

@Steve Howell I am a bit new to writing tests, can I complete the issue first and then take this up.

**Steve Howell** · 2017-01-25 14:02 UTC

For this kind of timing-related stuff, I think it's important to have automated tests that verify at least some of your code's expected behavior.  If you are having a hard time understanding how to write the tests, that's normal, but we might be able to answer questions and clarify things for you.  What is your current status with the tests you've written so far?

**Mahim Goyal** · 2017-01-25 14:04 UTC

I am facing problems with stubbing the setTimeout function, I cant actually understand its working. As for the test cases, I believe there is only one thing we can check i.e if the error message doesnt pop up when the server is online.

**Mahim Goyal** · 2017-01-25 14:05 UTC

I think I will try putting some more effort in tests and will try getting them up before proceeding further on issue.

**Tommy Ip** · 2017-01-25 14:05 UTC

Stubbing basically replace a function by another one, can you show us what you have got right now?

**Mahim Goyal** · 2017-01-25 14:09 UTC

So this is some raw code I wrote, nothing much. I am not getting what we have to do after this.

```
var compose = require("js/compose.js");

(function test_msg_server() {
	// Increased timeout to 15s so as to not run before 
	// the actual timeout processes.
	var callback;

    global.patch_builtin('setTimeout', function (f, interval) {
        assert.equal(interval, 15000);
        callback = f;
    });
    function assertions() {
    	assert.equal(compose.msg_server_status[local_id], "failed");
    }
}());
```

**Mahim Goyal** · 2017-01-25 14:09 UTC

Basically, just merged the stubbing suggested by Steve into my old code.

**Steve Howell** · 2017-01-25 14:15 UTC

That's headed in the right direction.  You just need to call the actual function now and see what happens.

**Steve Howell** · 2017-01-25 14:16 UTC

You want to think about unit tests as sort of similar to a mathematical proof.  ("If I call my function given that setTimeout behaves like X, then I expect my function to produce Y as a result and have Z as a side effect.")

**Mahim Goyal** · 2017-01-25 14:18 UTC

I get it. And by the function you mean `send_message(request)`right?

**Steve Howell** · 2017-01-25 14:18 UTC

I believe so.

**Mahim Goyal** · 2017-01-25 14:19 UTC

Ok, I think I am getting some direction now.

**Steve Howell** · 2017-01-25 14:19 UTC

And you can build up what's called a "dummy" request that has just enough data to help your tests execute the code you're interested in.  Great!

**Mahim Goyal** · 2017-01-25 14:20 UTC

Yes.

**Mahim Goyal** · 2017-01-25 14:21 UTC

Just to be absolutely clear what will be the side effect in our case

**Steve Howell** · 2017-01-25 14:36 UTC

I guess the alert would be the side effect.

**Mahim Goyal** · 2017-01-25 14:42 UTC

Ohh, I was thinking on the lines of failed or received.

**Steve Howell** · 2017-01-25 14:47 UTC

You probably want to verify those as well.

**Mahim Goyal** · 2017-01-25 15:07 UTC

Ok

**Mahim Goyal** · 2017-01-25 15:48 UTC

```
var compose = require("js/compose.js");

(function test_msg_server() {
	// Increased timeout to 15s so as to not run before 
	// the actual timeout processes.
	var callback;

    global.patch_builtin('setTimeout', function (f, interval) {
        assert.equal(interval, 15000);
        callback = f;
    });
    function assertions_to_test() {
    	var request = {client: "website",
    	               type: "stream",
    	               subject: "test",
    	               stream: "all",
    	               private_message_recipient: "AARON@zulip.com",
    	               content: "Zulip is awesome",
    	               sender_id: 1,
    	               queue_id: "1485357784:0"};
    	               
    	compose.send_message(request);
    	callback();
    	id = compose.local_id;
    	assert.equal(compose.msg_server_status[id], "failed");
    }
    assertions_to_test();
}());
```

**Mahim Goyal** · 2017-01-25 15:49 UTC

Is this fine?

**Steve Howell** · 2017-01-25 15:54 UTC

looks good...you'll want to be sure to actually run `assertions_to_test()` though. :)

**Mahim Goyal** · 2017-01-25 16:14 UTC

Yes I added that at the end. (edited it in the above code too)

**Mahim Goyal** · 2017-01-25 16:14 UTC

But I am getting an error.

**Mahim Goyal** · 2017-01-25 16:14 UTC

```
running tests for compose
/srv/zulip/static/js/compose.js:22
var uploads_domain = document.location.protocol + '//' + document.location.host;
                                                       ^

ReferenceError: document is not defined
    at /srv/zulip/static/js/compose.js:22:56
    at Object.<anonymous> (/srv/zulip/static/js/compose.js:1227:2)
    at Module._compile (module.js:556:32)
    at Object.Module._extensions..js (module.js:565:10)
    at Module.load (module.js:473:32)

```

**Sampriti Panda** · 2017-01-25 16:35 UTC

Oh I guess you need to stub that too.

**Steve Howell** · 2017-01-25 17:07 UTC

Yeah, `compose.js` has a lot of setup stuff.  You can do something like...

**Steve Howell** · 2017-01-25 17:08 UTC

~~~ js
set_global('document', {location: {protocol: "", host: ""}});

**Mahim Goyal** · 2017-01-25 17:40 UTC

Till now I have set more than 5 set_globals still more keep coming, will this happen because we are setting up the compose.js test file for the first time?

**Steve Howell** · 2017-01-25 18:00 UTC

Yeah...the first time setup is kind of tough--I should have warned you about that.   Unfortunately, `compose.js` is one of our older modules; in other modules, we have been a bit more disciplined about localizing setup to an init function.

**Mahim Goyal** · 2017-01-25 18:06 UTC

No problem, I am adding some export for functions too in compose.

**Steve Howell** · 2017-01-25 18:08 UTC

Ok, sounds good.  We should be mindful of creating separate commits where we can for things, but I wouldn't let that slow you down too much, as you are probably already dealing with enough complexity for now.

**Mahim Goyal** · 2017-01-25 18:15 UTC

I will try to add files in different commits as far as possible.

**Steve Howell** · 2017-01-25 18:34 UTC

ok

**Mahim Goyal** · 2017-01-25 18:47 UTC

I am facing problem with alert feature,
```
/srv/zulip/static/js/compose.js:599
            alert(request.content);
            ^

ReferenceError: alert is not defined
    at /srv/zulip/static/js/compose.js:599:13
    at assertions_to_test (/srv/zulip/frontend_tests/node_tests/compose.js:44:6)
    at test_msg_server (/srv/zulip/frontend_tests/node_tests/compose.js:48:5)
    at Object.<anonymous> (/srv/zulip/frontend_tests/node_tests/compose.js:49:2)
    at Module._compile (module.js:556:32)
    at Object.Module._extensions..js (module.js:565:10)
```

**Mahim Goyal** · 2017-01-25 18:48 UTC

I am thinking of removing the alert function and using the zulip's own notification popup!

**Mahim Goyal** · 2017-01-25 18:49 UTC

Like the one we get for huge amount of unread messages after staying offline.

**Steve Howell** · 2017-01-25 18:52 UTC

Yeah, we'll definitely want something more customized than alert().

**Steve Howell** · 2017-01-25 18:53 UTC

I would have something like `compose.report_content_not_sent()` that just calls `alert()` for now, and then we can refine that.  And then your unit tests can just stub that function to verify it's called without getting into the details of what it does.

**Mahim Goyal** · 2017-01-25 18:54 UTC

Ok

**Mahim Goyal** · 2017-01-25 19:36 UTC

I believe there is a syntax error, please help
```
/srv/zulip/frontend_tests/node_tests/compose.js:52
        assert.equal(compose.msg_server_status[id], "failed");
                                              ^

TypeError: Cannot read property 'undefined' of undefined
```

**Mahim Goyal** · 2017-01-25 19:36 UTC

(deleted)

**Steve Howell** · 2017-01-25 19:52 UTC

That is more of a runtime error.  It means that `compose.msg_server_status`is not an object-like thing.

**Steve Howell** · 2017-01-25 19:53 UTC

which could be a symptom of not properly initializing `compose.msg_server_status`

**Mahim Goyal** · 2017-01-25 20:13 UTC

What kind of initializing is required. In static compose.js msg_server_status is a global dictionary. I have used this on basis of that. Someone had earlier mentioned that this was the syntax for it.

**Steve Howell** · 2017-01-25 20:43 UTC

I'd need to see the code to see exactly what's going wrong.

**Mahim Goyal** · 2017-01-26 10:21 UTC

I found out the error in the previous message. I have a new error, which I couldn't figure out 
```
/srv/zulip/static/js/compose.js:448
if (page_params.use_websockets) {
    ^

ReferenceError: page_params is not defined
```

**Mahim Goyal** · 2017-01-26 10:23 UTC

I have defined page_params as 
```
set_global('page_params', {
    use_websockets: function() {},
    email: 'AARON@zulip.com',
});
```

**Mahim Goyal** · 2017-01-26 10:24 UTC

Where am I going wrong?

**Tommy Ip** · 2017-01-26 10:24 UTC

You might need to import compose.js after defining page_params

**Mahim Goyal** · 2017-01-26 10:28 UTC

```
var compose = require("js/compose.js");
```

**Mahim Goyal** · 2017-01-26 10:28 UTC

I have written this, but it is before defining paga_params

**Tommy Ip** · 2017-01-26 10:29 UTC

Yeah try putting it after page_params

**Mahim Goyal** · 2017-01-26 10:29 UTC

Yes it worked

**Tommy Ip** · 2017-01-26 10:33 UTC

Nice, if you want to know why that is the case, you can have a look at `compose.js`. In line 448, the conditional is located inside a [Immediately invoked function expression (IIFE)](https://en.wikipedia.org/wiki/Immediately-invoked_function_expression), which executes upon module import. So it is requiring `page_params` before it is available.

**Mahim Goyal** · 2017-01-26 10:37 UTC

Ok got it. Thanks!

**Mahim Goyal** · 2017-01-26 10:41 UTC

Can you help me in defining Socket?

**Mahim Goyal** · 2017-01-26 10:42 UTC

```
/srv/zulip/static/js/compose.js:449
    socket = new Socket("/sockjs");
```
Getting ReferenceError

**Steve Howell** · 2017-01-26 11:00 UTC

Does `set_global("Socket", function () {})` work?

**Mahim Goyal** · 2017-01-26 11:06 UTC

Yes it did.

**Mahim Goyal** · 2017-01-26 11:45 UTC

Need to make a clarification, shouldn't we make socket as a dependency rather than stubbing it out, because we will need it to send the message to server.

**Steve Howell** · 2017-01-26 12:07 UTC

We need to stub out a good chunk of the send-message-to-server code path, since you won't actually have a server to connect to.

**Steve Howell** · 2017-01-26 12:09 UTC

You will probably want to stub `transmit_message()` in particular.

**Steve Howell** · 2017-01-26 12:12 UTC

Something like:

~~~ js
var transmit_success_callback;
global.compose.transmit_message = function (request, success, error) {
     transmit_success_callback = success;
};
// do stuff in between
var success_data = {....} // simulated data
transmit_success_callback(success_data);

**Mahim Goyal** · 2017-01-26 12:24 UTC

Ok

**Mahim Goyal** · 2017-01-26 13:03 UTC

I am sorry to keep bugging you all but I am getting many different type of errors, so I will need some syntax for it.

**Mahim Goyal** · 2017-01-26 13:04 UTC

```
/srv/zulip/static/js/compose.js:455
    socket.send(request, success, function (type, resp) {
           ^

TypeError: socket.send is not a function
```

**Mahim Goyal** · 2017-01-26 13:04 UTC

Help with this please

**Steve Howell** · 2017-01-26 13:15 UTC

You should be able to avoid calling that by stubbing out one of its callers.  But the way you make foo.bar(....) do nothing is to say `set_global("foo", {bar: function () {}})`.

**Mahim Goyal** · 2017-01-26 13:41 UTC

I did that and it gave me the error send is not a function.

**Mahim Goyal** · 2017-01-26 13:42 UTC

```
/srv/zulip/static/js/compose.js:455
    socket.send(request, success, function (type, resp) {
           ^

TypeError: socket.send is not a function
```

**Mahim Goyal** · 2017-01-26 13:44 UTC

Code is this 
```
set_global("socket", {
	send: function() {}
});

**Steve Howell** · 2017-01-26 14:23 UTC

Are you doing `set_global` early enough in the script?

**Sampriti Panda** · 2017-01-26 14:24 UTC

If you are not testing the message sending functionality, then why not stub the whole thing.

**Sampriti Panda** · 2017-01-26 14:25 UTC

I have a feeling you are trying to stub the individual parts of the message sending functionality which is making it a bit difficult.

**Sampriti Panda** · 2017-01-26 14:25 UTC

Like I think there is probably a wrapper around the "socket.send" method which you could stub?

**Sampriti Panda** · 2017-01-26 14:26 UTC

I haven't read the code, so I might be completely wrong :P

**Steve Howell** · 2017-01-26 14:26 UTC

@Mahim Goyal Please re-read my suggestion above about stubbing `transmit_message()`.

**Mahim Goyal** · 2017-01-26 15:14 UTC

Yes I saw that Steve, I thought of using it when I would encounter transmit_message() error in the unit-test script. Would you like to see what I have written till now?

**Steve Howell** · 2017-01-26 15:26 UTC

Sure, I'll look at what you have now.  A general tip when you're doing this is when you get a traceback for a missing method, look to see if it makes more sense to stub out one of the callers vs. the low level method.

**Mahim Goyal** · 2017-01-26 15:34 UTC

Should I paste the whole code here?

**Steve Howell** · 2017-01-26 15:37 UTC

That's fine.

**Mahim Goyal** · 2017-01-26 15:37 UTC

```
var assert = require('assert');
set_global('document', {location: {protocol: "", host: ""}});

global.stub_out_jquery();

set_global("socket", {
	send: function() {}
});

set_global('blueslip', {});
set_global('channel', {
	post: function (options) {},
});

set_global('compose', {
    msg_server_status: {
    	'100.00': "failed",
    	'150.01': "failed",
}});
set_global('server_events', {
	assert_get_events_running: function() {},
});

set_global('page_params', {
    use_websockets: function() {},
    email: 'AARON@zulip.com',
});



set_global("Socket", function () {});

var compose = require("js/compose.js");

set_global('feature_flags', {
    alert_words: true,
});

(function test_msg_server() {
	// Increased timeout to 15s so as to not run before 
	// the actual timeout processes.
	var callback;

    global.patch_builtin('setTimeout', function (f, interval) {
        assert.equal(interval, 15000);
        callback = f;
    });
    var id;
    global.patch_builtin('send_message', function (request) {
        id = request.local_id;
    });

    global.patch_builtin('alert', function (content) {});
    
    

    function assertions_to_test() {
    	var request = {client: "website",
    	               type: "stream",
    	               subject: "test",
    	               stream: "all",
    	               private_message_recipient: "AARON@zulip.com",
    	               content: "Zulip is awesome",
    	               sender_id: 1,
    	               queue_id: "1485357784:0"};

    	compose._send_message(request);
    	callback();
    	id = 100.00;
    	assert.equal(compose.msg_server_status[id], "failed");
    }
    assertions_to_test();
}());
```

**Steve Howell** · 2017-01-26 15:39 UTC

That looks to be on the right track. You might want to rename the `callback` variable to something like `timeout_callback`.

**Steve Howell** · 2017-01-26 15:41 UTC

And then I would try stubbing out `transmit_message`and seeing if that allow to remove some of the other stubs.

**Mahim Goyal** · 2017-01-26 15:41 UTC

Ok on it.

**Mahim Goyal** · 2017-01-26 16:42 UTC

I stubbed out the transmit_message
```
var assert = require('assert');
set_global('document', {location: {protocol: "", host: ""}});

global.stub_out_jquery();

set_global("socket", {
	send: function() {}
});

set_global('blueslip', {});
set_global('channel', {
	post: function (options) {},
});

set_global('compose', {
    msg_server_status: {
    	'100.00': "failed",
    	'150.01': "failed",
}});
set_global('server_events', {
	assert_get_events_running: function() {},
});

set_global('page_params', {
    use_websockets: function() {},
    email: 'AARON@zulip.com',
});



set_global("Socket", function () {});

var compose = require("js/compose.js");

set_global('feature_flags', {
    alert_words: true,
});

(function test_msg_server() {
	// Increased timeout to 15s so as to not run before 
	// the actual timeout processes.
	var timeout_callback;

    global.patch_builtin('setTimeout', function (f, interval) {
        assert.equal(interval, 15000);
        timeout_callback = f;
    });
    var id;
    global.patch_builtin('send_message', function (request) {
        id = request.local_id;
    });

    global.patch_builtin('alert', function (content) {});
    
    var transmit_success_callback;
	global.compose.transmit_message = function (request, success, error) {
		 id = request.local_id;
	     transmit_success_callback = success;
	};

	transmit_success_callback({id: 400,msg: "", result: "success"});
    

    function assertions_to_test() {
    	var request = {client: "website",
    	               type: "stream",
    	               subject: "test",
    	               stream: "all",
    	               private_message_recipient: "AARON@zulip.com",
    	               content: "Zulip is awesome",
    	               sender_id: 1,
    	               queue_id: "1485357784:0"};

    	compose._send_message(request);
    	timeout_callback();
    	id = 100.00;
    	assert.equal(compose.msg_server_status[id], "failed");
    }
    assertions_to_test();
}());
```

**Mahim Goyal** · 2017-01-26 16:42 UTC

Is this fine

**Steve Howell** · 2017-01-26 16:55 UTC

Still seems like you are  making progress, but doesn't that allow you to remove the one `socket` stub now?

**Mahim Goyal** · 2017-01-26 17:13 UTC

Yes its working without that.

**Mahim Goyal** · 2017-01-26 17:16 UTC

I am getting this 
```
/srv/zulip/frontend_tests/node_tests/compose.js:61
        transmit_success_callback({id: 400,msg: "", result: "success"});
        ^

TypeError: transmit_success_callback is not a function
    at test_msg_server (/srv/zulip/frontend_tests/node_tests/compose.js:61:2)

**Steve Howell** · 2017-01-26 17:23 UTC

So I would try to step back and read your code a bit.  We now have a stub for `transmit_message` that, instead of actually transmitting a message, records the callback for us to use later in the test.  When would that stub get invoked?

**Mahim Goyal** · 2017-01-26 18:04 UTC

It would get invoked in the send_message() function.

**Steve Howell** · 2017-01-26 18:07 UTC

Ok, now look where are you calling `transmit_success_callback()`. :)

**Mahim Goyal** · 2017-01-26 18:13 UTC

Ok I got it. I think now I am starting to get a hang of it.

**Mahim Goyal** · 2017-01-26 18:13 UTC

Unfortunately the socket.send error has come up again, following is the latest code.

**Mahim Goyal** · 2017-01-26 18:14 UTC

```
var assert = require('assert');
set_global('document', {location: {protocol: "", host: ""}});

global.stub_out_jquery();

set_global("socket", {
    send: function() {}
});

set_global('blueslip', {});
set_global('channel', {
	post: function (options) {},
});

set_global('compose', {
    msg_server_status: {
    	'100.00': "failed",
    	'150.01': "failed",
}});
set_global('server_events', {
	assert_get_events_running: function() {},
});

set_global('page_params', {
    use_websockets: function() {},
    email: 'AARON@zulip.com',
});



set_global("Socket", function () {});

var compose = require("js/compose.js");

set_global('feature_flags', {
    alert_words: true,
});

(function test_msg_server() {
	// Increased timeout to 15s so as to not run before 
	// the actual timeout processes.
	var timeout_callback;

    global.patch_builtin('setTimeout', function (f, interval) {
        assert.equal(interval, 15000);
        timeout_callback = f;
    });
    var id;
    global.patch_builtin('send_message', function (request) {
        id = request.local_id;
    });

    global.patch_builtin('alert', function (content) {});
    
    var transmit_success_callback;
		global.compose.transmit_message = function (request, success, error) {
			 id = request.local_id;
		     transmit_success_callback = success;
		};
    
    function assertions_to_test() {
    	var request = {client: "website",
    	               type: "stream",
    	               subject: "test",
    	               stream: "all",
    	               private_message_recipient: "AARON@zulip.com",
    	               content: "Zulip is awesome",
    	               sender_id: 1,
    	               queue_id: "1485357784:0"};
        

		
    	compose._send_message(request);
    	transmit_success_callback({id: 400,msg: "", result: "success"});
    

    	timeout_callback();
    	id = 100.00;
    	assert.equal(compose.msg_server_status[id], "failed");
    }
    assertions_to_test();
}());

**Steve Howell** · 2017-01-26 18:33 UTC

I'll let you track that down.  I think now that this is starting to click for you, you'll find it a bit easier to do some deep debugging.  But I imagine you're kind of mentally exhausted, as callback logic and stubs can be tricky!  (Not to mention that compose.js has a lot of stuff going on.)

**Steve Howell** · 2017-01-26 18:34 UTC

For the `socket` thing, you should be able to read the traceback.  I think there is some quirk when node doesn't give tracebacks--I hope you're not running into that.

**Mahim Goyal** · 2017-01-26 18:56 UTC

Ok, I will continue it tomorrow.

**Steve Howell** · 2017-01-26 18:57 UTC

Sounds good.  You're making great progress!

**Vaibhav Singhal** · 2017-01-27 07:25 UTC

@Tim Abbott @Steve Howell @Mahim Goyal in case a person has a slow internet connection, there maybe many messages undelivered to server, which can result in many alerts (basically complaints by browser). This can be a bit frustrating.  
Maybe we can instead display the delivery information alongside the message, through a caution symbol image or something, and later when the browser receives a message delivery server event, that symbol can be changed to a message delivery symbol. What do you think ?

**Tommy Ip** · 2017-01-27 10:37 UTC

Yeah iMessage does that, it also has a option to manually resend the message.

**Tommy Ip** · 2017-01-27 10:40 UTC

https://images.iskysoft.com/mac-iphone-data-recovery/iphone-text-messages-not-working-01.png

**Vaibhav Singhal** · 2017-01-27 10:51 UTC

Yeah, had something like this in mind :)

**Mahim Goyal** · 2017-01-27 12:13 UTC

There wont be any alert kind of a thing, its not decided but we may show the error beside the message only in red font, we can also put a option for retrying to send the message later on( as suggested above too). There is a 15s timeout which seems sufficient to me.

**Sampriti Panda** · 2017-01-27 13:09 UTC

I thought we had this feature already.

**Mahim Goyal** · 2017-01-28 15:45 UTC

I tried exporting the send function in socket.js and tried stubbing the function calling socket.send() in compose.js but still I am getting this error. 
``` 
/srv/zulip/static/js/compose.js:455
    socket.send(request, success, function (type, resp) {
           ^

TypeError: socket.send is not a function

**Steve Howell** · 2017-01-28 15:48 UTC

Do you get a full traceback here?

**Mahim Goyal** · 2017-01-28 15:49 UTC

Do you mean this?
``` 
/srv/zulip/static/js/compose.js:455
    socket.send(request, success, function (type, resp) {
           ^

TypeError: socket.send is not a function
    at send_message_socket (/srv/zulip/static/js/compose.js:455:12)
    at Object.exports.transmit_message (/srv/zulip/static/js/compose.js:566:9)
    at Object.send_message [as _send_message] (/srv/zulip/static/js/compose.js:627:13)
    at assertions_to_test (/srv/zulip/frontend_tests/node_tests/compose.js:68:17)
    at test_msg_server (/srv/zulip/frontend_tests/node_tests/compose.js:76:5)
    at Object.<anonymous> (/srv/zulip/frontend_tests/node_tests/compose.js:77:2)
    at Module._compile (module.js:556:32)
    at Object.Module._extensions..js (module.js:565:10)
    at Module.load (module.js:473:32)
    at tryModuleLoad (module.js:432:12)
    at Function.Module._load (module.js:424:3)
    at Module.require (module.js:483:17)
    at require (internal/module.js:20:19)
    at /srv/zulip/frontend_tests/zjsunit/index.js:47:5
    at Array.forEach (native)
    at Object.<anonymous> (/srv/zulip/frontend_tests/zjsunit/index.js:41:7)
    at Module._compile (module.js:556:32)
    at Object.Module._extensions..js (module.js:565:10)
    at Module.load (module.js:473:32)
    at tryModuleLoad (module.js:432:12)
    at Function.Module._load (module.js:424:3)
    at Module.runMain (module.js:590:10)
    at run (bootstrap_node.js:394:7)
    at startup (bootstrap_node.js:149:9)
    at bootstrap_node.js:509:3

**Steve Howell** · 2017-01-28 15:49 UTC

Yep! So...

**Steve Howell** · 2017-01-28 15:50 UTC

it looks like you are using the **real** version of `transmit_message` instead of a stubbed one

**Mahim Goyal** · 2017-01-28 15:50 UTC

Got it.

**Mahim Goyal** · 2017-01-28 15:50 UTC

Let me work on it.

**Steve Howell** · 2017-01-28 15:51 UTC

Ok, sounds good!  Thanks for being patient with this stuff.  :)

**Mahim Goyal** · 2017-01-28 15:53 UTC

I am learning a lot of new stuff here, its my pleasure to be working on this.

**Steve Howell** · 2017-01-28 15:53 UTC

Great!

**Mahim Goyal** · 2017-01-28 17:11 UTC

I tried but couldn't find why transmit_message() is not getting stubbed. Here is my latest code.
```
var assert = require('assert');
set_global('document', {location: {protocol: "", host: ""}});

global.stub_out_jquery();

set_global('blueslip', {});
set_global('channel', {
    post: function (options) {},
});

set_global('compose', {
    msg_server_status: {
        '100.00': "failed",
        '150.01': "failed",
}});
set_global('server_events', {
    assert_get_events_running: function() {},
});

set_global('page_params', {
    use_websockets: function() {},
    email: 'AARON@zulip.com',
});


set_global("Socket", function () {});

var compose = require("js/compose.js");

set_global('feature_flags', {
    alert_words: true,
});

 

(function test_msg_server() {
    var timeout_callback;

    global.patch_builtin('setTimeout', function (f, interval) {
        assert.equal(interval, 15000);
        timeout_callback = f;
    });

    global.patch_builtin('alert', function (content) {});
    
    var id;
    function assertions_to_test() {
        var request = {client: "website",
                       type: "stream",
                       subject: "test",
                       stream: "all",
                       private_message_recipient: "AARON@zulip.com",
                       content: "Zulip is awesome",
                       sender_id: 1,
                       queue_id: "1485357784:0"};
        

        var transmit_success_callback;
        global.compose.transmit_message = function (request, success, error) {
            id = request.local_id;
            transmit_success_callback = success;
        }; 
        compose._send_message(request);
        transmit_success_callback({id: id,msg: "", result: "success"});
        timeout_callback();
        assert.equal(compose.msg_server_status[id], "failed");
    }
    assertions_to_test();
}());

**Steve Howell** · 2017-01-28 17:16 UTC

Hmmm, that is a bit mysterious. Let me think...

**Mahim Goyal** · 2017-01-28 17:16 UTC

Sure

**Steve Howell** · 2017-01-28 17:18 UTC

One thing you can do is this:

~~~ js
console.log(compose.transmit_message)
global.compose.transmit_message = ... // stub
console.log(compose.transmit_message)
~~~

See if that reveals anything surprising.

**Mahim Goyal** · 2017-01-28 17:19 UTC

Ok, I am trying it out

**Mahim Goyal** · 2017-01-28 17:21 UTC

Both are returning `[function]`

**Steve Howell** · 2017-01-28 17:21 UTC

ha, that's not very interesting :)

**Mahim Goyal** · 2017-01-28 17:22 UTC

Yes

**Steve Howell** · 2017-01-28 17:22 UTC

I think there's a way in JS to show the code of a function.

**Mahim Goyal** · 2017-01-28 17:24 UTC

Let me see

**Steve Howell** · 2017-01-28 17:24 UTC

~~~
> f = function () {x = 'x'};
[Function: f]
> f
[Function: f]
> f.toString()
'function () {x = \'x\'}'

**Steve Howell** · 2017-01-28 17:25 UTC

The output above (^^^) is from running `node` in my vm.

**Mahim Goyal** · 2017-01-28 17:26 UTC

Ok, let me see what transmit_message() shows!

**Steve Howell** · 2017-01-28 17:29 UTC

I think the problem is that I gave you misleading advice.  Since `compose` is basically scoped to this module, perhaps you should say `compose.transmit_message = ` instead of `global.compose.transmit_message =`.  But I'm a bit confused myself why the latter even worked.

**Mahim Goyal** · 2017-01-28 17:30 UTC

Maybe because transmit_message() has been exported.

**Steve Howell** · 2017-01-28 17:32 UTC

Yeah, understanding where all these things get put into various "namespaces" can be tricky.  But I might be mis-diagnosing the problem here, too.

**Mahim Goyal** · 2017-01-28 17:32 UTC

Changing it to `compose.transmit_message` worked.

**Steve Howell** · 2017-01-28 17:33 UTC

Awesome!

**Mahim Goyal** · 2017-01-28 19:20 UTC

In `send_message() ` we have a `var local_id`, its value is put using these lines 
```
if (feature_flags.local_echo) {
        local_id = echo.try_deliver_locally(request);
        console.log("echo try deliver");
        if (local_id !== undefined) {
            // We delivered this message locally
            request.local_id = local_id;
        }
    }
``` 
I am interested in putting the value of `local_id` myself. 
I believe there to be two ways around this, first is to make this part into a different function in compose.js and then stub it. And second one being able to change the value of `local_id`by directly accessing it through the test file. I am not sure of the second case, but I find it easier to go that way. What should be done in this case?

**Steve Howell** · 2017-01-28 19:26 UTC

Can we stub `echo.try_deliver_locally`?

**Mahim Goyal** · 2017-01-28 19:28 UTC

I tried stubbing that out but it gave me the error `echo.try_deliver_locally`is not a function. The same error we were facing in `socket.send`. Perhaps the syntax I am using might be incorrect.

**Mahim Goyal** · 2017-01-28 19:29 UTC

(deleted)

**Mahim Goyal** · 2017-01-28 19:29 UTC

```
echo.try_deliver_locally = function (request) {
    return 100;
};

**Steve Howell** · 2017-01-28 19:29 UTC

probably `set_global` is the answer here

**Mahim Goyal** · 2017-01-28 19:30 UTC

I did something of this sort.

**Mahim Goyal** · 2017-01-28 19:30 UTC

Ohhk, let me try that

**Mahim Goyal** · 2017-01-28 19:34 UTC

Yes that worked, could you help me understand the difference between the two different types of stubbing here.

**Steve Howell** · 2017-01-28 19:37 UTC

It basically has to do with the "scope" of the variable.  When you say `var = ...`, the variable is scoped to the module.  When you say `set_global` is it is attached to the `global` variable.

**Mahim Goyal** · 2017-01-28 19:40 UTC

Ok Thanks :)

**Mahim Goyal** · 2017-01-28 19:51 UTC

I have completed the unit test file of `compose.js`.

**Mahim Goyal** · 2017-01-28 19:51 UTC

I will be continuing with the issue.

**Mahim Goyal** · 2017-02-17 05:46 UTC

Hi @Steve Howell  , I recently restarted the work on removing the message hanging when server is down. I was wondering what should be the approach to remove the message from the message list. The `_sockjs.send` has already been called when the message was sent, so should I send another request asking to delete to message? In this does the server already contain some functions to delete the messages or those have to be built too?

**Steve Howell** · 2017-02-17 05:49 UTC

I am not aware of any specific API to remove messages from the view.  I would study all the message modules in static/js (message_list.js,  message_list_view.js, message_live_update.js) to try to figure out if there are existing helpers and/or figure out the best approach.

**Steve Howell** · 2017-02-17 05:50 UTC

Since the server being down is a relatively rare event, we would probably be okay with a fairly "blunt" approach where we might just remove the message from the message list and re-render.  But I would study the code a bit to see if there is a more precise approach that would work.

**Mahim Goyal** · 2017-02-17 05:54 UTC

Ok, I will also start with reading those modules.

**Mahim Goyal** · 2017-02-17 05:55 UTC

But my confusion is how do we kill that sockjs request which had been called initially?

**Mahim Goyal** · 2017-02-17 05:56 UTC

If there is a way to do it I think we can just delete the message from list and re-render the message with the error on user end.

**Steve Howell** · 2017-02-17 05:56 UTC

It might be hard to kill the request itself, but you should be able to set up the callbacks so that you effectively ignore the result of the request once you've abandoned the request.

**Steve Howell** · 2017-02-17 05:59 UTC

Do you know how closures work in Javascript?

**Mahim Goyal** · 2017-02-17 06:00 UTC

I am not familiar with this I guess.

**Mahim Goyal** · 2017-02-17 06:01 UTC

Gave a quick read.

**Mahim Goyal** · 2017-02-17 06:02 UTC

How can we implement it here?

**Steve Howell** · 2017-02-17 06:02 UTC

I tried googling it, and the first couple links weren't super obvious.  But basically when you set up callback functions you do that in the scope of another function that keeps track of state.

**Mahim Goyal** · 2017-02-17 06:03 UTC

Ok, as far as I got we intend to keep track of the local variable, is this right?

**Steve Howell** · 2017-02-17 06:06 UTC

Yeah, conceptually you can do something like this:

~~~ js
function send(message) {
    var abandoned = false;

    call_server(
        timeout: 15000,
        succeed: function () {
            if (!abandoned) {
                do_stuff();
            },
        timed_out: function () {
            abandoned = true;
        }
    );
}

**Mahim Goyal** · 2017-02-17 06:14 UTC

Ok, so if the timeout is over then the succeed function will be left and timed_out function would be called, is this correct?

**Steve Howell** · 2017-02-17 06:19 UTC

As written, both callbacks could be called--your timeout function could be invoked, but then you eventually get the success function called as well.  It's hard to prevent that scenario from happening, but you can just drop the success response if you've already done the timeout logic.  What's probably more important is that you can cancel timeout logic pretty easily if you get a success response.  When you set a timeout function in JS, you can get an object back that you can call something like `clearTimeout` on.

**Mahim Goyal** · 2017-02-17 06:24 UTC

Ok let me take some time to understand the `clearTimeout`object.

**Mahim Goyal** · 2017-02-17 15:24 UTC

So if the message is sent(success response) the timeout function will break. But how can we apply this to remove the message from sockjs request.

**Steve Howell** · 2017-02-17 15:39 UTC

I'm not sure I understand your question.  Once the request goes to the server, it's hard, maybe impossible, to undo the request, even if it takes a long time to go over the network.  But we generally only care about making it clear to the sender that there was a timeout--if the message eventually gets delivered, there's not much we can do about it.

**Mahim Goyal** · 2017-02-17 22:17 UTC

Ohh ok, I was going in a different direction altogether.

**Mahim Goyal** · 2017-02-17 22:19 UTC

Ok, so what should we convey to the user, maybe something like "Your message is taking more than usual time to send" ?

**Steve Howell** · 2017-02-17 22:22 UTC

We should just say "Your message was not received.", since that will probably be accurate 90% of the time.

**Mahim Goyal** · 2017-02-18 13:14 UTC

Ok then, I will implement this.

**Mahim Goyal** · 2017-03-07 12:07 UTC

How is this looking as a notification for undelivered message?
[Error message](https://chat.zulip.org/user_uploads/2/7d/uV3Ak53mgXkMbcgz_2_bLqEL/pasted_image.png)

**Rafid Aslam** · 2017-03-07 12:30 UTC

I think "Your message was not sent" would be better

**Mahim Goyal** · 2017-03-07 12:33 UTC

Ok, I will make that change.

**Mahim Goyal** · 2017-03-07 16:49 UTC

This is the final look,
[](https://chat.zulip.org/user_uploads/2/2e/Ojup06pScETDeb69rt18KwBD/pasted_image.png)

PR #3419

**Mahim Goyal** · 2017-03-07 16:50 UTC

@Steve Howell Please take a look at this PR.

**Mahim Goyal** · 2017-03-09 12:23 UTC

It would be great if to know if there are any related issues still open? I could work on those. Thanks.

**Sumana Harihareswara** · 2017-03-09 21:45 UTC

Hi @Mahim Goyal! Have you looked around the list of issues https://github.com/zulip/zulip/issues a bit?

**Sumana Harihareswara** · 2017-03-09 21:45 UTC

I don't know whether there are any related issues still open, but if you need help looking, I can do some searches

**Mahim Goyal** · 2017-03-10 08:02 UTC

Yes, I found some issues related to webhooks. I think I will work on those now. Thanks :)

**Sumana Harihareswara** · 2017-03-11 10:38 UTC

Glad to help. :)


## github and merge conflicts

*2017-01-24 to 2017-01-27 · 201 messages · [open in Zulip](https://chat.zulip.org/#narrow/channel/18-tools/topic/github.20and.20merge.20conflicts/with/136330)*

**Andrea  Longo** · 2017-01-24 19:52 UTC

I went to check the status of a PR, and saw it was showing there were conflicts. After I had last made changes in my branch, someone had a change involving the same files merged into master. I followed the github docs and resolved the conflicts, and now there's a second commit in my PR that looks like it is including the entire other person's change into my PR because of the merge.

**Andrea  Longo** · 2017-01-24 19:52 UTC

I'm also not sure why there appeared to be a line of code, a closing </div>, missing in my change. I added it where it should be when I resolved the conflict. (I checked both my branch and master and they didn't show a problem in either change.) Everything looked ok on github.

**Andrea  Longo** · 2017-01-24 19:52 UTC

But I didn't know what to do about this extra commit, so I rebased my branch in my dev environment to get the current code to see what it looked like. Because after resolving the conflict online, github should have the most recent and my local environment out of date.

**Andrea  Longo** · 2017-01-24 19:52 UTC

I get a merge conflict on the rebase of course, but when I look at the file, it's inserted the other person's change *above* mine. That wasn't what it looked like online, and isn't where it should be.

**Andrea  Longo** · 2017-01-24 19:52 UTC

Also when I look at the PR, I don't see the Travis report from automated testing, only coveralls.

**Andrea  Longo** · 2017-01-24 19:52 UTC

What just happened? Is this other person's change now a part of my PR? What should I do to get the correct files in my dev environment?

**Andrea  Longo** · 2017-01-24 19:53 UTC

This is the PR https://github.com/zulip/zulip/pull/2691

**Steve Howell** · 2017-01-24 19:56 UTC

I would try to find an old copy of your branch in `git reflog` that is clean, and work through the rebase process again.

**Andrea  Longo** · 2017-01-24 19:58 UTC

I haven't made any changes, so my current local version should be what was in my branch on github before this. If I abandon the rebase I'm in the middle of, I should get that back.

**Andrea  Longo** · 2017-01-24 19:58 UTC

If I then try the rebase again, would it be different?

**Steve Howell** · 2017-01-24 20:01 UTC

I'm guessing that somewhere along the way, something went wrong with your original rebase.  For tricky situations, you can be super methodical and mark every one of your changes with "e" for edit, and after each step use gitk to see what your current status is.

**Andrea  Longo** · 2017-01-24 20:03 UTC

Which one do you mean as the "original rebase"? Is that something github did for me when I resolved the conflict online? I see two commits in my PR, if there was a rebase would that be the case?

**Andrea  Longo** · 2017-01-24 20:03 UTC

I started one locally, to try to get the current state from github, but abandoned it.

**Steve Howell** · 2017-01-24 20:04 UTC

I may have misunderstood what you did, but if Github reports conflicts, you are usually best off to do an interactive rebase in your local environment on your feature branch.

**Andrea  Longo** · 2017-01-24 20:05 UTC

Uh, hmm. Their docs say doing it online is great. Maybe not?

**Andrea  Longo** · 2017-01-24 20:05 UTC

There was only a conflict because there was a more recently merged change that then made my still open PR conflict.

**Steve Howell** · 2017-01-24 20:06 UTC

I can't speak to how well GH works for this, because I was trained to do it always do it locally.

**Steve Howell** · 2017-01-24 20:07 UTC

If you do an interactive rebase locally, then the first commit that has a conflict with the newer changes on master will cause the rebase to pause, and you can resolve the conflict following the instructions git gives you, which are unfortunately a little cryptic/verbose, but essentially you just edit files with conflicts  and then do `git add foo.py` to re-stage files.

**Andrea  Longo** · 2017-01-24 20:08 UTC

So I should do a local rebase, fix up whatever needs fixing (moving this other person's change to the correct place in the code) and then push the whole thing back?

**Steve Howell** · 2017-01-24 20:09 UTC

yep, basically

**Steve Howell** · 2017-01-24 20:09 UTC

and you can get help here on resolving the conflicts...once you get "paused," I would maybe post the results of `git status` here

**Andrea  Longo** · 2017-01-24 20:10 UTC

I'm confused how this doesn't make it worse by co-mingling things in my PR that shouldn't be there.

**Andrea  Longo** · 2017-01-24 20:11 UTC

I'm concerned something else is broken because now Travis is saying there's a lint problem in a different file altogether. It wasn't doing that before.

**Andrea  Longo** · 2017-01-24 20:11 UTC

I'll try the rebase again and see how it goes.

**Steve Howell** · 2017-01-24 20:12 UTC

The way that git works, let's say that you have five changes that you made.  At the end of a rebase, you will still have five changes.  But maybe the third change touched a file that his since changed on master.  That is where you will need to make manual intervention to essentially re-construct what your change "would have been" if you had started the changes later.

**Steve Howell** · 2017-01-24 20:12 UTC

And it can often be a bit tricky, but we can try to help you work though it.

**Andrea  Longo** · 2017-01-24 20:24 UTC

I edited the conflicted files, and ran lint on the results
```
feorlen-nuc[feorlen]:~/zulip/dev/zulip$ ./tools/lint-all --pep8
ERROR:Duplicate ID(s) detected :Id 'jira' present at following files:
Line 1389:templates/zerver/integrations.html
Line 1389:templates/zerver/integrations.html
Line 1389:templates/zerver/integrations.html
ERROR:Duplicate ID(s) detected :Id 'gosquared' present at following files:
Line 1010:templates/zerver/integrations.html
Line 1010:templates/zerver/integrations.html
Line 1010:templates/zerver/integrations.html
ERROR:Duplicate ID(s) detected :Id 'sentry' present at following files:
Line 2211:templates/zerver/integrations.html
Line 2211:templates/zerver/integrations.html
Line 2211:templates/zerver/integrations.html
```

**Andrea  Longo** · 2017-01-24 20:25 UTC

It's complaining about every div id in the file

**Andrea  Longo** · 2017-01-24 20:26 UTC

I only edited the parts with wordpress and zapier

**Steve Howell** · 2017-01-24 20:29 UTC

I would use these commands to get some insight:

~~~
git status
git show
git diff
git diff --cached

**Andrea  Longo** · 2017-01-24 20:36 UTC

git status says
```
rebase in progress; onto dd9e0b8
You are currently rebasing branch 'wordpress-webhook' on 'dd9e0b8'.
```

and to do the rebase I'm using the same commands I would normally use to refresh my local environment, but maybe that's not correct? Should I specifically be working only with my branch?

**Andrea  Longo** · 2017-01-24 20:36 UTC

git fetch upstream
git checkout my-branch
git rebase upstream/master
git push origin my-branch

**Steve Howell** · 2017-01-24 20:37 UTC

Use this command to do an interactive rebase: `git rebase -i upstream/master`  (the `-i` makes it interactive)

**Andrea  Longo** · 2017-01-24 20:38 UTC

I've done interactive rebases, but only on my same branch to alter my history. So this is an interactive rebase between branches?

**Steve Howell** · 2017-01-24 20:38 UTC

99% of the time you rebase your feature branch relative to upstream/master

**Andrea  Longo** · 2017-01-24 20:40 UTC

this is how I've been using interactive rebase, to fix my commit history
https://help.github.com/articles/using-git-rebase-on-the-command-line/

**Andrea  Longo** · 2017-01-24 20:41 UTC

the upstream/master sequence there is for getting the latest changes from master into my branch

**Andrea  Longo** · 2017-01-24 20:41 UTC

so I don't understand what branches should be involved here

**Andrea  Longo** · 2017-01-24 20:42 UTC

The other person's change is in master. My change is in my branch. I did a thing online that tried to merge the two, and those changes are in a new commit in my branch.

**Andrea  Longo** · 2017-01-24 20:42 UTC

so I'm rebasing what to what?

**Andrea  Longo** · 2017-01-24 20:42 UTC

I was trying to get my local environment to match what github has for the same branch

**Andrea  Longo** · 2017-01-24 20:43 UTC

so I can see what happened

**Steve Howell** · 2017-01-24 20:43 UTC

Oh, so that doc covers another typical use of rebase.  There are two types of rebases that I do commonly:
* I want to fix up my own history, because I have small wip commits that should be squashed, or I want to combine commits, or I found a bug in one of my earlier commits that didn't surface till a later commit.
* My own history is fine, but I was working off an old copy of upstream/master

**Andrea  Longo** · 2017-01-24 20:44 UTC

I've been using that doc  for your first case, cleaning up commits. I should be doing something different?

**Steve Howell** · 2017-01-24 20:44 UTC

If github is reporting conflicts to you, that's where you need to worry about the latter case.

**Steve Howell** · 2017-01-24 20:44 UTC

Well, most of the basic techniques in that doc apply to both cases, but here's the key difference...

**Andrea  Longo** · 2017-01-24 20:45 UTC

I'm confused about what is conflicting with what, because I thought I was working only with different versions of my branch, the one on github and the one I have locally

**Steve Howell** · 2017-01-24 20:45 UTC

When you're cleaning up your own commits, you usually do something like `git rebase -i HEAD~7`, because you just want to rewrite the last 7 commits.

**Steve Howell** · 2017-01-24 20:46 UTC

But when you need to get current with `upstream/master`, you do `git rebase -i upstream/master`, which does something a little more complicated under the hood--it is trying to take your deltas and apply them to a different history.

**Steve Howell** · 2017-01-24 20:47 UTC

Most of the time, you get lucky with rebasing to a new master, because people generally are touching code totally unrelated to your changes, and git can just apply your diff to a slightly different starting point and "Do What I Mean."  But if somebody made changes to the same code, it forces you to resolve the conflict and be explicit.

**Andrea  Longo** · 2017-01-24 20:50 UTC

I started a refresh my branch rebase, but then that seemed wrong. Except even if I wanted to do that (rather than get my branch only) I'm confused about what lint is complaining about.

**Andrea  Longo** · 2017-01-24 20:51 UTC

so if I abort this, and then try to actually rebase with the same branch remote and local, that would presumably give me what I was trying to do. But may not be the best way out of this mess.

**Steve Howell** · 2017-01-24 20:52 UTC

Lint is complaining that two different templates are using the same HTML id, which can cause bugs in our code due to accidentally changing the wrong widget.

**Andrea  Longo** · 2017-01-24 20:52 UTC

but it's complaining that the same line in the same file is a duplicate of itself

**Steve Howell** · 2017-01-24 20:53 UTC

I would try to get back to some known, clean state.  If you can abort your rebase, I'd run lint on your feature branch to see if your feature branch is clean.  And then once you're confident that your branch is clean, but out of date, then work on rebasing to a new copy  of upstream/master.

**Andrea  Longo** · 2017-01-24 20:53 UTC

So if I abandon this, I'm back to where I started with different code in my branch on github vs local

**Andrea  Longo** · 2017-01-24 20:54 UTC

I'll run lint again, it was fine last time I tried it

**Andrea  Longo** · 2017-01-24 20:55 UTC

I don't understand what happened when I tried to resolve conflicts via github,  and what to do about the second commit in my branch that ccreated

**Andrea  Longo** · 2017-01-24 20:55 UTC

but first clean up where I am and see what that gets me

**Steve Howell** · 2017-01-24 20:55 UTC

Yeah, the lint output is strange--it seems almost like it thinks you have multiple copies of the file.

**Andrea  Longo** · 2017-01-24 20:56 UTC

in the same directory

**Andrea  Longo** · 2017-01-24 20:56 UTC

gaaaaaa now it's complaining about provision. no.

**Andrea  Longo** · 2017-01-24 20:56 UTC

not going to add that to this mess

**Andrea  Longo** · 2017-01-24 20:57 UTC

lint will take a few minutes to run on my slow test machine

**Andrea  Longo** · 2017-01-24 21:00 UTC

lint is fine. Not even the extra blank line in wordpress.py

**Andrea  Longo** · 2017-01-24 21:00 UTC

so should I try to rebase upstream/my-branch? Or is what is on github not reliable?

**Andrea  Longo** · 2017-01-24 21:01 UTC

or however that command would work, need to go find out

**Steve Howell** · 2017-01-24 21:05 UTC

Generally the process is this...

**Steve Howell** · 2017-01-24 21:07 UTC

~~~
git checkout feature-branch
./tools/lint-all # make sure you're happy
git fetch upstream
git rebase -i upstream/master
~~~

Let's say that you started working on your feature branch when there were 1000 commits on master.  You make commits 1001, 1002, and 1003 on your feature branch.  But meanwhile the rest of the world made commits 1001-1007 on master.  You want to rebase your changes so they become 1008, 1009, and 1010 on your feature branch.

**Andrea  Longo** · 2017-01-24 21:14 UTC

I've been doing something like that, although not interactive rebase when I update from master. I pushed some changes to my PR a few days ago, it was happy.

**Andrea  Longo** · 2017-01-24 21:15 UTC

And then I check on it today and it says there are conflicts, because in the meantime someone has a different thing merged in.

**Andrea  Longo** · 2017-01-24 21:15 UTC

It seems where I have a problem is in following github's recommendation and resolving those conflicts online.

**Andrea  Longo** · 2017-01-24 21:16 UTC

Rather than doing it in my local environment.

**Andrea  Longo** · 2017-01-24 21:17 UTC

I suppose it's possible to push what I have in my local environment, without the online merge, and make that "disappear"

**Andrea  Longo** · 2017-01-24 21:18 UTC

Then in theory I'd be back to where I was before I tried online merge. I don't know if that's good, but at least it would all be within my branch

**Steve Howell** · 2017-01-24 21:19 UTC

You're eventually gonna need to resolve the conflict, and the more you wait, the more likely you are to have master create even more conflicts with your branch.

**Andrea  Longo** · 2017-01-24 21:20 UTC

I'm not sure which version of my branch I should trust, the local one before the online merge with master, or the github one with it.

**Tim Abbott** · 2017-01-24 21:21 UTC

@Andrea  Longo are you using a tool like gitk or SourceTree to view your work?

**Andrea  Longo** · 2017-01-24 21:21 UTC

No, just plain command line

**Tim Abbott** · 2017-01-24 21:21 UTC

You should be able to use those tools to visually inspect both of those versions for whether they contain what you expect

**Tim Abbott** · 2017-01-24 21:22 UTC

(They show the Git commit graph and make this kind of investigating infinitely easier)

**Andrea  Longo** · 2017-01-24 21:22 UTC

the "local" environment isn't my laptop, however.

**Andrea  Longo** · 2017-01-24 21:22 UTC

which is why I don't use more fancy tools

**Tim Abbott** · 2017-01-24 21:22 UTC

you can X-forward if needed

**Tim Abbott** · 2017-01-24 21:23 UTC

but `tig` is a command-line tool that does something similar

**Andrea  Longo** · 2017-01-24 21:24 UTC

I'll look at tig then, I'm not sure if I can x-forward through the firewall

**Andrea  Longo** · 2017-01-24 21:25 UTC

But I'm still confused at why I got in this state and what to do about it. Should I presume the version of my branch on github is bad, do the rebase locally with upstream/master, and then force push over what is on github right now?

**Andrea  Longo** · 2017-01-24 21:25 UTC

That seems wrong.

**Tim Abbott** · 2017-01-24 21:27 UTC

I don't think you need to presume anything.  I think you should actually understand the 2 states using tools that help you do so (`tig` + `git show` in whatever combination you need to understand the two states), and then proceed once you understand

**Andrea  Longo** · 2017-01-24 21:30 UTC

I can see what is in the branch looking at github, and it now contains a second commit because I resolved the merge conflict online.

**Andrea  Longo** · 2017-01-24 21:31 UTC

My local version of that branch hasn't changed.

**Andrea  Longo** · 2017-01-24 21:32 UTC

I don't have anything to add to it for what I was working on (aside from the merge issue.)

**Tim Abbott** · 2017-01-24 21:33 UTC

OK, then it seems like you can just rebase your local copy (resolving the merge conflict again) and proceed?

**Andrea  Longo** · 2017-01-24 21:33 UTC

But now there is a conflict. It seems I should have ignored github's advice and not tried to resolve it online

**Andrea  Longo** · 2017-01-24 21:33 UTC

I tried that, by my usual method, and things went badly for unknown reasons.

**Tim Abbott** · 2017-01-24 21:34 UTC

Yes, you should definitely ignore GitHub's advice on this.  Their "resolve online" feature is only going to make your life difficult (oops, fixed typo).

**Andrea  Longo** · 2017-01-24 21:34 UTC

As far as I'm concerned, I'm actually done with this local branch. Unless there is further feedback on my work, it's done.

**Andrea  Longo** · 2017-01-24 21:35 UTC

So if there's a way to fix whatever github did without involving my local environment, it's fine with me

**Andrea  Longo** · 2017-01-24 21:36 UTC

I don't know if that is an option

**Tim Abbott** · 2017-01-24 21:36 UTC

Right, but fundamentally their web UI thing is designed around making ugly history involving merge commits

**Tim Abbott** · 2017-01-24 21:36 UTC

And thus isn't going to help anyone

**Andrea  Longo** · 2017-01-24 21:36 UTC

So I've noticed.

**Andrea  Longo** · 2017-01-24 21:37 UTC

What I'm unclear on is if I should do the rebase with master locally (provided I can sort out what its problem is) and then force the results of that to the version of my branch that is on github

**Andrea  Longo** · 2017-01-24 21:38 UTC

blowing away the bad idea online resolve in the process (since it's all in my branch)

**Andrea  Longo** · 2017-01-24 21:40 UTC

I'll try the merge again

**Andrea  Longo** · 2017-01-25 00:03 UTC

I try the merge again, still get the lint errors with the repaired conflict, so I presume something is broken within that file. I try deleting my code from it. Then deleting the zapier code from it. Nope.

**Andrea  Longo** · 2017-01-25 00:03 UTC

The error suggests a broken <div>, so I go hunting around looking to see if I can find a problem. I try an online div checker. It says they all match as far as it can tell. (Not perfect, but something.)

**Andrea  Longo** · 2017-01-25 00:03 UTC

Since it takes several minutes to try lint each time, I copy the file over to a vm that isn't quite as slow. It's from last week, so a little outdated but not terribly so. I replace the integrations.html it has with the broken one. And lint doesn't have a problem. I introduce extra whitespace into the file to make sure it's checking, and it finds that.

**Andrea  Longo** · 2017-01-25 00:03 UTC

So I go back to my regular environment and switch to a different branch, one that I was using yesterday. It has the Zapier change, but not mine. And this is the branch I made the lint change for yaml with yesterday, if somehow I broke lint. As-is, lint is happy. I replace integrations.html with the broken one. No problem. I introduce a whitespace error to make sure it's checking the file. Yup.

**Andrea  Longo** · 2017-01-25 00:03 UTC

Back to the problem branch, and without starting the rebase again, I replace the existing integrations.html with the edited merged version that should have worked but didn't. No errors. Introduce whitespace and check again, it finds that.

**Andrea  Longo** · 2017-01-25 00:03 UTC

I'm working with the local version of my branch, so without the online resolve from github. My branch by itself is fine. master in my environment is fine. The copy of the merged file with the pre-rebase branch is fine. Only when I try to rebase does it blow up.

**Andrea  Longo** · 2017-01-25 00:03 UTC

And the rebase introduces an extra blank line in a different file, one that is in my branch (and the change in question) but not in master. It has no conflicts, so why would it change? The file doesn't exist in master, why should there be a problem?

**Andrea  Longo** · 2017-01-25 00:04 UTC

None of this makes any sense. What could possibly be going wrong with the rebase?

**Steve Howell** · 2017-01-25 00:23 UTC

We should try to focus specifically on what is going on with the rebase.  If you start rebasing, you'll get to a commit that has a conflict.  For us to help you, we need specific details about the commit that is causing rebase issues.  These four commands are all instructive:

~~~
git status
git show
git diff
git diff --cached

**Andrea  Longo** · 2017-01-25 00:25 UTC

Before the rebase, or during?

**Andrea  Longo** · 2017-01-25 00:25 UTC

status told me what I was expecting, but the others were huge and full of all kinds of things

**Steve Howell** · 2017-01-25 00:26 UTC

During.

If you start with a clean feature branch and then do `git rebase -i upstream/master` what output do you see?

**Andrea  Longo** · 2017-01-25 00:26 UTC

Let me start over to make sure I don't have any experiments lying around

**Andrea  Longo** · 2017-01-25 00:28 UTC

When I start the rebase it tells me this:
```
pick 3819e25 Add WordPress webhook.

# Rebase 1d1dcab..3819e25 onto 1d1dcab
```

**Steve Howell** · 2017-01-25 00:29 UTC

Is 3819e25 a pretty big commit?

**Andrea  Longo** · 2017-01-25 00:29 UTC

It's a new webhook integration, so yes

**Andrea  Longo** · 2017-01-25 00:30 UTC

Should I see other commits from master in an interactive rebase like this?

**Steve Howell** · 2017-01-25 00:30 UTC

ok...then what happens after you exit the editor?

**Steve Howell** · 2017-01-25 00:30 UTC

no, what you see so far is normal

**Andrea  Longo** · 2017-01-25 00:30 UTC

```
error: could not apply 3819e25... Add WordPress webhook.

When you have resolved this problem, run "git rebase --continue".
If you prefer to skip this patch, run "git rebase --skip" instead.
To check out the original branch and stop rebasing, run "git rebase --abort".
Could not apply 3819e25c25c1715c010d72cc1ae3c18b98ee9290... Add WordPress webhook.
```

**Andrea  Longo** · 2017-01-25 00:30 UTC

So this is where I go fix up the conflicted files.

**Steve Howell** · 2017-01-25 00:31 UTC

Can you post the section of the file that's in conflict?

**Steve Howell** · 2017-01-25 00:31 UTC

if you do `git status` it will tell you the file that has conflicts

**Andrea  Longo** · 2017-01-25 00:33 UTC

```
      <img class="screenshot" src="/static/images/integrations/yo-app/002.png" />

      <p>Multiple users can use the same Yo bot; each user should use
      their own Zulip account email in the webhook URL.</p>
    </div>

<<<<<<< HEAD
    <div id="zapier" class="integration-instructions">
      <p>Get notifications from every event supported by Zapier.</p>
      <p>First, create the stream you'd like to use for Zapier notifications,
          and subscribe all interested parties to this stream.</p>

      <p><code>{{ external_api_uri_subdomain }}/v1/external/zapier?api_key=abcdefgh&amp;stream=zapier</code></p>

      <p>
        Next, create a ZAP, picking the service you'd like
        to receive notifications from as <code>Trigger (Step 1)</code>
      </p>
      <img class="screenshot" src="/static/images/integrations/zapier/001.png" />

      <p>and <code>Webhook</code> as <code>Action (Step 2)</code>.</p>
      <img class="screenshot" src="/static/images/integrations/zapier/002.png" />

      <p>As Step 2 action please choose <code>POST</code></p>
      <img class="screenshot" src="/static/images/integrations/zapier/003.png" />

      <p>
       Configure <code>Set up Webhooks by Zapier POST</code> as follows:

       <ul>
         <li><code>URL</code> is the url we created above</li>
         <li><code>Payload Type</code> set to <code>JSON</code></li>
       </ul>
      </p>

      <p>
        Finally, configure <code>Data</code>.
        You have to add 2 fields:
        <ul>
          <li><code>subject</code> is field corresponding to a subject of the message</li>
          <li><code>content</code> is field corresponding to a content of the message</li>
        </ul>
      </p>

      <p>Example configuration:</p>
      <img class="screenshot" src="/static/images/integrations/zapier/004.png" />

       <p>You're done! Example message:</p>

      <img class="screenshot" src="/static/images/integrations/zapier/005.png" />
=======
    <div id="wordpress" class="integration-instructions">

      <p>See WordPress blog notifications in Zulip!</p>

      <p>This integration works with both <a href="http://wordpress.com">WordPress.com</a>
      blogs and self-installed blogs using software from <a href="http://wordpress.org">
      WordPress.org</a> and the optional <a href="https://wordpress.org/plugins/hookpress/">
      HookPress plugin</a>. For more details on the two, please see the WordPress.com
      support page about <a href="https://en.support.wordpress.com/com-vs-org/"> the
      difference between WordPress.com and WordPress.org.</a></p>

      <p>The destination stream for your WordPress notifications must already exist. The
      default stream is <code>wordpress</code>. Some actions are only available for self-
      installed blogs. For a complete list of supported action types, please see the table
      at the bottom of this page.</p>

      <p><b>Configuration</b></p>

      <p><em>Note: screen capture images in this tutorial use a self-installed blog.</em></p>

      <p>To configure a new webhook from WordPress, go to the <b>Webhooks</b> page in the
      <b>Settings</b> section of your blog dashboard and click <b>Add webhook</b>.</p>

      <p><img class="screenshot" src="/static/images/integrations/wordpress/wordpress_hookpress.png" /></p>

      <p>If you use WordPress.com and have trouble locating the correct page, you can reach
      it by manually typing the url in your browser address bar as in this example:</p>

      <p><code>https://<em><b>yourblogname</b></em>.wordpress.com/wp-admin/options-general.php?page=webhooks</code><\
/p>

      <p>Select the hook type <b>action</b> and the specific action that should trigger
      this webhook notification. This example uses <b>publish_post</b>, which is triggered
      when a new blog post is created.</p>

      <p>The Zulip WordPress integration uses the fields <b>post_title</b>, <b>post_type</b>,
      and <b>post_url</b> for a <b>publish_post</b> action, so select those three fields in
      the list.</p>

      <p>Next, enter the URL for the Zulip endpoint, specifying your desired destination
      stream and topic. Construct your URL like this for a WordPress.com blog: </p>

      <p><code>http://localhost:9991/api/v1/external/wordpress?api_key=abcdefgh&stream=wordpress&topic=New%20Posts</\
code></p>

      <p>and like this for a self-installed blog:</p>

      <p><code>http://localhost:9991/api/v1/external/wordpress?api_key=abcdefgh;stream=wordpress;topic=New%20Posts</\
code></p>

      <p>The parameters are as follows:
      <ul>
        <li><code>api_key</code>: the API key for your Zulip bot</li>
        <li><code>stream</code>: the stream your WordPress notifications should be posted in</li>
        <li><code>topic</code>: the name of the topic in that stream</li>
      </ul>
      </p>

      <p><em><b>Important:</b> the HookPress plugin requires parameters delimited by
      semicolons. If you have a self-installed blog, separate parameters with <code>;</code>
      instead of <code>&</code>.</em></p>

      <p><img class="screenshot" src="/static/images/integrations/wordpress/wordpress_configure_url.png" /></p>

      <p>When you are done, your configured webhook should look like this:</p>

      <p><img class="screenshot" src="/static/images/integrations/wordpress/wordpress_config_done.png" /></p>

      <p>When a new post is published, a message is created in the specified Zulip stream
      and topic.</p>
      <p><img class="screenshot" src="/static/images/integrations/wordpress/wordpress_post_created.png" /></p>

      <p><b>Types of Actions</b></p>

      <p>To configure other actions, choose a supported action from the dropdown list and
      select the appropriate fields. </p>

      <p>
        <table style="width: 100%" >
          <tr><td><b>Action</b></td><td><b>Required Fields</b></td><td><b>Blog Type</b></td></tr>
          <tr><td>publish_post</td><td>post_title, post_type, post_url</td><td>Both</td></tr>
          <tr><td>publish_page</td><td>post_title, post_type, post_url</td><td>Both</td></tr>
          <tr><td>user_register</td><td>display_name, user_email</td><td>Self-installed</td></tr>
          <tr><td>wp_login</td><td>user_login</td><td>Self-installed</td></tr>
        </table>
      </p>

      <p><b>Congratulations! You're done!</b><br /></p>

>>>>>>> 3819e25... Add WordPress webhook.
    </div>

    <div id="zendesk" class="integration-instructions">
      <p>First, create the stream you'd like to use for Zendesk notifications,
```

**Andrea  Longo** · 2017-01-25 00:34 UTC

git status only says two files are in conflict. integrations.html is the one that is a problem, the other is trivial to fix.

**Tim Abbott** · 2017-01-25 00:34 UTC

It looks like you added your integration docs at the end, rather than in the alphabetically correct place?  The conflict is because we merged another integration that was alphabetically last (Zapier)

**Andrea  Longo** · 2017-01-25 00:34 UTC

```
rebase in progress; onto 1d1dcab
You are currently rebasing branch 'wordpress-webhook' on '1d1dcab'.
  (fix conflicts and then run "git rebase --continue")
  (use "git rebase --skip" to skip this patch)
  (use "git rebase --abort" to check out the original branch)

Changes to be committed:
  (use "git reset HEAD <file>..." to unstage)

	new file:   static/images/integrations/logos/wordpress.png
	new file:   static/images/integrations/wordpress/wordpress_config_done.png
	new file:   static/images/integrations/wordpress/wordpress_configure_url.png
	new file:   static/images/integrations/wordpress/wordpress_hookpress.png
	new file:   static/images/integrations/wordpress/wordpress_post_created.png
	new file:   zerver/fixtures/wordpress/wordpress_publish_page.txt
	new file:   zerver/fixtures/wordpress/wordpress_publish_post.txt
	new file:   zerver/fixtures/wordpress/wordpress_publish_post_no_data_provided.txt
	new file:   zerver/fixtures/wordpress/wordpress_publish_post_type_not_provided.txt
	new file:   zerver/fixtures/wordpress/wordpress_unknown_action_no_data.txt
	new file:   zerver/fixtures/wordpress/wordpress_unknown_action_no_hook_provided.txt
	new file:   zerver/fixtures/wordpress/wordpress_user_register.txt
	new file:   zerver/fixtures/wordpress/wordpress_wp_login.txt
	new file:   zerver/tests/webhooks/test_wordpress.py
	new file:   zerver/views/webhooks/wordpress.py

Unmerged paths:
  (use "git reset HEAD <file>..." to unstage)
  (use "git add <file>..." to mark resolution)

	both modified:      templates/zerver/integrations.html
	both modified:      zerver/lib/integrations.py

Untracked files:
  (use "git add <file>..." to include in what will be committed)
```

**Andrea  Longo** · 2017-01-25 00:35 UTC

I added it before zendesk

**Andrea  Longo** · 2017-01-25 00:36 UTC

The new zapier one should be directly after mine.

**Andrea  Longo** · 2017-01-25 00:36 UTC

Although in the merged file, it swaps locations

**Steve Howell** · 2017-01-25 00:37 UTC

Ok, it makes sense that zapier comes before yours, despite coming after you in the alphabet, because it was merged first.

**Andrea  Longo** · 2017-01-25 00:37 UTC

And, for reasons I don't understand, the divs are messed up.

**Steve Howell** · 2017-01-25 00:38 UTC

That's just `git` not really knowing about HTML.

**Andrea  Longo** · 2017-01-25 00:38 UTC

The closing div of the webhook docs is outside the merge markers

**Andrea  Longo** · 2017-01-25 00:38 UTC

So I fix up all that stuff, and the linter explodes. Even without trying to re-order the two changes.

**Andrea  Longo** · 2017-01-25 00:39 UTC

And I don't  know what is with the missing div

**Steve Howell** · 2017-01-25 00:40 UTC

if you look at 

~~~
<div>
   a
</div>
~~~

and 

~~~
div
  a
</div>

<div>
  b
</div>
~~~

git has no way to know that you didn't actually add this:

~~~
</div>

<div>
b
~~~

**Steve Howell** · 2017-01-25 00:41 UTC

even though you probably added this:

~~~

<div>
  b
</div>
~~~

It's a quirk of diffing that diff programs don't know which "</div>" you added.

**Andrea  Longo** · 2017-01-25 00:42 UTC

I was concerned that a line of code was missing, but I added it.

**Steve Howell** · 2017-01-25 00:42 UTC

After you attempt to clean up the HTML, you can do this:

~~~
git add <file>
git diff --cached
~~~

And the diff should look clean.

**Steve Howell** · 2017-01-25 00:43 UTC

What's the other conflicted file?

**Andrea  Longo** · 2017-01-25 00:43 UTC

It will take a few minutes to fix it because I have to copy and paste big blocks of code to move stuff around

**Andrea  Longo** · 2017-01-25 00:44 UTC

The other is integrations.py, which is two lines. They are also out of order, but it's obvious what should be done.

**Steve Howell** · 2017-01-25 00:48 UTC

ok

**Andrea  Longo** · 2017-01-25 00:48 UTC

`git diff --cached` shows all the changes for the wordpress webhook

**Steve Howell** · 2017-01-25 00:50 UTC

how does the one file look?  is it clear that after you fixed the conflict that there's a self-contained diff for wordpress in that template?

**Andrea  Longo** · 2017-01-25 00:50 UTC

`zerver/views/webhooks/wordpress.py` now has an extra blank line at the end, which the linter will gripe about in a few minutes

**Andrea  Longo** · 2017-01-25 00:51 UTC

the wordpress docs in the template look ok in the diff

**Andrea  Longo** · 2017-01-25 00:52 UTC

So lint is happy with that file, although it found the whitespace in wordpress.py

**Andrea  Longo** · 2017-01-25 00:52 UTC

The only difference is I hadn't done git add (because it was failing lint)

**Steve Howell** · 2017-01-25 00:54 UTC

That file doesn't even exist on master, correct?

**Andrea  Longo** · 2017-01-25 00:54 UTC

No it doesn't, not wordpress.py

**Steve Howell** · 2017-01-25 00:55 UTC

What's the lint error?

**Andrea  Longo** · 2017-01-25 00:55 UTC

Ok wait. If the linter only checks files that git knows exists, which I already figured out yesterday, and when I was testing the merged integrations.html with other branches it saw changes to the file even if I hadn't git added them, why does git adding it during the rebase make lint not fail now?

**Andrea  Longo** · 2017-01-25 00:56 UTC

lint is complaining about wordpress.py, which is unexpected but trivial to fix.

**Andrea  Longo** · 2017-01-25 00:56 UTC

But before, when I was doing this same thing with the exception of not having done git add, the linter was blowing up on integrations.html for seemingly no reason.

**Andrea  Longo** · 2017-01-25 00:58 UTC

Is all of this mess because I didn't git add during the rebase before running the linter?

**Andrea  Longo** · 2017-01-25 00:59 UTC

I made changes when I was testing in other environments, including on an entirely different machine, where I didn't git add the file and the linter saw expected introduced changes.

**Andrea  Longo** · 2017-01-25 00:59 UTC

Then why would it not work the same while in the middle of a rebase? The linter doesn't know that is happening.

**Steve Howell** · 2017-01-25 01:01 UTC

I'm not sure exactly what happened, but the linter should not care that you did `git add`--it just reads the file on disk.

**Andrea  Longo** · 2017-01-25 01:01 UTC

That's what I thought.

**Andrea  Longo** · 2017-01-25 01:02 UTC

But now lint is happy (running again because I removed the mysterious whitespace.)

**Andrea  Longo** · 2017-01-25 01:03 UTC

Lint does care if it's a brand new file that git doesn't know about. Yesterday I ran into that testing my yaml lint change because I had to create a dummy yaml file. It wasn't found by lister if it wasn't checked in.

**Andrea  Longo** · 2017-01-25 01:05 UTC

What I'm doing differently right now is that it's an interactive rebase rather than non, and I did git add.

**Andrea  Longo** · 2017-01-25 01:05 UTC

And lint is happy.

**Andrea  Longo** · 2017-01-25 01:06 UTC

This still doesn't make any sense. I appear to have a result I can use, but I have no idea why.

**Andrea  Longo** · 2017-01-25 01:06 UTC

I'm going to try completing the rebase

**Andrea  Longo** · 2017-01-25 01:09 UTC

Ok it worked, and tests are running on my branch on github

**Andrea  Longo** · 2017-01-25 01:10 UTC

If I'm being daft about the linter, I don't understand why. I started a rebase, I fiddled with files, I ran the linter.

**Andrea  Longo** · 2017-01-25 01:10 UTC

Now, I start an interactive rebase, fiddle with files, git add, and the linter is fine.

**Steve Howell** · 2017-01-25 01:10 UTC

It's true that lint won't check files that have never been added to git.

**Andrea  Longo** · 2017-01-25 01:11 UTC

But the file it was complaining about wasn't new.

**Andrea  Longo** · 2017-01-25 01:11 UTC

So when it griped, I presumed I had done something Very Very Wrong

**Steve Howell** · 2017-01-25 01:11 UTC

yeah...I don't know

**Andrea  Longo** · 2017-01-25 01:12 UTC

I feel bad wasting everyone's time working through this. But just as much as I can't explain why it didn't work earlier, I can't explain why it does now. Sunspots?

**Andrea  Longo** · 2017-01-25 01:13 UTC

I wish I knew what I could have avoided. Because the github "Yeah Sure Resolve!" online thing seems to be a red herring. The problem was the merge.

**Steve Howell** · 2017-01-25 01:14 UTC

I don't know. :)  If one of your earlier attempts to fix the conflict was off by a "</div>" or something, it's possible that lint would have failed but in a cryptic way.

**Andrea  Longo** · 2017-01-25 01:14 UTC

At least I'm not going to let github convince me to do that again.

**Andrea  Longo** · 2017-01-25 01:15 UTC

I tried to be very careful with editing, because tracking down divs is a mess. And it failed the same way on multiple attempts, all with fresh edits.

**Andrea  Longo** · 2017-01-25 01:15 UTC

Sunspots.

**Andrea  Longo** · 2017-01-25 01:15 UTC

I think it's time for dinner.

**Steve Howell** · 2017-01-25 01:15 UTC

:)

**Andrea  Longo** · 2017-01-25 01:18 UTC

Thanks for the help. I wish it hadn't been such a mess.

**Steve Howell** · 2017-01-25 01:27 UTC

no prob :)

**Andrea  Longo** · 2017-01-27 16:46 UTC

@Steve Howell I ran into this exact problem on another rebase, involving the same file. I did `git add` and it went away.

**Andrea  Longo** · 2017-01-27 16:46 UTC

So lint doesn't just care that git knows the file exists, it also cares if you've done `git add` after changing it.

**Andrea  Longo** · 2017-01-27 16:48 UTC

I'm not sure what it's looking at when it lints something that isn't added. The file on the filesystem is the same in both cases.

**Steve Howell** · 2017-01-27 16:51 UTC

https://chat.zulip.org/#narrow/near/136580/stream/tools/topic/github.20and.20merge.20conflicts

**Steve Howell** · 2017-01-27 16:51 UTC

It often uses our "lister" module, which finds the list of files from git.

**Andrea  Longo** · 2017-01-27 16:55 UTC

This file was already known to git.

**Andrea  Longo** · 2017-01-27 16:56 UTC

I was in the middle of fixing a merge conflict in that file, so I was changing it. The only difference between getting the bizarro lint results and correct results was that I had done `git add`. I had already made the necessary changes.

**Andrea  Longo** · 2017-01-27 16:58 UTC

Based on this behavior, a file has to both be known to git (previously added so that it exists) and any recent changes known to git as well (`git add` after editing.)

**Andrea  Longo** · 2017-01-27 16:59 UTC

So that edit I made to the docs about this isn't correct.

**Steve Howell** · 2017-01-27 17:10 UTC

If you're in the middle of a rebase, that file may not have been known to git in that particular commit's history.

**Steve Howell** · 2017-01-27 17:14 UTC

You can try an experiment like this to see it in action:

~~~
git checkout master
git checkout -b foo
echo 1 > a
git add a
git commit -am wip
echo 2foo > b
git add b
git commit -am wip

git checkout master
git checkout -b bar
echo 1 > a
git add a
git commit -am wip
echo 2bar > b
git add b
git commit -am wip

git rebase -i foo

**Andrea  Longo** · 2017-01-27 17:15 UTC

Yeah, I'll have to try it in a controlled environment to confirm. At least I got past it for this thing I'm in the middle of.


## don't test here

*2017-01-29 to 2020-02-15 · 8 messages · [open in Zulip](https://chat.zulip.org/#narrow/channel/18-tools/topic/don.27t.20test.20here/with/140580)*

**Cybervox** · 2017-01-29 13:15 UTC

coba

**P D** · 2019-11-21 04:30 UTC

how does this work

**Neil Pilgrim (neiljp)** · 2019-11-21 16:57 UTC

@P D For testing we recommend using the #**test here** stream :) There are examples of people testing features there too :)

**Aleks** · 2019-12-27 14:26 UTC

nbb

**Siddharth** · 2020-01-16 12:40 UTC

testing this text

**Damir Miric** · 2020-01-16 17:33 UTC

e

**Rohitt Vashishtha** · 2020-01-16 18:11 UTC

Please use #**test here** for testing.

**Chen Chiu** · 2020-02-15 18:42 UTC

Test


## copying files after npm installs a package

*2017-02-01 to 2017-02-01 · 9 messages · [open in Zulip](https://chat.zulip.org/#narrow/channel/18-tools/topic/copying.20files.20after.20npm.20installs.20a.20package/with/142434)*

**Andrea  Longo** · 2017-02-01 01:01 UTC

I've been looking into ways to make Swagger UI easily upgradable. The problem is that I only need one directory out of the entire package, and it needs to be somewhere you can get to it with a url. Not the global location where npm installs things.

**Andrea  Longo** · 2017-02-01 01:02 UTC

Someone on the Swagger mailing list says they have seen this done with a postflight script. While npm does let you run a script from a package, I don't see a way to run a custom script that isn't already part of the package.

**Andrea  Longo** · 2017-02-01 01:03 UTC

I haven't found anything in the current provision process that has a script like this. Where would one be run?

**Tim Abbott** · 2017-02-01 01:04 UTC

Can you declare that sort of thing in `package.json`?

**Tim Abbott** · 2017-02-01 01:04 UTC

If not, we could just write code to do it as part of `scripts/lib/node_cache.py`

**Andrea  Longo** · 2017-02-01 01:04 UTC

In the Swagger UI package itself, it would appear so.

**Andrea  Longo** · 2017-02-01 01:05 UTC

But we don't control that

**Andrea  Longo** · 2017-02-01 01:07 UTC

So somewhere at the end `node_cache.py` would copy files? I looked at that to see if anything was already handled like that. I'd have to spend more time with it to see where it might be done.

**Andrea  Longo** · 2017-02-01 01:09 UTC

It looks like it builds a list of commands to execute, so after that completes presumably.


## HTML Comments

*2017-02-02 to 2017-02-03 · 3 messages · [open in Zulip](https://chat.zulip.org/#narrow/channel/18-tools/topic/HTML.20Comments/with/143579)*

**Brock Whittaker** · 2017-02-02 18:58 UTC

Hey, so currently the templates linters don't like HTML comments at all. For example with the syntax as follows:

```html
<div class="action-content">
    <!--
    <a class="small">
        COMPARE ZULIP WITH COMPETITORS <span class="arrow">&gt;</span>
    </a>
    -->
    <a class="small">
        SEE ALL FEATURES <span class="arrow">&gt;</span>
    </a>
</div>
```

You get the following traceback error for mismatched tags:

```
Traceback (most recent call last):
  File "tools/check-templates", line 154, in <module>
    check_our_files()
  File "tools/check-templates", line 44, in check_our_files
    check_html_templates(by_lang['html'], args.modified, args.all_dups)
  File "tools/check-templates", line 142, in check_html_templates
    validate(fn=fn, check_indent=(fn not in bad_files))
  File "/srv/zulip/tools/lib/template_parser.py", line 203, in validate
    state.matcher(token)
  File "/srv/zulip/tools/lib/template_parser.py", line 191, in f
    ''' % (fn, problem, start_token.s, start_line, start_col, end_tag, end_line, end_col))
lib.template_parser.TemplateParserException: 
                    fn: templates/zerver/hello.html
                    Mismatched tag.
                    start:
                        <div class="action-content">
                        line 105, col 17
                    end tag:
                        a
                        line 109, col 21
                    
```

I think this simply stems from not being able to handle multi-line commenting. Any thoughts on changing it to accept comments?

**Steve Howell** · 2017-02-02 19:01 UTC

I think the problem is a little more specific here--I suspect the parser is tripping over the fact that inside the comment we have block tags.  We should fix this regardless of my following question, but why are we commenting out code instead of simply deleting it or putting it inside of something like `if feature_turned_on`?

**Steve Howell** · 2017-02-03 03:29 UTC

#3568


## tool for scanning issues

*2017-02-02 to 2017-02-02 · 8 messages · [open in Zulip](https://chat.zulip.org/#narrow/channel/18-tools/topic/tool.20for.20scanning.20issues/with/143801)*

**Vishnu KS** · 2017-02-02 21:26 UTC

@Tim Abbott The tool is not giving me any errors when I run using  Python2.7 (I am getting an InsecurePlatformWarning warning though). Can you explain me a bit more about the problem? I must have missed something.

**Tim Abbott** · 2017-02-02 21:27 UTC

Interesting; it was failing for me

**Tim Abbott** · 2017-02-02 21:27 UTC

let me get the traceback again

**Tim Abbott** · 2017-02-02 21:28 UTC

So it's initially this:
```
Traceback (most recent call last):
  File "./tools/check-issue-labels", line 11, in <module>
    import configparser
ImportError: No module named configparser
```

**Tim Abbott** · 2017-02-02 21:28 UTC

Which makes sense, because it's called ConfigParser in Python 2.7

**Tim Abbott** · 2017-02-02 21:29 UTC

(How are you testing?  I'm using `source /srv/zulip-venv/bin/activate`)

**Vishnu KS** · 2017-02-02 21:31 UTC

I am also inside the VM. I think I have configparser installed in my vm.

**Vishnu KS** · 2017-02-02 21:31 UTC

I will fix it. :)


## run-dev

*2017-02-03 to 2017-02-03 · 5 messages · [open in Zulip](https://chat.zulip.org/#narrow/channel/18-tools/topic/run-dev/with/144157)*

**Steve Howell** · 2017-02-03 15:53 UTC

@Tim Abbott For this change, do we want to make it so that you can't launch run-dev if the old pid file is still around?  It seems like a common failure scenario is that somebody opens up two terminals and tries to run the server, but the port is taken.  I think in that case the pid file would be overwritten, so it still be hard to track down the old server.

https://github.com/zulip/zulip/commit/cb1d61cae055dbbf3a4df84de21c13b5917028a0

**Tim Abbott** · 2017-02-03 17:53 UTC

hmm, yeah, I guess the order-of-operations is wrong.  Potentially it should just kill the old one?

**Tim Abbott** · 2017-02-03 17:53 UTC

Hmm, and actually there's another issue to think about, namely that we probably want a separate pid file for each test suite.  Can probably key it off the port number or something

**Steve Howell** · 2017-02-03 18:22 UTC

There's also the possible future directions to consider, where we may switch the tests tools to using long-running servers, either shared or distinct.  I would think we'd probably key off the name of the tool.

**Tim Abbott** · 2017-02-03 18:26 UTC

yeah, that'd be reasonable too


## sed

*2017-02-28 to 2017-02-28 · 2 messages · [open in Zulip](https://chat.zulip.org/#narrow/channel/18-tools/topic/sed/with/158855)*

**Tommy Ip** · 2017-02-28 16:36 UTC

https://marmelab.com/blog/2017/02/28/sedy-the-serverless-github-bot-which-fix-typos-for-you.html I think this could fit into our workflow nicely

**Tim Abbott** · 2017-02-28 18:01 UTC

cool!  Though it looks like something that individual developers setup themselves (in that it needs push access to every fork, not just a central one)


## mypy error getting value from dict

*2017-03-01 to 2017-03-01 · 19 messages · [open in Zulip](https://chat.zulip.org/#narrow/channel/18-tools/topic/mypy.20error.20getting.20value.20from.20dict/with/159758)*

**Andrea  Longo** · 2017-03-01 19:49 UTC

I've got a dict `payload` and it's defined for mypy as type `Dict[str, Iterable[Dict[str, Any]]]`. This works:
```
foo = payload.get('foo')
```
but this doesn't
```
foo = payload.get('foo', 'Missing foo')
```
The error I get is `Argument 2 to "get" of "dict" has incompatible type "str"; expected Iterable[Dict[str, Any]]`

**Andrea  Longo** · 2017-03-01 19:49 UTC

My data is dicts inside dicts, typical for JSON. I'm confused why mypy would complain.

**Andrea  Longo** · 2017-03-01 19:52 UTC

On another line, I'm trying to get something from a nested dict:
```
bar = payload.get('bar', {}).get('baz')
```
and mypy is unhappy that the inner dict `Iterable[Dict[str, Any]]` has no `get`.

**Andrea  Longo** · 2017-03-01 19:54 UTC

I'm not sure if the initial type is incorrect, or I have to do something funky to use default values with `get`. The code works fine, but I don't know what is up with mypy.

**Tim Abbott** · 2017-03-01 19:55 UTC

@Andrea  Longo can you post the code?  This will not be possible to debug without the code in front of us

**Andrea  Longo** · 2017-03-01 19:56 UTC

Sure!

**Andrea  Longo** · 2017-03-01 19:56 UTC

```
def api_splunk_webhook(request, user_profile, client,
                       payload=REQ(argument_type='body'), stream=REQ(default='splunk'),
                       topic=REQ(default='Splunk Alert')):
    # type: (HttpRequest, UserProfile, Client, Dict[str, Iterable[Dict[str, Any]]], Text, Optional[Text]) -> HttpResponse                                                                              

    # use default values if expected data is not provided                                           
    search_name = payload.get('search_name', 'Missing search_name')
    results_link = payload.get('results_link')
    host = payload.get('result', {}).get('host', 'Missing host')
    source = payload.get('result', {}).get('source')
    raw = payload.get('result', {}).get('_raw')
```

**Andrea  Longo** · 2017-03-01 19:56 UTC

You can see I was experimenting to get it to work.

**Andrea  Longo** · 2017-03-01 19:57 UTC

so much for trying something different when I was almost done with a feature :)

**Tim Abbott** · 2017-03-01 20:03 UTC

So your issue is probably this part of the type annotation line:`Dict[str, Iterable[Dict[str, Any]]]`

**Tim Abbott** · 2017-03-01 20:04 UTC

Basically, you're declaring that all the values in that `payload` dict are `Iterable[dict[str, any]]`, and actually the different pieces have different types

**Tim Abbott** · 2017-03-01 20:04 UTC

So you should be declaring `payload` as `Dict[str, Any]` instead

**Andrea  Longo** · 2017-03-01 20:04 UTC

Ah, ok! I started by taking out Iterable and that didn't work.

**Andrea  Longo** · 2017-03-01 20:06 UTC

It will take a few minutes to run mypy, but that makes sense. Everything was fine until I tried to use  a default value with `get`.

**Andrea  Longo** · 2017-03-01 20:07 UTC

Thanks!

**Tim Abbott** · 2017-03-01 20:07 UTC

you can pass a file to mypy to make it check just that file quickly

**Andrea  Longo** · 2017-03-01 20:07 UTC

I missed that you could do that, cool!

**Andrea  Longo** · 2017-03-01 20:08 UTC

This is the first time I've run into any problems with mypy

**Andrea  Longo** · 2017-03-01 20:10 UTC

Yay it works. Awesome. I was trying to make it more complicated than I needed to.


## trouble with vagrant

*2017-04-04 to 2017-04-05 · 15 messages · [open in Zulip](https://chat.zulip.org/#narrow/channel/18-tools/topic/trouble.20with.20vagrant/with/184821)*

**Robert Hönig** · 2017-04-04 20:03 UTC

I am trying to reset my dev environment. I ran `vagrant destroy`, followed by `vagrant up` and `vagrant ssh`. The last command seems to succeed, yet when I cd to zulip and try to run `tools/run-dev.py`, I get the message
> You need to run tools/run-dev.py inside a Zulip dev environment.
If you are using Vagrant, you can `vagrant ssh` to enter the Vagrant guest.

This happened even after I restarted my computer (Windows).

**Yago González** · 2017-04-04 20:04 UTC

Just a long shot, but have you tried provisioning first?

**Robert Hönig** · 2017-04-04 20:05 UTC

I did recently, will give it a try.

**Steve Howell** · 2017-04-04 20:08 UTC

You can also post the output of `tools/diagnose` to help us debug it.

**Robert Hönig** · 2017-04-04 20:18 UTC

hmm, `provision` is still running. is it normal that it takes so long after `vagrant destroy`?

**Yago González** · 2017-04-04 20:19 UTC

Well it takes a while when it's run for the first time (which is your case, since you're on a brand new Vagrant VM)

**Tim Abbott** · 2017-04-04 20:21 UTC

In theory, `vagrant up` should have provisioned after the `vagrant destroy`; can you post the `vagrant up` output?  It's possible something failed and thus it didn't provision.

**Robert Hönig** · 2017-04-04 20:25 UTC

`vagrant up`:
```
$ vagrant up
The system cannot find the path specified.
The system cannot find the path specified.
The system cannot find the path specified.
The system cannot find the path specified.
The system cannot find the path specified.
The system cannot find the path specified.
Bringing machine 'default' up with 'virtualbox' provider...
==> default: Checking if box 'ubuntu/trusty64' is up to date...
==> default: A newer version of the box 'ubuntu/trusty64' is available! You currently
==> default: have version '20170202.1.0'. The latest is version '20170330.0.1'. Run
==> default: `vagrant box update` to update.
==> default: Clearing any previously set forwarded ports...
==> default: Clearing any previously set network interfaces...
==> default: Preparing network interfaces based on configuration...
    default: Adapter 1: nat
==> default: Forwarding ports...
    default: 9991 (guest) => 9991 (host) (adapter 1)
    default: 22 (guest) => 2222 (host) (adapter 1)
==> default: Running 'pre-boot' VM customizations...
==> default: Booting VM...
==> default: Waiting for machine to boot. This may take a few minutes...
    default: SSH address: 127.0.0.1:2222
    default: SSH username: vagrant
    default: SSH auth method: private key
    default: Warning: Remote connection disconnect. Retrying...
==> default: Machine booted and ready!
==> default: Checking for guest additions in VM...
    default: The guest additions on this VM do not match the installed version of
    default: VirtualBox! In most cases this is fine, but in rare cases it can
    default: prevent things such as shared folders from working properly. If you see
    default: shared folder errors, please make sure the guest additions within the
    default: virtual machine match the version of VirtualBox you have installed on
    default: your host and reload your VM.
    default:
    default: Guest Additions Version: 4.3.36
    default: VirtualBox Version: 5.1
==> default: Mounting shared folders...
    default: /srv/zulip => C:/Program Files/Git/zulip
==> default: Machine already provisioned. Run `vagrant provision` or use the `--provision`
==> default: flag to force provisioning. Provisioners marked to run always will still run.

```

**Tim Abbott** · 2017-04-04 20:47 UTC

> Machine already provisioned. Run `vagrant provision` or use the `--provision`

Suggests that it did not run the provisioning code

**Robert Hönig** · 2017-04-05 20:57 UTC

Yup, reprovisioning worked. Thanks everyone! 
>Machine already provisioned. Run vagrant provision or use the --provision

Why would it say "machine already provisioned", when it is in fact not?

**Tim Abbott** · 2017-04-05 21:03 UTC

That's `vagrant` output.  It tells you whether the machine has _ever_ been provisioned, not whether it's up-to-date

**Robert Hönig** · 2017-04-05 21:04 UTC

Oh, interesting!

**Sumana Harihareswara** · 2017-04-05 21:06 UTC

@Robert Hönig [I've noted a few data points re: how long re-provisioning takes on my machine](https://chat.zulip.org/#narrow/stream/development.20help/topic/provision.20timing.20tests) -- if it's been a while since I last provisioned, or if I'm provisioning from scratch, ~12 minutes is kind of normal.

**Robert Hönig** · 2017-04-05 21:10 UTC

I see, and from the discussion, I guess that the internet conection speed is also somewhat important?

**Sumana Harihareswara** · 2017-04-05 21:11 UTC

Often, yeah. I imagine it might also be helpful to have a closer mirror that you get packages from


## linting

*2017-04-21 to 2017-04-21 · 3 messages · [open in Zulip](https://chat.zulip.org/#narrow/channel/18-tools/topic/linting/with/191261)*

**Tim Abbott** · 2017-04-21 20:43 UTC

Should we rename `tools/lint-all` to `tools/lint`?

**Joshua Pan** · 2017-04-21 20:45 UTC

That'll be nice. I never understood why we had `lint-all` when we didn't have any other linting programs

**Tim Abbott** · 2017-04-21 20:48 UTC

Cool.  https://github.com/zulip/zulip/issues/4574


## gitlint

*2017-04-22 to 2021-01-19 · 66 messages · [open in Zulip](https://chat.zulip.org/#narrow/channel/18-tools/topic/gitlint/with/191530)*

**Tim Abbott** · 2017-04-22 05:34 UTC

@Tommy Ip it feels like this exception is probably a bug in your new commit message linter?
https://travis-ci.org/timabbott/zulip/jobs/224594200

The commit message, "debug", is clearly bad, but it shouldn't throw an exception :)

**Tommy Ip** · 2017-04-22 07:46 UTC

I will take a look

**Tommy Ip** · 2017-04-22 08:10 UTC

:weary: I messed up the sorting of the word list when I format it, that's why the binary search didn't work...

**Tommy Ip** · 2017-04-22 08:21 UTC

@Tim Abbott Fixed in #4582

**Tim Abbott** · 2017-04-28 00:06 UTC

@Tommy Ip I just saw another error, from repushing a newer version of a branch: https://travis-ci.org/zulip/zulip/jobs/226621415

We should check what the spec of TRAVIS_COMMIT_RANGE is; I am now suspecting it could in some cases be comparing against an older version of your branch (aka the last thing you pushed) and thus branches that force-push might sometimes fail?  Not sure ...

**Tim Abbott** · 2017-04-28 17:30 UTC

Yeah, OK, I can confirm this

**Tim Abbott** · 2017-04-28 17:31 UTC

TRAVIS_COMMIT_RANGE for that PR is from the commit selected in this screenshot to to the top of tabbott/mobile-otp in this screenshot:
[pasted image](https://chat.zulip.org/user_uploads/2/5d/ZXll3-iirPqDz7BmtI_kvdYO/pasted_image.png)

**Tim Abbott** · 2017-04-28 17:32 UTC

So I think what we probably need to do is basically our own thing, maybe involving `$(git merge-base $FIRST_PART_OF_TRAVIS_COMMIT_RANGE $END_OF_TRAVIS_COMMIT_RANGE)..$END_OF_TRAVIS_COMMIT_RANGE`

**Tim Abbott** · 2017-04-28 17:38 UTC

@Tommy Ip how have you tested #4625?  I'm using: `env TRAVIS=1 TRAVIS_COMMIT_RANGE=upstream/master~200...upstream/master ./tools/lint`, and it appears to throw a ton of errors with the current code in master.  I'm not sure this strategy is going to work out.

**Tommy Ip** · 2017-04-28 18:00 UTC

yeah quite a lot of them failed the lint

**Tim Abbott** · 2017-04-28 18:04 UTC

I think this may just mean that this whitelist approach isn't the right strategy

**Tim Abbott** · 2017-04-28 18:04 UTC

Maybe we should go back to the old blacklist, but only check the first word ( / first word after `:`)

**Tim Abbott** · 2017-04-28 18:04 UTC

Regardless, I think our testing strategy should be that we require only a small fraction of commits we're happy with to fail the linter

**Tommy Ip** · 2017-04-28 18:04 UTC

Yeah that should help

**Tim Abbott** · 2017-04-28 18:04 UTC

Otherwise it's going to be really annoying :)

**Steve Howell** · 2017-04-28 18:17 UTC

I still like the whitelist approach.  I was assuming we'd compile a pretty big whitelist up front--basically, do a one-time scan of the codebase and whitelist any verb that appears in 2+ commits at the front.

**Tim Abbott** · 2017-04-28 18:19 UTC

@Steve Howell try the command that I gave with 1000 commits, and you'll see there's a huge range we'd need to whitelist to get down to even a 1% false positive rate, which is still probably unacceptably high for a linter.

**Steve Howell** · 2017-04-28 18:37 UTC

If you make the whitelist 360 words, then these are the kind of words you reject:

~~~
369       1 Zoom
370       1 zerver.lib.upload.
371       1 [zephyr_mirror]
372       1 Wrapped
373       1 Widening
374       1 We're
375       1 Visual
376       1 [verify
377       1 validate
378       1 Utility
379       1 "Users"
380       1 UserProfile.
381       1 UserMessage.
382       1 UserActivity,
383       1 URLs
384       1 update_user_profile_caches
385       1 Untabify
386       1 unset
387       1 Unrevert
388       1 Unpack
389       1 Unique
390       1 Unconditionally
391       1 Uncondense
392       1 Uncollapsing
393       1 Un-blue
394       1 Typo
395       1 Tweaks
396       1 Triple-quote
397       1 Transmit
398       1 Translate
399       1 transactions
400       1 tools/travis/py3k
401       1 Tools
402       1 Tolerate
403       1 Tokens
404       1 Toggle
405       1 TLS
406       1 Title
407       1 Timezone

**Alex Dehnert** · 2017-04-28 18:38 UTC

360 words seems like a really long whitelist...

**Steve Howell** · 2017-04-28 18:39 UTC

For a human or a computer?

**Tommy Ip** · 2017-04-28 18:43 UTC

Yeah these are the top first words (last 2000 commits):
```
[('add', 310),
 ('fix', 300),
 ('clean', 145),
 ('remove', 124),
 ('extract', 96),
 ('move', 86),
 ('upgrade', 82),
 ('change', 82),
 ('use', 71),
 ('update', 49),
 ('rename', 44),
 ('make', 40),
 ('refactor', 25),
 ('improve', 24),
 ("don't", 21),
 ('replace', 19),
 ('simplify', 16),
 ('bring', 16),
 ('handle', 15),
 ('create', 14),
 ('pass', 14),
 ('document', 13),
 ('raise', 13),
 ('switch', 11),
 ('disable', 9),
...
```

**Steve Howell** · 2017-04-28 18:43 UTC

I'm working on a cleaned up list.

**Steve Howell** · 2017-04-28 18:46 UTC

Exactly 200 words:

~~~
Accept
Access
Add
Adjust
Advertise
Align
Allow
Also
Always
Annotate
Annotation
Apply
Automate
Automatically
Avoid
Ban
Blacklist
Blur
Break
Bring
Build
Bump
Cache
Calculate
Call
Canonicalize
Catch
Center
Change
Check
Clarify
clean
Clean
Cleanup
Clear
Close
Comment
Configure
Conform
Consistently
Consolidate
Convert
Copy
Correct
Correctly
Create
De-duplicate
Defer
Delete
Deprecate
Describe
Disable
Display
Do
Document
Don't
Downgrade
Download
DRY
Edit
Eliminate
Enable
Encode
Enforce
Enhance
Ensure
Exclude
Exit
Expand
Explain
Export
Expose
Extend
Extract
Factor
Fade
Fetch
Filter
Finish
Fix
Flip
Flush
Focus
Generate
Get
Give
Handle
Hardcode
Have
Hide
Ignore
Implement
Import
Improve
Include
Increase
Increment
Initial
Initialize
Install
Introduce
Keep
Let
Limit
Link
Linkify
Live-update
Load
Log
Maintain
Make
Mark
Match
Mention
Merge
Migrate
Modify
More
Move
Normalize
Open
Optimize
Organize
Parse
Pass
Patch
Populate
Preserve
Prevent
Properly
Provide
Put
Raise
Read
Rearrange
Recommend
Redesign
Redirect
Reduce
Re-enable
Refactor
Reformat
Reindent
Release
Remove
Rename
Render
Reorder
Reorganize
Replace
Report
Require
Restart
Restore
Restructure
Restyle
Return
Revert
Rewrite
Run
Save
Select
Send
Separate
Set
Setup
Show
Silence
Simplify
Skip
Sort
Specify
Speed
Split
Start
Stop
Store
Strip
Suggest
Support
Suppress
Switch
Take
Test
Trim
Truncate
Turn
Tweak
Type
Unbreak
Unify
Update
Upgrade
Use
Validate
Verify
Warn
Workaround
Wrap
Write

**Alex Dehnert** · 2017-04-28 18:48 UTC

For a human? Like, the computer is all that will be routinely working with the list, but in general I vaguely expect a whitelist to see some ongoing maintenance by a human, and 360 (or 200) entries seem to suggest to me a bunch of changes will need to happen. But maybe we really do want people to standardize their commit messages on the top 200 words and rephrase any creative verbs.

**Tim Abbott** · 2017-04-28 18:50 UTC

In practice, 50% of the problem we're actually trying to solve here is first word "Fixing".  It seems like we can solve that issue with basically 0% false positive rate (and thus ~0% overhead) using the blacklist approach, and so we should probably just do that

**Steve Howell** · 2017-04-28 18:51 UTC

I still kind of disagree.  People often don't even start with a verb.

**Tim Abbott** · 2017-04-28 19:21 UTC

I think we should probably turn this test off until we can get both this and the git range issue fixed

**Tim Abbott** · 2017-04-28 19:22 UTC

(The git range one is kinda tricky, because of how `TRAVIS_COMMIT_RANGE` will include commits not present in the git repository Travis makes for you, somewhat idiotically)

**Steve Howell** · 2017-04-28 19:24 UTC

Sounds like a good idea to turn it off for now, since we've gotten some good feedback.

One additional piece of feedback that I'll give is that in my workflow I run the linter a lot, often way before making a decent commit message, and the `--no-gitlint` option is helpful, but still kind of clumsy for my workflow.  I'm not sure the best way to solve it.

**Tommy Ip** · 2017-04-28 19:24 UTC

yeah I will have a look at the issue in Travis upstream

**Tim Abbott** · 2017-04-28 19:24 UTC

We have `--no-gitlint` running automatically in the pre-commit hook

**Steve Howell** · 2017-04-28 19:25 UTC

(The clumsiness comes from having several common commands that I run that do things like running node/lint or node/lint/casper or test-all, depending on what type of code I'm running and how close I am to my final commit.)

**Steve Howell** · 2017-04-28 19:25 UTC

I think `./tools/lint` does git linting by default.

**Steve Howell** · 2017-04-28 19:26 UTC

I don't even use a pre-commit hook...for me the pain is running lint.

**Tim Abbott** · 2017-04-28 19:27 UTC

You should consider using `tools/pre-commit` (`tools/setup-git-repo` enables it) -- it only runs on the files that are changed and thus is basically instant

**Steve Howell** · 2017-04-28 19:27 UTC

It's not a **huge** pain for me, so just treat my feedback as a data point, not an enhancement request.  But I suspect other folks will eventually give similar feedback when they get into deeper development.

**Tim Abbott** · 2017-04-28 19:28 UTC

But I think the issue remains for anyone who isn't using the linter, so "Just use the pre-commit hook" can't be a complete answer

**Tommy Ip** · 2017-04-28 19:28 UTC

does `tools/lint` have an option to only lint changed files?

**Steve Howell** · 2017-04-28 19:28 UTC

Are we talking about the same thing?  I'm complaining about spam when running lint.

**Tim Abbott** · 2017-04-28 19:28 UTC

yes, we are.

**Tim Abbott** · 2017-04-28 19:29 UTC

the pre-commit hook just runs the linter, but only on the new commit/changes that you just made, and thus is fast and doesn't complain about test/debug commits you might have made 30 minutes ago

**Tim Abbott** · 2017-04-28 19:30 UTC

And thus is a nicer workflow than running `tools/lint` manually, which currently will report anything that would fail the linter in your repo/git history

**Tim Abbott** · 2017-04-28 19:30 UTC

I think we could also do some sort of `tools/lint --fast` that (A) just checks files modified since upstream/master and (B) doesn't run gitlint, sorta mimicking what the `pre-commit` hook does. (and then maybe we swap the names or something)

**Tim Abbott** · 2017-04-28 19:31 UTC

So it's `lint` vs. `lint --full` or something

**Steve Howell** · 2017-04-28 19:33 UTC

If it were up to me, we'd just remove the commit hook from `./tools/lint` and make it part of something bigger like `test-all`.

**Tim Abbott** · 2017-04-28 19:33 UTC

I don't understand that comment?

**Tim Abbott** · 2017-04-28 19:34 UTC

The purpose of the pre-commit hook is to you find out in like 200ms whether you have lint errors in code you just committed, which can save you time rebasing to fix little issues that you've built other commits on top of.

**Steve Howell** · 2017-04-28 19:35 UTC

My reasoning is that while I'm developing I probably make about 5 to 30 edits for any non-trivial feature before making a commit message, and I want to lint after all the small edits, but I only need to clean up the commit message once.

**Tim Abbott** · 2017-04-28 19:35 UTC

Oh, I see, by "commit hook" you don't mean the Git pre-commit hook, you mean the "commit message check"

**Steve Howell** · 2017-04-28 19:35 UTC

I'm saying lint reporting JS errors is way more valuable to me on an iterative level than checking my commit message.

**Tim Abbott** · 2017-04-28 19:36 UTC

Yeah, that makes sense, we're just talking about two different things :).

**Steve Howell** · 2017-04-28 19:36 UTC

That's why I asked earlier. :)

**Tim Abbott** · 2017-04-28 19:36 UTC

I'm talking about running the JS/python/etc. lint checks on just the files that are changed in a commit when creating a commit.

**Tim Abbott** · 2017-04-28 19:37 UTC

Anyway, what I'm saying is that changing your workflow to use the Git `pre-commit` hook would sorta make the problem with the commit message linter go away, because rather than manually running `tools/lint` a lot and getting the commit message errors, you wouldn't.

**Tim Abbott** · 2017-04-28 19:38 UTC

I guess another approach is to make a `--gitlint` option similar to `--pep8` that is off by default but on in Travis and `test-all`.

**Tim Abbott** · 2017-04-28 19:38 UTC

hrm

**Steve Howell** · 2017-04-28 19:38 UTC

Yeah, that's what I was trying to suggest earlier.

**Steve Howell** · 2017-04-28 19:40 UTC

I said earlier:

> If it were up to me, we'd just remove the commit hook [**sic**] from ./tools/lint and make it part of something bigger like test-all.

But I should have s/hook/check/

**Tim Abbott** · 2017-04-28 19:41 UTC

OK I think here's one proposal:
* We move `gitlint` into a `tools/lint --all` (that replaces `--pep8` and `--no-gitlint`), so it's not part of the default run.  Need to document this somewhat.
* [followup] We consider making `tools/lint` only lint the files changed between the merge-based with upstream/master and the current working tree, basically to make it much faster mostly for free.

The main downside with that proposal is just complexity; for new people to the project, they may be confused why `tools/lint` doesn't report their commit message problems, but Travis (or whatever) complains.  I think that's probably OK; we already have like 5-10 other checks that we run in Travis that you can run in development but are relatively obscure.

**Steve Howell** · 2017-04-28 19:50 UTC

This might be a bit heavy, but you could require that users specify an argument every time:
* --quick: does incremental checks, skips gitlint and pep8
* --final: does thorough check, checking all files and running gitlint/pep8

If the user does not provide either argument, we'll give them good help.  And in the  docs we'll give an even more thorough description of the optimal workflow.  (Run --quick as you're debugging/trying stuff out, and then run --final before checkin.)

**Debayan Ganguly(LoopThrough-i-j)** · 2021-01-15 22:31 UTC

Hi can anyone explain why zulip/zulip [ignores: title-imperative-mood](https://github.com/zulip/zulip/blob/08d716c74175a8b63bf8eb1080381c77f3f853c6/.gitlint#L2) and creates a [custom one](https://github.com/zulip/zulip/blob/08d716c74175a8b63bf8eb1080381c77f3f853c6/tools/lib/gitlint-rules.py#L115)

**Debayan Ganguly(LoopThrough-i-j)** · 2021-01-16 07:30 UTC

can we move gitlint to zulint?

**Tim Abbott** · 2021-01-19 05:33 UTC

@Debayan Ganguly if I had to guess, the title-imperative mood feature didn't exist at the time we wrote our integration.,

**Tim Abbott** · 2021-01-19 05:34 UTC

Seems like a good opportunity to replace that with the upstream one.

**Tim Abbott** · 2021-01-19 05:34 UTC

(Maybe worth a bit of comparison in what they do)

**Debayan Ganguly(LoopThrough-i-j)** · 2021-01-19 09:28 UTC

Okay great I am working on this is python-zulip-api, Would you mind reviewing it after I am ready with it. Then I will make the required changes in zulip/zulip as well. I was recommending to have the gitlint rules file shifted to zulint. That would allow reusability of code across all the repos.


## unread count debugging

*2017-04-25 to 2017-04-26 · 3 messages · [open in Zulip](https://chat.zulip.org/#narrow/channel/18-tools/topic/unread.20count.20debugging/with/192918)*

**Tim Abbott** · 2017-04-25 22:41 UTC

I just added a new tool for doing quick development with high unread counts in 60225012e65e3372470ff61091c3acdd6782b7cf
@Brock Whittaker @Sriram FYI :)

**Tim Abbott** · 2017-04-25 22:41 UTC

It's not useful for backruptcy, since you need to also be a few days behind temporally, but should be helpful otherwise

**James Wang** · 2017-04-26 07:26 UTC

oooo nice tool - thanks this will be helpful!!


## code migrations

*2017-05-05 to 2017-05-07 · 4 messages · [open in Zulip](https://chat.zulip.org/#narrow/channel/18-tools/topic/code.20migrations/with/196870)*

**Tim Abbott** · 2017-05-05 22:22 UTC

I think a good project to try to complete before PyCon (which is likely to generate a lot of PRs that take time to merge) would be the migration to put us in compliance with PEP-8 rule E261.  @Aditya Bansal I was thinking that with your TinglingGit tool, this might be fairly easy to do without creating a lot of disruption; would you be up for giving that a try?  

Depending how this goes, we may end up wanting an extra-fancy version of the TinglingGit check that actually checks for conflicts within a file (not just file matching), but we can start with seeing what fraction of the violations can be fixed without even touching files with open PRs.

**Aditya Bansal** · 2017-05-06 14:49 UTC

Sure I have had that on my TODO for long time now, perhaps would be nice to get it done before PyCon. I should be able to do its first pass by today.

**Aditya Bansal** · 2017-05-07 20:48 UTC

Ohk, i have done the first pass of this change and created a [PR](https://github.com/zulip/zulip/pull/4707).

**Aditya Bansal** · 2017-05-07 20:49 UTC

I guess almost 50% of the files having violations to E261 rule have been fixed in PR.


## rerun option

*2017-05-08 to 2017-05-09 · 5 messages · [open in Zulip](https://chat.zulip.org/#narrow/channel/18-tools/topic/rerun.20option/with/197366)*

**Steve Howell** · 2017-05-08 18:01 UTC

It seems like the `--rerun` option may be broken or have surprising semantics.  I'm wondering if this is possible related to running parallel threads.

**Tim Abbott** · 2017-05-08 18:04 UTC

Oh, yeah, I bet that, along with coverage, its data store hasn't been ported to be parallel-friendly.

**Tim Abbott** · 2017-05-08 18:04 UTC

Open an issue and tag Umair?

**Steve Howell** · 2017-05-08 18:09 UTC

#4716 ping @Umair Khan

**Umair Khan** · 2017-05-09 04:53 UTC

Looking at this.


## travis flake?

*2017-05-13 to 2017-05-13 · 2 messages · [open in Zulip](https://chat.zulip.org/#narrow/channel/18-tools/topic/travis.20flake.3F/with/202301)*

**Steve Howell** · 2017-05-13 18:09 UTC

This seems like a Tornado flake.  I am gonna amend the PR in an hour or so for other reasons, so I'll find out for sure that's it not my code.  Just a data point for now.

https://travis-ci.org/zulip/zulip/jobs/231877651

**Tim Abbott** · 2017-05-13 19:13 UTC

agreed; not totally clear from the logs what happened


## to capture short videos as gifs

*2017-05-14 to 2023-10-09 · 21 messages · [open in Zulip](https://chat.zulip.org/#narrow/channel/18-tools/topic/to.20capture.20short.20videos.20as.20gifs/with/202575)*

**Tejas Kasetty** · 2017-05-14 15:37 UTC

Do you guys know any useful tool to record screens as gifs? I want to post an Issue and have seen few of you do it with gifs.

**Nash Vail** · 2017-05-14 15:37 UTC

LiceCap is there

**Tejas Kasetty** · 2017-05-14 15:37 UTC

thanx

**Nash Vail** · 2017-05-14 15:37 UTC

http://www.cockos.com/licecap/

**Tim Abbott** · 2017-05-14 16:16 UTC

Can one of you add a note to our README.md documentation (or a new page linked from there) on doing this?  We have a section where we talk about proposed design changes, and I feel like this perhaps belongs there

**Joshua Pan** · 2017-05-14 17:42 UTC

I use Gyazo GIF

**Shayan Toqraee** · 2017-05-15 11:44 UTC

@Joshua Pan Gyazo doesn't create GIFs in fact, it create mp4 movies. At least it was like that a few weeks ago.

**Joshua Pan** · 2017-05-15 14:25 UTC

Really? I just use it so I don't need to go into the hassle of uploading.

**Shu Chen** · 2023-10-05 16:49 UTC

Reviving this topic as I'm also interested in grabbing UI work as gifs to share. Has anything changed in the last 6 years? It looks like licecap and gyazo are both still around. I recently used the OSX screenshot tool and it spit out a .mov that I had to run through ffmpeg (and in the end it didn't look very good). I'm mostly interested in how quickly I can get it done, and either OSX or Linux support (so my only restriction is no Windows-only)

**Karl Stolley** · 2023-10-05 17:10 UTC

It's a web based tool, so it hurts my nerd cred, but EZGif.com does a great job of taking native MacOS screen captures and converting them to GIFs: https://ezgif.com/video-to-gif You can see the results on some of my PRs, like #26893

**Karl Stolley** · 2023-10-05 17:11 UTC

Note I always edit down the raw capture using the quick-look view, so all I'm doing on EZGif is setting up the frame rates, color optimization, etc.

**Alex Vandiver** · 2023-10-05 19:00 UTC

We should now have support for playing `.mov` files inline, which may make this a bit easier?

**Alex Vandiver** · 2023-10-05 19:01 UTC

Apparently we've not deployed that yet?  Let me fix that.

**Alex Vandiver** · 2023-10-05 19:12 UTC

Hm, it's `.mp4` and `.webm`, not `.mov`, which means on OSX there's an additional step to the built-in screen recorder.

**Alex Vandiver** · 2023-10-05 19:13 UTC

[Screen-Recording-2023-10-05-at-3.12.15-PM.mp4](https://chat.zulip.org/user_uploads/2/c3/PxkKxIpX2HGZhCfv6YIDSnhc/Screen-Recording-2023-10-05-at-3.12.15-PM.mp4)

**Karl Stolley** · 2023-10-05 20:04 UTC

Yeah, only the cross-platform `.mp4` and `.webm` formats are supported. That’s intentional

**Alex Vandiver** · 2023-10-05 20:06 UTC

Yeah, totally reasonable -- I'd forgotten that `.mov` wasn't, and that that's what the screen recorder produced.

**Greg Price** · 2023-10-05 20:12 UTC

Bit specialized but extremely handy when applicable: for capturing videos from an Android device, the tool that I've found works well is found inside Android Studio.

It's in the "Logcat" panel which you can get from the bottom toolbar, and then it's the "video camera" icon in the left toolbar of that panel: [image.png](https://chat.zulip.org/user_uploads/2/45/I0_hCw8ug1GEhDDud711cTIY/image.png)

The tooltip is "Record Screen".

Do that when you have a device connected for debugging, and it's just a couple of clicks to start a video and then another to end it. The result is a `.mp4` file.

**Greg Price** · 2023-10-05 20:15 UTC

That one also comes with the option to show visual feedback for taps: 
[image.png](https://chat.zulip.org/user_uploads/2/dd/Z3thxgQU61EZrjYhpDSfx0Nz/image.png)

(that's the dialog box you get on tapping the "video camera" icon)

which is extremely helpful for almost any kind of UI demonstration to make it comprehensible — the viewer wasn't there to see your actual physical finger touch the screen, and that feature lets them nevertheless see what your finger was doing.

**Alya Abbott** · 2023-10-06 02:50 UTC

I use Gifox on a Mac; I haven't done any research to try to find the best option or anything, but it works.

**Shu Chen** · 2023-10-09 08:57 UTC

Thanks everyone! I'll give these tools a try and see how they work out. I recently tried out ezgif on Karl's suggestion because I was able to extract a .mp4 from android via Greg's suggestion, but really only needed a way in that situation to slide the video to the relevant bit. Maybe it'll be easier on the mac mini with the tools there


## review

*2017-06-10 to 2017-06-11 · 6 messages · [open in Zulip](https://chat.zulip.org/#narrow/channel/18-tools/topic/review/with/223710)*

**Yago González** · 2017-06-10 15:06 UTC

Why do we `rebase upstream/master` after fetching and checking out to the PR's branch?

**Aditya Bansal** · 2017-06-10 15:13 UTC

I guess maybe to check if it has any conflicts with current master.

**Rohitt Vashishtha** · 2017-06-10 19:31 UTC

I asked the same question a while back and thought that trying out a PR as it was would be better. Thus, you'd find two tools in the `/tools` directory:
1. `fetch-pull-request`
2. `fetch-rebase-pull-request`

**Rohitt Vashishtha** · 2017-06-10 19:33 UTC

<aybe because from a merger's point of view, rebasing is important so he'd prefer to use the second tool. As someone just reviewing the PR and hoping to not have to solve any merge conflicts, first option should be good.

**Tim Abbott** · 2017-06-10 23:26 UTC

@Yago González it's because the tools were originally written for my use case of merging things, and when you're about to merge something, you want to see if it still works after rebasing onto master, since that's what you're going to merge :)

**Yago González** · 2017-06-11 06:42 UTC

Perfectly makes sense :)


## general chat

*2017-10-14 to 2017-10-14 · 1 messages · [open in Zulip](https://chat.zulip.org/#narrow/channel/18-tools/topic/general.20chat/with/298553)*

**Chriser** · 2017-10-14 21:46 UTC

Simplified Chinese translation only one line，Why not update the website of the simplified Chinese language files？


## open a PR when ready

*2017-10-19 to 2017-10-19 · 8 messages · [open in Zulip](https://chat.zulip.org/#narrow/channel/18-tools/topic/open.20a.20PR.20when.20ready/with/300693)*

**Rishi Gupta** · 2017-10-19 04:02 UTC

A feature that would be super useful to me is the ability to "open a PR only if tests pass in travis". 
Is this something that seems plausible using the github API? 
@Cynthia Lin and @Joshua Pan, in case you have thoughts on this from having worked on zulipbot.

**Joshua Pan** · 2017-10-19 04:04 UTC

Hmm, I've never seen this before.

**Tim Abbott** · 2017-10-19 04:05 UTC

I'm pretty sure something equivalent could be done with a simple script that mostly talks to the GitHub API.

**Tim Abbott** · 2017-10-19 04:05 UTC

E.g. one way to do it would be to run tests locally in a second checkout/Vagrant instance (so it won't interfere with your main thing) and then open a PR if they pass.

**Joshua Pan** · 2017-10-19 04:06 UTC

Wait, the only way this is possible if you have Travis set up on your own fork, otherwise Travis tests will never run.

**Tim Abbott** · 2017-10-19 04:06 UTC

I would certainly appreciate a tool to do that, since it'd help with the "I think this is good, but want to rerun tests before merging".

**Cynthia Lin** · 2017-10-19 04:51 UTC

It's plausible to automatically open a PR, but as for only doing so after travis tests pass, it'd have to rely on some form of Travis webhook

**Tim Abbott** · 2017-10-19 04:54 UTC

I think trying to hook it off of Travis could be kinda annoying, which is why I was thinking of the "run tests in a separate clone" strategy.


## tools/optimize-svg

*2017-10-27 to 2017-10-27 · 4 messages · [open in Zulip](https://chat.zulip.org/#narrow/channel/18-tools/topic/tools.2Foptimize-svg/with/305333)*

**Robert Hönig** · 2017-10-27 09:24 UTC

I find the output of `tools/optimize-svg` misleading in the case when you have unoptimized SVG files:
> ERROR: svgo detected unoptimized SVG files in the `static/images/integrations/logos` folder.
Please run `svgo -f static/images/integrations/logos` and commit the file changes to optimize them.

Firstly, the command `svgo` doesn't exsist in my vagrant dev env. Looking into the code, it should rather be smt like `node_modules/.bin/svgo -f static/images/integrations/logos`.

Secondly, this command gets already executed by `tools/optimize-svg`, there is no need to rerun it. I see though that we have differing cases for Travis and the local env here, so maybe make the output conditional and print `run tools/optimize-svg` when Travis is detected?

**Dmitry Ponomarev** · 2017-10-27 12:45 UTC

(deleted)

**Dmitry Ponomarev** · 2017-10-27 12:45 UTC

(deleted)

**Tim Abbott** · 2017-10-27 16:02 UTC

@Robert Hönig yeah, that sounds good.


## 会話１

*2017-10-30 to 2017-10-30 · 3 messages · [open in Zulip](https://chat.zulip.org/#narrow/channel/18-tools/topic/.E4.BC.9A.E8.A9.B1.EF.BC.91/with/306484)*

**KIKIJIKI** · 2017-10-30 06:49 UTC

よ

**KIKIJIKI** · 2017-10-30 06:50 UTC

返事

**KIKIJIKI** · 2017-10-30 06:50 UTC

よよよ


## 会話２

*2017-10-30 to 2017-10-30 · 4 messages · [open in Zulip](https://chat.zulip.org/#narrow/channel/18-tools/topic/.E4.BC.9A.E8.A9.B1.EF.BC.92/with/306486)*

**KIKIJIKI** · 2017-10-30 06:50 UTC

よよ

**Joshua Pan** · 2017-10-30 07:00 UTC

@KIKIJIKI Can you test in #**test here** stream? Thanks!

**KIKIJIKI** · 2017-10-30 07:01 UTC

ops sorry, I thought I was in #**test here**

**KIKIJIKI** · 2017-10-30 07:02 UTC

I'd delete the messages but looks like I can't


## broken linter rule

*2017-11-01 to 2017-11-01 · 4 messages · [open in Zulip](https://chat.zulip.org/#narrow/channel/18-tools/topic/broken.20linter.20rule/with/307830)*

**Brock Whittaker** · 2017-11-01 19:38 UTC

The linter rule for commas between selectors seems to break with @keyframes. This is what passes lint:

```css
@keyframes shake {
    10%, 90% {
        transform: translate3d(-1px, 0, 0);
    }

    20%,
    80% {
        transform: translate3d(2px, 0, 0);
    }

    30%,
    50%,
    70% {
        transform: translate3d(-3px, 0, 0);
    }

    40%,
    60% {
        transform: translate3d(3px, 0, 0);
    }
}
```

However if I try to change to this:

```css
-    10%, 90% {
+    10%,
+    90% {
         transform: translate3d(-1px, 0, 0);
     }
```

Which is **technically** correct, it throws an error. @Steve Howell

**Steve Howell** · 2017-11-01 19:44 UTC

Hrm, what's the error?  That change does indeed seem like something that should pass lint.  As an aside, the #**test suites** stream has mostly superceded this stream.

**Brock Whittaker** · 2017-11-01 20:08 UTC

```
css       | 78,79c78
css       | <     10%,
css       | <     90% {
css       | ---
css       | >     10%, 90% {
css       | static/styles/components.css seems to be broken:
```

**Steve Howell** · 2017-11-01 20:28 UTC

That's strange...the other examples with the same style pass, correct?


## zulip subdomain

*2017-11-06 to 2017-11-11 · 13 messages · [open in Zulip](https://chat.zulip.org/#narrow/channel/18-tools/topic/zulip.20subdomain/with/312328)*

**Rishi Gupta** · 2017-11-06 23:51 UTC

Currently if you click on iago in the dev environment, it takes you to zulip.zulipdev.org:9991. 
* I'd guess this breaks if you're not on the internet.
* It breaks if you're developing on a droplet. 

Would it make sense to make zulip the "root" domain?

**Rishi Gupta** · 2017-11-07 00:12 UTC

I guess making zulip the root domain wouldn't fix the second problem; it'd still take you to zulipdev.com.
@Vishnu Ks, any ideas?

**Vishnu KS** · 2017-11-07 10:26 UTC

Let me try to fix this :)

**Tim Abbott** · 2017-11-07 19:01 UTC

@Vishnu Ks I think we might be able to address this using @Greg Price's recent work on REALM_HOSTS.

**Tim Abbott** · 2017-11-07 19:01 UTC

Basically, I think we can set the REALM_HOST for the `zulip` realm to be `localhost:9991` or something.

**Greg Price** · 2017-11-08 04:51 UTC

Yeah, that should work. Try it out and ask questions if anything's unclear -- if so we should probably edit the comment to make it clear :)

**Vishnu KS** · 2017-11-10 22:06 UTC

* Setting host of zulip realm to localhost:9991 worked as expected.  This should solve #1 for all pre-created realms.
* One way to solve #2 is by setting the EXTERNAL_HOST environment variable to username.zulipdev.org:9991 when the droplet is created. I got the clicking on iago thing working successfully using this method. But some tests are failing due to this (github auth tests so far). If this is a good approach I can start working on implementing this and fixing tests. Thoughts?

**Tim Abbott** · 2017-11-10 22:26 UTC

@Vishnu Ks for droplets, I think we currently have some auto-detection for whether it's a droplet (might involve the username being "zulipdev" or something in provision).  We can use something like that (hopefully a bit more user-controllable) to let us set EXTERNAL_HOST in just `dev_settings.py` (not also `test_settings.py`) on droplets.

**Vishnu KS** · 2017-11-10 23:58 UTC

@Tim Abbott Created #7364

**Vishnu KS** · 2017-11-11 00:01 UTC

Let me know if this was not something you had in mind. I am off to bed now as I have a junior school alumni meet to attend in like 4 hours :)

**Tim Abbott** · 2017-11-11 00:15 UTC

Nice, that's what I was thinking :)

**Tim Abbott** · 2017-11-11 00:16 UTC

We should try out `REALM_HOSTS` tomorrow to see if it can get us back to the place where you don't need Internet to do local development....

**Vishnu KS** · 2017-11-11 21:00 UTC

Created #7371 which will allow us to work on zulip realm without the need of internet.


## 测试1

*2018-01-06 to 2018-01-06 · 1 messages · [open in Zulip](https://chat.zulip.org/#narrow/channel/18-tools/topic/.E6.B5.8B.E8.AF.951/with/429311)*

**jackzhou010** · 2018-01-06 15:19 UTC

test


## travis failing

*2018-01-09 to 2018-01-09 · 2 messages · [open in Zulip](https://chat.zulip.org/#narrow/channel/18-tools/topic/travis.20failing/with/434926)*

**Robert Hönig** · 2018-01-09 08:36 UTC

Travis backend tests are failing because of this inaccessible URL:
https://pythonhosted.org/Markdown/extensions/api.html

The `Markdown` page of that site was online until recently.

**Steve Howell** · 2018-01-09 13:34 UTC

I pushed a fix.


## Bug

*2018-02-08 to 2018-02-08 · 6 messages · [open in Zulip](https://chat.zulip.org/#narrow/channel/18-tools/topic/Bug/with/488193)*

**nil** · 2018-02-08 13:21 UTC

This is a topic about bug test

**nil** · 2018-02-08 13:22 UTC

another talk about bugs

**nil** · 2018-02-08 13:25 UTC

again

**Harshit Bansal** · 2018-02-08 13:26 UTC

@nil Please use #**test here** for testing. Thanks! :)

**nil** · 2018-02-08 13:26 UTC

@Harshit Bansal I'm sorry :-)

**Harshit Bansal** · 2018-02-08 13:26 UTC

No problem. :)


## Design

*2018-02-08 to 2018-02-08 · 2 messages · [open in Zulip](https://chat.zulip.org/#narrow/channel/18-tools/topic/Design/with/488195)*

**nil** · 2018-02-08 13:23 UTC

This is a topic about design

**nil** · 2018-02-08 13:26 UTC

yet another


## --processes arg for test-all

*2018-03-18 to 2018-03-25 · 18 messages · [open in Zulip](https://chat.zulip.org/#narrow/channel/18-tools/topic/--processes.20arg.20for.20test-all/with/544324)*

**Rafid Aslam** · 2018-03-18 10:48 UTC

Would it be nice if we add an argument again (`--processes`) for `tools/test-all`? (though it will only be used by `tools/test-backend`)

**Tim Abbott** · 2018-03-18 17:28 UTC

@Rafid Aslam can you explain what you'd want to use that argument for?

**Rafid Aslam** · 2018-03-19 00:06 UTC

@Tim Abbott sure, sometimes `tools/test-all` failing at `tools/test-backend` because by default it uses many processes (4), I can get it succeeded in my computer at around 1-2 processes. So I think it'd be nice if the `--processes` argument for `tools/test-backend` could be controlled through `tools/test-all`

**Tim Abbott** · 2018-03-19 00:42 UTC

@Rafid Aslam I think ideally we'd debug and fix any issues that make it fail running in parallel; what sort of failures are you seeing?

**Tim Abbott** · 2018-03-19 00:42 UTC

I'm curious if it's something that suggests OOM or something like the issue we're debugging on #**test suites**, which we haven't been able to reproduce locally.

**Rafid Aslam** · 2018-03-25 05:24 UTC

@Tim Abbott  Some kind of problems like this:
```
Running zerver.webhooks.freshdesk.tests.FreshdeskHookTests.test_inline_image
** Test is TOO slow: zerver.webhooks.freshdesk.tests.FreshdeskHookTests.test_inline_image (1.637 s)

======================================================================
FAIL: test_inline_image (zerver.webhooks.freshdesk.tests.FreshdeskHookTests)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/usr/lib/python3.4/unittest/case.py", line 58, in testPartExecutor
    yield
  File "/usr/lib/python3.4/unittest/case.py", line 577, in run
    testMethod()
  File "/srv/zulip/zerver/webhooks/freshdesk/tests.py", line 77, in test_inline_image
    content_type="application/x-www-form-urlencoded")
  File "/srv/zulip/zerver/lib/test_classes.py", line 633, in api_stream_message
    return self.send_and_test_stream_message(*args, **kwargs)
  File "/srv/zulip/zerver/lib/test_classes.py", line 642, in send_and_test_stream_message
    self.STREAM_NAME, **kwargs)
  File "/srv/zulip/zerver/lib/test_classes.py", line 586, in send_json_payload
    self.assertEqual(msg.sender.email, user_profile.email)
  File "/usr/lib/python3.4/unittest/case.py", line 797, in assertEqual
    assertion_func(first, second, msg=msg)
  File "/usr/lib/python3.4/unittest/case.py", line 1170, in assertMultiLineEqual
    self.fail(self._formatMessage(msg, standardMsg))
  File "/usr/lib/python3.4/unittest/case.py", line 642, in fail
    raise self.failureException(msg)
AssertionError: 'error-bot@zulip.com' != 'webhook-bot@zulip.com'
- error-bot@zulip.com
?  ^^ ^
+ webhook-bot@zulip.com
? + ^^ ^^
```
It often fails when I run it with `--processes 4`

I'm not sure about OOM, what is it anyway?

**Tim Abbott** · 2018-03-25 06:10 UTC

Intersting; can you try adding some print statements and debugging what's happening?

**Rafid Aslam** · 2018-03-25 10:49 UTC

@Tim Abbott yup! I think I've figured out the problem.
This is the message I got from the debugging.
```
{'subject': 'testserver: slow queries', 'timestamp': 1521973130, 'id': 914, 'type': 'stream', 'sending_client': 'Internal', 'sender_short_name': 'error-bot', 'sender_id': 10, 'sender_email': 'error-bot@zulip.com', 'sender_realm_str': 'zulip', 'recipient': 'logs', 'sender_full_name': 'Zulip Error Bot', 'content': '    127.0.0.1       POST    200  2.0s (mem: 9ms/16) (md: 31ms/1) (db: 62ms/20q) (+start: 10ms) /api/v1/external/freshdesk (webhook-bot@zulip.com via ZulipFreshdeskWebhook) (webhook-bot@zulip.com)'}
```
perhaps because I was opening many tabs and applications in my laptop, it slowed down the test processes. Then when the testcase was sending queries to the database, the timeout passed out and the "Error bot" showed up first before the expected message.

I think we can deactivate the 'Error bot' temporarily when running the test-backend? or is there any suggestion?

**Steve Howell** · 2018-03-25 11:27 UTC

@Rafid Aslam If we are getting slow queries during tests, it's possible we have a code problem, so we probably don't want to completely disable that code.  I'd work instead on making the symptom a little more obvious of those kind of failures.  If you're pretty convinced your machine was just overtaxed, that's a good explanation of this problem, but it might be worth taking a quick look at the queries.

**Tim Abbott** · 2018-03-25 15:21 UTC

@Rafid Aslam ahh, that makes a lot of sense!

**Tim Abbott** · 2018-03-25 15:22 UTC

I think it also explains a flake we got in master with something @Eeshan Garg recently submitted.

**Tim Abbott** · 2018-03-25 15:23 UTC

This is a very reasonable problem to see with a relatively under-powered machine, when we're checking for "the last message sent" because under this configuration, `error-bot` sends a Zulip message, and that can throw off tests that are built around assertions on the number of messages sent.

**Tim Abbott** · 2018-03-25 15:24 UTC

I think what I want to do here is disable `ERROR_BOT` by default in `test_settings.py`, and just enabled it in any tests where we're actually testing that code path.

**Tim Abbott** · 2018-03-25 15:24 UTC

Oh, and I bet this is actually also the cause of the test failures in the add_missing_messages code path that @Aditya Bansal was debugging...

**Tim Abbott** · 2018-03-25 15:24 UTC

This is a great find.

**Aditya Bansal** · 2018-03-25 17:18 UTC

when these tests are slowed down and error bot comes into play.  Are the original messages sent are scrapped and instead error_bot sends a message?

**Tim Abbott** · 2018-03-25 17:35 UTC

No, what's happening is just that tests that check the number of messages sent get an off-by-one error (because error_bot sent a message) and tests that check the last message sent can also get the wrong "last message" if the error-bot one came later.

**Aditya Bansal** · 2018-03-25 19:09 UTC

So actually messages couldn't have been gone off for the add_missing_messages test as the same way as the error bot case because error bot case adds a message (that is a +1) whereas in the case of test_add_missing_messages we were short of 1 message.
The test_add_missing_messages case requires an event to be happening just at the time of the sending those messages to explain the anomaly because it had block of code containing similar tests on sending messages and counts just before it in the same test which executed fine.
(Should we be talking about this in some other topic or stream?)


## rocketchat importer

*2018-06-30 to 2018-06-30 · 7 messages · [open in Zulip](https://chat.zulip.org/#narrow/channel/18-tools/topic/rocketchat.20importer/with/605755)*

**Robby O'Connor** · 2018-06-30 04:12 UTC

has anyone worked on a rocket chat import tool yet?

**Rishi Gupta** · 2018-06-30 05:53 UTC

@Robby O'Connor we have not. It should be pretty easy to get it into the zulip import format though, if the rocket.chat export part is easy. We'd be happy to help someone work through a patch to add official support.

**Robby O'Connor** · 2018-06-30 06:00 UTC

I'll look into it i guess

**Rishi Gupta** · 2018-06-30 06:04 UTC

great, thanks! Feel free to post here liberally (e.g. in #**backend**  or #**development help**) as you look into it.

**Tim Abbott** · 2018-06-30 08:21 UTC

@Rhea Parekh may be able to provide advice as well

**Rhea Parekh** · 2018-06-30 17:41 UTC

I would be able to help build this support if there is a working rocket chat export. Also the other thing we can do is, try to find out if there is a Rocket.chat to Slack importer, and then we can do that to get slack data, then import it to Zulip using Zulip's Slack import tool.

**Rishi Gupta** · 2018-06-30 17:52 UTC

@Robby O'Connor fyi


## push-to-pull-request

*2018-07-24 to 2018-07-24 · 11 messages · [open in Zulip](https://chat.zulip.org/#narrow/channel/18-tools/topic/push-to-pull-request/with/616868)*

**Tim Abbott** · 2018-07-24 01:11 UTC

@Greg Price I discovered with @Rishi Gupta a key bug in `push-to-pull-request`; it doesn't check if `jq` is installed.

**Tim Abbott** · 2018-07-24 01:11 UTC

(And thus throws confusing errors in that case)

**Tim Abbott** · 2018-07-24 01:12 UTC

Since it's something you usually run outside Vagrant (since you need to be able to push), I think the correct solution is that we should check whether `jq` is in PATH, and if not, throw a nice error message, rather than installing it in our dev environment.

**Abhigyan Khaund** · 2018-07-24 04:04 UTC

@Akash Nimare  The issue that maybe we faced the other day related to `jq` in this tool.

**Akash** · 2018-07-24 04:42 UTC

Oh yes, I didn't know that.

**Tim Abbott** · 2018-07-24 05:21 UTC

Sounds like other folks ran into this problem :)

**Greg Price** · 2018-07-24 05:49 UTC

Ha, oops :smiley: -- yeah, I agree with that solution.

**Greg Price** · 2018-07-24 06:17 UTC

Pushed a fix. Thanks for the report!

**Tim Abbott** · 2018-07-24 06:19 UTC

@Greg Price I don't see the push?

**Greg Price** · 2018-07-24 06:19 UTC

Oh ha, thanks -- should be there now.

**Greg Price** · 2018-07-24 06:21 UTC

(I have my `zulip` clone configured differently from my `zulip-mobile` clone, which I use more often these days; so the first time, I actually pushed to gnprice/zulip instead of zulip/zulip.)


## vagrant

*2018-12-13 to 2021-01-27 · 156 messages · [open in Zulip](https://chat.zulip.org/#narrow/channel/18-tools/topic/vagrant/with/671218)*

**Rishi Gupta** · 2018-12-13 08:28 UTC

My `/home/vagrant/.bash_profile` looks like the following, for some reason. 
```
source .bashrc
source /srv/zulip-venv/bin/activate
cd /srv/zulip
source /srv/zulip-py3-venv/bin/activate
cd /srv/zulip
source /srv/zulip-py3-venv/bin/activate
cd /srv/zulip
source /srv/zulip-py3-venv/bin/activate
cd /srv/zulip
source /srv/zulip-py3-venv/bin/activate
cd /srv/zulip
source /srv/zulip-py3-venv/bin/activate
cd /srv/zulip
source /srv/zulip-py3-venv/bin/activate
cd /srv/zulip
source /srv/zulip-py3-venv/bin/activate
cd /srv/zulip
source /srv/zulip-py3-venv/bin/activate
cd /srv/zulip
source /srv/zulip-py3-venv/bin/activate
cd /srv/zulip
source /srv/zulip-py3-venv/bin/activate
cd /srv/zulip
source /srv/zulip-py3-venv/bin/activate
cd /srv/zulip
source /srv/zulip-py3-venv/bin/activate
cd /srv/zulip
source /srv/zulip-py3-venv/bin/activate
cd /srv/zulip
source /srv/zulip-py3-venv/bin/activate
cd /srv/zulip
source /srv/zulip-py3-venv/bin/activate
cd /srv/zulip
source /srv/zulip-py3-venv/bin/activate
cd /srv/zulip
source /srv/zulip-py3-venv/bin/activate
cd /srv/zulip
source /srv/zulip-py3-venv/bin/activate
cd /srv/zulip
source /srv/zulip-py3-venv/bin/activate
cd /srv/zulip
source /srv/zulip-py3-venv/bin/activate
cd /srv/zulip
source /srv/zulip-py3-venv/bin/activate
cd /srv/zulip
source /srv/zulip-py3-venv/bin/activate
cd /srv/zulip
```

Any ideas how I got so many copies of
```
cd /srv/zulip
source /srv/zulip-py3-venv/bin/activate
```

**Vishnu KS** · 2018-12-13 09:44 UTC

@Rishi Gupta I think there was a bug before that used to write these lines each and every time we do provision. It was fixed like an year before. Its shouldn't increase the number of lines now.

**Vishnu KS** · 2018-12-13 09:59 UTC

So all these lines are from like an year before. You can verify by running provision and noting the number of lines before and after.

**Vishnu KS** · 2018-12-13 10:02 UTC

https://github.com/zulip/zulip/commit/508686bed48cc3c6f7c7dc21f69e7a2e37de1263

**Rishi Gupta** · 2018-12-13 17:07 UTC

got it. Thanks!

**Tim Abbott** · 2018-12-13 17:22 UTC

Definitely worth cleaning that up in your copy :)

**Hendrik Visage** · 2020-05-17 17:59 UTC

Seems the most relevant place/topic:

I just tonight tested MAIN zulip branch with vagrant on MacOS (10.14.6, Vagrant 2.2.9, VirtualBox 6.1.8)

I just, doesn't start, typically stuck on the booting of that VM (and it "stuck" VBox Manager too ;(). seems that this line in `VagrantFile` is the guilty:
```
123     vb.customize [ "modifyvm", :id, "--uartmode1", "disconnected" ]
```
Commenting it out, and the VM starts and gets configured

**Greg Price** · 2020-05-19 02:00 UTC

@Hendrik Visage I'd recommend #**provision help** -- that's a more active stream which covers this kind of issue, and you might get an answer quicker there.

(I don't have any ideas for you myself, sorry; this isn't a subsystem I spend much time with.)

**Diptesh Choudhuri** · 2020-12-27 15:47 UTC

Question: why does this project use vagrant instead of docker?

**Ganesh Pawar (ganpa3)** · 2020-12-27 16:27 UTC

Vagrant is a virtual development environment manager. It builds and maintains docker containers, VirtualBox, etc. You can use Docker, VirtualBox, or parallels for working on Zulip. You can refer ```Vagrantfile``` for more details.

**Aman (amanagr)** · 2020-12-27 16:56 UTC

@Diptesh Choudhuri are you talking about development or production installation? We support different kinds of setup (including docker) for dev purposes based on OS.

**Diptesh Choudhuri** · 2020-12-28 01:35 UTC

I'm talking about the development environment.
On a side note, I find the vagrantfile quite difficult to follow. Does it actually build any docker containers in the development environment? I see a Dockerfile-postgresql in the repo but no explicit mention of it in the Vagrantfile.

**Aman (amanagr)** · 2020-12-28 02:08 UTC

@Diptesh Choudhuri What is your OS?

**Aman (amanagr)** · 2020-12-28 02:09 UTC

I don't think you have any need to read Vagrantfile unless you are debugging something in there.

**Diptesh Choudhuri** · 2020-12-28 03:04 UTC

I use Arch Linux. I am not really debugging anything. But i am trying to learn vagrant and how it might be more useful over docker. Basically I am trying to understand why would ZT use vagrant over docker.

**Diptesh Choudhuri** · 2020-12-28 03:05 UTC

And due to the lack of good resources regarding vagrant and Django, I have been trying to read into ZTs Vagrantfile.

**Aman (amanagr)** · 2020-12-28 03:11 UTC

Vagrant is just a wrapper to help us support running our dev setup on different OS and using different providers like parallels, docker, virtualbox etc.

**Aman (amanagr)** · 2020-12-28 03:12 UTC

We ZT to indicated zulip terminal here. What do mean by it?

**Aman (amanagr)** · 2020-12-28 03:12 UTC

Did you read the vagrant setup docs? https://zulip.readthedocs.io/en/latest/development/setup-vagrant.html

**Ganesh Pawar (ganpa3)** · 2020-12-28 03:46 UTC

@Diptesh Choudhuri Since you are using Arch, you will be using Docker for working on Zulip. You can see the Dockerfile at ```tools/setup/dev-vagrant-docker/Dockerfile```.

**Diptesh Choudhuri** · 2020-12-28 03:59 UTC

Very sorry. I thought ZT meant Zulip itself. Is ZT the thing I get when I do `vagrant ssh` in the project root?

**Diptesh Choudhuri** · 2020-12-28 03:59 UTC

(replying to Aman Agrawal)
> Did you read the vagrant setup docs? https://zulip.readthedocs.io/en/latest/development/setup-vagrant.html
Yes I did. I have already setup Zulip in my machine and it works fine.

**Diptesh Choudhuri** · 2020-12-28 03:59 UTC

(replying to Ganesh Pawar)
> @Diptesh Choudhuri Since you are using Arch, you will be using Docker for working on Zulip. You can see the Dockerfile at ```tools/setup/dev-vagrant-docker/Dockerfile```.
Thank you very much!

**Aman (amanagr)** · 2020-12-28 04:01 UTC

(replying to Diptesh Choudhuri)
> Very sorry. I thought ZT meant Zulip itself. Is ZT the thing I get when I do `vagrant ssh` in the project root?
No, you get ubuntu 18 with zulip-py3-env activated.

**Aman (amanagr)** · 2020-12-28 04:02 UTC

You are inside zulip project too. I don't know how you picked up zt keyword.

**Diptesh Choudhuri** · 2020-12-28 04:02 UTC

I was looking at some of the other threads. Must have picked it up from there. Sorry for the confusion.

**Diptesh Choudhuri** · 2020-12-28 05:34 UTC

Is there any specific reason why Zulip uses the docker provider for Linux instead of Virtual BOX?

**Anders Kaseorg** · 2020-12-28 21:59 UTC

On platforms where you have the option, Docker is more efficient.

**Diptesh Choudhuri** · 2020-12-29 01:43 UTC

Docker is faster because it doesn't create virtual machines, however I am starting to love Vagrant because of the ssh features it provides.

**Anders Kaseorg** · 2020-12-29 08:55 UTC

That isn’t an either-or choice. When you run `vagrant up --provider=docker`, you get the Docker backend of Vagrant, with which you can use `vagrant ssh` just as you can with the VirtualBox backend of Vagrant.

**Rein Zustand** · 2020-12-29 09:16 UTC

Also, Docker has `docker attach` (https://docs.docker.com/engine/reference/commandline/attach/) which allows interactive shell to the container.

**Rein Zustand** · 2020-12-29 09:21 UTC

Or `docker start -i <container_name>`.

**Anders Kaseorg** · 2020-12-29 09:32 UTC

You don’t interact with Docker directly to use the Zulip development environment; it all goes through Vagrant, which uses the backend you specified behind the scenes (Docker or VirtualBox).

**Rein Zustand** · 2020-12-29 09:35 UTC

The method I mentioned may not be the recommended approach for devs, but just wanted to say that the "ssh" advantage of Vagrant is not specific to Vagrant.

**Diptesh Choudhuri** · 2020-12-29 10:22 UTC

But when you do docker -i the shell you get is ephemeral. The changes are destroyed as soon as you exit it. Vagrant works on virtual machines and the changes you make are saved.

**Diptesh Choudhuri** · 2020-12-29 10:22 UTC

I'll be honest, I'm very new to this ssh stuff. Maybe you can do remote development with docker afterall and I just don't know it yet

**Diptesh Choudhuri** · 2020-12-29 10:23 UTC

Either way remote development with vagrant is quite neat imo

**Rein Zustand** · 2020-12-29 10:27 UTC

There is `docker --mount` to bind a directory from the parent os and make it accessible from the Docker shell.

**Rein Zustand** · 2020-12-29 10:27 UTC

```docker run -it --name foobar --mount src=`pwd`,target=/common_folder,type=bind ubuntu```

**Rein Zustand** · 2020-12-29 10:29 UTC

The ````pwd```` directory will be accessible inside the Docker shell at `/common_folder`.

**Diptesh Choudhuri** · 2020-12-29 10:32 UTC

Oh I'm aware of docker volumes. What I was talking about is remote development.

Vscode has this extension which let's me develop directly inside the virtual machine that vagrant creates. This way I don't even have to have python installed on my system to develop for zulip.

**Rein Zustand** · 2020-12-29 10:33 UTC

May I know the extension? I'm guessing people probably have written an equivalent extension for Docker too.

**Diptesh Choudhuri** · 2020-12-29 13:28 UTC

https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.vscode-remote-extensionpack

**Diptesh Choudhuri** · 2020-12-29 13:28 UTC

It's called remote development

**Vishnu KS** · 2020-12-29 15:05 UTC

(replying to Diptesh Choudhuri)
> I'll be honest, I'm very new to this ssh stuff. Maybe you can do remote development with docker afterall and I just don't know it yet
This is possible with vscode. See https://code.visualstudio.com/docs/remote/containers

**Vishnu KS** · 2020-12-29 15:11 UTC

> Docker is faster because it doesn't create virtual machines, however I am starting to love Vagrant because of the ssh features it provides.

This is true only for Linux. For Windows and Mac, docker still needs a virtual machine that runs Linux since docker containers are run by making use of namespaces and control groups present only in the Linux kernel.

**Diptesh Choudhuri** · 2020-12-29 15:18 UTC

Wow this stuff is so cool. Seems like i have been living under a rock all this while.

**Rein Zustand** · 2020-12-30 03:24 UTC

> For Windows and Mac, docker still needs a virtual machine that runs Linux since docker containers are run by making use of namespaces and control groups present only in the Linux kernel.

What about running Docker/Vagrant on WSL for Windows?

**Anders Kaseorg** · 2020-12-30 03:38 UTC

Vagrant actually has a [WSL backend](https://www.vagrantup.com/docs/other/wsl), no Docker necessary. I don’t think anyone’s tried it with the Zulip dev environment yet though.

**Aman (amanagr)** · 2020-12-30 04:01 UTC

Oh! We should definitely try to integrate that. Looks like it was added recently https://github.com/hashicorp/vagrant/blob/main/website/content/docs/other/wsl.mdx

**Diptesh Choudhuri** · 2020-12-30 04:07 UTC

Can I take this up?

**Diptesh Choudhuri** · 2020-12-30 04:08 UTC

Integration with Vagrant and WSL

**Aman (amanagr)** · 2020-12-30 06:24 UTC

@Diptesh Choudhuri Sure!

**Diptesh Choudhuri** · 2020-12-30 09:14 UTC

Hello I have been able to get zulip running with WSL. What do i do next?

**Diptesh Choudhuri** · 2020-12-31 03:42 UTC

About setting up vagrant with WSL. I have been able to do that. Should i write documentation for it? @Aman Agrawal

**Aman (amanagr)** · 2020-12-31 06:27 UTC

@Diptesh Choudhuri Yes.

**Diptesh Choudhuri** · 2021-01-01 15:29 UTC

Can someone please assign me issue #16994? I can't claim it since I'm a first time contributor.

**Aman (amanagr)** · 2021-01-01 15:36 UTC

@Diptesh Choudhuri Just did!

**Diptesh Choudhuri** · 2021-01-01 15:38 UTC

Thanks! Will get to it asap.

**Diptesh Choudhuri** · 2021-01-01 17:22 UTC

Thanks! Will get to it asap.

**Diptesh Choudhuri** · 2021-01-02 05:42 UTC

@Aman Agrawal where do you recommend I add the documentation? Should I do it under the Windows 10 heading in setup-vagrant.md?

**Aman (amanagr)** · 2021-01-02 05:53 UTC

We need to see if wsl is a better provider than virtualbox. Since wsl is more tightly integrated with windows, it ideally should be (or will be in long run).  Can you open a PR with just the code changes? I would like to test how easy it is to setup and should we recommend it by default or not in vagrant setup.

**Diptesh Choudhuri** · 2021-01-02 06:28 UTC

I am using the virtual box provider, the only difference is that the command vagrant up is run in Ubuntu bash that WSL provides. It still uses the virtualbox provider

**Diptesh Choudhuri** · 2021-01-02 06:29 UTC

There are a few other commands that need to be executed to get it working correctly but that's pretty much all there is.

**Aman (amanagr)** · 2021-01-02 12:45 UTC

Oh! I was thinking we would use WSL as a vagrant provider. Sorry for the misunderstanding on my part. I am not sure folks would like to run vagrant from within wsl rather than directly doing dev setup on top it. I don't think we should be recommending that in our developer docs either.

**Aman (amanagr)** · 2021-01-02 12:46 UTC

@Anders Kaseorg what do you recommend?

**Diptesh Choudhuri** · 2021-01-02 13:22 UTC

Should I try something with custom providers? https://www.vagrantup.com/docs/plugins/providers

**Aman (amanagr)** · 2021-01-02 14:12 UTC

I would suggest waiting for Anders to reply.

**Anders Kaseorg** · 2021-01-02 21:40 UTC

Aman is right, the [proposal](https://chat.zulip.org/#narrow/stream/18-tools/topic/vagrant/near/1089719) was to try the WSL backend of Vagrant. I don’t think there’s any reason to run Vagrant inside WSL.

**Diptesh Choudhuri** · 2021-01-03 04:39 UTC

Alright that does make sense. Should I close the github issue?

**Aman (amanagr)** · 2021-01-04 01:37 UTC

just did.

**Tim Abbott** · 2021-01-05 00:52 UTC

Hmm, yeah, using WSL as a Vagrant provider does seem worth trying.

**Anders Kaseorg** · 2021-01-05 00:55 UTC

I think what I assumed was a WSL provider is actually a Hyper-V provider?

**Anders Kaseorg** · 2021-01-05 00:56 UTC

WSL 2 uses Hyper-V but I’m not sure if the performance implications would be quite the same. Still worth trying.

**Tim Abbott** · 2021-01-05 00:57 UTC

Ahh, I see.  Yeah, that could still be a good choice.

**Diptesh Choudhuri** · 2021-01-05 05:14 UTC

I'll try to configure a hyperV provider then today. If I succeed, I'll reopen the issue #16994.

**Aman (amanagr)** · 2021-01-05 05:50 UTC

I found an effort done by someone in this direction https://github.com/deluxebrain/wsl-vagrant-hyperv-setup . @Diptesh Choudhuri , might be worth taking a look.

**Diptesh Choudhuri** · 2021-01-05 13:16 UTC

I am in the middle of my exams so I might not be able to do it this week. Thanks for the pointer though @Aman Agrawal !

**Diptesh Choudhuri** · 2021-01-07 13:41 UTC

I worked on this today and here's what I could do:

**Note:** All my efforts failed and I have concluded that it is pretty much impossible to configure a hyper-V provider for zulip. I am just describing what all I could observe.

1. It's extremely slow. We initially started this venture because  believed that hyper-V might be faster due to it being native to windows. However, each fresh `vagrant up` took at least 30 minutes on my decent machine. Not to mention the fact that none of the provisioning actually passed.
2. Most provisions failed specifically at one point: [here](https://github.com/IgnisDa/zulip/blob/master/Vagrantfile#L181) and sometimes due to a failed mount command that is used to bring up the synced drives [here](https://github.com/IgnisDa/zulip/blob/master/Vagrantfile#L64).
3. I tried all types of synced folder strategies described in the vagrant [docs](https://www.vagrantup.com/docs/synced-folders). None of them worked. [SMB](https://www.vagrantup.com/docs/synced-folders/smb) was particularly disappointing since there were a lot of permission errors.
4. I also had to create a separate windows user on my machine since vagrant and Hyper-V just won't play nice with the default one. I don't think any developer contributing to zulip would like to do that.
5. Going by the [pointer](https://github.com/deluxebrain/wsl-vagrant-hyperv-setup#wsl-vagrant-hyperv-setup) given by @Aman Agrawal in his previous message, even if we are able to configure a hyper-V provider, it would put the guest machine is a read only mode, which pretty much defeats the purpose of remote development.

All in all, I was really disappointed how difficult Hyper-V (and Windows) is to work with. 10/10 wouldn't recommend.

**Aman (amanagr)** · 2021-01-08 03:20 UTC

@Diptesh Choudhuri Thanks for your efforts!

**Rein Zustand** · 2021-01-08 04:12 UTC

Maybe the issue should remain open, then retry a year or two later once the tech has matured?

**Greg Price** · 2021-01-08 04:57 UTC

Thanks also for the detailed notes!

**Greg Price** · 2021-01-08 05:00 UTC

(replying to Diptesh Choudhuri)
> 5. Going by the [pointer](https://github.com/deluxebrain/wsl-vagrant-hyperv-setup#wsl-vagrant-hyperv-setup) given by @Aman Agrawal in his previous message, even if we are able to configure a hyper-V provider, it would put the guest machine is a read only mode, which pretty much defeats the purpo …

One thing I notice in that doc is that it refers several times to "us[ing] Vagrant with Hyper-V *within WSL*", or other wordings of the same idea.

That sounds to me like it's focused on using WSL for the *outer* environment, aka the host, where you run Vagrant *from*.

I'd expect that to be a more or less unrelated thing from using WSL just for the *inner* environment, aka the guest, the environment that Vagrant manages for you (and, for the Zulip case, where your Zulip dev server would live.) I think the goal that would be most interesting here is to find a way to use WSL as the guest.

**Greg Price** · 2021-01-08 05:02 UTC

> Two-way synced folders are not supported
>
> Vagrant support for two-way synced folders is via either VirtualBox or SMB. The former is obviously not applicable, and unfortunately the latter does not work under WSL.

This in particular sounds very much like it's specifically about WSL as the *host* environment.

Those [Vagrant docs](https://www.vagrantup.com/docs/synced-folders/smb) say that SMB isn't supported when the host is Linux, only when the host is Windows or macOS. So it makes sense that that'd mean it isn't supported when the host is WSL, because a WSL environment is a kind of Linux environment.

But if you use plain old Windows for the host and WSL for the guest, then that's Windows as host and Linux as guest -- and the docs clearly say that should work great with SMB.

**Greg Price** · 2021-01-08 05:07 UTC

I'd also expect that using WSL as the host would quite likely make things slower. That means having a VM for the host as well as a VM for the guest; and it might even mean having the guest as a VM inside the VM for the host. I expect that nesting a VM inside a VM is not a common configuration for Hyper-V (if it's even possible), and it'd be unsurprising for it to be quite slow.

**Greg Price** · 2021-01-08 05:12 UTC

OK, I just took a look around those Vagrant docs that you helpfully linked to.

Based on what's at https://www.vagrantup.com/docs/providers , I think the most promising strategy doesn't involve WSL (or at least nothing labeled WSL in the instructions.) Instead, the goal is to use the "Hyper-V provider", while running the Vagrant commands themselves straight from Windows,  the same way as you'd use Vagrant with the VirtualBox provider (as our instructions currently say to do.)

**Greg Price** · 2021-01-08 05:14 UTC

The upstream instructions for that are here:
https://www.vagrantup.com/docs/providers/hyperv
and the pages next to that one.

The Vagrant "box" you'll probably want to use is this one:
https://app.vagrantup.com/hashicorp/boxes/bionic64

**Greg Price** · 2021-01-08 05:18 UTC

There are a couple of limitations mentioned in the docs:
https://www.vagrantup.com/docs/providers/hyperv/limitations

They don't sound like blockers. If the Hyper-V provider turns out to be noticeably faster, or otherwise nicer to use, than the VirtualBox provider, I think they'll be well worth living with.

The one about networking configuration sounds like it might potentially require some adjustments to our config to get things to work. If you run into trouble, post here with details (with copy-paste of your commands and the error messages), and we can debug.

**Diptesh Choudhuri** · 2021-01-08 05:41 UTC

To be honest, I used both methods. Using windows as the host and then used wsl as host. The WSL one was a bit more successful since it alteast got to the venv setup before failing, Using windows host mostly couldn't even boot the VM up. 

Additionally there is also the problem of Hyper V not being supported on Windows Home edition. I don't know how big of a problem this is, but I had to upgrade mine to Pro before I even got to do the actual vagrant part.

**Diptesh Choudhuri** · 2021-01-08 05:44 UTC

But I am willing to try again. What changes to the vagrantfile do you recommend I do?

**Greg Price** · 2021-01-08 05:52 UTC

Great!

I'd recommend trying it again, and then posting here with the specific obstacle you run into. Then we can investigate how to handle it :smile:

**Greg Price** · 2021-01-08 05:53 UTC

Specifically, use copy-paste to post the exact commands you're trying and the output they're giving. Use a [code block](https://zulip.com/help/format-your-message-using-markdown#code) so that the output doesn't get bits of it interpreted as Markdown formatting.

**Greg Price** · 2021-01-08 05:55 UTC

(replying to Diptesh Choudhuri)
> Additionally there is also the problem of Hyper V not being supported on Windows Home edition. I don't know how big of a problem this is, but I had to upgrade mine to Pro before I even got to do the actual vagrant part.

Hmm, yeah, that probably means we'll have to keep the VirtualBox instructions too.

But if we can get it working and it turns out to run faster, or otherwise be nicer to use, then that will be quite valuable for anyone else who's on Windows Pro (or higher.)

**Diptesh Choudhuri** · 2021-01-08 12:00 UTC

**Try 1:**
I added this to the `Vagrantfile`
```ruby
  config.vm.provider "hyperv" do |h, override|
    override.vm.box = "bento/ubuntu-16.04"
    h.linked_clone = true
    h.memory = vm_memory
    h.cpus = vm_num_cpus
  end
```
This failed due to insufficient memory:
[1.PNG](https://chat.zulip.org/user_uploads/2/a/ZDDwa7g-yDDw_8_vOPttlgoX/1.PNG)
(Additionally this about 265 seconds to download the 16.04 box and complete upto this error)

**Diptesh Choudhuri** · 2021-01-08 12:39 UTC

**Try 2:**
I changed the `Vagrantfile` to:
```ruby
  config.vm.provider "hyperv" do |h, override|
    override.vm.box = "bento/ubuntu-16.04"
    # h.linked_clone = true
    h.memory = vm_memory
    h.maxmemory = vm_memory
    h.cpus = vm_num_cpus
  end
```
This failed due to what I believe to be permission errors. I got this error yesterday too. [2.PNG](https://chat.zulip.org/user_uploads/2/cb/e6yWGD5GsXLh-xG_SC8PX23A/2.PNG)

**Diptesh Choudhuri** · 2021-01-08 12:43 UTC

After running the commands as stated above and running `vagrant destroy -f` and `vagrant up`. I got this: [3.PNG](https://chat.zulip.org/user_uploads/2/72/bzi_dV7NS_tvzTfhMcfLU-kb/3.PNG)

**Aman (amanagr)** · 2021-01-08 12:47 UTC

(replying to Rein Zustand)
> Maybe the issue should remain open, then retry a year or two later once the tech has matured?
Makes sense.

**Diptesh Choudhuri** · 2021-01-08 13:13 UTC

Alright theres some good news. Though the actual provision is still underway, but it seems like the new configuration I used has worked. 
I will wait till all of the provision is complete and report here if it works.

**Diptesh Choudhuri** · 2021-01-08 13:14 UTC

I then plan to execute `vagrant up --provider=virtualbox` and compare the time taken in the hyperv case.

**Diptesh Choudhuri** · 2021-01-08 13:50 UTC

Alright provisioning worked fine. Took 32 minutes to be exact. However I can't actually access the development server.

**Diptesh Choudhuri** · 2021-01-08 13:52 UTC

After running `./tools/run-dev.py`, I go to `localhost:9991` on chrome and it says refused to connect.

**Diptesh Choudhuri** · 2021-01-08 13:53 UTC

The ssh address of the VM booted up is ` 172.21.237.218` and when I go to ` 172.21.237.218:9991`, I get an error in JSON format.

**Diptesh Choudhuri** · 2021-01-08 13:53 UTC

```JSON
{"result":"error","msg":"Invalid subdomain","code":"NONEXISTENT_SUBDOMAIN"}
```

**Diptesh Choudhuri** · 2021-01-08 13:54 UTC

Also there seem to be requests made to the django server (in the run-dev.py) output but they all seem to 404 out.

Any pointers on what I should do?

**Diptesh Choudhuri** · 2021-01-08 13:56 UTC

Here's my `Vagrantfile`:
```ruby
  config.vm.provider "hyperv" do |h, override|
    override.vm.box = "bento/ubuntu-18.04"
    # h.linked_clone = true
    h.memory = vm_memory
    h.maxmemory = vm_memory
    h.cpus = vm_num_cpus
  end
```

**Diptesh Choudhuri** · 2021-01-08 14:08 UTC

There seems to be some pointers in [this](https://www.vagrantup.com/docs/providers/hyperv/limitations#limited-networking) section. But I can't seem to make or tails of it.

**Diptesh Choudhuri** · 2021-01-08 14:09 UTC

[4.PNG](https://chat.zulip.org/user_uploads/2/58/zJwEg3AA-m8Jqc3xbzQHKgpL/4.PNG) 
As you can see, theres no ports being forwarded and idk how to solve this...

**Greg Price** · 2021-01-09 01:27 UTC

Great, that sounds like progress!

**Greg Price** · 2021-01-09 01:29 UTC

(replying to Diptesh Choudhuri)
> After running the commands as stated above and running `vagrant destroy -f` and `vagrant up`. I got this: [3.PNG](https://chat.zulip.org/user_uploads/2/72/bzi_dV7NS_tvzTfhMcfLU-kb/3.PNG)

How did you resolve this one? Did you use the command printed there (with `mount -t cifs`), or do something else?

**Greg Price** · 2021-01-09 01:30 UTC

(replying to Diptesh Choudhuri)
> ```JSON {"result":"error","msg":"Invalid subdomain","code":"NONEXISTENT_SUBDOMAIN"} ```

That is an error from the Zulip server! So you successfully have it running, and are making HTTP requests to it and getting responses back (and from the actual Zulip application code, not from some intermediate layer like nginx.) I think this is very close.

**Greg Price** · 2021-01-09 01:36 UTC

I think the first thing to try would be to make some small tweaks in `zproject/dev_settings.py` in order to get it completely working. Take a look at this block:
```python
        # For local development environments, we use localhost by
        # default, via the "zulipdev.com" hostname.
        EXTERNAL_HOST = 'zulipdev.com:9991'
        # Serve the main dev realm at the literal name "localhost",
        # so it works out of the box even when not on the Internet.
        REALM_HOSTS = {
            'zulip': 'localhost:9991',
        }
```

Try editing `REALM_HOSTS` so that instead of `localhost:9991` it has `172.21.237.218:9991` (using the same IP address that you're able to use to get that JSON error.)

Then restart the server (or maybe it will automatically?), and I think that should resolve the NONEXISTENT_SUBDOMAIN error.

**Greg Price** · 2021-01-09 01:38 UTC

Once you have it completely working, then that's a significant accomplishment, and the next step is to write down some notes and send a docs PR so that other people are able to follow the path you found and make use of the result of this work :smile:

**Greg Price** · 2021-01-09 01:42 UTC

After that, it would be nice to avoid needing to make any edits to `dev_settings.py`. That's the part where forwarding a port would be useful to find a way to do.

Specifically you'd want to set it up so that traffic sent to port 9991 on `localhost`, aka port 9991 on 127.0.0.1, gets forwarded to port 9991 on 172.21.237.218, or in general the IP address of your VM. Then you could visit `localhost:9991` in your browser, and the request would get forwarded to the same place you're already sending it, but at the HTTP level it'd be saying it was looking for a host called `localhost`, which is what the settings in `dev_settings.py` expect.

**Greg Price** · 2021-01-09 01:44 UTC

If port forwarding turns out to be hard to do, there could also potentially be other solutions -- port forwarding itself isn't necessary. The goal that port forwarding is helpful for is to avoid having to make any ad hoc local edits like to `dev_settings.py`; and even that goal isn't absolutely necessary, it just removes a piece of friction in the way of someone using the setup.

**Diptesh Choudhuri** · 2021-01-09 06:53 UTC

(replying to Greg Price)
> (replying to Diptesh Choudhuri) ```quote After running the commands as stated above and running `vagrant destroy -f` and `vagrant up`. I got this: [3.PNG](https://chat.zulip.org/user_uploads/2/72/bzi_dV7NS_tvzTfhMcfLU-kb/3.PNG) ``` How did you resolve this one? Did you use the command printed there (with `mount -t cifs`) …
I am not sure how I did. The only difference between the previous Vagrantfile seems to be the base box. Ubuntu18 as compared to 16.

**Diptesh Choudhuri** · 2021-01-09 06:56 UTC

I have a few questions:
1. Where exactly do I add the docs for this? `setup-vagrant.md` looks like a nice place.
2. How do I setup port forwarding? Shouldn't the users have to make this change themselves since each machine might report a differnent IP address? We can't hardcode that into `dev_settings.py`. I am thinking maybe use some sort of enviroment varaible?

**Diptesh Choudhuri** · 2021-01-09 06:57 UTC

However if there is any other way to achieve this, please nudge me in the correct direction. I have absolutely no experience with networking haha.

**Diptesh Choudhuri** · 2021-01-09 07:04 UTC

Weirdly enough that did help but the dev server doesn't seem to be working as expected. 
[5.PNG](https://chat.zulip.org/user_uploads/2/a7/VedpK6OSHL9v0S10TEp2LXfz/5.PNG) 
[6.PNG](https://chat.zulip.org/user_uploads/2/d/0M43AnBgXTbIXdrUtrdInOYS/6.PNG)

**Diptesh Choudhuri** · 2021-01-10 13:38 UTC

@Greg Price please tell me what i could do next?

**Greg Price** · 2021-01-11 18:03 UTC

(replying to Diptesh Choudhuri)
> I have a few questions: 1. Where exactly do I add the docs for this? `setup-vagrant.md` looks like a nice place.

Sure -- either there or as a new section in https://zulip.readthedocs.io/en/latest/development/setup-advanced.html (it says "non-Vagrant" now, but might make sense to generalize it to just "advanced setup").

It's easy to move the text around, so just go with something and it might get changed while merging.

> Shouldn't the users have to make this change themselves since each machine might report a differnent IP address? We can't hardcode that into `dev_settings.py`.

Right, that's why it would be nicer to not have to write down the IP address there :smile: 

I don't know how to set up port forwarding on Windows -- I'd start by googling [port forwarding windows](https://www.google.com/search?q=port+forwarding+windows). Maybe plus "vagrant" in that query.

**Greg Price** · 2021-01-11 18:06 UTC

(replying to Diptesh Choudhuri)
> [6.PNG](https://chat.zulip.org/user_uploads/2/d/0M43AnBgXTbIXdrUtrdInOYS/6.PNG)

Hmm, I'm not sure what to make of this. Those failed requests don't look like anything from Zulip -- "vendors" in particular doesn't sound like any request that Zulip would make.

**Greg Price** · 2021-01-11 18:07 UTC

I kind of wonder if you have perhaps a browser extension that's doing that activity?

**Greg Price** · 2021-01-11 18:08 UTC

What does the JS console say?

**Greg Price** · 2021-01-11 18:08 UTC

Also: what was the exact setup that you did in order to get to that point?

**Diptesh Choudhuri** · 2021-01-17 02:57 UTC

@Greg Price  Sorry for replying so late, I got busy with stuff.

> Right, that's why it would be nicer to not have to write down the IP address there

I couldn't find anything which could be useful to tackle our situation here. However, I do have a solution that should work. 

Instead of hardcoding the value of `REALM_HOSTS` in `dev_settings.py`, we could load it like this: 

```python
REALM_HOSTS = {
            'zulip': os.environ.get('ZULIP_REALM_HOST', 'localhost:9991'),
        }
```
And then in the case of HyperV provider, we can run a custom provisioner which will set this environment variable (possibly by writing to `/etc/profile.d/set-zulip-variables.sh`). This way we won't end up breaking any existing code we have.

> Also: what was the exact setup that you did in order to get to that point?

Should I make a PR for this to the docs so that you can try it out yourself? There are also a few additions to `Vagrantfile` itself that I had to make.

**Diptesh Choudhuri** · 2021-01-17 03:36 UTC

> What does the JS console say?

Good question. When I open the JS console, it seems like it is making requests to the wrong server for static files.
[7.PNG](https://chat.zulip.org/user_uploads/2/4e/0_2mWPKsgeKpsWOo1LLq9pF4/7.PNG) 

This leads me to believe there is some other setting I will have to change to get this to work (currently, only made the change to `REALM_HOSTS`) as you mentioned. I couldn't find anything else in `dev_settings.py`. Where should I look for it?

**Diptesh Choudhuri** · 2021-01-17 03:41 UTC

Looking into it a bit more, these errors are being generated by only those files which are being served by webpack.

**Diptesh Choudhuri** · 2021-01-17 03:53 UTC

I tried to make some changes to `webpack.config.ts` but that doesn't seem to work. I don't have a clue how to proceed now.

**Diptesh Choudhuri** · 2021-01-19 18:14 UTC

@Greg Price Could you help me in the issue I described above? I'm deadlocked and don't know how to proceed.

**Greg Price** · 2021-01-20 03:38 UTC

(replying to Diptesh Choudhuri)
> > What does the JS console say? Good question. When I open the JS console, it seems like it is making requests to the wrong server for static files. [7.PNG](https://chat.zulip.org/user_uploads/2/4e/0_2mWPKsgeKpsWOo1LLq9pF4/7.PNG)

Aha -- yeah, I agree with that interpretation. It looks like it's trying to talk to `localhost:9991` instead of the appropriate IP address.

**Greg Price** · 2021-01-20 03:40 UTC

I tried a quick search for `localhost` in the `zproject/` directory, which is where all the settings live. This bit looks quite suspicious:
```
$ rg -C4 localhost zproject/
zproject/computed_settings.py
…
531-if PRODUCTION or IS_DEV_DROPLET or os.getenv('EXTERNAL_HOST') is not None:
532-    STATIC_URL = urljoin(ROOT_DOMAIN_URI, '/static/')
533-else:
534:    STATIC_URL = 'http://localhost:9991/static/'
```

**Greg Price** · 2021-01-20 03:40 UTC

Hmm, though that's not totally satisfying because the URLs it's trying and failing to talk to don't have `/static/` in the path -- instead the paths start with `/webpack/`.

**Greg Price** · 2021-01-20 03:42 UTC

Ah, but this explains that part:
```
$ rg -wC4 webpack zproject/
zproject/computed_settings.py
...
564-WEBPACK_LOADER = {
565-    'DEFAULT': {
566-        'CACHE': not DEBUG,
567:        'BUNDLE_DIR_NAME': '../webpack/' if DEBUG else 'webpack-bundles/',
568-        'STATS_FILE': os.path.join(DEPLOY_ROOT, WEBPACK_STATS_FILE),
569-    },
570-}
```

So that value for `BUNDLE_DIR_NAME` would cause `http://localhost:9991/static/` to turn into `http://localhost:9991/webpack/`.

**Greg Price** · 2021-01-20 03:43 UTC

@Diptesh Choudhuri I suspect that if you edit that `STATIC_URL` definition so that it uses the appropriate IP address instead of `localhost`, that things will work. Or at least that you'll get past this current issue.

**Greg Price** · 2021-01-20 03:47 UTC

I'm also not sure why the `localhost` case is there in the first place -- why we don't unconditionally do the ROOT_DOMAIN_URI thing.

@Anders Kaseorg do you think we could make a version of that work unconditionally? I see in zulip/zulip@99242138a you added the conditional, as part of making that URL an absolute one.

**Greg Price** · 2021-01-20 03:51 UTC

Then in zulip/zulip@e47e1cd64 we added the IS_DEV_DROPLET part of the condition, to fix basically exactly this same problem for the case of a droplet.

**Greg Price** · 2021-01-20 03:54 UTC

Oh, here's another thing you might try: setting `EXTERNAL_HOST`. This is usually done as an environment variable; you can do it with these instructions:
https://zulip.readthedocs.io/en/latest/development/remote.html#setting-up-the-development-environment

**Diptesh Choudhuri** · 2021-01-20 05:45 UTC

Yay it all works now! Thank you so much @Greg Price ! 
I am all ready to make a PR for this. However there are a few settings I had to change in the the `computed_settings.py` and `dev_settings.py` for this to work. What should I do? Loading them in via environment variables and using a fallback when these environment variables don't exists sounds like a good idea. Please tell me how I should proceed there.

Meanwhile I will start adding the relevant stuff to the docs.

**Greg Price** · 2021-01-20 05:47 UTC

Great! :tada: 

I think a good place to start would be to just post the exact changes you had to make. Then we can work out how best to handle them in the code.

**Greg Price** · 2021-01-20 05:48 UTC

One possibility would be to say that you need to set EXTERNAL_HOST (is that one of the things you did?) as an environment variable, and then fix the code as necessary so that everything works, using that as the source of data on what the relevant IP address is.

**Greg Price** · 2021-01-20 05:49 UTC

(But whether that's a good idea for all the needed changes will depend on exactly what they are.)

**Diptesh Choudhuri** · 2021-01-20 05:53 UTC

In `Vagrantfile`:
```ruby
  config.vm.provider "hyperv" do |h, override|
    override.vm.box = "bento/ubuntu-18.04"
    h.memory = vm_memory
    h.maxmemory = vm_memory
    h.cpus = vm_num_cpus
  end
```

In `zproject\computed_settings.py`:
```python
# line number: 534
 STATIC_URL = 'http://172.21.142.130:9991/static/'
```

In `zproject\dev_settings.py`:
```py
# line number: 33
REALM_HOSTS = {
            'zulip': '172.21.142.130:9991',
}
```
The value `'172.21.142.130'` seems to change (not sure about this though), but it can be found easily by running `hostname -I` in the virtual machine.
Additionally, I plan to add docs to `docs\development\setup-advanced.md`.

Now that I see the number of changes I had to make, they don't seem all that large, but damn it took a long time.

**Greg Price** · 2021-01-20 06:10 UTC

(replying to Diptesh Choudhuri)
> Now that I see the number of changes I had to make, they don't seem all that large, but damn it took a long time.

Yeah, sometimes that's how development goes :laughter_tears:

**Greg Price** · 2021-01-20 06:11 UTC

Cool, so for both of those settings changes I think the right path will be to make them based on EXTERNAL_HOST.

**Greg Price** · 2021-01-20 06:12 UTC

So I'd suggest revising them so that they just use EXTERNAL_HOST (and no longer have to include your specific IP address in the code), and have the docs say to be sure to set EXTERNAL_HOST when running the dev environment this way.

**Greg Price** · 2021-01-20 06:15 UTC

In PR review you might get some feedback suggesting different ways to write the settings logic, particularly to make sure it all continues to work well for people running in different environments. I'm not an expert in this area and I'm not sure what all the right conditions will be.

But I think ultimately we'll want it to be that, at least in this particular environment, those two settings end up getting their information from EXTERNAL_HOST.

**Diptesh Choudhuri** · 2021-01-20 14:04 UTC

(replying to Greg Price)
> So I'd suggest revising them so that they just use EXTERNAL_HOST (and no longer have to include your specific IP address in the code), and have the docs say to be sure to set EXTERNAL_HOST when running the dev environment this way.
Instead of requiring our users to set this environment variable themselves, can we not instead just run a custom provision script for HyperV which sets an environment variable? That way they don't have to run an `export EXTERNAL_HOST` everytime they run `./tools/run-dev.py` in a new shell?

**Diptesh Choudhuri** · 2021-01-20 14:35 UTC

Alright, looks like the changes to either of the settings file (mentioned above) are not required. Instead we can simply run `export EXTERNAL_HOST="$(hostname -I | xargs):9991"` (the `xargs` is necessary to trim some whitespaces), then `./tools/run-dev.py` and then go to `http://host-ip-number:9991/` to access the zulip dev website.

**Greg Price** · 2021-01-20 20:08 UTC

(replying to Diptesh Choudhuri)
> Instead of requiring our users to set this environment variable themselves, can we not instead just run a custom provision script for HyperV which sets an environment variable? That way they don't have to run an `export EXTERNAL_HOST` everytime they run `./tools/run-dev.py` in a new shell?

Yeah, I think a good followup would be to try to find a way to automate that part too.

But having instructions to make it all work just by setting EXTERNAL_HOST will be a great step forward, and then anything we do to automate setting EXTERNAL_HOST can build on top of that.

**Greg Price** · 2021-01-20 20:12 UTC

(replying to Diptesh Choudhuri)
> Alright, looks like the changes to either of the settings file (mentioned above) are not required. Instead we can simply run `export EXTERNAL_HOST="$(hostname -I | xargs):9991"` (the `xargs` is necessary to trim some whitespaces), then `./tools/run-dev.py` and then go to `http://host-ip-number:9991/ …

Great!

I'm... kind of confused why that already works, in particular for the STATIC_URL part. It looked like that code would result in sending the requests to `http://localhost:9991/…`. But if it does already work, then that's handy.

**Diptesh Choudhuri** · 2021-01-21 09:47 UTC

@Greg Price  I made a PR at https://github.com/zulip/zulip/pull/17098. Could someone please review it?

**Diptesh Choudhuri** · 2021-01-23 07:59 UTC

@Greg Price Could you please review the PR I made? Or if you are not available for that, could you refer me someone who could review it instead?

**Greg Price** · 2021-01-25 22:53 UTC

Thanks, that PR looks great! Left a few comments.

**Diptesh Choudhuri** · 2021-01-26 12:53 UTC

Thanks @Greg Price for the comments. I fixed them and pushed a commit. Could you please take a look at that?

**Diptesh Choudhuri** · 2021-01-26 13:05 UTC

As you said in the review comments of #17098, I opened an issue for the bug but I am unable to claim the issue for myself since I am a new contributor. Could someone please assign me https://github.com/zulip/zulip/issues/17125?

**Diptesh Choudhuri** · 2021-01-27 10:00 UTC

@Greg Price I made the changes as you requested. Could you please review them again?


## password

*2019-04-04 to 2019-07-04 · 7 messages · [open in Zulip](https://chat.zulip.org/#narrow/channel/18-tools/topic/password/with/728023)*

**Matteo Sanguin** · 2019-04-04 13:28 UTC

voglio capire cosa significa

**Matteo Sanguin** · 2019-04-04 13:28 UTC

test

**Matteo Sanguin** · 2019-04-04 13:28 UTC

bella storia

**Matteo Sanguin** · 2019-04-04 13:28 UTC

mah

**Matteo Sanguin** · 2019-04-04 13:29 UTC

ok ok 
okok

**Matteo Sanguin** · 2019-04-04 13:29 UTC

d :neutral:

**Abdul Fatah** · 2019-07-04 04:10 UTC

test


## alert

*2020-03-10 to 2020-03-10 · 35 messages · [open in Zulip](https://chat.zulip.org/#narrow/channel/18-tools/topic/alert/with/829118)*

**Yash RE** · 2020-03-10 04:57 UTC

Okay, so recently I came across this trick, were you could type `sleep 2; alert` and alert would cause a pop up to appear which let's you know sleep 2 has ended, I see a lot of potential utility with eg `./tools/lint` and `./test-js-with..`

I'll admit that I don't actually test local much and use CI to run my tests because I can just push and wait to see if it works despite the obvious draw back that CI takes 20 mins a pop sometimes. Having an option like the above in place would make it much easier for me to rely on local testing and linting rather than throwing jobs at CI.

now, the problem here is: I can't use `alert` from vagrant, it doesn't work.
I tried installing `libnotify-bin`, which is a package vagrant machine is missing, and using `alert` but it didn't work.
I then found a plug in called `vagrant-notify` but that didn't work and I've realized that I'm out of my depths here since I don't know our vagrant set up well enough to actually change/fix the problems I'm having

**Anders Kaseorg** · 2020-03-10 05:18 UTC

I don’t know what `alert` is, but it sounds like something that needs to run on the host, not the Vagrant guest. So, on the host, you can do `vagrant ssh -c 'tools/lint'; alert`.

**Greg Price** · 2020-03-10 05:40 UTC

That sounds right to me.

**Yash RE** · 2020-03-10 05:41 UTC

wow, that'll work :tada: (only small caveat being that I won't be able to see the log... but that's okay.)
Thanks Anders!

Time to go set up the aliases:
`lint = "vagrant ssh -c  './tools/lint';alert"`
`test = "vagrant ssh -c  './tools/test-js-with-node';alert"`

**Yash RE** · 2020-03-10 05:41 UTC

uhhhh... wait. hold on... that doesn't give me the right exit code on test failure, so it won't work right with `test` because I won't know if I have success or fail... so, not super useful.

**Greg Price** · 2020-03-10 05:42 UTC

I'm now curious where your `alert` command comes from!

Because... I recently rediscovered where I had an `alert` command that works exactly like that (right down to depending on `libnotify-bin`), as an alias in my `.bashrc`, which I have had there since before I put my dotfiles into source control in 2013.

**Greg Price** · 2020-03-10 05:44 UTC

It should, unless `vagrant ssh` is unhelpfully swallowing the exit code.

**Anders Kaseorg** · 2020-03-10 05:46 UTC

`vagrant ssh` passes along the exit code from the inner command. (Did you try it?)

**Yash RE** · 2020-03-10 05:46 UTC

uhhh, no I did not try it, I was just thinking

**Yash RE** · 2020-03-10 05:46 UTC

if it works then this is perfect

**Yash RE** · 2020-03-10 05:46 UTC

I will go test

**Anders Kaseorg** · 2020-03-10 05:47 UTC

(I would not recommend overwriting the `test` shell builtin, though.)

**Yash RE** · 2020-03-10 05:48 UTC

So, if you want to know what alert does, here's a small gif... the pop up box is extremely truncated, but you can see it's there... I could have switched screens or anything and it would have still told me that the command had finished.
[running alert](https://chat.zulip.org/user_uploads/2/32/CrG9-1n0pQAltzj2h90UQFgM/alert-from-desktop.gif)

**Yash RE** · 2020-03-10 05:50 UTC

> (I would not recommend overwriting the `test` shell builtin, though.)
I'll go with just `t` then, didn't realize there was a builtin for `test`.

**Yash RE** · 2020-03-10 05:51 UTC

> I'm now curious where your `alert` command comes from!
I do not understand the question here, are you asking where I got the idea of using `alert` from?

**Anders Kaseorg** · 2020-03-10 05:53 UTC

No, like, there isn’t an `alert` command in the entire Ubuntu repository.

**Yash RE** · 2020-03-10 06:15 UTC

uh.. I just had `alert`, I don't know when or where I got it from... I only know the name `libnotify-bin` from the error that vagrant gives when I try and run `alert` from within the shell

**Anders Kaseorg** · 2020-03-10 06:24 UTC

Oh I see. It’s a shell alias defined in Ubuntu’s default `~/.bashrc`.

**Yash RE** · 2020-03-10 06:29 UTC

I found out about the existence of `alert` a few days ago, I was searching for tips and aliases to improve productivity :)

**Yash RE** · 2020-03-10 06:38 UTC

Aah, okay, this explains a lot https://askubuntu.com/questions/423646/use-of-default-alias-alert:
`notify-send --urgency=low -i "$([ $? = 0 ] && echo terminal || echo error)" "$(history|tail -n1|sed -e '\''s/^\s*[0-9]\+\s*//;s/[;&|]\s*alert$//'\'')"`

**Yash RE** · 2020-03-10 06:52 UTC

[That pop up tells me that the test failed](https://chat.zulip.org/user_uploads/2/a4/Z2_AzqRggzt7hUYZfn0F28Ut/alert-for-test-fail.gif)

**Greg Price** · 2020-03-10 06:53 UTC

(replying to Anders Kaseorg)
> Oh I see. It’s a shell alias defined in Ubuntu’s default `~/.bashrc`.

Aha! That must be where it got into my own `~/.bashrc` from, then. Good to know :slight_smile:

**Greg Price** · 2020-03-10 06:55 UTC

FWIW here's the version I cleaned it up into (and fixed to work on Debian with GNOME) after rediscovering it recently:
```bash
# Show a desktop notification; useful after a long-running command.
#
# Use like so: `some_long_command ; alert`.  Shows the command line,
# and a "terminal" icon on success or "warning" on failure.
#
# Example:
#   $ echo foo; sleep 1; alert
#
# Requires `notify-send`, e.g. from `apt install libnotify-bin`.
# The icon names used should exist inside /usr/share/icons/; those
# below are supplied by at least GNOME.
alert () {
    local failure="$?" icon text
    (( failure )) && icon=dialog-warning || icon=utilities-terminal
    text="$(fc -ln -0 | perl -pe 's/[;&|] \s* alert $//x')"
    notify-send --icon="${icon}" "${text}"
}
```

**Greg Price** · 2020-03-10 06:56 UTC

I definitely remember finding it useful sometimes in the past.

**Greg Price** · 2020-03-10 06:58 UTC

(The fix required for Debian, at least as installed on my laptop and desktop, which I think reflect the default here, is just that the icon names in the original don't exist, so I picked new icons.)

**Yash RE** · 2020-03-10 07:25 UTC

`perl -pe '..` :rolling_on_the_floor_laughing: 

throw back to #**learning>perl one-liners**

**Yash RE** · 2020-03-10 07:33 UTC

I really hope this conversation can be useful to other contributors too. Especially if you've been reluctant to use local tests/lints this could make that easier for you.

**Greg Price** · 2020-03-10 07:37 UTC

(replying to Yash RE)
> throw back to #**learning>perl one-liners**
Indeed. :slight_smile:

It's doing much the same job there as `sed` does in the original. (The first half of what `sed` does is stripping off a number, which my version obviates by having `fc` not print in the first place. The second half corresponds directly to that `perl -pe` command.)

Use of `sed` is still fairly common in old-fashioned shell scripts and one-liners, for many of the same things Perl one-liners are good for. But Perl makes simple things equally simple, and keeps things much saner as the problem gets even a little complex, so I generally just always use `perl` instead.

**Anders Kaseorg** · 2020-03-10 07:46 UTC

In this case, there’s a pure `bash` version with an even longer run of inexplicable punctuation: `text="$(fc -ln -0)"; text="${text%[;&|]*( )alert}"`. (May require `shopt -s extglob`.)

**Yash RE** · 2020-03-10 08:05 UTC

another minor convenience thing, is it possible to execute a command right after `vagrant ssh` and stay in the shell? (so like `-c` but without exiting)
eg, I almost always go `vagrant ssh`, `clear`, `./tools/run-dev.py` and would like to alias the process

**Greg Price** · 2020-03-10 08:09 UTC

(replying to Anders Kaseorg)
> In this case, there’s a pure `bash` version with an even longer run of inexplicable punctuation: `text="$(fc -ln -0)"; text="${text%[;&|]*( )alert}"`. (May require `shopt -s extglob`.)

Neat!

FWIW `shopt extglob` tells me I have it set, and I don't see it mentioned in my dotfiles or in `/etc/bash.bashrc` or `/etc/profile{,.d/}`. So perhaps it's the default? ... With at least the build of `bash` shipped by Debian.

**Anders Kaseorg** · 2020-03-10 08:10 UTC

You often get it enabled by `bash-completion`, I think.

**Greg Price** · 2020-03-10 08:11 UTC

Aha, yeah, that's it.

**Anders Kaseorg** · 2020-03-10 08:12 UTC

@Yash RE You could `vagrant ssh -c 'clear; tools/run-dev.py; bash -l'`.

**Yash RE** · 2020-03-10 08:14 UTC

sweet! thanks!


## populate with messages

*2020-06-22 to 2020-06-23 · 7 messages · [open in Zulip](https://chat.zulip.org/#narrow/channel/18-tools/topic/populate.20with.20messages/with/911213)*

**Kaustubh Nair** · 2020-06-22 15:31 UTC

Is there an easy way to populate the db with unread messages?

**Tim Abbott** · 2020-06-22 19:47 UTC

@Kaustubh Nair yes, `manage.py mark_all_messages_unread`.

**Tim Abbott** · 2020-06-22 19:47 UTC

Will take whatever messages you have and make them all unread messages.

**Cyphase** · 2020-06-22 19:48 UTC

This seems like what you want: https://zulip.readthedocs.io/en/latest/subsystems/pointer.html#testing-and-development

**Cyphase** · 2020-06-22 19:49 UTC

Although that document will probably change soon once the pointer is fully gone.

**Tim Abbott** · 2020-06-22 19:51 UTC

Yep!  We try to link that in a bunch of relevant places, and one of the remaining projects for the pointer work is to rewrite that document for the pointer-free world.

**Kaustubh Nair** · 2020-06-23 08:49 UTC

Great, that helps. Thanks!


## Swagger UI

*2020-11-17 to 2020-11-17 · 2 messages · [open in Zulip](https://chat.zulip.org/#narrow/channel/18-tools/topic/Swagger.20UI/with/1064206)*

**Rekha Jayaram** · 2020-11-17 00:55 UTC

Hi, Is there a swagger UI url that I can hit to test the API endpoints? I was hoping to authenticate and then be able to use the Swagger UI to try out the API endpoints

**Tim Abbott** · 2020-11-17 02:07 UTC

@Rekha Jayaram there isn't a hosted version at present, though it's pretty easy to upload `zerver/openapi/zulip.yaml` to https://editor.swagger.io/ and do what you describe.


## tools/build_pygments_data

*2020-11-17 to 2020-11-18 · 12 messages · [open in Zulip](https://chat.zulip.org/#narrow/channel/18-tools/topic/tools.2Fbuild_pygments_data/with/1064324)*

**Sumanth Rao** · 2020-11-17 01:58 UTC

This error in the generated pygments data in `static/generated/pygments_data.json` caught my attention. 

```
"juttle": {"priority": {"priority": 0, "pretty_name": "Juttle"}, "pretty_name": "Juttle"}
```

while we should actually expect 

```
"juttle": {"priority": 0, "pretty_name": "Juttle"}
```

**Sumanth Rao** · 2020-11-17 01:58 UTC

It seems the cause of this, is because the aliases for the language `Juttle` occurs twice in the tuple resulting from `get_all_lexers()`. Here's a small snippet to reproduce.

``` python3
In [15]: from pygments.lexers import get_all_lexers

In [16]: lexers = get_all_lexers()

In [17]: {alias[0]: alias[1] for alias in lexers}.get('Juttle')
Out[17]: ('juttle', 'juttle')
```

**Sumanth Rao** · 2020-11-17 02:00 UTC

Most likely this is a bug in upstream pygments/ python-pygments wrapper. If so, should we open an issue for it? FYI @Anders Kaseorg , I observed this when looking at your recent PR #16755

**Anders Kaseorg** · 2020-11-17 02:01 UTC

It wasn’t introduced by my change; I checked that the output was bitwise identical.

**Sumanth Rao** · 2020-11-17 02:02 UTC

Yeah, it seems to have existed in the previous output as well, through I only observed it now.

**Anders Kaseorg** · 2020-11-17 02:02 UTC

The problem is that constructing `langs` via incremental type-shifting mutation was not a good plan.

**Sumanth Rao** · 2020-11-17 02:03 UTC

Yeah, we should just build a new dict, instead of incrementally replacing the same.

**Anders Kaseorg** · 2020-11-17 02:12 UTC

#16757

**Sumanth Rao** · 2020-11-17 03:00 UTC

Filed this in pygments issue tracker - https://github.com/pygments/pygments/issues/1604

**Anders Kaseorg** · 2020-11-17 03:04 UTC

Want to send a PR? Should be easy.

**Sumanth Rao** · 2020-11-17 12:54 UTC

Yup https://github.com/pygments/pygments/pull/1606 :)

**Tim Abbott** · 2020-11-18 20:45 UTC

Thanks for submitting the upstream fix!


## tornado error

*2020-12-30 to 2020-12-30 · 1 messages · [open in Zulip](https://chat.zulip.org/#narrow/channel/18-tools/topic/tornado.20error/with/1090149)*

**Notification Bot** · 2020-12-30 15:13 UTC

This topic was moved by @Vishnu KS to #**development help>tornado error**


## wsl dev error

*2020-12-30 to 2020-12-30 · 4 messages · [open in Zulip](https://chat.zulip.org/#narrow/channel/18-tools/topic/wsl.20dev.20error/with/1090157)*

**Jenish** · 2020-12-30 15:38 UTC

[image.png](https://chat.zulip.org/user_uploads/2/ea/_nd8fg0wLO1SUWOmU0-QRVGj/image.png) 
error in wsl mode

**Aman (amanagr)** · 2020-12-30 15:42 UTC

@Jenish try running `./tools/wsl/start_services` then provision.

**Jenish** · 2020-12-30 15:43 UTC

okay

**Jenish** · 2020-12-30 15:44 UTC

(replying to Aman Agrawal)
> @Jenish try running `./tools/wsl/start_services` then provision.
Thanks


## chokidar error when running dev server

*2021-03-16 to 2021-03-28 · 14 messages · [open in Zulip](https://chat.zulip.org/#narrow/channel/18-tools/topic/chokidar.20error.20when.20running.20dev.20server/with/1133736)*

**Riken Shah** · 2021-03-16 18:53 UTC

When running dev server (`tools/run-dev.py --interface=''`), It shows a lot of chokidar errors.
For eg: (This is just the last few lines there are approx more than 200-500 lines)
```bash
Error from chokidar (/home/riken/zulip): Error: ENOSPC: System limit for number of file watchers reached, watch '/home/riken/zulip/webpack.config.ts'
Error from chokidar (/home/riken/zulip): Error: ENOSPC: System limit for number of file watchers reached, watch '/home/riken/zulip/yarn.lock'
Error from chokidar (/home/riken/zulip/static/generated): Error: ENOSPC: System limit for number of file watchers reached, watch '/home/riken/zulip/static/generated'
Error from chokidar (/home/riken/zulip/static/generated): Error: ENOSPC: System limit for number of file watchers reached, watch '/home/riken/zulip/static/generated/pygments_data.json'
```
Running on Ubuntu 18.04.5 LTS on GCP with 4 vCPUs, 4 GB memory (e2-highcpu-4 ) VM.

Because of this, I've to manually restart the server whenever I make any change to frontend files.

**Greg Price** · 2021-03-16 20:25 UTC

Thanks for the report! That sounds pretty annoying.

**Greg Price** · 2021-03-16 20:25 UTC

I think you're seeing this issue (or something closely related):
https://webpack.js.org/configuration/watch/#not-enough-watchers

**Greg Price** · 2021-03-16 20:26 UTC

Fortunately the fix is pretty simple: run `echo fs.inotify.max_user_watches=524288 | sudo tee -a /etc/sysctl.conf && sudo sysctl -p`.

**Greg Price** · 2021-03-16 20:28 UTC

And then if that fixes it, we should probably put that somewhere so that others don't have to deal with it in the future :smile: How did you set up the VM you're using? I haven't interacted with Zulip dev VMs in GCP.

**Riken Shah** · 2021-03-16 20:55 UTC

Thanks, Greg. That worked!
>How did you set up the VM you're using?

It was a pretty simple process, I followed this [guide](https://zulip.readthedocs.io/en/latest/development/setup-advanced.html#installing-directly-on-ubuntu-debian-centos-or-fedora) on direct installation on Ubuntu. I've also created a simple bash script that will configure my GitHub account and handle installation so I don't have to rewrite every command again whenever I change VM.

Fun Fact:
I've been using GCP for the last 2 months, and my total bill so far is zero $. 
> How?

Actually, GCP provides free $300 credits for 3-moths to the new user. So wherever my trial period gets over, I create a new google account :grimacing:. (PRO TIP: You can use the same credit card, again and again, with multiple accounts.)

**Tim Abbott** · 2021-03-16 21:07 UTC

https://github.com/zulip/zulip/issues/12565 is relevant.

**Greg Price** · 2021-03-17 01:03 UTC

Indeed. It'd be good to merge a fix like that one, then :smile:

**Greg Price** · 2021-03-17 01:06 UTC

It looks like the existing #12637 should solve the problem just fine on any environment that's a full VM with its own kernel (vs. a container) -- and in a container it should be harmless except the `sysctl` command will fail.

Since we haven't developed a fuller solution in the couple of years since, then, perhaps we should merge that and just swallow failures in the `sysctl` command. That'd have solved the problem for @Riken Shah (Riken-Shah) .

**Greg Price** · 2021-03-17 01:06 UTC

(Or if there's an easy clean way to check in advance whether `sysctl` is supposed to work, we can do that and then not swallow failures.)

**Greg Price** · 2021-03-17 01:12 UTC

The thing about this issue is that unless you've seen basically the exact same issue before, it is super confusing to debug. And as long as it's present, it's quite a blocker to doing anything. So I think it's worth merging a fix even if the fix is slightly messy or incomplete.

**Ganesh Pawar (ganpa3)** · 2021-03-17 04:48 UTC

I think merging #12637 with a check for containers seems fine.

**Tim Abbott** · 2021-03-17 19:53 UTC

@Anders Kaseorg want to make a call on this?  I could also imagine our trying to check if we're inside a container, and for now do nothing in that case but for the future perhaps document something for the user to do on their host?

**Priyam Seth (Signior-X)** · 2021-03-28 07:40 UTC

(replying to Riken Shah (Riken-Shah))
> When running dev server (`tools/run-dev.py --interface=''`), It shows a lot of chokidar errors. For eg: (This is just the last few lines there are approx more than 200-500 lines) ```bash Error from chokidar (/home/riken/zulip): Error: ENOSPC: System limit for number of file watchers reached, watch ' …
Just FYI, this system limit for number of file watchers is a very common issue, and it comes just one time for a user, and after you extend the limit, it doesn't come again. I haven't faced this yet on Zulip. Maybe because I set it when I was working on a project using React.js


## navigate is not defined error - for integration screenshots

*2021-03-28 to 2021-03-29 · 5 messages · [open in Zulip](https://chat.zulip.org/#narrow/channel/18-tools/topic/navigate.20is.20not.20defined.20error.20-.20for.20integration.20screenshots/with/1145983)*

**Zixuan James Li** · 2021-03-28 22:11 UTC

I tried to run `./tools/generate-integration-docs-screenshot --integration bitbucket` to generate a screenshot for bitbucket's documentation, but it gives me the following error:
```
Error: Evaluation failed: ReferenceError: navigate is not defined
  at __puppeteer_evaluation_script__:1:17
  ...
  File "./tools/generate-integration-docs-screenshot", line 195, in capture_last_message_screenshot
    subprocess.check_call(["node", screenshot_script, message_id, image_path])
  File "/usr/lib/python3.8/subprocess.py", line 364, in check_call
    raise CalledProcessError(retcode, cmd)
subprocess.CalledProcessError: Command '['node', '/home/pig208/zulip/tools/message-screenshot.js', '106', 
'static/images/integrations/bitbucket/002.png']' returned non-zero exit status 1.
```
And this is the line of JS code where things go wrong
```
await page.evaluate(() => navigate.up());
```
But if I comment this line, everything just works fine. Does anyone else encounter the same issue?

**Zixuan James Li** · 2021-03-28 22:12 UTC

The files related are `tools/message-screenshot.js` and `tools/generate-integration-docs-screenshot`.

**Zixuan James Li** · 2021-03-28 22:16 UTC

I just found that it has been solved 2 days ago in this commit https://github.com/zulip/zulip/commit/62c5782f66bf6136d313ed98fdd72ba528454a52.

**Tim Abbott** · 2021-03-29 00:16 UTC

Yep!  One reason to rebase to upstream/master before starting any development project -- usually that results in less bugs :)

**Zixuan James Li** · 2021-03-29 00:23 UTC

That's so true. I guess I still need to get used to it. :joy:


## virtualenv on macos

*2021-04-03 to 2021-04-03 · 5 messages · [open in Zulip](https://chat.zulip.org/#narrow/channel/18-tools/topic/virtualenv.20on.20macos/with/1152144)*

**Ken Clary** · 2021-04-03 01:55 UTC

what actually depends on having the venv in /srv? (due to vagrant-on-bigsur issues, trying to manually install on OSX) I don't have a /srv and OSX is very stubborn about stopping me from creating one.

**Anders Kaseorg** · 2021-04-03 02:09 UTC

I don’t think we expect manual install to be possible directly on a non-Linux system; you’ll almost certainly need some kind of Linux container or VM.

**Rein Zustand** · 2021-04-03 02:32 UTC

Definitely not recommended. Also, prior attempt on macOS: https://chat.zulip.org/#narrow/stream/65-checkins/topic/Aman.20Agrawal/near/970375

**Tim Abbott** · 2021-04-03 05:14 UTC

FWIW, back in 2013 we did support installing directly on a Mac -- it involved a very long wiki page explaining how to install all of our dependencies.

**Tim Abbott** · 2021-04-03 05:15 UTC

@Ken Clary a better option if you don't have working virtualization is https://zulip.readthedocs.io/en/latest/development/remote.html.  (We have a system that'll make a remote Linux VM for folks).  @Vishnu KS or @Rohitt Vashishtha can make one for you.


## #15964 - Remove redundant yarn cache

*2021-04-25 to 2021-05-03 · 18 messages · [open in Zulip](https://chat.zulip.org/#narrow/channel/18-tools/topic/.2315964.20-.20Remove.20redundant.20yarn.20cache/with/1168877)*

**Riken Shah** · 2021-04-25 11:05 UTC

I have been working on #15964 - Avoid leaking huge amounts of disk in the yarn cache in old production servers.

I have some doubts:
- Is the [6 months or older time period to delete files under `~/.cache/yarn/v6`](https://github.com/zulip/zulip/issues/15964#issue-667436153) fixed Or Should we use [`threshold_days` argument](https://github.com/zulip/zulip/blob/ebe822341d7eb4d1e9982694719612800e989551/scripts/lib/zulip_tools.py#L67)? (By default it is 14 days but if it's too low, we can add a check that it should be at least greater than a month.)
- If we delete the old files, It'd not affect the dev environment, right? 
- One thing I found strange is, that my VM is around a month old but it still detected some files that had `mtime` older than 6 months?

I have created [WIP PR](https://github.com/zulip/zulip/pull/18259) and would really appreciate a review.

**Tim Abbott** · 2021-04-25 16:38 UTC

@Riken Shah (Riken-Shah) we probably want to use `threshold_days` as a parameter name, even if we want a different default.

**Tim Abbott** · 2021-04-25 16:40 UTC

The `mtime` detail is interesting -- it's very possible that `yarn` is doing something fancy with `mtime` itself; if so, then we may be unable to useless clean "old" cache items and the only thing we can do is remove the old-version format directories.  Can you post the timestamp you have for a specific file in that category?  We can then check if it's the same for other folks.

**Riken Shah** · 2021-04-26 10:09 UTC

> Can you post the timestamp you have for a specific file in that category? We can then check if it's the same for other folks.

Actually, when I was testing I forget to add the `--dry-run` argument and it deleted those files, even after running `yarn install` I can't seem to find such files. 

Can someone help me here?

If your dev environment is not older than six months,  run the following commands,
```bash
tools/fetch-pull-request 18259
tools/provision # Not Necessary
python3 scripts/lib/clean_yarn_cache.py --dry-run
```
If you see the output with `Cleaning unused yarn cache: /home/$USER/yarn/v6/...`,
Run `date -r {file_path} "+%s" ` to get the timestamp and send the message with `file_path` and their `timestamp` here.

**Riken Shah** · 2021-04-26 15:30 UTC

I think so we need to avoid deleting the old files as, 

> [Deleting individual files from the Yarn cache is not safe. If you delete half of the files in a cached package, the next yarn install will install half of that package.](https://github.com/zulip/zulip/pull/18259#pullrequestreview-644186128)

Then should we only go with deleting old-version format directories?

**Tim Abbott** · 2021-04-26 17:02 UTC

@Riken Shah (Riken-Shah) yeah, that sounds right.

**Tim Abbott** · 2021-04-26 23:31 UTC

OK, so I've merged the simplified #18259, which just removes the old version cache directories.

**Tim Abbott** · 2021-04-26 23:32 UTC

It's still the case that the `v6` directory can grow to like 6GB; for comparison, 1.1GB or so is how big that it is after a fresh installation.

**Tim Abbott** · 2021-04-26 23:33 UTC

I think a valid theory is that we could check whether the `v6` directory was too large (E.g. >4GB) and if so, just delete it completely, if we're trying to minimize Zulip's disk footprint for a specific server.   (Or maybe just have an option to disable yarn caching altogether, which might be the right solution for a system that isn't regularly using `upgrade-zulip-from-git` but uses it once).

**Tim Abbott** · 2021-04-26 23:33 UTC

But I'm OK with declaring partial victory here and moving on.

**Greg Price** · 2021-04-28 18:43 UTC

We could also use the atime instead of the mtime. Try `ls -l --time=atime` and see how that looks. On my machine it looks consistent with being the time the given package was actually added to the cache.

**Tim Abbott** · 2021-04-28 18:46 UTC

Perhaps; I think just periodically deleting the entire directory (it's a cache, after all) would be pretty reasonable.  We could, e.g., just create a stamp file the last time we deleted the entire cache, and check if that file is more than N months old, in making the determination.

**Tim Abbott** · 2021-04-28 18:46 UTC

(We don't want to check how big something is, because that's expensive with how many files are in these directories).

**Riken Shah** · 2021-04-28 19:50 UTC

> Perhaps; I think just periodically deleting the entire directory (it's a cache, after all) would be pretty reasonable. We could, e.g., just create a stamp file the last time we deleted the entire cache, and check if that file is more than N months old, in making the determination.

I'll start working on it.

Do we need to run `yarn install` or `tools/provision` after deleting the directory?

**Tim Abbott** · 2021-04-28 22:31 UTC

Nope!  It's just a cache, so realistically whatever's needed will be downloaded again the next time we provision.

**Riken Shah** · 2021-04-30 16:49 UTC

Opened #18329 for the above feature.

I have some doubt: 
- If we want to use `threshold_days`, then is it alright if  `days_cutoff` be by default 15 days?
- Currently, I have set `days_cutoff` to 180 days.
- I have currently set the stamp path as `~/.cache/yarn/yarn_cache_deleted`, Is it alright?

**Riken Shah** · 2021-05-03 19:14 UTC

Tim, #18329 is also ready for review.

**Tim Abbott** · 2021-05-03 19:22 UTC

Tagging that as something to look at post-release; I think it has too high a risk/reward ratio for merging in the next week.


## tools/generate-integration-docs-screenshot for remote user

*2021-04-30 to 2021-04-30 · 7 messages · [open in Zulip](https://chat.zulip.org/#narrow/channel/18-tools/topic/tools.2Fgenerate-integration-docs-screenshot.20for.20remote.20user/with/1171745)*

**Riken Shah** · 2021-04-30 08:53 UTC

Currently if I run `./tools/generate-integration-docs-screenshot`, it fails because on remote enviroment `localhost:9991` is not allowed.
Maybe we should add an option in `tools/message-screenshot.js` to select the `host` from either `EXTERNAL_HOST` or `localhost:9991`.
```bash
--- a/tools/message-screenshot.js
+++ b/tools/message-screenshot.js
@@ -9,7 +9,7 @@ require("css.escape");
 const mkdirp = require("mkdirp");
 const puppeteer = require("puppeteer");
 
-const host = "localhost:9991";
+const host = process.env.EXTERNAL_HOST || "localhost:9991";
 const options = {};
```

**Tim Abbott** · 2021-04-30 15:33 UTC

I think structurally, we should have the caller pass in the host, which should be `realm.host`, accessible in the caller (`tools/generate-integration-docs-screenshot`)

**Adam Birds** · 2021-04-30 16:17 UTC

This was implemented by myself a few weeks back.

**Tim Abbott** · 2021-04-30 16:19 UTC

Yeah, I had a feeling of deja vu; I think probably the PR @Riken Shah (Riken-Shah) was reviewing wasn't rebased.

**Tim Abbott** · 2021-04-30 16:19 UTC

(One tip is that if a PR rebases without merge conflicts, it's worth rebasing it before trying to test it, since that avoids this sort of failure mode).

**Adam Birds** · 2021-04-30 16:19 UTC

Yeah, the commit for it is in `master` at https://github.com/zulip/zulip/commit/3b974d9ef7d3ff7479a0793f5b996f15d6bfbd40

**Riken Shah** · 2021-04-30 16:21 UTC

Ohh Yes!
I forget to rebase it, I found this when I was reviewing #17867.


## tools/lint --fix doesn't remove unused imports

*2021-06-06 to 2021-06-06 · 4 messages · [open in Zulip](https://chat.zulip.org/#narrow/channel/18-tools/topic/tools.2Flint.20--fix.20doesn.27t.20remove.20unused.20imports/with/1201993)*

**Abhijeet Bodas** · 2021-06-06 08:22 UTC

Why does `tools/lint --fix` not remove/fix unused imports (but just gives errors that there are unused imports)? This will be super helpful, because I frequently do wrong autocompletes in my editor, and the wrong autocomplete also automatically imports the wrong function.

**Tim Abbott** · 2021-06-06 15:03 UTC

@Abhijeet Bodas basically, because `tools/lint` runs like 12 different linters, and only half or so support a "--fix" option.  (And `pyflakes`, which we use for unused imports, is one of the ones that doesn't support that).

**Tim Abbott** · 2021-06-06 15:04 UTC

Auto-fixing lint issues is something that's a lot easier for some possible linter rules than others, so even some of the linters that support the options won't do it for all classes of errors.  Unused imports is certainly in the category that would be easy if one were to do it.

**Tim Abbott** · 2021-06-06 15:05 UTC

Part of what can be challenging with auto-fixing linter errors that are not just about whitespace is that sometimes a linter has determined that there's an inconsistency in your code, but it's not always totally clear what the developer's intent was (and there's multiple ways one could try to resolve that inconsistency).


## lint issue

*2021-06-28 to 2021-06-28 · 7 messages · [open in Zulip](https://chat.zulip.org/#narrow/channel/18-tools/topic/lint.20issue/with/1220158)*

**Riken Shah** · 2021-06-28 12:14 UTC

Can someone help with this lint failure? 
I am working on #18955 and it is failing on, 

https://github.com/zulip/zulip/runs/2931410539

```bash
eslint    | 
eslint    | /__w/zulip/zulip/frontend_tests/node_tests/user_status.js
eslint    |   7:18  error  There should be no empty line within import group  import/order
eslint    | 
eslint    | ✖ 1 problem (1 error, 0 warnings)
eslint    | 
```

When I tried to remove that line it shows,

```bash
eslint    | 
eslint    | /home/riken/zulip/frontend_tests/node_tests/user_status.js
eslint    |   7:1  error  Expected 1 empty line after require statement not followed by another require  import/newline-after-import
eslint    | 
eslint    | ✖ 1 problem (1 error, 0 warnings)
eslint    |   1 error and 0 warnings potentially fixable with the `--fix` option.
eslint    | 
```

So, I think so it is the issue with `eslint`.

**Priyank Patel** · 2021-06-28 18:02 UTC

Moving the `page_params` import right after `blueslip` fixes this:
```diff
 const {mock_esm, zrequire} = require("../zjsunit/namespace");
 const {run_test} = require("../zjsunit/test");
 const blueslip = require("../zjsunit/zblueslip");
+const {page_params} = require("../zjsunit/zpage_params");
 
 const channel = mock_esm("../../static/js/channel");
 const user_status = zrequire("user_status");
 const emoji_codes = zrequire("../generated/emoji/emoji_codes.json");
 const emoji = zrequire("../shared/js/emoji");
-const {page_params} = require("../zjsunit/zpage_params");
 
```

**Notification Bot** · 2021-06-28 22:35 UTC

This topic was moved by @Tim Abbott to #**issues>double send bug**

**Tim Abbott** · 2021-06-28 22:36 UTC

(That last notification was just for a single message within the topic).

**Tim Abbott** · 2021-06-28 22:36 UTC

Back to the topic at hand, I would expect some modules to need `page_params` to be initialized before them.

**Tim Abbott** · 2021-06-28 22:37 UTC

But I'm not sure I'd expect that for any of those specific modules.

**Tim Abbott** · 2021-06-28 22:38 UTC

Oh, that's just a linter issue, so that's likely a convention, not functional.


## test-js-with-puppeteer

*2021-07-17 to 2022-01-29 · 12 messages · [open in Zulip](https://chat.zulip.org/#narrow/channel/18-tools/topic/test-js-with-puppeteer/with/1233584)*

**Riken Shah** · 2021-07-17 11:37 UTC

While debugging the failure for #**automated testing>master failing**,
I noticed that while trying to run an individual file(eg: `tools/test-js-with-puppeteer message-basics`),
It failed with this error,

```bash
Error: Cannot find module './message-basics.ts'
Require stack:
- /home/riken/zulip/imaginaryUncacheableRequireResolveScript
    at Function.Module._resolveFilename (internal/modules/cjs/loader.js:902:15)
    at Function.resolve (internal/modules/cjs/helpers.js:98:19)
    at requireResolveNonCached (/srv/zulip-npm-cache/905c424937a7083297b2e3fbd8a8c970a766fae9/node_modules/ts-node/dist/bin.js:318:16)
    at getProjectSearchDir (/srv/zulip-npm-cache/905c424937a7083297b2e3fbd8a8c970a766fae9/node_modules/ts-node/dist/bin.js:288:35)
    at main (/srv/zulip-npm-cache/905c424937a7083297b2e3fbd8a8c970a766fae9/node_modules/ts-node/dist/bin.js:192:27)
    at Object.<anonymous> (/srv/zulip-npm-cache/905c424937a7083297b2e3fbd8a8c970a766fae9/node_modules/ts-node/dist/bin.js:348:5)
    at Module._compile (internal/modules/cjs/loader.js:1085:14)
    at Object.Module._extensions..js (internal/modules/cjs/loader.js:1114:10)
    at Module.load (internal/modules/cjs/loader.js:950:32)
    at Function.Module._load (internal/modules/cjs/loader.js:790:14) {
  code: 'MODULE_NOT_FOUND',
  requireStack: [ '/home/riken/zulip/imaginaryUncacheableRequireResolveScript' ]
}
```

After a bit of investigation I found it was due to `find_js_test_files` gives incorrect file path (`/home/riken/zulip/message-basics.ts` :cross_mark: ). 

This was introduced in [d4c8b01530e](https://github.com/zulip/zulip/commit/d4c8b01530e29fb10b0c321b43896d4b72f892be#diff-a7b8c4e5a1554a43397bb1bfef8c8ddcb4101e98459d3e9e4323d5a667b23ecf) (@Anders Kaseorg  FYI).

Maybe a fix for this is,
```diff
diff --git a/tools/lib/test_script.py b/tools/lib/test_script.py
index f9764f6c51..2ce73a37c0 100644
--- a/tools/lib/test_script.py
+++ b/tools/lib/test_script.py
@@ -106,7 +106,7 @@ def find_js_test_files(test_dir: str, files: Iterable[str]) -> List[str]:
     test_files = []
     for file in files:
         file = min(
-            (file_name for file_name in os.listdir(test_dir) if file_name.startswith(file)),
+            (os.path.join(test_dir, file_name) for file_name in os.listdir(test_dir) if file_name.startswith(file)),
             default=os.path.join(test_dir, file),
         )
         test_files.append(os.path.abspath(file))
```

**Anders Kaseorg** · 2021-07-18 07:47 UTC

#19300

**Tim Abbott** · 2021-07-18 18:49 UTC

Thanks for fixing!

**梅超凡** · 2021-08-08 14:28 UTC

:smile:

**Steve Howell** · 2022-01-28 17:16 UTC

It seems like when you run `test-js-with-puppeteer` with bogus filename arguments, it very expensively starts the server and then cryptically reports it as a failed test after a bunch of noise.  Does anybody have time to fix this?

**Steve Howell** · 2022-01-28 17:17 UTC

This is a really long-winded way of telling me that "bogus" isn't a test.

~~~
$ ./tools/test-js-with-puppeteer bogus
Chromium is already in /srv/zulip-npm-cache/4173fd72875e8321a667c17ee59232a5cfbe21b1/node_modules/puppeteer/.local-chromium/linux-938248; skipping download.
+ tools/setup/generate-fixtures
 pg_terminate_backend
----------------------
(0 rows)

DROP DATABASE
CREATE DATABASE

Waiting for test server (may take a while)


Starting Zulip on:

        http://zulipdev.com:9981/

Internal ports:
   9981: Development server proxy (connect here)
   9982: Django
   9983: Tornado

Tornado server (re)started on port 9983
Django process (re)started. Quit the server with CONTROL-C.
2022-01-28 17:16:22.094 INFO [zr] 127.0.0.1       GET     301   2ms /accounts/home (unauth@root via python-requests)
2022-01-28 17:16:22.095 INFO [django.server] "GET /accounts/home HTTP/1.1" 301 0
2022-01-28 17:16:22.185 INFO [zr] 127.0.0.1       GET     302   6ms (db: 1ms/1q) (+start: 75ms) /accounts/home/ (unauth@root via python-requests)
2022-01-28 17:16:22.186 INFO [django.server] "GET /accounts/home/ HTTP/1.1" 302 0
2022-01-28 17:16:22.337 INFO [zr] 127.0.0.1       GET     200 123ms (db: 1ms/1q) (+start: 16ms) /accounts/find/ (unauth@root via python-requests)


--- SERVER IS UP! ---



===================== (1/1) bogus
Running node --unhandled-rejections=strict /home/zulipdev/zulip/node_modules/.bin/ts-node --script-mode --transpile-only /home/zulipdev/zulip/bogus


node:internal/modules/cjs/loader:936
  throw err;
  ^

Error: Cannot find module './bogus'
Require stack:
- /home/zulipdev/zulip/imaginaryUncacheableRequireResolveScript
    at Function.Module._resolveFilename (node:internal/modules/cjs/loader:933:15)
    at Function.resolve (node:internal/modules/cjs/helpers:108:19)
    at requireResolveNonCached (/srv/zulip-npm-cache/4173fd72875e8321a667c17ee59232a5cfbe21b1/node_modules/ts-node/dist/bin.js:321:16)
    at getProjectSearchDir (/srv/zulip-npm-cache/4173fd72875e8321a667c17ee59232a5cfbe21b1/node_modules/ts-node/dist/bin.js:291:40)
    at main (/srv/zulip-npm-cache/4173fd72875e8321a667c17ee59232a5cfbe21b1/node_modules/ts-node/dist/bin.js:193:27)
    at Object.<anonymous> (/srv/zulip-npm-cache/4173fd72875e8321a667c17ee59232a5cfbe21b1/node_modules/ts-node/dist/bin.js:351:5)
    at Module._compile (node:internal/modules/cjs/loader:1101:14)
    at Object.Module._extensions..js (node:internal/modules/cjs/loader:1153:10)
    at Module.load (node:internal/modules/cjs/loader:981:32)
    at Function.Module._load (node:internal/modules/cjs/loader:822:12) {
  code: 'MODULE_NOT_FOUND',
  requireStack: [ '/home/zulipdev/zulip/imaginaryUncacheableRequireResolveScript' ]
}
+ env PGHOST=localhost PGUSER=zulip_test scripts/setup/terminate-psql-sessions zulip_test
 pg_terminate_backend
----------------------
 t
(1 row)

Destroying test database for alias 'default'...
Cloning test database for alias 'default'...
2022-01-28 17:16:27.317 INFO [bmemcached.protocol] Flushing memcached
2022-01-28 17:16:27.319 INFO [zr] 127.0.0.1       POST    200   2ms (+start: 21ms) /flush_caches (unauth@zulip via python-requests)
Waiting for children to stop...

The Puppeteer frontend tests failed! The failing test was:
    ./tools/test-js-with-puppeteer bogus
For help debugging, read:
  https://zulip.readthedocs.io/en/latest/testing/testing-with-puppeteer.html
or report and ask for help in chat.zulip.org
It's also worthy to see screenshots generated on failure stored under var/puppeteer/*.png

**Steve Howell** · 2022-01-28 17:19 UTC

I think this is a more pleasant experience:

~~~
$ time ./tools/test-js-with-node bogus
Cannot find bogus (/home/zulipdev/zulip/frontend_tests/node_tests/bogus.js)

real    0m0.119s
user    0m0.109s
sys     0m0.010s

**Tim Abbott** · 2022-01-28 17:26 UTC

Yeah, agreed that this is annoying.  Worth opening an issue with the "tools" area label, at least.

**Tim Abbott** · 2022-01-28 17:26 UTC

Of course, the problem here is that the test discovery process runs inside puppeteer which takes time to startup; so the fix would likely be to add a duplicate glob check in the wrapping code.

**Steve Howell** · 2022-01-28 22:59 UTC

#20970

**Steve Howell** · 2022-01-28 23:02 UTC

(replying to Tim Abbott)
> Of course, the problem here is that the test discovery process runs inside puppeteer which takes time to startup; so the fix would likely be to add a duplicate glob check in the wrapping code.

I'm not sure that's completely accurate, as the Python layer seems to call `find_js_test_files`to build up a list of files.

**Tim Abbott** · 2022-01-29 01:31 UTC

I see, in that case, this should be pretty doable.


## provisioning

*2021-08-11 to 2021-08-13 · 2 messages · [open in Zulip](https://chat.zulip.org/#narrow/channel/18-tools/topic/provisioning/with/1246165)*

**Rohitt Vashishtha** · 2021-08-11 06:37 UTC

I was wondering if there's a very restricted set of things where we bump the provision number and if we could do away with the concept, or at least create a way to automatically resolve merge conflicts if provision versions are different, or more broadly, if this is even a thing that needs fixing.

For example, we have a tool similar to our renumbering migrations script.

Also, we could have provision hash the `yarn.lock` and other files before each provision and check the hash to see if we need provisioning.

**Tim Abbott** · 2021-08-13 22:51 UTC

It's mostly possible for various common categories (there's a long issue detailing them).  I'd be happy to see someone working on the easy pieces (E.g. `yarn.lock` changes).


## --groups param for ./tools/lint

*2021-11-20 to 2021-11-20 · 4 messages · [open in Zulip](https://chat.zulip.org/#narrow/channel/18-tools/topic/--groups.20param.20for.20.2E.2Ftools.2Flint/with/1284692)*

**Yash RE** · 2021-11-20 17:26 UTC

Please correct me if I'm wrong, but `./tools/lint --fix --groups=frontend` is ~ one of the only places where we use `--<flag>=<option>` instead of `--<flag> <option>`.
Does it have to be that way? If not, can we change it for consistency?

**Anders Kaseorg** · 2021-11-20 19:39 UTC

Not sure what you mean. Both forms are supported, and in general I prefer `--flag=option` because it's unambiguous as to whether it's an option to `--flag` or an argument to the top-level command.

**Yash RE** · 2021-11-20 19:42 UTC

huh. okay. I guess I've just been wrong for a while.

**Anders Kaseorg** · 2021-11-20 19:42 UTC

Also it happens to result in better Black formatting when there's a multi-line argument list like [this](https://github.com/zulip/zulip/blob/4.7/tools/webpack#L31).


## grammar checker

*2021-12-30 to 2022-02-21 · 48 messages · [open in Zulip](https://chat.zulip.org/#narrow/channel/18-tools/topic/grammar.20checker/with/1302715)*

**Rein Zustand** · 2021-12-30 14:49 UTC

We currently use Codespell to check for typos. What if we go one step further, to also check for grammatical errors? I recently discovered https://caderek.github.io/gramma/, a CLI grammar checker that uses [LanguageTool](https://languagetool.org/), A FOSS grammar, style, and spell checker.

Styles can additionally be enforced, such as to recommend using short, simple sentences with active voice.

**Greg Price** · 2021-12-30 19:04 UTC

My experience with grammar checkers is that they make lots and lots of bad suggestions, and neutral suggestions (don't make the text really worse or better, but can waste your time), as well as good ones.

**Greg Price** · 2021-12-30 19:05 UTC

If people find a tool helpful, that's great. But I definitely wouldn't want to have it enforcing anything, or making loud suggestions by default.

**Rein Zustand** · 2021-12-31 01:50 UTC

I tested it on docs/production/security-model.md. The majority of the suggestion seems to be useful:

```
cat docs/production/security-model.md| pylanguagetool --disabled-categories "TYPOS,TYPOGRAPHY" --disabled-rules "DOUBLE_PUNCTUATION"
filetype not detected, assuming plaintext
English (US) detected (99% confidence)

Use a comma before ‘so’ if it connects two independent clauses (unless they are closely connected and short).
  ✗ ..., please report it to security@zulip.com so we can do a responsible security announ...
                                               ^^^
  ✓ ..., please report it to security@zulip.com, so we can do a responsible security announ...

This word has been used in one of the immediately preceding sentences. Using a synonym could make your text more interesting to read, unless the repetition is intentional.
  ✗ ... for an extended   discussion on how we chose this value.   Estimating the guessabili...
                                               ^^^^^
  ✓ ... for an extended   discussion on how we decided this value.   Estimating the guessabili...
  ✓ ... for an extended   discussion on how we selected this value.   Estimating the guessabili...
  ✓ ... for an extended   discussion on how we picked this value.   Estimating the guessabili...

This word has been used in one of the immediately preceding sentences. Using a synonym could make your text more interesting to read, unless the repetition is intentional.
  ✗ ...t the strength of the   passwords users choose. <!---   If the BHOS15 link ever goes d...
                                               ^^^^^^
  ✓ ...t the strength of the   passwords users decide. <!---   If the BHOS15 link ever goes d...
  ✓ ...t the strength of the   passwords users select. <!---   If the BHOS15 link ever goes d...
  ✓ ...t the strength of the   passwords users pick. <!---   If the BHOS15 link ever goes d...

Possible missing comma found.
  ✗ ...exist, or interact     with them in any way until they are added. Given a stream na...
                                               ^^^
  ✓ ...exist, or interact     with them in any way, until they are added. Given a stream na...

Use “an” instead of ‘a’ if the following word starts with a vowel sound, e.g. ‘an article’, ‘an hour’.
  ✗ ...password or deactivate their account in a   SSO system, since neither of those pr...
                                               ^
  ✓ ...password or deactivate their account in an   SSO system, since neither of those pr...

Possible missing comma found.
  ✗ ...s - Zulip supports user-uploaded files. Ideally they should be hosted   from a separate...
                                               ^^^^^^^
  ✓ ...s - Zulip supports user-uploaded files. Ideally, they should be hosted   from a separate...

Possible typo: you repeated a word
  ✗ ... a result,   Zulip supports routing all outgoing outgoing HTTP requests [through   Smokescreen][s...
                                               ^^^^^^^^^^^^^^^^^
  ✓ ... a result,   Zulip supports routing all outgoing HTTP requests [through   Smokescreen][s...
```

**Rein Zustand** · 2021-12-31 01:51 UTC

Rules such as
> This word has been used in one of the immediately preceding sentences. Using a synonym could make your text more interesting to read, unless the repetition is intentional.

can be disabled completely.

**Rein Zustand** · 2021-12-31 01:52 UTC

This is a clear typo:
" ✗ ... a result,   Zulip supports routing all **outgoing outgoing** HTTP requests [through   Smokescreen][s..."

**Tim Abbott** · 2021-12-31 02:03 UTC

@Rein Zustand those results are more promising than I'd have expected!  I think if you want to try running it on a few files and make a PR that makes it happy improving language, that'd be a good way to evaluate whether it's something we want to use more broadly.

**Greg Price** · 2021-12-31 04:47 UTC

The "outgoing outgoing" fix is a good one, and so is the a->an fix.

I think none of the three comma suggestions are actually improvements.

**Greg Price** · 2021-12-31 04:48 UTC

(And as you hint at, the "use a synonym for variation" suggestion is basically always going to be inappropriate for our use and we'd want to disable it.)

**Rein Zustand** · 2021-12-31 13:19 UTC

I will try to count the number of rules that are used by LanguageTool by default, and see if it makes more sense to specify `--disabled-rules` instead of `--enabled-rules`.

**Rein Zustand** · 2022-01-20 12:38 UTC

There are [5342 rules](https://community.languagetool.org/rule/list?lang=en) as LanguageTool 5.7-SNAPSHOT (2022-01-19 21:33:04 +0000). There is no indication if they are checked all at once.

**Rein Zustand** · 2022-01-20 13:05 UTC

LT seems to complain a lot about unit space: 
```
Insert a space between the numerical value and the unit symbol.
  ✗ ... 11 Bullseye Debian 10 Buster  At least 2GB RAM, and 10GB disk space  If you expect...
                                               ^^^
  ✓ ... 11 Bullseye Debian 10 Buster  At least 2 GB RAM, and 10GB disk space  If you expect...
  UNIT_SPACE: Missing space between numeric value and unit (e.g., 25 km)
```
Should I just exclude this rule?

**Rein Zustand** · 2022-01-20 13:13 UTC

https://community.languagetool.org/rule/show/UNIT_SPACE?lang=en

**Rein Zustand** · 2022-01-20 13:17 UTC

```
The word ‘install’ is not a noun.
  ✗ ...p, just pass the  flag when running the install script. The  and  options are required ...
                                               ^^^^^^^
  ✓ ...p, just pass the  flag when running the installation script. The  and  options are required ...
  A_INSTALL: a/the + install
```
This is rather minor, but it happens several times.

**Rein Zustand** · 2022-01-20 13:30 UTC

Made #20853.

**Rein Zustand** · 2022-01-20 13:39 UTC

(replying to Rein Zustand)
> https://community.languagetool.org/rule/show/UNIT_SPACE?lang=en
LT cites  Bureau international des poids et mesures for the rule. The bipm.org url linked is dead, but you can see the statement in the answer of https://english.stackexchange.com/questions/2794/punctuation-with-units:
> The numerical value always precedes the unit, and a space is always used to separate the unit from the number. (…) The only exceptions to this rule are for the unit symbols for degree, minute, and second for plane angle, °, ′, and ″, respectively, for which no space is left between the numerical value and the unit symbol.

**Greg Price** · 2022-01-20 16:45 UTC

That UNIT_SPACE change is pretty reasonable, and I wouldn't be opposed to consistently writing things that way.

**Greg Price** · 2022-01-20 17:00 UTC

The A_INSTALL thing is... well, "install script" is a normal term. "Installation script" is not a normal term. More broadly, in technical software usage "install" *is* a noun.

**Greg Price** · 2022-01-20 17:02 UTC

The changes in the PR look fine. The one adding "an" in a heading isn't exactly necessary, because it's normal for headings to omit articles, but the rest are all definitely good.

**Anders Kaseorg** · 2022-01-20 23:59 UTC

I would say “installation script” is more correct than “install script”, unless you’re literally talking about “the `install` script” with a code span. Yes, people informally use “install” as a noun and even more informally as an adjective, but documentation shouldn’t.

**Rein Zustand** · 2022-01-21 00:06 UTC

I looked around for the usage in other docs:

Docker: https://docs.docker.com/engine/install/rhel/
> The installation script requires root or sudo privileges to install and use Docker.

Oracle: https://docs.oracle.com/cd/E18752_01/html/817-0406/ch3enhancepkg-10289.html
> This section discusses optional package installation scripts.

**Rein Zustand** · 2022-01-21 00:08 UTC

I can't find "install script" in any official docs yet. Though they are used in blog/forum posts.

**Steve Howell** · 2022-01-21 00:09 UTC

“Installation” is no more of an adjective than “install”.

**Steve Howell** · 2022-01-21 00:15 UTC

I think “installing script” is the pedantic way to turn a verb into an adjective.

**Steve Howell** · 2022-01-21 00:16 UTC

But it sounds awkward.

**Rein Zustand** · 2022-01-21 00:17 UTC

I also notice that e.g in security-model.md, the line wrap is not consistent. Sometimes, the paragraph is wrapped with 72 textwidth, another with 76. Sometimes it is not wrapped properly either:
```
  - Bots with the `can_forge_sender` permission can send messages that appear to have been sent by
    another user. They also have the ability to see the names of all
    streams, including private streams. This is important for implementing
    integrations like the Jabber, IRC, and Zephyr mirrors.
```
Which textwidth should I use? The default by vim is 80.

**Rein Zustand** · 2022-01-21 00:18 UTC

I will do the wrapping only on the lines with my change.

**Rein Zustand** · 2022-01-21 00:19 UTC

(replying to Steve Howell (showell))
> I think “installing script” is the pedantic way to turn a verb into an adjective.
LT says that the problem is that "install" is not a noun, and "installation" is more suitable because it is a noun.

**Anders Kaseorg** · 2022-01-21 00:46 UTC

There’s nothing unusual about using a -tion noun as an adjective: “production line”, “disambiguation page”, “opposition party”, “communication protocol”, “election day”, “observation deck”.

**Steve Howell** · 2022-01-21 01:04 UTC

Fair enough.

**Greg Price** · 2022-01-21 01:27 UTC

(If we're getting technical about grammar here, none of those are adjectives. All of them are nouns. One of the ways a noun can be used in English, which is what's happening in each of those examples, is as an "attributive noun" or "noun adjunct":
https://www.merriam-webster.com/words-at-play/nouns-that-look-like-adjectives
https://en.wikipedia.org/wiki/Noun_adjunct
)

**Greg Price** · 2022-01-21 01:30 UTC

(replying to Rein Zustand)
> I can't find "install script" in any official docs yet.

I do, googling for that phrase in quotes. Here's an example:
https://www.ibm.com/docs/en/slpm/10.2.0?topic=client-run-install-script
> ## Run the install script
> […] 1. As root, run the install script as follows:

**Greg Price** · 2022-01-21 01:31 UTC

The software in question is something I'd never heard of, but the same thing is true of most of the results I find googling for "installation script".

**Greg Price** · 2022-01-21 01:32 UTC

Making the search `"install script" -post -pre` cuts out a lot of results that aren't matches, making it easier to find results that are. Here's Chef:
https://docs.chef.io/chef_install_script/
> ## Chef Software Install Script
> In addition to the default install behavior, the Chef Software Install script supports the following options:

**Anders Kaseorg** · 2022-01-21 01:33 UTC

IBM is just inconsistent. Searching all of their documentation, there are [5,132 results for "installation script"](https://www.ibm.com/docs/en/search/%22installation%20script%22) and [2,402 results for "install script"](https://www.ibm.com/docs/en/search/%22install%20script%22).

**Anders Kaseorg** · 2022-01-21 01:35 UTC

The Chef script is named `install`, and they also use [“installation script”](https://docs.chef.io/install_chef_air_gap/#create-a-bootstrap-template).

**Greg Price** · 2022-01-21 01:42 UTC

That last page has one use of "installation script", and four of "install script".

And the latter refer to something that doesn't have any particular name in code like `install` -- it's a file you're instructed to create for yourself, following an example.

**Steve Howell** · 2022-01-21 01:43 UTC

https://en.m.wikipedia.org/wiki/Attributive_verb

**Anders Kaseorg** · 2022-01-21 01:48 UTC

(I wasn’t suggesting that “installing script” would be ungrammatical—it would just be awkward, like you observed.)

**Steve Howell** · 2022-01-21 01:51 UTC

“Installation script” is totally fine by me.  I enjoy the grammar debates. 😀

**Tim Abbott** · 2022-01-21 20:09 UTC

We could also use "installer", though I feel like that tends to be used for a GUI installation process.

**Rein Zustand** · 2022-01-22 14:44 UTC

Made #20886. I also accidentally found several "nginx" not being written as "Nginx" -- this is not caught by LT.

**Rein Zustand** · 2022-01-22 14:46 UTC

Raised #20887.

**Rein Zustand** · 2022-01-22 14:50 UTC

LT complains about this https://github.com/zulip/zulip/blob/fd1d4e101b5d6baaa19ae3166e568244c2582f26/docs/production/export-and-import.md?plain=1#L237.

See https://community.languagetool.org/rule/show/WITH_THE_EXCEPTION_OF?lang=en&subId=1
```
Description:	with the exception of (except)
Message:	Consider using except or except for
Category:	Redundant Phrases (
```

**Anders Kaseorg** · 2022-01-22 20:58 UTC

nginx is written in lowercase in its own documentation, even at the beginning of sentences. We wouldn't recapitalize iOS, so I don't see any justification for recapitalizing nginx.

**Rein Zustand** · 2022-01-22 23:13 UTC

Should we consistently use "nginx" instead of "Nginx" then? Currently, it is a mix. Though with "Nginx", it is easier for grep  to capture only the code part or the textual part.

**Tim Abbott** · 2022-01-24 05:26 UTC

@Rein Zustand I think so, yeah.

**Rein Zustand** · 2022-02-21 14:07 UTC

I found a new grammar checker called [Vale](https://github.com/errata-ai/vale). Found it from the list of linters in a vim auto-linter plugin. This time, it is fast, and supports custom writing style linting. The default ones that can be chosen can be found in https://github.com/errata-ai/styles. E.g. Microsoft style guide, and Google developer documentation style guide.


## set -u

*2021-12-31 to 2022-01-18 · 18 messages · [open in Zulip](https://chat.zulip.org/#narrow/channel/18-tools/topic/set.20-u/with/1302911)*

**Rein Zustand** · 2021-12-31 13:15 UTC

This incident  of an accidental 77 TB data deletion in a supercomputing system, https://news.ycombinator.com/item?id=29734021, was due to undefined variables. And so, in the HN thread, people have been recommending to add `set -e`, `set -u`, plus Shellcheck. I'm aware of the presence of `set -e` and Shellcheck in zulip/zulip, but not `set -u` (only scripts/lib/setup-apt-repo contains it). Is there a reason why `set -u` is not used in most of the shell scripts? What about `set -o pipefail`? (See https://gist.github.com/robin-a-meade/58d60124b88b60816e8349d1e3938615)

**Greg Price** · 2021-12-31 18:51 UTC

>   A new improved version of the script was applied on the system.
>
>  However, during deployment, there was a lack of consideration as the periodical script was not disabled.
>
>  The modified shell script was reloaded from the middle.
>
>  As a result, the find command containing undefined variables was executed and deleted the files.

I think the most important issue there was that a script was mutated while it was running. That can cause totally arbitrary bad behavior -- no combination of `set` options will necessarily stop it before it causes damage.

Zulip avoids that sort of problem with its system of making each deployment in a new directory tree, and mutating only a symlink to point at the new current version.

**Greg Price** · 2021-12-31 18:55 UTC

`set -u` is probably better to have than to not have. (Then you explicitly say `"${foo:-}"` or whatever, with the `:-`, when you do want to allow the variable to be unset.)

But I think its impact is a lot smaller than that of `set -e` -- I think the number of bugs it's likely to affect is much smaller, if you're writing reasonable code in the first place.

**Alex Dehnert** · 2021-12-31 18:58 UTC

https://sipb.mit.edu/doc/safe-shell/ is a page I wrote years ago about safer shell practices. (I like `set -f` as well, which disables globbing.)

**Greg Price** · 2021-12-31 18:58 UTC

`set -o pipefail` is also often helpful but I feel like I've run into situations where it caused problems that were a pain to work around (which contrasts with `set -e` and `set -u`, where the solution when the behavior it causes isn't what you intended is to add a few more characters that make your intent explicit.)

I guess a comment on that gist has an example:
https://gist.github.com/robin-a-meade/58d60124b88b60816e8349d1e3938615#gistcomment-4012229

**Greg Price** · 2021-12-31 18:59 UTC

Ah, I'd forgotten about that page, thanks for mentioning it :smile:

**Greg Price** · 2021-12-31 19:00 UTC

The other points in that document (like using quotes, and `--` before positional arguments) are good advice too.

**Alex Dehnert** · 2021-12-31 19:01 UTC

(I should perhaps note that the history clearly indicates Anders contributed too, and it's likely that others -- possibly including other now-Zulip-y folks -- did too.)

**Alex Vandiver** · 2021-12-31 19:25 UTC

(replying to Rein Zustand)
> I'm aware of the presence of `set -e` and Shellcheck in zulip/zulip, but not `set -u` (only scripts/lib/setup-apt-repo contains it). Is there a reason why `set -u` is not used in most of the shell scripts?

We use `set -eu` in many of our scripts:
```
$ git grep 'set -eu'
puppet/zulip/files/secret-env-wrapper:set -eu
scripts/lib/install-node:set -euo pipefail
scripts/lib/install-yarn:set -euo pipefail
tools/build-release-tarball:set -eu
tools/cache-zulip-git-version:set -eu
tools/ci/build-docker-images:set -eux
tools/run-yarn-deduplicate:set -eu
tools/setup/bootstrap-awscli.sh:set -eu
tools/setup/install-shellcheck:set -eu
tools/setup/install-shfmt:set -eu

**Anders Kaseorg** · 2021-12-31 19:34 UTC

We should use `set -eu` in all scripts, as well as `-o pipefail` if applicable. Please add them (after verifying that we don't rely on their absence, of course).

**Alex Dehnert** · 2022-01-01 01:36 UTC

I just ran across https://twitter.com/leifwalsh/status/1477046954257436673?t=FuKep5fs6QBw3d1L7smeIQ&s=19 on Twitter :)

**Rein Zustand** · 2022-01-11 10:58 UTC

Raised #20748.

**Anant Verma** · 2022-01-15 12:59 UTC

(replying to Anders Kaseorg)
> We should use `set -eu` in all scripts, as well as `-o pipefail` if applicable. Please add them (after verifying that we don't rely on their absence, of course).
I've picked up this issue and was reading through these commands. I have a query regarding pipefail. How can I verify that the script relies on it's absence or not?

**Rein Zustand** · 2022-01-15 14:13 UTC

@Anant Verma for a starter, you can look to improve scripts that don't use pipes.

**Greg Price** · 2022-01-18 19:30 UTC

@Anant Verma Please take a look back at our contributor docs on picking an issue to work on:
https://zulip.readthedocs.io/en/latest/overview/contributing.html#picking-an-issue-to-work-on

The time for claiming an issue is after you've worked out answers to this sort of question about how you'd approach it, either on your own or by asking in chat. I've gone and unassigned the issue to make clear it's still open for others to take on.

**Greg Price** · 2022-01-18 19:34 UTC

To the substance of your question: unfortunately, I think there is not a simple way to reliably do so, and I think the same thing is true of `set -u`. If the script doesn't use pipelines at all then it's not affected by `set -o pipefail`, but pipelines are a very commonly-used shell feature so I expect that wouldn't help for very many scripts (and there'd still be the matter of `set -u`.)

And of course the point of using `set -o pipefail` is to have it where it *can* have an effect on behavior, so applying it to the scripts that never use pipes wouldn't get us very far into resolving this issue anyway.

**Greg Price** · 2022-01-18 19:40 UTC

I think the steps for adding these flags will look basically like:
* Understand the shell programming language.
* Understand what the specific features `set -u` and `set -o pipefail` change in the shell's behavior.
* For a given script, read it line by line, and asking at each bit of code: Could those flags cause an error here? Under what conditions would they do so? What would the non-error behavior be in those conditions? Could that non-error behavior be desirable?
* Most of the answers will be: no, they can't at this line; or yes, they can, and that's good because the non-error behavior would be nonsense.
* Occasionally the answers will be: yes, they can, ooh and actually that'd be bad because we were relying on the non-error behavior at that line. These will require revising the code at those spots to get the desired behavior explicitly, even with those flags set.
* Then it's possible to set the flags on that script, and repeat on the next script.

**Greg Price** · 2022-01-18 19:41 UTC

Note those first two steps, though. I think this issue is one that will probably only make sense for someone to take who has spent some time writing shell scripts before.


## node --coverage tracebacks

*2022-01-07 to 2022-01-07 · 21 messages · [open in Zulip](https://chat.zulip.org/#narrow/channel/18-tools/topic/node.20--coverage.20tracebacks/with/1306042)*

**Steve Howell** · 2022-01-07 14:43 UTC

I am in the process of debugging (or at least explaining the bug) for the situation that running `test-js-with-node` produces bad stack traces if you run with the `--coverage` option.  I am doing this mostly live.

**Steve Howell** · 2022-01-07 14:47 UTC

First I simulate a bug in `people.js`:

~~~ diff
$ git diff
diff --git a/static/js/people.js b/static/js/people.js
index 690865f6bb..05ffcddbd0 100644
--- a/static/js/people.js
+++ b/static/js/people.js
@@ -324,6 +324,7 @@ export function get_display_full_names(user_ids) {
 }

 export function get_full_name(user_id) {
+    throw new Error("cannot find user_id");
     return people_by_user_id_dict.get(user_id).full_name;
 }


~~~

**Steve Howell** · 2022-01-07 14:50 UTC

And then I run a normal test:

~~~ spoiler
~~~~
$ ./tools/test-js-with-node people
Starting node tests...
running test people
        test: basics
        test: sort_but_pin_current_user_on_top with me
        test: sort_but_pin_current_user_on_top without me
        test: check_active_non_active_users
        test: pm_lookup_key
        test: get_recipients
        test: get_full_name
--------------------------------------------------
test failed: /home/zulipdev/zulip/frontend_tests/node_tests/people.js > get_full_name

Error: cannot find user_id
    at Object.get_full_name (/home/zulipdev/zulip/static/js/people.js:327:11)
    at /home/zulipdev/zulip/frontend_tests/node_tests/people.js:454:26
    at /home/zulipdev/zulip/frontend_tests/node_tests/people.js:67:9
    at /home/zulipdev/zulip/frontend_tests/zjsunit/test.js:34:13
    at Object.exports.with_overrides (/home/zulipdev/zulip/frontend_tests/zjsunit/namespace.js:413:9)
    at exports.run_test (/home/zulipdev/zulip/frontend_tests/zjsunit/test.js:33:19)
    at test_people (/home/zulipdev/zulip/frontend_tests/node_tests/people.js:65:5)
    at Object.<anonymous> (/home/zulipdev/zulip/frontend_tests/node_tests/people.js:452:1)
    at Module._compile (node:internal/modules/cjs/loader:1101:14)
    at Module._compile (/srv/zulip-npm-cache/4173fd72875e8321a667c17ee59232a5cfbe21b1/node_modules/pirates/lib/index.js:99:24)
    at Module._extensions..js (node:internal/modules/cjs/loader:1153:10)
    at Object.newLoader [as .js] (/srv/zulip-npm-cache/4173fd72875e8321a667c17ee59232a5cfbe21b1/node_modules/pirates/lib/index.js:104:7)
    at Module.load (node:internal/modules/cjs/loader:981:32)
    at Module._load (node:internal/modules/cjs/loader:822:12)
    at Function.load [as _load] (/home/zulipdev/zulip/frontend_tests/zjsunit/namespace.js:90:12)
    at Module.require (node:internal/modules/cjs/loader:1005:19)
    at require (node:internal/modules/cjs/helpers:102:18)
    at run_one_module (/home/zulipdev/zulip/frontend_tests/zjsunit/index.js:78:5)
(...)


** Tests failed, PLEASE FIX! **

~~~

**Steve Howell** · 2022-01-07 14:50 UTC

And the main thing to look at is this:

~~~
Error: cannot find user_id
    at Object.get_full_name (/home/zulipdev/zulip/static/js/people.js:327:11)
    at /home/zulipdev/zulip/frontend_tests/node_tests/people.js:454:26
    at /home/zulipdev/zulip/frontend_tests/node_tests/people.js:67:9
    at /home/zulipdev/zulip/frontend_tests/zjsunit/test.js:34:13

**Steve Howell** · 2022-01-07 14:54 UTC

The line numbers are accurate.  The column numbers are accurate as far as I can tell, since it sort of depends on which part of an expression you expect the traceback to point you to.

**Steve Howell** · 2022-01-07 14:56 UTC

When you instead run `./tools/test-js-with-node --coverage people`, you can see that the corresponding part of the traceback looks like this:

~~~
    at Object.get_full_name (/home/zulipdev/zulip/static/js/people.js:29:3862)
    at /home/zulipdev/zulip/frontend_tests/node_tests/people.js:34:2291
    at /home/zulipdev/zulip/frontend_tests/node_tests/people.js:4:674
    at /home/zulipdev/zulip/frontend_tests/zjsunit/test.js:2:1492

**Steve Howell** · 2022-01-07 14:59 UTC

The filenames are clearly accurate, but the rows and columns pretty clearly refer to the "compiled" JS code, not the original.  Obviously, this can be confusing.  Once you know this quirk, my workflow has always been to just debug the single test without `--coverage`, but it's clearly something we want to fix.  For reference, this bug has been in place for at least a couple years, and it was introduced by some sort of webpack/babel change.

**Steve Howell** · 2022-01-07 15:04 UTC

It's pretty to see what's happening under the hood:

~~~
$ git diff tools
diff --git a/tools/test-js-with-node b/tools/test-js-with-node
index f7b808dd1d..e8985a7e74 100755
--- a/tools/test-js-with-node
+++ b/tools/test-js-with-node
@@ -326,6 +326,7 @@ def run_tests_via_node_js() -> int:
         command = node_tests_cmd

     try:
+        print(command); sys.exit(1)
         ret = subprocess.check_call(command)

**Steve Howell** · 2022-01-07 15:05 UTC

~~~
$ ./tools/test-js-with-node people
Starting node tests...
['node', '--stack-trace-limit=100', '/home/zulipdev/zulip/frontend_tests/zjsunit/index.js', '/home/zulipdev/zulip/frontend_tests/node_tests/people.js']

$ ./tools/test-js-with-node --coverage people
You cannot use --coverage with parallel tests. Running in serial mode.

Starting node tests...
['/home/zulipdev/zulip/node_modules/.bin/nyc', '--extension', '.hbs', '--extension', '.ts', '--report-dir', '/home/zulipdev/zulip/var/node-coverage', '--temp-directory', '/home/zulipdev/zulip/var/node-coverage', '-r=lcov', '-r=json', '-r=text-summary', 'node', '--stack-trace-limit=100', '/home/zulipdev/zulip/frontend_tests/zjsunit/index.js', '/home/zulipdev/zulip/frontend_tests/node_tests/people.js']

**Steve Howell** · 2022-01-07 15:10 UTC

~~This looks promising: https://www.npmjs.com/package/@istanbuljs/nyc-config-babel ~~

**Steve Howell** · 2022-01-07 15:39 UTC

One thing to note is that `nyc` clearly has some notion of the source map, since it reports missing lines correctly.

~~~
$ git diff
diff --git a/static/js/people.js b/static/js/people.js
index 690865f6bb..23ea1bf3e8 100644
--- a/static/js/people.js
+++ b/static/js/people.js
@@ -327,6 +327,10 @@ export function get_full_name(user_id) {
     return people_by_user_id_dict.get(user_id).full_name;
 }

+export function ignore(user_id) {
+    return people_by_user_id_dict.get(user_id).full_name;
+}
+
~~~

~~~
ERROR: static/js/people.js no longer has complete node test coverage
  Lines missing coverage: 331

**Steve Howell** · 2022-01-07 15:45 UTC

https://github.com/istanbuljs/nyc/blob/master/lib/source-maps.js

**Steve Howell** · 2022-01-07 16:01 UTC

After some fruitless web searches and greps against `nyc` and `jest` codebases, I have a new idea.  Let's make sure that there are no shenanigans from `frontend_tests/zjsunit/index.js`:

~~~
$ git diff
diff --git a/frontend_tests/zjsunit/index.js b/frontend_tests/zjsunit/index.js
index 46f81cc86a..a9b43968be 100644
--- a/frontend_tests/zjsunit/index.js
+++ b/frontend_tests/zjsunit/index.js
@@ -32,6 +32,9 @@ require("@babel/register")({
     ],
 });

+// after babel config
+throw new Error("simulate index.js does not wanna play today");
+
 // Create a helper function to avoid sneaky delays in tests.
 function immediate(f) {
     return () => f();
(zulip-py3-venv) ~/zulip (node_stack)
$
(zulip-py3-venv) ~/zulip (node_stack)
$ ./tools/test-js-with-node people
Starting node tests...
/home/zulipdev/zulip/frontend_tests/zjsunit/index.js:36
throw new Error("simulate index.js does not wanna play today");
^

Error: simulate index.js does not wanna play today
    at Object.<anonymous> (/home/zulipdev/zulip/frontend_tests/zjsunit/index.js:36:7)

**Steve Howell** · 2022-01-07 16:03 UTC

Ok, same result as simulating a deeper failure: when you hack `index.js` to throw an error before doing anything of substance, the line number refers to the wrong source line:

~~~
$ ./tools/test-js-with-node --coverage people
You cannot use --coverage with parallel tests. Running in serial mode.

Starting node tests...
/home/zulipdev/zulip/frontend_tests/zjsunit/index.js:3
cov_aoveywdim().s[16]++;throw new Error("simulate index.js does not wanna play today");// Create a helper function to avoid sneaky delays in tests.
                        ^

Error: simulate index.js does not wanna play today
    at Object.<anonymous> (/home/zulipdev/zulip/frontend_tests/zjsunit/index.js:3:31)

**Steve Howell** · 2022-01-07 16:09 UTC

Ok, you can completely exonerate `index.js` from doing anything funny by making it a single-line program:

~~~
$ cat frontend_tests/zjsunit/index.js
throw new Error("simulate index.js just throws an error");
(zulip-py3-venv) ~/zulip (node_stack)
$ ./tools/test-js-with-node --coverage people
You cannot use --coverage with parallel tests. Running in serial mode.

Starting node tests...
/home/zulipdev/zulip/frontend_tests/zjsunit/index.js:2
cov_aoveywdim=function(){return actualCoverage;};}return actualCoverage;}cov_aoveywdim();cov_aoveywdim().s[0]++;throw new Error("simulate index.js just throws an error");
                                                                                                                ^

Error: simulate index.js just throws an error
    at Object.<anonymous> (/home/zulipdev/zulip/frontend_tests/zjsunit/index.js:2:119)

**Steve Howell** · 2022-01-07 16:10 UTC

And if you take `nyc` out of the equation, things are back to normal:

~~~
$ ./tools/test-js-with-node people
Starting node tests...
/home/zulipdev/zulip/frontend_tests/zjsunit/index.js:1
throw new Error("simulate index.js just throws an error");
^

Error: simulate index.js just throws an error
    at Object.<anonymous> (/home/zulipdev/zulip/frontend_tests/zjsunit/index.js:1:7)

**Steve Howell** · 2022-01-07 16:30 UTC

Ok, let's just take `test-js-with-node` completely out of the equation:

[image.png](https://chat.zulip.org/user_uploads/2/6a/JIYwuCFC0FqiKafJDY_JErmA/image.png)

**Steve Howell** · 2022-01-07 16:38 UTC

And it looks like the only transpilation noise here is from `nyc` itself adding instrumentation:


cov_2lltoxcv55=function(){return actualCoverage;};}return actualCoverage;}cov_2lltoxcv55();cov_2lltoxcv55().s[0]++;console.info("1");cov_2lltoxcv55().s[1]++;console.info("2");cov_2lltoxcv55().s[2]++;console.info("3");cov_2lltoxcv55().s[3]++;throw new Error("bla");cov_2lltoxcv55().s[4]++;console.info("never reached");

**Steve Howell** · 2022-01-07 16:53 UTC

Ok, I think I have a plan, but gotta think about it a bit.

**Steve Howell** · 2022-01-07 20:18 UTC

#20716

**Steve Howell** · 2022-01-07 20:44 UTC

re-pushing due to puppeteer flake


## node --coverage control-c

*2022-01-07 to 2022-01-08 · 8 messages · [open in Zulip](https://chat.zulip.org/#narrow/channel/18-tools/topic/node.20--coverage.20control-c/with/1306234)*

**Steve Howell** · 2022-01-07 20:33 UTC

It appears that `nyc` does not support control-C, so I filed an issue: https://github.com/istanbuljs/nyc/issues/1442

**Steve Howell** · 2022-01-07 20:39 UTC

Since our `--coverage` option is just a thin wrapper around `nyc`, if we want to terminate the grandchild process, our Python wrapper needs to either find the pid of the process on its own, or we need to somehow tell the grandchild to terminate itself.

In our normal mode, we are running `node` directly, and killing the process is trivial.

**Yash RE** · 2022-01-08 02:50 UTC

I was suspicious that this was the case, thanks for filing the issue.

**Steve Howell** · 2022-01-08 02:52 UTC

To be clear, we can probably work around this with about 15 lines of code, but it’s kinda ugly.

**Yash RE** · 2022-01-08 02:52 UTC

yeah

**Anders Kaseorg** · 2022-01-08 02:54 UTC

[c8](https://github.com/bcoe/c8) might work better. It doesn’t have that issue, at least.

**Steve Howell** · 2022-01-08 02:55 UTC

Yeah, c8 is definitely worth exploring.

**Steve Howell** · 2022-01-08 06:22 UTC

see #**tools>__Rewire__**


## __Rewire__

*2022-01-08 to 2022-01-11 · 174 messages · [open in Zulip](https://chat.zulip.org/#narrow/channel/18-tools/topic/__Rewire__/with/1306662)*

**Anders Kaseorg** · 2022-01-08 02:57 UTC

I switched zulipbot to c8 for native ES modules support, which we could also take advantage of if we got rid of `__Rewire__`.

**Steve Howell** · 2022-01-08 03:55 UTC

It would be a good start to at least confine the direct uses of  `__Rewire__` to `frontend_tests/zjsunit/namespace.js`, and we're not that far:

~~~
$ git grep __Rewire | grep -v namespace.js | wc -l
32

**Anders Kaseorg** · 2022-01-08 04:02 UTC

I don’t think confining `__Rewire__` to `namespace.js` gets us closer to removing it. If anything, wrapping it in functions that look pretty normalizes and encourages its further use.

**Steve Howell** · 2022-01-08 04:04 UTC

I kinda disagree. If everything that goes through `__Rewire__` instead goes through something like `with_overrides`, then that allows you to re-formulate the problem.

**Anders Kaseorg** · 2022-01-08 04:04 UTC

Anyway, I think I understand the `nyc` issue. `nyc` installs a signal handler so it can write coverage data when the program is terminated by a signal. But since JS is single-threaded, if it’s in the middle of a long block of computation or synchronous I/O, it’s not allowed to enter the signal handler until that completes.

Demo:

```js
process.once("SIGINT", () => {
  console.log("got SIGINT, reraising");
  process.kill(process.pid, "SIGINT");
});

for (let i = 0; i < 2e9; ++i) if (i % 1e8 == 0) console.log(i);

console.log("sleeping");
setTimeout(() => {
  console.log("done");
}, 1000);
```

**Anders Kaseorg** · 2022-01-08 04:05 UTC

There is no re-formulation of `__Rewire__`. We need to individually fix every test that uses it (directly or indirectly) to work a different way.

**Anders Kaseorg** · 2022-01-08 04:10 UTC

But since `with_overrides` magically decides whether or not to use `__Rewire__`, we don’t even know how many tests there are to be fixed, and we aren’t discouraging in any way the addition of new tests that will need to be fixed.

**Steve Howell** · 2022-01-08 04:15 UTC

There's no magic.  The only thing that `with_overrides` does to determine whether or not to use `__Rewire__` is see if the object claims to use `__Rewire__`.  It's like you're saying its magical to climb on a horse to expect it to run like a horse because it has a long nose and neighs.

**Anders Kaseorg** · 2022-01-08 04:17 UTC

It’s not important whether you call it magic. The point is, to decide whether a test that uses `with_overrides` is indirectly using `__Rewire__`, you need to examine the particular way in which `with_overrides` is used. There is no simple syntactic distinction we could use to grep for tests indirectly using `__Rewire__`.

**Steve Howell** · 2022-01-08 04:21 UTC

I think you confine all direct calls to `__Rewire__` to go through either `with_fields` or `with_overrides`, then you change the problem to be searching for `with_*`, which can be clarifying.

**Anders Kaseorg** · 2022-01-08 04:22 UTC

The reason that’s not clarifying is that you’re lumping it together with *other* uses of `with_fields` and `with_overrides` that do not use `__Rewire__` and will not need fixes.

**Steve Howell** · 2022-01-08 04:23 UTC

But if the goal is to eliminate `__Rewire__`, won't a solution be easier if there's a single (well, double) abstraction layer that everything funnels through?

**Anders Kaseorg** · 2022-01-08 04:24 UTC

No, because again, we can’t make a single fix to the abstraction layer to avoid using `__Rewire__`, we need to make individual fixes at all the individual call sites.

**Anders Kaseorg** · 2022-01-08 04:25 UTC

The thing that `__Rewire__` does is fundamentally impossible in vanilla JS. Module bindings are supposed to be immutable. The only reason `__Rewire__` works is that we have this expensive buggy Babel plugin that we’d like to get rid of.

**Steve Howell** · 2022-01-08 04:25 UTC

That premise only makes sense in a world where transpilation is required and `__Rewire__` is the only solution that people can imagine.

**Anders Kaseorg** · 2022-01-08 04:29 UTC

I don’t understand? Clearly `__Rewire__` is not the only solution to the general problem of “I want to test this functionality in Zulip”. But it is the only solution to the specific problem of “I want to mutate this immutable ES module binding”.

**Steve Howell** · 2022-01-08 04:29 UTC

The whole notion that "module bindings are supposed to be immutable" is an artificial constraint, especially in a testing environment in a dynamic language.  It doesn't even make sense in supposedly static languages in testing environments.  C is static as hell and it has dynamic linking.

**Anders Kaseorg** · 2022-01-08 04:32 UTC

What are you proposing? We should convince the ECMAScript committee to change how module bindings work? We should write a custom Node.js patch? Obviously we could do these things, but that doesn’t make them good ideas.

**Steve Howell** · 2022-01-08 04:33 UTC

We don't need to convince committees of anything.  It's a completely solvable problem now.

**Anders Kaseorg** · 2022-01-08 04:33 UTC

I’m listening.

**Steve Howell** · 2022-01-08 04:34 UTC

We have a transpiler system.  When it needs static bindings, it makes them static.  When it needs dynamic bindings, it makes them dynamic.

**Anders Kaseorg** · 2022-01-08 04:35 UTC

That’s what babel-plugin-rewire-ts is.

**Steve Howell** · 2022-01-08 04:35 UTC

Exactly.

**Anders Kaseorg** · 2022-01-08 04:35 UTC

It’s buggy and expensive and I want to get rid of it.

**Steve Howell** · 2022-01-08 04:37 UTC

Is it intrinsically buggy and expensive, or is it just a bad implementation?

**Steve Howell** · 2022-01-08 04:38 UTC

The fundamental concept seems fine to me.  When module A calls something from module B, dynamically call it though B.

**Anders Kaseorg** · 2022-01-08 04:39 UTC

It’s possible that some improvements could be made, but it will never be as good as not having it, and fixing our tests is a much better return on investment.

**Steve Howell** · 2022-01-08 04:40 UTC

But there's nothing fundamentally wrong with the test themselves.  It's like your blaming the tests for wanting to drive the car when ECMA committee designed a perfectly good horse.

**Steve Howell** · 2022-01-08 04:40 UTC

It's just mocking.

**Steve Howell** · 2022-01-08 04:40 UTC

I have almost have the horse/car metaphor in reverse.

**Anders Kaseorg** · 2022-01-08 04:41 UTC

We can still do module mocking; `rewiremock` is fine. Jest has equivalent functionality that we can migrate to if we decide to go with Jest.

**Anders Kaseorg** · 2022-01-08 04:43 UTC

The thing we should avoid is trying to treat immutable module bindings as if they’re mutable. If we want to mutate something, we should just export helper functions for mutating it.

**Anders Kaseorg** · 2022-01-08 04:45 UTC

I think this will make the tests clearer, since we won’t be lying to ourselves about immutability. You might disagree and think the lie is convenient. But either way, it will definitely make our code more compatible with the tooling that’s available, and even if one might imagine a world where other tooling is better, that world isn’t this world.

**Steve Howell** · 2022-01-08 04:50 UTC

I can live in a world where all tooling is perfect, and you can live in a world where the entire Legacy Zulip Codebase has been carefully constructed to export helper functions, and we can both live in a world with unicorns and leprechauns.

I have no opposition to exporting helper functions.  Have at it.

**Steve Howell** · 2022-01-08 04:52 UTC

It's very simple conceptually to make module bindings mutable.  It basically comes for nothing in a real-world module system, which was clearly possible to build with 2015 technology (outside the scope of Zulip).  It's indirection.  It's a vtable.

**Anders Kaseorg** · 2022-01-08 04:57 UTC

I think I’ve already clarified that my argument is not that there’s a conceptual difficulty with mutable bindings.

**Steve Howell** · 2022-01-08 05:01 UTC

(replying to Anders Kaseorg)
> It’s possible that some improvements could be made, but it will never be as good as not having it, and fixing our tests is a much better return on investment.

Is this the crux of your argument?  (I think you clarified later that fixing the tests requires at least some fixing of the actual code itself.)

**Anders Kaseorg** · 2022-01-08 05:02 UTC

Sure.

**Anders Kaseorg** · 2022-01-08 05:06 UTC

I’d have thought you’d be more excited about removing an expensive transpilation step. I know you want to get back to the days where the Node tests ran in four seconds; I think this is the biggest blocker.

**Steve Howell** · 2022-01-08 05:07 UTC

My challenge to you, and I sincerely don't mean this is in a sarcastic or rhetorical way, is to just show me an example.  Fish around for a couple places where we use `__Rewire__` now, and fix them.  Ideally the PR would have two commits:
* one just fixes a truly-dumbly written test
* another re-structrures the "real" code to fix a dumb-but-pragmatic test

**Steve Howell** · 2022-01-08 05:11 UTC

(replying to Anders Kaseorg)
> I’d have thought you’d be more excited about removing an expensive transpilation step. I know you want to get back to the days where the Node tests ran in four seconds; I think this is the biggest blocker.

I love transpilation, and it has made our codebase much better (largely due to you).  Transpilation doesn't have to be expensive.  Even compilation can be cheap.  You can cache it.  All I'm saying is that we're transpiling to an underlying language that's completely dynamic, and it's not the most of esoteric of languages, it's fricking JavaScript.

**Anders Kaseorg** · 2022-01-08 05:12 UTC

Right, most of our transpilation is standard stuff that will probably eventually be migrated to Rust. The biggest reason babel-plugin-rewire-ts is expensive is that it writes code that’s expensive at runtime.

**Steve Howell** · 2022-01-08 05:14 UTC

(replying to Anders Kaseorg)
> Right, most of our transpilation is standard stuff that will probably eventually be migrated to Rust.

Heh, yeah, I like that vision.

> The biggest reason babel-plugin-rewire-ts is expensive is that it writes code that’s expensive at runtime.
Is that actually true?

**Anders Kaseorg** · 2022-01-08 05:14 UTC

It replaces every global variable access with a function call.

**Steve Howell** · 2022-01-08 05:15 UTC

(replying to Anders Kaseorg)
> It replaces every global variable access with a function call.
But how expensive are function calls?

**Steve Howell** · 2022-01-08 05:17 UTC

Or how inexpensive are JS variable accesses?

**Anders Kaseorg** · 2022-01-08 05:18 UTC

Function calls are certainly more expensive than not having function calls. Indirection isn’t free unless it can be optimized away, and this definitely can’t be optimized away because it’s fundamentally replacing an access that was static with something that’s actually dynamic and really will change. I can’t say that I’ve done a detailed benchmark.

**Anders Kaseorg** · 2022-01-08 05:24 UTC

The slowdown is at least a factor of 80× on this microbenchmark:

```js
let i;
for (i = 0; i < 1e8; i++);
```

**Anders Kaseorg** · 2022-01-08 05:25 UTC

I was going to paste in the result of transpiling that, but uh, I hit the 10000 character message limit.

**Anders Kaseorg** · 2022-01-08 05:26 UTC

[transpiled.js](https://chat.zulip.org/user_uploads/2/88/zIulqQZ7_DClUCHcSi9Nragy/transpiled.js)

**Steve Howell** · 2022-01-08 05:30 UTC

I guess if we wanted a true benchmark, we could hack `__Rewire__` to do something like triple function calls to make the overhead stand out more.  My intuition is that it's not the real bottleneck, and it's not like our tests our super slow now.

**Steve Howell** · 2022-01-08 05:31 UTC

Once the node tests actually get around to running the transpiled code, I believe they're generally fast, even if the transpiled code is slightly chunkier than it should be.

**Anders Kaseorg** · 2022-01-08 05:34 UTC

This transpilation isn’t just a chunky wrapper around equivalently fast code. It sprinkles function calls *everywhere*.

```js
for (_assign__("i", 0); _get__("i") < 1e8; _update_operation__("++", "i", false)) {
  ;
}
```

**Steve Howell** · 2022-01-08 05:37 UTC

That's from `__Rewire__`?

**Anders Kaseorg** · 2022-01-08 05:37 UTC

Yes, it’s from babel-plugin-rewire-ts. (I haven’t actually called `__Rewire__` anywhere, just done the transpilation needed to make it so I could.)

**Steve Howell** · 2022-01-08 05:40 UTC

What happens with this?:

~~~
function foo() {
  let i;
  for (i = 0; i < 1e8; i++);
}
const bar = foo;
const zed = bar;
zed()

**Anders Kaseorg** · 2022-01-08 05:42 UTC

That `i` isn’t global, so it won’t be replaced. But `foo`, `bar`, and `zed` will be.

```js
function foo() {
  var i;

  for (i = 0; i < 1e8; i++) {
    ;
  }
}

var bar = _get__("foo");
var zed = _get__("bar");
_get__("zed")();
```

**Steve Howell** · 2022-01-08 05:43 UTC

My hunch is that the slowdown for this is a bit less than 80x?

**Anders Kaseorg** · 2022-01-08 05:45 UTC

I don’t think it will be 80× in our actual tests, but 2× wouldn’t shock me at all. Most of our tests are testing that functions call other functions that call other functions, and since each function is itself a global variable, each function call gets doubled.

**Steve Howell** · 2022-01-08 05:48 UTC

(replying to Anders Kaseorg)
> Most of our tests are testing that functions call other functions that call other functions [...]

That's not true.  Most of our node tests call functions all the way down the stack and don't mock.

**Anders Kaseorg** · 2022-01-08 05:49 UTC

I didn’t intend to imply that they were mocked.

**Steve Howell** · 2022-01-08 05:49 UTC

Maybe I misunderstood your wording then.

**Anders Kaseorg** · 2022-01-08 05:50 UTC

Not important. Point is, we have lots of function calls, and they’re all getting doubled.

**Steve Howell** · 2022-01-08 05:51 UTC

Fair enough, but I still contend that most of our individual tests are plenty fast. I would challenge you to a case study of one of our slowest tests, which is `buddy_data.js`.  It's slow because at least one of our tests does a big loop over 1000 things.

**Steve Howell** · 2022-01-08 05:53 UTC

We could probably fix it by investigating the transpiled code for this:

~~~
152 function set_presence(user_id, status) {
153     presence.presence_info.set(user_id, {
154         status,
155         last_active: 9999,
156     });
157 }

**Anders Kaseorg** · 2022-01-08 05:54 UTC

~~That’s going to compile to `__get_("presence").presence_info.set(…)`.~~

**Anders Kaseorg** · 2022-01-08 05:55 UTC

~~And any call to `set_presence` is going to compile to a `__get_` as well.~~ (Edit: this is not transpiled because it’s in the test code.)

**Steve Howell** · 2022-01-08 05:55 UTC

which you could probably pull out of the loop

**Anders Kaseorg** · 2022-01-08 05:56 UTC

Do you really want to start cluttering our code with local copies of global variables just because global variables are slow in our tests?

**Steve Howell** · 2022-01-08 05:57 UTC

(replying to Anders Kaseorg)
> Do you really want to start cluttering our code with local copies of global variables just because global variables are slow in our tests?

Well, in this case, I think you could do that in the test, not the actual code, for the one node test that actually takes more than half a second to run.

**Anders Kaseorg** · 2022-01-08 05:58 UTC

Only the actual code is transpiled with babel-plugin-rewire-ts, not the tests (the tests don’t need to mock themselves).

**Anders Kaseorg** · 2022-01-08 05:58 UTC

The tests [aren’t](https://github.com/zulip/zulip/blob/f97093ba327e92ea3847fa2f5f7ac280d5ccf0ba/frontend_tests/zjsunit/index.js#L23-L28) transpiled at all.

**Steve Howell** · 2022-01-08 05:59 UTC

The reason that the tests call `presence.presence_info.set(user_id)` is that we haven't exported a helper function like `presence.set_user_as_present(user_id)`.

**Steve Howell** · 2022-01-08 06:04 UTC

Here's a more concrete example:

~~~
406 test("bulk_data_hacks", () => {
407     // sanity check
408     assert.equal(mark.user_id, 1005);
409
410     for (const i of _.range(mark.user_id + 1, 2000)) {
411         const person = {
412             user_id: i,
413             full_name: `Human ${i}`,
414             email: `person${i}@example.com`,
415         };
416         people.add_active_user(person);
417     }

**Anders Kaseorg** · 2022-01-08 06:04 UTC

(Perhaps I should clarify `presence.presence_info.set()` is still allowed in the immutable bindings world. The thing that would be disallowed is `presence.presence_info = …`.)

**Steve Howell** · 2022-01-08 06:06 UTC

We do do that, unfortunately:

~~~
123     let presence_info = new Map();
124     presence_info.set(alice.user_id, {status: "active"}); // counts as present
125     presence_info.set(fred.user_id, {status: "idle"}); // does not count as present
126     // jill not in list
127     presence_info.set(mark.user_id, {status: "offline"}); // does not count
128     presence.__Rewire__("presence_info", presence_info);

**Anders Kaseorg** · 2022-01-08 06:06 UTC

Indeed. That should be easy to fix though—we can run `presence.presence_info.clear()` and add whatever we want to it without reassigning it.

**Steve Howell** · 2022-01-08 06:07 UTC

(replying to Anders Kaseorg)
> Indeed. That should be easy to fix though—we can run `presence.presence_info.clear()` and add whatever we want to it without reassigning it.

Exactly.

**Steve Howell** · 2022-01-08 06:08 UTC

We actually do the `clear` in the test wrapper:

~~~
 98 function test(label, f) {
 99     run_test(label, ({override}) => {
100         user_settings.presence_enabled = true;
101         compose_fade_helper.clear_focused_recipient();
102         stream_data.clear_subscriptions();
103         peer_data.clear_for_testing();
104         user_status.initialize({user_status: {}});
105         presence.presence_info.clear();
106         people.init();
107         people.add_active_user(me);
108         people.initialize_current_user(me.user_id);
109         muted_users.set_muted_users([]);
110         f({override});
111     });
112 }

**Steve Howell** · 2022-01-08 06:08 UTC

(line 105)

**Steve Howell** · 2022-01-08 06:10 UTC

Going back to my earlier challenge, I would ask you to carve out a few hours to knock out a few things.  You would probably enjoy it more than talking to me, haha!  (We are a few hours into this convo, and I am seriously enjoying it and learning from it, but you know what I mean.)

**Steve Howell** · 2022-01-08 06:11 UTC

The `buddy_data` module isn't super complex, but the test is a bit hairy.

**Steve Howell** · 2022-01-08 06:11 UTC

But even the test isn't super strange.  It's just slinging data around.

**Anders Kaseorg** · 2022-01-08 06:12 UTC

Unfortunately, I also have a lot of less fun stuff to do. But I’m hoping we can agree on a vague direction.

**Steve Howell** · 2022-01-08 06:12 UTC

I think we have the same overall goals.

**Steve Howell** · 2022-01-08 06:14 UTC

I know you have plenty on your plate, but I think your time would be well leveraged at some point to just spend a couple hours killing off `presence.__Rewire__(...)` in `buddy_data.js`, if it does nothing else but avoid us re-hashing the same issue (as well as giving us some examples to build on).

**Anders Kaseorg** · 2022-01-08 06:20 UTC

Here’s an experiment that’s easy to do: if I just take the subset of tests that miraculously pass without `babel-plugin-rewire-ts` already, removing `babel-plugin-rewire-ts` seems to make those tests run about 40% faster on a cold cache and 20% faster on a warm cache.

**Steve Howell** · 2022-01-08 06:25 UTC

Fair enough, but I don't find that super compelling.  You're sampling for the tests that get zero benefit from the overall strategy, and you're proving that they're sacrificing for the greater good at about a 30% penalty.

**Steve Howell** · 2022-01-08 06:27 UTC

I would guess there's at least one outlier in there that kinda distorts the results.  (Maybe "distorts the results" is a little strong, but I bet we could find a particular test that just suffers particularly badly from function overhead, and just fix it.)

**Steve Howell** · 2022-01-08 06:30 UTC

I don't really mind colorful language for rhetorical purposes, since I often engage it in myself, but "miraculously passes"?  There are no miracles here.  Obviously any module that we choose to test without mocking is not gonna require the rewire plugin.

**Steve Howell** · 2022-01-08 06:30 UTC

And it will therefore run successfully.

**Anders Kaseorg** · 2022-01-08 06:39 UTC

I see no reason to suspect the slowdown is concentrated in a small number of tests. (And if it were the case that the slowdown in a small number of tests is *so egregious* as to account for 30% of the *overall* total, does that really make it better?)

**Steve Howell** · 2022-01-08 06:42 UTC

Maybe I don't understand your experiment.

**Steve Howell** · 2022-01-08 06:43 UTC

Did you do this?
* run something to find all tests that don't require the plugin
* eliminate all other tests
* run the non-mocked tests with the plugin
* run the non-mocked tests without the plugin

**Anders Kaseorg** · 2022-01-08 06:44 UTC

Yeah.

`tools/test-js-with-node alert_words billing_helpers blueslip_stacktrace bot_data buddy_list channel colorspace components compose_closed_ui compose_error compose_fade compose_state compose_video copy_and_paste deprecated_feature_notice dispatch_subs dropdown_list_widget emoji emoji_picker event_status example1 example2 example3 example4 example5 example6 example7 fenced_code fetch_status filter fold_dict hash_util hashchange i18n keydown_util lazy_set linkifiers list_cursor list_widget message_edit message_events message_fetch message_list message_list_data message_list_view message_store muting narrow_activate narrow_state navbar_alerts notifications password peer_data pill_typeahead pm_conversations poll_widget presence recent_senders reload_state rendered_markdown rtl schema scroll_util search_pill server_events settings_bots settings_config settings_data settings_emoji settings_profile_fields spoilers stream_data stream_pill stream_settings_ui stream_sort stream_topic_history submessage support templates timerender top_left_corner topic_generator topic_list_data typeahead typeahead_helper typing_data unread user_events user_group_pill user_groups user_pill user_search user_status util vdom watchdog widgetize zblueslip zjquery`

before and after

```diff
--- a/frontend_tests/zjsunit/index.js
+++ b/frontend_tests/zjsunit/index.js
@@ -27,7 +27,6 @@ require("@babel/register")({
         ),
     ],
     plugins: [
-        "babel-plugin-rewire-ts",
         ["@babel/plugin-transform-modules-commonjs", {lazy: () => true}],
     ],
 });
```

**Steve Howell** · 2022-01-08 06:45 UTC

What are the wall times?

**Steve Howell** · 2022-01-08 06:46 UTC

I would run with `--parallel 1` just to eliminate one possible red herring.

**Anders Kaseorg** · 2022-01-08 06:47 UTC

Approximately 14.3s vs. 10.2s on a cold cache, and 6.5s vs 5.1s on a warm cache. Passing specific tests already implies `--parallel 1`.

**Anders Kaseorg** · 2022-01-08 06:48 UTC

(Cache being `node_modules/.cache/@babel/register`.)

**Steve Howell** · 2022-01-08 06:48 UTC

Any outliers among the tests?

**Anders Kaseorg** · 2022-01-08 06:48 UTC

I don’t have individual test timings, but visually there don’t seem to be particular outliers.

**Steve Howell** · 2022-01-08 06:51 UTC

If you have 99 files running in 6.5s, the average test takes 65ms, so it's kinda hard to see visual slowness.

**Anders Kaseorg** · 2022-01-08 06:52 UTC

Yeah, and also hard to measure even if I had the timings. But I know there isn’t one test that takes a whole second on a warm cache, for example.

**Steve Howell** · 2022-01-08 06:54 UTC

Do you know the JS equiv of `t = time.time(); ...; duration = time.time() - t` off the top of your head?

**Steve Howell** · 2022-01-08 06:54 UTC

to wrap around ` run_one_module(file);`

**Steve Howell** · 2022-01-08 06:57 UTC

diff coming

**Anders Kaseorg** · 2022-01-08 06:57 UTC

The slowest test in this run was 133 ms.

**Steve Howell** · 2022-01-08 06:59 UTC

~~~
$ git diff
diff --git a/frontend_tests/zjsunit/index.js b/frontend_tests/zjsunit/index.js
index 98dfa25c99..30fb22d469 100644
--- a/frontend_tests/zjsunit/index.js
+++ b/frontend_tests/zjsunit/index.js
@@ -73,7 +73,7 @@ require("../../static/js/templates"); // register Zulip extensions
 function run_one_module(file) {
     zjquery.clear_initialize_function();
     zjquery.clear_all_elements();
-    console.info("running test " + path.basename(file, ".js"));
+    // console.info("running test " + path.basename(file, ".js"));
     test.set_current_file_name(file);
     require(file);
     namespace.complain_about_unused_mocks();
@@ -105,7 +105,10 @@ try {
         namespace.mock_esm("../../static/js/realm_user_settings_defaults", zpage_params);
         require("../../static/js/realm_user_settings_defaults");

+        const t0 = performance.now();
         run_one_module(file);
+        const t1 = performance.now();
+        console.log(`${t1 - t0} milliseconds for ${file}.`);

         if (blueslip.reset) {
             blueslip.reset();

**Anders Kaseorg** · 2022-01-08 07:01 UTC

It was `i18n`. Removing `babel-plugin-rewire-ts` has no particular effect on its speed (136 ms).

**Steve Howell** · 2022-01-08 07:02 UTC

This isn't specifically relevant to our discussion, but it's kinda odd how little of a long-tail effect we have:

~~~
$ ./tools/test-js-with-node | sort -n | tail -30
200.34779357910156 milliseconds for /home/zulipdev/zulip/frontend_tests/node_tests/bot_data.js.
207.6830596923828 milliseconds for /home/zulipdev/zulip/frontend_tests/node_tests/buddy_list.js.
209.41170120239258 milliseconds for /home/zulipdev/zulip/frontend_tests/node_tests/echo.js.
210.25925827026367 milliseconds for /home/zulipdev/zulip/frontend_tests/node_tests/rendered_markdown.js.
210.71217346191406 milliseconds for /home/zulipdev/zulip/frontend_tests/node_tests/stream_list.js.
211.20136642456055 milliseconds for /home/zulipdev/zulip/frontend_tests/node_tests/pill_typeahead.js.
212.16405868530273 milliseconds for /home/zulipdev/zulip/frontend_tests/node_tests/stream_topic_history.js.
219.54312133789062 milliseconds for /home/zulipdev/zulip/frontend_tests/node_tests/alert_words.js.
225.56795501708984 milliseconds for /home/zulipdev/zulip/frontend_tests/node_tests/copy_and_paste.js.
228.17451858520508 milliseconds for /home/zulipdev/zulip/frontend_tests/node_tests/settings_muted_users.js.
229.31959915161133 milliseconds for /home/zulipdev/zulip/frontend_tests/node_tests/compose_actions.js.
229.96519088745117 milliseconds for /home/zulipdev/zulip/frontend_tests/node_tests/popovers.js.
234.03579330444336 milliseconds for /home/zulipdev/zulip/frontend_tests/node_tests/billing_helpers.js.
255.2539520263672 milliseconds for /home/zulipdev/zulip/frontend_tests/node_tests/hashchange.js.
265.1624946594238 milliseconds for /home/zulipdev/zulip/frontend_tests/node_tests/message_fetch.js.
286.6225700378418 milliseconds for /home/zulipdev/zulip/frontend_tests/node_tests/dispatch.js.
292.7466506958008 milliseconds for /home/zulipdev/zulip/frontend_tests/node_tests/narrow.js.
309.8213653564453 milliseconds for /home/zulipdev/zulip/frontend_tests/node_tests/typeahead_helper.js.
310.29996490478516 milliseconds for /home/zulipdev/zulip/frontend_tests/node_tests/stream_edit.js.
320.9191665649414 milliseconds for /home/zulipdev/zulip/frontend_tests/node_tests/muting.js.
330.72377014160156 milliseconds for /home/zulipdev/zulip/frontend_tests/node_tests/i18n.js.
343.1552543640137 milliseconds for /home/zulipdev/zulip/frontend_tests/node_tests/search_suggestion_legacy.js.
377.97934341430664 milliseconds for /home/zulipdev/zulip/frontend_tests/node_tests/compose_validate.js.
420.2076835632324 milliseconds for /home/zulipdev/zulip/frontend_tests/node_tests/drafts.js.
448.39171981811523 milliseconds for /home/zulipdev/zulip/frontend_tests/node_tests/search_suggestion.js.
555.272331237793 milliseconds for /home/zulipdev/zulip/frontend_tests/node_tests/compose.js.
609.6618347167969 milliseconds for /home/zulipdev/zulip/frontend_tests/node_tests/composebox_typeahead.js.
772.4026031494141 milliseconds for /home/zulipdev/zulip/frontend_tests/node_tests/activity.js.
1203.4907913208008 milliseconds for /home/zulipdev/zulip/frontend_tests/node_tests/markdown.js.
1448.3049201965332 milliseconds for /home/zulipdev/zulip/frontend_tests/node_tests/buddy_data.js.

**Anders Kaseorg** · 2022-01-08 07:03 UTC

It’s hard to say anything much more concrete with all this noise. You’re welcome to try a more detailed analysis if you want. But it seems clear at least that the overhead is not concentrated in just a few of the slowest tests.

**Steve Howell** · 2022-01-08 07:07 UTC

Yeah, the 99 files is a bigger sampler size than I expected, and the fact that we don't have any truly egregious outliers definitely supports your thesis as well.

**Steve Howell** · 2022-01-08 07:08 UTC

We shouldn't get distracted from the main point that we both agree that there are clear reasons to avoid `__Rewire__`, and some of it is just gonna be grunt work that's beneath both of our pay grades, haha.

**Steve Howell** · 2022-01-08 07:10 UTC

with plugin (top 10 slowest)

~~~
168.6056251525879 milliseconds for /home/zulipdev/zulip/frontend_tests/node_tests/filter.js.
179.8735237121582 milliseconds for /home/zulipdev/zulip/frontend_tests/node_tests/message_fetch.js.
181.9219093322754 milliseconds for /home/zulipdev/zulip/frontend_tests/node_tests/billing_helpers.js.
182.13512802124023 milliseconds for /home/zulipdev/zulip/frontend_tests/node_tests/hashchange.js.
188.11119842529297 milliseconds for /home/zulipdev/zulip/frontend_tests/node_tests/stream_data.js.
191.27273559570312 milliseconds for /home/zulipdev/zulip/frontend_tests/node_tests/example5.js.
201.65106582641602 milliseconds for /home/zulipdev/zulip/frontend_tests/node_tests/typeahead_helper.js.
265.85093688964844 milliseconds for /home/zulipdev/zulip/frontend_tests/node_tests/message_list_view.js.
287.9731025695801 milliseconds for /home/zulipdev/zulip/frontend_tests/node_tests/i18n.js.
314.91796493530273 milliseconds for /home/zulipdev/zulip/frontend_tests/node_tests/user_search.js.

**Anders Kaseorg** · 2022-01-08 07:11 UTC

Okay. My proposed first step would be to split the `with_field` and `override` APIs into halves that use `__Rewire__` and halves that don’t, so we can grep for the callers that do, and we have a way to measure the scale of the problem.

**Steve Howell** · 2022-01-08 07:12 UTC

without plugin:

~~~
142.7454376220703 milliseconds for /home/zulipdev/zulip/frontend_tests/node_tests/example2.js.
144.06861877441406 milliseconds for /home/zulipdev/zulip/frontend_tests/node_tests/stream_topic_history.js.
146.78477478027344 milliseconds for /home/zulipdev/zulip/frontend_tests/node_tests/unread.js.
147.60385513305664 milliseconds for /home/zulipdev/zulip/frontend_tests/node_tests/alert_words.js.
158.708984375 milliseconds for /home/zulipdev/zulip/frontend_tests/node_tests/pill_typeahead.js.
169.49462509155273 milliseconds for /home/zulipdev/zulip/frontend_tests/node_tests/billing_helpers.js.
183.36732864379883 milliseconds for /home/zulipdev/zulip/frontend_tests/node_tests/example5.js.
221.38972091674805 milliseconds for /home/zulipdev/zulip/frontend_tests/node_tests/typeahead_helper.js.
233.49700546264648 milliseconds for /home/zulipdev/zulip/frontend_tests/node_tests/i18n.js.
278.75306701660156 milliseconds for /home/zulipdev/zulip/frontend_tests/node_tests/message_list_view.js.

**Steve Howell** · 2022-01-08 07:15 UTC

(replying to Anders Kaseorg)
> Okay. My proposed first step would be to split the `with_field` and `override` APIs into halves that use `__Rewire__` and halves that don’t, so we can grep for the callers that do, and we have a way to measure the scale of the problem.
I feel like that's unnecessary since you were obviously able to identify the split with some quick hacking.

**Anders Kaseorg** · 2022-01-08 07:16 UTC

All I did was run all the tests and check which ones pass. This doesn’t give me a way to identify specific call sites.

**Anders Kaseorg** · 2022-01-08 07:19 UTC

And it doesn’t give us an easy way to spot new uses of `__Rewire__` in code review and ask people not to add new tests that rely on it.

**Steve Howell** · 2022-01-08 07:19 UTC

Maybe I'm confused, but we still have 32 uses of `__Rewire__` in the tests themselves.

**Steve Howell** · 2022-01-08 07:20 UTC

That seems like the low hanging fruit to me for research/demonstration purposes.

**Anders Kaseorg** · 2022-01-08 07:23 UTC

I don’t see what further research is required there. We’ve talked about how to remove the direct `__Rewire__`s from `buddy_data`, for example. There’s no fundamental obstacle to removing any of them. I just want to know how many there will be.

**Anders Kaseorg** · 2022-01-08 07:24 UTC

And I want to know that others won’t be adding them while we try to remove them.

**Steve Howell** · 2022-01-08 07:26 UTC

BTW, for me, wall times go from 9.2s -> 8.6s (removing console.log noise) on the 99 files.

**Steve Howell** · 2022-01-08 07:27 UTC

(w/warm caches)

**Steve Howell** · 2022-01-08 07:30 UTC

(replying to Anders Kaseorg)
> And I want to know that others won’t be adding them while we try to remove them.

At least for direct calls, you can do `git log -S` and peek at the authors and be confident that 2021 was all about cleaning up the problem.

**Steve Howell** · 2022-01-08 07:33 UTC

(replying to Anders Kaseorg)
> I don’t see what further research is required there. We’ve talked about how to remove the direct `__Rewire__`s from `buddy_data`, for example. There’s no fundamental obstacle to removing any of them. I just want to know how many there will be.
How many indirect calls to `__Rewire__`?  That's like a 10-minute instrumentation hack that you will do maybe three times more in your life?

**Anders Kaseorg** · 2022-01-08 07:35 UTC

What exactly are you arguing here? Is there a good reason to make this already-annoying refactoring project more annoying?

**Anders Kaseorg** · 2022-01-08 07:36 UTC

I’ve done a lot of these refactoring projects, and the first step is to construct a way to grep for the code to be refactored. Is there a reason we *shouldn’t* do this?

**Steve Howell** · 2022-01-08 07:37 UTC

I am saying that we just grep for direct calls to `__Rewire__` that haven't yet been encapsulated and fix those first.

**Anders Kaseorg** · 2022-01-08 07:37 UTC

I don’t want to solve 10% of the problem when I don’t even know how inaccurate that 10% guess is.

**Steve Howell** · 2022-01-08 07:38 UTC

As you argued, every caller to `__Rewire__`, whether indirect or direct, probably requires some case-by-case solution.  And I'm telling you that the worst 10% are the ones that haven't already been ported to `with_field` or `with_overrides`.  Because I have also done a lot of these refactoring projects.

**Anders Kaseorg** · 2022-01-08 07:39 UTC

I explained above why `with_field` and `with_overrides` don’t make this any easier.

**Anders Kaseorg** · 2022-01-08 07:40 UTC

And I don’t think any particular one will be significantly worse than any other. In the worst case, we add a three-line helper function to do the assignment.

**Anders Kaseorg** · 2022-01-08 07:41 UTC

There may be work to be saved by dealing with many similar calls at once, but that requires knowing where they are.

**Steve Howell** · 2022-01-08 07:41 UTC

But you're apparently not understanding why the 32 directs calls to `__Rewire__` are a bigger hindrance to your goals than the ~500 `override` calls that are all more sane.

**Anders Kaseorg** · 2022-01-08 07:42 UTC

Can you point to a direct `__Rewire__` that’s particularly less sane?

**Steve Howell** · 2022-01-08 07:43 UTC

https://chat.zulip.org/#narrow/stream/18-tools/topic/__Rewire__/near/1306769

**Anders Kaseorg** · 2022-01-08 07:44 UTC

That’s the one we talked about above. We write `presence.presence_info.clear()` and add stuff with `.set()`.

**Anders Kaseorg** · 2022-01-08 07:44 UTC

(Alternatively, we could add the three-line helper function, because we could always add the three-line helper function, but in this case we don’t need to.)

**Steve Howell** · 2022-01-08 07:47 UTC

~~~
924     $("#stream_message_recipient_stream").val("BOGUS STREAM");
925     message = compose.create_message_object();
926     assert.equal(message.to, "BOGUS STREAM");
927     assert.equal(message.topic, "lunch");
928     assert.equal(message.content, "burrito");
929
930     override(compose_state, "get_message_type", () => "private");
931     compose_state.__Rewire__(
932         "private_message_recipient",
933         () => "alice@example.com, bob@example.com",
934     );

**Anders Kaseorg** · 2022-01-08 07:48 UTC

That one can probably be done by mocking `compose_pm_pill`. Alternatively, three-line helper function.

**Anders Kaseorg** · 2022-01-08 07:50 UTC

Also does anything make the `get_message_type` override that indirectly uses `__Rewire__` more sane than the `private_message_recipient` override that directly uses `__Rewire__`? Surely you see why I’d likely want to deal with those two at once.

**Anders Kaseorg** · 2022-01-08 07:51 UTC

In fact elsewhere in the same test we override the same `private_message_recipient` function using `override()`.

**Steve Howell** · 2022-01-08 07:55 UTC

If your concern is hunting down situations to fix, it's an easy instrumentation hack to get something like this:

~~~
$ ./tools/test-js-with-node typing_status
Starting node tests...
running test typing_status
        test: basics
   using rewire to call <obj>.get_user_ids_string
   using rewire to call <obj>.get_user_ids_string
   using rewire to call <obj>.maybe_ping_server
   using rewire to call <obj>.start_or_extend_idle_timer
   using rewire to call <obj>.get_user_ids_string
   using rewire to call <obj>.maybe_ping_server
   using rewire to call <obj>.start_or_extend_idle_timer
   using rewire to call <obj>.get_user_ids_string
   using rewire to call <obj>.stop_last_notification
   using rewire to call <obj>.actually_ping_server
   using rewire to call <obj>.start_or_extend_idle_timer
   using rewire to call <obj>.get_user_ids_string
   using rewire to call <obj>.stop_last_notification

**Steve Howell** · 2022-01-08 07:55 UTC

~~~
$ git diff
diff --git a/frontend_tests/zjsunit/namespace.js b/frontend_tests/zjsunit/namespace.js
index 26d377006e..e64aa8e49f 100644
--- a/frontend_tests/zjsunit/namespace.js
+++ b/frontend_tests/zjsunit/namespace.js
@@ -397,7 +397,10 @@ exports.with_overrides = function (test_function) {
         new_f._patched_with_override = true;

         if ("__esModule" in obj && "__Rewire__" in obj) {
-            obj.__Rewire__(func_name, new_f);
+            obj.__Rewire__(func_name, (...args) => {
+                console.info(`   using rewire to call <obj>.${func_name}`);
+                return new_f(...args);
+            });
             restore_callbacks.push(() => {
                 obj.__Rewire__(func_name, old_f);
             });

**Anders Kaseorg** · 2022-01-08 07:59 UTC

I’ve explained what my concerns are. I want to get a high level overview of the scale of the problem. I want to be able to use `grep` to examine the call sites and the surrounding code, so as to group similar call sites and break down the problem into manageable pieces. I want to be able to give Tim a simple pattern to reject during code review that doesn’t involve applying a patch and running a command.

**Anders Kaseorg** · 2022-01-08 08:00 UTC

These are not unreasonable things to want. These are not difficult things to achieve. All I’m asking is that we agree on a very simple API tweak to enable them.

**Steve Howell** · 2022-01-08 08:03 UTC

(replying to Anders Kaseorg)
> These are not unreasonable things to want. These are not difficult things to achieve. All I’m asking is that we agree on a very simple API tweak to enable them.
Fair enough.  It's probably easiest if you just do a full PR rather than us haggle on the API too much.  This is basically about having twin versions of `with_overrides`, correct?  (so we can distinguish the rare non-ES6 cases from the vast majority)

**Anders Kaseorg** · 2022-01-08 08:04 UTC

For `with_overrides` it’s actually the `override` callback that would be twinned. We can bikeshed about how to wrangle that in the API.

**Anders Kaseorg** · 2022-01-08 08:06 UTC

I think you suggested before that we could change `with_overrides((override) => {… override() …})` to `with_overrides((t) => {… t.override() …})` so we could hang other functions there, and that would be one way to make this work.

**Steve Howell** · 2022-01-08 08:06 UTC

(replying to Anders Kaseorg)
> For `with_overrides` it’s actually the `override` callback that would be twinned. We can bikeshed about how to wrangle that in the API.

My bikeshed is that you can probably produce a pretty minimal diff if `override` handles the most common case, and then name the other twin whatever you want (or pass in some kind of ~~override~~ alternative flag).

**Steve Howell** · 2022-01-08 08:07 UTC

(replying to Anders Kaseorg)
> I think you suggested before that we could change `with_overrides((override) => {… override() …})` to `with_overrides((t) => {… t.override() …})` so we could hang other functions there, and that would be one way to make this work.

Yeah, my memory is fuzzy, but that general idea seems fine.

**Steve Howell** · 2022-01-08 08:14 UTC

Huh, it's much closer to 50/50 than I thought, if you run this patch:

~~~
$ git diff
diff --git a/frontend_tests/zjsunit/namespace.js b/frontend_tests/zjsunit/namespace.js
index 26d377006e..a1d9addda7 100644
--- a/frontend_tests/zjsunit/namespace.js
+++ b/frontend_tests/zjsunit/namespace.js
@@ -397,12 +397,18 @@ exports.with_overrides = function (test_function) {
         new_f._patched_with_override = true;

         if ("__esModule" in obj && "__Rewire__" in obj) {
-            obj.__Rewire__(func_name, new_f);
+            obj.__Rewire__(func_name, (...args) => {
+                console.info(`   using rewire to call <obj>.${func_name}`);
+                return new_f(...args);
+            });
             restore_callbacks.push(() => {
                 obj.__Rewire__(func_name, old_f);
             });
         } else {
-            obj[func_name] = new_f;
+            obj[func_name] = (...args) => {
+                console.info(`   DIRECT PATCH <obj>.${func_name}`);
+                return new_f(...args);
+            };
             restore_callbacks.push(() => {
                 obj[func_name] = old_f;
             });

**Anders Kaseorg** · 2022-01-08 08:17 UTC

Okay. All else being roughly equal, how about `override` vs. `override_rewire` and `with_field` vs. `with_field_rewire` so we can easily remember that the `_rewire` versions are deprecated?

**Steve Howell** · 2022-01-08 08:26 UTC

Yep, that's fine.

**Steve Howell** · 2022-01-08 08:32 UTC

We probably want `override_$` as well.  It's almost all in one test:

~~~
$ git grep "override($,"
frontend_tests/node_tests/billing_helpers.js:    override($, "ajax", ({type, url, data, success, error}) => {
frontend_tests/node_tests/event_status.js:    override($, "get", async (url, data) => {
frontend_tests/node_tests/event_status.js:    override($, "get", async (url, data) => {
frontend_tests/node_tests/event_status.js:    override($, "get", async (url, data) => {
frontend_tests/node_tests/event_status.js:    override($, "get", async (url, data) => {
frontend_tests/node_tests/event_status.js:    override($, "get", async (url, data) => {
frontend_tests/node_tests/event_status.js:    override($, "get", async (url, data) => {
frontend_tests/node_tests/event_status.js:    override($, "get", async (url, data) => {
frontend_tests/node_tests/event_status.js:    override($, "get", async (url, data) => {
frontend_tests/node_tests/event_status.js:    override($, "get", async (url, data) => {
frontend_tests/node_tests/event_status.js:    override($, "get", async (url, data) => {
frontend_tests/node_tests/event_status.js:    override($, "get", async (url, data) => {
frontend_tests/node_tests/event_status.js:    override($, "get", async (url, data) => {
frontend_tests/node_tests/event_status.js:    override($, "get", async (url, data) => {
frontend_tests/node_tests/event_status.js:    override($, "get", async (url, data) => {
frontend_tests/node_tests/message_list.js:    override($, "Event", (ev) => {
frontend_tests/zjsunit/zjquery.js:                override($, "${prop}", () => {...});

**Steve Howell** · 2022-01-08 08:33 UTC

(The billing system doesn't have the `channel.js` layer that the main app has.)

**Anders Kaseorg** · 2022-01-08 08:36 UTC

Dunno. That doesn’t need to interact with this, since it’s not an ESM.

**Steve Howell** · 2022-01-08 08:37 UTC

Yeah, I don't know the exact implications off the top of my head.  I just noticed there was a tiny bit of zjquery-specific code in `with_overrides`.

**Steve Howell** · 2022-01-08 08:38 UTC

~~~
394         // Let zjquery know this function was patched with override,
395         // so it doesn't complain about us modifying it.  (Other
396         // code can also use this, as needed.)
397         new_f._patched_with_override = true;

**Anders Kaseorg** · 2022-01-08 10:20 UTC

#20730

**Steve Howell** · 2022-01-08 14:37 UTC

This is awesome! https://github.com/zulip/zulip/pull/20730#discussion_r780674091

**Steve Howell** · 2022-01-08 15:01 UTC

merged

**Steve Howell** · 2022-01-08 16:44 UTC

#20732

**Steve Howell** · 2022-01-08 17:08 UTC

Where can I find the generated code for the transpiled modules?  (Or how can I output the generated code to look at it?)

**Steve Howell** · 2022-01-08 17:36 UTC

Ok, I can basically read [the plugin tests](https://github.com/speedskater/babel-plugin-rewire/blob/master/fixtures/transformation/forOf/expected.js) to figure out the mechanisms here.  Yeah, that's pretty intense.

**Steve Howell** · 2022-01-08 18:41 UTC

I hacked my local copy of the rewire plugin to see where we are getting the most `__get__` calls:

~~~
   9453 dispatch -> emoji_codes
   7366 emoji_picker -> emoji_codes
   6302 dispatch -> emojis_by_name
   6301 dispatch -> default_emoji_aliases
   5497 search_suggestion -> Filter
   5359 markdown -> emoji_codes
   5350 search_suggestion_legacy -> Filter
   5283 emoji -> emoji_codes
   5260 reactions -> emoji_codes
   5257 hotkey -> emoji_codes
   5255 user_status -> emoji_codes
   4203 user_status -> default_emoji_aliases
   4203 reactions -> default_emoji_aliases
   4203 hotkey -> default_emoji_aliases
   4203 emoji_picker -> default_emoji_aliases
   4203 emoji -> default_emoji_aliases
   4202 markdown -> default_emoji_aliases
   3147 dispatch -> get_emoji_name
   2480 filter -> Filter
   2112 emoji_picker -> emoji
   2102 emoji -> emojis_by_name
   2101 user_status -> emojis_by_name
   2101 reactions -> emojis_by_name
   2100 markdown -> emojis_by_name
   2100 hotkey -> emojis_by_name
   2100 emoji_picker -> emojis_by_name
   1672 search_suggestion -> Handlebars
   1584 emoji -> get_emoji_codepoint
   1580 reactions -> get_emoji_codepoint
   1577 user_status -> get_emoji_codepoint
   1577 markdown -> get_emoji_codepoint
   1577 hotkey -> get_emoji_codepoint
   1577 emoji_picker -> get_emoji_codepoint
   1577 dispatch -> get_emoji_codepoint
   1446 hotkey -> overlays

**Steve Howell** · 2022-01-08 18:59 UTC

~~~
$ git grep emoji_codes.json frontend_tests/
frontend_tests/node_tests/dispatch.js:const emoji_codes = zrequire("../generated/emoji/emoji_codes.json");
frontend_tests/node_tests/emoji.js:const emoji_codes = zrequire("../generated/emoji/emoji_codes.json");
frontend_tests/node_tests/emoji_picker.js:const emoji_codes = zrequire("../generated/emoji/emoji_codes.json");
frontend_tests/node_tests/hotkey.js:const emoji_codes = zrequire("../generated/emoji/emoji_codes.json");
frontend_tests/node_tests/markdown.js:const emoji_codes = zrequire("../generated/emoji/emoji_codes.json");
frontend_tests/node_tests/reactions.js:const emoji_codes = zrequire("../generated/emoji/emoji_codes.json");
frontend_tests/node_tests/user_status.js:const emoji_codes = zrequire("../generated/emoji/emoji_codes.json");

**Steve Howell** · 2022-01-08 19:02 UTC

And then:

~~~
$ git grep emoji.initialize frontend_tests/
frontend_tests/node_tests/dispatch.js:emoji.initialize({realm_emoji, emoji_codes});
frontend_tests/node_tests/emoji.js:emoji.initialize({realm_emoji, emoji_codes});
frontend_tests/node_tests/emoji_picker.js:    emoji.initialize({
frontend_tests/node_tests/hotkey.js:emoji.initialize({
frontend_tests/node_tests/markdown.js:emoji.initialize(emoji_params);
frontend_tests/node_tests/reactions.js:emoji.initialize(emoji_params);
frontend_tests/node_tests/user_status.js:emoji.initialize(emoji_params);

**Steve Howell** · 2022-01-08 19:52 UTC

I tried this crazy experiment...

~~~ diff
diff --git a/static/shared/js/emoji.js b/static/shared/js/emoji.js
index 7653e240a8..b034b09b0d 100644
--- a/static/shared/js/emoji.js
+++ b/static/shared/js/emoji.js
@@ -75,6 +75,10 @@ const zulip_emoji = {
 };

 export function get_emoji_name(codepoint) {
+    return _get_emoji_name(emoji_codes, codepoint);
+}
+
+function _get_emoji_name(emoji_codes, codepoint) {
     // get_emoji_name('1f384') === 'holiday_tree'
     if (Object.prototype.hasOwnProperty.call(emoji_codes.codepoint_to_name, codepoint)) {
         return emoji_codes.codepoint_to_name[codepoint];
@@ -83,6 +87,10 @@ export function get_emoji_name(codepoint) {
 }

 export function get_emoji_codepoint(emoji_name) {
+    return _get_emoji_codepoint(emoji_codes, emoji_name);
+}
+
+function _get_emoji_codepoint(emoji_codes, emoji_name) {
     // get_emoji_codepoint('avocado') === '1f951'
     if (Object.prototype.hasOwnProperty.call(emoji_codes.name_to_codepoint, emoji_name)) {
         return emoji_codes.name_to_codepoint[emoji_name];
@@ -111,7 +119,8 @@ export function get_realm_emoji_url(emoji_name) {
 }

 export function build_emoji_data(realm_emojis) {
-    emojis_by_name.clear();
+    const _emojis_by_name = emojis_by_name;
+    _emojis_by_name.clear();
     for (const [realm_emoji_name, realm_emoji] of realm_emojis) {
         const emoji_dict = {
             name: realm_emoji_name,
@@ -121,22 +130,25 @@ export function build_emoji_data(realm_emojis) {
             url: realm_emoji.emoji_url,
             has_reacted: false,
         };
-        emojis_by_name.set(realm_emoji_name, emoji_dict);
+        _emojis_by_name.set(realm_emoji_name, emoji_dict);
     }

+    const _emoji_codes = emoji_codes;
+    const __get_emoji_name = _get_emoji_name;
+    const _default_emoji_aliases = default_emoji_aliases;
     for (const codepoints of Object.values(emoji_codes.emoji_catalog)) {
         for (const codepoint of codepoints) {
-            const emoji_name = get_emoji_name(codepoint);
-            if (emoji_name !== undefined && !emojis_by_name.has(emoji_name)) {
+            const emoji_name = __get_emoji_name(_emoji_codes, codepoint);
+            if (emoji_name !== undefined && !_emojis_by_name.has(emoji_name)) {
                 const emoji_dict = {
                     name: emoji_name,
                     display_name: emoji_name,
-                    aliases: default_emoji_aliases.get(codepoint),
+                    aliases: _default_emoji_aliases.get(codepoint),
                     is_realm_emoji: false,
                     emoji_code: codepoint,
                     has_reacted: false,
                 };
-                emojis_by_name.set(emoji_name, emoji_dict);
+                _emojis_by_name.set(emoji_name, emoji_dict);
             }
         }
     }
@@ -249,13 +261,17 @@ export function initialize(params) {

     build_emoticon_translations();

+    const _default_emoji_aliases = default_emoji_aliases;
+    const _emoji_codes = emoji_codes;
+    const __get_emoji_codepoint = _get_emoji_codepoint;
+
     for (const value of emoji_codes.names) {
-        const base_name = get_emoji_codepoint(value);
+        const base_name = __get_emoji_codepoint(_emoji_codes, value);

-        if (default_emoji_aliases.has(base_name)) {
-            default_emoji_aliases.get(base_name).push(value);
+        if (_default_emoji_aliases.has(base_name)) {
+            _default_emoji_aliases.get(base_name).push(value);
         } else {
-            default_emoji_aliases.set(base_name, [value]);
+            _default_emoji_aliases.set(base_name, [value]);
         }
     }

~~~

**Steve Howell** · 2022-01-08 19:53 UTC

You could see clearly that the rewire helpers were no longer being invoked in a big loop during `initialize`, but the speedup was too noisy to measure.

**Steve Howell** · 2022-01-08 20:02 UTC

(BTW I excluded `buddy_data.js` from that experiment.)

**Tim Abbott** · 2022-01-11 01:57 UTC

(replying to Steve Howell (showell))
> #20732

I just caught up on this thread and merged this followup as well. I like the path forward selected here!


## pyright

*2022-01-11 to 2022-01-11 · 1 messages · [open in Zulip](https://chat.zulip.org/#narrow/channel/18-tools/topic/pyright/with/1308049)*

**Rein Zustand** · 2022-01-11 10:53 UTC

I discovered [Pyright](https://github.com/microsoft/pyright) while I was configuring LSP on my neovim. According to https://www.wisdomgeek.com/development/web-development/python/statically-type-checking-python-code-using-pyright, the old READMe of the project page claimed that Pyright was ~5x faster than Mypy. Is it worth investigating to use it to replace Mypy in zulip/zulip?


## provision error w/realm emojis

*2022-02-14 to 2022-02-16 · 30 messages · [open in Zulip](https://chat.zulip.org/#narrow/channel/18-tools/topic/provision.20error.20w.2Frealm.20emojis/with/1328036)*

**Steve Howell** · 2022-02-14 13:38 UTC

~~~
Successfully populated test database.
+ '[' -e /home/steve/.zuliprc ']'
New digest written to: /home/steve/zulip/var/540f509f-e672-47ed-b522-a3a345a4745e/db_files_hash_for_dev
New digest written to: /home/steve/zulip/var/540f509f-e672-47ed-b522-a3a345a4745e/migrations_hash_zulip_test_template
+ env DJANGO_SETTINGS_MODULE=zproject.test_settings ZULIP_DB_NAME=zulip_test_template ./manage.py migrate --no-input
Operations to perform:
  Apply all migrations: analytics, auth, confirmation, contenttypes, corporate, otp_static, otp_totp, pgroonga, sessions, social_django, two_factor, zerver, zilencer
Running migrations:
  Applying zerver.0376_set_realmemoji_author_and_reupload_realmemoji...2022-02-14 13:33:06.319 WARN [urllib3.connectionpool] Retrying (Retry(total=2, connect=None, read=None, redirect=None, status=None)) after connection broken by 'NewConnectionError('<urllib3.connection.HTTPConnection object at 0x7f42fb39e970>: Failed to establish a new connection: [Errno -2] Name or service not known')': /user_avatars/2/emoji/images/1.png.original
2022-02-14 13:33:08.323 WARN [urllib3.connectionpool] Retrying (Retry(total=1, connect=None, read=None, redirect=None, status=None)) after connection broken by 'NewConnectionError('<urllib3.connection.HTTPConnection object at 0x7f42fb39eb80>: Failed to establish a new connection: [Errno -2] Name or service not known')': /user_avatars/2/emoji/images/1.png.original
2022-02-14 13:33:12.329 WARN [urllib3.connectionpool] Retrying (Retry(total=0, connect=None, read=None, redirect=None, status=None)) after connection broken by 'NewConnectionError('<urllib3.connection.HTTPConnection object at 0x7f42fb39ed90>: Failed to establish a new connection: [Errno -2] Name or service not known')': /user_avatars/2/emoji/images/1.png.original
2022-02-14 13:33:12.336 ERR  [] Problem handling data on queue deferred_work
Traceback (most recent call last):
  File "/srv/zulip-py3-venv/lib/python3.8/site-packages/urllib3/connection.py", line 174, in _new_conn
    conn = connection.create_connection(
  File "/srv/zulip-py3-venv/lib/python3.8/site-packages/urllib3/util/connection.py", line 72, in create_connection
    for res in socket.getaddrinfo(host, port, family, socket.SOCK_STREAM):
  File "/usr/lib/python3.8/socket.py", line 918, in getaddrinfo
    for res in _socket.getaddrinfo(host, port, family, type, proto, flags):
socket.gaierror: [Errno -2] Name or service not known

**Steve Howell** · 2022-02-14 13:40 UTC

@Mateusz Mandera FYI. ^^^

**Steve Howell** · 2022-02-14 13:42 UTC

The above error was followed by a whole bunch of other tracebacks.  Apart from being scary, it hasn't affected my workflow yet, as I can run the server, and I'm not doing any work related to realm emojis.

**Steve Howell** · 2022-02-14 13:45 UTC

Here is a piece of the above:

~~~
Failed to establish a new connection: [Errno -2] Name or service not known')': /user_avatars/2/emoji/images/1.png.original
2022-02-14 13:33:12.336 ERR  [] Problem handling data on queue deferred_work

**Steve Howell** · 2022-02-14 13:48 UTC

~~~
Traceback (most recent call last):
  File "/home/steve/zulip/zerver/worker/queue_processors.py", line 322, in do_consume
    consume_func(events)
  File "/home/steve/zulip/zerver/worker/queue_processors.py", line 356, in <lambda>
    consume_func = lambda events: self.consume(events[0])
  File "/home/steve/zulip/zerver/worker/queue_processors.py", line 1074, in consume
    handle_reupload_emojis_event(realm, logger)
  File "/home/steve/zulip/zerver/lib/upload.py", line 1186, in handle_reupload_emojis_event
    emoji_file_content = get_emoji_file_content(session, emoji_url, realm_emoji.id, logger)
  File "/home/steve/zulip/zerver/lib/upload.py", line 1156, in get_emoji_file_content
    response = session.get(original_emoji_url)
  File "/srv/zulip-py3-venv/lib/python3.8/site-packages/requests/sessions.py", line 542, in get
    return self.request('GET', url, **kwargs)
  File "/srv/zulip-py3-venv/lib/python3.8/site-packages/requests/sessions.py", line 529, in request
    resp = self.send(prep, **send_kwargs)
  File "/srv/zulip-py3-venv/lib/python3.8/site-packages/requests/sessions.py", line 645, in send
    r = adapter.send(request, **kwargs)
  File "/home/steve/zulip/zerver/lib/outgoing_http.py", line 41, in send
    return super().send(*args, **kwargs)
  File "/srv/zulip-py3-venv/lib/python3.8/site-packages/requests/adapters.py", line 519, in send
    raise ConnectionError(e, request=request)
requests.exceptions.ConnectionError: HTTPConnectionPool(host='zulip.testserver', port=80): Max retries exceeded with url: /user_avatars/2/emoji/images/1.png.original (Caused by NewConnectionError('<urllib3.connection.HTTPConnection object at 0x7f42fb39efa0>: Failed to establish a new connection: [Errno -2] Name or service not known'))

**Steve Howell** · 2022-02-14 13:49 UTC

I wonder if this is a problem with my droplet setup.  I set EXTERNAL_HOST to <my ip address>:9991 in my bashrc.

**Mateusz Mandera** · 2022-02-14 14:01 UTC

(replying to Steve Howell (showell))
> I wonder if this is a problem with my droplet setup. I set EXTERNAL_HOST to <my ip address>:9991 in my bashrc.
Hmm yeah sounds likely. The `deferred_work` worker wants to make GET requests to this:
```
        emoji_url = get_emoji_url(emoji_filename, realm_emoji.realm_id)
        if emoji_url.startswith("/"):
            emoji_url = urljoin(realm_emoji.realm.uri, emoji_url)
```

and it looks like in your deployment `realm_emoji.realm.uri` is `zulip.testserver`, which won't work :thinking:

**Mateusz Mandera** · 2022-02-14 14:02 UTC

Possibly we should just have this RealmEmoji-reuploading code check `if settings.TEST_SUITE:` and be no-op in that case?

**Steve Howell** · 2022-02-14 14:03 UTC

Probably.

**Mateusz Mandera** · 2022-02-14 14:03 UTC

Have you tried running `rebuild-test-database`? I think this error should only be manifesting itself in the test environment if the migration gets applied on top of an already provisioned test db

**Steve Howell** · 2022-02-14 14:04 UTC

I wondered about that, but the first line I reported to you above is `Successfully populated test database.`.

**Mateusz Mandera** · 2022-02-14 14:04 UTC

(replying to Mateusz Mandera)
> Have you tried running `rebuild-test-database`? I think this error should only be manifesting itself in the test environment if the migration gets applied on top of an already provisioned test db
(because if it's not provisioned yet, then there are no `Realm`s and thus no "reupload" events get pushed to the `deferred_work` queue)

**Steve Howell** · 2022-02-14 14:05 UTC

OTOH when I ran provision again, I have no errors, but maybe that's due to the queue just being cleared.

**Mateusz Mandera** · 2022-02-14 14:06 UTC

(replying to Steve Howell (showell))
> I wondered about that, but the first line I reported to you above is `Successfully populated test database.`.
Yeah, it'll give that result, because the migration simply pushed an event to the queue worker - so it itself completed successfully. Then the queue worker errored out in parallel when trying to process the event, and eventually ended up dropping the event. Allowing things to proceed normally.

**Steve Howell** · 2022-02-14 14:31 UTC

I wonder if @Yash RE is going to encounter this on his droplet.  I also wonder if I will encounter it again the next time I do a full provision.  At this point I'm not really blocked, but I could imagine this confusing folks in the future.

Let me know if you need me to try anything out.

**Yash RE** · 2022-02-14 17:18 UTC

(I have currently been working locally due to (a) issue prioritization and (b) droplet being broken but I'll message here if I do see this)

**Tim Abbott** · 2022-02-14 21:39 UTC

We should figure out a way to just make this migration a noop in initial provisioning.

**Tim Abbott** · 2022-02-14 21:42 UTC

@Mateusz Mandera FYI.  I think ideally we'd have it be a noop when installing a new production system too somehow.

**Tim Abbott** · 2022-02-14 21:42 UTC

Hmm I guess for new systems there are 0 realms in the database?

**Tim Abbott** · 2022-02-14 21:42 UTC

So maybe it's ok :)

**Mateusz Mandera** · 2022-02-14 21:42 UTC

My reading is that this is a noop in initial provisioning - no realms, so no events get pushed

**Mateusz Mandera** · 2022-02-14 21:43 UTC

I think it's just the "apply the migration to an already provisioned test db" case that's an issue

**Tim Abbott** · 2022-02-14 21:56 UTC

Yeah makes sense.

**Tim Abbott** · 2022-02-14 21:56 UTC

In theory it should be fine then.

**Tim Abbott** · 2022-02-14 21:57 UTC

(rabbitmq should be working when we run migrations normally anyway)

**Tim Abbott** · 2022-02-14 21:58 UTC

Oh does something make the development environment try to run enqueued events immediately here?

**Mateusz Mandera** · 2022-02-14 21:58 UTC

Just opened https://github.com/zulip/zulip/pull/21129 for this

**Mateusz Mandera** · 2022-02-14 21:58 UTC

(replying to Tim Abbott)
> Oh does something make the development environment try to run enqueued events immediately here?
I don't think so, the events should get processed when the workers starts, so upon `run-dev.py`

**Mateusz Mandera** · 2022-02-14 21:59 UTC

In my local testing there was no issue with running `run-dev.py` after the migrations, the events got processed correctly and reuploaded emoji.

**Tim Abbott** · 2022-02-16 01:27 UTC

Great, thanks!


## puppeteer loop option

*2022-02-25 to 2022-03-04 · 19 messages · [open in Zulip](https://chat.zulip.org/#narrow/channel/18-tools/topic/puppeteer.20loop.20option/with/1334901)*

**Steve Howell** · 2022-02-25 16:54 UTC

Can we add a `--loop` option to `test-js-with-puppeteer`?  How do people normally run it in a loop?

The [documentation](https://zulip.readthedocs.io/en/latest/testing/testing-with-puppeteer.html) has this as a TODO.

**Steve Howell** · 2022-02-25 16:55 UTC

I suppose many people put it in a bash loop, but that can be slow if you have to keep re-starting the server.

**Steve Howell** · 2022-02-25 16:55 UTC

For my own testing, I do something like this, which is easy enough, but it would obviously be nice to automate this:

~~~ diff
$ git diff
diff --git a/tools/test-js-with-puppeteer b/tools/test-js-with-puppeteer
index 45ae405c46..00ad99dd61 100755
--- a/tools/test-js-with-puppeteer
+++ b/tools/test-js-with-puppeteer
@@ -112,7 +112,12 @@ def run_tests(files: Iterable[str], external_host: str) -> None:
                     response = input('Tests failed. Press Enter to re-run tests, "q" to quit: ')
         else:
             ret = 1
-            ret, current_test_num = run_tests()
+            for i in range(1000):
+                ret, current_test_num = run_tests()
+                if ret == 0:
+                    print("SUCCESS!!!\n\n\n\n\n\n\n\n", i)
+                else:
+                    break

**Steve Howell** · 2022-02-25 16:56 UTC

From the docs:

~~~
TODO: Document how to run 100x in CI to check for nondeterministic failures.

**Tim Abbott** · 2022-02-25 18:49 UTC

@Dinesh Ch @Riken Shah (Riken-Shah) are the folks who've done most of that style of testing and may be able to comment.

**Dinesh Ch** · 2022-02-26 16:56 UTC

Yes, we wanted to add a `--loop` option when working on puppeteer tests.

About running it in CI, we were discussing something like running tests 100 times if there are any changes in puppeteer tests in PRs. We wanted to figure out a cleaner/easier way than editing CI files to run these 100times. By that TODO, I think we just meant to mention setting a bash loop in CI files as that's what we had done mostly. But it'd be nice to have a `--loop` option so we don't resort to using a bash loop which is slower because of server re-starts as @Steve Howell (showell) mentioned above.

**Dinesh Ch** · 2022-03-01 11:38 UTC

@Steve Howell (showell) are you or anyone working on adding this `--loop` option? If not, I'd like to try. I think it could make things a bit faster for running puppeteer stress tests when working on flaky tests.

**Steve Howell** · 2022-03-01 11:45 UTC

@Dinesh Ch Please do!  Please also see if #20970 is something you have time to fix.  (No worries if you don't.)

**Steve Howell** · 2022-03-01 11:46 UTC

(I am definitely not working on `--loop` nor do I know of anybody else.  I am happy to file an issue for it, but if you are just gonna knock it out, it may be unnecessary.)

**Dinesh Ch** · 2022-03-01 11:53 UTC

Okay, will work on it soon. I think filing an issue is not necessary.

Sure, will look into #20970 later after this. Adding it to my TODO...

**Dinesh Ch** · 2022-03-02 05:35 UTC

#21286 for both `--loop` and #20970. And also for a little bit of refactoring.

**Steve Howell** · 2022-03-02 12:50 UTC

@Dinesh Ch I had one [question about the PR](https://github.com/zulip/zulip/pull/21286/commits/bd31386e2aa12f3ce015d93015a8828e8a353bcf#r817658833)

**Dinesh Ch** · 2022-03-02 17:56 UTC

Fixed it. Thanks for that! :)

**Steve Howell** · 2022-03-02 17:57 UTC

Merged, thanks!

**Steve Howell** · 2022-03-03 22:06 UTC

@Dinesh Ch I think a529dc8c766a4603b72a36f32e90552e4696c1eb may have broken the use case of entering the full file name for autocomplete convenience:

~~~
$ ./tools/test-js-with-puppeteer frontend_tests/puppeteer_tests/subscriptions.ts
Chromium is already in /srv/zulip-npm-cache/aa1da94ca5d276aa34a36e7046261667a813804e/node_modules/puppeteer/.local-chromium/linux-961656; skipping download.
Traceback (most recent call last):
  File "./tools/test-js-with-puppeteer", line 162, in <module>
    run_tests(options.tests, external_host, options.loop)
  File "./tools/test-js-with-puppeteer", line 96, in run_tests
    test_files = find_js_test_files(test_dir, files)
  File "/home/steve/zulip/tools/lib/test_script.py", line 119, in find_js_test_files
    raise Exception(f"Cannot find a matching file for '{file}' in '{test_dir}'")
Exception: Cannot find a matching file for 'frontend_tests/puppeteer_tests/subscriptions.ts' in '/home/steve/zulip/frontend_tests/puppeteer_tests'

**Steve Howell** · 2022-03-03 22:07 UTC

I don't view this as a severe bug, but we should probably fix it forward soon-ish or just revert the commit.

**Tim Abbott** · 2022-03-04 00:33 UTC

Yeah, that feature is pretty useful.  I think we can fix forward but we shouldn't lose track of it.

**Dinesh Ch** · 2022-03-04 06:44 UTC

#21317

**Steve Howell** · 2022-03-04 09:48 UTC

@Dinesh Ch Merged!  Thanks for the timely follow up here.


## change initial passwords for test db reset

*2022-03-04 to 2022-03-04 · 2 messages · [open in Zulip](https://chat.zulip.org/#narrow/channel/18-tools/topic/change.20initial.20passwords.20for.20test.20db.20reset/with/1338905)*

**Dinesh Ch** · 2022-03-04 07:09 UTC

Is there a reason we want 
(replying to Steve Howell (showell))
> I think we should start a new discussion on #**tools** to decide whether we want to change passwords a bit more aggressively in the test databases.
Is there a reason we want to change initial passwords on resetting databases?

**Tim Abbott** · 2022-03-04 20:51 UTC

I'm not aware of a reason we'd want to do this.


## doc_tests

*2022-03-08 to 2022-03-09 · 5 messages · [open in Zulip](https://chat.zulip.org/#narrow/channel/18-tools/topic/doc_tests/with/1340711)*

**Steve Howell** · 2022-03-08 16:30 UTC

We have certain tests that output a crazy amount of parsed YAML if your event schema is slightly broken.  They are very difficult to debug.

**Lauryn Menard** · 2022-03-08 17:32 UTC

Agreed.

**Tim Abbott** · 2022-03-08 17:51 UTC

Yeah, unfortunately I don't really know what we can readily do about that situation; it's a third-party error message.

**Steve Howell** · 2022-03-09 00:22 UTC

Even if some of the problems here are kinda tricky to solve, I think it's worth a deep dive on making it easier to develop full-stack features without immediately getting bogged down by openapi concerns.

**Steve Howell** · 2022-03-09 00:22 UTC

(both in terms of being able to bypass checks and having nicer feedback)


## stream events

*2022-03-22 to 2022-03-22 · 1 messages · [open in Zulip](https://chat.zulip.org/#narrow/channel/18-tools/topic/stream.20events/with/1350300)*

**Notification Bot** · 2022-03-22 22:31 UTC

@Tim Abbott changed the [access permissions](/help/stream-permissions) for this stream from **Public** to **Web-public**.


## automatic provision when running the development server

*2022-04-06 to 2022-04-17 · 7 messages · [open in Zulip](https://chat.zulip.org/#narrow/channel/18-tools/topic/automatic.20provision.20when.20running.20the.20development.20server/with/1361243)*

**Riken Shah** · 2022-04-06 16:17 UTC

Hey folks,
Just a thought,
When changing a branch in zulip or rebasing a branch we have to run `provision` every time. 
Can't we run it automatically when we run the dev server?

**Tim Abbott** · 2022-04-06 21:35 UTC

Good question. We certainly wouldn't want to remove the ability to run it independently, since it can be useful to run provision without stopping the development server at times.

**Tim Abbott** · 2022-04-06 21:35 UTC

I could also imagine perhaps an optional post-rebase hook?  Not sure.

**Alya Abbott** · 2022-04-07 23:00 UTC

That sounds great! I'm often having to check on whether `provision` is finished so that I can run the dev server, and then I'm stuck waiting again while it boots up.

**Steve Howell** · 2022-04-08 14:37 UTC

I don’t want provision to be completely automated, since I occasionally switch to ancient branches for research purposes.

**Steve Howell** · 2022-04-08 14:38 UTC

I think we should address just the run-dev scenario specifically.

**Riken Shah** · 2022-04-17 12:41 UTC

Opened a [WIP PR](https://github.com/zulip/zulip/pull/21833). 

Where we run auto-provision wherever we are checking for provision. 
Showing the output if provision fails. 
And skipping auto-provision if `--skip-provision-check` arg is passed.


## size / quota

*2022-04-11 to 2022-04-14 · 7 messages · [open in Zulip](https://chat.zulip.org/#narrow/channel/18-tools/topic/size.20.2F.20quota/with/1364274)*

**FrancoisPE** · 2022-04-11 13:27 UTC

Hello
I would lile to manage 'zulip size  : disk due to uploads, database, etc... in order to ensure not to exceed my vps capacity.
I though it was possible to find out such output but I don't see where to look for.

**Tim Abbott** · 2022-04-11 20:56 UTC

@FrancoisPE I don't think we have a specific tool for that but you can readily use standard tools to look at the disk size consumed by your postgres database, use `du` to look at your uploaded files directory, and `/home/zulip` more generally, and then `/var/log/zulip` is the rest of it. 

We have a few documented configuration options to control disk usage by logs in particular.

**FrancoisPE** · 2022-04-12 17:03 UTC

@Tim Abbott  Thanks a lot.
I dig around limiting database and 'upload file' folder size. I see that there is message retention capabilities in Zulip.
My concern is VPS crash due to capability overpassed...
I imagine a cron job testing db and upload folder size and based on driven limits, running a manage.py retention_message time_limit... Is that possible ? 
I found a way for user to manage their own message retention settings... But nothing else ?

**Tim Abbott** · 2022-04-12 21:28 UTC

@FrancoisPE the message retention settings are global for streams and servers, not individual users.

**FrancoisPE** · 2022-04-13 06:14 UTC

Ok
Is there a way to manage this with manage.py ?

**Tim Abbott** · 2022-04-13 18:30 UTC

@FrancoisPE no, but you can use the Zulip API to configure retention policies.

**FrancoisPE** · 2022-04-14 05:34 UTC

That's really nice feature 😀


## View / restore deleted message

*2022-04-12 to 2022-04-14 · 4 messages · [open in Zulip](https://chat.zulip.org/#narrow/channel/18-tools/topic/View.20.2F.20restore.20deleted.20message/with/1364917)*

**Aaron** · 2022-04-12 11:38 UTC

Two places in the documentation mention that deleted posts are stored temporarily in a special format which could be restored in the event of erroneous deletion. I'm in that situation now and need to view (but not restore) something in a deleted message. The documentation states that we should contact support for assistance with this, but i'm wondering if it's perhaps functionality offered by `manage.py`. I don't see anything obvious in the list of subcommands. Does anyone know?

**Aaron** · 2022-04-12 11:47 UTC

on closer inspection I can see there is a `restore_messages` subcommand which does restore them, but i can't see a way to find a single deleted message and restore (or preferably just view) the contents of it

**Alex Vandiver** · 2022-04-12 16:12 UTC

I don't believe we have any automated tools for searching and viewing deleted messages.

If you're just looking for the content, one technique would be to, as the `zulip` user, run `./manage.py dbshell` and:
```sql
select date_sent, content from zerver_archivedmessage order by date_sent;
```

**Aaron** · 2022-04-14 13:46 UTC

@Alex Vandiver this was incredibly helpful, thank you very much


## improved renumber-migrations ?

*2022-04-20 to 2022-04-20 · 10 messages · [open in Zulip](https://chat.zulip.org/#narrow/channel/18-tools/topic/improved.20renumber-migrations.20.3F/with/1370548)*

**Adam Sah** · 2022-04-20 12:32 UTC

I like to keep my branches closely in sync with main, but this means resolving conflicts... mostly that's fine but I've noticed that many of my branches pickup artificial conflicts due to migration numbering.  renumber-migrations works but it's manual and annoying.

a modest proposal: during development, reserve and use 9999_xxx for the current migration - then as part of merging into main, allocate the final migration number.

if y'all like this, we'd put in tooling & docs, e.g.
 - a check that migration #9999 is never used in a branch named "main"
 -  add "renumber-migrations --main" which finds migration #9999 and renumbers it to the next number.
 - modify "manage.py makemigrations" to allocate 9999
(if this is interesting to you, I can put together a PR)

**Tim Abbott** · 2022-04-20 15:26 UTC

I think we should be able to make `renumber-migrations` not annoying -- there's no reason it should need to ask any questions, since it should be able to determine the desired graph without any user input.

**Tim Abbott** · 2022-04-20 15:27 UTC

I've been sad about that problem with the tool since we wrote it like 3 years ago.

**Adam Sah** · 2022-04-20 15:53 UTC

thx! @Tim Abbott - silent operation is great too! but I think that's a different issue... I'm trying to remove the need to run `renumber-migrations` at all when merging from main, because it's currently a big source of "false" conflicts that cause CI to fail, and therefore I can't automate keeping my (many) branches/PRs in sync with main. Reserving 9999 for the current branch's migration solves this... or is there a better design?

(I'm happy code, test & send a PR...)

**Tim Abbott** · 2022-04-20 16:10 UTC

Well, if `renumber-migrations` was non-interactive, your script could just run it as part of its rebase process.

**Tim Abbott** · 2022-04-20 16:11 UTC

I don't think the 9999 option is a great solution, since (for example) some branches will have multiple migrations.

**Adam Sah** · 2022-04-20 16:38 UTC

gotcha - I'll queue up a PR as a new param to renumber-migrations to handle this common case. What do you want to call it?  (--automerge?)

**Tim Abbott** · 2022-04-20 17:15 UTC

I don't think we need a parameter -- it's just a bug that this tool doesn't model the original and new graphs correctly to not have to prompt you.

**Tim Abbott** · 2022-04-20 17:16 UTC

(The test case where it's nontrivial that you should try  is when there's 3 new migrations on each branch).

**Adam Sah** · 2022-04-20 21:20 UTC

various issues relating to renumber-migrations, i.e. see which apply and can be done at the same time...
https://github.com/zulip/zulip/issues?q=%22renumber-migrations%22+label%3A%22area%3A+tooling%22


## droplet

*2022-06-02 to 2022-06-02 · 4 messages · [open in Zulip](https://chat.zulip.org/#narrow/channel/18-tools/topic/droplet/with/1387735)*

**Tim Abbott** · 2022-06-02 21:12 UTC

@Droplet Bot HarshitOnGitHub

**Droplet Bot** · 2022-06-02 21:12 UTC

Trying to create droplet. Please wait.

**Droplet Bot** · 2022-06-02 21:12 UTC

Creating Zulip developer environment for GitHub user harshitongithub...
Checking to see if GitHub user harshitongithub exists...
...user exists!
Checking to see that GitHub user has available public keys...
No keys found. Has user harshitongithub added SSH keys to their GitHub account?

**Tim Abbott** · 2022-06-02 21:13 UTC

@Harshit Bansal looks like you need to do some setup first; see https://zulip.readthedocs.io/en/latest/development/request-remote.html


## GitHub Copilot

*2022-06-22 to 2022-07-08 · 20 messages · [open in Zulip](https://chat.zulip.org/#narrow/channel/18-tools/topic/GitHub.20Copilot/with/1394971)*

**Adam Sah** · 2022-06-22 06:46 UTC

Interesting conversation... Lots of fans...
https://news.ycombinator.com/item?id=31825742

**Neil Pilgrim (neiljp)** · 2022-06-22 18:34 UTC

I'm sure I could benefit from more code completion, but I'm a little wary of these tools leading to seemingly correct code (to the author), ie. giving a false sense of security. Sure this might be treated through education or can be caught in code review, but I suspect I'd get frustrated if I was reviewing code that repeatedly needed fixing due to authors using it to churn out 'reasonable looking' code.

**Matt** · 2022-06-22 19:11 UTC

One of my favorite relevant, cautionary quotes:
> We found that we were making mistakes due to the complexity, and then we wrote scripts to write the configs for us, and using these scripts, we made mistakes in a faster, more automated manner. -- http://cricket.sourceforge.net/support/doc/intro.html

**Adam Sah** · 2022-06-23 00:15 UTC

where to draw the line?  taken to the extreme, purists would say we should code in machine language (not even use an assembler!)

**Anders Kaseorg** · 2022-06-23 00:30 UTC

Compilers are generally well-tested tools designed for the purpose of performing a comprehensively specified translation, not randomly evolved to reproduce the average behavior of humans trying to do the same thing.

**Matt** · 2022-06-23 16:59 UTC

Drew DeVault has a new piece talking about cross-license poisoning etc. for open source development use of Copilot (and ostensibly the newly-announced AWS [CodeWhisperer](https://aws.amazon.com/blogs/aws/now-in-preview-amazon-codewhisperer-ml-powered-coding-companion/)) https://drewdevault.com/2022/06/23/Copilot-GPL-washing.html

**Tim Abbott** · 2022-06-29 00:24 UTC

I think this category of tool is an interesting topic. I don't think I've really fully formed my opinions on it.

From an abstract point of view, of course I'd like for it to be possible for me to use a super cool smart code completion engine that uses machine learning, among other technologies, to make good suggestions when I'm programming.

If someone were to develop such a tool using a training set consisting entirely of code written specifically for the purpose of being good examples / training data, and the model was designed in such a way that it could entirely run locally, that seems like a programming assistant tool that could be useful when used carefully.

**Tim Abbott** · 2022-06-29 00:26 UTC

But GitHub's project is pretty different from that vision in several key ways, and I think it's also the case that what I described would be hard to create. (In part because it's hard to imagine the kinds of organizations with the resources to build such a thing, that would actually be responsible about not bulk-importing code from open source or other sources in order to get enough training data).

**Tim Abbott** · 2022-06-29 00:30 UTC

There's obviously legal questions about how the US legal system, fair use rules, etc., apply to something like GitHub CoPilot. It seems possible to me that the Microsoft/Amazon strategy here will be "We have lots of money and lawyers and feel confident that we can model this as a legal expense budget for the product that is affordable for our organization". As Uber, Facebook, and others have demonstrated, if you have enough money and influence, you can ensure that the laws let you do the thing you want to do as long as there's enough complexity in the legal question.

**Tim Abbott** · 2022-06-29 00:31 UTC

As a result, I prefer to focus on thinking about the moral question of GitHub/Microsoft profiting by selling this sort of service that is, fundamentally, generated from the work of the open source community and GitHub users in particular, without any attempt to get permission/consent. That sort of analysis makes me feel pretty down on CoPilot.

**Tim Abbott** · 2022-06-29 00:33 UTC

Even permissive open source licenses, like Zulip's own Apache 2.0 license, require attribution when copying the work.

**Rein Zustand** · 2022-07-01 16:34 UTC

Selected papers on Copilot hosted on FSF: https://www.fsf.org/licensing/copilot.

**Neil Pilgrim (neiljp)** · 2022-07-04 00:44 UTC

The SFC didn't heavily use GitHub, but they're now leaving completely and strongly advising movement away in light of Copilot general launch:
https://sfconservancy.org/blog/2022/jun/30/give-up-github-launch/

**Greg Price** · 2022-07-05 18:42 UTC

> Meanwhile, the work of our committee continues to carefully study the general question of AI-assisted software development tools. One recent preliminary finding was that AI-assisted software development tools can be constructed in a way that by-default respects FOSS licenses. […] While Microsoft's GitHub was the first mover in this area, by way of comparison, early reports suggest that Amazon's new CodeWhisperer system (also launched last week) seeks to provide proper attribution and licensing information for code suggestions.

Hmm, that's an interesting tidbit about Amazon's thing!

(Several links omitted in my copy-paste.)

**Adam Birds** · 2022-07-08 02:11 UTC

I recently registered for GitHub's Student Pack, and with that is free use of GitHub Pilot. I just thought I'd give it a whirl to see how it worked etc. I'd installed it and then forgot I had for a bit and then something crazy happened.

I was doing a uni assignment and part of this was some small tasks in Python. I knew how to do them so it was never going to be an issue, but the uni likes us to do add a line like this at the top:

`## Problem: Take a list of grades, convert them into points and print an average GPA`

So I did this, then added a line like:

`## Input: Get list of grades.`

So I declared my list. as I started typing `## Output...` it completed that line. Then as soon as I started writing the for loop, literally as I pressed space after the for, it offered to complete the rest of the code (and it was correct) . Its incredibly powerful, clearly, even more so when you add comments telling it what you want to do. Whilst I was kind of mesmerized at how clever it is and clearly the machine learning involved is at epic levels, but it certainly made me question the ethics of it. I've yet to test it to see if it will be able to auto complete a much more complex problem if i was to express it in comments.

It was also able to understand that the variable `speed_of_light` should be initialized at the speed of light and multiple variations of doing this too.  Certainly an interesting topic of discussion.

**Adam Birds** · 2022-07-08 02:19 UTC

One thing I would like to see how it does, is it to give it one of the CS50 problems that I have previously completed to complete from the open-source Harvard CS50 class as some of them are incredibly difficult and require you to have a good understanding of the logic behind the problem and would be really interested as to whether it can do it itself or how much of it can complete. That for me would be a good test of where it sits ethically. If students can use it to literally complete their CS assignments, its worrying to say the least.

**Rafid Aslam** · 2022-07-08 04:19 UTC

I was also amazed when I and my friends tried it for the first time. One of my friend were using it to complete his database assignments (about making sql queries), he was like that, writing some comments to describe what he want then "ez pz man, thanks to copilot". I used it too to code in a language that I wasn't familar of (dart using flutter framework), creating component like button, etc, is as easy as writing comments to describe what we want (of course most of them needs modification, but only a little)

**Tim Abbott** · 2022-07-08 19:48 UTC

I'd expect an algorithm like Copilot that has crawled all the repositories on GitHub to be effective on something like CS50 problems, where there's a good chance that GitHub's data set contains some user's Git repository where they uploaded their personal solutions.

It's of course already possible to cheat on CS homework assignments through many sites where you can pay someone to do your homework ... but I expect tool like Copilot is a much easier method for that, since it doesn't involve interacting with another person.

**Tim Abbott** · 2022-07-08 19:50 UTC

This reminds me of the transition for certain types of math exams that I experienced during high school when graphing calculators became ubiquitous... a lot of problems that would be assigned could be solved by just typing the integral into your graphing calculator. Which has an interesting combination of "this is a useful capability that it's probably good for students to be able to command" with "this makes it very easy to get the correct answer without learning what the course is intending to teach you".

**Neil Pilgrim (neiljp)** · 2022-07-08 23:49 UTC

I'm not sure most of the calculators we had access to had that feature, but graphing alone was pretty useful on its own ;)
I can imagine it definitely makes courses want to reformulate their assessments into a different structure - a) what's the answer b) what makes it a good answer? I don't think that students will necessarily like the result, though - most I know who've taken "open book" exams definitely don't think they're easier, for example - or equally I expect, online exams during the pandemic?

For a few years I taught a more 'conceptual' course on Optics, since it was aimed at both those studying core physics and other areas, and it was surprising (or not...) how much the physics students wanted more maths questions - sure they were used to it, but they also didn't want to follow part (b) and express more of the 'why' (for however much that makes sense in physics).


## GitHub

*2022-07-04 to 2022-07-11 · 24 messages · [open in Zulip](https://chat.zulip.org/#narrow/channel/18-tools/topic/GitHub/with/1399660)*

**Rein Zustand** · 2022-07-04 05:23 UTC

After reading https://sfconservancy.org/GiveUpGitHub/, I think a timely action for Kandra Labs is to allow ways for people to contribute to Zulip without using GitHub. Or maybe it is too early to act?

**Rohitt Vashishtha** · 2022-07-05 16:44 UTC

But if the Zulip repos continue to live on Github, even if we move all development to, say, Gitlab or self-host the git server, Github Co Pilot would still be able to read that code.

Case in point, Linux source being mirrored on GitHub.

All those attribution questions still stand, and it takes just one person to push their clone of Zulip onto their Github account (?).

**Greg Price** · 2022-07-05 16:50 UTC

Do read the article -- it doesn't say that moving off will hide the code from Copilot, and it's mostly not about Copilot at all.

**Rohitt Vashishtha** · 2022-07-05 17:13 UTC

I did, it is an ideological stance about not using GitHub anymore. While that would work to prevent a lock-in to closed source GitHub tooling, I'm just saying that not using GitHub won't protect the stance you're taking against CoPilot at least.

**Greg Price** · 2022-07-05 18:01 UTC

(replying to Rohitt Vashishtha)
> While that would work to prevent a lock-in to closed source GitHub tooling

Yes, that is the point of the article.

**Greg Price** · 2022-07-05 18:05 UTC

I think it's been a bit of an uncomfortable juxtaposition for a long time that while Zulip is firmly 100% open source, and being open source is important to us, we do our work on GitHub which is a closed-source platform.

**Greg Price** · 2022-07-05 18:07 UTC

The main reason we've always stayed there is that it's also important to us that it be easy for people to show up and start contributing. GitHub is familiar to many people, and many people already have accounts there, both of which help keep the barriers to participation low.

Of course, both of those are also reflections of the network lock-in effect that GitHub has -- it's attractive because it's big, so it keeps getting bigger because it's attractive.

**Greg Price** · 2022-07-05 18:15 UTC

In addition to being a closed-source platform, GitHub as a product for discussions and especially for code reviews is, to put it bluntly, terrible.

* Its model of how a code review works is incompatible with the way Zulip actually does code review. (Within GitHub's model, you have your choice of an unreadably messy Git history, or a Git history with just one commit per PR.) This causes important features like "what changed since the last time I reviewed this" to not work. Reviewers work around these, incompletely, by fetching and using Git locally rather than the actual GitHub interface.

* When a PR or issue thread gets even moderately long, GitHub starts hiding part of it. Basically any time I open up a thread that isn't short, I have to Ctrl+F for "hidden", click the "show N hidden items" button -- then repeat, if it was a long thread -- before it's possible to read the whole thing, or to search with Ctrl+F for any keywords in the actual discussion.

* It's full of bugs where a page sometimes live-updates, but often doesn't. After too many times where I was fooled into thinking nobody had replied yet on a given thread, I regularly refresh the whole page to be sure.

**Greg Price** · 2022-07-05 18:16 UTC

Again, we tolerate all that because it's important to us that it be easy for people to show up and start contributing, and there isn't an obvious alternative platform we could use that would be close to as good in that respect.

**Greg Price** · 2022-07-05 18:23 UTC

(replying to Rein Zustand)
> I think a timely action for Kandra Labs is to allow ways for people to contribute to Zulip without using GitHub.

I think it would be difficult to do this effectively other than by actually migrating off of GitHub.

The thing is that GitHub is where the reviews happen. An essential part of contributing code to Zulip is responding to code reviews, participating in the discussion there. One could imagine some kind of arrangement where a contributor doesn't have a GitHub account or interact directly with GitHub servers, going instead through some arms-length contraption that dealt with GitHub on their behalf… but in any substantive sense that's still using GitHub.

(Of course there are also important [ways to contribute](https://zulip.readthedocs.io/en/latest/overview/contributing.html#ways-to-contribute) other than through code! But generally these already don't require GitHub -- even when it comes to reporting issues, I think we get more reports here on chat.zulip.org (that we then turn into GitHub issues) than on GitHub directly. So I'm reading this suggestion as about ways to contribute *code* to Zulip.)

**Greg Price** · 2022-07-05 18:28 UTC

Here's something that I think *is* actionable now, though:

I think it would be good for people in the Zulip community to try out alternative platforms for Git hosting and code review, with any small other projects people might have.

**Greg Price** · 2022-07-05 18:31 UTC

This will give us experience with what the alternatives are, and what they do well and what the rough spots are.

Even with a solo project where nobody else is involved, this would be useful exploration for aspects like creating a repo, managing repos, and using Git with the service.

Then a lot of the more complicated aspects of such a platform come in when collaborating with other people, so a project you work on with others would be especially informative.

**Greg Price** · 2022-07-05 18:38 UTC

The two services suggested in that Conservancy article are:
https://sourcehut.org/
https://codeberg.org/

**Rein Zustand** · 2022-07-05 23:48 UTC

> One could imagine some kind of arrangement where a contributor doesn't have a GitHub account or interact directly with GitHub servers, going instead through some arms-length contraption that dealt with GitHub on their behalf… but in any substantive sense that's still using GitHub.

I don't see it as a problem as long as the said contributor doesn't have to interact with GitHub directly.

**Tim Abbott** · 2022-07-06 00:10 UTC

I'd definitely prefer to use an open source GitHub alternative. I don't think GitLab qualifies -- they're firmly open core, and I'd be very surprised if we were happy using only their open source featureset. (I've also been disappointed with it when I've tried it, but that's something that can change).

I'd be curious to hear about anyone's experiences with Sourcehut or Codeberg; I've not tried either.

**Tim Abbott** · 2022-07-06 00:12 UTC

At present, my feeling on this issue is that "Replacing GitHub" will be a long term project for the open source community, not one that can be achieved quickly by just switching to existing alternatives.

**Greg Price** · 2022-07-06 01:33 UTC

When Debian was looking a few years ago for a code hosting/review service they could self-host (a "forge" application, as people sometimes call it), they ended up going with GitLab.

Plenty of people in the Debian community were dissatisfied with the open-core-ness of GitLab too, so I take that as an indication that all the alternatives then available (2017–2018) were significantly worse products at the time. I believe Gitea (the software that Codeberg uses) was around then, but SourceHut I've only heard of more recently.

**Greg Price** · 2022-07-06 01:34 UTC

From the little I've looked at SourceHut, it has a bit of a distinctive model -- it aims to take the traditional mailing-list style of code collaboration, the one the Linux kernel and the Git project itself still run on, and mesh that with a web app.

**Rein Zustand** · 2022-07-06 03:46 UTC

Popular repos in each solutions:
- Codeberg: https://codeberg.org/explore/repos?sort=moststars&q=&tab=
- SourceHut: https://sr.ht/projects/featured

I couldn't find any notable major projects in those lists.

**Greg Price** · 2022-07-06 03:52 UTC

Good thought. And yeah, I don't recognize any of the names in either of those lists other than those of Codeberg and SourceHut themselves.

**Greg Price** · 2022-07-06 03:53 UTC

That may change as the SFC's campaign makes progress.

**Tim Abbott** · 2022-07-06 18:47 UTC

I kinda hope someone does a crowdfunding campaign like the one originally done for Ghost (https://www.kickstarter.com/projects/johnonolan/ghost-just-a-blogging-platform) in this space; this seems like a problem statement where one likely does need substantial funding in order to build something that can be a strong replacement for GitHub ... and where there's enough people that care about the problem statement that you could potentially raise a bunch of VC-free money for a project with a 100% FOSS vision that way.

**Rein Zustand** · 2022-07-11 01:39 UTC

I think Codeberg will be more mainstream than SourceHut. This is how a PR is done in SourceHut: https://lists.sr.ht/~sircmpwn/sr.ht-dev/%3C20220708210741.25628-1-me%40adnano.co%3E#%3CCLAKZ9PZ3QO9.3SVZJUDDQ1NB6@taiga%3E. I have to do several clicks just to find the "pull requests", i.e. by going to the mailing lists, and pick one relevant mailing list, and then click on the patches list. I know it's what the Linux kernel review system is like, but it looks like for > 500 LOC it is going to be a pain to review. Not to mention that it's hard to give inline comments.

Codeberg / Gitea is more familiar to those who are already used to GitHub/GitLab: e.g. https://codeberg.org/dnkl/foot/pulls/1099/files.

**Matt** · 2022-07-11 15:20 UTC

I've been "on and off" SourceHut for a while. Drew DeVault (SR.HT's benefactor/owner) is prominent in FOSS, has a lot of great contributions, and can be polarizing. If just using it "as a git forge" it's just fine, although I do miss some of GitHub's automagics around language-specific .gitignores, common redirects, and all of the communication tools. For tiny projects, or projects with established comms (Like the kernel) this is probably fine, but if you use GitHub AllTheThings, SR.HT will be a tough pill)


## migration/import from discord

*2022-09-22 to 2022-09-28 · 10 messages · [open in Zulip](https://chat.zulip.org/#narrow/channel/18-tools/topic/migration.2Fimport.20from.20discord/with/1439661)*

**RolandK** · 2022-09-22 21:15 UTC

is it possible to migrate (with preserving all messages) from discord to zulip, for example via csv? via https://github.com/Tyrrrz/DiscordChatExporter for example ?   did anybody do such ?

**Tim Abbott** · 2022-09-22 22:40 UTC

Not at present, though it's probably the next most important data import tool to add.

**RolandK** · 2022-09-22 22:52 UTC

thanks

**Matt** · 2022-09-22 22:56 UTC

there are a few discord-to-slack converters out there. One could probably use one of those to give Zulip a "slack export" to import. I haven't tried it. But curiosity may not allow that to last long...

**RolandK** · 2022-09-23 00:04 UTC

:D

yeah. i see i can even choose in which country i can provide access to slack to all my data :D

https://slack.com/blog/transformation/introducing-data-residency-for-slack

**Rein Zustand** · 2022-09-23 11:07 UTC

The problem is that Zulip, Discord, and Slack have different threading model. But Discord threading is more similar to Zulip's than Slack's.

**Tim Abbott** · 2022-09-23 17:54 UTC

It could be worth trying that Discord-to-Slack process as a workaround, but I'd prefer that we spend effort on writing a tool processing the output of https://github.com/Tyrrrz/DiscordChatExporter, than trying to chain together tools; I think the reason Rein mentioned of corrupting threading is a good example of why the indirect process would be significantly worse.

**Matt** · 2022-09-23 18:52 UTC

It appears Slack has a super primitive CSV import schema, which is what the three discord-to-slack converters I tried last night did. It did work if I then imported to Slack and then exported from Slack, and then imported into Zulip :laughing: I don't think it would be hard for someone to take the DCE CSV format and munge that directly.

**Rein Zustand** · 2022-09-25 07:48 UTC

@Matt Keller if you have a sample fixture of a Discord export, I can make a prototype converter for it.

**Rohitt Vashishtha** · 2022-09-28 07:07 UTC

We can easily generate our own fixtures. [This](https://github.com/Tyrrrz/DiscordChatExporter/tree/master/DiscordChatExporter.Cli.Tests) seems like a good starting point. The instructions prompt to join a specific Discord server they've created with some test cases, which looks like this:

[image.png](https://chat.zulip.org/user_uploads/2/ca/tVqyfFJ1uDJmpppJ6Cw2dB7C/image.png) 

I'll see what kind of output we get...


## ✔ provisioning dependency management

*2022-12-08 to 2022-12-12 · 13 messages · [open in Zulip](https://chat.zulip.org/#narrow/channel/18-tools/topic/.E2.9C.94.20provisioning.20dependency.20management/with/1476603)*

**Josh Klar** · 2022-12-08 08:47 UTC

It occurs to me after authoring https://github.com/zulip/zulip/pull/23793 that we're effectively homebrewing a Linux package manager (of which dozens... or maybe dozens-of-hundreds... of examples already exist) in the `scripts/lib/install-*` scripts, which occasionally share a design language and implementation details, and occasionally do not.

I know I've heard rumblings about Nix here (which I have scar tissue from on the MacOS side of the world, but generally neutral-leaning-positive opinions of in Linux-land), I'll personally throw [KISS Linux's barebones shell-based package manager](https://github.com/kisslinux/kiss) in the ring as being an especially short jump from where we are now, and of course there's dozens of other options, *but*, ultimately I'd like to open a discussion on migrating to something more formal than the current ad-hoc scripts (with no real ETA on when that happens, as it's also not a huge burning issue).

**Anders Kaseorg** · 2022-12-08 09:15 UTC

Nix has many unique advantages that I outlined [here](https://chat.zulip.org/#narrow/stream/3-backend/topic/provision.20via.20nix/near/1354366).

**Anders Kaseorg** · 2022-12-08 09:28 UTC

Any traditional Linux packager really isn’t what we want, because it would make us responsible for managing a package repository somewhere in a universe that’s orthogonal to our Git history. That would be inconvenient, entail a constant risk of breaking old releases that depend on specific versions of the packages, and make it difficult for anyone but the few core contributors with access to the package repository to do development on those packages.

**Josh Klar** · 2022-12-08 09:36 UTC

Don't get me wrong, I've run NixOS on rigs, I get the selling points (and am also familiar with the time investment required) of the full "boiled ocean", if you will. My proposal is smaller in scope and blast radius as a "can be done quickly and at least eliminates much of the repetition and so forth, and hopefully not a thing we feel bad about tossing if Nix were to land" item.

Specifically the one I linked would be able to bring the package history into the tree rather easily, as the package templates are, themselves, shell scripts. One could probably make similar arguments for Portage or other systems that allow overlays/partial repos/etc.

**Anders Kaseorg** · 2022-12-08 09:49 UTC

I don’t see how it solves our problem? We don’t want to commit built packages into the tree, and we only want to spend time building and installing versions that have actually changed, so we’d need to write a wrapper around this thing that’s at least as complicated as the scripts we have now.

**Josh Klar** · 2022-12-08 10:00 UTC

Moving download/proxy args/checksum/etc. logic into some consistent format that can be tersely called in the provisioner (`zulip-dep-helper install transifex-cli nodejs yarn` or whatever) would to me solve the repetition problem across the `install-*` scripts, and I suspect there's ways to go down that road without ending up with the same line count (or duplicated logic) we currently have, and again, as a stopgap along the way to potential more sophisticated systems if desired.

**Anders Kaseorg** · 2022-12-08 10:18 UTC

I’m open to proposals, but I will push back on the idea that repetition is axiomatically problematic, and worry that the leaky abstraction layer that would need to be built over these scripts that have slightly different needs would very likely grow into more of a sprawling mess than the scripts themselves are.

**Josh Klar** · 2022-12-08 10:22 UTC

It's also entirely possible the answer I'm looking for is actually just `source ./packaging_helpers.sh` which defines some Plain Old POSIX SH util functions to encapsulate the truly duplicated bits, without going down the "... and then put it in a tarball, and then blah..." path that effectively all formal package managers do.

Anyway, open to any outcomes here, up to and including "eh, whatever, even if we copy-paste this file 10 more times next year that's still not yet a problem".

**Anders Kaseorg** · 2022-12-08 10:28 UTC

~4 of these scripts have served us for years. We keep them rare on purpose, because each dependency that isn’t part of APT, PyPI, or NPM is another thing that requires unique maintenance work to take updates for it separately.

**Tim Abbott** · 2022-12-08 20:12 UTC

Yeah, ultimately this is our first Go dependency used in the development environment, and no matter what system we're using, adding a new type of thing usually is a bit of extra work.

**Tim Abbott** · 2022-12-08 20:17 UTC

Personally I'd much rather have a 30 line bit of shell duplicated 5 times than a 2k line third-party shell script. We can of course deduplicate by having a bit of a shell library, but I'm not sure it'd actually be easy to refactor to that model.

**Rein Zustand** · 2022-12-11 13:45 UTC

I think the man-hour effort is better spent on transitioning to Nix than to replace the existing provisioning. The existing provisioning is already time tested, and anything temporary that would replace it, is not.

**Notification Bot** · 2022-12-12 19:49 UTC

@Josh Klar has marked this topic as resolved.


## ./tools/lint

*2023-02-24 to 2023-02-24 · 2 messages · [open in Zulip](https://chat.zulip.org/#narrow/channel/18-tools/topic/.2E.2Ftools.2Flint/with/1513150)*

**Yash RE** · 2023-02-24 08:55 UTC

Is there a way to get lint to run on all the files changed in just the previous commit? The workaround I use is to just "undo last commit" in vscode (which is essentially soft reset on HEAD) and then run `./tools/lint -m`.

**Anders Kaseorg** · 2023-02-24 16:49 UTC

You can give a list of files:

```shell
tools/lint $(git diff --name-only @^)
```


## TinglingGit (typescript migration)

*2023-03-19 to 2023-03-21 · 9 messages · [open in Zulip](https://chat.zulip.org/#narrow/channel/18-tools/topic/TinglingGit.20.28typescript.20migration.29/with/1527932)*

**xoldyckk** · 2023-03-19 14:02 UTC

[Screenshot_20230319_193008.png](https://chat.zulip.org/user_uploads/2/15/XqlSG1Bq86bLzUfq3P5MO7ew/Screenshot_20230319_193008.png) 
@Anders Kaseorg TinglingGit tool by zulip, does it no longer work? It hasn't got an update in 4 years, could this be related to the issue I'm having?

**Anders Kaseorg** · 2023-03-19 17:39 UTC

I’ve never used that tool. It seems to be Python 2–only.

**Alex Vandiver** · 2023-03-19 17:58 UTC

It's also not used by Zulip, so I'm not sure why you're running it.

**xoldyckk** · 2023-03-19 18:06 UTC

It's mentioned here:- https://zulip.readthedocs.io/en/latest/testing/typescript.html#migration-strategy

**Cyphase** · 2023-03-19 19:19 UTC

Which links to this: https://github.com/zulip/TinglingGit

**xoldyckk** · 2023-03-19 20:24 UTC

(replying to Cyphase)
> Which links to this: https://github.com/zulip/TinglingGit
Yes. So, was I wrong about something?

**Cyphase** · 2023-03-19 23:20 UTC

No; I was backing you up in fact. :smile: It's actually a Zulip tool. Looks like it was written by @Aditya Bansal, with the README by @Tim Abbott.

**Tim Abbott** · 2023-03-20 17:18 UTC

We've not used it in a few years, someone should feel free to update it but I don't think we need it for this particular migration.

**Tim Abbott** · 2023-03-21 01:03 UTC

The cases where it's useful is when one is rewriting large files that might have a lot of internal refactoring in other PRs, but my experience with the TypeScript migration thus far is that it's unlikely to have major merge conflicts with other work that feels worth planning around.


## Ai course generation tools

*2023-08-03 to 2023-08-04 · 6 messages · [open in Zulip](https://chat.zulip.org/#narrow/channel/18-tools/topic/Ai.20course.20generation.20tools/with/1619449)*

**PizChy Wachida** · 2023-08-03 18:06 UTC

ตัวอย่าง: https://coursegen.ai/my-courses

**Aman (amanagr)** · 2023-08-03 18:10 UTC

[Screenshot-2023-08-03-at-11.40.21-PM.png](https://chat.zulip.org/user_uploads/2/9d/AMFOTBOosYhoBBYTZCOogprK/Screenshot-2023-08-03-at-11.40.21-PM.png)
For some time now @PizChy Wachida

**Alex Vandiver** · 2023-08-03 18:55 UTC

This seems spammy, since it's @PizChy Wachida's only message, and they joined today.

**PizChy Wachida** · 2023-08-04 22:12 UTC

@Aman (amanagr) https://github.com/PizChy-WachidA/coursegen

**PizChy Wachida** · 2023-08-04 22:40 UTC

@Alex Vandiver I joined 1 day. That doesn't mean I'm spam.  You must have forgotten that..everyone starts from 1. 🤐

**Greg Price** · 2023-08-04 23:26 UTC

@PizChy Wachida This server's purpose is for discussions in the Zulip development community, not for people to show up and advertise their unrelated projects. Doing so is spam.

Please review the community guidelines:
https://zulip.com/development-community/


## Fedora 38

*2023-08-21 to 2023-12-17 · 6 messages · [open in Zulip](https://chat.zulip.org/#narrow/channel/18-tools/topic/Fedora.2038/with/1628750)*

**Shu Chen** · 2023-08-21 18:40 UTC

I managed to get provision working in Fedora 38: see https://github.com/sirpengi/zulip/commit/86c0220811a1ab001aa71afc2e0617dea5eb60e8
I do have a few questions about how to proceed:
- not sure what to do about jump from F34 to F38. Should we remove the old versions? 34 was EOL in June 2022: https://docs.fedoraproject.org/en-US/releases/eol/
- There's no issue for this yet, I could make one, or I could co-opt https://github.com/zulip/zulip/issues/20635 for this?
- Is there a test suite I can integrate this to, I suspect we'd like more confidence than "it works on Shu's computer"?

**Tim Abbott** · 2023-08-21 18:43 UTC

Feel free to coopt https://github.com/zulip/zulip/issues/20635 and close that with your PR.

For development environment provisioning for platforms that we don't support in production; we don't have any automated tests -- generally the individual(s) who are using it will notice if something breaks, which tends to be pretty rare, and that person will be well-equipped to fix the issue.

**Tim Abbott** · 2023-08-21 18:44 UTC

I think it's fine to drop Fedora 34 support; generally we've had at most one Fedora user at a time and we tend to just leave support in place for whatever version(s) someone is actively using, which is why the support gets stale from time to time.

**Tim Abbott** · 2023-08-21 18:46 UTC

(And if someone new shows up with Fedora 37 or whatever, it's probably only a couple lines of changes for them to get the development environment working)

**Shu Chen** · 2023-08-21 18:46 UTC

Great, I can proceed from here to get this integrated then. I'll be a long-term active Fedora user so maybe it's possible to reach 2 Fedora users at a time soon!

**Old Schepperhand** · 2023-12-17 23:53 UTC

@Shu Chen as you asked for it, here I am :wave: :wink:


## Prohibiting automatic activation of zulip-py3-venv

*2023-09-11 to 2023-09-12 · 7 messages · [open in Zulip](https://chat.zulip.org/#narrow/channel/18-tools/topic/Prohibiting.20automatic.20activation.20of.20zulip-py3-venv/with/1638012)*

**Sudip Bose** · 2023-09-11 13:19 UTC

Hi fellas, I saw this issue: https://github.com/zulip/zulip/issues/15029. Under Zulip's good first issue tag, I want to work on it. While I do know how to claim it, I'm wondering whether this is the right place to ask some questions about it. FYI, this issue is labelled under '''area:provision''', since #**provision help**  is specifically dedicated to helping set up the environment, not discussing issues about it, I came here to ask. Pardon me if this is not the right thread. Can you please point me where I should discuss Provision issues in Zulip chat?

**Alex Vandiver** · 2023-09-11 14:11 UTC

Here is a fine place!

**Sudip Bose** · 2023-09-11 17:59 UTC

(replying to Alex Vandiver)
> Here is a fine place!

Hey, Alex, thanks for the heads-up! So if you looked at the issue, it's about zulip-py3-venv getting automatically activated when we enter the shell for a given setup. @Aman (amanagr) mentioned that the virtual environment should only be activated for vagrant/docker/droplets setup while potentially ignoring others.

When we run  `./tools/provision`, along with upgrading and installing the development environment, it creates a file `.zprofile` in the root contains the activation command `source /srv/zulip-py3-venv/bin/activate` and also appends this command to my bash profile at `.profile` (at least this is for my WS2 machine, assuming in other setups things will be more or less same).

 If I could find the file that writes this command and insert a check like if the user machine is something other than vagrant, docker, or droplets, then it should avoid writing the activation command to the user's bash profile. That would solve the problem. So I checked the provision bash file at `zulip/tools/provision`. I don't see any line that says - `"source " + os.path.join(VENV_PATH, "bin", "activate")`, which I think was used to write the command to the bash profile of the user. Since the issue is old, there is a possibility that the line is written somewhere else. Can you please tell me where I should look? Thanks for reading this. Your help would be greatly appreciated.

**Greg Price** · 2023-09-11 19:36 UTC

In general a good strategy for finding the code that's responsible for something is to find a string that will probably appear in that code, and then use `git grep` to search the codebase for that.

Here, it seems like the relevant code will very likely have to mention the filename ".zprofile", and that's a pretty distinctive string. So try running `git grep zprofile`.

**Greg Price** · 2023-09-11 19:41 UTC

(replying to Sudip Bose)
> So I checked the provision bash file at `zulip/tools/provision`. I don't see any line that says - `"source " + os.path.join(VENV_PATH, "bin", "activate")`

Alternatively you could search for this string: `git grep -F '"source " + os.path.join(VENV_PATH, "bin", "activate")'`. And you're in luck — that finds a match too!

The key is that you search the whole codebase, with `git grep` or another tool, rather than a single file. Or possibly start in a single file, but then broaden it when you don't find what you're looking for there.

**Sudip Bose** · 2023-09-12 07:39 UTC

That's a great advice @Greg Price ! Thank you so much for the help.

**Sudip Bose** · 2023-09-12 12:48 UTC

I found the file that was responsible for writing the activation command `source /srv/zulip-py3-venv/bin/activate` to the user's bash_profile. So I add a condition that checks the host machine's type before writing it. If the host machine is a WSL container or a native Linux distribution, then I'm simply avoiding writing the command to the bash profile.

I'm using Python's os module to check whether `"/proc/sys/fs/binfmt_misc/WSLInterop"` or `/etc/os-release` paths exist on the host machine. The former path is a common path for all WSL containers, and the latter one is common for native Linux machines, or at least common for all the distributions that Zulip currently supports. I checked on my machine, which is a WSL2 container, and now the virtual environment is not getting activated automatically.

I already claimed the issue; should I raise a PR with all the necessary information, or are there any tests or anything else that I need to do? Can any of you please help? Thanks.


## ✔ How to logout

*2024-01-05 to 2024-01-05 · 2 messages · [open in Zulip](https://chat.zulip.org/#narrow/channel/18-tools/topic/.E2.9C.94.20How.20to.20logout/with/1714077)*

**Prasanth Kumar Taviti** · 2024-01-05 07:38 UTC

#**tools**  how to logout

**Notification Bot** · 2024-01-05 07:38 UTC

@Prasanth Kumar Taviti has marked this topic as resolved.


## How to update frontend webpage

*2024-03-25 to 2024-03-28 · 7 messages · [open in Zulip](https://chat.zulip.org/#narrow/channel/18-tools/topic/How.20to.20update.20frontend.20webpage/with/1765939)*

**Yu-Cheng, Xia** · 2024-03-25 15:14 UTC

Hi, I am new to Zulip. I am dealing with an issue which need to change the scrollbar visibility, and I want to see that in my local machine. However, I don't know which tool should I use to update the zulip webpage. Please help me out! Thanks!

**Tim Abbott** · 2024-03-26 00:17 UTC

Which of our developer tutorials have you read to try to answer that question?

**Yu-Cheng, Xia** · 2024-03-27 15:44 UTC

I have checked multiple tutorials like [development tutorial](https://zulip.readthedocs.io/en/latest/development/using.html) and [front-end change](https://zulip.readthedocs.io/en/latest/tutorials/new-feature-tutorial.html#frontend-changes)

**Yu-Cheng, Xia** · 2024-03-27 15:46 UTC

@Tim Abbott  It mentioned that the /web/src will be automatically updated via webpack, but I tried to reload the website and nothing happened.

**Tim Abbott** · 2024-03-27 18:35 UTC

Can you be very explicit what you're doing an what you're expecting to change?

**Yu-Cheng, Xia** · 2024-03-28 10:16 UTC

Sure! I am trying to solve issue [#29393](https://github.com/zulip/zulip/issues/29393) and this should be solved by changing the css file under web/styles or the `right_sidebar.hbs` under web/templates. However, after I made some modification on either file, there was no different shown on the website.

**Tim Abbott** · 2024-03-28 19:29 UTC

Templates changes you need to reload for; CSS you usually don't. But my first theory would be that you're not actually making the changes you think you are.


## wps

*2024-04-03 to 2024-04-03 · 4 messages · [open in Zulip](https://chat.zulip.org/#narrow/channel/18-tools/topic/wps/with/1774114)*

**Aj Boctil** · 2024-04-03 18:14 UTC

hi how to fix wps problems?

**Tim Abbott** · 2024-04-03 18:14 UTC

You're going to need to provide more detail about what problem you're having. See our community guidelines advice on how to ask good questions.

**Aj Boctil** · 2024-04-03 18:16 UTC

how fix the unsave documents when it terms of saving the documents

**Tim Abbott** · 2024-04-03 18:19 UTC

Are you in the right place? This chat is for conversations about [Zulip](https://zulip.com).


## renumber-migrations gets stuck at 0501

*2024-04-08 to 2024-08-09 · 19 messages · [open in Zulip](https://chat.zulip.org/#narrow/channel/18-tools/topic/renumber-migrations.20gets.20stuck.20at.200501/with/1776776)*

**Tanmay Kumar (tnmkr)** · 2024-04-08 17:54 UTC

There are two conflicting migrations:
```
(zulip-py3-venv) vagrant@fbc57b970081:/srv/zulip$ tools/renumber-migrations
Conflicting migrations:
1. 0501_mark_introduce_zulip_view_modals_as_read.py
2. 0501_delete_dangling_usermessages.py
Enter the order in which these migrations should be arranged:
```
There is no way to tell the tool to "do nothing", other than [hardcoding migrations to skip](https://github.com/zulip/zulip/blob/f4d109c289f614273b43b411cbd8d1fad128842e/tools/renumber-migrations#L57).

**Tanmay Kumar (tnmkr)** · 2024-04-08 18:00 UTC

Created PR #29653 to skip 0501

**Tanmay Kumar (tnmkr)** · 2024-04-08 19:00 UTC

Actually i think my commit message may not be correct?
```
renumber-migrations: Skip migration 0501.
Security fix cf8b9ad needed migration
`zerver/0501_delete_dangling_usermessages` on the 8.x branch (3db1733).
This resulted in two migrations numbered 0501, due to which this tool
always got stuck on 0501.
```

The last migration on `8.x` branch was 496, so according to my logic this migration should've been numbered 497. But it obviously isn't.

**Karl Stolley** · 2024-04-08 19:12 UTC

Have you read the Zulip documentation about migrations? There's useful information for handling numbering conflicts: https://zulip.readthedocs.io/en/latest/subsystems/schema-migrations.html

**Karl Stolley** · 2024-04-08 19:15 UTC

Oh I see. These are existing migrations

**Neil Pilgrim (neiljp)** · 2024-04-08 23:30 UTC

See https://chat.zulip.org/#narrow/stream/3-backend/topic/zerver.2F0501.20migrations.20break.20upgrades.20to.20main.2C.20future.209.2Ex/near/1773766

**Neil Pilgrim (neiljp)** · 2024-04-08 23:31 UTC

I assumed from reading that conversation, that the issue was fixed for `main` and the `8.x` branches, but perhaps not?

**Alex Vandiver** · 2024-04-09 02:09 UTC

The *migrations* are fine.  The `renumber-migrations` tool is not smart enough to handle the situation, howeverr.

**Tim Abbott** · 2024-04-10 15:37 UTC

The tool is pretty basic and likely deserves a rewrite to handle this and other more basic situations better.

**Anders Kaseorg** · 2024-04-10 19:19 UTC

First someone should check whether [django-linear-migrations](https://adamj.eu/tech/2020/12/10/introducing-django-linear-migrations/) can be made to work for our scenario.

**Tim Abbott** · 2024-04-10 20:06 UTC

Oh yeah, thanks for the reminder, I am intrigued by that possibility.

**Rohan Gudimetla** · 2024-07-11 12:39 UTC

One good thing about it is it would show merge conflicts in case we need to renumber migrations after rebase.

However. seems like their `rebase_migration` command to renumber the migrations currently only supports single migration in an app ([open issue](https://github.com/adamchainz/django-linear-migrations/issues/27)).

**Tim Abbott** · 2024-07-11 16:56 UTC

That's a pretty important limitation. I expect we'd need to fix that if we were to use it. He did say PRs welcome, though who knows if the maintainer is still active; we can always fork if needed I suppose.

**Tim Abbott** · 2024-07-11 16:56 UTC

So might be reasonable to spend a bit of time looking at the code and whether it's reasonable.

**Rohan Gudimetla** · 2024-08-05 14:05 UTC

I opened [#343](https://github.com/adamchainz/django-linear-migrations/pull/343) there (waiting for response from maintainer), which consist of 2 commits:
- Commit 1 - Makes it possible to renumber chains of migrations in a single app (previously, it used to handle just a single migration)
- Commit 2 - While rebasing migrations, if the migration to be rebased is applied, it unapplies and then rebases them (Previously is used to throw out an error asking the user to rebase).

**Rohan Gudimetla** · 2024-08-05 14:05 UTC

After these changes, it could be used I guess.

**Greg Price** · 2024-08-08 18:17 UTC

A direct link to that PR: https://github.com/adamchainz/django-linear-migrations/pull/343

**Anders Kaseorg** · 2024-08-08 23:50 UTC

@Rohan Gudimetla If your changes are independent from each other, I recommend submitting them as two independent PRs, in order to make it easier for the maintainer to review and merge each change separately. (Small open source projects are typically maintained on volunteer time, and it’s easier to find spare time for multiple small tasks than for one large task.)

**Rohan Gudimetla** · 2024-08-09 11:47 UTC

Sure, opened a separate PR - https://github.com/adamchainz/django-linear-migrations/pull/346 to unapply migrations while rebase (extracted it from previous PR).


## Linting JSON files

*2024-12-18 to 2024-12-19 · 20 messages · [open in Zulip](https://chat.zulip.org/#narrow/channel/18-tools/topic/Linting.20JSON.20files/with/2008522)*

**Niloth** · 2024-12-18 17:20 UTC

I noticed that we don't have any linting for JSON files.

**Niloth** · 2024-12-18 17:20 UTC

I searched the docs for any mentions of recommended conventions. Found a [mention here](https://zulip.readthedocs.io/en/stable/documentation/api.html#:~:text=usually%20json.dumps(result%2C%20indent%3D4%2C%20sort_keys%3DTrue)) of `json.dumps(result, indent=4, sort_keys=True)`, that's it. The [JSON Integration](https://zulip.com/integrations/doc/json) uses 2 spaces.

**Niloth** · 2024-12-18 17:21 UTC

Of the ~3000 JSON files in the repo, 6 different indentation conventions are being used, and 2/3rds of them use 2 spaces.

**Niloth** · 2024-12-18 17:21 UTC

While I do realise that since JSON is a serialization format and not a presentation format, there is usually no standard indentation, but wouldn't we still prefer having a particular convention? Would we want to lint for it, with an autofix option?

**Tim Abbott** · 2024-12-18 17:24 UTC

So most of the JSON files in the repository are fixtures captured from third-party services, and our preference has been to preserve the exact input that the third party provided, rather than processing/canonicalizing it in some way.

**Tim Abbott** · 2024-12-18 17:25 UTC

In theory, it shouldn't matter if we canonicalize it -- it's very unlikely that we'll have an issue where our JSON parser fails to process something -- but there's also very little benefit to doing any processing on files whose purpose is to be raw data captured from a third-party service.

**Niloth** · 2024-12-18 17:30 UTC

Isn't the benefit just uniformity?
I've come across integrations with fixtures that have several different indentations, and editing them can tag the entire fixture as modified (depending on your editor settings), and it was unnecessarily difficult when I was trying to use diffs between fixtures to identify varying fields.

**Tim Abbott** · 2024-12-18 17:37 UTC

In theory, we should never be editing captured fixtures. (But of course there end up being reasons to do that). 

The main cost of canonicalizing them is that it requires folks contributing integrations to do canonicalization work after capturing them to pass the linter. Probably not a big deal.

I have no objection to doing a one-time formatting of JSON fixtures from webhooks if it'll make your life easier for maintaining integrations. 

We could also add a linter, but I'd want to check it isn't slow given the very large volume of fixtures. I'd do `indent=2, sort_keys=True` for fixtures, since they tend to be very highly nested. (indent=4 can be more readable for other contexts). See `corporate/tests/test_stripe.py` for existing example logic for how we do this for Stripe fixtures, which we have 1770 of in `corporate/tests/stripe_fixtures/`, and uses those flags.

**Anders Kaseorg** · 2024-12-18 19:56 UTC

Prettier formats our JSON files, except the ones we specifically ignore using `.prettierignore` in `/corporate/tests/stripe_fixtures`, `/locale`, `/zerver/tests/fixtures`, and `/zerver/webhooks/*/fixtures`. We could un-ignore them.

**Anders Kaseorg** · 2024-12-18 20:00 UTC

However, before doing that, we should decide whether we really want to continue sleepwalking toward 4-space indents when the rest of the JS world is using 2.

**Niloth** · 2024-12-18 20:05 UTC

After @Tim Abbott's replies, I was thinking that if I'm the only person that gets benefited, then I'd rather just come up with a local solution (with a couple of extra but automated steps) than editing the entire repo and making everyone conform to it.

**Niloth** · 2024-12-18 20:08 UTC

(replying to Anders Kaseorg)
> we should decide whether we really want to continue sleepwalking toward 4-space indents when the rest of the JS world is using 2.
I was also wondering about the `sort_keys=True`, while that helps a lot in creating uniform fixtures, some fixtures are originally sorted conveniently, with related fields being placed near each other.

**Tim Abbott** · 2024-12-18 21:11 UTC

(replying to Anders Kaseorg)
> However, before doing that, we should decide whether we really want to continue sleepwalking toward 4-space indents when the rest of the JS world is using 2.

I don't think there was any proposal to use 4-space indents anywhere new? My proposal was to use 2-space indents here, without spending attention on other places where indentation occurs.

(Since the existing large population of JSON fixtures, the stripe fixtures, is already 2-space indented)

**Anders Kaseorg** · 2024-12-18 21:30 UTC

We have Prettier configured for 4 spaces.

**Anders Kaseorg** · 2024-12-18 21:31 UTC

We want to be consistent with `.editorconfig`, because that’s the root of @Niloth’s editor settings issue.

**Tim Abbott** · 2024-12-18 23:16 UTC

Does prettier support different configuration for different file types?

**Anders Kaseorg** · 2024-12-19 00:36 UTC

Yes. I’m not saying this is hard. I’m saying we should make a deliberate decision.

**Tim Abbott** · 2024-12-19 00:39 UTC

We have just these JSON files that are not fixtures or translation data in zulip/zulip:
```
$ git ls-files | grep [.]json$ | grep -v fixture | grep -v ^locale/
.vscode/extensions.json
package.json
tools/duplicate_commits.json
tools/screenshots/companies.json
tools/screenshots/for-education.json
tools/screenshots/for-events.json
tools/screenshots/for-research.json
tools/setup/emoji/emoji_map.json
tools/setup/lang.json
tsconfig.json
web/shared/package.json
web/shared/tsconfig.json
web/webpack.assets.json
web/webpack.dev-assets.json
zerver/management/data/unified_reactions.json
```

**Tim Abbott** · 2024-12-19 00:41 UTC

Yeah. I have no objection to adjusting our prettier configuration to doing 2-space indent for JSON; it's very little stuff that we edit manually, will have almost no merge conflicts, and we don't have a ton of integrations PRs open that would require running the linter on after a rebase.

**Tim Abbott** · 2024-12-19 00:41 UTC

I think we need to be more deliberative with TS files, since there's a lot of them and it'll be messier for ongoing work; if we want to make a change, I'd probably want to do it with the 10.0 release for backporting sanity.


## non-mypy type checking

*2025-05-18 to 2025-05-20 · 16 messages · [open in Zulip](https://chat.zulip.org/#narrow/channel/18-tools/topic/non-mypy.20type.20checking/with/2176327)*

**Alex Vandiver** · 2025-05-18 14:23 UTC

Meta just released their Rust-based type checker: https://pyrefly.org/

**Tim Abbott** · 2025-05-18 19:39 UTC

I think we'll want to wait for the Rust-based one that the `uv` folks to come out before migrating, since if I recall correctly, Pyre requires a different strategy for things like Django plugins.

**Alex Vandiver** · 2025-05-19 11:44 UTC

Ah, well: 

On May 13, [Charlie Marsh wrote](https://bsky.app/profile/crmarsh.com/post/3lp2xij4tas2w):
> Today, we’re announcing the preview release of ty, an extremely fast type checker and language server for Python, written in Rust.
>
> In early testing, it's 10x, 50x, even 100x faster than existing type checkers. (We've seen >600x speed-ups over Mypy in some real-world projects.)

**Alex Vandiver** · 2025-05-19 14:42 UTC

A very naïve `uvx ty check` on the Zulip codebase completes in ~7s for me.  However, actually being able to switch to it is likely blocked on https://github.com/astral-sh/ty/issues/291 or similar, or none of the Django pieces will typecheck.

**Greg Price** · 2025-05-19 17:30 UTC

This is an interesting comment on that thread:

> I will add in that based on my professional on the job experience with Django for 11 years I have viewed typing Django as pretty much a lost cause. […] I had previously success re-tooling Django classes to add in type information that gave better results than the mypy Django plugins.

I don't have a first-hand sense of how well our Django usage is covered now by type-checking. How does that description compare with our experience?

**Anders Kaseorg** · 2025-05-19 17:48 UTC

Mypy without the Django plugin gives us 3113 errors, mostly about models missing `id` fields, foreign key `_id` fields, and reverse relations, and some about typed dictionaries for query results. Manually annotating all of that would be error-prone, and failing to manually annotate it would encourage us to write uglier and slower code.

**Anders Kaseorg** · 2025-05-19 17:53 UTC

This is just one of many ways that Django is proving to be a bad tool for today’s era of development. (Other notable ways include its still-poor async support and its total lack of modularity.)

**Zixuan James Li** · 2025-05-19 18:01 UTC

> Django dev teams typically aren't interested in adopting type checking

Specially, a reason that django-stubs couldn't get integrated into Django is that plugins are really type-checker dependent.

There was a [PR](https://github.com/django/deps/pull/65) (in 2020) integrating some form of static type checking into Django. Ultimately it didn't go through, the Django Technical Board [suggested](https://groups.google.com/g/django-developers/c/C_Phs05kL1Q) that there are "competing technologies" (type checkers) and "at this moment Django is not in a position to favor any one". This is relevant because the dynamic nature of Django makes type checking behavior dependent on a specific implementation.

This might have changed, but I think plugins aren't getting standardized any time soon. Sometimes type checkers implement special logic, but that too is type-checker dependent.

**Anders Kaseorg** · 2025-05-19 18:06 UTC

If the Django devs were serious about enabling type checking, they would be migrating towards APIs that are type-checkable without requiring custom plugins, in coordination with the people who are adding the needed type features via Python PEPs.

**Anders Kaseorg** · 2025-05-19 18:08 UTC

But the market for a typed Django is shrinking as the users who care about type checking start migrating from Django to modern tech stacks instead.

**Tim Abbott** · 2025-05-19 19:01 UTC

I think we will want to wait and see how `ty` progresses on this issue. A very large portion of Python web applications are written in Django, and they will need to have a way to check Django codebases if they want to dominate the Python tooling market, which they very clearly do.

**Greg Price** · 2025-05-19 19:45 UTC

(replying to Anders Kaseorg)
> migrating towards APIs that are type-checkable without requiring custom plugins, in coordination with the people who are adding the needed type features via Python PEPs.

One thing I learned about from that thread is [PEP 681 dataclass transforms](https://peps.python.org/pep-0681/), whose ambitions explicitly included ORMs and in particular Django:
> Several popular libraries have behaviors that are similar to dataclasses, but these behaviors cannot be described using standard type annotations. Such projects include attrs, pydantic, and object relational mapper (ORM) packages such as SQLAlchemy and Django.

Sadly it doesn't look like there's been any work to actually apply them to Django, at least not that I found with a few minutes' searching just now. SQLAlchemy has done it, though:
https://docs.sqlalchemy.org/en/20/orm/dataclasses.html

**Anders Kaseorg** · 2025-05-19 19:52 UTC

Yeah, also [SQLModel](https://sqlmodel.tiangolo.com/features/) (which is based on SQLAlchemy and Pydantic).

**Greg Price** · 2025-05-19 19:54 UTC

Looks like a good idea!

**Steve Howell** · 2025-05-20 17:31 UTC

I've been listening to this today about ty (formerly under the code name Red Knot):

https://talkpython.fm/episodes/show/506/ty-astrals-new-type-checker-formerly-red-knot

This is the Rust-based one that the `uv` folks are coming out with, as Tim mentioned above.

I don't have any opinions on how this applies to Zulip, or the Django issues in particular, but the podcast is a pretty easy listen if folks are interested.

**Steve Howell** · 2025-05-20 17:35 UTC

One thing they mention fairly early in the podcast (sorry, don't have the timestamp handy) is that one of their goals, apart from obvious performance gains, is to "smooth the curve" for projects that have systems that are type-safe in practice but maybe cause type checkers to choke on a bunch of false positives.  Their comments are in a slightly different context than Zulip's.


## weave semantic merge

*2026-03-30 to 2026-03-30 · 5 messages · [open in Zulip](https://chat.zulip.org/#narrow/channel/18-tools/topic/weave.20semantic.20merge/with/2422603)*

**Alex Vandiver** · 2026-03-30 18:13 UTC

TIL about https://github.com/Ataraxy-Labs/weave / https://ataraxy-labs.github.io/weave/

I wonder if it'd eliminate the trivial import conflicts I get sometimes.  My only question I can't tell from their docs is how to ensure that the resultant output passes `ruff-format` (e.g. in sorting and wrapping imports)

**Alex Vandiver** · 2026-03-30 18:55 UTC

Sadly, doesn't look like it manages that.

**Alex Vandiver** · 2026-03-30 19:48 UTC

```
[backports-11.x b34237e87a] import_util: Refactor a `get_domain_name_for_import`.
 Author: Mateusz Mandera <mateusz.mandera@zulip.com>
 Date: Thu Jan 22 17:25:24 2026 +0700
 2 files changed, 12 insertions(+), 3 deletions(-)
weave [zerver/data_import/slack.py]: unchanged: 21, ours-only: 16, theirs-only: 1, added-ours: 4, deleted: 2, CONFLICTS: 1
weave: 1 conflict(s) in 'zerver/data_import/slack.py'
  - interstitial `file_header`: both modified
Auto-merging zerver/data_import/import_util.py
Auto-merging zerver/data_import/slack.py
CONFLICT (content): Merge conflict in zerver/data_import/slack.py
error: could not apply d7de16ab18... import_util: Refactor a `ImportedBotEmail`.
hint: After resolving the conflicts, mark them with
hint: "git add/rm <pathspec>", then run
hint: "git cherry-pick --continue".
hint: You can instead skip this commit with "git cherry-pick --skip".
hint: To abort and get back to the state before "git cherry-pick",
hint: run "git cherry-pick --abort".
hint: Disable this message with "git config set advice.mergeConflict false"
```

**Greg Price** · 2026-03-30 20:36 UTC

Definitely seems like a good idea if the execution is good.

There's a lot of dynamic range in how good or bad the execution could be, though. It's a complex problem.

**Greg Price** · 2026-03-30 20:38 UTC

If a tool like this is otherwise really good but the output isn't formatted, it could still be worth using — just making a habit of following with `git rebase -x ruff-format`.

(But also, for a tool with this goal I think it'd be a very sensible feature request for it to learn to run an auto-formatter after resolving any conflicts.)


## codespell lint integration (#39467)

*2026-06-08 to 2026-06-25 · 7 messages · [open in Zulip](https://chat.zulip.org/#narrow/channel/18-tools/topic/codespell.20lint.20integration.20.28.2339467.29/with/2475380)*

**Joel Taylor** · 2026-06-08 13:54 UTC

Hi! I opened #39467 (https://github.com/zulip/zulip/pull/39467) to integrate codespell into the tools/lint framework (issue #20082). @laurynmm suggested I discuss the approach here since I took a different route than the issue described.

The issue flagged per-path exclusions as the tricky part, and the implied fix was extending the zulint interface to support them. Instead of changing that interface, I register codespell as an external linter and carry the existing exclusions through codespell's own --skip option, reusing the current .codespellignore. That keeps zulint untouched while still getting codespell into ./tools/lint (so it respects --modified and --fix). I also dropped the now-redundant standalone run-codespell CI step.

Does that direction sound reasonable, or would you prefer I extend the zulint exclusion interface as the issue originally suggested? Happy to go either way.

**Joel Taylor** · 2026-06-09 14:55 UTC

Hey! I opened #39467 to wire codespell into the tools/lint framework (#20082). The issue called out per-path exclusions as the tricky bit and leaned toward changing the zulint interface. I took a different route: instead of touching the zulint interface, I carry the existing exclusions through codespell's own --skip option and reuse .codespellignore, then dropped the now-redundant standalone codespell CI step. Wanted to sanity-check that approach with folks here before it goes further — does keeping it out of the zulint interface seem reasonable, or is there a reason the exclusions should live there?

**Notification Bot** · 2026-06-09 15:30 UTC

[A message](https://chat.zulip.org/#narrow/channel/18-tools/topic/codespell.20lint.20integration.20.28.2339467.29/near/2475380) was moved here from #**tools>codespell** by @Lauryn Menard.

**Lauryn Menard** · 2026-06-09 15:33 UTC

This was the [comment](https://github.com/zulip/zulip/pull/19995#issuecomment-947387626) from @Anders Kaseorg that is linked to in the issue description:

> zulint lists all tracked files in one `git ls-files` invocation, with the result shared among all linters to be run. This invocation takes something something like 4 milliseconds, essentially all of which is `fork`+`exec` overhead and not actual computation. For all practical purposes, the only rele …

**Lauryn Menard** · 2026-06-09 15:34 UTC

The issue is from 2021, so not sure if much has or hasn't changed with this.

**Joel Taylor** · 2026-06-09 21:40 UTC

Thanks @Lauryn (and Anders for the context). I think the PR actually lands on the practical side of both points:

On fork+exec — codespell is registered as a single external_linter, so it runs once over the shared git ls-files result (filtered by the extension list), adding just one exec and picking up --modified scoping for free. No per-file forking.

On the per-linter exclude limitation Anders mentioned (exclude only living on the shared list_files call) — that's exactly why I didn't touch the zulint interface here. I carry codespell's path exclusions through its native --skip plus .codespellignore, so the codespell-specific excludes stay out of the shared zulint config and I don't need the interface extension for this case.

What I deliberately didn't do is the larger redesign Anders sketched (dropping the list-of-languages concept in favor of path/shebang regexes or globfilter). That feels like a separate, bigger change to the zulint API, and out of scope for just wiring codespell into the framework — happy to open a separate issue/discussion for it if there's appetite.

So my question for the team: is the minimal "lean on codespell's own --skip" approach acceptable to land now, or would you rather hold codespell integration until zulint grows real per-linter file selection?

**Tim Abbott** · 2026-06-25 02:18 UTC

I think we don't need to block on zulint changes for something like this.


## Unsupported Platform Error on Ubuntu-Derivative distros

*2026-07-18 to 2026-07-27 · 2 messages · [open in Zulip](https://chat.zulip.org/#narrow/channel/18-tools/topic/Unsupported.20Platform.20Error.20on.20Ubuntu-Derivative.20distros/with/2497255)*

**Phant0m1zed** · 2026-07-18 11:16 UTC

I was setting up the local development environment using `tools/provision` and hit this:

```
CRITICAL:root:Unsupported platform: zorin 18
Provisioning failed (exit code 1)!
Look at the traceback(s) above to find more about the errors.
Resolve the errors or get help on chat.
If you can fix this yourself, you can re-run tools/provision at any time.
Logs are here: zulip/var/log/provision.log
```

Zorin OS 18.1 core is based directly on Ubuntu 24.04. `/etc/os-release` confirms it:

```
PRETTY_NAME="Zorin OS 18.1"
NAME="Zorin OS"
VERSION_ID="18"
VERSION="18.1"
VERSION_CODENAME=noble
ID=zorin
ID_LIKE="ubuntu debian"
UBUNTU_CODENAME=noble
```

Other derivatives like Mint and Pop!_OS likely hit the same issue.

I checked `tools/lib/provision.py` and found the root cause:

```python
distro_info = platform.freedesktop_os_release()
vendor = distro_info["ID"]
os_version = distro_info["VERSION_ID"]
if vendor == "debian" and os_version == "12":  # bookworm
    POSTGRESQL_VERSION = "15"
elif vendor == "debian" and os_version == "13":  # trixie
    POSTGRESQL_VERSION = "17"
elif vendor == "ubuntu" and os_version == "22.04":  # jammy
    POSTGRESQL_VERSION = "14"
elif vendor == "ubuntu" and os_version == "24.04":  # noble
    POSTGRESQL_VERSION = "16"
elif vendor == "ubuntu" and os_version == "26.04":  # resolute
    POSTGRESQL_VERSION = "18"
elif vendor == "fedora" and os_version in ("43", "44"):
    POSTGRESQL_VERSION = "17"
elif vendor == "rhel" and os_version.startswith("7."):
    POSTGRESQL_VERSION = "10"
elif vendor == "centos" and os_version == "7":
    POSTGRESQL_VERSION = "10"
else:
    logging.critical("Unsupported platform: %s %s", vendor, os_version)
    sys.exit(1)
```

This only matches exact `ID` values, so derivative distros always fall through to the `else` branch, even if their underlying base is actually supported. It also means this list needs manual updates every time Ubuntu/Debian/Fedora release a new version e.g., Ubuntu 28.04 would hit the same error next year until someone adds it.

Is the narrow OS list an intentional design choice, or would a fix that recognizes Ubuntu-derivatives via `ID_LIKE`/`UBUNTU_CODENAME` be welcome? I would be delighted to write a fix if so.

**Alex Vandiver** · 2026-07-27 17:22 UTC

> It also means this list needs manual updates every time Ubuntu/Debian/Fedora release a new version e.g., Ubuntu 28.04 would hit the same error next year until someone adds it.

That's pretty intentional -- it means that we have an explicit step to test the dev/prod experience on the new release before we officially  add it to the supported set.

We don't really have the bandwidth to add more supported distros.  If Zorin is sufficiently compatable, you can add a local `elif` block and provision.  But we don't have the time to gain familiarity on a new distro, sufficient to be able to help debug it, so I don't see us expanding the support list, even for adjacent derived distros.

