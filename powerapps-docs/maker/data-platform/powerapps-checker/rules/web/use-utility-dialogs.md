---
title: use-utility-dialogs Power Apps checker reference | Microsoft Docs
description: Power app checker rule reference for use-utility-dialogs.
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
# `use-utility-dialogs`

Use Web API dialogs in form and ribbon commands.

## Recommendation

Alerts should be replaced with `Xrm.Navigation.openAlertDialog`,
while confirms should be replaced with `Xrm.Navigation.openConfirmDialog`. For more information, go to [Xrm.Navigation](/power-apps/developer/model-driven-apps/clientapi/reference/xrm-navigation).
