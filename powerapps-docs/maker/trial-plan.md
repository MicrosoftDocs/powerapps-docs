---
title: FAQ about the free trial license | Microsoft Docs
description: What the free trial license for PowerApps includes, how to sign up for it, and what happens when it expires
services: ''
suite: powerapps
documentationcenter: na
author: AFTOwen
manager: kfile
editor: ''
tags: ''

ms.service: powerapps
ms.devlang: na
ms.topic: article
ms.tgt_pltfrm: na
ms.workload: na
ms.date: 03/12/2018
ms.author: anneta

---
# FAQ about the free trial license for PowerApps
Sign up for the free trial license to get all PowerApps functionality for 30 days. This license offers the same  capacity and premium features as a PowerApps Plan 2 license, which is more than what many [Office 365 and Dynamics 365 plans](../administrator/pricing-billing-skus.md) or a PowerApps Plan 1 license includes.

## What premium features does the trial license include?

* **Access to the Common Data Service**, which is a secure business data platform built into PowerApps. This service comes with hundreds of standard business entities, so all your apps can share the same definition of “customer,” “product,” “lead,” and more. [Learn more](./common-data-service/data-platform-intro.md)
* **Access to premium connections** such as Salesforce, DB2, Zendesk, and the Common Data Service. With many Office 365 and Dynamics 365 plans, you can connect to data sources such as Office 365, Dynamics 365, Dropbox, and Twitter. With the trial license, you can also connect to data through premium connectors such as these:
  
    ![](./media/trial-plan/premium-connectors.png)
  
    In the [complete list of connectors](./canvas-apps/connections-list.md), premium connectors appear with a badge:
  
    ![](./media/trial-plan/premium-badge.png)
* **Access to the PowerApps admin center**, in which you can manage your environments, databases, user permissions, and data policies. [Learn more](../administrator/introduction-to-the-admin-center.md)

For more information about the functionality and capacity in the trial license, see the [pricing page](https://powerapps.microsoft.com/pricing/).

## What email address can I use?
You can use a work or school address to sign up for a trial license. If you use another kind of address, you might experience one of the symptoms in this table.

| Symptom / Error Message | Cause and Workaround |
| --- | --- |
| **Personal email addresses (e.g. nancy@gmail.com)** <br> <br> You receive a message like the following during signup: <br> <br> `You entered a personal email address: Please enter your work email address so we can securely store your company's data.` <br> <br> or <br> <br> `That looks like a personal email address. Enter your work address so we can connect you with others in your company. And don’t worry. We won’t share your address with anyone.` |PowerApps does not support email addresses provided by consumer email services or telecommunications providers. <br> <br> To complete signup, try again using an email address assigned by your work or school. |
| **.gov or .mil addresses** <br> <br> You receive a message like the following during signup: <br> <br> `PowerApps unavailable: PowerApps is not available for users with .gov or .mil email addresses at this time. Use another work email address or check back later.` <br> <br> or <br> <br> `We can't finish signing you up. It looks like Microsoft PowerApps isn't currently available for your work or school.` |PowerApps does not support .gov or .mil addresses at this time. |
| **Email address is not an Office 365 ID** <br> <br>  You receive a message like the following during signup: <br> <br> `We can't find you at contoso.com.  Do you use a different ID at work or school? Try signing in with that, and if it doesn't work, contact your IT department.` |Your organization signs in to Office 365 and other Microsoft services with IDs other than email addresses. For example, your email address might be Nancy.Smith@contoso.com, but your ID is nancys@contoso.com. <br> <br> To complete signup, use the ID that your organization has assigned to you for signing in to Office 365 or other Microsoft services.  If you don't know what this is, contact your IT administrator. |

## What happens when my trial expires?
After 30 days, you'll be prompted to request an extension of the trial or purchase a plan. You can find details about all plans on the [pricing page](https://powerapps.microsoft.com/pricing/).

* If you have access to PowerApps through Office 365, Dynamics 365, or a PowerApps Plan 1 license, you can still use PowerApps, but you might lose access to the Common Data Service, premium connectors, the admin center, and other Plan 2 features. For example, this screen might appear if you try to create a premium connection:
  
    ![](./media/trial-plan/premium-trial-expired.png)

* If your only access to PowerApps is through the trial (for which you signed up on the [PowerApps site](http://powerapps.microsoft.com/) or the [pricing page](http://powerapps.microsoft.com/pricing)), this screen will appear if you try to access PowerApps:
  
    ![](./media/trial-plan/extend-screen.png)

## How many days are left before my trial expires?
You'll soon be able to see how many days are left before your trial expires.

## What happens to my data when my trial expires?
If you still have access to PowerApps, you can continue to use it. Any data in the Common Data Service will remain as it is, and any app or flow that used the Common Data Service as a data source will continue to run as it did. But you won't be able to use that app or flow, and you'll be prompted to request an extension of the trial or purchase a plan if you try to modify a schema or entities in the Common Data Service.

## What should I do next?
You can retain access to PowerApps and its features by doing either of the following:

* Extend your trial license when prompted.
* Review the available plans on the PowerApps [pricing page](https://powerapps.microsoft.com/pricing/), and then [purchase one](../administrator/signup-for-powerapps-admin.md).

