---
title: "Visualization data description schema (model-driven apps) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "The following is the schema for the data description XML string for charts in visualization. This can be used to validate the contents of the data description XML string while creating a chart." # 115-145 characters including spaces. This abstract displays in the search result.
ms.custom: ""
ms.date: 10/31/2018
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
# Visualization data description schema

<!-- https://docs.microsoft.com/dynamics365/customer-engagement/developer/customize-dev/visualization-data-description-schema -->

The following is the schema for the data description XML string for charts in visualization. This can be used to validate the contents of the data description XML string while creating a chart. For more information, see [Understanding Charts: Underlying Data and Chart Representation](understand-charts-underlying-data-chart-representation.md). [!INCLUDE[schema_download](../../includes/schema-download.md)] and see the file `VisualizationDataDescription.xsd` in the folder.  
  
## Schema  
  
```xml  
<?xml version='1.0' encoding='utf-8'?>  
<xs:schema attributeFormDefault='unqualified'  
           elementFormDefault='qualified'  
           xmlns:xs='https://www.w3.org/2001/XMLSchema'>  
 <xs:element name='datadefinition'>  
  <xs:complexType>  
   <xs:sequence>  
    <xs:element name='fetchcollection'>  
     <xs:complexType>  
      <xs:sequence>  
       <xs:element maxOccurs='unbounded'  
                   name='fetch'>  
        <xs:annotation>  
         <!--FetchXML goes here-->  
        </xs:annotation>  
       </xs:element>  
      </xs:sequence>  
     </xs:complexType>  
    </xs:element>  
    <xs:element name='categorycollection'>  
     <xs:complexType>  
      <xs:sequence>  
       <xs:element name='category'  
                   type='CategoryType'  
                   minOccurs='1'  
                   maxOccurs='unbounded' />  
      </xs:sequence>  
     </xs:complexType>  
    </xs:element>  
   </xs:sequence>  
  </xs:complexType>  
 </xs:element>  
 <xs:complexType name ='CategoryType'>  
  <xs:sequence>  
   <xs:element minOccurs='1'  
               maxOccurs='unbounded'  
               name='measurecollection'>  
    <xs:complexType>  
     <xs:sequence>  
      <xs:element minOccurs='1'  
                  maxOccurs='unbounded'  
                  name='measure'>  
       <xs:complexType>  
        <xs:attribute name='alias'  
                      type='xs:string'  
                      use='required' />  
       </xs:complexType>  
      </xs:element>  
     </xs:sequence>  
    </xs:complexType>  
   </xs:element>  
  </xs:sequence>  
  <xs:attribute name='alias'  
                type='xs:string'  
                use='optional' />  
 </xs:complexType>  
</xs:schema>  
```  
### See also  
 [Customize Visualizations and Dashboards](customize-visualizations-dashboards.md)   
 [Understanding Charts: Underlying Data and Chart Representation](understand-charts-underlying-data-chart-representation.md)   
 [Sample Charts](sample-charts.md)   
 [Use FetchXML to construct a query](../data-platform/use-fetchxml-construct-query.md)

[!INCLUDE[footer-include](../../includes/footer-banner.md)]