---
title: do-not-make-parent-assumption Power Apps checker reference | Microsoft Docs
description: Power Apps checker rule reference for do-not-make-parent-assumption.
author: ecarrleemsft
ms.topic: reference
ms.date: 07/18/2022
ms.service: "powerapps"
ms.subservice: dataverse-maker
ms.author: matp
search.audienceType: 
  - maker
---
# `do-not-make-parent-assumption`

Don't assume that the usage of `global.parent`, `window.parent`, `window.opener`, or `this.parent` from JavaScript web resources will result in the same context across versions or client types, for example mobile, tablet, and browser. Consider a different approach when attempting to interact with one of these contexts. For more information, go to [best practices: avoid-window-top](/power-apps/developer/model-driven-apps/best-practices/business-logic/avoid-window-top).
