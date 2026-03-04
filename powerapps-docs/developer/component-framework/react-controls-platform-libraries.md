---
title: "React controls & platform libraries | Microsoft Docs"
description: "You can achieve significant performance gains using React and platform libraries. When you use React and platform libraries, you're using the same infrastructure used by the Power Apps platform. This means you no longer have to package React and Fluent packages individually for each control."
keywords: "Component Framework, code components, Power Apps controls"
author: anuitz
ms.author: anuitz
ms.date: 10/10/2025
ms.reviewer: jdaly
ms.custom:
  - "dyn365-a11y"
  - "dyn365-developer"
ms.topic: how-to
ms.subservice: pcf
contributors:
  - miglisic
  - JimDaly
---

# React controls & platform libraries

When you use React and platform libraries, you're using the same infrastructure used by the Power Apps platform. This means you no longer have to package React and Fluent libraries individually for each control. All controls share a common library instance and version to provide a seamless and consistent experience.

By reusing the existing platform React and Fluent libraries, you can expect the following benefits:

- Reduced control bundle size
- Optimized solution packaging
- Faster runtime transfer, scripting, and control rendering
- Design and theme alignment with the Power Apps Fluent design system  

With the benefits available by reusing these component resources, we expect this approach will become the preferred way all Power Apps code components will be created after this feature reaches general availability.

> [!NOTE]
> With GA release, all existing virtual controls will continue to function. However, they should be rebuilt and deployed using the latest CLI version (>=1.37) to facilitate future platform React version upgrades.

## Prerequisites

As with any component, you must install [Visual Studio Code](https://code.visualstudio.com/Download) and the [Microsoft Power Platform CLI](../data-platform/powerapps-cli.md#install-microsoft-power-platform-cli) as described here: [Prerequisites](implementing-controls-using-typescript.md#prerequisites)

> [!NOTE]
> If you have already installed Power Platform CLI for Windows, make sure you are running the latest version by using the `pac install latest` command.
> The Power Platform Tools for Visual Studio Code should update automatically.

## Create a React component

> [!NOTE]
> These instructions expect that you have created code components before. If you have not, see this tutorial: [Create your first component](implementing-controls-using-typescript.md)

There's a new `--framework` (`-fw`) parameter for the [pac pcf init](/power-platform/developer/cli/reference/pcf#pac-pcf-init) command. Set the value of this parameter to `react`.

The following table shows the long form of the commands:

| Parameter           | Value             |
| ------------------- | ----------------- |
| `--name`            | `ReactSample`     |
| `--namespace`       | `SampleNamespace` |
| `--template`        | `field`           |
| `--framework`       | `react`           |
| `--run-npm-install` | `true` (default)  |

The following PowerShell command uses the parameter shortcuts and creates a React component project and run `npm-install` in the folder where you run the command:

```powershell
pac pcf init -n ReactSample -ns SampleNamespace -t field -fw react -npm
```

You can now build and view the control in the test harness as usual using `npm start`.

After you build the control, you can package it inside solutions and use it for model-driven apps (including custom pages) and canvas apps like standard code components.

## Differences from standard components

This section describes the differences between a React component and a standard component.

### ControlManifest.Input.xml

The [control element](manifest-schema-reference/control.md) `control-type` attribute is set to `virtual` rather than `standard`.

> [!NOTE]
> Changing this value does not convert a component from one type to another.

Within the [resources element](manifest-schema-reference/resources.md), find two new [platform-library element](manifest-schema-reference/platform-library.md) child elements like the following example:

```xml
<resources>
  <code path="index.ts" order="1" />
  <platform-library name="React" version="16.14.0" />
  <platform-library name="Fluent" version="9.46.2" />
</resources>
```
> [!NOTE]
> For more information about valid platform library versions, see [Supported platform libraries list](#supported-platform-libraries-list).

We recommend using platform libraries for Fluent 8 and 9. If you don't use Fluent, you should remove the `platform-library` element where the `name` attribute value is `Fluent`.

### Index.ts

The [ReactControl.init](reference/react-control/init.md) method for control initialization doesn't have `div` parameters because React controls don't render the DOM directly. Instead [ReactControl.updateView](reference/react-control/updateview.md) returns a ReactElement that has the details of the actual control in React format.

### bundle.js

React and Fluent libraries aren't included in the package because they're shared, therefore the size of bundle.js is smaller.

## Sample controls

The following controls are included in the samples. They function the same as their standard versions but offer better performance since they are virtual controls.

|Sample |Description|Link|
|---------|---------|---------|
|ChoicesPickerReact|The standard [ChoicesPickerControl](https://github.com/microsoft/PowerApps-Samples/tree/master/component-framework/ChoicesPickerControl) converted to be a React Control. |[ChoicesPickerReact Sample](https://github.com/microsoft/PowerApps-Samples/tree/master/component-framework/ChoicesPickerReactControl)|
|FacepileReact|The [ReactStandardControl](https://github.com/microsoft/PowerApps-Samples/tree/master/component-framework/ReactStandardControl) converted to be a React Control.|[FacepileReact](https://github.com/microsoft/PowerApps-Samples/tree/master/component-framework/FacepileReactControl)|

## Supported platform libraries list

Platform libraries are made available both at the build and runtime to the controls that are using platform libraries capability. Currently, the following versions are provided by the platform and are the highest currently supported versions.

| Name   | npm package name            | Allowed version range  | Version loaded |
| ------ | --------------------------- | ---------------------- | -------------- |
| React  | react                       | 16.14.0                | 17.0.2 (Model), 16.14.0 (Canvas) |
| Fluent | @fluentui/react             | 8.29.0                 | 8.29.0         |
| Fluent | @fluentui/react             | 8.121.1                | 8.121.1        |
| Fluent | @fluentui/react-components  | >=9.4.0 <=9.46.2       | 9.68.0         |

> [!NOTE]
> The application might load a higher compatible version of a platform library at runtime, but the version might not be the latest version available. Fluent 8 and Fluent 9 are each supported but can not both be specified in the same manifest.

## FAQ

### Q: Can I convert an existing standard control to a React control using platform libraries?

A: No. You must create a new control using the new template and then update the manifest and index.ts methods. For reference, compare the standard and react samples described above.

### Q: Can I use React controls & platform libraries with Power Pages?

A: No. React controls & platform libraries are currently only supported for canvas and model-driven apps. In Power Pages, React controls don't update based on changes in other fields.

## Related articles

[What are code components?](custom-controls-overview.md)<br/>
[Code components for canvas apps](component-framework-for-canvas-apps.md)<br/>
[Create and build a code component](create-custom-controls-using-pcf.md)<br/>
[Learn Power Apps component framework](/training/paths/use-power-apps-component-framework)<br/>
[Use code components in Power Pages](../../maker/portals/component-framework.md)

[!INCLUDE[footer-include](../../includes/footer-banner.md)]
