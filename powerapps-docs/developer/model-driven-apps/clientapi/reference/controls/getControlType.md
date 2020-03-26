---
title: "getControlType (Client API reference) in model-driven apps for Dynamics 365| MicrosoftDocs"
ms.date: 10/31/2018
ms.service: powerapps
ms.topic: "reference"
applies_to: "Dynamics 365 (online)"
ms.assetid: 4d025f92-db16-440c-9f82-e40d71e09862
author: "KumarVivek"
ms.author: "kvivek"
manager: "annbe"
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---
# getControlType (Client API reference)



Returns a value that categorizes controls.

## Control Types supported

All

## Syntax

`getControl(arg).getControlType();`

**Return Value**:

**Type**: String

|Return Value |Decsription|
|--|--|
|standard|A standard control|
|iframe|An IFRAME control|
|kbsearch|A knowledge base search control|
|lookup|A lookup control|
|multiselectoptionset|A multi-select option set control|
|notes|A notes control|
|optionset|An option set control|
|quickform | A [quick view](../formContext-ui-quickForms.md) control|
|subgrid | A [subgrid](../grids.md) control|
|timercontrol | A timer control|
|timelinewall | A timeline control (for Unified Interface)|
|webresource | A web resource control|
|customcontrol: \<*namespace*>.\<*name*> | A custom control for Dynamics 365 mobile clients (phones and tablets)|
|customsubgrid:\<*namespace*>.\<*name*> | A custom dataset control for Dynamics 365 mobile clients (phones and tablets)|

### Related topics

[Controls](../controls.md)

[getControl](getcontrol.md)


