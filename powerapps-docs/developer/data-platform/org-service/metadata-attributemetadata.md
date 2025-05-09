---
title: "Work with column definitions (Microsoft Dataverse) | Microsoft Docs"
description: "Describes common operations on column definitions (attribute metadata)."
ms.date: 12/12/2022
ms.reviewer: jdaly
ms.topic: how-to
author: mkannapiran
ms.author: kamanick
search.audienceType: 
  - developer
contributors:
  - PHecke
  - JimDaly
---

# Work with column definitions

[!INCLUDE[cc-terminology](../includes/cc-terminology.md)]

This topic describes a number of common operations that can be applied to column definitions (attribute metadata).

<a name="BKMK_CreateAttributes"></a>

## Create columns

 You create columns (attributes) by defining one of the <xref:Microsoft.Xrm.Sdk.Metadata.AttributeMetadata> types and then passing it to the <xref:Microsoft.Xrm.Sdk.Messages.CreateAttributeRequest> message.  
  
 The following code sample defines the <xref:Microsoft.Xrm.Sdk.Metadata.AttributeMetadata> for a number of different types of columns and adds them to a `List<AttributeMetadata>`. At the end of the code the column definitions are passed to an instance of the <xref:Microsoft.Xrm.Sdk.Messages.CreateAttributeRequest> class and the column is created using the <xref:Microsoft.Xrm.Sdk.IOrganizationService>.<xref:Microsoft.Xrm.Sdk.IOrganizationService.Execute*> method.  
  
 The following sample code assumes that the current customization prefix is 'new' because that is the default customization prefix for the organization solution publisher. You should use the customization prefix for the solution publisher that makes sense for your solution context.  

