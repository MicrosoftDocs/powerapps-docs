---
title: "getEntityMainFormDescriptor (Client API reference) in model-driven apps| MicrosoftDocs"
ms.date: 10/09/2020
ms.service: powerapps
ms.topic: "reference"
applies_to: "Dynamics 365 (online)"
ms.assetid: 28c36741-0070-435c-a42f-49f4dda2ef7f
author: "Nkrb"
ms.author: "nabuthuk"
manager: "kvivek"
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---

# getEntityMainFormDescriptor (Client API reference)

[!INCLUDE[./includes/getEntityMainFormDescriptor-description.md](./includes/getEntityMainFormDescriptor-description.md)] 

## Syntax

`Xrm.Utility.getEntityDefaultMainFormDescriptor(entityName, formId);`

## Parameters

|Name |Type |Required |Description |
|---|---|---|---|
|entityName|String|Yes|The logical name of the entity.|
|formId|String|No|The form ID of the entity.|
||||

## Returns

**Type**: Promise

**Description**: Returns a promise containing the default main form descriptor with the following attributes.

|Attribute Name| Type| Description|
|-------------|-------|-----------|
|Attributes| Array of strings| List of all the attributes on the main form.|
|EntityLogicalName| String| The logical name of the specified entity.|
|Id| string| The form ID of the specified entity.|
|Label| String| The label of the specified entity.|
|Name| String| The display name of the specified entity.|
|Sections| String| The sections name of the specified entity.|
|ShowLabel| Boolean| Indicates whether to show the label of the specified entity or not.|
|Visible| Boolean| Indicates whether the form is visible or not.|
||||

## Example

The following sample code shows how to get the main form descriptor for a specified entity. 

```javascript
  // Define the entity and form ID
  var entityName = "account";
  var formId = "8448b78f-8f42-454e-8e2a-f8196b0419af";

  // Get the entity main form descriptor 
  Xrm.Utility.getEntityMainFormDescriptor(entityName, formId);
```

## Related topics

[Xrm.Utility](../xrm-utility.md)

[!INCLUDE[footer-include](../../../../../includes/footer-banner.md)]