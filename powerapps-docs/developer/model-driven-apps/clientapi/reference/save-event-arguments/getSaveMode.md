---
title: "getSaveMode (Client API reference) in model-driven apps| MicrosoftDocs"
description: Includes description and supported parameters for the getSaveMode method.
ms.date: 04/21/2021
ms.service: powerapps
ms.topic: "reference"
applies_to: "Dynamics 365 (online)"
ms.assetid: 03e970ee-7ed3-4df2-9670-222d76a479fd
author: "Nkrb"
ms.author: "nabuthuk"
manager: "kvivek"
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---
# getSaveMode (Client API reference)



[!INCLUDE[./includes/getSaveMode-description.md](./includes/getSaveMode-description.md)]

## Syntax

`executionContext.getEventArgs().getSaveMode()`

## Return Value

**Type**: Number

**Description**: The following table describes the supported values returned to detect different ways table records may be saved by the user.

|Value |Save mode |Table|
|---|---|---|
|1|Save|All|
|2|Save and Close|All|
|5|Deactivate|All|
|6|Reactivate|All|
|7|Send|Email|
|15|Disqualify|Lead|
|16|Qualify|Lead|
|47|Assign|User or Team owned tables|
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

To save a record the user must select the **Save** icon at the bottom of the form or a custom **Save** command needs to be added to the command bar.

### Related topics

[isDefaultPrevented](isDefaultPrevented.md)

[preventDefault](preventDefault.md)



[!INCLUDE[footer-include](../../../../../includes/footer-banner.md)]