---
title: use-appsidepane-api Power Apps checker reference | Microsoft Docs
description: Power Apps checker rule reference for use-appsidepane-api.
author: tylerol
ms.topic: reference
ms.date: 10/20/2023
ms.service: "powerapps"
ms.subservice: dataverse-maker
ms.author: matp
search.audienceType: 
  - maker
---
# `use-appsidepane-api`

Use Xrm.App.sidePanes.createPane instead of Xrm.Panels.loadPanel.

## Recommendation

The Xrm.Panels.loadPanel API is being replaced with Xrm.App.sidePanes.createPane because the former only supports a single pane while the latter supports multiple panes. For more information, go to [Use with Xrm.App.panels.loadPanel](/power-apps/developer/model-driven-apps/clientapi/create-app-side-panes).
