---
title: "Sample: Enable field security for a table (Microsoft Dataverse) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "This sample shows how to enable field security for a table" # 115-145 characters including spaces. This abstract displays in the search result.
ms.custom: ""
ms.date: 3/27/2021
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
# Sample: Enable field security for a table

[!INCLUDE[cc-terminology](../../includes/cc-terminology.md)]

This sample shows how to enable field security for a table.  You can download the sample from [here](https://github.com/Microsoft/PowerApps-Samples/tree/master/cds/orgsvc/C%23/FieldSecurity). 

[!INCLUDE[cc-terminology](../../includes/cc-terminology.md)]

This sample requires additional users that are not in your system. Create the required users manually in **Microsoft 365** in order to run the sample without any errors. For this sample, create a user profile **as is** shown below. 

**First Name**: Samantha<br/>
**Last Name**: Smith<br/>
**Security Role**: Marketing Manager<br/>
**UserName**: ssmith@yourorg.onmicrosoft.com<br/>

## How to run this sample

[!include[cc-how-to-run-samples](../../includes/cc-how-to-run-samples.md)]

## How this sample works

In order to simulate the scenario described above, the sample will do the following:

### Setup

1. Checks for the current version of the org.
2. Gets the user that you have created manually in **Microsoft 365**.
3. Retrieve the security role needed to assign to the user. 
4. Retrieve the default business unit needed to create the team.
5. Instantiate a team record and set its property values. 

### Demonstrate

1. Creates field security profile and create the request object and set the monikers with the teamprofiles_assocation relationship.
2. Creates custom activity table and columns using the `CreateEntityRequest` and `CreateAttributeRequest` message.
3. Create the field permission for the identity column.

### Clean up

Display an option to delete the records in [Setup](#setup). The deletion is optional in case you want to examine the tables and data created by the sample. You can manually delete the records to achieve the same result.


[!INCLUDE[footer-include](../../../../includes/footer-banner.md)]
