---
title: "Manage model-driven app properties in the PowerApps app designer | MicrosoftDocs"
description: "Learn how to manage the properties for your app"
keywords: ""
ms.date: 06/27/2018
ms.service: crm-online
ms.custom:
ms.topic: article
applies_to:
  - "Dynamics 365 (online)"
  - "Dynamics 365 Version 9.x"
  - "powerapps"
author: "Mattp123"
ms.assetid: e773e60f-0211-4c4b-a1af-663be4997629
ms.author: matp
manager: kvivek
ms.reviewer:
ms.suite:
ms.tgt_pltfrm:
caps.latest.revision: 14
topic-status: Drafting
---

# Manage model-driven app properties in the app designer

App properties define important details about the app, like its title or URL. You define app properties when you create an app. If you want to change those properties later, you can do that in the app designer.

1.  In the app designer, on the right side, select the **Properties** tab.

    > [!div class="mx-imgBorder"]
    > ![App designer Properties pane](media/app-designer-properties-tab.png "App designer Properties pane")

2.  Change the information, as required:

    |Property|Description|
    |--------------|-----------------|
    |**Name**|Enter a unique and meaningful name for the app.|
    |**Description**|Type a short description of what the app is.|
    |**Icon**|By default, the **Use Default App** check box is selected. To select a different web resource as an icon for the app, clear the check box, and then select an icon from the drop-down list. This icon is displayed on the app's preview tile.|
    |**Unique Name**| You cannot change the unique name. Using the unique name, you can query tables to get data from the database.|
    |**Choose a welcome page for the app**|This option allows you to select from the web resources available in your environment. The welcome pages you create can contain useful information to users such as links to videos, upgrade instructions, or getting started information. For more information about how to create a web resource, such as an HTML file that you can use as a welcome page, see [Create and edit web resources to extend the web application](create-edit-web-resources.md).|
    |**Enable Mobile Offline**|This option enables the app to be available offline on mobiles to the profiles that are selected using **Mobile Offline Profiles** drop down list.|

3.  Save the app.

## Next steps
 [Create or edit an app](create-edit-app.md)
