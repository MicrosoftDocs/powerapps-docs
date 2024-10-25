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

In this article, you'll learn about the source code files of a canvas app.

We use Power FX + YAML as our language for Power Apps Source Code. YAML is friendly for humans to read, and there are already a large number of editors, tools, and libraries for manipulating YAML.

>[!NOTE]
> We support only a restricted subset of YAML. Only the constructs described in this document are supported.

## Pre-requisits

To use this feature you must create an [Early release cycle environment.](https://learn.microsoft.com/en-us/power-platform/admin/early-release). 

## How to access the Source Code files

Source code for Canvas Apps is represented as *.pa.yaml files and are managed by Power Apps Studio.

A msapp file is collection of files compacted in a binary file, including the source code. 

> [!TIP]
> To effectively ALM, it's recommended to use solutions. Canvas apps packages don’t support ALM and should only be used for basic import and export capabilities when Dataverse isn’t accessible.

The source code files are designed to be used with the Dataverse Git Integration, where you no longer need to use .msapp files.

You can also extract the source code files either from the .msapp file or by using Power Platform CLI.

The *.pa.yaml files are within the \src folder of the extracted msapp. 

>[!Important]
> In the extracted msapp, only files within the directory \src are designed to be used with source control.

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

Older msapps will not have the \src folder.

To generate source code files for an older msapp you must import the .msapp in Power Apps Studio before [extract the source code files.](#extract-source-code-files-from-a-msapp-file)

In the src folder, you have:
- App.pa.yaml to represent the App
- One file per screen [screen Name].pa.yaml to represent the screen
- One file pre component [component Name].pa.yaml to represent the component.

>[!IMPORTANT]
> Only *.pa.yaml files within "\src" folder can be used as source code.

## Power Fx YAML

Microsoft Power Fx has a well-established grammar for expressions based on Excel. However, when used in Power Apps and other hosts where UI provides the name-to-expression binding for a formula, there is no standard way of editing the formula binding as text.

We've selected the industry standard [YAML](https://yaml.org/spec/1.2/spec.html) as our language for this binding. There are already a large number of editors, tools, and libraries for working with YAML. This article describes how we represent formulas in YAML.

At this time, we support only a restricted subset of YAML. Only the constructs described in this article are supported.

For more details, visit [Power Fx YAML formula grammar](https://learn.microsoft.com/en-us/power-platform/power-fx/yaml-formula-grammar).

## Power Apps YAML schema versions

There are 3 schema versions of Power Apps Source Code:

|Format Name|File Extension|Description|
|-----------|-----------|-------|
| [Experimental](#experimental-format-fxyaml) | *.fx.yaml| Version used by the experimental [Power Apps Git version control](./canvas-apps/git-version-control.md)  and [pac canvas unpack](https://learn.microsoft.com/en-us/power-platform/developer/cli/reference/canvas#pac-canvas-unpack) - no longer in development.|
| [Code View Preview](#code-view-preview) | -  | Version used by Code View, Copy Code and Paste Code - to be used in Power Apps Studio when building new apps only, not suitable for version control. |
| [Source Code Preview](#source-code-preview-payaml) | *.pa.yaml files | Includes improvements and version information for Source Control. This is the current and effective version of Canvas YAML. |

>[!NOTE]
> You cannot copy YAML code from a pa.yaml file and paste as code in Power Apps Studio yet. In the future, Code View will use the same format.

## Experimental format (*.fx.yaml)

This is an experimental format, used by Power Platform CLI to process and convert canvas application in a source code format.

You cannot directly convert *.fx.yaml files to the new formats. To convert older apps, you must pack the canvas app in a *.msapp and import the file in Power Apps Studio.

## Code View Preview 

This format was designed to be used while creating apps within Power Apps Studio, to copy and paste controls. In this format, the source code is native instead of converted. 
Other changes from the experimental format:

- Removed Z Index Property
A screen is now represented as an array of controls. Because order is now significant, we can imply the ZIndex property from the position of the control. We use asc order for normal controls and desc order for responsive controls.
 
- Replaced JSON Object representation

We no longer use the sintax "As" to define the control type. The name identifier of the control stays on the left and it is unique. Only properties different than the default are serialized. Two new Properties define the control type and the default values:
  - Control: The template used for the controls. 
  - Variant: Can change the default fields, add fields, remove fields or modify the behaviour of the control. 

These properties are used to instantiate the controls and don't accept Power Fx expressions.

## Source Code Preview (*.pa.yaml)

This schema was designed for source control and to allow use of a single YAML file. 

>[!Important]
>
> YAML source code for Canvas Apps is in preview. The schema is being actively developed.
> Content may be incomplete and subject to change.
> pa.yaml files are read-only and should only be used to review changes made within Power Apps Studio. pa.yaml files are not used when loading the app. 
> External editing, merging and conflict resolution are not supported.

Updates:

- High level node
Elements are grouped in a high level node.

- Includes the version of the control
You can specify the version of the control in the Control property, by using the operator @. If a version is not specified, the most current version of the control will be used.

- Simplified variant names
Not all controls require variant. If the control requires a variant, the name is simplified and more user friendly.

- Consistent ZIndex for all controls
All controls use ascending order to imply the ZIndex value, starting with 1.

## Supported Scenario

The source code for a canvas app can be used to review changes done my makers within Power Apps Studio. You should not change pa.yaml files or create canvas apps with other text editors yet. More scenarios will be possible in the future.

JSON files within the MSAPP are not designed to be stable across save and load cycles and should not be used as source code.

The YAML schema is in active development, the content may be incomplete.

## Schema updates

|Change|Authoring version|Description|
|---|---|---|
|Initial Version|---|Initial version, support simple controls|


