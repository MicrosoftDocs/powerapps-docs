---
title: "Sample: Retrieve absolute URL and site collection URL(Common Data Service for Apps) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "This sample shows how to retrieve the absolute URL and site collection URL of a SharePoint location" # 115-145 characters including spaces. This abstract displays in the search result.
ms.custom: ""
ms.date: 08/01/2018
ms.reviewer: ""
ms.service: "powerapps"
ms.topic: "samples"
author: "brandonsimons" # GitHub ID
ms.author: "jdaly" # MSFT alias of Microsoft employees only
manager: "ryjones" # MSFT alias of manager or PM counterpart
---
# Sample: Retrieve absolute URL and site collection URL of a location record

<!-- https://docs.microsoft.com/en-us/dynamics365/customer-engagement/developer/integration-dev/sample-retrieve-absolute-url-and-site-collection-url-of-a-location-record -->

This sample shows how to retrieve the absolute URL and the site collection URL of a SharePoint Server location record using the [RetrieveAbsoluteAndSiteCollectionUrlRequest](https://docs.microsoft.com/en-us/dotnet/api/microsoft.crm.sdk.messages.retrieveabsoluteandsitecollectionurlrequest?view=dynamics-general-ce-9) message.

## How to run this sample

[!include[cc-how-to-run-samples](../../includes/cc-how-to-run-samples.md)]

## What this sample does

The `RetrieveAbsoluteAndSiteCollectionUrlRequest` messages is intended to be used in a scenario that contains data that is needed to retrieve the absolute URL nd the site collection URL for a SharePoint location record.

## How this sample works

In order to simulate the scenario described in [What this sample does](#what-this-sample-does), the sample will do the following:

### Setup

1. Checks for the current version of the org. 
1. The `CreateRequireRecords` method creates entity records that are used by the sample.

### Demonstrate

1. The `RetrieveAbsoluteAndSiteCollectionUrlRequest` is used to retrieve the absolute URL and site collection URL of the SharePoint record.

### Clean up

1. Display an option to delete the records created in the [Setup](#setup).

    The deletion is optional in case you want to examine the entities and data created by the sample. You can manually delete the records to achieve the same result.
