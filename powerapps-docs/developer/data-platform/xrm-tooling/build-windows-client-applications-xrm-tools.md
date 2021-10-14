---
title: "Build Windows client applications using the XRM tools (Microsoft Dataverse)| Microsoft Docs"
description: "XRM tooling is a set of APIs that provides support for building Windows client applications for Microsoft Dataverse"
ms.custom: ""
ms.date: 03/27/2019
ms.reviewer: "pehecke"
ms.service: powerapps
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "get-started-article"
applies_to: 
  - "Dynamics 365 (online)"
ms.assetid: e2f22576-1705-4854-a804-a1ca232c0cfc
caps.latest.revision: 33
author: "MattB-msft"
ms.author: "nabuthuk"
manager: "kvivek"
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---
# Build Windows client applications using the XRM tools

XRM tooling is a set of APIs built on top of the Microsoft Dataverse assembly APIs (Organization service and Discovery service) that provide support for building Windows client applications for Dataverse. It provides the following capabilities:  
  
- Supports all the authentication modes to sign in to Dataverse instance.  
- Provides PowerShell support for authentication and connection to Dataverse instance.  
- Provides thread safety for actions performed in Dataverse in a multithreaded environment. More information [Multithreading in Components](/previous-versions/3es4b6yy(v=vs.140)), [Thread-Safe Components](/previous-versions/a8544e2s(v=vs.140))  
- Provides a common Windows Presentation Foundation login control for Dataverse for consistent sign-in experience to Dataverse from your Windows client applications.  
- Supports secure storage of the sign-in credentials and reuse of the stored credentials to automatically sign in to Dataverse after initial sign in.  
- Provides built-in diagnostic tracing and performance reporting of the actions performed in Dataverse, which you can configure based on your organization’s requirements.  

## Components of XRM tooling  

XRM tooling has the following three components:  
  
- **Interface for developers**: This provides the low-level interaction and wrapper methods for the Dataverse SDK assembly APIs. It is an instrumented API that provides a thread safe environment for making calls to Dataverse with built-in diagnostic capabilities to help you determine the performance of individual calls. It also provides a standard set of trace listeners for debugging support. The namespace for this component is <xref:Microsoft.Xrm.Tooling.Connector>.  
  
- **Common login control**: This is a WPF user control that provides a common user interface for the sign in experience to Dataverse. The login control provides support for all the authentication modes that are supported by Dataverse. The common login control has built-in encryption for securely storing your credentials/profile, and then reusing it at runtime to automatically sign in to Dataverse. The namespace for this component is <xref:Microsoft.Xrm.Tooling.CrmConnectControl>.  
  
- **Web resource utility**: This provides support for accessing information from the following two types of web resources in Dataverse: Image and XML. You can access an image from a Dataverse web resource and return it as WPF BitmapImage objects. Similarly, you can return an XML web resource as a string. The namespace for this component is <xref:Microsoft.Xrm.Tooling.WebResourceUtility>.  
  
## Client applications that use XRM tooling

The following applications in the current version of Dataverse use the common WPF login control for authenticating users while signing in to Dataverse from the client application:  
  
- Unified Service Desk. More information: [Extend Unified Service Desk](/dynamics365/customer-engagement/unified-service-desk/extend-unified-service-desk)

<!--Package Deployer tool. More information: [Deploy packages using Package Deployer and Windows PowerShell](../../administrator/deploy-packages-using-package-deployer-windows-powershell.md)-->   

<!--Configuration Migration tool. More information [Manage your configuration data](../../administrator/manage-configuration-data.md)-->  
  
### See also

[Sample: Quick start for XRM Tooling API](sample-quick-start-xrm-tooling-api.md)<br />
<!--[Blog: PowerShell module for performing data operations and manipulating user and system settings in Dataverse](https://blogs.msdn.com/b/crm/archive/2015/09/25/powershell-module-for-performing-data-operations-and-manipulating-user-and-system-settings-in-crm.aspx)-->



[!INCLUDE[footer-include](../../../includes/footer-banner.md)]