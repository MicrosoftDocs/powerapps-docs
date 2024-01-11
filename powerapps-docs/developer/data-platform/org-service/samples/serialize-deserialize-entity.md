---
title: "Sample: Serialize and deserialize entity instances (Microsoft Dataverse) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "This sample showcases how to serialize and deserialize entity instances." # 115-145 characters including spaces. This abstract displays in the search result.
ms.date: 04/03/2022
author: divkamath
ms.author: dikamath
ms.reviewer: pehecke
ms.topic: sample
search.audienceType:
  - developer
contributors:
  - JimDaly
  - phecke
---

# Sample: Serialize and deserialize entity instances

This sample shows how to serialize early-bound and late-bound entity instances into an XML format, and how to de-serialize from an XML format to an early-bound entity instances.

> [!div class="nextstepaction"]
> [SDK for .NET: Serialize and deserialize entity instances sample code](https://github.com/microsoft/PowerApps-Samples/tree/master/dataverse/orgsvc/C%23/SerializeDeserializeEntity)

## How to run this sample

[!include[cc-how-to-run-samples](../../includes/cc-how-to-run-samples.md)]

## What this sample does

The `DataContractSerializer` message is intended to be used in a scenario where it Serializes and deserializes an instance of a type into an XML stream or document using a supplied data contract. This class cannot be inherited.

## How this sample works

In order to simulate the scenario described in [What this sample does](#what-this-sample-does), the sample will do the following:

### Setup

1. Checks for the current version of the org.
1. The `CreateRequiredRecords` method creates required sample data for the sample.

### Demonstrate

1. The `DataContractSerializer` method serializes the contact records into XML and write it to the hard drive.
1. The `earlyBoundSerializer` method deserializes the entity instance.

### Clean up

Display an option to delete the records created in the [Setup](#setup). The deletion is optional in case you want to examine the tables and data created by the sample. You can manually delete the records to achieve the same result.

[!INCLUDE[footer-include](../../../../includes/footer-banner.md)]
