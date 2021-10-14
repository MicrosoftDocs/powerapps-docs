---
title: "isAvailableOffline (Client API reference) in model-driven apps| MicrosoftDocs"
description: Includes description and supported parameters for the isAvailableOffline method.
ms.date: 04/21/2021
ms.service: powerapps
ms.topic: "reference"
applies_to: "Dynamics 365 (online)"
ms.assetid: ea9eacc0-2e31-49f4-a329-dcdf430a5a7e
author: "Nkrb"
ms.author: "nabuthuk"
manager: "kvivek"
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---
# isAvailableOffline (Client API reference)



[!INCLUDE[./includes/isAvailableOffline-description.md](./includes/isAvailableOffline-description.md)] 

## Syntax

`Xrm.WebApi.offline.isAvailableOffline(entityLogicalName);`

## Parameters

<table style="width:100%">
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