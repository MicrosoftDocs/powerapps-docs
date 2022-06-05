---
title: "Retrieve the history of audited data changes (Microsoft Dataverse) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "Describes how to programmatically retrieve the audit change history." # 115-145 characters including spaces. This abstract displays in the search result.
ms.date: 06/03/2022
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

After auditing is enabled and data changes are made to those tables and columns being audited, you can retrieve the data change history.

> [!NOTE]
> Audit data is not available using the Dataverse TDS (SQL) endpoint. More information: [Use SQL to query data](../dataverse-sql-query.md)

## Audit table

Data for auditing events is in the [Auditing (Audit) table](../reference/entities/audit.md). In the Web API the <xref:Microsoft.Dynamics.CRM.audit?text=audit EntityType> is the resource for this data. The audit table is read-only.

The audit table provides the data for the **View Audit Summary** displayed in the Power Platform admin center. More information: [Administrators Guide: View audit logging details](/power-platform/admin/audit-data-user-activity#view-audit-logging-details)

Calling user must have the `prvReadAuditSummary` privilege to retrieve data from this table. More information: [Example: Check whether a user has a privilege](../security-access-coding.md#example-check-whether-a-user-has-a-privilege)

The following table summarizes important columns in the audit table.

|SchemaName<br />LogicalName<br />DisplayName  |Type  |Description  |
|---------|---------|---------|
|`Action`<br />`action`<br />**Event**|Choice|Options that represent the event that caused the change. More information: [Actions](#audit-actions)|
|`AttributeMask`<br />`attributemask`<br />**Changed Field**|Memo| When the change represents a data change to a record, contains a comma separated list of numbers that correspond to the <xref:Microsoft.Xrm.Sdk.Metadata.AttributeMetadata>.<xref:Microsoft.Xrm.Sdk.Metadata.AttributeMetadata.ColumnNumber> for the columns changed in the transaction for the action.<br /><br />**Note:** Rather han try to use this data, use the messages to retrieve change history. More information: [Retrieve audit change history](#retrieve-audit-change-history) |
|`AuditId`<br />`auditid`<br /> **Record Id**|Unique Identifier|The primary key for the audit table.|
|`CallingUserId`<br />`callinguserid`<br />**Calling User**|Lookup|The calling user when impersonation is used for the operation. Otherwise null. |
|`CreatedOn`<br />`createdon`<br />**Changed Date**|DateTime|When the audit record was created, which is when the user operation took place.|
|`ObjectId`<br />`objectid`<br />**Record**|Lookup|The unique identifier for the record that was audited.|
|`ObjectTypeCode`<br />`objecttypecode`<br />**Entity**|EntityName|The logical name of the table referred to by the `objectid` column.|
|`Operation`<br />`operation`<br />**Operation**|Choice|The operation that caused the audit record. One of 4 values:<br />1 = Create<br />2 = Update<br />3 = Delete<br />4 = Access<br />|
|`UserId`<br />`userid`<br />**Changed By**|Lookup|The Id of the user who caused the change.|

### Audit Actions

At the time this topic was written there were 74 options in the [Action Choices/Options](/power-apps/developer/data-platform/reference/entities/audit#action-choicesoptions) which correspond to events in the system. You can use these to filter for specific events.

The following groups categorize these events.

#### Table row events

These events capture changes to a record.

|Value|Label|Message|Description|
|-----|-----|-------|-------|
|1|Create |`Create`|A record is created.|
|2|Update|`Update`|A record is updated.|
|3|Delete|`Delete`|A record is deleted.|
|12|Merge|`Merge`|A record is merged with another.|
|13|Assign|`Assign`|The `ownerid` column value for a user-owned table record is changed.|
|41|Set State|`SetState`|The `statecode` column value for a record is changed.|

#### Record Sharing events

These events capture changes to record access when a record is shared.

|Value|Label|Message|Description|
|-----|-----|-------|-------|
|14|Share|`GrantAccess`|A user is granted privileges to a record.|
|48|Modify Share|`ModifyAccess`|The privileges granted to a user changes.|
|49|Unshare|`RevokeAccess`|A user's access to a record is removed.|

#### Many-to-Many relationship events

These events capture changes when data changes for Many-to-Many relationships.

|Value|Label|Message|Description|
|-----|-----|-------|-------|
|33|Associate Entities|`Associate`|One or more records are associated to another.|
|34|Disassociate Entities|`Disassociate`|One or more records are disassociated from another.|
|53|Assign Role To Team|`Associate`|A security role is assigned to a team.|
|54|Remove Role From Team|`Disassociate`|A security role is removed from a team.|
|55|Assign Role To User|`Associate`|A security role is assigned to a user.|
|56|Remove Role From User|`Disassociate`|A security role is removed from a user.|


#### User Access Events

These options are used to capture history of user access when user access auditing is enabled. The audit record for these events will have the `operation` column value of 4.

|Value|Label|Description|
|-----|-----|-------|
|64|User Access via Web|User is accessing Dataverse using a model-driven app.|
|65|User Access via Web Services|User is accessing Dataverse using web services using a client other than a model-driven app.|
|112|User Access Audit Started|User access audit began.|
|113|User Access Audit Stopped|User access audit ended.|

For a SDK for .NET sample showing use of these action options, see [Sample: Audit user access](../org-service/samples/audit-user-access.md).

#### Metadata change events

These events capture changes to table and column definitions as well as changes to the organization table.

|Value|Label|Description|
|-----|-----|-------|
|100|Delete Entity|User deleted a table.|
|101|Delete Attribute|User deleted a column.|
|102|Audit Change at Entity Level|User changed a table definition to enable or disable auditing.|
|103|Audit Change at Attribute Level|User changed a column definition to enable or disable auditing.|
|104|Audit Change at Org Level|A change was made to organization settings.|

#### Audit change events

These events capture changes to audit settings.

|Value|Label|Description|
|-----|-----|-------|
|105|Entity Audit Started|A table was enabled for auditing.|
|106|Attribute Audit Started|A column was enabled for auditing.|
|107|Audit Enabled|Auditing was enabled for the organization.|
|108|Entity Audit Stopped|A table was disabled for auditing.|
|109|Attribute Audit Stopped|Auditing was disabled for |
|110|Audit Disabled|A column was disabled for auditing.|
|111|Audit Log Deletion|An audit log was deleted.|

#### Security Role change events

|Value|Label|Message|Description|
|-----|-----|-------|-------|
|57|Add Privileges to Role|`AddPrivilegesRole`|Privileges added to a role.|
|58|Remove Privileges From Role|`RemovePrivilegeRole`|Privileges removed from a role.|
|59|Replace Privileges In Role|`ReplacePrivilegesRole`|Privileges for a role are replaced.|

#### Other Actions

The remaining action options will generally refer to auditable operations that apply to specific solutions, such as Dynamics 365 Sales, Dynamics 365 Customer Service, and Dynamics 365 Marketing.

The labels for these actions should align to an [SdkMessage.Name](../reference/entities/sdkmessage.md#BKMK_Name) value that represents the action. The specific operation may be a combination of the action name and a table. For example, option with value 10 and label **Close** should correspond to the `CloseIncident` or `CloseQuote` messages.

### audit table relationships

The audit table has only two Many-to-One relationships with the `systemuser` table:

|Relationship|Audit Table Lookup|Description  |
|---------|---------|---------|
|`lk_audit_userid`|`userid`|Relates the user to all the audit records created because of changes they made.|
|`lk_audit_callinguserid`|`callinguserid`|Relates the user to any of the audit records they created while impersonating another user.|

You can use these relationships to filter audit data records created for a specific user.

> [!NOTE]
> The audit entity supports only one link entity in a query. Since only two relationships exist with the `systemuser` table, this means you can include data from either the `callinguserid` or `userid` columns, but not both at the same time.
> You cannot build queries using QueryExpression or FetchXml that join audit data with tables other than the two formal relationships that exist with the `systemuser` table.


### audit EntityType definition

With the Web API, you will use the <xref:Microsoft.Dynamics.CRM.audit?text=audit EntityType> resource to read data from the `audit` table. The following is the **EntityType** definition Web API $metadata service document without annotations:

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

More information: [CSDL $metadata document](../webapi/web-api-service-documents.md#csdl-metadata-document)

> [!NOTE]
> The [ChangeData Column](../reference/entities/audit.md#BKMK_ChangeData) is not included in the Web API <xref:Microsoft.Dynamics.CRM.audit?text=audit EntityType>. Rather than try to use this data, use the messages to retrieve change history. More information: [Retrieve audit change history](#retrieve-audit-change-history).


### Example: Find Contact records deleted by a user

The following examples are queries showing audit history for contact records deleted by a specific user.

# [Web API](#tab/webapi)

Both of the following queries return the same response.

The following one filters on the `_userid_value` property of the audit record where the value matches `<user id>`.

**Request**

```http
GET [Organization URI]/api/data/v9.2/audits?$select=_objectid_value,objecttypecode,createdon,_userid_value&$orderby=createdon desc&$filter=operation eq 3 and objecttypecode eq 'contact' and _userid_value eq '<user id>' HTTP/1.1

Accept: application/json  
OData-MaxVersion: 4.0  
OData-Version: 4.0
If-None-Match: null
Prefer: odata.include-annotations="*" 
```

The following one accesses the collection of audit records for a specific user with the `lk_audit_userid` collection-valued navigation property from the `systemuser` table where the `systemuserid` value matches `<user id>`

**Request**

```http
GET [Organization URI]/api/data/v9.2/systemusers(<user id>)/lk_audit_userid?$select=_objectid_value,objecttypecode,createdon,_userid_value&$orderby=createdon desc&$filter=operation eq 3 and objecttypecode eq 'contact' HTTP/1.1

Accept: application/json  
OData-MaxVersion: 4.0  
OData-Version: 4.0
If-None-Match: null
Prefer: odata.include-annotations="*" 
```


**Response**

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

# [SDK for .NET](#tab/sdk)

There are two static methods below that show the number of deleted contact records for the specified user. These queries use aggregation so they are not limited to 5,000 results. But they are limited to the higher 50,000 record limit for aggregation.

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

More information: [Build queries with QueryExpression](../org-service/build-queries-with-queryexpression.md)

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

More information:

- [Use FetchXML to construct a query](../use-fetchxml-construct-query.md)
- [Use FetchXML aggregation](../use-fetchxml-aggregation.md)

---

## Retrieve audit change history

There are three messages you can use to retrieve data changes that are audited.

|Web API  |SDK for .NET  |Description |
|---------|---------|---------|
|<xref:Microsoft.Dynamics.CRM.RetrieveAuditDetails?text=RetrieveAuditDetails Function>|<xref:Microsoft.Crm.Sdk.Messages.RetrieveAuditDetailsRequest?text=RetrieveAuditDetailsRequest Class>|Retrieve the full audit details from an audit record.|
|<xref:Microsoft.Dynamics.CRM.RetrieveAttributeChangeHistory?text=RetrieveAttributeChangeHistory Function>|<xref:Microsoft.Crm.Sdk.Messages.RetrieveAttributeChangeHistoryRequest?text=RetrieveAttributeChangeHistoryRequest Class>|Retrieves the change history for an single column of an audited record.|
|<xref:Microsoft.Dynamics.CRM.RetrieveRecordChangeHistory?text=RetrieveRecordChangeHistory Function>|<xref:Microsoft.Crm.Sdk.Messages.RetrieveRecordChangeHistoryRequest?text=RetrieveRecordChangeHistoryRequest Class>|Retrieve all audited data changes for a specific record.|

To use these messages you must have the `prvReadRecordAuditHistory` and `prvReadAuditSummary` privileges. More information: [Example: Check whether a user has a privilege](../security-access-coding.md#example-check-whether-a-user-has-a-privilege)

### AuditDetail types

These messages provide additional details that depend on the type of action. These details are implemented using different types that are derived from a base `AuditDetail` type as shown in the following table:

|Web API|SDK for .NET|Description |
|---------|---------|---------|
|<xref:Microsoft.Dynamics.CRM.AuditDetail?text=AuditDetail ComplexType>|<xref:Microsoft.Crm.Sdk.Messages.AuditDetail?text=AuditDetail Class>|The base type for the derived classes. Provides access to the audit record.|
|<xref:Microsoft.Dynamics.CRM.AttributeAuditDetail?text=AttributeAuditDetail ComplexType>|<xref:Microsoft.Crm.Sdk.Messages.AttributeAuditDetail?text=AttributeAuditDetail Class>|Provides details when data changes occur for a record. Provides access to old values and new values. <br /> Returned by the following types of actions: <br />- [Table row events](#table-row-events)<br />- [Metadata change events](#metadata-change-events)<br />- [Audit change events](#audit-change-events)|
|<xref:Microsoft.Dynamics.CRM.RelationshipAuditDetail?text=RelationshipAuditDetail ComplexType>|<xref:Microsoft.Crm.Sdk.Messages.RelationshipAuditDetail?text=RelationshipAuditDetail Class>|Provides details when records are associated or disassociated using Many-to-Many relationship. Provides the name of the relationship and a list of the records that the operation changed.<br /> Returned by [Many-to-Many relationship events](#many-to-many-relationship-events)|
|<xref:Microsoft.Dynamics.CRM.RolePrivilegeAuditDetail?text=RolePrivilegeAuditDetail ComplexType>|<xref:Microsoft.Crm.Sdk.Messages.RolePrivilegeAuditDetail?text=RolePrivilegeAuditDetail Class>|Provides details when the definitions of [Security Role (Role)](../reference/entities/role.md) records change. Provides information about the old and new role privileges associated to the role.<br />Returned by [Security Role change events](#security-role-change-events)|
|<xref:Microsoft.Dynamics.CRM.ShareAuditDetail?text=ShareAuditDetail ComplexType>|<xref:Microsoft.Crm.Sdk.Messages.ShareAuditDetail?text=ShareAuditDetail Class>|Provides details when a record is shared, unshared, or when the level of access to a shared record changes. <br /> Returned by [Record Sharing events](#record-sharing-events)|
|<xref:Microsoft.Dynamics.CRM.UserAccessAuditDetail?text=UserAccessAuditDetail ComplexType>|<xref:Microsoft.Crm.Sdk.Messages.UserAccessAuditDetail?text=UserAccessAuditDetail Class>|Provides details to track user access auditing. Provides details on the interval and access time. <br /> Returned by [User Access Events](#user-access-events)|

> [!IMPORTANT]
> Large column values included in `AttributeAuditDetail` `OldValue` or `NewValue` properties such as [Email.Description](../reference/entities/email.md#BKMK_Description) or [Annotation](../reference/entities/annotation.md) are limited (capped) to 5KB or ~5,000 characters in length. A capped column value can be recognized by three dots at the end of the text, for example "lorem ipsum, lorem ip…".
>
> Because the data is truncated, you cannot use the audit data to restore changes for these column values.


### RetrieveAuditDetails Message

Use this message to retrieve the audit details for a single audit record.

# [Web API](#tab/webapi)

<xref:Microsoft.Dynamics.CRM.RetrieveAuditDetails> is a function bound to the audit table.

When you include the `Prefer: odata.include-annotations="*"` request header you will get formatted values.

The example below shows the <xref:Microsoft.Dynamics.CRM.AttributeAuditDetail?text=AttributeAuditDetail ComplexType> returned when the `parentaccountid` is set on an `account` record.

**Request**

```http
GET [Organization URI]/api/data/v9.2/audits(12869c65-d7d3-ec11-b656-281878f0eba9)/Microsoft.Dynamics.CRM.RetrieveAuditDetails HTTP/1.1

Accept: application/json  
OData-MaxVersion: 4.0  
OData-Version: 4.0
If-None-Match: null
Prefer: odata.include-annotations="*" 
```

**Response**

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

More information:

- <xref:Microsoft.Dynamics.CRM.RetrieveAuditDetails?text=RetrieveAuditDetails Function>
- <xref:Microsoft.Dynamics.CRM.RetrieveAuditDetailsResponse?text=RetrieveAuditDetailsResponse ComplexType>
- [Use Web API functions](../webapi/use-web-api-functions.md)
- [Include formatted values](../webapi/query-data-web-api.md#include-formatted-values)


# [SDK for .NET](#tab/sdk)

The following `ShowAuditDetail` static method will return audit details for any type of audit details that can be tracked by an audit record. 

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

The `DisplayAuditDetail` static method will output different details to the console depending on the type of audit detail. This method is used by other SDK for .NET samples on this page.

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

More information:

- <xref:Microsoft.Crm.Sdk.Messages.RetrieveAuditDetailsRequest?text=RetrieveAuditDetailsRequest Class>
- <xref:Microsoft.Crm.Sdk.Messages.RetrieveAuditDetailsResponse?text=RetrieveAuditDetailsResponse Class>
- <xref:Microsoft.Xrm.Sdk.IOrganizationService.Execute*?text=IOrganizationService.Execute Method>

---

### RetrieveAttributeChangeHistory Message

Use this message to retrieve a list of changes for a specific table column.

Use the `PagingInfo` parameter to control the number of records to return and move forward or backward through the pages. For subsequent requests, set the `PagingInfo.PagingCookie` property to the value returned by the `AuditDetailCollection.PagingCookie`.

Changes for this message will always be `AttributeAuditDetail` types.

# [Web API](#tab/webapi)

This example returns a single audited change history for the `description` column of an `account` table record.

**Request**

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

**Response**

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
More information:
- <xref:Microsoft.Dynamics.CRM.RetrieveAttributeChangeHistory?text=RetrieveAttributeChangeHistory Function>
- <xref:Microsoft.Dynamics.CRM.RetrieveAttributeChangeHistoryResponse?text=RetrieveAttributeChangeHistoryResponse ComplexType>
- <xref:Microsoft.Dynamics.CRM.AuditDetailCollection?text=AuditDetailCollection ComplexType>

> [!NOTE]
> The <xref:Microsoft.Dynamics.CRM.AttributeAuditDetail?text=AttributeAuditDetail ComplexType> returned currently does not include the `AuditRecord` property so there is no data about who made the change and when it was made.

# [SDK for .NET](#tab/sdk)

The `ShowAttributeChangeHistory` static method below will return the first 20 audited changes for specified column in the specified record.

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

More information:

- <xref:Microsoft.Crm.Sdk.Messages.RetrieveAttributeChangeHistoryRequest?text=RetrieveAttributeChangeHistoryRequest Class>
- <xref:Microsoft.Crm.Sdk.Messages.RetrieveAttributeChangeHistoryResponse?text=RetrieveAttributeChangeHistoryResponse Class>
- <xref:Microsoft.Xrm.Sdk.IOrganizationService.Execute*?text=IOrganizationService.Execute Method>

---

### RetrieveRecordChangeHistory Message

The `RetrieveRecordChangeHistory` message shows the history of data changes for a given record indicated by the `Target` parameter.

Use the `PagingInfo` parameter to control the number of records to return and move forward or backward through the pages. For subsequent requests, set the `PagingInfo.PagingCookie` property to the value returned by the `AuditDetailCollection.PagingCookie`

The results of this message are commonly seen as the `AttributeAuditDetail` data displayed in model-driven apps when you select **Related** > **Audit history**. It shows the old values and the new values of the records, but it will also return `RelationshipAuditDetail` and `ShareAuditDetail` types.

This message can also be used to with the `systemuser` and `role` tables to return `RolePrivilegeAuditDetail` and `UserAccessAuditDetail` types.




# [Web API](#tab/webapi)

The following example returns just the first two of four changes for an account record.

**Request**

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

**Response**

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

More information:

- <xref:Microsoft.Dynamics.CRM.RetrieveRecordChangeHistory?text=RetrieveRecordChangeHistory Function>
- <xref:Microsoft.Dynamics.CRM.RetrieveRecordChangeHistoryResponse?text=RetrieveRecordChangeHistoryResponse ComplexType>
- <xref:Microsoft.Dynamics.CRM.PagingInfo?text=PagingInfo ComplexType>
- [Use Web API functions](../webapi/use-web-api-functions.md)

> [!NOTE]
> The <xref:Microsoft.Dynamics.CRM.AuditDetail?text=AuditDetail ComplexType> values returned currently do not include the `AuditRecord` property so there is no data about who made the change and when it was made.

# [SDK for .NET](#tab/sdk)

For a full sample, see [Sample: Audit table data changes](../org-service/samples/audit-entity-data-changes.md).

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

More information:

- [Sample: Audit table data changes](../org-service/samples/audit-entity-data-changes.md).
- <xref:Microsoft.Crm.Sdk.Messages.RetrieveRecordChangeHistoryRequest?text=RetrieveRecordChangeHistoryRequest Class>
- <xref:Microsoft.Crm.Sdk.Messages.RetrieveRecordChangeHistoryResponse?text=RetrieveRecordChangeHistoryResponse Class>
- <xref:Microsoft.Xrm.Sdk.Query.PagingInfo?text=PagingInfo Class>
- <xref:Microsoft.Xrm.Sdk.IOrganizationService.Execute*?text=IOrganizationService.Execute Method>

---

### See also

[Auditing overview](overview.md)<br />
[Configure auditing](configure.md)<br />
[Delete audit data](delete-audit-data.md)<br />
[Sample: Audit table data changes](../org-service/samples/audit-entity-data-changes.md)<br />
[Sample: Audit user access](../org-service/samples/audit-user-access.md)<br />
[Administrators Guide: Audit data and user activity for security and compliance](/power-platform/admin/audit-data-user-activity)

[!INCLUDE [footer-banner](../../../includes/footer-banner.md)]