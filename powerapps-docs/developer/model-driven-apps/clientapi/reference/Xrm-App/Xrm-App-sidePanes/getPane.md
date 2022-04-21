---
title: "getPane (Client API reference) in model-driven apps| MicrosoftDocs"
description: Includes description and supported parameters for the getPane method.
ms.author: jdaly
author: adrianorth
manager: kvivek
ms.date: 04/04/2022
ms.reviewer: jdaly
ms.topic: "reference"
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
contributors:
  - JimDaly
---
# getPane (Client API reference)

Returns the side pane corresponding to the input ID. If the side pane does not exist, undefined is returned.

## Syntax

`Xrm.App.sidePanes.getPane(panelId);`

## Return value

Returns the [AppSidePane](../../xrm-app-appsidepane.md) object.

### Related topics

[sidePanes](../../xrm-app-sidepanes.md)

[Creating side panes using client API](../../../create-app-side-panes.md)