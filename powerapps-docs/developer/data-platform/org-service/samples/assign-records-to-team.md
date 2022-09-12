---
title: " Assign a record to a team (Microsoft Dataverse) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "This sample showcases how to assign records to a team." # 115-145 characters including spaces. This abstract displays in the search result.
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

# Assign a record to a team

This sample shows how to assign a record to a team by using the [AssignRequest](/dotnet/api/microsoft.crm.sdk.messages.assignrequest) message.

You can download the sample from [here](https://github.com/microsoft/PowerApps-Samples/tree/master/dataverse/orgsvc/C%23/AssignRecordToTeam).

## How to run this sample

[!include[cc-how-to-run-samples](../../includes/cc-how-to-run-samples.md)]

## What this sample does

The [AssignRequest](/dotnet/api/microsoft.crm.sdk.messages.assignrequest) message is intended to be used in a scenario where it contains the data that is needed to assign the specified record to a new owner (user or team) by changing the OwnerId column of the record.

## How this sample works

In order to simulate the scenario described in [What this sample does](#what-this-sample-does), the sample will do the following:

### Setup

1. Checks for the current version of the org.
1. Creates required data that this sample requires.

### Demonstrate

The `AssignRequest` message assigns the account record created for the sample to a team.

### Clean up

Displays an option to delete all the data created in the sample. The deletion is optional in case you want to examine the data created by the sample. You can manually delete the data to achieve same results.

[!INCLUDE[footer-include](../../../../includes/footer-banner.md)]
