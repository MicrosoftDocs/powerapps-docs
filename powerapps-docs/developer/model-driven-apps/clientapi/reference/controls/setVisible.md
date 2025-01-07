---
title: "control.setVisible (Client API reference) in model-driven apps"
description: Includes description and supported parameters for the control.setVisible method.
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
# control.setVisible (Client API reference)

Sets a value that indicates whether the control is visible. 

## Control types supported

All

## Syntax

`formContext.getControl(arg).setVisible(bool);`

## Parameter

|Name|Type|Required|Description|
|----|----|----|----|
|`bool`|Boolean|Yes|Specify **true** to show the control; **false** to hide the control.|

>[!NOTE]
> If a control is set to false and is in a section that is hidden and if you set the control to true, the section will be visible.

>[!NOTE]
> If a control bound to a Business Required column is set to not be visible, the form will no longer require it to have a value before saving. See [Column requirement level](../../../../data-platform/entity-attribute-metadata.md#column-requirement-level) for more information.

### Related articles

[getVisible](getVisible.md)


[!INCLUDE[footer-include](../../../../../includes/footer-banner.md)]
