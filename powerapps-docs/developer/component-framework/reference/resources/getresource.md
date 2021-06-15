---
title: getResource | Microsoft Docs
description: Provides information about the methods available for getResource.
keywords:
ms.author: nabuthuk
author: Nkrb
manager: kvivek
ms.date: 10/01/2019
ms.service: "powerapps"
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: 5c04ba7c-acfe-4375-8dd8-6c537ded9352
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

### Related topics

[Resources](../resources.md)<br/>
[Power Apps component framework API reference](../../reference/index.md)<br/>
[Power Apps component framework overview](../../overview.md)

[!INCLUDE[footer-include](../../../../includes/footer-banner.md)]