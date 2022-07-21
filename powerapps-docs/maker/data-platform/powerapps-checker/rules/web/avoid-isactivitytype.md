---
title: avoid-isactivitytype Power Apps checker reference | Microsoft Docs
description: Power Apps checker rule reference for avoid-isactivitytype.
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
# `avoid-isactivitytype`

Replace Xrm.Utility.isActivityType method with new Xrm.Utility.getEntityMetadata and don't use in ribbon rules.

## Recommendation

For details on the correct Xrm.Utility functions go to the [Xrm.Utility.getEntityMetadata](/powerapps/developer/model-driven-apps/clientapi/reference/xrm-utility/getentitymetadata) documentation. 