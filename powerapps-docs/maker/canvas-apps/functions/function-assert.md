---
title: Assert function | Microsoft Docs
description: Reference information, including syntax, for the Assert function in Power Apps Test Studio
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
# Assert function in Power Apps Test Studio

An assertion is a condition or an expression that evaluates to true or false in a test. If the expression returns false, the test case will fail. Assertions are used to validate the expected result of a test or test step, against the actual result and to fail the test if the condition is false. 

## Syntax

*Assert(expression, message)*

- *Expression* – Required. An expression that evaluates to true or false.
- *Message* – Not Required. A message that describes the assertion failure. 


## Example

```Assert(kudosAfterTest = kudosBeforeTest + 1, "Kudos count incorrect. Expected : " & kudosBeforeTest + 1  & " Actual :" & kudosAfterTest)```

### See Also

[Test Studio Overview](../test-studio.md) <br>
[Working with Test Studio](../working-with-test-studio.md)
