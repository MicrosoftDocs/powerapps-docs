---
title: "Create or edit quick view forms in PowerApps | MicrosoftDocs"
description: "Learn how to create or edit a quick view form"
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
ms.assetid: 9b101734-cc11-4d05-bd45-eb611eae9931
caps.latest.revision: 14
ms.author: "matp"
manager: "kvivek"
---

# Quickstart: Create a quick view form to view information about a related entity

In this quickstart you learn how to create a quick view form and how to add a quick view control to a main form. 

A quick view form can be added to another form as a quick view control. It provides a template to view information about a related entity record within a form for another entity record. This means your app users do not need to navigate to a different record to see the information needed to do their work.  
  
 Quick view controls are associated with a lookup field that is included in a form. If the lookup field value is not set, the quick view control will not be visible. Data in quick view controls cannot be edited and quick view forms do not support form scripts.  
  
 Because quick view forms are viewed using a quick view control in a form, they do not include header, footer, or navigation areas. Security roles cannot be assigned to quick view forms and they cannot be activated or deactivated.  
  
<a name="BKMK_CreateQFV"></a>   
## Create a quick view form  
 You create quick view forms using the form editor in a manner similar to the way you create other forms. Quick view forms are read-only. Use them to create forms that are for reading purposes only.  
  
1. On the [PowerApps](https://web.powerapps.com) site, select **Model-driven** (lower left of the navigation pane).  

     ![Model-driven design mode](media/model-driven-switch.png)

> [!IMPORTANT]
> “If the **Model-driven** design mode isn't available, you may need to [Create an environment](https://docs.microsoft.com/powerapps/administrator/create-environment).     
  
2. Expand **Data**, select **Entities**, select the entity that you want, and then select the **Forms** tab. 
  
3. On the toolbar, select **Add form** > **Quick View Form**.  
  
4. On the form editor toolbar, select **Form Properties**.  
  
5. In the **Form Properties** dialog box, enter a **Form Name** and **Description** to differentiate this quick view form from any others. Select **OK** to close the **Form Properties** dialog box.  
  
6. In the form designer drag any fields from the **Field Explorer** into the section on the form. 
  
    > [!IMPORTANT]
    >  If you add a field and choose **Field Requirement** > **Business Required** and then save it, you will not be able to delete the field.  
  
7. To save the form and close the form editor select **Save**.  

8. Select **Publish** to see the new form in the application.
  
<a name="BKMK_EditQVF"></a>   
## Edit a quick view form  
 Quick view forms have a simplified layout because they are designed to be viewed within a form section. Only one single column tab is available. You can add only additional single column sections, fields, subgrids, and spacers.   
  
> [!NOTE]
>  You cannot delete a field that is **Business Required**. You will receive this message if you try to delete the field: “The field you are trying to remove is required by the system or business.” If you do not want the field in the form you have to delete the entire form and then recreate it.  
  
 When you edit a quick view form, you must publish your changes before they will be visible in the application.  
  
<a name="BKMK_AddQVF"></a>   
## Add a quick view control to a main form  
 Quick view forms can only be added to a main form where a lookup field exists that targets the entity of the quick view form.  
  
1.  On the [PowerApps](https://web.powerapps.com) site, select **Model-driven** (lower left of the navigation pane).  

> [!IMPORTANT]
> “If the **Model-driven** design mode isn't available, you may need to [Create an environment](https://docs.microsoft.com/powerapps/administrator/create-environment).     
  
2.  Expand **Data**, select **Entities**, select the entity that you want, and then select the **Forms** tab.  

3. Select a form, which **Type** is **Main**.

4. On the form designer select the **Insert** tab, and then on the toolbar select **Quick View Form**.  
  
5.  In the **Quick View Control Properties** dialog box, set the properties for the quick view control, such as **Name**, **Label**, and **Quick View Form**. More information: [Quick view control properties](quick-view-control-properties-legacy.md).  
  
6.  Select **OK** to close the **Quick View Control Properties** dialog box.  
  
7.  Select the **Home** tab, and then select **Publish** to make the quick view control appear on the form.  
  
## Next steps   
 [Create and design forms](create-design-forms.md)   
 [Create or edit quick create forms](create-edit-quick-create-forms.md)
