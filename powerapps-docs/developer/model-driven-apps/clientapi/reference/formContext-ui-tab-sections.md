---
title: "formContext.ui.tabs section (Client API reference) in model-driven apps"
description: "A section contains methods to manage how it appears as well as accessing the tab that contains the section."
author: MitiJ
ms.author: mijosh
ms.date: 05/31/2022
ms.reviewer: jdaly
ms.topic: reference
applies_to: "Dynamics 365 (online)"
ms.subservice: mda-developer
search.audienceType: 
  - developer
contributors:
  - JimDaly
---
# formContext.ui.tabs section (Client API reference)

A section contains methods to manage how it appears as well as accessing the tab that contains the section.

You can retrieve a section object (say **sectionObj**) by using the following example code:

```JavaScript
var tabObj = formContext.ui.tabs.get(arg);
var sectionObj = tabObj.sections.get(arg);
```

## Properties

- **controls**: The section controls collection provides access to the controls within a section. See [Collections (Client API reference)](collections.md) for information about the methods exposed by collections. See [Controls (Client API reference)](controls.md) for information about the properties and methods exposed by the objects in this collection.


## Methods

|Name | Description |
|--|--|
|[getLabel](formContext-ui-tab-sections/getLabel.md)|[!INCLUDE[formContext-ui-tab-sections/includes/getLabel-description.md](formContext-ui-tab-sections/includes/getLabel-description.md)]|
|[getName](formContext-ui-tab-sections/getName.md)|[!INCLUDE[formContext-ui-tab-sections/includes/getName-description.md](formContext-ui-tab-sections/includes/getName-description.md)]|
|[getParent](formContext-ui-tab-sections/getParent.md)|[!INCLUDE[formContext-ui-tab-sections/includes/getParent-description.md](formContext-ui-tab-sections/includes/getParent-description.md)]|
|[getVisible](formContext-ui-tab-sections/getVisible.md)|[!INCLUDE[formContext-ui-tab-sections/includes/getVisible-description.md](formContext-ui-tab-sections/includes/getVisible-description.md)]|
|[setLabel](formContext-ui-tab-sections/setLabel.md)|[!INCLUDE[formContext-ui-tab-sections/includes/setLabel-description.md](formContext-ui-tab-sections/includes/setLabel-description.md)]|
|[setVisible](formContext-ui-tab-sections/setVisible.md)|[!INCLUDE[formContext-ui-tab-sections/includes/setVisible-description.md](formContext-ui-tab-sections/includes/setVisible-description.md)]|

### Related articles

[formcontext.ui.tabs](formcontext-ui-tabs.md)   
[formContext](../clientapi-form-context.md)


[!INCLUDE[footer-include](../../../../includes/footer-banner.md)]
