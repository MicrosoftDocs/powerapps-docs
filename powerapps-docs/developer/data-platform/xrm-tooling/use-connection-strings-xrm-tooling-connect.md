---
title: "Use XRM Tooling Connection Strings for Dataverse"
description: "Learn how to use XRM tooling connection strings in an app configuration to connect to Dataverse securely."
ms.date: 03/31/2026
author: MattB-msft
ms.author: mbarbour
ms.reviewer: pehecke
ms.topic: how-to
search.audienceType: 
  - developer
contributors: 
  - JimDaly
  - phecke
---
# Use connection strings in XRM tooling to connect to Microsoft Dataverse

XRM tooling enables you to connect to your Dataverse environment by using connection strings. This approach is similar to the concept of connection strings used with **SQL Server**. Configuration files natively support connection strings, including the ability to encrypt the configuration sections for maximum security. This feature enables you to configure Dataverse connections at deployment time, and not hard code them in your application.

Read the following important information about using a connection string in application code.
[!INCLUDE [cc-connection-string](../includes/cc-connection-string.md)]

<a name="Create"></a>

## Create a connection string

 Specify the connection string in the `app.config` or `web.config` file for your project, as shown in the following example.  
  
```xml  
<connectionStrings>  
    <add name="MyCDSServer" connectionString="AuthType=OAuth;Username=jsmith@contoso.onmicrosoft.com;Password=passcode;Url=https://contosotest.crm.dynamics.com;AppId=51f81489-12ee-4a9e-aaae-a2591f45987d;RedirectUri=app://58145B91-0C36-4500-8554-080854F2AC97;TokenCacheStorePath=c:\MyTokenCache;LoginPrompt=Auto"/>
</connectionStrings>  
```  
  
> [!IMPORTANT]
> If you add any sensitive information to the `app.config` or `web.config file`, such as an account password, take appropriate security precautions to protect the information.  
  
 After creating the connection string, use it to create a <xref:Microsoft.Xrm.Tooling.Connector.CrmServiceClient> object.  
  
```csharp  
//Use the connection string named "MyCDSServer"  
//from the configuration file  
CrmServiceClient svc = new CrmServiceClient(ConnectionString);  
```

Alternatively, you can use the <xref:Microsoft.PowerPlatform.Dataverse.Client.ServiceClient> class.

```csharp
ServiceClient svc = new ServiceClient(ConnectionString);  
```
  
> [!NOTE]
> To access the connection string in your code, include the following `using` directive to reference the `System.Configuration` namespace: `using System.Configuration;`  
  
 After creating a service client object, use the object to perform actions in Dataverse. For more information, see [Use XRM Tooling to execute actions in Dataverse](use-xrm-tooling-execute-actions.md).  
  
<a name="Parameters"></a>

## Connection string parameters

 The connection string contains a series of name=value pairs separated by semicolons. The following table lists supported parameters, which you can enter in any order.  
  
