---
title: Starter Portal package version 9.2.2103.x
description: Learn about the Starter Portal package version 9.2.2103 and the changes.
author: GitanjaliSingh33msft
ms.service: powerapps
ms.topic: conceptual
ms.custom: 
ms.date: 04/05/2021
ms.author: gisingh
ms.reviewer: tapanm
contributors:
    - tapanm-msft
    - GitanjaliSingh33msft
---

# Starter Portal package version 9.2.2103.x

Starter Portal package version 9.2.2103.x is generally available. To learn about how to update your portal solution, go to [Update the Power Apps portals solution](../admin/update-portal-solution.md).

In this article, you'll learn about the fixes and enhancements included in this update.

> [!NOTE]
> - The update package for Starter Portal shows as Common Data Service Starter Portal in Power Platform admin center.
> - Package updates are released in stages across regions. During the rollout phase, your environment may take time to show the new package update depending on your region.

For a full list of all portal updates released to date and their corresponding KB articles, go to [Portal Capabilities for Microsoft Dynamics 365 Releases](https://support.microsoft.com/topic/portal-capabilities-for-microsoft-dynamics-365-releases-81f5fcc9-ef72-8b2e-5b4b-29e9840fb5c4).

For more information about creating a portal with Starter Portal package, go to [Create a Dataverse starter portal](../create-portal.md) or [Create a starter portal in an environment containing customer engagement apps](../create-dynamics-portal.md).

## Enhancements

The package update includes the following enhancements extending the capabilities of portals.

- [Power Apps component framework](../../../developer/component-framework/overview.md) update with control style of **Code Components**.
- [Terminology changes](../terminology-changes.md) for portals.
- Change solutions upgrade behavior to update instead of upgrade if existing version is 9.2.x.
- Support for special characters (\#, %, \*, ‰, €) in file name for attachments to [Azure Blob Storage](../enable-azure-storage.md).
- Handle XSS vector gracefully on page load.

## Fixes

The package update includes the fixes for the following problems.

- Saving Entity Form Metadata without mandatory field.
- Action button configuration gets cleared within additional setting.
- Enable IsVisibleInMobileClient field for Contact in Microsoft Identity.
- Web form lookup field to create new entity form isn't working.
- Deactivating a root page needs to deactivate its content pages.
- Hide Post back URL Field on the web form step.

> [!NOTE]
> In addition, this package release contains accessibility fixes.

### See also

[Release updates](../release-updates.md) <br>
[Portal Capabilities for Microsoft Dynamics 365 Releases](https://support.microsoft.com/topic/portal-capabilities-for-microsoft-dynamics-365-releases-81f5fcc9-ef72-8b2e-5b4b-29e9840fb5c4) <br>
[How to Determine the Version of a Microsoft Dynamics 365 Portal](https://support.microsoft.com/topic/how-to-determine-the-version-of-a-microsoft-dynamics-365-portal-d2400fdc-b1dd-597b-feab-87abc805325e)