```csharp
// Create storage for new  being created
var addedColumns = new List<AttributeMetadata>();
int languageCode = 1033; //English


// Create a yes/no column
var boolColumn = new BooleanAttributeMetadata
{
    // Set base properties
    SchemaName = "new_Boolean",
    LogicalName = "new_boolean",
    DisplayName = new Label("Sample Boolean", languageCode),
    RequiredLevel = new AttributeRequiredLevelManagedProperty(AttributeRequiredLevel.None),
    Description = new Label("Boolean Column", languageCode),
    // Set extended properties
    OptionSet = new BooleanOptionSetMetadata(
        new OptionMetadata(new Label("True", languageCode), 1),
        new OptionMetadata(new Label("False", languageCode), 0)
        )
};

// Add to list
addedColumns.Add(boolColumn);

// Create a date time column
var dateTimeColumn = new DateTimeAttributeMetadata
{
    // Set base properties
    SchemaName = "new_Datetime",
    LogicalName = "new_datetime",
    DisplayName = new Label("Sample DateTime", languageCode),
    RequiredLevel = new AttributeRequiredLevelManagedProperty(AttributeRequiredLevel.None),
    Description = new Label("DateTime Column", languageCode),
    // Set extended properties
    Format = DateTimeFormat.DateOnly,
    ImeMode = ImeMode.Disabled
};

// Add to list
addedColumns.Add(dateTimeColumn);

// Create a decimal column   
var decimalColumn = new DecimalAttributeMetadata
{
    // Set base properties
    SchemaName = "new_Decimal",
    LogicalName = "new_decimal",
    DisplayName = new Label("Sample Decimal", languageCode),
    RequiredLevel = new AttributeRequiredLevelManagedProperty(AttributeRequiredLevel.None),
    Description = new Label("Decimal Column", languageCode),
    // Set extended properties
    MaxValue = 100,
    MinValue = 0,
    Precision = 1
};

// Add to list
addedColumns.Add(decimalColumn);

// Create a integer column   
var integerColumn = new IntegerAttributeMetadata
{
    // Set base properties
    SchemaName = "new_Integer",
    LogicalName = "new_integer",
    DisplayName = new Label("Sample Integer", languageCode),
    RequiredLevel = new AttributeRequiredLevelManagedProperty(AttributeRequiredLevel.None),
    Description = new Label("Integer Column", languageCode),
    // Set extended properties
    Format = IntegerFormat.None,
    MaxValue = 100,
    MinValue = 0
};

// Add to list
addedColumns.Add(integerColumn);

// Create a memo column 
var memoColumn = new MemoAttributeMetadata
{
    // Set base properties
    SchemaName = "new_Memo",
    LogicalName = "new_memo",
    DisplayName = new Label("Sample Memo", languageCode),
    RequiredLevel = new AttributeRequiredLevelManagedProperty(AttributeRequiredLevel.None),
    Description = new Label("Memo Column", languageCode),
    // Set extended properties
    Format = StringFormat.TextArea,
    ImeMode = ImeMode.Disabled,
    MaxLength = 500
};

// Add to list
addedColumns.Add(memoColumn);

// Create a money column   
var moneyColumn = new MoneyAttributeMetadata
{
    // Set base properties
    SchemaName = "new_Money",
    LogicalName = "new_money",
    DisplayName = new Label("Sample Money", languageCode),
    RequiredLevel = new AttributeRequiredLevelManagedProperty(AttributeRequiredLevel.None),
    Description = new Label("Money Column", languageCode),
    // Set extended properties
    MaxValue = 1000.00,
    MinValue = 0.00,
    Precision = 1,
    PrecisionSource = 1,
    ImeMode = ImeMode.Disabled
};

// Add to list
addedColumns.Add(moneyColumn);

// Create a choice column   
var picklistColumn =
    new PicklistAttributeMetadata
    {
        // Set base properties
        SchemaName = "new_Picklist",
        LogicalName = "new_picklist",
        DisplayName = new Label("Sample Picklist", languageCode),
        RequiredLevel = new AttributeRequiredLevelManagedProperty(AttributeRequiredLevel.None),
        Description = new Label("Picklist Attribute", languageCode),
        // Set extended properties
        // Build local picklist options
        OptionSet = new OptionSetMetadata
        {
            IsGlobal = false,
            OptionSetType = OptionSetType.Picklist,
            Options =
            {
               new OptionMetadata(
                  new Label("Created", languageCode), null),
               new OptionMetadata(
                  new Label("Updated", languageCode), null),
               new OptionMetadata(
                  new Label("Deleted", languageCode), null)
            }
        }
    };

// Add to list
addedColumns.Add(picklistColumn);

// Create a string column
var stringColumn = new StringAttributeMetadata
{
    // Set base properties
    SchemaName = "new_String",
    LogicalName = "new_string",

    DisplayName = new Label("Sample String", languageCode),
    RequiredLevel = new AttributeRequiredLevelManagedProperty(AttributeRequiredLevel.None),
    Description = new Label("String Column", languageCode),
    // Set extended properties
    MaxLength = 100
};

// Add to list
addedColumns.Add(stringColumn);

//Multi-select column requires version 9.0 or higher.
if (_productVersion > new Version("9.0"))
{

    // Create a multi-select Choices column
    var multiSelectChoiceColumn = new MultiSelectPicklistAttributeMetadata()
    {
        SchemaName = "new_MultiSelectOptionSet",
        LogicalName = "new_multiselectoptionset",
        DisplayName = new Label("Choices column", languageCode),
        RequiredLevel = new AttributeRequiredLevelManagedProperty(AttributeRequiredLevel.None),
        Description = new Label("Choices columndescription", languageCode),
        OptionSet = new OptionSetMetadata()
        {
            IsGlobal = false,
            OptionSetType = OptionSetType.Picklist,
            Options = {
               new OptionMetadata(new Label("First Option",languageCode),null),
               new OptionMetadata(new Label("Second Option",languageCode),null),
               new OptionMetadata(new Label("Third Option",languageCode),null)
            }
        }
    };
    // Add to list
    addedColumns.Add(multiSelectChoiceColumn);

    // Create a BigInt column
    var bigIntColumn = new BigIntAttributeMetadata
    {
        // Set base properties
        SchemaName = "new_BigInt",
        LogicalName = "new_bigint",
        DisplayName = new Label("Sample Big Int", languageCode),
        RequiredLevel = new AttributeRequiredLevelManagedProperty(AttributeRequiredLevel.None),
        Description = new Label("Big Int Column", languageCode)
       

    };
    // Add to list
    addedColumns.Add(bigIntColumn);

}

foreach (AttributeMetadata aColumn in addedColumns)
{
    // Create the request.
    var createAttributeRequest = new CreateAttributeRequest
    {
        EntityName = Contact.EntityLogicalName,
        Attribute = aColumn
    };

    // Execute the request using IOrganizationService instance
    service.Execute(createAttributeRequest);

    Console.WriteLine($"Created the {aColumn.SchemaName} column.");
}
```

<a name="BKMK_RetrieveAttribute"></a>

