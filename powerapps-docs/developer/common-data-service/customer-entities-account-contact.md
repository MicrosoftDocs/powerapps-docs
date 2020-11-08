---
title: "Customer tables (account, contact, customeraddress) (Common Data Service) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "The account and contact tables in Common Data Service are essential for identifying and managing customers, selling products and services, and providing superior service to the customers. A customer address entity is used to store address and shipping information for a customer." # 115-145 characters including spaces. This abstract displays in the search result.
ms.custom: ""
ms.date: 11/08/2020
ms.reviewer: "pehecke"
ms.service: powerapps
ms.topic: "article"
author: "mayadumesh" # GitHub ID
ms.author: "jdaly" # MSFT alias of Microsoft employees only
manager: "ryjones" # MSFT alias of manager or PM counterpart
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---
# Customer tables (account, contact, customeraddress)

[!INCLUDE[cc-data-platform-banner](../../includes/cc-data-platform-banner.md)]

The *account* and *contact* tables in Common Data Service are essential for identifying and managing customers, selling products and services, and providing superior service to the customers. A *customer address* entity is used to store address and shipping information for a customer.  
  
## Account entity
 
The account entity is one of the tables in Common Data Service to which most other tables are attached or parented. In Common Data Service, an account represents a company with which the business unit has a relationship. Information that is included in an account is all relevant contact information, company information, category, relationship type, and address information. Other information that applies includes the following items:  
  
- An account can be a parent to almost any other entity. This includes another account.  
  
- An account can be a standalone entity.  
  
- An account can have only one account as its parent.  
  
- Accounts can have multiple child accounts and child contacts.  
  
Account management is one of the important concepts of business-to-business customer relationship management (Dynamics 365) because an organization wants to see all the activities they have with another company All these activities come together at the account level.  

More information: [Account table](reference/entities/account.md).
  
## Contact entity

In Common Data Service, a contact represents a person, usually an individual, with whom a business unit has a relationship, such as a customer, a supplier, or a colleague. The contact entity is one of the tables that most other tables are linked to. A contact can be a stand-alone entity. Included in this entity are professional, personal, and family information, and multiple addresses. More information: [Contact table](reference/entities/contact.md).
  
Both accounts and contacts are part of managing customers and are related to one another in the following ways:  
  
- A contact can be a parent to every other entity except accounts and contacts.  
  
- A contact can have only one account as its parent.  
  
- A contact can be marked as the primary contact person for an account by using the <xref:Microsoft.Xrm.Sdk.IOrganizationService.Update*> method.  
  
The contact entity stores all information about a person such as an email address, street address, telephone numbers, and other related information, such as the birthday or anniversary date. Depending on the type of customers a business unit has, it needs either only contacts, or contacts and accounts, to give a full view of its customers.  
  
The basic operations that you can perform on a contact include Create, Read, Update, and Delete.  
  
Linking tables such as activities and notes to the contact table lets user see all the communication the user has had with a customer, any actions the user has taken on behalf of the customer, and all information the user needs about the customer.

## CustomerAddress entity

This entity contains address and shipping information. It is used to store additional addresses for an account or contact. More information: [CustomerAddress table](reference/entities/customeraddress.md)

>[!NOTE]
>The Customer Address table is updated at the platform level when a change is made to the Account or Contact tables. 
>Because of this, no separate SDK call will be made to update or create the Customer Address entity. Any code that is triggering 
>on address updates or creates should be pointing to the Contact or Account tables.
