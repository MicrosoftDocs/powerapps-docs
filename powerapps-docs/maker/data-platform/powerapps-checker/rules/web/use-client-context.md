---
title: use-client-context Power Apps checker reference | Microsoft Docs
description: Power Apps checker rule reference for use-client-context.
author: ecarrleemsft
ms.topic: reference
ms.date: 07/18/2022
ms.service: "powerapps"
ms.subservice: dataverse-maker
ms.author: matp
search.audienceType: 
  - maker
---
# `use-client-context`

Don't use `Xrm.Page`. Although `Xrm.Page` is deprecated, `parent.Xrm.Page` will continue to work with HTML web resources embedded in forms as this is the only way to access the form context from the HTML web resource. For a more comprehensive list of appropriate replacements for `Xrm.Page` functionality, go to [Client API Deprecations](/power-platform/important-changes-coming#some-client-apis-are-deprecated).
