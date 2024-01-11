---
title: "Sample: Create a custom activity (Microsoft Dataverse) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "This sample shows how to create a custom activity" # 115-145 characters including spaces. This abstract displays in the search result.
ms.date: 04/03/2022
author: NHelgren
ms.author: nhelgren
ms.reviewer: jdaly
ms.topic: sample
search.audienceType:
  - developer
contributors:
  - JimDaly
  - phecke
---

# Sample: Create a custom activity

This sample demonstrates how to create a custom activity using [CreateEntityRequest](/dotnet/api/microsoft.xrm.sdk.messages.createentityrequest) and [CreateAttributeRequest](/dotnet/api/microsoft.xrm.sdk.messages.createattributerequest).

> [!div class="nextstepaction"]
> [SDK for .NET: Create a custom activity sample code](https://github.com/microsoft/PowerApps-Samples/tree/master/dataverse/orgsvc/C%23/CustomActivity)

[!INCLUDE[cc-terminology](../../includes/cc-terminology.md)]

## How to run this sample

[!include[cc-how-to-run-samples](../../includes/cc-how-to-run-samples.md)]

## What this sample does

The `CreateEntityRequest` message and `CreateAttributeRequest` message is intended to be used in a scenario to create custom activity.

## How this sample works

In order to simulate the scenario described in [What this sample does](#what-this-sample-does), the sample will do the following:

### Setup

Checks for the current version of the current org.

### Demonstrate

1. Creates the custom activity table using the `CreateEntityRequest` message.
2. Publishes the created custom activity table.
3. Creates few columns to the custom activity table using `CreateAttributeRequest` message.

### Clean up

Display an option to delete the records in [Setup](#setup). The deletion is optional in case you want to examine the tables and data created by the sample. You can manually delete the records to achieve the same result.

[!INCLUDE[footer-include](../../../../includes/footer-banner.md)]
