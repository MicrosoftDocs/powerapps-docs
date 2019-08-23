---
title: "Add and configure a quick view component on a form | MicrosoftDocs"
ms.custom: ""
ms.date: 08/22/2019
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

# Add and configure a quick view component on a form  
This article outlines how makers can add and configure a quick view component using the new form designer.

## Add a quick view component
Adding a quick view component is the same as any other component. More information: [Add, move or delete components on a form](add-move-or-delete-components-on-form.md)

## Configure a view component
These are the properties available to configure when using a quick view component on a form using the new form designer.

|Area   |Name  |Description  |
|---------|---------|---------|
|**Display options** | **Label** | The localizable label for the quick view visible to users. <br /> This property is required. |
| **Display options** | **Name** |  The unique name for the quick view that is used when referencing it in scripts. The name can contain only alphanumeric characters and underscores. <br />This property is required. |
| **Display options**  | **Hide label** |  When selected, the quick view label is hidden. |
| **Display options**  | **Quick view forms** |  A list of quick view forms that will be displayed to end-users. <br />To configure the list of forms, select **Select forms ...** and then in the **Lookup** drop down select a lookup field that you want to display a quick view form for. <br />Depending on the lookup field you select in the **Lookup** drop down you will see drop downs that will let you select quick view forms for one or more entities. |
