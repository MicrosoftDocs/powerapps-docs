---
title: "formContext.ui.sections (Client API reference) in model-driven apps| MicrosoftDocs"
description: "A section contains methods to manage how it appears as well as accessing the tab that contains the section."
ms.author: jdaly
author: adrianorth
manager: kvivek
ms.date: 03/12/2022
ms.reviewer: jdaly
ms.topic: "reference"
applies_to: "Dynamics 365 (online)"
ms.subservice: mda-developer
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
contributors:
  - JimDaly
---
# formContext.ui.sections (Client API reference)



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
|[getLabel](formcontext-ui-sections/getLabel.md)|[!INCLUDE[formcontext-ui-sections/includes/getLabel-description.md](formcontext-ui-sections/includes/getLabel-description.md)]|
|[getName](formcontext-ui-sections/getName.md)|[!INCLUDE[formcontext-ui-sections/includes/getName-description.md](formcontext-ui-sections/includes/getName-description.md)]|
|[getParent](formcontext-ui-sections/getParent.md)|[!INCLUDE[formcontext-ui-sections/includes/getParent-description.md](formcontext-ui-sections/includes/getParent-description.md)]|
|[getVisible](formcontext-ui-sections/getVisible.md)|[!INCLUDE[formcontext-ui-sections/includes/getVisible-description.md](formcontext-ui-sections/includes/getVisible-description.md)]|
|[setLabel](formcontext-ui-sections/setLabel.md)|[!INCLUDE[formcontext-ui-sections/includes/setLabel-description.md](formcontext-ui-sections/includes/setLabel-description.md)]|
|[setVisible](formcontext-ui-sections/setVisible.md)|[!INCLUDE[formcontext-ui-sections/includes/setVisible-description.md](formcontext-ui-sections/includes/setVisible-description.md)]|

### Related topics

[formcontext.ui.tabs](formcontext-ui-tabs.md)

[formContext](../clientapi-form-context.md)


[!INCLUDE[footer-include](../../../../includes/footer-banner.md)]