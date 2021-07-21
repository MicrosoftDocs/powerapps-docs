---
title: "Understand charts: Underlying data and chart representation (model-driven apps) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "Charts display data visually by mapping textual values on two axes: horizontal (x) and vertical (y). The x axis is called the category axis and the y axis is called the series axis." # 115-145 characters including spaces. This abstract displays in the search result.
ms.custom: ""
ms.date: 07/15/2021
ms.reviewer: ""
ms.service: powerapps
ms.topic: "article"
author: "Nkrb" # GitHub ID
ms.subservice: mda-developer
ms.author: "nabuthuk" # MSFT alias of Microsoft employees only
manager: "kvivek" # MSFT alias of manager or PM counterpart
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---
# Understand charts: Underlying data and chart representation

Charts display data visually by mapping textual values on two axes: horizontal (x) and vertical (y). The x axis is called the *category* axis and the y axis is called the *series* axis. The category axis can display numeric as well as non-numeric values whereas the series axis only displays numeric values.  
  
 Charts in model-driven apps can be further classified into the following:  
  
- **Single-series charts**: Charts that display data with a series (y) value mapped to a category (x) value.  
  
- **Multi-series charts**:  Charts that display data with multiple series values mapped to a single category value. Multi-series charts include stacked column charts, which vertically display the contribution of each series to a total across categories, and 100% stacked column charts, which compare the percentage that each series contributes to a total across categories. You can combine different compatible chart types in multi-series charts, for example, column and line, bar and line, and so on.  
  
> [!NOTE]
>  Multi-category charts can be created through the web application or by modifying the XML strings described here.  
  
 While authoring a chart in model-driven apps using the SDK, you need to consider the following two important aspects:  
  
- **Underlying data for the chart**: Specified using the *data description* XML string.  
  
- **Data representation (appearance)**: Specified using the *presentation description* XML string.  
  
> [!NOTE]
> Microsoft Chart Controls lets you create various types of charts such as column, bar, area, line, pie, funnel, bubble, and radar. The chart designer in model-driven apps lets you create only certain types of charts. However, using the SDK, you can create most of the chart types that are supported by Microsoft Chart Controls.  
  
## Use the data description XML string to specify chart data  

 The data description XML string defines the data that is displayed on the chart. The contents of the XML string are validated against the visualization data description schema. For more information about the schema, see [Visualization Data Description Schema](visualization-data-description-schema.md).  
  
 You can specify the data description XML string while you are creating a chart using the `SavedQueryVisualization.DataDescription` or `UserQueryVisualization.DataDescription` for the organization-owned or user-owned chart respectively.  
  
 The data description XML string contains the following two elements: `<FetchCollection>` and `<CategoryCollection>`.  

[!INCLUDE[cc-terminology](../data-platform/includes/cc-terminology.md)]

### The \<FetchCollection> element 
 
 The `<FetchCollection>` element uses FetchXML to retrieve data for the chart. The FetchXML query specifies information about the table columns, aggregate functions, and the group by clauses for the data to be displayed in a chart. All the FetchXML aggregate functions are supported for charts. For more information about the FetchXML aggregate functions, see [Use FetchXML aggregation](../data-platform/use-fetchxml-aggregation.md).  
  
 The FetchXML query enables you to filter your data. Also, filters are applied on charts through views. Therefore, if a filter condition is already specified in the FetchXML query in the `<FetchCollection>` element, and additionally a filter is applied through a view, the chart will display data that is returned after it applies all the filters. For more information about how to use the FetchXML query to filter data, see [Use FetchXML to construct a query](../data-platform/use-fetchxml-construct-query.md).  
  
> [!NOTE]
>  Although the data description XML string is validated again the visualization data description schema, the FetchXML query inside the `<FetchCollection>` element is not. The FetchXML query is validated against the FetchXML schema. For more information, see [FetchXML schema](../data-platform/fetchxml-schema.md).  
  
 If the chart is a comparison chart, the `<FetchCollection>` element will contain two groups by* clauses.  
  
### The \<CategoryCollection> element  

 The `<CategoryCollection>` element contains information about the category (horizontal) and the series (vertical) axes in a chart.  
  
