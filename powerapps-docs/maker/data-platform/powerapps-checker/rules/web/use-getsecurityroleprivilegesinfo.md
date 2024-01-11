---
title: use-getsecurityroleprivilegesinfo Power Apps checker reference | Microsoft Docs
description: Power Apps checker rule reference for use-getsecurityroleprivilegesinfo.
author: ecarrleemsft
ms.topic: reference
ms.date: 07/18/2022
ms.service: "powerapps"
ms.subservice: dataverse-maker
ms.author: matp
search.audienceType: 
  - maker
---
# `use-getsecurityroleprivilegesinfo`

Avoid `userSettings.securityRolePrivileges`. This returns only privilege GUIDs, which are difficult to work with. You might be making extra network requests to get further details about the privilege GUID and that degrades performance. Use [userSettings.getSecurityRolePrivilegesInfo()](/power-apps/developer/model-driven-apps/clientapi/reference/xrm-utility/getglobalcontext/usersettings#getsecurityroleprivilegesinfo) instead, which gives you more details about each security role privilege.
