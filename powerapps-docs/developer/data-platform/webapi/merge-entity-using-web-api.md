---
title: "Merge table rows using the Web API (Microsoft Dataverse)| Microsoft Docs"
description: "Read how to use the Merge unbound action to merge two table rows"
ms.date: 08/10/2023
author: divkamath
ms.author: dikamath
ms.reviewer: jdaly
search.audienceType: 
  - developer
contributors: 
  - JimDaly
---

# Merge table rows using the Web API

[!INCLUDE[cc-terminology](../includes/cc-terminology.md)]

When you find duplicate records you can combine them into one using the <xref:Microsoft.Dynamics.CRM.Merge?text=Merge Action>.

> [!NOTE]
> Only the following entity types can be merged:
> - <xref:Microsoft.Dynamics.CRM.account>
> - <xref:Microsoft.Dynamics.CRM.contact>
> - `lead`: Available with [Dynamics 365 for Sales](/dynamics365/sales/help-hub)
> - `incident` : Available with [Dynamics 365 for Service](/dynamics365/customer-service/help-hub)
>
>   See [Merge behavior for incident](#merge-behavior-for-incident)

## Merge action

Merge is an unbound action that accepts four parameters:

|Name  |Type  |Description| Optional|
|---------|---------|---------|---------|
|`Target`|<xref:Microsoft.Dynamics.CRM.crmbaseentity>|The target of the merge operation.| No|
|`Subordinate`|<xref:Microsoft.Dynamics.CRM.crmbaseentity>|The entity record from which to merge data.| No|
|`UpdateContent`|<xref:Microsoft.Dynamics.CRM.crmbaseentity>|Additional entity attributes to be set during the merge operation.| Yes|
|`PerformParentingChecks`|Boolean|Indicates whether to check if the parent information is different for the two entity records.| No|

Merging will move any useful data from the `Subordinate` record to the `Target` record. Any existing data in the `Target` record will not be overwritten. Then the `Subordinate` record is deactivated.
To perform this operation the caller must have privileges and access rights to both the records identified as the `Target` and `Subordinate`.

Use a POST request to send data to merge records. 
This example merges two account entity records while updating `accountnumber` property of the record that will remain after the merge.

**Request:**

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

**Response:** 

```http
HTTP/1.1 204 No Content
OData-Version: 4.0
```

## Merge behavior for incident

The merge behavior for `incident` (case) table is different from `account`, `contact`, or `lead` tables.

- The `UpdateContent` parameter data is not used.
- Merge is performed in the security context of the user

   Merge operations for other tables are performed with a system user security context. Because incident merge operations are performed in the security context of the user, the user must have the security privileges to perform any of the actions, such as re-parenting related records, that are performed by the merge operation.

   If the user merging records doesn't have privileges for all the actions contained within the merge operation, the merge operation will fail and roll back to the original state.

### See also

[Use Web API actions](use-web-api-actions.md)<br />
[Merge duplicate records](../../../user/merge-duplicate-records.md)<br />
<xref:Microsoft.Crm.Sdk.Messages.MergeRequest?text=MergeRequest Class><br />
[Administration Guide: Merge data](/power-platform/admin/merge-data)<br />
[Dynamics 365 for Service: Merge cases](/dynamics365/customer-service/customer-service-hub-user-guide-merge-cases)

[!INCLUDE[footer-include](../../../includes/footer-banner.md)]
