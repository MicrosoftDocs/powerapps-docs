---
title: Starter portal package version 9.3.2201.x
description: Learn about the changes included in starter portal package version 9.3.2201, including problem fixes and enhancements to extend the capabilities of portals.
author: GitanjaliSingh33msft
ms.service: powerapps
ms.topic: conceptual
ms.custom: 
ms.date: 01/28/2022
ms.subservice: portals
ms.author: gisingh
ms.reviewer: ndoelman
contributors:
    - nickdoelman
    - GitanjaliSingh33msft
---

# Starter portal package version 9.3.2201.x

Starter portal package version 9.3.2201.x is generally available. To learn how to update your portal solution, go to [Update the Power Apps portals solution](../admin/update-portal-solution.md).

In this article, you'll learn about the fixes and enhancements included in this update.

> [!NOTE]
> - The update package for starter portal shows as "Common Data Service Starter Portal" in the Power Platform admin center.
> - Package updates are released in stages across regions. During the rollout phase, your environment may take time to show the new package update depending on your region.

For a full list of all portal updates released to date and their corresponding KB articles, go to [Portal Capabilities for Microsoft Dynamics 365 Releases](https://support.microsoft.com/topic/portal-capabilities-for-microsoft-dynamics-365-releases-81f5fcc9-ef72-8b2e-5b4b-29e9840fb5c4).

For more information about creating a portal with starter portal package, go to [Create a Dataverse starter portal](../create-portal.md) or [Create a starter portal in an environment containing customer engagement apps](../create-dynamics-portal.md).

## Enhancements

The package update includes the following enhancements to extend the capabilities of portals:

- Within the Portal Management app, portal user passwords can be updated using a metadata driven dialog.

- Column permission configuration added to the Portal Management app.

- Ability to disable the legacy runtime CMS editor popup for starter templates.

- Web Notification solution is deprecated.

- Website record configuration in Portal Management app to include additional information such as website version. 

- Website configuration reorganized for easier navigation to related website metadata:
    - Tabs promoted:
        - Basic Forms
        - Lists
    - Tabs moved to related:
        - Web Link Sets
        - Site Markers
        - Publishing States
        - Website Access Permissions

- Filetype attribute added.

- Adx_pagenotification workflow will be removed from MicrosoftCrmPortalBaseWorkflows solution.

- Handlebar.js updated to latest version

## Fixes

The package update includes the fixes for the following problems:

- Fixed issue to provide correct partial URL error message and local translation string.

### See also

[Release updates](../release-updates.md) <br>
[Portal Capabilities for Microsoft Dynamics 365 Releases](https://support.microsoft.com/topic/portal-capabilities-for-microsoft-dynamics-365-releases-81f5fcc9-ef72-8b2e-5b4b-29e9840fb5c4) <br>
[How to Determine the Version of a Microsoft Dynamics 365 Portal](https://support.microsoft.com/topic/how-to-determine-the-version-of-a-microsoft-dynamics-365-portal-d2400fdc-b1dd-597b-feab-87abc805325e)
