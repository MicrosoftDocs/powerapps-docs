---
title: "Comparing Microsoft Lists, Dataverse for Teams, and Dataverse | Microsoft Docs"
description: Quickly understand and apply the key considerations that will help you pick the correct data source for your app between one Microsoft Lists, Dataverse for Teams, and Dataverse.
author: matp
ms.service: powerapps
ms.topic: conceptual
ms.custom: 
ms.date: 04/22/2021
ms.author: mmercuri
ms.reviewer: matp
---
# Comparing Microsoft Lists, Dataverse for Teams, and Dataverse

Whether you’re using Power Apps to build a small app for your team or a mission critical app for your business, there are many great options for data. 

This article focuses on three of the most popular data technologies used in Microsoft Power Platform: Microsoft Lists, Microsoft Dataverse for Teams, and Microsoft Dataverse. With the answers to the questions below, you can quickly understand and apply the key considerations that will help you pick the correct one for your application.

The questions are broken out into four categories: 

|Category |Questions |
|----------|---------|
| Data |What types of data (and how much of it) will your application require?<br/>How do you want to search the data? |
|Application | How will the app be made available, for example in Teams, custom code, etc.?<br/>Will guests be accessing your application?<br/>Who will build the app; low-code or pro developers?<br/>What special capabilities does your application need? |
|Integration |What do you want to integrate the system with, for example, databases, services, etc.? |
|Admin and governance | What are your organizations requirements related to security and compliance?<br/>Are there special requirements for backing up and restoring the data? |

## Key considerations and differences between Lists, Dataverse for Teams, and Dataverse

Using the answers to the questions above, use the table below to help identify the right technology for your application.

|Considerations  |Lists  |Dataverse for Teams  |Dataverse  |
|- |- |- |- |
|Kinds of data  |Lists, File, Image  |Relational, File, or Image  |Relational, File, Image, Lake, Log, Relevance Search<br/>Virtual tables  |
|Number of Data Types  |15  |23 (Currency is basic version)  |24 (Currency is advanced version)  |
|Common Data Model  |N/A  |User table only  |Full support  |
|Capacity  |Up to 30M rows<br/>([considerations](/office365/servicedescriptions/sharepoint-online-service-description/sharepoint-online-limits) for lists > 100k)  |Up to 1 million rows<br/><br/>Small number of files or images<br/><br/>2000 API Calls per day per user  |No specified limit on rows. No specified limit of files or images 2,000 with option of capacity add-ons  |
| Data Movement  |Create from/Export to Excel  |Dataflows In  |Dataflows In/Out<br/>Server-side sync<br/>Synapse Integration (Bring Your Own Data Lake, Data Factory)  |
|Security  |Owners, Members, Visitors, Designers, Approvers roles Customizable permissions  |Owner, Member, Guest roles<br/><br/> Share app with Azure AD group  |Robust options to satisfy complex enterprise scenario requirements (roles, business units, auditing, CMK, hierarchical/field-Level security, etc.)  |
|Clients  |Lists, Teams*, Custom Code <br/><br/>*Cant create/pin lists on mobile  |Teams  |Teams, Power Apps, Power Apps portals, Dynamics 365, custom code |
|Guest Limitations  |Can't create or delete a list  |Can't make, install, or edit apps  |Must be in Azure AD using Azure B2B  |
|Pro Dev  |REST API<br/>Graph API  | -  |REST API<br/>Software Development Kit (SDK)<br/> Plug-in Support <br/>Integration (Event Hub, Service Bus, Webhook, Export to Lake) SQL Server Management Studio Integration  |
|Package and deploy  |Package and deploy Lists  |Single unmanaged solution per environment  |Unlimited  |
|Additional capabilities  |Calculations and rollups  |-  |Business workflows<br/>Business rules<br/>Calculations and rollups<br/>Mobile offline  |

### See also

[How are Dataverse for Teams and Dataverse different?](data-platform-compare.md) <br />
[What is Dataverse?](/powerapps/maker/data-platform/data-platform-intro)


[!INCLUDE[footer-include](../includes/footer-banner.md)]