---
title: "getSaveMode (Client API reference) in Dynamics 365 Customer Engagement| MicrosoftDocs"
ms.date: 10/31/2017
ms.service: "crm-online"
ms.topic: "reference"
applies_to: "Dynamics 365 (online)"
ms.assetid: 03e970ee-7ed3-4df2-9670-222d76a479fd
author: "KumarVivek"
ms.author: "kvivek"
manager: "amyla"
---
# getSaveMode (Client API reference)

[!INCLUDE[](../../../../includes/cc_applies_to_update_9_0_0.md)]

[!INCLUDE[./includes/getSaveMode-description.md](./includes/getSaveMode-description.md)]

## Syntax

`executionContext.getEventArgs().getSaveMode()`

## Return Value

**Type**: Number

**Description**: The following table describes the supported values returned to detect different ways entity records may be saved by the user.

|Value |Save mode |Entity|
|---|---|---|
|1|Save|All|
|2|Save and Close|All|
|5|Deactivate|All|
|6|Reactivate|All|
|7|Send|Email|
|15|Disqualify|Lead|
|16|Qualify|Lead|
|47|Assign|User or Team owned entities|
|58|Save as Completed|Activities|
|59|Save and New|All|
|70|Auto Save|All|

## Remarks

This method is essential if you want to enable auto-save for most forms in an organization but disable it for specific forms.  

## Example

The following code registered for the **OnSave** event with the execution context passed to it will prevent any saves that initiate from an auto-save but allow all others. With auto-save enabled, navigating away is equivalent to **Save and Close**. This code will prevent any saves that are initiated by the 30 second timer or when people navigate away from a form with unsaved data.

```JavaScript
function preventAutoSave(executionContext) {
    var eventArgs = executionContext.getEventArgs();
    if (eventArgs.getSaveMode() == 70 || eventArgs.getSaveMode() == 2) {
        eventArgs.preventDefault();
    }
}
```

To save a record the user must click the **Save** icon at the bottom of the form or a custom **Save** command needs to be added to the command bar.

### Related topics

[isDefaultPrevented](isDefaultPrevented.md)

[preventDefault](preventDefault.md)

