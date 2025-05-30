---
title: "Create a visualization (chart) (model-driven apps)"
description: "Learn how to create a chart visualization and a web resource visualization."
author: jasongre
ms.author: jasongre
ms.date: 04/01/2022
ms.reviewer: jdaly
ms.topic: how-to
ms.assetid: 9dbed5ee-21a4-ab86-fc4c-08c3838e42f2
ms.subservice: mda-developer
search.audienceType:
  - developer
contributors:
  - JimDaly
---

# Create a visualization (chart)

To create a visualization programmatically, you must create a record for the [SavedQueryVisualization table](../data-platform/reference/entities/savedqueryvisualization.md) or [UserQueryVisualization table](../data-platform/reference/entities/userqueryvisualization.md) to create an organization-owned or user-owned chart respectively. This topic shows how to create a chart visualization and a web resource visualization.

[!INCLUDE[cc-terminology](../data-platform/includes/cc-terminology.md)]

<a name="Before"></a>

## Before you create a visualization

Before creating a visualization, make sure that you are aware of the following:

- **Type of visualization**: If you want your visualizations to be available across the organization and don't want to manage the access levels at a more detailed level, you might want to create an organization-owned visualization. However, if you're concerned about the access privileges and security of your visualization, consider creating a user-owned visualization where you have more control over who can access it.

  > [!NOTE]
  > Organization-owned visualizations can only be created by those users who have the System Administrator or System Customizer role.

- **Associated Table**: Visualizations are attached to tables. More information: [Tables supported for visualizations](view-data-with-visualizations-charts.md). You can attach a chart to a supported table by using the [SavedQueryVisualization.PrimaryEntityTypeCode](../data-platform/reference/entities/savedqueryvisualization.md#BKMK_PrimaryEntityTypeCode) or [UserQueryVisualization.PrimaryEntityTypeCode](../data-platform/reference/entities/userqueryvisualization.md#BKMK_PrimaryEntityTypeCode) parameter.

<a name="CreateChart"></a>

## Create a chart visualization

Charts require you to specify the underlying data for the charts and how the charts will look in the form of _data description_ and _presentation description_ XML strings. More information: [Specifying chart data](understand-charts-underlying-data-chart-representation.md) and [Sample Charts](sample-charts.md).

For a complete sample on how to create an organization-owned chart, see [Sample: Create, retrieve, update, and delete (CRUD) a chart](https://github.com/microsoft/PowerApps-Samples/tree/master/dataverse/orgsvc/CSharp/CRUDOperationsChart).

### Create a multi-series chart

Multi-series charts map multiple series (vertical) axis values to a single category (horizontal) axis value. The only difference from a single series chart is that these charts have multiple `<measurecollection>` and corresponding `<series>` elements specified in the XML strings. Each `<measurecollection>` element contains a child element called `<measure>` that defines a series (vertical) axis value for the same category (horizontal) value. More information: [Understanding Charts: Underlying data and chart representation](understand-charts-underlying-data-chart-representation.md).

For a sample multi-series chart and the corresponding data description and presentation descriptions XML strings, see [Multi-Series chart](sample-charts.md#multi-series-chart).

<a name="CreateWRVisualization"></a>

## Create a web resource visualization

Visualizations containing web resources don't require you to specify the data description and presentation description XML strings. The following sample demonstrates how to create an organization-owned visualization containing a web resource by using the SDK.

```csharp
var newWebResourceVisualization = new SavedQueryVisualization()
{
   Name = "Sample Dashboard Visualization",
   Description = "Sample organization-owned visualization",
  PrimaryEntityTypeCode = Account.EntityLogicalName,
   WebResourceId = new EntityReference(WebResource.EntityLogicalName, _webResourceId))

};
_orgOwnedVisualizationId = service.Create(newWebResourceVisualization);
```

If you want to create a web resource visualization by using the Microsoft Dataverse, you must create an XML file in the following format, and then use **Import Chart** in the ribbon to import the visualization.

```xml
<visualization>
  <name>Visualization_Name</name>
  <description>Description</description>
  <webresourcename>Name_Of_An_Existing_Web_Resource</webresourcename>
  <primaryentitytypecode>Entity_Logical_Name</primaryentitytypecode>
  <isdefault>Value: true or false</isdefault>
</visualization>
```

For example, to create a _Sample Visualization_ that displays an existing Web resource called _new_TestWebResource_, and the visualization should be attached to the _account_ table, the XML should look like.

```xml
<visualization>
  <name>Sample Visualization</name>
  <description>Sample Web Resource Visualization.</description>
  <webresourcename>new_TestWebResource</webresourcename>
  <primaryentitytypecode>account</primaryentitytypecode>
  <isdefault>false</isdefault>
</visualization>
```

### See also

[Charts](view-data-with-visualizations-charts.md)  
[Specifying chart data](understand-charts-underlying-data-chart-representation.md)  
[Actions on chart](actions-visualizations-charts.md)  
[Sample charts](sample-charts.md)  
[Data visualization and analytics](customize-visualizations-dashboards.md)  
[Sample: Create, retrieve, update, and delete (CRUD) a chart](https://github.com/microsoft/PowerApps-Samples/tree/master/dataverse/orgsvc/CSharp/CRUDOperationsChart)

[!INCLUDE[footer-include](../../includes/footer-banner.md)]
