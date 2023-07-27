---
layout: post
title: Security in a Development environment
author: "Phil Massyn"
categories: security
tags: ["secops","security"]
image: securityvsdev.jpg
---

As a security professional, you would most often be dealing with teams that are directly responsible for the security of a system.  In many cases, developers will have the ability to make or break the security of their particular solutions, and in many situations, too much frustration for the security team.  I have observed firsthand how adversarial the relationship between security and developers can be.  It doesn't have to be that way.

    For this post, the word "developer" can be interchanged with System Engineer or Solution Architect.  

## Roles and Responsibilities

Let's take a step back, and consider the responsibilities of the teams.  The security team (in most cases) is tasked with protecting the company's information assets.  They do this by performing risk assessments, creating policies and procedures, and then enforcing these policies through tooling and reporting.

The development team is tasked with developing software or solutions, helping their business and customers to succeed, and ultimately making money.

## What went wrong?

On the one extreme side of the spectrum, we have a security team that is the team of "No".  Whenever any developer wants to do something, the default answer from the security team is always no.  This non-business engaging attitude is creating a culture where developers simply won't engage with Security anymore, go "rogue" and do their own thing.

On the other side of the spectrum, you have a development team that has absolutely no regard for security, and simply does whatever they need to deliver on their projects, and security is an afterthought in their delivery.

## What are the problems?

### Security is our number 1 priority

I've seen companies claim security is their first priority, yet that sentiment is usually quite far removed from reality.  While security is important, in many cases, meeting a project on time and within budget is more important than security.  Maybe Security should be priority 2.

### Security is not part of the Development

This is almost too obvious to say, but I'll say it anyway.  Any development team that does not work side-by-side with their security colleagues is bound to fail.  There's a bit of an agile mindset that comes in, ensuring that security requirements are built into the solution from the start will avoid delays and issues later down the track.  It is simply cheaper to implement security controls right from the start than trying to implement them after the solution has already shipped.

### Treating Security as a quality gate

There are compliance processes that state a solution cannot go live without Security approval.  Nothing wrong with that.  The problem however, as stated previously, is if Security is not part of the development process, then the quality gate becomes a hindrance.  

When this happens, Security is now the bottleneck that stands in the way of project delivery.

## Solving the issue

### Why are we here?

It is important to recognize the roles we all play in the company.  Developers and Security alike must deliver and protect the company investments.  Developers need to recognize the importance of Security, and Security needs to recognize the importance of having developers create innovative solutions to be used by the company to help pay our salaries.

### Tooling over process

Developers do not want the security team looming over their shoulders every second of the day while they are developing, and I don't blame them.  They also do not want to sit through numerous approval and governance meetings to justify and explain why they developed a particular solution in a particular way.

Tools can be put in place to ensure certain development standards are being adhered to.  Most modern development environments will have some form of [CI/CD](https://www.redhat.com/en/topics/devops/what-is-ci-cd) pipeline, and integrating security tooling into the pipeline is a sure way to ensure quality solutions are being delivered, without slowing down the developers.

### Education over Discipline

No one wants to be confronted about developing bad code.  A better approach would be to educate teams on correct development practices, showing examples of secure code, and how to use secure development patterns.  The introduction of a CI/CD pipeline that enforces secure code quality can be used as a training tool, to ensure development teams understand the code quality that is to be expected before code is deployed to production.

### Collaboration over governance

Having a non-adversarial attitude towards development security is more constructive than dealing with issues on an ongoing basis.  I like the idea of an "open door" policy, where developers dare to ask questions and raise security concerns without fear of retribution.  It is when we have an open and collaborative culture toward security that development teams will feel comfortable in raising their concerns without the need to become defensive.  When we have an inclusive culture of both security and developers working together towards a common goal of serving the company that pays their salary, only then will you have quality software and solutions delivered.
