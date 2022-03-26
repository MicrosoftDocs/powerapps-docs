---
title: "React Controls & Platform Libraries Public Preview| Microsoft Docs"
description: "You can achieve significant performance gains using React and platform libraries. When you use React and platform libraries, you are using the same infrastructure used by the Power Apps platform. This means you no longer have to package React and Fluent packages individually for each control."
keywords: "Component Framework, code components, Power Apps controls"
ms.author: jdaly
author: noazarur-microsoft
manager: kvivek
ms.date: 03/26/2022
ms.reviewer: jdaly
ms.custom:
  - "dyn365-a11y"
  - "dyn365-developer"
ms.topic: article
ms.subservice: pcf
---

# React Controls & Platform Libraries Public Preview

[!INCLUDE [cc-beta-prerelease-disclaimer](../../includes/cc-beta-prerelease-disclaimer.md)]

You can achieve significant performance gains using React and platform libraries. When you use React and platform libraries, you are using the same infrastructure used by the Power Apps platform. This means you no longer have to package React and Fluent packages individually for each control. All controls will share a common library instance and version to provide a seamless and consistent experience.

By re-using the existing platform React and Fluent libraries, you can expect the following benefits:

- Reduced control bundle size
- Optimized solution packaging
- Faster runtime transfer, scripting and control rendering

With the benefits available by re-using these component resources, we expect this approach will become the standard way all Power Apps components will be created after this feature reaches general availability.

## Prerequisites

Just as with any component, you must install [Visual Studio Code](https://code.visualstudio.com/Download) and the [Microsoft Power Platform CLI](../data-platform/powerapps-cli.md#install-microsoft-power-platform-cli) as described here: [Prerequisites](implementing-controls-using-typescript.md#prerequisites)

> [!NOTE]
> If you have already installed the Microsoft Power Platform CLI, make sure you are running the latest version by using the `pac install latest` command.

<!-- Will there be any additional steps to enable the feature? -->

## Create a React component

> [!NOTE]
> These instructions expect that you have created components before. If you have not, see this tutorial: [Create your first component](implementing-controls-using-typescript.md)

There is a new `--framework` (`-fw`) parameter for the `pac pcf init` command. Set the value of this parameter to `react`.

The following PowerShell command will create a react component project and run `npm-install` in the `C:\pcf\reactsample` folder with the following parameters:


|Parameter  |Value  |
|---------|---------|
|`name`     |`ReactSample`|
|`namespace`|`SampleNamespace`|
|`template`|`field`|
|`framework`|`react`|
|`run-npm-install`|`true` (default)|

```powershell
PS C:\pcf\reactsample> pac pcf init `
-n ReactSample `
-ns SampleNamespace `
-t field `
-fw react `
-npm
```

You can now build and view the control in the test harness as usual using `npm start`.

After you build the control you can package it inside solutions and use it for model-driven and canvas apps like standard code components.

## Differences from standard components

These are the differences between a React component and a standard component.

### ControlManifest.Input.xml

The [control element](manifest-schema-reference/control.md) has a new 
