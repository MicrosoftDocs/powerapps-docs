---
title: "Define ribbon enable rules (model-driven apps) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces"
description: "Learn about defining specific rules to control when the ribbon elements are enabled during configuration of ribbon elements." # 115-145 characters including spaces. This abstract displays in the search result."
keywords: ""
ms.date: 08/01/2018
ms.service:
  - "powerapps"
ms.custom:
  - ""
ms.topic: article
ms.assetid: 201f5db9-be65-7c3b-8202-822d78338bd6
author: JimDaly # GitHub ID
ms.author: jdaly # MSFT alias of Microsoft employees only
manager: shilpas # MSFT alias of manager or PM counterpart
ms.reviewer: 
---

# Define ribbon enable rules

<!-- https://docs.microsoft.com/en-us/dynamics365/customer-engagement/developer/customize-dev/define-ribbon-enable-rules -->

When configuring Ribbon elements you can define specific rules to control when the ribbon elements are enabled. The `<EnableRule>` element is used as follows:  

-   Use the `/RuleDefinitions/EnableRules/EnableRule` element to define rules controlling when the ribbon element should be enabled.  

-   Use the `/CommandDefinitions/CommandDefinition/EnableRules/EnableRule` element to associate specific enable rules to a command definition.  

## What does enabled mean?  
 With the command bar, commands that are disabled are hidden. With the ribbon, commands that are disabled are visible but do not respond to events.  

## Control when ribbon elements are enabled  
 Enable rules are intended to be re-used. By defining them with rule definitions, you can use the same enable rule for many command definitions. When more than one enable rule is defined for a command definition, all of the enable rules must evaluate as true for the ribbon element to be enabled.  

 All Enable rules provide an optional attribute to specify whether the default value of the rule is true or false and an optional `InvertResult` attribute to allow for returning a negative result when the item being tested returns true.  

 The `/RuleDefinitions/EnableRules/EnableRule` element supports the following types of rules:  

### Command Client Type Rule
 Uses the `<CommandClientTypeRule>` element. [!INCLUDE[ribbon_element_CommandClientTypeRule](../../includes/ribbon-element-commandclienttyperule.md)]  

 The `Type` values correspond to the following:  


|   Value   |                                                                               Presentation                                                                               |
|-----------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `Modern`  |                                       The command bar is presented using [!INCLUDE[pn_moca_full](../../includes/pn-moca-full.md)].                                       |
| `Refresh` |                                                      The command bar is presented using the updated user interface.                                                      |
| `Legacy`  | The ribbon is presented in forms for entities that were not updated or in a list view in [!INCLUDE[pn_crm_for_outlook_full](../../includes/pn-crm-for-outlook-full.md)]. |

### Crm Client Type Rule
Uses the  `<CrmClientTypeRule>` element to allow definition of rules depending on the type of client used. Type options are as follows:  

-   `Web`  

-   `Outlook`  

### Crm Offline Access State Rule
 Uses the `<CrmOfflineAccessStateRule>` element. Use this criteria to enable a ribbon element based on whether [!INCLUDE[pn_crm_outlook_offline_access](../../includes/pn-crm-outlook-offline-access.md)] is currently offline.  

### Crm Outlook Client Type Rule
 Uses the `<CrmOutlookClientTypeRule>` element. Use this rule if you want to only display a button for a specific type of [!INCLUDE[pn_crm_for_outlook_full](../../includes/pn-crm-for-outlook-full.md)]. Type options are as follows:  

-   `CrmForOutlook`  

-   `CrmForOutlookOfflineAccess`  

### Custom Rule
 Uses the `<CustomRule>` element. Use this kind of rule to call a function in a JavaScript Library that returns a Boolean value.  

> [!NOTE]
>  Custom rules that do not return a value quickly can affect the performance of the ribbon. If you have to perform logic that might take some time to complete, use the following strategy to make your custom rule asynchronous:  
>   
> 1.  Define a rule that checks for a custom object. You might check for an object such as `Window.ContosoCustomObject.RuleIsTrue` that you just attach to the Window.  
> 2.  If that object exists, return it.  
> 3.  If that object does not exist, define the object and set the value as false.  
> 4.  Before you return a value, use [settimeout](https://msdn.microsoft.com/library/ms536753\(VS.85\).aspx) <!-- TODO not sure about this link--> to execute an asynchronous callback function to re-set the object. Then return false.  
> 5.  After the callback function has performed the operations that are required to determine the correct result, it sets the value of the object and uses the `refreshRibbon` method to refresh the ribbon.  
> 6.  When the ribbon is refreshed, it detects the object together with the accurate value set and the rule is evaluated.  

### Entity Rule
 Uses the `<EntityRule>` element. Entity rules allow for evaluation of the current entity. This is useful when you define custom actions that apply to the Entity Template instead of for specific entities. For example, you may want to add a ribbon element to all entities except for several specific entities. It is easier to define the custom action for the Entity Template that applies to all entities and then use an Entity Rule to filter out those that should be excluded.  

 The entity rule also includes an optional Context attribute to specify whether the entity is being displayed in the Form or a list (HomePageGrid). The optional `AppliesTo` attribute can be set to `PrimaryEntity` or `SelectedEntity` to distinguish whether the entity is being displayed in a subgrid.  

### Form State Rule
 Uses the `<FormStateRule>` element. Use the `FormState` rule to determine the current type of form that is displaying a record. State options are as follows:  

-   `Create`  

-   `Existing`  

-   `ReadOnly`  

-   `Disabled`  

-   `BulkEdit`  

### Or Rule
 Uses the `<OrRule>` element. The `OrRule` lets you override the default AND comparison for multiple enable rule types. Use the `OrRule` element to define several possible valid combinations to check.

### Outlook Item Tracking Rule
 Uses the `<OutlookItemTrackingRule>` element. Use the `TrackedInCrm` attribute for this element to determine whether the record is being tracked in [!INCLUDE[pn_dynamics_crm](../../includes/pn-dynamics-crm.md)] Common Data Service for Apps.  

### Outlook Version Rule
 Uses the `<OutlookVersionRule>` element. Use this to enable a ribbon element for a specific version of [!INCLUDE[pn_MS_Outlook_Full](../../includes/pn-ms-outlook-full.md)] as follows:  

-   `2003`  

-   `2007`  

-   `2010`  

### Page Rule
 Uses the `<PageRule>` element. This type of rule checks the URL of the page being displayed. It returns true if the `Address` matches.  

### Record Privilege Rule
 Uses the `<RecordPrivilegeRule>` element. Use this rule to determine whether the current user has privileges on a specific record. These privileges differ from an Entity privilege because they can include privileges gained by another user sharing the record with the current user.  

### Selection Count Rule
 Uses the `<SelectionCountRule>` element. Use this kind of rule with a ribbon displayed for a list to enable a button when specific maximum and minimum numbers of records in the grid are selected. For example, if your button merges records, you should make sure at least two records are selected before enabling the ribbon control.  

### Sku Rule
 Uses the `<SkuRule>` element. Use this kind of rule to enable a ribbon element for a specific SKU version of [!INCLUDE[pn_dynamics_crm](../../includes/pn-dynamics-crm.md)] as follows:  

-   `OnPremise`  

-   `Online`  

-   `Spla`  

### Value Rule
Uses the `<ValueRule>` element. Use this rule to check the value of a specific field in the record being displayed in the form. You must specify the `Field` and the `Value` to check.  

### See also  
 [Customize commands and the ribbon](customize-commands-ribbon.md)   
 [Define Ribbon Commands](define-ribbon-commands.md)   
 [Define Ribbon Display Rules](define-ribbon-display-rules.md)