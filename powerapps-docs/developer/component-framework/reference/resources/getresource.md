---
title: getResource (Power Apps component framework API reference) | Microsoft Docs
description: Provides information about the methods available for getResource.
ms.author: noazarur
author: noazarur-microsoft
ms.date: 05/27/2022
ms.reviewer: jdaly
ms.topic: reference
ms.subservice: pcf
contributors:
 - JimDaly
---

# getResource

[!INCLUDE [getresource-description](includes/getresource-description.md)]

## Available for 

Model-driven apps

## Syntax

`context.resources.getResource(id, success, failure)`

## Parameters

| Parameter Name|Type|Required|Description|
| ------------- |----|--------|-----------|
|id|`String`|Yes|The resource string identifier.|
|success|`function (string) => void`|No|The success callback. Resource data is returned in base 64 encoded format.|
|failure|`function () => void`|No|The failure callback.|

### Example

```TypeScript
 private setDefaultImage(): void {
    this._context.resources.getResource(
      DefaultImageFileName,
      this.setImage.bind(this, false, "png"),
      this.showError.bind(this)
    );
    this.controlContainer.classList.add(NoImageClassName);
    // If it already has value, we need to update the output
    if (this._context.parameters.value.raw) {
      this._value = null;
      this._notifyOutputChanged();
    }
  }
```

### Related articles

[Resources](../resources.md)<br/>
[Power Apps component framework API reference](../../reference/index.md)<br/>
[Power Apps component framework overview](../../overview.md)

[!INCLUDE[footer-include](../../../../includes/footer-banner.md)]
