---
title: Starter portal package version 9.2.2108.x
description: Learn about the changes included in starter portal package version 9.2.2108, including problem fixes and enhancements to extend the capabilities of portals.
author: GitanjaliSingh33msft
ms.service: powerapps
ms.topic: conceptual
ms.custom: 
ms.date: 08/24/2021
ms.subservice: portals
ms.author: gisingh
ms.reviewer: ndoelman
contributors:
    - nickdoelman
    - GitanjaliSingh33msft
---

# Starter portal package version 9.2.2108.x

Starter portal package version 9.2.2108.x is generally available. To learn how to update your portal solution, go to [Update the Power Apps portals solution](../admin/update-portal-solution.md).

In this article, you'll learn about the fixes and enhancements included in this update.

> [!NOTE]
> - The update package for starter portal shows as "Common Data Service Starter Portal" in the Power Platform admin center.
> - Package updates are released in stages across regions. During the rollout phase, your environment may take time to show the new package update depending on your region.

For a full list of all portal updates released to date and their corresponding KB articles, go to [Portal Capabilities for Microsoft Dynamics 365 Releases](https://support.microsoft.com/topic/portal-capabilities-for-microsoft-dynamics-365-releases-81f5fcc9-ef72-8b2e-5b4b-29e9840fb5c4).

For more information about creating a portal with starter portal package, go to [Create a Dataverse starter portal](../create-portal.md) or [Create a starter portal in an environment containing customer engagement apps](../create-dynamics-portal.md).

## Enhancements

The package update includes the following enhancements to extend the capabilities of portals:

- Table permissions enabled for forms and list by default for new records.
- Form-level warning notification added for existing records that has **Enable Table Permissions** option unchecked, and when users un-checks the checkbox.
- Form-level error notification added in a list that has OData feed enabled and **Enable Table Permissions** unchecked.

## Fixes

The package update includes the fixes for the following problems:

- Customer configured contact name is getting overwritten by the solution **msdynce_PortalPrivacyExtensions**.

### See also

[Release updates](../release-updates.md) <br>
[Portal Capabilities for Microsoft Dynamics 365 Releases](https://support.microsoft.com/topic/portal-capabilities-for-microsoft-dynamics-365-releases-81f5fcc9-ef72-8b2e-5b4b-29e9840fb5c4) <br>
[How to Determine the Version of a Microsoft Dynamics 365 Portal](https://support.microsoft.com/topic/how-to-determine-the-version-of-a-microsoft-dynamics-365-portal-d2400fdc-b1dd-597b-feab-87abc805325e)
