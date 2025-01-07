---
title: "openSearchResult (Client API reference) in model-driven apps"
description: Includes description and supported parameters for the openSearchResult method.
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
# openSearchResult (Client API reference)

Opens a search result in the search control by specifying the result number.

## Control types supported

knowledge base search control

## Syntax

```JavaScript
var kbSearchControl = formContext.getControl("<name>");
var openResultStatus = kbSearchControl.openSearchResult(resultNumber, mode);
```

## Parameter

|Name|Type|Required|Description|
|--|--|--|--|
|`resultNumber`|Number|Yes|Numerical value specifying the result number to be opened. Result number starts from 1.|
|`mode`|String|No|Specify "Inline" or "Popout". If you do not specify a value for the argument, the default ("Inline") option is used.<br/><br/>The "Inline" mode opens the result inline either in the reading pane of the control or in a reference panel tab in case of reference panel. The "Popout" mode opens the result in a pop-out window.|

## Return Value

**Type**: Boolean

**Description**:  Status of opening the specified search result. Returns 1 if successful; 0 if unsuccessful. The method will return -1 if the specified resultNumber value is not present, or if the specified mode value is invalid.

[!INCLUDE[footer-include](../../../../../includes/footer-banner.md)]
