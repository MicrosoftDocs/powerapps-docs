---
title: "Change the solution publisher prefix | MicrosoftDocs"
ms.custom: ""
ms.date: 05/11/2018
ms.reviewer: ""
ms.service: "crm-online"
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
applies_to: 
  - "Dynamics 365 (online)"
  - "Dynamics 365 Version 9.x"
author: "Mattp123"
ms.assetid: ece684h8-ad40-4bfa-975a-3e5bafb854aa
caps.latest.revision: 55
ms.author: "matp"
manager: "kvivek"
---

# Change the solution publisher prefix

Every customization you make is part of a solution. Every solution has a publisher. By default, the solution you will work with in PowerApps will be the **Common Data Services Default Solution** which is associated with the **CDS Default Publisher**.

The default customization prefix will be randomly assigned for this publisher, for example it could be `cr8a3`. This means that the name of every new item of metadata created for your organization will have this prepended to the names used to uniquely identify the items. If you create a new entity named **Animal**, the unique name used by CDS for Apps would be `cr8a3_animal`. The same is true for any new fields (attributes), relationships, or optionset options.

Unless you will distribute your solution so that it is installed together with metadata items that were created for another solution publisher, it really isn't important what the customization prefix is. It isn't visible to most people who use your apps. But it is exposed to developers and other technical people who do things like build reports. It provides a quick way to understand which solution added the item.

For this reason, many people like to change the solution publisher prefix so that it will be more meaningful, especially when viewing metadata items that include those imported from other solutions. 

> [!NOTE]
> If you change the solution publisher prefix, you should do it before you create an new metadata items. You can't change the names of metadata items.
> When you change the customizaiton prefix value, make sure to tab to the next field. The **Option Value Prefix** will automatically generate a number based on the customization prefix. This number is used when you add options to option sets and provides an indicator of which solution was used to add the option. 

## Change the solution publisher prefix for the CDS Default Publisher  

 1. In the PowerApps portal, select **Model-driven** in the bottom left corner.
 2. Click **Advanced** in the left navigation to open the **Common Data Services Default Solution**
 3. In the solution explorer, select the **Information** area in the left navigation.
 4. Click the **Publisher** link to open the **CDS Default Publisher** form.
 5. Edit the **Prefix** field value to the customization prefix you want.
 6. Click **Save and Close**.
  
## Change the solution publisher prefix for any publisher

People who distribute their solutions will typically work within a solution that they create rather than the **Common Data Services Default Solution**. The customization prefix is usually set when they create the solution. You can change the customization prefix for another unmanaged solution you are working with by following these steps: 

 1. In the PowerApps portal, select **Model-driven** in the bottom left corner.
 2. Click **Advanced** in the left navigation to open the **Common Data Services Default Solution**
 3. Edit the URL of the page to remove everything after `dynamics.com` and reload the page.
 4. Navigate to **Settings** > **Customization** > **Customizations**. 
 5. Click **Publishers**. You can now see a list of publishers available.
 6. Click the publisher that you want to edit to open the publisher form.
 7. Edit the **Prefix** field value to the customization prefix you want.
 6. Click **Save and Close**.
  