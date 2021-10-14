---
title: "PostSave Event (Client API reference) in model-driven apps| MicrosoftDocs"
description: Information about PostSave event methods.
ms.date: 04/15/2021
ms.service: powerapps
ms.topic: "reference"
applies_to: "Dynamics 365 (online)"
ms.assetid: 89123cde-7c66-4c7d-94e4-e287285019f8
author: "Nkrb"
ms.author: "nabuthuk"
manager: "kvivek"
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---

# PostSave Event

PostSave event occurs after the `OnSave` event is complete. This event is used to support or execute custom logic using web resources to perform after `Save` actions when the `save` event is successful or failed due to server errors.

Use the [addOnPostSave](../controls/addOnPostSave.md) and [removeOnPostSave](../controls/removeOnPostSave.md) methods to manage event handlers for this event.

> [!NOTE]
> This method is supported only on Unified Interface

## Syntax

`formContext.data.entity.addOnPostSave(myFunction)`

## Parameter

|Name|Type|Required|Description|
|------|------|------|---------|
|myFunction|function reference|Yes|The function to add to the PostSave event. The [execution context](../../clientapi-execution-context.md) is automatically passed as the first parameter to this function.|
|||||

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
  window.setTimeout(function () { formContext.ui.clearFormNotification(myUniqueId); }, 10000);
  
}

```

## Relates articles

[getEntityReference](../save-event-arguments/getEntityReference.md)<br/>
[getIsSaveSuccess](../save-event-arguments/getIsSaveSuccess.md)<br/>
[getSaveErrorInfo](../save-event-arguments/getSaveErrorInfo.md)

[!INCLUDE[footer-include](../../../../../includes/footer-banner.md)]
