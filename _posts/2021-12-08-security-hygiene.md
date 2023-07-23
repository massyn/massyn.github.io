---
layout: post
title:  Security Hygiene
author: "Phil Massyn"
categories: security
tags: ["security"]
#image: php.jpg
---

Security hygiene is the practice of maintaining a computer system, by ensuring the basic controls are executed on a regular basis.  It is, at its core, a precautionary practice, sometimes may be seen as mundane, yet still critical to the safe operation of your IT system.

## So what is security hygiene?
Any computer system has some sort of infrastructure that enables it to operate, be it servers, databases, or network equipment.  For our discussion around security hygiene, we'll exclude the architecture of the solution for the moment.  A proper architecture is key to a secure system, but that will be a separate discussion.

When we talk about security hygiene, we refer to the set of controls that, if left unattended, tend to degrade over some time.  One example might be your anti-malware signatures.  If you were to update your signatures right now, your system should be a lot more secure against malware attacks.  If you fail to update the signatures from that point onward, the longer you want, the more likely your system becomes vulnerable to a malware attack.  The solution is to ensure the malware signatures are updated frequently.

## Hygiene Matrix

I've put together a key list of risks and controls, with potential mitigation strategies that should help you in identifying where you may have gaps in your environment.  This is not an exhaustive list.  For that, I would recommend that you refer to Annex A of ISO27001, or refer to one of the many [NIST frameworks](https://csrc.nist.gov/projects/risk-management/sp800-53-controls) available.

|**Domain**|**Risk**|**Control**|
|--|--|--|
|**IDENTITY**|Leaked Credential (username and password)|[User deprovisioning](#user-deprovisioning)|
||Fraudulent activity|[Revoke access](#revoke-access)|
|**DATA PROTECTION**|Data loss|[Backups](#backups)|
|||[Disaster Recovery](#disaster-recovery)|
|**NETWORK**|Unauthorized Access|[Firewall rule management](#firewall-rule-management)|
|||[Network Encryption](#network-encryption)|
|**MALWARE**|Malware infection|[Update malware signatures](#update-malware-signatures)|
|||[Run malware scans](#run-malware-scans)|
|**VULNERABILITY**|System vulnerabilities|[Patching](#patching)|

## Identity

### User deprovisioning
When users are no longer required on your system, you need to delete them.  Any user account that goes into a dormant state has the risk of being exploited, either by the person that had the access, or by someone else who is exploiting what might potentially be a weak password.

Consider that for a moment - a former employee may have left your organization could still have access to your system.  Depending on what your system is doing, you may not want anyone not within your organization to still have access to your system.

* At regular intervals, check all user accounts, and confirm that they are still required.

### Revoke access
How much access do users have?  Do they have access to sensitive data, or have the ability to cause a lot of damange?  If so, you may need to review the access allocated to each of your users.

* At regular intervals, review the access assigned to each of the user accounts.  Do not forget that you need to review your system accounts as well.

## Data Protection

### Backups

Sometime things go wrong.  Hardware failures, human error, natural disasters, all things that can result in an outage of your solution.  When this happens, you need to be able to get your system back up and running as quickly as possible.

* At regular intervals, perform a backup of your system, and store the backups in a safe location, typically in an offsite, or cloud storage location.
* At regular intervals, check that your backups are in fact running.

### Disaster recovery

A backup is one key requirement, but can you actually restore from that backup? A disaster recovery plan helps to ensure that you know what to do in the event of a disaster, how to access your backups, and how to get the system up and running with the least of effort.

* At regular intervals, perform a diaster recovery test to ensure you can restore your system to full working condition.

Don't forget that the disaster recovery plan should be available.  Should your server crash, or you loose a database, you don't want to spend your time trying to remember where you saved your disaster recovery document.

## Network

### Firewall rule management

Firewalls, security groups, network ACLs - they perform similar functions, by restricting network access.  While this control does not strictly sit in the space of security hygiene, the ongoing management of your network access rules do.  When your firewall rules are not properly managed, or when the change management process is not strictly followed, you risk exposing your environment to unauthorised entities.

* At regular intervals, perform a network scan to identity any exposed ports on the network. 

### Network Encryption

Having data traffic encrypted is a good practice to ensure confidentiality is not compromised.  Setting up SSL/TLS is a design issue, however maintaining the certificate, and ensuring the ciphers are still secure, is not.

* At regular intervals, check the TLS/SSL certificate to ensure that it is still valid, and if it comes up for renewal, ensure it is renewed prior to expiry.
* At regular intervals, use a tool like [SSL Labs](https://www.ssllabs.com/ssltest/) to test if your SSL/TLS configuration has any weaknesses that need to be remediated.

## Malware

### Update Malware Signatures

Having an anti-virus / anti-malware solution is one thing, making sure that the signatures are up to date will reduce the liklihood of malware causing an outage on your system.  If your software allows it, enable automatic signature updates.  You should also be alerted (email, Slack, etc) when malware has been detected.

* At regular intervals, check that the signatures are being updated.

### Run Malware Scans

Your anti-malware solution should be configured for real-time scanning.  If this not an option, setup a scan to happen regularly.

* At regulaer intervals, run a malware scan on your system.

## Vulnerability

### Patching

No software is ever perfect.  Regardless of how good a developer is, and how much testing is done, chances are there's an issue hidden in the code, and it is only a matter of time until someone finds the vulnerability, and exploits it.  Software vendors are frequently providing updates to their software, and in many cases, the updates do address security vulnerabilities that may exist within that software.

* Enable automatic updates (if possible).  

Automated updates may not be suitable, as it could cause unplanned outages, or, without proper testing, could cause unintended issues with your solution.

* Develop a testing plan, then at regular intervals, test the patches prior to deploying it to production.

## Conclusion
The list of controls in this post is not conclusive.  There may be more required, depending on your particular solution.

In a modern environment, you would most probably implement an ISMS based on ISO27001.  I would recommend that you check out [ISMS Owner](https://www.ismsowner.com) if you want to learn more about what an Information Security Management System is.
