---
title: "Verifying access in code (Microsoft Dataverse) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "Learn how to use the security related APIs to verify user access to a record." # 115-145 characters including spaces. This abstract displays in the search result.
ms.date: 06/05/2023
ms.reviewer: pehecke
ms.topic: article
author: paulliew # GitHub ID
ms.subservice: dataverse-developer
ms.author: paulliew # MSFT alias of Microsoft employees only
search.audienceType: 
  - developer
---

# Verifying access in code

[!INCLUDE[cc-terminology](includes/cc-terminology.md)]

The only time you don't need to be concerned about security concepts is when you're writing code that a user with the System
Administrator security role runs. Because this role is all powerful and can't be
edited, you can be assured that the user can do anything. In all other cases,
you need to consider how security is applied.

- If you're creating a **client application**, you should evaluate the user's
    privileges for a table or for a specific table record and control which
    commands you enable. If a user isn't allowed to create a table, you can
    disable the user interface in your app to allow creating a new table of that type. If they don't have read access to a table, your client application can choose to not
    display components related to viewing lists of that type of table.

- If you're writing a **synchronous plug-in**, you can't attempt some
    data operation and throw away the exception. Any operation that fails within a
    synchronous plug-in causes the entire data transaction to be rolled back. If
    you have some part of the process that is optional depending on the user's
    privileges, you should check the user's privileges first.

There are two strategies you can apply to detect which operations a user can
perform:

- Test individual table records
- Check the user's security privileges

These strategies are described below.

## Test individual table records

User interaction with specific table records usually begins with a query. If a
user has no access to any records for that table, the query returns
no records, and there's nothing further the user can attempt except to create a
new record. Testing whether the user can create a new record requires using the
other strategy (mentioned above) to check the user's security privileges.

However, if the user was successful in retrieving table records using a query, you
can then test a record using the `RetrievePrincipalAccess` message.

### [SDK for .NET](#tab/sdk)

The following `GetAccessRights` static method uses the SDK [RetrievePrincipalAccessRequest Class](xref:Microsoft.Crm.Sdk.Messages.RetrievePrincipalAccessRequest) to retrieve a set of access rights that a user, team, or organization has for a record using the [AccessRights Enum](xref:Microsoft.Crm.Sdk.Messages.AccessRights).

```csharp
/// <summary>
/// Gets which access rights a user, team, or organization has for a specific record.
/// </summary>
/// <param name="service">Authenticated client implementing the IOrganizationService interface</param>
/// <param name="userOrTeamOrOrganization">The user, team, or organization to check</param>
/// <param name="entity">A reference to the entity to check.</param>
/// <returns>The access rights the user can perform.</returns>
static AccessRights GetAccessRights(
        IOrganizationService service,
        EntityReference userOrTeamOrOrganization,
        EntityReference entity)
{
    var request = new RetrievePrincipalAccessRequest()
    {
        Principal = userOrTeamOrOrganization,
        Target = entity
    };

    var response = (RetrievePrincipalAccessResponse)service.Execute(request);

    return response.AccessRights;
}
```