|Parameter name|Description|  
|--------------------|-----------------|  
|`ServiceUri`, `Service Uri`, `Url`, or `Server`|Specifies the URL to the Dataverse environment. The URL can use http or https protocol, and the port is optional. The default port is 80 for the http protocol and 443 for the https protocol. The server URL is typically in the format `https://`*`<organization-name>`*`.crm.dynamics.com`<br /><br /> The organization-name is required.|
|`UserName`, `User Name`, `UserId`, or `User Id`|Specifies the user's identification name associated with the credentials.|  
|`Password`|Specifies the password for the user name associated with the credentials.|  
|`HomeRealmUri` or `Home Realm Uri`|Specifies the Home Realm Uri.|  
|`AuthenticationType` or `AuthType`|Specifies the authentication type to connect to Dataverse environment. Valid values are: `AD`, `IFD` (AD FS enabled), `OAuth`, `Certificate`, `ClientSecret`, or `Office365`. However,  only `OAuth`, `Certificate`, `ClientSecret`, and `Office365` are permitted values for Dataverse environments.<br/><br/>**NOTE**: `Office365` authentication type is deprecated, and we recommend using `OAuth` as the preferred authentication type. For more information, see [What should I do to fix my application code if affected?](/powerapps/developer/data-platform/authenticate-office365-deprecation#what-should-i-do-to-fix-my-application-code-if-affected)|  
|`RequireNewInstance`|Specifies whether to reuse an existing connection if recalled while the connection is still active. If set to `true`, the system creates a unique connection. If set to `false`, the existing connection can be reused.|  
|`ClientId`, `AppId` or `ApplicationId`|Specifies the `ClientID` assigned when you registered your application in Microsoft Entra ID or Active Directory Federation Services (AD FS).|
|`ClientSecret` or `Secret` |Required when Auth Type is set to `ClientSecret`. Client Secret string to use for authentication.|
|`RedirectUri` or `ReplyUrl`|Specifies the redirect URI of the application you registered in Microsoft Entra ID or Active Directory Federation Services (AD FS).<br /><br /> This parameter is applicable only when the authentication type is specified as `OAuth`.|  
|`TokenCacheStorePath`|Specifies the full path to the location where the user token cache should be stored. The running process should have access to the specified path. It's the process's responsibility to set and configure this path.<br /><br /> This parameter is applicable only when the authentication type is specified as `OAuth`.|  
|`LoginPrompt`|Specifies whether the user is prompted for credentials if the credentials aren't supplied. Valid values are:<br /><br /> -   `Always`: Always prompts the user to specify credentials.<br />-   `Auto`: Allows the user to select in the login control interface whether to display the prompt or not.<br />-   `Never`: Doesn't prompt the user to specify credentials. If using a connection method that doesn't have a user interface, use this value.<br /><br /> This parameter is applicable only when the authentication type is specified as `OAuth`.|  
|`StoreName` or `CertificateStoreName`|Specifies the store name where the certificate identified by thumbprint can be found. When set, `Thumbprint` is required.|
|`Thumbprint` or `CertThumbprint`| Specifies the thumbprint of the certificate to be utilized during an S2S connection. When set, `AppID` is required and `UserID` and `Password` values are ignored.|
|`Integrated Security`|Specifies to use current Windows credentials to attempt to create a token for the instances. As of NuGet release Microsoft.CrmSdk.XrmTooling.CoreAssembly Version 9.1.0.21|

> [!NOTE]
> <b>When using the `OAuth` AuthType\AuthenticationType</b><br/>
> For development and prototyping purposes, the following AppId or ClientId and Redirect URI are provided for use in OAuth Flows.<br/>
> For production use, create an AppId or ClientId that is specific to your tenant in the Azure Management portal.<br/>
> Sample AppId or ClientId = 51f81489-12ee-4a9e-aaae-a2591f45987d<br/>
> Sample RedirectUri = app://58145B91-0C36-4500-8554-080854F2AC97<br/>

<a name="Examples"></a>

## Connection string examples

The following examples show how you can use connection strings for connecting to online deployments and authentication scenarios. For connection string examples of on-premises and IFD deployment instances, see [Use connection strings in XRM tooling to connect](/dynamics365/customerengagement/on-premises/developer/xrm-tooling/use-connection-strings-xrm-tooling-connect).

### Named account using Office365  

Create a new connection to Dataverse using a UserName or Password via Office365.

> [!NOTE]
> This `AuthType` is deprecated. Use `OAuth` as the preferred authentication type. For more information, see [Authenticate using Office365](/power-platform/important-changes-coming#deprecation-of-office365-authentication-type-and-organizationserviceproxy-class-for-connecting-to-dataverse).

```xml
<add name="MyCDSServer" 
 connectionString="
  AuthType=Office365;
  Username=jsmith@contoso.onmicrosoft.com; 
  Password=passcode;
  Url=https://contoso.crm.dynamics.com"/>  
```  
  
### OAuth using named account in Microsoft 365 with UX to prompt for authentication  

Create a new connection to Dataverse using a UserID or Password via OAuth.

> [!NOTE]
> OAuth is the preferred auth type for connecting to Dataverse when using an interactive flow.  This auth type fully supports the features of Microsoft Entra ID Conditional Access and Multi-Factor authentication.

```xml
<add name="MyCDSServer"
 connectionString="
  AuthType=OAuth;
  Username=jsmith@contoso.onmicrosoft.com;
  Password=passcode;
  Url=https://contosotest.crm.dynamics.com;
  AppId=51f81489-12ee-4a9e-aaae-a2591f45987d;
  RedirectUri=app://58145B91-0C36-4500-8554-080854F2AC97;
  TokenCacheStorePath=c:\MyTokenCache;
  LoginPrompt=Auto"/>  
```  

### OAuth using current logged in user with fall back UX to prompt for authentication

Create a new connection to Dataverse using the current logged in user via OAuth.

> [!NOTE]
> OAuth is the preferred auth type for connecting to Dataverse when using an interactive flow. This auth type fully supports the features of Microsoft Entra ID Conditional Access and Multi-Factor authentication.

```xml
<add name="MyCDSServer"
 connectionString="
  AuthType=OAuth;
  Username=jsmith@contoso.onmicrosoft.com;
  Integrated Security=true;
  Url=https://contosotest.crm.dynamics.com;
  AppId=51f81489-12ee-4a9e-aaae-a2591f45987d;
  RedirectUri=app://58145B91-0C36-4500-8554-080854F2AC97;
  TokenCacheStorePath=c:\MyTokenCache\msal_cache.data;
  LoginPrompt=Auto"/>  
```  

### Certificate based authentication

Create a new connection to Dataverse by using an application or client ID and a certificate.

```xml
<add name="MyCDSServer" 
  connectionString="
  AuthType=Certificate;
  url=https://contosotest.crm.dynamics.com;
  thumbprint={CertThumbPrintId};
  ClientId={AppId};"
  />
```

### ClientId or Client Secret based authentication

Create a new connection to Dataverse by using an application or client ID and a client secret.

```xml
<add name="MyCDSServer" 
  connectionString="
  AuthType=ClientSecret;
  url=https://contosotest.crm.dynamics.com;
  ClientId={AppId};
  ClientSecret={ClientSecret}"
  />
```

<a name="ConnectionStatus"></a>

## Determine your connection status

 To determine if the connection request was successful, check the value of the <xref:Microsoft.Xrm.Tooling.Connector.CrmServiceClient>.<xref:Microsoft.Xrm.Tooling.Connector.CrmServiceClient.IsReady> property. If **true**, the connection is successful, and you're ready to work. Otherwise, check the values of the <xref:Microsoft.Xrm.Tooling.Connector.CrmServiceClient>.<xref:Microsoft.Xrm.Tooling.Connector.CrmServiceClient.LastCrmError> and <xref:Microsoft.Xrm.Tooling.Connector.CrmServiceClient>.<xref:Microsoft.Xrm.Tooling.Connector.CrmServiceClient.LastCrmException> properties for the cause of the connection failure.  
  
### See also

[Build Windows client applications using the XRM tools](build-windows-client-applications-xrm-tools.md)<br />
[Use CrmServiceClient constructors to connect to Dataverse](use-crmserviceclient-constructors-connect.md)<br />
[Use XRM Tooling to execute actions in Dataverse](use-xrm-tooling-execute-actions.md)<br />
<xref:Microsoft.Xrm.Tooling.Connector.CrmServiceClient>

[!INCLUDE[footer-include](../../../includes/footer-banner.md)]
