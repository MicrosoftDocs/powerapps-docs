---
title: Power Apps preview program 
description: Get early access to functionalities with Power Apps Preview Program
author: jimholtz
ms.service: powerapps
ms.topic: conceptual
ms.custom: 
  - canvas
ms.date: 09/03/2021
ms.author: jimholtz
search.audienceType: 
  - admin
search.app:
  - D365CE
  - PowerApps
---
# Power Apps preview program

Microsoft Power Apps updates the platform and its capabilities every few days or weeks. The Power Apps preview program is a way to get early access to those upcoming functionalities and updates prior to availability in other regions (where customer production apps are deployed).

With the Power Apps preview program, you can:
- **Try out, learn, and dogfood upcoming functionalities**: Many functionalities will be rolled out first in the preview for a few days to get feedback. By participating in the preview program, you can learn about new functionalities sooner and provide feedback. Also, you will be ready to quickly take advantage of new functionalities as soon as they reach regions where their production apps are created.
- **Enable business continuity by ensuring current apps will continue to work** with the upcoming updates (vNext) of Power Apps.

## What in Power Apps is available for preview?

To access the preview functionalities, you need to be in a preview environment or using a preview URL. We have preview features for the following areas across Power Apps.

### Canvas apps

For preview, experimental, and retired features in canvas apps, use [Power Apps Studio](/powerapps/maker/canvas-apps/working-with-experimental-preview) to turn the features On or Off while editing your app.

For early access to upcoming changes in canvas apps, use the following environments:

- [Preview environments](#how-to-get-early-access-to-the-upcoming-updates) - Upcoming changes are typically rolled out to preview environments 1-2 weeks before they're available to all other regions.
- [Sandbox environments](/power-platform/admin/sandbox-environments) - To access preview version of Power Apps on sandbox environments, use make.preview.powerapps.com. 

### Portals, model-driven apps and app management

You can create, manage, and share apps using [Power Apps][2] (make.powerapps.com). To use the preview functionalities, we recommend that you are in a [preview](#how-to-get-early-access-to-the-upcoming-updates) or [sandbox](/power-platform/admin/sandbox-environments) environment and not in a production environment. Then, go to the preview version of [Power Apps][3] (make.preview.powerapps.com).

## How to get early access to the upcoming updates?

For Power Platform, all the apps, flows, and related resources are stored in an environment. Early access to all preview functionalities are also available with an environment created in a region where the vNext (preview) is deployed. For now, there is only one region, **Preview (United States)**, as shown in the image below:

> [!div class="mx-imgBorder"] 
> ![Preview environment.](media/env3-preview.png "Preview environment") 

Select the region for the environment as **Preview (United States)** and accept the consent for joining the preview program to create the environment to get access to the next version (vNext) of Power Apps.
All the apps and other resources created in this environment are on the vNext version of the platform (SAAS).

## How to learn about the latest updates?

You can get aware of the new functionalities, which are available for preview at [What’s new in Power Apps][5]. The functionalities that are only available in the preview have a ‘Preview’ tag.

## Key scenarios to test with the preview program

1. **Validate your production apps with the upcoming Power Apps updates (vNext)**

   You might like to verify your production apps, to be working fine with the next upcoming updates on Power Apps. You can [copy](/powerapps/maker/data-platform/export-solutions) the apps from a production environment to an environment in First Release and play the apps to test out the scenarios. Note, all the other necessary resources like CustomAPI, Power Automate, etc., will also need to be moved along with it. This should just create another copy of these apps and required resources. You can start testing out the newer updates not just for playing an app, but also while editing and managing the apps.
   
2. **Trying out the new functionalities available in preview**

   We will be launching many new functionalities initially in the **Preview (United States)** region. You can try out the new functionalities prior to their being available in rest of the regions (which might impact your production environment).

## How to provide feedback to the product team?

You can provide feedback on the [Power Apps forum][8] and/or contact [support][9].

## What are the known issues and limitations?

1. **Power Apps portals and clients which are not available in preview**

   There are certain functionalities, services, and portals, which are available in preview:
   
   ![Available in preview.](media/table.png)

2. **Using apps created in preview environments in production environments**

   Power Apps does not support opening apps saved in preview only versions of Power Apps in production environments. Most versions of Power Apps will eventually move from preview into production, but how and when this happens is influenced by many factors so it should not be relied on. We recommend you use production environments to create or edit any app intended for use in a production environment.

3. **Database cannot be created in Preview region**

   Currently, you cannot create a database with Microsoft Dataverse in an environment in Preview (United States) region - we're working on it.


<!--Reference links in article-->
[2]: https://make.powerapps.com
[3]: https://make.preview.powerapps.com
[4]: /powerapps/maker/canvas-apps/working-with-experimental-preview
[5]: /powerapps/whats-new
[7]: https://preview.create.powerapps.com
[8]: https://powerusers.microsoft.com/t5/PowerApps-Community/ct-p/PowerApps1
[9]: https://powerapps.microsoft.com/support/


[!INCLUDE[footer-include](../includes/footer-banner.md)]