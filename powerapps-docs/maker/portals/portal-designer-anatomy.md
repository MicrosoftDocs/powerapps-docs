---
title: Power Apps portals Studio
description: Learn how to use Power Apps portals Studio.
author: neerajnandwana-msft
ms.topic: conceptual
ms.collection: get-started
ms.date: 2/23/2022
ms.subservice: portals
ms.author: nenandw
ms.reviewer: kkendrick
contributors:
    - neerajnandwana-msft
    - nickdoelman
    - ProfessorKendrick
    - sampatn
---

# Power Apps portals Studio

[!INCLUDE [cc-portals-studio-ga-banner](../../includes/cc-portals-studio-ga-banner.md)]

You can use Power Apps portals Studio to create and customize your website. It contains various options to add and configure webpages, components, forms, and lists.

> [!NOTE]
> To use the portals Studio, you will need to be assigned the [system administrator role](/power-platform/admin/assign-security-roles) in the same Microsoft Dataverse environment as your site. 

## Open portals Studio

To open Power Apps portals Studio:

1. Go to **Active Sites** tab on [Power Pages](https://make.powerpages.microsoft.com).

1. On your site, select **More Commands**(...) for the site, then choose **Edit in Power Apps Sutdio** 

    ![Select Edit in Power Apps Studio to open the site in Power Apps Portals Studio.](media/manage-existing-portals/edit-in-power-apps.png "Select Edit in Power Apps Studio to open the site in Studio")

## Understand portals Studio

The anatomy of Power Apps portals Studio is as follows:

![Power Apps portals Studio anatomy.](media/maker-anatomy.png "Power Apps portals Studio anatomy")  

| **Annotation** | **Name**        | **Description**                                                                              |
|----------------|-----------------|----------------------------------------------------------------------------------------------|
| 1              | Command bar     | Allows you to: <ul> <li> Create a webpage. </li> <li> Delete a component. </li> <li> Sync Configuration - synchronizes the latest portal configuration changes in Microsoft Dataverse database with your current Studio session. For example, use *Sync Configuration* to reflect the changes in Studio when using the Portal Management app to change the configuration of pages, forms or any other objects. </li> <li> Browse website - clears the portal cache and opens the current portal page. </li></ul>  |
| 2              | Toolbelt        | Allows you to:<ul><li>View and manage webpages</li><li>Add components</li><li>Edit templates</li></ul>  |
| 3              | Canvas          | Contains components that build a webpage.                                                    |
| 4              | Footer          | Displays autosave status and allows you to open-source code editor.                         |
| 5              | Properties pane | Displays properties of webpage and selected components and lets you edit them as required. |

> [!NOTE]
> - Editing a portal through Power Apps portals Studio will temporarily cause poor portal performance due to multiple background processes. For example, the clear cache process runs and reloads data from Microsoft Dataverse.
> - Power Apps portals Studio only supports editing in the language selected while provisioning the portal. For help with creating portals in additional languages, see [Create additional portals in an environment](create-additional-portals.md).

## Next steps

[Create and manage webpages](create-manage-webpages.md)

### See also

[Customize webpages](compose-page.md)


[!INCLUDE[footer-include](../../includes/footer-banner.md)]
