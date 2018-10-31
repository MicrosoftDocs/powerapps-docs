---
title: "Customize option sets (Common Data Service for Apps) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "Describes how to work with global and local option sets in code." # 115-145 characters including spaces. This abstract displays in the search result.
ms.custom: ""
ms.date: 10/31/2018
ms.reviewer: ""
ms.service: "powerapps"
ms.topic: "article"
author: "brandonsimons" # GitHub ID
ms.author: "jdaly" # MSFT alias of Microsoft employees only
manager: "ryjones" # MSFT alias of manager or PM counterpart
---
# Customize option sets

Typically, you use *global* option sets to set fields so that different fields can share the same set of options, which are maintained in one location. Unlike *local* options sets which are defined only for a specific attribute, you can reuse global option sets. You will also see them used in request parameters in a manner similar to an enumeration.  
  
When you define a global option set by using <xref:Microsoft.Xrm.Sdk.Messages.CreateOptionSetRequest>, 
we recommend that you let the system assign a value. You do this by passing a **null** value when you create the 
new `OptionMetadata` instance. When you define an option, it will contain an option value prefix specific to the 
context of the publisher set for the solution that the option set is created in. 
This prefix helps reduce the chance of creating duplicate option sets for a managed solution, 
and in any option sets that are defined in organizations where your managed solution is installed. For more information, 
see [Merge option set options](../understand-managed-solutions-merged.md#merge-option-set-options).  
 
## Messages Request Classes  

Use the following message request classes to work with global option sets

- <xref:Microsoft.Xrm.Sdk.Messages.CreateOptionSetRequest>
- <xref:Microsoft.Xrm.Sdk.Messages.DeleteOptionSetRequest>
- <xref:Microsoft.Xrm.Sdk.Messages.RetrieveAllOptionSetsRequest>
- <xref:Microsoft.Xrm.Sdk.Messages.RetrieveOptionSetRequest>  
- <xref:Microsoft.Xrm.Sdk.Messages.UpdateOptionSetRequest> 

Use the following message request classes with both global and local option sets.

- <xref:Microsoft.Xrm.Sdk.Messages.DeleteOptionValueRequest>
- <xref:Microsoft.Xrm.Sdk.Messages.InsertOptionValueRequest>
- <xref:Microsoft.Xrm.Sdk.Messages.InsertStatusValueRequest>
- <xref:Microsoft.Xrm.Sdk.Messages.OrderOptionRequest>
- <xref:Microsoft.Xrm.Sdk.Messages.UpdateOptionValueRequest>
- <xref:Microsoft.Xrm.Sdk.Messages.UpdateStateValueRequest>  

<a name="BKMK_RetrieveAGlobalOptionSet"></a>

## Retrieve a global option set  

 The following sample shows how to retrieve a global option set by name using the <xref:Microsoft.Xrm.Sdk.Messages.RetrieveOptionSetRequest> message:  
  

```csharp
// Use the RetrieveOptionSetRequest message to retrieve  
// a global option set by it's name.
RetrieveOptionSetRequest retrieveOptionSetRequest =
    new RetrieveOptionSetRequest
    {
        Name = _globalOptionSetName
    };

// Execute the request.
RetrieveOptionSetResponse retrieveOptionSetResponse =
    (RetrieveOptionSetResponse)svc.Execute(
    retrieveOptionSetRequest);

Console.WriteLine("Retrieved {0}.",
    retrieveOptionSetRequest.Name);

// Access the retrieved OptionSetMetadata.
OptionSetMetadata retrievedOptionSetMetadata =
    (OptionSetMetadata)retrieveOptionSetResponse.OptionSetMetadata;

// Get the current options list for the retrieved attribute.
OptionMetadata[] optionList =
    retrievedOptionSetMetadata.Options.ToArray();
```

  
<a name="BKMK_CreateGlobalOptionSet"></a>  
 
## Create a global option set
  
Use the <xref:Microsoft.Xrm.Sdk.Messages.CreateOptionSetRequest> message to create a new global option set. Set the 
 <xref:Microsoft.Xrm.Sdk.Metadata.OptionSetMetadataBase.IsGlobal> property to `true` to indicate that the option set is global. The following code example creates a global option set called “Example Option Set”:  
  
```csharp
// Define the request object and pass to the service.
CreateOptionSetRequest createOptionSetRequest = new CreateOptionSetRequest
{
    // Create a global option set (OptionSetMetadata).
    OptionSet = new OptionSetMetadata
    {
        Name = _globalOptionSetName,
        DisplayName = new Label("Example Option Set", _languageCode),
        IsGlobal = true,
        OptionSetType = OptionSetType.Picklist,
        Options = 
    {
        new OptionMetadata(new Label("Open", _languageCode), null),
        new OptionMetadata(new Label("Suspended", _languageCode), null),
        new OptionMetadata(new Label("Cancelled", _languageCode), null),
        new OptionMetadata(new Label("Closed", _languageCode), null)
    }
    }
};

// Execute the request.
CreateOptionSetResponse optionsResp =
    (CreateOptionSetResponse)svc.Execute(createOptionSetRequest);
```

  
<a name="BKMK_CreatePicklistWithGlobalOptionSet"></a>  
 
## Create a picklist that uses a global option set  

 The following sample shows how to create a picklist attribute that uses a global option set by using 
 <xref:Microsoft.Xrm.Sdk.Messages.CreateAttributeRequest>:  
  

```csharp
// Create a Picklist linked to the option set.
// Specify which entity will own the picklist, and create it.
CreateAttributeRequest createRequest = new CreateAttributeRequest
{
    EntityName = Contact.EntityLogicalName,
    Attribute = new PicklistAttributeMetadata
    {
        SchemaName = "sample_examplepicklist",
        LogicalName = "sample_examplepicklist",
        DisplayName = new Label("Example Picklist", _languageCode),
        RequiredLevel = new AttributeRequiredLevelManagedProperty(AttributeRequiredLevel.None),

        // In order to relate the picklist to the global option set, be sure
        // to specify the two attributes below appropriately.
        // Failing to do so will lead to errors.
        OptionSet = new OptionSetMetadata
        {
            IsGlobal = true,
            Name = _globalOptionSetName
        }
    }
};

svc.Execute(createRequest);
```

  
<a name="BKMK_UpdateGlobalOptionSet"></a>

## Update a global option set 

The following sample shows how to update the label for a global option set by using 
 <xref:Microsoft.Xrm.Sdk.Messages.UpdateOptionSetRequest>:  
  

```csharp
// Use UpdateOptionSetRequest to update the basic information of an option
// set. Updating option set values requires different messages (see below).
UpdateOptionSetRequest updateOptionSetRequest = new UpdateOptionSetRequest
{
    OptionSet = new OptionSetMetadata
    {
        DisplayName = new Label("Updated Option Set", _languageCode),
        Name = _globalOptionSetName,
        IsGlobal = true
    }
};

svc.Execute(updateOptionSetRequest);

//Publish the OptionSet
PublishXmlRequest pxReq1 = new PublishXmlRequest { ParameterXml = String.Format("<importexportxml><optionsets><optionset>{0}</optionset></optionsets></importexportxml>", _globalOptionSetName) };
svc.Execute(pxReq1);
```

  
<a name="BKMK_OrderingOptions"></a> 
  
## Ordering options  

The following sample shows how the options in a global option set can be ordered by using 
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
svc.Execute(orderOptionRequest);

//Publish the OptionSet
PublishXmlRequest pxReq4 = new PublishXmlRequest { 
ParameterXml = String.Format("<importexportxml><optionsets><optionset>{0}</optionset></optionsets></importexportxml>", _globalOptionSetName) 
};
svc.Execute(pxReq4);
```

  
<a name="BKMK_RetrieveAllGlobalOptionSets"></a>  
 
## Retrieve all global option sets  

The following sample shows how to retrieve all global option sets by using 
 <xref:Microsoft.Xrm.Sdk.Messages.RetrieveAllOptionSetsRequest>:  
  

```csharp
// Use RetrieveAllOptionSetsRequest to retrieve all global option sets.
// Create the request.
RetrieveAllOptionSetsRequest retrieveAllOptionSetsRequest =
    new RetrieveAllOptionSetsRequest();

// Execute the request
RetrieveAllOptionSetsResponse retrieveAllOptionSetsResponse =
    (RetrieveAllOptionSetsResponse)svc.Execute(
    retrieveAllOptionSetsRequest);

// Now you can use RetrieveAllOptionSetsResponse.OptionSetMetadata property to 
// work with all retrieved option sets.
if (retrieveAllOptionSetsResponse.OptionSetMetadata.Count() > 0)
{
    Console.WriteLine("All the global option sets retrieved as below:");
    int count = 1;
    foreach (OptionSetMetadataBase optionSetMetadata in
        retrieveAllOptionSetsResponse.OptionSetMetadata)
    {
        Console.WriteLine("{0} {1}", count++,
            (optionSetMetadata.DisplayName.LocalizedLabels.Count >0)? optionSetMetadata.DisplayName.LocalizedLabels[0].Label : String.Empty);
    }
}
```

  
<a name="BKMK_DeleteAGlobalOptionSet"></a>

## Delete a global option set

 The following sample shows how to check whether a global option set is being used by another solution component by using `RetrieveDependentComponents` message (<xref href="Microsoft.Dynamics.CRM.RetrieveDependentComponents?text=RetrieveDependentComponents Function" /> or <xref:Microsoft.Crm.Sdk.Messages.RetrieveDependentComponentsRequest>), and then how to delete it by using `DeleteOptionSet` message (For Organization Service, use <xref:Microsoft.Xrm.Sdk.Messages.DeleteOptionSetRequest>):  
  

```csharp
// Create the request to see which components have a dependency on the
// global option set.
RetrieveDependentComponentsRequest dependencyRequest =
    new RetrieveDependentComponentsRequest
    {
        ObjectId = _optionSetId,
        ComponentType = (int)componenttype.OptionSet
    };

RetrieveDependentComponentsResponse dependencyResponse =
    (RetrieveDependentComponentsResponse)svc.Execute(
    dependencyRequest);

// Here you would check the dependencyResponse.EntityCollection property
// and act as appropriate. However, we know there is exactly one 
// dependency so this example deals with it directly and deletes 
// the previously created attribute.
DeleteAttributeRequest deleteAttributeRequest =
    new DeleteAttributeRequest
{
    EntityLogicalName = Contact.EntityLogicalName,
    LogicalName = "sample_examplepicklist"
};

svc.Execute(deleteAttributeRequest);

Console.WriteLine("Referring attribute deleted.");
  
// Finally, delete the global option set. Attempting this before deleting
// the picklist above will result in an exception being thrown.
DeleteOptionSetRequest deleteRequest = new DeleteOptionSetRequest
{
    Name = _globalOptionSetName
};

svc.Execute(deleteRequest);
```

  
### See also

[Create and update option sets using the Web API](../webapi/create-update-optionsets.md)