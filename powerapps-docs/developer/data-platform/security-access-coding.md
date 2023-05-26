---
title: "Verifying access in code (Microsoft Dataverse) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "Learn how to use the security related APIs to verify user access to a record." # 115-145 characters including spaces. This abstract displays in the search result.
ms.date: 05/21/2022
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

The only time you don't need to be concerned about security concepts is when you
are writing code that is expected to be run by a user with the System
Administrator security role. Because this role is all powerful and cannot be
edited, you can be assured that the user can do anything. In all other cases,
you need to consider how security is applied.

- If you are creating a **client application**, you should evaluate the user's
    privileges for a table or for a specific table record and control which
    commands you enable. If a user is not allowed to create a table, you can
    disable the user interface in your app to allow creating a new table of that type. If they don't have read access to a table, your client application can choose to not
    display components related to viewing lists of that type of table.

- If you are writing a **synchronous plug-in**, you can't simply attempt some
    data operation and throw away the exception. Any operation that fails within a
    synchronous plug-in will cause the entire data transaction to be rolled back. If
    you have some part of the process that is optional depending on the user's
    privileges, you should check the user's privileges first.

There are two strategies you can apply to detect which operations a user can
perform:

- Test individual table records
- Check the user's security privileges

These strategies are described below.

## Test individual table records

User interaction with specific table records usually begins with a query. If a
user has no access to any records for that table, the query will simply return
no records and there is nothing further the user can attempt except to create a
new record. Testing whether the user can create a new record requires using the
other strategy (mentioned above) to check the user's security privileges.

However, if the user was successful in retrieving table records using a query, you
can then test a record using the `RetrievePrincipalAccess` message.

The following method uses the SDK <xref:Microsoft.Crm.Sdk.Messages.RetrievePrincipalAccessRequest> class to allow retrieving a set of access rights defined within the <xref:Microsoft.Crm.Sdk.Messages.AccessRights> enumeration.

```csharp
/// <summary>
/// Gets which access rights a user has for a specific record.
/// </summary>
/// <param name="svc">The IOrganizationService instance to use.</param>
/// <param name="user">The user to check</param>
/// <param name="entity">A reference to the entity to check.</param>
/// <returns>The access rights the user can perform.</returns>

static AccessRights GetAccessRights(IOrganizationService svc, EntityReference
user, EntityReference entity) {

  try
  {
    var accessRightsRequest = new RetrievePrincipalAccessRequest() 
        { Principal = user, Target = entity };

    return ((RetrievePrincipalAccessResponse)svc.Execute(accessRightsRequest)).AccessRights;
  }
  catch (Exception)
  {
    throw;
  }
}
```

For the Web API use the <xref:Microsoft.Dynamics.CRM.RetrievePrincipalAccess> function and <xref:Microsoft.Dynamics.CRM.AccessRights> EnumType.

