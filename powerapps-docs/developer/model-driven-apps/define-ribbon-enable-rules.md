---
title: "Define ribbon enable rules (model-driven apps) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces"
description: "Learn about defining specific rules to control when the ribbon elements are enabled during configuration of ribbon elements." # 115-145 characters including spaces. This abstract displays in the search result."
keywords: ""
ms.date: 04/15/2021
ms.service: powerapps
ms.topic: article
ms.assetid: 201f5db9-be65-7c3b-8202-822d78338bd6
author: Nkrb 
ms.author: nabuthuk
manager: kvivek 
ms.reviewer: kvivek 
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---

# Define ribbon enable rules

When configuring ribbon elements, you can define specific rules to control when the ribbon elements are enabled. The `<EnableRule>` element is used as follows:  

- Use the `/RuleDefinitions/EnableRules/EnableRule` element to define rules controlling when the ribbon element should be enabled.  

- Use the `/CommandDefinitions/CommandDefinition/EnableRules/EnableRule` element to associate specific enable rules to a command definition.  

## What does enabled mean?  

With the command bar, commands that are disabled are hidden. With the ribbon, commands that are disabled are visible but do not respond to events.  

## Control when ribbon elements are enabled  

Enable rules are intended to be reused. By defining them with rule definitions, you can use the same enable rule for many command definitions. When more than one enable rule is defined for a command definition, all of the enable rules must evaluate as true for the ribbon element to be enabled.  

 All Enable rules provide an optional parameter to specify whether the default value of the rule is true or false and an optional `InvertResult` parameter to allow for returning a negative result when the item being tested returns true.  

 The `/RuleDefinitions/EnableRules/EnableRule` element supports the following types of rules:  

[!INCLUDE[cc-terminology](../data-platform/includes/cc-terminology.md)]

### Command Client Type Rule
 Uses the `<CommandClientTypeRule>` element. [!INCLUDE[ribbon_element_CommandClientTypeRule](../../includes/ribbon-element-commandclienttyperule.md)]  

 The `Type` values correspond to the following:  


|   Value   | Presentation               |
|-----------|------------------------------------------------|
| `Modern`  |   The command bar is presented using [!INCLUDE[pn_moca_full](../../includes/pn-moca-full.md)].        |
| `Refresh` |   The command bar is presented using the updated user interface.                                                      |
| `Legacy`  | The ribbon is presented in forms for tables that were not updated or in a list view in [!INCLUDE[pn_crm_for_outlook_full](../../includes/pn-crm-for-outlook-full.md)]. |

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

 Uses the `<CustomRule>` element. Use this kind of rule to call a function in a [Script (JScript) web resource](./script-jscript-web-resources.md) that returns a Promise (Unified Interface) or boolean (Unified Interface and web client).

```JavaScript
function EnableRule()
{
    const value = Xrm.Page.getAttribute("column1").getValue();
    return value === "Active";
}
```

> [!NOTE]
> Custom rules that do not return a value quickly can affect the performance of the ribbon. If you have to perform logic that might take some time to complete (for example, a network request), use the following strategy to make your custom rule asynchronous.

 Unified Interface rules support returning a Promise rather than boolean for asynchronous rule evaluation. If the promise does not resolve within 10 seconds, the rule will resolve with a false value.

 > [!NOTE]
 >  Promises-based rules will only work on Unified Interface, so they cannot be used if classic Web Client is still being used.

 ```JavaScript
// Old synchronous style
/*
function EnableRule() {
    const request = new XMLHttpRequest();
    request.open('GET', '/bar/foo', false);
    request.send(null);
    return request.status === 200 && request.responseText === "true";
}
*/

// New asynchronous style
function EnableRule() {
    const request = new XMLHttpRequest();
    request.open('GET', '/bar/foo');

    return new Promise(function(resolve, reject) {
        request.onload = function (e) {
            if (request.readyState === 4) {
                if (request.status === 200) {
                    resolve(request.responseText === "true");
                } else {
                    reject(request.statusText);
                }
            }
        };
        request.onerror = function (e) {
            reject(request.statusText);
        };

        request.send(null);
    });
}
```


