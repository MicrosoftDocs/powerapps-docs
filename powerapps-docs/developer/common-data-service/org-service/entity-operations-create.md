---
title: "<Topic Title> (Common Data Service for Apps) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "<Description>" # 115-145 characters including spaces. This abstract displays in the search result.
ms.custom: ""
ms.date: 08/01/2018
ms.reviewer: ""
ms.service: "powerapps"
ms.topic: "article"
author: "JimDaly" # GitHub ID
ms.author: "jdaly" # MSFT alias of Microsoft employees only
manager: "ryjones" # MSFT alias of manager or PM counterpart
---
# Create entities using the Organization Service

<!-- use-early-bound-entity-classes-create-update-delete.md
manage-duplicate-detection-create-update.md -->

## Use IOrganizationService.Create

### Late-bound example

The following example shows using the <xref:Microsoft.Xrm.Sdk.Entity> class to create an account record using the  <xref:Microsoft.Xrm.Sdk.IOrganizationService>.<xref:Microsoft.Xrm.Sdk.IOrganizationService.Create*> method. 

```csharp
//Use Entity class with entity logical name
var account = new Entity("account");

// set attribute values
    // string primary name
    account["name"] = "Contoso";            
    // Boolean (Two option)
    account["creditonhold"] = false;
    // DateTime
    account["lastonholdtime"] = new DateTime(2017, 1, 1);
    // Double
    account["address1_latitude"] = 47.642311;
    account["address1_longitude"] = -122.136841;
    // Int
    account["numberofemployees"] = 500;
    // Lookup
    var USDollarCurrencyId = new Guid("547d3ece-e80c-e811-a95b-000d3af4434f");
    var USDCurrencyReference = new EntityReference("transactioncurrency", USDollarCurrencyId);
    account["transactioncurrencyid"] = USDCurrencyReference;
    // Money
    account["revenue"] = 5000000.00;
    // Picklist (Option set)
    account["accountcategorycode"] = new OptionSetValue(1); //Preferred customer
                
//Create the account
Guid accountid = crmSvc.Create(account);
```

### Early-bound example


## Use the CreateRequest class

You can use either the late-bound <xref:Microsoft.Xrm.Sdk.Entity> class or the early-bound `Account` class with the <xref:Microsoft.Xrm.Sdk.Messages.CreateRequest> by setting the instance to the <xref:Microsoft.Xrm.Sdk.Messages.CreateRequest.Target> property and then using the <xref:Microsoft.Xrm.Sdk.IOrganizationService>.<xref:Microsoft.Xrm.Sdk.IOrganizationService.Execute*> to get a <xref:Microsoft.Xrm.Sdk.Messages.CreateResponse>. The id of the created record will be in the <xref:Microsoft.Xrm.Sdk.Messages.CreateResponse.id> property value.

```csharp
var request = new CreateRequest() { Target = account };
var response  = (CreateResponse)crmSvc.Execute(request);
Guid accountid = response.id;
```