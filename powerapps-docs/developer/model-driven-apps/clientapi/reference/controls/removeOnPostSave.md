---
title: "removeOnPostSave (Client API reference) in model-driven apps| MicrosoftDocs"
description: Includes description and supported parameters for the removeOnPostSave method.
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
# removeOnPostSave (Client API reference)

Removes the event handler from the [PostSave](../events/postsave.md) event.

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

