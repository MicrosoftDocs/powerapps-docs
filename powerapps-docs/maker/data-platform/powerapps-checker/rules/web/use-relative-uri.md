---
title: use-relative-uri Power Apps checker reference | Microsoft Docs
description: Power Apps checker rule reference for use-relative-uri.
author: ecarrleemsft
ms.topic: reference
ms.date: 07/18/2022
ms.service: "powerapps"
ms.subservice: dataverse-maker
ms.author: matp
search.audienceType: 
  - maker
---
# `use-relative-uri`

Don't use absolute Microsoft Dataverse endpoint URLs.

## Recommendation

Don't use an absolute reference to a Microsoft Dataverse endpoint. Microsoft Dataverse endpoint URLs should be constructed using the appropriate client API function along with a relative path to the desired endpoint.
