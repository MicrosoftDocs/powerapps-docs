---
title: Sharing and assigning
description: Learn about the security that applies to sharing and assigning records.
ms.date: 04/06/2025
ms.reviewer: pehecke
ms.topic: concept-article
author: paulliew
ms.subservice: dataverse-developer
ms.author: paulliew
search.audienceType: 
  - developer
contributors: 
  - JimDaly
  - SEOKK-MSFT
---
# Sharing and assigning

[!INCLUDE[cc-terminology](includes/cc-terminology.md)]

In this article, we'll look at security access when sharing and assigning records.

## Sharing records

Sharing lets users give other users or teams access to specific customer
information. Sharing records is useful for sharing information with users in roles that
have only the **Basic** access level. For example, in an organization that gives
salespeople **Basic** read and write access to accounts, a salesperson can share an
opportunity with another salesperson so that they can both track the progress of
an important sale.

For security reasons, develop the practice of sharing only the necessary records
with the smallest set of users possible. Only grant the minimum access required
for users to do their jobs. A user might have access to the same record in more
than one context. For example, a user might share a record directly with
specific access rights, and they might also be on a team in which the same
record is shared with different access rights. In this case, the access rights
that this user has on the record are the union of all the rights.

When you share a record with another user using the `GrantAccess` message, you must indicate what access rights you want to
grant to the other user. To modify the access of a shared record, use the `ModifyAccess` message. Access rights on a shared record can be different for each user with whom the record is shared. However, you can't give a user any
rights that they wouldn't have for that type of table, based on the role
assigned to that user. For example, if a user doesn't have **Read** privileges on
accounts and you share an account with that user, the user is unable to see
that account.


### GrantAccess example

These examples show the use of the `GrantAccess` message to share a record with another principal.

#### [SDK for .NET](#tab/sdk)

The following `ShareRecord` static method shows how to use the [PrincipalAccess Class](xref:Microsoft.Crm.Sdk.Messages.PrincipalAccess) to specify a reference to a principal (user, team, or organization) with a set of [AccessRights](xref:Microsoft.Crm.Sdk.Messages.AccessRights) that contain the rights that to be granted to the principal.

```csharp
/// <summary>
/// Shares a record with a principal
/// </summary>
/// <param name="service">Authenticated client implementing the IOrganizationService interface</param>
/// <param name="principal">The user, team, or organization to share the record with.</param>
/// <param name="access">The access rights to grant</param>
/// <param name="record">The record to share</param>
static void ShareRecord(
   IOrganizationService service,
   EntityReference principal,
   AccessRights access,
   EntityReference record)
{

   PrincipalAccess principalAccess = new()
   {
         AccessMask = access,
         Principal = principal
   };

   GrantAccessRequest request = new()
   {
         PrincipalAccess = principalAccess,
         Target = record
   };

   service.Execute(request);
}
```

#### [Web API](#tab/webapi)

The following example shows the use of the [GrantAccess Action](xref:Microsoft.Dynamics.CRM.GrantAccess) using the [PrincipalAccess ComplexType](xref:Microsoft.Dynamics.CRM.PrincipalAccess) to specify the principal (user, team, or organization) and level of access to grant using the values in the [AccessRights EnumType](xref:Microsoft.Dynamics.CRM.AccessRights).

**Request:**

```http
POST [Organization Uri]/api/data/v9.2/GrantAccess
OData-MaxVersion: 4.0
OData-Version: 4.0
If-None-Match: null
Accept: application/json
Content-Type: application/json; charset=utf-8
Content-Length: 361

{
  "Target": {
    "accountid": "aaaaaaaa-0000-1111-2222-bbbbbbbbbbbb",
    "@odata.type": "Microsoft.Dynamics.CRM.account"
  },
  "PrincipalAccess": {
    "AccessMask": "WriteAccess, DeleteAccess",
    "Principal": {
      "systemuserid": "22cc22cc-dd33-ee44-ff55-66aa66aa66aa",
      "@odata.type": "Microsoft.Dynamics.CRM.systemuser"
    }
  }
}
```

