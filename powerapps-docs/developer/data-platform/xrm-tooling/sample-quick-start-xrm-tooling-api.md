---
title: "Sample: Quick start for XRM Tooling API (Microsoft Dataverse)| Microsoft Docs"
description: "This code sample demonstrates how to connect to a Microsoft Dataverse environment by using the XRM Tooling APIs, and then perform basic create, update, retrieve, and delete operations on a table"
ms.custom: ""
ms.date: 04/12/2021
ms.reviewer: "pehecke"
ms.service: powerapps
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "samples"
applies_to: 
  - "Dynamics 365 (online)"
ms.assetid: 060d45bb-b7fd-48bd-ab8f-629c1b8bc1dc
caps.latest.revision: 20
author: "MattB-msft"
ms.author: "nabuthuk"
manager: "kvivek"
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---
# Sample: Quick start for XRM Tooling API

[!INCLUDE[cc-terminology](../includes/cc-terminology.md)]

The QuickStart sample is a .NET Framework managed code sample that shows how to connect to a Microsoft Dataverse instance by using the XRM Tooling APIs, and perform basic create, update, retrieve, and delete operations on a table. For more information about XRM Tooling, see [Build windows client applications using the XRM tools](build-windows-client-applications-xrm-tools.md).

Download the sample: [Work with XRM Tooling API](https://github.com/microsoft/PowerApps-Samples/tree/master/cds/Xrm%20Tooling/Quick%20start%20for%20XRM%20Tooling%20API)

## How to run the sample

1. Download and extract the sample so that you have a copy locally.  
2. Open the `Quick start for XRM Tooling\C#\QuickStartXRMToolingWPFClient.sln`  file in Visual Studio.  
3. Press **F5** to compile and run the program.  


## Demonstrates

- The sample code is built using the **WPF Application for CRM** SDK template that provides a common login control with built-in support for authentication and credential caching and reuse. For more information about the common login control and how to use the SDK template in Visual Studio, see [Use the XRM Tooling common login control](use-xrm-tooling-common-login-control-client-applications.md).  
- No helper code is used to establish a connection to Dataverse.  
- After connecting to Dataverse, the sample performs basic create, update, retrieve, and delete operations on an account table.  
- Stores user credentials in a configuration file (`Default_QuickStartXRMToolingWPFClient.exe.config`) in the `c:\Users\`*`<username>`*`\AppData\Roaming\Microsoft\QuickStartXRMToolingWPFClient` folder when the sample is run for the first time, and thereafter prompts the user to either use the stored or specify new credentials at runtime to sign in to Dataverse.  
- Generates the following log files, if any issue occurs, to aid troubleshooting:  
- Login_ErrorLog.log: To report sign-in errors. This file is available at `C:\Users\`*`<username>`*`\AppData\Roaming\Microsoft\QuickStartXRMToolingWPFClient`.  
- QuickStartXRMToolingWPFClient.log: To report operational errors. This file is available at the same location as the executable, that is in the debug folder of your Visual Studio project.  

### See also

[Use the XRM Tooling common login control](use-xrm-tooling-common-login-control-client-applications.md)<br />
[Build Windows client applications using the XRM tools](build-windows-client-applications-xrm-tools.md)<br />



[!INCLUDE[footer-include](../../../includes/footer-banner.md)]