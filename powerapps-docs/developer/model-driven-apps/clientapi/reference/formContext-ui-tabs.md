---
title: "formContext.ui.tabs (Client API reference) in model-driven apps| MicrosoftDocs"
description: "Learn about working with processes in model-driven apps using client API."
ms.date: 10/31/2018
ms.service: powerapps
ms.topic: "reference"
applies_to: "Dynamics 365 (online)"
ms.assetid: 1888a882-7dfc-41a8-9bb4-d693d6046666
author: "Nkrb"
ms.subservice: mda-developer
ms.author: "nabuthuk"
manager: "kvivek"
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---
# formContext.ui.tabs (Client API reference)



A tab is a group of sections on a page. It contains properties and methods to manipulate tabs as well as access to sections within the tab through the sections collection.

You can retrieve a tab object (say **tabObj**) by using the following example code:

```JavaScript
var tabObj = formContext.ui.tabs.get(arg);
```

## Properties

- **sections**: The sections collection provides access to sections within the tab. See [Collections (Client API reference)](collections.md) for information about methods to access the sections in the collection. See [formContext.ui section](formContext-ui-sections.md) for information about the properties and methods of the section objects in the collection.

## Methods

|Name | Description |
|--|--|
|[addTabStateChange](formcontext-ui-tabs/addTabStateChange.md)|[!INCLUDE[formcontext-ui-tabs/includes/addTabStateChange-description.md](formcontext-ui-tabs/includes/addTabStateChange-description.md)]|
|[getContentType](formcontext-ui-tabs/getContentType.md)|[!INCLUDE[formcontext-ui-tabs/includes/getContentType-description.md](formcontext-ui-tabs/includes/getContentType-description.md)]|
|[getDisplayState](formcontext-ui-tabs/getDisplayState.md)|[!INCLUDE[formcontext-ui-tabs/includes/getDisplayState-description.md](formcontext-ui-tabs/includes/getDisplayState-description.md)]|
|[getLabel](formcontext-ui-tabs/getLabel.md)|[!INCLUDE[formcontext-ui-tabs/includes/getLabel-description.md](formcontext-ui-tabs/includes/getLabel-description.md)]|
|[getName](formcontext-ui-tabs/getName.md)|[!INCLUDE[formcontext-ui-tabs/includes/getName-description.md](formcontext-ui-tabs/includes/getName-description.md)]|
|[getParent](formcontext-ui-tabs/getParent.md)|[!INCLUDE[formcontext-ui-tabs/includes/getParent-description.md](formcontext-ui-tabs/includes/getParent-description.md)]|
|[getVisible](formcontext-ui-tabs/getVisible.md)|[!INCLUDE[formcontext-ui-tabs/includes/getVisible-description.md](formcontext-ui-tabs/includes/getVisible-description.md)]|
|[removeTabStateChange](formcontext-ui-tabs/removeTabStateChange.md)|[!INCLUDE[formcontext-ui-tabs/includes/removeTabStateChange-description.md](formcontext-ui-tabs/includes/removeTabStateChange-description.md)]|
|[setContentType](formContext-ui-tabs/setContentType.md)|[!INCLUDE[formContext-ui-tabs/includes/setContentType-description.md](formContext-ui-tabs/includes/setContentType-description.md)]|
|[setDisplayState](formcontext-ui-tabs/setDisplayState.md)|[!INCLUDE[formcontext-ui-tabs/includes/setDisplayState-description.md](formcontext-ui-tabs/includes/setDisplayState-description.md)]|
|[setFocus](formcontext-ui-tabs/setFocus.md)|[!INCLUDE[formcontext-ui-tabs/includes/setFocus-description.md](formcontext-ui-tabs/includes/setFocus-description.md)]|
|[setLabel](formcontext-ui-tabs/setLabel.md)|[!INCLUDE[formcontext-ui-tabs/includes/setLabel-description.md](formcontext-ui-tabs/includes/setLabel-description.md)]|
|[setVisible](formcontext-ui-tabs/setVisible.md)|[!INCLUDE[formcontext-ui-tabs/includes/setVisible-description.md](formcontext-ui-tabs/includes/setVisible-description.md)]|

### Related topics

[formcontext.ui.tabs](formcontext-ui-tabs.md)

[formContext](../clientapi-form-context.md)



[!INCLUDE[footer-include](../../../../includes/footer-banner.md)]