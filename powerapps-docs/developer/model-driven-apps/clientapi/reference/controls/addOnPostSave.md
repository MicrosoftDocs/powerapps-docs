---
title: "addOnPostSave (Client API reference) in model-driven apps| MicrosoftDocs"
description: Includes description and supported parameters for the addOnPostSave method.
ms.date: 05/19/2021
ms.service: powerapps
ms.topic: "reference"
applies_to: "Dynamics 365 (online)"
ms.assetid: c398dbca-0ead-487a-8a92-35b1f2953bf6
author: "Nkrb"
ms.author: "nabuthuk"
manager: "kvivek"
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---
# addOnPostSave (Client API reference)

Adds an event handler to be called after the record is saved with success or failure.

## Syntax

```javascript
formContext.data.entity.addOnPostSave(myFunction);
```

### Parameter

|Name|Type|Required|Description|
|------|-----|------|----------|
|myFunction|function reference|Yes|The function to be added to the `PostSave` event after the record is saved with success or failure.|

### See also

[PostSave event](../events/postsave.md)

[removeOnPostSave](removeOnPostSave.md) 

