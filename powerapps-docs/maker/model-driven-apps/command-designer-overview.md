---
title: "Command designer overview | MicrosoftDocs"
description: "Overview of modern commanding, command designer, and Power Fx"
Keywords: command bar, command designer
author: caburk
ms.author: caburk
ms.reviewer: matp
manager: kvivek
ms.date: 07/26/2021
ms.service: powerapps
ms.subservice: mda-maker
ms.topic: conceptual
search.audienceType: 
  - maker
search.app: 
  - PowerApps
  - D365CE
---
# Modern commanding overview

[!INCLUDE [cc-beta-prerelease-disclaimer](../../includes/cc-beta-prerelease-disclaimer.md)]

> [!IMPORTANT]
> - This is a preview feature, and may not be available in all regions.
> - [!INCLUDE[cc_preview_features_definition](../../includes/cc-preview-features-definition.md)]
  
 Command bars are at the core of every model-driven app and appear in many different locations. Commands are arranged in relation to other commands and are associated with a command bar location. The group of commands associated with a specific location make up a command bar. 
 
> [!div class="mx-imgBorder"]
> ![Command bar](media/CommandDesigner-location.png "Command bar")
 
 ## Classic commanding deficiencies

Classic commands (formerly known as the ribbon) were not customizable using low code. With code, command customizations were difficult, tedious, and error prone. In order to scale commanding to low-code as well as [converge canvas and model-driven apps](/power-platform-release-plan/2021wave1/power-apps/converging-canvas-into-model-driven-apps-custom-page), it was vital to reinvent and rebuild the command infrastructure.

**Classic commands** had several key **gaps** including:
  - No low code designer. This results in many forced XML hacks that often caused breaking changes.
  - Different apps couldn’t use a different set of commands for common tables.
  - Lack of granular level scopes could impact performance due to processing unused logic on the client.
  - The legacy solution implementation was designed for the now deprecated web client. It has been highly problematic and has an overly complex structure that’s no longer needed in the Unified Interface.
  - “Ribbon” concepts that are no longer relevant: Tabs, Groups, Scaling, MaxSize, TabCommands, CustomActions, and HideCustomActions.
  - Classic “Ribbons” and commands lacked proper application lifecycle management (ALM) support and management within solutions.
  - Legacy code wasn’t capable of handling app separation, solution segmentation, solution patches, or promote and delete concept (solution upgrade).
  - Missing all core solution behaviors like add/remove, managed properties, dependencies, and so on.
  - Had a different, unconventional mechanism for localization.
  - Too flexible. Every custom action, button, group, command action, or rule, at every level can be overridden, making it hard for users to understand what has been modified.
    
## Modern commanding key improvements

Modern commanding largely addresses the above gaps and provides a modern infrastructure that will continue to scale.
  
- New infrastructure, combines benefits of canvas and model-driven apps.
- Low-code designer.
- Power Fx support for visibility and actions.
- JavaScript remains supported.
- Better ALM support.
- Better app level control – commands are applied to individual apps.
- Simple, flat data model.
- Many workarounds used today are no longer needed.
- Classic commands remain supported. Apps can run both classic and modern commands side-by-side.
- No forced customer migration.
- Arrange modern commands amongst existing classic commands.

## Command bar locations

-	**Main grid**. This command bar is displayed when using the left-hand navigation of an app to view a full page list of records in this table.
    > [!div class="mx-imgBorder"]
    > ![Command bar on main grid](media/commanddesigner-home-grid-location.png "Command bar on main grid")
    
- **Main form**. This command bar is displayed on the table’s main forms. This appears at the top of the form and is not the same as the associated view or subgrid view that will appear in different areas of the form.
    > [!div class="mx-imgBorder"]
    > ![Main form](media/CommandDesigner-main-form-location.png "Main form")
    
- **Subgrid view**. This command bar is displayed on forms of other tables that render this table’s data within a subgrid.
   -	For example, the account main form has a subgrid control that lists contact records related to the account record. To edit the below command bar, edit the command bar for the contact table then subgrid view.
    > [!div class="mx-imgBorder"]
    > ![Subgrid view](media/CommandDesigner-subrid-location.png "Subgrid view")

-	**Associated view**. This command bar is displayed on the form of a parent table when viewing related data in this table.
   -	For example, from the main form of an account record select the **Related** tab then select a related table like contacts.
    > [!div class="mx-imgBorder"]
    > ![Associated view](media/CommandDesigner-associated-view-location.png "Associated view")
    
-	**Quick actions**. There is not a specialized entry point from the command designer because quick actions are edited via the main grid of the table.
    > [!div class="mx-imgBorder"]
    > ![Quick actions](media/CommandDesigner-quick-actions-location.png.jpg "Quick actions")

### See also
[Customize the command bar using command designer](use-command-designer.md) <br />
[Manage commands in solutions](manage-commands-in-solutions.md) <br />
[Modern commanding known limitations](command-designer-limitations.md)