With the value returned by this method, you can use the [Enum.HasFlag Method](/dotnet/api/system.enum.hasflag#System_Enum_HasFlag_System_Enum_)
to return a [Boolean](xref:System.Boolean) value when the user has access to perform specific
operations on the table.

The following code snippet shows how to use the
`GetAccessRights` static method to test whether a user has access to append records
to an account record using the `AppendToAccess` member.

```C#
var whoIAm = (WhoAmIResponse)service.Execute(new WhoAmIRequest());

var meRef = new EntityReference("systemuser", whoIAm.UserId);

QueryExpression query = new("account") { 
        ColumnSet = new ColumnSet("accountid"),
        TopCount = 1
};

EntityCollection accounts = service.RetrieveMultiple(query);

EntityReference accountRef = accounts
    .Entities
    .FirstOrDefault()
    .ToEntityReference();

AccessRights rights = GetAccessRights(service, meRef, accountRef);

var canAppendTo = rights.HasFlag(AccessRights.AppendToAccess);
```

### [Web API](#tab/webapi)

The following example shows how to use the [RetrievePrincipalAccess function](xref:Microsoft.Dynamics.CRM.RetrievePrincipalAccess) to retrieve the access rights that a user has for an account record. The [RetrievePrincipalAccessResponse ComplexType](xref:Microsoft.Dynamics.CRM.RetrievePrincipalAccessResponse) provides the details of the users rights using [AccessRights EnumType](xref:Microsoft.Dynamics.CRM.AccessRights).

**Request:**

```http
GET [Organization Uri]/api/data/v9.2/systemusers(4026be43-6b69-e111-8f65-78e7d1620f5e)/Microsoft.Dynamics.CRM.RetrievePrincipalAccess(Target=@p1)?@p1={'@odata.id':'accounts(e41ac31a-dcdf-ed11-a7c7-000d3a993550)'}
OData-MaxVersion: 4.0
OData-Version: 4.0
If-None-Match: null
Accept: application/json
```

**Response:**

```http
HTTP/1.1 200 OK
OData-Version: 4.0

{
  "@odata.context": "[Organization Uri]/api/data/v9.2/$metadata#Microsoft.Dynamics.CRM.RetrievePrincipalAccessResponse",
  "AccessRights": "ReadAccess, WriteAccess, AppendAccess, AppendToAccess, CreateAccess, DeleteAccess, ShareAccess, AssignAccess"
}
```

---

With access to a table record, you can use the access rights returned to test any
operations that apply to that record. But this test doesn't include capabilities that
apply to other operations, such as creating a new record or any other privilege
that isn't bound to a specific table. For these operations, you need to [Check a user's security privileges](#check-a-users-security-privileges).

### Get principals with access to a record

Some data operations require another user have access to a record. If you have
just one specific user, team, or organization, you can test using the `RetrievePrincipalAccess` message.

However, if you need a list of all the  users, teams, or organizations that a record has been shared with, use the `RetrieveSharedPrincipalsAndAccess` message. `RetrieveSharedPrincipalsAndAccess` provides details about the access rights each user, team, or organization has because the record was shared with them.

#### [SDK for .NET](#tab/sdk)

The following `GetSharedPrincipalsAndAccess` static method uses the [RetrieveSharedPrincipalsAndAccessRequest](xref:Microsoft.Crm.Sdk.Messages.RetrieveSharedPrincipalsAndAccessRequest) and [RetrieveSharedPrincipalsAndAccessResponse](xref:Microsoft.Crm.Sdk.Messages.RetrieveSharedPrincipalsAndAccessResponse) classes to return an array of [PrincipalAccess](xref:Microsoft.Crm.Sdk.Messages.PrincipalAccess) data with details about the principals and the access they have because the record was shared with them.

```csharp
/// <summary>
/// Returns details about access principals have because a record was shared with them.
/// </summary>
/// <param name="service">Authenticated client implementing the IOrganizationService interface</param>
/// <param name="target">The record to check</param>
/// <returns>The principal access data for each user, team, or organization</returns>
static PrincipalAccess[] GetSharedPrincipalsAndAccess(
    IOrganizationService service,
    EntityReference target)
{
    var request = new RetrieveSharedPrincipalsAndAccessRequest()
    {
        Target = target
    };

    var response = (RetrieveSharedPrincipalsAndAccessResponse)service.Execute(request);

    return response.PrincipalAccesses;
}
```

#### [Web API](#tab/webapi)

The following example uses the [RetrieveSharedPrincipalsAndAccess Function](xref:Microsoft.Dynamics.CRM.RetrieveSharedPrincipalsAndAccess) and the [RetrieveSharedPrincipalsAndAccessResponse ComplexType](xref:Microsoft.Dynamics.CRM.RetrieveSharedPrincipalsAndAccessResponse) returned provides an array of [PrincipalAccess ComplexType](xref:Microsoft.Dynamics.CRM.PrincipalAccess) with details about the principals and the access they have because the record was shared with them.

**Request:**

```http
GET [Organization Uri]/api/data/v9.2/RetrieveSharedPrincipalsAndAccess(Target=@p1)?@p1={'@odata.id':'accounts(86914942-34cb-ed11-b596-0022481d68cd)'}
OData-MaxVersion: 4.0
OData-Version: 4.0
If-None-Match: null
Accept: application/json
```

**Response:**

```http
HTTP/1.1 200 OK
OData-Version: 4.0

{
  "@odata.context": "[Organization Uri]/api/data/v9.2/$metadata#Microsoft.Dynamics.CRM.RetrieveSharedPrincipalsAndAccessResponse",
  "PrincipalAccesses": [
    {
      "AccessMask": "DeleteAccess",
      "Principal": {
        "@odata.type": "#Microsoft.Dynamics.CRM.systemuser",
        "ownerid": "7761da90-2383-e911-a962-000d3a13c05d"
      }
    },
    {
      "AccessMask": "DeleteAccess",
      "Principal": {
        "@odata.type": "#Microsoft.Dynamics.CRM.systemuser",
        "ownerid": "8061643d-ebf7-e811-a974-000d3a1e1c9a"
      }
    }
  ]
}
```

---

## Check a user's security privileges

When you don't have a specific table record to test, such as whether a user can
create a new table record, you must rely on checking the user's security
privileges. These privileges are stored in the [Privilege table](reference/entities/privilege.md).

There are nearly 1000 individual privileges in the Dataverse database and the
number grows with every table that is added to the system.
You can retrieve a list of the privileges available in your environment by executing the
following FetchXML query.

```XML
<fetch version='1.0' distinct='true' no-lock='true' >
  <entity name='privilege' >
    <attribute name='name' />
  </entity>
</fetch>
```

> [!TIP]
> The [XrmToolBox FetchXML Builder](https://www.xrmtoolbox.com/plugins/Cinteros.Xrm.FetchXmlBuilder/) is a useful tool to compose and test FetchXML queries.

The value of the `name` attribute follows this naming convention pattern when the
privilege applies to tables: "prv+Verb+Table SchemaName". The verb is one of **Append**, **AppendTo**, **Assign**, **Create**, **Delete**,
**Share**, **Write**.

In addition to the privileges for tables, there are less than 100 other
special privileges that aren't associated with tables. You can use the
following query to retrieve these privileges.

```XML
<fetch version='1.0' distinct='true' no-lock='true' >

<entity name='privilege' >
  <attribute name='name' />
  <filter>
    <condition attribute='name' operator='not-begin-with' value='prvAppend' />
    <condition attribute='name' operator='not-begin-with' value='prvAssign' />
    <condition attribute='name' operator='not-begin-with' value='prvCreate' />
    <condition attribute='name' operator='not-begin-with' value='prvDelete' />
    <condition attribute='name' operator='not-begin-with' value='prvRead' />
    <condition attribute='name' operator='not-begin-with' value='prvShare' />
    <condition attribute='name' operator='not-begin-with' value='prvWrite' />
  </filter>
</entity>

</fetch>
```

Use these messages to retrieve privileges by privilege ID or name. They include privileges that the user might have from teams.

| Message | Web API function<br/>SDK request class |
| --- | --- |
|`RetrieveUserPrivilegeByPrivilegeId`| [RetrieveUserPrivilegeByPrivilegeId Function](xref:Microsoft.Dynamics.CRM.RetrieveUserPrivilegeByPrivilegeId)<br/>[RetrieveUserPrivilegeByPrivilegeIdRequest Class](xref:Microsoft.Crm.Sdk.Messages.RetrieveUserPrivilegeByPrivilegeIdRequest)|
|`RetrieveUserPrivilegeByPrivilegeName`| [RetrieveUserPrivilegeByPrivilegeName Function](xref:Microsoft.Dynamics.CRM.RetrieveUserPrivilegeByPrivilegeName)<br/>[RetrieveUserPrivilegeByPrivilegeNameRequest Class](xref:Microsoft.Crm.Sdk.Messages.RetrieveUserPrivilegeByPrivilegeNameRequest)|
|`RetrieveUserSetOfPrivilegesByIds`|[RetrieveUserSetOfPrivilegesByIds Function](xref:Microsoft.Dynamics.CRM.RetrieveUserSetOfPrivilegesByIds)<br/>[RetrieveUserSetOfPrivilegesByIdsRequest Class](xref:Microsoft.Crm.Sdk.Messages.RetrieveUserSetOfPrivilegesByIdsRequest)|
|`RetrieveUserSetOfPrivilegesByNames`|[RetrieveUserSetOfPrivilegesByNames Function](xref:Microsoft.Dynamics.CRM.RetrieveUserSetOfPrivilegesByNames)<br/>[RetrieveUserSetOfPrivilegesByNamesRequest Class](xref:Microsoft.Crm.Sdk.Messages.RetrieveUserSetOfPrivilegesByNamesRequest)|

### Example: Check whether a user has a privilege

The following examples show the use of the `RetrieveUserPrivilegeByPrivilegeName` message. This message retrieves the list of privileges for a system user (user) from all direct roles associated with the system user and from all indirect roles associated with teams in which the system user is a member of based on the specified privilege name.

#### [.NET SDK](#tab/sdk)

The following `HasPrivilege` static method returns whether the user has the named privilege.

```csharp
/// <summary>
/// Returns whether specified user has a named privilege
/// </summary>
/// <param name="service">The IOrganizationService instance to use.</param>
/// <param name="systemUserId">The Id of the user.</param>
/// <param name="privilegeName">The name of the privilege.</param>
/// <returns></returns>
static bool HasPrivilege(IOrganizationService service,
        Guid systemUserId,
        string privilegeName)
{
    var request = new
        RetrieveUserPrivilegeByPrivilegeNameRequest
    {
        PrivilegeName = privilegeName,
        UserId = systemUserId
    };
    var response =
        (RetrieveUserPrivilegeByPrivilegeNameResponse)service
        .Execute(request);
    if (response.RolePrivileges.Length > 0)
    {
        return true;
    }
    return false;
}
```

More information:

- [IOrganizationService.Execute Method](xref:Microsoft.Xrm.Sdk.IOrganizationService.Execute%2A)
- [RetrieveUserPrivilegeByPrivilegeNameResponse Class](xref:Microsoft.Crm.Sdk.Messages.RetrieveUserPrivilegeByPrivilegeNameResponse)

#### [Web API](#tab/webapi)

This example tests whether a user with systemuserid of `00000000-0000-0000-0000-000000000001` has the `prvReadAuditSummary` privilege. Because the [RetrieveUserPrivilegeByPrivilegeNameResponse  ComplexType](xref:Microsoft.Dynamics.CRM.RetrieveUserPrivilegeByPrivilegeNameResponse)`.RolePrivileges` collection contains [RolePrivilege ComplexType](xref:Microsoft.Dynamics.CRM.RolePrivilege) data, the user has the privilege.

**Request:**

```http
GET [Organization Uri]/api/data/v9.2/systemusers(00000000-0000-0000-0000-000000000001)/Microsoft.Dynamics.CRM.RetrieveUserPrivilegeByPrivilegeName(PrivilegeName='prvReadAuditSummary')
OData-MaxVersion: 4.0
OData-Version: 4.0
If-None-Match: null
Prefer: odata.include-annotations="*"
```

**Response:**

```http
HTTP/1.1 200 OK
Content-Type: application/json; odata.metadata=minimal
OData-Version: 4.0
Preference-Applied: odata.include-annotations="*"

{
    "@odata.context": "[Organization Uri]/api/data/v9.2/$metadata#Microsoft.Dynamics.CRM.RetrieveUserPrivilegeByPrivilegeNameResponse",
    "RolePrivileges": [
        {
            "Depth": "Global",
            "PrivilegeId": "c2cbe3db-62c8-4661-9ac5-7691c83242f5",
            "BusinessUnitId": "38e0dbe4-131b-e111-ba7e-78e7d1620f5e",
            "PrivilegeName": "prvReadAuditSummary"
        }
    ]
}
```

More information:

- [Use Web API functions](webapi/use-web-api-functions.md)
- [Bound functions](webapi/use-web-api-functions.md#bound-functions)
- [RetrieveUserPrivilegeByPrivilegeName Function](xref:Microsoft.Dynamics.CRM.RetrieveUserPrivilegeByPrivilegeName)
- [RetrieveUserPrivilegeByPrivilegeNameResponse ComplexType](xref:Microsoft.Dynamics.CRM.RetrieveUserPrivilegeByPrivilegeNameResponse)

---

## Retrieve privileges for a security role

You can retrieve the privileges associated with a security role.

#### [SDK for .NET](#tab/sdk)

The following static `GetRolePrivileges` method retrieves the privileges associated with a role.

```csharp
/// <summary>
/// Retrieves the privileges for a role.
/// </summary>
/// <param name="service">Authenticated client implementing the IOrganizationService interface</param>
/// <param name="roleId">The id of the role</param>
/// <returns>Privilege records associated to the role</returns>
static EntityCollection GetRolePrivileges(IOrganizationService service, Guid roleId) {

    Relationship roleprivileges_association = new("roleprivileges_association");

    var relationshipQueryCollection = new RelationshipQueryCollection();

    var relatedPrivileges = new QueryExpression("privilege")
    {
        ColumnSet = new ColumnSet("name")
    };

    relationshipQueryCollection.Add(roleprivileges_association, relatedPrivileges);

    var request = new RetrieveRequest()
    {
        ColumnSet = new ColumnSet(true),
        RelatedEntitiesQuery = relationshipQueryCollection,
        Target = new EntityReference("role", roleId)
    };

    var response = (RetrieveResponse)service.Execute(request);

    return response.Entity.RelatedEntities[roleprivileges_association];
}
```

More information: [Retrieve with related rows](org-service/entity-operations-retrieve.md#retrieve-with-related-rows)

#### [Web API](#tab/webapi)

The following example returns the privileges associated with a role with a given `roleid`.

**Request:**

```http
GET [Organization Uri]/api/data/v9.2/roles(<roleid>)/roleprivileges_association?$select=name&$orderby=name
OData-MaxVersion: 4.0
OData-Version: 4.0
If-None-Match: null
Accept: application/json
```

**Response:**

```http
HTTP/1.1 200 OK
OData-Version: 4.0

{
  "@odata.context": "[Organization Uri]/api/data/v9.2/$metadata#privileges(name)",
  "value": [
    {
      "@odata.etag": "W/\"10646316\"",
      "name": "prvCreateSharePointData",
      "privilegeid": "5eb85025-363b-46ea-a77e-ce24159cd231"
    },
    {
      "@odata.etag": "W/\"35414093\"",
      "name": "prvReadconversationtranscript",
      "privilegeid": "448bd4ab-41e4-4055-b288-36110522d6e8"
    },
    {
      "@odata.etag": "W/\"10646495\"",
      "name": "prvReadSharePointData",
      "privilegeid": "fecbd29c-df64-4ede-a611-47226b402c22"
    },
    {
      "@odata.etag": "W/\"10646213\"",
      "name": "prvReadSharePointDocument",
      "privilegeid": "d71fc8d0-99bc-430e-abd7-d95c64f11e9c"
    },
    {
      "@odata.etag": "W/\"10646645\"",
      "name": "prvWriteSharePointData",
      "privilegeid": "cfdd12cf-090b-4599-8302-771962d2350a"
    }
  ]
}
```

More information: [Filtered collections](webapi/query-data-web-api.md#filtered-collections)

---

### See Also

[Plug-ins](plug-ins.md)

[!INCLUDE[footer-include](../../includes/footer-banner.md)]
