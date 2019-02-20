---
title: "View data with visualizations (charts)  (model-driven apps) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "Visualizations let you see your business data graphically. A visualization is attached to an entity in Common Data Services for Apps. You can attach multiple visualizations to an entity, however, only one visualization can be displayed at a time along-side a grid. You can view multiple visualizations at the same time by using a dashboard." # 115-145 characters including spaces. This abstract displays in the search result.
ms.custom: ""
ms.date: 10/31/2018
ms.reviewer: ""
ms.service: "powerapps"
ms.topic: "article"
author: "KumarVivek" # GitHub ID
ms.author: "kvivek" # MSFT alias of Microsoft employees only
manager: "shilpas" # MSFT alias of manager or PM counterpart
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---
# View data with visualizations (charts)

<!-- https://docs.microsoft.com/dynamics365/customer-engagement/developer/customize-dev/view-data-with-visualizations-charts -->


Visualizations let you see your business data graphically. A visualization is attached to an entity in Common Data Services for Apps. You can attach multiple visualizations to an entity, however, only one visualization can be displayed at a time along-side a grid. You can view multiple visualizations at the same time by using a dashboard. More information: [Analyze Data with Dashboards](analyze-data-with-dashboards.md)  
  
 You can use a chart or a web resource as a visualization in CDS for Apps. For charts, you can use the chart designer in Model-driven Apps. However, to use a web resource in a visualization, you must either use the SDK or import a custom visualization XML into Model-driven Apps.
  
<a name="VisualizationTypes"></a>   
## Visualization ownership  
 In Model-driven Apps, there are two types of visualization ownership: organization-owned and user-owned.  
  
- An organization-owned visualization is owned by an organization, and cannot be assigned or shared. The `SavedQueryVisualization` entity represents the organization-owned visualization. These visualizations are solution-aware entities in Model-driven Apps. Whenever you update a saved query visualization, you must publish the changes for the updates to be available across the organization by using the <xref:Microsoft.Crm.Sdk.Messages.PublishAllXmlRequest> message. This entity is referred to as a *System Chart* in the Model-driven Apps web application.  
  
- A user-owned visualization is owned by an individual user, and can be assigned and shared with other users and teams. The `UserQueryVisualization` entity represents the user-owned visualization. This entity is referred to as a *User Chart* in the Model-driven Apps web application, and is displayed under **My Charts** in the chart drop-down list.  
  
  A user query visualization is not associated with a user query (view), despite the entity name. The view aspect of this entity is used only for setting the filter criteria.  
  
