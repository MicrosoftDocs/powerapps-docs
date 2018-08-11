---
title: "Browse the metadata for your organization (Common Data Service for Apps) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "You can use the Entity Metadata Browser to view entities and their properties in Dynamics 365 Customer Engagement. The Entity Metadata Browser is a managed solution you can download and install on your organization." # 115-145 characters including spaces. This abstract displays in the search result.
ms.custom: ""
ms.date: 08/01/2018
ms.reviewer: ""
ms.service: "powerapps"
ms.topic: "article"
author: "JimDaly" # GitHub ID
ms.author: "jdaly" # MSFT alias of Microsoft employees only
manager: "ryjones" # MSFT alias of manager or PM counterpart
---
# Browse the metadata for your environment

You can use the Entity Metadata Browser to view entities and their properties in Common Data Service for Apps. The Entity Metadata Browser is a managed solution you can download using the links below.


|                                                                                               Version                                                                                                |                                                                                     Download                                                                                      |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Common Data Service for Apps | [Microsoft Downloads: MetadataBrowser_3_0_0_5_managed.zip](http://download.microsoft.com/download/8/E/3/8E3279FE-7915-48FE-A68B-ACAFB86DA69C/MetadataBrowser_3_0_0_5_managed.zip) |

After you download the solution, you must install it. For information about how to install a managed solution, see [Import, update, and export solutions](/dynamics365/customer-engagement/developer/customize/import-update-export-solutions)  

## Open as an app
CDS for Apps is configured as an app. After you install the **Entity Metadata Browser** solution, locate the **Metadata Tools** app and open it. **Entities** is the default view. From the **Tools** navigation area you can select **Entity Metadata** to inspect individual entities.

## Open from the solution configuration page
For earlier versions you must use the following steps, but these also work for the latest verison.  

After you install the **Entity Metadata Browser** solution, open the managed solution by double-clicking the row in the solutions list and view the **Configuration** page to view information about the Entity Metadata Browser and buttons to launch two different views.
- **Metadata Browser** is equivilent to the **Entities** view in the app.
- **Entity Metadata Browser** is equivilent to the **Entity Metadata** view in the app.

## Entities view
You can perform the following actions:

- **View Entity Details**: Select an entity to view using the **Entity Metadata** view.
- **Edit Entity**: Open the selected entity form in the default organization, if the entity supports this.
- **Text Search**: Perform a text search to filter displayed entities using the following entity properties: <xref:Microsoft.Xrm.Sdk.Metadata.EntityMetadata.SchemaName>, <xref:Microsoft.Xrm.Sdk.Metadata.EntityMetadata.LogicalName>, <xref:Microsoft.Xrm.Sdk.Metadata.EntityMetadata.DisplayName>, <xref:Microsoft.Xrm.Sdk.Metadata.EntityMetadata.ObjectTypeCode>, or <xref:Microsoft.Xrm.Sdk.Metadata.MetadataBase.MetadataId>.
- **Filter Entities**: Set simple criteria to view a sub-set of entities. All criteria are evaluated using AND logic.
- **Filter Properties**: Filter the properties displayed for any selected entity. There are nearly 100 properties in the list. Use this to select just the ones you are interested in.

## Entity Metadata view
 You can perform the following actions for a single entity:

- **Entity**: Change the entity that you want to view.
- **Properties**: View all the properties for the entity and filter the properties displayed.

    - **Edit Entity**: Open the selected entity edit form in the default organization, if the entity supports this.
    - **Filter Properties**: Filter the properties displayed for any selected entity. There are nearly 100 properties in the list. Use this to select just the ones you are interested in.

- **Attributes**: View the entity attributes in a master/detail view. With this view you can:

    - **Edit Attribute**: Open the selected attribute form in the default organization, if the attribute supports this.
    - **Text Search**: Perform a text search to filter displayed attributes using the following attribute properties: <xref:Microsoft.Xrm.Sdk.Metadata.AttributeMetadata.SchemaName>, <xref:Microsoft.Xrm.Sdk.Metadata.AttributeMetadata.LogicalName>, <xref:Microsoft.Xrm.Sdk.Metadata.AttributeMetadata.DisplayName>, or <xref:Microsoft.Xrm.Sdk.Metadata.MetadataBase.MetadataId>.
    - **Filter Attributes**: Filter attributes by any attribute property values.
    - **Filter Properties**: Filter the properties displayed for the selected attribute.

- **Keys**: If alternate keys are enabled for an entity you can examine how they are configured.

- **Relationships**: View the three types of entity relationships: One-To-Many, Many-To-One, and Many-To-Many. With these views you can:  
    - **Edit Relationship**: Open the selected relationship form in the default organization, if the relationship supports this.  
    - **Text Search**: Perform a text search to filter displayed relationships using values relevant to the type of relationship.  
    - **Filter Properties**: Filter the relationship by any relationship property value.

- **Privileges**: View entity privileges. With this view you can:  
    - Filter the displayed privilege using the `PrivilegeId`.

> [!NOTE]
> When viewing the entity detail properties, you’ll see that many complex properties are expandable. The most useful value is displayed with a link that allows toggling to a more detailed view. The detailed view reflects the structure of the data if you were to retrieve it programmatically. The detailed view also reveals other relevant data that can be retrieved in the same area, for example, if any localized labels are present for **Display Name** properties.

> [!TIP]
> To copy text from the page, simply select the text and use the Ctrl+C keyboard shortcut or the context menu **Copy** command.

## Community tools

**Metadata Browser** is a tool that XrmToolbox community developed for CDS for Apps. Please see the [Developer tools](developer-tools.md) topic for community developed tools.

> [!NOTE]
> The community tools are not a product of CDS for Apps and does not extend support to the community tools. 
> If you have questions pertaining to the tool, please contact the publisher. More Information: [XrmToolBox](https://www.xrmtoolbox.com).

### See also

 [Developer Tools for Dynamics 365](developer-tools.md)<br />
 [Customize Entity Metadata](customize-entity-metadata.md)<br />
 [Extend the Metadata Model for Dynamics 365](/dynamics365/customer-engagement/developer/org-service/use-organization-service-metadata)<br />
 [Create Early Bound Entity Classes with the Code Generation Tool (CrmSvcUtil.exe)](/dynamics365/customer-engagement/developer/org-service/create-early-bound-entity-classes-code-generation-tool)<br />
 [Analyze Plug-in Performance](/dynamics365/customer-engagement/developer/analyze-plugin-performance)<br />
 [Solution Tools for Team Development](solution-tools-team-development.md)<br />