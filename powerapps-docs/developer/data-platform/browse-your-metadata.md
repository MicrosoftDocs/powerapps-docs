---
title: "Browse the metadata for your organization (Microsoft Dataverse) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "You can use the Metadata Browser to view tables and their properties in Microsoft Dataverse. The Metadata Browser is a managed solution you can download and install on your organization." # 115-145 characters including spaces. This abstract displays in the search result.
ms.custom: ""
ms.date: 03/16/2021
ms.reviewer: "pehecke"
ms.service: powerapps
ms.topic: "article"
author: "phecke" # GitHub ID
ms.author: "pehecke" # MSFT alias of Microsoft employees only
manager: "ryjones" # MSFT alias of manager or PM counterpart
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---
# Browse the metadata for your environment

[!INCLUDE[cc-data-platform-banner](../../includes/cc-data-platform-banner.md)]

You can use the Metadata Browser to view tables and their properties in Microsoft Dataverse. The Metadata Browser is a managed solution you can download using the links below.


## Import the solution

After you download the solution, you must import it to be able to use it.

## Open as an app
Dataverse is configured as an app. After you install the **Entity Metadata Browser** solution, locate the **Metadata Tools** app and open it. **Entities** is the default view. From the **Tools** navigation area you can select **Entity Metadata** to inspect individual tables.

## Use the app
After you import the solution successfully, locate the app by selecting **Apps** in the left navigation pane; the app is listed as **Metadata Tools**.

After you install the **Entity Metadata Browser** solution, open the managed solution by double-clicking the row in the solutions list and view the **Configuration** page to view information about the Metadata Browser and buttons to launch two different views.
- **Metadata Browser** is equivalent to the **Entities** view in the app.
- **Entity Metadata Browser** is equivalent to the **Entity Metadata** view in the app.

## Entities view

On opening the app, **Entities** is the default view.

![Entities view](media/metadata-tools-entity.png)

You can perform the following actions:

- **View Entity Details**: Select a table to view using the **Entity Metadata** view.
- **Edit Entity**: Open the selected table form in the default organization, if the table supports this.
- **Text Search**: Perform a text search to filter displayed tables using the following table properties: <xref:Microsoft.Xrm.Sdk.Metadata.EntityMetadata.SchemaName>, <xref:Microsoft.Xrm.Sdk.Metadata.EntityMetadata.LogicalName>, <xref:Microsoft.Xrm.Sdk.Metadata.EntityMetadata.DisplayName>, <xref:Microsoft.Xrm.Sdk.Metadata.EntityMetadata.ObjectTypeCode>, or <xref:Microsoft.Xrm.Sdk.Metadata.MetadataBase.MetadataId>.
- **Filter Entities**: Set simple criteria to view a sub-set of tables. All criteria are evaluated using AND logic.
- **Filter Properties**: Filter the properties displayed for any selected table. There are nearly 100 properties in the list. Use this to select just the ones you are interested in.

## Entity Metadata view

You can perform the following actions for a single table:

- **Entity**: Change the table that you want to view.
- **Properties**: View all the properties for the table and filter the properties displayed.

    - **Edit Entity**: Open the selected table edit form in the default organization, if the table supports this.
    - **Filter Properties**: Filter the properties displayed for any selected table. There are nearly 100 properties in the list. Use this to select just the ones you are interested in.

- **Attributes**: View the columns in a master/detail view. With this view you can:

    - **Edit Attribute**: Open the selected column form in the default organization, if the column supports this.
    - **Text Search**: Perform a text search to filter displayed columns using the following column properties: <xref:Microsoft.Xrm.Sdk.Metadata.AttributeMetadata.SchemaName>, <xref:Microsoft.Xrm.Sdk.Metadata.AttributeMetadata.LogicalName>, <xref:Microsoft.Xrm.Sdk.Metadata.AttributeMetadata.DisplayName>, or <xref:Microsoft.Xrm.Sdk.Metadata.MetadataBase.MetadataId>.
    - **Filter Attributes**: Filter columns by any column property values.
    - **Filter Properties**: Filter the properties displayed for the selected column.

- **Keys**: If alternate keys are enabled for a table you can examine how they are configured.

- **Relationships**: View the three types of relationships: One-To-Many, Many-To-One, and Many-To-Many. With these views you can:  
    - **Edit Relationship**: Open the selected relationship form in the default organization, if the relationship supports this.  
    - **Text Search**: Perform a text search to filter displayed relationships using values relevant to the type of relationship.  
    - **Filter Properties**: Filter the relationship by any relationship property value.

- **Privileges**: View table privileges. With this view you can:  
    - Filter the displayed privilege using the `PrivilegeId`.

> [!NOTE]
> When viewing the table detail properties, you'll see that many complex properties are expandable. The most useful value is displayed with a link that allows toggling to a more detailed view. The detailed view reflects the structure of the data if you were to retrieve it programmatically. The detailed view also reveals other relevant data that can be retrieved in the same area, for example, if any localized labels are present for **Display Name** properties.

> [!TIP]
> To copy text from the page, simply select the text and use the Ctrl+C keyboard shortcut or the context menu **Copy** command.

## Community tools

**Metadata Browser** is a tool that XrmToolbox community developed for Dataverse. Please see the [Developer tools](developer-tools.md) topic for community developed tools.

> [!NOTE]
> The community tools are not a product of Dataverse and Microsoft does not provide support for the community tools. 
> If you have questions pertaining to the tool, please contact the publisher. More Information: [XrmToolBox](https://www.xrmtoolbox.com).

### See also

 [Developer Tools for Dataverse](developer-tools.md)<br />
 [Customize Entity Metadata](customize-entity-metadata.md)<br />
  


[!INCLUDE[footer-include](../../includes/footer-banner.md)]