---
title: "Customer tables (account, contact, customeraddress) (Microsoft Dataverse) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "The account and contact tables are essential for identifying and managing customers, selling products and services, and providing superior service to the customers. A customer address table is used to store address and shipping information for a customer." # 115-145 characters including spaces. This abstract displays in the search result.
ms.custom: ""
ms.date: 03/30/2020
ms.reviewer: "pehecke"
ms.service: powerapps
ms.topic: "article"
author: "mayadumesh" # GitHub ID
ms.subservice: dataverse-developer
ms.author: "jdaly" # MSFT alias of Microsoft employees only
manager: "ryjones" # MSFT alias of manager or PM counterpart
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---
# Customer tables (account, contact, customeraddress)

[!INCLUDE[cc-terminology](includes/cc-terminology.md)]


The *account* and *contact* tables in Microsoft Dataverse are essential for identifying and managing customers, selling products and services, and providing superior service to the customers. A *customer address* table is used to store address and shipping information for a customer.  
  
## Account table
 
The account table is one of the tables in Dataverse to which most other tables are attached or parented. In Dataverse, an account represents a company with which the business unit has a relationship. Information that is included in an account is all relevant contact information, company information, category, relationship type, and address information. Other information that applies includes the following items:  
  
- An account can be a parent to almost any other table. This includes another account.  
  
- An account can be a standalone table.  
  
- An account can have only one account as its parent.  
  
- Accounts can have multiple child accounts and child contacts.  
  
Account management is one of the important concepts of business-to-business customer relationship management (Dynamics 365) because an organization wants to see all the activities they have with another company All these activities come together at the account level.  

More information: [Account table](reference/entities/account.md).
  
## Contact table

In Dataverse, a contact represents a person, usually an individual, with whom a business unit has a relationship, such as a customer, a supplier, or a colleague. The contact table is one of the tables that most other tables are linked to. A contact can be a stand-alone table. Included in this table are professional, personal, and family information, and multiple addresses. More information: [Contact table](reference/entities/contact.md).
  
Both accounts and contacts are part of managing customers and are related to one another in the following ways:  
  
- A contact can be a parent to every other table except accounts and contacts.  
  
- A contact can have only one account as its parent.  
  
- A contact can be marked as the primary contact person for an account by using the <xref:Microsoft.Xrm.Sdk.IOrganizationService.Update*> method.  
  
The contact table stores all information about a person such as an email address, street address, telephone numbers, and other related information, such as the birthday or anniversary date. Depending on the type of customers a business unit has, it needs either only contacts, or contacts and accounts, to give a full view of its customers.  
  
The basic operations that you can perform on a contact include Create, Read, Update, and Delete.  
  
Linking tables such as activities and notes to the contact table lets user see all the communication the user has had with a customer, any actions the user has taken on behalf of the customer, and all information the user needs about the customer.

## CustomerAddress table

This table contains address and shipping information. It is used to store additional addresses for an account or contact.

>[!NOTE]
>The Customer Address table is updated at the platform level when a change is made to the Account or Contact tables. Because of this, no separate SDK call will be made to update or create the Customer Address table. Any code that is triggering on address updates or creates should be pointing to the Contact or Account tables.
  

[!INCLUDE[footer-include](../../includes/footer-banner.md)]