---
title: Source Code files for Canvas apps (pa.yaml)
description: Learn about Source Code files for canvas apps.
author: marcelbf
ms.author: marcelbf
ms.date: 10/17/2024
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

# Source Code files for Canvas apps (preview)

[!INCLUDE [preview-banner](~/../shared-content/shared/preview-includes/preview-banner.md)]

The source code for a canvas app can be used to review changes done my makers within Power Apps Studio. You should not change pa.yaml files or create canvas apps with other text editors yet. More scenarios will be possible in the future.

JSON files within the MSAPP are not designed to be stable across save and load cycles and should not be used as source code.

>[!Note]
> - The generated canvas app YAML code is read-only and should not be modified.
> - The YAML schema is in active development, the content may be incomplete.
> - The current proposed static schema for *.pa.yaml files can be found [here](https://raw.githubusercontent.com/microsoft/PowerApps-Tooling/refs/heads/master/schemas/pa-yaml/v3.0/pa.schema.yaml).


We utilize Power Fx and YAML as the language for Power Apps Source Code. YAML is known for its human-readable format and benefits from a wide array of existing editors, tools, and libraries for its manipulation.

>[!NOTE]
> We support only a restricted subset of YAML. Only the constructs described in this document are supported.



## Prerequisite

To use this feature, you must create an [Early release cycle environment.](https://learn.microsoft.com/en-us/power-platform/admin/early-release). 

## How to access the Source Code files

Power Apps Studio generates the source code for Canvas Apps, represented as *.pa.yaml files within the msapp.

A msapp file is a collection of files compacted in a binary file, including the source code. 

> [!TIP]
> To effectively use ALM, it's recommended to use solutions. [Canvas apps package](https://learn.microsoft.com/power-apps/maker/canvas-apps/export-import-app-package) don’t support ALM and should only be used for basic import and export capabilities when Dataverse isn’t accessible.

The source code files are designed to use with the Dataverse Git Integration, where you no longer need to use .msapp files.

You can also extract the source code files either from the .msapp file or by using Power Platform CLI.

The *.pa.yaml files are within the \Src folder of the extracted msapp. 

>[!Important]
> In the extracted msapp, only files within the directory \Src are designed to be used with source control.

### Use Power Platform CLI to download and extract the pa.yaml files

Use Power Platform CLI to connect to your enviroment.

Once connected to a environment, use the command [pac canvas list](https://learn.microsoft.com/en-us/power-platform/developer/cli/reference/canvas#pac-canvas-list) to list the canvas apps of your current environment and [pac canvas download](https://learn.microsoft.com/en-us/power-platform/developer/cli/reference/canvas#pac-canvas-download) with the [parameter -d](https://learn.microsoft.com/en-us/power-platform/developer/cli/reference/canvas#--extract-to-directory--d), to extract the source code files.

### Extract source code files from a .msapp file

You can [export your canvas app as a .msapp file](../canvas-apps/export-import-single-app.md#export-msapp-files-in-power-apps). 

You can either, manually unzip the .msapp file or use the following command:
```powershell
 Expand-Archive -Path "C:\path\to\yourFile.msapp" -DestinationPath "C:\path\to\destination"
```

## msapp file structure

Older msapps don't have the \src folder.

To generate source code files for an older msapp, you must import and resave/download the new .msapp in Power Apps Studio before [extract the source code files.](#extract-source-code-files-from-a-msapp-file)

In the src folder, you have:
- App.pa.yaml to represent the App
- One file per screen [screen Name].pa.yaml to represent the screen
- One folder \Component, with one file per [component](https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/create-component#create-an-example-component) [component Name].pa.yaml.

>[!IMPORTANT]
> Only *.pa.yaml files within "\src" folder can be used as source code.

## Power Fx YAML

Microsoft Power Fx has a well-established grammar for expressions based on Excel. However, when used in Power Apps and other hosts where UI provides the name-to-expression binding for a formula, there's no standard way of editing the formula binding as text.

We did select the industry standard [YAML](https://yaml.org/spec/1.2/spec.html) as our language for this binding. There are already a large number of editors, tools, and libraries for working with YAML.

At this time, we support only a restricted subset of YAML. Only the constructs described in this article are supported.

For more details, visit [Power Fx YAML formula grammar](https://learn.microsoft.com/en-us/power-platform/power-fx/yaml-formula-grammar).

## Power Apps YAML schema versions

Currently there are three schema versions of Power Apps Source Code:

|Format Name|File Extension|Description|
|-----------|-----------|-------|
| [Experimental](#experimental-format-fxyaml) | *.fx.yaml| Version used by the experimental [Power Apps Git version control](./canvas-apps/git-version-control.md)  and [pac canvas unpack](https://learn.microsoft.com/en-us/power-platform/developer/cli/reference/canvas#pac-canvas-unpack) - no longer in development.|
| [Code View Early Preview](#code-view-preview) | -  | Early Preview version used by Code View, Copy Code, and Paste Code - to be used in Power Apps Studio when building new apps only, not suitable for version control. This schema is an early preview version. Code view will switch to the Source Code Preview format when it's ready.|
| [Source Code Preview](#source-code-preview-payaml) | *.pa.yaml files | Includes improvements and version information for Source Control. This schema is the current and effective version of Canvas YAML. |

>[!NOTE]
> You cannot copy YAML code from a pa.yaml file and paste as code in Power Apps Studio yet. In the future, Code View will use the Source Code format.

## Experimental format (*.fx.yaml)

This schema is an experimental format, used by Power Platform CLI to process and convert canvas application in a source code format. It's no longer in development.

You can't directly convert *.fx.yaml files to the new formats. To convert older apps, you must pack the canvas app in a *.Msapp and import the file in Power Apps Studio.

## Code View Early Preview 

This format was designed to use while creating apps within Power Apps Studio, to copy and paste controls. In this format, the source code is native instead of converted. 

>[!Important]
> This format is an early preview and it is temporary. Code view, copy code and paste code will all use the Source Code Preview schema.

Changes from the experimental format:

- Removed ZIndex Property
A screen is now represented as an array of controls. Because order is now significant, we can imply the ZIndex property from the position of the control. We use asc order for normal controls and desc order for responsive controls.
 
- Replaced JSON Object representation

We no longer use the syntax "As" to define the control type. The name identifier of the control stays on the left and it's unique. Only properties different than the default are serialized. Two new Properties define the control type and the default values:
  - Control: The Control Type in YAML. 
  - Variant: Identifies a variant of a control type. May change the default property values, add or remove properties, or modify the behaviour/layout of the control. 

These properties are used to instantiate the controls and don't accept Power Fx expressions.

## Source Code Preview (*.pa.yaml)

>[!Important]
>
> YAML source code for Canvas Apps is in preview. The schema is being actively developed.
> Content may be incomplete and subject to change.
> pa.yaml files are read-only and should only be used to review changes made within Power Apps Studio. pa.yaml files are not used when loading the app. 
> External editing, merging and conflict resolution are not supported.

This schema was designed for source control and to allow use of a single YAML file. It's an update from the Code View format.

Updates from previous format:

- Top-level node
Elements are grouped in a top-level level node. "App" and "Screens" keywords are examples of the top-level keywords.

- Includes the version of the control
You can specify the version of the control in the Control Key-word, by using the operator @. If a version isn't specified, the most current version of the control will be used.

- Simplified variant names
Not all controls require variant. If the control requires a variant, the name is simplified and more user friendly.

- Consistent ZIndex for all controls
All controls use ascending order to imply the ZIndex value, starting with 1. This behavior is similar to the [CSS 2 spec](https://drafts.csswg.org/css2/#z-index).

>[!Note]
> The YAML schema is in active development, the content may be incomplete.
> The current proposed static schema for *.pa.yaml files can be found [here](https://raw.githubusercontent.com/microsoft/PowerApps-Tooling/refs/heads/master/schemas/pa-yaml/v3.0/pa.schema.yaml).

## Schema updates

|Change|Authoring version|Description|
|---|---|---|
|Initial Version|---|Initial version, support simple controls|


