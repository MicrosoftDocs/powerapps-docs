---
title: "Assign dashboard to another user (Microsoft Dataverse) | Microsoft Docs"
description: "This sample showcases how to assign a user-owned dashboard to another user " 
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

# Assign a user-owned dashboard to another user

This sample shows how to use the [AssignRequest](/dotnet/api/microsoft.crm.sdk.messages.assignrequest) class to assign a user-owned visualization to another user. Because you can't delete a user-owned dashboard that is assigned to another user, this sample shows how to use impersonation to delete the user-owned dashboard.

> [!div class="nextstepaction"]
> [SDK for .NET: Assign a user-owned dashboard to another user sample code](https://github.com/microsoft/PowerApps-Samples/tree/master/dataverse/orgsvc/CSharp/AssignUserOwnedDashboardToAnother)

[!INCLUDE[cc-terminology](../../includes/cc-terminology.md)]

This sample requires an additional user that isn't available in your system. Create the required user manually in **Microsoft 365** to run the sample without any errors. For this sample, create a user profile **as is** shown below.

**First Name**: Kevin<br/>
**Last Name**: Cook<br/>
**Security Role**: Sales Manager<br/>
**UserName**: `kcook@yourorg.onmicrosoft.com`<br/>

## How to run this sample

[!include[cc-how-to-run-samples](../../includes/cc-how-to-run-samples.md)]

## What this sample does

Use the [AssignRequest](/dotnet/api/microsoft.crm.sdk.messages.assignrequest) class when you need to assign a specified record to a new owner (user or team). The class contains the data needed to change the `OwnerId` column of the record.

## How this sample works

To simulate the scenario described in [What this sample does](#what-this-sample-does), the sample performs the following steps:

### Setup

1. Check for the current version of the org.
1. Use the `CreateRequiredRecords` method to create the table records that this sample requires.
1. Use the `mySavedQuery` query to grab the default public view for the opportunities.
1. Use the `visualizationQuery` query to retrieve the visualizations out of the system. This sample assumes that you have the **Top opportunities** visualization.
1. Use the `_otherUSerId` method to create the user to whom the dashboard will be assigned.

### Demonstrate

Use the `AssignRequest` class to assign the visualization or chart to the newly created user.

### Clean up

Display an option to delete the sample data in [Setup](#setup). The deletion is optional in case you want to examine the tables and data created by the sample. You can manually delete the records to achieve the same result.

[!INCLUDE[footer-include](../../../../includes/footer-banner.md)]
