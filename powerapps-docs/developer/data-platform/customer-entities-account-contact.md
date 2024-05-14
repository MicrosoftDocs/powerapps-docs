---
title: "Customer tables (account, contact, customeraddress) (Microsoft Dataverse) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "The account and contact tables are essential for identifying and managing customers, selling products and services, and providing superior service to the customers. A customer address table is used to store address and shipping information for a customer." # 115-145 characters including spaces. This abstract displays in the search result.
ms.date: 11/10/2023
ms.reviewer: pehecke
ms.topic: article
author: mayadumesh # GitHub ID
ms.subservice: dataverse-developer
ms.author: mayadu # MSFT alias of Microsoft employees only
search.audienceType: 
  - developer
---
# Customer tables (account, contact, customeraddress)

The *account* and *contact* tables in Microsoft Dataverse are essential for identifying and managing customers, selling products and services, and providing superior service to the customers. A *customer address* table is used to store address and shipping information for a customer.  
  
## Account table
 
The account table is one of the tables in Dataverse to which most other tables are attached or parented. In Dataverse, an account represents a company with which the business unit has a relationship. Information that is included in an account is all relevant contact information, company information, category, relationship type, and address information. Other information that applies includes the following items:  
  
- An account can be a parent to most table types, including another account.  
  
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

This table contains address and shipping information. It is used to store additional addresses for an account or contact. The platform creates Customer Address rows by default upon creation of an account or contact, irrespective of whether the current address values are blank or not.

>[!NOTE]
>The Customer Address table is updated at the platform level when a change is made to the Account or Contact tables. Because of this, no separate SDK call will be made to update or create the Customer Address table. Any code that is triggering on address updates or creates should be pointing to the Contact or Account tables.
  

[!INCLUDE[footer-include](../../includes/footer-banner.md)]

## Disable Empty Record Creation

Users can disable empty record creation.

**Configuration required to disable empty record creation**
Navigate to Power Platform Admin Center (PPAC) and click on **Environments** option on the left side panel.
Choose the radio button corresponding to the environment that needs "Disable empty record creation" feature enabled. 
Click on **Settings** on the top of the page and on the next page, navigate to **Product** and **Features** settings page.
Scroll down the **Features** setting page to enable **Disable Empty Address Record Creation** 
click Save on the bottom of the page to save the changes.

**How does this feature work**
The Power Platform Environment where the **Disable Empty Address Record Creation** is enabled, an address record will not be created if incoming payload does not contain data in address info. This feature ensures that an address record will be created only if the incoming payload contains address data.
**Note**: Enabling this feature does not remove existing empty address records. 

The **Disable Empty Address Record Creation** setting is applicable only for Account, Contact and Lead tables in Dataverse. Any other table that is associated with an address will not be impacted by this setting. For example if a table named Warehouse or Location has address associated with it and the incoming payload has empty address data, an empty address data record will be created for Warehouse.

The user can add or remove the **Disable Empty Address Record Creation** setting anytime. However the changes to setting will not have any impact on its previous setting. For example If **Disable Empty Address Record Creation** was enabled earlier and the user turned it off later, the system will NOT backfill any missing empty address table records. And Microsoft does not support to manually backfill those empty address records.

## Delete Address Data in Dataverse ##

**Enable Deletion of Address Records** is a feature that allows an user to delete address data in Dataverse if this flag is enabled in Product Features setting page. The default functionality in Dataverse will not allow users to delete address records in Dataverse. Address record deletion capability is applicable only for Account, Contact and Lead tables in Dataverse.

Enabling "Deletion of Address Records" feature in Dataverse allows address records to be deleted through the user experience in Power Platform or through bulk delete operation or through SDK. 

**Configuration required to Enable Deletion of address records**
Navigate to Power Platform Admin Center (PPAC) and click on **Environments** option on the left side panel.
Choose the radio button corresponding to the environment that needs "Disable empty record creation" feature enabled. 
Click on **Settings** on the top of the page and on the next page, navigate to **Product** and **Features** settings page.
Scroll down the **Features** setting page to enable **Enable Deletion of Address Records** 
click Save on the bottom of the page to save the changes.

