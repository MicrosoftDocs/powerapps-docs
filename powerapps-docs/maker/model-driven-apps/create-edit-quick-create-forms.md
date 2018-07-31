---
title: "Create or edit model-driven app quick create forms in PowerApps | MicrosoftDocs"
description: "Learn how to create or edit a quick create form"
ms.custom: ""
ms.date: 05/23/2018
ms.reviewer: ""
ms.service: "crm-online"
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
applies_to: 
  - "Dynamics 365 (online)"
  - "Dynamics 365 Version 9.x"
  - "powerapps"
author: "Mattp123"
ms.assetid: 68ca9059-cc5a-45e7-88bd-cc57186bbb48
caps.latest.revision: 18
ms.author: "matp"
manager: "kvivek"
---
# Create or edit model-driven app quick create forms for a streamlined data entry experience

In this topic, you create and edit a quick create form.

 With quick create forms, your app can have a streamlined data entry experience with full support for logic defined by form scripts and business rules. In a PowerApps model-driven app, quick create forms appear when you select the **Create** button in the navigation bar or when you choose **+ New** when creating a new record from a lookup or sub-grid.
  
 The Dynamics 365 customer engagement mobile apps use quick create forms for creating new records. If an entity already has a quick create form configured for it, the mobile apps use that form. If an entity doesn't have a configured quick create form, PowerApps generates a quick create form  for creating records in the mobile apps based on the main form definition.  
  
<a name="BKMK_QuickCreateFormEntities"></a>   
## Entities with quick create forms  
 By default only the following system entities have quick create forms.  
  
|||||  
|-|-|-|-|  
|Account|Campaign Response|Case|Competitor|  
|Contact|Lead|Opportunity||  
  
Although you can create quick create forms for system activity entities, with the exception of the appointment entity, they do not support quick create forms. With the release of Dynamics 365, version 9.0, the appointment entity includes a quick create form for use with the Unified Interface. Currently, the option to disable the quick create form for the appointment entity is not supported. Any of the other [updated entities](create-design-forms.md) and any custom entities can be enabled to support these forms by selecting **Allow Quick Create** in the entity definition and creating a quick create form for the entity. 

You can enable custom activity entities to support quick create forms, and you can create quick create forms for those entities. However, the quick create form for custom activity entities will not be used when people select **Create** on the navigation bar. These quick create forms can be used only when people add a new record for a sub-grid that displays that specific custom activity entity.  
  
<a name="BKMK_CreateQuickCreate"></a>   
## Create a quick create form  
 Although you can define multiple quick create forms, only one quick create form can be used by everyone. The form everyone will use is set using the form order. Quick create forms cannot be assigned to security roles and they do not provide the capability for the user to switch forms.  
  
> [!NOTE]
>  The entity must have the **Allow Quick Create** option enabled for the quick create form to be displayed. 
  
### How to create a quick create form  
  
1.  On the [PowerApps](https://web.powerapps.com) site, select **Model-driven** (lower left of the navigation pane).  

     ![Model-driven design mode](media/model-driven-switch.png)

> [!IMPORTANT]
> “If the **Model-driven** design mode isn't available, you may need to [Create an environment](https://docs.microsoft.com/powerapps/administrator/create-environment).     
  
2.  Expand **Data**, select **Entities**, select the entity that you want, and then select the **Forms** tab.  

3.  On the toolbar select **Add form** > **Quick Create Form**.  
  
4.  In the form designer drag any fields from the **Field Explorer** into the sections on the form.  
  
5.  When you are finished, select **Save**.  
  
6.  Select **Publish** to see the new form in the application.  
  
<a name="BKMK_EditQuickCreate"></a>   
## Edit a quick create form  
 While quick create forms support form scripts and business rules, their purpose is different from main forms and they don’t support all the capabilities of main forms. Quick create forms always have one section with three columns. You can’t add additional sections or columns.  
  
 The following controls cannot be added to quick create forms:  
  
-   Sub-grids  
  
-   Quick View Forms  
  
-   Web resources  
  
-   iFrames  
  
-   Notes  
  
-   Bing Maps  
  
If you add a composite field to a quick create form, it will be displayed as separate fields.  
  
### To edit a quick create form  
  
1.  On the [PowerApps](https://web.powerapps.com) site, select **Model-driven** (lower left of the navigation pane).  

> [!IMPORTANT]
> “If the **Model-driven** design mode isn't available, you may need to [Create an environment](https://docs.microsoft.com/powerapps/administrator/create-environment).    
  
2. Expand **Data**, select **Entities**, select the entity that you want, and then select the **Forms** tab.    

3. In the form list, select a form where the form **Type** is **Quick Create**.  
  
3.  Drag any fields from the **Field Explorer** into the sections in the form.  
  
     See [Configure event handlers](configure-event-handlers-legacy.md) for information about editing event handlers for form scripts.  
  
4.  When you are finished, select **Save**.  
  
5.  Select **Publish** to see the modified form in the application.  
  
### Next steps  
[Overview of the form editor user interface](form-editor-user-interface-legacy.md)
