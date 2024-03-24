---
title: " Retrieve license information (Microsoft Dataverse) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "This sample showcases how to retrieve license information " # 115-145 characters including spaces. This abstract displays in the search result.
ms.date: 04/03/2022
author: JimDaly #TODO: No Owner
ms.author: jdaly
ms.reviewer: pehecke
ms.topic: sample
search.audienceType:
  - developer
contributors:
  - JimDaly
  - phecke
---

# Retrieve license information

This sample shows how to use the [IDeploymentService.RetrieveDeploymentLicenseTypeRequest](/dotnet/api/microsoft.crm.sdk.messages.retrievedeploymentlicensetyperequest) message and the [IOrganizationService.RetrieveLicenseInfoRequest](/dotnet/api/microsoft.crm.sdk.messages.retrievelicenseinforequest) message to retrieve information about licenses.

> [!div class="nextstepaction"]
> [SDK for .NET: Retrieve license information sample code](https://github.com/microsoft/PowerApps-Samples/tree/master/dataverse/orgsvc/C%23/RetrieveLicenseInformation)

## How to run this sample

[!include[cc-how-to-run-samples](../../includes/cc-how-to-run-samples.md)]

## What this sample does

The [IDeploymentService.RetrieveDeploymentLicenseTypeRequest](/dotnet/api/microsoft.crm.sdk.messages.retrievedeploymentlicensetyperequest) message is intended to be used in a scenario where it contains data that is needed to retrieve the type of license for a deployment of Microsoft Dataverse.

The [IOrganizationService.RetrieveLicenseInfoRequest](/dotnet/api/microsoft.crm.sdk.messages.retrievelicenseinforequest) message is intended to be used in a scenario where it contains data that is needed to retrieve the number of used and available licenses for a deployment of Dataverse.

## How this sample works

In order to simulate the scenario described in [What this sample does](#what-this-sample-does), the sample will do the following:

### Setup

Checks for the current version of the org.

### Demonstrate

1. The `deploymentTypeRequest` method creates a request to retrieve the deployment license types.
2. The `licenseInfoRequest` message creates request to retrieve the licensed info request.

### Clean up

This sample creates no records. No cleanup is required.

[!INCLUDE[footer-include](../../../../includes/footer-banner.md)]
