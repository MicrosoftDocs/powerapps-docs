---
title: "Ribbons available in model-driven apps | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "The article describes where ribbons are defined and modified" # 115-145 characters including spaces. This abstract displays in the search result.
ms.custom: ""
ms.date: 04/14/2021
ms.reviewer: ""
ms.service: powerapps
ms.topic: "article"
author: "KumarVivek" # GitHub ID
ms.subservice: mda-developer
ms.author: "kvivek" # MSFT alias of Microsoft employees only
manager: "shilpas" # MSFT alias of manager or PM counterpart
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---
# Ribbons available

This article describes where ribbons are defined and modified in model-driven apps.

<a name="ribbon_defs"></a>  

## Ribbon definitions 

Model-driven apps contain default `<RibbonDiffXml>` definitions for all ribbons in the application. You can export and view the current XML defining the ribbon for your organization, but you cannot update the XML directly. You customize the ribbon by defining how you want it to be changed. The change definitions that you specify are applied at runtime when the ribbon is displayed in the application. 
 All of your changes will be in the `<CustomAction>` or `<HideCustomAction>` elements. These elements are applied over the default ribbon definitions provided by model-driven apps.  

When you write your change definitions, you will frequently need to reference the definitions of the default ribbons. For example, if you want to hide a specific ribbon element, you will need to know the unique ID of that element. If you want to position a new ribbon element within or next to an existing ribbon element, you will need to know the ID values for those elements, as well as the sequence order that will control the relative position of the elements.  

Because of this requirement to reference the definitions of existing ribbon elements, it is important to understand the current ribbon definitions in your organization. There are two messages you can use to export XML files representing the current state of your ribbons. These definitions include any customizations that have already been applied to your system so that you can customize any custom ribbons that were previously applied. For more information, see [Export Ribbon Definitions](export-ribbon-definitions.md).  

