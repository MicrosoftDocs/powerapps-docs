---
title: Source code files for canvas apps (pa.yaml)
description: Learn about how to view source code files for canvas apps.
author: marcelbf
ms.author: marcelbf
ms.date: 3/18/2025
ms.topic: how-to
ms.reviewer: 
ms.subservice: canvas-maker
ms.collection: get-started
search.audienceType: 
  - maker  
  - developer
ms.custom:
  - canvas  
---

# View source code files for canvas apps

Use the source code for a canvas app to review changes made by makers in Power Apps Studio. The generated canvas app YAML code is read-only and can't be modified. Any changes to the file are ignored and might be lost.

> - The YAML schema is in active development, and the content might be incomplete.
> - The current static schema for ***.pa.yaml** files is available [here](https://raw.githubusercontent.com/microsoft/PowerApps-Tooling/refs/heads/master/schemas/pa-yaml/v3.0/pa.schema.yaml).

Power Fx and YAML are the languages used for Power Apps source code. YAML is valued for its human-readable format and benefits from a wide array of editors, tools, and libraries for manipulation.

## Access source code files

You have access to the source code files if you're using the [Power Platform Git Integration](/power-platform/alm/git-integration/overview), eliminating the need for **.msapp** files.

The Power Apps Studio creates the source code for canvas apps, which is stored as *.pa.yaml files within the **.msapp** file. The **.msapp** file is a binary file that contains a collection of files, including the source code.

> [!TIP]
> To effectively use application lifecycle management (ALM), it's recommended to use solutions. [Canvas apps package](export-import-app-package.md) doesn't support ALM and should only be used for basic import and export capabilities when Dataverse isn't available.

You can also get the source code files either from the **.msapp** file or by using [Power Platform CLI](/power-platform/developer/cli/introduction).

The ***.pa.yaml** files can be found in the **\Src** folder of the extracted **.msapp**.

> [!Important]
> Only files located in the **\Src** directory of the extracted **.msapp** are intended for use with source control.
> The JSON files in the **.msapp** shouldn't be used as source code because those aren't stable between save and load cycles.

### Download and Extract the pa.yaml files using Power Platform CLI

Connect to your environment using Power Platform CLI and then use the following commands:

1. To list the canvas apps in your current environment, use the command: [pac canvas list](/power-platform/developer/cli/reference/canvas#pac-canvas-list).
1. To extract the source code files, use the command: [pac canvas download](/power-platform/developer/cli/reference/canvas#pac-canvas-download) with the [parameter -d](/power-platform/developer/cli/reference/canvas#--extract-to-directory--d).


### Extract source code files from a .msapp file

To extract source code files from a [.msapp file](export-import-single-app.md#export-msapp-files-in-power-apps), you have two options:

1. Manually unzip the **.msapp** file.
1. Alternatively, you can use the following command: 

```powershell
 Expand-Archive -Path "C:\path\to\yourFile.msapp" -DestinationPath "C:\path\to\destination"
```

## File structure for a .msapp file

For older **.msapp** files without the \src folder, follow these steps to generate source code files:

1. Import and resave and download the new **.msapp** in Power Apps Studio.
1. After that, you can proceed to [extract the source code files](#extract-source-code-files-from-a-msapp-file).

In the **\src** folder, find the following files and folders:

- **App.pa.yaml**: Represents the App.
- **[screen Name].pa.yaml**: One file for each screen, representing the screen.
- **\Component**: A folder containing one file for each [component](create-component.md#create-an-example-component), represented as [component Name].pa.yaml.

Only ***.pa.yaml** files within the **\src** folder can be used as source code. Any other file shouldn't be used as source code.

## Power Apps YAML schema versions

Currently, the only active schema version of Power Apps source code is Source Code (*.pa.yaml). The following table shows the other historical formats:

|Format name|File extension|Description|
|-----------|-----------|-------|
| [Experimental](power-apps-yaml.md#experimental-format-fxyaml) | *.fx.yaml| Retired. Version used by the experimental [Power Apps Git version control](git-version-control.md) and [pac canvas unpack](/power-platform/developer/cli/reference/canvas#pac-canvas-unpack)—no longer in development.|
| [Early preview](power-apps-yaml.md#early-preview) | -  | Retired. The version used by code view, copy code, and paste code. There's no version information in this schema, so it isn't suitable for version control. When [code view](code-view.md) is generally available (GA), it switches to the source code preview format.|
| [Source code](power-apps-yaml.md#source-code-payaml) | *.pa.yaml files | Active. Includes enhancements and version details for source control. |

## Experimental format (*.fx.yaml)

This schema is retired.

This schema describes an experimental format used by the Power Platform CLI to process and convert canvas apps into a source code format. This format isn't actively developed anymore.

You can't directly convert ***.fx.yaml** files to the new formats. To convert older apps, package the canvas app as a **.msapp** file and import it into Power Apps Studio.

## Preview

This schema is retired.

This version is used by [Code view](code-view.md) during the [preview](working-with-experimental-preview.md#preview) period. It is designed to create canvas apps in Power Apps Studio, letting you easily copy and paste controls. In this version, the source code is used in Power Apps Studio instead of being converted, like the experimental format.

The format during preview was temporary and is no longer in use. You can paste code from the preview format.

Here are the changes made from the experimental format:

1. **ZIndex property removal**: The ZIndex property is removed. Instead, a screen is represented as an array of controls. The order of controls determines their stacking order. Normal controls are ordered in ascending order, while responsive controls are ordered in descending order.
1. **JSON object representation replacement**: The "As" syntax is no longer used to define the control type. Instead, the left side of the control's name identifier remains unique. Only properties that differ from the default values are serialized. Two new properties define the control type and default values:

- **Control**: Represents the control type in YAML.
- **Variant**: Identifies a variant of a control type, which might alter default property values, add or remove properties, or modify the behavior or layout of the control.

These properties are used for instantiating controls and don't accept Power Fx expressions.

## Source code (*.pa.yaml)

> [!IMPORTANT]
>
> - The YAML source code for canvas apps is actively being developed. The content may be incomplete and subject to change.
> - The **.pa.yaml** files are read-only and should only be used to review changes made in Power Apps Studio. These files are not used when an app is loading.
> - External editing, merging, and conflict resolution is supported only in [Power Platform Git Integration](/power-platform/alm/git-integration/overview).

This schema is designed for source control purposes and allows the use of a single YAML file.

Updates from the previous format include:

1. Grouping of Top-Level Node Elements:
    - The top-level keywords "App" and "Screens" are examples of how elements are now grouped in a top-level node.
2. Control Version Specification:
    - You can now specify the version of a control using the Control Keyword followed by the **@** operator. If no version is specified, the most current version of the control is used. The version is used to deserialize the properties of the source code. Runtime version of the control is defined by the authoring version.
3. Simplified Variant Names:
    - Not all controls require a variant.
4. Consistent ZIndex for All Controls:
    - All controls now use an ascending order to determine the ZIndex value, starting from 1. This behavior aligns with the [CSS 2 spec](https://drafts.csswg.org/css2/#z-index).
