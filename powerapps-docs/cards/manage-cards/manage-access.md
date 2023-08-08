---
title: Manage access
description: This article will help you use security roles to manage cards.
ms.date: 11/17/2022
ms.topic: overview
author: sericks007
ms.author: sericks
ms.reviewer: 
ms.custom: 
ms.collection: 

---

# Manage access

This article will help you use security roles to manage cards and explains how to delete a record.

## Manage cards with security roles

This section shows you how to manage cards using security roles.

### Change who can create cards

Cards are stored as rows in Dataverse within the **Card** table. Administrators can use [security roles to control who can create, read, and update cards](/power-platform/admin/wp-security-cds#tablerecord-ownership).

For example, if the user is only assigned to a security role that does not have permission to create rows in the **Card** table, then the user won't be able to create cards.

Note that a user will still be able to receive and use cards sent in Teams, regardless of the security role assigned to the user, as those cards are accessed by the Cards for Power Apps service.

### Disable cards for an environment

The Cards for Power Apps service uses the security role called **Cards Role** to communicate with Dataverse. By removing permissions for the **Cards Role** in an environment to create, read, or update the **Card** table, no one will be able to use cards within that environment.

### Cards security roles

- **Cards Basic Role** can be used to grant a user access to view, create, and use cards in that environment.

   Other security roles can be modified to view, create, and use cards by changing security role access to the **Card** table in Dataverse.

- **Cards Role** is used internally by the Cards for Power Apps service to communicate with Dataverse.
