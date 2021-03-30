---
title: "Sample: Validate and execute saved query(Microsoft Dataverse) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "This sample shows how to validate and execute a saved query." # 115-145 characters including spaces. This abstract displays in the search result.
ms.custom: ""
ms.date: 10/31/2018
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
# Sample: Validate and execute a saved query

[!INCLUDE[cc-data-platform-banner](../../../../includes/cc-data-platform-banner.md)]

<!-- Needs supporting conceptual topic 
https://docs.microsoft.com/dynamics365/customer-engagement/developer/org-service/sample-validate-execute-saved-query
-->
This sample shows how to use the [IOrganizationService.ValidateSavedQueryRequest](/dotnet/api/microsoft.crm.sdk.messages.validatesavedqueryrequest?view=dynamics-general-ce-9) message to validate a FetchXML query, and then use the [IOrganizationService.ExecuteByIdSavedQueryRequest](/dotnet/api/microsoft.crm.sdk.messages.executebyidsavedqueryrequest?view=dynamics-general-ce-9) message to execute the query. You can download the sample from [here](https://github.com/Microsoft/PowerApps-Samples/tree/master/cds/orgsvc/C%23/ValidateandExecuteSavedQuery).

## How to run this sample

[!include[cc-how-to-run-samples](../../includes/cc-how-to-run-samples.md)]


## What this sample does

The `ValidateSavedQueryRequest` class is intended to be used in a scenario where it contains the data that is needed to validate a saved query (view). 

The `ExecuteByIdSavedQueryRequest` class is intended to be used in a scenario where it contains data that is needed to execute a saved query (view) that has the specified ID.

## How this sample works

In order to simulate the scenario described in [What this sample does](#what-this-sample-does), the sample will do the following:

### Setup

1. Checks for the current version of the org.
1. The `Account` method creates 3 account records.
1. The `SavedQuery` method creates a Saved query.
1. The `UserQuery` method creates a User query.


### Demonstrate
1. The `ValidateSavedQueryRequest` method creates the validate request.
1. The `ExecuteByIdSavedQueryRequest` method executes the saved query.

### Clean up

Displays an option to delete all the data created in the sample. The deletion is optional in case you want to examine the data created by the sample. You can manually delete the data to achieve same results.


[!INCLUDE[footer-include](../../../../includes/footer-banner.md)]