---
title: "Form XML schema (model-driven apps) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "Learn about schema definition for form customizations." # 115-145 characters including spaces. This abstract displays in the search result.
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
# Form XML schema

The following is the schema definition for form customizations for model-driven apps. More information: [Customize forms](customize-entity-forms.md). [!INCLUDE[schema_download](../../includes/schema-download.md)].  

[!INCLUDE[cc-terminology](../data-platform/includes/cc-terminology.md)]

## Schema  
  
```xml  
<?xml version="1.0"?>  
<xs:schema xmlns:xs="https://www.w3.org/2001/XMLSchema"  
           elementFormDefault="qualified"  
           attributeFormDefault="unqualified">  
  <xs:include schemaLocation="RibbonCore.xsd" />  
  <xs:element name="form"  
              type="FormType" />  
  <xs:complexType name="ClientFileIncludeAttributeType">  
    <xs:attribute name="src"  
                  use="required">  
      <xs:simpleType>  
        <xs:restriction base ="xs:string">  
          <xs:pattern value ="(\$webresource:|/)(.)+"/>  
        </xs:restriction>  
      </xs:simpleType>  
    </xs:attribute>  
  
  </xs:complexType>  
  <xs:complexType name="ClientResourcesType">  
    <xs:all>  
      <xs:element name="internalresources"  
                  minOccurs ="0"  
                  maxOccurs ="1">  
        <xs:complexType>  
          <xs:all>  
            <xs:element name ="clientincludes"  
                        minOccurs ="0"  
                        maxOccurs ="1">  
              <xs:complexType >  
                <xs:choice minOccurs="0"  
                           maxOccurs ="100000" >  
                  <xs:element name ="internaljscriptfile"  
                              type="ClientFileIncludeAttributeType"  
                              minOccurs ="0"  
                              maxOccurs ="1" />  
                  <xs:element name ="internalcssfile"  
                              type="ClientFileIncludeAttributeType"  
                              minOccurs ="0"  
                              maxOccurs ="1" />  
                </xs:choice>  
  
              </xs:complexType >  
            </xs:element>  
            <xs:element name ="clientvariables"  
                        minOccurs="0"  
                        maxOccurs ="1">  
              <xs:complexType>  
                <xs:sequence>  
                  <xs:element name ="internaljscriptvariable"  
                              minOccurs ="0"  
                              maxOccurs ="100000">  
                    <xs:complexType>  
                      <xs:attribute name="name"  
                                    use ="required">  
                        <xs:simpleType>  
                          <xs:restriction base ="xs:string">  
                            <xs:pattern value="LOCID_([A-Za-z0-9_])+"/>  
                            <xs:maxLength value ="32"/>  
                          </xs:restriction>  
                        </xs:simpleType>  
                      </xs:attribute>  
                      <xs:attribute name ="resourceid"  
                                    use="required" >  
                        <xs:simpleType>  
                          <xs:restriction base ="xs:string">  
                            <xs:pattern value="([A-Za-z0-9_.])+"/>  
                          </xs:restriction>  
                        </xs:simpleType>  
                      </xs:attribute>  
  
                    </xs:complexType>  
                  </xs:element>  
                </xs:sequence>  
  
              </xs:complexType>  
            </xs:element>  
          </xs:all>  
  
        </xs:complexType>  
      </xs:element>  
      <xs:element name="isvresources"  
                  minOccurs ="0"  
                  maxOccurs ="1">  
        <xs:complexType>  
          <xs:sequence>  
            <xs:element name ="clientincludes"  
                        minOccurs ="0"  
                        maxOccurs ="1">  
              <xs:complexType >  
                <xs:sequence>  
                  <xs:element name ="webresource"  
                              minOccurs ="0"  
                              maxOccurs ="100000">  
                    <xs:complexType>  
                      <xs:attribute name="path"  
                                    type="xs:string"  
                                    use ="required"/>  
                      <xs:attribute name="type"  
                                    use ="required">  
                        <xs:simpleType>  
                          <xs:restriction base="xs:string">  
                            <xs:enumeration value="jscript"/>  
                            <xs:enumeration value ="css" />  
                          </xs:restriction>  
                        </xs:simpleType>  
                      </xs:attribute>  
  
                    </xs:complexType>  
                  </xs:element>  
                </xs:sequence>  
  
              </xs:complexType>  
            </xs:element>  
          </xs:sequence>  
  
        </xs:complexType>  
      </xs:element>  
    </xs:all>  
  
  </xs:complexType>  
  <xs:complexType name="FormDisplayConditionsType">  
    <xs:choice minOccurs="0"  
               maxOccurs="1">  
      <xs:element name="Everyone"  
                  minOccurs="1"  
                  maxOccurs="1">  
        <xs:complexType>  
  
        </xs:complexType>  
      </xs:element>  
      <xs:element name="Role"  
                  minOccurs="1"  
                  maxOccurs="unbounded">  
        <xs:complexType>  
          <xs:attribute name="Id"  
                        type="FormGuidType"  
                        use="required" />  
  
        </xs:complexType>  
      </xs:element>  
    </xs:choice>  
    <xs:attribute name="FallbackForm"  
                  type="xs:boolean"  
                  use="optional" />  
    <xs:attribute name="Order"  
                  type="xs:integer"  
                  use="optional" />  
  
  </xs:complexType>  
  <xs:complexType name="FormLocalizedLabel">  
    <xs:attribute name="LCID"  
                  type="xs:integer" />  
    <xs:attribute name="Text"  
                  type="xs:string" />  
  
  </xs:complexType>  
  <xs:complexType name="FormLocalizedTitles">  
    <xs:sequence minOccurs="1"  
                 maxOccurs="unbounded">  
      <xs:element name="Title"  
                  type="FormLocalizedLabel" />  
    </xs:sequence>  
  
  </xs:complexType>  
  <xs:complexType name="FormNavBarAreasType">  
    <xs:sequence>  
      <xs:element name="NavBarArea"  
                  minOccurs="0"  
                  maxOccurs="unbounded">  
        <xs:complexType>  
          <xs:sequence>  
            <xs:element name="Titles"  
                        minOccurs="1"  
                        maxOccurs="1"  
                        type="FormLocalizedTitles" />  
          </xs:sequence>  
          <xs:attribute name="Id"  
                        type="xs:string"  
                        use="required" />  
  
        </xs:complexType>  
      </xs:element>  
    </xs:sequence>  
  
  </xs:complexType>  
  <xs:complexType name="FormNavBarType">  
    <xs:choice minOccurs="0"  
               maxOccurs="100000">  
      <xs:element minOccurs="0"  
                  maxOccurs="1"  
                  name="NavBarItem">  
        <xs:complexType>  
          <xs:sequence>  
            <xs:element name="Titles"  
                        minOccurs="1"  
                        maxOccurs="1"  
                        type="FormLocalizedTitles" />  
          </xs:sequence>  
          <xs:attribute name="Icon"  
                        type="xs:string"  
                        use="required" />  
          <xs:attribute name="Url"  
                        type="xs:string"  
                        use="required" />  
          <xs:attribute name="Id"  
                        type="xs:string"  
                        use="required" />  
          <xs:attribute name="PassParams"  
                        type="FormCRM_Boolean"  
                        use="optional" />  
          <xs:attribute name="Sequence"  
                        type="xs:nonNegativeInteger"  
                        use="optional" />  
          <xs:attribute name="Area"  
                        type="xs:string"  
                        use="optional" />  
          <xs:attribute name="Client"  
                        type="xs:string"  
                        use="optional" />  
          <xs:attribute name="AvailableOffline"  
                        type="xs:boolean"  
                        use="optional" />  
  
        </xs:complexType>  
      </xs:element>  
      <xs:element name="NavBarByRelationshipItem"  
                  minOccurs="0"  
                  maxOccurs="1">  
        <xs:complexType>  
          <xs:all>  
            <xs:element name="Titles"  
                        minOccurs="0"  
                        maxOccurs="1"  
                        type="FormLocalizedTitles" />  
            <xs:element name="ToolTip"  
                        minOccurs="0"  
                        maxOccurs="1">  
              <xs:complexType>  
                <xs:sequence>  
                  <xs:element name="Titles"  
                              minOccurs="1"  
                              maxOccurs="1"  
                              type="FormLocalizedTitles" />  
                </xs:sequence>  
  
              </xs:complexType>  
            </xs:element>  
            <xs:element name="Privileges"  
                        minOccurs="0"  
                        maxOccurs ="1">  
              <xs:complexType>  
                <xs:sequence >  
                  <xs:element name ="Privilege"  
                              minOccurs ="1"  
                              maxOccurs ="100000">  
                    <xs:complexType>  
                      <xs:attribute name ="Entity"  
                                    type ="xs:string"  
                                    use ="required"/>  
                      <xs:attribute name="Privilege"  
                                    type ="xs:string"  
                                    use ="required"/>  
  
                    </xs:complexType>  
                  </xs:element>  
                </xs:sequence>  
  
              </xs:complexType>  
            </xs:element>  
          </xs:all>  
          <xs:attribute name="RelationshipName"  
                        type="xs:string"  
                        use="required" />  
          <xs:attribute name="Id"  
                        type="xs:string"  
                        use="required" />  
          <xs:attribute name="Area"  
                        type="xs:string"  
                        use="optional" />  
          <xs:attribute name="TitleResourceId"  
                        type="xs:string"  
                        use="optional" />  
          <xs:attribute name="Client"  
                        type="xs:string"  
                        use="optional" />  
          <xs:attribute name="AvailableOffline"  
                        type="xs:boolean"  
                        use="optional" />  
          <xs:attribute name="Icon"  
                        type="xs:string"  
                        use="optional" />  
          <xs:attribute name="Sequence"  
                        type="xs:nonNegativeInteger"  
                        use="optional" />  
          <xs:attribute name="Show"  
                        type="xs:boolean"  
                        use="optional" />  
          <xs:attribute name="ViewId"  
                        type="FormISVGuid"  
                        use="optional" />  
  
        </xs:complexType>  
      </xs:element>  
    </xs:choice>  
    <xs:attribute name="ValidForCreate"  
                  type="FormCRM_Boolean"  
                  use="optional" />  
    <xs:attribute name="ValidForUpdate"  
                  type="FormCRM_Boolean"  
                  use="optional" />  
  
  </xs:complexType>  
  <xs:complexType name="FormNavigationType">  
    <xs:all>  
      <xs:element name="NavBarAreas"  
                  type="FormNavBarAreasType"  
                  minOccurs="0"  
                  maxOccurs="1" />  
      <xs:element name="NavBar"  
                  type="FormNavBarType"  
                  minOccurs="0"  
                  maxOccurs="1" />  
    </xs:all>  
  
  </xs:complexType>  
  <xs:complexType name ="FormParametersType">  
    <xs:choice minOccurs="1"  
               maxOccurs ="100000">  
      <xs:element name ="querystringparameter"  
                  type="FormQueryStringParameterType"  
                  minOccurs ="0"  
                  maxOccurs ="1" />  
    </xs:choice>  
  
  </xs:complexType>  
  <xs:complexType name="FormQueryStringParameterType">  
    <xs:attribute name="name"  
                  type="FormQueryStringParameterNameAttributeType"  
                  use="required" />  
    <xs:attribute name="type"  
                  type="FormParameterAttributeType"  
                  use="required" />  
  
  </xs:complexType>  
  <xs:complexType name="FormType">  
    <xs:all>  
      <xs:element name="ancestor"  
                  minOccurs="0"  
                  maxOccurs="1">  
        <xs:complexType>  
          <xs:attribute name="id"  
                        type="FormGuidType"  
                        use="required" />  
        </xs:complexType>  
      </xs:element>  
      <xs:element name="hiddencontrols"  
                  minOccurs="0"  
                  maxOccurs="1">  
        <xs:complexType>  
          <xs:sequence>  
            <xs:element name="data"  
                        minOccurs="0"  
                        maxOccurs="unbounded">  
              <xs:complexType>  
                <xs:attribute name="id"  
                              type="xs:string" />  
                <xs:attribute name="datafieldname"  
                              type="xs:string" />  
                <xs:attribute name="classid"  
                              type="FormGuidType" />  
                <xs:attribute name="relationship"  
                              type="xs:string" />  
  
              </xs:complexType>  
            </xs:element>  
          </xs:sequence>  
  
        </xs:complexType>  
      </xs:element>  
      <xs:element name="controlDescriptions"  
                  minOccurs="0"  
                  maxOccurs="1">  
        <xs:complexType>  
          <xs:sequence>  
            <xs:element name="controlDescription"  
                        minOccurs="0"  
                        maxOccurs="unbounded">  
              <xs:complexType>  
                <xs:sequence>  
                  <xs:element name="customControl"  
                              minOccurs="0"  
                              maxOccurs="unbounded">  
                    <xs:complexType>  
                      <xs:sequence>  
                        <xs:element name="parameters"  
                                    minOccurs="0"  
                                    maxOccurs="1">  
                          <xs:complexType>  
                            <xs:sequence>  
                              <xs:any minOccurs="0"  
                                      maxOccurs="unbounded"  
                                      processContents="skip"></xs:any>  
                            </xs:sequence>  
                          </xs:complexType>  
                        </xs:element>  
                      </xs:sequence>  
                      <xs:attribute name="id"  
                                    type="FormGuidType"  
                                    use="required" />  
                      <xs:attribute name="formFactor"  
                                    type="xs:integer"  
                                    use="optional" />  
                      <xs:attribute name="name"  
                                    type="xs:string"  
                                    use="optional" />  
                      <xs:attribute name="version"  
                                    type="xs:string"  
                                    use="optional" />  
  
                    </xs:complexType>  
                  </xs:element>  
                </xs:sequence>  
                <xs:attribute name="forControl"  
                              type="xs:string"  
                              use="required" />  
  
              </xs:complexType>  
            </xs:element>  
          </xs:sequence>  
  
        </xs:complexType>  
      </xs:element>  
      <xs:element name="tabs"  
                  minOccurs="1"  
                  maxOccurs="1">  
        <xs:complexType>  
          <xs:sequence>  
            <xs:element name="tab"  
                        minOccurs="1"  
                        maxOccurs="100">  
              <xs:complexType>  
                <xs:all>  
                  <xs:element name="labels"  
                              type="FormXmlLabelsType"  
                              minOccurs="0"  
                              maxOccurs="1" />  
                  <xs:element name="tabheader"  
                              type="FormXmlHeaderFooterType"  
                              minOccurs="0"  
                              maxOccurs="1"/>  
                  <xs:element name="tabfooter"  
                              type="FormXmlHeaderFooterType"  
                              minOccurs="0"  
                              maxOccurs="1"/>  
                  <xs:element name="columns"  
                              minOccurs="1"  
                              maxOccurs="1">  
                    <xs:complexType>  
                      <xs:sequence>  
                        <xs:element name="column"  
                                    minOccurs="1"  
                                    maxOccurs="3">  
                          <xs:complexType>  
                            <xs:sequence>  
                              <xs:element name="sections"  
                                          minOccurs="0"  
                                          maxOccurs="1">  
                                <xs:complexType>  
                                  <xs:sequence>  
                                    <xs:element name="section"  
                                                minOccurs="0"  
                                                maxOccurs="unbounded">  
                                      <xs:complexType>  
                                        <xs:all>  
                                          <xs:element name="labels"  
                                                      type="FormXmlLabelsType"  
                                                      minOccurs="0"  
                                                      maxOccurs="1" />  
                                          <xs:element name="rows"  
                                                      minOccurs="0"  
                                                      maxOccurs="1">  
                                            <xs:complexType>  
                                              <xs:sequence>  
                                                <xs:element name="row"  
                                                            minOccurs="0"  
                                                            maxOccurs="unbounded">  
                                                  <xs:complexType>  
                                                    <xs:sequence>  
                                                      <xs:element name="cell"  
                                                                  minOccurs="0"  
                                                                  maxOccurs="unbounded">  
                                                        <xs:complexType>  
                                                          <xs:all>  
                                                            <xs:element name="labels"  
                                                                        type="FormXmlLabelsType"  
                                                                        minOccurs="0"  
                                                                        maxOccurs="1" />  
                                                            <xs:element name="control"  
                                                                        type="FormXmlControlType"  
                                                                        minOccurs="0"  
                                                                        maxOccurs="1" />  
                                                            <xs:element name="events"  
                                                                        type="FormXmlEventsType"  
                                                                        minOccurs="0"  
                                                                        maxOccurs="1" />  
                                                          </xs:all>  
                                                          <xs:attribute name="auto"  
                                                                        type="xs:boolean" />  
                                                          <xs:attribute name="addedby"  
                                                                        type="xs:string" />  
                                                          <xs:attributeGroup ref="FormXmlCellCommon"/>  
                                                        </xs:complexType>  
                                                      </xs:element>  
                                                    </xs:sequence>  
                                                    <xs:attribute name="addedby"  
                                                                  type="xs:string" />  
                                                    <xs:attributeGroup ref="FormXmlRowCommon"/>  
                                                  </xs:complexType>  
                                                </xs:element>  
                                              </xs:sequence>  
                                              <xs:attribute name="addedby"  
                                                            type="xs:string" />  
  
                                            </xs:complexType>  
                                          </xs:element>  
                                        </xs:all>  
                                        <xs:attribute name="group"  
                                                      type="xs:string" />  
                                        <xs:attribute name="name"  
                                                      type="xs:string" />  
                                        <xs:attribute name="showlabel"  
                                                      type="xs:boolean" />  
                                        <xs:attribute name="labelid"  
                                                      type="FormGuidType"  
                                                      use="optional" />  
                                        <xs:attribute name="showbar"  
                                                      type="xs:boolean" />  
                                        <xs:attribute name="id"  
                                                      type="FormGuidType" />  
                                        <xs:attribute name="IsUserDefined"  
                                                      type="xs:string" />  
                                        <xs:attribute name="height"  
                                                      type="xs:string" />  
                                        <xs:attribute name="locklevel"  
                                                      type="xs:nonNegativeInteger" />  
                                        <xs:attribute name="layout"  
                                                      type="xs:string" />  
                                        <xs:attribute name="addedby"  
                                                      type="xs:string" />  
                                        <xs:attribute name="visible"  
                                                      type="xs:boolean" />  
                                        <xs:attribute name="availableforphone"  
                                                      type="xs:boolean" />  
                                        <xs:attribute name="rowheight"  
                                                      type="xs:nonNegativeInteger"  
                                                      use="optional" />  
                                        <xs:attribute name="autoexpand"  
                                                      type="xs:boolean"  
                                                      use="optional" />  
                                        <xs:attributeGroup ref="FormXmlSectionCommon"/>  
  
                                      </xs:complexType>  
                                    </xs:element>  
                                  </xs:sequence>  
                                  <xs:attribute name="addedby"  
                                                type="xs:string" />  
  
                                </xs:complexType>  
                              </xs:element>  
                            </xs:sequence>  
                            <xs:attribute name="width"  
                                          type="FormPercentageType"  
                                          use="required" />  
  
                          </xs:complexType>  
                        </xs:element>  
                      </xs:sequence>  
  
                    </xs:complexType>  
                  </xs:element>  
                  <xs:element name="events"  
                              type="FormXmlEventsType"  
                              minOccurs="0"  
                              maxOccurs="1" />  
                </xs:all>  
                <xs:attribute name="group"  
                              type="xs:string" />  
                <xs:attribute name="name"  
                              type="xs:string" />  
                <xs:attribute name="verticallayout"  
                              type="xs:boolean" />  
                <xs:attribute name="showlabel"  
                              type="xs:boolean" />  
                <xs:attribute name="labelid"  
                              type="FormGuidType"  
                              use="optional" />  
                <xs:attribute name="id"  
                              type="FormGuidType" />  
                <xs:attribute name="IsUserDefined"  
                              type="xs:string" />  
                <xs:attribute name="locklevel"  
                              type="xs:nonNegativeInteger" />  
                <xs:attribute name="addedby"  
                              type="xs:string" />  
                <xs:attribute name="expanded"  
                              type="xs:boolean" />  
                <xs:attribute name="visible"  
                              type="xs:boolean" />  
                <xs:attribute name="availableforphone"  
                              type="xs:boolean" />  
                <xs:attribute name="collapsible"  
                              type="xs:boolean" />  
  
              </xs:complexType>  
            </xs:element>  
          </xs:sequence>  
          <xs:attribute name="showlabels"  
                        type="xs:boolean" />  
          <xs:attribute name="addedby"  
                        type="xs:string" />  
          <xs:attribute name="filterby"  
                        type="xs:string" />  
          <xs:attribute name="dashboardCategory"  
                        type="xs:string" />  
          <xs:attribute name="timeframe"  
                        type="xs:string" />  
          <xs:attribute name="primaryentitylogicalname"  
                        type="xs:string" />  
          <xs:attribute name="entityview"  
                        type="xs:string" />  
          <xs:attribute name="tilespresent"  
                        type="xs:boolean" />  
  
        </xs:complexType>  
      </xs:element>  
      <xs:element name="header"  
                  type="FormXmlHeaderFooterType"  
                  minOccurs="0"  
                  maxOccurs="1"/>  
      <xs:element name="footer"  
                  type="FormXmlHeaderFooterType"  
                  minOccurs="0"  
                  maxOccurs="1"/>  
      <xs:element name="events"  
                  type="FormXmlEventsType"  
                  minOccurs="0"  
                  maxOccurs="1" />  
      <xs:element name="formLibraries"  
                  type="FormXmlLibraryType"  
                  minOccurs="0"  
                  maxOccurs="1" />  
      <xs:element name="externaldependencies"  
                  type="FormXmlExternalDependenciesType"  
                  minOccurs="0"  
                  maxOccurs="1" />  
      <xs:element name="formparameters"  
                  type="FormParametersType"  
                  minOccurs="0"  
                  maxOccurs="1">  
        <xs:unique name="UniqueName">  
          <xs:selector xpath ="./querystringparameter"/>  
          <xs:field xpath ="@name"/>  
        </xs:unique>  
      </xs:element>  
      <xs:element name ="clientresources"  
                  type ="ClientResourcesType"  
                  minOccurs ="0"  
                  maxOccurs ="1"></xs:element>  
      <xs:element name="Navigation"  
                  type="FormNavigationType"  
                  minOccurs="0"  
                  maxOccurs="1"/>  
      <xs:element name="DisplayConditions"  
                  type="FormDisplayConditionsType"  
                  minOccurs="0"  
                  maxOccurs="1" />  
      <xs:element name="RibbonDiffXml"  
                  type="RibbonEntityDiffXmlType"  
                  minOccurs="0"  
                  maxOccurs="1" />  
    </xs:all>  
    <xs:attribute name="enablerelatedinformation"  
                  type="xs:boolean" />  
    <xs:attribute name="relatedInformationCollapsed"  
                  type="xs:boolean" />  
    <xs:attribute name="hasmargin"  
                  type="xs:boolean" />  
    <xs:attribute name="addedby"  
                  type="xs:string" />  
    <xs:attribute name="shownavigationbar"  
                  type="xs:boolean" />  
    <xs:attribute name="showImage"  
                  type="xs:boolean" />  
    <xs:attribute name="maxWidth"  
                  use="optional">  
      <xs:simpleType>  
        <xs:restriction base="xs:positiveInteger">  
          <xs:minInclusive value="400" />  
        </xs:restriction>  
      </xs:simpleType>  
    </xs:attribute>  
  
  </xs:complexType>  
  <xs:complexType name="FormXmlControlType">  
    <xs:sequence>  
      <xs:element name="labels"  
                  type="FormXmlLabelsType"  
                  minOccurs="0"  
                  maxOccurs="1" />  
      <xs:element name="parameters"  
                  minOccurs="0"  
                  maxOccurs="1">  
        <xs:complexType>  
          <xs:choice minOccurs="1"  
                     maxOccurs="1">  
            <!-- LATER: (TobinZ, 2008-07-24) - Divide this list up into sets that are valid together. -->  
            <xs:choice minOccurs="1"  
                       maxOccurs="unbounded">  
              <xs:element name="Url"  
                          type="xs:string"  
                          minOccurs="0"  
                          maxOccurs="1" />  
              <xs:element name="PassParameters"  
                          type="xs:boolean"  
                          minOccurs="0"  
                          maxOccurs="1" />  
              <xs:element name="Security"  
                          type="xs:boolean"  
                          minOccurs="0"  
                          maxOccurs="1" />  
              <xs:element name="Scrolling"  
                          type="xs:string"  
                          minOccurs="0"  
                          maxOccurs="1" />  
              <xs:element name="Border"  
                          type="xs:string"  
                          minOccurs="0"  
                          maxOccurs="1" />  
              <xs:element name="Preload"  
                          type="xs:string"  
                          minOccurs="0"  
                          maxOccurs="1" />  
              <xs:element name="IsPassword"  
                          type="xs:boolean"  
                          minOccurs="0"  
                          maxOccurs="1" />  
              <xs:element name="IsColorValue"  
                          type="xs:boolean"  
                          minOccurs="0"  
                          maxOccurs="1" />  
              <!--Web Resource related parameters. Included in this section since they   
								can include Url, PassParameters etc-->  
              <xs:element name="Height"  
                          type="xs:unsignedInt"  
                          minOccurs="0"  
                          maxOccurs="1"/>  
              <xs:element name="Width"  
                          type="xs:unsignedInt"  
                          minOccurs="0"  
                          maxOccurs="1"/>  
              <xs:element name="AltText"  
                          type="xs:string"  
                          minOccurs="0"  
                          maxOccurs="1"/>  
              <xs:element name="SizeType"  
                          type="WebResourceSizeType"  
                          minOccurs="0"  
                          maxOccurs="1"/>  
              <xs:element name="ShowInROF"  
                          type="xs:boolean"  
                          minOccurs="0"  
                          maxOccurs="1" />  
              <xs:element name="ShowOnMobileClient"  
                          type="xs:boolean"  
                          minOccurs="0"  
                          maxOccurs="1" />  
              <xs:element name="HorizontalAlignment"  
                          type="ImageHorizontalAlignmentType"  
                          minOccurs="0"  
                          maxOccurs="1"/>  
              <xs:element name="VerticalAlignment"  
                          type="ImageVerticalAlignmentType"  
                          minOccurs="0"  
                          maxOccurs="1"/>  
              <xs:element name="Data"  
                          type="xs:string"  
                          minOccurs="0"  
                          maxOccurs="1" />  
              <xs:element name="WebResourceId"  
                          type="xs:string"  
                          minOccurs="0"  
                          maxOccurs="1" />  
              <!--Parameters for Rich Editor Control-->  
              <xs:element name="ReadOnly"  
                          type="xs:boolean"  
                          minOccurs="0"  
                          maxOccurs="1" />  
              <xs:element name="ShowDialogs"  
                          type="xs:boolean"  
                          minOccurs="0"  
                          maxOccurs="1" />  
              <xs:element name="IsViewExpandable"  
                          type="xs:boolean"  
                          minOccurs="0"  
                          maxOccurs="1" />  
              <xs:element name="HideToolbar"  
                          type="xs:boolean"  
                          minOccurs="0"  
                          maxOccurs="1" />  
              <xs:element name="ToolbarJSON"  
                          type="xs:string"  
                          minOccurs="0"  
                          maxOccurs="1" />  
              <xs:element name="ExpandedToolbarJSON"  
                          type="xs:string"  
                          minOccurs="0"  
                          maxOccurs="1" />  
              <xs:element name="HiddenToolbarJSON"  
                          type="xs:string"  
                          minOccurs="0"  
                          maxOccurs="1" />  
              <xs:element name="ClassName"  
                          type="xs:string"  
                          minOccurs="0"  
                          maxOccurs="1" />  
            </xs:choice>  
            <!--Parameters for unbound lookup control-->  
            <xs:choice minOccurs="1"  
                       maxOccurs="unbounded">  
              <xs:element name="TargetEntities"  
                          minOccurs="0"  
                          maxOccurs="1">  
                <xs:complexType>  
                  <xs:sequence>  
                    <xs:element name="TargetEntity"  
                                minOccurs="1"  
                                maxOccurs="unbounded">  
                      <xs:complexType>  
                        <xs:all>  
                          <xs:element name="EntityLogicalName"  
                                      type="xs:string"  
                                      minOccurs="1"  
                                      maxOccurs="1" />  
                          <xs:element name="DefaultViewId"  
                                      type="FormGuidType"  
                                      minOccurs="0"  
                                      maxOccurs="1" />  
                          <xs:element name="IsDeDupLookup"  
                                      type="xs:boolean"  
                                      minOccurs="0"  
                                      maxOccurs="1" />  
                          <xs:element name="UnboundLookupStyle"  
                                      type="xs:string"  
                                      minOccurs="0"  
                                      maxOccurs="1" />  
                        </xs:all>  
                      </xs:complexType>  
                    </xs:element>  
                  </xs:sequence>  
                </xs:complexType>  
              </xs:element>  
            </xs:choice>  
            <!-- Parameters for the subgrid control and and reference panel subgrid control -->  
            <xs:choice minOccurs="1"  
                       maxOccurs="unbounded">  
              <xs:element name="ViewId"  
                          type="FormGuidType"  
                          minOccurs="0"  
                          maxOccurs="1" />  
              <xs:element name="IsUserView"  
                          type="xs:boolean"  
                          minOccurs="0"  
                          maxOccurs="1" />  
              <xs:element name="IsUserChart"  
                          type="xs:boolean"  
                          minOccurs="0"  
                          maxOccurs="1" />  
              <xs:element name="RelationshipName"  
                          type="xs:string"  
                          minOccurs="0"  
                          maxOccurs="1" />  
              <xs:element name="RelationshipRoleOrdinal"  
                          type="RelationshipRoleOrdinalType"  
                          minOccurs="0"  
                          maxOccurs="1" />  
              <xs:element name="TargetEntityType"  
                          type="xs:string"  
                          minOccurs="1"  
                          maxOccurs="1" />  
              <xs:element name="AutoExpand"  
                          type="GridResizeType"  
                          minOccurs="0"  
                          maxOccurs="1" />  
              <xs:element name="RecordsPerPage"  
                          type="xs:unsignedShort"  
                          minOccurs="0"  
                          maxOccurs="1" />  
              <xs:element name="MaxRowsBeforeScroll"  
                          type="xs:integer"  
                          minOccurs="0"  
                          maxOccurs="1" />  
              <xs:element name="EnableQuickFind"  
                          type="xs:boolean"  
                          minOccurs="0"  
                          maxOccurs="1" />  
              <xs:element name="EnableJumpBar"  
                          type="xs:boolean"  
                          minOccurs="0"  
                          maxOccurs="1" />  
              <xs:element name="EnableViewPicker"  
                          type="xs:boolean"  
                          minOccurs="0"  
                          maxOccurs="1" />  
              <xs:element name="ViewIds"  
                          type="xs:string"  
                          minOccurs="0"  
                          maxOccurs="1" />  
              <xs:element name="ChartGridMode"  
                          type="xs:string"  
                          minOccurs="0"  
                          maxOccurs="1" />  
              <xs:element name="VisualizationId"  
                          type="xs:string"  
                          minOccurs="0"  
                          maxOccurs="1" />  
              <xs:element name="EnableChartPicker"  
                          type="xs:boolean"  
                          minOccurs="0"  
                          maxOccurs="1" />  
              <xs:element name="EnableContextualActions"  
                          type="xs:boolean"  
                          minOccurs="0"  
                          maxOccurs="1" />  
              <xs:element name="TeamTemplateId"  
                          type="FormGuidType"  
                          minOccurs="0"  
                          maxOccurs="1" />  
              <xs:element name="GridUIMode"  
                          type="xs:string"  
                          minOccurs="0"  
                          maxOccurs="1" />  
              <xs:element name="ReferencePanelSubgridIconUrl"  
                          type="xs:string"  
                          minOccurs="0"  
                          maxOccurs="1" />  
            </xs:choice>  
            <!-- Parameters for Power BI Tile control -->  
            <xs:choice minOccurs="1"  
                       maxOccurs="unbounded">  
              <xs:element name="PowerBIDashboardId"  
                          type="xs:string"  
                          minOccurs="0"  
                          maxOccurs="1" />  
              <xs:element name="TileId"  
                          type="xs:string"  
                          minOccurs="0"  
                          maxOccurs="1" />  
              <xs:element name="TileUrl"  
                          type="xs:string"  
                          minOccurs="0"  
                          maxOccurs="1" />  
            </xs:choice>  
            <!-- Parameters for the lookup control -->  
            <xs:choice minOccurs="1"  
                       maxOccurs="unbounded">  
              <xs:element name="DefaultViewId"  
                          type="FormGuidType"  
                          minOccurs="0"  
                          maxOccurs="1" />  
              <xs:element name="FilterRelationshipName"  
                          type="xs:string"  
                          minOccurs="0"  
                          maxOccurs="1" />  
              <xs:element name="DependentAttributeName"  
                          type="xs:string"  
                          minOccurs="0"  
                          maxOccurs="1" />  
              <xs:element name="DependentAttributeType"  
                          type="xs:string"  
                          minOccurs="0"  
                          maxOccurs="1" />  
              <xs:element name="AutoResolve"  
                          type="xs:boolean"  
                          minOccurs="0"  
                          maxOccurs="1" />  
              <xs:element name="ResolveEmailAddress"  
                          type="xs:boolean"  
                          minOccurs="0"  
                          maxOccurs="1" />  
              <xs:element name="DefaultViewReadOnly"  
                          type="xs:boolean"  
                          minOccurs="0"  
                          maxOccurs="1" />  
              <xs:element name="ViewPickerReadOnly"  
                          type="xs:boolean"  
                          minOccurs="0"  
                          maxOccurs="1" />  
              <xs:element name="AllowFilterOff"  
                          type="xs:boolean"  
                          minOccurs="0"  
                          maxOccurs="1" />  
              <xs:element name="DisableMru"  
                          type="xs:boolean"  
                          minOccurs="0"  
                          maxOccurs="1" />  
              <xs:element name="DisableQuickFind"  
                          type="xs:boolean"  
                          minOccurs="0"  
                          maxOccurs="1" />  
              <xs:element name="DisableViewPicker"  
                          type="xs:boolean"  
                          minOccurs="0"  
                          maxOccurs="1" />  
              <xs:element name="AvailableViewIds"  
                          type="xs:string"  
                          minOccurs="0"  
                          maxOccurs="1" />  
              <xs:element name="EntityLogicalName"  
                          type="xs:string"  
                          minOccurs="0"  
                          maxOccurs="1" />  
              <xs:element name="IsInlineNewEnabled"  
                          type="xs:boolean"  
                          minOccurs="0"  
                          maxOccurs="1" />  
              <xs:element name="InlineViewIds"  
                          type="xs:string"  
                          minOccurs="0"  
                          maxOccurs="1" />  
              <xs:element name="UnboundLookupTypes"  
                          type="xs:string"  
                          minOccurs="0"  
                          maxOccurs="1" />  
              <xs:element name="UnboundLookupBrowse"  
                          type="xs:boolean"  
                          minOccurs="0"  
                          maxOccurs="1" />  
              <xs:element name="UnboundLookupControlType"  
                          type="xs:string"  
                          minOccurs="0"  
                          maxOccurs="1" />  
              <xs:element name="ShowAsBreadcrumbControl"  
                          type="xs:boolean"  
                          minOccurs="0"  
                          maxOccurs="1" />  
            </xs:choice>  
            <!-- Parameters for the TextBox -->  
            <xs:choice minOccurs="1"  
                       maxOccurs="unbounded">  
              <xs:element name="MaxLength"  
                          type="xs:integer"  
                          minOccurs="0"  
                          maxOccurs="1" />  
              <xs:element name="Format"  
                          type="FormatType"  
                          minOccurs="0"  
                          maxOccurs="1" />  
            </xs:choice>  
            <!-- Parameters for the Label -->  
            <xs:choice minOccurs="1"  
                       maxOccurs="unbounded">  
              <xs:element name="IsTitle"  
                          type="xs:boolean"  
                          minOccurs="0"  
                          maxOccurs="1" />  
            </xs:choice>  
            <!-- Parameters for the Numbers (i.e Whole, Decimal, Currency)-->  
            <xs:choice minOccurs="1"  
                       maxOccurs="unbounded">  
              <xs:element name="MinValue"  
                          type="xs:double"  
                          minOccurs="0"  
                          maxOccurs="1" />  
              <xs:element name="MaxValue"  
                          type="xs:double"  
                          minOccurs="0"  
                          maxOccurs="1" />  
              <xs:element name="Precision"  
                          type="xs:integer"  
                          minOccurs="0"  
                          maxOccurs="1" />  
            </xs:choice>  
            <!-- Parameters for the PickList Control and Two Value Option(Radio) Control -->  
            <xs:choice minOccurs="1"  
                       maxOccurs="unbounded">  
              <xs:element name="DefaultValue"  
                          type="xs:string"  
                          minOccurs="0"  
                          maxOccurs="1" />  
              <xs:element name="OptionSetId"  
                          type="FormGuidType"  
                          minOccurs="0"  
                          maxOccurs="1" />  
            </xs:choice>  
            <!-- Parameters for the quickformcollection control and reference panel quick form collection control -->  
            <xs:choice minOccurs="1"  
                       maxOccurs="unbounded">  
              <xs:element name="QuickForms"  
                          type="xs:string"  
                          minOccurs="1"  
                          maxOccurs="1" />  
              <xs:element name="ControlMode"  
                          type="xs:string"  
                          minOccurs="0"  
                          maxOccurs="1" />  
              <xs:element name="ReferencePanelQuickFormCollectionIconUrl"  
                          type="xs:string"  
                          minOccurs="0"  
                          maxOccurs="1" />  
              <xs:element name="DisplayAsCustomer360Tile"  
                          type="xs:boolean"  
                          minOccurs="0"  
                          maxOccurs="1" />  
            </xs:choice>  
            <!-- Parameters for the tabs control -->  
            <xs:choice minOccurs="1"  
                       maxOccurs="unbounded">  
              <xs:element name="DefaultTabId"  
                          type="xs:string"  
                          minOccurs="0"  
                          maxOccurs="1" />  
              <xs:element name="ShowArticleTab"  
                          type="xs:boolean"  
                          minOccurs="0"  
                          maxOccurs="1" />  
              <xs:group ref="SearchWidgetControlParameters"  
                        minOccurs="0"  
                        maxOccurs="unbounded" />  
            </xs:choice>  
            <!-- Link Control parameters -->  
            <xs:choice minOccurs="1"  
                       maxOccurs="unbounded">  
              <xs:element name="LinkControlDefinitionId"  
                          type="FormGuidType"  
                          minOccurs="0"  
                          maxOccurs="1" />  
              <xs:element name="ShowLinkControlLabel"  
                          type="xs:boolean"  
                          minOccurs="0"  
                          maxOccurs="1" />  
            </xs:choice>  
            <!-- Bing Maps Control parameters -->  
            <xs:choice minOccurs="1"  
                       maxOccurs="unbounded">  
              <xs:element name="AddressField"  
                          type="xs:string"  
                          minOccurs="1"  
                          maxOccurs="1" />  
            </xs:choice>  
            <!-- Timer Control parameters -->  
            <xs:choice minOccurs="1"  
                       maxOccurs="unbounded">  
              <xs:element name="FailureTimeField"  
                          type="xs:string"  
                          minOccurs="1"  
                          maxOccurs="1" />  
              <xs:element name="SuccessConditionName"  
                          type="xs:string"  
                          minOccurs="1"  
                          maxOccurs="1" />  
              <xs:element name="SuccessConditionValue"  
                          type="xs:string"  
                          minOccurs="1"  
                          maxOccurs="1" />  
              <xs:element name="FailureConditionName"  
                          type="xs:string"  
                          minOccurs="0"  
                          maxOccurs="1" />  
              <xs:element name="FailureConditionValue"  
                          type="xs:string"  
                          minOccurs="0"  
                          maxOccurs="1" />  
              <xs:element name="WarningConditionName"  
                          type="xs:string"  
                          minOccurs="0"  
                          maxOccurs="1" />  
              <xs:element name="WarningConditionValue"  
                          type="xs:string"  
                          minOccurs="0"  
                          maxOccurs="1" />  
              <xs:element name="CancelConditionName"  
                          type="xs:string"  
                          minOccurs="0"  
                          maxOccurs="1" />  
              <xs:element name="CancelConditionValue"  
                          type="xs:string"  
                          minOccurs="0"  
                          maxOccurs="1" />  
              <xs:element name="PauseConditionName"  
                          type="xs:string"  
                          minOccurs="0"  
                          maxOccurs="1" />  
              <xs:element name="PauseConditionValue"  
                          type="xs:string"  
                          minOccurs="0"  
                          maxOccurs="1" />  
            </xs:choice>  
            <!-- Search Widget parameters -->  
            <xs:choice minOccurs="1"  
                       maxOccurs="unbounded">  
              <xs:group ref="SearchWidgetControlParameters"  
                        minOccurs="0"  
                        maxOccurs="unbounded" />  
            </xs:choice>  
            <!-- Queue Control parameters -->  
            <xs:choice minOccurs="1"  
                       maxOccurs="unbounded">  
              <xs:element name="StreamObjects"  
                          minOccurs="1"  
                          maxOccurs="1" >  
                <xs:complexType>  
                  <xs:sequence>  
                    <xs:element name="ShowAsTiles"  
                                type="xs:boolean"  
                                minOccurs="1"  
                                maxOccurs="1" />  
                    <xs:element name="StreamObject"  
                                minOccurs="1"  
                                maxOccurs="unbounded" >  
                      <xs:complexType>  
                        <xs:sequence>  
                          <xs:element name="LogicalEntityName"  
                                      type="xs:string"  
                                      minOccurs="1"  
                                      maxOccurs="1" />  
                          <xs:choice minOccurs="1"  
                                     maxOccurs="1">  
                            <!-- Parameters for stream objects of type queue -->  
                            <xs:choice minOccurs="1"  
                                       maxOccurs="unbounded">  
                              <xs:element name="QueueId"  
                                          type="FormGuidType"  
                                          minOccurs="1"  
                                          maxOccurs="1" />  
                              <xs:element name="QueueViewId"  
                                          type="FormGuidType"  
                                          minOccurs="1"  
                                          maxOccurs="1" />  
                            </xs:choice>  
                            <!-- Parameters for stream objects of type entity view -->  
                            <xs:choice minOccurs="1"  
                                       maxOccurs="unbounded">  
                              <xs:element name="EntityViewId"  
                                          type="FormGuidType"  
                                          minOccurs="1"  
                                          maxOccurs="1" />  
                            </xs:choice>  
                            <!-- Parameters for stream objects of type saved query on queue -->  
                            <xs:choice minOccurs="1"  
                                       maxOccurs="unbounded">  
                              <xs:element name="SavedQueryID"  
                                          type="FormGuidType"  
                                          minOccurs="1"  
                                          maxOccurs="1" />  
                              <xs:element name="QueueViewIdForSavedQuery"  
                                          type="FormGuidType"  
                                          minOccurs="1"  
                                          maxOccurs="1" />  
                            </xs:choice>  
                          </xs:choice>  
                        </xs:sequence>  
                        <xs:attribute name="type"  
                                      type="xs:nonNegativeInteger"  
                                      use="required" />  
                        <xs:attribute name="id"  
                                      type="FormGuidType"  
                                      use="required" />  
  
                      </xs:complexType>  
                    </xs:element>  
                  </xs:sequence>  
  
                </xs:complexType>  
              </xs:element>  
            </xs:choice>  
            <!-- Date Range Control parameters -->  
            <xs:choice minOccurs="1"  
                       maxOccurs="unbounded">  
              <xs:element name="AttributeLogicalName"  
                          type="xs:string"  
                          minOccurs="0"  
                          maxOccurs="1" />  
              <xs:element name="TimeFrame"  
                          type="xs:string"  
                          minOccurs="0"  
                          maxOccurs="1" />  
            </xs:choice>  
          </xs:choice>  
  
        </xs:complexType>  
      </xs:element>  
    </xs:sequence>  
    <xs:attribute name="id"  
                  type="xs:string" />  
    <xs:attribute name="uniqueid"  
                  type="FormGuidType" />  
    <xs:attribute name="classid"  
                  type="FormGuidType" />  
    <xs:attribute name="labelid"  
                  type="FormGuidType" />  
    <xs:attribute name="datafieldname"  
                  type="xs:string" />  
    <xs:attribute name="disabled"  
                  type="xs:boolean" />  
    <xs:attribute name="addedby"  
                  type="xs:string" />  
    <xs:attribute name="isunbound"  
                  type="xs:boolean" />  
    <xs:attribute name="isrequired"  
                  type="xs:boolean" />  
    <xs:attribute name="relationship"  
                  type="xs:string" />  
    <xs:attribute name="indicationOfSubgrid"  
                  type="xs:boolean" />  
  
  </xs:complexType>  
  <xs:complexType name="FormXmlLibraryType">  
    <xs:sequence>  
      <xs:element name="Library"  
                  minOccurs="1"  
                  maxOccurs="50">  
        <xs:complexType>  
          <xs:attribute name="name"  
                        type="xs:string"  
                        use="required" />  
          <xs:attribute name="libraryUniqueId"  
                        type="xs:string"  
                        use="required" />  
  
        </xs:complexType>  
      </xs:element>  
    </xs:sequence>  
  
  </xs:complexType>  
  <xs:simpleType name="CrmEventType">  
    <xs:restriction base="xs:string">  
      <xs:enumeration value="DataEvent" />  
      <xs:enumeration value="ControlEvent" />  
    </xs:restriction>  
  </xs:simpleType>  
  <xs:complexType name="FormXmlHandlerType">  
    <xs:sequence>  
      <xs:element name="dependencies"  
                  minOccurs="0"  
                  maxOccurs="1">  
        <xs:complexType>  
          <xs:sequence>  
            <xs:element name="dependency"  
                        minOccurs="0"  
                        maxOccurs="unbounded">  
              <xs:complexType>  
                <xs:attribute name="id"  
                              type="xs:string" />  
  
              </xs:complexType>  
            </xs:element>  
          </xs:sequence>  
  
        </xs:complexType>  
      </xs:element>  
    </xs:sequence>  
    <xs:attribute name="functionName"  
                  type="xs:string"  
                  use="required" />  
    <xs:attribute name="libraryName"  
                  type="xs:string"  
                  use="required" />  
    <xs:attribute name="handlerUniqueId"  
                  type="xs:string"  
                  use="required" />  
    <xs:attribute name="enabled"  
                  type="xs:boolean" />  
    <xs:attribute name="passExecutionContext"  
                  type="xs:boolean" />  
    <xs:attribute name="parameters"  
                  type="xs:string" />  
  
  </xs:complexType>  
  <xs:complexType name="FormXmlEventsType">  
    <xs:sequence>  
      <xs:element name="event"  
                  minOccurs="1"  
                  maxOccurs="unbounded">  
        <xs:complexType>  
          <xs:all>  
            <xs:element name="Handlers"  
                        minOccurs="0"  
                        maxOccurs="1">  
              <xs:complexType>  
                <xs:sequence>  
                  <xs:element name="Handler"  
                              type="FormXmlHandlerType"  
                              minOccurs="0"  
                              maxOccurs="50" />  
                </xs:sequence>  
  
              </xs:complexType>  
            </xs:element>  
            <xs:element name="InternalHandlers"  
                        minOccurs="0"  
                        maxOccurs="1">  
              <xs:complexType>  
                <xs:sequence>  
                  <xs:element name="Handler"  
                              type="FormXmlHandlerType"  
                              minOccurs="0"  
                              maxOccurs="50" />  
                </xs:sequence>  
  
              </xs:complexType>  
            </xs:element>  
            <xs:element name="dependencies"  
                        minOccurs="0"  
                        maxOccurs="1">  
              <xs:complexType>  
                <xs:sequence>  
                  <xs:element name="dependency"  
                              minOccurs="0"  
                              maxOccurs="unbounded">  
                    <xs:complexType>  
                      <xs:attribute name="id"  
                                    type="xs:string" />  
  
                    </xs:complexType>  
                  </xs:element>  
                </xs:sequence>  
  
              </xs:complexType>  
            </xs:element>  
          </xs:all>  
          <xs:attribute name="name"  
                        type="xs:string" />  
          <xs:attribute name="BehaviorInBulkEditForm"  
                        type="BehaviorInBulkEditForm" />  
          <xs:attribute name="application"  
                        type="xs:boolean" />  
          <xs:attribute name="active"  
                        type="xs:boolean" />  
          <xs:attribute name="eventType"  
                        type="CrmEventType" />  
          <xs:attribute name="attribute"  
                        type="xs:string" />  
  
        </xs:complexType>  
      </xs:element>  
    </xs:sequence>  
  
  </xs:complexType>  
  <xs:complexType name="FormXmlExternalDependenciesType">  
    <xs:sequence>  
      <xs:element name="dependency"  
                  minOccurs="1"  
                  maxOccurs="unbounded">  
        <xs:complexType>  
          <xs:attribute name="id"  
                        type="xs:string" />  
  
        </xs:complexType>  
      </xs:element>  
    </xs:sequence>  
  
  </xs:complexType>  
  <xs:complexType name="FormXmlLabelsType">  
    <xs:sequence>  
      <xs:element name="label"  
                  minOccurs="0"  
                  maxOccurs="unbounded">  
        <xs:complexType>  
          <xs:attribute name="description"  
                        use="required"  
                        type="xs:string" />  
          <xs:attribute name="languagecode"  
                        use="required"  
                        type="xs:positiveInteger" />  
          <xs:attribute name="addedby"  
                        type="xs:string" />  
  
        </xs:complexType>  
      </xs:element>  
    </xs:sequence>  
  
  </xs:complexType>  
  <xs:complexType name="FormXmlHeaderFooterType">  
    <xs:sequence>  
      <xs:element name="rows"  
                  minOccurs="1"  
                  maxOccurs="1">  
        <xs:complexType>  
          <xs:sequence>  
            <xs:element name="row"  
                        minOccurs="0"  
                        maxOccurs="unbounded">  
              <xs:complexType>  
                <xs:sequence>  
                  <xs:element name="cell"  
                              minOccurs="0"  
                              maxOccurs="unbounded">  
                    <xs:complexType>  
                      <xs:all>  
                        <xs:element name="labels"  
                                    type="FormXmlLabelsType"  
                                    minOccurs="0"  
                                    maxOccurs="1" />  
                        <xs:element name="control"  
                                    type="FormXmlControlType"  
                                    minOccurs="0"  
                                    maxOccurs="1" />  
                      </xs:all>  
                      <xs:attributeGroup ref="FormXmlCellCommon"/>  
                    </xs:complexType>  
                  </xs:element>  
                </xs:sequence>  
                <xs:attributeGroup ref="FormXmlRowCommon"/>  
              </xs:complexType>  
            </xs:element>  
          </xs:sequence>  
  
        </xs:complexType>  
      </xs:element>  
    </xs:sequence>  
    <xs:attribute name="id"  
                  type="FormGuidType"  
                  use="required" />  
    <xs:attributeGroup ref="FormXmlSectionCommon" />  
  </xs:complexType>  
  <xs:attributeGroup name="FormXmlSectionCommon">  
    <xs:attribute name="columns"  
                  type="xs:nonNegativeInteger" />  
    <xs:attribute name="labelwidth"  
                  type="xs:nonNegativeInteger" />  
    <xs:attribute name="celllabelalignment"  
                  use="optional">  
      <xs:simpleType>  
        <xs:restriction base="xs:string">  
          <xs:enumeration value="Center"/>  
          <xs:enumeration value="Left"/>  
          <xs:enumeration value="Right"/>  
        </xs:restriction>  
      </xs:simpleType>  
    </xs:attribute>  
    <xs:attribute name="celllabelposition"  
                  use="optional">  
      <xs:simpleType>  
        <xs:restriction base="xs:string">  
          <xs:enumeration value="Top"/>  
          <xs:enumeration value="Left"/>  
        </xs:restriction>  
      </xs:simpleType>  
    </xs:attribute>  
  
  </xs:attributeGroup>  
  <xs:attributeGroup name="FormXmlRowCommon">  
    <xs:attribute name="height"  
                  type="xs:string" />  
  
  </xs:attributeGroup>  
  <xs:attributeGroup name="FormXmlCellCommon">  
    <xs:attribute name="id"  
                  type="FormGuidType" />  
    <xs:attribute name="showlabel"  
                  type="xs:boolean" />  
    <xs:attribute name="labelid"  
                  type="FormGuidType"  
                  use="optional" />  
    <xs:attribute name="locklevel"  
                  type="xs:nonNegativeInteger" />  
    <xs:attribute name="rowspan"  
                  type="xs:nonNegativeInteger" />  
    <xs:attribute name="colspan"  
                  type="xs:nonNegativeInteger" />  
    <xs:attribute name="userspacer"  
                  type="xs:boolean" />  
    <xs:attribute name="ispreviewcell"  
                  type="xs:boolean"/>  
    <xs:attribute name="visible"  
                  type="xs:boolean" />  
    <xs:attribute name="availableforphone"  
                  type="xs:boolean" />  
    <xs:attribute name="isstreamcell"  
                  type="xs:boolean" />  
    <xs:attribute name="ischartcell"  
                  type="xs:boolean" />  
    <xs:attribute name="istilecell"  
                  type="xs:boolean" />  
  
  </xs:attributeGroup>  
  <xs:simpleType name="BehaviorInBulkEditForm">  
    <xs:restriction base="xs:string">  
      <xs:enumeration value="Disabled" />  
      <xs:enumeration value="EnabledButNoRender" />  
      <xs:enumeration value="Enabled" />  
    </xs:restriction>  
  </xs:simpleType>  
  <xs:simpleType name="FormCRM_Boolean">  
    <xs:restriction base="xs:unsignedByte">  
      <xs:minInclusive value="0" />  
      <xs:maxInclusive value="1" />  
    </xs:restriction>  
  </xs:simpleType>  
  <xs:simpleType name="FormGuidType">  
    <xs:annotation>  
      <xs:documentation xml:lang="en">  
        The representation of a GUID, generally the id of an element.  
      </xs:documentation>  
    </xs:annotation>  
    <xs:restriction base="xs:string">  
      <xs:pattern value="\{[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}\}" />  
    </xs:restriction>  
  </xs:simpleType>  
  <xs:simpleType name="FormISVGuid">  
    <xs:restriction base="xs:string">  
      <xs:pattern value="\{?[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}\}?" />  
    </xs:restriction>  
  </xs:simpleType>  
  <xs:simpleType name ="FormParameterAttributeType">  
    <xs:restriction base ="xs:string">  
      <xs:enumeration value ="Boolean" />  
      <xs:enumeration value ="DateTime" />  
      <xs:enumeration value ="Double" />  
      <xs:enumeration value ="EntityType" />  
      <xs:enumeration value ="Integer" />  
      <xs:enumeration value ="Long" />  
      <xs:enumeration value ="PositiveInteger" />  
      <xs:enumeration value ="SafeString" />  
      <xs:enumeration value ="UniqueId" />  
      <xs:enumeration value ="UnsignedInt" />  
    </xs:restriction>  
  </xs:simpleType >  
  <xs:simpleType name ="FormParameterPassAsAttributeType">  
    <xs:restriction base ="xs:string">  
      <xs:enumeration value ="QueryString" />  
    </xs:restriction>  
  </xs:simpleType>  
  <xs:simpleType name="FormPercentageType">  
    <xs:restriction base="xs:string">  
      <xs:pattern value="^(100|[0-9]{1,2})%$" />  
    </xs:restriction>  
  </xs:simpleType>  
  <xs:simpleType name="FormQueryStringParameterNameAttributeType">  
    <xs:restriction base="xs:string">  
      <xs:pattern value="(?![cC][rR][mM]_)([A-Za-z0-9])+([_])+([A-Za-z0-9_])*"/>  
    </xs:restriction>  
  </xs:simpleType>  
  <xs:simpleType name="GridResizeType">  
    <xs:restriction base="xs:string">  
      <xs:enumeration value="Auto"/>  
      <xs:enumeration value="Fixed"/>  
      <xs:enumeration value="AutoWithFixedMax"/>  
    </xs:restriction>  
  </xs:simpleType>  
  <xs:simpleType name="ImageHorizontalAlignmentType">  
    <xs:restriction base ="xs:string">  
      <xs:enumeration value ="Left" />  
      <xs:enumeration value ="Right" />  
      <xs:enumeration value ="Center" />  
      <xs:enumeration value ="NotSet" />  
    </xs:restriction>  
  </xs:simpleType>  
  <xs:simpleType name="ImageVerticalAlignmentType">  
    <xs:restriction base ="xs:string">  
      <xs:enumeration value ="Top" />  
      <xs:enumeration value ="Middle" />  
      <xs:enumeration value ="Bottom" />  
      <xs:enumeration value ="NotSet" />  
    </xs:restriction>  
  </xs:simpleType>  
  <xs:simpleType name="RelationshipRoleOrdinalType">  
    <xs:restriction base="xs:unsignedByte">  
      <xs:enumeration value="1" />  
      <xs:enumeration value="2" />  
    </xs:restriction>  
  </xs:simpleType>  
  <xs:simpleType name ="WebResourceSizeType">  
    <xs:restriction base ="xs:string">  
      <xs:enumeration value ="StretchToFit" />  
      <xs:enumeration value ="StretchMaintainAspectRatio" />  
      <xs:enumeration value ="Original" />  
      <xs:enumeration value ="Specific" />  
    </xs:restriction>  
  </xs:simpleType>  
  <xs:simpleType name="FormatType">  
    <xs:restriction base ="xs:string">  
      <xs:enumeration value ="SingleLineOfText" />  
      <xs:enumeration value ="WholeNumber" />  
      <xs:enumeration value ="DecimalNumber" />  
      <xs:enumeration value ="Currency" />  
      <xs:enumeration value="Date" />  
      <xs:enumeration value="DateTime" />  
      <xs:enumeration value="DateAndTime" />  
      <xs:enumeration value="Url" />  
      <xs:enumeration value="Ticker" />  
      <xs:enumeration value="Email" />  
      <xs:enumeration value="TextArea" />  
    </xs:restriction>  
  </xs:simpleType>  
  <xs:simpleType name="solutionactionType">  
    <xs:restriction base="xs:string">  
      <xs:enumeration value="Added" />  
      <xs:enumeration value="Removed" />  
      <xs:enumeration value="Modified" />  
    </xs:restriction>  
  </xs:simpleType >  
  <xs:attributeGroup name="FormXmlBaseElementCommon">  
    <xs:attribute name="solutionaction"  
                  type="solutionactionType" />  
  </xs:attributeGroup>  
  <xs:complexType name ="solutionStringType">  
    <xs:simpleContent>  
      <xs:extension base="xs:string">  
        <xs:attributeGroup ref="FormXmlBaseElementCommon"/>  
      </xs:extension>  
    </xs:simpleContent>  
  </xs:complexType>  
  <xs:complexType name ="solutionBooleanType">  
    <xs:simpleContent>  
      <xs:extension base="xs:boolean">  
        <xs:attributeGroup ref="FormXmlBaseElementCommon"/>  
      </xs:extension>  
    </xs:simpleContent>  
  </xs:complexType>  
  <xs:complexType name ="solutionFormGuidType">  
    <xs:simpleContent>  
      <xs:extension base="FormGuidType">  
        <xs:attributeGroup ref="FormXmlBaseElementCommon"/>  
      </xs:extension>  
    </xs:simpleContent>  
  </xs:complexType>  
  <xs:complexType name ="solutionUnsignedIntType">  
    <xs:simpleContent>  
      <xs:extension base="xs:unsignedInt">  
        <xs:attributeGroup ref="FormXmlBaseElementCommon"/>  
      </xs:extension>  
    </xs:simpleContent>  
  </xs:complexType>  
  <xs:complexType name ="solutionWebResourceSizeType">  
    <xs:simpleContent>  
      <xs:extension base="WebResourceSizeType">  
        <xs:attributeGroup ref="FormXmlBaseElementCommon"/>  
      </xs:extension>  
    </xs:simpleContent>  
  </xs:complexType>  
  <xs:complexType name ="solutionImageHorizontalAlignmentType">  
    <xs:simpleContent>  
      <xs:extension base="ImageHorizontalAlignmentType">  
        <xs:attributeGroup ref="FormXmlBaseElementCommon"/>  
      </xs:extension>  
    </xs:simpleContent>  
  </xs:complexType>  
  <xs:complexType name ="solutionFormatType">  
    <xs:simpleContent>  
      <xs:extension base="FormatType">  
        <xs:attributeGroup ref="FormXmlBaseElementCommon"/>  
      </xs:extension>  
    </xs:simpleContent>  
  </xs:complexType>  
  <xs:complexType name ="solutionImageVerticalAlignmentType">  
    <xs:simpleContent>  
      <xs:extension base="ImageVerticalAlignmentType">  
        <xs:attributeGroup ref="FormXmlBaseElementCommon"/>  
      </xs:extension>  
    </xs:simpleContent>  
  </xs:complexType>  
  <xs:complexType name ="solutionRelationshipRoleOrdinalType">  
    <xs:simpleContent>  
      <xs:extension base="RelationshipRoleOrdinalType">  
        <xs:attributeGroup ref="FormXmlBaseElementCommon"/>  
      </xs:extension>  
    </xs:simpleContent>  
  </xs:complexType>  
  <xs:complexType name ="solutionGridResizeType">  
    <xs:simpleContent>  
      <xs:extension base="GridResizeType">  
        <xs:attributeGroup ref="FormXmlBaseElementCommon"/>  
      </xs:extension>  
    </xs:simpleContent>  
  </xs:complexType>  
  <xs:complexType name ="solutionUnsignedShortType">  
    <xs:simpleContent>  
      <xs:extension base="xs:unsignedShort">  
        <xs:attributeGroup ref="FormXmlBaseElementCommon"/>  
      </xs:extension>  
    </xs:simpleContent>  
  </xs:complexType>  
  <xs:group name="SearchWidgetControlParameters">  
    <xs:choice>  
      <xs:element name="FilterResults"  
                  type="xs:string"  
                  minOccurs="0"  
                  maxOccurs="1" />  
      <xs:element name="AllowChangingFiltersOnUI"  
                  type="xs:boolean"  
                  minOccurs="0"  
                  maxOccurs="1" />  
      <xs:element name="ShowLanguageFilter"  
                  type="xs:boolean"  
                  minOccurs="0"  
                  maxOccurs="1" />  
      <xs:element name="ShowDepartmentFilter"  
                  type="xs:boolean"  
                  minOccurs="0"  
                  maxOccurs="1" />  
      <xs:element name="EnableAutoSuggestions"  
                  type="xs:boolean"  
                  minOccurs="0"  
                  maxOccurs="1" />  
      <xs:element name="SearchForAutoSuggestionsUsing"  
                  type="xs:string"  
                  minOccurs="0"  
                  maxOccurs="1" />  
      <xs:element name="EnableRating"  
                  type="xs:boolean"  
                  minOccurs="0"  
                  maxOccurs="1" />  
      <xs:element name="ShowRatingUsing"  
                  type="xs:string"  
                  minOccurs="0"  
                  maxOccurs="1" />  
      <xs:element name="AutoSuggestionSource"  
                  type="xs:string"  
                  minOccurs="0"  
                  maxOccurs="1" />  
      <xs:element name="SelectPrimaryCustomer"  
                  type="xs:string"  
                  minOccurs="0"  
                  maxOccurs="1" />  
      <xs:element name="NumberOfResults"  
                  type="xs:unsignedInt"  
                  minOccurs="0"  
                  maxOccurs="1" />  
      <xs:element name="ShowContextualActions"  
                  type="xs:string"  
                  minOccurs="0"  
                  maxOccurs="1" />  
      <xs:element name="ActionList"  
                  type="xs:string"  
                  minOccurs="0"  
                  maxOccurs="1" />  
      <xs:element name="ReferencePanelSearchWidgetIconUrl"  
                  type="xs:string"  
                  minOccurs="0"  
                  maxOccurs="1" />  
      <xs:element name="SelectDefaultLanguage"  
                  type="xs:string"  
                  minOccurs="0"  
                  maxOccurs="1" />  
    </xs:choice>  
  </xs:group>  
</xs:schema>  
  
```  
  
### See also  
 [Customize forms](customize-entity-forms.md)   
 [Create, install, and update a managed solution](/power-platform/alm/solution-api)<br/>
 [Create, export, or import an Unmanaged solution](/power-platform/alm/solution-api)<br/>
 [Form XML schema](form-xml-schema.md)


[!INCLUDE[footer-include](../../includes/footer-banner.md)]