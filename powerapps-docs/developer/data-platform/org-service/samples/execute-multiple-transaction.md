---
title: "Sample: Execute multiple requests in transaction (Microsoft Dataverse) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "This sample shows how to execute multiple request in transaction." # 115-145 characters including spaces. This abstract displays in the search result.
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
# Sample: Execute multiple requests in transaction

[!INCLUDE[cc-data-platform-banner](../../../../includes/cc-data-platform-banner.md)]

This sample shows how to use a single web method call to execute all message requests in a collection as part of a single database transaction. It is a common requirement in business applications to coordinate changes of multiple records in the system so that either all the data changes succeed, or none of them do. In database terms, this is known as executing multiple operations in a single transaction with the ability to roll back all data changes should any one operation fail.

You can execute two or more organization service requests in a single database transaction using the [ExecuteTransactionRequest](/dotnet/api/microsoft.xrm.sdk.messages.executetransactionrequest?view=dynamics-general-ce-9) message request. 

You can download the sample from [here](https://github.com/microsoft/PowerApps-Samples/tree/master/cds/orgsvc/C%23/ExecuteMultipleInTransaction).

## How to run this sample

[!include[cc-how-to-run-samples](../../includes/cc-how-to-run-samples.md)]

## What this sample does

The `ExecuteTransactionRequest` message is intended to be used in a scenario where it contains  data that is needed to execute one or more message requests in a single database transaction, and optionally return a collection of results.

## How this sample works

In order to simulate the scenario described in [What this sample does](#what-this-sample-does), the sample will do the following:

### Setup

Checks for the current version of the org.

### Demonstrate

1. The `ExecuteTransactionRequest` method creates the `ExecuteTransactionRequest` object.
2. The `OrganizationRequestCollection` method creates an empty organization request collection.
3. The `CreateRequest` method is added for each table to the request collection.

### Clean up

Display an option to delete the records created in the [Setup](#setup). The deletion is optional in case you want to examine the tables and data created by the sample. You can manually delete the records to achieve the same result.


[!INCLUDE[footer-include](../../../../includes/footer-banner.md)]