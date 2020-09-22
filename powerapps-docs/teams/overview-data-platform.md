---
title: Project Oakdale overview | Microsoft Docs
description: Provides an overview of Project Oakdale.
author: NHelgren
ms.service: powerapps
ms.topic: conceptual
ms.custom: 
ms.date: 09/16/2020
ms.author: nhelgren
ms.reviewer: matp
---
# Overview of Project Oakdale

[!INCLUDE [cc-beta-prerelease-disclaimer.md](../includes/cc-beta-prerelease-disclaimer.md)]

Project Oakdale delivers a built-in, low-code data platform for Microsoft Teams. It provides relational data storage, rich data types, enterprise-grade governance, and one-click solution deployment. Project Oakdale enables everyone to easily build and deploy apps.

:::image type="content" source="media/tables-in-teams.png" alt-text="Project Oakdale table in Teams":::

Some of the benefits of Project Oakdale include:

- Support to build low-code and no-code apps, flows, and chatbots for and within Teams.

- Core data capabilities from the same platform behind Microsoft Power Platform and Dynamics 365.

- Storage, rich data types with enterprise capabilities, and one-click solution deployment.

- A new visual editor that makes it even easier to define and populate table data.

- Enterprise security that's easy to use and aligned with the approach used in Teams.

- Inclusion in most existing Teams licenses.

- Storage of 2 GB per team, and support for up to 1 million rows.

- Support for up to 500 teams.

- The capability to be promoted to full Common Data Service.

## Tables in Project Oakdale

Project Oakdale tables provide the ability to create, populate, and query data within Project Oakdale. Tables represent different types of entities important to an organization, such as a table to store products or another to store orders.  

Each of these tables includes columns that contain data about the subject of the table. For example, a table named *Product* might have columns that contain a product name, product identifier, manufacturer identifier, and price. Each of these columns can contain different types of data. For example, the type of data for a product name is text, identifiers could be numbers, and so on.

A solution often has multiple tables that are used together in an application. For example, an Order table might reference multiple other tables, such as Customer, Product, and Country. These tables are "related" to one another, and tables provide the way to create those relationships.

You can create and populate these tables with a new visual editor that makes it even easier to work with these tables.

> [!NOTE]
> All the capabilities found in tables are powered by Project Oakdale. Although this will satisfy many situations, in some situations an organization might want to have additional capacity, capabilities, or control over their solution. In these scenarios, Project Oakdale environments can be upgraded to Common Data Service. The upgrade process, referred to as *promotion*, has several considerations discussed in [Promotion process](/power-platform/admin/about-teams-environment?branch=teams-preview#promotion-process) in the Microsoft Power Platform admin guide.

## Security in Project Oakdale

These tables and the applications that use them are secured with enterprise-grade security that's easy to understand and use for low-code and no-code developers. Security in Project Oakdale aligns to how security is handled in Teams, with a focus on Owners, Members, and Guests.

## Administer Project Oakdale environment

You can administer and manage Project Oakdale environment using the Power Platform admin center. More information: [About the Project Oakdale environment](/power-platform/admin/about-teams-environment) in the Power Platform admin guide.

## Frequent asked questions (FAQs)

Here is a list of FAQs for Project Oakdale; also see [Project Oakdale licensing FAQs](/power-platform/admin/powerapps-flow-licensing-faq#project-oakdale) in the Power Platform admin guide.

### Why are we launching Project Oakdale?

Teams usage has grown rapidly with 75 Million daily active users. So, there a unique platform opportunity in focusing on Teams and Microsoft Power Platform.

### What does Project Oakdale enable and how does this impact Microsoft Power Platform and Teams users? 

Power Apps developers and Power Virtual Agents chatbot creators will now be able to make and manage their apps and bots directly in Teams with embedded Power Apps and Power Virtual Agents apps. This enables a streamlined end-to-end user experience and allows makers to deploy to Teams with one click through the Teams app store. These new features are powered by Power Platform enhancement in Teams that provide enterprise datastores with rich data types to Microsoft 365 users and is now included in Microsoft 365 and Office 365 licenses.

Also, apps built with Power Apps and used in Teams will be responsive to the form factor that they're loaded on, meaning a creator can build an app once for users to view full screen on both mobile devices and desktops.  

### What value does Project Oakdale offer for professional developers?

Common Data Service includes a robust set of capabilities for professional developers, including API access, the ability to create plug-ins, and so on. 

Project Oakdale is initially focused on the low-code and no-code developer and does not provide access to these capabilities at launch. However, Project Oakdale capability along with premium functionality through Power apps provides professional developers the ability to create robust solutions with far less code, including extending the out-of-the-box capabilities of Power Automate with their own custom logic in Azure functions, connect their own web services, etc.

### When should customers use Lists versus Project Oakdale?

Lists is great for quickly tracking data in Teams. All your lists are instantly usable inside of Teams. Additionally, you can build canvas apps and flows on top of your Lists just like you can today in SharePoint. Project Oakdale is great for building Microsoft Power Platform solutions in Teams. The key differences are in type of storage, for example, relational table storage and support for file and image data with find, filter, and sort, and the ability to easily work with multiple tables.

### How does security and governance differ between Common Data Service and Microsoft Project Oakdale?

Project Oakdale is enterprise grade and designed to work within Teams. Focused on Teams, it aligns with the core roles identified in the environment: Owners, Members, and Guests. 

For Project Oakdale, access to the environment is restricted just to the Teams owners, members, and guests. Granting access to environment is managed by Teams Owner by adding or removing the Teams members. 
- Supports Teams Azure AD security group with runtime (JIT) user access and privilege checks.  
- Auto assignment of System Administrator security role to Teams Owners. 
- Ability to assign different security roles to Teams Owners and Members.  
- No security settings management for Business Unit and Teams is required.

Common Data Service is designed to be used in any application (not just Teams) and includes additional security features such as auditing, sharing, field level and hierarchical security.  

### How do users import data into tables in Project Oakdale?
In addition to Office data sources like SharePoint and Excel and files in CSV format, users will have the opportunity to bring in data through connectors.

### Which tables are available to developers in Project Oakdale?  
 
Project Oakdale makes it easy for users to create custom tables for all of their scenarios. 

It also includes a User table that represents the Common Data Model's [User entity](https://docs.microsoft.com/common-data-model/schema/core/applicationcommon/user). Data stored in the User table corresponds to a user in Azure Active Directory (Azure AD). 


### Does Project Oakdale include support for Common Data Model?
 
During public preview, the User table is included in Project Oakdale. A broader set of Common Data Model entity support is available out-of-the-box in Common Data Service. 

### Can I use tables from other environments?
 
Applications can include data from environments that the maker has access to within the current tenant.

### Where can I use the new Visual Editor?

In addition to the Visual Editor experience previously found in Common Data Service, Project Oakdale includes a new, easy-to-use editable grid that helps user be even more productive. You can also use tables from other environments subject to the normal permission model. The new Visual Editor is currently only available in Oakdale.

### Can I use applications built using Project Oakdale Preview later in the generally available (GA) version of Project Oakdale?

Yes, Project Oakdale applications built using the preview version can be used later in the generally available version of Project Oakdale. 

### As an ISV, can I publish my solution to the Teams store?
We anticipate a rich ecosystem of solutions for Project Oakdale in the Teams store.  ISV’s are encouraged to build and publish solutions for Project Oakdale.

### See also

[How are Project Oakdale and Common Data Service different?](data-platform-compare.md) <br />
[Create tables](create-table.md)<br/>
[Work with table relationships](relationships-table.md)
