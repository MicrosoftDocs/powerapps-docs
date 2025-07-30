---
title: Manage access
description: This article helps you use security roles to manage cards.
ms.date: 11/17/2022
ms.topic: overview
author: mduelae
ms.author: mkaur
ms.reviewer: 
ms.custom: 
ms.collection: 

---

# Manage access

[!INCLUDE[cards-deprecation-banner](~/includes/cards-deprecation-notice.md)]

This article explains how to manage cards using security roles, and also provides guidance on deleting a record.

## Change who can create cards

Cards are stored as rows in Dataverse within the **Card** table. Administrators can use [security roles to control who can create, read, and update cards](/power-platform/admin/wp-security-cds#tablerecord-ownership).

For example, if a user is only assigned to a security role that doesn't have permission to create rows in the **Card** table, then the user can't create cards. 

Note, regardless of the user's security role, a user can still receive and use cards sent through Teams.

## Disable cards for an environment

The communication between Cards for Power Apps and Dataverse relies on the **Cards Role** security role. If you remove permissions for the **Cards Role** to create, read, or update the **Card** table in the environment will result in the unavailability of cards for all users in that environment.


## Cards security roles

- **Cards Basic Role** can be used to grant a user access to view, create, and use cards in that environment.

   Other security roles can be modified to view, create, and use cards by changing security role access to the **Card** table in Dataverse.

- **Cards Role** is used internally by the Cards for Power Apps service to communicate with Dataverse.
