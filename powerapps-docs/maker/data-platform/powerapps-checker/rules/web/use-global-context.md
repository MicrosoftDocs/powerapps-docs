---
title: use-global-context Power Apps checker reference | Microsoft Docs
description: Power Apps checker rule reference for use-global-context.
author: ecarrleemsft
ms.topic: reference
ms.date: 07/18/2022
ms.service: "powerapps"
ms.subservice: dataverse-maker
ms.author: matp
search.audienceType: 
  - maker
---
# `use-global-context`

Don't use `Xrm.Page.context`. For access to the global context use `Xrm.Utility.getGlobalContext`.

## Recommendation

For more detail on appropriate replacement APIs, go to [Client API deprecations](/power-platform/important-changes-coming#some-client-apis-are-deprecated).
