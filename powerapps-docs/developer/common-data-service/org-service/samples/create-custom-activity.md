---
title: "Sample: Create a custom activity (Common Data Service for Apps) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "This sample shows how to create a custom activity" # 115-145 characters including spaces. This abstract displays in the search result.
ms.custom: ""
ms.date: 08/01/2018
ms.reviewer: ""
ms.service: "powerapps"
ms.topic: "article"
author: "brandonsimons" # GitHub ID
ms.author: "jdaly" # MSFT alias of Microsoft employees only
manager: "ryjones" # MSFT alias of manager or PM counterpart
---
# Sample: Create a custom activity

<!-- https://docs.microsoft.com/en-us/dynamics365/customer-engagement/developer/sample-create-custom-activity -->

This sample demonstrates how to create a custom activity using [CreateEntityRequest](https://docs.microsoft.com/en-us/dotnet/api/microsoft.xrm.sdk.messages.createentityrequest?view=dynamics-general-ce-9) and [CreateAttributeRequest](https://docs.microsoft.com/en-us/dotnet/api/microsoft.xrm.sdk.messages.createattributerequest?view=dynamics-general-ce-9).  

## How to run this sample

See [How to run samples](../../../How-to-run-samples.md) for information about how to run this sample.

## What this sample does

The `CreateEntityRequest` message and `CreateAttributeRequest` message is intended to be used in a scenario to create custom activity.

## How this sample works

In order to simulate the scenario described in [What this sample does](#what-this-sample-does), the sample will do the following:

### Setup

1. Checks the version of the current org.

### Demonstrate

1. Creates the custom activity entity using the `CreateEntityRequest` message.
2. Publishes the created custom activity entity.
3. Creates few attributes to the custom activity entity using `CreateAttributeRequest` mesage.

### Clean up

1. Display an option to delete the records in [Setup](#setup).

    The deletion is optional in case you want to examine the entities and data created by the sample. You can manually delete the records to achieve the same result.
