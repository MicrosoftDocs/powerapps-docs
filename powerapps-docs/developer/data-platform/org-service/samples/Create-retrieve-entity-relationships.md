---
title: "Sample: Create and retrieve table relationships"
description: This sample shows how to create and retrieve table relationships.
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

# Sample: Create and retrieve table relationships

This sample shows how to create and retrieve table relationships. The following classes are used to create and retrieve the relationships:

- [CreateOneToManyRequest class](/dotnet/api/microsoft.xrm.sdk.messages.createonetomanyrequest)
- [CreateManyToManyRequest class](/dotnet/api/microsoft.xrm.sdk.messages.createmanytomanyrequest)
- [CanBeReferencedRequest class](/dotnet/api/microsoft.xrm.sdk.messages.canbereferencedrequest)
- [CanBeReferencingRequest class](/dotnet/api/microsoft.xrm.sdk.messages.canbereferencingrequest)
- [CanManyToManyRequest class](/dotnet/api/microsoft.xrm.sdk.messages.canmanytomanyrequest)
- [RetrieveRelationshipRequest class](/dotnet/api/microsoft.xrm.sdk.messages.retrieverelationshiprequest)

> [!div class="nextstepaction"]
> [SDK for .NET: Create and retrieve table relationships sample code](https://github.com/microsoft/PowerApps-Samples/tree/master/dataverse/orgsvc/CSharp/CreateRetrieveEntityRelationships)

[!INCLUDE[cc-terminology](../../includes/cc-terminology.md)]

## How to run this sample

[!INCLUDE[cc-how-to-run-samples](../../includes/cc-how-to-run-samples.md)]

## What this sample does

This sample uses the classes listed earlier to create and retrieve table relationships.

## How this sample works

To simulate the scenario described in [What this sample does](#what-this-sample-does), the sample code performs the following steps:

### Setup

Checks for the current version of the org.

### Demonstrate

1. Use the `CreateOneToManyRequest` class to create a new one-to-many (1:N) relationship.
2. Use the `CreateManyToManyRequest` class to create a new many-to-many (N:N) relationship.
3. The `EligibleCreateManyToManyRelationship` method verifies whether tables can participate in an N:N relationship by using the [CanBeReferencedRequest](xref:Microsoft.Xrm.Sdk.Messages.CanBeReferencedRequest) and [CanBeReferencingRequest](xref:Microsoft.Xrm.Sdk.Messages.CanBeReferencingRequest) classes.
4. The `RetrieveRelationshipRequest` class retrieves the two tables relationships you previously created.

### Clean up

Displays an option to delete the records you created in the [Setup](#setup). The deletion is optional in case you want to examine the tables and data created by the sample. You can manually delete the records to achieve the same result.

[!INCLUDE[footer-include](../../../../includes/footer-banner.md)]
