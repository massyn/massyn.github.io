---
layout: post
title: Why did I get hacked?
author: "Phil Massyn"
categories: security
tags: ["security"]
image: hacker.jpg
---

It's a question I get asked frequently.  Friends and family have faced this numerous times.  "My Facebook account got hacked!  How did this happen?"

## You picked a terrible password

Yes I know - picking a good, strong password is difficult.  It is also the main reason you got hacked.  The password you picked is terrible.  It's not entirely your fault.  Every site where you create an account expects you to have a password.

![type:video](https://www.youtube.com/embed/aHaBH4LqGsI)

To make things easier on yourself, you tend to use the same password everywhere.  *Password reuse* is one major cause of breaches.  Website operators do not always store your password securely, and when their site is breached, the attackers would most often get a hold of your password, and then they'll be able to log onto another site, using your same credentials.

Another big issue I've noticed, is we're not good at setting up Two Factor Authentication (or MFA - Multi-Factor Authentication).  Most sites offer it already but leave it up to you to enable.  You may already be familiar with it - when you log onto your banking app, they would very often send you a text message on your phone with a code.  

### What can you do about it?

* Sign up for the [haveibeenpwned](https://haveibeenpwned.com/) service.  You will be notified if your account has been compromised in any major data breach.
* Use a different password for every site.
    * If you're an iPhone user, you can simply use the [Saved Passwords](https://support.apple.com/en-us/HT211146) feature on your iPhone to keep track of the different passwords.
    * You can also use any of the free Password Managers out there.  Personally, I am using [Bitwarden](https://www.bitwarden.com), and it works quite well.  If you're not used to a password manager, the idea of using one might be a bit daunting, but stick to it.
* Enable Two-Factor Authentication.
    * [Facebook](https://www.facebook.com/help/148233965247823/)
    * [Twitter](https://help.twitter.com/en/managing-your-account/two-factor-authentication)
    * [Instagram](https://help.instagram.com/566810106808145)
    * [Snapchat](https://support.snapchat.com/en-US/article/find-an-authentication-app)
    * TikTok - At time of writing, TikTok does not appear to support 2FA.
* Pick a strong password
    * Use a site like [PasswordsGenerator](https://passwordsgenerator.net/) to generate a secure password for you.  Memorise it!
    * If you're not keen on using a password manager, you could use that single password, and simply prefix it with the name of the site you're logging on, so for example, if you picked `2(GJv5h$` as your password, you could use `facebook2(GJv5h$` for your facebook account, `twitter2(GJv5h$` for twitter, etc.

## Clicking on links

I can't stress this enough - **DO NOT CLICK ON LINKS!!**  It doesn't matter who sends them to you, do not click on links!

This happened to me... A few months ago, I received a Facebook message from one of my friends.  The message read something like this...

    OMG Phil!  I can't believe I saw you in this video... https://<insert dodgy link here>

Right.  There's just so many things in that message that immediately jumped out at me.  I immediately contacted them, and it turns out they knew the account was compromised.

Another typical one I see regularly, is _Your Amazon parcel is on its way..._ with a link to some odd site.

Here's the problem.  Both legitimate companies, and attackers use the same techniques to try and convince you to click on that link.  If you're expecting that parcel from Amazon, you're more likely to click the link.  If the message is scary enough, like _A speeding fine has been issued in your name_, you are probably also going to click on the link.

If you did happen to click on the link, and it asks you to enter your username or password, DON'T!  This is an example of a phishing attack, where the attacker is able to harvest your username and password, and then log onto your account.

### What can you do about it?

* Simply, do not click on the link!
* If you think the link might be legitimate, contact the person who sent it to you (preferably on another medium).  If they texted you, call them.  Do not text them back, because the message may have been sent from a breached account.

## Lending an old phone

I received a message on Instagram from a family friend, asking for a "secure code" that will be sent to my account.  The message was a little suspicious, because this family friend very rarely messages me, and to suddenly get a message was really out of the ordinary.  I contacted the family friend, and it turns out they knew nothing about the message.  What had happen, was that they got a new iPhone, and gave the old phone to a friend without deleting all their apps.

The friend simply logged on to all sorts of sites, and eventually got the phone infected with some malware, which then started contacting all contacts on the phone.

### What can you do about it?

* Your phone is like your toothbrush - do not lend it out.
* If you have replaced your device, do a factory reset first before you give it to someone else.

## Free Resources

* [Learn Security](https://learnsecurity.amazon.com/) - Free security training from Amazon