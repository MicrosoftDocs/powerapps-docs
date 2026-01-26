---
title: " Retrieve roles for an organization (Microsoft Dataverse) | Microsoft Docs"
description: "This sample showcases how to retrieve roles for an organization " 
ms.date: 04/03/2022
author: paulliew
ms.author: paulliew
ms.reviewer: jdaly
ms.topic: sample
search.audienceType:
  - developer
contributors:
  - JimDaly
  - phecke
---

# Retrieve the roles for an organization

This sample shows how to retrieve the roles for an organization by using the [IOrganizationService.RetrieveMultiple](/dotnet/api/microsoft.xrm.sdk.iorganizationservice.retrievemultiple) method.

> [!div class="nextstepaction"]
> [SDK for .NET: Retrieve the roles for an organization sample code](https://github.com/microsoft/PowerApps-Samples/tree/master/dataverse/orgsvc/CSharp/RetrieveRolesForOrganization)

## How to run this sample

[!include[cc-how-to-run-samples](../../includes/cc-how-to-run-samples.md)]

## What this sample does

The [IOrganizationService.RetrieveMultiple](/dotnet/api/microsoft.xrm.sdk.iorganizationservice.retrievemultiple) message is intended to be used in a scenario where it contains data that is needed to retrieve a collection of records.

## How this sample works

In order to simulate the scenario described in [What this sample does](#what-this-sample-does), the sample will do the following:

### Setup

Checks for the current version of the org.

### Demonstrate

The `query` method retrieves all the roles that are present in an organization.

### Clean up

This sample creates no records. No cleanup is required.

[!INCLUDE[footer-include](../../../../includes/footer-banner.md)]
