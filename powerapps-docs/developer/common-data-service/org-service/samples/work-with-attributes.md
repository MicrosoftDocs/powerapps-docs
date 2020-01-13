---
title: "Sample: Work with attributes (Common Data Service) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "This sample shows how to work with attributes" # 115-145 characters including spaces. This abstract displays in the search result.
ms.custom: ""
ms.date: 10/31/2018
ms.reviewer: ""
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

# Work with attribute metadata

This sample shows how to perform various actions on attributes.

## How to run this sample

[!include[cc-how-to-run-samples](../../includes/cc-how-to-run-samples.md)]

## What this sample does

This sample shows how to create different types of attributes in Common Data Service.

## How this sample works

In order to simulate the scenario described in [What this sample does](#what-this-sample-does), the sample will do the following:

### Setup

Checks for the current version of the org.

### Demonstrate

1. The `BooleanAttributeMetadata` method creates an attribute of type boolean.
2. The `DateTimeAttributeMetadata` message creates an attribute of type date time.
3. The `DecimalAttributeMetadata` message creates an attribute of type decimal.
4. The `IntegerAttributeMetadata` message creates an attribute of type integer.
5. The `MemoAttributeMetadata` message creates an attribute of type memo.
6. The `MoneyAttributeMetadata` message creates an attribute of type money.
7. The `PicklistAttributeMetadata` message creates an attribute of type picklist.

### Clean up

Displays an option to delete all the data created in the sample. The deletion is optional in case you want to examine the data created by the sample. You can manually delete the data to achieve same results.