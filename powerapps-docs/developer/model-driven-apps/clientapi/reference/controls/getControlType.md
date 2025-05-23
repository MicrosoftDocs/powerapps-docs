---
title: "control.getControlType (Client API reference) in model-driven apps for Dynamics 365"
description: Includes  description and supported parameters for the getControlType method.
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
# control.getControlType (Client API reference)

Returns a value that categorizes controls.

## Control Types supported

All

## Syntax

`getControl(arg).getControlType();`

[!INCLUDE[cc-terminology](../../../../data-platform/includes/cc-terminology.md)]

**Return Value**:

**Type**: String

|Return Value |Description|
|----|----|
|standard|A standard control|
|iframe|An IFRAME control|
|kbsearch|A knowledge base search control|
|lookup|A lookup control|
|choices|A choices control|
|notes|A notes control|
|choice|A choice control|
|quickform | A [quick view](../formContext-ui-quickForms.md) control|
|formcomponent | A [form component control](../../../../../maker/model-driven-apps/form-component-control.md#client-api)|
|subgrid | A [subgrid](../grids.md) control|
|timercontrol | A timer control|
|timelinewall | A timeline control (for Unified Interface)|
|webresource | A web resource control|
|customcontrol: \<*namespace*>.\<*name*> | A custom control for Dynamics 365 mobile clients (phones and tablets)|
|customsubgrid:\<*namespace*>.\<*name*> | A custom dataset control for Dynamics 365 mobile clients (phones and tablets)|

### Related articles

[Controls](../controls.md)   
[getControl](getcontrol.md)

[!INCLUDE[footer-include](../../../../../includes/footer-banner.md)]
