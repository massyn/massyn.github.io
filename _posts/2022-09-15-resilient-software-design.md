---
layout: post
title: "Resilient Software Design"
author: "Phil Massyn"
categories: engineering
tags: ["software engineering"]
image: code.jpg
---

When you operate a large fleet of servers, patching your operating system and other software components is a necessary task to prevent malware and external threat actors from taking control of your system.  In a number of cases, I've heard clients use the words: "I can't patch my system because it might cause an outage."  Let's unpack this disturbing statement.

## The scenario

The client was operating a large number of EC2 instances on AWS, running a large website, with many moving parts.  The web front-end was hooked up to queueing systems, links to external API services, the works.  They recognise the need to patch their infrastructure (the vulnerability report was quite clear on the gaps!), yet the thought of executing `yum update -y` on their server fleet struck fear in the entire team.  Why?  There was previously an incident, where the team performed an upgrade on their systems, and it caused an unexpected outage on their environment, resulting in a major business disruption.

## Why did this happen?

No one knows.  Once I joined the client, this issue had already happened.  When I tried to review the PIR (Post Incident Report), it was never created. There was never a root cause analysis performed on what exactly caused the outage.  All the team could recall of the incident, were the challenges they faced when trying to recover the system, with management breathing down their necks.  It was simply attributed to the patching process, and that's all the team remembered.  The problem was no one was able to truely articulate that (for example) an upgrade of component X resulted in a disruption in process Y.

## Change Management

Any organisation operating a large IT infrastructure must adopt some sort of [ITIL](https://en.wikipedia.org/wiki/ITIL) processes.  Included in the library, is a formal framework around Change Management.  In a nutshell, Change Management is about understanding the change to be performed, planning that change, testing it, and then executing it.  It also includes steps for rollback, in the event something goes wrong.

What became obvious for me, was how the client did not have a robust change management process in place.  They simply relied on the word of the developer that everything is ok, yet never performed extensive system testing.

## Test, Test, Test!

Thing don't always work as planned, and sometimes changes happen outside of your control.  Developers might be focussing on their individual code, yet neglect to realise that changes on the operating system, or their web server software could have an impact in how their application behaves.

It is important to have a test plan in place.  For developers working on the platform, it will be trivial to build a number of test scripts, some basic programs that can be executed to test the functionality across the entire environment.  Not only will this serve as a way to quickly validate that the environment is healthy, it can also serve as a troubleshooting tool, to help the operational teams identify where a potential break might exist in the environment.

## Poor development and practices

This unfortunately happens way too often.  Developers use API calls in a way it was never designed, or using practices like accessing file system locations, or calling command line utilities from their application in a way that is not designed robustly.

Let me share a rudimentary example.  A developer may need to check if a particular user account exists on the system.  They implement a line of code, like `cat /etc/passwd | grep $USERNAME` (now regardless of the major security code injection issue this creates, stay with me on the robust design issue!).  During a system hardening process, the security team decides to reduce the permissions of the `/etc/passwd` file, thus breaking this functionality in the application.  What the developer _should have_ done, was to utilise an LDAP library, to connect to their inhouse identity server instead, and perform the lookup that way instead.

The other consideration is that the example I've given is not guaranteed to give the same output every time. A few years ago, the passwords of Linux machines were in the `/etc/passwd` file. They subsequently moved to the `/etc/shadow` file.  If the application was expecting to see a password in one file, but the OS moved it to another, that will also break functionality.  The point is this - do not rely on arbitrary operating system functionality when there is no guarantee that this functionality will even exist in future.

## Understand your dependencies

A solution is not just software running on a server.  It is a complex piece of engineering with many different moving parts and many different dependencies.  Having a properly documented architecture is crucial in the ongoing support and maintenance of your platform.

Your developer and engineering teams have to work closely together to ensure that all system dependencies are properly documented and kept up to date.  Even a single-page document, that simply shows all the components and how they link with each other will go a long way in helping to troubleshoot outages.

## "Hard-coded" dependencies

I love disaster recovery tests.  By forcing the team to go through a DRP test, taking the software they've developed, and redeploying it on a brand-new operating system will highlight many of the hardcoded dependencies that may exist in the software.

My client was committed to a particular flavour of Linux.  When asked why they are running on this old version, instead of (for example) the supported version of Amazon Linux offered directly by the vendor, they couldn't not provide an answer.

If you consider that software vendors that develop commercial software do not create software for a particular version of Linux.  They create software that is capable of executing on different platforms since they cannot control what flavour or version their customers might be running.  Just like commercial software vendors, your developer has to be mindful of architecting solutions on a particular platform.

In the same spirit, this client also used a messaging solution.  Their application was hard-coded to operate with Rabbit MQ, a well-known and established component used in many enterprises.  They wanted to simplify their architecture and migrate to the SQS solution offered by AWS.  It turned out to be a huge task since the use of Rabbit MQ was deeply integrated in how the application operated.  As a best practice, it is better to have a single library within your application that performs a function (call it a wrapper function), where you can simply state `sendMessage($body)` and have this function then perform the call to Rabbit MQ.  The advantage to this approach is when you decide to change the architecture, your developer only has to change one function, update it to point to the new platform, and the entire solution will start using the new component.  s

## Lessons learnt

* Have a robust **Root Cause Analysis** methodology in place, investigate every incident thoroughly, and learn from it.
* A formal **Change Management Process** must be implemented across the landscape, tracking every change, and ensuring proper testing and rollback plans are in place.
* Ensure that proper **Development Practices** are adopted across the development team.
* All dependencies must be clearly **documented**.

## Summary

Will these lessons learn to solve the problem?  It might, or it might not.  There is no guarantee that there won't be some odd component that only existed in production, yet was missed in pre-production.  As much as we'd like to ensure production and pre-production environments are aligned, they seldom are.  These practices will however reduce the likelihood of something bad happening.