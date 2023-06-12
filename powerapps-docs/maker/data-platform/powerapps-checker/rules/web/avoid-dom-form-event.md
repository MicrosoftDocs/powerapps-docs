---
title: avoid-dom-form-event Power Apps checker reference | Microsoft Docs
description: Power Apps checker rule reference for avoid-dom-form-event.
author: ecarrleemsft
ms.topic: reference
ms.date: 02/14/2023
ms.service: "powerapps"
ms.subservice: dataverse-maker
ms.author: matp
search.audienceType: 
  - maker
---
# `avoid-dom-form-event`

Don't register or unregister handles to the Document Object Model (DOM) events of model-driven apps. This isn't a supported approach in Dynamics 365 or Power Apps. Use the supported [Client-side event handlers](/power-apps/developer/model-driven-apps/clientapi/reference/events) instead.

## Options
- By default, violations are only reported when certain `Xrm` or `Mscrm` calls are made in the same file, so that violations outside of Dataverse are not reported.  The `requireXrm` option, which is `true` by default, can be set to `false` to report all violations regardless of `Xrm` or `Mscrm` usage
  - Example: `"@microsoft/power-apps/avoid-dom-form-event": ["error", { requireXrm: false }]`
