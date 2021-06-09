---
title: "Sharing and assigning (Microsoft Dataverse) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "Learn about the security that applies to sharing and assigning records." # 115-145 characters including spaces. This abstract displays in the search result.
ms.custom: ""
ms.date: 03/11/2021
ms.reviewer: "pehecke"
ms.service: powerapps
ms.topic: "article"
author: "paulliew" # GitHub ID
ms.author: "paulliew" # MSFT alias of Microsoft employees only
manager: "sunilg" # MSFT alias of manager or PM counterpart
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---
# Sharing and assigning

[!INCLUDE[cc-terminology](includes/cc-terminology.md)]

In this article we will look at the security access when sharing and assigning records.

## Sharing records

Sharing lets users give other users or teams access to specific customer
information. This is useful for sharing information with users in roles that
have only the **Basic** access level. For example, in an organization that gives
salespeople **Basic** read and write access to accounts, a salesperson can share an
opportunity with another salesperson so that they can both track the progress of
an important sale.

For security reasons, develop the practice of sharing only the necessary records
with the smallest set of users possible. Only grant the minimum access required
for users to do their jobs. A user might have access to the same record in more
than one context. For example, a user might share a record directly with
specific access rights, and he or she might also be on a team in which the same
record is shared with different access rights. In this case, the access rights
that this user has on the record are the union of all the rights.

When you share a record with another user using the `GrantAccess` message (<xref:Microsoft.Dynamics.CRM.GrantAccess> action, <xref:Microsoft.Crm.Sdk.Messages.GrantAccessRequest> class), or modify access using the `ModifyAccess` message (<xref:Microsoft.Dynamics.CRM.ModifyAccess> action, <xref:Microsoft.Crm.Sdk.Messages.ModifyAccessRequest> class), you must indicate what access rights you want to
grant to the other user. Access rights on a shared record can be different for
each user with whom the record is shared. However, you cannot give a user any
rights that he or she would not have for that type of table, based on the role
assigned to that user. For example, if a user does not have **Read** privileges on
accounts and you share an account with that user, the user will be unable to see
that account.

### Sharing and inheritance

If a record is created and the parent record has certain sharing properties, the
new record inherits those properties. For example, Joe and Mike are working on a
high priority lead. Joe creates a new lead and two activities, shares the lead
with Mike, and selects cascade sharing. Mike makes a telephone call and sends an
email regarding the new lead. Joe sees that Mike has contacted the company two
times, so he does not make another call.

Sharing is maintained on individual records. A record inherits the sharing
properties from its parent and maintains its own sharing properties. Therefore,
a record can have two sets of sharing properties — one that it has on its own, and
one that it inherits from its parent.

Removing the share of a parent record removes the sharing properties of objects
(records) that it inherited from the parent. That is, all users who previously
had visibility into this record no longer have visibility. Child objects still
could be shared to some of these users if they were shared individually, not
from the parent record.

## Assigning records

Anyone with **Assign** access rights on a record can assign that record to
another user. When a record is assigned, the new user or team becomes the owner
of the record and its related records. The original user or team loses ownership
of the record, but automatically shares it with the new owner.

In Microsoft Dataverse, the system administrator can decide for an organization
whether records should be shared with previous owners or not after the assign
operation. If **Share reassigned records with original owner** is selected (see **System Settings** > **General**), then the previous owner
shares the record with all access rights after the assign operation. Otherwise,
the previous owner does not share the record and may not have access to the
record, depending on his or her privileges. The Organization table's
[ShareToPreviousOwnerOnAssign](reference/entities/organization.md#sharetopreviousowneronassign-choicesoptions) column controls this setting.

## Revoking access

As the owner of a record, you can revoke (remove) user access to your shared record. To do so, use the `RevokeAccess` message (<xref:Microsoft.Dynamics.CRM.RevokeAccess> action, <xref:Microsoft.Crm.Sdk.Messages.RevokeAccessRequest> class).

More information: [Shared access](/power-platform/admin/how-record-access-determined#shared-access.md)

### See also

[Sample: Share records using GrantAccess, ModifyAccess and RevokeAccess messages](org-service/samples/share-records-using-grantaccess-modifyaccess-revokeaccess-messages.md)

[!INCLUDE[footer-include](../../includes/footer-banner.md)]