With the value returned by this method, you can use the [Enum.HasFlag Method](/dotnet/api/system.enum.hasflag#System_Enum_HasFlag_System_Enum_)
to return a Boolean value when the user has access to perform specific
operations on the table. The following code snippet shows how to use the above
GetAccessRights() method to test whether a user has access to append records
to a specific account record using the `AppendToAccess` member.

```C#
var whoIAm = (WhoAmIResponse)svc.Execute(new WhoAmIRequest());

var me = new EntityReference("systemuser", whoIAm.UserId);

// TODO Substitute a valid accountid GUID here.
var exampleAccount = (Account)svc.Retrieve("account",
    new Guid("4e9f3434-20e5-e811-a975-000d3af49bf8"), new ColumnSet("accountid"));

var accessRights = GetAccessRights(svc, me, exampleAccount.ToEntityReference());

var canAppendTo = accessRights.HasFlag(AccessRights.AppendToAccess);
```

With access to a table record, you can use this method to test any
operations that apply to that record. But this doesn't include capabilities that
apply to other operations, such as creating a new record or any other privilege
that isn't bound to a specific table.

### Get Principals with access to a record

Some data operations require another user have access to a record. If you have
just one specific user or team, you can test the other user using the `RetrievePrincipalAccess` message (<xref:Microsoft.Dynamics.CRM.RetrievePrincipalAccess> function, <xref:Microsoft.Crm.Sdk.Messages.RetrievePrincipalAccessRequest> class).

The `RetrieveSharedPrincipalsAndAccess` message (Web API <xref:Microsoft.Dynamics.CRM.RetrieveSharedPrincipalsAndAccess?text=RetrieveSharedPrincipalsAndAccess Function> or .NET SDK <xref:Microsoft.Crm.Sdk.Messages.RetrieveSharedPrincipalsAndAccessRequest?text=RetrieveSharedPrincipalsAndAccessRequest Class>) returns a list of all the users that a record has been shared with. It provides details about the access rights each user has because the record was shared with them.

## Check a user's security privileges

When you don't have a specific table record to test, such as whether they can
create a new table record, you must rely on checking the user's security
privileges. These privileges are stored in the [Privilege table](reference/entities/privilege.md).

There are nearly one thousand individual privileges in the Dataverse database and the
number will grow with every table or custom action that is added to the system.
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

In addition to the privileges for tables, there are less than one hundred other
special privileges that are not associated with tables. You can use the
following query to retrieve these.

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
|`RetrieveUserPrivilegeByPrivilegeId`| <xref:Microsoft.Dynamics.CRM.RetrieveUserPrivilegeByPrivilegeId?text=RetrieveUserPrivilegeByPrivilegeId Function><br/><xref:Microsoft.Crm.Sdk.Messages.RetrieveUserPrivilegeByPrivilegeIdRequest?text=RetrieveUserPrivilegeByPrivilegeIdRequest Class> |
|`RetrieveUserPrivilegeByPrivilegeName`| <xref:Microsoft.Dynamics.CRM.RetrieveUserPrivilegeByPrivilegeName?text=RetrieveUserPrivilegeByPrivilegeName Function><br/><xref:Microsoft.Crm.Sdk.Messages.RetrieveUserPrivilegeByPrivilegeNameRequest?text=RetrieveUserPrivilegeByPrivilegeNameRequest Class> |
|`RetrieveUserSetOfPrivilegesByIds`| <xref:Microsoft.Dynamics.CRM.RetrieveUserSetOfPrivilegesByIds?text=RetrieveUserSetOfPrivilegesByIds Function>|
|`RetrieveUserSetOfPrivilegesByNames`| <xref:Microsoft.Dynamics.CRM.RetrieveUserSetOfPrivilegesByNames?text=RetrieveUserSetOfPrivilegesByNames Function>|

<!-- As of 2022-5-21 there are no SDK request classes for RetrieveUserSetOfPrivilegesByIds or RetrieveUserSetOfPrivilegesByNames -->

### Example: Check whether a user has a privilege

The following examples show the use of the `RetrieveUserPrivilegeByPrivilegeName` message.

# [Web API](#tab/webapi)

This example tests whether the a user with systemuserid of `00000000-0000-0000-0000-000000000001` has the `prvReadAuditSummary` privilege. Because the <xref:Microsoft.Dynamics.CRM.RetrieveUserPrivilegeByPrivilegeNameResponse?text=RetrieveUserPrivilegeByPrivilegeNameResponse  ComplexType>`.RolePrivileges` collection contains data, the user has the privilege.

**Request**

```http
GET [Organization Uri]/api/data/v9.2/systemusers(00000000-0000-0000-0000-000000000001)/Microsoft.Dynamics.CRM.RetrieveUserPrivilegeByPrivilegeName(PrivilegeName='prvReadAuditSummary') HTTP/1.1
OData-MaxVersion: 4.0
OData-Version: 4.0
If-None-Match: null
Prefer: odata.include-annotations="*"
```

**Response**

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
- <xref:Microsoft.Dynamics.CRM.RetrieveUserPrivilegeByPrivilegeName?text=RetrieveUserPrivilegeByPrivilegeName Function>
- <xref:Microsoft.Dynamics.CRM.RetrieveUserPrivilegeByPrivilegeNameResponse?text=RetrieveUserPrivilegeByPrivilegeNameResponse  ComplexType>

# [.NET SDK](#tab/sdk)

```csharp
/// <summary>
/// Returns whether specified user has a named privilege
/// </summary>
/// <param name="svc">The IOrganizationService instance to use.</param>
/// <param name="systemUserId">The Id of the user.</param>
/// <param name="privilegeName">The name of the privilege.</param>
/// <returns></returns>
static bool HasPrivilege(IOrganizationService svc,
Guid systemUserId,
string privilegeName)
{
    var req = new
        RetrieveUserPrivilegeByPrivilegeNameRequest
    {
        PrivilegeName = privilegeName,
        UserId = systemUserId
    };
    try
    {
        var resp =
            (RetrieveUserPrivilegeByPrivilegeNameResponse)svc
            .Execute(req);
        if (resp.RolePrivileges.Length > 0)
        {
            return true;
        }
    }
    catch (System.ServiceModel.FaultException)
    {
        //Invalid userid or privilege name
        throw;
    }
    catch (Exception)
    {
        throw;
    }
    return false;
}
```

More information:

- <xref:Microsoft.Xrm.Sdk.IOrganizationService.Execute*?text=IOrganizationService.Execute Method>
- <xref:Microsoft.Crm.Sdk.Messages.RetrieveUserPrivilegeByPrivilegeNameResponse?text=RetrieveUserPrivilegeByPrivilegeNameResponse Class>

---

## Retrieve privileges for a security role

You can retrieve privileges by security role. Below is a Web API example showing how this is done.

**Request**

```http
GET [Organization URI]/api/data/v9.0/roles(<role ID>)/roleprivileges_association?$select=name&$orderby=privilegeid 
```

### See Also

[Plug-ins](plug-ins.md)

[!INCLUDE[footer-include](../../includes/footer-banner.md)]
