---
title: "Define Ribbon Display Rules (Model-Driven Apps)"
description: "Learn how ribbon display rules control when elements appear in model-driven apps, and use available rule types to configure command visibility."
author: clromano
ms.author: clromano
ms.date: 02/02/2024
ms.reviewer: jdaly
ms.topic: article
ms.subservice: mda-developer
search.audienceType: 
  - developer
contributors: 
  - JimDaly
  - caburk
---

# Define ribbon display rules

[!INCLUDE [cc-modern-commanding](../data-platform/includes/cc-modern-commanding.md)]

Use ribbon display rules to control when ribbon elements appear, so commands show only in the appropriate client, form, table, or user context.  

- Use the `/RuleDefinitions/DisplayRules/DisplayRule` element to define rules that control when to display the ribbon element.  
- Use the `/CommandDefinitions/CommandDefinition/DisplayRules/DisplayRule` element to associate specific display rules with a command definition.  

[!INCLUDE[cc-terminology](../data-platform/includes/cc-terminology.md)]

## Control when to display ribbon elements  

By defining display rules in rule definitions, you can use the same display rule for many command definitions. When you define more than one display rule for a command definition, all of the display rules must evaluate as true for the ribbon element to display.  

All display rules provide an optional parameter to specify whether the default value of the rule is true or false, and an optional `InvertResult` parameter to enable returning a negative result when the item being tested returns true.  

 The `/RuleDefinitions/DisplayRules/DisplayRule` element supports the following types of rules:  

## `<CommandClientTypeRule>`  

[!INCLUDE[ribbon_element_CommandClientTypeRule](../../includes/ribbon-element-commandclienttyperule.md)]

The `Type` values correspond to the following:  


|   Value   |   Presentation       |
|-----------|----------------------------------|
| `Modern`  | The command bar is presented using Dynamics 365 for tablets.          |
| `Refresh` | The command bar is presented using the updated user interface.        |
| `Legacy`  | The ribbon is presented in forms for tables that aren't updated or in a list view in Dynamics 365 for Outlook. |

## `<CrmClientTypeRule>`

 Define rules based on the type of client used. `Type` options are:  

- `Web`  
- `Outlook`  

## `<CrmOfflineAccessStateRule>`  

Use this criteria to display a ribbon element based on whether Dynamics 365 for Microsoft Office Outlook with Offline Access is currently offline.  

## `<CrmOutlookClientTypeRule>`  

Use this rule if you want to display a button for the specific type of Dynamics 365 for Outlook. `Type` options are as follows:  

- `CrmForOutlook`  
- `CrmForOutlookOfflineAccess`  

## `<CrmOutlookClientVersionRule>`  

[!INCLUDE[ribbon_element_CrmOutlookClientVersionRule](../../includes/ribbon-element-crmoutlookclientversionrule.md)]

  Valid values:  

- `2003`  
- `2007`  
- `2010`  

## `<EntityPrivilegeRule>`  

Use this kind of rule to display ribbon elements when a user has specific privileges for a table. You must specify the privilege depth and the specific privilege you want to check.  

## `<EntityPropertyRule>`  

Use this rule to define rules based on the Boolean values of specific table properties. The `PropertyName` options are:  

- `DuplicateDetectionEnabled`  
- `GridFiltersEnabled`  
- `HasStateCode`  
- `IsConnectionsEnabled`  
- `MailMergeEnabled`  
- `WorksWithQueue`  
- `HasActivities`  
- `IsActivity`  
- `HasNotes`  

## `<EntityRule>`  

Use this rule to evaluate the current table. This rule is useful when you define custom actions that apply to the table template instead of specific tables. For example, you might want to add a ribbon element to all tables except for some specific tables. It's easier to define the custom action for the table template that applies to all tables and then use an `EntityRule` to filter out those that you want to exclude.  

The `EntityRule` includes an optional context parameter to specify whether the table is displayed in the form or a list (HomePageGrid). Set the optional `AppliesTo` parameter to `PrimaryEntity` or `SelectedEntity` to distinguish whether the table is displayed in a subgrid.  

## `<FormEntityContextRule>`  

[!INCLUDE[ribbon_element_FormEntityContextRule](../../includes/ribbon-element-formentitycontextrule.md)]

## `<FormStateRule`  

Use the form state rule to determine the current type of form that is displaying a record. `State` options are as follows:  

- `Create` 
- `Existing`  
- `ReadOnly`  
- `Disabled`  
- `BulkEdit`  

## `<FormTypeRule>`  

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

## `<HideForTabletExperienceRule>`  

[!INCLUDE[ribbon_element_HideForTabletExperienceRule](../../includes/ribbon-element-hidefortabletexperiencerule.md)]

## `<MiscellaneousPrivilegeRule>`  

Use this rule to check for privileges that don't apply to a specific table, such as ExportToExcel, MailMerge, or GoOffline.  

## `<OrganizationSettingRule>`  

Use this rule to display a ribbon element if specific organization settings are enabled. The setting options are:  

- `IsSharepointEnabled`  
- `IsSOPIntegrationEnabled`  
- `IsFiscalCalendarDefined`  

## `<OrRule>` 

Use this rule to override the default AND comparison for multiple display rule types. Use the `OrRule` element to define several possible valid combinations to check.  


## `<OutlookRenderTypeRule>`  

Use this rule to display a ribbon element if the ribbon is displayed in [!INCLUDE[pn_MS_Outlook_Short](../../includes/pn-ms-outlook-short.md)] in a specific way. The `Type` options are:  

   - `Web`  
   - `Outlook`  

## `<OutlookVersionRule>`  

Use this rule to display a ribbon element for a specific version of Outlook. The `Version` options are:  

- `2003`  
- `2007`  
- `2010`  

## `<PageRule>`  

This rule checks the URL of the page being displayed. It returns true if the address matches.

## `<ReferencingAttributeRequiredRule>`

A rule that detects whether the referencing attribute for an entity is required.

This rule is for a very specific case. Use this rule when there's a relationship-bound subgrid or an associated grid on the page. This rule tests whether the referencing attribute used in the relationship is required. Use this rule to hide the **Add Existing** record type button when it isn't appropriate to display it.

In an entity relationship, the lookup field in the related record (the referencing attribute) might be required or not. For example, the **Regarding** field of an activity isn't required, but the **Potential Customer** field of an opportunity is required. The **Add Existing Activity** button sets the **Regarding** field value to the current record context and it can only work if the **Regarding** field doesn't already have a value. All opportunity records have a value in their **Potential Customer** field, so it never makes sense to display an **Add Existing Opportunity** button. This rule detects that the referencing attribute is required and returns true.

## `<RelationshipTypeRule>` 

Apply this rule to records selected in a grid. It lets you determine the type of relationship, as follows:  

- `OneToMany`  
- `ManyToMany`  
- `NoRelationship`  

## `<SkuRule>`  
  
Use this rule to display a ribbon element for a specific SKU version of Microsoft Dataverse, as follows:  

- `OnPremise`  
- `Online`  
- `Spla`  

## `<ValueRule>`  

Use this rule to check the value of a specific column in the record displayed in the form.  

> [!NOTE]
>  For commands defined for subgrid for forms using the updated user experience, you can't use value rules within display rules. Use this element within an `<EnableRule>` to hide an element.  

### See also  

[Customize commands and the ribbon](customize-commands-ribbon.md)   
[Define ribbon enable rules](define-ribbon-enable-rules.md)   
[Define ribbon actions](define-ribbon-actions.md)


[!INCLUDE[footer-include](../../includes/footer-banner.md)]
