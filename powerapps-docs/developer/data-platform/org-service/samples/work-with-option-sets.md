---
title: "Sample: Work with choices (Microsoft Dataverse) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "This sample shows how to work with choices" # 115-145 characters including spaces. This abstract displays in the search result.
ms.date: 04/06/2022
author: NHelgren
ms.author: nhelgren
ms.reviewer: pehecke
ms.topic: sample
search.audienceType:
  - developer
contributors:
  - JimDaly
  - phecke
---

# Work with choices

This sample shows how to work with choices. Typically, you use choices to set columns so that different columns can share the same set of options, which are maintained in one location. Unlike local options sets which are defined only for a specific column, you can reuse choices. You will also see them used in request parameters in a manner similar to an enumeration.

When you define a choices column by using [CreateOptionSetRequest](/dotnet/api/microsoft.xrm.sdk.messages.createoptionsetrequest), we recommend that you let the system assign a value. You do this by passing a null value when you create the new `OptionMetadata` instance. When you define an option, it will contain an option value prefix specific to the context of the publisher set for the solution that the choices column is created in. This prefix helps reduce the chance of creating duplicate choices for a managed solution, and in any choices column that are defined in organizations where your managed solution is installed. For more information, see [Merge choices values](/power-platform/alm/how-managed-solutions-merged#merge-option-set-options).

Use the following message request classes to work with choices:

- <xref:Microsoft.Xrm.Sdk.Messages.CreateOptionSetRequest>
- <xref:Microsoft.Xrm.Sdk.Messages.DeleteOptionSetRequest>
- <xref:Microsoft.Xrm.Sdk.Messages.RetrieveAllOptionSetsRequest>
- <xref:Microsoft.Xrm.Sdk.Messages.RetrieveOptionSetRequest>
- <xref:Microsoft.Xrm.Sdk.Messages.UpdateOptionSetRequest>

Use the following message request classes with choices:

- <xref:Microsoft.Xrm.Sdk.Messages.DeleteOptionValueRequest>
- <xref:Microsoft.Xrm.Sdk.Messages.InsertOptionValueRequest>
- <xref:Microsoft.Xrm.Sdk.Messages.InsertStatusValueRequest>
- <xref:Microsoft.Xrm.Sdk.Messages.OrderOptionRequest>
- <xref:Microsoft.Xrm.Sdk.Messages.UpdateOptionValueRequest>
- <xref:Microsoft.Xrm.Sdk.Messages.UpdateStateValueRequest>

> [!div class="nextstepaction"]
> [SDK for .NET: Work with choices sample code](https://github.com/microsoft/PowerApps-Samples/tree/master/dataverse/orgsvc/C%23/WorkWithOptionSets)

## How to run this sample

[!include[cc-how-to-run-samples](../../includes/cc-how-to-run-samples.md)]

## What this sample does

The `CreateOptionSetRequest`, `DeleteOptionSetRequest`, `RetrieveOptionSetRequest`, and `UpdateOptionSetRequest` messages are intended to be used in a scenario where it contains the data that is needed to work with choices.

## How this sample works

In order to simulate the scenario described in [What this sample does](#what-this-sample-does), the sample will do the following:

### Setup

Checks for the current version of the org.

### Demonstrate

1. The `CreateOptionSetRequest` method creates a choices column. You need to set the parameter `IsGlobal=true`.
2. The `CreateAttributeRequest` method creates a choices column linked to the choices.
3. The `UpdateOptionSetRequest` method updates the basic information of the choices column.
4. The `PublishXmlRequest` method publishes the choices column.
5. The `InsertOptionValueRequest` method inserts a new option into a choices column.
6. The `RetrieveOptionSetRequest` method retrieves the choices column by it's name.

### Clean up

Display an option to delete the records created in the [Setup](#setup). The deletion is optional in case you want to examine the tables and data created by the sample. You can manually delete the records to achieve the same result.

[!INCLUDE[footer-include](../../../../includes/footer-banner.md)]
