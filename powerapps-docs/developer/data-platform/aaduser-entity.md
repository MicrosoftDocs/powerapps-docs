---
title: "Azure Active Directory user (AADuser) table (Microsoft Dataverse) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "An Azure Active Directory user virtual table in Microsoft Dataverse." # 115-145 characters including spaces. This abstract displays in the search result.
ms.custom: ""
ms.date: 04/20/2022
ms.reviewer: "pehecke"
ms.topic: "article"
author: "NHelgren" # GitHub ID
ms.service: powerapps
ms.subservice: dataverse-developer
ms.author: "nhelgren" # MSFT alias of Microsoft employees only
manager: "sunilg" # MSFT alias of manager or PM counterpart
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---
# Azure Active Directory user table

Microsoft Dataverse includes a virtual table named AAD user (aaduser). This virtual table provides a connection to Azure Active Directory (AAD) and returns data about users within your AAD organization. No virtual table configuration is required to use the functionality. This is an online only feature.

## Lookups using AAD user

You can easily add a lookup to this virtual table from within the Power Apps portal.

:::image type="content" source="media/add-lookup-aaduser.png" alt-text="Create a lookup column with a related table of AADUser":::

## Permissions

The AAD user table functions using Microsoft Graph. Users in your organization need to be assigned Graph permissions in order to view and use the AAD user virtual table.

## Allowed operations

Only read and read-multiple operations are possible through the AAD user virtual table.

### See also

[aaduser table/entity reference](reference/entities/aaduser.md)<br/>
[Security and data access](security-model.md)

[!INCLUDE[footer-include](../../includes/footer-banner.md)]