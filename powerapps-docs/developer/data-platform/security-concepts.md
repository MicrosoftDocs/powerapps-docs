---
title: "Security concepts for developers (Microsoft Dataverse) | Microsoft Docs" 
description: "A brief summary of security concepts." 
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
# Security concepts for developers

[!INCLUDE[cc-terminology](includes/cc-terminology.md)]

A brief summary of key security concepts that developers should understand is listed below. For more details about Microsoft Dataverse security see [Security concepts in Microsoft Dataverse](/power-platform/admin/wp-security-cds).

- Dataverse uses security roles to control what data operations users can perform.

- Each security role defines a set of privilege and access level combinations for each table. The combination of privilege and access provides *access rights*.

- A *privilege* is the capability to perform specific operation:
        **Create**, **Read**, **Write**, **Delete**, **Append**, **AppendTo**,
        **Assign**, and **Share**.
  - There are also some privileges that do not apply to tables, but to specific capabilities.

- Access level applies to operations that depend on how tables are owned.
  - There are five access levels: **Global**, **Deep**, **Local**, **Basic**, and **None**.
  - Some tables are owned by the organization. These access levels can only be **Global** or **None**, which are effectively on/off switches.
  - Some tables are owned by teams or users, which together are referred to as *security principals*.

  - For tables owned by security principals, the access levels refer to where the security principals are defined within a potential hierarchy of business units.
    - By default, there is one business unit. Organizations can configure multiple business units when they want to limit access or permissions within their organization.
    - Each security principal is associated with a single business unit.
    - Within a business unit, **Local** provides access to all data for that table within the business unit.
    - **Basic** provides access to a record that a user owns, either directly or by virtue of belonging to the team that owns the table record, or because the record was shared with them.
    - **None** prevents access to any records for the table.
    - **Global** and **Deep** only apply when there is a hierarchy of business units. **Global** provides access to all levels, and **Deep** provides access to the current business unit and any below it in the hierarchy.

- Each user can be associated with one or more security roles.

- Users can be associated with teams that can have security roles associated with them.

- The user’s access to perform specific operations on a given table record is the least restrictive evaluation of all the security roles that apply.

### See Also

[How access to a record is determined](/power-platform/admin/how-record-access-determined)

[!INCLUDE[footer-include](../../includes/footer-banner.md)]