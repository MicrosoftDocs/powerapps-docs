---
title: "Sample: Retrieve currency exchange rate (Common Data Service for Apps) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "This sample shows how to create a new currency and retrieve and display currency exchange rate." # 115-145 characters including spaces. This abstract displays in the search result.
ms.custom: ""
ms.date: 10/31/2018
ms.reviewer: ""
ms.service: "powerapps"
ms.topic: "samples"
author: "brandonsimons" # GitHub ID
ms.author: "jdaly" # MSFT alias of Microsoft employees only
manager: "ryjones" # MSFT alias of manager or PM counterpart
---
# Sample: Retrieve currency exchange rate

<!-- https://docs.microsoft.com/en-us/dynamics365/customer-engagement/developer/sample-retrieve-currency-exchange-rate -->

This sample shows how to create a new currency, and how to retrieve and display the currency exchange rate relative to the organization’s base currency. You can download the sample from [here](https://github.com/Microsoft/PowerApps-Samples/tree/master/cds/orgsvc/C%23/RetrieveCurrencyExchangeRate).

## How to run this sample

[!include[cc-how-to-run-samples](../../includes/cc-how-to-run-samples.md)]

## What this sample does

The `RetrieveExchangeRateRequest` message is intended to be used in a scenario where it contains data that is needed to retrieve the exchange rate.

## How this sample works

In order to simulate the scenario described in [What this sample does](#what-this-sample-does), the sample will do the following:

### Setup

1. Checks for the current version of the org. 
2. The `TransactionCurrency` method creates a new currency for the sample.

### Demonstrate

1. The `RetrieveExchangeRateRequest` message retrieves the exchange rate against the base currency of the org.

### Clean up

1. Display an option to delete the sample data created  in [Setup](#setup).
    The deletion is optional in case you want to examine the entities and data created by the sample. You can manually delete the records to achieve the same result.
