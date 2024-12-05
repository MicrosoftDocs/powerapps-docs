---
title: "Sample: Simplified connection quick start (Developer Guide for Microsoft Dataverse) | MicrosoftDocs"
description: "This sample shows you how to connect to the Microsoft Dataverse web services using the CrmServiceClient and perform basic create, update, retrieve, and delete operations on a table. "
ms.date: 12/04/2024
author: MattB-msft
ms.topic: sample
ms.author: mbarbour
ms.reviewer: jdaly
applies_to:
  - Microsoft Dataverse (online)
search.audienceType:
  - developer
contributors:
  - JimDaly
  - phecke
---

# Sample: Simplified connection quick start using Microsoft Dataverse

[!INCLUDE[cc-terminology](../includes/cc-terminology.md)]

This C# .NET sample shows how to connect to the Microsoft Dataverse web service using the <xref:Microsoft.Xrm.Tooling.Connector.CrmServiceClient> class and a connection string. The sample then perform create, update, retrieve, and delete operations on a Dataverse table. For more information about the <xref:Microsoft.Xrm.Tooling.Connector.CrmServiceClient> see [Use CrmServiceClient constructors to connect to Dataverse](use-crmserviceclient-constructors-connect.md).

> [!NOTE]
> You could also use the <xref:Microsoft.PowerPlatform.Dataverse.Client.ServiceClient> instead of the <xref:Microsoft.Xrm.Tooling.Connector.CrmServiceClient> class in this sample.

## Requirements

- Visual Studio 2019 or later
- Dataverse test environment and valid user logon credentials

## How to run the sample

1. Clone the [PowerApps-Samples](https://github.com/microsoft/PowerApps-Samples) repository so that you have a copy locally.
1. Open the `dataverse\Xrm Tooling\QuickStartCS\C#\QuickStartCS.sln` file in Visual Studio.
1. In **Solution Explorer**, modify the `App.config` file with connection information for your Dataverse instance before running the sample. See the example App.config below.
1. Press **F5** to compile and run the program.

## Demonstrates

This sample authenticates the user with Dataverse web services by using a connection string passed to the <xref:Microsoft.Xrm.Tooling.Connector.CrmServiceClient> class.

After obtaining a reference to the Organization web service, the sample performs create, update, retrieve, and delete operations on an `account` table. The sample also handles common exceptions.

In addition, this sample supports `OAuth` authentication and advanced connection diagnostics that is configured in the App.config file. For more information on using diagnostics, see [Configure tracing for XRM Tooling](configure-tracing-xrm-tooling.md).

## Example App.config

The following shows a sample `app.config file`. To use this, remove the comment characters “<!- -” at the beginning of the \<add name=… /> line and the “- ->” at the end on the line within the connectionStrings XML tags. Next, modify the connection string username, url, and password values as appropriate for your Dataverse test environment.

```xml
<?xml version="1.0" encoding="utf-8"?>
<configuration>
  <connectionStrings>

  <!--<add name="Connect"
  connectionString="
  AuthType=OAuth;
  Username=jsmith@contoso.onmicrosoft.com;
  Url=https://contosotest.crm.dynamics.com;
  Password=passcode;
  AppId=51f81489-12ee-4a9e-aaae-a2591f45987d;
  RedirectUri=app://58145B91-0C36-4500-8554-080854F2AC97;
  TokenCacheStorePath=d:\MyTokenCache;
  LoginPrompt=Auto"/>-->

  </connectionStrings>
</configuration>
```

Read the following important information about using a connection string in application code.
[!INCLUDE [cc-connection-string](../includes/cc-connection-string.md)]

### See als

[Use connection strings in XRM tooling to connect to Dataverse](use-connection-strings-xrm-tooling-connect.md)

[!INCLUDE[footer-include](../../../includes/footer-banner.md)]
