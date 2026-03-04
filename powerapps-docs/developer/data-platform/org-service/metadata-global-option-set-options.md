---
title: "Insert, update, delete, and order global choices (Microsoft Dataverse) | Microsoft Docs"
description: "Code samples to show how to insert, update, delete, and order global choices." 
ms.date: 03/04/2026
author: MsSQLGirl
ms.author: jukoesma
ms.reviewer: jdaly
ms.topic: "article"
search.audienceType: 
  - developer
---

# Insert, update, delete, and order global choices

[!INCLUDE[cc-terminology](../includes/cc-terminology.md)]

These code samples show you how to insert, update, delete, and order global choices.  
  
<a name="BKMK_InsertNewOption"></a>

## Insert a new choice

 The following static `InsertOptionValue` method shows how to add a new choice to global choices by using
 <xref:Microsoft.Xrm.Sdk.Messages.InsertOptionValueRequest>:  
  
```csharp
static int InsertOptionValue(
    IOrganizationService service,
    string globalOptionSetName,
    Label value)
{
    var request = new InsertOptionValueRequest
    {
        OptionSetName = globalOptionSetName,
        Label = value
    };

    int newOptionValue = ((InsertOptionValueResponse)service.Execute(request)).NewOptionValue;

    // Publish the OptionSet
    service.Execute(new PublishXmlRequest
    {
        ParameterXml = string.Format(
            "<importexportxml><optionsets><optionset>{0}</optionset></optionsets></importexportxml>",
            globalOptionSetName)
    });

    return newOptionValue;
}
```
  
<a name="BKMK_UpdateAnOption"></a>

## Update a choice

 The following static `UpdateOptionValue` method shows how to update a choice in global choices by using
 <xref:Microsoft.Xrm.Sdk.Messages.UpdateOptionValueRequest>:

```csharp
static void UpdateOptionValue(
    IOrganizationService service,
    string globalOptionSetName,
    int value,
    Label label)
{
    service.Execute(new UpdateOptionValueRequest
    {
        OptionSetName = globalOptionSetName,
        Value = value,
        Label = label
    });

    // Publish the OptionSet
    service.Execute(new PublishXmlRequest
    {
        ParameterXml = string.Format(
            "<importexportxml><optionsets><optionset>{0}</optionset></optionsets></importexportxml>",
            globalOptionSetName)
    });
}
```
  
<a name="BKMK_DeleteAnOption"></a>

## Delete a choice

 The following static `DeleteOptionValue` method shows how to delete a choice in global choices by using
 <xref:Microsoft.Xrm.Sdk.Messages.DeleteOptionValueRequest>:

```csharp
static void DeleteOptionValue(
    IOrganizationService service,
    string globalOptionSetName,
    int value)
{
    service.Execute(new DeleteOptionValueRequest
    {
        OptionSetName = globalOptionSetName,
        Value = value
    });
}
```  
  
<a name="BKMK_OrderOptions"></a>

## Order of choices
  
 The following static `OrderOptions` method shows how to set the order of choices in global choices by using
 <xref:Microsoft.Xrm.Sdk.Messages.OrderOptionRequest>:

```csharp
static void OrderOptions(
    IOrganizationService service,
    string globalOptionSetName,
    IEnumerable<OptionMetadata> updateOptionList)
{
    service.Execute(new OrderOptionRequest
    {
        OptionSetName = globalOptionSetName,
        // Use Select linq function to get only values in an array from the option list.
        Values = updateOptionList.Select(x => x.Value.Value).ToArray()
    });

    // Publish the OptionSet
    service.Execute(new PublishXmlRequest
    {
        ParameterXml = string.Format(
            "<importexportxml><optionsets><optionset>{0}</optionset></optionsets></importexportxml>",
            globalOptionSetName)
    });
}
```

The following example shows using the static `OrderOptions` method to order a set of options based on the text of the label.

```csharp
// Change the order of the original option's list.
// Use the OrderBy (OrderByDescending) linq function to sort options in  
// ascending order according to label text.
// For ascending order use this:
var updateOptionList =
    optionList.OrderBy(x => x.Label.LocalizedLabels[0].Label).ToList();

// For descending order use this:
// var updateOptionList =
//      optionList.OrderByDescending(
//      x => x.Label.LocalizedLabels[0].Label).ToList();
OrderOptions(service, _globalOptionSetName, updateOptionList)

``

[!INCLUDE[footer-include](../../../includes/footer-banner.md)]
