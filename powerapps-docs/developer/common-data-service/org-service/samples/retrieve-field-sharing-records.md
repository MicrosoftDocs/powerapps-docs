---
title: "Sample: Retrieve field sharing records (Common Data Service for Apps) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "This sample shows how to retreive the field sharing records for an entity." # 115-145 characters including spaces. This abstract displays in the search result.
ms.custom: ""
ms.date: 08/01/2018
ms.reviewer: ""
ms.service: "powerapps"
ms.topic: "samples"
author: "brandonsimons" # GitHub ID
ms.author: "jdaly" # MSFT alias of Microsoft employees only
manager: "ryjones" # MSFT alias of manager or PM counterpart
---
# Sample: Retrieve field sharing records

<!-- https://docs.microsoft.com/en-us/dynamics365/customer-engagement/developer/sample-retrieve-field-sharing-records -->

This sample shows how to retrieve the `PrincipalObjectAttributeAccess` (field sharing) records for an entity. You can download the sample from [here](https://github.com/Microsoft/PowerApps-Samples/tree/master/cds/orgsvc/C%23/RetrieveFieldSharing).

## How to run this sample

[!include[cc-how-to-run-samples](../../includes/cc-how-to-run-samples.md)]

## What this sample does

The `PrincipleObjectAttributeAccess` message is intended to be used in a scenario where it retrieves the field sharing records for an entity.

## How this sample works

In order to simulate the scenario described in [What this sample does](#what-this-sample-does), the sample will do the following:

### Setup

1. Checks for the current version of the org.
2. The `CreateAttributeRequest` method creates the custom fields required for the sample.

### Demonstrate

1. The `WhoAMIRequest` retrieves the current user's information.
2. The `RetrieveUserPrivilegesRequest` message checks if the current user has `prvReadPOAA`.
3. The `PrincipalObjectAttributeAccess` creates POAA entity for the custom fields created in the Setup(#setup).
4. Using the `QueryExpression` retrieve user shared attribute permissions.

### Clean up

1. Display an option to delete the sample data that is created in [Setup](#setup).

    The deletion is optional in case you want to examine the entities and data created by the sample. You can manually delete the records to achieve the same result.
