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

After auditing is enabled and data changes are made to those tables and columns being audited, you can retrieve the data change history.

> [!NOTE]
> Audit data is not available using the Dataverse TDS (SQL) endpoint. More information: [Use SQL to query data](../dataverse-sql-query.md)

## Audit table

Data for auditing events is in the [Auditing (Audit) table](../reference/entities/audit.md). In the Web API the <xref:Microsoft.Dynamics.CRM.audit?text=audit EntityType> is the resource for this data. The audit table is read-only.

The audit table provides the data for the **View Audit Summary** displayed in the Power Platform admin center. More information: [Administrators Guide: Use the Audit Summary view](/power-platform/admin/manage-dataverse-auditing#use-the-audit-summary-view)

Calling user must have the `prvReadAuditSummary` privilege to retrieve data from this table.

The following table summarizes important columns in the audit table.

|SchemaName<br />LogicalName<br />DisplayName  |Type  |Description  |
|---------|---------|---------|
|`Action`<br />`action`<br />Event|Choice|74 options that represent the name of the message that caused the change. More information: [Actions](#audit-actions)|
|`AttributeMask`<br />`attributemask`<br />Changed Field|Memo|May contain a comma separated list of numbers that correspond to the <xref:Microsoft.Xrm.Sdk.Metadata.AttributeMetadata>.<xref:Microsoft.Xrm.Sdk.Metadata.AttributeMetadata.ColumnNumber> for the columns changed in the transaction for the action. |
|`AuditId`<br />`auditid`<br /> Record Id|Unique Identifier|The primary key for the audit table.|
|`CallingUserId`<br />`callinguserid`<br />Calling User|Lookup|The calling user when impersonation is used for the operation. Otherwise null. |
|`CreatedOn`<br />`createdon`<br />Changed Date|DateTime|When the audit record was created, which is when the user operation took place.|
|`ObjectId`<br />`objectid`<br />Record|Lookup|The unique identifier for the record that was audited.|
|`ObjectTypeCode`<br />`objecttypecode`<br />Entity|EntityName|The logical name of the entity referred to by the `objectid` column.|
|`Operation`<br />`operation`<br />Operation|Choice|The operation that caused the audit record. One of 4 values:<br />1 = Create<br />2 = Update<br />3 = Delete<br />4 = Access<br />|
|`UserId`<br />`userid`<br />Changed By|Lookup|The Id of the user who caused the change.|



<!-- Does the User Info column ever contain data? How does it get written there? 
Not in a 3rd-party plug-in. Audit table doesn't support plug-in step registrations
-->

## Audit Actions

There are currently 74 options in the [Action Choices/Options](/power-apps/developer/data-platform/reference/entities/audit#action-choicesoptions) which generally correspond to messages in the system, with some exceptions.

You can use these to filter for specific operations. The following table includes the options:

<!-- 

TODO: complete the table descriptions 
Each one should have a corresponding Operation value

-->

|Value|Label|Message|Comment|
|-----|-----|-------|-------|
|0|Unknown|None|Not a known message|
|1|Create |`Create`||
|2|Update|`Update`||
|3|Delete|`Delete`||
|4|Activate|||
|5|Deactivate|||
|11|Cascade|||
|12|Merge|`Merge`||
|13|Assign|`Assign`||
|14|Share|`GrantAccess`||
|15|Retrieve|`Retrieve`||
|16|Close|`CloseIncident`<br />`CloseQuote`|See [Message groups](#message-groups)|
|17|Cancel|||
|18|Complete|||
|20|Resolve|||
|21|Reopen|||
|22|Fulfill|||
|23|Paid|||
|24|Qualify|||
|25|Disqualify|||
|26|Submit|||
|27|Reject|||
|28|Approve|||
|29|Invoice|||
|30|Hold|||
|31|Add Member||See [Message groups](#message-groups)|
|32|Remove Member|||
|33|Associate Entities|`Associate`||
|34|Disassociate Entities|`Disassociate`||
|35|Add Members|||
|36|Remove Members|||
|37|Add Item||See [Message groups](#message-groups)|
|38|Remove Item|||
|39|Add Substitute|||
|40|Remove Substitute|||
|41|Set State|`SetState`||
|42|Renew|`RenewContract`<br />`RenewEntitlement`|See [Message groups](#message-groups)|
|43|Revise||See [Message groups](#message-groups)|
|44|Win||See [Message groups](#message-groups)|
|45|Lose||See [Message groups](#message-groups)|
|46|Internal Processing|||
|47|Reschedule|||
|48|Modify Share|`ModifyAccess`||
|49|Unshare|`RevokeAccess`||
|50|Book|||
|51|Generate Quote From Opportunity|||
|52|Add To Queue|||
|53|Assign Role To Team|||
|54|Remove Role From Team|||
|55|Assign Role To User|||
|56|Remove Role From User|||
|57|Add Privileges to Role|||
|58|Remove Privileges From Role|||
|59|Replace Privileges In Role|||
|60|Import Mappings|||
|61|Clone|||
|62|Send Direct Email|||
|63|Enabled for organization|||
|64|User Access via Web|None|See [User Access Actions](#user-access-actions)|
|65|User Access via Web Services|None|See [User Access Actions](#user-access-actions)|
|100|Delete Entity||User deleted a table.|
|101|Delete Attribute||User deleted a column.|
|102|Audit Change at Entity Level||User changed a table definition to enable or disable auditing.|
|103|Audit Change at Attribute Level||User changed a column definition to enable or disable auditing.|
|104|Audit Change at Org Level|||
|105|Entity Audit Started|||
|106|Attribute Audit Started|||
|107|Audit Enabled|||
|108|Entity Audit Stopped|||
|109|Attribute Audit Stopped|||
|110|Audit Disabled|||
|111|Audit Log Deletion|||
|112|User Access Audit Started|None|See [User Access Actions](#user-access-actions)|
|113|User Access Audit Stopped|None|See [User Access Actions](#user-access-actions)|

#### Message groups

There are some action options that can represent more than one message. Some messages have a common verb that is appended with a table name. In this way some action options can represent more than one message. You need to filter on the `objecttypecode` to differentiate the specific message. For example:

|Value|Label|Table|Message|
|---------|---------|---------|---------|
|31|Add Member|`List`|`AddMemberList`|
|37|Add Item|`Campaign`|`AddItemCampaign`|
|37|Add Item|`CampaignActivity`|`CampaignActivity`|
|44|Win|`Opportunity`|`WinOpportunity`|
|16|Close|`Incident`|`CloseIncident`|
|16|Close|`Quote`|`CloseQuote`|
|42|Renew|`Contract`|`RenewContract`|
|42|Renew|`Entitlement`|`RenewEntitlement`|
|43|Revise|`Quote`|`ReviseQuote`|

In the .NET SDK you will find request and response class definitions for many of these within the <xref:Microsoft.Crm.Sdk.Messages?text=Microsoft.Crm.Sdk.Messages Namespace>, such as:

 - <xref:Microsoft.Crm.Sdk.Messages.AddMemberListRequest?text=AddMemberListRequest Class>/<xref:Microsoft.Crm.Sdk.Messages.AddMemberListResponse?text=AddMemberListResponse Class>
 - <xref:Microsoft.Crm.Sdk.Messages.AddItemCampaignRequest?text=AddItemCampaignRequest Class>/<xref:Microsoft.Crm.Sdk.Messages.AddItemCampaignResponse?text=AddItemCampaignResponse Class>
 - <xref:Microsoft.Crm.Sdk.Messages.AddItemCampaignActivityRequest?text=AddItemCampaignActivityRequest Class>/<xref:Microsoft.Crm.Sdk.Messages.AddItemCampaignActivityResponse?text=AddItemCampaignActivityResponse Class>
 - <xref:Microsoft.Crm.Sdk.Messages.WinOpportunityRequest?text=WinOpportunityRequest Class>/<xref:Microsoft.Crm.Sdk.Messages.WinOpportunityResponse?text=WinOpportunityResponse Class>
 - <xref:Microsoft.Crm.Sdk.Messages.CloseIncidentRequest?text=CloseIncidentRequest Class>/<xref:Microsoft.Crm.Sdk.Messages.CloseIncidentResponse?text=CloseIncidentResponse Class>
 
In the Web API, you will find corresponding actions in the Web API $metadata service document when a solution containing the definition of these messages is installed. These messages are only found in the Dynamics 365 solutions such as Dynamics 365 Sales, Dynamics 365 Customer Service, and Dynamics 365 Marketing.

#### User Access Actions

The following `action` options are used to capture history of user access when user access auditing is enabled.

|Value|Label|Description|
|-----|-----|-------|
|64|User Access via Web|User is accessing Dataverse using a model-driven app.|
|65|User Access via Web Services|User is accessing Dataverse using web services using a client other than a model-driven app.|
|112|User Access Audit Started|User access audit began.|
|113|User Access Audit Stopped|User access audit ended.|

For a .NET SDK sample showing use of these action options, see [Sample: Audit user access](../org-service/samples/audit-user-access.md).

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

<!-- Questions: 
Why is the Audit TransactionId frequently an empty GUID (but not always)? Does it matter?
Is UserAdditionalInfo ever not null?
Is RegardingObjectId ever not null? -->

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
  <NavigationProperty Name="callinguserid" Type="mscrm.systemuser" Nullable="false" Partner="lk_audit_callinguserid">
      <ReferentialConstraint Property="_callinguserid_value" ReferencedProperty="systemuserid" />
  </NavigationProperty>
  <NavigationProperty Name="userid" Type="mscrm.systemuser" Nullable="false" Partner="lk_audit_userid">
      <ReferentialConstraint Property="_userid_value" ReferencedProperty="systemuserid" />
  </NavigationProperty>
</EntityType>
```

More information: [CSDL $metadata document](../webapi/web-api-service-documents.md#csdl-metadata-document)

In the Web API, the `callinguserid` and `userid` single-valued navigation properties will always return `null` when using `$expand`. You must depend on the corresponding [Lookup properties](../webapi/web-api-properties.md#lookup-properties): `_callinguserid_value` and `_userid_value` to access data for these navigation properties.

Lookup properties contain additional information when `GET` requests are sent using the `Prefer: odata.include-annotations="*"` request header. Using this preference will make sure that you get the `Microsoft.Dynamics.CRM.lookuplogicalname` and `OData.Community.Display.V1.FormattedValue` annotation values, but the `Microsoft.Dynamics.CRM.associatednavigationproperty` annotation values are not included with lookup properties in the `audit` EntityType.

<!-- I think this is a bug. As noted above, for the _userid_value and _callinguserid_value lookup properties, there are associated navigation properties that could be returned. lk_audit_userid and lk_audit_callinguserid -->

## Example: Find Contact records deleted by a user

The following examples are queries showing audit history for contact records deleted by a specific user.

# [Web API](#tab/webapi)

Both of the following queries return the same response.

The following one filters on the `_userid_value` property of the audit record where the value matches `<user id>`.

**Request**

```http
GET [Organization URI]/api/data/v9.2/audits?$select=_objectid_value,objecttypecode,createdon,_userid_value&$orderby=createdon desc&$filter=operation eq 3 and objecttypecode eq 'contact' and _userid_value eq '<user id>' HTTP/1.1

Prefer: odata.include-annotations="*" 
```

The following one accesses the collection of audit records for a specific user with the `lk_audit_userid` collection-valued navigation property from the `systemuser` table where the `systemuserid` value matches `<user id>`

**Request**

```http
GET [Organization URI]/api/data/v9.2/systemusers(<user id>)/lk_audit_userid?$select=_objectid_value,objecttypecode,createdon,_userid_value&$orderby=createdon desc&$filter=operation eq 3 and objecttypecode eq 'contact' HTTP/1.1

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
      "_userid_value": "4026be43-6b69-e111-8f65-78e7d1620f5e",
      "transactionid": "00000000-0000-0000-0000-000000000000",
      "attributemask": "47,45,42,298,96,260,93,50,201,28,25,107,32,90,261,262,178,121,61,55,71,35,296,289,108,177,120,69,117,265,243,174,46,80,95,246,287,59,30,102,3,208,202,282,73,74,21,78,67,128,54,51,183,254,210,236,19,126,53,268,124,38,184,34,234,31,231,10019,118,33,76,98,292,271,52,297,6,70,123,129,132,133,242,103,36,39,114,22,293,48,249,295,235,12,99,11,8,5,10162,97,181,306,245,57,18,200,49,106,109,110,16,24,43,122,175,44,27,139,259,125,233,127,134,284,180,130,56,14,286,92,247,94,270,179,113,206,288,283,17,101,209,294,263,15,176,10017,4,29,203,119,37,72,40,20,266,267,173,211,91,111,105,290,131,264,10026,116,104,23,26,41,10020,66,100,115,2"
    },
    < Other results truncated for brevity>
  ]
}

```


# [.NET SDK](#tab/sdk)

There are two static methods below that show the number of deleted contact records for the specified user.

The following one uses <xref:Microsoft.Xrm.Sdk.Query.QueryExpression?text=QueryExpression Class>.

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
    QueryExpression query =
    new QueryExpression(entityName: "audit")
    {
        ColumnSet = new ColumnSet("objectid", "createdon")
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

    int count = records.Entities.Count();
    Console.WriteLine(
        $"User has deleted {count} contact records");
}
```

The following one uses <xref:Microsoft.Xrm.Sdk.Query.FetchExpression?text=FetchExpression Class> with a query composed using FetchXml.

```csharp
/// <summary>
/// Shows the number of contacts deleted by a user.
/// </summary>
/// <param name="svc">IOrganizationService to use</param>
/// <param name="systemuserid">The user's id.</param>
static void ShowNumberContactsDeletedByUserFetchXml(
    IOrganizationService svc,
    Guid systemuserid)
{
    string fetchXml = $@"<fetch>
        <entity name='audit'>
            <attribute name='objectid' />
            <attribute name='createdon' />
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

    FetchExpression query =
        new FetchExpression(fetchXml);

    EntityCollection records =
        svc.RetrieveMultiple(query);

    int count = records.Entities.Count();
    Console.WriteLine(
        $"User has deleted {count} contact records");
}
```

> [!NOTE]
> The following FetchXml also works. It uses the relationship to the `systemuser` table to provide the filter and the systemuserid matches `<user id>`.

```xml
<fetch>
   <entity name="systemuser">
      <filter>
         <condition attribute="systemuserid"
            operator="eq"
            value="<user id>" />
      </filter>
      <link-entity name="audit"
         from="userid"
         to="systemuserid"
         alias="audit">
         <attribute name="objectid"
            alias="objectid" />
         <attribute name="createdon"
            alias="changeddate" />
         <filter>
            <condition attribute="operation"
               operator="eq"
               value="3" />
            <condition attribute="objecttypecode"
               operator="eq"
               value="2" />
         </filter>
      </link-entity>
   </entity>
</fetch>
```

---

  
## Retrieve the change history

There are three messages you can use to retrieve data changes that are audited.

|Web API  |.NET SDK  |Description |
|---------|---------|---------|
|<xref:Microsoft.Dynamics.CRM.RetrieveAuditDetails?text=RetrieveAuditDetails Function>|<xref:Microsoft.Crm.Sdk.Messages.RetrieveAuditDetailsRequest?text=RetrieveAuditDetailsRequest Class>|Retrieve the full audit details from an audit record.|
|<xref:Microsoft.Dynamics.CRM.RetrieveAttributeChangeHistory?text=RetrieveAttributeChangeHistory Function>|<xref:Microsoft.Crm.Sdk.Messages.RetrieveAttributeChangeHistoryRequest?text=RetrieveAttributeChangeHistoryRequest Class>|Retrieve all changes to a specific column.|
|<xref:Microsoft.Dynamics.CRM.RetrieveRecordChangeHistory?text=RetrieveRecordChangeHistory Function>|<xref:Microsoft.Crm.Sdk.Messages.RetrieveRecordChangeHistoryRequest?text=RetrieveRecordChangeHistoryRequest Class>|Retrieve all audited data changes for a specific record.|

### AuditDetail types

These messages provide additional details that depend on the type of action. These details are implemented using different types that are derived from a base AuditDetail type as shown in the following table:

|Web API|.NET SDK|Description |
|---------|---------|---------|
|<xref:Microsoft.Dynamics.CRM.AuditDetail?text=AuditDetail ComplexType>|<xref:Microsoft.Crm.Sdk.Messages.AuditDetail?text=AuditDetail Class>|The base type for the derived classes. Provides access to the audit record.|
|<xref:Microsoft.Dynamics.CRM.AttributeAuditDetail?text=AttributeAuditDetail ComplexType>|<xref:Microsoft.Crm.Sdk.Messages.AttributeAuditDetail?text=AttributeAuditDetail Class>|Provides details when data changes occur for a record. Provides access to old values and new values. |
|<xref:Microsoft.Dynamics.CRM.RelationshipAuditDetail?text=RelationshipAuditDetail ComplexType>|<xref:Microsoft.Crm.Sdk.Messages.RelationshipAuditDetail?text=RelationshipAuditDetail Class>|Provides details when records are associated or disassociated using Many-to-Many relationship. Provides the name of the relationship and a list of the records that the operation changed.|
|<xref:Microsoft.Dynamics.CRM.RolePrivilegeAuditDetail?text=RolePrivilegeAuditDetail ComplexType>|<xref:Microsoft.Crm.Sdk.Messages.RolePrivilegeAuditDetail?text=RolePrivilegeAuditDetail Class>|Provides details when the definitions of [Security Role (Role)](../reference/entities/role.md) records change. Provides information about the old and new role privileges associated to the role.|
|<xref:Microsoft.Dynamics.CRM.ShareAuditDetail?text=ShareAuditDetail ComplexType>|<xref:Microsoft.Crm.Sdk.Messages.ShareAuditDetail?text=ShareAuditDetail Class>|Provides details when a record is shared, unshared, or when the level of access to a shared record changes. |
|<xref:Microsoft.Dynamics.CRM.UserAccessAuditDetail?text=UserAccessAuditDetail ComplexType>|<xref:Microsoft.Crm.Sdk.Messages.UserAccessAuditDetail?text=UserAccessAuditDetail Class>|Provides details to track user access auditing. Provides details on the interval and access time.|

### RetrieveAuditDetails Message

Use this message to retrieve the audit details for a specific record.

# [Web API](#tab/webapi)

<xref:Microsoft.Dynamics.CRM.RetrieveAuditDetails> is a function bound to the audit table.

When you include the `Prefer: odata.include-annotations="*"` request header you will get formatted values.

The example below shows the <xref:Microsoft.Dynamics.CRM.AttributeAuditDetail?text=AttributeAuditDetail ComplexType> returned when the `parentaccountid` is set on an `account` record.

**Request**

```http
GET [Organization URI]/api/data/v9.2/audits(12869c65-d7d3-ec11-b656-281878f0eba9)/Microsoft.Dynamics.CRM.RetrieveAuditDetails HTTP/1.1
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


# [.NET SDK](#tab/sdk)

The following `ShowAuditDetail` static method will return audit details for any type of audit details that can be tracked by an audit record. 

The `DisplayAuditDetail` static method will output different details to the console depending on the type of audit detail. This method is used by other samples on this page.

```csharp
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

/// <summary>
/// Displays properties of the different classes derived from AuditDetail
/// </summary>
/// <param name="auditDetail"></param>
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



# [Web API](#tab/webapi)

**Request**

```http
GET [Organization URI]/api/data/v9.2/RetrieveAttributeChangeHistory(Target=@target,AttributeLogicalName=@attributeLogicalName,PagingInfo=@paginginfo)?
@target={ '@odata.id':'accounts(611e7713-68d7-4622-b552-85060af450bc)'}
&@attributeLogicalName='description'
&@paginginfo={
   "PageNumber": 1,
   "Count": 8,
   "ReturnTotalRecordCount": true
}
```

**Response**

```http
HTTP/1.1 200 OK

{
    "@odata.context": "[Organization URI]/api/data/v9.2/$metadata#Microsoft.Dynamics.CRM.RetrieveAttributeChangeHistoryResponse",
    "AuditDetailCollection": {
        "MoreRecords": false,
        "PagingCookie": "",
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
                    "description": "Added using Flow because the account name changed to: Updated Account Name"
                },
                "NewValue": {
                    "@odata.type": "#Microsoft.Dynamics.CRM.account",
                    "description": "deleting phone number"
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
                    "description": "Setting Phone Number"
                },
                "NewValue": {
                    "@odata.type": "#Microsoft.Dynamics.CRM.account",
                    "description": "Added using Flow because the account name changed to: Updated Account Name"
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
                    "@odata.type": "#Microsoft.Dynamics.CRM.account"
                },
                "NewValue": {
                    "@odata.type": "#Microsoft.Dynamics.CRM.account",
                    "description": "Setting Phone Number"
                }
            }
        ]
    }
}
```

# [.NET SDK](#tab/sdk)

```csharp
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

This is the data displayed in model-driven apps when you select **Related** > **Audit history**. It shows the old values and the new values of the records.

Calling user must have the `prvReadRecordAuditHistory` privilege to use this message.

The message supports paging through the optional `PagingInfo` parameter to define how many records to return and what page of records to return.


# [Web API](#tab/webapi)

<xref:Microsoft.Dynamics.CRM.RetrieveRecordChangeHistory?text=RetrieveRecordChangeHistory Function> is an unbound function The `Target` parameter is a reference to a table row.  More information: [Use Web API functions](../webapi/use-web-api-functions.md)

This function returns an <xref:Microsoft.Dynamics.CRM.RetrieveRecordChangeHistoryResponse?text=RetrieveRecordChangeHistoryResponse ComplexType> where the `AuditDetailCollection` property is an <xref:Microsoft.Dynamics.CRM.AuditDetailCollection?text=AuditDetailCollection ComplexType>. The `AuditDetailCollection.AuditDetails` property contains the collection of <xref:Microsoft.Dynamics.CRM.AuditDetail?text=AuditDetail ComplexType> with data about the changes that occurred.

`AuditDetail` is base complex type with five derived complex types:

|Complex Type  |Description  |
|---------|---------|
|<xref:Microsoft.Dynamics.CRM.AttributeAuditDetail?text=AttributeAuditDetail ComplexType>|When data change to record.|
|<xref:Microsoft.Dynamics.CRM.RelationshipAuditDetail?text=RelationshipAuditDetail ComplexType>|When there are changes how records are associated in Many-to-Many relationships.|
|<xref:Microsoft.Dynamics.CRM.RolePrivilegeAuditDetail?text=RolePrivilegeAuditDetail ComplexType>|When the <xref:Microsoft.Dynamics.CRM.privilege?text=privilege EntityType> associated to a <xref:Microsoft.Dynamics.CRM.role?text=role EntityType> changes.|
|<xref:Microsoft.Dynamics.CRM.ShareAuditDetail?text=ShareAuditDetail ComplexType>|When shared access to a record changes.|
|<xref:Microsoft.Dynamics.CRM.UserAccessAuditDetail?text=UserAccessAuditDetail ComplexType>|When one of the [User Access Actions](#user-access-actions) occurs.|


Use the <xref:Microsoft.Dynamics.CRM.PagingInfo?text=PagingInfo ComplexType> to specify the initial page to return and the number of 
<xref:Microsoft.Dynamics.CRM.AuditDetail?text=AuditDetail ComplexType> records to return.

For subsequent requests, set the `PagingInfo.PagingCookie` property to the value of the `AuditDetailCollection.PagingCookie` property that was returned.

The following example returns just the first two of four changes for an account record.

<!-- Question:
What do these AttributeAuditDetail properties for?

Descriptions are not clear.
Why doesn't it have some way to link to an auditRecord?
Web API reference doesn't show derived complex types such as this.
You have to go to https://docs.microsoft.com/en-us/power-apps/developer/data-platform/webapi/reference/attributeauditdetail?view=dataverse-latest to see this type Base Type is AuditDetail.

From: .NET reference: https://docs.microsoft.com/dotnet/api/microsoft.crm.sdk.messages.attributeauditdetail?view=dataverse-sdk-latest#properties

"InvalidNewValueAttributes": [], Gets a collection of attempted attribute changes that are not valid.
"LocLabelLanguageCode": 0, Gets or sets the language code for the label.
"DeletedAttributes": {
                    "Count": 0,
                    "Keys": [],
                    "Values": []
                }, 	Gets a list of deleted attributes.

 -->


**Request**

```http
{{webapiurl}}RetrieveRecordChangeHistory(Target=@target,PagingInfo=@paginginfo)?
@target={ '@odata.id':'accounts(611e7713-68d7-4622-b552-85060af450bc)'}
&@paginginfo={
   "PageNumber": 1,
   "Count": 2,
   "ReturnTotalRecordCount": true
}
```

**Response**

```http
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


# [.NET SDK](#tab/sdk)


This function executes the `RetrieveRecordChangeHistory` message for a specified record and processes the response.

For each Audit record, it displays the properties and uses the `DisplayAuditDetail` method defined in the [RetrieveAuditDetails Message](#retrieveauditdetails-message) example to display the details.

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
- <xref:Microsoft.Crm.Sdk.Messages.RetrieveRecordChangeHistoryRequest?text=RetrieveRecordChangeHistoryRequest Class>
- <xref:Microsoft.Crm.Sdk.Messages.RetrieveRecordChangeHistoryResponse?text=RetrieveRecordChangeHistoryResponse Class>
- <xref:Microsoft.Xrm.Sdk.IOrganizationService.Execute*?text=IOrganizationService.Execute Method>

---


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