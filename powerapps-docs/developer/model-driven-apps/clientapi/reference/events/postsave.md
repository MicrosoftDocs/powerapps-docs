---
title: "PostSave Event (Client API reference) in model-driven apps"
description: Information about PostSave event methods.
author: MitiJ
ms.author: mijosh
ms.date: 08/20/2024
ms.reviewer: jdaly
ms.topic: reference
applies_to: "Dynamics 365 (online)"
search.audienceType: 
  - developer
contributors:
  - JimDaly
---

# PostSave Event

PostSave event occurs after the `OnSave` event is complete. This event is used to support or execute custom logic using web resources to perform after `Save` actions when the `save` event is successful or failed due to server errors.

[!INCLUDE [cc_book-instead-of-save](../../../../../includes/cc_book-instead-of-save.md)]

Use the [addOnPostSave](../formContext-data-entity/addOnPostSave.md)  and [removeOnPostSave](../formContext-data-entity/removeOnPostSave.md) methods to manage event handlers for this event.

> [!NOTE]
> This method is supported only on Unified Interface

## Syntax

`formContext.data.entity.addOnPostSave(myFunction)`

## Parameter

|Name|Type|Required|Description|
|------|------|------|---------|
|`myFunction`|function reference|Yes|The function to add to the PostSave event. The [execution context](../../clientapi-execution-context.md) is automatically passed as the first parameter to this function.|

[!INCLUDE[cc-terminology](../../../../data-platform/includes/cc-terminology.md)]

### Example 

The following sample code displays organization unique name as form notification.

```JavaScript
function addMessageToOnPostSave(executionContext) {
   var formContext = executionContext.getFormContext();
    formContext.data.entity.addOnPostSave(displayOrgName);
}

// function to display organization unique name.

function displayOrgName(executionContext)
{
  var formContext = executionContext.getFormContext();
  var orgName = Xrm.Utility.getGlobalContext().organizationSettings.uniqueName;
  var myuniqueId = "_myUniqueId";
  formContext.ui.setFormNotification(orgName, "INFO", myuniqueId);
}

```

### Related articles

[getEntityReference](../save-event-arguments/getEntityReference.md)   
[getIsSaveSuccess](../save-event-arguments/getIsSaveSuccess.md)   
[getSaveErrorInfo](../save-event-arguments/getSaveErrorInfo.md)   
[Events (Client API reference)](../events.md)   
[Events in forms and grids in model-driven apps](../../events-forms-grids.md)

[!INCLUDE[footer-include](../../../../../includes/footer-banner.md)]
