---
title: "Sample: Make a report available or unavailable to organization (Microsoft Dataverse) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "This sample shows how to make a report available or unavailable to an organization.." # 115-145 characters including spaces. This abstract displays in the search result.
ms.date: 04/03/2022
author: JimDaly #TODO: No Owner
ms.author: jdaly
ms.reviewer: pehecke
ms.topic: sample
search.audienceType:
  - developer
contributors:
  - JimDaly
  - phecke
---

# Sample: Make a report available or unavailable to organization

This sample shows how to make a report available or unavailable to an organization.

> [!div class="nextstepaction"]
> [SDK for .NET: Make a report available or unavailable to organization sample code](https://github.com/microsoft/PowerApps-Samples/tree/master/dataverse/orgsvc/C%23/MakeReportAvailableToOrganization)

## How to run this sample

[!include[cc-how-to-run-samples](../../includes/cc-how-to-run-samples.md)]

## How this sample works

In order to simulate the scenario described above, the sample will do the following:

### Setup

1. Checks for the current version of the org.
2. The `CreateRequiredRecords` method creates records that this sample requires.

### Demonstrate

1. The `service.Retrieve` method retrieves existing personal report.
2. Set `IsPersonal` parameter to false.
3. The `service.Update` method makes the report available for the organization.
4. Set `IsPersonal` parameter to true. This makes the report unavailable for the organization.

### Clean up

Display an option to delete the sample data that is created in [Setup](#setup). The deletion is optional in case you want to examine the tables and data created by the sample. You can manually delete the records to achieve the same result.

[!INCLUDE[footer-include](../../../../includes/footer-banner.md)]
