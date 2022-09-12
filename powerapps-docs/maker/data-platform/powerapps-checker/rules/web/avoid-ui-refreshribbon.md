---
title: avoid-ui-refreshribbon Power Apps checker reference | Microsoft Docs
description: Power Apps checker rule reference for avoid-ui-refreshribbon.
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
# `avoid-ui-refreshribbon`

Don't use `ui.refreshRibbon` during evaluation of ribbon rules. This API triggers duplicated network calls from ribbon and degrades performance. Use promises and asynchronous patterns.