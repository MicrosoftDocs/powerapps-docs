---
title: "isAvailableOffline (Client API reference) in model-driven apps| MicrosoftDocs"
description: Includes description and supported parameters for the isAvailableOffline method.
ms.author: jdaly
author: adrianorth
manager: kvivek
ms.date: 03/12/2022
ms.reviewer: jdaly
ms.topic: "reference"
applies_to: "Dynamics 365 (online)"
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
contributors:
  - JimDaly
---
# isAvailableOffline (Client API reference)



[!INCLUDE[./includes/isAvailableOffline-description.md](./includes/isAvailableOffline-description.md)] 

## Syntax

`Xrm.WebApi.offline.isAvailableOffline(entityLogicalName);`

## Parameters

<table>
<tr>
<th>Name</th>
<th>Type</th>
<th>Required</th>
<th>Description</th>
</tr>
<tr>
<td>entityLogicalName</td>
<td>String</td>
<td>Yes</td>
<td>Logical name of the table. For example: "account".</td>
</tr>

</table>

## Return Value

**Type**: Boolean.

**Description**: true if the table is present in user’s profile and is currently available for use in offline mode; otherwise false.

[Xrm.WebApi.offline](offline.md)

[Xrm.WebApi](../xrm-webapi.md)






[!INCLUDE[footer-include](../../../../../includes/footer-banner.md)]