---
layout: post
title:  The us-east-1 outage of 2021
author: "Phil Massyn"
categories: cloud
tags: ["aws"]
#image: php.jpg
---

December 7th 2021 saw an outage in the **us-east-1** region of AWS.  The outage had a significant impact, not just on AWS, but for many customers all around the world.

## What happened?

From reading the [summary](https://aws.amazon.com/message/12721/) provided by AWS, it would seem that a software issue caused an autoscaling event on their backend services, that resulted in a massive network traffic surge, to the point where the backend network was severely congested, blocking access to AWS' internal log monitoring systems, which also hampered AWS' ability to do their own triage and remediation activities.

What added to the frustration for customers, is the [AWS status dashboard](https://status.aws.amazon.com/) was also not being updated, giving a sense that _everything is fine_, when in fact, AWS was having a really bad day.  This was also attributed to the internal backend network being congested.

The incident also highlighted the high level of dependency we have on the **us-east-1** region.  Some key services, like [IAM](https://aws.amazon.com/iam/), only run from this region, so an outage to this region would cause a huge disruption for all AWS customers world-wide.  I would imagine that some authentication services would be distributed across all regions, however any changes to policies would occur in us-east-1 first before they are replicated worldwide.  So even when your solution runs out of another region, you may experience some disruption when this region is impacted.

## Let's move away from AWS!!

So your business may have suffered some sort of an impact as a result of this issue.  I'm sure there will be some executive somewhere that will use this event as an excuse to move to another vendor.  Some CIOs may even go as far as deciding the risk is too great, and they want to move their systems back to their own data centers.  As a business owner, it is your prerogative  to make that decision, but you'd be wrong.

## Emotionally-fuelled risk assessment

The worst thing your organization can do is to make a business decision fuelled by emotions.  Sure, the AWS outage may have been a major issue for you, it may have resulted in lost revenue, lost data, business disruption (or any other impact that may have happened).  Tempers may have been flaring, executives shouting at the IT department for not living up to their SLAs, I'm sure you know the drill.  To make a decision to move to another platform, on the off chance of a single outage, is not going to solve the problem.

Let's put this in perspective.  What happened with AWS this week had a one-in-a-million shot of occurring.  Every piece of software has bugs.  It doesn't matter how well you test, something will go wrong, and in this case, it happened to AWS.  Even if you moved your workload to another platform, that vendor may also face similar issues (did you forget about the number of vulnerabilities discovered in Azure in the last few months?).

**Let's move it back onPrem!** - ok, so now we have to invest _a lot of money_ to build our on prem environment, make sure the UPS, fire suppression, air conditioning, backups, physical security, cabling, and all the other pieces of infrastructure is in place, and managed.  I don't have to tell you what an expensive, and time-consuming task that would be.

In a previous role, I was the systems engineer, responsible for maintaining the computer room located on the 1st floor of the building.  One night, there was a massive storm that ripped through the city, and the computer room flooded (on the first floor of the building!).  It happened due to a drainpipe that was installed in the computer room floor, designed to drain water out of the computer room that got clogged.  When the rain came, it pushed water out from the drain, and flooded the computer room.  The lesson learnt that day, was that just because something seems unlikely (like a flood happening on the first floor), doesn't mean it couldn't happen.

## So now what?

AWS is the largest cloud provider in the world.  They take these outages very seriously.  Even when you host your own data center, the chances of an outage in your own computer room is much higher than an outage with AWS.  These guys know what they're doing.  They've been doing it for many years, they have experts and specialists that manage the backend environment much better than what we'd be doing in our data centers.  They also have the advantage to scale.  With a few key engineers, they can build a world-class data center, and simply give you the advantage to use their skill and expertise.

* **Give AWS a chance to figure this out.**  There will be more lessons learnt from this outage.  Fixes will be built, tested, and implemented.  This outage, like the few before it, will not go in vain.
* **Consider your own risk position.**  If a single region outage is causing a significant outage, you may need to reconsider the architecture of your solution, and build more redundancy and resilience into your environment.  I am not a fan of a _multi-cloud strategy_ as additional cloud environments do introduce additional complexity that you need to manage.  Depending on your risk appetite, you could look into using an additional vendor as a DRP environment.  This works ok when you're only dealing with _universally common objects_, like virtual machines.  An EC2 instance can be moved (relatively easily) from AWS to Azure.  Something like Lambda functions and DynamoDB tables, not so much.
* **Design a fully redundant system.** - The [Well Architected Framework](https://aws.amazon.com/architecture/well-architected/) is a must-have for any AWS Solutions Architect designing a solution.  Review your architecture, and plan for proper redundancy that fits within your business requirements and budget.




