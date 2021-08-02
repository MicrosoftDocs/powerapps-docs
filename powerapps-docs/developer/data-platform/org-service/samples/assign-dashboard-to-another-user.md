---
title: " Assign dashboard to another user (Microsoft Dataverse) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "This sample showcases how to assign a user-owned dashboard to another user " # 115-145 characters including spaces. This abstract displays in the search result.
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

# Assign a user-owned dashboard to another user

[!INCLUDE[cc-data-platform-banner](../../../../includes/cc-data-platform-banner.md)]

This sample shows how to assign a user-owned visualization to another using the [AssignRequest](/dotnet/api/microsoft.crm.sdk.messages.assignrequest?view=dynamics-general-ce-9) message. Because you can’t delete a user-owned dashboard that is assigned to another user, this sample shows how to use impersonation to delete the user-owned dashboard. You can download the sample from [here](https://github.com/microsoft/PowerApps-Samples/tree/master/cds/orgsvc/C%23/AssignUserOwnedDashboardToAnother).

[!INCLUDE[cc-terminology](../../includes/cc-terminology.md)]

This sample requires an additional user that isn't available in your system. Create the required user manually in **Microsoft 365** in order to run the sample without any errors. For this sample create a user profile **as is** shown below. 

**First Name**: Kevin<br/>
**Last Name**: Cook<br/>
**Security Role**: Sales Manager<br/>
**UserName**: kcook@yourorg.onmicrosoft.com<br/>

## How to run this sample

[!include[cc-how-to-run-samples](../../includes/cc-how-to-run-samples.md)]

## What this sample does

The [AssignRequest](/dotnet/api/microsoft.crm.sdk.messages.assignrequest?view=dynamics-general-ce-9) message is intended to be used in a scenario where it contains the data that is needed to assign the specified record to a new owner (user or team) by changing the OwnerId column of the record.

## How this sample works

In order to simulate the scenario described in [What this sample does](#what-this-sample-does), the sample will do the following:

### Setup

1. Checks for the current version of the org.
2. The `CreateRequiredRecords` method creates table records that this sample requires.
3. The `mySavedQuery` method grabs the default public view for the opportunities.
4. The `visualizationQuery` method retrieves the visualizations out of the system. This sample assumes that you have the **Top opportunities**. 
5. The `_otherUSerId` method creates the user to whom the dashboard will be assigned.

### Demonstrate

The `AssignRequest` method assigns the visualization or chart to the newly created user.

### Clean up

Display an option to delete the sample data in [Setup](#setup). The deletion is optional in case you want to examine the tables and data created by the sample. You can manually delete the records to achieve the same result.


[!INCLUDE[footer-include](../../../../includes/footer-banner.md)]