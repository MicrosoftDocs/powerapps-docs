---
title: "React controls & platform libraries (Preview) | Microsoft Docs"
description: "You can achieve significant performance gains using React and platform libraries. When you use React and platform libraries, you are using the same infrastructure used by the Power Apps platform. This means you no longer have to package React and Fluent packages individually for each control."
keywords: "Component Framework, code components, Power Apps controls"
ms.author: jdaly
author: HemantGaur
manager: kvivek
ms.date: 03/31/2022
ms.reviewer: jdaly
ms.custom:
  - "dyn365-a11y"
  - "dyn365-developer"
ms.topic: article
ms.subservice: pcf
contributors:
  - HemantGaur
  - noazarur-microsoft
  - JimDaly
---

# React controls & platform libraries (Preview)

[!INCLUDE [cc-beta-prerelease-disclaimer](../../includes/cc-beta-prerelease-disclaimer.md)]

You can achieve significant performance gains using React and platform libraries. When you use React and platform libraries, you are using the same infrastructure used by the Power Apps platform. This means you no longer have to package React and Fluent libraries individually for each control. All controls will share a common library instance and version to provide a seamless and consistent experience.

By re-using the existing platform React and Fluent libraries, you can expect the following benefits:

- Reduced control bundle size
- Optimized solution packaging
- Faster runtime transfer, scripting and control rendering

With the benefits available by re-using these component resources, we expect this approach will become the preferred way all Power Apps code components will be created after this feature reaches general availability.

## Prerequisites

Just as with any component, you must install [Visual Studio Code](https://code.visualstudio.com/Download) and the [Microsoft Power Platform CLI](../data-platform/powerapps-cli.md#install-microsoft-power-platform-cli) as described here: [Prerequisites](implementing-controls-using-typescript.md#prerequisites)

> [!NOTE]
> If you have already installed the Standalone Power Platform CLI, make sure you are running the latest version by using the `pac install latest` command.
> The Power Platform Tools for Visual Studio Code should update automatically.

## Create a React component

> [!NOTE]
> These instructions expect that you have created code components before. If you have not, see this tutorial: [Create your first component](implementing-controls-using-typescript.md)

There is a new `--framework` (`-fw`) parameter for the [pac pcf init](/power-platform/developer/cli/reference/pcf#pac-pcf-init) command. Set the value of this parameter to `react`.

The following table shows the long form of the commands:

| Parameter           | Value             |
| ------------------- | ----------------- |
| `--name`            | `ReactSample`     |
| `--namespace`       | `SampleNamespace` |
| `--template`        | `field`           |
| `--framework`       | `react`           |
| `--run-npm-install` | `true` (default)  |

The following PowerShell command uses the parameter shortcuts and will create a React component project and run `npm-install` in the folder where you run the command:

```powershell
pac pcf init -n ReactSample -ns SampleNamespace -t field -fw react -npm
```

You can now build and view the control in the test harness as usual using `npm start`.

After you build the control you can package it inside solutions and use it for model-driven apps (including custom pages) and canvas apps like standard code components.

## Differences from standard components

These are the differences between a React component and a standard component.

### ControlManifest.Input.xml

The [control element](manifest-schema-reference/control.md) `control-type` attribute is set to `virtual` rather than `standard`.

> [!NOTE]
> Changing this value does not convert a component from one type to another.

Within the [resources element](manifest-schema-reference/resources.md), you will find two new [platform-library element](manifest-schema-reference/platform-library.md) child elements like the following:

```xml
<resources>
    <code path="index.ts" order="1" />
   <platform-library name="React" version="16.8.6" />
   <platform-library name="Fluent" version="8.29.0" />
</resources>
```

> [!NOTE]
> Do not change the version numbers for these `platform-library` elements. These are the versions used by the platform.

We recommend using Fluent platform libraries. If you don't use Fluent, you should remove this element: `<platform-library name="Fluent" version="8.29.0" />`

### Index.ts

The [ReactControl.init](reference/react-control/init.md) method for control initialization does not have `div` parameters because these controls do not render the DOM directly. Instead [ReactControl.updateView](reference/react-control/updateview.md) returns a ReactElement which has the details of the actual control in React format.

### bundle.js

React and Fluent libraries are not included in the package because they are shared, therfore the size of bundle.js is significantly smaller.

## Sample controls

You can find two new controls added to the samples as part of this preview. Functionally, they are the same as their standard version but will have much better performance.

|Sample |Description|Link|
|---------|---------|---------|
|ChoicesPickerReact|The standard [ChoicesPickerControl](https://github.com/microsoft/PowerApps-Samples/tree/master/component-framework/ChoicesPickerControl) converted to be a React Control. |[ChoicesPickerReact Sample](https://github.com/microsoft/PowerApps-Samples/tree/master/component-framework/ChoicesPickerReactControl)|
|FacepileReact|The [ReactStandardControl](https://github.com/microsoft/PowerApps-Samples/tree/master/component-framework/ReactStandardControl)converted to be a React Control.|[FacepileReact](https://github.com/microsoft/PowerApps-Samples/tree/master/component-framework/FacepileReactControl)|

## Supported platform libraries list

| Name   | Version |
| ------ | ------- |
| React  | 16.8.6  |
| Fluent | 8.29.0  |

## FAQ

### Q: Can I convert an existing standard control to a React control using platform libraries?

A: No. You must create a new control using the new template and then update the manifest and index.ts methods. For reference, compare the standard and react samples described above.

## Related topics

[What are code components?](custom-controls-overview.md)<br/>
[Code components for canvas apps](component-framework-for-canvas-apps.md)<br/>
[Create and build a code component](create-custom-controls-using-pcf.md)<br/>
[Learn Power Apps component framework](/training/paths/use-power-apps-component-framework)<br/>
[Use code components in Power Pages](../../maker/portals/component-framework.md)

[!INCLUDE[footer-include](../../includes/footer-banner.md)]
