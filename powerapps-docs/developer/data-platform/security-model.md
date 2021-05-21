---
title: "Security and data access (Microsoft Dataverse) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "Microsoft Dataverse provides a security model that protects data integrity and privacy, and supports efficient data access and collaboration." # 115-145 characters including spaces. This abstract displays in the search result.
ms.custom: intro-internal
ms.date: 03/11/2021
ms.reviewer: "pehecke"
ms.service: powerapps
ms.topic: "article"
author: "paulliew" # GitHub ID
ms.author: "paulliew" # MSFT alias of Microsoft employees only
manager: "sunilg" # MSFT alias of manager or PM counterpart
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---
# Security and data access

Microsoft Dataverse provides a security model that protects data integrity and privacy, and supports efficient data access and collaboration. The goals of the model are as follows:

- Provide users with the access only to the appropriate levels of information that is required to do their jobs.
- Categorize users by role and restrict access based on those roles.
- Support data sharing so that users and teams can be granted access to records that they do not own for a specified collaborative effort.
- Prevent a user's access to records the user does not own or share.

As a developer, you should know that the data operations in your code run in the context of a user. If your code attempts to perform an operation that the user is not allowed to perform, an exception will be thrown. Your code will only be able to perform operations based on the privileges assigned to the user account through security roles or team membership. How can you make sure that errors related to security don’t impact your code?

-	If you are developing a synchronous [plug-in](plug-ins.md) (an event handler), any error in a data operation will cause the entire data transaction being processed to fail. You cannot simply ignore the error in a try/catch. How can you test whether the current user has the privileges to perform the operation and the appropriate level of access to a record so that your logic will succeed?
-	If you are developing an application with a user interface, you probably want to disable or hide commands which the user cannot perform.

The first step is to understand the security concepts that apply to data access. You should understand how to configure and manage security roles because you will need to apply them when you test your code. But this is beyond the scope of this topic.  You can find more information about security concepts in general and security configuration tasks in [Security concepts in Microsoft Dataverse](/power-platform/admin/wp-security-cds).

In the security related topics that follow, we will assume that you have have a basic understanding of Microsoft Dataverse security concepts and administration so that we can proceed with addressing the security and data access APIs that you will need to use in your plug-in or application.


[!INCLUDE[footer-include](../../includes/footer-banner.md)]