<a name="Charts"></a>   
## Chart visualizations  
 Charts let you see summaries of grid data. The charts are built by using the Microsoft Chart Controls for Microsoft .NET Framework 3.5. For more information about Microsoft Chart Controls, see [Download: Chart Controls for .NET Framework](http://go.microsoft.com/fwlink/p/?LinkId=128852).  
  
 These charts are integrated with the grids in the web application. When you apply a filter (query) to the data in a grid, the filter is applied to the chart also, and the chart is updated accordingly. Similarly, when you perform drill-down operations on a chart, the grid data is updated automatically.  
  
 A chart attached to an entity is available for all the views for the entity. A chart displays data according to the currently selected (or displayed) view of an entity. A chart can display data from both a saved query (organization-owned view) and a user query (user-owned view).  
  
 Charts display data for only those saved queries (organization-owned views) that use FetchXML (`SavedQuery.FetchXml` attribute) to filter the records. If a saved query uses the query API (`SavedQuery.QueryAPI` attribute) to filter the records, the chart will not appear for that saved query. This limitation is not applicable for user queries (user-owned views) because the user query entity does not use the `QueryAPI` attribute to filter the records.  
  
 For more information about how to work with charts, see [Understanding Charts: Underlying Data and Chart Representation](understand-charts-underlying-data-chart-representation.md).  
  
<a name="ChartTypes"></a>   
### Chart types in Microsoft chart controls  
 Microsoft Chart Controls is used to build charts in Model-driven Apps. Microsoft Chart Controls enable you to create various chart types such as column, bar, area, stacked, line, bubble, and pie.  
  
 The following chart types are supported out-of-box in CDS for Apps: *Column*, *Area*, *Bar*, *Line*, *Pie*, and *Funnel*. However, you can extend the functionality by creating other supported Microsoft Chart Controls chart types such as multi-series, stacked, and 100% stacked (comparison) charts by specifying appropriate content in the data description and presentation description XML strings for a chart. More information: [Specifying Chart Data](understand-charts-underlying-data-chart-representation.md)  
  
<a name="WebResources"></a>   
## Web resource visualizations  
 Web resources are virtual files that are stored in the Model-driven Apps database and may be retrieved using a unique URL address. You can display an existing web resource as a visualization, and display it in the **Charts** area in Model-driven Apps together with other charts for an entity. For more information about web resources, see [Web resources for model-driven apps](web-resources.md).  
  
 You can use the following types of web resources in a visualization: [Webpage (HTML) web resources](webpage-html-web-resources.md) and [Image (JPG, PNG, GIF, ICO) Web Resources](image-web-resources.md). For more information about how to create a visualization with a web resource, see [Create a web resource visualization](create-visualization-chart.md#create-a-web-resource-visualization).  
  
<a name="SupportedVisualizationEntities"></a>   
## Entities supported for visualizations  
 You can create and attach visualizations to only those entities in CDS for Apps that support the new ribbon interface. This is because all of the chart controls are only present in the ribbon interface of CDS for Apps. Custom entities are also supported for visualizations. You can turn off the visualization support for custom entities if you want to. However, you cannot disable visualization support for the default entities.  
  
 The following lists the default entities that are supported for visualizations.  
  
 Account  
ActivityPointer  
Appointment  
BulkOperation  
Campaign  
CampaignActivity  
CampaignResponse  
Competitor  
Connection  
Contact  
Contract  
Email  
Entitlement  
EntitlementChannel  
EntitlementTemplateChannel  
Fax  
Goal  
GoalRollupQuery  
Incident  
Invoice  
InvoiceDetail  
KbArticle  
Lead  
Letter  
List  
Mailbox  
Metric  
Opportunity  
OpportunityProduct  
PhoneCall  
Position  
PriceLevel  
Product  
ProductAssociation  
ProductSubstitute  
QueueItem  
Quote  
QuoteDetail  
RecurringAppointmentMaster  
Report  
SalesLiterature  
SalesOrder  
SalesOrderDetail  
Service  
ServiceAppointment  
SLAKPIInstance  
SocialActivity  
SocialProfile  
SystemUser  
Task  
Team  
Territory  
UoMSchedule  
  
### See also  
 [Chart and Analyze Data](customize-visualizations-dashboards.md)   
 [Specifying Chart Data](understand-charts-underlying-data-chart-representation.md)   
 [Actions on Chart](actions-visualizations-charts.md)   
 [Create a Chart](create-visualization-chart.md)   
 [Sample Charts](sample-charts.md)   
 [SavedQueryVisualization Entity](../common-data-service/reference/entities/savedqueryvisualization.md)   
 [UserQueryVisualization Entity](../common-data-service/reference/entities/userqueryvisualization.md)
 [Download: Chart Controls for .NET Framework Language Pack](http://www.microsoft.com/downloads/details.aspx?FamilyId=581FF4E3-749F-4454-A5E3-DE4C463143BD&displaylang=en)   
 [Download: Chart Controls Add-on for Visual Studio](http://www.microsoft.com/downloads/details.aspx?FamilyId=1D69CE13-E1E5-4315-825C-F14D33A303E9&displaylang=en)   
 [Download: Chart Controls for .NET Framework Documentation](http://go.microsoft.com/fwlink/p/?LinkId=128301)   
 [Samples Environment for Microsoft Chart Controls](http://code.msdn.microsoft.com/mschart)   
 [Chart Controls Forum](http://go.microsoft.com/fwlink/p/?LinkId=128713)
