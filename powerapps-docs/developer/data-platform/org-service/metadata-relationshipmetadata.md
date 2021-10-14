---
title: "Create and retrieve table row relationships (Microsoft Dataverse) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "Shows code samples to create and retrieve table row relationships." # 115-145 characters including spaces. This abstract displays in the search result.
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

# Create and retrieve table row relationships

[!INCLUDE[cc-terminology](../includes/cc-terminology.md)]

This topic shows how to create and retrieve table row relationships. You can download the sample from [here](https://github.com/microsoft/PowerApps-Samples/tree/master/cds/orgsvc/C%23/CreateRetrieveEntityRelationships).
  
<a name="BKMK_Create1NEntityRelationship"></a>   

## Create a 1:N row relationship  

 The following code sample uses the [EligibleCreateOneToManyRelationship](#eligiblecreateonetomanyrelationship) method to verify that the `Account` and `Campaign` tables can participate in a 1:N row relationship and then creates the relationship by using <xref:Microsoft.Xrm.Sdk.Messages.CreateOneToManyRequest>.  
  
```csharp
bool eligibleCreateOneToManyRelationship =
    EligibleCreateOneToManyRelationship("account", "campaign");

if (eligibleCreateOneToManyRelationship)
{
    CreateOneToManyRequest createOneToManyRelationshipRequest =
        new CreateOneToManyRequest
    {
        OneToManyRelationship =
        new OneToManyRelationshipMetadata
        {
            ReferencedEntity = "account",
            ReferencingEntity = "campaign",
            SchemaName = "new_account_campaign",
            AssociatedMenuConfiguration = new AssociatedMenuConfiguration
            {
                Behavior = AssociatedMenuBehavior.UseLabel,
                Group = AssociatedMenuGroup.Details,
                Label = new Label("Account", 1033),
                Order = 10000
            },
            CascadeConfiguration = new CascadeConfiguration
            {
                Assign = CascadeType.NoCascade,
                Delete = CascadeType.RemoveLink,
                Merge = CascadeType.NoCascade,
                Reparent = CascadeType.NoCascade,
                Share = CascadeType.NoCascade,
                Unshare = CascadeType.NoCascade
            }
        },
        Lookup = new LookupAttributeMetadata
        {
            SchemaName = "new_parent_accountid",
            DisplayName = new Label("Account Lookup", 1033),
            RequiredLevel = new AttributeRequiredLevelManagedProperty(AttributeRequiredLevel.None),
            Description = new Label("Sample Lookup", 1033)
        }
    };


    CreateOneToManyResponse createOneToManyRelationshipResponse =
        (CreateOneToManyResponse)service.Execute(
        createOneToManyRelationshipRequest);

    _oneToManyRelationshipId =
        createOneToManyRelationshipResponse.RelationshipId;
    _oneToManyRelationshipName = 
        createOneToManyRelationshipRequest.OneToManyRelationship.SchemaName;

    Console.WriteLine(
        "The one-to-many relationship has been created between {0} and {1}.",
        "account", "campaign");
}
```
  
<a name="BKMK_EligibleCreateOneToManyRelationship"></a>

### EligibleCreateOneToManyRelationship  

 The following code sample uses the `EligibleCreateOneToManyRelationship` method that in turn uses <xref:Microsoft.Xrm.Sdk.Messages.CanBeReferencedRequest> and <xref:Microsoft.Xrm.Sdk.Messages.CanBeReferencingRequest> to verify whether two table rows can participate in a 1:N relationship.  
  
```csharp
/// <summary>
/// Determines whether two entities are eligible to participate in a relationship
/// </summary>
/// <param name="referencedEntity">Primary Entity</param>
/// <param name="referencingEntity">Referencing Entity</param>
/// <returns></returns>
public bool EligibleCreateOneToManyRelationship(string referencedEntity, 
    string referencingEntity)
{
    //Checks whether the specified entity can be the primary entity in one-to-many
    //relationship.
    CanBeReferencedRequest canBeReferencedRequest = new CanBeReferencedRequest
    {
        EntityName = referencedEntity
    };

    CanBeReferencedResponse canBeReferencedResponse =
        (CanBeReferencedResponse)service.Execute(canBeReferencedRequest);

    if (!canBeReferencedResponse.CanBeReferenced)
    {
        Console.WriteLine(
            "Entity {0} can't be the primary entity in this one-to-many relationship", 
            referencedEntity);
    }

    //Checks whether the specified entity can be the referencing entity in one-to-many
    //relationship.
    CanBeReferencingRequest canBereferencingRequest = new CanBeReferencingRequest
    {
        EntityName = referencingEntity
    };

    CanBeReferencingResponse canBeReferencingResponse =
        (CanBeReferencingResponse)service.Execute(canBereferencingRequest);

    if (!canBeReferencingResponse.CanBeReferencing)
    {
        Console.WriteLine(
            "Entity {0} can't be the referencing entity in this one-to-many relationship", 
            referencingEntity);
    }


    if (canBeReferencedResponse.CanBeReferenced == true
        && canBeReferencingResponse.CanBeReferencing == true)
    {
        return true;
    }
    else
    {
        return false;
    }
}
```
  
<a name="BKMK_CreateNNEntityRelationship"></a>   

## Create an N:N relationship  

 The following code sample uses the [EligibleCreateManyToManyRelationship](#BKMK_EligibleCreateManyToManyRelationship) method to verify that the `Account` and `Campaign` tables can participate in a N:N row relationship and then creates the table row relationship by using <xref:Microsoft.Xrm.Sdk.Messages.CreateManyToManyRequest>.  
  
```csharp
bool accountEligibleParticipate =
    EligibleCreateManyToManyRelationship("account");
bool campaignEligibleParticipate =
    EligibleCreateManyToManyRelationship("campaign");

if (accountEligibleParticipate && campaignEligibleParticipate)
{

    CreateManyToManyRequest createManyToManyRelationshipRequest =
        new CreateManyToManyRequest
    {
        IntersectEntitySchemaName = "new_accounts_campaigns",
        ManyToManyRelationship = new ManyToManyRelationshipMetadata
        {
            SchemaName = "new_accounts_campaigns",
            Entity1LogicalName = "account",
            Entity1AssociatedMenuConfiguration =
            new AssociatedMenuConfiguration
            {
                Behavior = AssociatedMenuBehavior.UseLabel,
                Group = AssociatedMenuGroup.Details,
                Label = new Label("Account", 1033),
                Order = 10000
            },
            Entity2LogicalName = "campaign",
            Entity2AssociatedMenuConfiguration =
            new AssociatedMenuConfiguration
            {
                Behavior = AssociatedMenuBehavior.UseLabel,
                Group = AssociatedMenuGroup.Details,
                Label = new Label("Campaign", 1033),
                Order = 10000
            }
        }
    };

    CreateManyToManyResponse createManytoManyRelationshipResponse =
        (CreateManyToManyResponse)service.Execute(
        createManyToManyRelationshipRequest);


    _manyToManyRelationshipId =
        createManytoManyRelationshipResponse.ManyToManyRelationshipId;
    _manyToManyRelationshipName =
        createManyToManyRelationshipRequest.ManyToManyRelationship.SchemaName;

    Console.WriteLine(
        "The many-to-many relationship has been created between {0} and {1}.",
        "account", "campaign");
}
```
  
<a name="BKMK_EligibleCreateManyToManyRelationship"></a>   

### EligibleCreateManyToManyRelationship  

 The following code sample creates a `EligibleCreateManyToManyRelationship` method that uses <xref:Microsoft.Xrm.Sdk.Messages.CanManyToManyRequest> to verify whether a table can participate in a N:N row relationship.  
  
```csharp
/// <summary>
/// Determines whether the entity can participate in a many-to-many relationship.
/// </summary>
/// <param name="entity">Entity</param>
/// <returns></returns>
public bool EligibleCreateManyToManyRelationship(string entity)
{
    CanManyToManyRequest canManyToManyRequest = new CanManyToManyRequest
    {
        EntityName = entity
    };

    CanManyToManyResponse canManyToManyResponse =
        (CanManyToManyResponse)service.Execute(canManyToManyRequest);

    if (!canManyToManyResponse.CanManyToMany)
    {
        Console.WriteLine(
            "Entity {0} can't participate in a many-to-many relationship.", 
            entity);
    }

    return canManyToManyResponse.CanManyToMany;
}
```
  
<a name="BKMK_RetrieveEntityRelationships"></a>

## Retrieve table row relationships

 The following code sample retrieves the two table row relationships previously created using <xref:Microsoft.Xrm.Sdk.Messages.RetrieveRelationshipRequest>. The first example uses the `MetadataId` and the second uses the `Name`.  
  
```csharp
//You can use either the Name or the MetadataId of the relationship.

//Retrieve the One-to-many relationship using the MetadataId.
RetrieveRelationshipRequest retrieveOneToManyRequest =
    new RetrieveRelationshipRequest { MetadataId = _oneToManyRelationshipId };
RetrieveRelationshipResponse retrieveOneToManyResponse =
    (RetrieveRelationshipResponse)service.Execute(retrieveOneToManyRequest);

Console.WriteLine("Retrieved {0} One-to-many relationship by id", retrieveOneToManyResponse.RelationshipMetadata.SchemaName);

//Retrieve the Many-to-many relationship using the Name.
RetrieveRelationshipRequest retrieveManyToManyRequest =
    new RetrieveRelationshipRequest { Name = _manyToManyRelationshipName};
RetrieveRelationshipResponse retrieveManyToManyResponse =
    (RetrieveRelationshipResponse)service.Execute(retrieveManyToManyRequest);

Console.WriteLine("Retrieved {0} Many-to-Many relationship by Name", retrieveManyToManyResponse.RelationshipMetadata.MetadataId);
```

### See Also  

 [Table relationship definition messages](../entity-relationship-metadata-messages.md)   

[!INCLUDE[footer-include](../../../includes/footer-banner.md)]