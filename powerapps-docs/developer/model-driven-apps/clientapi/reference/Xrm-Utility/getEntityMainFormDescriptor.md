---
title: "getEntityMainFormDescriptor (Client API reference) in model-driven apps"
description: Includes description and supported parameters for the getEntityMainFormDescriptor method.
author: sriharibs-msft
ms.author: srihas
ms.date: 03/12/2022
ms.reviewer: jdaly
ms.topic: reference
applies_to: "Dynamics 365 (online)"
search.audienceType: 
  - developer
contributors:
  - JimDaly
---

# getEntityMainFormDescriptor (Client API reference)

[!INCLUDE[./includes/getEntityMainFormDescriptor-description.md](./includes/getEntityMainFormDescriptor-description.md)] 

## Syntax

`Xrm.Utility.getEntityMainFormDescriptor(entityName, formId);`

## Parameters

|Name |Type |Required |Description |
|---|---|---|---|
|`entityName`|String|Yes|The logical name of the table.|
|`formId`|String|No|The form ID of the table.|

## Returns

**Type**: Promise

**Description**: Returns a promise containing the default main form descriptor with the following values.

|Parameter Name| Type| Description|
|-------------|-------|-----------|
|`Attributes`| Array of strings| List of all the columns on the main form.|
|`EntityLogicalName`| String| The logical name of the specified table.|
|`Id`| string| The form ID of the specified table.|
|`Label`| String| The label of the specified table.|
|`Name`| String| The display name of the specified table.|
|`Sections`| String| The sections name of the specified table.|
|`ShowLabel`| Boolean| Indicates whether to show the label of the specified table or not.|
|`Visible`| Boolean| Indicates whether the form is visible or not.|

## Example

The following sample code shows how to get the main form descriptor for a specified table. 

```javascript
  // Define the table and form ID
  var entityName = "account";
  var formId = "8448b78f-8f42-454e-8e2a-f8196b0419af";

  // Get the main form descriptor 
  Xrm.Utility.getEntityMainFormDescriptor(entityName, formId);
```

## Related articles

[Xrm.Utility](../xrm-utility.md)

[!INCLUDE[footer-include](../../../../../includes/footer-banner.md)]
