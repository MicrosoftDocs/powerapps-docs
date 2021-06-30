---
title: "Insert, update, delete, and order global choices (Microsoft Dataverse) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "Code samples to show how to insert, update, delete, and order global choices." # 115-145 characters including spaces. This abstract displays in the search result.
ms.custom: ""
ms.date: 06/10/2021
ms.reviewer: "pehecke"
ms.service: powerapps
ms.topic: "article"
author: "JimDaly" # GitHub ID
ms.author: "jdaly" # MSFT alias of Microsoft employees only
manager: "ryjones" # MSFT alias of manager or PM counterpart
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---

# Insert, update, delete, and order global choices

[!INCLUDE[cc-terminology](../includes/cc-terminology.md)]

These code samples show you how to insert, update, delete, and order global choices.  
  
<a name="BKMK_InsertNewOption"></a>

## Insert a new choice

 The following code sample shows how to add a new choice to global choices by using
 <xref:Microsoft.Xrm.Sdk.Messages.InsertOptionValueRequest>:  
  
```csharp
// Use InsertOptionValueRequest to insert a new option into a 
// global option set.
InsertOptionValueRequest insertOptionValueRequest =
    new InsertOptionValueRequest
    {
        OptionSetName = _globalOptionSetName,
        Label = new Label("New Picklist Label", _languageCode)
    };

// Execute the request and store the newly inserted option value 
// for cleanup, used in the later part of this sample.
_insertedOptionValue = ((InsertOptionValueResponse)_serviceProxy.Execute(
    insertOptionValueRequest)).NewOptionValue;

//Publish the OptionSet
PublishXmlRequest pxReq2 = new PublishXmlRequest { ParameterXml = String.Format("<importexportxml><optionsets><optionset>{0}</optionset></optionsets></importexportxml>", _globalOptionSetName) };
_serviceProxy.Execute(pxReq2);
```
  
<a name="BKMK_UpdateAnOption"></a>

## Update a choice

 The following code sample shows how to update a choice in global choices by using
 <xref:Microsoft.Xrm.Sdk.Messages.UpdateOptionValueRequest>:  
  
```csharp
// In order to change labels on option set values (or delete) option set
// values, you must use UpdateOptionValueRequest 
// (or DeleteOptionValueRequest).
UpdateOptionValueRequest updateOptionValueRequest =
    new UpdateOptionValueRequest
    {
        OptionSetName = _globalOptionSetName,
        // Update the second option value.
        Value = optionList[1].Value.Value,
        Label = new Label("Updated Option 1", _languageCode)
    };

_serviceProxy.Execute(updateOptionValueRequest);

//Publish the OptionSet
PublishXmlRequest pxReq3 = new PublishXmlRequest { ParameterXml = String.Format("<importexportxml><optionsets><optionset>{0}</optionset></optionsets></importexportxml>", _globalOptionSetName) };
_serviceProxy.Execute(pxReq3);
```
  
<a name="BKMK_DeleteAnOption"></a>

## Delete a choice

 The following sample shows how to delete a choice in global choies by using 
 <xref:Microsoft.Xrm.Sdk.Messages.DeleteOptionValueRequest>:  
  
```csharp
// Use the DeleteOptionValueRequest message 
// to remove the newly inserted label.
DeleteOptionValueRequest deleteOptionValueRequest =
    new DeleteOptionValueRequest
{
    OptionSetName = _globalOptionSetName,
    Value = _insertedOptionValue
};

// Execute the request.
_serviceProxy.Execute(deleteOptionValueRequest);
```  
  
<a name="BKMK_OrderOptions"></a>

## Order of choices
  
 The following sample shows how to set the order of choices in global choices by using
 <xref:Microsoft.Xrm.Sdk.Messages.OrderOptionRequest>:  
  
```csharp
// Change the order of the original option's list.
// Use the OrderBy (OrderByDescending) linq function to sort options in  
// ascending (descending) order according to label text.
// For ascending order use this:
var updateOptionList =
    optionList.OrderBy(x => x.Label.LocalizedLabels[0].Label).ToList();

// For descending order use this:
// var updateOptionList =
//      optionList.OrderByDescending(
//      x => x.Label.LocalizedLabels[0].Label).ToList();

// Create the request.
OrderOptionRequest orderOptionRequest = new OrderOptionRequest
{
    // Set the properties for the request.
    OptionSetName = _globalOptionSetName,
    // Set the changed order using Select linq function 
    // to get only values in an array from the changed option list.
    Values = updateOptionList.Select(x => x.Value.Value).ToArray()
};

// Execute the request
_serviceProxy.Execute(orderOptionRequest);

//Publish the OptionSet
PublishXmlRequest pxReq4 = new PublishXmlRequest { ParameterXml = String.Format("<importexportxml><optionsets><optionset>{0}</optionset></optionsets></importexportxml>", _globalOptionSetName) };
_serviceProxy.Execute(pxReq4);
```

[!INCLUDE[footer-include](../../../includes/footer-banner.md)]