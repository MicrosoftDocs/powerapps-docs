---
title: "addCustomFilter (Client API reference) in model-driven apps| MicrosoftDocs"
description: Adds filters to the results displayed in the lookup. Each filter is combined with any previously added filter.
ms.date: 04/15/2021
ms.service: powerapps
ms.topic: "reference"
applies_to: "Dynamics 365 (online)"
ms.assetid: e359b-c4d9-48ac-a57b-367c2e6168c5
author: "Nkrb"
ms.author: "nabuthuk"
manager: "kvivek"
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---
# addCustomFilter (Client API reference)

Adds filters to the results displayed in the lookup. Each filter will be combined with any previously added filters as an `AND` condition.

## Control types supported

Lookup

## Syntax

`formContext.getControl(arg).addCustomFilter(filter, entityLogicaName)`

## Parameters

- **filter**: String. The fetchXml filter element to apply. For example:

    ```xml
    <filter type="and">
      <condition attribute="address1_city" operator="eq" value="Redmond" />
    </filter>
    ```

- **entityLogicalName**: (Optional) String. If this is set, the filter only applies to that table type. Otherwise, it applies to all types of tables returned.

[!INCLUDE[cc-terminology](../../../../data-platform/includes/cc-terminology.md)]

## Remarks

This method can only be used in a function in an event handler for the [Lookup Control PreSearch Event](../events/presearch.md).

## Example

The following code sample is for the Opportunity form **Account** (parentaccountid) lookup. When the **Sdk.setParentAccountIdFilter** function is set in the form **Onload** event handler, the **Sdk.filterCustomAccounts** function is added to the **PreSearch** event for that lookup. Remember to select the option to pass in the execution context when setting the function in the form **Onload** event handler. The result is that only accounts with the **Category** (accountcategorycode) value of **Preferred Customer** (1) will be returned.

```JavaScript
// A namespace defined for SDK sample code
// You should define a unique namespace for your libraries
var Sdk = window.Sdk || {};

// set 'Sdk.setParentAccountIdFilter' in the Opportunity form onload event handler
Sdk.setParentAccountIdFilter = function (executionContext) {

    // get the form context
    formContext = executionContext.getFormContext();
    formContext.getControl("parentaccountid").addPreSearch(Sdk.filterCustomerAccounts);
}

Sdk.filterCustomerAccounts = function () {

    // Only show accounts with the type 'Preferred Customer'
    var customerAccountFilter = "<filter type='and'><condition attribute='accountcategorycode' operator='eq' value='1'/></filter>";
    formContext.getControl("parentaccountid").addCustomFilter(customerAccountFilter, "account");
}
```
[addPreSearch](addPreSearch.md)

[formContext](../../clientapi-form-context.md)

[!INCLUDE[footer-include](../../../../../includes/footer-banner.md)]