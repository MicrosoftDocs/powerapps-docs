---
title: "Sample: Create and retrieve table relationships"
description: This sample shows how to create and retrieve table relationships.
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

# Sample: Create and retrieve table relationships

This sample shows how to create and retrieve table relationships. The following methods are used to create and retrieve the relationships:

- [CreateOneToManyRequest](/dotnet/api/microsoft.xrm.sdk.messages.createonetomanyrequest)
- [CreateManyToManyRequest](/dotnet/api/microsoft.xrm.sdk.messages.createmanytomanyrequest)
- [CanBeReferencedRequest](/dotnet/api/microsoft.xrm.sdk.messages.canbereferencedrequest)
- [CanBeReferencingRequest](/dotnet/api/microsoft.xrm.sdk.messages.canbereferencingrequest)
- [CanManyToManyRequest](/dotnet/api/microsoft.xrm.sdk.messages.canmanytomanyrequest)
- [RetrieveRelationshipRequest](/dotnet/api/microsoft.xrm.sdk.messages.retrieverelationshiprequest)

> [!div class="nextstepaction"]
> [SDK for .NET: Create and retrieve table relationships sample code](https://github.com/microsoft/PowerApps-Samples/tree/master/dataverse/orgsvc/C%23/CreateRetrieveEntityRelationships)

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
