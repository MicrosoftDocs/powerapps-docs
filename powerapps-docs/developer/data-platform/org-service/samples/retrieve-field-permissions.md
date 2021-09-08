---
title: "Sample: Retrieve field permissions (Microsoft Dataverse) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "This sample shows how to retrieve secured columns for a user" # 115-145 characters including spaces. This abstract displays in the search result.
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
# Sample: Retrieve field permissions

[!INCLUDE[cc-data-platform-banner](../../../../includes/cc-data-platform-banner.md)]


This sample shows how to retrieve secured columns for a user according to the steps outlined in [Field security tables](/dynamics365/customer-engagement/developer/field-security-entities). You can download the sample from [here](https://github.com/Microsoft/PowerApps-Samples/tree/master/cds/orgsvc/C%23/RetrieveFieldPermission).

This sample requires additional users that are not in your system. Create the required users manually in **Microsoft 365** in order to run the sample without any errors. For this sample create a user profile **as is** shown below. Replace `yourorg` with the organization name.

**First Name**: Samantha <br/>
**Last Name**: Smith<br/>
**Security Role**: Marketing Manager<br/>
**UserName**: ssmith@yourorg.onmicrosoft.com<br/>

## How to run this sample

[!include[cc-how-to-run-samples](../../includes/cc-how-to-run-samples.md)]

## What this sample does

The `FieldPermission` class is intended to be used in a scenario where it contains the data that defines the possible permission types.

## How this sample works

In order to simulate the scenario described in [What this sample does](#what-this-sample-does), the sample will do the following:

### Setup

1. Checks for the current version of the org.
1. Gets the user information that you have created manually in **Microsoft 365**.
1. The `QueryExpression` method retrieves the security role needed to assign to the user.
1. The `Team` method instantiate a team record and set its property values.

### Demonstrate

1. The `FieldSecurityProfile` method creates field security profile.
1. The `AssociateRequest` method adds team and user to the profile.
1. The `CreateEntityRequest` method creates a new custom activity table for the sample.
1. The `RolePrivilege` method adds privileges for the new custom table.
1. The `AddPrivilegeRoleRequest` method creates and execute the `RolePrivilege` method.
1. The `FieldPermission` method creates field permission object for identity.

### Clean up

Display an option to delete the records created in the [Setup](#setup). The deletion is optional in case you want to examine the tables and data created by the sample. You can manually delete the records to achieve the same result.


[!INCLUDE[footer-include](../../../../includes/footer-banner.md)]