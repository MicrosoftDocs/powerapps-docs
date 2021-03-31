---
title: "Information about Power Apps portals package version 9.2.2103 | MicrosoftDocs"
description: "Learn about the Power Apps portals package version 9.2.2103 and the changes."
author: GitanjaliSingh33msft
ms.service: powerapps
ms.topic: conceptual
ms.custom: 
ms.date: 03/30/2021
ms.author: gisingh
ms.reviewer: tapanm
---

# Power Apps portals package version 9.2.2103

Power Apps portal package version 9.2.2103 is generally available. To learn about how to update your portal solution, go to [Update the Power Apps portals solution](../admin/update-portal-solution.md).

In this article, you'll learn about:

- Features and enhancements included in this update.
- Scope of the release.

For a full list of all portal updates released to date and their corresponding KB articles, go to [Portal Capabilities for Microsoft Dynamics 365 Releases](https://support.microsoft.com/topic/portal-capabilities-for-microsoft-dynamics-365-releases-81f5fcc9-ef72-8b2e-5b4b-29e9840fb5c4).

## Updates included with portals package version 9.2.2103

This portals package version update includes the following changes to Dataverse starter portal, and blank portal.

### Enhancements

- [Power Apps component framework](../../../developer/component-framework/overview.md) update with control style of **Code Components**.
- [Terminology changes](../terminology-changes.md) for portals.
- New entity **adx_BotConsumer** added for [Power Apps Virtual Agents](/power-virtual-agents) support with forms, views & relationships.
- Change solutions upgrade behavior to update instead of upgrade if existing version is 9.2.x.
- Support for special characters (\#, %, \*, ‰, €) in file name for attachments to [Azure Blob Storage](../enable-azure-storage.md).
- Handle XSS vector gracefully on page load.

### Fixes

- Saving Entity Form Metadata without mandatory field.
- Action button configuration gets cleared within additional setting.
- Enable IsVisibleInMobileClient field for Contact in Microsoft Identity.
- Web form lookup field create new metadata is not working.
- Deactivating a root page needs to deactivate it's content pages too.
- Hide Post back URL Field on the web form step.
- Web form lookup field create new metadata is not working.

> [!NOTE]
> In addition, this package also release contains accessibility fixes.

### See also

[Release updates](../release-updates.md) <br>
[Portal Capabilities for Microsoft Dynamics 365 Releases](https://support.microsoft.com/topic/portal-capabilities-for-microsoft-dynamics-365-releases-81f5fcc9-ef72-8b2e-5b4b-29e9840fb5c4) <br>
[How to Determine the Version of a Microsoft Dynamics 365 Portal](https://support.microsoft.com/topic/how-to-determine-the-version-of-a-microsoft-dynamics-365-portal-d2400fdc-b1dd-597b-feab-87abc805325e)
