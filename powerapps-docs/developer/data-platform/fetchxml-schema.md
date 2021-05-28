---
title: "FetchXML schema (Microsoft Dataverse) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "The FetchXML query language is one available method to create data queries against the Microsoft Dataverse database." # 115-145 characters including spaces. This abstract displays in the search result.
ms.custom: ""
ms.date: 03/18/2021
ms.reviewer: "pehecke"
ms.service: powerapps
ms.topic: "article"
author: "mayadumesh" # GitHub ID
ms.author: "jdaly" # MSFT alias of Microsoft employees only
manager: "ryjones" # MSFT alias of manager or PM counterpart
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---
# FetchXML schema

[!INCLUDE[cc-terminology](includes/cc-terminology.md)]

The FetchXML query language is used to create queries against the Microsoft Dataverse database. The following is the schema for the FetchXML query language. For more information, see [Use FetchXML to construct a query](use-fetchxml-construct-query.md).

You can find this schema in the `Schemas\9.0.0.2090\Fetch.xsd` folder when you download the Schemas zip file.
Download the [Schemas](https://download.microsoft.com/download/B/9/7/B97655A4-4E46-4E51-BA0A-C669106D563F/Schemas.zip).
  
## FetchXML Schema  
  
```xml
<?xml version="1.0" encoding="utf-8" ?>
<xs:schema id="fetch" elementFormDefault="qualified" xmlns:xs="https://www.w3.org/2001/XMLSchema"
	xmlns:mstns="https://tempuri.org/fetch/unique">
  <xs:annotation>
    <xs:documentation>Schema name: fetch-schema</xs:documentation>
  </xs:annotation>
  <!--
	
		condition element - used for capturing entity and link-entity
							"where" clause criteria
		
	-->
  <!-- [XDR-XSD] "value" element  -->
  <xs:element name="value" type="xs:string"></xs:element>
  <!-- [XDR-XSD] "condition" element  -->
  <xs:element name="condition">
    <xs:complexType>
      <xs:choice minOccurs="0" maxOccurs="unbounded">
        <!-- -->
        <!--
		The attribute "value" is used for all operators that compare to a single value (for example, eq).
		The element "value" is used for operators that compare to multiple values (for example, in).
		Some operators require neither the attribute "value" or the element "value" (for example, null).
	-->
        <xs:element name="value" minOccurs="0" maxOccurs="unbounded">
          <xs:complexType>
            <xs:simpleContent>
              <xs:extension base="xs:string">
                <xs:attribute name="uiname" type="xs:string" />
                <xs:attribute name="uitype" type="xs:string" />
              </xs:extension>
            </xs:simpleContent>
          </xs:complexType>
        </xs:element>
      </xs:choice>
      <!-- -->
      <xs:attribute name="column" type="xs:string" />
      <xs:attribute name="attribute" type="xs:string"></xs:attribute>
      <xs:attribute name="entityname" type="xs:string"></xs:attribute>
      <xs:attribute name="operator" use="required" type="operator"></xs:attribute>
      <!--
		The attribute "value" is used for all operators that compare to a single value (for example, eq).
		The element "value" is used for operators that compare to multiple values (for example, in).
		Some operators require neither the attribute "value" or the element "value" (for example, null).
	-->
      <xs:attribute name="value" type="xs:string"></xs:attribute>
      <xs:attribute name="aggregate" type="AggregateType"></xs:attribute>
      <xs:attribute name="rowaggregate" type="RowAggregateType"></xs:attribute>
      <xs:attribute name="alias" type="xs:string"></xs:attribute>
      <xs:attribute name="uiname" />
      <xs:attribute name="uitype" />
      <xs:attribute name="uihidden" type="TrueFalse01Type" />
    </xs:complexType>
  </xs:element>
  <!--
	
		filter element - used for constructing complex conditionals
						 legal on entity and link-entity
		
	-->
  <!-- [XDR-XSD] "filter" element  -->
  <xs:element name="filter">
    <xs:complexType>
      <xs:choice minOccurs="0" maxOccurs="unbounded">
        <!-- -->
        <xs:element ref="condition" minOccurs="0" maxOccurs="500" />
        <xs:element ref="filter" minOccurs="0" maxOccurs="unbounded" />
      </xs:choice>
      <!-- -->
      <xs:attribute name="type" default="and">
        <xs:simpleType>
          <xs:restriction base="xs:NMTOKEN">
            <xs:enumeration value="and" />
            <xs:enumeration value="or" />
          </xs:restriction>
        </xs:simpleType>
      </xs:attribute>
      <xs:attribute name="isquickfindfields" type="xs:boolean" />
    </xs:complexType>
  </xs:element>
  <!--
	
		attribute elements - used for selecting attributes from the
							 surrounding entity / link-entity, these
							 values are returned as part of the fetch
		
	-->
  <!-- [XDR-XSD] "all-attributes" element  -->
  <xs:element name="all-attributes">
    <xs:complexType></xs:complexType>
  </xs:element>
  <!-- [XDR-XSD] "attribute" element  -->
  <xs:complexType name="FetchAttributeType">
    <xs:attribute name="name" use="required" type="xs:string"></xs:attribute>
    <xs:attribute name="build" type="build"></xs:attribute>
    <xs:attribute name="addedby" type="xs:string" />
    <xs:attribute name="alias" type="xs:string"></xs:attribute>
    <xs:attribute name="aggregate" type="AggregateType"></xs:attribute>
    <xs:attribute name="groupby" type="FetchBoolType"></xs:attribute>
    <xs:attribute name="dategrouping" type="DateGroupingType"></xs:attribute>
    <xs:attribute name="usertimezone" type="FetchBoolType"></xs:attribute>
    <xs:attribute name="distinct" type="FetchBoolType"></xs:attribute>
  </xs:complexType>
  <!--
	
	order element - used to specify a sort order

	-->
  <!-- [XDR-XSD] "order" element  -->
  <xs:complexType name="FetchOrderType">
    <xs:choice minOccurs="0" maxOccurs="unbounded">
      <!-- -->
    </xs:choice>
    <!-- -->
    <xs:attribute name="attribute" type="xs:string"></xs:attribute>
    <xs:attribute name="alias" type="xs:string"></xs:attribute>
    <xs:attribute name="descending" default="false" type="xs:boolean"></xs:attribute>
  </xs:complexType>
  <!--
	
		link-entity element - used for joining one entity to its "parent"
		
	-->
  <!-- [XDR-XSD] "link-entity" element  -->
  <xs:complexType name="FetchLinkEntityType">
    <xs:choice minOccurs="0" maxOccurs="unbounded">
      <!-- -->
      <xs:element ref="all-attributes" minOccurs="0" />
      <xs:element name="attribute" type="FetchAttributeType" minOccurs="0" maxOccurs="unbounded" />
      <xs:element name="order" type="FetchOrderType" minOccurs="0" maxOccurs="1" />
      <xs:element ref="filter" minOccurs="0" />
      <xs:element name="link-entity" type="FetchLinkEntityType" />
    </xs:choice>
    <!-- -->
    <xs:attribute name="name" use="required" type="xs:string"></xs:attribute>
    <xs:attribute name="to" type="xs:string"></xs:attribute>
    <xs:attribute name="from" type="xs:string"></xs:attribute>
    <xs:attribute name="alias" type="xs:string"></xs:attribute>
    <xs:attribute name="link-type" type="xs:string"></xs:attribute>
    <xs:attribute name="visible" type="xs:boolean"></xs:attribute>
    <xs:attribute name="intersect" type="xs:boolean"></xs:attribute>
    <xs:attribute name="enableprefiltering" type="xs:boolean"></xs:attribute>
    <xs:attribute name="prefilterparametername" type="xs:string"></xs:attribute>
  </xs:complexType>
  <!--
	
		entity element - used for specifying the root element for a fetch, only
						 one root entity is allowed in a given fetch, all others
						 are dependent on this entity and are marked as
						 link-entity
		
	-->
  <!-- [XDR-XSD] "entity" element  -->
  <xs:complexType name="FetchEntityType">
    <xs:choice minOccurs="0" maxOccurs="unbounded">
      <!-- -->
      <xs:element ref="all-attributes" minOccurs="0" />
      <xs:element name="attribute" type="FetchAttributeType" minOccurs="0" maxOccurs="unbounded" />
      <xs:element name="order" type="FetchOrderType" minOccurs="0" maxOccurs="unbounded" />
      <xs:element name="link-entity" type="FetchLinkEntityType" />
      <xs:element ref="filter" minOccurs="0" />
    </xs:choice>
    <!-- -->
    <xs:attribute name="name" use="required" type="xs:string"></xs:attribute>
    <xs:attribute name="enableprefiltering" type="xs:boolean"></xs:attribute>
    <xs:attribute name="prefilterparametername" type="xs:string"></xs:attribute>
  </xs:complexType>
  <!--
	
		fetch element - root element for the query
		
	-->
  <!-- [XDR-XSD] "fetch" element  -->
  <xs:element name="fetch" type="FetchType"/>
  <xs:complexType name="FetchType">
    <xs:choice minOccurs="0" maxOccurs="unbounded">
      <!-- -->
      <xs:element name="entity" type="FetchEntityType" />
      <!-- This is for the Reports view only -->
      <xs:element name="order" type="FetchOrderType" minOccurs="1" maxOccurs="1" />
    </xs:choice>
    <!-- -->
    <xs:attribute name="version"/>
    <xs:attribute name="count" type="xs:integer"/>
    <xs:attribute name="page" type="xs:integer"/>
    <xs:attribute name="paging-cookie" type="xs:string"/>
    <xs:attribute name="utc-offset" type="IntOrEmpty"/>
    <xs:attribute name="aggregate" type="xs:boolean"/>
    <xs:attribute name="distinct" type="xs:boolean"/>
    <xs:attribute name="top" type="xs:integer"/>
    <xs:attribute name="mapping">
      <xs:simpleType>
        <xs:restriction base="xs:NMTOKEN">
          <xs:enumeration value="internal" />
          <xs:enumeration value="logical" />
        </xs:restriction>
      </xs:simpleType>
    </xs:attribute>
    <xs:attribute name="min-active-row-version" type="xs:boolean" use="optional" default="false"/>
    <xs:attribute name="output-format">
      <xs:simpleType>
        <xs:restriction base="xs:NMTOKEN">
          <xs:enumeration value="xml-ado" />
          <xs:enumeration value="xml-auto" />
          <xs:enumeration value="xml-elements" />
          <xs:enumeration value="xml-raw" />
          <xs:enumeration value="xml-platform" />
        </xs:restriction>
      </xs:simpleType>
    </xs:attribute>
    <xs:attribute name="returntotalrecordcount" type="xs:boolean" use="optional" default="false" />
    <xs:attribute name="no-lock" type="xs:boolean" use="optional" default="false" />
  </xs:complexType>
  <!-- [XDR-XSD] XDR datatype derivations -->
  <xs:element name="savedquery">
    <xs:complexType>
      <xs:all>
        <xs:element name="name" type="xs:string" minOccurs="1" maxOccurs="1" />
        <xs:element name="savedqueryid" type="guid" minOccurs="1" maxOccurs="1" />
        <xs:element name="returnedtypecode" type="SerializedInteger" minOccurs="1" maxOccurs="1" />
        <xs:element name="description" type="xs:string" minOccurs="0" maxOccurs="1" />
        <xs:element name="querytype" type="SerializedInteger" minOccurs="1" maxOccurs="1" />
        <xs:element name="IsCustomizable" type="SerializedTrueFalse01Type" minOccurs="0" maxOccurs="1" />
        <xs:element name="CanBeDeleted" type="SerializedTrueFalse01Type" minOccurs="0" maxOccurs="1" />
        <xs:element name="IntroducedVersion" type="VersionType" minOccurs="0" maxOccurs="1" />
        <xs:element name="isquickfindquery" type="SerializedTrueFalse01Type" minOccurs="0" maxOccurs="1" />
        <xs:element name="isuserdefined" type="SerializedTrueFalse01Type" minOccurs="0" maxOccurs="1" />
        <xs:element name="isdefault" type="SerializedTrueFalse01Type" minOccurs="0" maxOccurs="1" />
        <xs:element name="isprivate" type="xs:boolean" minOccurs="0" maxOccurs="1" />
        <xs:element name="queryapi" type="xs:string" minOccurs="0" maxOccurs="1" />
        <xs:element name="fetchxml" minOccurs="0" maxOccurs="1">
          <xs:complexType>
            <xs:sequence>
              <xs:element ref="fetch" minOccurs="0" maxOccurs="1" />
            </xs:sequence>
          </xs:complexType>
        </xs:element>
        <xs:element name="columnsetxml" minOccurs="0" maxOccurs="1">
          <xs:complexType>
            <xs:sequence>
              <xs:element name="columnset" minOccurs="0" maxOccurs="1">
                <xs:complexType>
                  <xs:choice minOccurs="0" maxOccurs="unbounded">
                    <!-- Because <column> contains text and one attribute we cannot specify its type. We have to define it as a complexType with a simple content. -->
                    <xs:element name="column" minOccurs="0" maxOccurs="1">
                      <xs:complexType>
                        <xs:simpleContent>
                          <xs:extension base="xs:string">
                            <xs:attribute name="build" type="build" />
                            <xs:attribute name="addedby" type="xs:string" />
                          </xs:extension>
                        </xs:simpleContent>
                      </xs:complexType>
                    </xs:element>
                    <xs:choice>
                      <xs:element name="ascend" minOccurs="0" maxOccurs="1" />
                      <xs:element name="descend" minOccurs="0" maxOccurs="1" />
                    </xs:choice>
                    <xs:element name="filter" minOccurs="0" maxOccurs="1">
                      <!-- Allow support for v1.5 format -->
                      <xs:complexType>
                        <xs:sequence>
                          <xs:element name="condition" minOccurs="1" maxOccurs="500">
                            <xs:complexType>
                              <xs:attribute name="column" type="xs:string" use="required" />
                              <xs:attribute name="operator" type="operator" use="optional" />
                              <xs:attribute name="value" type="xs:string" use="optional"/>
                            </xs:complexType>
                          </xs:element>
                        </xs:sequence>

                        <xs:attribute name="column" type="xs:string" use="optional" />
                        <xs:attribute name="operator" type="operator" use="optional" />
                        <xs:attribute name="value" type="xs:string" use="optional"/>
                        <xs:attribute name="type" type="xs:string" use="optional"/>

                      </xs:complexType>
                    </xs:element>
                  </xs:choice>
                  <xs:attribute name="version"></xs:attribute>
                  <xs:attribute name="distinct" type="xs:boolean"/>
                </xs:complexType>
              </xs:element>
            </xs:sequence>
          </xs:complexType>
        </xs:element>
        <xs:element name="layoutxml" minOccurs="0" maxOccurs="1">
          <xs:complexType>
            <xs:sequence>
              <xs:element name="grid" minOccurs="0" maxOccurs="1">
                <xs:complexType>
                  <xs:sequence>
                    <xs:element name="row" minOccurs="1" maxOccurs="1">
                      <xs:complexType>
                        <xs:sequence>
                          <xs:element name="cell" minOccurs="1" maxOccurs="unbounded">
                            <xs:complexType>
                              <xs:sequence></xs:sequence>
                              <xs:attribute name="name" type="xs:string" use="required" />
                              <xs:attribute name="width" type="xs:integer" use="optional" />
                              <xs:attribute name="LabelId" type="xs:string" use="optional" />
                              <xs:attribute name="label" type="xs:string" use="optional" />
                              <xs:attribute name="desc" type="xs:string" use="optional" />
                              <xs:attribute name="ishidden" type="xs:integer" use="optional" />
                              <xs:attribute name="disableSorting" type="xs:integer" use="optional" />
                              <xs:attribute name="disableMetaDataBinding" type="xs:integer" use="optional" />
                              <xs:attribute name="cellType" type ="xs:string" />
                              <xs:attribute name="imageproviderwebresource" type ="xs:string" />
                              <xs:attribute name="imageproviderfunctionname" type ="xs:string" />
                            </xs:complexType>
                          </xs:element>
                        </xs:sequence>
                        <xs:attribute name="name" type="xs:string" use="required" />
                        <xs:attribute name="id" type="xs:string" use="required" />
                        <xs:attribute name="multiobjectidfield" type="xs:string" />
                        <xs:attribute name="layoutstyle" type="xs:string" />
                      </xs:complexType>
                    </xs:element>
                  </xs:sequence>
                  <xs:attribute name="name" type="xs:string" use="required" />
                  <xs:attribute name="select" type="xs:boolean" use="required" />
                  <xs:attribute name="preview" type="BoolOrEmpty" use="required" />
                  <xs:attribute name="icon" type="BoolOrEmpty" use="required" />
                  <xs:attribute name="jump" type="xs:string" use="optional" />
                  <xs:attribute name="object" type="xs:integer" use="required" />
                  <xs:attribute name="disableInlineEditing" type="xs:integer" use="optional" />
                  <xs:attribute name="iconrenderer" type="xs:string" />
                  <xs:attribute name="multilinerows" type="BoolOrEmpty" use="optional" />
                </xs:complexType>
              </xs:element>
            </xs:sequence>
          </xs:complexType>
        </xs:element>
      </xs:all>
      <xs:attribute name="donotuseinLCID" type="xs:string" use="optional" />
      <xs:attribute name="useinLCID" type="xs:string" use="optional" />
    </xs:complexType>
  </xs:element>
  <xs:complexType name="SerializedInteger">
    <xs:simpleContent>
      <xs:extension base="xs:nonNegativeInteger">
        <xs:attribute name="formattedvalue" type="xs:string" />
      </xs:extension>
    </xs:simpleContent>
  </xs:complexType>
  <xs:simpleType name="build">
    <xs:restriction base="xs:string">
      <xs:enumeration value="1.504021" />
      <xs:enumeration value="1.003017" />
    </xs:restriction>
  </xs:simpleType>
  <xs:simpleType name="operator">
    <xs:restriction base="xs:NMTOKEN">
      <xs:enumeration value="eq" />
      <xs:enumeration value="neq" />
      <xs:enumeration value="ne" />
      <xs:enumeration value="gt" />
      <xs:enumeration value="ge" />
      <xs:enumeration value="le" />
      <xs:enumeration value="lt" />
      <xs:enumeration value="like" />
      <xs:enumeration value="not-like" />
      <xs:enumeration value="in" />
      <xs:enumeration value="not-in" />
      <xs:enumeration value="between" />
      <xs:enumeration value="not-between" />
      <xs:enumeration value="null" />
      <xs:enumeration value="not-null" />
      <xs:enumeration value="yesterday" />
      <xs:enumeration value="today" />
      <xs:enumeration value="tomorrow" />
      <xs:enumeration value="last-seven-days" />
      <xs:enumeration value="next-seven-days" />
      <xs:enumeration value="last-week" />
      <xs:enumeration value="this-week" />
      <xs:enumeration value="next-week" />
      <xs:enumeration value="last-month" />
      <xs:enumeration value="this-month" />
      <xs:enumeration value="next-month" />
      <xs:enumeration value="on" />
      <xs:enumeration value="on-or-before" />
      <xs:enumeration value="on-or-after" />
      <xs:enumeration value="last-year" />
      <xs:enumeration value="this-year" />
      <xs:enumeration value="next-year" />
      <xs:enumeration value="last-x-hours" />
      <xs:enumeration value="next-x-hours" />
      <xs:enumeration value="last-x-days" />
      <xs:enumeration value="next-x-days" />
      <xs:enumeration value="last-x-weeks" />
      <xs:enumeration value="next-x-weeks" />
      <xs:enumeration value="last-x-months" />
      <xs:enumeration value="next-x-months" />
      <xs:enumeration value="olderthan-x-months" />
      <xs:enumeration value="olderthan-x-years" />
      <xs:enumeration value="olderthan-x-weeks" />
      <xs:enumeration value="olderthan-x-days" />
      <xs:enumeration value="olderthan-x-hours" />
      <xs:enumeration value="olderthan-x-minutes" />
      <xs:enumeration value="last-x-years" />
      <xs:enumeration value="next-x-years" />
      <xs:enumeration value="eq-userid" />
      <xs:enumeration value="ne-userid" />
      <xs:enumeration value="eq-userteams" />
      <xs:enumeration value="eq-useroruserteams" />
      <xs:enumeration value="eq-useroruserhierarchy" />
      <xs:enumeration value="eq-useroruserhierarchyandteams" />
      <xs:enumeration value="eq-businessid" />
      <xs:enumeration value="ne-businessid" />
      <xs:enumeration value="eq-userlanguage" />
      <xs:enumeration value="this-fiscal-year" />
      <xs:enumeration value="this-fiscal-period" />
      <xs:enumeration value="next-fiscal-year" />
      <xs:enumeration value="next-fiscal-period" />
      <xs:enumeration value="last-fiscal-year" />
      <xs:enumeration value="last-fiscal-period" />
      <xs:enumeration value="last-x-fiscal-years" />
      <xs:enumeration value="last-x-fiscal-periods" />
      <xs:enumeration value="next-x-fiscal-years" />
      <xs:enumeration value="next-x-fiscal-periods" />
      <xs:enumeration value="in-fiscal-year" />
      <xs:enumeration value="in-fiscal-period" />
      <xs:enumeration value="in-fiscal-period-and-year" />
      <xs:enumeration value="in-or-before-fiscal-period-and-year" />
      <xs:enumeration value="in-or-after-fiscal-period-and-year" />
      <xs:enumeration value="begins-with" />
      <xs:enumeration value="not-begin-with" />
      <xs:enumeration value="ends-with" />
      <xs:enumeration value="not-end-with" />
      <xs:enumeration value="under"/>
      <xs:enumeration value="eq-or-under" />
      <xs:enumeration value="not-under"/>
      <xs:enumeration value="above" />
      <xs:enumeration value="eq-or-above" />
      <xs:enumeration value="contain-values" />
      <xs:enumeration value="not-contain-values" />
    </xs:restriction>
  </xs:simpleType>
  <xs:simpleType name="VersionType">
    <xs:annotation>
      <xs:documentation xml:lang="en">
        The representation of a Version number.
      </xs:documentation>
    </xs:annotation>
    <xs:restriction base="xs:string">
      <xs:pattern value="^[0-9]+(\.[0-9]+){1,3}$" />
    </xs:restriction>
  </xs:simpleType>
  <xs:simpleType name="guid">
    <xs:restriction base="xs:string">
      <xs:pattern value="\{?[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}\}?" />
    </xs:restriction>
  </xs:simpleType>
  <xs:simpleType name="BoolOrEmpty">
    <xs:union memberTypes="xs:boolean">
      <xs:simpleType>
        <xs:restriction base="xs:string">
          <xs:enumeration value="" />
        </xs:restriction>
      </xs:simpleType>
    </xs:union>
  </xs:simpleType>
  <xs:simpleType name="IntOrEmpty">
    <xs:union memberTypes="xs:integer">
      <xs:simpleType>
        <xs:restriction base="xs:string">
          <xs:enumeration value="" />
        </xs:restriction>
      </xs:simpleType>
    </xs:union>
  </xs:simpleType>
  <xs:simpleType name="TrueFalse01Type">
    <xs:restriction base="xs:string">
      <xs:enumeration value="0" />
      <xs:enumeration value="1" />
    </xs:restriction>
  </xs:simpleType>
  <xs:simpleType name="AggregateType">
    <xs:restriction base="xs:NMTOKEN">
      <xs:enumeration value="count" />
      <xs:enumeration value="countcolumn" />
      <xs:enumeration value="sum" />
      <xs:enumeration value="avg" />
      <xs:enumeration value="min" />
      <xs:enumeration value="max" />
    </xs:restriction>
  </xs:simpleType>
  <xs:simpleType name="RowAggregateType">
    <xs:restriction base="xs:NMTOKEN">
      <xs:enumeration value="countchildren" />
    </xs:restriction>
  </xs:simpleType>
  <xs:simpleType name="DateGroupingType">
    <xs:restriction base="xs:NMTOKEN">
      <xs:enumeration value="day" />
      <xs:enumeration value="week" />
      <xs:enumeration value="month" />
      <xs:enumeration value="quarter" />
      <xs:enumeration value="year" />
      <xs:enumeration value="fiscal-period" />
      <xs:enumeration value="fiscal-year" />
    </xs:restriction>
  </xs:simpleType>
  <xs:simpleType name="FetchBoolType">
    <xs:restriction base="xs:NMTOKEN">
      <xs:enumeration value="true" />
      <xs:enumeration value="false" />
      <xs:enumeration value="1" />
      <xs:enumeration value="0" />
    </xs:restriction>
  </xs:simpleType>
  <xs:complexType name="SerializedTrueFalse01Type">
    <xs:simpleContent>
      <xs:extension base="TrueFalse01Type">
        <xs:attribute name="name" type="xs:string" />
      </xs:extension>
    </xs:simpleContent>
  </xs:complexType>
  <xs:complexType name="LocalizedNamesType">
    <xs:sequence>
      <xs:element name="LocalizedName" type="FieldXmlFieldUIType" minOccurs="0" maxOccurs="unbounded" />
    </xs:sequence>
  </xs:complexType>
  <xs:complexType name="DescriptionsType">
    <xs:sequence>
      <xs:element name="Description" type="FieldXmlFieldUIType" minOccurs="0" maxOccurs="unbounded" />
    </xs:sequence>
  </xs:complexType>
  <xs:complexType name="ColorsType">
    <xs:sequence>
      <xs:element name="Color" type="FieldXmlFieldUIType" minOccurs="0" maxOccurs="unbounded" />
    </xs:sequence>
  </xs:complexType>
  <xs:complexType name="FieldXmlFieldUIType">
    <xs:attribute name="id" type="guid" />
    <xs:attribute name="description" use="required" type="xs:string" />
    <xs:attribute name="languagecode" use="required" type="xs:positiveInteger" />
  </xs:complexType>
</xs:schema>
```  
  
### See also  
 [Retrieve data with queries](/dynamics365/customer-engagement/developer/retrieve-data-queries-sdk-assemblies)   
 [Schemas used in Dynamics 365](/dynamics365/customer-engagement/developer/schemas-used-dynamics-365)   
 [Build queries with FetchXML](/dynamics365/customer-engagement/developer/build-queries-fetchxml)

[!INCLUDE[footer-include](../../includes/footer-banner.md)]