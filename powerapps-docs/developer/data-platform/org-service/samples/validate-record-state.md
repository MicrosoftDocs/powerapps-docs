---
title: " Validate and set record state (Microsoft Dataverse) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "This sample showcases how to validate a change of state of a table and set state." # 115-145 characters including spaces. This abstract displays in the search result.
ms.custom: ""
ms.date: 12/20/2019
ms.reviewer: "pehecke"
ms.service: powerapps
ms.topic: "samples"
author: "JimDaly" # GitHub ID
ms.author: "jdaly" # MSFT alias of Microsoft employees only
manager: "ryjones" # MSFT alias of manager or PM counterpart
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---

# Validate record state and set the state of record

[!INCLUDE[cc-data-platform-banner](../../../../includes/cc-data-platform-banner.md)]

This sample shows how to validate a change of state of a table and set a state of a table. You can download the sample from [here](https://github.com/microsoft/PowerApps-Samples/tree/master/cds/orgsvc/C%23/ValidateAndSetRecordState).

## How to run this sample

[!include[cc-how-to-run-samples](../../includes/cc-how-to-run-samples.md)]

## What this sample does

The `IsValidStateTransitionRequest` message is intended to be used in a scenario where it contains the data that is needed to validate the state transition.

## How this sample works

In order to simulate the scenario described in [What this sample does](#what-this-sample-does), the sample will do the following:

### Setup

1. Checks for the current version of the org.
2. The `CreateRequiredRecords` method creates any table records that this sample requires.

### Demonstrate

1. The `EntityReference` method creates a EntityReference to represent open case. 
2. The `IsValidStateTransitionRequest`  method sets the transition request to an open case.
3. The `checkState.NewState` property checks if a new state of resolved and a new state of problem solved are valid.
4. The `IsValidStateTransitionResponse` method executes the request.

### Clean up

Display an option to delete the sample data that is created in [Setup](#setup). The deletion is optional in case you want to examine the tables and data created by the sample. You can manually delete the records to achieve the same result.



[!INCLUDE[footer-include](../../../../includes/footer-banner.md)]