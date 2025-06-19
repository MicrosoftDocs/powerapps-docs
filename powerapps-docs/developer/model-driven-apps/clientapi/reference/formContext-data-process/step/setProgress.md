---
title: "setProgress (Client API reference) in model-driven apps"
description: Includes description and supported parameters for the setProgress method.
author: matthidinger
ms.author: mahiding
ms.date: 03/12/2022
ms.reviewer: jdaly
ms.topic: reference
applies_to: "Dynamics 365 (online)"
search.audienceType: 
  - developer
contributors:
  - JimDaly
---
# setProgress (Client API reference)

[!INCLUDE[./includes/setProgress-description.md](./includes/setProgress-description.md)]

## Syntax

`stepObj.setProgress(stepProgress,message);`

## Parameters

|Name|Type|Required|Description|
|---|---|---|---|
|`stepProgress`|Number|Yes|Specify one of the following values to specify the step progress:<br />0: None<br />1: Processing<br />2: Completed<br />3: Failure<br />4: Invalid|
|`message`|String|No|An optional message that is set as the Alt text on the icon for the step.|

## Return Value

**Type**: String. 

**Description**: Returns `invalid` or `success` depending on whether the step progress was updated.

## Remarks

This method is supported only for the action steps. Action steps are buttons on the business process stages that users can click to trigger an on-demand workflow or action. Action step is a preview feature introduced in the v9.0 release. More information: See the **Business Process Flow automation with Action Steps** section in [Blog: New automation and visualization features for Business Process Flows (public preview)](https://blogs.msdn.microsoft.com/crm/2017/10/25/new-automation-and-visualization-features-for-business-process-flows-public-preview/).

### Related articles

[getProgress](getprogress.md)   
[formContext.data.process](../../formContext-data-process.md)

[!INCLUDE[footer-include](../../../../../../includes/footer-banner.md)]
