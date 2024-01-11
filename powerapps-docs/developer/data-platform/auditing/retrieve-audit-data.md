---
title: Retrieve the history of audited data changes
description: Learn how to programmatically retrieve the audit change history of records in Microsoft Dataverse.
ms.date: 06/02/2023
ms.reviewer: jdaly
ms.topic: conceptual
author: paulliew
ms.author: paulliew
ms.subservice: dataverse-developer
search.audienceType: 
  - developer
contributors:
 - JimDaly
 - phecke
ms.custom: bap-template
---

# Retrieve the history of audited data changes

When auditing is enabled and data in audited tables and columns is changed, you can retrieve the change history of those tables and columns.

Audit data isn't available using the [Dataverse TDS (SQL) endpoint](../dataverse-sql-query.md).

Audit history is not available for tables in the mobile app.

## Audit table

Auditing events are stored in the [Auditing (Audit) table](../reference/entities/audit.md). In the Web API, the [audit EntityType](xref:Microsoft.Dynamics.CRM.audit) is the resource for this data. The audit table is read-only.

The audit table provides the data for the [**View Audit Summary**](/power-platform/admin/manage-dataverse-auditing#view-audit-logging-details) displayed in the Power Platform admin center.

[Make sure the calling user has the `prvReadAuditSummary` privilege](../security-access-coding.md#example-check-whether-a-user-has-a-privilege) to retrieve data from the table.

The following table summarizes important columns in the audit table.

|SchemaName<br/>LogicalName<br/>DisplayName|Type|Description|
|---------|---------|---------|
|`Action`<br/>`action`<br/>**Event**|Choice|Represents the event that caused the change. [Learn more about actions](#audit-actions).|
|`AttributeMask`<br/>`attributemask`<br/>**Changed Field**|Memo|When the change represents a change to record data, contains a comma-separated list of numbers that correspond to the [AttributeMetadata.ColumnNumber](xref:Microsoft.Xrm.Sdk.Metadata.AttributeMetadata.ColumnNumber) for the columns that were changed.<br/><br/>**Note:** Don't use this data. Instead, use the messages to [retrieve change history](#retrieve-audit-change-history).|
|`AuditId`<br/>`auditid`<br/> **Record Id**|Unique identifier|Identifies the primary key for the audit table.|
|`CallingUserId`<br/>`callinguserid`<br/>**Calling User**|Lookup|Identifies the calling user when impersonation is used for the operation; otherwise, null.|
|`CreatedOn`<br/>`createdon`<br/>**Changed Date**|DateTime|Identifies when the audit record was created, which is when the user operation took place.|
|`ObjectId`<br/>`objectid`<br/>**Record**|Lookup|Uniquely identifies the record that was audited.|
|`ObjectTypeCode`<br/>`objecttypecode`<br/>**Entity**|EntityName|Displays the logical name of the table referred to by the `objectid` column.|
|`Operation`<br/>`operation`<br/>**Operation**|Choice|Identifies the operation that created the audit record; one of four values:<br/>1 = Create<br/>2 = Update<br/>3 = Delete<br/>4 = Access<br/>|
|`UserId`<br/>`userid`<br/>**Changed By**|Lookup|Displays the ID of the user who changed the data.|

### Audit actions

Use [Action Choices/Options](/power-apps/developer/data-platform/reference/entities/audit#action-choicesoptions) to filter for specific events. The following tables categorize the events.

#### Table row events

These events capture changes to a record.

|Value|Label|Message|Description|
|-----|-----|-------|-------|
|1|Create|`Create`|A record is created.|
|2|Update|`Update`|A record is updated.|
|3|Delete|`Delete`|A record is deleted.|
|12|Merge|`Merge`|A record is merged with another.|
|13|Assign|`Assign`|The `ownerid` column value for a user-owned table record is changed.|
|41|Set State|`SetState`|The `statecode` column value for a record is changed.|

#### Record sharing events

These events capture changes to record access when a record is shared.

|Value|Label|Message|Description|
|-----|-----|-------|-------|
|14|Share|`GrantAccess`|A user is granted privileges to a record.|
|48|Modify Share|`ModifyAccess`|The privileges granted to a user are changed.|
|49|Unshare|`RevokeAccess`|A user's access to a record is removed.|

#### Many-to-many relationship events

These events capture changes for many-to-many relationships.

|Value|Label|Message|Description|
|-----|-----|-------|-------|
|33|Associate Entities|`Associate`|One or more records are associated with another.|
|34|Disassociate Entities|`Disassociate`|One or more records are disassociated from another.|
|53|Assign Role To Team|`Associate`|A security role is assigned to a team.|
|54|Remove Role From Team|`Disassociate`|A security role is removed from a team.|
|55|Assign Role To User|`Associate`|A security role is assigned to a user.|
|56|Remove Role From User|`Disassociate`|A security role is removed from a user.|

#### User access events

These options capture the history of user access when user access auditing is enabled. The audit record for these events has an `operation` column value of 4.

|Value|Label|Description|
|-----|-----|-------|
|64|User Access via Web|User is accessing Dataverse using a model-driven app.|
|65|User Access via Web Services|User is accessing Dataverse with web services using a client other than a model-driven app.|
|112|User Access Audit Started|User access audit began.|
|113|User Access Audit Stopped|User access audit ended.|

The [Sample: Audit user access](../org-service/samples/audit-user-access.md) shows how to use these action options to audit user access.

#### Metadata change events

These events capture changes to table and column definitions as well as changes to the organization table.

|Value|Label|Description|
|-----|-----|-------|
|100|Delete Entity|User deleted a table.|
|101|Delete Attribute|User deleted a column.|
|102|Audit Change at Entity Level|User changed a table definition to enable or disable auditing.|
|103|Audit Change at Attribute Level|User changed a column definition to enable or disable auditing.|
|104|Audit Change at Org Level|User changed organization settings.|

#### Audit change events

These events capture changes to audit settings.

|Value|Label|Description|
|-----|-----|-------|
|105|Entity Audit Started|Auditing was enabled for a table.|
|106|Attribute Audit Started|Auditing was enabled for a column.|
|107|Audit Enabled|Auditing was enabled for the organization.|
|108|Entity Audit Stopped|Auditing was disabled for a table.|
|109|Attribute Audit Stopped|Auditing was disabled for an attribute.|
|110|Audit Disabled|Auditing was disabled for a column.|
|111|Audit Log Deletion|An audit log was deleted.|

#### Security role change events

These events capture changes to security roles.

|Value|Label|Message|Description|
|-----|-----|-------|-------|
|57|Add Privileges to Role|`AddPrivilegesRole`|Privileges were added to a role.|
|58|Remove Privileges From Role|`RemovePrivilegeRole`|Privileges were removed from a role.|
|59|Replace Privileges In Role|`ReplacePrivilegesRole`|Privileges for a role were replaced.|

#### Other actions

The remaining action options generally refer to auditable operations that apply to specific solutions, such as Dynamics 365 Sales, Customer Service, and Marketing.

The labels for these actions should align with an [SdkMessage.Name](../reference/entities/sdkmessage.md#BKMK_Name) value that represents the action. The specific operation may be a combination of the action name and a table. For example, an option with a value of 10 and the label **Close** should correspond to the `CloseIncident` or `CloseQuote` messages.

### Audit table relationships

The audit table has only two many-to-one relationships with the `systemuser` table:

|Relationship|Audit Table Lookup|Description |
|---------|---------|---------|
|`lk_audit_userid`|`userid`|Relates the user to all the audit records created because of changes they made.|
|`lk_audit_callinguserid`|`callinguserid`|Relates the user to any of the audit records they created while impersonating another user.|

You can use these relationships to filter audit data records created for a specific user.

The audit entity supports only one link entity in a query. Since only two relationships exist with the `systemuser` table, you can include data from either the `callinguserid` or `userid` columns, but not both at the same time.

You can't build queries using QueryExpression or FetchXml that join audit data with tables other than the two formal relationships that exist with the `systemuser` table.

### Audit EntityType definition

With the Web API, use the [audit EntityType](xref:Microsoft.Dynamics.CRM.audit) resource to read data from the audit table. The following data is the audit EntityType definition from the Web API [CSDL $metadata service document](../webapi/web-api-service-documents.md#csdl-metadata-document) without annotations.

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
  <NavigationProperty Name="callinguserid" Type="mscrm.systemuser" 
    Nullable="false" Partner="lk_audit_callinguserid">
      <ReferentialConstraint Property="_callinguserid_value" 
        ReferencedProperty="systemuserid" />
  </NavigationProperty>
  <NavigationProperty Name="userid" Type="mscrm.systemuser" 
    Nullable="false" Partner="lk_audit_userid">
      <ReferentialConstraint Property="_userid_value" 
        ReferencedProperty="systemuserid" />
  </NavigationProperty>
</EntityType>
```

> [!NOTE]
> The [ChangeData Column](../reference/entities/audit.md#BKMK_ChangeData) isn't included in the Web API [audit EntityType](xref:Microsoft.Dynamics.CRM.audit). Don't use this data. Instead, use the messages to [retrieve audit change history](#retrieve-audit-change-history).

### Example: Find contact records deleted by a user

The following examples are queries that show the audit history for contact records deleted by a specific user.

#### [Web API](#tab/webapi)

Both of the following queries return the same response.

The following query filters on the `_userid_value` property of the audit record where the value matches `<user id>`.

**Request:**

```http
GET [Organization URI]/api/data/v9.2/audits?$select=_objectid_value,objecttypecode,createdon,_userid_value&$orderby=createdon desc&$filter=operation eq 3 and objecttypecode eq 'contact' and _userid_value eq '<user id>'

Accept: application/json  
OData-MaxVersion: 4.0  
OData-Version: 4.0
If-None-Match: null
Prefer: odata.include-annotations="*" 
```

The following query accesses the collection of audit records for a specific user with the `lk_audit_userid` collection-valued navigation property from the `systemuser` table, where the `systemuserid` value matches `<user id>`.

**Request:**

```http
GET [Organization URI]/api/data/v9.2/systemusers(<user id>)/lk_audit_userid?$select=_objectid_value,objecttypecode,createdon,_userid_value&$orderby=createdon desc&$filter=operation eq 3 and objecttypecode eq 'contact'

Accept: application/json  
OData-MaxVersion: 4.0  
OData-Version: 4.0
If-None-Match: null
Prefer: odata.include-annotations="*" 
```

**Response:**

```http
HTTP/1.1 200 OK
Preference-Applied: odata.include-annotations="*"

{
  "@odata.context": "[Organization URI]/api/data/v9.2/$metadata#audits(_objectid_value,objecttypecode,createdon,_userid_value)",
  "@Microsoft.Dynamics.CRM.totalrecordcount": -1,
  "@Microsoft.Dynamics.CRM.totalrecordcountlimitexceeded": false,
  "value": [
    {
      "_objectid_value@Microsoft.Dynamics.CRM.lookuplogicalname": "contact",
      "_objectid_value": "0e76dc8a-41b5-ec11-983f-0022482bf046",
      "objecttypecode@OData.Community.Display.V1.FormattedValue": "Contact",
      "objecttypecode": "contact",
      "createdon@OData.Community.Display.V1.FormattedValue": "5/12/2022 3:19 PM",
      "createdon": "2022-05-12T22:19:12Z",
      "_userid_value@Microsoft.Dynamics.CRM.lookuplogicalname": "systemuser",
      "_userid_value@OData.Community.Display.V1.FormattedValue": "FirstName LastName",
      "_userid_value": "4026be43-6b69-e111-8f65-78e7d1620f5e"
    },
    < Other results truncated for brevity>
  ]
}

```

#### [SDK for .NET](#tab/sdk)

The following two static methods show the number of contact records the specified user deleted. These queries use aggregation, so they aren't limited to 5,000 results. However, they're limited to the higher 50,000 record limit for aggregation.


`ShowNumberContactsDeletedByUserQE` uses <xref:Microsoft.Xrm.Sdk.Query.QueryExpression>.



```csharp
/// <summary>
/// Shows the number of contacts deleted by a user.
/// </summary>
/// <param name="svc">IOrganizationService to use</param>
/// <param name="systemuserid">The user's id.</param>
static void ShowNumberContactsDeletedByUserQE(
    IOrganizationService svc,
    Guid systemuserid)
{
    var columnSet = new ColumnSet("auditid");

    //Adding Attribute expression to use aggregation
    columnSet
        .AttributeExpressions
        .Add(new XrmAttributeExpression(
            attributeName: "auditid",
            aggregateType: XrmAggregateType.Count,
            alias: "count"));

    var query =
    new QueryExpression(entityName: "audit")
    {
        ColumnSet = columnSet
    };

    query.Criteria.AddCondition(
        attributeName: "userid",
        conditionOperator: ConditionOperator.Equal,
        values: systemuserid);

    query.Criteria.AddCondition(
        attributeName: "operation",
        conditionOperator: ConditionOperator.Equal,
        values: 3);

    query.Criteria.AddCondition(
        attributeName: "objecttypecode",
        conditionOperator: ConditionOperator.Equal,
        values: "contact");

    EntityCollection records =
        svc.RetrieveMultiple(query);

    int number = (int)
        ((AliasedValue)records
        .Entities[0]["count"])
        .Value;

    Console.WriteLine(
        $"User has deleted {number} contact records");
}
```

Learn more about:

- [Build queries with QueryExpression](../org-service/build-queries-with-queryexpression.md)


`ShowNumberContactsDeletedByUserFetchXml` uses <xref:Microsoft.Xrm.Sdk.Query.FetchExpression> with a query composed using FetchXml.


```csharp
/// <summary>
/// Shows the number of contacts deleted by a user.
/// </summary>
/// <param name="svc">IOrganizationService instance to use</param>
/// <param name="systemuserid">The user's id.</param>
static void ShowNumberContactsDeletedByUserFetchXml(
IOrganizationService svc,
Guid systemuserid)
{
    string fetchXml = $@"<fetch 
    distinct='false' 
    mapping='logical' 
    aggregate='true'>
<entity name='audit'>
    <attribute name='auditid' 
        aggregate='count' 
        alias='count' />
    <filter>
        <condition attribute='userid' 
            operator='eq' 
            value='{systemuserid}' />
        <condition attribute='operation' 
            operator='eq' 
            value='3' />
        <condition attribute='objecttypecode' 
            operator='eq' 
            value='2' />
    </filter>
</entity>
</fetch>";

    int number;

    try
    {
        EntityCollection records =
        svc.RetrieveMultiple(new FetchExpression(fetchXml));

        number = (int)
            ((AliasedValue)records
            .Entities[0]["count"])
            .Value;
    }
    catch (Exception)
    {
        throw;
    }
    Console.WriteLine(
        $"User has deleted {number} contact records");
}
```

Learn more about:

- [Use FetchXML to construct a query](../use-fetchxml-construct-query.md)
- [Use FetchXML aggregation](../use-fetchxml-aggregation.md)

---

## Retrieve audit change history

You can use any of three messages to retrieve data changes that are audited.

|Web API |SDK for .NET |Description|
|---------|---------|---------|
|[RetrieveAuditDetails Function](xref:Microsoft.Dynamics.CRM.RetrieveAuditDetails)|[RetrieveAuditDetailsRequest Class>](xref:Microsoft.Crm.Sdk.Messages.RetrieveAuditDetailsRequest)|Retrieve the full audit details from an audit record.|
|[RetrieveAttributeChangeHistory Function](xref:Microsoft.Dynamics.CRM.RetrieveAttributeChangeHistory)|[RetrieveAttributeChangeHistoryRequest Class](xref:Microsoft.Crm.Sdk.Messages.RetrieveAttributeChangeHistoryRequest)|Retrieve the change history for a single column of an audited record.|
|[RetrieveRecordChangeHistory Function](xref:Microsoft.Dynamics.CRM.RetrieveRecordChangeHistory)|[RetrieveRecordChangeHistoryRequest Class](xref:Microsoft.Crm.Sdk.Messages.RetrieveRecordChangeHistoryRequest)|Retrieve all audited data changes for a specific record.|

To use these messages, [make sure you have the `prvReadRecordAuditHistory` and `prvReadAuditSummary` privileges](../security-access-coding.md#example-check-whether-a-user-has-a-privilege).

### AuditDetail types

These messages provide more details that depend on the type of action. The details are implemented using types that are derived from a base `AuditDetail` type, as shown in the following table.

|Web API|SDK for .NET|Description|
|---------|---------|---------|
|[AuditDetail ComplexType](xref:Microsoft.Dynamics.CRM.AuditDetail)|[AuditDetail Class](xref:Microsoft.Crm.Sdk.Messages.AuditDetail)|Displays the base type for the derived classes. Provides access to the audit record.|
|[AttributeAuditDetail ComplexType](xref:Microsoft.Dynamics.CRM.AttributeAuditDetail)|[AttributeAuditDetail Class](xref:Microsoft.Crm.Sdk.Messages.AttributeAuditDetail)|Provides details when data changes occur for a record. Provides access to old values and new values.<br/>Returned by the following types of actions:<br/>- [Table row events](#table-row-events)<br/>- [Metadata change events](#metadata-change-events)<br/>- [Audit change events](#audit-change-events)|
|[RelationshipAuditDetail ComplexType](xref:Microsoft.Dynamics.CRM.RelationshipAuditDetail)|[RelationshipAuditDetail Class](xref:Microsoft.Crm.Sdk.Messages.RelationshipAuditDetail)|Provides details when records are associated or disassociated using a many-to-many relationship. Provides the name of the relationship and a list of the records the operation changed.<br/>Returned by [many-to-many relationship events](#many-to-many-relationship-events).|
|[RolePrivilegeAuditDetail ComplexType](xref:Microsoft.Dynamics.CRM.RolePrivilegeAuditDetail)|[RolePrivilegeAuditDetail Class](xref:Microsoft.Crm.Sdk.Messages.RolePrivilegeAuditDetail)|Provides details when the definitions of [Security Role (Role)](../reference/entities/role.md) records change. Provides information about the old and new role privileges associated with the role.<br/>Returned by [security role change events](#security-role-change-events).|
|[ShareAuditDetail ComplexType](xref:Microsoft.Dynamics.CRM.ShareAuditDetail)|[ShareAuditDetail Class](xref:Microsoft.Crm.Sdk.Messages.ShareAuditDetail)|Provides details when a record is shared or unshared or when the level of access to a shared record changes.<br/> Returned by [record sharing events](#record-sharing-events).|
|[UserAccessAuditDetail ComplexType](xref:Microsoft.Dynamics.CRM.UserAccessAuditDetail)|[UserAccessAuditDetail Class>](xref:Microsoft.Crm.Sdk.Messages.UserAccessAuditDetail)|Provides details to track user access auditing. Provides details on the interval and access time.<br/> Returned by [user access events](#user-access-events).|

> [!IMPORTANT]
>
> - The Web API types listed earlier that inherit from [AuditDetail ComplexType](xref:Microsoft.Dynamics.CRM.AuditDetail) don't return the `AuditRecord` navigation property value they should inherit from `AuditDetail`. The SDK for .NET classes returns this data.
>
> - Large column values included in `AttributeAuditDetail` `OldValue` or `NewValue` properties such as [Email.Description](../reference/entities/email.md#BKMK_Description) or [Annotation](../reference/entities/annotation.md) are capped at 5KB or about 5,000 characters. A capped column value can be recognized by an ellipsis (&hellips;) at the end of the text; for example, "lorem ipsum, lorem ip…" Because the data is truncated, you can't use it to restore changes to these column values.

### RetrieveAuditDetails message

Use this message to retrieve the audit details for a single audit record.

# [Web API](#tab/webapi)

<xref:Microsoft.Dynamics.CRM.RetrieveAuditDetails> is a function bound to the audit table. Include the `Prefer: odata.include-annotations="*"` request header to get [formatted values](../webapi/query-data-web-api.md#formatted-values).

The following example shows the [AttributeAuditDetail ComplexType](xref:Microsoft.Dynamics.CRM.AttributeAuditDetail) returned when the `parentaccountid` is set on an `account` record.

**Request:**

```http
GET [Organization URI]/api/data/v9.2/audits(12869c65-d7d3-ec11-b656-281878f0eba9)/Microsoft.Dynamics.CRM.RetrieveAuditDetails

Accept: application/json  
OData-MaxVersion: 4.0  
OData-Version: 4.0
If-None-Match: null
Prefer: odata.include-annotations="*" 
```

**Response:**

```http
HTTP/1.1 200 OK
OData-Version: 4.0
Preference-Applied: odata.include-annotations="*"

{
 "@odata.context": "[Organization URI]/api/data/v9.2/$metadata#Microsoft.Dynamics.CRM.RetrieveAuditDetailsResponse",
 "AuditDetail": {
  "@odata.type": "#Microsoft.Dynamics.CRM.AttributeAuditDetail",
  "InvalidNewValueAttributes": [],
  "LocLabelLanguageCode": 0,
  "DeletedAttributes": {
   "Count": 0,
   "Keys": [],
   "Values": []
  },
  "OldValue": {
   "@odata.type": "#Microsoft.Dynamics.CRM.account"
  },
  "NewValue": {
   "@odata.type": "#Microsoft.Dynamics.CRM.account",
   "_parentaccountid_value@OData.Community.Display.V1.FormattedValue": "A. Datum Corporation",
   "_parentaccountid_value@Microsoft.Dynamics.CRM.associatednavigationproperty": "parentaccountid",
   "_parentaccountid_value@Microsoft.Dynamics.CRM.lookuplogicalname": "account",
   "_parentaccountid_value": "d249d106-38b5-ec11-983f-002248296cd0"
  }
 }
}
```

Learn more about:

- [RetrieveAuditDetails Function](xref:Microsoft.Dynamics.CRM.RetrieveAuditDetails)
- [RetrieveAuditDetailsResponse ComplexType](xref:Microsoft.Dynamics.CRM.RetrieveAuditDetailsResponse)

# [SDK for .NET](#tab/sdk)

The following `ShowAuditDetail` static method returns audit details for any type of audit details that can be tracked by an audit record.

```csharp
/// <summary>
/// Returns audit details for the specified audit record
/// </summary>
/// <param name="svc">The IOrganizationService instance to use.</param>
/// <param name="auditid">The auditid for the audit record.</param>
static void ShowAuditDetail(
    IOrganizationService svc,
    Guid auditid)
{

    RetrieveAuditDetailsRequest req =
                new RetrieveAuditDetailsRequest
                {
                    AuditId = auditid
                };

    RetrieveAuditDetailsResponse resp =
        (RetrieveAuditDetailsResponse)svc.Execute(req);

    DisplayAuditDetail(resp.AuditDetail);
}
```

#### DisplayAuditDetail method

The `DisplayAuditDetail` static method outputs different details to the console depending on the type of audit detail. This method is used by other SDK for .NET samples on this page.



```csharp
/// <summary>
/// Displays properties of the different classes derived from AuditDetail
/// </summary>
/// <param name="auditDetail">The instance of a type derived from AuditDetail</param>
static void DisplayAuditDetail(AuditDetail auditDetail)
{
    switch (auditDetail)
    {
        case AttributeAuditDetail aad:

            Entity oldRecord = aad.OldValue;
            Entity newRecord = aad.NewValue;
            List<string> oldKeys = new List<string>();

            //Look for changed or deleted values that are included in the OldValue collection
            oldRecord.Attributes.Keys.ToList().ForEach(k =>
            {
                if (oldRecord.FormattedValues.Keys.Contains(k))
                {
                    if (newRecord.FormattedValues.Contains(k))
                    {
                        Console.WriteLine(
                            $"\tChange:{k}:{oldRecord.FormattedValues[k]} => " +
                            $"{newRecord.FormattedValues[k]}");
                    }
                    else
                    {

                        Console.WriteLine($"\tDeleted:{k}:" +
                            $"{oldRecord.FormattedValues[k]}");
                    }
                }
                else
                {
                    if (newRecord.Attributes.Keys.Contains(k))
                    {

                        Console.WriteLine($"\tChange:{k}:{oldRecord[k]} => " +
                            $"{newRecord[k]}");
                    }
                    else
                    {
                        Console.WriteLine($"\tDeleted:{k}:{oldRecord[k]}");
                    }
                }

                oldKeys.Add(k); //Add to list so we don't check again
            });

            //Look for New values that are only in the NewValues collection
            newRecord.Attributes.Keys.ToList().ForEach(k =>
            {
                if (!oldKeys.Contains(k))//Exclude any keys for changed or deleted values
                {
                    if (newRecord.FormattedValues.Keys.Contains(k))
                    {
                        Console.WriteLine($"\tNew Value:{k} => " +
                            $"{newRecord.FormattedValues[k]}");
                    }
                    else
                    {
                        Console.WriteLine($"\tNew Value:{k}:{newRecord[k]}");
                    }
                }
            });
            break;

        case ShareAuditDetail sad:
            Console.WriteLine($"\tUser: {sad.Principal.Name}");
            Console.WriteLine($"\tOld Privileges: {sad.OldPrivileges}");
            Console.WriteLine($"\tNew Privileges: {sad.NewPrivileges}");
            break;

        //Applies to operations on N:N relationships
        case RelationshipAuditDetail rad:
            Console.WriteLine($"\tRelationship Name :{rad.RelationshipName }");
            Console.WriteLine($"\tRecords:");
            rad.TargetRecords.ToList().ForEach(y =>
            {
                Console.WriteLine($"\tTarget Record :{y.Name}");
            });
            break;

        //Only applies to role record
        case RolePrivilegeAuditDetail rpad:

            List<string> newRolePrivileges = new List<string>();
            rpad.NewRolePrivileges.ToList().ForEach(y =>
            {
                if (y != null)
                {
                    newRolePrivileges.Add(
                    $"\t\tPrivilege Id:{y.PrivilegeId} Depth:{y.Depth}\n");
                }
            });

            List<string> oldRolePrivileges = new List<string>();
            rpad.OldRolePrivileges.ToList().ForEach(y =>
            {
                if (y != null)
                {
                    oldRolePrivileges.Add(
                    $"\t\tPrivilege Id:{(y.PrivilegeId)} Depth:{y.Depth}\n");
                }
            });

            List<string> invalidNewPrivileges = new List<string>();
            rpad.InvalidNewPrivileges.ToList().ForEach(y =>
            {
                if (y != null)
                {
                    invalidNewPrivileges.Add(
                    $"\t\tGuid:{y}\n");
                }
            });

            Console.WriteLine($"\tNew Role Privileges:\n{string.Join(string.Empty, newRolePrivileges.ToArray())}");
            Console.WriteLine($"\tOld Role Privileges:\n{string.Join(string.Empty, oldRolePrivileges.ToArray())}");
            Console.WriteLine($"\tInvalid New Privileges:\n{string.Join(string.Empty, invalidNewPrivileges.ToArray())}"); ;
            break;

        //Only applies for systemuser record
        case UserAccessAuditDetail uaad:
            Console.WriteLine($"\tAccess Time:{uaad.AccessTime}");
            Console.WriteLine($"\tInterval:{uaad.Interval}");
            break;
    }
}
```

Learn more about:

- [RetrieveAuditDetailsRequest Class](xref:Microsoft.Crm.Sdk.Messages.RetrieveAuditDetailsRequest)
- [RetrieveAuditDetailsResponse Class](xref:Microsoft.Crm.Sdk.Messages.RetrieveAuditDetailsResponse)
- [IOrganizationService.Execute Method](xref:Microsoft.Xrm.Sdk.IOrganizationService.Execute%2A)

---

### RetrieveAttributeChangeHistory Message

Use this message to retrieve a list of changes for a specific table column.

Use the `PagingInfo` parameter to control the number of records to return and move forward or backward through the pages. For subsequent requests, set the `PagingInfo.PagingCookie` property to the value returned by the `AuditDetailCollection.PagingCookie`.

Changes for this message are always `AttributeAuditDetail` types.

#### [Web API](#tab/webapi)

This example returns a single audited change history for the `description` column of an `account` table record.

**Request:**

```http
GET [Organization URI]/api/data/v9.2/RetrieveAttributeChangeHistory(Target=@target,AttributeLogicalName=@attributeLogicalName,PagingInfo=@paginginfo)?
@target={ '@odata.id':'accounts(611e7713-68d7-4622-b552-85060af450bc)'}
&@attributeLogicalName='description'
&@paginginfo={
   "PageNumber": 1,
   "Count": 1,
   "ReturnTotalRecordCount": true
}

Accept: application/json  
OData-MaxVersion: 4.0  
OData-Version: 4.0
If-None-Match: null
```

**Response:**

```http
HTTP/1.1 200 OK

{
 "@odata.context": "[Organization URI]/api/data/v9.2/$metadata#Microsoft.Dynamics.CRM.RetrieveAttributeChangeHistoryResponse",
 "AuditDetailCollection": {
  "MoreRecords": true,
  "PagingCookie": "<cookie page=\"1\"><cookieExtensions ContinuationToken=\"{&quot;pageNumber&quot;:2,&quot;continuationToken&quot;:&quot;[{\\&quot;compositeToken\\&quot;:{\\&quot;token\\&quot;:null,\\&quot;range\\&quot;:{\\&quot;min\\&quot;:\\&quot;3A800000000000000000000000000000\\&quot;,\\&quot;max\\&quot;:\\&quot;3B000000000000000000000000000000\\&quot;}},\\&quot;orderByItems\\&quot;:[{\\&quot;item\\&quot;:\\&quot;2022-05-13T22:06:46.6175613Z\\&quot;}],\\&quot;rid\\&quot;:\\&quot;CVoNAJIidnNsmz0AAADwAw==\\&quot;,\\&quot;skipCount\\&quot;:0,\\&quot;filter\\&quot;:null}]&quot;}\" /></cookie>",
  ,
  "TotalRecordCount": 3,
  "AuditDetails": [
   {
    "@odata.type": "#Microsoft.Dynamics.CRM.AttributeAuditDetail",
    "InvalidNewValueAttributes": [],
    "LocLabelLanguageCode": 0,
    "DeletedAttributes": {
     "Count": 0,
     "Keys": [],
     "Values": []
    },
    "OldValue": {
     "@odata.type": "#Microsoft.Dynamics.CRM.account",
     "description": "Old description value"
    },
    "NewValue": {
     "@odata.type": "#Microsoft.Dynamics.CRM.account",
     "description": "New description value"
    }
   }
  ]
 }
}
```

Learn more about:

- [RetrieveAttributeChangeHistory Function](xref:Microsoft.Dynamics.CRM.RetrieveAttributeChangeHistory)
- [RetrieveAttributeChangeHistoryResponse ComplexType](xref:Microsoft.Dynamics.CRM.RetrieveAttributeChangeHistoryResponse)
- [AuditDetailCollection ComplexType](xref:Microsoft.Dynamics.CRM.AuditDetailCollection)

#### [SDK for .NET](#tab/sdk)

The `ShowAttributeChangeHistory` static method returns the first 20 audited changes for the specified column in the specified record.

This method depends on the example [DisplayAuditDetail method](#displayauditdetail-method) included in the [RetrieveAuditDetails Message](#retrieveauditdetails-message) example on this page.

```csharp
/// <summary>
/// Returns up to 20 audited changes for the specified column of a specified record.
/// </summary>
/// <param name="svc">The IOrganizationService instance to use.</param>
/// <param name="target">The specified record.</param>
/// <param name="columnLogicalName">The specified column.</param>
static void ShowAttributeChangeHistory(IOrganizationService svc,
            EntityReference target,
            string columnLogicalName)
{
    RetrieveAttributeChangeHistoryRequest req =
        new RetrieveAttributeChangeHistoryRequest
        {
            Target = target,
            AttributeLogicalName = columnLogicalName,
            PagingInfo = new PagingInfo
            {
                PageNumber = 1,
                Count = 20,
                ReturnTotalRecordCount = true
            }
        };

    RetrieveAttributeChangeHistoryResponse resp =
        (RetrieveAttributeChangeHistoryResponse)svc.Execute(req);
    var auditDetailCollection = resp.AuditDetailCollection;

    int recordsReturned = auditDetailCollection.AuditDetails.Count;
    int totalRecords = auditDetailCollection.TotalRecordCount;
    Console.WriteLine($"Retrieved {recordsReturned} of " +
        $"{totalRecords} auditdetail records.");

    auditDetailCollection.AuditDetails.ToList().ForEach(x =>
    {

        Entity auditRecord = x.AuditRecord;

        Console.WriteLine($"Change Date: " +
            $"{auditRecord.FormattedValues["createdon"]}");
        Console.WriteLine($"Change By: " +
            $"{((EntityReference)auditRecord["userid"]).Name}");
        Console.WriteLine($"Action: " +
            $"{auditRecord.FormattedValues["action"]}");
        Console.WriteLine($"Operation: " +
            $"{auditRecord.FormattedValues["operation"]}");

        DisplayAuditDetail(auditDetail: x);

        Console.WriteLine();
    });
}
```

Learn more about:

- [RetrieveAttributeChangeHistoryRequest Class](xref:Microsoft.Crm.Sdk.Messages.RetrieveAttributeChangeHistoryRequest)
- [RetrieveAttributeChangeHistoryResponse Class](xref:Microsoft.Crm.Sdk.Messages.RetrieveAttributeChangeHistoryResponse)
- [IOrganizationService.Execute Method](xref:Microsoft.Xrm.Sdk.IOrganizationService.Execute%2A)

---

### RetrieveRecordChangeHistory Message

The `RetrieveRecordChangeHistory` message shows the history of data changes for the record indicated by the `Target` parameter.

Use the `PagingInfo` parameter to control the number of records to return and move forward or backward through the pages. For subsequent requests, set the `PagingInfo.PagingCookie` property to the value returned by the `AuditDetailCollection.PagingCookie`.

The results of this message are commonly seen as the `AttributeAuditDetail` data displayed in model-driven apps when you select **Related** > **Audit history**. It shows the old values and the new values of the records, but it also returns `RelationshipAuditDetail` and `ShareAuditDetail` types.

This message can also be used with the `systemuser` and `role` tables to return `RolePrivilegeAuditDetail` and `UserAccessAuditDetail` types.

#### [Web API](#tab/webapi)

The following example returns just the first two of four changes to an account record.

**Request:**

```http
GET [Organization URI]/api/data/v9.2/RetrieveRecordChangeHistory(Target=@target,PagingInfo=@paginginfo)?
@target={ '@odata.id':'accounts(611e7713-68d7-4622-b552-85060af450bc)'}
&@paginginfo={
   "PageNumber": 1,
   "Count": 2,
   "ReturnTotalRecordCount": true
}
Accept: application/json  
OData-MaxVersion: 4.0  
OData-Version: 4.0
If-None-Match: null
```

**Response:**

```http
HTTP/1.1 200 OK

{
 "@odata.context": "[Organization URI]/api/data/v9.2/$metadata#Microsoft.Dynamics.CRM.RetrieveRecordChangeHistoryResponse",
 "AuditDetailCollection": {
  "MoreRecords": true,
  "PagingCookie": "<cookie page=\"1\"><cookieExtensions ContinuationToken=\"{&quot;pageNumber&quot;:2,&quot;continuationToken&quot;:&quot;[{\\&quot;compositeToken\\&quot;:{\\&quot;token\\&quot;:null,\\&quot;range\\&quot;:{\\&quot;min\\&quot;:\\&quot;38000000000000000000000000000000\\&quot;,\\&quot;max\\&quot;:\\&quot;38800000000000000000000000000000\\&quot;}},\\&quot;orderByItems\\&quot;:[{\\&quot;item\\&quot;:\\&quot;2022-05-13T22:06:27.8029732Z\\&quot;}],\\&quot;rid\\&quot;:\\&quot;CVoNAJIidnPOnT0AAAAICA==\\&quot;,\\&quot;skipCount\\&quot;:0,\\&quot;filter\\&quot;:null}]&quot;}\" /></cookie>",
  "TotalRecordCount": 4,
  "AuditDetails": [
   {
    "@odata.type": "#Microsoft.Dynamics.CRM.AttributeAuditDetail",
    "InvalidNewValueAttributes": [],
    "LocLabelLanguageCode": 0,
    "DeletedAttributes": {
     "Count": 0,
     "Keys": [],
     "Values": []
    },
    "OldValue": {
     "@odata.type": "#Microsoft.Dynamics.CRM.account",
     "description": "Old description value"
    },
    "NewValue": {
     "@odata.type": "#Microsoft.Dynamics.CRM.account",
     "description": "New description value"
    }
   },
   {
    "@odata.type": "#Microsoft.Dynamics.CRM.AttributeAuditDetail",
    "InvalidNewValueAttributes": [],
    "LocLabelLanguageCode": 0,
    "DeletedAttributes": {
     "Count": 0,
     "Keys": [],
     "Values": []
    },
    "OldValue": {
     "@odata.type": "#Microsoft.Dynamics.CRM.account",
     "_ownerid_value@OData.Community.Display.V1.FormattedValue": "FirstName LastName",
     "_ownerid_value@Microsoft.Dynamics.CRM.associatednavigationproperty": "ownerid",
     "_ownerid_value@Microsoft.Dynamics.CRM.lookuplogicalname": "systemuser",
     "_ownerid_value": "4026be43-6b69-e111-8f65-78e7d1620f5e"
    },
    "NewValue": {
     "@odata.type": "#Microsoft.Dynamics.CRM.account",
     "_ownerid_value@OData.Community.Display.V1.FormattedValue": "TeamName",
     "_ownerid_value@Microsoft.Dynamics.CRM.associatednavigationproperty": "ownerid",
     "_ownerid_value@Microsoft.Dynamics.CRM.lookuplogicalname": "team",
     "_ownerid_value": "39e0dbe4-131b-e111-ba7e-78e7d1620f5e"
    }
   }
  ]
 }
}
```

> [!NOTE]
> The [AuditDetail ComplexType](xref:Microsoft.Dynamics.CRM.AuditDetail) values returned don't include the `AuditRecord` property, so no data about who made the change and when it was made is available.

Learn more about:

- [RetrieveRecordChangeHistory Function](xref:Microsoft.Dynamics.CRM.RetrieveRecordChangeHistory)
- [RetrieveRecordChangeHistoryResponse ComplexType](xref:Microsoft.Dynamics.CRM.RetrieveRecordChangeHistoryResponse)
- [PagingInfo ComplexType](xref:Microsoft.Dynamics.CRM.PagingInfo)

#### [SDK for .NET](#tab/sdk)

This `ShowRetrieveRecordChangeHistory` static method executes the `RetrieveRecordChangeHistory` message for a specified record and processes the response.

For each audit record, it displays the properties and uses the example [DisplayAuditDetail method](#displayauditdetail-method) defined in the [RetrieveAuditDetails Message](#retrieveauditdetails-message) on this page to display the details.

```csharp
/// <summary>
/// Shows the results of the RetrieveRecordChangeHistory message
/// </summary>
/// <param name="svc">The IOrganizationService instance to use</param>
/// <param name="record">A reference to a record of a table enabled for auditing</param>
static void ShowRetrieveRecordChangeHistory(
    IOrganizationService svc, 
    EntityReference record)
{
    var req = new RetrieveRecordChangeHistoryRequest
    {
        Target = record,
        PagingInfo = new PagingInfo
        {
            PageNumber = 1,
            Count = 20,
            ReturnTotalRecordCount = true
        }
    };

    var resp = (RetrieveRecordChangeHistoryResponse)svc.Execute(req);
    var auditDetailCollection = resp.AuditDetailCollection;

    int recordsReturned = auditDetailCollection.AuditDetails.Count;
    int totalRecords = auditDetailCollection.TotalRecordCount;
    Console.WriteLine($"Retrieved {recordsReturned} of {totalRecords} auditdetail records.");

    auditDetailCollection.AuditDetails.ToList().ForEach(x =>
    {

        Entity auditRecord = x.AuditRecord;

        Console.WriteLine($"Change Date: {auditRecord.FormattedValues["createdon"]}");
        Console.WriteLine($"Change By: {((EntityReference)auditRecord["userid"]).Name}");
        Console.WriteLine($"Action: {auditRecord.FormattedValues["action"]}");
        Console.WriteLine($"Operation: {auditRecord.FormattedValues["operation"]}");

        DisplayAuditDetail(auditDetail: x);
        
        Console.WriteLine();
    });
}
```

Learn more about:

- [RetrieveRecordChangeHistoryRequest Class](xref:Microsoft.Crm.Sdk.Messages.RetrieveRecordChangeHistoryRequest)
- [RetrieveRecordChangeHistoryResponse Class](xref:Microsoft.Crm.Sdk.Messages.RetrieveRecordChangeHistoryResponse)
- [PagingInfo Class](xref:Microsoft.Xrm.Sdk.Query.PagingInfo)
- [IOrganizationService.Execute Method](xref:Microsoft.Xrm.Sdk.IOrganizationService.Execute%2A)
- [Sample: Audit table data changes](../org-service/samples/audit-entity-data-changes.md).

---

### See also

[Auditing overview](overview.md)  
[Configure auditing](configure.md)  
[Delete audit data](delete-audit-data.md)  
[Manage Dataverse auditing](/power-platform/admin/manage-dataverse-auditing)  
[Sample: Audit table data changes](../org-service/samples/audit-entity-data-changes.md)  
[Sample: Audit user access](../org-service/samples/audit-user-access.md)

[!INCLUDE [footer-banner](../../../includes/footer-banner.md)]
