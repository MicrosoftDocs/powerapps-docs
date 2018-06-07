---
title:  Manage Support instances | Microsoft Docs
description: In this quickstart, you learn how to download a list of apps created in your environments
services: 'powerapps'
suite: powerapps
documentationcenter: na
author: jimholtz
manager: kfile
editor: ''
tags: ''

ms.service: powerapps
ms.devlang: na
ms.topic: article
ms.tgt_pltfrm: na
ms.workload: na
ms.date: 03/21/2018
ms.author: jimholtz

---
# Manage Support instances

> [!NOTE]
> ![This page is under construction. Check back soon!](media/under_construction.png "Coming soon")  [!INCLUDE[cc-under-construction](../includes/cc-under-construction.md)]

[!INCLUDE[cc-applies-to-update-9-0-0](../includes/cc_applies_to_update_9_0_0.md)]<br/>[!INCLUDE [cc_applies_to_update_8_2_0](../includes/cc_applies_to_update_8_2_0.md)]

A Support instance is any non-production instance of [!INCLUDE[pn_CRM_Online](../includes/pn-crm-online.md)] used by Microsoft Support to reproduce and resolve customer issues. When there is an issue affecting the operation of your online service, Microsoft can create a Support instance in your tenant to troubleshoot and repair the issue.  It is isolated from your production instance so it does not impact your business operations. Dynamics 365 System admins have full control of managing and providing organization data by [copying it](copy-environment.md) to a Support instance. 

**What is a Support instance?**

-  It is an instance created in your tenant by Microsoft for purposes of preventing, detecting, or repairing problems affecting the operation of your online service.
-  It does not require any additional non-production instance to be purchased.
-  The database size of a Support instance does not count towards your storage limit.
-  It resides in the same regional datacenter as your source instance. 

**What data is in a Support instance?**

-  When a Support instance is initially created by Microsoft, it contains no customer data or customizations.
-  System admins [manage Support instances](manage-online-environments.md) in the [!INCLUDE[pn_dyn_365_admin_center](../includes/pn-dyn-365-admin-center.md)].
-  System admins can [copy an instance](copy-environment.md) to a Support instance, and then choose whether to provide a [Minimal](copy-environment.md#minimal-copy-instance) or a [Full](copy-environment.md#full-copy-instance) copy of their instance.
-  System admins must consent to providing a copy of their data to Microsoft. 

**Who has access to a Support instance?**

Minimal copy:

-  Microsoft staff who are members of a support security group

Full copy:

-  Microsoft staff who are members of an elevated support security group

**What kind of data access does Microsoft have?**

Online (via the application):

-  System admin privileges

Database (via SQL query tools):

-  Read/Write access to all tables
-  Access to the database requires additional approval by Microsoft and it is managed, controlled, and granted as needed.
-  Access to the database is time limited (for example, 30 minutes) and expires automatically.

**How long does a Support instance stay in your tenant?**

1. 14 days or upon resolution of the problem.
2. System admins can [delete](delete-environment.md) the Support instance at any time.

**Is access and usage of Support instance audited?** 

Yes.