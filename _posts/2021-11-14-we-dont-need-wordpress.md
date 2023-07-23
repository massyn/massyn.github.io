---
layout: post
title: We don't need Wordpress
author: "Phil Massyn"
categories: security
tags: ["security"]
image: wordpress.png
---

## Introduction
[Wordpress](https://wordpress.com) has been the defacto blogging and content management system for many websites.  It is [claimed](https://techjury.net/blog/percentage-of-wordpress-websites/#gref) to be running on around 455 million websites globally, well over 30% of all websites globally.  Wordpress is a big deal. There's a huge amount of [plugins](https://en-au.wordpress.org/plugins/) available that can turn the site into anything imaginable.

My own website has also been operating with Wordpress for quite a while, until recently when I decided to pull the plug on Wordpress.

## First some history

Many years ago, when [massyn.net](https://www.massyn.net) first came into being, I recall I had the whole thing running as a [Perl](https://www.perl.org/) script, with no database backend.  It was rough -- local text files, no real standards, other than just a script trying to render some HTML.  Back then (I'm talking mid 2000s), the server was running off an old desktop.

![Old setup](2004-computer-setup.png)
Yes - I had a convoluted setup on some old hardware!.  I had port 80 (http) opened on my ADSL router, with [DynDNS](https://account.dyn.com/) setup to automatically update the server's FQDN name whenever the IP changed.  Security was not at the top of mind with this setup.

## Challenges

Having these machines running all the time was a problem.  The first problem was the noise.  The second was the power bill.  Electricity in Australia isn't cheap.  At one stage I calculatd my power bill alone for these machines was around $100AUD per month.  I also had to back things up.  The one machine had a hard drive failure, and I lost some data, and backing up data to a portable drive every few weeks just wasn't the most glamarous of activities.

## The history

Ah, [netcraft](https://sitereport.netcraft.com/?url=www.massyn.net) - you are awesome!  According to their stats...

* 2004 - massyn.net was first discovered running Linux, hosted through my ISP iiNet.
* 2005 - I'm not sure what I was thinking hosting on Windows.. But.. apparantly that happened.
* 2006 - Hosted with GoDaddy -- it was much cheaper hosting the site there instead of running the servers myself
* 2007 - I suspect around this time I started using Wordpress.
* 2017 - Moved the hosting to Digital Ocean -- I do recall it started before that.
* 2020 - Since I am now an AWS Security specialist, I decided to move the server to AWS.
* 2021 - Yeah, that's not going to work -- let's just use the free wordpress hosted site instead.
* 2021 - And now we are here - away from Wordpress.

## So Wordpress or not - what's the deal?

Wordpress is a PHP application that requires a web server capable of serving PHP files, as well as a mySQL database.  Depending on the load, the modules you load, the amount of content you have, your server will get very busy, very quickly.  Since I am also a security specialist, I want to ensure my site is secure.  I have faced some defaced websites through Wordpress before (and yes, massyn.net did get defaced at some point).  I learnt that while Wordpress is relatively secure, the challenge is with the plugins.  Plugins are not scrutinised to the same level as the core Wordpress product.  If you install a plugin, you are essentially allowing the author of that plugin to do whatever they thought was a good idea at the time to your Wordpress installation.  This is in many cases a necessary evil.. Wordpress out of the box is relatively basic, and can't do much, so you need to load the plugins and themes to extend it's functionality.

Under the hood, every time someone access your website, Wordpress would execute PHP code, connect to your mySQL database, read the content, render the HTML, and pass it back to the requester.  This is fairly standard.  One issue is that you now have multiple points of failure. Anyone of these steps can fail, causing the site to be rendered non-responsive.

Then maintenance kicks in.  A new version of Wordpress is available, or an update to a plugin or a theme, and you have to go through the process of updating it (and pray you don't break anything in the process.. And yes - this has happened to me!)

Wordpress has it's place.  It is a very flexibile and powerful tool.  When I reviewed my hosting requirements, I realized that having a dedicated virtual machine at [AWS](https://aws.amazon.com) was a bit of an overkill.  It came down to understanding my requirements - I just need a very basic web presence as a platform to share ideas and opinions.

## So what's the plan?

While talking to a friend in Japan, we were discussing the security implications of using AWS S3's [static web hosting](https://docs.aws.amazon.com/AmazonS3/latest/userguide/WebsiteHosting.html) feature for some of his company's websites.  It never occurred to me that I could simply host my website just as an S3 site - I don't need a huge infrastructure of databases and web servers just to get my content out - I can use a Static Site Generator.

I looked at a few options, and decided to settle on [MkDocs](https://www.mkdocs.org).  It took me about an hour just to get it running.  Within a day, I had reworked [AWSSecurity.info](https://www.awssecurity.info) complete into markdown language and migrated into mkdocs.

I went on to setup an S3 bucket in AWS, uploaded the content into S3, configured a [CloudFront CDN](https://aws.amazon.com/cloudfront/) in front of S3, with full SSL enabled.

## How it's going?

So far so good (I guess!).  All the content is maintained in a private github repository, and I have a script I simply run that will generate the site from markdown language into HTML, and then using the AWS CLI to upload the content into the S3 bucket.  It is a fairly seamless exercise.  There has been a couple of minor issues that I had to deal with.  In no particular order...

* The theme I chose in mkdocs had some bugs, and did not render.  I had to choose a different theme
* CloudFront did not (by default) look for index.html in any folder generated by mkdocs.  I had to use the ```--no-directory-urls``` parameter to force mkdocs to generate individual files.
* I have no idea how many visits my site is getting (yet).  I will see the bill at the end of the month when AWS will charge me for the actual volume consumed.  Watch this space for more detail.
   * There are options of using Google Analytics.  I have not explored that yet.

## Final words

There are various options available to content developers today.  Getting a presence on the internet these days should not be a difficult exercise.  I am quite happy with my setup, since I now have a fully managed web hosting environment, with very little moving parts, and with an unlikely risk of compromise or defacement.  And backups?  Since the core content is in my github repo, I can easly rebuild the site if I need to.

Continue using Wordpress.  If however you want to reduce your hosting bill, then moving to an S3 hosted website with a static site generator might be the way to go.

