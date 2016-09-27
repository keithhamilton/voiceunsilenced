# voiceunsilenced
A Twitter bot that listens for your tweets, calls someone, and reads your tweets
to that person.

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)


##License
This codebase is freely available to the public for **non-commercial** uses under a
modified version of The Unlicense found [here](https://github.com/keithhamilton/voiceunsilenced/blob/master/LICENSE).

## What is it?
VoiceUnsilenced is a tool for political expression that leverages Twitter in
combination with automated telephony to take what people tweet, and translate it
into phone calls to people who need to hear what is being said.

##Why?
I created VoiceUnsilenced because the United States of America has a problem.

We prefer to ignore, rationalize, or support the killing of innocent black men
and women rather than to address the issue for what it is: a systemically racist
society that targets people of color then kills them.

Then, in the wake of these killings, we are encouraged to contact our
representatives in the wake of tragedy using technology that doesn't make sense
to us in the current age.

We use social media and texting to communicate, so asking people to look up, then
call a representative is akin to handing them a pen and paper, along with a
phone and asking them to choose which is more convenient.

VoiceUnsilenced gives people a voice and a simple way to contact Congressional
representatives in the locations of violence against citizens. But that tool, in
the hands of a few, doesn't truly empower everyone else.

As an open-source tool, it is yours to use to contact whomever you want, really.
Maybe you'll start a similar campaign. Maybe you'll use it to bolster supporters
of your cause. Maybe you'll use it to contact The President's office.

It's completely up to you, but however you choose to use it, all you have to do
is set up a phone number, a Twitter app, and click "Deploy."

##How Do I Use It?
It's easy to deploy your own VoiceUnsilenced bot. Let's break it down.

###1. Check Prerequisites
You will need a [Twitter dev account](https://dev.twitter.com) and an active
[Twilio account](https://twillio.com). Both are free to create, although you
will need to charge up your Twilio account to actually use the bot. Calls are
$0.015 each.

You will need to create a read/write Twitter app. You can do this in the Twitter Dev site,
but instructions for this are out of the scope of this README.

Finally, you will need a [Heroku account](https://heroku.com). Heroku is a very
simple service that allows people to host web applications cheaply.

###2. Deploy this to Heroku

#####A note on cost
The `master` branch of this program will deploy VoiceUnsilenced on Heroku's
Hobby plan, which will cost about $20/month. This default was chosen so the bot
would never go to sleep. If you would like to deploy this on Heroku's Free tier,
switch to the [free-heroku](https://github.com/keithhamilton/voiceunsilenced/tree/free-heroku) branch and follow the deploy instructions there.

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)


###3. Update the configuration values
Once you are in the Heroku web interface, you'll be asked to fill out all of the
config values for the VoiceUnsilenced app. Where possible, suitable defaults
have been set, and with others descriptions are available to help you know what
you'll need there.

After you have all of the values in, click the big "Deploy for Free" button at
the bottom of the page, and your app will fire up in Heroku.

All you have to do then is start tweeting at it.

##Contributing to VoiceUnsilenced
This software is provided under The Unlicense, so you are free to do whatever
you want to a fork of this code, without attribution or limitation. That being
said, if you'd like to contribute to the core repository, or have issues with
it, I just ask you observe the following.

###Contributions
Before making a contribution, be sure to:

1. Fork the repo into your own account.
2. Make the changes.
3. Open a pull request against the master branch, providing some insight into
   the changes (why, what, etc).

I will accept any updates that make sense to me with respect to the original
intent of this project. If I don't accept the cnages, again, you are free to
republish this in any form, so no big deal there.

###Issues
If you have an issue with the program, please file an issue in this repo unless
the issue is with Twitter, Twilio, or Heroku. I will close your issue without
resolution if it is not an actual issue with this codebase.


##FAQ
####I'm not a developer...is this something I can use too?
I think so. You'll have to get over a few small learning curves to get this out
in the open (like, say, learning what Heroku is or creating a Twitter app), but
a terse Google search should surface enough information to get going. You can
always hit me up on Twitter with questions, and I'll do my best to answer.

#####Does this have to be used for contacting Congresspeople?
Not at all. That's just the intent of the VoiceUnsilenced bot. Although they're
names `CONGRESS_NAMES` and `CONGRESS_NUMBERS`, these configuration values can be
for anyone, and any number of anyones at that.

All you need to ensure is that the numbers and names are comma-separated (i.e.,
Joe,Jane,Sam,Fred) and that the order is the same, so the first name corresponds
to the first number, and so on.

#####What about the "from" numbers and names (from Twilio)?
You can have as many from names and numbers as possible. Again, for
VoiceUnsilenced, the intent is to only contact Congress on behalf of one
indiviual, but the bot can support many.

There is an assumption in the code that you will either have one or many, so if
you have many, make sure you treat the names/numbers in the same manner as with
the contact names/numbers (as described above).

#####What is Twilio, anyway?
Twilio is a service that affords developers access to all kinds of
telecommunication media. Examples are telephony (as used with this bot), text
messaging, MMS, and more. If you want to learn more about it, hop over to the
[Twilio](https://twilio.com) site. 

#####How much does it cost to run this bot?
That depends on a few things:

1. **Heroku.** The way this is set up, your bot will be deployed under a Hobby setup
   plan in Heroku. Because of the drawbacks of a Free setup, namely that it will
   go to sleep during long periods of inactivity, we've used Hobby as the
   default, which will cost about $20 a month.
   
   If you would like to deploy VoiceUnsilenced on Heroku's free plan, you can
   switch to the
   [free-heroku](https://github.com/keithhamilton/voiceunsilenced/tree/free-heroku)
   branch, and follow the deploy instructions there.

2. **Twilio.** Twilio isn't free, unless you are just doing testing, which you
   won't be with this bot. Calls are $0.015 each, which isn't bad, really. For
   just $15 you can generate 1,000 calls with this bot. If you think you might
   get 1,000,000 calls, you will need to plan for a bigger budget.
   
#####I have other questions. How can I contact you?
You can tweet at me or shoot an email...it's in my profile.