## Retrieve a column

 This code sample shows how to retrieve the <xref:Microsoft.Xrm.Sdk.Metadata.AttributeMetadata> for a column using the <xref:Microsoft.Xrm.Sdk.Messages.RetrieveAttributeRequest>. This sample retrieves the definition for a custom <xref:Microsoft.Xrm.Sdk.Metadata.StringAttributeMetadata> column called 'new_string' from the Contact table that was created in [Create columns](#BKMK_CreateAttributes).
  
> [!NOTE]
> Because <xref:Microsoft.Xrm.Sdk.Messages.RetrieveAttributeRequest.RetrieveAsIfPublished> is true, this request returns the current unpublished definition of this column. You might use this if you are creating a column editor and you want to retrieve the unpublished definition of the column. Otherwise, you should not specify `RetrieveAsIfPublished`. More information: [Retrieving unpublished definitions](/dynamics365/customer-engagement/developer/customize-dev/publish-customizations#retrieving-unpublished-metadata).  

```csharp
// Create the request
RetrieveAttributeRequest attributeRequest = new RetrieveAttributeRequest
{
    EntityLogicalName = Contact.EntityLogicalName,
    LogicalName = "new_string",
    RetrieveAsIfPublished = true
};

// Execute the request using IOrganizationService instance
RetrieveAttributeResponse attributeResponse =
    (RetrieveAttributeResponse)service.Execute(attributeRequest);

Console.WriteLine("Retrieved the attribute {0}.",
    attributeResponse.AttributeMetadata.SchemaName);
```

<a name="BKMK_UpdateAttribute"></a>

## Update a column

 This code sample code shows how to update a column (attribute). This sample uses the <xref:Microsoft.Xrm.Sdk.Messages.UpdateAttributeRequest> to change the <xref:Microsoft.Xrm.Sdk.Metadata.AttributeMetadata>.<xref:Microsoft.Xrm.Sdk.Metadata.AttributeMetadata.DisplayName> property of a previously retrieved custom column for the `Contact` table.  

```csharp
// Modify the retrieved attribute
AttributeMetadata retrievedAttributeMetadata =
    attributeResponse.AttributeMetadata;
retrievedAttributeMetadata.DisplayName =
    new Label("Update String Attribute", 1033); // English

// Update an attribute retrieved via RetrieveAttributeRequest
UpdateAttributeRequest updateRequest = new UpdateAttributeRequest
{
    Attribute = retrievedAttributeMetadata,
    EntityName = Contact.EntityLogicalName,
    MergeLabels = false
};

// Execute the request using IOrganizationService instance
service.Execute(updateRequest);

Console.WriteLine("Updated the attribute {0}.",
    retrievedAttributeMetadata.SchemaName);
```

<a name="BKMK_CreateLookupAttribute"></a>

## Create a lookup column

 A lookup column is created by using the <xref:Microsoft.Xrm.Sdk.Messages.CreateOneToManyRequest>.  

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
// Execute the request using IOrganizationService instance
service.Execute(req);
```

<a name="BKMK_createcustlookup"></a>

## Create a customer lookup column

 Unlike a lookup column, a customer lookup column is created using the <xref:Microsoft.Xrm.Sdk.Messages.CreateCustomerRelationshipsRequest> message, which adds two relationships to the lookup column: one to the `Account` table and the other one to the `Contact` table. You cannot add relationship to any other table except for `Account` and `Contact` for a customer lookup column.  

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
// Execute the request using IOrganizationService instance
service.Execute(createCustomerReq);
```

<a name="BKMK_CreatePicklistGlobalOptionSet"></a>

## Create a choice column that uses global choices

 This sample code shows how to create a <xref:Microsoft.Xrm.Sdk.Metadata.PicklistAttributeMetadata> choice column that is associated with global choices.  
  
 The following sample uses <xref:Microsoft.Xrm.Sdk.Messages.CreateAttributeRequest> to set the options for a <xref:Microsoft.Xrm.Sdk.Metadata.PicklistAttributeMetadata> column to use global choices with a name represented by the string variable `_globalOptionSetName`. More information: [Customize choices](metadata-option-sets.md)  
 
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
        DisplayName = new Label("Example Picklist", 1033), //English
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
// Execute the request using IOrganizationService instance
service.Execute(createRequest);
```

<a name="BKMK_InsertNewStatusValue"></a>

## Insert a new status value

 This sample code shows how to insert a new **Status Reason** choice for <xref:Microsoft.Xrm.Sdk.Metadata.StatusAttributeMetadata> column.  
  
 The following sample code uses the <xref:Microsoft.Xrm.Sdk.Messages.InsertStatusValueRequest> to specify a new choice for the `Contact` table `Contact.StatusCode` column that is valid when the `Contact.StateCode` is 0 (Active). The <xref:Microsoft.Xrm.Sdk.IOrganizationService>.<xref:Microsoft.Xrm.Sdk.IOrganizationService.Execute*> method processes the request.  
  
 The following sample code allows two valid **Status Reason** choices for active contacts: **Active** and **Dormant**.  
  
```csharp
// Use InsertStatusValueRequest message to insert a new status 
// in an existing status attribute. 
// Create the request.
InsertStatusValueRequest insertStatusValueRequest =
    new InsertStatusValueRequest
{
    AttributeLogicalName = "statuscode",
    EntityLogicalName = Contact.EntityLogicalName,
    Label = new Label("Dormant", 1033), //English
    StateCode = 0
};

// Execute the request using IOrganizationService instance and store newly inserted value 
// for cleanup, used later part of this sample. 
_insertedStatusValue = ((InsertStatusValueResponse)service.Execute(
    insertStatusValueRequest)).NewOptionValue;

Console.WriteLine("Created {0} with the value of {1}.",
    insertStatusValueRequest.Label.LocalizedLabels[0].Label,
    _insertedStatusValue);
```

<a name="BKMK_UpdateStateValue"></a>

## Update a state value

 This sample code shows how to change the label for a choice in a <xref:Microsoft.Xrm.Sdk.Metadata.StateAttributeMetadata> column.
  
 The following sample code uses <xref:Microsoft.Xrm.Sdk.Messages.UpdateStateValueRequest> to change the `Contact.StateCode` choice label from **Active** to **Open**.  

```csharp
// Modify the state value label from Active to Open.
// Create the request.
UpdateStateValueRequest updateStateValue = new UpdateStateValueRequest
{
    AttributeLogicalName = "statecode",
    EntityLogicalName = Contact.EntityLogicalName,
    Value = 1,
    Label = new Label("Open", 1033) //English
};

// Execute the request using IOrganizationService instance
service.Execute(updateStateValue);

Console.WriteLine(
    "Updated {0} state attribute of {1} entity from 'Active' to '{2}'.",
    updateStateValue.AttributeLogicalName,
    updateStateValue.EntityLogicalName,
    updateStateValue.Label.LocalizedLabels[0].Label
    );
```

 You cannot add or remove `StateCode` choices, but you can change the labels for the choices.  
  
<a name="BKMK_InsertNewOptionLocalOptionSet"></a>

## Insert a new choice in local choices

 This sample code shows how to add a new choice to local choices. The following sample uses <xref:Microsoft.Xrm.Sdk.Messages.InsertOptionValueRequest> to add a new choice to a custom <xref:Microsoft.Xrm.Sdk.Metadata.PicklistAttributeMetadata> column for the `Contact` table.  

```csharp
// Create a request.
InsertOptionValueRequest insertOptionValueRequest =
    new InsertOptionValueRequest
{
    AttributeLogicalName = "new_picklist",
    EntityLogicalName = Contact.EntityLogicalName,
    Label = new Label("New Picklist Label", 1033) //English
};

// Execute the request using IOrganizationService instance
int insertOptionValue = ((InsertOptionValueResponse)service.Execute(
    insertOptionValueRequest)).NewOptionValue;

Console.WriteLine("Created {0} with the value of {1}.",
    insertOptionValueRequest.Label.LocalizedLabels[0].Label,
    insertOptionValue);
```

<a name="BKMK_ChangeOrderOptionLocalOptionSet"></a>

## Change the order of choices in local choices

 This sample code shows how to change the order of choices in local choices. The following sample retrieves a custom <xref:Microsoft.Xrm.Sdk.Metadata.PicklistAttributeMetadata> column and changes the order of the original choices using the [OrderBy](/dotnet/api/system.linq.enumerable.orderby)**LINQ** function to sort items in ascending order by the label text. Then it uses <xref:Microsoft.Xrm.Sdk.Messages.OrderOptionRequest> to set the new order of the choices for the column.  
  
 Use the [OrderByDescending](/dotnet/api/system.linq.enumerable.orderbydescending) linq function to order the items in descending order.  

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

// Execute the request using IOrganizationService instance
RetrieveAttributeResponse retrieveAttributeResponse =
    (RetrieveAttributeResponse)service.Execute(
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

// Execute the request using IOrganizationService instance
service.Execute(orderOptionRequest);

Console.WriteLine("Option Set option order changed");
```

<a name="BKMK_DeleteAttribute"></a>

## Delete a column

 This code sample shows how to delete columns stored in a `List<`<xref:Microsoft.Xrm.Sdk.Metadata.AttributeMetadata>`>` that were created for the `Contact` table in [Create columns](#BKMK_CreateAttributes). For each <xref:Microsoft.Xrm.Sdk.Metadata.AttributeMetadata> the <xref:Microsoft.Xrm.Sdk.Messages.DeleteAttributeRequest> prepares the request that is processed using <xref:Microsoft.Xrm.Sdk.IOrganizationService>.<xref:Microsoft.Xrm.Sdk.IOrganizationService.Execute*>.  

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
    // Execute the request using IOrganizationService instance
    service.Execute(deleteAttribute);
}
```

[!INCLUDE[footer-include](../../../includes/footer-banner.md)]
