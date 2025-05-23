---
title: avoid-window-top Power Apps checker reference | Microsoft Docs
description: Power Apps checker rule reference for avoid-window-top.
author: ecarrleemsft
ms.topic: reference
ms.date: 07/18/2022
ms.service: "powerapps"
ms.subservice: dataverse-maker
ms.author: matp
search.audienceType: 
  - maker
---
# `avoid-window-top`

Don't use `window.top` or `window.parent.parent`. Using either of these fields will likely result in cross-origin security errors when hosted outside of the primary web client. Develop an alternate approach. For more information, go to [best practices: avoid-window-top](/power-apps/developer/model-driven-apps/best-practices/business-logic/avoid-window-top).
