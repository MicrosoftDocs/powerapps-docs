---
title: "Sample: Create and retrieve table relationships  (Microsoft Dataverse) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "This sample shows how to create and retrieve table relationships." # 115-145 characters including spaces. This abstract displays in the search result.
ms.custom: ""
ms.date: 06/17/2021
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

# Create and retrieve table relationships

[!INCLUDE[cc-data-platform-banner](../../../../includes/cc-data-platform-banner.md)]

This sample shows how to create and retrieve table relationships. The following methods are used to create and retrieve the relationships:

- [CreateOneToManyRequest](/dotnet/api/microsoft.xrm.sdk.messages.createonetomanyrequest?view=dynamics-general-ce-9)
- [CreateManyToManyRequest](/dotnet/api/microsoft.xrm.sdk.messages.createmanytomanyrequest?view=dynamics-general-ce-9)
- [CanBeReferencedRequest](/dotnet/api/microsoft.xrm.sdk.messages.canbereferencedrequest?view=dynamics-general-ce-9)
- [CanBeReferencingRequest](/dotnet/api/microsoft.xrm.sdk.messages.canbereferencingrequest?view=dynamics-general-ce-9)
- [CanManyToManyRequest](/dotnet/api/microsoft.xrm.sdk.messages.canmanytomanyrequest?view=dynamics-general-ce-9)
- [RetrieveRelationshipRequest](/dotnet/api/microsoft.xrm.sdk.messages.retrieverelationshiprequest?view=dynamics-general-ce-9)

You can download the sample from [here](https://github.com/microsoft/PowerApps-Samples/tree/master/cds/orgsvc/C%23/CreateRetrieveEntityRelationships).

[!INCLUDE[cc-terminology](../../includes/cc-terminology.md)]

## How to run this sample

[!include[cc-how-to-run-samples](../../includes/cc-how-to-run-samples.md)]

## What this sample does

The `CreateOneToManyRequest`, `CreateManyToManyRequest`, `CanManyToManyRequest`, `CreateOneToManyRequest`, `CanBeReferencedRequest`, `CanBeReferencingRequest`, and `RetrieveRelationshipRequest` messages are intended to be used in a scenario where it contains the data that is needed to create and retrieve table relationships.

## How this sample works

In order to simulate the scenario described in [What this sample does](#what-this-sample-does), the sample will do the following:

### Setup

Checks for the current version of the org.

### Demonstrate

1. The `CreateOneToManyRequest` method creates a new One-to-Many (1:N) relationship. 
2. The `CreateManyToManyRequest` method creates a new Many-To-Many (N:N) relationship.
3. The `EligibleCreateManyToManyRelationship` method verifies whether tables can participate in N:N relationship.
4. The `RetrieveRelationshipRequest` method retrieves the two tables relationships previously created.


### Clean up

Display an option to delete the records created in the [Setup](#setup). The deletion is optional in case you want to examine the tables and data created by the sample. You can manually delete the records to achieve the same result.


[!INCLUDE[footer-include](../../../../includes/footer-banner.md)]