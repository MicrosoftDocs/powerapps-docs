---
title: V source code files for canvas apps (pa.yaml)
description: Learn about how to view source code files for canvas apps.
author: marcelbf
ms.author: marcelbf
ms.date: 11/1/2024
ms.topic: conceptual
ms.reviewer: 
ms.subservice: canvas-maker
ms.collection: get-started
search.audienceType: 
  - maker  
  - developer
ms.custom:
  - canvas  
---

# View source code files for canvas apps (preview)

[!INCLUDE [preview-banner](~/../shared-content/shared/preview-includes/preview-banner.md)]

You can use the source code for a canvas app to review changes made my makers in Power Apps Studio. The generated canvas app YAML code is read-only and shouldn't be modified. Any change in the file will be ignored and can be lost.

Currently, we don't recommended that you modify **pa.yaml** files or create canvas apps using other text editors. However, more scenarios will be supported in the future.

> [!NOTE]
> - The YAML schema is in active development, the content may be incomplete.
> - The current proposed static schema for ***.pa.yaml** files can be found, [here](https://raw.githubusercontent.com/microsoft/PowerApps-Tooling/refs/heads/master/schemas/pa-yaml/v3.0/pa.schema.yaml).


We use Power Fx and YAML as the languages for Power Apps source code. YAML is appreciated for its human-readable format and benefits from a wide array of existing editors, tools, and libraries for its manipulation.

## Prerequisite

To use this feature, you must create an [Early release cycle environment](/power-platform/admin/early-release). 

## Access source code files

You have access to the source code files if you're using the [Dataverse Git Integration](/power-platform/alm/git-integration/overview), eliminating the need for **.msapp** files.

The Power Apps Studio creates the source code for canvas apps, which is stored as *.pa.yaml files within the **.msapp** file. The **.msapp** file is a binary file that contains a collection of files, including the source code.

> [!TIP]
> To effectively use ALM, it's recommended to use solutions. [Canvas apps package](export-import-app-package.md) doesn't support ALM and should only be used for basic import and export capabilities when Dataverse isn't available.

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


## Power Fx YAML

Microsoft Power Fx utilizes a grammar for expressions that is based on Excel and well-established. However, when using Power Apps and other hosts that rely on UI for formula binding, there's no standardized method for editing formula bindings as text.

We choose [YAML](https://yaml.org/spec/1.2/spec.html)  as the industry standard language for formula binding. YAML has a wide array of editors, tools, and libraries available for working with it.

> [!NOTE]
> Currently, we only support a limited subset of YAML. Only the constructs outlined in this article are supported. More information: [Power Fx YAML formula grammar](/power-platform/power-fx/yaml-formula-grammar).

## Power Apps YAML schema versions

Currently there are three schema versions of Power Apps Source Code:

|Format Name|File Extension|Description|
|-----------|-----------|-------|
| [Experimental](power-apps-yaml.md#experimental-format-fxyaml) | *.fx.yaml| Version used by the experimental [Power Apps Git version control](git-version-control.md)  and [pac canvas unpack](/power-platform/developer/cli/reference/canvas#pac-canvas-unpack) - no longer in development.|
| [Early Preview](power-apps-yaml.md#early-preview) | -  | The version used by code view, copy code, and paste code. There's no version information in this schema, therefore it isn't suitable for version control. When [code view](code-view.md) is generally available (GA), it switches to the source code preview format.|
| [Source Code](power-apps-yaml.md#source-code-payaml) | *.pa.yaml files | Includes enhancements and version details for source control and it is in active development. |

>[!NOTE]
> You can't copy YAML code from a pa.yaml file and paste it as code in Power Apps Studio. However, in the future, code view will utilize the source code format for this purpose.

## Experimental format (*.fx.yaml)

This schema represents an experimental format employed by the Power Platform CLI to process and convert canvas apps into a source code format. However, this format is no longer being actively developed.

You can't directly convert ***.fx.yaml** files to the new formats. To convert older apps, you need to package the canvas app as a **.msapp** file and import it into Power Apps Studio.

## Early Preview

This version is used by [Code view](code-view.md). Is designed to create apps within Power Apps Studio, letting you easily copy and paste controls. In this version, the source code is used in Power Apps Studio instead of being converted (like the experimental format).

The Early Preview format is a preview feature and is temporary. In the future, both code view, copy code, and paste code are going to use the same source code version.

Here are the changes made from the experimental format:

1. **ZIndex Property Removal**: The ZIndex property is removed. Instead, a screen is now represented as an array of controls. The order of controls now determines their stacking order. Normal controls are ordered in ascending order, while responsive controls are ordered in descending order.
1. **JSON Object Representation Replacement**: We no longer use the "As" syntax to define the control type. Instead, the left side of the control's name identifier remains unique. Only properties that differ from the default values are serialized. Two new properties are added to define the control type and default values:

- **Control**: Represents the control type in YAML.
- **Variant**: Identifies a variant of a control type, which might alter default property values, add or remove properties, or modify the behavior/layout of the control.

These properties are used for instantiating controls and don't accept Power Fx expressions.

## Source code (*.pa.yaml)

> [!IMPORTANT]
>
> - The YAML source code for canvas apps is currently in preview and actively being developed. The content may be incomplete and subject to change.
> - The **.pa.yaml** files are read-only and should only be used to review changes made in Power Apps Studio. These files are not used when an app is loading.
> - External editing, merging, and conflict resolution isn't supported.

This schema is designed for source control purposes and allows the use of a single YAML file. It's an updated format compared to the previous code view.

Updates from the previous format include:

1. Grouping of Top-Level Node Elements:
    - The top-level keywords "App" and "Screens" are examples of how elements are now grouped in a top-level node.
2. Control Version Specification:
    - You can now specify the version of a control using the Control Keyword followed by the **@** operator. If no version is specified, the most current version of the control is used.
3. Simplified Variant Names:
    - Not all controls require a variant. For controls that do require a variant, the name is simplified and more user-friendly.
4. Consistent ZIndex for All Controls:
    - All controls now use an ascending order to determine the ZIndex value, starting from 1. This behavior aligns with the [CSS 2 spec](https://drafts.csswg.org/css2/#z-index).



## Schema updates

|Change|Authoring version|Description|
|---|---|---|
|Initial Version|---|Initial version, support simple controls|


