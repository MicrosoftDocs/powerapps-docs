---
title: "Sample: Retrieve currency exchange rate" 
description: "This sample shows how to create a new currency and retrieve and display currency exchange rate."
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

# Sample: Retrieve currency exchange rate

This sample shows how to create a new currency, and how to retrieve and display the currency exchange rate relative to the organization's base currency.

> [!div class="nextstepaction"]
> [SDK for .NET: Retrieve currency exchange rate sample code](https://github.com/microsoft/PowerApps-Samples/tree/master/dataverse/orgsvc/CSharp/RetrieveCurrencyExchangeRate)

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

The `RetrieveExchangeRateRequest` message retrieves the exchange rate against the base currency of the org.

### Clean up

Display an option to delete the sample data created in [Setup](#setup). The deletion is optional in case you want to examine the tables and data created by the sample. You can manually delete the records to achieve the same result.

[!INCLUDE[footer-include](../../../../includes/footer-banner.md)]
