---
title: "Sample: Quick start for XRM Tooling API (Microsoft Dataverse)| Microsoft Docs"
description: "This code sample demonstrates how to connect to a Microsoft Dataverse environment by using the XRM Tooling APIs, and then perform basic create, update, retrieve, and delete operations on a table"
ms.date: 01/31/2023
author: MattB-msft
ms.author: mbarbour
ms.reviewer: pehecke
ms.topic: sample
applies_to:
  - "Dynamics 365 (online)"
search.audienceType:
  - developer
contributors:
  - JimDaly
  - phecke
---

# Sample: Quick start for XRM Tooling API

[!INCLUDE[cc-terminology](../includes/cc-terminology.md)]

This C# .NET code sample shows how to connect to a Microsoft Dataverse environment using the WPF based XRM Tooling login control. Next, the sample performs create, update, retrieve, and delete operations on a Dataverse table. For more information about XRM Tooling, see [Build windows client applications using the XRM tools](build-windows-client-applications-xrm-tools.md).

## Requirements

- Visual Studio 2019 or later
- Dataverse test environment and valid user logon credentials

## How to run the sample

1. Clone the [PowerApps-Samples](https://github.com/microsoft/PowerApps-Samples) repository so that you have a copy locally.
2. Open the `dataverse\Xrm Tooling\Quick start for XRM Tooling\C#\QuickStartXRMToolingWPFClient.sln` file in Visual Studio.
3. Press **F5** to compile and run the program.

You will be prompted for environment logon information.

## Demonstrates

- The sample code provides a common login control with built-in support for authentication and credential caching and reuse. For more information about the common login control see [Use the XRM Tooling common login control](use-xrm-tooling-common-login-control-client-applications.md).
- After connecting to Dataverse, the sample performs create, update, retrieve, and delete operations on an account table.
- Stores user credentials in a configuration file (`Default_QuickStartXRMToolingWPFClient.exe.config`) in the `c:\Users\`_`<username>`_`\AppData\Roaming\Microsoft\QuickStartXRMToolingWPFClient` folder when the sample is run for the first time, and thereafter prompts the user to either use the stored or specify new credentials at runtime to sign in to Dataverse.
- Generates the following log files, if any issue occurs, to aid troubleshooting:
  - Login_ErrorLog.log: To report sign-in errors. This file is available at `C:\Users\`_`<username>`_`\AppData\Roaming\Microsoft\QuickStartXRMToolingWPFClient`.
  - QuickStartXRMToolingWPFClient.log: To report operational errors. This file is available at the same location as the executable, that is in the debug folder of your Visual Studio project.

### See also

[Use the XRM Tooling common login control](use-xrm-tooling-common-login-control-client-applications.md)  
[Build Windows client applications using the XRM tools](build-windows-client-applications-xrm-tools.md)

[!INCLUDE[footer-include](../../../includes/footer-banner.md)]
