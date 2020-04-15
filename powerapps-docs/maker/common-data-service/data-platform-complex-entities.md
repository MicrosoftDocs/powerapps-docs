---
title: Complex entities requiring Power Apps Plan 2 licenses | Microsoft Docs
description: A list of complex entities in Common Data Service that require a Power Apps Plan 2 license.
author: lancedMicrosoft
manager: kvivek
ms.service: powerapps
ms.component: cds
ms.topic: reference
ms.date: 04/15/2020
ms.author: lanced
search.audienceType: 
  - maker
search.app: 
  - PowerApps
  - D365CE
---

# Complex entities and licensing

> [!IMPORTANT]
> This topic is applicable *only* for older Power Apps Plan 1 and Plan 2 licenses. This is because complex entities are only applicable for the older Power Apps Plan 1 and Plan 2 licenses, and not for the latest Power Apps per app and Power Apps per user plans.
> 
> For the latest information on licensing requirements for entities, see the [Power Apps licensing guide](https://go.microsoft.com/fwlink/p/?linkid=2085130).

Entities that include the following complex server-side logic require users of an app or flow that uses these entities to have a Power Apps Plan 2 or Power Automate Plan 2 license:

* Code plug-ins. More information: [Plug-in development](/powerapps/developer/common-data-service/plug-ins)
* Real-time workflows. More information: [Workflow processes](/flow/workflow-processes)

    > [!IMPORTANT]
    >  Only workflows that are converted to a real-time workflow are considered real-time and synchronous. Workflows that are run in the background can still be used with the appropriate Power Apps plan and do not require additional licenses.

To know whether or not you've added complex business logic to your entities, review the list of plug-in assemblies and workflows configured in your environment.

## Complex entities installed with Dynamics 365 apps
The following table lists entities that contain complex server-side logic out-of-the-box as part of the installation of model-driven applications in Dynamics 365, such as Dynamics 365 Sales and Dynamics 365 Customer Service. This list is intended as a guide. Depending on which Dynamics 365 apps and versions are installed in your environment, the list of complex entities may vary.

> [!NOTE]
>  If you are using the Common Data Service and have not installed a Dynamics 365 application or third-party solution, your environment will not have entities containing complex server side logic.

* Account
* Agreement
* Agreement Booking Date
* Agreement Booking Incident
* Agreement Booking Product
* Agreement Booking Service
* Agreement Booking Service Task
* Agreement Booking Setup
* Agreement Invoice Date
* Agreement Invoice Product
* Agreement Invoice Setup
* Agreement Sub-Status
* Bookable Resource
* Bookable Resource Booking
* Bookable Resource Booking Header
* Bookable Resource Category
* Bookable Resource Category Assn
* Bookable Resource Characteristic
* Bookable Resource Group
* Booking Alert
* Booking Alert Status
* Booking Status
* Characteristic
* Competency Requirement (Deprecated)
* Competitor
* Contact
* Customer Asset
* Delegation
* Expense
* Field Computation
* Field Service Price List Item
* Filter
* Follow
* Incident Type
* Incident Type Product
* Incident Type Service
* Incident Type Service Task
* Integration Job
* Integration Job Detail
* Inventory Adjustment
* Inventory Adjustment Product
* Inventory Transfer
* Invoice
* Invoice Frequency
* Invoice Line
* Invoice Line Detail
* Journal
* Journal Line
* Lead
* Note
* OData v4 Data Source
* Opportunity
* Opportunity Line
* Opportunity Line Detail
* Order
* Order Invoicing Product
* Order Invoicing Setup
* Order Line
* Payment
* Payment Detail
* Post Configuration
* Post Rule Configuration
* Postal Code
* Price List
* Price List Item
* Product
* Project
* Project Approval
* Project Contract Line Detail
* Project Contract Line Milestone
* Project Contract Line Resource Category
* Project Contract Line Transaction Category
* Project Parameter
* Project Stages
* Project Task Status User
* Project Team Member Sign-Up
* Purchase Order
* Purchase Order Bill
* Purchase Order Product
* Purchase Order Receipt
* Purchase Order Receipt Product
* Purchase Order Sub Status
* Queue Item
* Quote
* Quote Booking Incident
* Quote Booking Product
* Quote Booking Service
* Quote Booking Service Task
* Quote Booking Setup
* Quote Invoicing Product
* Quote Invoicing Setup
* Quote Line
* Quote Line Detail
* Quote Line Milestone
* Quote Line Resource Category
* Quote Line Transaction Category
* Quote Project Price List
* Rating Model
* Rating Value
* Requirement Characteristic
* Requirement Resource Category
* Requirement Resource Preference
* Requirement Status
* Resource Request
* Resource Requirement
* Resource Requirement Detail
* RMA
* RMA Product
* RMA Receipt
* RMA Receipt Product
* RMA Sub-Status
* Role competency requirement
* Role Price
* RTV
* RTV Product
* RTV Sub-Status
* Tax Code
* Tax Code Detail
* Time Entry
* Time Group
* Time Group Detail
* Time Off Request
* Transaction Category Price
* User
* View
* Wall View
* Warehouse
* Work Order
* Work Order Incident
* Work Order Product
* Work Order Service
* Work Order Service Task
* Work Order Sub-Status
* Work template

