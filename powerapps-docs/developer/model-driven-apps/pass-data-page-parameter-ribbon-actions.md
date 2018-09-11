---
title: "Pass data from a page as a parameter to Ribbon actions (model-driven apps) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "The topic describes options for using the <CrmParameter> element to retrieve these values. " # 115-145 characters including spaces. This abstract displays in the search result.
ms.custom: ""
ms.date: 08/01/2018
ms.reviewer: ""
ms.service: "powerapps"
ms.topic: "article"
author: "KumarVivek" # GitHub ID
ms.author: "kvivek" # MSFT alias of Microsoft employees only
manager: "shilpas" # MSFT alias of manager or PM counterpart
---
# Pass data from a page as a parameter to Ribbon Actions

<!-- https://docs.microsoft.com/en-us/dynamics365/customer-engagement/developer/customize-dev/pass-dynamics-365-data-page-parameter-ribbon-actions -->

When you define an action in a ribbon, you frequently have to pass data from the page to either a JavaScript function or a URL. This topic describes options for using the [\<CrmParameter\>](https://msdn.microsoft.com/library/gg309332.aspx) element to retrieve these values.

## Form and grid context in ribbon actions

To pass in the execution context (*form context* or *grid context*) information to JavaScript function for your ribbon actions, specify **PrimaryControl** as the `<CrmParameter>` value in your ribbon definition. The passed in PrimaryControl value is used as an argument in your JavaScript function that provides the *form context* or *grid context* depending on where the ribbon command is executed. 

For example, here is a sample ribbon definition where we pass in the **PrimaryControl** parameter to the JavaScript function:

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

Next, in the **new_mySampleScript.js** web resource file referenced in the example above, define your JavaScript function with the **primaryControl** variable as an argument. This argument provides the *form* or *grid* context depending on where the ribbon command is executed:

```JavaScript
function mySampleFunction(primaryControl) {
    var formContext = primaryControl;
    // Perform operations using the formContext object
}
```

You can also specify **CommandProperties** as `<CrmParameter>` value in your ribbon definition to pass details about the event from the ribbon control. You can use this to send contextual information to your JavaScript function where specific actions can be determined based on the context of the event.

> [!NOTE]
> Getting *form context* and *grid context* for JavaScript functions for ribbon actions is different from how you get these values in form scripting. For information about form scripting and how to get these contexts, see [Client API form context](clientapi/clientapi-form-context.md) and [Client API grid context](clientapi/clientapi-grid-context.md).

## Form values

With a form ribbon, you can use the `data.entity`.[attributes](clientapi/reference/attributes.md) collection and the `ui`.[controls](clientapi/reference/controls.md) collection to retrieve and set values for known fields. 

For example, the following sample code shows how to retrieve the account name field on the account form, and then set a value in the websiteurl field based on the account name value:

```JavaScript
function mySampleFunction(primaryControl) {
    var formContext = primaryControl;    
    var accountName = formContext.getControl("name").getAttribute().getValue();    

    // Set the WebSiteURL field if account name contains "Contoso"
    if (accountName.toLowerCase().search("contoso") != -1) {
        formContext.getAttribute("websiteurl").setValue("http://www.contoso.com");
    }
    else {
        Xrm.Navigation.openAlertDialog({ text: "Account name does not contain 'Contoso'." });
    }
}
```

  
## Grid values  
 The majority of the values available for the `<CrmParameter>` element are related to working with data displayed in a grid or hierarchy chart. By using the `Value` attribute enumeration options, you can easily isolate items by:  
  
- **Selected items**  
  
    -   SelectedControlSelectedItemCount  
  
    -   SelectedControlSelectedItemIds  
  
    -   SelectedControlSelectedItemReferences  
  
- **All items**  
  
    -   SelectedControlAllItemCount  
  
    -   SelectedControlAllItemIds  
  
    -   SelectedControlAllItemReferences  
  
- **Unselected items**  
  
    -   SelectedControlUnselectedItemCount  
  
    -   SelectedControlUnselectedItemIds  
  
    -   SelectedControlUnselectedItemReferences  
  
  For each of these groupings, you can gather the number of items and the GUID identifier. If you are passing the values to a URL, you can also retrieve `EntityReference` objects that contain all the information that you need to uniquely identify the objects in the grid. These parameters apply whether the page viewed is the main grid (`HomepageGrid`) or a sub grid located in a form. When used together with the `SelectedEntityTypeName` parameter, you have all the information that you must have to pass to another application.  
  
 
  
## Other context information  
 In addition to data values, you can retrieve client context information by using [\<CrmParameter\>](https://msdn.microsoft.com/library/gg309332.aspx).  You can use the following options as the value for the `CrmParameter` element: `OrgName`, `OrgLcid`, and `UserLcid`.
 
 For a `<Url>` action, you can also use the `PassParams` attribute to include contextual information.  
  
 The `Value` options `PrimaryEntityTypeName` and `FirstPrimaryItemId` provide information for an entity record. You can use `PrimaryItemIds` for a `HomepageGrid` ribbon to get a list of all the displayed items.
  
### See also  
 [Customize the Ribbon](customize-commands-ribbon.md)   
 [Passing Parameters to a URL using the Ribbon](pass-parameters-url-by-using-ribbon.md)    
 [Define Ribbon Actions](define-ribbon-actions.md)   
 [Define Custom Actions to modify the Ribbon](define-custom-actions-modify-ribbon.md)<br>
 [Client API form context](clientapi/clientapi-form-context.md)<br>
 [Client API grid context](clientapi/clientapi-grid-context.md)<br>
 
