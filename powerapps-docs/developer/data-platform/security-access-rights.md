---
title: "Data operations and access rights (Microsoft Dataverse) | Microsoft Docs" 
description: "Describes the access rights needed for specific data operations." 
ms.custom: ""
ms.date: 03/11/2021
ms.reviewer: "pehecke"
ms.service: powerapps
ms.topic: "article"
author: "paulliew" # GitHub ID
ms.subservice: dataverse-developer
ms.author: "paulliew" # MSFT alias of Microsoft employees only
manager: "sunilg" # MSFT alias of manager or PM counterpart
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---
# Data operations and access rights

[!INCLUDE[cc-terminology](includes/cc-terminology.md)]

Let's talk about the data operations that you can performs and the access rights required for each. The following table lists the messages that correspond with common data operations and the access rights required to execute those messages.

| Message(s) | Access rights required |
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

Sometimes, security dependencies exist because it is necessary to have more than
one access right to perform a given action. For example, if you have the
**create** access right for accounts, you can create a record of the account
table type. However, unless you also have **read** access for accounts, you
cannot create an account record and be the owner of that new record.

The following table lists the access right dependencies for the actions
specified.

| Action | Access rights required |
|---|---|
| Create a record and be the record owner | CREATE, READ  |
| Share a record | SHARE. This right is required by the person doing the share operation.<p/> READ. This right is required by the person doing the share operation and also by the person with whom the record is being shared.|
| Assign a record | ASSIGN, WRITE, READ |
| Append to a record | WRITE, READ, APPENDTO |
| Append a record | WRITE, READ, APPEND |

Another type of dependency exists when objects are subordinate to another
object. For example, the opportunity object cannot exist on its own. Each
opportunity is always attached to an account or contact. To create an
opportunity, you must have the access right **appendto** on accounts and the
access right **append** on opportunities.

### See Also

[How access to a record is determined](/power-platform/admin/how-record-access-determined)

[!INCLUDE[footer-include](../../includes/footer-banner.md)]