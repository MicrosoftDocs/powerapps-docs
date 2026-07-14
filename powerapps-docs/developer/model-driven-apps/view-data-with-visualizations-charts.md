---
title: "View data with visualizations (charts)  (model-driven apps)"
description: "Visualizations let you see your business data graphically. A visualization is attached to a table in Microsoft Dataverse. You can attach multiple visualizations to a table, however, only one visualization can be displayed at a time alongside a grid. You can view multiple visualizations at the same time by using a dashboard."
author: jasongre
ms.author: jasongre
ms.date: 06/18/2026
ms.reviewer: jdaly
ms.subservice: mda-developer
search.audienceType: 
  - developer
contributors: 
  - JimDaly
---  
# View data with visualizations (charts)

Visualizations let you see your business data graphically. A visualization is attached to a table in Microsoft Dataverse. You can attach multiple visualizations to a table, but you can display only one visualization at a time alongside a grid. You can view multiple visualizations at the same time by using a dashboard. For more information, see [Analyze data with dashboards](analyze-data-with-dashboards.md).  
  
In Dataverse, you can use a chart or a web resource as a visualization. For charts, you can use the chart designer in model-driven apps. However, to use a web resource in a visualization, you must either use the SDK or import a custom visualization XML into model-driven apps.

> [!IMPORTANT]
> When you import a chart, the XML encoded to a base64 string has a maximum length of 16,000 characters. This string represents roughly 12,000 characters before encoding.

[!INCLUDE[cc-terminology](../data-platform/includes/cc-terminology.md)]

<a name="VisualizationTypes"></a> 

## Visualization ownership  

In model-driven apps, two types of visualization ownership exist: organization-owned and user-owned.  
  
- You can't assign or share organization-owned visualizations. The [`SavedQueryVisualization` table](../data-platform/reference/entities/savedqueryvisualization.md) represents the organization-owned visualization. These visualizations are solution-aware tables in model-driven apps. Whenever you update a saved query visualization, you must publish the changes for the updates to be available across the organization by using the <xref:Microsoft.Crm.Sdk.Messages.PublishAllXmlRequest> message. The model-driven apps web application refers to this table as a *System Chart*.  
  
- You can assign and share user-owned visualizations with other users and teams. The [`UserQueryVisualization` table](../data-platform/reference/entities/userqueryvisualization.md) represents the user-owned visualization. The model-driven apps web application refers to this table as a *User Chart*, and it appears under **My Charts** in the chart drop-down list.  
  
  Despite the table name, a user query visualization isn't associated with a user query (view). The view aspect of this table is used only for setting the filter criteria.  
  
<a name="Charts"></a> 

## Chart visualizations 

Charts let you see summaries of grid data. The charts use Microsoft Chart Controls for Microsoft .NET Framework 3.5. For more information about Microsoft Chart Controls, see [Toolbox - Microsoft Chart Controls, Visual Studio Automatic Code Snippets, And More](/archive/msdn-magazine/2009/april/microsoft-chart-controls-visual-studio-automatic-code-snippets).  
  
These charts integrate with the grids in the web application. When you apply a filter (query) to the data in a grid, the filter also applies to the chart, and the chart updates accordingly. Similarly, when you perform drill-down operations on a chart, the grid data updates automatically.  
  
A chart attached to a table is available for all the views for the table. A chart displays data according to the currently selected (or displayed) view of a table. A chart can display data from both a saved query (organization-owned view) and a user query (user-owned view).  
  
Charts display data for only those saved queries (organization-owned views) that use FetchXML (`SavedQuery.FetchXml`) to filter the records. If a saved query uses the query API (`SavedQuery.QueryAPI`) to filter the records, the chart doesn't appear for that saved query. This limitation doesn't apply to user queries (user-owned views) because the user query table doesn't use the `QueryAPI` to filter the records.  
  
For more information about how to work with charts, see [Understanding Charts: Underlying data and chart representation](understand-charts-underlying-data-chart-representation.md).  
  
<a name="ChartTypes"></a>

### Chart types in Microsoft chart controls  

Model-driven apps use Microsoft Chart Controls to build charts. Microsoft Chart Controls enable you to create various chart types such as column, bar, area, stacked, line, bubble, and pie.  
  
Dataverse supports the following chart types out of the box: *Column*, *Area*, *Bar*, *Line*, *Pie*, and *Funnel*. You can extend the functionality by creating other supported Microsoft Chart Controls chart types such as multiseries, stacked, and 100% stacked (comparison) charts by specifying appropriate content in the data description and presentation description XML strings for a chart. [Learn more about specifying chart data](understand-charts-underlying-data-chart-representation.md).  
  
<a name="WebResources"></a>

## Web resource visualizations

Web resources are virtual files that are stored in the model-driven apps database and can be retrieved by using a unique URL address. You can display an existing web resource as a visualization, and display it in the **Charts** area in model-driven apps together with other charts for a table. For more information about web resources, see [Web resources for model-driven apps](web-resources.md).  

You can use the following types of web resources in a visualization: [Webpage (HTML) web resources](webpage-html-web-resources.md) and [Image (JPG, PNG, GIF, ICO) web resources](image-web-resources.md). For more information about how to create a visualization with a web resource, see [Create a web resource visualization](create-visualization-chart.md#create-a-web-resource-visualization).  
  

## Tables supported for visualizations 

You can create and attach visualizations only to tables in Dataverse that support the ribbon interface. Supporting the ribbon interface is required because all of the chart controls are only present in the ribbon interface of model-driven apps. Custom tables also support visualizations. You can turn off the visualization support for custom tables if you want. However, you can't disable visualization support for the default tables. 

## Control limit on dashboards

A dashboard can contain a maximum of 20 controls. You can't increase this limit. If you exceed the limit, you get the following error message:

> Name: `MaximumControlsLimitExceeded`<br />
> Code: `0x8004E301`<br />
> Number: `-2147163391`<br />
> Message: `The dashboard Form XML contains more than the maximum allowed number of control elements: 20.`
  
### See also

[Chart and analyze data](customize-visualizations-dashboards.md)   
[Specifying chart data](understand-charts-underlying-data-chart-representation.md)   
[Actions on chart](actions-visualizations-charts.md)   
[Create a chart](create-visualization-chart.md)   
[Sample charts](sample-charts.md)   
[SavedQueryVisualization table](../data-platform/reference/entities/savedqueryvisualization.md)   
[UserQueryVisualization table](../data-platform/reference/entities/userqueryvisualization.md)   
[Download: Chart Controls for .NET Framework documentation](/previous-versions/visualstudio/visual-studio-2010/dd456632(v=vs.100))   


[!INCLUDE[footer-include](../../includes/footer-banner.md)]
