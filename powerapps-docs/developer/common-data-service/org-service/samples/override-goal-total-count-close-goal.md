---
title: "Sample: Override goal total count and close the goal (Common Data Service for Apps) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "This sample shows how to override the goal total count and close the goal." # 115-145 characters including spaces. This abstract displays in the search result.
ms.custom: ""
ms.date: 08/01/2018
ms.reviewer: ""
ms.service: "powerapps"
ms.topic: "samples"
author: "brandonsimons" # GitHub ID
ms.author: "jdaly" # MSFT alias of Microsoft employees only
manager: "ryjones" # MSFT alias of manager or PM counterpart
---
# Sample: Override goal total count and close the goal

<!-- https://docs.microsoft.com/en-us/dynamics365/customer-engagement/developer/sample-override-goal-total-count-close-goal -->

This sample shows how to override the goal total count and close the goal.

This sample requires additional users that are not in your system. Create the required user **as is** shown below manually in **Office 365**. 

**First Name**: Samantha<br/>
**Last Name**: Smith<br/>
**Security Role**: Marketing Manager<br/>
**UserName**: ssmith@yourorg.onmicrosoft.com<br/>

## How to run this sample

[!include[cc-how-to-run-samples](../../includes/cc-how-to-run-samples.md)]

## What this sample does


This sample shows how to override the goal total count and close the goal.

## How this sample works

In order to simulate the scenario described in [What this sample does](#what-this-sample-does), the sample will do the following:

### Setup

1. Checks for the version of the org.
2. Retrieves the sales manager user created manually in **Office 365**.
3. Creates a `PhoneCall` record and supporting account record for the sample.
4. Creates ActivityPartys for the phone calls "From" field.
5. Creates an open phone call.
6. Closes the first phone call and creates a second one.
7. Closes the second phone call.

### Demonstrate

1. Creates Metric, and setting the Metric type to `count` and also setting `IsAmount` to false.
2. The `RollupFields` creates a rollup field which targets completed (received) phone calls.
3. The `GoalRollupQuery` creates the goal rollup queries, locating the incoming and outgoing closed phone calls. 
4. Creates a goal to track the open incoming phone calls.
5. The `RecalculateRequest` calculates the rollup for goals. 
6. Overrides the actual and in-progress values of the goal.
7. Set `goal.IsOverridden =true` prevents the rollup values to be overwritten during the next recalculate operation.

### Clean up

1. Display an option to delete the sample data created in [Setup](#setup).

    The deletion is optional in case you want to examine the entities and data created by the sample. You can manually delete the records to achieve the same result.
