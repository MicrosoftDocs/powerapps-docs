---
title: Create custom picklists | Microsoft Docs
description: Create a custom picklist.
services: powerapps
documentationcenter: na
author: pvillads
manager: kfend
editor: ''
tags: ''

ms.service: powerapps
ms.devlang: na
ms.topic: article
ms.tgt_pltfrm: na
ms.workload: na
ms.date: 02/09/2017
ms.author: kfend

---
# Create custom picklists
It's now possible to create your own picklists, in addition to the ones that are available out-of-the-box. Picklists, which are basically a named list of items that include a name and descriptions, are a simple concept. When the picklist fields are rendered, a drop-down menu that contains the display names of the items will appear. 

Picklists are added by using the menu item, **Picklists** on the **Common Data Service** tab, under the **Entities** menu. Click the menu to view all of the picklists that are currently defined in your environment. Several commonly used picklists are already defined for you and can easily be identified by their type, **Standard**. The ones that you create for yourself are the type **Custom**.

1. To create a new picklist, at the top of the page, click **New Picklist**. On the page that opens, define your picklist by entering the name, display name, and a description.
   > [!IMPORTANT]
> The picklist name can't be changed after you create the picklist. There are a few requirements for the picklist name. The name must be simple and can't contain any special characters. Also, you can only have one picklist with a particular name. If you try to create another picklist with the same name, you will receive an error. These restrictions don't apply to the **Display name**.
   
    In this topic, we will create a picklist that can be used to choose a mode of transportation.
2. Name the picklist **Transportation** and add the information to the required fields.
3. Click **Next**, and on the next page provide the different elements of the picklist, for this example, the transportation providers. When the page opens, you will see that a single item is already created. Update the line item with information appropriate to the picklist that you are creating. Editing is done in the line. There is not a separate page for each picklist item. Click in the  **NewItem** field to add the first item. Any time that you need a new picklist element, click **Add item** at the top right of the screen to add a new row. 

You can delete an item by clicking the garbage can icon on the far right of each item line. When all of the required items have been added, click **Create** to create the list and submit it to the server. You will see the picklist added to the list of existing picklists.

You can now use the picklist to define fields on your entities by adding a field type **Picklist**, and then using the **Display name** in the **Properties** pane for the field. 

