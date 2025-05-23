---
title: "control.setDisabled (Client API reference) in model-driven apps"
description: Includes description and supported parameters for the control.setDisabled method.
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
# control.setDisabled (Client API reference)

Sets whether the control is disabled.

## Control types supported

All except **kbsearch** control type

## Syntax

`formContext.getControl(arg).setDisabled(bool);`

## Parameter

|Name|Type|Required|Description|
|--|--|--|--|
|`bool`|Boolean|Yes|Specify **true** or **false** to disable or enable the control.|

> [!NOTE]
> If a control bound to a Business Required column is set to be disabled, the form will no longer require it to have a value before saving. See [Column requirement level](../../../../data-platform/entity-attribute-metadata.md#column-requirement-level) for more information.

### Related articles

[getDisabled](getDisabled.md)

[!INCLUDE[footer-include](../../../../../includes/footer-banner.md)]
