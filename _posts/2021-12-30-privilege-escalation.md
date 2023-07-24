---
layout: post
title:  Privilege escalation risks in AWS
author: "Phil Massyn"
categories: cloud
tags: ["aws","security"]
#image: php.jpg
---

A **privilege escalation** risk is where a user account within a system has the ability to elevate their privileges to a higher level than what was originally intended.  This can have disastrous consequences, particularly if you have an insider threat.  This type of risk is not limited to insiders only.  Any user account with the right permissions can result in unwanted elevated permissions.

## The scenario

_Least Privilege_ dictates that a user account (this includes service accounts) should only have the absolute least amount of permissions necessary to do the job - no more, and no less.  Assuming you have all of this in place for your user accounts, everything should be fine.  Your users can do their thing, and your auditors are happy.

In your system, you have a Lambda function, and for some reason, this Lambda function is running with an Administrator role.  On face value, while this may be a concern, since the function is controlled within your CI/CD pipeline, you're assuming everything is ok.

A developer within your team has requested `lambda:UpdateFunctionCode` to be added to his role, via an inline user policy.  This seems benign enough, and the permissions is granted and applied.  The developer however has an ulterior motive.  Using his newly assigned permissions, he crafts a special Lambda payload.  He uploads it into the Lambda function, and on the next execution, instead of executing the original function code, the Lambda function (with admin permissions) executed the code uploaded by the rogue developer.

## IAM
This is a bit more obvious.  Anyone with access to IAM has the potential access to circumvent everything.  This can include the ability to create new user accounts, creating new policies, updating existing user accounts, to name just a few.

## EC2
What if your developer has the ability to create an EC2 instance?  Seems simple enough.  Within EC2, you may have created an EC2 instance role that has high level access.  By allowing a developer to be able to create an EC2 instance and attaching a pre-existing EC2 instance policy to that EC2 instance, they can gain admin rights to the rest of your AWS account by simply SSH-ing into their new EC2 instance, which will then inherit high level permissions.

## CloudFormation
CloudFormation is a bit more obvious.  Anyone with the ability to create CloudFormation stacks has the ability to create any resources, including new IAM policies, users and roles, that will allow them to gain admin rights.  Restrict the access of anyone who has the rights to create cloudformation stacks.

## Permissions to watch out for
### Lambda
* `lambda:UpdateFunctionCode`
* `iam:PassRole`, `lambda:CreateFunction`, and `lambda:InvokeFunction`

### IAM
* `iam:CreatePolicyVersion`
* `iam:SetDefaultPolicyVersion`
* `iam:PutRolePolicy`
* `iam:CreateAccessKey`
* `iam:CreateLoginProfile`
* `iam:UpdateLoginProfile`
* `iam:AttachUserPolicy`
* `iam:AttachGroupPolicy`
* `iam:AttachRolePolicy`
* `iam:PutUserPolicy`
* `iam:PutGroupPolicy`
* `iam:AddUserToGroup`
* `iam:UpdateAssumeRolePolicy` and `sts:AssumeRole`

## EC2
* `iam:PassRole` and `ec2:RunInstances`

### Glue
* `glue:UpdateDevEndpoint`
* `iam:PassRole` and `glue:CreateDevEndpoint`

### CloudFormation
* `iam:PassRole` and `cloudformation:CreateStack`

### DataPipeLine
* `iam:PassRole`, `datapipeline:CreatePipeline`, and `datapipeline:PutPipelineDefinition`

## My take-away

* Do not under-estimate the determination of the adversery who really wants to take advantage of you.
* Be careful simply adding permissions to a user or policy.  Challenge, review, scrutinize, and document every request.
* Review your CloudTrail logs - make sure that no one is abusing the privileges you have granted to them.
* Revoke the access once the required task has been completed.  Sensitive permissions like these should not remain.
* The mere existance of a role means it can be used.  Remove unused roles.


