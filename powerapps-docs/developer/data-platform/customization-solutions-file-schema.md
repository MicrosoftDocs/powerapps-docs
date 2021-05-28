---
title: "Customization solutions file schema (Microsoft Dataverse) | Microsoft Docs"
description: "The following is the schema definition for an solution customization file used by Microsoft Dataverse."
ms.custom: ""
ms.date: 03/18/2021
ms.reviewer: "pehecke"
ms.service: powerapps
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
helpviewer_keywords: 
  - "schemas"
ms.assetid: 71e3e594-0240-4af1-99b4-135042b7a000
caps.latest.revision: 19
author: "shmcarth" # GitHub ID
ms.author: "jdaly"
manager: "ryjones"
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---

# Customization solutions file schema

[!INCLUDE[cc-terminology](includes/cc-terminology.md)]

The following is the schema definition for an import/export customization file from Microsoft Dataverse.

You can find schema in the `Schemas\9.0.0.2090\CustomizationsSolution.xsd` folder when you download the Schemas zip file.

Download the [Schemas](https://download.microsoft.com/download/B/9/7/B97655A4-4E46-4E51-BA0A-C669106D563F/Schemas.zip).

For more information, see [Solutions overview](../../maker/data-platform/solutions-overview.md)
  
## Schema  
  
```xml  
<?xml version="1.0"?>
<xs:schema xmlns:xs="https://www.w3.org/2001/XMLSchema" elementFormDefault="qualified" attributeFormDefault="unqualified">
	<xs:include schemaLocation="isv.config.xsd" />
	<xs:include schemaLocation="SiteMapType.xsd" />
	<xs:include schemaLocation="FormXml.xsd" />
	<xs:include schemaLocation="Fetch.xsd" />
	<xs:simpleType name="ObjectTypeCodeType">
		<xs:restriction base="xs:positiveInteger"></xs:restriction>
	</xs:simpleType>
	<xs:simpleType name="TrueFalseType">
		<xs:restriction base="xs:string">
			<xs:enumeration value="True" />
			<xs:enumeration value="False" />
		</xs:restriction>
	</xs:simpleType>
	<xs:simpleType name="GuidType">
		<xs:annotation>
			<xs:documentation xml:lang="en">
				The representation of a GUID, generally the id of an element.
			</xs:documentation>
		</xs:annotation>
		<xs:restriction base="xs:string">
			<xs:pattern value="\{?[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}\}?" />
		</xs:restriction>
	</xs:simpleType>
	<xs:simpleType name="LengthPositiveInteger">
		<xs:restriction base="xs:positiveInteger" />
	</xs:simpleType>
	<xs:simpleType name="LengthMax">
		<xs:restriction base="xs:string">
			<xs:pattern value="max" />
		</xs:restriction>
	</xs:simpleType>
	<xs:simpleType name="LengthMinusOne">
		<xs:restriction base="xs:string">
			<xs:pattern value="-1" />
		</xs:restriction>
	</xs:simpleType>
	<xs:simpleType name="LengthType">
		<xs:union memberTypes="LengthPositiveInteger LengthMax LengthMinusOne" />
	</xs:simpleType>
	<xs:simpleType name="PercentageType">
		<xs:restriction base="xs:string">
			<xs:pattern value="^(100|[0-9]{1,2})%$" />
		</xs:restriction>
	</xs:simpleType>
	<xs:simpleType name="OptionSetEnumType">
		<xs:restriction base="xs:string">
			<xs:enumeration value="picklist" />
			<xs:enumeration value="state" />
			<xs:enumeration value="status" />
			<xs:enumeration value="bit" />
		</xs:restriction>
	</xs:simpleType>
	<xs:simpleType name="CrmDataType">
		<xs:restriction base="xs:string">
			<xs:enumeration value="virtual" />
			<xs:enumeration value="primarykey" />
			<xs:enumeration value="uniqueidentifier" />
			<xs:enumeration value="char" />
			<xs:enumeration value="nchar" />
			<xs:enumeration value="varchar" />
			<xs:enumeration value="nvarchar" />
			<xs:enumeration value="ntext" />
			<xs:enumeration value="text" />
			<xs:enumeration value="numeric" />
			<xs:enumeration value="int" />
			<xs:enumeration value="smallint" />
			<xs:enumeration value="tinyint" />
			<xs:enumeration value="bigint" />
			<xs:enumeration value="binary" />
			<xs:enumeration value="varbinary" />
			<xs:enumeration value="image" />
			<xs:enumeration value="float" />
			<xs:enumeration value="decimal" />
			<xs:enumeration value="real" />
			<xs:enumeration value="money" />
			<xs:enumeration value="smallmoney" />
			<xs:enumeration value="bit" />
			<xs:enumeration value="timezone" />
			<xs:enumeration value="datetime" />
			<xs:enumeration value="smalldatetime" />
			<xs:enumeration value="timestamp" />
			<xs:enumeration value="lookup" />
			<xs:enumeration value="picklist" />
			<xs:enumeration value="multiselectpicklist" />
			<xs:enumeration value="partylist" />
			<xs:enumeration value="customer" />
			<xs:enumeration value="owner" />
			<xs:enumeration value="state" />
			<xs:enumeration value="status" />
			<xs:enumeration value="sql_variant" />
			<xs:enumeration value="phoneticguide" />
			<xs:enumeration value="HierarchyId" />
			<xs:enumeration value="managedproperty" />
		</xs:restriction>
	</xs:simpleType>
	<xs:simpleType name="CrmCascadeSecurityLinkType">
		<xs:restriction base="xs:string">
			<xs:enumeration value="ActiveOnly" />
			<xs:enumeration value="Cascade" />
			<xs:enumeration value="NoCascade" />
			<xs:enumeration value="UserOwned" />
		</xs:restriction>
	</xs:simpleType>
	<xs:simpleType name="CrmCascadeDeleteLinkType">
		<xs:restriction base="xs:string">
			<xs:enumeration value="Cascade" />
			<xs:enumeration value="NoCascade" />
			<xs:enumeration value="RemoveLink" />
			<xs:enumeration value="Restrict" />
		</xs:restriction>
	</xs:simpleType>
	<xs:simpleType name="NavPaneDisplayOptionType">
		<xs:restriction base="xs:string">
			<xs:enumeration value="UseCollectionName" />
			<xs:enumeration value="UseLabel" />
			<xs:enumeration value="DoNotDisplay" />
		</xs:restriction>
	</xs:simpleType>
	<xs:simpleType name="NavPaneAreaType">
		<xs:restriction base="xs:string">
			<xs:enumeration value="Details" />
			<xs:enumeration value="Sales" />
			<xs:enumeration value="Service" />
			<xs:enumeration value="Marketing" />
			<xs:enumeration value="InternetMarketing" />
			<xs:enumeration value="ProcessCenter" />
		</xs:restriction>
	</xs:simpleType>
	<xs:simpleType name="CrmEntityIconType">
		<xs:restriction base="xs:string">
			<xs:enumeration value="GridIcon" />
			<xs:enumeration value="NavigationIcon" />
			<xs:enumeration value="OutlookShortcutIcon" />
			<xs:enumeration value="WatermarkIcon" />
			<xs:enumeration value="LargeEntityIcon" />
			<xs:enumeration value="VectorIcon" />
		</xs:restriction>
	</xs:simpleType>
	<xs:simpleType name="EntityAttributeNameBaseType">
		<xs:restriction base="xs:string">
			<xs:minLength value="1" />
			<xs:maxLength value="50" />
		</xs:restriction>
	</xs:simpleType>
	<xs:simpleType name="EntityAttributeLocalizedNameBaseType">
		<xs:restriction base="xs:string">
			<xs:minLength value="1" />
		</xs:restriction>
	</xs:simpleType>
	<xs:simpleType name="EntityRelationshipTypeType">
		<xs:restriction base="xs:string">
			<xs:enumeration value="OneToMany" />
			<xs:enumeration value="ManyToMany" />
		</xs:restriction>
	</xs:simpleType>
	<xs:complexType name="EntityRelationshipRolesType">
		<xs:sequence>
			<xs:element name="EntityRelationshipRole" minOccurs="1" maxOccurs="2">
				<xs:complexType>
					<xs:sequence>
						<xs:element name="NavPaneDisplayOption" type="NavPaneDisplayOptionType" minOccurs="0" maxOccurs="1" />
						<xs:element name="NavPaneArea" type="NavPaneAreaType" minOccurs="0" maxOccurs="1" />
						<xs:element name="NavPaneOrder" type="xs:nonNegativeInteger" minOccurs="0" maxOccurs="1" />
						<xs:element name="NavigationPropertyName" type="xs:string" minOccurs="0" maxOccurs="1" />
						<xs:element name="CustomLabels" type="CustomLabelsType" minOccurs="0" maxOccurs="1" />
						<xs:element name="RelationshipRoleType" type="xs:nonNegativeInteger" minOccurs="0" maxOccurs="1" />
						<xs:element name="AssociationRoleOrdinal" type="xs:nonNegativeInteger" minOccurs="0" maxOccurs="1" />
					</xs:sequence>
				</xs:complexType>
			</xs:element>
		</xs:sequence>
	</xs:complexType>
	<xs:element name="LocalizedName" type="EntityAttributeLocalizedNameBaseType" />
	<xs:element name="LocalizedCollectionName" type="EntityAttributeLocalizedNameBaseType" />
	<xs:complexType name="EntityNameType">
		<xs:simpleContent>
			<xs:extension base="EntityAttributeNameBaseType">
				<xs:attribute name="LocalizedName" type="EntityAttributeLocalizedNameBaseType" use="required" />
			</xs:extension>
		</xs:simpleContent>
	</xs:complexType>
	<xs:complexType name="LocalizedCollectionNamesType">
		<xs:sequence>
			<xs:element name="LocalizedCollectionName" type="FieldXmlFieldUIType" minOccurs="0" maxOccurs="unbounded" />
		</xs:sequence>
	</xs:complexType>
	<xs:complexType name="CustomLabelsType">
		<xs:sequence>
			<xs:element name="CustomLabel" type="FieldXmlFieldUIType" minOccurs="0" maxOccurs="unbounded" />
		</xs:sequence>
	</xs:complexType>
	<xs:complexType name="LookupTypesType">
		<xs:sequence>
			<xs:element minOccurs="0" maxOccurs="unbounded" name="LookupType">
				<xs:complexType>
					<xs:simpleContent>
						<xs:extension base="xs:integer">
							<xs:attribute name="id" type="xs:string" use="required" />
						</xs:extension>
					</xs:simpleContent>
				</xs:complexType>
			</xs:element>
		</xs:sequence>
	</xs:complexType>
	<xs:complexType name="displaynamestype">
		<xs:sequence>
			<xs:element name="displayname" type="FieldXmlFieldUIType" minOccurs="0" maxOccurs="unbounded" />
		</xs:sequence>
	</xs:complexType>
	<xs:complexType name="statestype">
		<xs:sequence>
			<xs:element name="state" minOccurs="0" maxOccurs="unbounded">
				<xs:complexType>
					<xs:sequence>
						<xs:element name="labels" minOccurs="1" maxOccurs="1">
							<xs:complexType>
								<xs:sequence>
									<xs:element name="label" type="FieldXmlFieldUIType" minOccurs="1" maxOccurs="unbounded" />
								</xs:sequence>
							</xs:complexType>
						</xs:element>
						<xs:element name="Descriptions" type="DescriptionsType" minOccurs="0" maxOccurs="1" />
					</xs:sequence>
					<xs:attribute name="value" use="required" type="xs:integer" />
					<xs:attribute name="Color" type="xs:string"/>
					<xs:attribute name="defaultstatus" use="required" type="xs:integer" />
					<xs:attribute name="invariantname" use="required" type="xs:string" />
					<xs:attribute name="addedby" type="xs:string"></xs:attribute>
				</xs:complexType>
			</xs:element>
		</xs:sequence>
	</xs:complexType>
	<xs:complexType name="statusestype">
		<xs:sequence>
			<xs:element name="status" minOccurs="0" maxOccurs="unbounded">
				<xs:complexType>
					<xs:sequence>
						<xs:element name="labels" minOccurs="1" maxOccurs="1">
							<xs:complexType>
								<xs:sequence>
									<xs:element name="label" type="FieldXmlFieldUIType" minOccurs="1" maxOccurs="unbounded" />
								</xs:sequence>
							</xs:complexType>
						</xs:element>
						<xs:element name="Descriptions" type="DescriptionsType" minOccurs="0" maxOccurs="1" />
						<xs:element name="Colors" type="ColorsType" minOccurs="0" maxOccurs="1" />
					</xs:sequence>
					<xs:attribute name="value" use="required" type="xs:integer" />
					<xs:attribute name="Color" type="xs:string" />
					<xs:attribute name="state" type="xs:integer" />
					<xs:attribute name="defaultstatus" type="xs:integer" />
					<xs:attribute name="addedby" type="xs:string"></xs:attribute>
					<xs:attribute name="TransitionData" type="xs:string"></xs:attribute>
				</xs:complexType>
			</xs:element>
		</xs:sequence>
	</xs:complexType>
	<xs:complexType name="optionsetstype">
		<xs:sequence>
			<xs:element name="optionset" type="optionsettype" minOccurs="0" maxOccurs="unbounded" />
		</xs:sequence>
	</xs:complexType>
	<xs:complexType name="optionsettype">
		<xs:sequence>
			<xs:element name="OptionSetType" type="OptionSetEnumType" minOccurs="0" maxOccurs="1" />
			<xs:element name="IsGlobal" type="TrueFalse01Type" minOccurs="0" maxOccurs="1" />
			<xs:element name="IntroducedVersion" type="VersionType" minOccurs="0" maxOccurs="1" />
			<xs:element name="IsCustomizable" type="TrueFalse01Type" minOccurs="0" maxOccurs="1" />
			<xs:element name="ExternalTypeName" type="xs:string" minOccurs="0" maxOccurs="1" />
			<xs:element name="displaynames" type="displaynamestype" minOccurs="0" maxOccurs="1" />
			<xs:element name="Descriptions" type="DescriptionsType" minOccurs="0" maxOccurs="1" />
			<xs:element name="options" type="optionstype" minOccurs="0" maxOccurs="1" />
			<xs:element name="statuses" type="statusestype" minOccurs="0" maxOccurs="1" />
			<xs:element name="states" type="statestype" minOccurs="0" maxOccurs="1" />
		</xs:sequence>
		<xs:attribute name="Name" use="required" type="xs:string" />
		<xs:attribute name="localizedName" use="optional" type="xs:string" />
		<xs:attribute name="description" use="optional" type="xs:string" />
		<xs:attribute name="unmodified" use="optional" type="TrueFalse01Type" />
	</xs:complexType>
	<xs:complexType name="pluginassembliestype">
		<xs:sequence>
			<xs:element name="PluginAssembly" type="pluginassemblytype" minOccurs="0" maxOccurs="unbounded" />
		</xs:sequence>
	</xs:complexType>
	<xs:complexType name="pluginassemblytype">
		<xs:sequence>
			<xs:element name="Description" type="xs:string" minOccurs="0" maxOccurs="1" />
			<xs:element name="IsolationMode" type="xs:integer" minOccurs="0" maxOccurs="1" />
			<xs:element name="SourceType" type="xs:integer" minOccurs="0" maxOccurs="1" />
			<xs:element name="Path" type="xs:string" minOccurs="0" maxOccurs="1" />
			<xs:element name="Url" type="xs:string" minOccurs="0" maxOccurs="1" />
			<xs:element name="UserName" type="xs:string" minOccurs="0" maxOccurs="1" />
			<xs:element name="IntroducedVersion" type="VersionType" minOccurs="0" maxOccurs="1" />
			<xs:element name="IsCustomizable" type="TrueFalse01Type" minOccurs="0" maxOccurs="1" />
			<xs:element name="AuthType" type="xs:integer" minOccurs="0" maxOccurs="1" />
			<xs:element name="FileName" type="xs:string" minOccurs="0" maxOccurs="1" />
			<xs:element name="PluginTypes" type="plugintypestype" minOccurs="0" maxOccurs="1" />
			<xs:element name="IsHidden" type="TrueFalse01Type" minOccurs="0" maxOccurs="1" />
		</xs:sequence>
		<xs:attribute name="FullName" use="required" type="xs:string" />
		<xs:attribute name="PluginAssemblyId" use="optional" type="xs:string" />
		<xs:attribute name="CustomizationLevel" use="optional" type="xs:integer" />
		<xs:attribute name="unmodified" use="optional" type="TrueFalse01Type" />
	</xs:complexType>
	<xs:complexType name="plugintypestype">
		<xs:sequence>
			<xs:element name="PluginType" type="plugintypetype" minOccurs="0" maxOccurs="unbounded" />
		</xs:sequence>
	</xs:complexType>
	<xs:complexType name="plugintypetype">
		<xs:sequence>
			<xs:element name="Description" type="xs:string" minOccurs="0" maxOccurs="1" />
			<xs:element name="FriendlyName" type="xs:string" minOccurs="1" maxOccurs="1" />
			<xs:element name="WorkflowActivityGroupName" type="xs:string" minOccurs="0" maxOccurs="1" />
		</xs:sequence>
		<xs:attribute name="Name" use="optional" type="xs:string" />
		<xs:attribute name="AssemblyQualifiedName" use="required" type="xs:string" />
		<xs:attribute name="PluginTypeId" use="optional" type="xs:string" />
	</xs:complexType>
	<xs:complexType name="sdkmessageprocessingstepstype">
		<xs:sequence>
			<xs:element name="SdkMessageProcessingStep" type="sdkmessageprocessingsteptype" minOccurs="0" maxOccurs="unbounded" />
		</xs:sequence>
	</xs:complexType>
	<xs:complexType name="sdkmessageprocessingsteptype">
		<xs:sequence>
			<xs:element name="PluginTypeName" type="xs:string" minOccurs="0" maxOccurs="1" />
			<xs:element name="PluginTypeId" type="xs:string" minOccurs="0" maxOccurs="1" />
			<xs:element name="PrimaryEntity" type="xs:string" minOccurs="0" maxOccurs="1" />
			<xs:element name="SecondaryEntity" type="xs:string" minOccurs="0" maxOccurs="1" />
			<xs:element name="AsyncAutoDelete" type="TrueFalse01Type" minOccurs="0" maxOccurs="1" />
			<xs:element name="Configuration" type="xs:string" minOccurs="0" maxOccurs="1" />
			<xs:element name="Description" type="xs:string" minOccurs="0" maxOccurs="1" />
			<xs:element name="FilteringAttributes" type="xs:string" minOccurs="0" maxOccurs="1" />
			<xs:element name="ImpersonatingUserIdName" type="xs:string" minOccurs="0" maxOccurs="1" />
			<xs:element name="InvocationSource" type="xs:integer" minOccurs="0" maxOccurs="1" />
			<xs:element name="Mode" type="xs:integer" minOccurs="0" maxOccurs="1" />
			<xs:element name="Rank" type="xs:integer" minOccurs="0" maxOccurs="1" />
			<xs:element name="SdkMessageId" type="GuidType" minOccurs="0" maxOccurs="1" />
			<xs:element name="EventHandler" type="GuidType" minOccurs="0" maxOccurs="1" />
			<xs:element name="EventHandlerTypeCode" type="xs:integer" minOccurs="0" maxOccurs="1" />
			<xs:element name="Stage" type="xs:integer" minOccurs="0" maxOccurs="1" />
			<xs:element name="IsCustomizable" type="TrueFalse01Type" minOccurs="0" maxOccurs="1" />
			<xs:element name="IsHidden" type="TrueFalse01Type" minOccurs="0" maxOccurs="1" />
			<xs:element name="SupportedDeployment" type="xs:integer" minOccurs="0" maxOccurs="1" />
			<xs:element name="IntroducedVersion" type="VersionType" minOccurs="0" maxOccurs="1" />
			<xs:element name="SdkMessageProcessingStepImages" type="sdkmessageprocessingstepimagestype" minOccurs="0" maxOccurs="1" />
		</xs:sequence>
		<xs:attribute name="SdkMessageProcessingStepId" use="required" type="GuidType" />
		<xs:attribute name="Name" use="optional" type="xs:string" />
		<xs:attribute name="unmodified" use="optional" type="TrueFalse01Type" />
	</xs:complexType>
	<xs:complexType name="entitydatasourcestype">
		<xs:sequence>
			<xs:element name="EntityDataSource" type="entitydatasourcetype" minOccurs="0" maxOccurs="unbounded" />
		</xs:sequence>
	</xs:complexType>
	<xs:complexType name="entitydatasourcetype">
		<xs:sequence>
			<xs:element name="Name" type="xs:string" minOccurs="0" maxOccurs="1" />	  
			<xs:element name="ConnectionDefinition" type="xs:string" minOccurs="0" maxOccurs="1" />			
			<xs:element name="EntityDataProviderId" type="GuidType" minOccurs="1" maxOccurs="1" />
			<xs:element name="IsCustomizable" type="TrueFalse01Type" minOccurs="0" maxOccurs="1" />
	</xs:sequence>
		<xs:attribute name="EntityDataSourceId" use="required" type="GuidType" />
	</xs:complexType>
	<xs:complexType name="sdkmessageprocessingstepimagestype">
		<xs:sequence>
			<xs:element name="SdkMessageProcessingStepImage" type="sdkmessageprocessingstepimagetype" minOccurs="0" maxOccurs="unbounded" />
		</xs:sequence>
	</xs:complexType>
	<xs:complexType name="sdkmessageprocessingstepimagetype">
		<xs:sequence>
			<xs:element name="Description" type="xs:string" minOccurs="0" maxOccurs="1" />
			<xs:element name="SdkMessageProcessingStepImageId" type="GuidType" minOccurs="0" maxOccurs="1" />
			<xs:element name="Attributes" type="xs:string" minOccurs="0" maxOccurs="1" />
			<xs:element name="EntityAlias" type="xs:string" minOccurs="0" maxOccurs="1" />
			<xs:element name="ImageType" type="xs:integer" minOccurs="0" maxOccurs="1" />
			<xs:element name="MessagePropertyName" type="xs:string" minOccurs="0" maxOccurs="1" />
			<xs:element name="RelatedAttributeName" type="xs:string" minOccurs="0" maxOccurs="1" />
			<xs:element name="IsCustomizable" type="TrueFalse01Type" minOccurs="0" maxOccurs="1" />
			<xs:element name="IntroducedVersion" type="VersionType" minOccurs="0" maxOccurs="1" />
		</xs:sequence>
		<xs:attribute name="Name" use="optional" type="xs:string" />
	</xs:complexType>
	<xs:complexType name="serviceendpointstype">
		<xs:sequence>
			<xs:element name="ServiceEndpoint" type="serviceendpointtype" minOccurs="0" maxOccurs="unbounded" />
		</xs:sequence>
	</xs:complexType>
	<xs:complexType name="serviceendpointtype">
		<xs:sequence>
			<xs:element name="ConnectionMode" type="xs:integer" minOccurs="0" maxOccurs="1" />
			<xs:element name="Contract" type="xs:integer" minOccurs="0" maxOccurs="1" />
			<xs:element name="Description" type="xs:string" minOccurs="0" maxOccurs="1" />
			<xs:element name="Path" type="xs:string" minOccurs="0" maxOccurs="1" />
			<xs:element name="SolutionNamespace" type="xs:string" minOccurs="0" maxOccurs="1" />
			<xs:element name="UserClaim" type="xs:integer" minOccurs="0" maxOccurs="1" />
			<xs:element name="IsCustomizable" type="TrueFalse01Type" minOccurs="0" maxOccurs="1" />
			<xs:element name="AuthType" type="xs:integer" minOccurs="0" maxOccurs="1" />
			<xs:element name="MessageFormat" type="xs:integer" minOccurs="0" maxOccurs="1" />
			<xs:element name="NamespaceAddress" type="xs:string" minOccurs="0" maxOccurs="1" />
			<xs:element name="NamespaceFormat" type="xs:integer" minOccurs="0" maxOccurs="1" />
			<xs:element name="SASKeyName" type="xs:string" minOccurs="0" maxOccurs="1" />
			<xs:element name="Url" type="xs:string" minOccurs="0" maxOccurs="1" />
		</xs:sequence>
		<xs:attribute name="ServiceEndpointId" use="required" type="GuidType" />
		<xs:attribute name="Description" use="optional" type="xs:string" />
		<xs:attribute name="Name" use="optional" type="xs:string" />
		<xs:attribute name="unmodified" use="optional" type="TrueFalse01Type" />
	</xs:complexType>
	<xs:complexType name="webresourcestype">
		<xs:sequence>
			<xs:element name="WebResource" type="webresourcetype" minOccurs="0" maxOccurs="unbounded" />
		</xs:sequence>
	</xs:complexType>
	<xs:complexType name="webresourcetype">
		<xs:sequence>
			<xs:element name="WebResourceId" type="GuidType" minOccurs="1" maxOccurs="1" />
			<xs:element name="Name" type="xs:string" minOccurs="1" maxOccurs="1" />
			<xs:element name="DisplayName" type="xs:string" minOccurs="0" maxOccurs="1" />
			<xs:element name="Description" type="xs:string" minOccurs="0" maxOccurs="1" />
			<xs:element name="SilverlightVersion" type="xs:string" minOccurs="0" maxOccurs="1" />
			<xs:element name="LanguageCode" type="xs:integer" minOccurs="0" maxOccurs="1" />
			<xs:element name="WebResourceType" type="xs:integer" minOccurs="0" maxOccurs="1" />
			<xs:element name="IntroducedVersion" type="VersionType" minOccurs="0" maxOccurs="1" />
			<xs:element name="IsEnabledForMobileClient" type="TrueFalse01Type" minOccurs="0" maxOccurs="1" />
			<xs:element name="IsAvailableForMobileOffline" type="TrueFalse01Type" minOccurs="0" maxOccurs="1" />
			<xs:element name="DependencyXml" type="xs:string" minOccurs="0" maxOccurs="1" />
			<xs:element name="IsCustomizable" type="TrueFalse01Type" minOccurs="0" maxOccurs="1" />
			<xs:element name="CanBeDeleted" type="TrueFalse01Type" minOccurs="0" maxOccurs="1" />
			<xs:element name="IsHidden" type="TrueFalse01Type" minOccurs="0" maxOccurs="1" />
			<xs:element name="FileName" type="xs:string" minOccurs="0" maxOccurs="1" />
		</xs:sequence>
		<xs:attribute name="unmodified" use="optional" type="TrueFalse01Type" />
	</xs:complexType>
	<xs:complexType name="customcontrolstype">
		<xs:sequence>
			<xs:element name="CustomControl" type="customcontroltype" minOccurs="0" maxOccurs="unbounded" />
		</xs:sequence>
	</xs:complexType>
	<xs:complexType name="customcontroltype">
		<xs:sequence>
			<xs:element name="Name" type="xs:string" minOccurs="1" maxOccurs="1" />
			<xs:element name="FileName" type="xs:string" minOccurs="0" maxOccurs="1" />
		</xs:sequence>
	</xs:complexType>
	<xs:complexType name="optionstype">
		<xs:sequence>
			<xs:element name="option" minOccurs="0" maxOccurs="unbounded">
				<xs:complexType>
					<xs:sequence>
						<xs:element name="labels" minOccurs="1" maxOccurs="1">
							<xs:complexType>
								<xs:sequence>
									<xs:element name="label" type="FieldXmlFieldUIType" minOccurs="1" maxOccurs="unbounded" />
								</xs:sequence>
							</xs:complexType>
						</xs:element>
						<xs:element name="Descriptions" type="DescriptionsType" minOccurs="0" maxOccurs="1" />
						<xs:element name="Colors" type="ColorsType" minOccurs="0" maxOccurs="1" />
					</xs:sequence>
					<xs:attribute name="id" type="GuidType" />
					<xs:attribute name="value" use="required" type="xs:integer" />
					<xs:attribute name="ExternalValue" type="xs:string" />
					<xs:attribute name="Color" type="xs:string" />
					<xs:attribute name="addedby" type="xs:string" />
				</xs:complexType>
			</xs:element>
		</xs:sequence>
	</xs:complexType>
	<xs:simpleType name="CrmIdentifier">
		<xs:restriction base="xs:string">
			<xs:pattern value="[a-zA-Z0-9_]+" />
		</xs:restriction>
	</xs:simpleType>
	<xs:simpleType name="CrmClient">
		<xs:restriction base="xs:string">
			<xs:pattern value="((Outlook|Web|All|OutlookWorkstationClient|OutlookLaptopClient),?)+" />
		</xs:restriction>
	</xs:simpleType>
	<xs:simpleType name="CrmLicense">
		<xs:restriction base="xs:string">
			<xs:pattern value="((SmallBusiness|Professional|All),?)+" />
		</xs:restriction>
	</xs:simpleType>
	<xs:simpleType name="CrmPrivilegeId">
		<xs:restriction base="xs:string">
			<xs:pattern value="((Read|Write|Append|AppendTo|Create|Delete|Share|Assign|All|AllowQuickCampaign|LearningPath),?)+" />
		</xs:restriction>
	</xs:simpleType>
	<xs:complexType name="LookupType">
		<xs:simpleContent>
			<xs:extension base="GuidType">
				<xs:attribute name="name" type="xs:string" />
				<xs:attribute name="dsc" type="xs:nonNegativeInteger" />
			</xs:extension>
		</xs:simpleContent>
	</xs:complexType>
	<xs:element name="ImportExportXml">
		<xs:complexType>
			<xs:sequence>
				<xs:element name="Entities" type="EntitiesType" minOccurs="0" maxOccurs="1" />
				<xs:element name="Roles" type="RolesType" minOccurs="0" maxOccurs="1" />
				<xs:element name="Workflows" type="WorkflowsType" minOccurs="0" maxOccurs="1" />
				<xs:element name="FieldSecurityProfiles" type="FieldSecurityProfilesType" minOccurs="0" maxOccurs="1" />
				<xs:element name="Templates" type="CrmTemplatesType" minOccurs="0" maxOccurs="1" />
				<xs:element name="RibbonDiffXml" type="RibbonGlobalDiffXmlType" minOccurs="0" maxOccurs="1" />
				<xs:element name="IsvConfig" minOccurs="0" maxOccurs="1">
					<xs:complexType>
						<xs:sequence>
							<xs:element name="configuration" type="IsvConfigurationType" maxOccurs="1" />
						</xs:sequence>
					</xs:complexType>
				</xs:element>
				<xs:element name="RelationshipRoles" type="RelationshipRolesType" minOccurs="0" maxOccurs="1" />
				<xs:element name="ConnectionRoles" type="ConnectionRolesType" minOccurs="0" maxOccurs="1" />
				<xs:element name="SiteMap" minOccurs="0" maxOccurs="1">
					<xs:complexType>
						<xs:sequence>
							<xs:element name="SiteMap" type="SiteMapType" maxOccurs="1">
								<xs:unique name="AreaIdMustBeUnique">
									<xs:selector xpath="Area" />
									<xs:field xpath="@Id" />
								</xs:unique>
							</xs:element>
						</xs:sequence>
					</xs:complexType>
				</xs:element>
				<xs:element name="EntityMaps" type="EntityMapsType" minOccurs="0" maxOccurs="1" />
				<xs:element name="EntityRelationships" type="EntityRelationShipsType" minOccurs="0" maxOccurs="1" />
				<xs:element name="OrganizationSettings" type="OrganizationSettingsType" minOccurs="0" maxOccurs="1" />
				<xs:element name="optionsets" type="optionsetstype" minOccurs="0" maxOccurs="1" />
				<xs:element name="Reports" type="ReportsType" minOccurs="0" maxOccurs="1" />
				<xs:element name="RoutingRules" type="RoutingRulesType" minOccurs="0" maxOccurs="1" />
				<xs:element name="ChannelPropertyGroups" type="ChannelPropertyGroupsType" minOccurs="0" maxOccurs="1" />
				<xs:element name="ConvertRules" type="ConvertRulesType" minOccurs="0" maxOccurs="1" />
				<xs:element name="MobileOfflineProfiles" type="MobileOfflineProfilesType" minOccurs="0" maxOccurs="1" />
				<xs:element name="Slas" type="SlasType" minOccurs="0" maxOccurs="1" />
				<xs:element name="ChannelAccessProfiles" type="ChannelAccessProfilesType" minOccurs="0" maxOccurs="1" />
				<xs:element name="ChannelAccessProfileRules" type="ProfileRulesType" minOccurs="0" maxOccurs="1" />
				<xs:element name="Dashboards" type="DashboardsType" minOccurs="0" maxOccurs="1" />
				<xs:element name="InteractionCentricDashboards" type="InteractionCentricDashboardsType" minOccurs="0" maxOccurs="1" />
				<xs:element name="Dialogs" type="DialogsType" minOccurs="0" maxOccurs="1" />
				<xs:element name="WebResources" type="webresourcestype" minOccurs="0" maxOccurs="1" />
				<xs:element name="CustomControls" maxOccurs="1" minOccurs="0" type="customcontrolstype" />
				<xs:element name="SolutionPluginAssemblies" type="pluginassembliestype" minOccurs="0" maxOccurs="1" />
				<xs:element name="SdkMessageProcessingSteps" type="sdkmessageprocessingstepstype" minOccurs="0" maxOccurs="1" />
				<xs:element name="ServiceEndpoints" type="serviceendpointstype" minOccurs="0" maxOccurs="1" />
				<xs:element name="AppModuleSiteMaps" type="AppModuleSiteMapsType" minOccurs="0" maxOccurs="1" />
				<xs:element name="AppModules" type="AppModulesType" minOccurs="0" maxOccurs="1" />
				<xs:element name="EntityDataProviders" type="EntityDataProvidersType" minOccurs="0" maxOccurs="1" />
				<xs:element name="EntityDataSources" type="entitydatasourcestype" minOccurs="0" maxOccurs="1" />
				<xs:element name="Languages" type="LanguagesType" minOccurs="0" maxOccurs="1" />
				<xs:element name="GlobalSearchConfigurations" type="GlobalSearchConfigurationType" minOccurs="0" maxOccurs="1" />
				<xs:element name="StoredProcedures" type="StoredProceduresType" minOccurs="0" maxOccurs="1" />
			</xs:sequence>
		</xs:complexType>
	</xs:element>
	<xs:complexType name="LanguagesType">
		<xs:sequence>
			<xs:element name="Language" type="xs:nonNegativeInteger" minOccurs="1" maxOccurs="unbounded" />
		</xs:sequence>
	</xs:complexType>
	<xs:complexType name="GlobalSearchConfigurationType">
		<xs:choice minOccurs="0" maxOccurs="unbounded">
			<xs:element name="GlobalSearchConfiguration">
				<xs:complexType>
					<xs:sequence>
						<xs:element name="GlobalSearchConfigurationId" type="GuidType" minOccurs="0" maxOccurs="1" />
						<xs:element name="Name" type="xs:string" minOccurs="0" maxOccurs="1" />
						<xs:element name="PrimaryEntityOTC" type="xs:integer" minOccurs="0" maxOccurs="1" />
						<xs:element name="SearchProviderName" type="xs:string" minOccurs="0" maxOccurs="1" />
						<xs:element name="SearchProviderResultsPage" type="xs:string" minOccurs="0" maxOccurs="1" />
						<xs:element name="IsLocalized" type="TrueFalse01Type" minOccurs="0" maxOccurs="1" />
						<xs:element name="IsEnabled" type="TrueFalse01Type" minOccurs="0" maxOccurs="1"  />
						<xs:element name="IsSearchBoxVisible" type="TrueFalse01Type" minOccurs="0" maxOccurs="1" />
					</xs:sequence>
					<xs:attribute name="GlobalSearchConfigurationId" use="required" type="xs:string" />
					<xs:attribute name="Name" use="required" type="xs:string" />
				</xs:complexType>
			</xs:element>
		</xs:choice>
	</xs:complexType>
	<xs:complexType name="DependentType">
		<xs:attribute name="type" use="required" type="xs:string" />
		<xs:attribute name="name" use="required" type="xs:string" />
	</xs:complexType>
	<xs:complexType name="DependentsType">
		<xs:sequence>
			<xs:element name="Dependent" type="DependentType" minOccurs="0" maxOccurs="unbounded" />
		</xs:sequence>
	</xs:complexType>
	<xs:complexType name="EntitiesType">
		<xs:sequence>
			<xs:element name="Entity" minOccurs="0" maxOccurs="unbounded">
				<xs:complexType>
					<xs:all>
						<xs:element name="Name" minOccurs="1" maxOccurs="1">
							<xs:complexType>
								<xs:simpleContent>
									<xs:extension base="EntityNameType">
										<xs:attribute name="OriginalName" type="xs:string" use="required" />
									</xs:extension>
								</xs:simpleContent>
							</xs:complexType>
						</xs:element>
						<xs:element name="ObjectTypeCode" type="ObjectTypeCodeType" minOccurs="0" maxOccurs="1" />
						<xs:element name="EntityInfo" type="EntityInfoType" minOccurs="0" maxOccurs="1" />
						<xs:element name="FormXml" minOccurs="0" maxOccurs="1">
							<xs:complexType>
								<xs:sequence>
									<xs:element name="forms" type="SystemFormsType" minOccurs="0" maxOccurs="unbounded"></xs:element>
								</xs:sequence>
							</xs:complexType>
						</xs:element>
						<xs:element name="SavedQueries" type="SavedQueriesType" minOccurs="0" maxOccurs="1" />
						<xs:element name="Visualizations" type="VisualizationsType" minOccurs="0" maxOccurs="1" />
						<xs:element name="RibbonDiffXml" type="RibbonEntityDiffXmlType" minOccurs="0" maxOccurs="1" />
						<xs:element name="Icons" type="IconsType" minOccurs="0" maxOccurs="1" />
						<xs:element name="Strings" type="StringsType" minOccurs="0" maxOccurs="1" />
						<xs:element name="HierarchyRules" type="HierarchyRulesType" minOccurs="0" maxOccurs="1" />
						<xs:element name="CustomControlDefaultConfigs" type="CustomControlDefaultConfigsType" minOccurs="0" maxOccurs="1" />
						<xs:element name="indexes" type="indexesType" minOccurs="0" maxOccurs="1" />
					</xs:all>
				</xs:complexType>
			</xs:element>
		</xs:sequence>
	</xs:complexType>
	<xs:complexType name="StoredProceduresType">
		<xs:sequence>
			<xs:element name="procedure" minOccurs="0" maxOccurs="unbounded">
				<xs:complexType>
					<xs:sequence>
						<xs:element name="database" type="xs:string" minOccurs="1" maxOccurs="1" />
						<xs:element name="target" type="xs:string" minOccurs="1" maxOccurs="1"/>
						<xs:element name="file" type="xs:string" minOccurs="1" maxOccurs="1" />
						<xs:element name="description" type="xs:string" minOccurs="1" maxOccurs="1" />
					</xs:sequence>
					<xs:attribute name="name" use="required" type="xs:string" />
				</xs:complexType>
			</xs:element>
		</xs:sequence>
	</xs:complexType>
	<xs:complexType name="EntityInfoType">
		<xs:choice minOccurs="1" maxOccurs="1">
			<xs:element name="entity">
				<xs:complexType>
					<xs:all>
						<xs:element name="EntitySetName" type="xs:string" minOccurs="0" maxOccurs="1" />
						<xs:element name="ExternalName" type="xs:string" minOccurs="0" maxOccurs="1" />
						<xs:element name="ExternalCollectionName" type="xs:string" minOccurs="0" maxOccurs="1" />
						<xs:element name="HasRelatedNotes" type="TrueFalseType" minOccurs="0" maxOccurs="1" />
						<xs:element name="HasRelatedFeedback" type="TrueFalseType" minOccurs="0" maxOccurs="1" />
						<xs:element name="HasRelatedActivities" type="TrueFalseType" minOccurs="0" maxOccurs="1" />
						<xs:element name="IsConnectionsEnabled" type="TrueFalse01Type" minOccurs="0" maxOccurs="1" />
						<xs:element name="IsDocumentManagementEnabled" type="TrueFalse01Type" minOccurs="0" maxOccurs="1" />
						<xs:element name="IsCollaboration" type="TrueFalse01Type" minOccurs="0" maxOccurs="1" />
						<xs:element name="AutoRouteToOwnerQueue" type="TrueFalse01Type" minOccurs="0" maxOccurs="1" />
						<xs:element name="AutoCreateAccessTeams" type="TrueFalse01Type" minOccurs="0" maxOccurs="1" />
						<xs:element name="OwnershipTypeMask" type="xs:string" minOccurs="0" maxOccurs="1" />
						<xs:element name="IsAuditEnabled" type="TrueFalse01Type" minOccurs="0" maxOccurs="1" />
						<xs:element name="IsActivity" type="TrueFalse01Type" minOccurs="0" maxOccurs="1" />
						<xs:element name="ActivityTypeMask" type="xs:string" minOccurs="0" maxOccurs="1" />
						<xs:element name="DaysSinceRecordLastModified" type="xs:integer" minOccurs="0" maxOccurs="1" />
						<xs:element name="IsActivityParty" type="TrueFalse01Type" minOccurs="0" maxOccurs="1" />
						<xs:element name="IsReplicated" type="TrueFalse01Type" minOccurs="0" maxOccurs="1" />
						<xs:element name="IsReplicationUserFiltered" type="TrueFalse01Type" minOccurs="0" maxOccurs="1" />
						<xs:element name="IsRequiredOffline" type="TrueFalse01Type" minOccurs="0" maxOccurs="1" />
						<xs:element name="IsDuplicateCheckSupported" type="TrueFalse01Type" minOccurs="0" maxOccurs="1" />
						<xs:element name="IsBusinessProcessEnabled" type="TrueFalse01Type" minOccurs="0" maxOccurs="1" />
						<xs:element name="IsInteractionCentricEnabled" type="TrueFalse01Type" minOccurs="0" maxOccurs="1" />
						<xs:element name="IsMailMergeEnabled" type="TrueFalse01Type" minOccurs="0" maxOccurs="1" />
						<xs:element name="IsVisibleInMobile" type="TrueFalse01Type" minOccurs="0" maxOccurs="1" />
						<xs:element name="MobileClientType" type="xs:int" minOccurs="0" maxOccurs="1" />
						<xs:element name="IsVisibleInMobileClient" type="TrueFalse01Type" minOccurs="0" maxOccurs="1" />
						<xs:element name="IsReadOnlyInMobileClient" type="TrueFalse01Type" minOccurs="0" maxOccurs="1" />
						<xs:element name="IsOfflineInMobileClient" type="TrueFalse01Type" minOccurs="0" maxOccurs="1" />
						<xs:element name="IsReadingPaneEnabled" type="TrueFalse01Type" minOccurs="0" maxOccurs="1" />
						<xs:element name="IsMapiGridEnabled" type="TrueFalse01Type" minOccurs="0" maxOccurs="1" />
						<xs:element name="IsCustomizable" type="TrueFalse01Type" minOccurs="0" maxOccurs="1" />
						<xs:element name="IsRenameable" type="TrueFalse01Type" minOccurs="0" maxOccurs="1" />
						<xs:element name="IsMappable" type="TrueFalse01Type" minOccurs="0" maxOccurs="1" />
						<xs:element name="CanModifyConnectionSettings" type="TrueFalse01Type" minOccurs="0" maxOccurs="1" />
						<xs:element name="CanModifyAuditSettings" type="TrueFalse01Type" minOccurs="0" maxOccurs="1" />
						<xs:element name="CanModifyMobileVisibility" type="TrueFalse01Type" minOccurs="0" maxOccurs="1" />
						<xs:element name="CanModifyMobileClientVisibility" type="TrueFalse01Type" minOccurs="0" maxOccurs="1" />
						<xs:element name="CanModifyMobileClientReadOnly" type="TrueFalse01Type" minOccurs="0" maxOccurs="1" />
						<xs:element name="CanModifyMobileClientOffline" type="TrueFalse01Type" minOccurs="0" maxOccurs="1" />
						<xs:element name="CanModifyDuplicateDetectionSettings" type="TrueFalse01Type" minOccurs="0" maxOccurs="1" />
						<xs:element name="CanModifyMailMergeSettings" type="TrueFalse01Type" minOccurs="0" maxOccurs="1" />
						<xs:element name="CanModifyQueueSettings" type="TrueFalse01Type" minOccurs="0" maxOccurs="1" />
						<xs:element name="CanCreateAttributes" type="TrueFalse01Type" minOccurs="0" maxOccurs="1" />
						<xs:element name="CanBeRelatedEntityInRelationship" type="TrueFalse01Type" minOccurs="0" maxOccurs="1" />
						<xs:element name="CanBePrimaryEntityInRelationship" type="TrueFalse01Type" minOccurs="0" maxOccurs="1" />
						<xs:element name="CanBeInManyToMany" type="TrueFalse01Type" minOccurs="0" maxOccurs="1" />
						<xs:element name="CanCreateForms" type="TrueFalse01Type" minOccurs="0" maxOccurs="1" />
						<xs:element name="CanCreateCharts" type="TrueFalse01Type" minOccurs="0" maxOccurs="1" />
						<xs:element name="CanCreateViews" type="TrueFalse01Type" minOccurs="0" maxOccurs="1" />
						<xs:element name="CanModifyAdditionalSettings" type="TrueFalse01Type" minOccurs="0" maxOccurs="1" />
						<xs:element name="LocalizedNames" type="LocalizedNamesType" minOccurs="0" maxOccurs="1" />
						<xs:element name="LocalizedCollectionNames" type="LocalizedCollectionNamesType" minOccurs="0" maxOccurs="1" />
						<xs:element name="Descriptions" type="DescriptionsType" minOccurs="0" maxOccurs="1" />
						<xs:element name="EntityMask" type="xs:string" minOccurs="0" maxOccurs="1" />
						<xs:element name="EntityHelpUrlEnabled" type="TrueFalse01Type" minOccurs="0" maxOccurs="1" />
						<xs:element name="EntityHelpUrl" type="xs:string" minOccurs="0" maxOccurs="1" />
						<xs:element name="IconLargeName" type="xs:string" minOccurs="0" maxOccurs="1" />
						<xs:element name="IconMediumName" type="xs:string" minOccurs="0" maxOccurs="1" />
						<xs:element name="IconSmallName" type="xs:string" minOccurs="0" maxOccurs="1" />
						<xs:element name="IconVectorName" type="xs:string" minOccurs="0" maxOccurs="1" />
						<xs:element name="IsQuickCreateEnabled" type="TrueFalse01Type" minOccurs="0" maxOccurs="1" />
						<xs:element name="IntroducedVersion" type="VersionType" minOccurs="0" maxOccurs="1" />
						<xs:element name="EnforceStateTransitions" type="TrueFalse01Type" minOccurs="0" maxOccurs="1" />
						<xs:element name="CanChangeHierarchicalRelationship" type="TrueFalse01Type" minOccurs="0" maxOccurs="1" />
						<xs:element name="IsKnowledgeManagementEnabled" type="TrueFalse01Type" minOccurs="0" maxOccurs="1" />
						<xs:element name="EntityColor" type="xs:string" minOccurs="0" maxOccurs="1" />
						<xs:element name="ChangeTrackingEnabled" type="TrueFalse01Type" minOccurs="0" maxOccurs="1" />
						<xs:element name="CanChangeTrackingBeEnabled" type="TrueFalse01Type" minOccurs="0" maxOccurs="1" />
						<xs:element name="IsOneNoteIntegrationEnabled" type="TrueFalse01Type" minOccurs="0" maxOccurs="1" />
						<xs:element name="IsDocumentRecommendationsEnabled" type="TrueFalse01Type" minOccurs="0" maxOccurs="1" />
						<xs:element name="IsBPFEntity" type="TrueFalse01Type" minOccurs="0" maxOccurs="1" />
						<xs:element name="DataProviderId" type="GuidType" minOccurs="0" maxOccurs="1" />
						<xs:element name="DataSourceId" type="GuidType" minOccurs="0" maxOccurs="1" />
						<xs:element name="SyncToExternalSearchIndex" type="TrueFalse01Type" minOccurs="0" maxOccurs="1" />
						<xs:element name="CanEnableSyncToExternalSearchIndex" type="TrueFalse01Type" minOccurs="0" maxOccurs="1" />
						<xs:element name="IsEnabledForExternalChannels" type="TrueFalse01Type" minOccurs="0" maxOccurs="1" />
						<xs:element name="IsSLAEnabled" type="TrueFalse01Type" minOccurs="0" maxOccurs="1" />
						<xs:element name="MobileOfflineFilters" type="xs:string" minOccurs="0" maxOccurs="1" />
						<xs:element name="EntityKeys" minOccurs="0" maxOccurs="1">
							<xs:complexType>
								<xs:sequence>
									<xs:element name="EntityKey" minOccurs="0" maxOccurs="unbounded">
										<xs:complexType>
											<xs:all>
												<xs:element name="Name" type="xs:string" minOccurs="1" maxOccurs="1" />
												<xs:element name="LogicalName" type="EntityAttributeNameBaseType" minOccurs="0" maxOccurs="1" />
												<xs:element name="IntroducedVersion" type="VersionType" minOccurs="0" maxOccurs="1" />
												<xs:element name="IsCustomizable" type="TrueFalse01Type" minOccurs="0" maxOccurs="1" />
												<xs:element name="displaynames" type="displaynamestype" minOccurs="0" maxOccurs="1" />
												<xs:element name="EntityKeyAttributes" minOccurs="1" maxOccurs="1">
													<xs:complexType>
														<xs:sequence>
															<xs:element name="AttributeName" type="EntityAttributeNameBaseType" minOccurs="1" maxOccurs="unbounded" />
														</xs:sequence>
													</xs:complexType>
												</xs:element>
											</xs:all>
										</xs:complexType>
									</xs:element>
								</xs:sequence>
							</xs:complexType>
						</xs:element>
						<xs:element name="attributes" minOccurs="1" maxOccurs="1">
							<xs:complexType>
								<xs:sequence>
									<xs:element name="attribute" minOccurs="0" maxOccurs="unbounded">
										<xs:complexType>
											<xs:all>
												<xs:element name="Type" type="CrmDataType" minOccurs="0" maxOccurs="1" />
												<xs:element name="Name" type="EntityAttributeNameBaseType" minOccurs="0" maxOccurs="1" />
												<xs:element name="LogicalName" type="EntityAttributeNameBaseType" minOccurs="0" maxOccurs="1" />
												<xs:element name="ExternalName" type="xs:string" minOccurs="0" maxOccurs="1" />
												<xs:element name="IsCustomField" type="TrueFalse01Type" minOccurs="0" maxOccurs="1" />
												<xs:element name="ValidForCreateApi" type="TrueFalse01Type" minOccurs="0" maxOccurs="1" />
												<xs:element name="ValidForReadApi" type="TrueFalse01Type" minOccurs="0" maxOccurs="1" />
												<xs:element name="ValidForUpdateApi" type="TrueFalse01Type" minOccurs="0" maxOccurs="1" />
												<xs:element name="DisplayMask" type="xs:string" minOccurs="0" maxOccurs="1" />
												<xs:element name="Length" type="LengthType" minOccurs="0" maxOccurs="1" />
												<xs:element name="IsLogical" type="TrueFalse01Type" minOccurs="0" maxOccurs="1" />
												<xs:element name="AttributeOf" type="EntityAttributeNameBaseType" minOccurs="0" maxOccurs="1" />
												<xs:element name="YomiOf" type="EntityAttributeNameBaseType" minOccurs="0" maxOccurs="1" />
												<xs:element name="CalculationOf" type="EntityAttributeNameBaseType" minOccurs="0" maxOccurs="1" />
												<xs:element name="AggregateOf" type="EntityAttributeNameBaseType" minOccurs="0" maxOccurs="1" />
												<xs:element name="IsAuditEnabled" type="TrueFalse01Type" minOccurs="0" maxOccurs="1" />
												<xs:element name="XmlAbbreviation" type="xs:string" minOccurs="0" maxOccurs="1" />
												<xs:element name="ImeMode" type="xs:string" minOccurs="0" maxOccurs="1" />
												<xs:element name="RequiredLevel" type="xs:string" minOccurs="0" maxOccurs="1" />
												<xs:element name="LinkedAttribute" type="xs:string" minOccurs="0" maxOccurs="1" />
												<xs:element name="Format" type="xs:string" minOccurs="0" maxOccurs="1" />
												<xs:element name="MaxLength" type="xs:integer" minOccurs="0" maxOccurs="1" />
												<xs:element name="MinValue" type="xs:double" minOccurs="0" maxOccurs="1" />
												<xs:element name="MaxValue" type="xs:double" minOccurs="0" maxOccurs="1" />
												<xs:element name="Accuracy" type="xs:integer" minOccurs="0" maxOccurs="1" />
												<xs:element name="Descriptions" type="DescriptionsType" minOccurs="0" maxOccurs="1" />
												<xs:element name="displaynames" type="displaynamestype" minOccurs="0" maxOccurs="1" />
												<xs:element name="OptionSetName" type="xs:string" minOccurs="0" maxOccurs="1" />
												<xs:element name="optionset" type="optionsettype" minOccurs="0" maxOccurs="1" />
												<xs:element name="AppDefaultValue" type="xs:integer" minOccurs="0" maxOccurs="1" />
												<xs:element name="AccuracySource" type="xs:integer" minOccurs="0" maxOccurs="1" />
												<xs:element name="ReferencedEntityObjectTypeCode" type="ObjectTypeCodeType" minOccurs="0" maxOccurs="1" />
												<xs:element name="LookupBrowse" type="TrueFalse01Type" minOccurs="0" maxOccurs="1" />
												<xs:element name="LookupStyle" type="xs:string" minOccurs="0" maxOccurs="1" />
												<xs:element name="LookupTypes" type="LookupTypesType" minOccurs="0" maxOccurs="1" />
												<xs:element name="IsSecured" type="TrueFalse01Type" minOccurs="0" maxOccurs="1" />
												<xs:element name="IsCustomizable" type="TrueFalse01Type" minOccurs="0" maxOccurs="1" />
												<xs:element name="IsRenameable" type="TrueFalse01Type" minOccurs="0" maxOccurs="1" />
												<xs:element name="CanModifySearchSettings" type="TrueFalse01Type" minOccurs="0" maxOccurs="1" />
												<xs:element name="CanModifyRequirementLevelSettings" type="TrueFalse01Type" minOccurs="0" maxOccurs="1" />
												<xs:element name="CanModifyFieldLevelSecuritySettings" type="TrueFalse01Type" minOccurs="0" maxOccurs="1" />
												<xs:element name="CanModifyAdditionalSettings" type="TrueFalse01Type" minOccurs="0" maxOccurs="1" />
												<xs:element name="IntroducedVersion" type="VersionType" minOccurs="0" maxOccurs="1" />
												<xs:element name="SourceType" type="xs:integer" minOccurs="0" maxOccurs="1" />
												<xs:element name="FormulaDefinitionFileName" type="xs:string" minOccurs="0" maxOccurs="1" />
												<xs:element name="Behavior" type="xs:integer" minOccurs="0" maxOccurs="1" />
												<xs:element name="CanChangeDateTimeBehavior" type="TrueFalse01Type" minOccurs="0" maxOccurs="1" />
												<xs:element name="IsGlobalFilterEnabled" type="TrueFalse01Type" minOccurs="0" maxOccurs="1" />
												<xs:element name="IsSortableEnabled" type="TrueFalse01Type" minOccurs="0" maxOccurs="1" />
												<xs:element name="CanModifyGlobalFilterSettings" type="TrueFalse01Type" minOccurs="0" maxOccurs="1" />
												<xs:element name="CanModifyIsSortableSettings" type="TrueFalse01Type" minOccurs="0" maxOccurs="1" />
												<xs:element name="IsActive" type="TrueFalse01Type" minOccurs="0" maxOccurs="1" />
												<xs:element name="IsDataSourceSecret" type="TrueFalse01Type" minOccurs="0" maxOccurs="1" />
											</xs:all>
											<xs:attribute name="PhysicalName" use="required" type="EntityAttributeNameBaseType" />
											<xs:attribute name="unmodified" use="optional" type="TrueFalse01Type" />
										</xs:complexType>
									</xs:element>
								</xs:sequence>
							</xs:complexType>
						</xs:element>
					</xs:all>
					<xs:attribute name="Name" use="required" type="EntityAttributeNameBaseType" />
					<xs:attribute name="unmodified" use="optional" type="TrueFalse01Type" />
				</xs:complexType>
			</xs:element>
		</xs:choice>
	</xs:complexType>
	<xs:complexType name="ChannelPropertyGroupsType">
		<xs:choice minOccurs="0" maxOccurs="unbounded">
			<xs:element name="ChannelPropertyGroup">
				<xs:complexType>
					<xs:sequence>
						<xs:element name="ChannelProperty" minOccurs="0" maxOccurs="unbounded">
							<xs:complexType>
								<xs:sequence>
									<xs:element name="ChannelPropertyId" type="GuidType" minOccurs="1" maxOccurs="1" />
									<xs:element name="Name" type="xs:string" minOccurs="1" maxOccurs="1" />
									<xs:element name="Description" type="xs:string" minOccurs="0" maxOccurs="1" />
									<xs:element name="DataType" type="xs:integer" minOccurs="0" maxOccurs="1" />
									<xs:element name="ApplicationSource" type="xs:string" minOccurs="0" maxOccurs="1" />
								</xs:sequence>
							</xs:complexType>
						</xs:element>
						<xs:element name="ChannelPropertyGroupId" type="GuidType" minOccurs="1" maxOccurs="1" />
						<xs:element name="Name" type="xs:string" minOccurs="1" maxOccurs="1" />
						<xs:element name="Description" type="xs:string" minOccurs="0" maxOccurs="1" />
						<xs:element name="ChannelEntity" type="EntityAttributeNameBaseType" minOccurs="1" maxOccurs="1" />
					</xs:sequence>
				</xs:complexType>
			</xs:element>
		</xs:choice>
	</xs:complexType>
	<xs:complexType name="ConvertRulesType">
		<xs:choice minOccurs="0" maxOccurs="unbounded">
			<xs:element name="ConvertRule">
				<xs:complexType>
					<xs:sequence>
						<xs:element name="ConvertRuleItems" minOccurs="0" maxOccurs="unbounded">
							<xs:complexType>
								<xs:sequence>
									<xs:element name="ConvertRuleItem" minOccurs="0" maxOccurs="unbounded">
										<xs:complexType>
											<xs:sequence>
												<xs:element name="ConvertRuleItemId" type="GuidType" minOccurs="0" maxOccurs="1" />
												<xs:element name="ConvertRuleId" type="GuidType" minOccurs="0" maxOccurs="1" />
												<xs:element name="Name" type="xs:string" minOccurs="0" maxOccurs="1" />
												<xs:element name="Description" type="xs:string" minOccurs="0" maxOccurs="1" />
												<xs:element name="ConditionXml" type="xs:string" minOccurs="0" maxOccurs="1" />
												<xs:element name="PropertiesXml" type="xs:string" minOccurs="0" maxOccurs="1" />
												<xs:element name="WorkflowId" type="GuidType" minOccurs="0" maxOccurs="1" />
											</xs:sequence>
											<xs:attribute name="ConvertRuleItemId" type="xs:string" use="required" />
											<xs:attribute name="Name" use="required" type="xs:string" />
										</xs:complexType>
									</xs:element>
								</xs:sequence>
							</xs:complexType>
						</xs:element>
						<xs:element name="ConvertRuleId" type="GuidType" minOccurs="0" maxOccurs="1" />
						<xs:element name="Name" type="xs:string" minOccurs="0" maxOccurs="1" />
						<xs:element name="SourceTypeCode" type="xs:integer" minOccurs="0" maxOccurs="1" />
						<xs:element name="AllowUnknownSender" type="xs:boolean" minOccurs="0" maxOccurs="1" />
						<xs:element name="SendAutomaticResponse" type="xs:boolean" minOccurs="0" maxOccurs="1" />
						<xs:element name="CheckIfResolved" type="xs:boolean" minOccurs="0" maxOccurs="1" />
						<xs:element name="CheckActiveEntitlement" type="xs:boolean" minOccurs="0" maxOccurs="1" />
						<xs:element name="CheckDirectMessages" type="xs:boolean" minOccurs="0" maxOccurs="1" />
						<xs:element name="CheckBlockedSocialProfile" type="xs:boolean" minOccurs="0" maxOccurs="1" />
						<xs:element name="ChannelPropertyGroupId" type="GuidType" minOccurs="0" maxOccurs="1" />
						<xs:element name="ResponseTemplateId" type="GuidType" minOccurs="0" maxOccurs="1" />
						<xs:element name="ResolvedSince" type="xs:integer" minOccurs="0" maxOccurs="1" />
						<xs:element name="WorkflowId" type="GuidType" minOccurs="0" maxOccurs="1" />
						<xs:element name="SourceChannelEntity" type="EntityAttributeNameBaseType" minOccurs="0" maxOccurs="1" />
						<xs:element name="RecordVersion" type="xs:string" minOccurs="0" maxOccurs="1" />
					</xs:sequence>
					<xs:attribute name="ConvertRuleId" use="required" type="xs:string" />
					<xs:attribute name="Name" use="required" type="xs:string" />
				</xs:complexType>
			</xs:element>
		</xs:choice>
	</xs:complexType>
	<xs:complexType name="MobileOfflineProfilesType">
		<xs:choice minOccurs="0" maxOccurs="unbounded">
			<xs:element name="MobileOfflineProfile">
				<xs:complexType>
					<xs:sequence>
						<xs:element name="MobileOfflineProfileItems" minOccurs="0" maxOccurs="unbounded">
							<xs:complexType>
								<xs:sequence>
									<xs:element name="MobileOfflineProfileItem" minOccurs="0" maxOccurs="unbounded">
										<xs:complexType>
											<xs:sequence>
												<xs:element name="MobileOfflineProfileItemAssociations" minOccurs="0" maxOccurs="unbounded">
													<xs:complexType>
														<xs:sequence>
															<xs:element name="MobileOfflineProfileItemAssociation" minOccurs="0" maxOccurs="unbounded">
																<xs:complexType>
																	<xs:sequence>
																		<xs:element name="MobileOfflineProfileItemAssociationId" type="GuidType" minOccurs="1" maxOccurs="1" />
																		<xs:element name="MobileOfflineProfileItemId" type="GuidType" minOccurs="1" maxOccurs="1" />
																		<xs:element name="Name" type="xs:string" minOccurs="1" maxOccurs="1" />
																		<xs:element name="RelationshipDisplayName" type="xs:string" minOccurs="1" maxOccurs="1" />
																		<xs:element name="ProfileItemAssociationEntityFilter" type="xs:string" minOccurs="0" maxOccurs="1" />
																		<xs:element name="IntroducedVersion" type="VersionType" minOccurs="0" maxOccurs="1" />
																	</xs:sequence>
																	<xs:attribute name="MobileOfflineProfileItemAssociationId" type="xs:string" use="required" />
																	<xs:attribute name="Name" use="required" type="xs:string" />
																</xs:complexType>
															</xs:element>
														</xs:sequence>
													</xs:complexType>
												</xs:element>
												<xs:element name="MobileOfflineProfileItemId" type="GuidType" minOccurs="1" maxOccurs="1" />
												<xs:element name="RegardingObjectId" type="GuidType" minOccurs="1" maxOccurs="1" />
												<xs:element name="Name" type="xs:string" minOccurs="1" maxOccurs="1" />
												<xs:element name="RecordDistributionCriteria" type="xs:int" minOccurs="0" maxOccurs="1" />
												<xs:element name="RecordsOwnedByMe" type="xs:boolean" minOccurs="0" maxOccurs="1" />
												<xs:element name="RecordsOwnedByMyTeam" type="xs:boolean" minOccurs="0" maxOccurs="1" />
												<xs:element name="RecordsOwnedByMyBusinessUnit" type="xs:boolean" minOccurs="0" maxOccurs="1" />
												<xs:element name="ProfileItemEntityFilter" type="xs:string" minOccurs="0" maxOccurs="1" />
												<xs:element name="EntitySchemaName" type="xs:string" minOccurs="1" maxOccurs="1" />
												<xs:element name="IntroducedVersion" type="VersionType" minOccurs="0" maxOccurs="1" />
											</xs:sequence>
											<xs:attribute name="MobileOfflineProfileItemId" type="xs:string" use="required" />
											<xs:attribute name="Name" use="required" type="xs:string" />
										</xs:complexType>
									</xs:element>
								</xs:sequence>
							</xs:complexType>
						</xs:element>
						<xs:element name="MobileOfflineProfileId" type="GuidType" minOccurs="1" maxOccurs="1" />
						<xs:element name="Name" type="xs:string" minOccurs="1" maxOccurs="1" />
						<xs:element name="Description" type="xs:string" minOccurs="0" maxOccurs="1" />
						<xs:element name="IntroducedVersion" type="VersionType" minOccurs="0" maxOccurs="1" />
					</xs:sequence>
					<xs:attribute name="MobileOfflineProfileId" use="required" type="xs:string" />
					<xs:attribute name="Name" use="required" type="xs:string" />
					<xs:attribute name="unmodified" use="optional" type="TrueFalse01Type" />
				</xs:complexType>
			</xs:element>
		</xs:choice>
	</xs:complexType>
	<xs:complexType name="RoutingRulesType">
		<xs:choice minOccurs="0" maxOccurs="unbounded">
			<xs:element name="RoutingRule">
				<xs:complexType>
					<xs:sequence>
						<xs:element name="RoutingRuleId" type="GuidType" minOccurs="0" maxOccurs="1" />
						<xs:element name="Name" type="xs:string" minOccurs="0" maxOccurs="1" />
						<xs:element name="Description" type="xs:string" minOccurs="0" maxOccurs="1" />
						<xs:element name="RoutingRuleItems" minOccurs="0" maxOccurs="unbounded">
							<xs:complexType>
								<xs:sequence>
									<xs:element name="RoutingRuleItem" minOccurs="0" maxOccurs="unbounded">
										<xs:complexType>
											<xs:sequence>
												<xs:element name="Name" type="xs:string" minOccurs="1" maxOccurs="1" />
												<xs:element name="Description" type="xs:string" minOccurs="0" maxOccurs="1" />
												<xs:element name="RoutingRuleId" type="GuidType" minOccurs="1" maxOccurs="1" />
												<xs:element name="ConditionXml" type="xs:string" minOccurs="0" maxOccurs="1" />
											</xs:sequence>
											<xs:attribute name="RoutingRuleItemId" type="xs:string" use="required" />
											<xs:attribute name="Name" use="required" type="xs:string" />
										</xs:complexType>
									</xs:element>
								</xs:sequence>
							</xs:complexType>
						</xs:element>
						<xs:element name="Workflows" type="WorkflowsType" minOccurs="0" maxOccurs="1" />
					</xs:sequence>
					<xs:attribute name="RoutingRuleId" use="required" type="xs:string" />
					<xs:attribute name="Name" use="required" type="xs:string" />
				</xs:complexType>
			</xs:element>
		</xs:choice>
	</xs:complexType>
	<xs:complexType name="ChannelAccessProfilesType">
		<xs:choice minOccurs="0" maxOccurs="unbounded">
			<xs:element name="ChannelAccessProfile">
				<xs:complexType>
					<xs:sequence>
						<xs:element name="Name" type="xs:string" minOccurs="0" maxOccurs="1" />
						<xs:element name="ChannelAccessProfileId" type="GuidType" minOccurs="0" maxOccurs="1" />
						<xs:element name="EmailAccess" type="xs:boolean" minOccurs="0" maxOccurs="1" />
						<xs:element name="FacebookAccess" type="xs:boolean" minOccurs="0" maxOccurs="1" />
						<xs:element name="PhoneAccess" type="xs:boolean" minOccurs="0" maxOccurs="1" />
						<xs:element name="TwitterAccess" type="xs:boolean" minOccurs="0" maxOccurs="1" />
						<xs:element name="WebAccess" type="xs:boolean" minOccurs="0" maxOccurs="1" />
						<xs:element name="ViewKnowledgeArticles" type="xs:boolean" minOccurs="0" maxOccurs="1" />
						<xs:element name="ViewArticleRating" type="xs:boolean" minOccurs="0" maxOccurs="1" />
						<xs:element name="RateKnowledgeArticles" type="xs:boolean" minOccurs="0" maxOccurs="1" />
						<xs:element name="SubmitFeedback" type="xs:boolean" minOccurs="0" maxOccurs="1" />
						<xs:element name="StateCode" type="xs:int" minOccurs="0" maxOccurs="1" />
						<xs:element name="StatusCode" type="xs:int" minOccurs="0" maxOccurs="1" />
						<xs:element name="IsGuestProfile" type="xs:boolean" minOccurs="0" maxOccurs="1" />
						<xs:element name="EnabledEntities" type="xs:string" minOccurs="0" maxOccurs="1" />
						<xs:element name="ChannelAccessProfilePrivileges" minOccurs="0" maxOccurs="unbounded">
							<xs:complexType>
								<xs:sequence>
									<xs:element name="ChannelAccessProfilePrivilege" minOccurs="0" maxOccurs="unbounded">
										<xs:complexType>
											<xs:attribute name="name" use="required" type="xs:string" />
											<xs:attribute name="level" use="required" type="xs:int" />
										</xs:complexType>
									</xs:element>
								</xs:sequence>
							</xs:complexType>
						</xs:element>
					</xs:sequence>
					<xs:attribute name="ChannelAccessProfileId" use="required" type="xs:string" />
					<xs:attribute name="Name" use="required" type="xs:string" />
					<xs:attribute name="unmodified" use="optional" type="TrueFalse01Type" />
				</xs:complexType>
			</xs:element>
		</xs:choice>
	</xs:complexType>
	<xs:complexType name="ProfileRulesType">
		<xs:choice minOccurs="0" maxOccurs="unbounded">
			<xs:element name="ChannelAccessProfileRule">
				<xs:complexType>
					<xs:sequence>
						<xs:element name="ChannelAccessProfileRuleId" type="GuidType" minOccurs="0" maxOccurs="1" />
						<xs:element name="Name" type="xs:string" minOccurs="0" maxOccurs="1" />
						<xs:element name="Description" type="xs:string" minOccurs="0" maxOccurs="1" />
						<xs:element name="ChannelAccessProfileRuleItems" minOccurs="0" maxOccurs="unbounded">
							<xs:complexType>
								<xs:sequence>
									<xs:element name="ChannelAccessProfileRuleItem" minOccurs="0" maxOccurs="unbounded">
										<xs:complexType>
											<xs:sequence>
												<xs:element name="Name" type="xs:string" minOccurs="1" maxOccurs="1" />
												<xs:element name="Description" type="xs:string" minOccurs="0" maxOccurs="1" />
												<xs:element name="ChannelAccessProfileRuleId" type="GuidType" minOccurs="1" maxOccurs="1" />
												<xs:element name="ConditionXml" type="xs:string" minOccurs="0" maxOccurs="1" />
												<xs:element name="AssociatedChannelAccessProfile" type="GuidType" minOccurs="0" maxOccurs="1" />
											</xs:sequence>
											<xs:attribute name="ChannelAccessProfileRuleItemId" type="xs:string" use="required" />
											<xs:attribute name="Name" use="required" type="xs:string" />
										</xs:complexType>
									</xs:element>
								</xs:sequence>
							</xs:complexType>
						</xs:element>
						<xs:element name="Workflows" type="WorkflowsType" minOccurs="0" maxOccurs="1" />
					</xs:sequence>
					<xs:attribute name="ChannelAccessProfileRuleId" use="required" type="xs:string" />
					<xs:attribute name="Name" use="required" type="xs:string" />
				</xs:complexType>
			</xs:element>
		</xs:choice>
	</xs:complexType>
	<xs:complexType name="HierarchyRulesType">
		<xs:choice minOccurs="0" maxOccurs="unbounded">
			<xs:element name="HierarchyRule">
				<xs:complexType>
					<xs:sequence>
						<xs:element name="HierarchyRuleID" type="GuidType" minOccurs="1" maxOccurs="1" />
						<xs:element name="PrimaryEntityFormID" type="GuidType" minOccurs="1" maxOccurs="1" />
						<xs:element name="PrimaryEntityLogicalName" type="xs:string" minOccurs="1" maxOccurs="1" />
						<xs:element name="ShowDisabled" type="TrueFalse01Type" minOccurs="1" maxOccurs="1" />
						<xs:element name="IntroducedVersion" type="VersionType" minOccurs="0" maxOccurs="1" />
						<xs:element name="IsCustomizable" type="TrueFalse01Type" minOccurs="0" maxOccurs="1" />
						<xs:element name="LocalizedNames" type="LocalizedNamesType" minOccurs="1" maxOccurs="1" />
						<xs:element name="Descriptions" type="DescriptionsType" minOccurs="0" maxOccurs="1" />
					</xs:sequence>
					<xs:attribute name="unmodified" use="optional" type="TrueFalse01Type" />
				</xs:complexType>
			</xs:element>
		</xs:choice>
	</xs:complexType>
	<xs:complexType name="CustomControlDefaultConfigsType">
		<xs:sequence>
			<xs:element name="CustomControlDefaultConfig" minOccurs="0" maxOccurs="unbounded">
				<xs:complexType>
					<xs:sequence>
						<xs:element name="PrimaryEntityTypeCode" type="xs:integer" minOccurs="0" maxOccurs="1" />
						<xs:element name="CustomControlDefaultConfigId" type="GuidType" minOccurs="1" maxOccurs="1" />
						<xs:element name="ControlDescriptionXML">
							<xs:complexType>
								<xs:sequence>
									<xs:element name="controlDescriptions" minOccurs="0" maxOccurs="1">
										<xs:complexType>
											<xs:sequence>
												<xs:element name="controlDescription" minOccurs="0" maxOccurs="1">
													<xs:complexType>
														<xs:sequence>
															<xs:element name="customControl" minOccurs="0" maxOccurs="unbounded">
																<xs:complexType>
																	<xs:sequence>
																		<xs:element name="parameters" minOccurs="1" maxOccurs="1">
																			<xs:complexType>
																				<xs:sequence>
																					<xs:any minOccurs="0" maxOccurs="unbounded" processContents="skip"></xs:any>
																				</xs:sequence>
																			</xs:complexType>
																		</xs:element>
																	</xs:sequence>
																	<xs:attribute name="id" type="FormGuidType" use="optional" />
																	<xs:attribute name="formFactor" type="xs:integer" use="optional" />
																	<xs:attribute name="name" type="xs:string" use="optional" />
																	<xs:attribute name="version" type="xs:string" use="optional" />
																</xs:complexType>
															</xs:element>
														</xs:sequence>
													</xs:complexType>
												</xs:element>
											</xs:sequence>
										</xs:complexType>
									</xs:element>
								</xs:sequence>
							</xs:complexType>
						</xs:element>
						<xs:element name="IntroducedVersion" type="xs:string" minOccurs="0" maxOccurs="1" />
						<xs:element name="formLibraries" type="FormXmlLibraryType" minOccurs="0" maxOccurs="1" />
						<xs:element name="events" type="FormXmlEventsType" minOccurs="0" maxOccurs="1" />
					</xs:sequence>
				</xs:complexType>
			</xs:element>
		</xs:sequence>
	</xs:complexType>
	<xs:complexType name="indexesType">
		<xs:sequence>
			<xs:element name="index" minOccurs="0" maxOccurs="unbounded">
				<xs:complexType>
					<xs:sequence>
						<xs:element name="IsClustered" type="xs:boolean" minOccurs="0" maxOccurs="1" />
						<xs:element name="IsUnique" type="xs:boolean" minOccurs="0" maxOccurs="1" />
						<xs:element name="IsPrimaryKey" type="xs:boolean" minOccurs="1" maxOccurs="1" />
						<xs:element name="IsUniqueConstraint" type="xs:boolean" minOccurs="0" maxOccurs="1" />
						<xs:element name="IndexType" type="xs:integer" minOccurs="0" maxOccurs="1" />
						<xs:element name="attributes" minOccurs="1" maxOccurs="1">
							<xs:complexType>
								<xs:sequence>
									<xs:element name="attribute" minOccurs="1" maxOccurs="unbounded">
										<xs:complexType>
											<xs:attribute name="Name" use="required" type="xs:string" />
											<xs:attribute name="order" use="required" type="xs:string" />
											<xs:attribute name="IsIncludeAttribute" use="optional" type="xs:boolean" />
											<xs:attribute name="SortDescending" use="optional" type="xs:boolean" />
										</xs:complexType>
									</xs:element>
								</xs:sequence>
							</xs:complexType>
						</xs:element>
						<xs:element name="filters" minOccurs="0" maxOccurs="1">
							<xs:complexType>
								<xs:sequence>
									<xs:element name="filter" minOccurs="1" maxOccurs="unbounded">
										<xs:complexType>
											<xs:attribute name="attribute" use="required" type="xs:string" />
											<xs:attribute name="operator" use="required" type="xs:string" />
											<xs:attribute name="value" use="optional" type="xs:string" />
										</xs:complexType>
									</xs:element>
								</xs:sequence>
							</xs:complexType>
						</xs:element>
					</xs:sequence>
					<xs:attribute name="Name" use="required" type="xs:string" />
				</xs:complexType>
			</xs:element>
		</xs:sequence>
	</xs:complexType>
	<xs:complexType name="EntityMapsType">
		<xs:choice minOccurs="0" maxOccurs="unbounded">
			<xs:element name="EntityMap">
				<xs:complexType>
					<xs:sequence>
						<xs:element name="EntitySource" type="xs:string" minOccurs="1" maxOccurs="1" />
						<xs:element name="EntityTarget" type="xs:string" minOccurs="1" maxOccurs="1" />
						<xs:element name="AttributeMaps" minOccurs="0" maxOccurs="1">
							<xs:complexType>
								<xs:sequence>
									<xs:element name="AttributeMap" minOccurs="0" maxOccurs="unbounded">
										<xs:complexType>
											<xs:sequence>
												<xs:element name="AttributeSource" type="EntityAttributeNameBaseType" minOccurs="1" maxOccurs="1" />
												<xs:element name="AttributeTarget" type="EntityAttributeNameBaseType" minOccurs="1" maxOccurs="1" />
											</xs:sequence>
											<xs:attribute name="addedby" type="xs:string" />
										</xs:complexType>
									</xs:element>
								</xs:sequence>
							</xs:complexType>
						</xs:element>
					</xs:sequence>
					<xs:attribute name="addedby" type="xs:string" />
				</xs:complexType>
			</xs:element>
		</xs:choice>
	</xs:complexType>
	<xs:complexType name="RolesType">
		<xs:sequence>
			<xs:element name="Role" minOccurs="0" maxOccurs="unbounded">
				<xs:complexType>
					<xs:sequence>
						<xs:element name="IsCustomizable" type="TrueFalse01Type" minOccurs="0" maxOccurs="1" />
						<xs:element name="IntroducedVersion" type="VersionType" minOccurs="0" maxOccurs="1" />
						<xs:element name="RolePrivileges" type="RolePrivilegestype" minOccurs="0" maxOccurs="1" />
					</xs:sequence>
					<xs:attribute name="name" use="required" type="xs:string" />
					<xs:attribute name="id" use="required" type="GuidType" />
					<xs:attribute name="unmodified" use="optional" type="TrueFalse01Type" />
				</xs:complexType>
			</xs:element>
		</xs:sequence>
	</xs:complexType>
	<xs:complexType name="RolePrivilegestype">
		<xs:sequence>
			<xs:element name="RolePrivilege" type="RolePrivilegeType" minOccurs="0" maxOccurs="unbounded" />
		</xs:sequence>
	</xs:complexType>
	<xs:complexType name="RolePrivilegeType">
		<xs:attribute name="name" use="required" type="xs:string" />
		<xs:attribute name="level" use="required" type="PrivilegeLevelType" />
	</xs:complexType>
	<xs:simpleType name="PrivilegeLevelType">
		<xs:restriction base="xs:string">
			<xs:enumeration value="Basic" />
			<xs:enumeration value="Local" />
			<xs:enumeration value="Deep" />
			<xs:enumeration value="Global" />
		</xs:restriction>
	</xs:simpleType>
	<xs:complexType name="FieldSecurityProfilesType">
		<xs:sequence>
			<xs:element name="FieldSecurityProfile" minOccurs="0" maxOccurs="unbounded">
				<xs:complexType>
					<xs:sequence>
						<xs:element name="FieldPermissions" type="FieldPermissionsType" minOccurs="0" maxOccurs="1" />
					</xs:sequence>
					<xs:attribute name="name" use="required" type="xs:string" />
					<xs:attribute name="description" use="optional" type="xs:string" />
					<xs:attribute name="fieldsecurityprofileid" use="required" type="GuidType" />
					<xs:attribute name="unmodified" use="optional" type="TrueFalse01Type" />
				</xs:complexType>
			</xs:element>
		</xs:sequence>
	</xs:complexType>
	<xs:complexType name="FieldPermissionsType">
		<xs:sequence>
			<xs:element name="FieldPermission" minOccurs="0" maxOccurs="unbounded">
				<xs:complexType>
					<xs:sequence>
						<xs:element name="EntityName" type="xs:string" minOccurs="1" maxOccurs="1" />
						<xs:element name="AttributeName" type="xs:string" minOccurs="1" maxOccurs="1" />
						<xs:element name="CanRead" type="xs:integer" minOccurs="1" maxOccurs="1" />
						<xs:element name="CanUpdate" type="xs:integer" minOccurs="1" maxOccurs="1" />
						<xs:element name="CanCreate" type="xs:integer" minOccurs="1" maxOccurs="1" />
					</xs:sequence>
				</xs:complexType>
			</xs:element>
		</xs:sequence>
	</xs:complexType>
	<xs:complexType name="WorkflowsType">
		<xs:sequence>
			<xs:element name="Workflow" minOccurs="0" maxOccurs="unbounded">
				<xs:complexType>
					<xs:sequence>
						<xs:element name="XamlFileName" type="xs:string" minOccurs="0" maxOccurs="1" />
						<xs:element name="ImageFileName" type="xs:string" minOccurs="0" maxOccurs="1" />
						<xs:element name="Type" type="xs:nonNegativeInteger" minOccurs="0" maxOccurs="1" />
						<xs:element name="Subprocess" type="TrueFalse01Type" minOccurs="0" maxOccurs="1" />
						<xs:element name="Category" type="xs:nonNegativeInteger" minOccurs="0" maxOccurs="1" />
						<xs:element name="Mode" type="xs:nonNegativeInteger" minOccurs="0" maxOccurs="1" />
						<xs:element name="LanguageCode" type="xs:nonNegativeInteger" minOccurs="0" maxOccurs="1" />
						<xs:element name="Scope" type="xs:nonNegativeInteger" minOccurs="0" maxOccurs="1" />
						<xs:element name="OnDemand" type="TrueFalse01Type" minOccurs="0" maxOccurs="1" />
						<xs:element name="TriggerOnUpdateAttributeList" type="xs:string" minOccurs="0" maxOccurs="1" />
						<xs:element name="TriggerOnCreate" type="TrueFalse01Type" minOccurs="0" maxOccurs="1" />
						<xs:element name="TriggerOnDelete" type="TrueFalse01Type" minOccurs="0" maxOccurs="1" />
						<xs:element name="AsyncAutodelete" type="TrueFalse01Type" minOccurs="0" maxOccurs="1" />
						<xs:element name="SyncWorkflowLogOnFailure" type="TrueFalse01Type" minOccurs="0" maxOccurs="1" />
						<xs:element name="StateCode" type="xs:nonNegativeInteger" minOccurs="0" maxOccurs="1" />
						<xs:element name="StatusCode" type="xs:nonNegativeInteger" minOccurs="0" maxOccurs="1" />
						<xs:element name="CreateStage" type="xs:nonNegativeInteger" minOccurs="0" maxOccurs="1" />
						<xs:element name="UpdateStage" type="xs:nonNegativeInteger" minOccurs="0" maxOccurs="1" />
						<xs:element name="DeleteStage" type="xs:nonNegativeInteger" minOccurs="0" maxOccurs="1" />
						<xs:element name="Rank" type="xs:integer" minOccurs="0" maxOccurs="1" />
						<xs:element name="processorder" type="xs:nonNegativeInteger" minOccurs="0" maxOccurs="1" />
						<xs:element name="processroleassignment" type="xs:string" minOccurs="0" maxOccurs="1" />
						<xs:element name="RunAs" type="xs:nonNegativeInteger" minOccurs="0" maxOccurs="1" />
						<xs:element name="SdkMessageId" type="GuidType" minOccurs="0" maxOccurs="1" />
						<xs:element name="UniqueName" type="xs:string" minOccurs="0" maxOccurs="1" />
						<xs:element name="IsTransacted" type="TrueFalse01Type" minOccurs="0" maxOccurs="1" />
						<xs:element name="IntroducedVersion" type="VersionType" minOccurs="0" maxOccurs="1" />
						<xs:element name="IsCustomizable" type="TrueFalse01Type" minOccurs="0" maxOccurs="1" />
						<xs:element name="RendererObjectTypeCode" type="xs:integer" minOccurs="0" maxOccurs="1" />
						<xs:element name="BusinessProcessType" type="xs:nonNegativeInteger" minOccurs="0" maxOccurs="1" />
						<xs:element name="FormId" type="GuidType" minOccurs="0" maxOccurs="1" />
						<xs:element name="PrimaryEntity" type="xs:string" minOccurs="0" maxOccurs="1" />
						<xs:element name="LocalizedNames" minOccurs="0" maxOccurs="1">
							<xs:complexType>
								<xs:sequence>
									<xs:element name="LocalizedName" minOccurs="0" maxOccurs="unbounded">
										<xs:complexType>
											<xs:attribute name="description" type="xs:string" />
											<xs:attribute name="languagecode" type="xs:int" />
										</xs:complexType>
									</xs:element>
								</xs:sequence>
							</xs:complexType>
						</xs:element>
						<xs:element name="Descriptions" minOccurs="0" maxOccurs="1">
							<xs:complexType>
								<xs:sequence>
									<xs:element name="Description" minOccurs="0" maxOccurs="unbounded">
										<xs:complexType>
											<xs:attribute name="description" type="xs:string" />
											<xs:attribute name="languagecode" type="xs:int" />
										</xs:complexType>
									</xs:element>
								</xs:sequence>
							</xs:complexType>
						</xs:element>						
						<xs:element name="labels" minOccurs="0" maxOccurs="1" type="WorkflowLabelsType" />
						<xs:element name="ProcessTriggers" type="ProcessTriggersType" minOccurs="0" maxOccurs="1" />
					</xs:sequence>
					<xs:attribute name="Name" use="required" type="xs:string" />
					<xs:attribute name="Description" use="optional" type="xs:string" />
					<xs:attribute name="WorkflowId" use="required" type="GuidType" />
					<xs:attribute name="unmodified" use="optional" type="TrueFalse01Type" />
				</xs:complexType>
			</xs:element>
		</xs:sequence>
	</xs:complexType>
	<xs:complexType name="WorkflowLabelsType">
		<xs:sequence>
			<xs:element name="steplabels" minOccurs="0" maxOccurs="unbounded">
				<xs:complexType>
					<xs:sequence>
						<xs:element name="label" minOccurs="0" maxOccurs="unbounded">
							<xs:complexType>
								<xs:attribute name="languagecode" type="xs:string" use="required" />
								<xs:attribute name="description" type="xs:string" use="required" />
							</xs:complexType>
						</xs:element>
					</xs:sequence>
					<xs:attribute name="id" use="required" type="GuidType" />
				</xs:complexType>
			</xs:element>
		</xs:sequence>
	</xs:complexType>
	<xs:complexType name="ProcessTriggersType">
		<xs:sequence>
			<xs:element name="ProcessTrigger" minOccurs="0" maxOccurs="unbounded">
				<xs:complexType>
					<xs:sequence>
						<xs:element name="controltype" type="xs:nonNegativeInteger" minOccurs="0" maxOccurs="1" />
						<xs:element name="methodid" type="GuidType" minOccurs="0" maxOccurs="1" />
						<xs:element name="formid" type="GuidType" minOccurs="0" maxOccurs="1" />
						<xs:element name="scope" type="xs:nonNegativeInteger" minOccurs="0" maxOccurs="1" />
						<xs:element name="controlname" type="xs:string" minOccurs="0" maxOccurs="1" />
						<xs:element name="event" type="xs:string" minOccurs="1" maxOccurs="1" />
						<xs:element name="pipelinestage" type="xs:nonNegativeInteger" minOccurs="0" maxOccurs="1" />
						<xs:element name="iscustomizable" type="TrueFalse01Type" minOccurs="0" maxOccurs="1" />
						<xs:element name="primaryentitytypecode" type="xs:string" minOccurs="1" maxOccurs="1" />
					</xs:sequence>
					<xs:attribute name="processtriggerid" use="required" type="GuidType" />
				</xs:complexType>
			</xs:element>
		</xs:sequence>
	</xs:complexType>
	<xs:complexType name="DashboardsType">
		<xs:sequence>
			<xs:element name="Dashboard" minOccurs="0" maxOccurs="unbounded">
				<xs:complexType>
					<xs:all>
						<xs:element name="FormId" type="GuidType" minOccurs="1" maxOccurs="1" />
						<xs:element name="LocalizedNames" type="LocalizedNamesType" minOccurs="1" maxOccurs="1" />
						<xs:element name="Descriptions" type="DescriptionsType" minOccurs="0" maxOccurs="1" />
						<xs:element name="IsCustomizable" type="TrueFalse01Type" minOccurs="0" maxOccurs="1" />
						<xs:element name="IsDefault" type="SerializedTrueFalse01Type" minOccurs="0" maxOccurs="1" />
						<xs:element name="CanBeDeleted" type="TrueFalse01Type" minOccurs="0" maxOccurs="1" />
						<xs:element name="FormXml" type="FormXmlType" minOccurs="0" maxOccurs="1" />
						<xs:element name="IntroducedVersion" type="VersionType" minOccurs="0" maxOccurs="1" />
						<xs:element name="IsTabletEnabled" type="SerializedTrueFalse01Type" minOccurs="0" maxOccurs="1" />
					</xs:all>
					<xs:attribute name="unmodified" use="optional" type="TrueFalse01Type" />
				</xs:complexType>
			</xs:element>
		</xs:sequence>
	</xs:complexType>
	<xs:complexType name="InteractionCentricDashboardsType">
		<xs:sequence>
			<xs:element name="InteractionCentricDashboard" minOccurs="0" maxOccurs="unbounded">
				<xs:complexType>
					<xs:all>
						<xs:element name="FormId" type="GuidType" minOccurs="1" maxOccurs="1" />
						<xs:element name="LocalizedNames" type="LocalizedNamesType" minOccurs="1" maxOccurs="1" />
						<xs:element name="Descriptions" type="DescriptionsType" minOccurs="0" maxOccurs="1" />
						<xs:element name="IsCustomizable" type="TrueFalse01Type" minOccurs="0" maxOccurs="1" />
						<xs:element name="IsDefault" type="SerializedTrueFalse01Type" minOccurs="0" maxOccurs="1" />
						<xs:element name="CanBeDeleted" type="TrueFalse01Type" minOccurs="0" maxOccurs="1" />
						<xs:element name="FormXml" type="FormXmlType" minOccurs="0" maxOccurs="1" />
						<xs:element name="IntroducedVersion" type="VersionType" minOccurs="0" maxOccurs="1" />
						<xs:element name="IsTabletEnabled" type="SerializedTrueFalse01Type" minOccurs="0" maxOccurs="1" />
						<xs:element name="ObjectTypeCode" type="xs:integer" minOccurs="0" maxOccurs="1" />
					</xs:all>
					<xs:attribute name="unmodified" use="optional" type="TrueFalse01Type" />
				</xs:complexType>
			</xs:element>
		</xs:sequence>
	</xs:complexType>
	<xs:complexType name="DialogsType">
		<xs:sequence>
			<xs:element name="Dialog" minOccurs="0" maxOccurs="unbounded">
				<xs:complexType>
					<xs:all>
						<xs:element name="FormId" type="GuidType" minOccurs="1" maxOccurs="1" />
						<xs:element name="LocalizedNames" type="LocalizedNamesType" minOccurs="1" maxOccurs="1" />
						<xs:element name="Descriptions" type="DescriptionsType" minOccurs="0" maxOccurs="1" />
						<xs:element name="UniqueName" type="xs:string" minOccurs="1" maxOccurs="1" />
						<xs:element name="IsCustomizable" type="TrueFalse01Type" minOccurs="0" maxOccurs="1" />
						<xs:element name="CanBeDeleted" type="TrueFalse01Type" minOccurs="0" maxOccurs="1" />
						<xs:element name="FormXml" type="FormXmlType" minOccurs="0" maxOccurs="1" />
						<xs:element name="IntroducedVersion" type="VersionType" minOccurs="0" maxOccurs="1" />
						<xs:element name="IsTabletEnabled" type="SerializedTrueFalse01Type" minOccurs="0" maxOccurs="1" />
					</xs:all>
					<xs:attribute name="unmodified" use="optional" type="TrueFalse01Type" />
				</xs:complexType>
			</xs:element>
		</xs:sequence>
	</xs:complexType>
	<xs:complexType name="ReportsType">
		<xs:sequence>
			<xs:element name="ReportSignatureIdMappings" minOccurs="0" maxOccurs="1">
				<xs:complexType>
					<xs:sequence>
						<xs:element name="ReportSignatureIdMapping" minOccurs="0" maxOccurs="unbounded">
							<xs:complexType>
								<xs:attribute name="reportid" type="GuidType" use="required" />
								<xs:attribute name="signatureid" type="GuidType" use="required" />
								<xs:attribute name="signaturelcid" type="xs:integer" use="required" />
							</xs:complexType>
						</xs:element>
					</xs:sequence>
				</xs:complexType>
			</xs:element>
			<xs:element name="Report" minOccurs="0" maxOccurs="unbounded">
				<xs:complexType>
					<xs:all>
						<xs:element name="name" type="xs:string" minOccurs="1" maxOccurs="1" />
						<xs:element name="defaultfilter" minOccurs="0" maxOccurs="1">
							<xs:annotation></xs:annotation>
						</xs:element>
						<xs:element name="iscustomreport" type="TrueFalse01Type" minOccurs="0" maxOccurs="1" />
						<xs:element name="description" type="xs:string" minOccurs="0" maxOccurs="1" />
						<xs:element name="filename" type="xs:string" minOccurs="0" maxOccurs="1" />
						<xs:element name="languagecode" type="xs:integer" minOccurs="0" maxOccurs="1" />
						<xs:element name="bodyurl" type="xs:string" minOccurs="0" maxOccurs="1" />
						<xs:element name="mimetype" type="xs:string" minOccurs="0" maxOccurs="1" />
						<xs:element name="reportid" type="GuidType" minOccurs="1" maxOccurs="1" />
						<xs:element name="iscustomizable" type="TrueFalse01Type" minOccurs="0" maxOccurs="1" />
						<xs:element name="IntroducedVersion" type="VersionType" minOccurs="0" maxOccurs="1" />
						<xs:element name="createdinmajorversion" type="xs:int" minOccurs="0" maxOccurs="1" />
						<xs:element name="reporttypecode" minOccurs="1" maxOccurs="1">
							<xs:simpleType>
								<xs:restriction base="xs:integer">
									<xs:enumeration value="1" />
									<xs:enumeration value="2" />
									<xs:enumeration value="3" />
								</xs:restriction>
							</xs:simpleType>
						</xs:element>
						<xs:element name="ExportedFileName" type="xs:string" minOccurs="0" maxOccurs="1" />
						<xs:element name="ReportVisibilities" minOccurs="0" maxOccurs="1">
							<xs:complexType>
								<xs:sequence>
									<xs:element name="ReportVisibility" minOccurs="0" maxOccurs="unbounded">
										<xs:simpleType>
											<xs:restriction base="xs:integer">
												<xs:enumeration value="1" />
												<xs:enumeration value="2" />
												<xs:enumeration value="3" />
											</xs:restriction>
										</xs:simpleType>
									</xs:element>
								</xs:sequence>
							</xs:complexType>
						</xs:element>
						<xs:element name="ReportCategories" minOccurs="0" maxOccurs="1">
							<xs:complexType>
								<xs:sequence>
									<xs:element name="ReportCategory" minOccurs="0" maxOccurs="unbounded">
										<xs:complexType>
											<xs:simpleContent>
												<xs:extension base="xs:integer">
													<xs:attribute name="name" type="xs:string" use="required" />
												</xs:extension>
											</xs:simpleContent>
										</xs:complexType>
									</xs:element>
								</xs:sequence>
							</xs:complexType>
						</xs:element>
						<xs:element name="ReportEntities" minOccurs="0" maxOccurs="1">
							<xs:complexType>
								<xs:sequence>
									<xs:element name="ReportEntity" type="EntityAttributeNameBaseType" minOccurs="0" maxOccurs="unbounded" />
								</xs:sequence>
							</xs:complexType>
						</xs:element>
					</xs:all>
					<xs:attribute name="unmodified" use="optional" type="TrueFalse01Type" />
				</xs:complexType>
			</xs:element>
			<xs:element name="ReportLinks" minOccurs="0" maxOccurs="1">
				<xs:complexType>
					<xs:sequence>
						<xs:element name="ReportLink" minOccurs="0" maxOccurs="unbounded">
							<xs:complexType>
								<xs:attribute name="reportid" type="GuidType" use="required" />
								<xs:attribute name="parentreportid" type="GuidType" use="required" />
							</xs:complexType>
						</xs:element>
					</xs:sequence>
				</xs:complexType>
			</xs:element>
		</xs:sequence>
	</xs:complexType>
	<xs:complexType name="SlasType">
		<xs:choice minOccurs="0" maxOccurs="unbounded">
			<xs:element name="Sla">
				<xs:complexType>
					<xs:sequence>
						<xs:element name="SLAId" type="GuidType" minOccurs="0" maxOccurs="1" />
						<xs:element name="ApplicableFrom" type="xs:string" minOccurs="0" maxOccurs="1" />
						<xs:element name="Name" type="xs:string" minOccurs="0" maxOccurs="1" />
						<xs:element name="Description" type="xs:string" minOccurs="0" maxOccurs="1" />
						<xs:element name="AllowPauseResume" type="xs:boolean" minOccurs="0" maxOccurs="1" />
						<xs:element name="SLAType" type="xs:integer" minOccurs="0" maxOccurs="1" />
						<xs:element name="PrimaryEntityOTC" type="xs:integer" minOccurs="0" maxOccurs="1" />
						<xs:element name="SlaItems" minOccurs="0" maxOccurs="unbounded">
							<xs:complexType>
								<xs:sequence>
									<xs:element name="SlaItem" minOccurs="0" maxOccurs="unbounded">
										<xs:complexType>
											<xs:sequence>
												<xs:element name="slaid" type="xs:string" minOccurs="1" maxOccurs="1" />
												<xs:element name="slaitemid" type="xs:string" minOccurs="1" maxOccurs="1" />
												<xs:element name="relatedfield" type="xs:string" minOccurs="1" maxOccurs="1" />
												<xs:element name="name" type="xs:string" minOccurs="1" maxOccurs="1" />
												<xs:element name="description" type="xs:string" minOccurs="0" maxOccurs="1" />
												<xs:element name="applicablewhenxml" type="xs:string" minOccurs="0" maxOccurs="1" />
												<xs:element name="successconditionsxml" type="xs:string" minOccurs="0" maxOccurs="1" />
												<xs:element name="sequencenumber" type="xs:string" minOccurs="0" maxOccurs="1" />
												<xs:element name="workflowid" type="xs:string" minOccurs="0" maxOccurs="1" />
												<xs:element name="failureafter" type="xs:string" minOccurs="0" maxOccurs="1" />
												<xs:element name="warnafter" type="xs:string" minOccurs="0" maxOccurs="1" />
											</xs:sequence>
											<xs:attribute name="slaitemid" type="xs:string" use="required" />
											<xs:attribute name="name" use="required" type="xs:string" />
										</xs:complexType>
									</xs:element>
								</xs:sequence>
							</xs:complexType>
						</xs:element>
					</xs:sequence>
					<xs:attribute name="SLAId" use="required" type="xs:string" />
					<xs:attribute name="Name" use="required" type="xs:string" />
					<xs:attribute name="PrimaryEntityOTC" use="optional" type="xs:int" />
					<xs:attribute name="PrimaryEntityLogicalName" use="optional" type="xs:string" />
				</xs:complexType>
			</xs:element>
		</xs:choice>
	</xs:complexType>
	<xs:complexType name="OrganizationSettingsType">
		<xs:sequence>
			<xs:element name="general" minOccurs="0" maxOccurs="1">
				<xs:complexType>
					<xs:sequence>
						<xs:element name="fullnameconventioncode" type="xs:integer" minOccurs="0" maxOccurs="1" />
						<xs:element name="numberformat" type="xs:string" minOccurs="0" maxOccurs="1" />
						<xs:element name="negativeformatcode" type="xs:integer" minOccurs="0" maxOccurs="1" />
						<xs:element name="currencysymbol" type="xs:string" minOccurs="0" maxOccurs="1" />
						<xs:element name="currencyformatcode" type="xs:integer" minOccurs="0" maxOccurs="1" />
						<xs:element name="pricingdecimalprecision" type="xs:integer" minOccurs="0" maxOccurs="1" />
						<xs:element name="sharetopreviousowneronassign" type="TrueFalseType" minOccurs="0" maxOccurs="1" />
						<xs:element name="blockedattachments" type="xs:string" minOccurs="0" maxOccurs="1" />
						<xs:element name="getstartedpanecontentenabled" type="TrueFalseType" minOccurs="0" maxOccurs="1" />
						<xs:element name="ispresenceenabled" type="TrueFalseType" minOccurs="0" maxOccurs="1" />
						<xs:element name="isautosaveenabled" type="TrueFalseType" minOccurs="0" maxOccurs="1" />
						<xs:element name="globalhelpurl" type="xs:string" minOccurs="0" maxOccurs="1" />
						<xs:element name="globalhelpurlenabled" type="TrueFalseType" minOccurs="0" maxOccurs="1" />
						<xs:element name="globalappendurlparametersenabled" type="TrueFalseType" minOccurs="0" maxOccurs="1" />
						<xs:element name="istextwrapenabled" type="TrueFalseType" minOccurs="0" maxOccurs="1" />
					</xs:sequence>
				</xs:complexType>
			</xs:element>
			<xs:element name="calendar" minOccurs="0" maxOccurs="1">
				<xs:complexType>
					<xs:sequence>
						<xs:element name="weekstartdaycode" type="xs:integer" minOccurs="0" maxOccurs="1" />
						<xs:element name="calendartype" type="xs:integer" minOccurs="0" maxOccurs="1" />
						<xs:element name="dateformatcode" type="xs:integer" minOccurs="0" maxOccurs="1" />
						<xs:element name="dateseparator" type="xs:string" minOccurs="0" maxOccurs="1" />
						<xs:element name="timeformatcode" type="xs:integer" minOccurs="0" maxOccurs="1" />
						<xs:element name="showweeknumber" type="TrueFalseType" minOccurs="0" maxOccurs="1" />
						<xs:element name="maxappointmentdurationdays" type="xs:integer" minOccurs="0" maxOccurs="1" />
					</xs:sequence>
				</xs:complexType>
			</xs:element>
			<xs:element name="email" minOccurs="0" maxOccurs="1">
				<xs:complexType>
					<xs:sequence>
						<xs:element name="trackingprefix" type="xs:string" minOccurs="0" maxOccurs="1" />
						<xs:element name="trackingtokenidbase" type="xs:integer" minOccurs="0" maxOccurs="1" />
						<xs:element name="trackingtokeniddigits" type="xs:byte" minOccurs="0" maxOccurs="1" />
						<xs:element name="maximumtrackingnumber" type="xs:integer" minOccurs="0" maxOccurs="1" />
						<xs:element name="ignoreinternalemail" type="TrueFalseType" minOccurs="0" maxOccurs="1" />
						<xs:element name="rendersecureiframeforemail" type="TrueFalseType" minOccurs="0" maxOccurs="1" />
						<xs:element name="allowunresolvedpartiesonemailsend" type="TrueFalseType" minOccurs="0" maxOccurs="1" />
					</xs:sequence>
				</xs:complexType>
			</xs:element>
			<xs:element name="marketing" minOccurs="0" maxOccurs="1">
				<xs:complexType>
					<xs:sequence>
						<xs:element name="allowmarketingemailexecution" type="TrueFalseType" minOccurs="0" maxOccurs="1" />
						<xs:element name="allowautoresponsecreation" type="TrueFalseType" minOccurs="0" maxOccurs="1" />
						<xs:element name="allowautounsubscribe" type="TrueFalseType" minOccurs="0" maxOccurs="1" />
						<xs:element name="allowautounsubscribeacknowledgement" type="TrueFalseType" minOccurs="0" maxOccurs="1" />
						<xs:element name="acknowledgementtemplateid" type="GuidType" minOccurs="0" maxOccurs="1" />
					</xs:sequence>
				</xs:complexType>
			</xs:element>
			<xs:element name="customization" minOccurs="0" maxOccurs="1">
				<xs:complexType>
					<xs:sequence>
						<xs:element name="isappmode" type="TrueFalseType" minOccurs="0" maxOccurs="1" />
					</xs:sequence>
				</xs:complexType>
			</xs:element>
			<xs:element name="outlookSynchronization" minOccurs="0" maxOccurs="1">
				<xs:complexType>
					<xs:sequence>
						<xs:element name="tagpollingperiod" type="xs:integer" minOccurs="0" maxOccurs="1" />
						<xs:element name="tagmaxaggressivecycles" type="xs:byte" minOccurs="0" maxOccurs="1" />
						<xs:element name="allowoutlookscheduledsyncs" type="TrueFalseType" minOccurs="0" maxOccurs="1" />
						<xs:element name="minoutlooksyncinterval" type="xs:integer" minOccurs="0" maxOccurs="1" />
						<xs:element name="emailsendpollingperiod" type="xs:integer" minOccurs="0" maxOccurs="1" />
						<xs:element name="allowofflinescheduledsyncs" type="TrueFalseType" minOccurs="0" maxOccurs="1" />
						<xs:element name="minofflinesyncinterval" type="xs:integer" minOccurs="0" maxOccurs="1" />
						<xs:element name="allowaddressbooksyncs" type="TrueFalseType" minOccurs="0" maxOccurs="1" />
						<xs:element name="minaddressbooksyncinterval" type="xs:integer" minOccurs="0" maxOccurs="1" />
					</xs:sequence>
				</xs:complexType>
			</xs:element>
			<xs:element name="autoNumbering" minOccurs="0" maxOccurs="1">
				<xs:complexType>
					<xs:sequence>
						<xs:element name="campaignprefix" type="xs:string" minOccurs="0" maxOccurs="1" />
						<xs:element name="contractprefix" type="xs:string" minOccurs="0" maxOccurs="1" />
						<xs:element name="caseprefix" type="xs:string" minOccurs="0" maxOccurs="1" />
						<xs:element name="kbprefix" type="xs:string" minOccurs="0" maxOccurs="1" />
						<xs:element name="kaprefix" type="xs:string" minOccurs="0" maxOccurs="1" />
						<xs:element name="categoryprefix" type="xs:string" minOccurs="0" maxOccurs="1" />
						<xs:element name="orderprefix" type="xs:string" minOccurs="0" maxOccurs="1" />
						<xs:element name="invoiceprefix" type="xs:string" minOccurs="0" maxOccurs="1" />
						<xs:element name="uniquespecifierlength" type="xs:integer" minOccurs="0" maxOccurs="1" />
					</xs:sequence>
				</xs:complexType>
			</xs:element>
			<xs:element name="sales" minOccurs="0" maxOccurs="1">
				<xs:complexType>
					<xs:sequence>
						<xs:element name="useinbuiltrulefordefaultpricelistselection" type="TrueFalseType" minOccurs="0" maxOccurs="1" />
						<xs:element name="maxproductsinbundle" type="xs:integer" minOccurs="0" maxOccurs="1" />
						<xs:element name="oobpricecalculationenabled" type="TrueFalseType" minOccurs="0" maxOccurs="1" />
						<xs:element name="discountcalculationmethod" type="xs:integer" minOccurs="0" maxOccurs="1" />
						<xs:element name="maximumdynamicpropertiesallowed" type="xs:integer" minOccurs="0" maxOccurs="1" />
						<xs:element name="createproductswithoutparentinactivestate" type="TrueFalseType" minOccurs="0" maxOccurs="1" />
					</xs:sequence>
				</xs:complexType>
			</xs:element>
			<xs:element name="externalapplications" minOccurs="0" maxOccurs="1">
				<xs:complexType>
					<xs:sequence>
						<xs:element name="externalpartyentitysettings" type="xs:string" minOccurs="0" maxOccurs="1" />
						<xs:element name="externalpartycorrelationkeys" type="xs:string" minOccurs="0" maxOccurs="1" />
					</xs:sequence>
				</xs:complexType>
			</xs:element>
			<xs:element name="modulescontextsettings" minOccurs="0" maxOccurs="1">
				<xs:complexType>
					<xs:sequence>
						<xs:element name="modulescontext" type="xs:string" minOccurs="0" maxOccurs="1" />
					</xs:sequence>
				</xs:complexType>
			</xs:element>
		</xs:sequence>
	</xs:complexType>
	<xs:complexType name="EntityRelationShipsType">
		<xs:choice minOccurs="0" maxOccurs="unbounded">
			<xs:element name="EntityRelationship">
				<xs:complexType>
					<xs:all>
						<xs:element name="EntityRelationshipType" type="EntityRelationshipTypeType" minOccurs="1" maxOccurs="1" />
						<xs:element name="IntroducedVersion" type="VersionType" minOccurs="0" maxOccurs="1" />
						<xs:element name="IsHierarchical" type="TrueFalse01Type" minOccurs="0" maxOccurs="1" />
						<xs:element name="IsCustomizable" type="TrueFalse01Type" minOccurs="0" maxOccurs="1" />
						<xs:element name="ReferencingAttributeName" type="EntityAttributeNameBaseType" minOccurs="0" maxOccurs="1" />
						<xs:element name="ReferencingAttributeRequiredLevel" type="xs:nonNegativeInteger" minOccurs="0" maxOccurs="1" />
						<xs:element name="RelationshipDescription" minOccurs="0" maxOccurs="1">
							<xs:complexType>
								<xs:sequence>
									<xs:element name="Descriptions" type="DescriptionsType" minOccurs="0" maxOccurs="1" />
								</xs:sequence>
							</xs:complexType>
						</xs:element>
						<xs:element name="ReferencingEntityName" type="xs:string" minOccurs="0" maxOccurs="1" />
						<xs:element name="ReferencedEntityName" type="xs:string" minOccurs="0" maxOccurs="1" />
						<xs:element name="FirstEntityName" type="xs:string" minOccurs="0" maxOccurs="1" />
						<xs:element name="SecondEntityName" type="xs:string" minOccurs="0" maxOccurs="1" />
						<xs:element name="IntersectEntityName" type="xs:string" minOccurs="0" maxOccurs="1" />
						<xs:element name="CascadeAssign" type="CrmCascadeSecurityLinkType" minOccurs="0" maxOccurs="1" />
						<xs:element name="CascadeDelete" type="CrmCascadeDeleteLinkType" minOccurs="0" maxOccurs="1" />
						<xs:element name="CascadeReparent" type="CrmCascadeSecurityLinkType" minOccurs="0" maxOccurs="1" />
						<xs:element name="CascadeShare" type="CrmCascadeSecurityLinkType" minOccurs="0" maxOccurs="1" />
						<xs:element name="CascadeUnshare" type="CrmCascadeSecurityLinkType" minOccurs="0" maxOccurs="1" />
						<xs:element name="CascadeRollupView" type="CrmCascadeSecurityLinkType" minOccurs="0" maxOccurs="1" />
						<xs:element name="IsValidForAdvancedFind" type="TrueFalse01Type" minOccurs="0" maxOccurs="1" />
						<xs:element name="field" minOccurs="0" maxOccurs="1">
							<xs:complexType>
								<xs:sequence>
									<xs:element name="IsCustomizable" type="TrueFalse01Type" minOccurs="0" maxOccurs="1" />
									<xs:element name="IsRenameable" type="TrueFalse01Type" minOccurs="0" maxOccurs="1" />
									<xs:element name="CanModifySearchSettings" type="TrueFalse01Type" minOccurs="0" maxOccurs="1" />
									<xs:element name="CanModifyRequirementLevelSettings" type="TrueFalse01Type" minOccurs="0" maxOccurs="1" />
									<xs:element name="CanModifyFieldLevelSecuritySettings" type="TrueFalse01Type" minOccurs="0" maxOccurs="1" />
									<xs:element name="IsSecured" type="TrueFalse01Type" minOccurs="0" maxOccurs="1" />
									<xs:element name="DisplayMask" type="xs:string" minOccurs="0" maxOccurs="1" />
									<xs:element name="IsAuditEnabled" type="TrueFalse01Type" minOccurs="0" maxOccurs="1" />
									<xs:element name="LinkedAttribute" type="xs:string" minOccurs="0" maxOccurs="1" />
									<xs:element name="displaynames" type="displaynamestype" minOccurs="0" maxOccurs="unbounded" />
								</xs:sequence>
								<xs:attribute name="name" type="xs:string" use="required" />
								<xs:attribute name="requiredlevel" type="xs:string" use="required" />
								<xs:attribute name="imemode" type="xs:string" use="optional" />
								<xs:attribute name="lookupstyle" type="xs:string" use="optional" />
								<xs:attribute name="lookupbrowse" type="TrueFalse01Type" use="optional" />
								<xs:attribute name="lookuptypes" type="xs:string" use="optional" />
								<xs:attribute name="format" type="xs:string" use="optional" />
							</xs:complexType>
						</xs:element>
						<xs:element name="EntityRelationshipRoles" type="EntityRelationshipRolesType" minOccurs="0" maxOccurs="1" />
					</xs:all>
					<xs:attribute name="Name" use="required" type="xs:string" />
					<xs:attribute name="unmodified" use="optional" type="TrueFalse01Type" />
				</xs:complexType>
			</xs:element>
		</xs:choice>
	</xs:complexType>
	<xs:complexType name="IconsType">
		<xs:sequence>
			<xs:element name="Icon" minOccurs="0" maxOccurs="unbounded">
				<xs:complexType>
					<xs:simpleContent>
						<xs:extension base="xs:base64Binary">
							<xs:attribute name="type" use="required" type="CrmEntityIconType" />
						</xs:extension>
					</xs:simpleContent>
				</xs:complexType>
			</xs:element>
		</xs:sequence>
	</xs:complexType>
	<xs:complexType name="StringsType">
		<xs:choice maxOccurs="unbounded">
			<xs:element name="Strings" minOccurs="0" maxOccurs="unbounded">
				<xs:complexType>
					<xs:sequence>
						<xs:element name="String" minOccurs="0" maxOccurs="unbounded">
							<xs:complexType>
								<xs:simpleContent>
									<xs:extension base="xs:string">
										<xs:attribute name="languagecode" use="required" type="xs:string" />
										<xs:attribute name="Comment" use="required" type="xs:string" />
									</xs:extension>
								</xs:simpleContent>
							</xs:complexType>
						</xs:element>
					</xs:sequence>
					<xs:attribute name="ResourceKey" use="required" type="xs:string" />
					<xs:attribute name="unmodified" use="optional" type="TrueFalse01Type" />
				</xs:complexType>
			</xs:element>
		</xs:choice>
	</xs:complexType>
	<xs:complexType name="FormXmlType">
		<xs:sequence>
			<xs:element name="forms" type="FormsType" minOccurs="0" maxOccurs="unbounded"></xs:element>
		</xs:sequence>
		<xs:attribute name="addedby" type="xs:string" />
		<xs:attribute name="id" type="GuidType" />
	</xs:complexType>
	<xs:complexType name="FormsType">
		<xs:sequence>
			<xs:element name="form" type="FormType" minOccurs="1" maxOccurs="unbounded" />
		</xs:sequence>
		<xs:attribute name="type" type="SystemFormType" />
	</xs:complexType>
	<xs:complexType name="SystemFormsType">
		<xs:sequence>
			<xs:element name="systemform" minOccurs="1" maxOccurs="unbounded">
				<xs:complexType>
					<xs:all>
						<xs:element name="formid" type="GuidType" minOccurs="1" maxOccurs="1" />
						<xs:element name="IsCustomizable" type="TrueFalse01Type" minOccurs="0" maxOccurs="1" />
						<xs:element name="IntroducedVersion" type="VersionType" minOccurs="0" maxOccurs="1" />
						<xs:element name="CanBeDeleted" type="TrueFalse01Type" minOccurs="0" maxOccurs="1" />
						<xs:element name="FormPresentation" type="xs:nonNegativeInteger" minOccurs="0" maxOccurs="1" />
						<xs:element name="FormActivationState" type="xs:nonNegativeInteger" minOccurs="0" maxOccurs="1" />
						<xs:element name="form" type="FormType" minOccurs="1" maxOccurs="1" />
						<xs:element name="LocalizedNames" type="LocalizedNamesType" minOccurs="1" maxOccurs="1" />
						<xs:element name="Descriptions" type="DescriptionsType" minOccurs="0" maxOccurs="1" />
					</xs:all>
				<xs:attribute name="unmodified" use="optional" type="TrueFalse01Type" />
				</xs:complexType>
			</xs:element>
		</xs:sequence>
		<xs:attribute name="type" type="SystemFormType" />
	</xs:complexType>
	<xs:simpleType name="NonEmptyStringType">
		<xs:restriction base="xs:string">
			<xs:minLength value="1" />
		</xs:restriction>
	</xs:simpleType>
	<xs:complexType name="RelationshipRolesType">
		<xs:sequence>
			<xs:element name="RelationshipRole" minOccurs="0" maxOccurs="unbounded">
				<xs:complexType>
					<xs:sequence>
						<xs:element name="relationshiproleid" type="GuidType" minOccurs="1" maxOccurs="1" />
						<xs:element name="name" type="xs:string" minOccurs="1" maxOccurs="1" />
						<xs:element name="statecode" type="xs:nonNegativeInteger" minOccurs="1" maxOccurs="1" />
						<xs:element name="RelationshipRoleMap" minOccurs="0" maxOccurs="unbounded">
							<xs:complexType>
								<xs:sequence>
									<xs:element name="relationshiprolemapid" type="GuidType" minOccurs="1" maxOccurs="1" />
									<xs:element name="associateobjecttypecode" type="ObjectTypeCodeType" minOccurs="1" maxOccurs="1" />
									<xs:element name="primaryobjecttypecode" type="ObjectTypeCodeType" minOccurs="1" maxOccurs="1" />
								</xs:sequence>
							</xs:complexType>
						</xs:element>
					</xs:sequence>
				</xs:complexType>
			</xs:element>
		</xs:sequence>
	</xs:complexType>
	<xs:complexType name="ConnectionRolesType">
		<xs:sequence>
			<xs:element name="ConnectionRoles" minOccurs="1" maxOccurs="unbounded">
				<xs:complexType>
					<xs:sequence>
						<xs:element name="ConnectionRole" minOccurs="1" maxOccurs="unbounded">
							<xs:complexType>
								<xs:sequence>
									<xs:element name="connectionroleid" type="GuidType" minOccurs="1" maxOccurs="1" />
									<xs:element name="name" type="xs:string" minOccurs="1" maxOccurs="1" />
									<xs:element name="category" type="xs:nonNegativeInteger" minOccurs="0" maxOccurs="1" />
									<xs:element name="description" type="xs:string" minOccurs="0" maxOccurs="1" />
									<xs:element name="IsCustomizable" type="TrueFalse01Type" minOccurs="0" maxOccurs="1" />
									<xs:element name="IntroducedVersion" type="VersionType" minOccurs="0" maxOccurs="1" />
									<xs:element name="ConnectionRoleObjectTypeCodes" minOccurs="0" maxOccurs="1">
										<xs:complexType>
											<xs:sequence>
												<xs:element name="ConnectionRoleObjectTypeCode" minOccurs="1" maxOccurs="unbounded">
													<xs:complexType>
														<xs:sequence>
															<xs:element name="connectionroleobjecttypecodeid" type="GuidType" minOccurs="1" maxOccurs="1" />
															<xs:element name="associatedobjecttypecode" type="xs:string" minOccurs="1" maxOccurs="1" />
														</xs:sequence>
													</xs:complexType>
												</xs:element>
											</xs:sequence>
										</xs:complexType>
									</xs:element>
								</xs:sequence>
							</xs:complexType>
						</xs:element>
					</xs:sequence>
				</xs:complexType>
			</xs:element>
			<xs:element name="ConnectionRoleAssociations" minOccurs="0" maxOccurs="1">
				<xs:complexType>
					<xs:sequence>
						<xs:element name="ConnectionRoleAssociation" minOccurs="0" maxOccurs="unbounded">
							<xs:complexType>
								<xs:sequence>
									<xs:element name="connectionroleid" type="GuidType" minOccurs="1" maxOccurs="1" />
									<xs:element name="associatedconnectionroleid" type="GuidType" minOccurs="1" maxOccurs="1" />
								</xs:sequence>
							</xs:complexType>
						</xs:element>
					</xs:sequence>
				</xs:complexType>
			</xs:element>
		</xs:sequence>
	</xs:complexType>
	<xs:complexType name="CrmTemplatesType">
		<xs:sequence>
			<xs:element name="KBArticleTemplates" minOccurs="0" maxOccurs="1">
				<xs:complexType>
					<xs:sequence>
						<xs:element name="kbarticletemplate" minOccurs="0" maxOccurs="unbounded">
							<xs:complexType>
								<xs:all>
									<xs:element name="kbarticletemplateid" type="GuidType" minOccurs="0" maxOccurs="1" />
									<xs:element name="structurexml" type="xs:string" minOccurs="0" maxOccurs="1" />
									<xs:element name="formatxml" type="xs:string" minOccurs="0" maxOccurs="1" />
									<xs:element name="title" type="xs:string" minOccurs="0" maxOccurs="1" />
									<xs:element name="description" type="xs:string" minOccurs="0" maxOccurs="1" />
									<xs:element name="languagecode" type="xs:nonNegativeInteger" minOccurs="0" maxOccurs="1" />
									<xs:element name="IsCustomizable" type="TrueFalse01Type" minOccurs="0" maxOccurs="1" />
									<xs:element name="IntroducedVersion" type="VersionType" minOccurs="0" maxOccurs="1" />
								</xs:all>
								<xs:attribute name="addedby" type="xs:string" />
								<xs:attribute name="id" use="optional" type="GuidType" />
								<xs:attribute name="name" use="optional" type="xs:string" />
								<xs:attribute name="description" use="optional" type="xs:string" />
								<xs:attribute name="unmodified" use="optional" type="TrueFalse01Type" />
							</xs:complexType>
						</xs:element>
					</xs:sequence>
				</xs:complexType>
			</xs:element>
			<xs:element name="EmailTemplates" minOccurs="0" maxOccurs="1">
				<xs:complexType>
					<xs:sequence>
						<xs:element name="emailtemplate" minOccurs="0" maxOccurs="unbounded">
							<xs:complexType>
								<xs:all>
									<xs:element name="templateid" type="GuidType" minOccurs="0" maxOccurs="1" />
									<xs:element name="subject" type="xs:string" minOccurs="0" maxOccurs="1" />
									<xs:element name="subjectpresentationxml" type="xs:string" minOccurs="0" maxOccurs="1" />
									<xs:element name="ispersonal" type="TrueFalse01Type" minOccurs="0" maxOccurs="1" />
									<xs:element name="mimetype" type="xs:string" minOccurs="0" maxOccurs="1" />
									<xs:element name="templatetypecode" type="xs:nonNegativeInteger" minOccurs="0" maxOccurs="1" />
									<xs:element name="generationtypecode" type="xs:nonNegativeInteger" minOccurs="0" maxOccurs="1" />
									<xs:element name="body" type="xs:string" minOccurs="0" maxOccurs="1" />
									<xs:element name="title" type="xs:string" minOccurs="0" maxOccurs="1" />
									<xs:element name="description" type="xs:string" minOccurs="0" maxOccurs="1" />
									<xs:element name="presentationxml" type="xs:string" minOccurs="0" maxOccurs="1" />
									<xs:element name="versionnumber" type="xs:nonNegativeInteger" minOccurs="0" maxOccurs="1" />
									<xs:element name="languagecode" type="xs:nonNegativeInteger" minOccurs="0" maxOccurs="1" />
									<xs:element name="IsCustomizable" type="TrueFalse01Type" minOccurs="0" maxOccurs="1" />
									<xs:element name="ActivityMimeAttachments" type="activitymimeattachmentstype" minOccurs="0" maxOccurs="1" />
									<xs:element name="IntroducedVersion" type="VersionType" minOccurs="0" maxOccurs="1" />
								</xs:all>
								<xs:attribute name="addedby" type="xs:string" />
								<xs:attribute name="id" use="optional" type="GuidType" />
								<xs:attribute name="name" use="optional" type="xs:string" />
								<xs:attribute name="description" use="optional" type="xs:string" />
								<xs:attribute name="unmodified" use="optional" type="TrueFalse01Type" />
							</xs:complexType>
						</xs:element>
					</xs:sequence>
				</xs:complexType>
			</xs:element>
			<xs:element name="ContractTemplates" minOccurs="0" maxOccurs="1">
				<xs:complexType>
					<xs:sequence>
						<xs:element name="contracttemplate" minOccurs="0" maxOccurs="unbounded">
							<xs:complexType>
								<xs:all>
									<xs:element name="contracttemplateid" type="GuidType" minOccurs="0" maxOccurs="1" />
									<xs:element name="name" type="xs:string" minOccurs="0" maxOccurs="1" />
									<xs:element name="abbreviation" type="xs:string" minOccurs="0" maxOccurs="1" />
									<xs:element name="description" type="xs:string" minOccurs="0" maxOccurs="1" />
									<xs:element name="IsCustomizable" type="TrueFalse01Type" minOccurs="0" maxOccurs="1" />
									<xs:element name="IntroducedVersion" type="VersionType" minOccurs="0" maxOccurs="1" />
									<xs:element name="contractservicelevelcode" minOccurs="0" maxOccurs="1">
										<xs:complexType>
											<xs:simpleContent>
												<xs:extension base="xs:nonNegativeInteger">
													<xs:anyAttribute processContents="skip" />
												</xs:extension>
											</xs:simpleContent>
										</xs:complexType>
									</xs:element>
									<xs:element name="billingfrequencycode" minOccurs="0" maxOccurs="1">
										<xs:complexType>
											<xs:simpleContent>
												<xs:extension base="xs:nonNegativeInteger">
													<xs:anyAttribute processContents="skip" />
												</xs:extension>
											</xs:simpleContent>
										</xs:complexType>
									</xs:element>
									<xs:element name="allotmenttypecode" minOccurs="0" maxOccurs="1">
										<xs:complexType>
											<xs:simpleContent>
												<xs:extension base="xs:nonNegativeInteger">
													<xs:anyAttribute processContents="skip" />
												</xs:extension>
											</xs:simpleContent>
										</xs:complexType>
									</xs:element>
									<xs:element name="usediscountaspercentage" minOccurs="0" maxOccurs="1">
										<xs:complexType>
											<xs:simpleContent>
												<xs:extension base="xs:nonNegativeInteger">
													<xs:anyAttribute processContents="skip" />
												</xs:extension>
											</xs:simpleContent>
										</xs:complexType>
									</xs:element>
									<xs:element name="effectivitycalendar" type="xs:string" minOccurs="0" maxOccurs="1" />
								</xs:all>
								<xs:attribute name="addedby" type="xs:string" />
								<xs:attribute name="id" use="optional" type="GuidType" />
								<xs:attribute name="name" use="optional" type="xs:string" />
								<xs:attribute name="description" use="optional" type="xs:string" />
								<xs:attribute name="unmodified" use="optional" type="TrueFalse01Type" />
							</xs:complexType>
						</xs:element>
					</xs:sequence>
				</xs:complexType>
			</xs:element>
			<xs:element name="MailMergeTemplates" minOccurs="0" maxOccurs="1">
				<xs:complexType>
					<xs:sequence>
						<xs:element name="mailmergetemplate" minOccurs="0" maxOccurs="unbounded">
							<xs:complexType>
								<xs:all>
									<xs:element name="mailmergetemplateid" type="GuidType" minOccurs="0" maxOccurs="1" />
									<xs:element name="name" type="xs:string" minOccurs="0" maxOccurs="1" />
									<xs:element name="defaultfilter" type="xs:string" minOccurs="0" maxOccurs="1" />
									<xs:element name="filename" type="xs:string" minOccurs="0" maxOccurs="1" />
									<xs:element name="parameterxml" type="xs:string" minOccurs="0" maxOccurs="1" />
									<xs:element name="mimetype" type="xs:string" minOccurs="0" maxOccurs="1" />
									<xs:element name="templatetypecode" type="xs:nonNegativeInteger" minOccurs="0" maxOccurs="1" />
									<xs:element name="mailmergetype" type="xs:nonNegativeInteger" minOccurs="0" maxOccurs="1" />
									<xs:element name="filesize" type="xs:nonNegativeInteger" minOccurs="0" maxOccurs="1" />
									<xs:element name="documentformat" type="xs:nonNegativeInteger" minOccurs="0" maxOccurs="1" />
									<xs:element name="languagecode" type="xs:nonNegativeInteger" minOccurs="0" maxOccurs="1" />
									<xs:element name="body" type="xs:string" minOccurs="0" maxOccurs="1" />
									<xs:element name="description" type="xs:string" minOccurs="0" maxOccurs="1" />
									<xs:element name="entityPlatformName" type="xs:string" minOccurs="0" maxOccurs="1" />
									<xs:element name="IsCustomizable" type="TrueFalse01Type" minOccurs="0" maxOccurs="1" />
									<xs:element name="IntroducedVersion" type="VersionType" minOccurs="0" maxOccurs="1" />
								</xs:all>
								<xs:attribute name="addedby" type="xs:string" />
								<xs:attribute name="id" use="optional" type="GuidType" />
								<xs:attribute name="name" use="optional" type="xs:string" />
								<xs:attribute name="description" use="optional" type="xs:string" />
								<xs:attribute name="unmodified" use="optional" type="TrueFalse01Type" />
							</xs:complexType>
						</xs:element>
					</xs:sequence>
				</xs:complexType>
			</xs:element>
		</xs:sequence>
	</xs:complexType>
	<xs:complexType name="activitymimeattachmentstype">
		<xs:sequence>
			<xs:element name="ActivityMimeAttachment" type="activitymimeattachmenttype" minOccurs="0" maxOccurs="unbounded" />
		</xs:sequence>
	</xs:complexType>
	<xs:complexType name="activitymimeattachmenttype">
		<xs:sequence>
			<xs:element name="activitymimeattachmentid" type="GuidType" minOccurs="0" maxOccurs="1" />
			<xs:element name="attachmentid" type="GuidType" minOccurs="0" maxOccurs="1" />
			<xs:element name="attachmentnumber" type="xs:nonNegativeInteger" minOccurs="0" maxOccurs="1" />
			<xs:element name="filename" type="xs:string" minOccurs="0" maxOccurs="1" />
			<xs:element name="filesize" type="xs:nonNegativeInteger" minOccurs="0" maxOccurs="1" />
			<xs:element name="objectid" type="GuidType" minOccurs="0" maxOccurs="1" />
			<xs:element name="mimetype" type="xs:string" minOccurs="0" maxOccurs="1" />
			<xs:element name="subject" type="xs:string" minOccurs="0" maxOccurs="1" />
			<xs:element name="SolutionAttachmentsFileName" type="xs:string" minOccurs="0" maxOccurs="1" />
		</xs:sequence>
	</xs:complexType>
	<xs:complexType name="SavedQueriesType">
		<xs:choice maxOccurs="unbounded">
			<xs:element name="savedqueries">
				<xs:complexType>
					<xs:sequence>
						<xs:element name="savedquery" minOccurs="0" maxOccurs="unbounded">
							<xs:complexType>
								<xs:all>
									<xs:element name="savedqueryid" type="GuidType" minOccurs="1" maxOccurs="1" />
									<xs:element name="queryapi" type="xs:string" minOccurs="0" maxOccurs="1" />
									<xs:element name="LocalizedNames" type="LocalizedNamesType" minOccurs="1" maxOccurs="1" />
									<xs:element name="Descriptions" type="DescriptionsType" minOccurs="0" maxOccurs="1" />
									<xs:element name="IsCustomizable" type="SerializedTrueFalse01Type" minOccurs="0" maxOccurs="1" />
									<xs:element name="CanBeDeleted" type="TrueFalse01Type" minOccurs="0" maxOccurs="1" />
									<xs:element name="isquickfindquery" type="SerializedTrueFalse01Type" minOccurs="0" maxOccurs="1" />
									<xs:element name="fetchxml" minOccurs="0" maxOccurs="1">
										<xs:complexType>
											<xs:sequence>
												<xs:element name="fetch" type="FetchType" minOccurs="0" maxOccurs="1" />
											</xs:sequence>
										</xs:complexType>
									</xs:element>
									<xs:element name="IntroducedVersion" type="VersionType" minOccurs="0" maxOccurs="1" />
									<xs:element name="isdefault" type="SerializedTrueFalse01Type" minOccurs="0" maxOccurs="1" />
									<xs:element name="isprivate" type="TrueFalse01Type" minOccurs="0" maxOccurs="1" />
									<xs:element name="returnedtypecode" type="SerializedInteger" minOccurs="0" maxOccurs="1" />
									<xs:element name="conditionalformatting" type="xs:string" minOccurs="0" maxOccurs="1" />
									<xs:element name="layoutxml" minOccurs="0" maxOccurs="1">
										<xs:complexType>
											<xs:sequence>
												<xs:element name="grid" minOccurs="0" maxOccurs="1">
													<xs:complexType>
														<xs:sequence>
															<xs:element name="row" minOccurs="0" maxOccurs="unbounded">
																<xs:complexType>
																	<xs:sequence>
																		<xs:element name="cell" minOccurs="0" maxOccurs="unbounded">
																			<xs:complexType>
																				<xs:attribute name="name" type="xs:string" />
																				<xs:attribute name="width" type="xs:nonNegativeInteger" />
																				<xs:attribute name="disableMetaDataBinding" type="TrueFalse01Type" />
																				<xs:attribute name="LabelId" type="xs:string" />
																				<xs:attribute name="ishidden" type="TrueFalse01Type" />
																				<xs:attribute name="disableSorting" type="TrueFalse01Type" />
																				<xs:attribute name="addedby" type="xs:string" />
																				<xs:attribute name="desc" type="xs:string" />
																				<xs:attribute name="cellType" type="xs:string" />
																				<xs:attribute name="imageproviderwebresource" type="xs:string" />
																				<xs:attribute name="imageproviderfunctionname" type="xs:string" />
																			</xs:complexType>
																		</xs:element>
																	</xs:sequence>
																	<xs:attribute name="name" type="xs:string" />
																	<xs:attribute name="id" type="xs:string" />
																	<xs:attribute name="multiobjectidfield" type="xs:string" />
																	<xs:attribute name="layoutstyle" type="xs:string" />
																</xs:complexType>
															</xs:element>
															<xs:element name="controlDescriptions" minOccurs="0" maxOccurs="1">
																<xs:complexType>
																	<xs:sequence>
																		<xs:element name="controlDescription" minOccurs="0" maxOccurs="unbounded">
																			<xs:complexType>
																				<xs:sequence>
																					<xs:element name="customControl" minOccurs="0" maxOccurs="unbounded">
																						<xs:complexType>
																							<xs:sequence>
																								<xs:element name="parameters" minOccurs="0" maxOccurs="1">
																									<xs:complexType>
																										<xs:sequence>
																											<xs:any minOccurs="0" maxOccurs="unbounded" processContents="skip"></xs:any>
																										</xs:sequence>
																									</xs:complexType>
																								</xs:element>
																							</xs:sequence>
																							<xs:attribute name="id" type="GuidType" use="optional" />
																							<xs:attribute name="formFactor" type="xs:integer" use="optional" />
																							<xs:attribute name="name" type="xs:string" use="optional" />
																							<xs:attribute name="version" type="xs:string" use="optional" />
																						</xs:complexType>
																					</xs:element>
																				</xs:sequence>
																				<xs:attribute name="forControl" type="xs:string" use="optional" />
																			</xs:complexType>
																		</xs:element>
																	</xs:sequence>
																</xs:complexType>
															</xs:element>
														</xs:sequence>
														<xs:attribute name="name" type="xs:string" />
														<xs:attribute name="object" type="ObjectTypeCodeType" />
														<xs:attribute name="jump" type="xs:string" />
														<xs:attribute name="select" type="TrueFalse01Type" />
														<xs:attribute name="icon" type="TrueFalse01Type" />
														<xs:attribute name="preview" type="TrueFalse01Type" />
														<xs:attribute name="iconrenderer" type="xs:string" />
													</xs:complexType>
												</xs:element>
											</xs:sequence>
										</xs:complexType>
									</xs:element>
									<xs:element name="querytype" type="SerializedInteger" minOccurs="0" maxOccurs="1" />
									<xs:element name="columnsetxml" minOccurs="0" maxOccurs="1">
										<xs:complexType>
											<xs:sequence>
												<xs:element name="columnset" minOccurs="0" maxOccurs="1">
													<xs:complexType>
														<xs:choice minOccurs="0" maxOccurs="unbounded">
															<xs:element name="ascend" type="xs:string" minOccurs="0" />
															<xs:element name="descend" type="xs:string" minOccurs="0" />
															<xs:element name="column" minOccurs="0" maxOccurs="unbounded">
																<xs:complexType>
																	<xs:simpleContent>
																		<xs:extension base="xs:string">
																			<xs:attribute name="addedby" type="xs:string" />
																		</xs:extension>
																	</xs:simpleContent>
																</xs:complexType>
															</xs:element>
															<xs:element ref="filter" minOccurs="0" maxOccurs="unbounded" />
														</xs:choice>
														<xs:attribute name="version" type="xs:string" />
														<xs:attribute name="distinct" type="xs:boolean" />
													</xs:complexType>
												</xs:element>
											</xs:sequence>
										</xs:complexType>
									</xs:element>
								</xs:all>
								<xs:attribute name="unmodified" use="optional" type="TrueFalse01Type" />
							</xs:complexType>
						</xs:element>
					</xs:sequence>
					<xs:attribute name="entity" type="xs:string" />
					<xs:attribute name="morerecords" type="xs:string" />
					<xs:attribute name="paging-cookie" type="xs:string" />
					<xs:attribute name="version" type="xs:string" />
				</xs:complexType>
			</xs:element>
		</xs:choice>
	</xs:complexType>
	<xs:complexType name="VisualizationsType">
		<xs:choice maxOccurs="unbounded">
			<xs:sequence>
				<xs:element name="visualization" minOccurs="0" maxOccurs="unbounded">
					<xs:complexType>
						<xs:all>
							<xs:element name="savedqueryvisualizationid" type="GuidType" minOccurs="1" maxOccurs="1" />
							<xs:element name="LocalizedNames" type="LocalizedNamesType" minOccurs="1" maxOccurs="1" />
							<xs:element name="Descriptions" type="DescriptionsType" minOccurs="0" maxOccurs="1" />
							<xs:element name="webresourcename" type="xs:string" minOccurs="0" maxOccurs="1" />
							<xs:element name="customizationlevel" minOccurs="0" maxOccurs="1">
								<xs:complexType>
									<xs:simpleContent>
										<xs:extension base="xs:integer">
											<xs:attribute name="formattedvalue" type="xs:integer" use="required" />
										</xs:extension>
									</xs:simpleContent>
								</xs:complexType>
							</xs:element>
							<xs:element name="datadescription" minOccurs="0" maxOccurs="1">
								<xs:annotation></xs:annotation>
							</xs:element>
							<xs:element name="presentationdescription" minOccurs="0" maxOccurs="1">
								<xs:annotation></xs:annotation>
							</xs:element>
							<xs:element name="isdefault" type="SerializedTrueFalse01Type" minOccurs="0" maxOccurs="1" />
							<xs:element name="IsCustomizable" type="TrueFalse01Type" minOccurs="0" maxOccurs="1" />
							<xs:element name="IntroducedVersion" type="VersionType" minOccurs="0" maxOccurs="1" />
							<xs:element name="CanBeDeleted" type="TrueFalse01Type" minOccurs="0" maxOccurs="1" />
						</xs:all>
						<xs:attribute name="unmodified" use="optional" type="TrueFalse01Type" />
					</xs:complexType>
				</xs:element>
			</xs:sequence>
		</xs:choice>
	</xs:complexType>
	<xs:complexType name="IgnoredType">
		<xs:sequence>
			<xs:any processContents="skip" minOccurs="0" maxOccurs="unbounded" />
		</xs:sequence>
	</xs:complexType>
	<xs:simpleType name="ChartGridMode">
		<xs:restriction base="xs:string">
			<xs:enumeration value="Chart" />
			<xs:enumeration value="Grid" />
			<xs:enumeration value="All" />
		</xs:restriction>
	</xs:simpleType>
	<xs:simpleType name="SystemFormType">
		<xs:restriction base="xs:string">
			<xs:enumeration value="main" />
			<xs:enumeration value="preview" />
			<xs:enumeration value="appointmentBook" />
			<xs:enumeration value="minicampaignbo" />
			<xs:enumeration value="mobile" />
			<xs:enumeration value="dashboard" />
			<xs:enumeration value="interactioncentricdashboard" />
			<xs:enumeration value="other" />
			<xs:enumeration value="quick" />
			<xs:enumeration value="quickCreate" />
			<xs:enumeration value="card" />
			<xs:enumeration value="mainInteractionCentric" />
			<xs:enumeration value="taskBasedForm" />
			<xs:enumeration value="dialog" />
		</xs:restriction>
	</xs:simpleType>
	<xs:complexType name="AppModuleSiteMapsType">
		<xs:sequence>
			<xs:element name="AppModuleSiteMap" type="AppModuleSiteMapType" minOccurs="0" maxOccurs="unbounded" />
		</xs:sequence>
	</xs:complexType>
	<xs:complexType name="AppModuleSiteMapType">
		<xs:sequence>
			<xs:element name="SiteMapUniqueName" type="xs:string" minOccurs="1" maxOccurs="1" />
			<xs:element name="SiteMapName" type="xs:string" minOccurs="0" maxOccurs="1" />
			<xs:element name="SiteMap" type="SiteMapType" minOccurs="1" maxOccurs="1">
				<xs:unique name="AreaIdMustBeUniqueForAppModuleSiteMap">
					<xs:selector xpath="Area" />
					<xs:field xpath="@Id" />
				</xs:unique>
			</xs:element>
			<xs:element name="LocalizedNames" type="LocalizedNamesType" minOccurs="0" maxOccurs="1" />
		</xs:sequence>
	</xs:complexType>
	<xs:complexType name="AppModulesType">
		<xs:sequence>
			<xs:element name="AppModule" type="AppModuleType" minOccurs="1" maxOccurs="unbounded" />
		</xs:sequence>
	</xs:complexType>
	<xs:complexType name="AppModuleType">
		<xs:sequence>
			<xs:element name="UniqueName" type="xs:string" minOccurs="1" maxOccurs="1" />
			<xs:element name="IntroducedVersion" type="VersionType" minOccurs="1" maxOccurs="1" />
			<xs:element name="WebResourceId" type="xs:string" minOccurs="1" maxOccurs="1" />
			<xs:element name="WelcomePageId" type="xs:string" minOccurs="0" maxOccurs="1" />
			<xs:element name="FormFactor" type="xs:integer" minOccurs="1" maxOccurs="1" />
			<xs:element name="ClientType" minOccurs="0" maxOccurs="1">
			<xs:simpleType>
				<xs:restriction base="xs:integer">
					<xs:enumeration value="2"/>
					<xs:enumeration value="4"/>
					<xs:enumeration value="8"/>
				</xs:restriction>
			</xs:simpleType>
			</xs:element>
			<xs:element name="URL" type="xs:string" minOccurs="0" maxOccurs="1" />
			<xs:element name="AppModuleComponents" minOccurs="1" maxOccurs="1">
				<xs:complexType>
					<xs:sequence>
						<xs:element name="AppModuleComponent" type="AppModuleComponentType" minOccurs="0" maxOccurs="unbounded" />
					</xs:sequence>
				</xs:complexType>
			</xs:element>
			<xs:element name="AppModuleRoleMaps" minOccurs="0" maxOccurs="1">
				<xs:complexType>
					<xs:sequence>
						<xs:element name="Role" type="AppModuleRoleType" minOccurs="1" maxOccurs="unbounded" />
					</xs:sequence>
				</xs:complexType>
			</xs:element>
			<xs:element name="AppConfig" minOccurs="0" maxOccurs="1">
				<xs:complexType>
					<xs:all>
						<xs:element name="IntroducedVersion" type="VersionType" minOccurs="1" maxOccurs="1" />
						<xs:element name="AppModuleUniqueName" type="xs:string" minOccurs="1" maxOccurs="1"></xs:element>
						<xs:element name="StatusCode" type="xs:int" minOccurs="1" maxOccurs="1"></xs:element>
						<xs:element name="StateCode" type="xs:int" minOccurs="1" maxOccurs="1"></xs:element>
						<xs:element name="AppConfigInstances" type="AppConfigInstancesType" minOccurs="0" maxOccurs="1" />
						<xs:element name="NavigationSettings" type="NavigationSettingsType" minOccurs="0" maxOccurs="1" />				
					</xs:all>
				</xs:complexType>
			</xs:element>			
			<xs:element name="LocalizedNames" type="LocalizedNamesType" minOccurs="1" maxOccurs="1" />
			<xs:element name="Descriptions" type="DescriptionsType" minOccurs="0" maxOccurs="1" />			
		</xs:sequence>
	</xs:complexType>
	<xs:complexType name="AppModuleComponentType">
		<xs:attribute name="type" use="required" type="xs:int" />
		<xs:attribute name="schemaName" use="optional" type="xs:string" />
		<xs:attribute name="id" use="optional" type="GuidType" />
		<xs:attribute name="parentId" use="optional" type="GuidType" />
		<xs:attribute name="behavior" use="optional" type="xs:int" />
		<xs:attribute name="solutionaction" use="optional" type="solutionactionType" />
	</xs:complexType>
	<xs:complexType name="AppModuleRoleType">
		<xs:attribute name="id" use="required" type="GuidType" />
		<xs:attribute name="solutionaction" use="optional" type="solutionactionType" />
	</xs:complexType>
	<xs:complexType name="EntityDataProvidersType">
		<xs:sequence>
			<xs:element name="EntityDataProvider" type="EntityDataProviderType" minOccurs="0" maxOccurs="unbounded" />
		</xs:sequence>
	</xs:complexType>
	<xs:complexType name="EntityDataProviderType">
		<xs:sequence>
			<xs:element name="EntityDataProviderId" type="GuidType" minOccurs="1" maxOccurs="1" />
			<xs:element name="Name" type="xs:string" minOccurs="1" maxOccurs="1" />
			<xs:element name="DataSourceLogicalName" type="xs:string" minOccurs="0" maxOccurs="1" />
			<xs:element name="IsCustomizable" type="TrueFalse01Type" minOccurs="0" maxOccurs="1" />
			<xs:element name="RetrievePluginTypeId" type="xs:string" minOccurs="0" maxOccurs="1" />
			<xs:element name="RetrieveMultiplePluginTypeId" type="xs:string" minOccurs="0" maxOccurs="1" />
		</xs:sequence>
	</xs:complexType>
	<xs:complexType name="AppConfigInstancesType">
		<xs:sequence>
			<xs:element name="AppConfigInstance" minOccurs="0" maxOccurs="unbounded">
				<xs:complexType>
					<xs:all>
						<xs:element name="AppConfigMasterId" type="GuidType" minOccurs="1" maxOccurs="1"></xs:element>
						<xs:element name="Value" type="xs:string" minOccurs="1" maxOccurs="1"></xs:element>
					</xs:all>
					<xs:attribute name="type" use="required" type="xs:int" />
					<xs:attribute name="schemaname" use="optional" type="xs:string" />
					<xs:attribute name="id" use="optional" type="GuidType" />
					<xs:attribute name="solutionaction" use="optional" type="solutionactionType" />
				</xs:complexType>
			</xs:element>
		</xs:sequence>
	</xs:complexType>
	<xs:complexType name="NavigationSettingsType">
		<xs:sequence>
			<xs:element name="NavigationSetting" minOccurs="0" maxOccurs="unbounded">
				<xs:complexType>
					<xs:all>
						<xs:element name="NavigationSettingId" type="GuidType" minOccurs="1" maxOccurs="1"></xs:element>
						<xs:element name="ParentNavigationSettingId" type="GuidType" minOccurs="0" maxOccurs="1"></xs:element>
						<xs:element name="ResourceId" type="GuidType" minOccurs="0" maxOccurs="1"></xs:element>
						<xs:element name="GroupName" type="xs:string" minOccurs="0" maxOccurs="1"></xs:element>
						<xs:element name="PageUrl" type="xs:string" minOccurs="0" maxOccurs="1"></xs:element>
						<xs:element name="QuickSettingOrder" type="xs:int" minOccurs="0" maxOccurs="1"></xs:element>
						<xs:element name="SettingType" type="xs:int" minOccurs="0" maxOccurs="1"></xs:element>
						<xs:element name="IconResourceId" type="GuidType" minOccurs="0" maxOccurs="1"></xs:element>
						<xs:element name="Privileges" type="xs:int" minOccurs="0" maxOccurs="1"></xs:element>
						<xs:element name="EntitySchemaName" type="xs:string" minOccurs="0" maxOccurs="1"></xs:element>
						<xs:element name="AdvancedSettingOrder" type="xs:int" minOccurs="0" maxOccurs="1"></xs:element>
						<xs:element name="LocalizedNames" minOccurs="1" maxOccurs="1">
							<xs:complexType>
								<xs:sequence>
									<xs:element name="LocalizedName" minOccurs="1" maxOccurs="unbounded">
										<xs:complexType>
											<xs:attribute name="description" type="xs:string" />
											<xs:attribute name="languagecode" type="xs:int" />
										</xs:complexType>
									</xs:element>
								</xs:sequence>
							</xs:complexType>
						</xs:element>
						<xs:element name="Descriptions" type="DescriptionsType" minOccurs="0" maxOccurs="1" ></xs:element>
					</xs:all>
					<xs:attribute name="solutionaction" use="optional" type="solutionactionType" />
				</xs:complexType>
			</xs:element>
		</xs:sequence>
	</xs:complexType>	
</xs:schema>
```

[!INCLUDE[footer-include](../../includes/footer-banner.md)]