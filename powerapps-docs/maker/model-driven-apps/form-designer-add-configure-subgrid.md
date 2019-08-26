---
title: "Add and configure a sub-grid component on a form | MicrosoftDocs"
ms.custom: ""
ms.date: 08/26/2019
ms.reviewer: ""
ms.service: powerapps
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "get-started-article"
applies_to: 
  - "Dynamics 365 (online)"
  - "Dynamics 365 Version 9.x"
  - "PowerApps"
author: "Aneesmsft"
ms.author: "matp"
manager: "kvivek"
tags: 
  - "PowerApps maker portal impact"
search.audienceType: 
  - maker
search.app: 
  - "PowerApps"
  - D365CE
---

# Add and configure a sub-grid component on a form  
This article outlines how makers can add and configure a sub-grid component using the new form designer.

A form that is displaying the details of a record can use a sub-grid component to display a list of related or unrelated records in a tabular format.

## Add a sub-grid component
Adding a sub-grid component is the same as any other component. More information: [Add, move or delete components on a form](add-move-configure-or-delete-components-on-form.md)

## Configure a sub-grid component
These are the properties available to configure when using a sub-grid component on a form using the new form designer.

|Area   |Name  |Description  |
|---------|---------|---------|
| **Display options** | **Label** | The localizable label for the sub-grid visible to users. <br /><br />This property is required.|
| **Display options** |  **Name** |  The unique name for the sub-grid that is used when referencing it in scripts. The name can contain only alphanumeric characters and underscores. <br /><br />This property is required. |
| **Display options** | **Hide on phone** |  For a condensed version of the form on phone screens, sub-grid can be hidden. |
| **Display options** | **Show related records** |  When selected, the sub-grid will display only records related to the current record that is being displayed on the form. <br /><br />The **Entity** drop down is also filtered to only list entities that are related to the current entity. |
| **Display options** | **Entity** |  The entity whose records you want to display in the sub-grid. <br /><br />When **Show related records** is selected the list of entities is filtered to show only entities that are related to the current entity. In this case, in addition to the entity name the name of the lookup field is also displayed in parentheses. |
| **Display options** | **Default view** |  The view of the entity selected in the **Entity** property that will be used to get and display the list of records in the sub-grid. |
| **Display options** | **Allow users to change view** |  When selected, end-users will be able to change from the **Default view** to another view of the entity selected in the **Entity** property. |
| **Display options** | **Show all views** |  When selected, end-users will be able to change from the **Default view** to all other views of the entity selected in the **Entity** property. <br /><br />This property is only available when **Allow users to change view** is selected. |
| **Display options** | **Selected views** |  A list of views of the entity selected in the **Entity** property that end-users will be able to change to from the **Default view**. <br /><br />This property is only available when **Allow users to change view** is selected and **Show all views** is unselected. |

## See also
[Overview of the model-driven form designer](form-designer-overview.md)  
[Create, edit, or configure forms using the form designer](create-and-edit-forms.md)  
[Add, configure, move, or delete fields on a form](add-move-or-delete-fields-on-form.md)  
[Add, configure, move, or delete components on a form](add-move-configure-or-delete-components-on-form.md)  
[Add, configure, move, or delete sections on a form](add-move-or-delete-sections-on-form.md)  
[Add, configure, move, or delete tabs on a form](add-move-or-delete-tabs-on-form.md)  
[Configure header properties in the form designer](form-designer-header-properties.md)  
[Add and configure a quick view component on a form](form-designer-add-configure-quickview.md)  
[Using the tree view in the form designer](using-tree-view-on-form.md)  
[Create and edit fields](../common-data-service/create-edit-field-portal.md)  
