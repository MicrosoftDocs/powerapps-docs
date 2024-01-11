---
title: avoid-loadtheme Power Apps checker reference | Microsoft Docs
description: Power Apps checker rule reference for avoid-loadtheme.
author: lesyk
ms.topic: reference
ms.date: 02/17/2023
ms.service: "powerapps"
ms.subservice: dataverse-maker
ms.author: vilesyk
search.audienceType:
  - maker
---

# `avoid-loadtheme`

`loadTheme` is a way to provide a theme in global (and only global) scope, which will affect your entire application. We recommend that you replace `loadTheme` with `ThemeProvider`. That way, your application consistently has one way of providing a theme.

## Recommendation

For details on the correct `ThemeProvider` usage go to the [ThemeProvider](https://github.com/microsoft/fluentui/wiki/How-to-apply-theme-to-Fluent-UI-React-components#themeprovider-in-preview) documentation.
