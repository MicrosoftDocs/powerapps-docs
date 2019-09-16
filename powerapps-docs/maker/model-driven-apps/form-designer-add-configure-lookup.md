---
title: Configure a lookup component on a form | MicrosoftDocs"
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

# Configure a lookup component on a form  
A lookup field can be used to link to a record in another entity. A lookup component is automatically used when a lookup field is added to a form. Makers can configure a lookup component using the form designer.

## Configure a lookup component
These are the properties available to configure when using a lookup component on a form using the form designer.


<!--from editor: "Drop-down" should only be an adjective. In the following table, is it a list? A menu? -->


|Area  |Name  |Description  |
|---------|---------|---------|
| **Display options** | **Entity** |  The related entity that the lookup field connects to. |
| **Display options** | **Default view** |  The view of the entity selected in the **Entity** property that can be used to get and display the list of records that app users can select in the lookup drop-down. |
| **Display options** | **Allow users to change view** |  When selected, app users can change from the **Default view** to another view of the entity selected in the **Entity** property. |
| **Display options** | **Show all views** |  When selected, app users can change from the **Default view** to all other views of the entity selected in the **Entity** property. <br /><br />This property is only available when **Allow users to change view** is selected. |
| **Display options** | **Selected views** |  A list of views of the entity selected in the **Entity** property that app users can change to from the **Default view**. <br /><br />This property is only available when **Allow users to change view** is selected and **Show all views** is unselected. |

## See also
[Overview of the model-driven form designer](form-designer-overview.md)  
[Create, edit, or configure forms using the form designer](create-and-edit-forms.md)  
[Add, configure, move, or delete fields on a form](add-move-or-delete-fields-on-form.md)  
[Add, configure, move, or delete components on a form](add-move-configure-or-delete-components-on-form.md)  
[Add, configure, move, or delete sections on a form](add-move-or-delete-sections-on-form.md)  
[Add, configure, move, or delete tabs on a form](add-move-or-delete-tabs-on-form.md)  
[Configure header properties in the form designer](form-designer-header-properties.md)  
[Add and configure a sub-grid component on a form](form-designer-add-configure-subgrid.md)  
[Add and configure a quick view component on a form](form-designer-add-configure-quickview.md)  
[Using the tree view in the form designer](using-tree-view-on-form.md)  
[Create and edit fields](../common-data-service/create-edit-field-portal.md)  
