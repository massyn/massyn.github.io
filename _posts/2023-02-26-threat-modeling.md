---
layout: post
title: "Threat Modelling"
author: "Phil Massyn"
categories: security
tags: [threat modeling]
image: threat.jpg
---

Threat modeling is a process used by developers and engineers to understand the threats that exist that may exploit a weakness or vulnerability in a software application or platform.

## The Manifesto

Before we dive into some practical threat modeling ideas, I would invite you to read the [threatmodelingmanifesto.org](https://www.threatmodelingmanifesto.org/).  It's a quick easy read and sets the scene for what is important when doing threat modeling.  Read it - it is important.

## Where do we start?

A threat model is similar to a [risk assessment](https://ismsowner.com/risk-assessment.html).  The one big difference is that a risk assessment is focused on the reduction of potential business impact, whereas the threat model is focused on remediating the vulnerability that _someone_ or _something_ may exploit that can cause an impact to your system or application.

### Scope

So what are we dealing with?  Start by defining your scope.  It does not have to be overly complicated.  A simple statement that defines what you're doing, for example

    A Threat Model for the e-Commerce application hosted by Acme Corporation on the AWS cloud environment.

When defining your scope, it is a good idea to clarify if your threat model is only the application, the platform it is being hosted on, or both.  Regardless, the outcome of the scoping process should clarify exactly where you will be focusing your attention on.

### Information Flow

Many engineers will have architectural diagrams showing how the network is laid out, and how servers are placed on the network.  While architecture diagrams are valuable, they don't lend themselves well to threat modeling.  The Information Flow Diagram (or Data Flow Diagram - DFD) is a representation of how data flows through your system.

Here's an example of an information flow.  You'll notice that the information flow would in many cases resemble the process flow.  The key call out is that the information flow is tracking how information is flowing throughout your system.  Keep in mind though that how it flows through the system can be physical or logical components.  Putting it differently - while developing a piece of software, the information may flow through the application architecture on the same system through different components. How granular you go with your threat model is entirely up to you.  I would suggest that you keep it at a high level, since the boxes in the process would typically share the same process and memory space, and would therefore occupy the same authorization model.

Another call out I would also make is to indicate when the initiating connection is the _other way around_.  In many systems, the information flow would follow the network flow as well.  In my example below, the Warehouse Management system would be initiating the network call, pulling the data from the queue (indicated with the red arrow).

![information flow](/assets/img/informationflow.png)

## Identify the actors

A threat model will need actors - the people or systems that could exploit the threats.  These could include:

* State-Sponsored Adversaries (ATP)
* Opportunistic external attackers
* Malicious Insiders
* Accidental Insiders

### Employees vs Contractors

I have seen risk assessments and threat models that tend to _discriminate_ against contractors or third parties, creating a false perception that the risk with a non-employee is higher than that of an employee.  That is simply not true.  Any person is susceptible to phishing attacks or just plain human error.  A person's employment contract does not make them more or less secure.

If there is a legitimate concern in teams of policy enforcement with 3rd parties, this is more an issue with the procurement team and how they define the security clauses in contracts with 3rd parties rather than with the 3rd party employee themselves.

## Identify the weaknesses

This is a tricky one.  What can the _threat actor_ do to attack your system?  There are typically a number of things that an attacker want to achieve.  Let's have a closer look at the STRIDE model.

### STRIDE

|**Threat**|**Against**|**Description**|
|--|--|--|
|**S**poofing|Authenticity|An entity successfully identifies as another by falsifying data, to gain an illegitimate advantage|
|**T**ampering|Integrity|Sabotage|
|**R**epudiation|Non-repudiability|A statement's author cannot successfully dispute its authorship or the validity of an associated contract.|
|**I**nformation disclosure|Confidentiality|Unintentional information disclosure, data leak, information leakage and data spill|
|**D**enial of service|Availability|The perpetrator seeks to make a machine or network resource unavailable to its intended users by temporarily or indefinitely disrupting services of a host connected to a network|
|**E**levation of privilege|Authorization|The act of exploiting a bug, a design flaw, or a configuration oversight in an operating system or software application to gain elevated access to resources that are normally protected from an application or user.|

Once you've reviewed this model, you should be able to brainstorm a few ideas of what an attacker would be able to potentially do with the application that may result in one of the conditions listed in STRIDE.

## Prioritise

When you have a spreadsheet full of threats, it can be daunting to figure out what kind of an impact it would have.  Just like in a risk assessment, we can use a threat assessment matrix to determine the priority.  In this example, we use the _Ease of Exploitation_ and _Potential Impact_ as the two key criteria.

||**Difficult**|**Moderate**|**Easy**|
|--|--|--|--|
|**Disaster**|HIGH|HIGH|CRITICAL|
|**Problematic**|Low|Medium|HIGH|
|**Inconvenient**|Low|Low|Medium|

## What are we going to do about it?

Just like in a risk assessment, once you understand what your threats are, you start building a plan to reduce or remove the vulnerability.  When remediating the vulnerability, think of things like:

* A permanent fix (fixing a code or design issue that can be exploited)
* A workaround (something temporary that will remove the weakness, but may not last forever)
* Monitoring (you may not be able to fix the issue, but you can at least monitor for when a threat is using an exploit on this weakness)

## Things to look out for

### The unknown-unknown

Probably the biggest challenge is the Unknown-unknown - you don't know what you don't know.  While we try to understand what the different threat vectors are, there may be something new that no one has ever thought of.  You won't know that until the attack has occurred.  

There is no easy way to deal with it.  It will ultimately come down to creativity and brainstorming.  Reach out to colleagues or peers in other organizations who may have had similar experiences.

### Don't make assumptions

Instead of making an assumption (ie threat X is not possible because of control Y), test your ~~assumption~~ hypothesis.  Making assumptions without validation can lead you down the wrong path.

### "It could never happen"

It is important to keep an open mind.  Just because something bad hasn't happened yet, does not mean that it won't.  Encourage your team to participate and provide input into creative ways in which a potential attack could be launched.

## Example Threat Assessment

    A Threat Model for the e-Commerce application hosted by Acme Corporation on the AWS cloud environment.

    Completed by : B.Bunny
    Date Created : 2022-02-26
    Date Updated : 2023-02-27

### Information Flow Diagram

![information flow](/assets/img/informationflow.png)

### Threat Assessment

|**Component**|**Actor**|**Scenario**|**STRIDE**|**Severity**|**Mitigation**|
|--|--|--|--|--|--|
|Order API|External Adversary|An APT can perform a brute-force password attack|DE|MEDIUM|AWS Shield, AWS WAF is in place|
|Order Database|Accidental Incider|A database might be corrupted if the administrator does not perform the restores correctly|D|LOW|DRP plans are regularly tested in a non-production environment|
|Fulfillment queue|External adversary|An external adversary is able to update the order message to alter the order quantity, resulting in a loss of product sent to the wrong address|R|HIGH|Implement a hashing algorithm to sign the order with the customer public key prior to submitting it to the fulfillment queue to validate the order with the warehouse management system|

## References

* [https://www.threatmodelingmanifesto.org/](https://www.threatmodelingmanifesto.org/)
* [https://owasp.org/www-community/Threat_Modeling](https://owasp.org/www-community/Threat_Modeling)
* [https://owasp.org/www-community/Threat_Modeling_Process](https://owasp.org/www-community/Threat_Modeling_Process)
* [https://en.wikipedia.org/wiki/STRIDE_%28security%29](https://en.wikipedia.org/wiki/STRIDE_%28security%29)