**Response:**

```http
HTTP/1.1 204 NoContent
OData-Version: 4.0
```

---

### ModifyAccess example

These examples show the use of the `ModifyAccess` message to change the access granted to a principal for a shared record.

#### [SDK for .NET](#tab/sdk)

The following `ModifyShare` static method shows how to use the [PrincipalAccess Class](xref:Microsoft.Crm.Sdk.Messages.PrincipalAccess) to specify a reference to a principal (user, team, or organization) with a set of [AccessRights](xref:Microsoft.Crm.Sdk.Messages.AccessRights) that contain the rights that will be modified for the principal.

```csharp
/// <summary>
/// Modifies the access to a shared record.
/// </summary>
/// <param name="service">Authenticated client implementing the IOrganizationService interface</param>
/// <param name="principal">The user, team, or organization to modify rights to the shared.</param>
/// <param name="access">The access rights to modify</param>
/// <param name="record">The shared record</param>
static void ModifyShare(
   IOrganizationService service,
   EntityReference principal,
   AccessRights access,
   EntityReference record)
{
   PrincipalAccess principalAccess = new()
   {
         AccessMask = access,
         Principal = principal
   };

   ModifyAccessRequest request = new()
   {

         PrincipalAccess = principalAccess,
         Target = record
   };

   service.Execute(request);
}
```

#### [Web API](#tab/webapi)

The following example shows the use of the [ModifyAccess Action](xref:Microsoft.Dynamics.CRM.ModifyAccess) using the [PrincipalAccess ComplexType](xref:Microsoft.Dynamics.CRM.PrincipalAccess) to specify the principal (user, team, or organization) and level of access to modify using the values in the [AccessRights EnumType](xref:Microsoft.Dynamics.CRM.AccessRights).

**Request:**

```http
POST [Organization Uri]/api/data/v9.2/ModifyAccess
OData-MaxVersion: 4.0
OData-Version: 4.0
If-None-Match: null
Accept: application/json
Content-Type: application/json; charset=utf-8
Content-Length: 388

{
  "Target": {
    "accountid": "aaaaaaaa-0000-1111-2222-bbbbbbbbbbbb",
    "@odata.type": "Microsoft.Dynamics.CRM.account"
  },
  "PrincipalAccess": {
    "AccessMask": "WriteAccess, DeleteAccess, ShareAccess, AssignAccess",
    "Principal": {
      "systemuserid": "22cc22cc-dd33-ee44-ff55-66aa66aa66aa",
      "@odata.type": "Microsoft.Dynamics.CRM.systemuser"
    }
  }
}
```

**Response:**

```http
HTTP/1.1 204 NoContent
OData-Version: 4.0
```

---

### RevokeAccess example

The owner of the record can use the `RevokeAccess` message to revoke (remove) user access to the shared record.

### [SDK for .NET](#tab/sdk)

The following `RevokeShare` static method shows how to remove sharing access for a user to a record using the [RevokeAccessRequest Class](xref:Microsoft.Crm.Sdk.Messages.RevokeAccessRequest).

```csharp
/// <summary>
/// Revokes access to a shared record.
/// </summary>
/// <param name="service">Authenticated client implementing the IOrganizationService interface</param>
/// <param name="principal">The user, team, or organization to revoke rights to the shared record.</param>
/// <param name="record">The shared record</param>
static void RevokeShare(
   IOrganizationService service,
   EntityReference principal,
   EntityReference record)
{
   RevokeAccessRequest request = new()
   {
         Revokee = principal,
         Target = record
   };

   service.Execute(request);
}
```

### [Web API](#tab/webapi)

The following example shows how to use the [RevokeAccess Action](xref:Microsoft.Dynamics.CRM.RevokeAccess) to remove sharing access for a user to a record. In this example, a user is the `Revokee`, and an account record is the `Target`.

**Request:**

