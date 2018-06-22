---
title: "setDefaultView (Client API reference) in Dynamics 365 Customer Engagement| MicrosoftDocs"
ms.date: 10/31/2017
ms.service: "crm-online"
ms.topic: "reference"
applies_to: "Dynamics 365 (online)"
ms.assetid: 8c918cd4-d0ce-45e5-91a3-1addf11258c7
author: "KumarVivek"
ms.author: "kvivek"
manager: "amyla"
---
# setDefaultView (Client API reference)

[!INCLUDE[](../../../../includes/cc_applies_to_update_9_0_0.md)]

Sets the default view for the lookup control dialog box.

## Control types supported

Lookup

## Syntax

`formContext.getControl(arg).setDefaultView(viewId);`

## Parameter

|Name|Type|Required|Description|
|--|--|--|--|
|viewId|String|Yes|The ID of the view to be set as the default view.|

## Example

This **setDefaultViewSample** function will set the **account** entity form primary contact lookup default view to the **My Active Contacts** view.

```JavaScript
function setDefaultViewSample(executionContext) {
    var formContext = executionContext.getFormContext();
    formContext.getControl("primarycontactid").setDefaultView("{00000000-0000-0000-00AA-000010001003}");
}
```

### Related topics

[getDefaultView](getDefaultView.md) 


