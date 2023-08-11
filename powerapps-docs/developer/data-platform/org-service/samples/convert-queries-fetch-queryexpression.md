---
title: "Sample: Convert queries between Fetch and QueryExpression"
description: This sample shows how to convert queries between FetchXML and QueryExpression
ms.date: 04/03/2022
author: divkamath
ms.author: dikamath
ms.reviewer: jdaly
ms.topic: sample
search.audienceType:
  - developer
contributors:
  - JimDaly
  - phecke
---

# Sample: Convert queries between FetchXML and QueryExpression

This sample shows how to convert queries between FetchXML and [QueryExpression](xref:Microsoft.Xrm.Sdk.Query.QueryExpression).

> [!div class="nextstepaction"]
> [SDK for .NET: Convert queries between FetchXML and QueryExpression sample code](https://github.com/microsoft/PowerApps-Samples/tree/master/dataverse/orgsvc/C%23/Convertqueriesfetchqueryexpressions)


[!INCLUDE[cc-terminology](../../includes/cc-terminology.md)]

## How to run this sample

[!include[cc-how-to-run-samples](../../includes/cc-how-to-run-samples.md)]

## What this sample does

The `QueryExpression` and `fetchExpression` messages are intended to be used in a scenario that contains queries in a hierarchy of expressions and FetchXML respectively.

## How this sample works

In order to simulate the scenario described in [What this sample does](#what-this-sample-does), the sample does the following operations:

### Setup

1. Checks for the current version of the org.
1. The `CreateRequireRecords` method creates an account and two contact records that are used by the sample.
1. The `QueryExpression` builds a [QueryExpression](xref:Microsoft.Xrm.Sdk.Query.QueryExpression) to convert into FetchXML.
1. The `DoFetchXmlToQueryExpressionConversion` class creates a Fetch query to convert into a [QueryExpression](xref:Microsoft.Xrm.Sdk.Query.QueryExpression).
1. The `conversionRequest` method converts the generated [QueryExpression](xref:Microsoft.Xrm.Sdk.Query.QueryExpression) into FetchXML and vice versa.
1. Use the converted query to with a `RetrieveMultiple` request.

### Clean up

Display an option to delete the records created in the [Setup](#setup). The deletion is optional in case you want to examine the tables and data created by the sample. You can manually delete the records to achieve the same result.

[!INCLUDE[footer-include](../../../../includes/footer-banner.md)]
