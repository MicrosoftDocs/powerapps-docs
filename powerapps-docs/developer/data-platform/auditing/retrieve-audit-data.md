---
title: "Retrieve the history of audited data changes (Microsoft Dataverse) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "Describes how to programmatically retrieve the audit change history." # 115-145 characters including spaces. This abstract displays in the search result.
ms.date: 05/10/2022
ms.reviewer: jdaly
ms.topic: overview
author: Bluebear7 # GitHub ID
ms.subservice: dataverse-developer
ms.author: munzinge # MSFT alias of Microsoft employees only
manager: mayadu # MSFT alias of manager or PM counterpart
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
contributors:
 - JimDaly
 - phecke
---

# Retrieve the history of audited data changes

[!INCLUDE [cc-terminology](../includes/cc-terminology.md)]

After auditing is enabled and data changes are made to those tables and columns being audited, you can proceed to obtain the data change history.

## Audit table

Data for auditing events is in the [Auditing (Audit) table](../reference/entities/audit.md). In the Web API the <xref:Microsoft.Dynamics.CRM.audit?text=audit EntityType> is the resource for this data. The audit table is read-only. 

The following table summarizes important columns in the audit table.

|SchemaName<br />LogicalName<br />DisplayName  |Type  |Description  |
|---------|---------|---------|
|`Action`<br />`action`<br />Event|Choice|More than 70 options that represent the name of the message that caused the change. Each option has an integer and a localizable label value. For example:<br />0 = Unknown<br />1 = Create<br /> 2 = Update<br />3 = Delete<br />4 = Activate<br />5 = Deactivate<br />And so on... See [Action Choices/Options](/power-apps/developer/data-platform/reference/entities/audit#action-choicesoptions) for the complete list. |
|`AttributeMask`<br />`attributemask`<br />Changed Field|Memo|May contain a comma separated list of numbers that correspond to the <xref:Microsoft.Xrm.Sdk.Metadata.AttributeMetadata>.<xref:Microsoft.Xrm.Sdk.Metadata.AttributeMetadata.ColumnNumber> for the columns changed in the transaction for the action. |
|`AuditId`<br />`auditid`<br /> Record Id|Unique Identifier|The primary key for the audit table.|
|`CallingUserId`<br />`callinguserid`<br />Calling User|Lookup|The calling user when impersonation is used for the operation. Otherwise null. |
|`CreatedOn`<br />`createdon`<br />Changed Date|DateTime|When the audit record was created.|
|`ObjectId`<br />`objectid`<br />Record|Lookup|The unique identifier for the record that was audited.|
|`ObjectTypeCode`<br />`objecttypecode`<br />Entity|EntityName|The logical name of the entity referred to by the `objectid` column.|
|`Operation`<br />`operation`<br />Operation|Choice|The operation that cased the audit. One of 4 values:<br />1 = Create<br />2 = Update<br />3 = Delete<br />4 = Access<br />|
|`UserId`<br />`userid`<br />Changed By|Lookup|The user who caused the change|

<!-- |`RegardingObjectId`<br />`regardingobjectid`<br />Regarding |Lookup|         |
|`TransactionId`<br />`transactionid`<br />Transaction Id|         |         |
|`UserAdditionalInfo`<br />`useradditionalinfo`<br />User Info|         |         | 

UserAdditionalInfo is the only column that can be updated?
But the table doesn't support update
-->

### audit table relationships

The audit table has only two Many-to-one relationships with the `systemuser` table:

|Relationship|Audit Table Lookup|Description  |
|---------|---------|---------|
|`lk_audit_userid`|`userid`|Relates the user to all the audit records created because of changes they made.|
|`lk_audit_callinguserid`|`callinguserid`|Relates the user to any of the audit records they created while impersonating another user.|

You can use these relationships to filter audit data records created for a specific user.

> [!NOTE]
> The audit entity supports only one link entity in a query. Since only two relationships exist with the `systemuser` table, this means you can include data from either the `callinguserid` or `userid` columns, but not both at the same time.
> You cannot build queries using QueryExpression or FetchXml that join audit data with tables other than the two formal relationships that exist with the `systemuser` table.

<!-- Questions: 
Why is the Audit TransactionId frequently an empty GUID (but not always)? Does it matter?
Is UserAdditionalInfo ever not null?
Is RegardingObjectId ever not null? -->

### audit EntityType definition

With the Web API, you will use the <xref:Microsoft.Dynamics.CRM.audit?text=audit EntityType> resource to read data from the `audit` table. The following is the **EntityType** definition  Web API $metadata service document without annotations:

```xml
<EntityType Name="audit" BaseType="mscrm.crmbaseentity">
  <Key>
      <PropertyRef Name="auditid" />
  </Key>
  <Property Name="operation" Type="Edm.Int32" />
  <Property Name="attributemask" Type="Edm.String" Unicode="false" />
  <Property Name="action" Type="Edm.Int32" />
  <Property Name="useradditionalinfo" Type="Edm.String" Unicode="false" />
  <Property Name="createdon" Type="Edm.DateTimeOffset" />
  <Property Name="objecttypecode" Type="Edm.String" Unicode="false" />
  <Property Name="_callinguserid_value" Type="Edm.Guid" />
  <Property Name="_regardingobjectid_value" Type="Edm.Guid" />
  <Property Name="_objectid_value" Type="Edm.Guid" />
  <Property Name="_userid_value" Type="Edm.Guid" />
  <Property Name="transactionid" Type="Edm.Guid" />
  <Property Name="auditid" Type="Edm.Guid" />
  <NavigationProperty Name="callinguserid" Type="mscrm.systemuser" Nullable="false" Partner="lk_audit_callinguserid">
      <ReferentialConstraint Property="_callinguserid_value" ReferencedProperty="systemuserid" />
  </NavigationProperty>
  <NavigationProperty Name="userid" Type="mscrm.systemuser" Nullable="false" Partner="lk_audit_userid">
      <ReferentialConstraint Property="_userid_value" ReferencedProperty="systemuserid" />
  </NavigationProperty>
</EntityType>
```

More information: [CSDL $metadata document](../webapi/web-api-service-documents.md#csdl-metadata-document)

In the Web API, the `callinguserid` and `userid` single-valued navigation properties will always return `null` when using `$expand`. You must depend on the corresponding [Lookup properties](../webapi/web-api-properties.md#lookup-properties): `_callinguserid_value` and `_userid_value` to access data for these navigation properties. Lookup properties contain additional information when `GET` requests are sent using the `Prefer: odata.include-annotations="*"` request header. Using this preference will make sure that you get the `Microsoft.Dynamics.CRM.lookuplogicalname` and `OData.Community.Display.V1.FormattedValue` annotation values, but the `Microsoft.Dynamics.CRM.associatednavigationproperty` annotation values are not included with lookup properties in the `audit` EntityType.

<!-- I think this is a bug. As noted above, for the _userid_value and _callinguserid_value lookup properties, there are associated navigation properties that could be returned. lk_audit_userid and lk_audit_callinguserid -->

## Example: Find Contact records deleted by a user

The following examples are queries that use audit table data to show how many contact records were deleted by a specific user.

# [Web API](#tab/webapi)

<!-- These are equivilent

{{webapiurl}}systemusers(4026be43-6b69-e111-8f65-78e7d1620f5e)/lk_audit_userid?$select=_objectid_value,objecttypecode,createdon,_userid_value&$orderby=createdon desc&$filter=action eq 3 and objecttypecode eq 'contact'

{{webapiurl}}audits?$select=_objectid_value,objecttypecode,createdon,_userid_value&$orderby=createdon desc&$filter=action eq 3 and objecttypecode eq 'contact' and _userid_value eq '4026be43-6b69-e111-8f65-78e7d1620f5e' -->

**Request**

```http

```

**Response**

```http

```


# [Query Expression](#tab/queryexpression)

# [FetchXml](#tab/fetchxml)
---

  
## Retrieve the change history

 There are several messages requests that can be used to retrieve the audit change history. These requests are differentiated by the nature of what they retrieve.
Refer to the sample link at the end of this topic for sample code that demonstrates some of these change history message requests.

> [!IMPORTANT]
> Large column values, such as [Email.Description](../reference/entities/email.md#BKMK_Description) or [Annotation](../reference/entities/annotation.md) are limited (capped) to 5KB or ~5,000 characters in length. A capped column value can be recognized by three dots at the end of the text, for example "lorem ipsum, lorem ip…".
>
> Going forward, [Audit](../reference/entities/audit.md) table records will be stored in Microsoft Dataverse's log storage. Linking audit records with other table records using FetchXML or <xref:Microsoft.Xrm.Sdk.Query.QueryExpression> will no longer be possible.



### See also

[Auditing overview](auditing-overview.md)<br />
[Configure auditing](configure-auditing.md)<br />
[Delete audit data](delete-audit-data.md)<br />
[Sample: Audit table data changes](../org-service/samples/audit-entity-data-changes.md)


[!INCLUDE [footer-banner](../../../includes/footer-banner.md)]