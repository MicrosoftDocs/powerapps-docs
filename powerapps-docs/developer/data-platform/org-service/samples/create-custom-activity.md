---
title: "Sample: Create a custom activity (Microsoft Dataverse) | Microsoft Docs"
description: "This sample shows how to create a custom activity" 
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

# Sample: Create a custom activity

This sample shows how to create a custom activity by using [CreateEntityRequest](/dotnet/api/microsoft.xrm.sdk.messages.createentityrequest) and [CreateAttributeRequest](/dotnet/api/microsoft.xrm.sdk.messages.createattributerequest) classes.

> [!div class="nextstepaction"]
> [SDK for .NET: Create a custom activity sample code](https://github.com/microsoft/PowerApps-Samples/tree/master/dataverse/orgsvc/CSharp/CustomActivity)

[!INCLUDE[cc-terminology](../../includes/cc-terminology.md)]

## How to run this sample

[!INCLUDE[cc-how-to-run-samples](../../includes/cc-how-to-run-samples.md)]

## What this sample does

Use the `CreateEntityRequest` and `CreateAttributeRequest` classes to create a custom activity.

## How this sample works

To simulate the scenario described in [What this sample does](#what-this-sample-does), the sample performs the following steps:

### Setup

Checks for the current version of the current org.

### Demonstrate

1. Creates the custom activity table by using the `CreateEntityRequest` class.
2. Publishes the custom activity table.
3. Creates columns for the custom activity table by using the `CreateAttributeRequest` class.

### Clean up

Displays an option to delete the records in [Setup](#setup). You can optionally delete these records if you want to examine the tables and data that the sample created. To achieve the same result, you can manually delete the records.

[!INCLUDE[footer-include](../../../../includes/footer-banner.md)]
