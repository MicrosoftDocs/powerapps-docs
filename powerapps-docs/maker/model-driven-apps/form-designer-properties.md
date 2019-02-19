---
title: "Properties available in the form designer | MicrosoftDocs"
ms.custom: ""
ms.date: 02/19/2019
ms.reviewer: ""
ms.service: "crm-online"
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

# Properties available in the form designer

Located on the right-pane of the model-driven form designer, the always available property pane lets you quickly view and update the properties of any selected element. 

> [!div class="mx-imgBorder"] 
> ![](media/form-designer-property-pane.png "Form designer property pane")

## Form properties


|Name  |Description  |
|---------|---------|
|**Title**     | Enter a name that will be meaningful to people. This name will be shown to people when they use the form. If they can use multiple forms configured for the entity they will use this name to differentiate between available forms. <br /> This property is required.        |
|**Description**     |  Enter a description that explains how this form is different from other main forms. This description is only shown in the list of forms for an entity in the solution explorer.        |
|**Max Width**     | Set a maximum width (in pixels) to limit the width of the form. The default value is 1900. <br /> This property is required.       |
|**Show image**      | Show the entity’s **Primary Image** if it has one set. This setting will enable showing the image field in the header of this form. <br /> See Enable or disable entity options for more information about entity options.         |


## Tab properties

|Category   |Name  |Description  |
|---------|---------|---------|
|**Display options**      | **Tab label**      | The localizable label for the tab visible to users. <br /> This property is required.         |
| **Display options**      |  **Name**     |  The unique name for the tab that is used when referencing it in scripts. The name can contain only alphanumeric characters and underscores. <br />This property is required.      |
| **Display options**      |  **Expand this tab by default**      |  The tab state can toggle between expanded or collapsed using form scripts or by people selecting the label. Choose the default state for the tab.       |
| **Display options**      | **Hide tab**     | When selected, tab is hidden by default and can be shown using code.       |
| **Display options**      | **Hide on phone**     |  For a condensed version of this form on phone screens, tabs can be hidden.     |
| **Formatting**   | **Layout**     |  Tabs may have up to three columns. Use these options to set the number of tabs and what percentage of the total width they should fill.      |

## Section properties



## See also
[Create and edit forms using the form designer](create-and-edit-forms.md)