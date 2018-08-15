---
title: Responding to Data Subject Rights (DSR) requests for PowerApps customer data  | Microsoft Docs
description: Walkthough of how to respond to Data Subject Rights (DSR) requests for PowerApps customer data
author: jamesol-msft
manager: kvivek
ms.service: powerapps
ms.component: pa-admin
ms.topic: conceptual
ms.date: 05/23/2018
ms.author: jamesol
---

# Responding to Data Subject Rights (DSR) requests for PowerApps customer data

## Introduction to DSR Requests
The European Union (EU) General Data Protection Regulation (GDPR) gives rights to people (known in the regulation as *data subjects*) to manage the personal data that's been collected by an employer or other type of agency or organization (known as the *data controller* or just *controller*). Personal data is defined very broadly under the GDPR as any data that relates to an identified or identifiable natural person. The GDPR gives data subjects the right to do the following, as it pertains to their personal data:

* Obtain copies
* Request corrections
* Restrict processing
* Delete it
* Receive it in electronic format so it can be moved to another controller

A formal request by a data subject to a controller to take an action on his or her personal data is called a Data Subject Rights (DSR) request.

This article describes how Microsoft is preparing for the GDPR, and also provides examples of steps you can take to support GDPR compliance when using PowerApps, Microsoft Flow, and Common Data Service (CDS) for Apps. You'll learn how to use Microsoft products, services, and administrative tools to help controller customers find, access, and act on personal data in the Microsoft cloud in response to DSR requests.

The following actions are covered in this article:

* **Discover** — Use search and discovery tools to more easily find customer data that may be the subject of a DSR request. Once potentially responsive documents are collected, you can perform one or more of the following DSR actions to respond to the request. Alternatively, you may determine that the request doesn't meet your organization’s guidelines for responding to DSR requests.

* **Access** — Retrieve personal data that resides in the Microsoft cloud and, if requested, make a copy of that data available to the data subject.

* **Rectify** — Make changes or implement other requested actions on the personal data, where applicable.

* **Restrict** — Restrict the processing of personal data, either by removing licenses for various online services or turning off the desired services where possible. You can also remove data from the Microsoft cloud and retain it on-premises or at another location.

* **Delete** — Permanently remove personal data that resides in the Microsoft cloud.

* **Export** — Provide an electronic copy (in a machine-readable format) of personal data to the data subject.

## Discover
The first step in responding to a DSR request is to find the personal data that is the subject of the request. This first step&mdash;finding and reviewing the personal data at issue&mdash;will help you determine whether a DSR request meets your organization's requirements for honoring or declining a DSR request. For example, after finding and reviewing the personal data at issue, you may determine the request doesn’t meet your organization’s requirements because doing so may adversely affect the rights and freedoms of others.

### Step 1: Find personal data for the user in PowerApps
Below is a summary of the types of PowerApps resources that contain personal data for a specific user.