To help you get started, you can download the default ribbon definitions for model-driven apps from [Export Ribbon Definitions sample](https://github.com/microsoft/PowerApps-Samples/tree/master/cds/orgsvc/C%23/ExportRibbonDefinitions). `The ExportedRibbonXml` file includes the output files you would have for an organization.  

Within the exported ribbon XML files, the applicationRibbon.xml file includes all the ribbons that are not defined for a specific table. These correspond to the **Application Ribbons** solution component. For each table, you will find an *table name*ribbon.xml file. This corresponds to the `RibbonDiffXml` that is included in each table. If you want to edit the ribbon for a specific table, you should locate the ribbon XML file for that table.  

[!INCLUDE[cc-terminology](../data-platform/includes/cc-terminology.md)]

<a name="table_ribbons"></a>  

## Table ribbons  

All tables use a common ribbon definition called the *Table Ribbon Template*. The table ribbon template definition is located in the `applicationribbon.xml` file. When you create a custom table, the ribbon you see is the default ribbon defined by the table ribbon template. 
 Each system table has a separate `<RibbonDiffXml>` definition that builds upon the table ribbon template definition.  

 Within the applicationribbon.xml file, you can see the following tabs that apply to all tables:  

- `Mscrm.Form.{!EntityLogicalName}.MainTab`  

   Tab displays the table display name in the label.  

- `Mscrm.Form.{!EntityLogicalName}.Related`  

   Tab has the label **Add**.  

- `Mscrm.Form.{!EntityLogicalName}.Developer`  

   Tab has the label **Customize**.  

- `Mscrm.HomepageGrid.{!EntityLogicalName}.MainTab`  

   Tab displays the plural table display name in the label.  

- `Mscrm.HomepageGrid.{!EntityLogicalName}.View`  

   Tab has the label **View**.  

- `Mscrm.HomepageGrid.{!EntityLogicalName}.Related`  

   Tab has the label **Add**.  

- `Mscrm.HomepageGrid.{!EntityLogicalName}.Developer`  

   Tab has the label **Customize**.  

- `Mscrm.SubGrid.{!EntityLogicalName}.ContextualTabs`  

   When a sub grid in a form or chart has focus, the contextual tab appears with the label **List Tools**.  

  -   `Mscrm.SubGrid.{!EntityLogicalName}.MainTab`  

       Tab displays the plural table display name.  

  When you view the ribbon definitions for a specific table, you will see that the name of the table usually replaces the `{!EntityLogicalName}` token. When you see the `{!EntityLogicalName}` token in the ribbon definition for a specific table, that means there is no specific definition for that table and it simply uses the definition from the table ribbon template. When you define ribbons for a specific table, always use the actual table name. Ribbon modifications for a specific table must be defined in the `//ImportExportXml/Entities/Entity/RibbonDiffXml` node.  

  You can make changes that apply to all tables by defining the changes to the application ribbons substituting the token `{!EntityLogicalName}` in place of a table logical name in your RibbonDiffXml node. Changes to application ribbons that are defined for all tables must be defined in the `ImportExportXml/RibbonDiffXml` node. They cannot be defined in the RibbonDiffXml node for a specific table.  

### Grid ribbons  

The table grid ribbon is a collection of tabs that have an ID value beginning with `Mscrm.HomepageGrid.<entity logical name>`. For example, the tab with the text "Accounts" on an account table grid is `Mscrm.HomepageGrid.account.MainTab`. All the tabs displayed on the account table grid will have an ID value that begins with `Mscrm.HomepageGrid.account`.  

<a name="BKMK_SubGridRibbons"></a>   

### Subgrid ribbons  

 The table subgrid ribbon is a contextual group with a collection of tabs that have an ID value beginning with `Mscrm.SubGrid.<entity logical name>`. For example, the tab with the text "Accounts" on account table sub grid is `Mscrm.SubGrid.account.MainTab`.  

 When a list of records for a table is displayed within a sub grid on the form of another table or in a chart, there will be only three controls available directly above or within the subgrid. The behaviors for these controls can be modified by changing the commands that they are associated with.  

- **Add**: The default behavior of the command with the ![Add button.](media/customization-subgrid-add.PNG "Add button") icon depends on whether the records in the subgrid are related to the current record.  

     If the records are related to the current record, the default behavior is look for existing records. If an existing record cannot be found, or if the user simply wants to create a new record, they can select **Add New**.  

     If the records are not related to the current record, the default behavior is to add a new record. If the table has a Quick Create form this will be displayed, otherwise a new full form will be shown.  

     Activities are the exception to this pattern. The add command will always prompt for the type of activity first.

     > [!NOTE]
     >  Offline mode in Dynamics 365 does not support many-to-many relationship on custom tables. Due to this, the **Add New** button on a sub grid in Dynamics 365 offline mode will not be displayed.

- **Show List**: The command with the ![Open view button.](media/customization-open-view.PNG "Open view button") icon will open the full list where all available commands can be used.  

     If the subgrid is associated with the current record, the default behavior of this command is to open the associated  view.  

     If the subgrid is not associated with the current record, the default behavior of this command is to open the view in the main list view.  

- **Delete**: The ![Sublist delete icon.](media/customization-subgrid-delete.PNG "Sublist delete icon") icon is shown on the right side of the row when people hover over the records in the list.  

     For records with a 1:N relationship or no relationship, the default behavior is to delete the record. The delete may be blocked if it is not allowed due to relationship configurations. Open activities and invoices are common examples of records that may not be deleted due to relationship configurations.  

     For relationships displaying N:N relationships the default behavior is to remove the relationship joining the records rather than the record itself.  

  You can change the default behavior by changing the actions associated with the command using `<CommandDefinition>`, but you cannot change the name of the command. For example, you could change the delete action so that it deactivates the record rather than deleting it.  

  It is not possible to change the icons displayed for these commands. 
  You can hide these commands by using `<HideCustomAction>`.  

### Form ribbons  

 Each table can have multiple forms. You can define changes to the form ribbon for all forms for that table by adding your definition at the table level (`//ImportExportXml/Entities/Entity/RibbonDiffXml`).  

 Each table form can have a specific ribbon definition. In the exported customizations.xml file, you must add your modified `<RibbonDiffXml>` to this location:`//ImportExportXml/Entities/Entity/FormXml/forms/systemform/form/RibbonDiffXml`.  

 The form ribbon is a collection of tabs that have an ID value beginning with `Mscrm.Form.<entity logical name>`. For example, the tab with the label **Account** on account form is `Mscrm.Form.account.MainTab`. All the tabs displayed on the account form will have an ID value that begins with `Mscrm.Form.account`.  

<a name="BKMK_BasicHomeTab"></a>   

## Basic home tab  
The basic home tab is displayed on the main application ribbon whenever an alternative tab is not defined because of table context or a display rule that suppresses it for specific pages. For example, this tab is displayed when you view the model-driven apps **Help**. The ID of the basic home tab is `Mscrm.BasicHomeTab`.  

## Customizing global commandbar

You can customize the global commandbar (`Mscrm.GlobalTab`) by adding the buttons to `Mscrm.GlobalTab`. The out of the box buttons in the global commandbar currently cannot be modified, but new buttons can be added.

When the location of the `CustomAction` is set to `Location="Mscrm.GlobalTab.New.Controls._children`, custom button is displayed in the global commandbar at the top of the page.

> [!NOTE]
> This feature is supported only on Unified Interface.

<a name="other_ribbons"></a>   
## Other ribbons  
 Several other special purpose ribbon tabs and a contextual group are defined by model-driven apps.
 Each tab is associated with a specific `<TabDisplayRule>` that controls when they will display. The following table lists these tabs.  


|                 Tab                  |             Root Id              |           Description                  |
|--------------------------------------|----------------------------------|-----------------------------------|
|     Web Resource Edit page tab.      |    `Mscrm.WebResourceEditTab`    |   Displays when editing Web resources within a solution.      |
|           Form Editor tab            |      `Mscrm.FormEditorTab`       |   Provides Save, Edit, Select, and View groups of actions for forms.                               |
|        Form Editor Insert tab        |   `Mscrm.FormEditorInsertTab`    |   Provides buttons to insert Sections, Tabs, and Controls in forms.                                |
|        Dashboard Homepage tab        |       `Mscrm.DashboardTab`       |   Displays in the Workplace area.                                                    |
| Visualization Tools Contextual Group |    `Mscrm.VisualizationTools`    |   Displays when the **New Chart** button is clicked on the **Charts** tab displayed in the table grid ribbon.              |
|       AptbookTab Homepage tab        |        `Mscrm.AptbookTab`        |   Displays when viewing the Service Calendar in the Service area.                                    |
|          Advanced Find tab           |       `Mscrm.AdvancedFind`       |   Displays in the **Advanced Find** window.                                               |
|         Dashboard Editor tab         |    `Mscrm.DashboardEditorTab`    |   Displays when editing a dashboard.                                                   |
|            Documents tab             |       `Mscrm.DocumentsTab`       |   Displays if SharePoint integration has been enabled for the organization. |
|           Chart Editor tab           | `Mscrm.VisualizationDesignerTab` |   Displays when editing a chart from the solutions window.                                        |
|    Search Tools Contextual Group     |      `Mscrm.ArticleSearch`       |    Displays when viewing the `KBarticle` table.                                             |

<a name="BKMK_RibbonsForCustomPages"></a>

## Ribbons for custom pages

You can display custom pages in the application navigation using the SiteMap. These pages will always display the [Basic home tab](ribbons-available.md#BKMK_BasicHomeTab) (`Mscrm.BasicHomeTab`). 

It is not possible to use a `<PageRule>` to enable or display custom ribbon components on custom pages.  

### See also  

 [Customize the ribbon](customize-commands-ribbon.md)   
 [Command bar or ribbon presentation](command-bar-ribbon-presentation.md)


[!INCLUDE[footer-include](../../includes/footer-banner.md)]