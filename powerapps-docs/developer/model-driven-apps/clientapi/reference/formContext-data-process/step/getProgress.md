---
title: "getProgress (Client API reference) in Dynamics 365 Customer Engagement| MicrosoftDocs"
ms.date: 11/20/2017
ms.service: "crm-online"
ms.topic: "reference"
applies_to: "Dynamics 365 (online)"
ms.assetid: 56502c8b-af23-40d1-ad97-e780bb757d6d
author: "KumarVivek"
ms.author: "kvivek"
manager: "amyla"
---
# getProgress (Client API reference)



[!INCLUDE[./includes/getProgress-description.md](./includes/getProgress-description.md)]

## Syntax

`var stepProgress = stepObj.getProgress();`

## Return Value

**Type**: Number. 

**Description**: Returns one of the following values:

|Value |Description|
|--|--|
|0|None|
|1|Processing|
|2|Completed|
|3|Failure|
|4|Invalid|

## Remarks

This method is supported only for the action steps; not for the data steps. Action steps are buttons on the business process stages that users can click to trigger an on-demand workflow or action. Action step is a preview feature introduced in the [!INCLUDE[pn_crm_9_0_0_online](../../../../../includes/pn-crm-9-0-0-online.md)] release. More information: See the **Business Process Flow automation with Action Steps** section in [Blog: New automation and visualization features for Business Process Flows (public preview)](https://blogs.msdn.microsoft.com/crm/2017/10/25/new-automation-and-visualization-features-for-business-process-flows-public-preview/)

### Related topics

[setProgress](setprogress.md)

[formContext.data.process](../../formContext-data-process.md)
 


