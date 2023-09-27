---
title: "Sample: Work with views (Microsoft Dataverse) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "This sample shows how to work with views" # 115-145 characters including spaces. This abstract displays in the search result.
author: caburk
ms.author: caburk
ms.date: 06/10/2022
ms.reviewer: jdaly
ms.topic: sample
search.audienceType:
  - developer
contributors:
  - JimDaly
---

# Sample: Work with views

This sample shows how to perform various actions on views.

> [!div class="nextstepaction"]
> [SDK for .NET: Work with views sample code](https://github.com/microsoft/PowerApps-Samples/tree/master/dataverse/orgsvc/C%23/WorkWithViews)

## How to run this sample

[!include[cc-how-to-run-samples](../../includes/cc-how-to-run-samples.md)]

## What this sample does

This sample shows how to create a view and perform different actions on views.

## How this sample works

In order to simulate the scenario described in [What this sample does](#what-this-sample-does), the sample will do the following:

### Setup

Checks for the current version of the org.

### Demonstrate

1. The `layout` method creates the view that is required for the sample.
2. The `QueryExpression` message retrieves the views.

### Clean up

Displays an option to delete all the data created in the sample. The deletion is optional in case you want to examine the data created by the sample. You can manually delete the data to achieve same results.

[!INCLUDE[footer-include](../../../../includes/footer-banner.md)]
