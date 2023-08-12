---
title: "Sharing and assigning (Microsoft Dataverse) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "Learn about the security that applies to sharing and assigning records." # 115-145 characters including spaces. This abstract displays in the search result.
ms.date: 06/06/2023
ms.reviewer: pehecke
ms.topic: article
author: paulliew # GitHub ID
ms.subservice: dataverse-developer
ms.author: paulliew # MSFT alias of Microsoft employees only
search.audienceType: 
  - developer
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
    "accountid": "e41ac31a-dcdf-ed11-a7c7-000d3a993550",
    "@odata.type": "Microsoft.Dynamics.CRM.account"
  },
  "PrincipalAccess": {
    "AccessMask": "WriteAccess, DeleteAccess",
    "Principal": {
      "systemuserid": "7761da90-2383-e911-a962-000d3a13c05d",
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
    "accountid": "e41ac31a-dcdf-ed11-a7c7-000d3a993550",
    "@odata.type": "Microsoft.Dynamics.CRM.account"
  },
  "PrincipalAccess": {
    "AccessMask": "WriteAccess, DeleteAccess, ShareAccess, AssignAccess",
    "Principal": {
      "systemuserid": "7761da90-2383-e911-a962-000d3a13c05d",
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
[ShareToPreviousOwnerOnAssign](reference/entities/organization.md#sharetopreviousowneronassign-choicesoptions) column controls this setting.

> [!NOTE]
> The [Appointment table](reference/entities/appointment.md) has special logic when an appointment is assigned to another user. If the current owner is still a participant, such as the organizer or an attendee, the appointment record is shared with this user when the appointment is reassigned. This behavior occurs even if the **Share reassigned records with original owner** setting is disabled. Because the appointment may be shared with the previous owner, the user assigning the meeting requires both the **Assign** and **Share** access rights on the record.

## Revoking access

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
    "accountid": "e41ac31a-dcdf-ed11-a7c7-000d3a993550",
    "@odata.type": "Microsoft.Dynamics.CRM.account"
  },
  "Revokee": {
    "systemuserid": "7761da90-2383-e911-a962-000d3a13c05d",
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

### See also

[Sample: Share records using GrantAccess, ModifyAccess and RevokeAccess messages](org-service/samples/share-records-using-grantaccess-modifyaccess-revokeaccess-messages.md)

[!INCLUDE[footer-include](../../includes/footer-banner.md)]