### Entity Rule

 Uses the `<EntityRule>` element. `EntityRule` allow for evaluation of the current table. This is useful when you define custom actions that apply to the table template instead of for specific tables. For example, you may want to add a ribbon element to all tables except for several specific tables. It is easier to define the custom action for the table template that applies to all tables and then use an `EntityRule` to filter out those that should be excluded.  

 The `EntityRule` also includes an optional context parameter to specify whether the table is being displayed in the form or a list (HomePageGrid). The optional `AppliesTo` parameter can be set to `PrimaryEntity` or `SelectedEntity` to distinguish whether the table is being displayed in a subgrid.  

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
 Uses the `<OutlookItemTrackingRule>` element. Use the `TrackedInCrm` parameter for this element to determine whether the record is being tracked in Power Apps.  

### Outlook Version Rule
 Uses the `<OutlookVersionRule>` element. Use this to enable a ribbon element for a specific version of [!INCLUDE[pn_MS_Outlook_Full](../../includes/pn-ms-outlook-full.md)] as follows:  

-   `2003`  

-   `2007`  

-   `2010`  

### Page Rule
 Uses the `<PageRule>` element. This type of rule checks the URL of the page being displayed. It returns true if the `Address` matches.  

### Record Privilege Rule
 Uses the `<RecordPrivilegeRule>` element. Use this rule to determine whether the current user has privileges on a specific record. These privileges differ from a table privilege because they can include privileges gained by another user sharing the record with the current user.  

### Selection Count Rule
 Uses the `<SelectionCountRule>` element. Use this kind of rule with a ribbon displayed for a list to enable a button when specific maximum and minimum numbers of records in the grid are selected. For example, if your button merges records, you should make sure at least two records are selected before enabling the ribbon control.  

### Value Rule
Uses the `<ValueRule>` element. Use this rule to check the value of a specific column in the record being displayed in the form. You must specify the `Field` and the `Value` to check.

### Show On Quick Action Rule

Uses the `<EnableRule>` element. Use this rule to make the command appear only as quick action.

```xml
<CommandDefinition Id="new.contact.Command.Call">
  <EnableRules>
    <EnableRule Id="Mscrm.SelectionCountExactlyOne" />
    <EnableRule Id="Mscrm.ShowOnQuickAction" />
  </EnableRules>
  <DisplayRules />
  <Actions>
    <JavaScriptFunction FunctionName=" simplealert" />
  </Actions>
</CommandDefinition>
```

### Show On Grid and Quick Action rule

Uses the `<EnableRule>` element. Use this rule to make the command appear on the homepage grid and quick action.

```xml
<CommandDefinition Id="new.contact.Command.Call">
  <EnableRules>
    <EnableRule Id="Mscrm.SelectionCountExactlyOne" />
    <EnableRule Id="Mscrm.ShowOnGridAndQuickAction" />
  </EnableRules>
  <DisplayRules />
  <Actions>
    <JavaScriptFunction FunctionName=" simplealert" />
  </Actions>
</CommandDefinition>
```
### Show On Grid Rule

Uses the `<EnableRule>` element. Use this rule to make the quick action command appear on the homepage grid only. In other words, you can use this command to hide an existing quick action.

```xml
<CommandDefinition Id="new.contact.Command.Call">
  <EnableRules>
    <EnableRule Id="Mscrm.SelectionCountExactlyOne" />
    <EnableRule Id="Mscrm.ShowOnGrid" />
  </EnableRules>
  <DisplayRules />
  <Actions>
    <JavaScriptFunction FunctionName=" simplealert" />
  </Actions>
</CommandDefinition>
```

### See also  
 [Customize commands and the ribbon](customize-commands-ribbon.md)   
 [Define ribbon commands](define-ribbon-commands.md)   
 [Define ribbon display rules](define-ribbon-display-rules.md)


[!INCLUDE[footer-include](../../includes/footer-banner.md)]