-   Each `<Category>` sub-element has a child element called `<MeasureCollection>` that maps to the `<Series>` element in the presentation description XML. A single series chart has a single `<MeasureCollection>` child element whereas a multi-series chart will have multiple `<MeasureCollection>` child elements, each mapped to the respective `<Series>` element in the presentation description XML.  
  
-   Each `<MeasureCollection>` child element has an element called `<Measure>` that corresponds to the series (vertical) axis value, corresponding to each value on the category (horizontal) axis.  
  
### Example  
 The following is a sample data description XML string:  
  
```xml  
<datadefinition>  
  <fetchcollection>  
    <fetch mapping="logical" count="10">  
      <entity name="opportunity">  
        <attribute name="estimatedvalue" />  
        <order attribute="estimatedvalue" descending="true" />  
      </entity>  
    </fetch>  
  </fetchcollection>  
  <categorycollection>  
    <category>  
      <measurecollection>  
        <measure alias="estimatedvalue" />  
      </measurecollection>  
    </category>  
  </categorycollection></datadefinition>  
```  
  
For more sample data description XML strings, see [Sample Charts](sample-charts.md).  
  
## Use the presentation description XML string to specify data representation 

The presentation description XML string contains information about the appearance of the chart such as chart title, chart color, and chart type (bar, column, line, and so on). There is no schema definition for this XML string. However, the XML is a serialization of the [Chart](/dotnet/api/system.web.ui.datavisualization.charting.chart) class in Microsoft Chart Controls. More information: [Chart Controls](/previous-versions/visualstudio/visual-studio-2010/dd456632(v=vs.100))  

You can specify the presentation description XML string while you are creating a chart using the `SavedQueryVisualization.PresentationDescription` or `UserQueryVisualization.PresentationDescription` for the organization-owned or user-owned chart, respectively.

