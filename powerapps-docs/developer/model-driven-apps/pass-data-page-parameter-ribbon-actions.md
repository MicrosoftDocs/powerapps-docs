---
title: "Pass data from a page as a parameter to Ribbon actions (model-driven apps)"
description: "Learn how to pass data from model-driven app pages as parameters to ribbon actions using the CrmParameter element."
author: clromano
ms.author: clromano
ms.date: 03/27/2026
ms.reviewer: jdaly
ms.topic: how-to
ms.subservice: mda-developer
search.audienceType: 
  - developer
contributors: 
  - JimDaly
  - caburk
---
# Pass data from a page as a parameter to ribbon actions

[!INCLUDE [cc-modern-commanding](../data-platform/includes/cc-modern-commanding.md)]

When you define an action in a ribbon, you often need to pass data from the page to either a JavaScript function or a URL. This article describes options for using the [\<CrmParameter\>](/previous-versions/dynamicscrm-2016/developers-guide/gg309332(v=crm.8)) element to retrieve these values.

## Form and grid context in ribbon actions

To pass execution context (*form context* or *grid context*) information to a JavaScript function for your ribbon actions, specify **PrimaryControl** for the form context, or **SelectedControl** for the grid context as the `<CrmParameter>` value in your ribbon definition. **SelectedControl** passes the grid context, for both subgrids and homepage grids. The passed **PrimaryControl** or **SelectedControl** value is used as an argument in your JavaScript function for *form context* or *grid context* respectively. 

[!INCLUDE[cc-terminology](../data-platform/includes/cc-terminology.md)]

For example, here's a sample ribbon definition where you pass the **PrimaryControl** parameter to the JavaScript function:

```xml
<CommandDefinition Id="SampleCommand">
  <EnableRules/>
  <DisplayRules/>
  <Actions>
    <JavaScriptFunction Library="$webresource:new_mySampleScript.js" FunctionName="mySampleFunction">
      <CrmParameter Value="PrimaryControl" />
    </JavaScriptFunction>
  </Actions>
</CommandDefinition>
```

Next, in the **new_mySampleScript.js** web resource file referenced in the preceding example, define your JavaScript function with the **primaryControl** variable as an argument. This argument provides the *form* context where the ribbon command is executed:

```JavaScript
function mySampleFunction(primaryControl) {
    var formContext = primaryControl;
    // Perform operations using the formContext object
}
```

You can also specify **CommandProperties** as `<CrmParameter>` value in your ribbon definition to pass details about the event from the ribbon control. Use this parameter to send contextual information to your JavaScript function where specific actions can be determined based on the context of the event.

> [!NOTE]
> Getting *form context* and *grid context* for JavaScript functions for ribbon actions is different from how you get these values in form scripting. For information about form scripting and how to get these contexts, see [Client API form context](clientapi/clientapi-form-context.md) and [Client API grid context](clientapi/clientapi-grid-context.md).

## Form values

By using a form ribbon, you can use the `data.entity`.[attributes](clientapi/reference/attributes.md) collection and the `ui`.[controls](clientapi/reference/controls.md) collection to get and set values for known columns. 

For example, the following sample code shows how to get the account name column on the account form, and then set a value in the websiteurl column based on the account name value:

```JavaScript
function mySampleFunction(primaryControl) {
    var formContext = primaryControl;    
    var accountName = formContext.getControl("name").getAttribute().getValue();    

    // Set the WebSiteURL column if account name contains "Contoso"
    if (accountName.toLowerCase().search("contoso") != -1) {
        formContext.getAttribute("websiteurl").setValue("https://www.contoso.com");
    }
    else {
        Xrm.Navigation.openAlertDialog({ text: "Account name does not contain 'Contoso'." });
    }
}
```

  
## Grid values

Most of the values for the `<CrmParameter>` element relate to working with data displayed in a grid or hierarchy chart. By using the `Value` parameter enumeration options, you can easily isolate items by:  
  
- **Selected items**  
  
    -   `SelectedControlSelectedItemCount`  
    -   `SelectedControlSelectedItemIds`  
    -   `SelectedControlSelectedItemReferences`  
  
- **All items**  
  
    -   `SelectedControlAllItemCount`  
    -   `SelectedControlAllItemIds`  
    -   `SelectedControlAllItemReferences`  
  
- **Unselected items**  
  
    -   `SelectedControlUnselectedItemCount`  
    -   `SelectedControlUnselectedItemIds`  
    -   `SelectedControlUnselectedItemReferences`  
  
  For each of these groupings, you can gather the number of items and the GUID identifier. If you pass the values to a URL, you can also retrieve `EntityReference` objects that contain all the information you need to uniquely identify the objects in the grid. These parameters apply whether the page viewed is the main grid (`HomepageGrid`) or a sub grid located in a form. When used together with the `SelectedEntityTypeName` parameter, you have all the information you must pass to another application.  
  
 
  
## Other context information

 In addition to data values, you can retrieve client context information by using [\<CrmParameter\>](/previous-versions/dynamicscrm-2016/developers-guide/gg309332(v=crm.8)).  You can use the following options as the value for the `CrmParameter` element: `OrgName`, `OrgLcid`, and `UserLcid`.
 
 For a `<Url>` action, you can also use the `PassParams` to include contextual information.  
  
 The `Value` options `PrimaryEntityTypeName` and `FirstPrimaryItemId` provide information for a table record. You can use `PrimaryItemIds` for a `HomepageGrid` ribbon to get a list of all the displayed items.
  
### See also

[Customize the ribbon](customize-commands-ribbon.md)   
[Passing parameters to a URL using the ribbon](pass-parameters-url-by-using-ribbon.md)    
[Define ribbon actions](define-ribbon-actions.md)   
[Define custom actions to modify the ribbon](define-custom-actions-modify-ribbon.md)   
[Client API form context](clientapi/clientapi-form-context.md)   
[Client API grid context](clientapi/clientapi-grid-context.md)
 


[!INCLUDE[footer-include](../../includes/footer-banner.md)]
