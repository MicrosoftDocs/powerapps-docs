---
title: "Sample: Create a basic plug-in (Microsoft Dataverse) | Microsoft Docs"
description: "Learn how to write a simple plug-in that creates a follow-up activity."
ms.date: 04/03/2022
author: divka78
ms.author: dikamath
manager: sunilg
ms.reviewer: pehecke
ms.topic: sample
search.audienceType:
  - developer
search.app:
  - PowerApps
  - D365CE
contributors:
  - JimDaly
  - phecke
---

# Sample: Create a basic plug-in

[!INCLUDE[cc-terminology](../../includes/cc-terminology.md)]

This sample shows how to write a simple plug-in that creates a follow-up activity. You can download the sample from [here](https://github.com/microsoft/PowerApps-Samples/tree/master/dataverse/orgsvc/C%23/FollowupPlugin).

## How to run this sample

1. Download or clone the [Samples](https://github.com/Microsoft/PowerApps-Samples) repo so that you have a local copy. This sample is located under PowerApps-Samples-master\cds\orgsvc\C#\FollowupPlugin.
2. Open the sample solution in Visual Studio, navigate to the project's properties, and verify the assembly will be signed during the build. Press F6 to build the sample's assembly (FollowupPlugin.dll).
3. Run the Plug-in Registration tool and register the sample's assembly in the D365 server's sandbox and database. When registering a step, specify the Create message, account table, and asynchronous mode.
4. Using the D365 app, perform the appropriate operation to invoke the message and table request that you registered the plug-in on (create an account).
5. After the plug-in runs, you should see a new trace log entry "FollowupPlugin: Successfully created the task activity" and a new activity with the subject "Send e-mail to the new customer." that is scheduled to activate in 7 days.
6. When you are done testing, unregister the assembly and step.

## What this sample does

When executed upon creation of an account, the plug-in creates an activity to remind the user to follow-up with the account customer in 7 days.

## How this sample works

In order to simulate the scenario described in [What this sample does](#what-this-sample-does), the sample will do the following:

### Demonstrate

1. How to create a task activity and schedule it for a future date.
2. How to use the tracing service to log run-time information.
3. How to catch exceptions from the web service and process it.

### See also

[Write a plug-in](../../write-plug-in.md)  
[Register a plug-in](../../register-plug-in.md)

[!INCLUDE[footer-include](../../../../includes/footer-banner.md)]
