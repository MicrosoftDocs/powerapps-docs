---
title: "Add and configure a quick view component on a form | MicrosoftDocs"
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
  - "Power Apps maker portal impact"
search.audienceType: 
  - maker
search.app: 
  - "PowerApps"
  - D365CE
---

# Add and configure a quick view component on a form  
A main form that displays the details of a record can use a quick view component to display read-only details of a related record (lookup). The data displayed by the quick view component is defined by the quick view form of the related entity. When there is no related record, such as a lookup, the quick view component is automatically hidden.

## Add a quick view component
You add a quick view component in the same way as you add any other component. More information: [Add, configure, move, or delete components on a form](add-move-configure-or-delete-components-on-form.md)

## Configure a quick view component
These are the properties available to configure when using a quick view component on a form using the form designer.


<!--note from editor: "Drop-down" should be used only as an adjective. In the following table, is it a list? A menu? (It's used three times in line 44.) --> 


|Area   |Name  |Description  |
|---------|---------|---------|
|**Display options** | **Label** | The localizable label for the quick view visible to users. <br /><br /> This property is required. |
| **Display options** | **Name** |  The unique name for the quick view that is used when referencing it in scripts. The name can contain only alphanumeric characters and underscores. <br /> <br />This property is required. |
| **Display options**  | **Hide label** |  When selected, the quick view label is hidden. |
| **Display options**  | **Quick view forms** |  A list of quick view forms that are displayed to app users. <br /><br />To configure the list of quick view forms <br /><br /> Select **Select forms ...**, and then in the **Lookup** drop-down select a lookup field where you want to display a quick view form. <br /><br />Depending on the lookup field you select in the **Lookup** drop-down, you will see drop-downs that will let you select quick view forms for one or more entities. |

## See also
[Overview of the model-driven form designer](form-designer-overview.md)  
[Create, edit, or configure forms using the form designer](create-and-edit-forms.md)  
[Add, configure, move, or delete fields on a form](add-move-or-delete-fields-on-form.md)  
[Add, configure, move, or delete components on a form](add-move-configure-or-delete-components-on-form.md)  
[Add, configure, move, or delete sections on a form](add-move-or-delete-sections-on-form.md)  
[Add, configure, move, or delete tabs on a form](add-move-or-delete-tabs-on-form.md)  
[Configure header properties in the form designer](form-designer-header-properties.md)  
[Add and configure a sub-grid component on a form](form-designer-add-configure-subgrid.md)  
[Configure a lookup component on a form](form-designer-add-configure-lookup.md)  
[Using the tree view in the form designer](using-tree-view-on-form.md)  
[Create and edit fields](../common-data-service/create-edit-field-portal.md)  
