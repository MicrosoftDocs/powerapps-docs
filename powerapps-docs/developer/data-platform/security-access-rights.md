---
title: "Data operations and access rights (Microsoft Dataverse) | Microsoft Docs" 
description: "Describes the access rights needed for specific data operations." 
ms.custom: ""
ms.date: 02/26/2024
ms.reviewer: "pehecke"

ms.topic: "article"
author: "paulliew" # GitHub ID
ms.subservice: dataverse-developer
ms.author: "paulliew" # MSFT alias of Microsoft employees only
search.audienceType: 
  - developer
---
# Data operations and access rights

[!INCLUDE[cc-terminology](includes/cc-terminology.md)]

Let's talk about the data operations that you can perform and the access rights required for each. The following table lists the messages that correspond with common data operations and the access rights required to execute those messages.

| Messages | Access rights required |
|---|---|
| **Create** | CREATE |
| **Retrieve**, **RetrieveMultiple** | READ |
| **Update** | WRITE |
| **Delete** | DELETE |
| **Associate** | APPEND |
| **Associate**  | APPENDTO |
| **Update** of the `ownerid` column, or the legacy **Assign** message | ASSIGN |
| **GrantAccess**, **ModifyAccess**, **RevokeAccess**  | SHARE |

## Dependencies between access rights

Sometimes, security dependencies exist because it's necessary to have more than
one access right to perform a given action. For example, if you have the
**create** access right for accounts, you can create a record of the account
table type. However, unless you also have **read** access for accounts, you
can't create an account record and be the owner of that new record.

The following table lists the access right dependencies for the actions
specified.

| Action | Access rights required |
|---|---|
| Create a record and be the record owner | CREATE, READ  |
| Share a record | SHARE. This right is required by the person doing the share operation.<p/> READ. This right is required by the person doing the share operation and also by the person with whom the record is being shared.|
| Assign a record | ASSIGN, WRITE, READ <sup>1</sup> |
| Append to a record | WRITE, READ, APPENDTO |
| Append a record | WRITE, READ, APPEND |

<sup>1</sup> To provide granular level control on whom a record can be assigned to, switch the **AssertOwnershipAppendToAccess** [orgdbsettings](/power-platform/admin/environment-database-settings#install-the-organizationsettingseditor-tool) to **true**. This setting additionally requires the caller to have **AppendTo** access on the assignee (the user/team record being assigned as the owner).
When [record ownership](/power-platform/admin/wp-security-cds#record-ownership-in-modernized-business-units) in modernized business units is enabled, and **OwningBusinessUnit** is being changed, the caller is required to have **AppendTo** access on the new business unit. 

Another type of dependency exists when objects are subordinate to another
object. For example, the opportunity object can't exist on its own. Each
opportunity is always attached to an account or contact. To create an
opportunity, you must have the access right **appendto** on accounts and the
access right **append** on opportunities.

### See Also

[How access to a record is determined](/power-platform/admin/how-record-access-determined)

[!INCLUDE[footer-include](../../includes/footer-banner.md)]
