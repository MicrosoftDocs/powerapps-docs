---
title: "Merge table rows using the Web API (Microsoft Dataverse)| Microsoft Docs"
description: "Read how to use the Merge unbound action to merge two table rows"
ms.custom: ""
ms.date: 05/04/2021
ms.service: powerapps
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
applies_to: 
  - "Dynamics 365 (online)"
caps.latest.revision: 21
author: "JimDaly" # GitHub ID
ms.author: "jdaly"
ms.reviewer: "pehecke"
manager: "annbe"
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---

# Merge table rows using the Web API

[!INCLUDE[cc-terminology](../includes/cc-terminology.md)]

When you find duplicate records you can combine them into one using the [Merge Action](/dynamics365/customer-engagement/web-api/merge).

> [!NOTE]
> Only the following entity types can be merged:
> - [account](/dynamics365/customer-engagement/web-api/account)
> - [contact](/dynamics365/customer-engagement/web-api/contact)
> - [incident](/dynamics365/customer-engagement/web-api/incident)
> - [lead](/dynamics365/customer-engagement/web-api/lead)


## Merge action
Merge is an unbound action that accepts four parameters:


|Name  |Type  |Description  |
|---------|---------|---------|
|`Target`|[crmbaseentity ](/dynamics365/customer-engagement/web-api/crmbaseentity)|The target of the merge operation.|
|`Subordinate`|[crmbaseentity ](/dynamics365/customer-engagement/web-api/crmbaseentity)|The entity record from which to merge data.|
|`UpdateContent`|[crmbaseentity ](/dynamics365/customer-engagement/web-api/crmbaseentity)|Additional entity attributes to be set during the merge operation.|
|`PerformParentingChecks`|Boolean|Indicates whether to check if the parent information is different for the two entity records.|

All the parameters are required.

Use a POST request to send data to merge entities. This example merges two account entity records while updating `accountnumber` property of the record that will remain after the merge.

**Request**

```http
POST [Organization URI]/api/data/v9.0/Merge HTTP/1.1
Content-Type: application/json; charset=utf-8
OData-MaxVersion: 4.0
OData-Version: 4.0
Accept: application/json

{
  "Target": {
    "name": "Account 1",
    "accountid": "bb8055c0-aea6-ea11-a812-000d3a55d474",
    "@odata.type": "Microsoft.Dynamics.CRM.account"
  },
  "Subordinate": {
    "name": "Account 2",
    "accountid": "c38055c0-aea6-ea11-a812-000d3a55d474",
    "@odata.type": "Microsoft.Dynamics.CRM.account"
  },
  "UpdateContent": {
    "accountnumber": "1234",
    "@odata.type": "Microsoft.Dynamics.CRM.account"
  },
  "PerformParentingChecks": false
}
```

> [!IMPORTANT]
> Because the `Target`, `Subordinate`, and `UpdateContent` property types are not explicitly defined by the parameter, you must include the `@odata.type` annotation to specify the type.

**Response** 

```http
HTTP/1.1 204 No Content
OData-Version: 4.0
```

### See also

[Merge duplicate records](../../../user/merge-duplicate-records.md)<br />
<xref:Microsoft.Crm.Sdk.Messages.MergeRequest>

[!INCLUDE[footer-include](../../../includes/footer-banner.md)]