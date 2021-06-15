---
title: FAQs for Dataverse for Teams | Microsoft Docs
description: Frequent asked questions (FAQs) for Dataverse for Teams.
author: mmercuri
ms.service: powerapps
ms.topic: conceptual
ms.custom: 
ms.date: 09/22/2020
ms.author: mmercuri
ms.reviewer: kvivek
---
# FAQs for Dataverse for Teams 

Here is a list of frequently asked (FAQs) for Dataverse for Teams; also see [Dataverse for Teams licensing FAQs](/power-platform/admin/powerapps-flow-licensing-faq#dataverse-for-teams) in the Power Platform admin guide.

### What does Dataverse for Teams enable and how does this impact Microsoft Power Platform and Teams users? 

Power Apps developers and Power Virtual Agents chatbot creators will now be able to make and manage their apps and bots directly in Teams with embedded [Power Apps](overview.md) and [Power Virtual Agents](/power-virtual-agents/teams/fundamentals-what-is-power-virtual-agents-teams) apps. This enables a streamlined end-to-end user experience and allows makers to deploy to Teams with one click through the Teams app store. These new features are powered by Power Platform enhancement in Teams that provide enterprise datastores with rich data types to Microsoft 365 users and is now included in Microsoft 365 and Office 365 licenses.

Also, apps built with Power Apps and used in Teams will be responsive to the form factor that they're loaded on, meaning a creator can build an app once for users to view full screen on both mobile devices and desktops.  

### What value does Dataverse for Teams offer for professional developers?

Dataverse includes a robust set of capabilities for professional developers, including API access, the ability to create plug-ins, and so on. 

Dataverse for Teams is initially focused on the low-code and no-code developer and does not provide access to these capabilities at launch. However, Dataverse for Teams capability along with premium functionality through Power apps provides professional developers the ability to create robust solutions with far less code, including extending the out-of-the-box capabilities of Power Automate with their own custom logic in Azure functions, connect their own web services, etc.

### When should customers use Lists versus Dataverse for Teams?

Lists is great for quickly tracking data in Teams. All your lists are instantly usable inside of Teams. Additionally, you can build canvas apps and flows on top of your Lists just like you can today in SharePoint. 

Dataverse for Teams is great for building Microsoft Power Platform solutions in Teams. With support for files, images, and multiple related tables, Dataverse for Teams can meet your needs today and be promoted to the full Dataverse if you need additional capacity or capabilities in the future.

### How does security and governance differ between Dataverse and Microsoft Dataverse for Teams?

Dataverse for Teams is enterprise grade and designed to work within Teams. Focused on Teams, it aligns with the core roles identified in the environment: Owners, Members, and Guests. 

For Dataverse for Teams, access to the environment is restricted just to the Teams owners, members, and guests. 
Granting access to the environment is managed by Teams Owner by adding or removing the Teams members.
Key benefits include -
- Supports Teams Azure AD security group with runtime (JIT) user access and privilege checks.  
- Auto assignment of System Administrator security role to Teams Owners. 
- Ability to assign different security roles to Teams Owners and Members.  
- No security settings management for Business Unit and Teams is required.

Dataverse is designed to be used in any application (not just Teams) and includes additional security features such as auditing, sharing, field level and hierarchical security.  

### How do users import data into tables in Dataverse for Teams?
Makers have the opportunity to bring in data through both the apps they develop as well as via connectors in Power Apps and Power Automate.

### Which tables are available to developers in Dataverse for Teams?  
 
Dataverse for Teams makes it easy for users to create custom tables for all of their scenarios. 

It also includes a User table that represents the Common Data Model's [User entity](/common-data-model/schema/core/applicationcommon/user). Data stored in the User table corresponds to a user in Azure Active Directory (Azure AD). 


### Does Dataverse for Teams include support for Common Data Model?
 
The User table is included in Dataverse for Teams. A broader set of Common Data Model entity support is available out-of-the-box in Dataverse. 

### Can I use tables from other environments?
 
Applications can include data from environments that the maker has access to within the current tenant.

### Where can I use the new visual editor?

In addition to the table designer experience previously found in Dataverse, Dataverse for Teams includes a new, easy-to-use editable grid that helps user be even more productive. You can also use tables from other environments subject to the normal permission model. The new visual editor is currently available only in Dataverse for Teams.


### See also

[Dataverse for Teams overview](overview-data-platform.md)<br />
[How are Dataverse for Teams and Dataverse different?](data-platform-compare.md) <br />
[Create tables](create-table.md)<br/>
[Work with table relationships](relationships-table.md)


[!INCLUDE[footer-include](../includes/footer-banner.md)]