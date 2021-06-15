---
title: updatePopup | Microsoft Docs
description: Updates an existing popup in the service with the given name. Does nothing if popup does not exist yet.
keywords:
ms.author: nabuthuk
author: Nkrb
manager: kvivek
ms.date: 10/01/2019
ms.service: "powerapps"
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: fd98d153-391d-41e6-ac9d-d2350a4791b9

---

# updatePopup

[!INCLUDE [updatepopup-description](includes/updatepopup-description.md)]

## Available for 

Model-driven apps

## Syntax

`updatePopup(name, newProps)`

## Parameters

| Parameter Name|Type|Required|Description|
| ------------- |----|--------|-----------|
|name|`String`|Yes|The name of the popup you're trying to update.|
|newProps|[Popup](../popup.md)|No|The updated properties to give to the popup.|


### Related topics

[Popup Service](../popupservice.md)<br/>
[Power Apps component framework API reference](../../reference/index.md)<br/>
[Power Apps component framework overview](../../overview.md)

[!INCLUDE[footer-include](../../../../includes/footer-banner.md)]