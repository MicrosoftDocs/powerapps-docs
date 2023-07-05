---
title: use-utility-dialogs Power Apps checker reference | Microsoft Docs
description: Power Apps checker rule reference for use-utility-dialogs.
author: ecarrleemsft
ms.topic: reference
ms.date: 02/14/2023
ms.service: "powerapps"
ms.subservice: dataverse-maker
ms.author: matp
search.audienceType: 
  - maker
---
# `use-utility-dialogs`

Use Web API dialogs in form and ribbon commands.

## Recommendation

Alerts should be replaced with `Xrm.Navigation.openAlertDialog`,
while confirms should be replaced with `Xrm.Navigation.openConfirmDialog`. For more information, go to [Xrm.Navigation](/power-apps/developer/model-driven-apps/clientapi/reference/xrm-navigation).

## Options
- By default, violations are only reported when certain `Xrm` or `Mscrm` calls are made in the same file, so that violations outside of Dataverse are not reported.  The `requireXrm` option, which is `true` by default, can be set to `false` to report all violations regardless of `Xrm` or `Mscrm` usage
  - Example: `"@microsoft/power-apps/use-utility-dialogs": ["error", { requireXrm: false }]`
