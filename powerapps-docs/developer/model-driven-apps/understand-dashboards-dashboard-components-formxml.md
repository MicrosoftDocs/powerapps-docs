---
title: "Understand dashboards: Dashboard components and FormXML (model-driven apps)"
description: "Dashboards are one of the different types of forms in Mode-driven Apps. You can use the SystemForm.Type or UserForm.Type to determine whether the form is a dashboard."
author: jasongre
ms.author: jasongre
ms.date: 06/18/2026
ms.reviewer: jdaly
ms.topic: how-to
ms.subservice: mda-developer
search.audienceType: 
  - developer
contributors: 
  - JimDaly
---
# Understand dashboards: Dashboard components and FormXML

Dashboards are one of the different types of forms in model-driven apps. Use the `SystemForm.Type` or `UserForm.Type` to determine whether the form is a dashboard. A form of dashboard type has the property value of `0`.  

The definition of the form content and presentation is stored in the FormXML. For more information, see [Form XML Schema](form-xml-schema.md).  

 For sample FormXML strings for different types of dashboards, see [Sample Dashboards](sample-dashboards.md).  

## Dashboard components

A dashboard can contain charts, grids, IFRAMEs, or web resources. By default, a single dashboard can contain up to six of these components.  

### Charts

An organization-owned dashboard can contain only organization-owned charts. However, a user-owned dashboard can contain user-owned and organization-owned charts. For more information, see [Charts (Visualizations) for model-driven apps](view-data-with-visualizations-charts.md).  

### Grids

Grids fetch data from queries (views) in model-driven apps. An organization-owned dashboard can contain only the grids that fetch data from saved queries. However, a user-owned dashboard can contain grids that fetch data from user and saved queries. For more information, see [SavedQuery table](../data-platform/reference/entities/savedquery.md).

[!INCLUDE[cc-terminology](../data-platform/includes/cc-terminology.md)]

### IFRAMEs

When you add an IFRAME to an organization-owned dashboard, you can specify whether to restrict or allow cross-frame scripting.
To do so, use the `<Security>` parameter in the IFRAME control in the FormXML. However, for user-owned dashboards, cross-frame scripting for IFRAMEs is restricted, and you can't change it. If you attempt to create a user-owned dashboard that contains an IFRAME with cross-frame scripting enabled, an error message is displayed.  

### Web resources

You can include only form-enabled web resources in a dashboard. Although this restriction applies when you add a web resource by using the Dashboard designer in the web application, the SDK doesn't apply this restriction when you add a web resource to a dashboard. For more information, see [Web resources for model-driven apps](web-resources.md).

<a name="DashboardComponentsandFormXML"></a>

## Dashboard components and FormXML elements

Model-driven apps display dashboard components based on the values specified in the FormXML. The following image shows an example of a dashboard. Each dashboard can include multiple tabs. Tabs are a vertical stack that separates the body of the dashboard, and you can expand or collapse them. A tab can contain multiple sections. Sections enable grouping and layout of dashboard components.

> [!NOTE]
> The dashboard page doesn't display tab and section names.

 ![Dashboard components layout.](media/crm-v5s-dashboards-components.png "Dashboard components layout")

<a name="SupportedFormXMLElements"></a>

## FormXML elements supported for dashboards  

Although dashboards are a type of form, dashboards don't support all FormXML elements and parameters. The following table provides information about the FormXML elements, child elements, and parameters that dashboards support.

For sample FormXML for different types of dashboards, see [Sample Dashboards](sample-dashboards.md).  

|Element|Child Elements|Element parameters|
|----|----|----|
|`<form>`|`<tabs>`|none|
|`<tabs>`|`<tab>`|none|
|`<tab>`|-`<labels>`<br />-`<columns>`|-`id`<br />-`name`<br />-`expanded`<br />-`verticallayout`<br />-`showlabel`<br />-`locklevel` |
|`<labels>`|`<label>`|none|
|`<label>`|none|-`description`<br />-`languagecode`|
|`<columns>`|`<column>`|none|
|`<column>`|`<sections>`|`width`|
|`<sections>`|`<section>`|`addedby`|
|`<section>`|-`<labels>`<br />-`<rows>`|-`id`<br />-`name`<br />-`showlabel`<br />-`showbar`<br />-`columns`|
|`<rows>`|`<row>`|`addedby`|
|`<row>`|`<cell>`|`addedby`|
|`<cell>`|-`<labels>`<br />-`<control>`|-`auto`<br />-`addedby`<br />-`id`<br />-`showlabel`<br />-`rowspan`<br />-`colspan`|
|`<control>`|`<parameters>`|-`id`<br />-`classid`|
| `<parameters>` |-`<Url>`<br />-`<PassParameters>`<br />-`<Security>`<br />-`<Scrolling>`<br />-`<Border>`<br />-`<ViewIds>`<br />-`<ViewId>`<br />-`<IsUserView>`<br />-`<IsUserChart>`<br />-`<TargetEntityType>`<br />-`<AutoExpand>`<br />-`<RecordsPerPage>`<br />-`<EnableQuickFind>`<br />-`<EnableJumpBar>`<br />-`<EnableChartPicker>`<br />-`<EnableViewPicker>`<br />-`<ChartGridMode>`<br />-`<VisualizationId>` |none|


### See also

[Dashboards](analyze-data-with-dashboards.md)   
[Actions on dashboards](actions-dashboards.md)   
[Create a dashboard](create-dashboard.md)

[!INCLUDE[footer-include](../../includes/footer-banner.md)]
