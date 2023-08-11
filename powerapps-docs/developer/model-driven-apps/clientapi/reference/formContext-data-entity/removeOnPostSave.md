---
title: "removeOnPostSave (Client API reference) in model-driven apps| MicrosoftDocs"
description: Includes description and supported parameters for the removeOnPostSave method.
author: HemantGaur
ms.author: hemantg
ms.date: 03/12/2022
ms.reviewer: jdaly
ms.topic: reference
applies_to: "Dynamics 365 (online)"
search.audienceType: 
  - developer
contributors:
  - JimDaly
---
# removeOnPostSave (Client API reference)

[!INCLUDE [removeonpostsave-description](includes/removeonpostsave-description.md)]

[!INCLUDE [online-only-api-note](../../includes/online-only-api-note.md)]

## Syntax

```javascript
formContext.data.entity.removeOnPostSave(myFunction);
```

### Parameter

|Name|Type|Required|Description|
|------|-----|------|----------|
|myFunction|function reference|Yes|The function to be removed from the `PostSave` event.|

### See also

[PostSave event](../events/postsave.md)

[addOnPostSave](addOnPostSave.md) 

