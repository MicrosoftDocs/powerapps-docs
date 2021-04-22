---
title: "Define ribbon display rules (model-driven apps) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces"
description: "Learn about defining specific rules to control when the ribbon elements will display during the configuration of ribbon elements. " # 115-145 characters including spaces. This abstract displays in the search result."
keywords: ""
ms.date: 04/15/2021
ms.service: powerapps
ms.topic: article
ms.assetid: 70e5687f-4d0e-3d43-03f3-10e5aa5b0713
author: Nkrb # GitHub ID
ms.author: nabuthuk # MSFT alias of Microsoft employees only
manager: shilpas # MSFT alias of manager or PM counterpart
ms.reviewer: 
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---

# Define ribbon display rules

When configuring ribbon elements, you can define specific rules to control when the ribbon elements will display.  

- Use the /`RuleDefinitions`/DisplayRules/`<DisplayRule>` element to define rules controlling when the ribbon element should be displayed.  

- Use the /CommandDefinitions/`CommandDefinition`/DisplayRules/`<DisplayRule>` element to associate specific display rules to a command definition.  

[!INCLUDE[cc-terminology](../data-platform/includes/cc-terminology.md)]

## Control when ribbon elements are displayed  

By defining display rules in rule definitions, you can use the same display rule for many command definitions. When more than one display rule is defined for a command definition, all of the display rules must evaluate as true for the ribbon element to be displayed.  

All display rules provide an optional parameter to specify whether the default value of the rule is true or false and an optional `InvertResult` parameter to enable returning a negative result when the item being tested returns true.  

 The `/RuleDefinitions/DisplayRules/DisplayRule` element supports the following types of rules:  

 `<CommandClientTypeRule>`  
[!INCLUDE[ribbon_element_CommandClientTypeRule](../../includes/ribbon-element-commandclienttyperule.md)]

 The `Type` values correspond to the following:  


|   Value   |   Presentation       |
|-----------|----------------------------------|
| `Modern`  | The command bar is presented using Dynamics 365 for tablets.          |
| `Refresh` | The command bar is presented using the updated user interface.        |
| `Legacy`  | The ribbon is presented in forms for tables that were not updated or in a list view in Dynamics 365 for Outlook. |

 `<CrmClientTypeRule>`  
 Allows definition of rules depending on the type of client used. `Type` options are as follows:  

- Web  

- Outlook  

  `<CrmOfflineAccessStateRule>`  
  Use this criteria to display a ribbon element based on whether Dynamics 365 for Microsoft Office Outlook with Offline Access is currently offline.  

  `<CrmOutlookClientTypeRule>`  
  Use this rule if you want to display a button for the specific type of Dynamics 365 for Outlook. `Type` options are as follows:  

- CrmForOutlook  

- CrmForOutlookOfflineAccess  

  `<CrmOutlookClientVersionRule>`  
  [!INCLUDE[ribbon_element_CrmOutlookClientVersionRule](../../includes/ribbon-element-crmoutlookclientversionrule.md)]

  Valid values:  

- 2003  

- 2007  

- 2010  

  `<EntityPrivilegeRule>`  
  Use this kind of rule to display ribbon elements when a user has specific privileges for a table. You must specify the privilege depth and the specific privilege you want to check.  

  `<EntityPropertyRule>`  
  Allows definition of rules depending on the Boolean values of specific table properties. `PropertyName` options are as follows:  

- DuplicateDetectionEnabled  

- GridFiltersEnabled  

- HasStateCode  

- IsConnectionsEnabled  

- MailMergeEnabled  

- WorksWithQueue  

- HasActivities  

- IsActivity  

- HasNotes  

  `<EntityRule>`  
  This rule allow for evaluation of the current table. This is useful when you define custom actions that apply to the table template instead of for specific tables. For example, you may want to add a ribbon element to all tables except for some specific tables. It is easier to define the custom action for the table template that applies to all tables and then use an `EntityRule` to filter out those that should be excluded.  

  The `EntityRule` also includes an optional context parameter to specify whether the table is being displayed in the form or a list (HomePageGrid). The optional `AppliesTo` parameter can be set to `PrimaryEntity` or `SelectedEntity` to distinguish whether the table is being displayed in a subgrid.  

  `<FormEntityContextRule>`  
  [!INCLUDE[ribbon_element_FormEntityContextRule](../../includes/ribbon-element-formentitycontextrule.md)]

  `<FormStateRule`  
  Use the form state rule to determine the current type of form that is displaying a record. `State` options are as follows:  

- Create  

- Existing  

- ReadOnly  

- Disabled  

- BulkEdit  

  `<FormTypeRule>`  
  [!INCLUDE[ribbon_element_FormTypeRule](../../includes/ribbon-element-formtyperule.md)]

  The `Type` values correspond to the following:  

|Value|Presentation|  
|-----------|------------------|  
|`Main`|A form displayed in the application.|  
|`Preview`|The table preview form displayed as an expanding element in the grid.|  
|`AppointmentBook`|Used with the appointment, equipment, serviceappointment, and systemuser tables for the Service Scheduling user interface.|  
|`Dashboard`|The form defines a dashboard.|  
|`Quick`|A quick view form.|  
|`QuickCreate`|A quick create form.|  

 `<HideForTabletExperienceRule>`  
 [!INCLUDE[ribbon_element_HideForTabletExperienceRule](../../includes/ribbon-element-hidefortabletexperiencerule.md)]

 `<MiscellaneousPrivilegeRule>`  
 Use this kind of rule to check for privileges that do not apply to a specific table, such as ExportToExcel, MailMerge, or GoOffline.  

 `<OrganizationSettingRule>`  
 Use this to display a ribbon element if specific organization settings are enabled. Setting options are as follows:  

- IsSharepointEnabled  

- IsSOPIntegrationEnabled  

- IsFiscalCalendarDefined  

  `<OrRule>` 
  This rule lets you override the default AND comparison for multiple display rule types. Use the `OrRule` element to define several possible valid combinations to check.  

  `<OutlookRenderTypeRule>`  
  Use this to display a ribbon element if the ribbon is being displayed in [!INCLUDE[pn_MS_Outlook_Short](../../includes/pn-ms-outlook-short.md)] in a specific way. `Type` options are as follows:  

- Web  

- Outlook  

  `<OutlookVersionRule>`  
  Use this to display a ribbon element for a specific version of Outlook. `Version` options are as follows:  

- 2003  

- 2007  

- 2010  

  `<PageRule>`  
  This type of rule checks the URL of the page being displayed. It returns true if the address matches.  

  `<RelationshipTypeRule>` 
  This type of rule is applied to records selected in a grid. It lets you determine the type of relationship, as follows:  

- OneToMany  

- ManyToMany  

- NoRelationship  

  `<SkuRule>`  
  Use this kind of rule to display a ribbon element for a specific SKU version of Microsoft Dataverse, as follows:  

- OnPremise  

- Online  

- Spla  

  `<ValueRule>`  
  Use this rule to check the value of a specific column in the record being displayed in the form.  

> [!NOTE]
>  For commands defined for subgrid for forms using the updated user experience, value rules cannot be used within display rules. Use this element within an `<EnableRule>` to hide an element.  

### See also  
 [Customize commands and the ribbon](customize-commands-ribbon.md)   
 [Define ribbon enable rules](define-ribbon-enable-rules.md)   
 [Define ribbon actions](define-ribbon-actions.md)


[!INCLUDE[footer-include](../../includes/footer-banner.md)]