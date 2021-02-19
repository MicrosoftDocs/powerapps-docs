---
title: "Work with attribute metadata (Microsoft Dataverse) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "Describes common operations on attribute metadata." # 115-145 characters including spaces. This abstract displays in the search result.
ms.custom: ""
ms.date: 04/05/2019
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
# Work with attribute metadata

[!INCLUDE[cc-data-platform-banner](../../../includes/cc-data-platform-banner.md)]

This topic describes a number of common operations that can be applied to attribute metadata.

<a name="BKMK_CreateAttributes"></a>   
## Create attributes

 You create attributes by defining one of the <xref:Microsoft.Xrm.Sdk.Metadata.AttributeMetadata> types and then passing it to the <xref:Microsoft.Xrm.Sdk.Messages.CreateAttributeRequest> message.  
  
 The following sample defines the <xref:Microsoft.Xrm.Sdk.Metadata.AttributeMetadata> for a number of different types of attributes and adds them to a `List<AttributeMetadata>`. At the end of the code the attribute definitions are passed to an instance of the <xref:Microsoft.Xrm.Sdk.Messages.CreateAttributeRequest> class and the attribute is created using the <xref:Microsoft.Xrm.Sdk.IOrganizationService>.<xref:Microsoft.Xrm.Sdk.IOrganizationService.Execute*> method.  
  
 The following sample code assumes that the current customization prefix is ‘new’ because that is the default customization prefix for the organization solution publisher. You should use the customization prefix for the solution publisher that makes sense for your solution context.  

