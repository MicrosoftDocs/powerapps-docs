---
title: "Sample: Query and detect table definitions changes (Microsoft Dataverse) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "This sample shows how to  query and detect table definitions changes" # 115-145 characters including spaces. This abstract displays in the search result.
ms.custom: ""
ms.date: 05/08/2020
ms.reviewer: "nabuthuk"
ms.service: powerapps
ms.topic: "article"
author: "JimDaly" # GitHub ID
ms.author: "jdaly" # MSFT alias of Microsoft employees only
manager: "ryjones" # MSFT alias of manager or PM counterpart
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---

# Query and detect table definitions changes


[!INCLUDE[cc-data-platform-banner](../../../../includes/cc-data-platform-banner.md)]

This sample shows how to retrieve and detect changes in table definitions using [RetrieveMetadataChangeRequest](/dotnet/api/microsoft.xrm.sdk.messages.retrievemetadatachangesrequest?view=dynamics-general-ce-9) method. You can download the sample from [here](https://github.com/microsoft/PowerApps-Samples/tree/master/cds/orgsvc/C%23/MetadataQuery).

[!INCLUDE[cc-terminology](../../includes/cc-terminology.md)]

## How to run this sample

[!include[cc-how-to-run-samples](../../includes/cc-how-to-run-samples.md)]

## What this sample does

The `RetrieveMetadataChangeRequest` message is intended to be used in a scenario where it contains the data  that is needed to retrieve a collection of table definitions records that satisfy the specified criteria. The [RetrieveMetadataChangesResponse](/dotnet/api/microsoft.xrm.sdk.messages.retrievemetadatachangesresponse?view=dynamics-general-ce-9) returns a timestamp value that can be used with this request at a later time to return information about how table definitions have changed since the last request.

## How this sample works

To simulate the scenario described in [What this sample does](#what-this-sample-does), the sample will do the following:

### Setup

Checks for the current version of the org.

### Demonstrate

1. The `MetadataFilterExpression` method creates the filter expression to limit tables returned to non-intersect, user-owned tables not found in the list of excluded tables. 
2. The `MetadataConditionExpression` method returns the choice column.
3. The `MetadataPropertiesExpression` method limits the properties to be included with the columns.
4. The `LabelQueryExpression` method limits the labels returned to only those for user's preferred language.
5. The `RetrieveMetadataChangeRequest` method retrieves the table definitions for the query.


### Clean up

Display an option to delete the sample data that is created in [Setup](#setup). The deletion is optional in case you want to examine the tables and data created by the sample. You can manually delete the records to achieve the same result.


[!INCLUDE[footer-include](../../../../includes/footer-banner.md)]