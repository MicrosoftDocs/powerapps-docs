---
title: "Security Model (Common Data Service) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "Common Data service provides a security model that protects data integrity and privacy, and supports efficient data access and collaboration" # 115-145 characters including spaces. This abstract displays in the search result.
ms.custom: ""
ms.date: 10/19/2019
ms.reviewer: "pehecke"
ms.service: powerapps
ms.topic: "article"
author: "paulliew" # GitHub ID
ms.author: "jdaly" # MSFT alias of Microsoft employees only
manager: "ryjones" # MSFT alias of manager or PM counterpart
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---
# Security Model

[!INCLUDE[cc-data-platform-banner](../../includes/cc-data-platform-banner.md)]

Common Data Service provides a security model that protects data integrity and privacy, and supports efficient data access and collaboration. The goals of the model are as follows:
- Provide users with the access only to the appropriate levels of information that is required to do their jobs.
- Categorize users by role and restrict access based on those roles.
- Support data sharing so that users and teams can be granted access to records that they do not own for a specified collaborative effort.
- Prevent a user's access to records the user does not own or share.

**Role-based security** focuses on grouping a set of privileges together that describe the responsibilities (or tasks that can be performed) for a user. Common Data Service  includes a set of predefined security roles. Each aggregates a set of user rights to make user security management easier. Also, each application deployment can define its own roles to meet the needs of different users. Security roles are associated with a [business unit](businessunit-entity.md).

**Record-based security** focuses on access rights to specific records.

**Field-level security** restricts access to specific high business impact fields in an entity only to specified users or teams.
Combine role-based security, record-level security, and field-level security to define the overall security rights that users have within your Power Apps application.

As a developer, you should know that queries in your code run in the context of a user, and will only return records that the user is entitled to read.
Further, your code will only be able to perform operations based on the privileges assigned to the user account through the security roles or team membership.

For detailed information, see [Security in Common Data Service](/power-platform/admin/wp-security)