```csharp
// Create storage for new attributes being created
addedAttributes = new List<AttributeMetadata>();

// Create a boolean attribute
BooleanAttributeMetadata boolAttribute = new BooleanAttributeMetadata
{
    // Set base properties
    SchemaName = "new_Boolean",
    LogicalName = "new_boolean",
    DisplayName = new Label("Sample Boolean", _languageCode),
    RequiredLevel = new AttributeRequiredLevelManagedProperty(AttributeRequiredLevel.None),
    Description = new Label("Boolean Attribute", _languageCode),
    // Set extended properties
    OptionSet = new BooleanOptionSetMetadata(
        new OptionMetadata(new Label("True", _languageCode), 1),
        new OptionMetadata(new Label("False", _languageCode), 0)
        )
};

// Add to list
addedAttributes.Add(boolAttribute);

// Create a date time attribute
DateTimeAttributeMetadata dtAttribute = new DateTimeAttributeMetadata
{
    // Set base properties
    SchemaName = "new_Datetime",
    LogicalName = "new_datetime",
    DisplayName = new Label("Sample DateTime", _languageCode),
    RequiredLevel = new AttributeRequiredLevelManagedProperty(AttributeRequiredLevel.None),
    Description = new Label("DateTime Attribute", _languageCode),
    // Set extended properties
    Format = DateTimeFormat.DateOnly,
    ImeMode = ImeMode.Disabled
};

// Add to list
addedAttributes.Add(dtAttribute);

// Create a decimal attribute	
DecimalAttributeMetadata decimalAttribute = new DecimalAttributeMetadata
{
    // Set base properties
    SchemaName = "new_Decimal",
    LogicalName = "new_decimal",
    DisplayName = new Label("Sample Decimal", _languageCode),
    RequiredLevel = new AttributeRequiredLevelManagedProperty(AttributeRequiredLevel.None),
    Description = new Label("Decimal Attribute", _languageCode),
    // Set extended properties
    MaxValue = 100,
    MinValue = 0,
    Precision = 1
};

// Add to list
addedAttributes.Add(decimalAttribute);

// Create a integer attribute	
IntegerAttributeMetadata integerAttribute = new IntegerAttributeMetadata
{
    // Set base properties
    SchemaName = "new_Integer",
    LogicalName = "new_integer",
    DisplayName = new Label("Sample Integer", _languageCode),
    RequiredLevel = new AttributeRequiredLevelManagedProperty(AttributeRequiredLevel.None),
    Description = new Label("Integer Attribute", _languageCode),
    // Set extended properties
    Format = IntegerFormat.None,
    MaxValue = 100,
    MinValue = 0
};

// Add to list
addedAttributes.Add(integerAttribute);

// Create a memo attribute 
MemoAttributeMetadata memoAttribute = new MemoAttributeMetadata
{
    // Set base properties
    SchemaName = "new_Memo",
    LogicalName = "new_memo",
    DisplayName = new Label("Sample Memo", _languageCode),
    RequiredLevel = new AttributeRequiredLevelManagedProperty(AttributeRequiredLevel.None),
    Description = new Label("Memo Attribute", _languageCode),
    // Set extended properties
    Format = StringFormat.TextArea,
    ImeMode = ImeMode.Disabled,
    MaxLength = 500
};

// Add to list
addedAttributes.Add(memoAttribute);

// Create a money attribute	
MoneyAttributeMetadata moneyAttribute = new MoneyAttributeMetadata
{
    // Set base properties
    SchemaName = "new_Money",
    LogicalName = "new_money",
    DisplayName = new Label("Money Picklist", _languageCode),
    RequiredLevel = new AttributeRequiredLevelManagedProperty(AttributeRequiredLevel.None),
    Description = new Label("Money Attribue", _languageCode),
    // Set extended properties
    MaxValue = 1000.00,
    MinValue = 0.00,
    Precision = 1,
    PrecisionSource = 1,
    ImeMode = ImeMode.Disabled
};

// Add to list
addedAttributes.Add(moneyAttribute);

// Create a picklist attribute	
PicklistAttributeMetadata pickListAttribute =
    new PicklistAttributeMetadata
    {
        // Set base properties
        SchemaName = "new_Picklist",
        LogicalName = "new_picklist",
        DisplayName = new Label("Sample Picklist", _languageCode),
        RequiredLevel = new AttributeRequiredLevelManagedProperty(AttributeRequiredLevel.None),
        Description = new Label("Picklist Attribute", _languageCode),
        // Set extended properties
        // Build local picklist options
        OptionSet = new OptionSetMetadata
        {
            IsGlobal = false,
            OptionSetType = OptionSetType.Picklist,
            Options =
        {
            new OptionMetadata(
                new Label("Created", _languageCode), null),
            new OptionMetadata(
                new Label("Updated", _languageCode), null),
            new OptionMetadata(
                new Label("Deleted", _languageCode), null)
        }
        }
    };

// Add to list
addedAttributes.Add(pickListAttribute);

// Create a string attribute
StringAttributeMetadata stringAttribute = new StringAttributeMetadata
{
    // Set base properties
    SchemaName = "new_String",
    LogicalName = "new_string",

    DisplayName = new Label("Sample String", _languageCode),
    RequiredLevel = new AttributeRequiredLevelManagedProperty(AttributeRequiredLevel.None),
    Description = new Label("String Attribute", _languageCode),
    // Set extended properties
    MaxLength = 100
};

// Add to list
addedAttributes.Add(stringAttribute);

//Multi-select attribute requires version 9.0 or higher.
if (_productVersion > new Version("9.0"))
{

    // Create a multi-select optionset
    MultiSelectPicklistAttributeMetadata multiSelectOptionSetAttribute = new MultiSelectPicklistAttributeMetadata()
    {
        SchemaName = "new_MultiSelectOptionSet",
        LogicalName = "new_multiselectoptionset",
        DisplayName = new Label("Multi-Select OptionSet", _languageCode),
        RequiredLevel = new AttributeRequiredLevelManagedProperty(AttributeRequiredLevel.None),
        Description = new Label("Multi-Select OptionSet description", _languageCode),
        OptionSet = new OptionSetMetadata()
        {
            IsGlobal = false,
            OptionSetType = OptionSetType.Picklist,
            Options = {
        new OptionMetadata(new Label("First Option",_languageCode),null),
        new OptionMetadata(new Label("Second Option",_languageCode),null),
        new OptionMetadata(new Label("Third Option",_languageCode),null)
        }
        }
    };
    // Add to list
    addedAttributes.Add(multiSelectOptionSetAttribute);
}

// NOTE: LookupAttributeMetadata cannot be created outside the context of a relationship.
// Refer to the WorkWithRelationships.cs reference SDK sample for an example of this attribute type.

// NOTE: StateAttributeMetadata and StatusAttributeMetadata cannot be created via the SDK.

foreach (AttributeMetadata anAttribute in addedAttributes)
{
    // Create the request.
    CreateAttributeRequest createAttributeRequest = new CreateAttributeRequest
    {
        EntityName = Contact.EntityLogicalName,
        Attribute = anAttribute
    };

    // Execute the request.
    _serviceProxy.Execute(createAttributeRequest);

    Console.WriteLine("Created the attribute {0}.", anAttribute.SchemaName);
}
```

<a name="BKMK_RetrieveAttribute"></a>

