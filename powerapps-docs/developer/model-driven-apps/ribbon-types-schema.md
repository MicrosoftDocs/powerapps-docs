---
title: "Ribbon types schema (model-driven apps) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "The following is the schema definition for the ribbon types portion of an import/export customization file. It is included from the Ribbon Core Schema." # 115-145 characters including spaces. This abstract displays in the search result.
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
# Ribbon types schema

The following is the schema definition for the ribbon types portion of an import/export customization file. Ribbon types schema is included from the [Ribbon core schema](ribbon-core-schema.md). You can find schema  in the `Schemas\9.0.0.2090\RibbonTypes.xsd` folder when you download the Schemas zip file.

Download the [Schemas](https://download.microsoft.com/download/B/9/7/B97655A4-4E46-4E51-BA0A-C669106D563F/Schemas.zip).

For more information, see [Package and distribute Eetensions with solutions](../data-platform/introduction-solutions.md).

[!INCLUDE[cc-terminology](../data-platform/includes/cc-terminology.md)]
 
## Schema  
  
```xml  
<?xml version="1.0" encoding="utf-8"?>
<xs:schema id="CrmRibbonTypes" xmlns:xs="https://www.w3.org/2001/XMLSchema" >

	<!-- Command Definition Types -->
	<xs:complexType name="ActionsType">
		<xs:choice minOccurs="0" maxOccurs="unbounded">
			<xs:element name="JavaScriptFunction" type="JavaScriptFunctionType" />
			<xs:element name="Url" type="UrlType" />
			<xs:element name="OutlookCommand" type="OutlookCommandType" />
		</xs:choice>
	</xs:complexType>
	<xs:complexType name="CommandDefinitionsType">
		<xs:sequence>
			<xs:element name="CommandDefinition" type="CommandDefinitionType" minOccurs="0" maxOccurs="unbounded" />
		</xs:sequence>
	</xs:complexType>
	<xs:complexType name="CommandDefinitionType">
		<xs:sequence>
			<xs:element name="EnableRules" type="ReferenceEnableRulesType" minOccurs="1" maxOccurs="1" />
			<xs:element name="DisplayRules" type="ReferenceDisplayRulesType" minOccurs="1" maxOccurs="1" />
			<xs:element name="Actions" type="ActionsType" minOccurs="1" maxOccurs="1" />
		</xs:sequence>
		<xs:attribute name="Id" type="xs:string" use="required" />
	</xs:complexType>
	<xs:complexType name="JavaScriptFunctionType">
		<xs:sequence>
			<xs:group ref="ParameterType" minOccurs="0" maxOccurs="unbounded" />
		</xs:sequence>
		<xs:attribute name="FunctionName" type="JavaScriptIdentifier" use="required" />
		<xs:attribute name="Library" type="xs:string" use="required" />
	</xs:complexType>
	<xs:complexType name="OutlookCommandType">
		<xs:attribute name="ActionType" type="OutlookActionType" use="required" />
		<xs:attribute name="Data" type="xs:string" use="optional" />
	</xs:complexType>
	<xs:complexType name="ReferenceEnableRulesType">
		<xs:sequence>
			<xs:element name="EnableRule" type="ReferenceEnableRuleType" minOccurs="0" maxOccurs="unbounded" />
		</xs:sequence>
	</xs:complexType>
	<xs:complexType name="ReferenceDisplayRulesType">
		<xs:sequence>
			<xs:element name="DisplayRule" type="ReferenceDisplayRuleType" minOccurs="0" maxOccurs="unbounded" />
		</xs:sequence>
	</xs:complexType>
	<xs:complexType name="ReferenceEnableRuleType">
		<xs:attribute name="Id" type="xs:string" use="required" />
	</xs:complexType>
	<xs:complexType name="ReferenceDisplayRuleType">
		<xs:attribute name="Id" type="xs:string" use="required" />
	</xs:complexType>
	<xs:complexType name="UrlType">
		<xs:sequence>
			<xs:group ref="NamedParameterType" minOccurs="0" maxOccurs="unbounded" />
		</xs:sequence>
		<xs:attribute name="Address" type="xs:anyURI" use="required" />
		<xs:attribute name="WinMode" type="WinMode" use="optional" />
		<xs:attribute name="WinParams" type="xs:string" use="optional" />
		<xs:attribute name="PassParams" type="xs:boolean" use="optional" />
	</xs:complexType>

	<!-- Command Value Restrictions -->
	<xs:simpleType name="JavaScriptIdentifier">
		<xs:restriction base="xs:string">
			<xs:pattern value="[a-zA-Z_$][a-zA-Z_$0-9.]*" />
		</xs:restriction>
	</xs:simpleType>
	<xs:simpleType name="OutlookActionType">
		<xs:restriction base="xs:string">
			<xs:enumeration value="CheckForUpdates" />
			<xs:enumeration value="ConfigWizard" />
			<xs:enumeration value="GoTo" />
			<xs:enumeration value="GoOffline" />
			<xs:enumeration value="Help" />
			<xs:enumeration value="OpenOlkForm" />
			<xs:enumeration value="Promote" />
			<xs:enumeration value="SetRegarding" />
			<xs:enumeration value="Settings" />
			<xs:enumeration value="SignOut" />
			<xs:enumeration value="SignOutForgetMe" />
			<xs:enumeration value="OutlookImport" />
			<xs:enumeration value="Sync" />
		</xs:restriction>
	</xs:simpleType>
	<xs:simpleType name="WinMode">
		<xs:restriction base="xs:integer">
			<xs:minInclusive value="0" />
			<xs:maxInclusive value="2" />
		</xs:restriction>
	</xs:simpleType>

	<!-- Rule Container Types -->
	<xs:complexType name="RuleDefinitionsEntityType">
		<xs:sequence>
			<xs:element name="TabDisplayRules" type="TabDisplayRulesEntityType" minOccurs="1" maxOccurs="1" />
			<xs:element name="DisplayRules" type="DisplayRulesType" minOccurs="1" maxOccurs="1" />
			<xs:element name="EnableRules" type="EnableRulesType" minOccurs="1" maxOccurs="1" />
		</xs:sequence>
	</xs:complexType>
	<xs:complexType name="RuleDefinitionsGlobalType">
		<xs:sequence>
			<xs:element name="TabDisplayRules" type="TabDisplayRulesGlobalType" minOccurs="1" maxOccurs="1" />
			<xs:element name="DisplayRules" type="DisplayRulesType" minOccurs="1" maxOccurs="1" />
			<xs:element name="EnableRules" type="EnableRulesType" minOccurs="1" maxOccurs="1" />
		</xs:sequence>
	</xs:complexType>

	<xs:complexType name="EnableRulesType">
		<xs:sequence minOccurs="0" maxOccurs="unbounded">
			<xs:element name="EnableRule">
				<xs:complexType>
					<xs:choice minOccurs="1" maxOccurs="unbounded">
						<xs:group ref="EnableRulesGroup" />
						<xs:element name="OrRule" type="OrEnableRuleType" />
					</xs:choice>
					<xs:attribute name="Id" type="xs:string" use="required" />
				</xs:complexType>
			</xs:element>
		</xs:sequence>
	</xs:complexType>

	<xs:complexType name="OrEnableRuleType">
		<xs:sequence minOccurs="2" maxOccurs="unbounded">
			<xs:element name="Or">
				<xs:complexType>
					<xs:choice minOccurs="1" maxOccurs="unbounded">
						<xs:group ref="EnableRulesGroup" />
					</xs:choice>
				</xs:complexType>
			</xs:element>
		</xs:sequence>
	</xs:complexType>

	<xs:group name="EnableRulesGroup">
		<xs:choice>
			<xs:element name="CrmClientTypeRule" type="CrmClientTypeRuleType" />
			<xs:element name="CrmOutlookClientTypeRule" type="CrmOutlookClientTypeRuleType" />
			<xs:element name="CrmOfflineAccessStateRule" type="CrmOfflineAccessStateRuleType" />
			<xs:element name="CustomRule" type="CustomRuleType" />
			<xs:element name="EntityRule" type="EntityRuleType" />
			<xs:element name="FormStateRule" type="FormStateRuleType" />
			<xs:element name="OutlookItemTrackingRule" type="OutlookItemTrackingRuleType" />
			<xs:element name="OutlookVersionRule" type="OutlookVersionRuleType" />
			<xs:element name="PageRule" type="PageRuleType" />
			<xs:element name="RecordPrivilegeRule" type="RecordPrivilegeRuleType" />
			<xs:element name="SelectionCountRule" type="SelectionCountRuleType" />
			<xs:element name="SkuRule" type="SkuRuleType" />
			<xs:element name="ValueRule" type="ValueRuleType" />
			<xs:element name="CommandClientTypeRule" type="CommandClientTypeRuleType" />
		</xs:choice>
	</xs:group>

	<xs:complexType name="TabDisplayRulesEntityType">
		<xs:sequence minOccurs="0" maxOccurs="unbounded">
			<xs:element name="TabDisplayRule">
				<xs:complexType>
					<xs:choice minOccurs="1" maxOccurs="unbounded">
						<xs:element name="EntityRule" type="EntityTabRuleType" />
					</xs:choice>
					<xs:attribute name="TabCommand" type="xs:string" use="required" />
				</xs:complexType>
			</xs:element>
		</xs:sequence>
	</xs:complexType>

	<xs:complexType name="TabDisplayRulesGlobalType">
		<xs:sequence minOccurs="0" maxOccurs="unbounded">
			<xs:element name="TabDisplayRule">
				<xs:complexType>
					<xs:choice minOccurs="1" maxOccurs="unbounded">
						<xs:element name="EntityRule" type="EntityTabRuleType" />
						<xs:element name="PageRule" type="PageTabRuleType" />
					</xs:choice>
					<xs:attribute name="TabCommand" type="xs:string" use="required" />
				</xs:complexType>
			</xs:element>
		</xs:sequence>
	</xs:complexType>

	<xs:complexType name="DisplayRulesType">
		<xs:sequence minOccurs="0" maxOccurs="unbounded">
			<xs:element name="DisplayRule">
				<xs:complexType>
					<xs:choice minOccurs="1" maxOccurs="unbounded">
						<xs:group ref="DisplayRulesGroup" />
						<xs:element name="OrRule" type="OrDisplayRuleType" />
					</xs:choice>
					<xs:attribute name="Id" type="xs:string" use="required" />
				</xs:complexType>
			</xs:element>
		</xs:sequence>
	</xs:complexType>

	<xs:complexType name="OrDisplayRuleType">
		<xs:sequence minOccurs="2" maxOccurs="unbounded">
			<xs:element name="Or">
				<xs:complexType>
					<xs:choice minOccurs="1" maxOccurs="unbounded">
						<xs:group ref="DisplayRulesGroup" />
					</xs:choice>
				</xs:complexType>
			</xs:element>
		</xs:sequence>
	</xs:complexType>

	<xs:group name="DisplayRulesGroup">
		<xs:choice>
			<xs:element name="CrmClientTypeRule" type="CrmClientTypeRuleType" />
			<xs:element name="CommandClientTypeRule" type="CommandClientTypeRuleType" />
			<xs:element name="DeviceTypeRule" type="DeviceTypeRuleType" />
			<xs:element name="CrmOutlookClientTypeRule" type="CrmOutlookClientTypeRuleType" />
			<xs:element name="CrmOutlookClientVersionRule" type="CrmOutlookClientVersionRuleType" />
			<xs:element name="CrmOfflineAccessStateRule" type="CrmOfflineAccessStateRuleType" />
			<xs:element name="EntityRule" type="EntityRuleType" />
			<xs:element name="EntityPrivilegeRule" type="EntityPrivilegeRuleType" />
			<xs:element name="EntityPropertyRule" type="EntityPropertyRuleType" />
			<xs:element name="FormEntityContextRule" type="FormEntityContextRuleType" />
			<xs:element name="FormStateRule" type="FormStateRuleType" />
			<xs:element name="MiscellaneousPrivilegeRule" type="MiscellaneousPrivilegeRuleType" />
			<xs:element name="OrganizationSettingRule" type="OrganizationSettingRuleType" />
			<xs:element name="OutlookRenderTypeRule" type="OutlookRenderTypeRuleType" />
			<xs:element name="OutlookVersionRule" type="OutlookVersionRuleType" />
			<xs:element name="PageRule" type="PageRuleType" />
			<xs:element name="ReferencingAttributeRequiredRule" type="ReferencingAttributeRequiredRuleType" />
			<xs:element name="RelationshipTypeRule" type="RelationshipTypeRuleType" />
			<xs:element name="SkuRule" type="SkuRuleType" />
			<xs:element name="ValueRule" type="ValueRuleType" />
			<xs:element name="OptionSetRule" type ="OptionSetRuleType" />
			<xs:element name="FormTypeRule" type ="FormTypeRuleType" />
			<xs:element name="HideForTabletExperienceRule" type ="HideForTabletExperienceRuleType" />
			<xs:element name="HideIfNetBreezeNotAvailableRule" type ="HideIfNetBreezeNotAvailableRuleType" />
			<xs:element name="HideIfServiceMetadataAvailableRule" type ="HideIfServiceMetadataAvailableRuleType" />
			<xs:element name="HideIfSharepointS2SConfigurationEnabledRule" type ="HideIfSharepointS2SConfigurationEnabledRuleType" />
			<xs:element name="HideIfExportToExcelNotEnabledRule" type="HideIfExportToExcelNotEnabledRuleType" />
			<xs:element name="IsExportToExcelOnlineEnabledRule" type="IsExportToExcelOnlineEnabledRuleType" />
			<xs:element name="HideIfDisabledForMobileRule" type="HideIfDisabledForMobileRuleType" />
			<xs:element name="HideIfHybridSSSNotEnabledRule" type="HideIfHybridSSSNotEnabledRuleType" />
			<xs:element name="HideIfEmailSignatureNotEnabledRule" type="HideIfEmailSignatureNotEnabledRuleType" />
			<xs:element name="HideIfReverseHybridSSSNotEnabledRule" type="HideIfReverseHybridSSSNotEnabledRuleType" />
			<xs:element name="FeatureControlRule" type="FeatureControlRuleType" />
			<xs:element name="HideIfDelveNotAvailableRule" type ="HideIfDelveNotAvailableRuleType" />
			<xs:element name="HideIfTestExchangeServerNotEnabledRule" type="HideIfTestExchangeServerNotEnabledRuleType" />
			<xs:element name="HideIfSSSTroubleshootingNotEnabledRule" type="HideIfSSSTroubleshootingNotEnabledRuleType" />
			<xs:element name="HideIfCurrentUserIsNotSystemAdministratorRule" type="HideIfCurrentUserIsNotSystemAdministratorRuleType" />
			<xs:element name="HideIfPowerBITileNotAvailableRule" type ="HideIfPowerBITileNotAvailableRuleType" />
			<xs:element name="HideIfProcessActiveRule" type="HideIfProcessActiveRuleType" />
			<xs:element name="HideIfProcessInactiveRule" type="HideIfProcessInactiveRuleType" />
			<xs:element name="HideIfProcessUnificationIsDisabledRule" type="HideIfProcessUnificationIsDisabledRuleType" /> 
			<xs:element name="HideIfO365UserDoesNotHaveExchangeSubscriptionsRule" type ="HideIfO365UserDoesNotHaveExchangeSubscriptionsRuleType" />
			<xs:element name="HideIfEmailIsApprovedByAdminRule" type ="HideIfEmailIsApprovedByAdminType" />
			<xs:element name="HideIfUserIsNotTenantAdminRule" type ="HideIfUserIsNotTenantAdminType" />
			<xs:element name="HideIfEmailIsApprovedByAdminBasedOnESPRule" type ="HideIfEmailIsApprovedByAdminBasedOnESPRuleType" />
			<xs:element name="HideIfProductRecommendationsNotEnabledRule" type ="HideIfProductRecommendationsNotEnabledType" />
		</xs:choice>
	</xs:group>

	<!-- Rule Types -->
	<xs:complexType name="CrmClientTypeRuleType">
		<xs:attribute name="Type" use="required">
			<xs:simpleType>
				<xs:restriction base="xs:string">
					<xs:enumeration value="Web" />
					<xs:enumeration value="Outlook" />
				</xs:restriction>
			</xs:simpleType>
		</xs:attribute>
		<xs:attributeGroup ref="StandardRuleAttributes" />
	</xs:complexType>

	<xs:complexType name="CommandClientTypeRuleType">
		<xs:attribute name="Type" use="required">
			<xs:simpleType>
				<xs:restriction base="xs:string">
					<xs:enumeration value="Modern" />
					<xs:enumeration value="Refresh" />
					<xs:enumeration value="Legacy" />
				</xs:restriction>
			</xs:simpleType>
		</xs:attribute>
		<xs:attributeGroup ref="StandardRuleAttributes" />
	</xs:complexType>

	<xs:complexType name="DeviceTypeRuleType">
		<xs:attribute name="Type" use="required">
			<xs:simpleType>
				<xs:restriction base="xs:string">
					<xs:enumeration value="None" />
					<xs:enumeration value="Phone" />
					<xs:enumeration value="Tablet" />
					<xs:enumeration value="Web" />
					<xs:enumeration value="Outlook" />
					<xs:enumeration value="InteractionCentric" />
				</xs:restriction>
			</xs:simpleType>
		</xs:attribute>
		<xs:attributeGroup ref="StandardRuleAttributes" />
	</xs:complexType>

	<xs:complexType name="CrmOfflineAccessStateRuleType">
		<xs:attribute name="State" use="required">
			<xs:simpleType>
				<xs:restriction base="xs:string">
					<xs:enumeration value="Online" />
					<xs:enumeration value="Offline" />
				</xs:restriction>
			</xs:simpleType>
		</xs:attribute>
		<xs:attributeGroup ref="StandardRuleAttributes" />
	</xs:complexType>

	<xs:complexType name="CrmOutlookClientTypeRuleType">
		<xs:attribute name="Type" use="required">
			<xs:simpleType>
				<xs:restriction base="xs:string">
					<xs:enumeration value="CrmForOutlook" />
					<xs:enumeration value="CrmForOutlookOfflineAccess" />
				</xs:restriction>
			</xs:simpleType>
		</xs:attribute>
		<xs:attributeGroup ref="StandardRuleAttributes" />
	</xs:complexType>

	<xs:complexType name="OptionSetRuleType">
		<xs:attribute name="OptionSet" type="xs:string" use="required"/>
		<xs:attribute name="StateCode" type="xs:string" use="required"/>
		<xs:attribute name="ObjectTypeCode" type="xs:string" use="required"/>
		<xs:attributeGroup ref="StandardRuleAttributes" />
	</xs:complexType>
	
	<xs:complexType name="CustomRuleType">
		<xs:sequence>
			<xs:group ref="ParameterType" minOccurs="0" maxOccurs="unbounded" />
		</xs:sequence>
		<xs:attribute name="FunctionName" type="JavaScriptIdentifier" use="required" />
		<xs:attribute name="Library" type="xs:string" use="required" />
		<xs:attributeGroup ref="StandardRuleAttributes" />
	</xs:complexType>

	<xs:complexType name="EntityRuleType">
		<xs:attributeGroup ref="EntityRuleTypeAttributes" />
		<xs:attributeGroup ref="StandardRuleAttributes" />
	</xs:complexType>
	<xs:complexType name="EntityTabRuleType">
		<xs:attributeGroup ref="EntityRuleTypeAttributes" />
	</xs:complexType>
	<xs:attributeGroup name="EntityRuleTypeAttributes">
		<xs:attribute name="EntityName" type="xs:string" use="optional" />
		<xs:attribute name="AppliesTo" type="AppliesToType" use="optional" />
		<xs:attribute name="Context" use="optional">
			<xs:simpleType>
				<xs:restriction base="xs:string">
					<xs:pattern value="[a-zA-Z_][a-zA-Z_0-9]*" />
				</xs:restriction>
			</xs:simpleType>
		</xs:attribute>
	</xs:attributeGroup>

	<xs:complexType name="EntityPropertyRuleType">
		<xs:attribute name="EntityName" type="xs:string" use="optional" />
		<xs:attribute name="AppliesTo" type="AppliesToType" use="optional" />
		<xs:attribute name="PropertyName" use="required">
			<xs:simpleType>
				<xs:restriction base="xs:string">
					<xs:enumeration value="DuplicateDetectionEnabled" />
					<xs:enumeration value="GridFiltersEnabled" />
					<xs:enumeration value="HasStateCode" />
					<xs:enumeration value="IsConnectionsEnabled" />
					<xs:enumeration value="MailMergeEnabled" />
					<xs:enumeration value="WorksWithQueue" />
					<xs:enumeration value="HasActivities" />
					<xs:enumeration value="IsActivity" />
					<xs:enumeration value="HasNotes" />
					<xs:enumeration value="IsCustomizable" />
					<xs:enumeration value="IsActivityParty" />
					<xs:enumeration value="HasEmailAddresses" />
					<xs:enumeration value="IsChildEntity" />
					<xs:enumeration value="IsImportable" />
					<xs:enumeration value="IsEnabledForCharts" />
					<xs:enumeration value="IsBusinessProcessEnabled" />
					<xs:enumeration value="HasFeedback" />
					<xs:enumeration value="IsBPFEntity" />
				</xs:restriction>
			</xs:simpleType>
		</xs:attribute>
		<xs:attribute name="PropertyValue" type="xs:boolean" use="required" />
		<xs:attributeGroup ref="StandardRuleAttributes" />
	</xs:complexType>

	<xs:complexType name="FormEntityContextRuleType">
		<xs:attribute name="EntityName" type="xs:string" use="required" />
		<xs:attributeGroup ref="StandardRuleAttributes" />
	</xs:complexType>

	<xs:complexType name="FormStateRuleType">
		<xs:attribute name="State" use="required">
			<xs:simpleType>
				<xs:restriction base="xs:string">
					<xs:enumeration value="Create" />
					<xs:enumeration value="Existing" />
					<xs:enumeration value="ReadOnly" />
					<xs:enumeration value="Disabled" />
					<xs:enumeration value="BulkEdit" />
				</xs:restriction>
			</xs:simpleType>
		</xs:attribute>
		<xs:attributeGroup ref="StandardRuleAttributes" />
	</xs:complexType>

	<xs:complexType name="OrganizationSettingRuleType">
		<xs:attribute name="Setting" use="required">
			<xs:simpleType>
				<xs:restriction base="xs:string">
					<xs:enumeration value="IsSharepointEnabled" />
					<xs:enumeration value="IsSOPIntegrationEnabled" />
					<xs:enumeration value="IsFiscalCalendarDefined" />
					<xs:enumeration value="IsReadFormModeDefined" />
					<xs:enumeration value="IsBPFEntityCustomizationFeatureEnabled" />
				</xs:restriction>
			</xs:simpleType>
		</xs:attribute>
		<xs:attributeGroup ref="StandardRuleAttributes" />
	</xs:complexType>
	
	<xs:complexType name="FormTypeRuleType">
		<xs:attribute name="Type" use="required">
			<xs:simpleType>
				<xs:restriction base="xs:string">
					<xs:enumeration value="Main" />
					<xs:enumeration value="Preview" />
					<xs:enumeration value="AppointmentBook" />
					<xs:enumeration value="Dashboard" />
					<xs:enumeration value="Quick" />
					<xs:enumeration value="QuickCreate" />
					<xs:enumeration value="Card" />
					<xs:enumeration value="MainInteractionCentric" />
				</xs:restriction>
			</xs:simpleType>
		</xs:attribute>
		<xs:attributeGroup ref="StandardRuleAttributes" />
	</xs:complexType>

	<xs:complexType name="HideForTabletExperienceRuleType">
		<xs:attributeGroup ref="StandardRuleAttributes" />
	</xs:complexType>

	<xs:complexType name="HideIfNetBreezeNotAvailableRuleType">
		<xs:attributeGroup ref="StandardRuleAttributes" />
	</xs:complexType>

	<xs:complexType name="HideIfDisabledForMobileRuleType">
		<xs:attributeGroup ref="StandardRuleAttributes" />
	</xs:complexType>

	<xs:complexType name="HideIfServiceMetadataAvailableRuleType">
		<xs:attributeGroup ref="StandardRuleAttributes" />
	</xs:complexType>

	<xs:complexType name="HideIfSharepointS2SConfigurationEnabledRuleType">
		<xs:attributeGroup ref="StandardRuleAttributes" />
	</xs:complexType>

	<xs:complexType name="HideIfExportToExcelNotEnabledRuleType">
		<xs:attributeGroup ref="StandardRuleAttributes" />
	</xs:complexType>
	
	<xs:complexType name="IsExportToExcelOnlineEnabledRuleType">
		<xs:attributeGroup ref="StandardRuleAttributes" />
	</xs:complexType>

	<xs:complexType name="HideIfDelveNotAvailableRuleType">
		<xs:attributeGroup ref="StandardRuleAttributes" />
	</xs:complexType>
	
	<xs:complexType name="HideIfPowerBITileNotAvailableRuleType">
		<xs:attributeGroup ref="StandardRuleAttributes" />
	</xs:complexType>

	<xs:complexType name="HideIfProcessActiveRuleType">
		<xs:attributeGroup ref="StandardRuleAttributes" />
	</xs:complexType>

	<xs:complexType name="HideIfProcessInactiveRuleType">
		<xs:attributeGroup ref="StandardRuleAttributes" />
	</xs:complexType>
	
	<xs:complexType name="HideIfProcessUnificationIsDisabledRuleType">
		<xs:attributeGroup ref="StandardRuleAttributes" />
	</xs:complexType>
	
	<xs:complexType name="HideIfO365UserDoesNotHaveExchangeSubscriptionsRuleType">
		<xs:attributeGroup ref="StandardRuleAttributes" />
	</xs:complexType>
	
	<xs:complexType name="HideIfEmailIsApprovedByAdminBasedOnESPRuleType">
		<xs:attributeGroup ref="StandardRuleAttributes" />
	</xs:complexType>
	
	<xs:complexType name="HideIfSSSTroubleshootingNotEnabledRuleType">
		<xs:attributeGroup ref="StandardRuleAttributes" />
	</xs:complexType>

	<xs:complexType name="HideIfCurrentUserIsNotSystemAdministratorRuleType">
		<xs:attributeGroup ref="StandardRuleAttributes" />
	</xs:complexType>

	<xs:complexType name="HideIfHybridSSSNotEnabledRuleType">
		<xs:attributeGroup ref="StandardRuleAttributes" />
	</xs:complexType>

	<xs:complexType name="HideIfEmailSignatureNotEnabledRuleType">
		<xs:attributeGroup ref="StandardRuleAttributes" />
	</xs:complexType>
	
	<xs:complexType name="HideIfReverseHybridSSSNotEnabledRuleType">
		<xs:attributeGroup ref="StandardRuleAttributes" />
	</xs:complexType>

	<xs:complexType name="HideIfEmailIsApprovedByAdminType">
		<xs:attributeGroup ref="StandardRuleAttributes" />
	</xs:complexType>
	
	<xs:complexType name="HideIfUserIsNotTenantAdminType">
		<xs:attributeGroup ref="StandardRuleAttributes" />
	</xs:complexType>
	
	<xs:complexType name="HideIfProductRecommendationsNotEnabledType">
		<xs:attributeGroup ref="StandardRuleAttributes" />
	</xs:complexType>

	<xs:complexType name="HideIfTestExchangeServerNotEnabledRuleType">
		<xs:attributeGroup ref="StandardRuleAttributes" />
	</xs:complexType>

	<xs:complexType name="OutlookItemTrackingRuleType">
		<xs:attribute name="TrackedInCrm" type="xs:boolean" use="required" />
		<xs:attribute name="AppliesTo" type="AppliesToPrimaryType" use="optional" />
		<xs:attributeGroup ref="StandardRuleAttributes" />
	</xs:complexType>

	<xs:complexType name="OutlookRenderTypeRuleType">
		<xs:attribute name="Type" use="required">
			<xs:simpleType>
				<xs:restriction base="xs:string">
					<xs:enumeration value="Web" />
					<xs:enumeration value="Outlook" />
				</xs:restriction>
			</xs:simpleType>
		</xs:attribute>
		<xs:attributeGroup ref="StandardRuleAttributes" />
	</xs:complexType>

	<xs:complexType name="OutlookVersionRuleType">
		<xs:attribute name="Version" use="required">
			<xs:simpleType>
				<xs:restriction base="xs:string">
					<xs:enumeration value="2003" />
					<xs:enumeration value="2007" />
					<xs:enumeration value="2010" />
				</xs:restriction>
			</xs:simpleType>
		</xs:attribute>
		<xs:attributeGroup ref="StandardRuleAttributes" />
	</xs:complexType>

	<xs:complexType name="CrmOutlookClientVersionRuleType">
		<xs:attribute name="Major" type="xs:integer" use="required"/>
		<xs:attribute name="Minor" type="xs:integer" use="optional"/>
		<xs:attribute name="Build" type="xs:integer" use="optional"/>
		<xs:attribute name="Revision" type="xs:integer" use="optional"/>
		<xs:attributeGroup ref="StandardRuleAttributes" />
	</xs:complexType>

	<xs:complexType name="PageRuleType">
		<xs:attribute name="Address" type="xs:anyURI" use="required" />
		<xs:attributeGroup ref="StandardRuleAttributes" />
	</xs:complexType>
	<xs:complexType name="PageTabRuleType">
		<xs:attribute name="Address" type="xs:anyURI" use="required" />
	</xs:complexType>

	<xs:complexType name="RecordPrivilegeRuleType">
		<xs:attribute name="PrivilegeType" type="PrivilegeTypeType" use="required" />
		<xs:attribute name="AppliesTo" type="AppliesToPrimaryType" use="optional" />
		<xs:attributeGroup ref="StandardRuleAttributes" />
	</xs:complexType>
	<xs:complexType name="EntityPrivilegeRuleType">
		<xs:attribute name="PrivilegeType" type="PrivilegeTypeType" use="required" />
		<xs:attribute name="PrivilegeDepth" type="PrivilegeDepthType" use="required" />
		<xs:attribute name="AppliesTo" type="AppliesToType" use="optional" />
		<xs:attribute name="EntityName" type="xs:string" use="optional" />
		<xs:attributeGroup ref="StandardRuleAttributes" />
	</xs:complexType>

	<xs:complexType name="MiscellaneousPrivilegeRuleType">
		<xs:attribute name="PrivilegeName" type="xs:string" use="required" />
		<xs:attribute name="PrivilegeDepth" type="PrivilegeDepthType" use="optional" />
		<xs:attributeGroup ref="StandardRuleAttributes" />
	</xs:complexType>

	<xs:complexType name="ReferencingAttributeRequiredRuleType">
		<xs:attributeGroup ref="StandardRuleAttributes" />
	</xs:complexType>

	<xs:complexType name="RelationshipTypeRuleType">
		<xs:attribute name="AppliesTo" type="AppliesToSelectedType" use="required" />
		<xs:attribute name="RelationshipType" use="optional">
			<xs:simpleType>
				<xs:restriction base="xs:string">
					<xs:enumeration value="OneToMany" />
					<xs:enumeration value="ManyToMany" />
					<xs:enumeration value="NoRelationship" />
				</xs:restriction>
			</xs:simpleType>
		</xs:attribute>
		<xs:attribute name="AllowCustomRelationship" use="optional" type="xs:boolean" default="true" />
		<xs:attribute name="AllowSystemRelationship" use="optional" type="xs:boolean" default="true" />
		<xs:attributeGroup ref="StandardRuleAttributes" />
	</xs:complexType>

	<xs:complexType name="SelectionCountRuleType">
		<xs:attribute name="AppliesTo" type="AppliesToType" use="optional" />
		<xs:attribute name="Minimum" type="xs:integer" use="optional" />
		<xs:attribute name="Maximum" type="xs:integer" use="optional" />
		<xs:attributeGroup ref="StandardRuleAttributes" />
	</xs:complexType>

	<xs:complexType name="SkuRuleType">
		<xs:attribute name="Sku" use="required">
			<xs:simpleType>
				<xs:restriction base="xs:string">
					<xs:enumeration value="OnPremise" />
					<xs:enumeration value="Online" />
					<xs:enumeration value="Spla" />
				</xs:restriction>
			</xs:simpleType>
		</xs:attribute>
		<xs:attributeGroup ref="StandardRuleAttributes" />
	</xs:complexType>

	<xs:complexType name="ValueRuleType">
		<xs:attribute name="Field" type="xs:string" use="required" />
		<xs:attribute name="Value" type="xs:string" use="required" />
		<xs:attributeGroup ref="StandardRuleAttributes" />
	</xs:complexType>
	
	<xs:complexType name="FeatureControlRuleType">
		<xs:attribute name="FeatureControlBit" type="xs:string" use="required" />
		<xs:attribute name="ExpectedValue" type="xs:boolean" use="required" />
		<xs:attributeGroup ref="StandardRuleAttributes" />
	</xs:complexType>

	<!-- Rule Attributes -->
	<xs:attributeGroup name="StandardRuleAttributes">
		<xs:attribute name="Default" type="xs:boolean" use="optional" />
		<xs:attribute name="InvertResult" type="xs:boolean" use="optional" />
	</xs:attributeGroup>

	<!-- Rule Value Restrictions -->
	<xs:simpleType name="AppliesToType">
		<xs:restriction base="xs:string">
			<xs:enumeration value="PrimaryEntity" />
			<xs:enumeration value="SelectedEntity" />
		</xs:restriction>
	</xs:simpleType>
	<xs:simpleType name="AppliesToPrimaryType">
		<xs:restriction base="xs:string">
			<xs:enumeration value="PrimaryEntity" />
		</xs:restriction>
	</xs:simpleType>
	<xs:simpleType name="AppliesToSelectedType">
		<xs:restriction base="xs:string">
			<xs:enumeration value="SelectedEntity" />
		</xs:restriction>
	</xs:simpleType>
	
	<xs:simpleType name="PrivilegeDepthType">
		<xs:restriction base="xs:string">
			<xs:enumeration value="None" />
			<xs:enumeration value="Basic" />
			<xs:enumeration value="Local" />
			<xs:enumeration value="Deep" />
			<xs:enumeration value="Global" />
		</xs:restriction>
	</xs:simpleType>
	<xs:simpleType name="PrivilegeTypeType">
		<xs:restriction base="xs:string">
			<xs:enumeration value="Create" />
			<xs:enumeration value="Read" />
			<xs:enumeration value="Write" />
			<xs:enumeration value="Delete" />
			<xs:enumeration value="Assign" />
			<xs:enumeration value="Share" />
			<xs:enumeration value="Append" />
			<xs:enumeration value="AppendTo" />
		</xs:restriction>
	</xs:simpleType>

	<!-- Parameter Types -->
	<xs:group name="ParameterType">
		<xs:choice>
			<xs:element name="BoolParameter" type="BoolParameterType" />
			<xs:element name="CrmParameter" type="CrmParameterType" />
			<xs:element name="DecimalParameter" type="DecimalParameterType" />
			<xs:element name="IntParameter" type="IntParameterType" />
			<xs:element name="StringParameter" type="StringParameterType" />
		</xs:choice>
	</xs:group>
	<xs:group name="NamedParameterType">
		<xs:choice>
			<xs:element name="BoolParameter" type="BoolNamedParameterType" />
			<xs:element name="CrmParameter" type="CrmNamedParameterType" />
			<xs:element name="DecimalParameter" type="DecimalNamedParameterType" />
			<xs:element name="IntParameter" type="IntNamedParameterType" />
			<xs:element name="StringParameter" type="StringNamedParameterType" />
		</xs:choice>
	</xs:group>
	<xs:complexType name="BoolParameterType">
		<xs:attribute name="Value" type="xs:boolean" use="required" />
	</xs:complexType>
	<xs:complexType name="BoolNamedParameterType">
		<xs:attribute name="Value" type="xs:boolean" use="required" />
		<xs:attribute name="Name" type="xs:string" use="required" />
	</xs:complexType>
	<xs:complexType name="CrmParameterType">
		<xs:attribute name="Value" type="CrmParameterValue" use="required" />
	</xs:complexType>
	<xs:complexType name="CrmNamedParameterType">
		<xs:attribute name="Value" type="CrmNamedParameterValue" use="required" />
		<xs:attribute name="Name" type="xs:string" use="required" />
	</xs:complexType>
	<xs:complexType name="DecimalParameterType">
		<xs:attribute name="Value" type="xs:decimal" use="required" />
	</xs:complexType>
	<xs:complexType name="DecimalNamedParameterType">
		<xs:attribute name="Value" type="xs:decimal" use="required" />
		<xs:attribute name="Name" type="xs:string" use="required" />
	</xs:complexType>
	<xs:complexType name="IntParameterType">
		<xs:attribute name="Value" type="xs:integer" use="required" />
	</xs:complexType>
	<xs:complexType name="IntNamedParameterType">
		<xs:attribute name="Value" type="xs:integer" use="required" />
		<xs:attribute name="Name" type="xs:string" use="required" />
	</xs:complexType>
	<xs:complexType name="StringParameterType">
		<xs:attribute name="Value" type="xs:string" use="required" />
	</xs:complexType>
	<xs:complexType name="StringNamedParameterType">
		<xs:attribute name="Value" type="xs:string" use="required" />
		<xs:attribute name="Name" type="xs:string" use="required" />
	</xs:complexType>

	<xs:simpleType name="CrmParameterValue">
		<xs:restriction base="xs:string">
			<xs:enumeration value="PrimaryEntityTypeCode" />
			<xs:enumeration value="PrimaryEntityTypeName" />
			<xs:enumeration value="PrimaryItemIds" />
			<xs:enumeration value="FirstPrimaryItemId" />
			<xs:enumeration value="PrimaryControl" />
			<xs:enumeration value="PrimaryControlId" />
			<xs:enumeration value="SelectedEntityTypeCode" />
			<xs:enumeration value="SelectedEntityTypeName" />
			<xs:enumeration value="FirstSelectedItemId" />
			<xs:enumeration value="SelectedControl" />
			<xs:enumeration value="SelectedControlSelectedItemCount" />
			<xs:enumeration value="SelectedControlSelectedItemIds" />
			<xs:enumeration value="SelectedControlSelectedItemReferences" />
			<xs:enumeration value="SelectedControlAllItemCount" />
			<xs:enumeration value="SelectedControlAllItemIds" />
			<xs:enumeration value="SelectedControlAllItemReferences" />
			<xs:enumeration value="SelectedControlUnselectedItemCount" />
			<xs:enumeration value="SelectedControlUnselectedItemIds" />
			<xs:enumeration value="SelectedControlUnselectedItemReferences" />
			<xs:enumeration value="OrgName" />
			<xs:enumeration value="OrgLcid" />
			<xs:enumeration value="UserLcid" />
			<xs:enumeration value="CommandProperties" />
		</xs:restriction>
	</xs:simpleType>
	
	<xs:simpleType name="CrmNamedParameterValue">
		<xs:restriction base="xs:string">
			<xs:enumeration value="PrimaryEntityTypeCode" />
			<xs:enumeration value="PrimaryEntityTypeName" />
			<xs:enumeration value="PrimaryItemIds" />
			<xs:enumeration value="FirstPrimaryItemId" />
			<xs:enumeration value="PrimaryControl" />
			<xs:enumeration value="PrimaryControlId" />
			<xs:enumeration value="SelectedEntityTypeCode" />
			<xs:enumeration value="SelectedEntityTypeName" />
			<xs:enumeration value="FirstSelectedItemId" />
			<xs:enumeration value="SelectedControl" />
			<xs:enumeration value="SelectedControlSelectedItemCount" />
			<xs:enumeration value="SelectedControlSelectedItemIds" />
			<xs:enumeration value="SelectedControlAllItemCount" />
			<xs:enumeration value="SelectedControlAllItemIds" />
			<xs:enumeration value="SelectedControlUnselectedItemCount" />
			<xs:enumeration value="SelectedControlUnselectedItemIds" />
			<xs:enumeration value="OrgName" />
			<xs:enumeration value="OrgLcid" />
			<xs:enumeration value="UserLcid" />
			<xs:enumeration value="CommandProperties" />
		</xs:restriction>
	</xs:simpleType>

	<!-- LocLabels Types -->
	<xs:complexType name="RibbonLocLabelsType">
		<xs:sequence minOccurs="1" maxOccurs="1">
			<xs:element name="LocLabel" type="RibbonLocLabelType" minOccurs="0" maxOccurs="unbounded" />
		</xs:sequence>
	</xs:complexType>
	<xs:complexType name="RibbonLocLabelType">
		<xs:sequence minOccurs="1" maxOccurs="1">
			<xs:element name="Titles" type="RibbonTitlesType" minOccurs="1" maxOccurs="1" />
		</xs:sequence>
		<xs:attribute name="Id" type="xs:string" use="required" />
	</xs:complexType>
	<xs:complexType name="RibbonTitlesType">
		<xs:sequence minOccurs="1" maxOccurs="1">
			<xs:element name="Title" type="RibbonTitleType" minOccurs="1" maxOccurs="unbounded" />
		</xs:sequence>
	</xs:complexType>
	<xs:complexType name="RibbonTitleType">
		<xs:attribute name="description" type="xs:string" use="required" />
		<xs:attribute name="languagecode" type="xs:int" use="required" />
	</xs:complexType>
</xs:schema>

```  
  
### See also  
 [Customize commands and the ribbon](customize-commands-ribbon.md)   
 [Ribbon core schema](ribbon-core-schema.md)   
 [Ribbon WSS schema](ribbon-wss-schema.md)   
 [Customization XML reference](customization-xml-reference.md)


[!INCLUDE[footer-include](../../includes/footer-banner.md)]