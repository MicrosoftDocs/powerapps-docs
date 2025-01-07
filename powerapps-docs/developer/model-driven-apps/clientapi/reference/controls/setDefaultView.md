---
title: "setDefaultView (Client API reference) in model-driven apps"
description: Sets teh default view for the lookup control dialog box.
author: MitiJ
ms.author: mijosh
ms.date: 03/12/2022
ms.reviewer: jdaly
ms.topic: reference
applies_to: "Dynamics 365 (online)"
search.audienceType: 
  - developer
contributors:
  - JimDaly
---
# setDefaultView (Client API reference)

Sets the default view for the lookup control dialog box.

## Control types supported

Lookup

## Syntax

`formContext.getControl(arg).setDefaultView(viewId);`

## Parameter

|Name|Type|Required|Description|
|----|----|----|----|
|`viewId`|String|Yes|The ID of the view to be set as the default view.|

[!INCLUDE[cc-terminology](../../../../data-platform/includes/cc-terminology.md)]

## Example

This **setDefaultViewSample** function will set the **account** form primary contact lookup default view to the **My Active Contacts** view.

```JavaScript
function setDefaultViewSample(executionContext) {
    var formContext = executionContext.getFormContext();
    formContext.getControl("primarycontactid").setDefaultView("{00000000-0000-0000-00AA-000010001003}");
}
```

### Related articles

[getDefaultView](getDefaultView.md) 

[!INCLUDE[footer-include](../../../../../includes/footer-banner.md)]
