---
title: Introduction to the Power Platform ISV Studio | Microsoft Docs
description: Learn how apps are managed and supported through the ISV Studio portal.
services: ''
suite: powerapps
documentationcenter: na
author: "phecke" # GitHub ID
manager: kvivek
editor: ''
tags: ''
ms.service: powerapps
ms.devlang: na
ms.topic: article
ms.reviewer: pehecke
ms.workload: na
ms.date: 07/11/2019
ms.author: prkoduku
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---

# Introduction to ISV Studio for the Power Platform

[!INCLUDE [cc-beta-prerelease-disclaimer](../../includes/cc-beta-prerelease-disclaimer.md)]

ISV Studio is designed to become the go-to Power Platform destination for Independent Software Vendors (ISV) to monitor and manage their applications. ISV Studio provides a consolidated cross tenant view of all the applications an ISV is distributing to customers.

> [!IMPORTANT]
>
> - ISV Studio is a preview feature.
> - [!INCLUDE[cc_preview_features_definition](../../includes/cc-preview-features-definition.md)]

ISV Studio supports applications built on the Common Data Service that are published to and deployed through [AppSource](https://appsource.microsoft.com/). No telemetry will be provided on side loaded solutions not deployed through AppSource.

The applications currently available on the Common Data Service includes Power Apps as well as Dynamics 365 for Sales, Marketing, Service, and Talent.

As an end user installs an application from AppSource, a consent dialog will be displayed requesting the user to acknowledge that contact, usage, and transactional information may be shared with the application provider. This information is used by the provider to support billing and other transactional activities and to enable telemetry in ISV Studio for the ISV to learn from and act on.

A customer can request that data not be shared with the provider, in which case Microsoft will remove all data from that particular tenant within ISV Studio.

To access the public preview of ISV Studio, navigate your browser to [https://aka.ms/ISVStudio](https://aka.ms/ISVStudio/).

## Pre-requisites

1. The ISV must be associated with a Microsoft registered Partner organization [ISV] that has one or more supported apps published in [AppSource](https://appsource.microsoft.com/). Supported apps include Power Apps and model-driven apps in Dynamics 365 such as Dynamics 365 Sales and Dynamics 365 Customer Service.

2. The ISV must have an [Azure Active Directory](https://azure.microsoft.com/services/active-directory/) (AAD) account and the account must be configured as an app contributor or owner in Partner Center for the particular ISV.

If you want additional users to get access to ISV Studio, they can be added as app contributors in Partner Center.  Instructions can be found at
[Managing users on cloud partner portal](https://docs.microsoft.com/azure/marketplace/cloud-partner-portal-orig/cloud-partner-portal-manage-users).

Continue reading the "App" and "Tenant" page topics listed below to learn about the capabilities of ISV Studio.

Please send an email to [ISVFeedback@microsoft.com](mailto:ISVFeedback@microsoft.com) with any feedback or questions. Your feedback is important for us to shape the experiences moving forward.

## In this Section

[Home page](isv-app-management-homepage.md)  
[App page](isv-app-management-apppage.md)  
[Tenant page](isv-app-management-tenantpage.md)
[AppSource checker](isv-app-management-appsource-checker.md)
[Connector certification portal](https://docs.microsoft.com/connectors/custom-connectors/submit-certification)

### See also

[Introduction to solutions](introduction-solutions.md)  
[Publish your app on AppSource](publish-app-appsource.md)
