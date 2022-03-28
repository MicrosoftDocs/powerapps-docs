---
title: "getPane (Client API reference) in model-driven apps| MicrosoftDocs"
description: Includes description and supported parameters for the getPane method.
ms.author: jdaly
author: adrianorth
manager: kvivek
ms.date: 03/12/2022
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

[!INCLUDE[cc-beta-prerelease-disclaimer](../../../../../../includes/cc-beta-prerelease-disclaimer.md)]

Returns the side pane corresponding to the input ID. If the side pane does not exist, undefined is returned.

> [!IMPORTANT]
> - This is a preview feature, and isn't available in all regions.
> - [!INCLUDE[cc-preview-features-definition](../../../../../../includes/cc-preview-features-definition.md)]

## Syntax

`Xrm.App.sidePanes.getPane(panelId);`

## Return value

Returns the [AppSidePane](../../xrm-app-appsidepane.md) object.

### Related topics

[sidePanes](../../xrm-app-sidepanes.md)

[Creating side panes using client API](../../../create-app-side-panes.md)