> [!IMPORTANT]
> In Unified Interface, only a subset of properties are supported. More information: [Supported methods and properties in Unified Interface](#methods-and-properties-supported-in-unified-interface)

### Example for web client

The following is a sample presentation description XML string for web client:  
  
```xml  
<Chart Palette="BrightPastel">  
  <Series>  
    <Series _Template_="All" Color="153, 204, 255" BorderColor="164, 164, 164" BorderDashStyle="Solid" BorderWidth="1" ShadowColor="128, 128, 128, 128" ShadowOffset="1" IsValueShownAsLabel="true" Font="{0}, 6.75pt" BackGradientStyle="TopBottom" BackSecondaryColor="0, 102, 153" LabelForeColor="100, 100, 100" ChartType="Column">  
      <SmartLabelStyle Enabled="True" />  
      <Points />  
    </Series>  
  </Series>  
  <ChartAreas>  
    <ChartArea _Template_="All" BackColor="White" BorderColor="26, 59, 105" BorderWidth="0" BorderDashStyle="Solid">      <AxisY LineColor="204, 204, 204" TitleFont="{0}, 8pt, GdiCharSet=0" TitleForeColor="100, 100, 100" LabelAutoFitMaxFontSize="7" LabelAutoFitMinFontSize="7">  
        <MajorTickMark LineColor="Gray" />  
        <MajorGrid Enabled="false" />  
        <LabelStyle Font="{0}, 6.75pt, GdiCharSet=0" ForeColor="100, 100, 100" />  
      </AxisY>  
      <AxisX LineColor="204, 204, 204" TitleFont="{0}, 8pt, GdiCharSet=0" TitleForeColor="100, 100, 100" LabelAutoFitMaxFontSize="7" LabelAutoFitMinFontSize="7">        <MajorTickMark LineColor="Gray" />        <MajorGrid Enabled="false" />  
        <LabelStyle Font="{0}, 6.75pt, GdiCharSet=0" ForeColor="100, 100, 100" />  
      </AxisX>  
    </ChartArea>  
  </ChartAreas>  
  <Titles>  
    <Title _Template_="All" Font="{0}, 9pt, style=Bold, GdiCharSet=0" ForeColor="100, 100, 100"></Title>  
  </Titles>  
  <BorderSkin PageColor="Control" BackColor="CornflowerBlue" BackSecondaryColor="CornflowerBlue" />  
</Chart>  
```  
  
For more sample presentation description XML strings, see [Sample Charts](sample-charts.md).  

## Methods and properties supported in Unified Interface

The following section shows the methods and properties that are supported in Unified Interface:

### AxisX

Gets or sets the X-axis type of the series.

**Properties**

|Property Name| Description|
|-------------|------------|
|Enabled|Gets or sets a value that indicates whether an axis is enabled.|
|LabelStyle Enabled|Gets or sets a flag that indicates whether the label is enabled.|
|LabelStyle ForeColor|Gets or sets the color of the label.|
|LabelStyle Format|Gets or sets the formatting string for the label text. More information: [Supported numeric format for charts](#supported-numeric-format-for-charts-in-unified-interface)|
|LineColor|Gets or sets the line color of an axis.  More information: [Supported color format](#supported-color-format-in-unified-interface)|
|IsReversed|Gets or sets a flag which indicates whether the axis is reversed.<br/> If set to true, it has two effects for x-axis:<br/> - x-axis labels are flipped in the reversed order (from right-to-left)<br/>- It also bring the y-axis to the opposite side, to accommodate above right-to-left x-axis label.|
|MajorGrid Enabled|Gets or sets a flag that determines whether major or minor grid lines are enabled.|
|MajorGrid LineColor|Gets or sets the line color of a grid.  More information: [Supported color format](#supported-color-format-in-unified-interface)|
|MajorTickMark Enabled|Gets or sets a flag that determines whether major grid lines are enabled.|
|MajorTickMark LineColor|Gets or sets the line color of a grid.|
|Title|Gets or sets the title of the axis.|
|TitleForeColor|Gets or sets the text color of an axis title.  More information: [Supported color format](#supported-color-format-in-unified-interface)|


> [!TIP]
> - When there are too many `LABELS`, `HighCharts` omits every second label and tries to render again. A quick work around is to either remove the records, or zoom out the browser.

**Example**

```xml
 <AxisX Enabled="True" LineColor="165, 172, 181" Title="Test XAxis Title" TitleForeColor="91,151,213" IsReversed="true">
    <MajorTickMark LineColor="165, 172, 181" Enabled="true" />
    <MajorGrid LineColor="green" Enabled="true"/>
    <LabelStyle ForeColor="red" Format="#,0,.##K" Enabled="true" />
 </AxisX>
```

### AxisY

Gets or sets the Y-axis type of the series. 

**Properties**

|Property Name| Description|
|-------------|------------|
|AxisY2|Gets or sets an Axis object that represents the secondary Y-axis.<br/> - Second Y-axis only applies to multiple series chart. <br/> - If you create multiple series chart with the chart editor, by default, the `YAxisType=Secondary` property will be added to the 2nd series of your chart, and a `AxisY2` node is added to the XML.<br/> - If you want another series to be measured by second Y axis, you can move the `YAxisType=Secondary` to that series node. <br/> - If you don't want a second Y axis, you can delete the `YAxisType=Secondary`.<br/> - If a Y Axis (either primary or secondary) measures more than 1 series, title will not be added to that Y Axis, because Y Axis title doesn't know which series to display.|
|Enabled|Gets or sets a value that indicates whether an axis is enabled.|
|Interval|Gets or sets the interval of an axis.|
|LabelStyle Enabled|Gets or sets a flag that indicates whether the label is enabled.|
|LabelStyle ForeColor|Gets or sets the color of the label.|
|LabelStyle Format|Gets or sets the formatting string for the label text. More information: [Supported numeric format for charts](#supported-numeric-format-for-charts-in-unified-interface)|
|LineColor|Gets or sets the line color of an axis.  More information: [Supported color format](#supported-color-format-in-unified-interface)|
|MajorGrid Enabled|Gets or sets a flag that determines whether major grid lines are enabled.|
|MajorGrid LineColor|Gets or sets the line color of a grid.  More information: [Supported color format](#supported-color-format-in-unified-interface)|
|MajorTickMark Enabled|Gets or sets a flag that determines whether major grid lines are enabled.|
|MajorTickMark LineColor|Gets or sets the line color of a grid.|
|Maximum|Gets or sets the maximum value of an axis.|
|Minimum|Gets or sets the minimum value of an axis.|
|Title|Gets or sets the title of the axis.|
|TitleForeColor|Gets or sets the text color of an axis title.  More information: [Supported color format](#supported-color-format-in-unified-interface)|

**Example**

```xml
<AxisY Enabled="True" LineColor="165, 172, 181" Title="Test YAxis Title" TitleForeColor="91,151,213" Interval="1" Minimum="0" Maximum="5">
  <MajorTickMark LineColor="165, 172, 181" Enabled="true" />
  <MajorGrid LineColor="green" Enabled="true"/>
  <LabelStyle ForeColor="red" Enabled="true" />
</AxisY>
<AxisY2 Enabled="True" LineColor="165, 172, 181" Title="Test YAxis2 Title" TitleForeColor="91,151,213" Interval="10" Minimum="0" Maximum="100">
  <MajorTickMark LineColor="165, 172, 181" Enabled="true" />
  <MajorGrid LineColor="green" Enabled="true"/>
  <LabelStyle ForeColor="red" Enabled="true" />
</AxisY2>
```

### Chart

The root class for the charts. 

**Properties**

|Property Name|Description|
|-------------|------------|
|PaletteCustomColor|Gets or sets an array of custom palette colors.  It follows the priority as shown below: <br/> - Renders the color defined in the `Series` node. <br/> - If the color pallet is specified, chart picks the color from the color pallet. <br/> - If none is specified, it picks up the default color pallet.  More information: [Supported color format](#supported-color-format-in-unified-interface)|

**Example**

```xml
<Chart Palette="None" PaletteCustomColors="91, 151, 213; #4169E1, red, 127,97,142,206">
```

### ChartArea

Represents a chart area on the chart image.

**Properties**

|Property Name| Description|
|-------------|------------|
|Area3DStyle Enable3D|Gets or sets a value that indicates whether the flag toggles the 3D on and off for a chart area. It supports the following 3D chart types:<br/> - 3D Column <br/> - 3D Bar <br/> - 3D StackedColumn <br/> - 3D StackedBar <br/> - 3D StackedColumn100 <br/> - 3D StackedBar100 <br/> - 3D Pie|
|BackColor|Allow users to set the plot background to either a solid or a gradient color.  More information: [Supported color format](#supported-color-format-in-unified-interface)|
|BackSecondaryColor|Allow users to set the plot background to either a solid or a gradient color.  More information: [Supported color format](#supported-color-format-in-unified-interface)|
|BackGradientStyle|Allow users to set the plot background to either a solid or a gradient color.|

**Example**

```xml
<ChartArea BackColor="orange" BackSecondaryColor="purple" BackGradientStyle="LeftRight" >
  <Area3DStyle Enable3D="true" />
</ChartArea>
```

### Legend

Represents the legend for the chart image.

**Properties**

|Property Name| Description|
|-------------|------------|
|Enabled| Defines whether the legend is enabled. By default it is set to `True`.|

**Example**

```xml
<Legends>
  <Legend Enabled="True"/>
</Legends>
```

### Series

Stores data points and series.

**Properties**

|Property Name| Description|
|-------------|------------|
|BorderColor|Gets or sets the border color of the data point.  More information: [Supported color format](#supported-color-format-in-unified-interface)|
|BorderWidth|Gets or sets the border width of the data point.|
|ChartType| An enumeration value that indicates the chart type that is used to represent the series. The default value is Column. It supports the following chart types: <br/> - Column <br/> - StackedColumn <br/> - StackedColumn100 <br/> - Bar <br/> - StackedBar <br/> - StackedBar100 <br/> - Area <br/> - StackedArea <br/> - StackedArea100 <br/> -  Line <br/> - Pie <br/> - Funnel <br/> - Tag <br/> - Doughnut <br/> - Point|
|Color|Gets or sets the color of the data point. For funnel and pie charts, the color property defined in the series node is ignored, but picks the chart color from color palette.  More information: [Supported color format](#supported-color-format-in-unified-interface)|
|IsValueShownAsLabel|Gets or sets a flag that indicates whether to show the value of the data point on the label.|
|CustomProperties|Allows users to set `FunnelNeckHeight` and `FunnelNeckWidth` to customize funnel chart's shape. FunnelNeckHeight & FunnelNeckWidth represents the percentage. This parameter is only supported for funnel chart types.|
|IsVisibleInLegend|Gets or sets a flag that indicates whether the item is shown in the legend.|
|LabelForeColor|Gets or sets the text color of the label. More information: [Supported color format](#supported-color-format-in-unified-interface)|
|LabelFormat|Gets or sets the format of the data point label. More information: [Supported numeric format for charts](#supported-numeric-format-for-charts-in-unified-interface)|
|LegendText|Gets or sets the text of the item in the legend. For funnel and pie charts, the legend displays each data point's value in a series. Instead of displaying the series name as a whole.|
|YAxisType|Gets or sets the Y-axis type of a series. Only the second Y-axis is supported, not second X-axis.|

> [!NOTE]
> - Currently, we partially support `#PERCENT`. `#VAL` and `#TOTAL` are not supported in Unified Interface. 
> - We only support a maximum of 5 `Series` (1 series and 2 categories/groupby) in a chart. 

**Example**

```xml
<Series>
  <Series ChartType="Column" Color="91, 151, 213" LegendText="Est Revenue" IsVisibleInLegend="True" BorderColor="red" BorderWidth="1" IsValueShownAsLabel="True" LabelFormat="$#,0,.##K" LabelForeColor="59, 59, 59">
  </Series>
  <Series ChartType="Column" Color="237, 125, 49" LegendText="Actual Revenue" IsVisibleInLegend="True" BorderColor="red" BorderWidth="1" IsValueShownAsLabel="True" LabelFormat="$#,0,.##K" LabelForeColor="59, 59, 59" YAxisType="Secondary">
  </Series>
</Series>
```

### Supported color format in Unified Interface

Unified Interface supports the following color formats in chart presentation xml, which is compatible with web client:

- RGB Decimal format: 97,142,206
- RGB HEX format: #4169E1
- ARGB Decimal format: 127,90,138,57
- Browser recognized named colors: red, transparent

### Supported numeric format for charts in Unified Interface

|Formatting values|Description|
|------------|----------------|
|`#,0` | No scaling, No decimals, leading zero|
|`#,0,.##K`|Thousands, up to 2 decimals, leading zero|
|`#,0,,.##M`|Millions, up to 2 decimals, leading zero|
|`#,0,,,.##B` |Billions, up to 2 decimals, leading zero|
|`C`|Currency with default decimals|
|`C0`| Currency with no decimals|
|`C2`|Currency with 2 decimals|
|`F0`|Fixed point|
|`#,0;(#,0);' '`| No scaling, no decimals, leading zero, negative value shown in braces, suppress zeros|
|`#,0,.##K;(#,0,.##K);' '` | Thousands, up to 2 decimals, leading zero negative value shown in braces, suppress zeros|
|`#,0,,.##M;(#,0,,.##M);' '`| Millions,  up to 2 decimals, leading zero negative value shown in braces, suppress zeros|
|`#,0,,,.##B;(#,0,,,.##B);' '` | Billions, up to 2 decimals, leading zero negative value shown in braces, suppress zeros|
|`%`|Percent sign (%) in a format string causes a number to be multiplied by 100 before it is formatted|
|||

### See also  

[Visualizations (Charts)](view-data-with-visualizations-charts.md)   
[Actions on visualizations (Charts)](actions-visualizations-charts.md)   
[Create a chart](create-visualization-chart.md)   
[Use FetchXML to construct a query](../data-platform/use-fetchxml-construct-query.md)   
[FetchXML schema](../data-platform/fetchxml-schema.md)
[Visualization data description schema](visualization-data-description-schema.md)   
[Sample charts](sample-charts.md)   
[Chart class (Microsoft Chart Controls)](/dotnet/api/system.web.ui.datavisualization.charting.chart)


[!INCLUDE[footer-include](../../includes/footer-banner.md)]