## Retrieve an attribute

 This sample shows how to retrieve the <xref:Microsoft.Xrm.Sdk.Metadata.AttributeMetadata> for an attribute using the <xref:Microsoft.Xrm.Sdk.Messages.RetrieveAttributeRequest>. This sample retrieves the metadata for a custom <xref:Microsoft.Xrm.Sdk.Metadata.StringAttributeMetadata> attribute called ‘new_string’ from the Contact entity that was created in [Create Attributes](#BKMK_CreateAttributes).
  
> [!NOTE]
> Because <xref:Microsoft.Xrm.Sdk.Messages.RetrieveAttributeRequest.RetrieveAsIfPublished> is true, this request returns the current unpublished definition of this attribute. You might use this if you are creating an Attribute editor and you want to retrieve the unpublished definition of the attribute. Otherwise, you should not specify `RetrieveAsIfPublished`. More information: [Retrieving unpublished metadata](/dynamics365/customer-engagement/developer/customize-dev/publish-customizations#retrieving-unpublished-metadata).  

```csharp
// Create the request
RetrieveAttributeRequest attributeRequest = new RetrieveAttributeRequest
{
    EntityLogicalName = Contact.EntityLogicalName,
    LogicalName = "new_string",
    RetrieveAsIfPublished = true
};

// Execute the request
RetrieveAttributeResponse attributeResponse =
    (RetrieveAttributeResponse)_serviceProxy.Execute(attributeRequest);

Console.WriteLine("Retrieved the attribute {0}.",
    attributeResponse.AttributeMetadata.SchemaName);
```

<a name="BKMK_UpdateAttribute"></a>

## Update an attribute

 This sample code shows how to update an attribute. This sample uses the <xref:Microsoft.Xrm.Sdk.Messages.UpdateAttributeRequest> to change the <xref:Microsoft.Xrm.Sdk.Metadata.AttributeMetadata>.<xref:Microsoft.Xrm.Sdk.Metadata.AttributeMetadata.DisplayName> property of a previously retrieved custom attribute for the `Contact` entity.  

```csharp
// Modify the retrieved attribute
AttributeMetadata retrievedAttributeMetadata =
    attributeResponse.AttributeMetadata;
retrievedAttributeMetadata.DisplayName =
    new Label("Update String Attribute", _languageCode);

// Update an attribute retrieved via RetrieveAttributeRequest
UpdateAttributeRequest updateRequest = new UpdateAttributeRequest
{
    Attribute = retrievedAttributeMetadata,
    EntityName = Contact.EntityLogicalName,
    MergeLabels = false
};

// Execute the request
_serviceProxy.Execute(updateRequest);

Console.WriteLine("Updated the attribute {0}.",
    retrievedAttributeMetadata.SchemaName);
```

<a name="BKMK_CreateLookupAttribute"></a>

## Create a lookup attribute

 A lookup attribute is created by using the <xref:Microsoft.Xrm.Sdk.Messages.CreateOneToManyRequest>.  

```csharp
CreateOneToManyRequest req = new CreateOneToManyRequest()
{
    Lookup = new LookupAttributeMetadata()
    {
        Description = new Label("The referral (lead) from the bank account owner", 1033),
        DisplayName = new Label("Referral", 1033),
        LogicalName = "new_parent_leadid",
        SchemaName = "New_Parent_leadId",
        RequiredLevel = new AttributeRequiredLevelManagedProperty(AttributeRequiredLevel.Recommended)
    },
    OneToManyRelationship = new OneToManyRelationshipMetadata()
    {
        AssociatedMenuConfiguration = new AssociatedMenuConfiguration()
        {
            Behavior = AssociatedMenuBehavior.UseCollectionName,
            Group = AssociatedMenuGroup.Details,
            Label = new Label("Bank Accounts", 1033),
            Order = 10000
        },
        CascadeConfiguration = new CascadeConfiguration()
        {
            Assign = CascadeType.Cascade,
            Delete = CascadeType.Cascade,
            Merge = CascadeType.Cascade,
            Reparent = CascadeType.Cascade,
            Share = CascadeType.Cascade,
            Unshare = CascadeType.Cascade
        },
        ReferencedEntity = "lead",
        ReferencedAttribute = "leadid",
        ReferencingEntity = _customEntityName,
        SchemaName = "new_lead_new_bankaccount"
    }
};
_serviceProxy.Execute(req);
```

<a name="BKMK_createcustlookup"></a>

## Create a customer lookup attribute

 Unlike a lookup attribute, a customer lookup attribute is created using the <xref:Microsoft.Xrm.Sdk.Messages.CreateCustomerRelationshipsRequest> message, which adds two relationships to the lookup attribute: one to the `Account` entity and the other one to the `Contact` entity. You cannot add relationship to any other entity except for `Account` and `Contact` entities for a customer lookup attribute.  

```csharp
CreateCustomerRelationshipsRequest createCustomerReq = new CreateCustomerRelationshipsRequest
{
    Lookup = new LookupAttributeMetadata
    {
        Description = new Label("The owner of the bank account", 1033),
        DisplayName = new Label("Account owner", 1033),
        RequiredLevel = new AttributeRequiredLevelManagedProperty(AttributeRequiredLevel.ApplicationRequired),
        SchemaName = "new_customerid"
    },
    OneToManyRelationships = new OneToManyRelationshipMetadata[]
    {
        new OneToManyRelationshipMetadata()
        {
            ReferencedEntity = "account",
            ReferencingEntity = _customEntityName,
            SchemaName = "new_bankaccount_customer_account",
        },
        new OneToManyRelationshipMetadata()
        {
            ReferencedEntity = "contact",
            ReferencingEntity = _customEntityName,
            SchemaName = "new_bankaccount_customer_contact",
        }
    },
};
_serviceProxy.Execute(createCustomerReq);
```

<a name="BKMK_CreatePicklistGlobalOptionSet"></a>

## Create a picklist that uses a global option set

 This sample code shows how to create a <xref:Microsoft.Xrm.Sdk.Metadata.PicklistAttributeMetadata> attribute that is associated with a global option set.  
  
 The following sample uses <xref:Microsoft.Xrm.Sdk.Messages.CreateAttributeRequest> to set the options for a <xref:Microsoft.Xrm.Sdk.Metadata.PicklistAttributeMetadata> attribute to use a global option set with a name represented by the string variable `_globalOptionSetName`. More information: [Customize option sets](metadata-option-sets.md)  
 
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

_serviceProxy.Execute(createRequest);
```

<a name="BKMK_InsertNewStatusValue"></a>

## Insert a new status value

 This sample code shows how to insert a new **Status Reason** option for <xref:Microsoft.Xrm.Sdk.Metadata.StatusAttributeMetadata> attribute.  
  
 The following sample code uses the <xref:Microsoft.Xrm.Sdk.Messages.InsertStatusValueRequest> to specify a new option for the `Contact` entity `Contact.StatusCode` attribute that is valid when the `Contact.StateCode` is 0 (Active). The <xref:Microsoft.Xrm.Sdk.IOrganizationService>.<xref:Microsoft.Xrm.Sdk.IOrganizationService.Execute*> method processes the request.  
  
 The following sample code allows two valid **Status Reason** options for active contacts: **Active** and **Dormant**.  
  
```csharp
// Use InsertStatusValueRequest message to insert a new status 
// in an existing status attribute. 
// Create the request.
InsertStatusValueRequest insertStatusValueRequest =
    new InsertStatusValueRequest
{
    AttributeLogicalName = "statuscode",
    EntityLogicalName = Contact.EntityLogicalName,
    Label = new Label("Dormant", _languageCode),
    StateCode = 0
};

// Execute the request and store newly inserted value 
// for cleanup, used later part of this sample. 
_insertedStatusValue = ((InsertStatusValueResponse)_serviceProxy.Execute(
    insertStatusValueRequest)).NewOptionValue;

Console.WriteLine("Created {0} with the value of {1}.",
    insertStatusValueRequest.Label.LocalizedLabels[0].Label,
    _insertedStatusValue);
```

<a name="BKMK_UpdateStateValue"></a>

## Update a state value

 This sample code shows how to change the label for an option in a <xref:Microsoft.Xrm.Sdk.Metadata.StateAttributeMetadata> attribute.  
  
 The following sample code uses <xref:Microsoft.Xrm.Sdk.Messages.UpdateStateValueRequest> to change the `Contact.StateCode` option label from **Active** to **Open**.  

```csharp
// Modify the state value label from Active to Open.
// Create the request.
UpdateStateValueRequest updateStateValue = new UpdateStateValueRequest
{
    AttributeLogicalName = "statecode",
    EntityLogicalName = Contact.EntityLogicalName,
    Value = 1,
    Label = new Label("Open", _languageCode)
};

// Execute the request.
_serviceProxy.Execute(updateStateValue);

Console.WriteLine(
    "Updated {0} state attribute of {1} entity from 'Active' to '{2}'.",
    updateStateValue.AttributeLogicalName,
    updateStateValue.EntityLogicalName,
    updateStateValue.Label.LocalizedLabels[0].Label
    );
```

 You cannot add or remove `StateCode` options, but you can change the labels for the options.  
  
<a name="BKMK_InsertNewOptionLocalOptionSet"></a>

## Insert a new option in a local option set

 This sample code shows how to add a new option to a local option set. The following sample uses <xref:Microsoft.Xrm.Sdk.Messages.InsertOptionValueRequest> to add a new option to a custom <xref:Microsoft.Xrm.Sdk.Metadata.PicklistAttributeMetadata> attribute for the `Contact` entity.  

```csharp
// Create a request.
InsertOptionValueRequest insertOptionValueRequest =
    new InsertOptionValueRequest
{
    AttributeLogicalName = "new_picklist",
    EntityLogicalName = Contact.EntityLogicalName,
    Label = new Label("New Picklist Label", _languageCode)
};

// Execute the request.
int insertOptionValue = ((InsertOptionValueResponse)_serviceProxy.Execute(
    insertOptionValueRequest)).NewOptionValue;

Console.WriteLine("Created {0} with the value of {1}.",
    insertOptionValueRequest.Label.LocalizedLabels[0].Label,
    insertOptionValue);
```

<a name="BKMK_ChangeOrderOptionLocalOptionSet"></a>

## Change the order of options in a local option set

 This sample code shows how to change the order of options in a local option set. The following sample retrieves a custom <xref:Microsoft.Xrm.Sdk.Metadata.PicklistAttributeMetadata> attribute and changes the order of the original options using the [OrderBy](https://msdn.microsoft.com/library/system.linq.enumerable.orderby.aspx)**LINQ** function to sort items in ascending order by the label text. Then it uses <xref:Microsoft.Xrm.Sdk.Messages.OrderOptionRequest> to set the new order of the options for the attribute.  
  
 Use the [OrderByDescending](https://msdn.microsoft.com/library/system.linq.enumerable.orderbydescending.aspx) linq function to order the items in descending order.  

```csharp
// Use the RetrieveAttributeRequest message to retrieve  
// a attribute by it's logical name.
RetrieveAttributeRequest retrieveAttributeRequest =
    new RetrieveAttributeRequest
{
    EntityLogicalName = Contact.EntityLogicalName,
    LogicalName = "new_picklist",
    RetrieveAsIfPublished = true
};

// Execute the request.
RetrieveAttributeResponse retrieveAttributeResponse =
    (RetrieveAttributeResponse)_serviceProxy.Execute(
    retrieveAttributeRequest);

// Access the retrieved attribute.
PicklistAttributeMetadata retrievedPicklistAttributeMetadata =
    (PicklistAttributeMetadata)
    retrieveAttributeResponse.AttributeMetadata;

// Get the current options list for the retrieved attribute.
OptionMetadata[] optionList =
    retrievedPicklistAttributeMetadata.OptionSet.Options.ToArray();

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
    AttributeLogicalName = "new_picklist",
    EntityLogicalName = Contact.EntityLogicalName,
    // Set the changed order using Select linq function 
    // to get only values in an array from the changed option list.
    Values = updateOptionList.Select(x => x.Value.Value).ToArray()
};

// Execute the request
_serviceProxy.Execute(orderOptionRequest);

Console.WriteLine("Option Set option order changed");
```

<a name="BKMK_DeleteAttribute"></a>

## Delete an attribute

 This sample shows how to delete attributes stored in a `List<`<xref:Microsoft.Xrm.Sdk.Metadata.AttributeMetadata>`>` that were created for the `Contact` entity in [Create Attributes](#BKMK_CreateAttributes). For each <xref:Microsoft.Xrm.Sdk.Metadata.AttributeMetadata> the <xref:Microsoft.Xrm.Sdk.Messages.DeleteAttributeRequest> prepares the request that is processed using <xref:Microsoft.Xrm.Sdk.IOrganizationService>.<xref:Microsoft.Xrm.Sdk.IOrganizationService.Execute*>.  

```csharp
// Delete all attributes created for this sample.
foreach (AttributeMetadata anAttribute in addedAttributes)
{
    // Create the request object
    DeleteAttributeRequest deleteAttribute = new DeleteAttributeRequest
    {
        // Set the request properties 
        EntityLogicalName = Contact.EntityLogicalName,
        LogicalName = anAttribute.SchemaName
    };
    // Execute the request
    _serviceProxy.Execute(deleteAttribute);
}
```


[!INCLUDE[footer-include](../../../includes/footer-banner.md)]