---
title: "PostSave Event (Client API reference) in model-driven apps| MicrosoftDocs"
description: Information about PostSave event methods.
ms.date: 01/30/2021
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

Use the `addOnPostSave`  method to manage event handlers for this event.

> [!NOTE]
> This method is supported only on Unified Interface.

<!--Some of the post save events include which are used by one of the first party app Field Service.
1) When we create a work order incident, read incident type, and retrieve all incident products where incident type is equal to incident type on work order incident, then create work order products.
2) If work order incident is primary incident on work order, modifying the work order incident that is updates the primary inc
When a primary contact phone number is updated, update the same on the account phone number.-->

## Syntax

`formContext.data.entity.addOnPostSave()`

## Parameter

|Name|Type|Required|Description|
|------|------|------|---------|
|myFunction|function reference|Yes|The function to add to the PostSave event. The [execution context](../../clientapi-execution-context.md) is automatically passed as the first parameter to this function.|
|||||



<!--Code Example:
We call below method and it will display org name. For making decisions on whether the save succeeded or failed, executioncontext object will have params such as 
1) getIsSaveSuccess() - use this method to know if the save operation on the entity succeeds or fails
Usage - executionContext.getEventArgs(). getIsSaveSuccess();
2) getEntityReference() - it will have entity info being saved/updated in case of success such as entity id, entity name (for eg., account or contact)
Usage - executionContext.getEventArgs(). getEntityReference();
3) getSaveErrorInfo() - Error details on why an entity save failed.
Usage - executionContext.getEventArgs(). getSaveErrorInfo ();-->

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
  formContext.ui.setNotification(orgName, "INFO", myuniqueId);
  window.setTimeout(function () { formContext.ui.clearFormNotification(myUniqueId); }, 10000);
  
}

```

## Relates articles

[getEntityReference](../save-event-arguments/getEntityReference.md)<br/>
[getIsSaveSuccess](../save-event-arguments/getIsSaveSuccess.md)<br/>
[getSaveErrorInfo](../save-event-arguments/getSaveErrorInfo.md)

[!INCLUDE[footer-include](../../../../../includes/footer-banner.md)]