---
title: "Ribbon core schema (model-driven apps)"
description: "The following is the schema definition for the ribbon core portion of an import/export customization file. It is included from the Customization Solutions File Schema."
author: clromano
ms.author: clromano
ms.date: 04/01/2022
ms.reviewer: jdaly
ms.topic: reference
ms.subservice: mda-developer
search.audienceType: 
  - developer
contributors: 
  - JimDaly
---
# Ribbon core schema

The following is the schema definition for the ribbon core portion of an import/export customization file. It is included from the [Customization solutions file schema](../data-platform/customization-solutions-file-schema.md). `RibbonCore.xsd` schema includes `RibbonTypes.xsd` and `RibbonWss.xsd` and you can find schema  in the `Schemas\9.0.0.2090\RibbonCore.xsd` folder when you download the Schemas zip file.

Download the [Schemas](https://download.microsoft.com/download/B/9/7/B97655A4-4E46-4E51-BA0A-C669106D563F/Schemas.zip).

For more information, see [Package and distribute extensions with solutions](../data-platform/introduction-solutions.md).

[!INCLUDE[cc-terminology](../data-platform/includes/cc-terminology.md)]
 
## Ribbon Core Schema  
  
```xml  
<?xml version="1.0" encoding="utf-8"?>
<xs:schema id="CrmRibbonCore" xmlns:xs="https://www.w3.org/2001/XMLSchema">
   <xs:include schemaLocation="RibbonTypes.xsd" />
   <xs:include schemaLocation="RibbonWSS.xsd" />

   <!-- Root Element-->
   <xs:element name="RibbonDiffXml" type="RibbonGlobalDiffXmlType" />
   <xs:element name="CommandDefinitions" type="CommandDefinitionsType" />
   <xs:element name="RuleDefinitions" type="RuleDefinitionsGlobalType" />
   <xs:element name="Templates" type="TemplatesType" />
   <xs:element name="CustomActions" type="CustomActionsType" />

   <xs:element name="UI" type="CommandUIType">
   </xs:element>
   
   <!-- Element Types -->
   <xs:complexType name="RibbonEntityDiffXmlType">
      <xs:choice minOccurs="1" maxOccurs="1">
         <xs:sequence>
            <xs:element name="CustomActions" minOccurs="0" maxOccurs="1" type="CustomActionsType" />
            <xs:element name="Templates" type="TemplatesType" minOccurs="0" maxOccurs="1" />
            <xs:element name="CommandDefinitions" minOccurs="0" maxOccurs="1" type="CommandDefinitionsType" />
            <xs:element name="RuleDefinitions" minOccurs="0" maxOccurs="1" type="RuleDefinitionsEntityType" />
            <xs:element name="LocLabels" minOccurs="0" maxOccurs="1" type="RibbonLocLabelsType" />
         </xs:sequence>
         <xs:sequence>
            <xs:element name="RibbonNotSupported" minOccurs="1" maxOccurs="1">
               <xs:complexType>
                  <xs:sequence />
               </xs:complexType>
            </xs:element>
         </xs:sequence>
      </xs:choice>
   </xs:complexType>

   <xs:complexType name="RibbonGlobalDiffXmlType">
      <xs:sequence>
         <xs:element name="CustomActions" minOccurs="0" maxOccurs="1" type="CustomActionsType" />
         <xs:element name="Templates" type="TemplatesType" minOccurs="0" maxOccurs="1" />
         <xs:element name="CommandDefinitions" minOccurs="0" maxOccurs="1" type="CommandDefinitionsType" />
         <xs:element name="RuleDefinitions" minOccurs="0" maxOccurs="1" type="RuleDefinitionsGlobalType" />
         <xs:element name="LocLabels" minOccurs="0" maxOccurs="1" type="RibbonLocLabelsType" />
      </xs:sequence>
   </xs:complexType>

   <xs:complexType name="CustomActionsType">
      <xs:choice minOccurs="0" maxOccurs="unbounded">
         <xs:element name="CustomAction" type="CustomActionType" />
         <xs:element name="HideCustomAction" type="HideCustomActionType" />
      </xs:choice>
   </xs:complexType>

   <xs:complexType name="CustomActionType">
      <xs:sequence>
         <xs:element name="CommandUIDefinition" minOccurs="1" maxOccurs="1">
            <xs:complexType>
               <xs:choice>
                  <xs:element name="Button" type="ButtonType" />
                  <xs:element name="CheckBox" type="CheckBoxType" />
                  <xs:element name="ComboBox" type="ComboBoxType" />
                  <xs:element name="ColorPicker" type="ColorPickerType" />
                  <xs:element name="ContextualGroup" type="ContextualGroupType" />
                  <!-- <xs:element name="ContextualTabs" type="ContextualTabsType" /> -->
                  <xs:element name="Controls" type="ControlsType" />
                  <xs:element name="DropDown" type="DropDownType" />
                  <xs:element name="FlyoutAnchor" type="FlyoutAnchorType" />
                  <xs:element name="Gallery" type="GalleryType" />
                  <xs:element name="GalleryButton" type="GalleryButtonType" />
                  <xs:element name="GroupTemplate" type="GroupTemplateType" />
                  <xs:element name="Group" type="GroupType" />
                  <xs:element name="Groups" type="GroupsType" />
                  <xs:element name="InsertTable" type="InsertTableType" />
                  <!-- <xs:element name="Jewel" type="JewelType" /> -->
                  <xs:element name="Label" type="LabelType" />
                  <xs:element name="MRUSplitButton" type="MRUSplitButtonType" />
                  <xs:element name="MaxSize" type="MaxSizeType" />
                  <xs:element name="Menu" type="MenuType" />
                  <xs:element name="MenuSection" type="MenuSectionType" />
                  <!-- <xs:element name="QAT" type="QATType" /> -->
                  <!-- <xs:element name="Ribbon" type="RibbonType" /> -->
                  <xs:element name="Scale" type="ScaleType" />
                  <xs:element name="Scaling" type="ScalingType" />
                  <xs:element name="Spinner" type="SpinnerType" />
                  <xs:element name="SplitButton" type="SplitButtonType" />
                  <xs:element name="Tab" type="TabType" />
                  <!-- <xs:element name="Tabs" type="TabsType" /> -->
                  <xs:element name="TextBox" type="TextBoxType" />
                  <xs:element name="ToggleButton" type="ToggleButtonType" />
               </xs:choice>
            </xs:complexType>
         </xs:element>
      </xs:sequence>
      <xs:attribute name="Id" type="xs:string" />
      <xs:attribute name="Location" type="xs:string" />
      <xs:attribute name="Sequence" type="xs:int" />
      <xs:attribute name="Title" type="xs:string" />
   </xs:complexType>

   <xs:complexType name="HideCustomActionType">
      <xs:attribute name="HideActionId" type="xs:string" />
      <xs:attribute name="Location" type="xs:string" />
      <xs:attribute name="Sequence" type="xs:int" />
      <xs:attribute name="Title" type="xs:string" />
   </xs:complexType>
</xs:schema>
```  
  
### See also  

[Customize commands and the ribbon](customize-commands-ribbon.md)   
[Ribbon core schema](ribbon-core-schema.md)   
[Ribbon types schema](ribbon-types-schema.md)   
[Ribbon WSS schema](ribbon-wss-schema.md)   
[Customization solutions file schema](../data-platform/customization-solutions-file-schema.md)


[!INCLUDE[footer-include](../../includes/footer-banner.md)]
