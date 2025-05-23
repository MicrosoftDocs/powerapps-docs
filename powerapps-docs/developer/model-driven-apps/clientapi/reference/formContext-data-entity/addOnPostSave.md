---
title: "addOnPostSave (Client API reference) in model-driven apps"
description: Includes description and supported parameters for the addOnPostSave method.
author: MitiJ
ms.author: mijosh
ms.date: 03/12/2022
ms.reviewer: jdaly
ms.topic: reference
applies_to: "Dynamics 365 (online)"
search.audienceType: 
  - developer
contributors:
  - JimDaly
---
# addOnPostSave (Client API reference)

[!INCLUDE [addonpostsave-description](includes/addonpostsave-description.md)]

[!INCLUDE [online-only-api-note](../../includes/online-only-api-note.md)]

## Syntax

```javascript
formContext.data.entity.addOnPostSave(myFunction);
```

### Parameter

|Name|Type|Required|Description|
|------|-----|------|----------|
|`myFunction`|function reference|Yes|The function to be added to the `PostSave` event after the record is saved with success or failure.|

### Related articles

[PostSave event](../events/postsave.md)   
[removeOnPostSave](removeOnPostSave.md) 