```http
POST [Organization Uri]/api/data/v9.2/RevokeAccess
OData-MaxVersion: 4.0
OData-Version: 4.0
If-None-Match: null
Accept: application/json
Content-Type: application/json; charset=utf-8
Content-Length: 274

{
  "Target": {
    "accountid": "aaaaaaaa-0000-1111-2222-bbbbbbbbbbbb",
    "@odata.type": "Microsoft.Dynamics.CRM.account"
  },
  "Revokee": {
    "systemuserid": "00aa00aa-bb11-cc22-dd33-44ee44ee44ee",
    "@odata.type": "Microsoft.Dynamics.CRM.systemuser"
  }
}
```

**Response:**

```http
HTTP/1.1 204 NoContent
OData-Version: 4.0
```

---

More information: [Shared access](/power-platform/admin/how-record-access-determined#shared-access.md)

## Sharing and inheritance

If a record is created and the parent record has certain sharing properties, the
new record inherits those properties. For example, Joe and Mike are working on a
high priority lead. Joe creates a new lead and two activities, shares the lead
with Mike, and selects cascade sharing. Mike makes a telephone call and sends an
email regarding the new lead. Joe sees that Mike has contacted the company two
times, so Joe doesn't make another call.

Sharing is maintained on individual records. A record inherits the sharing
properties from its parent and maintains its own sharing properties. Therefore,
a record can have two sets of sharing properties—one that it has on its own, and
one that it inherits from its parent.

Removing the share of a parent record removes the sharing properties of objects
(records) that it inherited from the parent. That is, all users who previously
had visibility into this record no longer have visibility. Child objects still
could be shared to some of these users if they were shared individually, not
from the parent record.

## Assigning records

Anyone with **Assign** access rights on a record can assign that record to
another user. To assign a record, change the `ownerid` lookup value to refer to a new principal.

> [!NOTE]
> The SDK has an [AssignRequest class](xref:Microsoft.Crm.Sdk.Messages.AssignRequest) that is deprecated. More information: [Legacy update messages](org-service/entity-operations-update-delete.md#legacy-update-messages)

When a record is assigned, the new user, team or organization becomes the owner
of the record and its related records. The original user, team or organization loses ownership
of the record, but automatically shares it with the new owner.

In Microsoft Dataverse, the system administrator can decide for an organization
whether records should be shared with previous owners or not after the assign
operation. If **Share reassigned records with original owner** is selected (see **System Settings** > **General**), then the previous owner
shares the record with all access rights after the assign operation. Otherwise,
the previous owner doesn't share the record and may not have access to the
record, depending on their privileges. The Organization table's
[ShareToPreviousOwnerOnAssign](reference/entities/organization.md#BKMK_ShareToPreviousOwnerOnAssign) column controls this setting.

> [!NOTE]
> The [Appointment table](reference/entities/appointment.md) has special logic when an appointment is assigned to another user. If the current owner is still a participant, such as the organizer or an attendee, the appointment record is shared with this user when the appointment is reassigned. This behavior occurs even if the **Share reassigned records with original owner** setting is disabled. Because the appointment may be shared with the previous owner, the user assigning the meeting requires both the **Assign** and **Share** access rights on the record.



## Determine why a user has access

The [check access](/power-apps/user/access-checker) feature in model-driven apps provides information so that people can understand why a user has access to a record. To get this information with code, use the `RetrieveAccessOrigin` message. When passed information about a specific user and record, this message returns a sentence that describes why the user has access. The following are the possible responses when the operation succeeds:


```text
Access origin could not be determined because FCB is disabled.
PrincipalId is object owner (<record ID>)
PrincipalId is member of team (<team ID>) who is object owner (<record ID>)
PrincipalId is member of organization (<organization ID>) who is object owner (<record ID>)
PrincipalId has access to (<hierarchy security principal ID>) through hierarchy security. (<hierarchy security principal ID>) is object owner (<record ID>)
PrincipalId has direct poa access to object (<record ID>)
PrincipalId is member of team (<team ID>) who has poa access to object (<record ID>)
PrincipalId is member of organization (<organization ID>) who has poa access to object (<record ID>)
PrincipalId is owner of a parent entity of object (<child record ID>)
PrincipalId is member of team (<team ID>) who is owner of a parent entity of object (<child record ID>)
PrincipalId is member of organization (<organization ID>) who is owner of a parent entity of object (<child record ID>)
PrincipalId has access to (<hierarchy security principal ID>) through hierarchy security. (<hierarchy security principal ID>) is owner of a parent entity of object (<child record ID>)
PrincipalId has poa access to object's root entity (<child record ID>)
PrincipalId is member of team (<team ID>) who has poa access to object's root entity (<child record ID>)
PrincipalId is member of organization (<organization ID>) who has poa access to object's root entity (<child record ID>)
Access origin could not be found. Access does not come from POA table or object ownership.
```

# [SDK for .NET](#tab/sdk)

> [!NOTE]
> There is not currently a `RetrieveAccessOriginRequest` or `RetrieveAccessOriginResponse` class in the SDK. To use this message you must use the <xref:Microsoft.Xrm.Sdk.OrganizationRequest> and <xref:Microsoft.Xrm.Sdk.OrganizationResponse> classes. [Learn more about using messages with the SDK for .NET](org-service/use-messages.md).

```csharp
/// <summary>
/// Describes why a principal (systemuser or team) has access to a record.
/// </summary>
/// <param name="service">The authenticated IOrganizationService instance to use.</param>
/// <param name="objectId">The unique identifier of a record.</param>
/// <param name="tableLogicalName">The logical name of the table for the record in the ObjectId parameter.</param>
/// <param name="principalId">The unique identifier of the systemuser or team record.</param>
/// <returns>A sentence explaining why the principal has access to a record.</returns>
public static void OutputRetrieveAccessOrigin(IOrganizationService service,
    Guid objectId,
    string tableLogicalName,
    Guid principalId)
{
 
    var parameters = new ParameterCollection()
        {
            { "ObjectId", objectId},
            { "LogicalName", tableLogicalName},
            { "PrincipalId", principalId}
        };
 
    var request = new OrganizationRequest()
    {
        RequestName = "RetrieveAccessOrigin",
        Parameters = parameters
    };
 
    var response = service.Execute(request);
 
    Console.WriteLine(response.Results["Response"]);
}
```

Example output: `PrincipalId is object owner (aaaaaaaa-bbbb-cccc-1111-222222222222)`


# [Web API](#tab/webapi)

The [RetrieveAccessOrigin function](xref:Microsoft.Dynamics.CRM.RetrieveAccessOrigin) returns a [RetrieveAccessOriginResponse complex type](xref:Microsoft.Dynamics.CRM.RetrieveAccessOriginResponse). [Learn more about Dataverse Web API functions](webapi/use-web-api-functions.md).

**Request**:

```http
GET [Organization URI]/api/data/v9.2/RetrieveAccessOrigin(ObjectId=@objectId,LogicalName=@logicalName,PrincipalId=@principalId)?
@objectId=aaaaaaaa-0000-1111-2222-bbbbbbbbbbbb
&@logicalName='account'
&@principalId=bbbbbbbb-cccc-dddd-2222-333333333333
Accept: application/json  
OData-MaxVersion: 4.0  
OData-Version: 4.0
```

**Response**:

```http
HTTP/1.1 200 OK  
Content-Type: application/json; odata.metadata=minimal  
OData-Version: 4.0  
{  
    "@odata.context": "[Organization URI]/api/data/v9.2/$metadata#Microsoft.Dynamics.CRM.RetrieveAccessOriginResponse",
    "Response": "PrincipalId is object owner (aaaaaaaa-bbbb-cccc-1111-222222222222)"
}
```

---

### See also

[Share data in secured fields](column-level-security.md#share-data-in-secured-fields)   
[Sample: Share records using GrantAccess, ModifyAccess and RevokeAccess messages](org-service/samples/share-records-using-grantaccess-modifyaccess-revokeaccess-messages.md)

[!INCLUDE[footer-include](../../includes/footer-banner.md)]
