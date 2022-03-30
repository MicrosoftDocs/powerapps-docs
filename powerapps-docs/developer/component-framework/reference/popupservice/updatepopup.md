---
title: updatePopup | Microsoft Docs
description: Updates an existing popup in the service with the given name. Does nothing if popup does not exist yet.
keywords:
ms.author: jdaly
author: noazarur-microsoft
manager: kvivek
ms.date: 03/12/2022
ms.reviewer: jdaly
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"

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