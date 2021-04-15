---
title: "setDefaultView (Client API reference) in model-driven apps| MicrosoftDocs"
description: Sets teh default view for the lookup control dialog box.
ms.date: 04/15/2021
ms.service: powerapps
ms.topic: "reference"
applies_to: "Dynamics 365 (online)"
ms.assetid: 8c918cd4-d0ce-45e5-91a3-1addf11258c7
author: "Nkrb"
ms.author: "nabuthuk"
manager: "kvivek"
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---
# setDefaultView (Client API reference)

Sets the default view for the lookup control dialog box.

## Control types supported

Lookup

## Syntax

`formContext.getControl(arg).setDefaultView(viewId);`

## Parameter

|Name|Type|Required|Description|
|--|--|--|--|
|viewId|String|Yes|The ID of the view to be set as the default view.|

[!INCLUDE[cc-terminology](../../../../data-platform/includes/cc-terminology.md)]

## Example

This **setDefaultViewSample** function will set the **account** form primary contact lookup default view to the **My Active Contacts** view.

```JavaScript
function setDefaultViewSample(executionContext) {
    var formContext = executionContext.getFormContext();
    formContext.getControl("primarycontactid").setDefaultView("{00000000-0000-0000-00AA-000010001003}");
}
```

### Related topics

[getDefaultView](getDefaultView.md) 




[!INCLUDE[footer-include](../../../../../includes/footer-banner.md)]