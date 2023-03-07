---
title: use-org-setting Power Apps checker reference | Microsoft Docs
description: Power Apps checker rule reference for use-org-setting.
author: ecarrleemsft
manager: tapanm-msft
ms.topic: reference
ms.date: 07/18/2022
ms.service: "powerapps"
ms.subservice: dataverse-maker
ms.author: matp
search.audienceType: 
  - maker
search.app: 
  - PowerApps
---
# `use-org-setting`

Use organization settings. Specifically:
- Calls to `Xrm.Page.context.getIsAutoSaveEnabled()` should be replaced with `Xrm.Utility.getGlobalContext().organizationSettings.isAutoSaveEnabled`

- Calls to `Xrm.Page.context.getOrgLcid()` should be replaced with `Xrm.Utility.getGlobalContext().organizationSettings.languageId`

- Calls to `Xrm.Page.context.getOrgUniqueName()` should be replaced with `Xrm.Utility.getGlobalContext().organizationSettings.uniqueName`

## Recommendation

For more information, go to [Client API deprecations](/power-platform/important-changes-coming#some-client-apis-are-deprecated).
