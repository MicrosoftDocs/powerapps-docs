---
title: Trace function | Microsoft Docs
description: Reference information, including syntax, for the Trace function in Power Apps Test Studio
author: tapanm-msft
manager: kvivek
ms.service: powerapps
ms.topic: reference
ms.custom: canvas
ms.reviewer: tapanm
ms.date: 12/19/2018
ms.author: aheneay
search.audienceType: 
  - maker
search.app: 
  - PowerApps
---
# Trace function in Power Apps Test Studio

Trace is an optional test expression that can be used to provide additional information in your test results from the **OnTestCaseComplete** event. Trace event messages, as well as any messages for both passed and failed assertions, are contained in a Traces table in the TestCaseResult record. The Traces table has two properties, Message and Timestamp. 

## Syntax

*Trace(message)*

- *Message* – Required. A text value that creates a record in the Traces table in the TestCaseResult record. 

### See Also

[Test Studio Overview](../test-studio.md) <br>
[Working with Test Studio](../working-with-test-studio.md)
