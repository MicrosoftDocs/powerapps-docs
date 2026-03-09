---
title: " Assign chart to another user (Microsoft Dataverse) | Microsoft Docs"
description: "This sample showcases how to assign a user-owned visualization to another user " 
ms.date: 03/04/2026
author: MsSQLGirl
ms.author: jukoesma
ms.reviewer: jdaly
ms.topic: sample
search.audienceType:
  - developer
contributors:
  - JimDaly
  - phecke
---

# Assign a chart to another user

This sample shows how to assign a user-owned visualization to another user by using the [AssignRequest](/dotnet/api/microsoft.crm.sdk.messages.assignrequest) class.

> [!div class="nextstepaction"]
> [SDK for .NET: Assign a chart to another user sample code](https://github.com/microsoft/PowerApps-Samples/tree/master/dataverse/orgsvc/CSharp/AssignChartToAnotherUser)

[!INCLUDE[cc-terminology](../../includes/cc-terminology.md)]

This sample requires an additional user that isn't available in your system. Create the required user manually in **Microsoft 365** to run the sample without any errors. For this sample, create a user profile **as is** shown below.

**First Name**: Kevin<br/>
**Last Name**: Cook<br/>
**Security Role**: Sales Manager<br/>
**UserName**: `kcook@yourorg.onmicrosoft.com`<br/>

## How to run this sample

[!include[cc-how-to-run-samples](../../includes/cc-how-to-run-samples.md)]

## What this sample does

Use the [AssignRequest](/dotnet/api/microsoft.crm.sdk.messages.assignrequest) class to assign the specified record to a new owner (user or team). The operation changes the `OwnerId` column of the record.

## How this sample works

To simulate the scenario described in [What this sample does](#what-this-sample-does), the sample performs the following steps:

### Setup

1. Checks for the current version of the org.
2. The `CreateRequiredRecords` method creates a sample account and some opportunity records for the visualization.
3. The `newUserOwnedVisualization` method creates the visualization record.

### Demonstrate

The `AssignRequest` method assigns the visualization or chart to the new user.

### Clean up

Display an option to delete the sample data in [Setup](#setup). You can choose whether to delete this data. If you want to examine the tables and data created by the sample, you don't need to delete it. You can also manually delete the records.

[!INCLUDE[footer-include](../../../../includes/footer-banner.md)]
