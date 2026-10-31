---
title: "addCustomFilter (Client API Reference) in Model-Driven Apps"
description: Learn how to use addCustomFilter in model-driven apps to filter lookup results with fetchXml. Each filter combines with previous filters as an AND condition.
author: MitiJ
ms.author: mijosh
ms.date: 10/30/2026
ms.reviewer: jdaly
ms.topic: reference
ai-usage: ai-assisted
applies_to: "Dynamics 365 (online)"
search.audienceType: 
  - developer
contributors:
  - JimDaly
---
# addCustomFilter (Client API reference)

The `addCustomFilter` method adds filters to the results displayed in a lookup control in model-driven apps. Each filter is combined with any previously added filters as an `AND` condition.

## Control types supported

Lookup

## Syntax

`formContext.getControl(arg).addCustomFilter(filter, entityLogicalName)`

## Parameters

| Name | Type | Description |
| --- | --- | --- |
| `filter` | String | The FetchXML filter element to apply. |
| `entityLogicalName` | String | Optional. If you set this parameter, the filter only applies to that table type. Otherwise, it applies to all types of tables returned. |

For example, use the following XML for the `filter` parameter:

```xml
<filter type="and">
  <condition attribute="address1_city" operator="eq" value="Redmond" />
</filter>
```

## Remarks

Use this method in a function in an event handler for the [Lookup Control PreSearch Event](../events/presearch.md).

## Example

The following code sample is for the [Opportunity](/dynamics365/developer/reference/entities/opportunity) form [**Account**](/dynamics365/developer/reference/entities/opportunity#BKMK_ParentAccountId) (`parentaccountid`) lookup. When you set the `Sdk.setParentAccountIdFilter` function in the form `Onload` event handler, add the `Sdk.filterCustomerAccounts` function to the `PreSearch` event for that lookup. Remember to select the option to pass in the execution context when setting the function in the form `Onload` event handler. The result is that only accounts with the [**Category**](../../../../data-platform/reference/entities/account.md#BKMK_AccountCategoryCode) (`accountcategorycode`) value of **Preferred Customer** (1) are returned.

```JavaScript
// A namespace defined for SDK sample code
// You should define a unique namespace for your libraries
const Sdk = (window.Sdk ??= {});

// set 'Sdk.setParentAccountIdFilter' in the Opportunity form onload event handler
Sdk.setParentAccountIdFilter = (executionContext) => {
  const formContext = executionContext.getFormContext();
    formContext.getControl("parentaccountid").addPreSearch(Sdk.filterCustomerAccounts);
};

Sdk.filterCustomerAccounts = (executionContext) => {
  const control = executionContext.getEventSource();
  const customerAccountFilter = `
    <filter type="and">
      <condition attribute="accountcategorycode" operator="eq" value="1" />
    </filter>`;
  control.addCustomFilter(customerAccountFilter, "account");
};
```

### Related articles

[addPreSearch](addPreSearch.md)   
[formContext](../../clientapi-form-context.md)

[!INCLUDE[footer-include](../../../../../includes/footer-banner.md)]
