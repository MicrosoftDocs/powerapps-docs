---
title: "Create, retrieve, update, and delete dashboards (Microsoft Dataverse) | Microsoft Docs"
description: "This sample showcases how to create, retrieve, update, and delete an user-owned dashboards." 
ms.date: 03/04/2026
author: mspilde
ms.author: mspilde
ms.reviewer: jdaly
ms.topic: sample
search.audienceType:
  - developer
contributors:
  - JimDaly
  - phecke
---

# Sample: Create, retrieve, update, and delete a dashboard

This sample shows how to create, retrieve, update, and delete a user-owned dashboard by using the following methods:

- [IOrganizationService.Create](/dotnet/api/microsoft.xrm.sdk.iorganizationservice.create)
- [IOrganizationService.Retrieve](/dotnet/api/microsoft.xrm.sdk.iorganizationservice.retrieve)
- [IOrganizationService.Update](/dotnet/api/microsoft.xrm.sdk.iorganizationservice.update)
- [IOrganizationService.Delete](/dotnet/api/microsoft.xrm.sdk.iorganizationservice.delete)

> [!div class="nextstepaction"]
> [SDK for .NET: Create, retrieve, update, and delete a dashboard sample code](https://github.com/microsoft/PowerApps-Samples/tree/master/dataverse/orgsvc/CSharp/CRUDOperationsDashboard)

## How to run this sample

[!include[cc-how-to-run-samples](../../includes/cc-how-to-run-samples.md)]

## What this sample does

Use the `IOrganizationService` interface in a scenario where it contains data that provides programmatic access to the metadata and data for an organization.

## How this sample works

To simulate the scenario described in [What this sample does](#what-this-sample-does), the sample performs the following steps:

### Setup

Checks for the current version of the org.

### Demonstrate

1. The `mySavedQuery` method gets the default public view for opportunities.
1. The `visualizationQuery` method gets the visualizations from the system. This sample assumes that you have the **Top opportunities** visualization.
1. The `dashboard` method sets the dashboard and specifies the FormXml.
1. The `chartPicker` method enables the chart picker on the chart.

### Clean up

Display an option to delete the records you created in the [Setup](#setup) section. The deletion is optional in case you want to examine the tables and data that the sample created. You can manually delete the records to achieve the same result.

[!INCLUDE[footer-include](../../../../includes/footer-banner.md)]
