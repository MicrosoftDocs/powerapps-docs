---
title: "setCurrentView (Client API reference) in model-driven apps| MicrosoftDocs"
description: Includes description and supported parameters for the setCurrentView method.
ms.date: 04/21/2021
ms.service: powerapps
ms.topic: "reference"
applies_to: "Dynamics 365 (online)"
ms.assetid: f5ee65bf-2964-49c9-9dd2-d81416353bf3
author: "Nkrb"
ms.author: "nabuthuk"
manager: "kvivek"
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---
# setCurrentView (Client API reference)



[!INCLUDE[./includes/setCurrentView-description.md](./includes/setCurrentView-description.md)]

## Grid types supported

Read-only grid

## Syntax

`viewSelector.setCurrentView(object);`

## Parameter

|Name|Type|Required|Description|
|--|--|--|--|
|object|Lookup object|Yes|Specify the Lookup object that has the following values:<br/>- **entityType**: Number. The object type code for the SavedQuery (1039) or UserQuery (4230) that represents the view the user can select.<br/>- **id**: String. The Id for the view the user can select.<br/>- **name**: String. The name of the view the user can select.|

## Remarks

If the subgrid control is not configured to display the view selector, calling this method on the `viewSelector` object will throw an error.

To get the `viewSelector` object, see [ViewSelector](../viewselector.md).

## Example

```JavaScript
function setView(executionContext) {
    var ContactsIFollow = {
        entityType: 1039, // SavedQuery
        id: "3A282DA1-5D90-E011-95AE-00155D9CFA02",
        name: "Contacts I Follow"
    }
    // Get the gridContext
    var formContext = executionContext.getFormContext();
    var gridContext = formContext.getControl("Contacts");

    // Set the view using ContactsIFollow
    gridContext.getViewSelector().setCurrentView(ContactsIFollow);
}
```

### Related topics

[ViewSelector](../viewselector.md)






[!INCLUDE[footer-include](../../../../../../includes/footer-banner.md)]