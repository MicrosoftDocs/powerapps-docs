---
title: "Browse Table Definitions in Your Environment"
description: "Use the Metadata Browser to view Dataverse tables and properties in your environment. Download and install the solution to get started." 
ms.date: 04/26/2026
ms.reviewer: jdaly
ms.topic: how-to
author: JimDaly
ms.subservice: dataverse-developer
ms.author: jdaly
search.audienceType: 
  - developer
---
# Browse table definitions in your environment

Use the metadata browser to view table definitions and properties for all tables in your Dataverse environment. 

> [!div class="nextstepaction"]
> [ Download the MetadataBrowser_4_0_0_0_managed.zip managed solution to get started](https://go.microsoft.com/fwlink/?linkid=2362044&clcid=0x9)

## Import the solution

After you download the solution, import it to use it.

1. Sign in to [Power Apps](https://make.powerapps.com).
1. In the left navigation pane, select **Solutions**, and then select **Import solution** on the command bar.
1. On **Import a solution**, select **Browse** to locate the solution file (.zip) you downloaded, and select it.
1. Select **Next**. Information about the solution is displayed.
1. Select **Import**, and then finish the import process.

## Open the app

After you import the solution successfully, locate the app by selecting **Apps** in the left navigation pane. The app is listed as **Metadata Browser**.

:::image type="content" source="media/browse-your-metadata/metadata-browser-app.png" alt-text="Screenshot of Power Apps showing the Apps list with Metadata Browser selected and highlighted in the main panel.":::

Select the app to open it. The Metadata Browser loads all the table definitions from your environment and displays them in a split view.

> [!TIP]
> When the app opens inside a model-driven app, an **Open Web Resource directly** button appears in the header. Select this button to open the Metadata Browser in its own browser tab. Bookmark that URL so you can return to it quickly in the future without navigating through the model-driven app.

## Table list

The table list is the main view. It uses a split layout with two panes separated by a draggable divider.

:::image type="content" source="media/browse-your-metadata/table-list.png" alt-text="Screenshot of Metadata Browser in Power Apps with tables grid and properties of the selected table.":::

### Table list pane

The left pane shows a sortable list of all the tables in your environment. It displays the **Schema Name**, **Display Name**, and **Description** for each table. Select a column header to sort by that column.

Select a row to view that table's properties in the right pane. Double-click a row, or press **Enter**, to open the [details pane](#details-pane).

### Table properties pane

When you select a table in the table list, the table properties pane shows all the properties for that table as name-value pairs. These properties come from the [EntityMetadata class](xref:Microsoft.Xrm.Sdk.Metadata.EntityMetadata). You can sort by property name by selecting the **Property** column header.

Some properties represent collections, such as **Attributes**, **Keys**, **OneToManyRelationships**, **ManyToOneRelationships**, **ManyToManyRelationships**, and **Privileges**. These properties appear as buttons. Select a button to open the [details pane](#details-pane) to the corresponding tab. Buttons are disabled when the collection is empty.

### Toolbar

The toolbar above the table list provides the following controls:

- **Edit Table**: Opens the selected table on [Power Apps](https://make.powerapps.com) where you can edit it. Not all tables are editable.
- **Search**: Type in the search box to filter tables in real time. Search matches against the table's `SchemaName`, `LogicalName`, `DisplayName`, `ObjectTypeCode`, and `MetadataId` properties.
- **Filter Tables**: Opens the [filter dialog](#filter-dialog) where you can set filter criteria for table properties. The button is highlighted when a filter is active.
- **Filter Properties**: Opens the [property selector](#property-selector) dialog where you can choose which properties to show or hide in the right pane. The button is highlighted when any properties are hidden.

## Details pane

The details pane is an overlay that slides in from the right side of the screen. You can open it by double-clicking a table in the table list, or by selecting a collection button in the table properties list.

:::image type="content" source="media/browse-your-metadata/details-pane.png" alt-text="Screenshot of the details pane for the Account table, displaying Properties tab with a list of property names and values.":::

The details pane header shows the table's display name and a close button (**✕**). Below the header is a tab bar. Tabs only appear when the table has data for that category. Select a tab to view its content. You can also close the details pane by selecting the backdrop area to the left of the panel.

### Properties tab

Displays all properties for the selected table, similar to the right pane of the table list but in a larger view. Use the **Filter Properties** button to choose which properties to show or hide.

Collection properties appear as buttons that switch to the corresponding tab within the same details pane.

### Columns tab

Shows the table's columns (attributes) in a split layout.

- **Column list**: Lists each column with its **Schema Name**, **Display Name**, **Type**, and **Description**. Select a column to see its properties in the column properties.
- **Column properties**: Displays all properties for the selected column. These are the properties of the [AttributeMetadata class](xref:Microsoft.Xrm.Sdk.Metadata.AttributeMetadata) or derived classes.

:::image type="content" source="media/browse-your-metadata/columns-tab.png" alt-text="Screenshot of Columns tab with Account table selected, displaying column list and detailed properties pane.":::

The toolbar provides:

- **Edit Table columns**: Opens the table's columns page on [Power Apps](https://make.powerapps.com).
- **Search**: Filter columns by `SchemaName`, `LogicalName`, `DisplayName`, or `MetadataId`.
- **Filter Columns**: Opens the [filter dialog](#filter-dialog) with column-specific filter fields such as `AttributeType`, `RequiredLevel`, `DateTimeBehavior`, and others.
- **Filter Column properties**: Opens the [property selector](#property-selector) for the column properties.

### Keys tab

**Only when a table has alternate keys**, this tab shows the table's alternate keys in a split layout.

- **Keys list**: Lists each key with its **Display Name**, **Name**, and **Columns** (the key's attributes shown as a comma-separated list). These properties correspond to the [EntityKeyMetadata class](xref:Microsoft.Xrm.Sdk.Metadata.EntityKeyMetadata).
- **Key properties**: Displays all properties for the selected key.

### One-to-many, many-to-one, and many-to-many relationship tabs

Each relationship type has its own tab with a split layout.

- **Relationship list**: Lists relationships with columns relevant to the relationship type, such as schema name, referencing or referenced table, and referencing or referenced column.
- **Relationship properties**: Displays all properties for the selected relationship. These properties come from the [OneToManyRelationshipMetadata class](xref:Microsoft.Xrm.Sdk.Metadata.OneToManyRelationshipMetadata) or [ManyToManyRelationshipMetadata](xref:Microsoft.Xrm.Sdk.Metadata.ManyToManyRelationshipMetadata) classes.

Each tab provides:

- **Edit Relationship**: Opens the table's relationships page on [Power Apps](https://make.powerapps.com).
- **Search**: Filter relationships by schema name, table names, and column names.
- **Filter**: Opens the [filter dialog](#filter-dialog) with relationship-specific filter fields, including cascade configuration and associated menu configuration options.

Properties that contain table logical names, such as `ReferencingEntity`, `ReferencedEntity`, `Entity1LogicalName`, and `Entity2LogicalName`, appear as clickable links. Select a link to close the details pane, go to that table in the table list, and select it.

### Privileges tab

Shows the table's security privileges in a single grid (no split layout). Columns include **Name**, **PrivilegeId**, **PrivilegeType**, and several **CanBe...** properties. These properties come from the [SecurityPrivilegeMetadata class](xref:Microsoft.Xrm.Sdk.Metadata.SecurityPrivilegeMetadata). Use the search box to filter by `PrivilegeId`.  

## Search and filter metadata

The Metadata Browser provides several ways to find and focus on the metadata you need.

### Text search

Most views include a search box in the toolbar. Type text to instantly filter the displayed items. Search is case-insensitive and matches across multiple properties relevant to the current view.

### Filter dialog

Select a **Filter** button, such as **Filter Tables** or **Filter Columns**, to open the filter dialog. This dialog lets you set criteria for specific metadata properties. All criteria use AND logic, so you see only items that match every active criterion.

:::image type="content" source="media/browse-your-metadata/filter-table-properties.png" alt-text="Screenshot of the Filter Tables dialog with search box, filter options for IsChildEntity, IsCustomEntity, and IsCustomizable, and Close button.":::

The filter dialog supports several types of filter controls:

| Control type | Description |
|---|---|
| Boolean checkboxes | Filter by true or false values |
| Dropdown selectors | Filter by specific enumeration or option values |
| Exists / Doesn't exist | Filter by whether a property has a value |
| Date filters | Filter by date before or after a specific date |

Use the search box at the top of the dialog to find specific filter fields. Changes take effect immediately. The **Show All** checkbox resets all filters.

### Property selector

Select a **Filter Properties** button to open the property selector dialog. This dialog lets you choose which properties to show or hide in a property grid.

:::image type="content" source="media/browse-your-metadata/filter-properties.png" alt-text="Screenshot of the Filter Properties dialog showing a searchable list of property checkboxes with names and descriptions.":::

Each property is listed with a checkbox, name, and description. Use the search box to find properties by name or description. Select the **Show All** checkbox to reset all properties to visible. Select the checkbox in the column header to toggle all visible (non-filtered) rows at once.

The property visibility settings are shared between the table list and the details pane, so changes in one location immediately appear in the other.

## Understand complex property values

Many metadata properties contain complex data structures. The Metadata Browser displays these values with expandable controls so you can inspect the full detail.

### Labels

Label properties, such as **DisplayName** and **Description**, show the label text on a single line with an expand pointer (**▶**) and a **Copy** button. Select the expand pointer to reveal the full label structure, including all localized label values and metadata IDs.

:::image type="content" source="media/browse-your-metadata/label-properties-expand-behavior.png" alt-text="Screenshot of Metadata Browser showing DisplayName property expanded to reveal label structure and metadata details.":::

### Option sets

OptionSet properties display a summary of option values and labels. Select the expand pointer to view the full OptionSet metadata, including properties like `IsGlobal`, `IsCustomOptionSet`, and `IsManaged`. Expand further to see each individual option's detail, including type-specific properties for state and status options.

#### Simple options

The default view for options shows only the values and the localized labels. This view provides the data you need most of the time.

:::image type="content" source="media/browse-your-metadata/simple-options.png" alt-text="Screenshot of table columns editor displaying Status Reason option set with values 1: Active and 2: Inactive.":::

#### Expanded options

You can expand the options to view all the metadata that is sometimes important. For example, the [StatusOptionMetadata.TransitionData property](xref:Microsoft.Xrm.Sdk.Metadata.StatusOptionMetadata.TransitionData) can be important when you [define custom state model transitions](define-custom-state-model-transitions.md).

:::image type="content" source="media/browse-your-metadata/expanded-options.png" alt-text="Screenshot of Account table columns editor with Status Reason option set expanded to show metadata and option details.":::

> [!TIP]
> To copy text from the page, select the text and use **Ctrl+C**. You can also use the **Copy** buttons that appear next to labels and option set values to copy data to the clipboard.

## Community tools

Other tools created by the community that you can use to browse metadata for your environment include:

- [Power Platform ToolBox](https://www.powerplatformtoolbox.com/) includes [Metadata Browser](https://www.powerplatformtoolbox.com/tools/cbbb1649-3cc8-4c0f-9795-1ef64a1ab96d).
- [XrmToolBox](https://www.xrmtoolbox.com/) includes [Metadata Browser](https://www.xrmtoolbox.com/plugins/MsCrmTools.MetadataBrowser/).


> [!NOTE]
> These community tools are different tools than the one described in this article. Use whichever tool you like best. For more community developed tools, see the [Developer tools](developer-tools.md) article.
>
> The community tools aren't a product of Dataverse, and Microsoft doesn't provide support for the community tools. 
> If you have questions about the tool, contact the publisher. More Information: [XrmToolBox](https://www.xrmtoolbox.com).

### Related articles

 [Developer tools for Dataverse](developer-tools.md)   
 [Customize table definitions](customize-entity-metadata.md)
  

[!INCLUDE[footer-include](../../includes/footer-banner.md)]
