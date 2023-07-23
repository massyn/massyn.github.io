---
layout: post
title: "Optus breach of 2022"
author: "Phil Massyn"
categories: security
tags: [breach]
image: optus.png
---

[Optus](https://www.optus.com.au), one of the largest telcos in Australia has suffered a major security breach, losing the sensitive information of close to 10 million Australians.  A lot has been said already on the topic.  I wanted to focus on the psychology behind a breach.

## What we know so far

Like with most breaches, the actual mechanism used by the attacker will most likely never be revealed.  While unconfirmed at this stage, it would seem that the attacker leveraged an [unauthenticated API](https://twitter.com/Jeremy_Kirk/status/1573652986437726208) to scrape the data.

### Huh ??

An API (Application Programming Interface) is typically a web server of some sort used by large companies to share data between different systems.  In this case, you had something like a database with all the customer data accessible by various other systems.  These APIs are typically used from system-to-system.  When one system needs data from another, say for example the billing system needs to lookup the user's address to send them their monthly statement, it would call this API, retrieve the data, and process the bill.

When these API calls are made, just like you would enter a username and password on a website, the system also has to authenticate to the API.  Sometimes we use what is called a __bearer token__, in other cases, the API has to also provide a username and password.  What happened with Optus, was this API had no authentication at all.  Anyone could simply query the API, and retrieve the data without even providing any sort of authentication information.

## This was NOT a cyber attack

On September 22nd, 2022, [Optus announced](https://www.optus.com.au/about/media-centre/media-releases/2022/09/optus-notifies-customers-of-cyberattack) ([local copy](2022-09-26-optus-notifies-customers-of-cyberattack.md)) in the media that they suffered a data breach, and that they were the victim of a cyber attack.  I disagree with this statement.

A cyber attack is typically targeted and methodical, using various techniques to find a weakness in a system, and then exploiting it.  In this scenario, while the attacker did perform some of those activities, the main root cause is **Optus left the door open**.  This was straight-up negligence by Optus that resulted in the data being breached.  [Clare O'Neil agrees](https://twitter.com/ClareONeilMP/status/1574361824102711296) with this statement.

## The psychology at play

An Optus employee or contractor made a mistake.  One person was responsible for this breach.  We will never know the identity of the person.  Somewhere out there, is a person who has a huge amount of guilt of what they have done, may (or may not) be employed by Optus anymore, and may even face formal sanctions from Optus for their role in this breach.

Why did they do it?  Why did this developer leave an unauthenticated API wide open to be consumed by anyone?  Let me offer a few possible scenarios (in no particular order of preference).

### Management pressure

I have been in meetings where directors were threating to fire an IT team if they did not implement a particular solution at a particular time, regardless of the security and compliance risks that may exist.  If a developer is forced to implement a solution to meet some manager's objectives, without full consideration of the impact, it is possible that untested changes can make its way into production.  So while the employee may not have intended to leave the API open, the pressure of deploying an untested system may have resulted in an oversight.

### Negligence / Ignorance?

It is possible that the developer simply didn't know what they were doing.  It was [reported](https://www.protocol.com/bulletins/optus-data-breach-api-security) that a Google API may have been the culprit.  Is it possible the developer simply did not know how to configure it, and made a mistake?

### Governance

Large organizations tend to have very robust governance processes, that control everything from what software to buy, down to the exact task to be executed to enable a configuration change on a system.  I have been in situations where IT teams were quick to descope a particular piece of software, with a somewhat relevant justification (or excuse), only to lull themselves into a false sense of accomplishment that a particular process should not apply to them.

Is it possible the developer simply wanted to make a good impression, and meet their own targets, thinking that since it is a development API, the governance processes did not apply to them?

### Too much going on

Software engineering is complex.  When we consider the sheer scale of an operation like Optus, there is a lot of moving parts, lots of systems all talking to each other, sharing and exchanging data, and it is impossible for one individual to be across the entire architecture.

### Obscurity

I've met IT technicians who believe just because someone doesn't know a particular interface exists, they are safe from attack.  Developers would sometimes create dummy websites, typically as a subdomain of their main website to run tests and perform validations of new functionality before the site goes live.  The problem however, when we're talking about a data breach, an attacker will not discriminate between a production system, and a development system.  All systems are equal targets when they're connected to the internet.

Do not assume just because you're on a development environment that you are immune from attack.  That is a mistake.

### Testing with production data

When developing systems, developers should not be working with production data.  What we don't know, is if this change was part of development, or a deployment into production.  Assuming it is in development, the question should be asked by the developer had access to production data.

While not a fault of the developer, Optus may have messed up.  They did not adhere to **ISO27001 A.12.1.4** : _Separation of development, testing and operational environments_.

## Lessons Learnt

* Governance processes should exist to protect the organization, and the people operating their procedures.
* Where a business need is more important than a security risk, the risk acceptance process should be covered through the governance process.
* Separation of development and production environments is crucial.
* Developers should not have access to production environments.

## Final words

While we're still trying to figure out what this breach will mean for us, if we need to replace passports and drivers licenses, I hope that Optus will come forth with a formal root cause analysis, and share their findings on what caused this breach, and how an unauthenticated API came to exist.  As an industry, we need to learn from these breaches, and rather than creating more regulation to babysit companies, we should instead work on strategies around data retention (delete the old data when no longer required), and only storing data that is absolutely necessary for the basic operation of the site.

As this is an evolving story, I'm sure we'll hear more about it in the weeks to come.

