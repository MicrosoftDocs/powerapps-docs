---
title: "Ribbon WSS schema (model-driven apps) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "The following is the schema definition for the ribbon types WSS of an import/export customization file. It is included from the Ribbon Core Schema." # 115-145 characters including spaces. This abstract displays in the search result.
ms.custom: ""
ms.date: 10/31/2018
ms.reviewer: ""
ms.service: powerapps
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
# Ribbon WSS schema

<!-- https://docs.microsoft.com/dynamics365/customer-engagement/developer/customize-dev/ribbon-wss-schema -->

The following is the schema definition for the ribbon types WSS of an import/export customization file. Ribbon WSS is included from the [Ribbon Core Schema](ribbon-core-schema.md). You can find schema in the `Schemas\9.0.0.2090\RibbonWSS.xsd` folder when you download the Schemas zip file.

Download the [Schemas](https://download.microsoft.com/download/B/9/7/B97655A4-4E46-4E51-BA0A-C669106D563F/Schemas.zip).


For more information, see [Package and Distribute Extensions with Solutions](../data-platform/introduction-solutions.md).


## Schema  
  
```xml  
<?xml version="1.0" encoding="utf-8"?>
<xs:schema id="CrmRibbonWss" xmlns:xs="https://www.w3.org/2001/XMLSchema">

  <xs:simpleType name="AltType">
    <xs:restriction base="xs:string" />
  </xs:simpleType>

  <xs:simpleType name="ClassNameType">
    <xs:restriction base="xs:string" />
  </xs:simpleType>

  <xs:simpleType name="ContextualColorType">
    <xs:restriction base="xs:string">
      <xs:enumeration value="None" />
      <xs:enumeration value="DarkBlue" />
      <xs:enumeration value="LightBlue" />
      <xs:enumeration value="Teal" />
      <xs:enumeration value="Orange" />
      <xs:enumeration value="Green" />
      <xs:enumeration value="Magenta" />
      <xs:enumeration value="Yellow" />
      <xs:enumeration value="Purple" />
    </xs:restriction>
  </xs:simpleType>

  <xs:simpleType name="CommandType">
    <xs:restriction base="xs:string" />
  </xs:simpleType>

  <xs:simpleType name="CommandTypeType">
    <xs:restriction base="xs:string" >
      <xs:enumeration value="General" />
      <xs:enumeration value="OptionSelection" />
      <xs:enumeration value="IgnoredByMenu" />
    </xs:restriction>
  </xs:simpleType>

  <xs:simpleType name="DescriptionType">
    <xs:restriction base="xs:string" />
  </xs:simpleType>

  <xs:simpleType name="DisplayModeType">
    <xs:restriction base="xs:string">
      <xs:enumeration value="Default" />
      <xs:enumeration value="Small" />
      <xs:enumeration value="Medium" />
      <xs:enumeration value="Large" />
      <xs:enumeration value="Text" />
      <xs:enumeration value="Menu" />
      <xs:enumeration value="Menu16" />
      <xs:enumeration value="Menu32" />
      <xs:enumeration value="Thin" />
    </xs:restriction>
  </xs:simpleType>

  <xs:simpleType name="ElementDimensionsType">
    <xs:restriction base="xs:string">
      <xs:enumeration value="Size16by16" />
      <xs:enumeration value="Size32by32" />
      <xs:enumeration value="Size48by48" />
      <xs:enumeration value="Size64by48" />
      <xs:enumeration value="Size72by96" />
      <xs:enumeration value="Size96by72" />
      <xs:enumeration value="Size96by96" />
      <xs:enumeration value="Size128by128" />
      <xs:enumeration value="Size190by30" />
      <xs:enumeration value="Size190by40" />
      <xs:enumeration value="Size190by50" />
      <xs:enumeration value="Size190by60" />
    </xs:restriction>
  </xs:simpleType>

  <xs:simpleType name="HTMLType">
    <xs:restriction base="xs:string" />
  </xs:simpleType>

  <xs:simpleType name="IdType">
    <xs:restriction base="xs:string" />
  </xs:simpleType>

  <xs:simpleType name="ImageClassType">
    <xs:restriction base="xs:string" />
  </xs:simpleType>

  <xs:simpleType name="ImagePositionType">
    <xs:restriction base="xs:nonPositiveInteger" />
  </xs:simpleType>

  <xs:simpleType name="ImageUrlType">
    <xs:restriction base="xs:string" />
  </xs:simpleType>

  <xs:simpleType name="LabelCssType">
    <xs:restriction base="xs:string" />
  </xs:simpleType>

  <xs:simpleType name="LabelTextType">
    <xs:restriction base="xs:string" />
  </xs:simpleType>

  <xs:simpleType name="MenuItemIdType">
    <xs:restriction base="xs:string" />
  </xs:simpleType>

  <xs:simpleType name="ModernCommandTypeType">
    <xs:restriction base="xs:string">
      <xs:enumeration value="ControlCommand" />
      <xs:enumeration value="System" />
    </xs:restriction>
  </xs:simpleType>

  <xs:simpleType name="PixelLengthType">
    <xs:restriction base="xs:string" />
  </xs:simpleType>

  <xs:simpleType name="SectionTypeType">
    <xs:restriction base="xs:string">
      <xs:enumeration value="Divider" />
      <xs:enumeration value="OneRow" />
      <xs:enumeration value="TwoRow" />
      <xs:enumeration value="ThreeRow" />
    </xs:restriction>
  </xs:simpleType>

  <xs:simpleType name="SectionAlignmentType">
    <xs:restriction base="xs:string">
      <xs:enumeration value="Top" />
      <xs:enumeration value="Middle" />
    </xs:restriction>
  </xs:simpleType>

  <xs:simpleType name="SequenceType">
    <xs:restriction base="xs:integer" />
  </xs:simpleType>

  <xs:simpleType name="PriorityType">
    <xs:restriction base="xs:integer" />
  </xs:simpleType>

  <xs:simpleType name="SizeType">
    <xs:restriction base="xs:string" />
  </xs:simpleType>

  <xs:simpleType name="TemplateType">
    <xs:restriction base="xs:string" />
  </xs:simpleType>

  <xs:simpleType name="TemplateAliasType">
    <xs:restriction base="xs:string" />
  </xs:simpleType>

  <xs:simpleType name="TextDirectionType">
    <xs:restriction base="xs:string" />
  </xs:simpleType>

  <xs:simpleType name="TitleType">
    <xs:restriction base="xs:string" />
  </xs:simpleType>      
  
  <xs:simpleType name="UnitNameType">
    <xs:restriction base="xs:string" />
  </xs:simpleType>

  <xs:simpleType name="ValueType">
    <xs:restriction base="xs:decimal" />
  </xs:simpleType>

  <xs:complexType name="ButtonType">
    <xs:attribute name="Alt" type="AltType" />
    <xs:attribute name="Command" type="CommandType" />
    <xs:attribute name="CommandType" type="CommandTypeType" />
    <xs:attribute name="CommandValueId" type="xs:string" />
    <xs:attribute name="Description" type="xs:string" />
    <xs:attribute name="Id" type="IdType" use="required" />
    <xs:attribute name="Image32by32" type="ImageUrlType" />
    <xs:attribute name="Image32by32Class" type="ImageClassType" />
    <xs:attribute name="Image32by32Left" type="ImagePositionType" />
    <xs:attribute name="Image32by32Top" type="ImagePositionType" />
    <xs:attribute name="Image16by16" type="ImageUrlType" />
    <xs:attribute name="Image16by16Class" type="ImageClassType" />
    <xs:attribute name="Image16by16Left" type="ImagePositionType" />
    <xs:attribute name="Image16by16Top" type="ImagePositionType" />
    <xs:attribute name="LabelCss" type="LabelCssType" />
    <xs:attribute name="LabelText" type="LabelTextType" />
    <xs:attribute name="MenuItemId" type="MenuItemIdType" />
    <xs:attribute name="ModernCommandType" type="ModernCommandTypeType" />
    <xs:attribute name="Sequence" type="SequenceType" />
    <xs:attribute name="Priority" type="PriorityType" />
    <xs:attribute name="TemplateAlias" type="TemplateAliasType" />
    <xs:attribute name="ToolTipImage32by32" type="ImageUrlType" />
    <xs:attribute name="ToolTipImage32by32Class" type="ImageClassType" />
    <xs:attribute name="ToolTipImage32by32Left" type="ImagePositionType" />
    <xs:attribute name="ToolTipImage32by32Top" type="ImagePositionType" />
    <xs:attribute name="ToolTipTitle" type="xs:string" />
    <xs:attribute name="ToolTipDescription" type="xs:string" />
    <xs:attribute name="ToolTipHelpKeyWord" type="xs:string" />
    <xs:attribute name="ToolTipShortcutKey" type="xs:string" />
    <xs:attribute name="ModernImage" type="xs:string" />
  </xs:complexType>

  <xs:complexType name="CheckBoxType">
    <xs:attribute name="Alt" type="AltType" />
    <xs:attribute name="Command" type="CommandType" />
    <xs:attribute name="Id" type="IdType" use="required" />
    <xs:attribute name="LabelText" type="LabelTextType" />
    <xs:attribute name="QueryCommand" type="CommandType" />
    <xs:attribute name="TemplateAlias" type="TemplateAliasType" />
    <xs:attribute name="MenuItemId" type="MenuItemIdType" />
    <xs:attribute name="Sequence" type="SequenceType" />
    <xs:attribute name="ToolTipImage32by32" type="ImageUrlType" />
    <xs:attribute name="ToolTipImage32by32Class" type="ImageClassType" />
    <xs:attribute name="ToolTipImage32by32Left" type="ImagePositionType" />
    <xs:attribute name="ToolTipImage32by32Top" type="ImagePositionType" />
    <xs:attribute name="ToolTipTitle" type="xs:string" />
    <xs:attribute name="ToolTipDescription" type="xs:string" />
    <xs:attribute name="ToolTipHelpKeyWord" type="xs:string" />
    <xs:attribute name="ToolTipShortcutKey" type="xs:string" />
  </xs:complexType>

  <xs:complexType name="ColorPickerType">
    <xs:sequence>
      <xs:element name="Colors" type="ColorStylesType" minOccurs="0" maxOccurs="1" />
    </xs:sequence>
    <xs:attribute name="Command" type="CommandType" />
    <xs:attribute name="CommandPreview" type="CommandType" />
    <xs:attribute name="CommandRevert" type="CommandType" />
    <xs:attribute name="Id" type="IdType" use="required" />
    <xs:attribute name="QueryCommand" type="CommandType" />
    <xs:attribute name="Sequence" type="SequenceType" />
    <xs:attribute name="TemplateAlias" type="TemplateAliasType" />
  </xs:complexType>

  <xs:complexType name="ColorStylesType">
    <xs:sequence>
      <xs:element name="Color" type="ColorStyleType" minOccurs="0" maxOccurs="unbounded" />
    </xs:sequence>
  </xs:complexType>

  <xs:complexType name="ColorStyleType">
    <xs:attribute name="Sequence" type="SequenceType" />
    <xs:attribute name="Title" type="AltType" />
    <xs:attribute name="Style" type="xs:string" />
    <xs:attribute name="Color" type="xs:string" />
    <xs:attribute name="DisplayColor" type="xs:string" />
  </xs:complexType>

  <xs:complexType name="ComboBoxType">
    <xs:sequence>
      <xs:element name="Menu" type="MenuType" minOccurs="0" maxOccurs="1"/>
    </xs:sequence>
    <xs:attribute name="AllowFreeForm" type="xs:boolean" default="false" />
    <xs:attribute name="AltArrow" type="AltType" />
    <xs:attribute name="Alt" type="AltType" />
    <xs:attribute name="AutoComplete" type="xs:boolean" default="true" />
    <xs:attribute name="AutoCompleteDelay" type="xs:integer" default="100" />
    <xs:attribute name="CacheMenuVersions" type="xs:boolean" default="false" />
    <xs:attribute name="Command" type="CommandType" />
    <xs:attribute name="CommandMenuOpen" type="CommandType" />
    <xs:attribute name="CommandMenuClose" type="CommandType" />
    <xs:attribute name="CommandPreview" type="CommandType" />
    <xs:attribute name="CommandPreviewRevert" type="CommandType" />
    <xs:attribute name="ImeEnabled" type="xs:boolean" />
    <xs:attribute name="InitialItem" type="MenuItemIdType"/>
    <xs:attribute name="Id" type="IdType" use="required" />
    <xs:attribute name="QueryCommand" type="CommandType" />
    <xs:attribute name="PopulateDynamically" type="xs:boolean" default="false" />
    <xs:attribute name="PopulateQueryCommand" type="CommandType" />
    <xs:attribute name="PopulateOnlyOnce" type="xs:boolean" default="false" />
    <xs:attribute name="Sequence" type="SequenceType" />
    <xs:attribute name="TemplateAlias" type="TemplateAliasType" />
    <xs:attribute name="ToolTipImage32by32" type="ImageUrlType" />
    <xs:attribute name="ToolTipImage32by32Class" type="ImageClassType" />
    <xs:attribute name="ToolTipImage32by32Left" type="ImagePositionType" />
    <xs:attribute name="ToolTipImage32by32Top" type="ImagePositionType" />
    <xs:attribute name="ToolTipTitle" type="xs:string" />
    <xs:attribute name="ToolTipDescription" type="xs:string" />
    <xs:attribute name="ToolTipHelpKeyWord" type="xs:string" />
    <xs:attribute name="ToolTipSelectedItemTitle" type="xs:string" />
    <xs:attribute name="ToolTipShortcutKey" type="xs:string" />
    <xs:attribute name="Width" type="PixelLengthType" />
  </xs:complexType>

  <xs:complexType name="CommandUIType">
    <xs:sequence>
      <xs:choice minOccurs="1" maxOccurs="unbounded">
        <xs:element name="Ribbon" type="RibbonType" minOccurs="0" maxOccurs="1" />
        <xs:element name="QAT" type="QATType" minOccurs="0" maxOccurs="1" />
        <xs:element name="Jewel" type="JewelType" minOccurs="0" maxOccurs="1" />
        <xs:element name="Templates" type="TemplatesType" minOccurs="0" maxOccurs="1" />
      </xs:choice>
    </xs:sequence>
  </xs:complexType>

  <xs:element name="CommandUI" type="CommandUIType">
  </xs:element>

  <xs:complexType name="ContextualGroupType">
    <xs:sequence>
      <xs:element name="Tab" type="TabType" minOccurs="0" maxOccurs="unbounded" />
    </xs:sequence>
    <xs:attribute name="Color" type="ContextualColorType" />
    <xs:attribute name="Command" type="CommandType" />
    <xs:attribute name="ContextualGroupId" type="xs:string" />
    <xs:attribute name="Id" type="IdType" use="required" />
    <xs:attribute name="Sequence" type="SequenceType" />
    <xs:attribute name="Title" type="TitleType" />
  </xs:complexType>

  <xs:complexType name="ContextualTabsType">
    <xs:sequence>
      <xs:element name="ContextualGroup" type="ContextualGroupType" minOccurs="0" maxOccurs="unbounded"/>
    </xs:sequence>
    <xs:attribute name="Id" type="IdType" use="required" />
  </xs:complexType>

  <xs:complexType name="ControlRefType">
    <xs:attribute name="DisplayMode" type="DisplayModeType" />
    <xs:attribute name="TemplateAlias" type="TemplateAliasType" />
  </xs:complexType>

  <xs:complexType name="ControlsType">
    <xs:sequence>
      <xs:choice minOccurs="0" maxOccurs="unbounded">
        <xs:element name="Button" type="ButtonType" minOccurs="0" maxOccurs="unbounded" />
        <xs:element name="CheckBox" type="CheckBoxType" minOccurs="0" maxOccurs="unbounded" />
        <xs:element name="ComboBox" type="ComboBoxType" minOccurs="0" maxOccurs="unbounded" />
        <xs:element name="DropDown" type="DropDownType" minOccurs="0" maxOccurs="unbounded" />
        <xs:element name="FlyoutAnchor" type="FlyoutAnchorType" minOccurs="0" maxOccurs="unbounded" />
        <xs:element name="GalleryButton" type="GalleryButtonType" minOccurs="0" maxOccurs="unbounded" />
        <xs:element name="Label" type="LabelType" minOccurs="0" maxOccurs="unbounded" />
        <xs:element name="MRUSplitButton" type="MRUSplitButtonType" minOccurs="0" maxOccurs="unbounded" />
        <xs:element name="Spinner" type="SpinnerType" minOccurs="0" maxOccurs="unbounded" />
        <xs:element name="SplitButton" type="SplitButtonType" minOccurs="0" maxOccurs="unbounded" />
        <xs:element name="TextBox" type="TextBoxType" minOccurs="0" maxOccurs="unbounded" />
        <xs:element name="ToggleButton" type="ToggleButtonType" minOccurs="0" maxOccurs="unbounded" />
      </xs:choice>
    </xs:sequence>
    <xs:attribute name="Id" type="IdType" use="required" />
    <xs:attribute name="ToolTipImage32by32" type="ImageUrlType" />
    <xs:attribute name="ToolTipImage32by32Class" type="ImageClassType" />
    <xs:attribute name="ToolTipImage32by32Left" type="ImagePositionType" />
    <xs:attribute name="ToolTipImage32by32Top" type="ImagePositionType" />
    <xs:attribute name="ToolTipTitle" type="xs:string" />
    <xs:attribute name="ToolTipDescription" type="xs:string" />
    <xs:attribute name="ToolTipHelpKeyWord" type="xs:string" />
    <xs:attribute name="ToolTipShortcutKey" type="xs:string" />
    <xs:attribute name="ToolTipSelectedItemTitle" type="xs:string" />
  </xs:complexType>

  <xs:complexType name="DropDownType">
    <xs:sequence>
      <xs:element name="Menu" type="MenuType" minOccurs="0" maxOccurs="1"/>
    </xs:sequence>
    <xs:attribute name="AltArrow" type="AltType" />
    <xs:attribute name="Alt" type="AltType" />
    <xs:attribute name="CacheMenuVersions" type="xs:boolean" default="false" />
    <xs:attribute name="Command" type="CommandType" />
    <xs:attribute name="CommandMenuOpen" type="CommandType" />
    <xs:attribute name="CommandMenuClose" type="CommandType" />
    <xs:attribute name="CommandPreview" type="CommandType" />
    <xs:attribute name="CommandPreviewRevert" type="CommandType" />
    <xs:attribute name="InitialItem" type="MenuItemIdType" />
    <xs:attribute name="Id" type="IdType" use="required" />
    <xs:attribute name="PopulateDynamically" type="xs:boolean" default="false" />
    <xs:attribute name="PopulateQueryCommand" type="CommandType" />
    <xs:attribute name="PopulateOnlyOnce" type="xs:boolean" default="false" />
    <xs:attribute name="QueryCommand" type="CommandType" />
    <xs:attribute name="Sequence" type="SequenceType" />
    <xs:attribute name="TemplateAlias" type="TemplateAliasType" />
    <xs:attribute name="ToolTipImage32by32" type="ImageUrlType" />
    <xs:attribute name="ToolTipImage32by32Class" type="ImageClassType" />
    <xs:attribute name="ToolTipImage32by32Left" type="ImagePositionType" />
    <xs:attribute name="ToolTipImage32by32Top" type="ImagePositionType" />
    <xs:attribute name="ToolTipTitle" type="xs:string" />
    <xs:attribute name="ToolTipDescription" type="xs:string" />
    <xs:attribute name="ToolTipHelpKeyWord" type="xs:string" />
    <xs:attribute name="ToolTipShortcutKey" type="xs:string" />
    <xs:attribute name="ToolTipSelectedItemTitle" type="xs:string" />
    <xs:attribute name="Width" type="PixelLengthType" />
    <xs:attribute name="SelectedItemDisplayMode" type="DisplayModeType" />
  </xs:complexType>

  <xs:complexType name="FlyoutAnchorType">
    <xs:sequence>
      <xs:element name="Menu" type="MenuType" minOccurs="0" maxOccurs="1"/>
    </xs:sequence>
    <xs:attribute name="Alt" type="AltType" />
    <xs:attribute name="CacheMenuVersions" type="xs:boolean" default="false" />
    <xs:attribute name="Command" type="CommandType" />
    <xs:attribute name="CommandType" type="CommandTypeType" />
    <xs:attribute name="CommandMenuClose" type="CommandType" />
    <xs:attribute name="Id" type="IdType" use="required" />
    <xs:attribute name="Image16by16" type="ImageUrlType" />
    <xs:attribute name="Image16by16Class" type="ImageClassType" />
    <xs:attribute name="Image16by16Left" type="ImagePositionType" />
    <xs:attribute name="Image16by16Top" type="ImagePositionType" />
    <xs:attribute name="Image32by32" type="ImageUrlType" />
    <xs:attribute name="Image32by32Class" type="ImageClassType" />
    <xs:attribute name="Image32by32Left" type="ImagePositionType" />
    <xs:attribute name="Image32by32Top" type="ImagePositionType" />
    <xs:attribute name="LabelText" type="LabelTextType" />
    <xs:attribute name="ModernCommandType" type="ModernCommandTypeType" />
    <xs:attribute name="PopulateDynamically" type="xs:boolean" default="false" />
    <xs:attribute name="PopulateQueryCommand" type="CommandType" />
    <xs:attribute name="PopulateOnlyOnce" type="xs:boolean" default="false" />
    <xs:attribute name="Sequence" type="SequenceType" />
    <xs:attribute name="TemplateAlias" type="TemplateAliasType" />
    <xs:attribute name="ToolTipImage32by32" type="ImageUrlType" />
    <xs:attribute name="ToolTipImage32by32Class" type="ImageClassType" />
    <xs:attribute name="ToolTipImage32by32Left" type="ImagePositionType" />
    <xs:attribute name="ToolTipImage32by32Top" type="ImagePositionType" />
    <xs:attribute name="ToolTipTitle" type="xs:string" />
    <xs:attribute name="ToolTipDescription" type="xs:string" />
    <xs:attribute name="ToolTipHelpKeyWord" type="xs:string" />
    <xs:attribute name="ToolTipSelectedItemTitle" type="xs:string" />
    <xs:attribute name="ToolTipShortcutKey" type="xs:string" />
    <xs:attribute name="ModernImage" type="xs:string" />
  </xs:complexType>

  <xs:complexType name="GalleryType">
    <xs:sequence>
      <xs:element name="GalleryButton" type="GalleryButtonType" minOccurs="1" maxOccurs="unbounded" />
    </xs:sequence>
    <xs:attribute name="Command" type="CommandType" />
    <xs:attribute name="CommandPreview" type="CommandType" />
    <xs:attribute name="CommandRevert" type="CommandType" />
    <xs:attribute name="ElementDimensions" type="ElementDimensionsType" use="required" />
    <xs:attribute name="Id" type="IdType" use="required" />
    <xs:attribute name="QueryCommand" type="CommandType" />
    <xs:attribute name="Sequence" type="SequenceType" />
    <xs:attribute name="Width" type="xs:integer" use="required" />
  </xs:complexType>

  <xs:complexType name="GalleryButtonType">
    <xs:attribute name="Alt" type="AltType" />
    <xs:attribute name="Command" type="CommandType" />
    <xs:attribute name="CommandPreview" type="CommandType" />
    <xs:attribute name="CommandRevert" type="CommandType" />
    <xs:attribute name="CommandType" type="CommandTypeType" />
    <xs:attribute name="CommandValueId" type="xs:string" />
    <xs:attribute name="ElementDimensions" type="ElementDimensionsType" />
    <xs:attribute name="Id" type="IdType" use="required" />
    <xs:attribute name="Image" type="ImageUrlType" />
    <xs:attribute name="ImageClass" type="ImageClassType" />
    <xs:attribute name="ImageLeft" type="ImagePositionType" />
    <xs:attribute name="ImageTop" type="ImagePositionType" />
    <xs:attribute name="InnerHTML" type="HTMLType" />
    <xs:attribute name="MenuItemId" type="MenuItemIdType" />
    <xs:attribute name="QueryCommand" type="CommandType" />
    <xs:attribute name="Sequence" type="SequenceType" />
    <xs:attribute name="TemplateAlias" type="TemplateAliasType" />
    <xs:attribute name="ToolTipImage32by32" type="ImageUrlType" />
    <xs:attribute name="ToolTipImage32by32Class" type="ImageClassType" />
    <xs:attribute name="ToolTipImage32by32Left" type="ImagePositionType" />
    <xs:attribute name="ToolTipImage32by32Top" type="ImagePositionType" />
    <xs:attribute name="ToolTipTitle" type="xs:string" />
    <xs:attribute name="ToolTipDescription" type="xs:string" />
    <xs:attribute name="ToolTipHelpKeyWord" type="xs:string" />
    <xs:attribute name="ToolTipShortcutKey" type="xs:string" />
  </xs:complexType>

  <xs:complexType name="GroupTemplateType">
    <xs:sequence>
      <xs:element name="Layout" type="LayoutType" minOccurs="0" maxOccurs="unbounded" />
    </xs:sequence>
    <xs:attribute name="Id" type="IdType" use="required" />
    <xs:attribute name="ClassName" type="ClassNameType" />
  </xs:complexType>

  <xs:complexType name="GroupsType">
    <xs:sequence>
      <xs:element name="Group" type="GroupType" minOccurs="0" maxOccurs="unbounded" />
    </xs:sequence>
    <xs:attribute name="Id" type="IdType" use="required" />
  </xs:complexType>

  <xs:complexType name="GroupType">
    <xs:all>
      <xs:element name="Controls" type="ControlsType" minOccurs="1" maxOccurs="1" />
    </xs:all>
    <xs:attribute name="Command" type="CommandType" />
    <xs:attribute name="Description" type="DescriptionType" />
    <xs:attribute name="Id" type="IdType" use="required" />
    <xs:attribute name="Image32by32Popup" type="ImageUrlType" />
    <xs:attribute name="Image32by32PopupClass" type="ImageClassType" />
    <xs:attribute name="Image32by32PopupLeft" type="ImagePositionType" />
    <xs:attribute name="Image32by32PopupTop" type="ImagePositionType" />
    <xs:attribute name="PopupWidth" type="PixelLengthType" />
    <xs:attribute name="Sequence" type="SequenceType" />
    <xs:attribute name="Template" type="TemplateType" />
    <xs:attribute name="Title" type="TitleType" />
  </xs:complexType>

  <xs:complexType name="InsertTableType">
    <xs:attribute name="Alt" type="AltType" />
    <xs:attribute name="Command" type="CommandType" />
    <xs:attribute name="CommandType" type="CommandTypeType" />
    <xs:attribute name="CommandPreview" type="CommandType" />
    <xs:attribute name="CommandRevert" type="CommandType" />
    <xs:attribute name="Id" type="IdType" use="required" />
    <xs:attribute name="MenuSectionInitialTitle" type="xs:string" />
    <xs:attribute name="MenuSectionTitle" type="xs:string" />
    <xs:attribute name="Sequence" type="SequenceType" />
  </xs:complexType>

  <xs:complexType name="JewelType">
    <xs:sequence>
      <xs:element name="Menu" type="MenuType" minOccurs="0" maxOccurs="1"/>
    </xs:sequence>
    <xs:attribute name="Alt" type="AltType" />
    <xs:attribute name="CacheMenuVersions" type="xs:boolean" default="false" />
    <xs:attribute name="Command" type="CommandType" />
    <xs:attribute name="CommandMenuClose" type="CommandType" />
    <xs:attribute name="CommandMenuOpen" type="CommandType" />
    <xs:attribute name="Height" type="xs:integer" />
    <xs:attribute name="Id" type="IdType" use="required" />
    <xs:attribute name="ImageDownArrow" type="ImageUrlType" />
    <xs:attribute name="ImageDownArrowClass" type="ImageClassType" />
    <xs:attribute name="ImageDownArrowLeft" type="ImagePositionType" />
    <xs:attribute name="ImageDownArrowTop" type="ImagePositionType" />
    <xs:attribute name="ImageSideArrow" type="ImageUrlType" />
    <xs:attribute name="ImageSideArrowClass" type="ImageClassType" />
    <xs:attribute name="ImageSideArrowLeft" type="ImagePositionType" />
    <xs:attribute name="ImageSideArrowTop" type="ImagePositionType" />
    <xs:attribute name="ImageUpArrow" type="ImageUrlType" />
    <xs:attribute name="ImageUpArrowClass" type="ImageClassType" />
    <xs:attribute name="ImageUpArrowLeft" type="ImagePositionType" />
    <xs:attribute name="ImageUpArrowTop" type="ImagePositionType" />
    <xs:attribute name="Image" type="ImageUrlType" />
    <xs:attribute name="ImageClass" type="ImageClassType" />
    <xs:attribute name="ImageLeft" type="ImagePositionType" />
    <xs:attribute name="ImageTop" type="ImagePositionType" />
    <xs:attribute name="ImageHover" type="ImageUrlType" />
    <xs:attribute name="ImageHoverClass" type="ImageClassType" />
    <xs:attribute name="ImageHoverLeft" type="ImagePositionType" />
    <xs:attribute name="ImageHoverTop" type="ImagePositionType" />
    <xs:attribute name="ImageDown" type="ImageUrlType" />
    <xs:attribute name="ImageDownClass" type="ImageClassType" />
    <xs:attribute name="ImageDownLeft" type="ImagePositionType" />
    <xs:attribute name="ImageDownTop" type="ImagePositionType" />
    <xs:attribute name="ImageLeftSide" type="ImageUrlType" />
    <xs:attribute name="ImageLeftSideClass" type="ImageClassType" />
    <xs:attribute name="ImageLeftSideLeft" type="ImagePositionType" />
    <xs:attribute name="ImageLeftSideTop" type="ImagePositionType" />
    <xs:attribute name="ImageLeftSideWidth" type="xs:integer" />
    <xs:attribute name="ImageLeftSideHover" type="ImageUrlType" />
    <xs:attribute name="ImageLeftSideHoverClass" type="ImageClassType" />
    <xs:attribute name="ImageLeftSideHoverLeft" type="ImagePositionType" />
    <xs:attribute name="ImageLeftSideHoverTop" type="ImagePositionType" />
    <xs:attribute name="ImageLeftSideDown" type="ImageUrlType" />
    <xs:attribute name="ImageLeftSideDownClass" type="ImageClassType" />
    <xs:attribute name="ImageLeftSideDownLeft" type="ImagePositionType" />
    <xs:attribute name="ImageLeftSideDownTop" type="ImagePositionType" />
    <xs:attribute name="ImageRightSide" type="ImageUrlType" />
    <xs:attribute name="ImageRightSideClass" type="ImageClassType" />
    <xs:attribute name="ImageRightSideLeft" type="ImagePositionType" />
    <xs:attribute name="ImageRightSideTop" type="ImagePositionType" />
    <xs:attribute name="ImageRightSideWidth" type="xs:integer" />
    <xs:attribute name="ImageRightSideHover" type="ImageUrlType" />
    <xs:attribute name="ImageRightSideHoverClass" type="ImageClassType" />
    <xs:attribute name="ImageRightSideHoverLeft" type="ImagePositionType" />
    <xs:attribute name="ImageRightSideHoverTop" type="ImagePositionType" />
    <xs:attribute name="ImageRightSideDown" type="ImageUrlType" />
    <xs:attribute name="ImageRightSideDownClass" type="ImageClassType" />
    <xs:attribute name="ImageRightSideDownLeft" type="ImagePositionType" />
    <xs:attribute name="ImageRightSideDownTop" type="ImagePositionType" />
    <xs:attribute name="LabelCss" type="LabelCssType" />
    <xs:attribute name="LabelText" type="LabelTextType" />
    <xs:attribute name="PopulateDynamically" type="xs:boolean" default="false" />
    <xs:attribute name="PopulateQueryCommand" type="CommandType" />
    <xs:attribute name="PopulateOnlyOnce" type="xs:boolean" default="false" />
  </xs:complexType>

  <xs:complexType name="LabelType">
    <xs:attribute name="ForId" type="xs:string" />
    <xs:attribute name="Id" type="IdType" use="required" />
    <xs:attribute name="LabelText" type="LabelTextType" />
    <xs:attribute name="Image16by16" type="ImageUrlType" />
    <xs:attribute name="Image16by16Class" type="ImageClassType" />
    <xs:attribute name="Image16by16Left" type="ImagePositionType" />
    <xs:attribute name="Image16by16Top" type="ImagePositionType" />
    <xs:attribute name="Sequence" type="SequenceType" />
    <xs:attribute name="TemplateAlias" type="TemplateAliasType" />
    <xs:attribute name="QueryCommand" type="CommandType" />
    <xs:attribute name="Command" type="CommandType" />
    <xs:attribute name="ModernImage" type="xs:string" />
  </xs:complexType>

  <xs:complexType name="LayoutType">
    <xs:sequence>
      <xs:choice minOccurs="0" maxOccurs="unbounded">
        <xs:element name="Section" type="SectionType" minOccurs="0" maxOccurs="unbounded" />
        <xs:element name="OverflowSection" type="OverflowSectionType" minOccurs="0" maxOccurs="unbounded" />
      </xs:choice>
    </xs:sequence>
    <xs:attribute name="Title" type="TitleType" use="required" />
    <xs:attribute name="LayoutTitle" type="TitleType" />
  </xs:complexType>

  <xs:complexType name="MaxSizeType">
    <xs:attribute name="GroupId" type="IdType" use="required" />
    <xs:attribute name="Id" type="IdType" use="required" />
    <xs:attribute name="Sequence" type="SequenceType" />
    <xs:attribute name="Size" type="SizeType" use="required" />
  </xs:complexType>

  <xs:complexType name="MenuType">
    <xs:sequence>
      <xs:element name="MenuSection" type="MenuSectionType" minOccurs="1" maxOccurs="unbounded" />
    </xs:sequence>
    <xs:attribute name="Id" type="IdType" use="required" />
    <xs:attribute name="MaxWidth" type="PixelLengthType" />
  </xs:complexType>

  <xs:complexType name="MenuSectionType">
    <xs:choice minOccurs="1" maxOccurs="1">
      <xs:element name="Controls" type="MenuSectionControlsType" minOccurs="1" maxOccurs="1" />
      <xs:element name="Gallery" type="GalleryType" minOccurs="1" maxOccurs="1" />
    </xs:choice>
    <xs:attribute name="Id" type="IdType" use="required" />
    <xs:attribute name="Title" type="TitleType"/>
    <xs:attribute name="Scrollable" type="xs:boolean" default="false"/>
    <xs:attribute name="Sequence" type="SequenceType" />
    <xs:attribute name="MaxHeight" type="PixelLengthType" />
    <xs:attribute name="DisplayMode" type="DisplayModeType" default="Menu" />
  </xs:complexType>

  <xs:complexType name="MenuSectionControlsType">
    <xs:sequence>
      <xs:choice minOccurs="0" maxOccurs="unbounded">
        <xs:element name="ToggleButton" type="ToggleButtonType" minOccurs="0" maxOccurs="unbounded" />
        <xs:element name="Button" type="ButtonType" minOccurs="0" maxOccurs="unbounded" />
        <xs:element name="ColorPicker" type="ColorPickerType" minOccurs="0" maxOccurs="unbounded" />
        <xs:element name="FlyoutAnchor" type="FlyoutAnchorType" minOccurs="0" maxOccurs="unbounded" />
        <xs:element name="InsertTable" type="InsertTableType" minOccurs="0" maxOccurs="unbounded" />
      </xs:choice>
    </xs:sequence>
    <xs:attribute name="Id" type="IdType" use="required" />
  </xs:complexType>

  <xs:complexType name="MRUSplitButtonType">
    <xs:sequence>
      <xs:element name="Menu" type="MenuType" minOccurs="0" maxOccurs="1"/>
    </xs:sequence>
    <xs:attribute name="Alt" type="AltType" />
    <xs:attribute name="CacheMenuVersions" type="xs:boolean" default="false" />
    <xs:attribute name="Command" type="CommandType" />
    <xs:attribute name="CommandMenuOpen" type="CommandType" />
    <xs:attribute name="CommandMenuClose" type="CommandType" />
    <xs:attribute name="CommandPreview" type="CommandType" />
    <xs:attribute name="CommandPreviewRevert" type="CommandType" />
    <xs:attribute name="Id" type="IdType" use="required" />
    <xs:attribute name="InitialItem" type="MenuItemIdType" use="required" />
    <xs:attribute name="MenuAlt" type="AltType" />
    <xs:attribute name="MenuCommand" type="CommandType" />
    <xs:attribute name="PopulateDynamically" type="xs:boolean" default="false" />
    <xs:attribute name="PopulateQueryCommand" type="CommandType" />
    <xs:attribute name="PopulateOnlyOnce" type="xs:boolean" default="false" />
    <xs:attribute name="Sequence" type="SequenceType" />
    <xs:attribute name="QueryCommand" type="CommandType" />
    <xs:attribute name="TemplateAlias" type="TemplateAliasType" />
    <xs:attribute name="ToolTipImage32by32" type="ImageUrlType" />
    <xs:attribute name="ToolTipImage32by32Class" type="ImageClassType" />
    <xs:attribute name="ToolTipImage32by32Left" type="ImagePositionType" />
    <xs:attribute name="ToolTipImage32by32Top" type="ImagePositionType" />
    <xs:attribute name="ToolTipTitle" type="xs:string" />
    <xs:attribute name="ToolTipDescription" type="xs:string" />
    <xs:attribute name="ToolTipHelpKeyWord" type="xs:string" />
    <xs:attribute name="ToolTipSelectedItemTitle" type="xs:string" />
    <xs:attribute name="ToolTipShortcutKey" type="xs:string" />
  </xs:complexType>

  <xs:complexType name="LowScaleWarningType">
    <xs:attribute name="Id" type="IdType" use="required" />
    <xs:attribute name="Message" type="xs:string" />
    <xs:attribute name="Sequence" type="SequenceType" />
  </xs:complexType>

  <xs:complexType name="OverflowAreaType">
    <xs:attribute name="DisplayMode" type="DisplayModeType" />
    <xs:attribute name="TemplateAlias" type="TemplateAliasType" />
  </xs:complexType>

  <xs:complexType name="OverflowSectionType">
    <xs:attribute name="DisplayMode" type="DisplayModeType" />
    <xs:attribute name="DividerAfter" type="xs:boolean" />
    <xs:attribute name="DividerBefore" type="xs:boolean" />
    <xs:attribute name="TemplateAlias" type="TemplateAliasType" />
    <xs:attribute name="Type" type="SectionTypeType" />
  </xs:complexType>

  <xs:complexType name="QATType">
    <xs:sequence>
      <xs:element name="Controls" type="ControlsType" minOccurs="1" maxOccurs="1" />
    </xs:sequence>
    <xs:attribute name="Id" type="IdType" use="required" />
    <xs:attribute name="ImageDownArrow" type="ImageUrlType" />
    <xs:attribute name="ImageDownArrowClass" type="ImageClassType" />
    <xs:attribute name="ImageDownArrowLeft" type="ImagePositionType" />
    <xs:attribute name="ImageDownArrowTop" type="ImagePositionType" />
    <xs:attribute name="ImageSideArrow" type="ImageUrlType" />
    <xs:attribute name="ImageSideArrowClass" type="ImageClassType" />
    <xs:attribute name="ImageSideArrowLeft" type="ImagePositionType" />
    <xs:attribute name="ImageSideArrowTop" type="ImagePositionType" />
    <xs:attribute name="ImageUpArrow" type="ImageUrlType" />
    <xs:attribute name="ImageUpArrowClass" type="ImageClassType" />
    <xs:attribute name="ImageUpArrowLeft" type="ImagePositionType" />
    <xs:attribute name="ImageUpArrowTop" type="ImagePositionType" />
  </xs:complexType>

  <xs:complexType name="RibbonTemplatesType">
    <xs:sequence>
      <xs:element name="GroupTemplate" type="GroupTemplateType" minOccurs="0" maxOccurs="unbounded" />
    </xs:sequence>
    <xs:attribute name="Id" type="IdType" use="required" />
  </xs:complexType>

  <xs:complexType name="RibbonType">
    <xs:sequence>
      <xs:element name="Tabs" type="TabsType" minOccurs="1" maxOccurs="1" />
      <xs:element name="ContextualTabs" type="ContextualTabsType" minOccurs="1" maxOccurs="1" />
    </xs:sequence>
    <xs:attribute name="Id" type="IdType" use="required" />
    <xs:attribute name="Image32by32GroupPopupDefault" type="ImageUrlType" />
    <xs:attribute name="Image32by32GroupPopupDefaultClass" type="ImageClassType" />
    <xs:attribute name="Image32by32GroupPopupDefaultLeft" type="ImagePositionType" />
    <xs:attribute name="Image32by32GroupPopupDefaultTop" type="ImagePositionType" />
    <xs:attribute name="ImageDownArrow" type="ImageUrlType" />
    <xs:attribute name="ImageDownArrowClass" type="ImageClassType" />
    <xs:attribute name="ImageDownArrowLeft" type="ImagePositionType" />
    <xs:attribute name="ImageDownArrowTop" type="ImagePositionType" />
    <xs:attribute name="ImageSideArrow" type="ImageUrlType" />
    <xs:attribute name="ImageSideArrowClass" type="ImageClassType" />
    <xs:attribute name="ImageSideArrowLeft" type="ImagePositionType" />
    <xs:attribute name="ImageSideArrowTop" type="ImagePositionType" />
    <xs:attribute name="ImageUpArrow" type="ImageUrlType" />
    <xs:attribute name="ImageUpArrowClass" type="ImageClassType" />
    <xs:attribute name="ImageUpArrowLeft" type="ImagePositionType" />
    <xs:attribute name="ImageUpArrowTop" type="ImagePositionType" />
    <xs:attribute name="RootEventCommand" type="CommandType" />
    <xs:attribute name="TabSwitchCommand" type="CommandType" />
    <xs:attribute name="ScaleCommand" type="CommandType" />
    <xs:attribute name="TextDirection" type="TextDirectionType" />
    <xs:attribute name="ToolTipFooterText" type="xs:string" />
    <xs:attribute name="ToolTipFooterImage16by16" type="ImageUrlType" />
    <xs:attribute name="ToolTipFooterImage16by16Class" type="ImageClassType" />
    <xs:attribute name="ToolTipFooterImage16by16Left" type="ImagePositionType" />
    <xs:attribute name="ToolTipFooterImage16by16Top" type="ImagePositionType" />
    <xs:attribute name="ToolTipDisabledCommandImage16by16" type="ImageUrlType" />
    <xs:attribute name="ToolTipDisabledCommandImage16by16Class" type="ImageClassType" />
    <xs:attribute name="ToolTipDisabledCommandImage16by16Left" type="ImagePositionType" />
    <xs:attribute name="ToolTipDisabledCommandImage16by16Top" type="ImagePositionType" />
    <xs:attribute name="ToolTipDisabledCommandDescription" type="xs:string" />    
    <xs:attribute name="ToolTipDisabledCommandTitle" type="xs:string" />
    <xs:attribute name="ToolTipDisabledCommandHelpKey" type="xs:string" />
    <xs:attribute name="ToolTipHelpCommand" type="xs:string" />
    <xs:attribute name="ToolTipSelectedItemTitlePrefix" type="xs:string" />      
    <xs:attribute name="ShortcutKeyJumpToRibbon_Ctrl" type="xs:string" />
    <xs:attribute name="ShortcutKeyJumpToRibbon_Alt" type="xs:string" />
    <xs:attribute name="ShortcutKeyJumpToRibbon_Shift" type="xs:string" />
    <xs:attribute name="ShortcutKeyJumpToRibbon_AccessKey" type="xs:string" />
    <xs:attribute name="ShortcutKeyJumpToFirstControl_Ctrl" type="xs:string" />
    <xs:attribute name="ShortcutKeyJumpToFirstControl_Alt" type="xs:string" />
    <xs:attribute name="ShortcutKeyJumpToFirstControl_Shift" type="xs:string" />
    <xs:attribute name="ShortcutKeyJumpToFirstControl_AccessKey" type="xs:string" />
    <xs:attribute name="ATContextualTabText" type="xs:string" />
    <xs:attribute name="ATTabPositionText" type="xs:string" />
    <xs:attribute name="NavigationHelpText" type="xs:string" />
  </xs:complexType>

  <xs:complexType name="RowType">
    <xs:sequence>
      <xs:choice minOccurs="0" maxOccurs="unbounded">
        <xs:element name="ControlRef" type="ControlRefType" minOccurs="0" maxOccurs="unbounded" />
        <xs:element name="Strip" type="StripType" minOccurs="0" maxOccurs="unbounded" />
        <xs:element name="OverflowArea" type="OverflowAreaType" minOccurs="0" maxOccurs="unbounded" />
      </xs:choice>
    </xs:sequence>
  </xs:complexType>

  <xs:complexType name="ScaleType">
    <xs:attribute name="GroupId" type="IdType" use="required" />
    <xs:attribute name="Id" type="IdType" use="required" />
    <xs:attribute name="Sequence" type="SequenceType" />
    <xs:attribute name="Size" type="SizeType" use="required" />
    <xs:attribute name="PopupSize" type="SizeType" />
  </xs:complexType>

  <xs:complexType name="ScalingType">
    <xs:sequence>
      <xs:element name="MaxSize" type="MaxSizeType" minOccurs="0" maxOccurs="unbounded"/>
      <xs:choice minOccurs="0" maxOccurs="unbounded">
        <xs:element name="Scale" type="ScaleType" minOccurs="0" maxOccurs="1"/>
        <xs:element name="LowScaleWarning" type="LowScaleWarningType" minOccurs="0" maxOccurs="1"/>
      </xs:choice>
    </xs:sequence>
    <xs:attribute name="Id" type="IdType" use="required" />
  </xs:complexType>

  <xs:complexType name="SectionType">
    <xs:sequence>
      <xs:element name="Row" type="RowType" minOccurs="0" maxOccurs="3" />
    </xs:sequence>
    <xs:attribute name="Type" type="SectionTypeType" />
    <xs:attribute name="Alignment" type="SectionAlignmentType" />
  </xs:complexType>

  <xs:complexType name="SpinnerType">
    <xs:sequence>
      <xs:element name="Unit" type="UnitType" minOccurs="1" maxOccurs="unbounded" />
    </xs:sequence>
    <xs:attribute name="AccelerationInterval" type="xs:integer" />
    <xs:attribute name="AltDownArrow" type="AltType" />
    <xs:attribute name="AltUpArrow" type="AltType" />
    <xs:attribute name="Command" type="CommandType" />
    <xs:attribute name="DefaultUnit" type="UnitNameType" />
    <xs:attribute name="DefaultValue" type="ValueType" />
    <xs:attribute name="Id" type="IdType" use="required" />
    <xs:attribute name="ImeEnabled" type="xs:boolean" />
    <xs:attribute name="MultiplierInterval" type="xs:integer" />
    <xs:attribute name="QueryCommand" type="CommandType" />
    <xs:attribute name="Sequence" type="SequenceType" />
    <xs:attribute name="TemplateAlias" type="TemplateAliasType" />
    <xs:attribute name="ToolTipImage32by32" type="ImageUrlType" />
    <xs:attribute name="ToolTipImage32by32Class" type="ImageClassType" />
    <xs:attribute name="ToolTipImage32by32Left" type="ImagePositionType" />
    <xs:attribute name="ToolTipImage32by32Top" type="ImagePositionType" />
    <xs:attribute name="ToolTipTitle" type="xs:string" />
    <xs:attribute name="ToolTipDescription" type="xs:string" />
    <xs:attribute name="ToolTipHelpKeyWord" type="xs:string" />
    <xs:attribute name="ToolTipShortcutKey" type="xs:string" />
  </xs:complexType>

  <xs:complexType name="SplitButtonType">
    <xs:sequence>
      <xs:element name="Menu" type="MenuType" minOccurs="0" maxOccurs="1"/>
    </xs:sequence>
    <xs:attribute name="Alt" type="AltType" />
    <xs:attribute name="CacheMenuVersions" type="xs:boolean" default="false" />
    <xs:attribute name="Command" type="CommandType" />
    <xs:attribute name="CommandMenuOpen" type="CommandType" />
    <xs:attribute name="CommandMenuClose" type="CommandType" />
    <xs:attribute name="CommandType" type="CommandTypeType" />
    <xs:attribute name="Id" type="IdType" use="required" />
    <xs:attribute name="Image32by32" type="ImageUrlType" />
    <xs:attribute name="Image32by32Class" type="ImageClassType" />
    <xs:attribute name="Image32by32Left" type="ImagePositionType" />
    <xs:attribute name="Image32by32Top" type="ImagePositionType" />
    <xs:attribute name="Image16by16" type="ImageUrlType" />
    <xs:attribute name="Image16by16Class" type="ImageClassType" />
    <xs:attribute name="Image16by16Left" type="ImagePositionType" />
    <xs:attribute name="Image16by16Top" type="ImagePositionType" />
    <xs:attribute name="LabelText" type="LabelTextType" />
    <xs:attribute name="MenuAlt" type="AltType" />
    <xs:attribute name="MenuCommand" type="CommandType" />
    <xs:attribute name="PopulateDynamically" type="xs:boolean" default="false" />
    <xs:attribute name="PopulateQueryCommand" type="CommandType" />
    <xs:attribute name="PopulateOnlyOnce" type="xs:boolean" default="false" />
    <xs:attribute name="Sequence" type="SequenceType" />
    <xs:attribute name="TemplateAlias" type="TemplateAliasType" />
    <xs:attribute name="ToolTipImage32by32" type="ImageUrlType" />
    <xs:attribute name="ToolTipImage32by32Class" type="ImageClassType" />
    <xs:attribute name="ToolTipImage32by32Left" type="ImagePositionType" />
    <xs:attribute name="ToolTipImage32by32Top" type="ImagePositionType" />
    <xs:attribute name="ToolTipTitle" type="xs:string" />
    <xs:attribute name="ToolTipDescription" type="xs:string" />
    <xs:attribute name="ToolTipHelpKeyWord" type="xs:string" />
    <xs:attribute name="ToolTipSelectedItemTitle" type="xs:string" />
    <xs:attribute name="ToolTipShortcutKey" type="xs:string" />
    <xs:attribute name="ModernImage" type="xs:string" />
  </xs:complexType>

  <xs:complexType name="StripType">
    <xs:sequence>
      <xs:element name="ControlRef" type="ControlRefType" minOccurs="0" maxOccurs="unbounded" />
    </xs:sequence>
  </xs:complexType>

  <xs:complexType name="TabType">
    <xs:sequence>
      <xs:element name="Scaling" type="ScalingType" minOccurs="1" maxOccurs="1" />
      <xs:element name="Groups" type="GroupsType" minOccurs="1" maxOccurs="1" />
    </xs:sequence>
    <xs:attribute name="Command" type="CommandType" />
    <xs:attribute name="CssClass" type="ClassNameType" />
    <xs:attribute name="Description" type="DescriptionType" />
    <xs:attribute name="Id" type="IdType" use="required" />
    <xs:attribute name="Sequence" type="SequenceType" />
    <xs:attribute name="Title" type="TitleType" />
  </xs:complexType>

  <xs:complexType name="TabsType">
    <xs:sequence>
      <xs:element name="Tab" type="TabType" minOccurs="0" maxOccurs="unbounded" />
    </xs:sequence>
    <xs:attribute name="Id" type="IdType" use="required" />
  </xs:complexType>

  <xs:complexType name="TemplatesType">
    <xs:all>
      <xs:element name="RibbonTemplates" type="RibbonTemplatesType" />
    </xs:all>
  </xs:complexType>

  <xs:complexType name="TextBoxType">
    <xs:attribute name="Command" type="CommandType" />
    <xs:attribute name="Id" type="IdType" use="required" />
    <xs:attribute name="ImeEnabled" type="xs:boolean" />
    <xs:attribute name="MaxLength" type="xs:integer" />
    <xs:attribute name="QueryCommand" type="CommandType" />
    <xs:attribute name="Sequence" type="SequenceType" />
    <xs:attribute name="ShowAsLabel" type="xs:boolean" />
    <xs:attribute name="TemplateAlias" type="TemplateAliasType" />
    <xs:attribute name="ToolTipImage32by32" type="ImageUrlType" />
    <xs:attribute name="ToolTipImage32by32Class" type="ImageClassType" />
    <xs:attribute name="ToolTipImage32by32Left" type="ImagePositionType" />
    <xs:attribute name="ToolTipImage32by32Top" type="ImagePositionType" />
    <xs:attribute name="ToolTipTitle" type="xs:string" />
    <xs:attribute name="ToolTipDescription" type="xs:string" />
    <xs:attribute name="ToolTipHelpKeyWord" type="xs:string" />
    <xs:attribute name="ToolTipShortcutKey" type="xs:string" />
    <xs:attribute name="Width" type="PixelLengthType" />
  </xs:complexType>

  <xs:complexType name="ToggleButtonType">
    <xs:attribute name="Alt" type="AltType" />
    <xs:attribute name="Command" type="CommandType" />
    <xs:attribute name="CommandValueId" type="xs:string" />
    <xs:attribute name="Description" type="xs:string" />
    <xs:attribute name="Id" type="IdType" use="required" />
    <xs:attribute name="LabelCss" type="LabelCssType" />
    <xs:attribute name="LabelText" type="LabelTextType" />
    <xs:attribute name="Image32by32" type="ImageUrlType" />
    <xs:attribute name="Image32by32Class" type="ImageClassType" />
    <xs:attribute name="Image32by32Left" type="ImagePositionType" />
    <xs:attribute name="Image32by32Top" type="ImagePositionType" />
    <xs:attribute name="Image16by16" type="ImageUrlType" />
    <xs:attribute name="Image16by16Class" type="ImageClassType" />
    <xs:attribute name="Image16by16Left" type="ImagePositionType" />
    <xs:attribute name="Image16by16Top" type="ImagePositionType" />
    <xs:attribute name="MenuItemId" type="MenuItemIdType" />
    <xs:attribute name="QueryCommand" type="CommandType" />
    <xs:attribute name="Sequence" type="SequenceType" />
    <xs:attribute name="TemplateAlias" type="TemplateAliasType" />
    <xs:attribute name="ToolTipImage32by32" type="ImageUrlType" />
    <xs:attribute name="ToolTipImage32by32Class" type="ImageClassType" />
    <xs:attribute name="ToolTipImage32by32Left" type="ImagePositionType" />
    <xs:attribute name="ToolTipImage32by32Top" type="ImagePositionType" />
    <xs:attribute name="ToolTipTitle" type="xs:string" />
    <xs:attribute name="ToolTipDescription" type="xs:string" />
    <xs:attribute name="ToolTipHelpKeyWord" type="xs:string" />
    <xs:attribute name="ToolTipShortcutKey" type="xs:string" />
    <xs:attribute name="ModernImage" type="xs:string" />
  </xs:complexType>

  <xs:complexType name="UnitType">
    <xs:sequence>
      <xs:element name="UnitAbbreviation" type="UnitAbbreviationType" minOccurs="1" maxOccurs="unbounded" />
    </xs:sequence>
    <xs:attribute name="Name" type="UnitNameType" />
    <xs:attribute name="MinimumValue" type="ValueType" />
    <xs:attribute name="MaximumValue" type="ValueType" />
    <xs:attribute name="DecimalDigits" type="xs:integer" />
    <xs:attribute name="Interval" type="xs:double" />
  </xs:complexType>

  <xs:complexType name="UnitAbbreviationType">
    <xs:attribute name="Sequence" type="SequenceType" />
    <xs:attribute name="Value" type="UnitNameType" />
  </xs:complexType>
</xs:schema>
```  
  
### See also  
 [Customize commands and the ribbon](customize-commands-ribbon.md)   
 [Ribbon Types Schema](ribbon-types-schema.md)   
 [Customization XML Reference](customization-xml-reference.md)


[!INCLUDE[footer-include](../../includes/footer-banner.md)]