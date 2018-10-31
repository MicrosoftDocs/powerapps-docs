---
title: "Customer entities(account, contact) (Common Data Service for Apps) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "The account and contact entities in Dynamics 365 are essential for identifying and managing customers, selling products and services, and providing superior service to the customers. A customer address entity is used to store address and shipping information for a customer." # 115-145 characters including spaces. This abstract displays in the search result.
ms.custom: ""
ms.date: 10/31/2018
ms.reviewer: ""
ms.service: "powerapps"
ms.topic: "article"
author: "mayadumesh" # GitHub ID
ms.author: "jdaly" # MSFT alias of Microsoft employees only
manager: "ryjones" # MSFT alias of manager or PM counterpart
---
# Customer entities (account, contact)

<!-- 
Was Mike Carter

https://docs.microsoft.com/en-us/dynamics365/customer-engagement/developer/customer-entities-account-contact

Refactor so that the links to entity reference are in the body, not just in the See allso.
Add some h2 sections so it is skimmable
 -->

The *account* and *contact* entities in Common Data Service for Apps are essential for identifying and managing customers, selling products and services, and providing superior service to the customers. A *customer address* entity is used to store address and shipping information for a customer.  
  
## Account entity
 
The account entity is one of the entities in CDS for Apps to which most other entities are attached or parented. In CDS for Apps, an account represents a company with which the business unit has a relationship. Information that is included in an account is all relevant contact information, company information, category, relationship type, and address information. Other information that applies includes the following items:  
  
- An account can be a parent to almost any other entity. This includes another account.  
  
- An account can be a standalone entity.  
  
- An account can have only one account as its parent.  
  
- Accounts can have multiple child accounts and child contacts.  
  
Account management is one of the important concepts of business-to-business customer relationship management (Dynamics 365) because an organization wants to see all the activities they have with another company All these activities come together at the account level.  

More information: [Account Entity](reference/entities/account.md).
  
## Contact entity

In CDS for Apps, a contact represents a person, usually an individual, with whom a business unit has a relationship, such as a customer, a supplier, or a colleague. The contact entity is one of the entities that most other entities are linked to. A contact can be a stand-alone entity. Included in this entity are professional, personal, and family information, and multiple addresses. More information: [Contact Entity](reference/entities/contact.md).
  
Both accounts and contacts are part of managing customers and are related to one another in the following ways:  
  
- A contact can be a parent to every other entity except accounts and contacts.  
  
- A contact can have only one account as its parent.  
  
- A contact can be marked as the primary contact person for an account by using the <xref:Microsoft.Xrm.Sdk.IOrganizationService.Update*> method.  
  
The contact entity stores all information about a person such as an email address, street address, telephone numbers, and other related information, such as the birthday or anniversary date. Depending on the type of customers a business unit has, it needs either only contacts, or contacts and accounts, to give a full view of its customers.  
  
The basic operations that you can perform on a contact include Create, Read, Update, and Delete.  
  
Linking entities such as activities and notes to the contact entity lets user see all the communication the user has had with a customer, any actions the user has taken on behalf of the customer, and all information the user needs about the customer.  
  
## In This Section  
 [Account Entity](reference/entities/account.md)  
  
 [Contact Entity](reference/entities/contact.md)  
  
 [CustomerAddress Entity](reference/entities/customeraddress.md)  
  
## Related Sections  
 [Model Your Business Data With Dynamics 365](/dynamics365/customer-engagement/developer/model-business-data)  
  
 [Business Management Entities](/dynamics365/customer-engagement/developer/business-management-entities)
