---
title: "Build Windows client applications using the XRM tools (Common Data Service for Apps)| Microsoft Docs"
description: "XRM tooling is a set of APIs that provides support for building Windows client applications for CDS for Apps"
ms.custom: ""
ms.date: 10/31/2018
ms.reviewer: ""
ms.service: "crm-online"
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "get-started-article"
applies_to: 
  - "Dynamics 365 (online)"
ms.assetid: e2f22576-1705-4854-a804-a1ca232c0cfc
caps.latest.revision: 33
author: "MattB-msft"
ms.author: "kvivek"
manager: "kvivek"
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---
# Build Windows client applications using the XRM tools

XRM tooling is a set of APIs built on top of the Common Data Service for Apps assembly APIs (Organization service and Discovery service) that provide support for building Windows client applications for CDS for Apps. It provides the following capabilities:  
  
- Supports all the authentication modes to sign in to CDS for Apps.  
- Provides PowerShell support for authentication and connection to CDS for Apps.  
- Provides thread safety for actions performed in CDS for Apps in a multithreaded environment. More information [Multithreading in Components](https://msdn.microsoft.com/library/vstudio/3es4b6yy.aspx), [Thread-Safe Components](https://msdn.microsoft.com/library/vstudio/a8544e2s.aspx)  
- Provides a common Windows Presentation Foundation login control for CDS for Apps for consistent sign-in experience to CDS for Apps from your Windows client applications.  
- Supports secure storage of the sign-in credentials and reuse of the stored credentials to automatically sign in to CDS for Apps after initial sign in.  
- Provides built-in diagnostic tracing and performance reporting of the actions performed in CDS for Apps, which you can configure based on your organization’s requirements.  
  
## Components of XRM tooling  

XRM tooling has the following three components:  
  
- **Interface for developers**: This provides the low-level interaction and wrapper methods for the CDS for Apps SDK assembly APIs. It is an instrumented API that provides a thread safe environment for making calls to CDS for Apps with built-in diagnostic capabilities to help you determine the performance of individual calls. It also provides a standard set of trace listeners for debugging support. The namespace for this component is <xref:Microsoft.Xrm.Tooling.Connector>.  
  
- **Common login control**: This is a WPF user control that provides a common user interface for the sign in experience to CDS for Apps. The login control provides support for all the authentication modes that are supported by CDS for Apps. The common login control has built-in encryption for securely storing your credentials/profile, and then reusing it at runtime to automatically sign in to CDS for Apps. The namespace for this component is <xref:Microsoft.Xrm.Tooling.CrmConnectControl>.  
  
- **Web resource utility**: This provides support for accessing information from the following two types of web resources in CDS for Apps: Image and XML. You can access an image from a CDS for Apps web resource and return it as WPF BitmapImage objects. Similarly, you can return an XML web resource as a string. The namespace for this component is <xref:Microsoft.Xrm.Tooling.WebResourceUtility>.  
  
## Client applications that use XRM tooling

The following applications in the current version of CDS for Apps use the common WPF login control for authenticating users while signing in to CDS for Apps from the client application:  
  
- Unified Service Desk. More information: [Extend Unified Service Desk](/dynamics365/customer-engagement/unified-service-desk/extend-unified-service-desk)

<!-- TODO: fix links when files added to admin guide

- Package Deployer tool. More information: [Deploy packages using Dynamics 365 Package Deployer and Windows PowerShell](../../administrator/deploy-packages-using-package-deployer-windows-powershell.md)   

- Configuration Migration tool. More information [Manage your configuration data](../../administrator/manage-configuration-data.md)  

-->
  
### See also

[Sample: Quick start for XRM Tooling API](sample-quick-start-xrm-tooling-api.md)<br />
<!-- TODO:
[Use the CDS for Apps Organization service](use-microsoft-dynamics-365-organization-service.md)<br />
[Discover the URL for Your Organization With IDiscoveryService Web Service](org-service/discover-url-organization-organization-service.md)<br />
[Write Applications and Server Extensions](extend-dynamics-365-server.md)<br /> -->
[Blog: PowerShell module for performing data operations and manipulating user and system settings in CRM](http://blogs.msdn.com/b/crm/archive/2015/09/25/powershell-module-for-performing-data-operations-and-manipulating-user-and-system-settings-in-crm.aspx)