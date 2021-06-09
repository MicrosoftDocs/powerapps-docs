---
title: "Sample: Rollup goal data for a custom period against the target avenue (Microsoft Dataverse) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "This sample shows how to roll up goal data for a custom period against the target revenue" # 115-145 characters including spaces. This abstract displays in the search result.
ms.custom: ""
ms.date: 10/31/2018
ms.reviewer: "pehecke"
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
# Sample: Rollup goal data for a custom period against the target revenue

[!INCLUDE[cc-data-platform-banner](../../../../includes/cc-data-platform-banner.md)]

<!-- https://docs.microsoft.com/dynamics365/customer-engagement/developer/sample-rollup-goal-data-custom-period-target-revenue -->

This sample shows how to roll up goal data for a custom period against the target revenue. You can download the sample from [here](https://github.com/Microsoft/PowerApps-Samples/tree/master/cds/orgsvc/C%23/RollupGoalData).

This sample requires additional three users that are not in your system. Create the three required users **as is** shown below manually in **Microsoft 365**. Replace `yourorg` with the organization name.

**First Name**: Nancy<br/>
**Last Name**: Anderson<br/>
**Security Role**: Salesperson<br/>
**UserName**: nanderson@yourorg.onmicrosoft.com<br/>

**First Name**: David<br/>
**Last Name**: Bristol<br/>
**Security Role**: Salesperson<br/>
**UserName**: dbristol@yourorg.onmicrosoft.com<br/>

**First Name**: Kevin<br/>
**Last Name**: Cook<br/>
**Security Role**: SalesManager<br/>
**UserName**: kcook@yourorg.onmicrosoft.com<br/>

## How to run this sample

[!include[cc-how-to-run-samples](../../includes/cc-how-to-run-samples.md)]

## What this sample does

This sample shows how to roll up goal data for a custom period against the target revenue.

## How this sample works

In order to simulate the scenario described in [What this sample does](#what-this-sample-does), the sample will do the following:

### Setup

1. Checks for the version of the org.
2. Retrieves the sales manager and 2 sales representatives created manually in **Microsoft 365**.
3. Creates a sample unit group and retrieve the default unit id. 
4. Creates few products and new discount list.
5. The `PriceLevel` creates the price list.
6. The `ProductPriceLevel` creates a price list item for the first product and apply volume discount.
7. Creates account record for the opportunity's potential customer id.
8. Creates a new opportunity with user specified estimated revenue.
9. Creates a catalog products and override the list price.
10. Creates a new write-in opportunity product with a manual discount applied.

### Demonstrate

1. Creates Metric, and setting the Amount Data type to `Money`.
2. Creates a Rollup fields which targets the estimated values and actual values.
3. The `GoalRollupQuery` creates the goal rollup queries, locating the opportunities in the sales representative's area. 
4. Creates three goals, one parent goal and two child goals.
5. The `RecalculateRequest` calculates the rollup for goals. 

### Clean up

Display an option to delete the sample data created in [Setup](#setup). The deletion is optional in case you want to examine the entities and data created by the sample. You can manually delete the records to achieve the same result.


[!INCLUDE[footer-include](../../../../includes/footer-banner.md)]