---
title: Quick view control properties for model-driven app main forms in Power Apps | MicrosoftDocs
description: Understand the quick view control properties for main forms
Keywords: Quick view control properties; Dynamics 365; Main forms
author: Mattp123
applies_to: 
  - "Dynamics 365 (online)"
  - "Dynamics 365 Version 9.x"
  - "powerapps"
ms.author: matp
manager: kvivek
ms.date: 03/30/2020
ms.service: powerapps
ms.topic: article
ms.assetid: 68f68d5b-6c71-4b95-bb46-d48c59d9008e
search.audienceType: 
  - maker
search.app: 
  - PowerApps
  - D365CE
---
# Model-driven app quick view control properties

A quick view control on a model-driven app form displays data from a record that is selected in a lookup on the form. The data displayed in the control is defined using a quick view form. The data displayed is not editable, but when the primary field is included in the quick view form, it becomes a link to open the related record. More information: [Create and edit quick view forms](create-edit-quick-view-forms.md)  

> [!div class="mx-imgBorder"] 
> ![Contact quick view form on the account form](media/quick-view-form-contact.png "Contact quick view form on the account form")  

1.  Sign in to [Power Apps](https://make.powerapps.com/?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc).  

2.  Expand **Data**, select **Entities**, select the entity that you want, and then select the **Forms** tab.  

3.  Select a form, which **Type** is **Main**.

4.  In the form designer, select **Add Component**.

5.  In the left navigation pane, select **Quick view**.

6.  In the **Select quick view forms** dialog box, select a **Lookup** field included in the form, and then select a quick view form for the related entities. The related entities shown depend on the **Lookup** field you choose.  

    > [!div class="mx-imgBorder"] 
    > ![Add quick view control](media/select-quick-view-form.png "Add quick view control to main form")

7.  Select **Done** to close the **Select quick View forms** dialog box. The quick view form appears on the form, and the properties of the quick view appear in the Properties pane.

|Property|Description|  
|--------------|-----------------|  
|**Label**|**Required**: A label to display for the quick view form.|  
|**Name**|**Required**: The unique name for the quick view form that is used when referencing it in scripts.|  
|**Hide label**|Displays the label on the form.| 
|**Quick view forms**|Lists the quick view forms that you selected for the related entities. 
|**Select forms**|Select or change the selected quick view forms for the related entities. The related entities shown depend on the **Lookup** field you choose.|  
|**Components**|Properties to configure for the component. A quick view control component has no properties to configure, and by default is shown whether someone is using a web browser, Dynamics 365 for phones, or Dynamics 365 for tablets.

## Quick view control properties in classic form designer

1.  Sign in to [Power Apps](https://make.powerapps.com/?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc).  

2.  Expand **Data**, select **Entities**, select the entity that you want, and then select the **Forms** tab. 

3.  In the list of forms, open the form of type **Main**.

4.  On the command menu, select **Switch to classic**.

5.  Then on the **Insert** tab, select **Quick View Form** to view quick view control properties.

    > [!div class="mx-imgBorder"] 
    > ![quick-view-control](media/quick-view-control.png)
  
|Property|Description|  
|--------------|-----------------|  
|**Name**|**Required**: The unique name for the quick view form that is used when referencing it in scripts.|  
|**Label**|**Required**: A label to display for the quick view form.|  
|**Display label on the Form**|Displays the label on the form.|  
|**Lookup Field**|Choose one of the lookup fields included in the form.|  
|**Related entity**|This value depends on the **Lookup Field** you choose. It is usually the primary entity for the 1:N entity relationship for the lookup.<br /><br /> If the entity includes a **Potential Customer** lookup that can accept either an account or contact, in the **Quick View Form** field you can choose a quick view form for both account and contact by changing this value and then choosing another quick view form.|  
|**Quick View Form**|If the **Related entity** has any quick view forms you can select them here. Otherwise, select **New** to create one.<br /><br /> Select **Edit** to change the selected quick view form.|  
|**Additional Properties**|You can specify the default rendering style by selecting the check box.|

## Next steps

[Use the Main form and its components](use-main-form-and-components.md)
 
