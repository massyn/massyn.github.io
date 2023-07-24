---
layout: post
title: Digital Ocean is (probably not) better than AWS
author: "Phil Massyn"
categories: cloud
tags: ["aws","digitalocean"]
image: digitalocean.jpg
---

Earlier this week, while browsing through my [Twitter](https://twitter.com/massyn) feed, I saw a post where someone was saying that [Digital Ocean](https://www.digitalocean.com) was better than AWS.  Having used both of them extensively, the post caught my attention, and after reading through the comments, it became very clear to me that there was a huge misunderstanding between the two services.  Let's break it down.

_For the purposes of this post, Digital Ocean will also refer to the other VPS providers, like Linnode, Vultr, etc._

## What's the difference?

Where to begin... that's a tough one... The simplest analogy I could come up with is that AWS and Digital Ocean are like a scalpel, and a chain saw... Both can be used to cut things, one is however better at some tasks than the other.  That's typically the difference with these hosting platforms as well.

[AWS](https://aws.amazon.com) is a cloud service provider, specializing in more than just virtual machines, whereas [Digital Ocean](https://www.digitalocean.com)](https://www.digitalocean.com) is predominantly a virtual machine (VPS) provider.  A Virtual Machine is a server that runs in its own contained space, sharing the same piece of hardware.  This is a great way to leverage unused hardware by the software that needs it most.

## AWS is expensive

Sort of.  There is a difference though.  When you deal with AWS, you're dealing with a provider that been around the block a few times.  They have some of the most advanced data centers in the world, with some of the strongest security controls in their data centers.  If I need to choose where to host my data, and it's a choice of sensitive data, I would rather go with AWS.  If I'm just playing around with a virtual machine, and I just need to test some PHP app, I'd probably just spin it up on Digital Ocean.

## What about AWS Lightsail?

[AWS EC2](https://aws.amazon.com/pm/ec2/) is the flagship compute platform of AWS.  While EC2 has a great line of offerings, it is quite complicated.  When you create an EC2 instance, you have to create a security group (like a firewall), attach it to the instance, make sure you've requested a public IP address (if you want it to have internet access), and so on.  AWS recognized that the interface is a bit too complicated for the ad-hoc developer, so they developed [Lightsail](https://aws.amazon.com/lightsail/), which is still running the instances on the EC2 backend, but with a simpler interface, allowing developers to focus on their development, rather than designing complex infrastructure on AWS.

## Predictable pricing

This is where AWS EC2 is suffering a bit.  As individual developers, we want to know that our hosting fees are not going to blow out of the water.  This is where Digital Ocean is great.  The droplet will cost you $5 per month, and you won't get any surprises.  When you're hosting on AWS, while the instance charge may be around the $5p/m mark as well, the data charges are extra, so if for whatever reason your app starts to consume a lot of data, you may be charged extra.

For large enterprises, this is typically not a big problem, since the data usage charges are all grouped together.  When you have a few hundred VMs across your account, data usage would typically even out over the course of a month, and may peak over busier periods (ie Christmas sales, etc), depending on what your workload is used for.

## Redudancy

AWS makes redundant copies of the EC2 instances across multiple availability zones.  If there is a problem with an EC2 instance, they can fail it over to another AZ very quickly, in many cases, without you even knowing about it.  With Digital Ocean, that won't happen.  If there were to be a major problem in a Digital Ocean data center, your droplet will drop like a ton of bricks.

## Backups

I'm afraid you're a little bit on your own.  Both AWS and Digital Ocean offer a backup solution, but you have to turn it on yourself and pay for that extra.

Please be warned - having a backup does not guarantee you'll be able to recover a server.  Test your disaster recovery plan regularly!

## Losing data

There have been rumors that if you forget to pay your bill, Digital Ocean will simply delete your data.  I cannot confirm this point.  AWS has been known to keep the data, while the account is in a suspended state.

## Regional Availability

As of this writing, there are 29 active AWS regions.  Digital Ocean only has 8.  When you need your workload as close to your customer as possible, AWS may be able to provide you with a better offering than Digital Ocean.

AWS also has better support for storing your data in another region.

## Linux vs Windows

AWS offers both Linux and Windows, whereas Digital Ocean only has Linux images on offer.

## Additional services

With AWS, there is a ton of integration into other services.  Take IAM for example.  You can control to a very granular level who can get access to your AWS services.  You can't do that on Digital Ocean.  How about federation to your on-prem Active Directory?  Not an issue with AWS, but a big gap in Digital Ocean.

AWS also offers you the ability to control the access an EC2 instance has to the rest of the AWS infrastructure via [EC2 Instance Profiles](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_switch-role-ec2_instance-profiles.html).  Without having to worry about sharing access keys around, you can simply grant the EC2 instance access to an S3 bucket, or an RDS database.  On Digital Ocean, however, you will need to find a way to manage those keys.

Sending emails through SMTP on Digital Ocean is much easier than on AWS, which is blocked by default.  Good luck requesting AWS Support to unblock it for you.  If sending emails on AWS is your thing, you would probably have to use the [SNS](https://aws.amazon.com/sns/) service.

* On AWS, it is an additional service you have to pay for.  It is, however, a lot more stable and robust, and fully managed.
* On Digital Ocean, there is a high probability that your public IP has been blacklisted for spam by a previous owner of that IP.  You run the risk that any email you send will most likely be considered spam.

## In conclusion

I use AWS daily for a lot of production workloads, and I use Digital Ocean for some personal projects.  Both have their strengths and weaknesses, depending on what you want to use them for.  It depends on your workload, your budget, your tolerance to risk, and your ability to manage your infrastructure.  AWS does a lot of the heavy lifting for you.

Can we say that Digital Ocean is better than AWS?  No, you can't, and you also can't say that AWS is better than Digital Ocean.  

## Comparison

|**Area**|**AWS EC2**|**AWS Lightsail**|**Digital Ocean**|
|--|--|--|--|
|SLA|[99.99%](https://aws.amazon.com/compute/sla/)|[99.99%](https://aws.amazon.com/lightsail/sla-lightsail-instances-and-block-storage/)|[99.99%](https://www.digitalocean.com/community/questions/what-is-your-sla#)|
|1 CPU / 512MB / 10GB disk / 500GB traffic|$8|$5|$4|
|2 CPU / 2GB / 60GB disk / 3TB traffic|$15|$10|$18|
|Linux|Yes|Yes|Yes|
|Windows|Yes|Yes|No|
|Redundancy|Yes|No|No|