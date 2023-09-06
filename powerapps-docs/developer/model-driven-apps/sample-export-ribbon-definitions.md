---
title: "Sample: Export ribbon definitions  (model-driven apps) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "The sample shows how to export Ribbon definitions. It uses the RetrieveApplicationRibbon and RetrieveEntityRibbon messages." # 115-145 characters including spaces. This abstract displays in the search result.
author: JimDaly
ms.author: jdaly

ms.date: 04/01/2022
ms.reviewer: jdaly
ms.topic: sample
ms.subservice: mda-developer
search.audienceType:
  - developer
---

# Sample: Export ribbon definitions

This sample shows how to export ribbon definitions. It uses the Organization Service <xref:Microsoft.Crm.Sdk.Messages.RetrieveApplicationRibbonRequest> and <xref:Microsoft.Crm.Sdk.Messages.RetrieveEntityRibbonRequest> classes.

> [!div class="nextstepaction"]
> [SDK for .NET: Export ribbon definitions sample code](https://github.com/microsoft/PowerApps-Samples/tree/master/dataverse/orgsvc/C%23/ExportRibbonDefinitions)

## How to run this sample

[!include[cc-how-to-run-samples](../data-platform/includes/cc-how-to-run-samples.md)]

## What this sample does

The `RetrieveApplicationRibbon` message is intended to be used in a scenario where it contains data that is needed to retrieve the data that defines the content and behavior of the application ribbon. The `RetrieveEntityRibbon` message is intended to be used in a scenario where it contains data that is needed to retrieve ribbon definitions for a table.

## How this sample works

In order to simulate the scenario described in [What this sample does](#what-this-sample-does), the sample will do the following:

### Setup

Checks for the current version of the org.

### Demonstrate

1. The `RetrieveApplicationRibbon` message retrieves the application ribbon.
2. The `RetrieveEntityRibbon` message retrieves the system table ribbons

### Clean up

No clean up is required for this sample

### See also

[Customize commands and the ribbon](customize-commands-ribbon.md)<br />
[Pass parameters to a URL by using the ribbon](pass-parameters-url-by-using-ribbon.md)<br />
[Ribbon core schema](ribbon-core-schema.md)<br />
[Ribbon types schema](ribbon-types-schema.md)<br />
[Ribbon WSS schema](ribbon-wss-schema.md)<br />
<xref:Microsoft.Crm.Sdk.Messages.RetrieveApplicationRibbonRequest><br />
<xref:Microsoft.Crm.Sdk.Messages.RetrieveEntityRibbonRequest>

[!INCLUDE[footer-include](../../includes/footer-banner.md)]
