---
title: Microsoft Power Platform CLI canvas command| Microsoft Docs
description: "Includes descriptions and supported parameters for the canvas command."
keywords: Microsoft Power Platform CLI, code components, component framework, CLI
ms.subservice: dataverse-developer
ms.author: nabuthuk
author: Nkrb
manager: kvivek
ms.date: 09/15/2021
ms.service: "powerapps"
ms.topic: "article"
---

# Canvas

Commands for working with canvas app source files. Edit, manage, and collaborate on your app outside of Power Apps Studio with tools such as VS Code and GitHub.

> [!NOTE]
> The Canvas commands are in public preview. They may not be available in the version of Microsoft Power Platform CLI that you're using currently. 

## Parameters

|Property name|Description|Example|
|-------------|-----------|-------|
| pack | Creates an `.msapp` file from the previously unpacked source files. <br/>The result can be opened in Power Apps Studio by navigating to **File** > **Open** > **Browse**.<br/> After being unpacked, the source files can be edited and managed with external tools such as Visual Studio Code and GitHub. | `pac canvas pack --sources MyHelloWorldFiles --msapp HelloWorld.msapp` |
| unpack | Unpacks the `.msapp`  source file.<br/> Download the `.msapp` file from Power Apps Studio by navigating to **File** > **Save as** > **This computer**.<br/>  If the **sources** parameter is not specified, a directory with the same name and location as the `.msapp` file is used with `_src` suffix.  | `pac canvas unpack --msapp HelloWorld.msapp --sources MyHelloWorldFiles`<br/>`pac canvas unpack --msapp HelloWorld.msapp`<br/>*unpacks to default* `HelloWorld_src` *directory* |


### Folder structure

Unpack and pack properties use the following folder structure:

- **\src** - Control and component files. This contains the sources.
   - ***\*.fx.yaml*** - The formulas extracted from the `control.json` file.
    >[!NOTE]
    >This is the place to edit your formulas.
   - ***CanvasManifest.json*** - A manifest file that contains the information normally present in the header, properties, and publishInfo.
   - ***\*.json*** - The raw `control.json` file.
   - ***\EditorState\*.editorstate.json*** - Cached information for Power Apps Studio to use.
- **\DataSources** - All the data sources used by the app.
- **\Connections** - Connection instances saved with the app and used when reloading into Power Apps Studio. 
- **\Assets** - Media files embedded in the app.
- **\pkgs** - A downloaded copy of external references, such as templates, API definition files, and component libraries. These are similar to NuGet/NPM references. 
- **\other** - All miscellaneous files needed to re-create the `.msapp`.
   - ***entropy.json*** - Volatile elements (like timestamps) are extracted to this file. This helps reduce noisy differences in other files while ensuring that we can still round-trip.
   - Holds other files from the msapp, such as what's in \references.

### File format

The `.fx.yaml` files use a subset of [YAML](https://yaml.org/spec/1.2/spec.html). Similar to Excel, all expressions should begin with an equal sign `=`. More information: [Power Fx YAML Formula Grammar](/power-platform/power-fx/yaml-formula-grammar)

### Merging changes with Power Apps Studio

When merging changes that are made in two different Power Apps Studio sessions:

- Ensure that all the control names are unique. For example, inserting a button in two different sessions can result in two `Button1` controls. We recommend that you name the controls soon after you create them. The tool doesn't accept two controls with the same name.  
- For these files, merge them as you normally do:
   - \src\*.fx.yaml
- If there are conflicts or errors, you can delete these files:
   - \src\editorstate\*.json  - These files contain optional information in Power Apps Studio.
   - \other\entropy.json  
- For any conflicts in these files, it's ok to accept the latest version: 
   - \checksum.json
- If there are any merge conflicts under these paths, it isn't safe to merge. Let us know if this happens often; we'll work on restructuring the file format to avoid conflicts.
   - \Connections\*
   - \DataSources\*
   - \pkgs\*
   - CanvasManifest.json

### Open source

The canvas commands in Microsoft Power Platform CLI are open source. Discuss improvements, raise issues, and access the code from [Power Apps language tooling repository](https://github.com/microsoft/PowerApps-Language-Tooling).

### See also

[Power Apps component framework overview](../../../component-framework/overview.md)

[What is Microsoft Power Platform CLI](../../powerapps-cli.md)
