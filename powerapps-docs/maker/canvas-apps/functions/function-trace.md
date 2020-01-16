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
# Trace function 

When used with Test Studio, Trace is an optional expression that can be used to provide additional information in your test results from the **OnTestCaseComplete** event. Trace event messages, as well as any messages for both passed and failed assertions, are contained in a Traces table in the TestCaseResult record. The Traces table has two properties, Message and Timestamp. 

If you have allowed your app to send telemetry data to Azure Application Insights, the Trace function can also be used to send custom event or diagnostic information to your Application Insights resource. You can inspect this data in Application Insights to help diagnose problems or understand usage of your apps and features. Trace information used in Tests will also be recorded in Application Insights. All Trace messages can also be viewed in the Power Apps Monitor tool, which will help in debugging or identifying issues for real-time diagnostic sessions for your app.   

## Syntax

*Trace(message, severity, custom_record )*

- *Message* – Required. The information to be traced. In tests, this creates a record in the Traces table in the TestCaseResult record. 
- *Severity* - Optional. The severity level of the Trace recorded in Application Insights. Options are Information, Warning or Error. 
- *custom_record* - Optional. A record containing custom data that will be recorded in Application Insights. 
  

### See Also

[Test Studio Overview](../test-studio.md) <br>
[Working with Test Studio](../working-with-test-studio.md)
