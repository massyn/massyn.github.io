---
layout: post
title: Password policies
author: "Phil Massyn"
categories: security
tags: ["security"]
# image: php.jpg
---

Almost every company on the face of the planet have them... Password policies.  They describe how long and complex they need to be, how often you need to change them, much to the dismay of of your users.  Let's talk about passwords.  In this article we will only cover the authentication side of the security model.

## Something you know

A password is _something you know_, and hopefully something **only you** know.  It allows you get into a system, by authenticating you to the system.  In layman's terms, you prove to the system that you are who you claim you are, by providing something only you know, like a password.

## So what is a password policy?

A password policy is a document that describes how a password is supposed to be managed.  Your organization will most likely have one, with rules like :

* The password must be at least 10 characters long.
* The password must contain at least 1 upper case, 1 numeric, and 1 special character
* The password must be changed every 90 days

Your organization could go even further, requiring that you don't write it down, not share it with anyone, and most importantly, **keep it secret**.

## So what could go wrong?

### Forgetting the password

Users are terrible at remembering their passwords.  On top of that you force them to change the password every so often, they can't keep up.  Of course they're going to forget them.  Unless your service desk is equipped to deal with the influx of calls after a nice long holiday, or you have a password reset feature available at your organization (another tool I'm not a fan of), you'll have a tough time ensuring your users can log on all the time.

### Picking good passwords

Users cannot pick good passwords.  A good password should be easy to remember, but difficult to guess -- easier said than done!  Get that password reminder pop up, and you try to put it off for so long, and before you know it, you use the same password, and just increment the number at the end.  [Michael McIntyre](https://www.youtube.com/watch?v=aHaBH4LqGsI) really explained this one better than I could.

### Something embarrassing

That's a really good idea!  Use something really embarrassing as your password - no one will ever know, unless the passwords get leaked, then everyone will know your secret as well.  So no - don't use anything embarrassing as part of your password - that's a bad idea.

### Not storing passwords securely

This is not on the user, but more on the site operator.  Passwords must be securely stored.  The best way is to use something like a salted hash (PBKDF2).  Do not ever store the password in clear text.  If your tool uses MD5, don't.  It is also badly broken.  The point is - you have to assume that should your database be breached, that the attacker will not be able to use the hashed password to reverse engineer the password, and then be able to log onto another system.

### Password reuse

Don't use the same password everywhere.  Use a different password on every site... Easier said than done!  You try and remember all those passwords.  It is a nightmare!  So users tend to go for the easiest option, and use the same password everywhere.  Why is this bad?  If one site is breached, and the password is easily cracked, the attacker will be able to use your credentials on another site.  Just ask [Dropbox](https://www.theguardian.com/technology/2016/aug/31/dropbox-hack-passwords-68m-data-breach) how that worked out for them.

### Use a password manager

Yeah, this is fine.  I use [LastPass](https://www.lastpass.com).  The free version is probably ok for most people.  You then get into the thing of using different passwords on every site - the longer, and more complex, the better.  The problem I faced, is that it doesn't work on my phone - try to enter a 20 character passwords where 0 and O look the same -- you always get it wrong, unless you have the paid version, then you can use the LastPass app on your phone.

Don't get me wrong.  I use LastPass, and it is great.  My problem however is that the barrier-to-entry is very high.  When I try to preach to my friends and family on the use of a password manager, their eyes glaze over.  It's not easy for them.  They see it as a _geeky thing_ that only the tech-savvy use.  We still have a bit of work to do in this space to make it easier to use.

## Solution time

Enough talk about everything that can go wrong -- what can we do about it?  How can we make things a bit easier for our customers and employees?

### Get rid of password policies

Well, sort of.  Instead of getting rid of the policy, how about if we made it simpler, as in much simpler.  Keep your audience in mind.  They don't want to think about a new password every 90 days.  We usually define a password change frequency for a number of reasons, the biggest is that someone (or something) can guess the password, and with enough time, a password can be brute-forced.

**TIP** : Do a threat assessment against your password policy.  Consider what could really go wrong (unauthorized access), and then think critically about what controls you can put in place that do not punish your users who want to do the right thing.

### Use centralized authentication

This is less of an issue in large enterprises where you may have something like Active Directory that controls your access.  For an individual, if you can log on via Facebook, Google, or Apple, do it!  It is one less password you have to worry about, and these large vendors become your authentication provider.

### Account lockout

If you really consider your threat landscape, someone trying to break in by guessing the password is not a good idea.  Consider putting account lockout in place, but be mindful that you don't create an opportunity to cause a denial-of-service situation, where the attacker could try to logon with your CEO's account, just to annoy them by not being able to access their email when they really need to.

### Impossible login

So you logged on from Sydney, and two minutes later there is another logon from London.  That's not possible. Your system should be able to prevent logins like that.

### Multi-factor authentication

Why not require MFA on all logins?  Again we need to consider the barrier-to-entry, and how difficult it would be use.  Some systems require MFA on every logon, others will remember the browser you logged on from, and would supress the MFA login prompt, assuming you did not change browser since the last logon, or you did not change location since your last logon.

### Check HIBP

[Have you been Pwned](https://haveibeenpwned.com/)?  The site operated by [Troy Hunt](https://www.troyhunt.com) offers an [API](https://haveibeenpwned.com/API/v3) that allows you to check if the password chosen has been breached.  So whenever a password is changed, check the password against the HIBP database, to see if it is a breached password.  Basically - do not allow any passwords that have been breached.  This will also include the very basic passwords.

### Only change the password when compromized

If for whatever reason the password is leaked, only then should it be changed.  This may be a good incentive for your users to understand to keep their passwords secure, because if they don't, they'll be forced to change it.

### User education

Train, train, train!  I've seen so many cases where accounts get compromized because the user thought they were entering their credentials on a legitimate website, when in fact they have been phished.  Even the strictest security policy will not stop your user from being scammed into providing their credentials to an attacker.