Resources containing personal data |	Purpose
--- | ---
Environment |	An environment is a space to store, manage, and share your organization’s business data, apps, and flows. [Learn more](https://go.microsoft.com/fwlink/?linkid=872239)
Environment permissions	| Users are assigned to environments roles to be granted maker and administrative privileges within an environment. [Learn more](https://go.microsoft.com/fwlink/?linkid=872240)
Canvas app	| Cross-platform business apps that can be built from a power of a blank canvas and connected to over 200 data sources. [Learn more](https://go.microsoft.com/fwlink/?linkid=872241)
Canvas-app permissions	| Canvas apps can be shared with users within an organization. [Learn more](https://go.microsoft.com/fwlink/?linkid=872242)
Connection	| Used by connectors and allow for connectivity to APIs, systems, databases, etc. [Learn more](https://go.microsoft.com/fwlink/?linkid=872243)
Connection permissions	| Certain types of connections can be shared with users within an organization. [Learn more](https://go.microsoft.com/fwlink/?linkid=872244)
Custom connector	| Custom connectors that a user has created to provide access to a data source not offered through one of the PowerApps standard connectors. [Learn more](https://go.microsoft.com/fwlink/?linkid=872245)
Custom-connector permissions	| Custom connectors can be shared with users within an organization. [Learn more](https://go.microsoft.com/fwlink/?linkid=872246)
PowerApps user and user-app settings	| PowerApps stores several user preferences and settings that are used to deliver the PowerApps runtime and portal experiences.
PowerApps notifications	| PowerApps sends several types of notifications to users including when an app is shared with them and when a CDS for Apps export operation has completed.
Gateway	| Gateways are on-premises data gateways that can be installed by a user to transfer data quickly and securely between PowerApps and a data source that isn’t in the cloud. [Learn more](https://go.microsoft.com/fwlink/?linkid=872247)
Gateway permissions	| Gateways can be shared with users within an organization. [Learn more](https://go.microsoft.com/fwlink/?linkid=872249)
Model-driven apps and model-driven app permissions	| Model-driven app design is a component-focused approach to app development. Model-driven apps and their user access permissions are stored as data within the CDS for Apps database.  [Learn more](https://go.microsoft.com/fwlink/?linkid=872248)

PowerApps offers the following experiences to find personal data for a specific user:

- **Website access**: [PowerApps site](https://web.powerapps.com/?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc), [PowerApps Admin center](https://admin.powerapps.com/), and [Office 365 Service Trust Portal](https://servicetrust.microsoft.com/)
- **PowerShell access**: PowerApps cmdlets (for [app creators](https://go.microsoft.com/fwlink/?linkid=871448) and [administrators](https://go.microsoft.com/fwlink/?linkid=871804)) and [On-premises gateway cmdlets](https://go.microsoft.com/fwlink/?linkid=872238)

For detailed steps on how you can use these experiences to find personal data for a specific user for each of these types of resources, see [Responding to Data Subject Rights (DSR) requests to export PowerApps customer data](powerapps-gdpr-export-dsr.md).

After you find the data, you can then perform the specific action to satisfy the request by the data subject.

### Step 2: Find personal data for the user in Microsoft Flow
PowerApps licenses always include Microsoft Flow capabilities. In addition to being included in PowerApps licenses, Microsoft Flow is also available as a standalone service.

For guidance on how to discover personal data stored by the Microsoft Flow service, see [Responding to GDPR Data Subject Requests for Microsoft Flow](https://go.microsoft.com/fwlink/?linkid=872250).

> [!IMPORTANT]
> It is recommended that admins complete this step for a PowerApps user

### Step 3: Find personal data for the user in instances of CDS for Apps
Certain PowerApps licenses, including the PowerApps Community Plan, give the ability for users within your organization to create instances of CDS for Apps and to create and build apps on CDS for Apps. The PowerApps Community Plan is a free license that allows users to try out CDS for Apps in an individual environment. See the [PowerApps Pricing](https://powerapps.microsoft.com/pricing/) page for which capabilities are included in each PowerApps license.

For guidance on how to discover personal data stored by CDS for Apps, see [Responding to Data Subject Rights (DSR) requests for customer data in Common Data Service for Apps](common-data-service-gdpr-dsr-guide.md).

> [!IMPORTANT]
> It is recommended that admins complete this step for a PowerApps user.

## Rectify
If a data subject asks you to rectify the personal data that resides in your organization’s data, you and your organization must determine whether it’s appropriate to honor the request. Rectifying data may include editing, redacting, or removing personal data from a document or other type of item.

You can use Azure Active Directory to manage the identities (personal data) of your users withih PowerApps. Enterprise customers can manage DSR rectify requests by using the limited editing features within a given Microsoft service. As a data processor, Microsoft does not offer the ability to correct system-generated logs, because they reflect factual activities and constitute a historical record of events within Microsoft services. See [GDPR: Data Subject Requests (DSRs)](https://servicetrust.microsoft.com/ViewPage/GDPRDSR) for details.

## Restrict
Data subjects may request that you restrict processing of their personal data.  We provide both pre-existing application programming interfaces (APIs) and user interfaces (UIs).  These experiences provide the enterprise customer’s tenant administrator the capability to manage such DSRs through a combination of data export and data deletion. A customer may request:

* Export an electronic copy of the personal data of the user, including:

    - account(s)
    - system-generated logs
    - associated logs

* Delete the account and associated data residing within Microsoft systems.

## Export
The “right of data portability” allows a data subject to request a copy of his or her personal data in an electronic format (that’s a “structured, commonly used, machine read-able and interoperable format”) that may be transmitted to another data controller.

See [Responding to Data Subject Rights (DSR) requests to export PowerApps customer data](powerapps-gdpr-export-dsr.md) for details.

## Delete
The “right to erasure” by the removal of personal data from an organization’s customer data is a key protection in the GDPR. Removing personal data includes system-generated logs but not audit-log information.

PowerApps allows users to build line-of-business applications that are a critical part of your organization’s day-to-day operations. When a user leaves your organization, you will need to manually review and determine whether to delete certain data and resources that they have created. Other customer data will be automatically deleted whenever the user’s account is deleted from Azure Active Directory.

See [Responding to Data Subject Rights (DSR) requests to delete PowerApps customer data](powerapps-gdpr-delete-dsr.md) for details.
