---
title: "Use connection strings in XRM tooling to connect to Common Data Service for Apps (Common Data Service for Apps)| Microsoft Docs"
description: "XRM tooling enables you to connect to your Common Data Service for Apps environment by using connection strings"
ms.custom: ""
ms.date: 06/16/2018
ms.reviewer: ""
ms.service: "crm-online"
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
applies_to: 
  - "Dynamics 365 (online)"
ms.assetid: a98b2fce-df49-4b60-91f4-a4446aa61cd3
caps.latest.revision: 21
author: "MattB-msft"
ms.author: "kvivek"
manager: "kvivek"
---
# Use connection strings in XRM tooling to connect to Common Data Service for Apps

With CDS for Apps, XRM tooling enables you to connect to your CDS for Apps environment by using connection strings. This is similar to the concept of connection strings used with SQL Server. Connection strings have native support in configuration files, including the ability to encrypt the configuration sections for maximum security. This enables you to configure CDS for Apps connections at deployment time, and not hard code in your application to connect to your CDS for Apps environment.  
  
<a name="Create"></a> 

## Create a connection string

 You specify the connection string in the app.config or web.config file for your project, as shown in the following example.  
  
```xml  
<connectionStrings>  
    <add name="MyCDSServer" connectionString="AuthType=AD;Url=http://contoso:8080/Test;" />  
</connectionStrings>  
```  
  
> [!IMPORTANT]
>  If you add any sensitive information to the app.config or web.config file, for example an account password, be sure to take appropriate security precautions to protect the information.  
  
 After creating the connection string, you use it to create a <xref:Microsoft.Xrm.Tooling.Connector.CrmServiceClient> object.  
  
```csharp  
//Use the connection string named "MyCDSServer"  
//from the configuration file  
CrmServiceClient crmSvc = new CrmServiceClient(ConfigurationManager.ConnectionStrings["MyCDSServer"].ConnectionString);  
```  
  
> [!NOTE]
>  You’ll have to use the following `using` directive in your code to reference the `System.Configuration` namespace to access the connection string in your code: `using System.Configuration;`  
  
 After creating a <xref:Microsoft.Xrm.Tooling.Connector.CrmServiceClient> object, you can use the object to perform actions in CDS for Apps. More information: [Use XRM Tooling to execute actions in CDS for Apps](use-xrm-tooling-execute-actions.md)  
  
<a name="Parameters"></a>

## Connection string parameters

 The connection string contains a series of name=value pair separated by semi colons. The following table lists supported parameters, which can be entered in any order.  
  
|Parameter name|Description|  
|--------------------|-----------------|  
|ServiceUri, Service Uri, Url, or Server|Specifies the URL to the CDS for Apps environment. The URL can use http or https protocol, and the port is optional. The default port is 80 for the http protocol and 443 for the https protocol. The server URL is typically in the format `https://`*`<organization-name>`*`.crm.dynamics.com`<br /><br /> The organization-name is required.|  
|Domain|Specifies the domain that will verify user credentials.|  
|UserName, User Name, UserId, or User Id|Specifies the user's identification name associated with the credentials.|  
|Password|Specifies the password for the user name associated with the credentials.|  
|HomeRealmUri or Home Realm Uri|Specifies the Home Realm Uri.|  
|AuthenticationType or AuthType|Specifies the authentication type to connect to CDS for Apps environment. Valid values are: `AD`, `IFD` (AD FS enabled), `OAuth`, or `Office365`.<br /><br /> -   `AD` and `IFD` are permitted for CDS for Apps on-premises environments only.<br />-   `OAuth` is permitted for CDS for Apps and on-premises environments.<br />-   `Office365` is permitted for CDS for Apps environments only.|  
|RequireNewenvironment|Specifies whether to reuse an existing connection if recalled while the connection is still active. Default value is `false` that indicates the existing connection be reused. If set to `true`, will force the system to create a unique connection.|  
|ClientId, AppId or ApplicationId|Specifies the `ClientID` assigned when you registered your application in Azure Active Directory or Active Directory Federation Services (AD FS).<br /><br /> This parameter is applicable only when the authentication type is specified as `OAuth`.|  
|RedirectUri or ReplyUrl|Specifies the redirect URI of the application you registered in Azure Active Directory or Active Directory Federation Services (AD FS).<br /><br /> This parameter is applicable only when the authentication type is specified as `OAuth`.|  
|TokenCacheStorePath|Specifies the full path to the location where the user token cache should be stored. The running process should have access to the specified path. It is the processes responsibility to set and configure this path.<br /><br /> This parameter is applicable only when the authentication type is specified as `OAuth`.|  
|LoginPrompt|Specifies whether the user is prompted for credentials if the credentials are not supplied. Valid values are:<br /><br /> -   `Always`: Always prompts the user to specify credentials.<br />-   `Auto`: Allows the user to select in the login control interface whether to display the prompt or not.<br />-   `Never`: Does not prompt the user to specify credentials. If using a connection method does not have a user interface, you should use this value.<br /><br /> This parameter is applicable only when the authentication type is specified as `OAuth`.|  
|CertStoreName|Specifies the name of the location on the machine where certificate with thumbprint passed is located. This parameter is applicable only when the authentication type is specified as `Certificate`.|
|CertThumbPrint| Specifies the thumbprint of the certificate to use. This parameter is applicable only when the authentication type is specified as `Certificate`.|
|SkipDiscovery|If the parameter is set to true, the Service Uri should be used directly.| 
  
<a name="Examples"></a>

## Connection string examples
 
The following examples show how you can use connection strings for connecting to different deployments and authentication scenarios.  

<!-- TODO: Get rid of on-premises examples & settings? or just comment them out? -->

<!-- ### Integrated on-premises authentication  
  
```xml
<add name="MyCRMServer" connectionString="AuthType=AD;Url=http://contoso:8080/Test;" />  
```  
  
### Named account using on-premises authentication  
  
```xml  
<add name="MyCRMServer" connectionString="AuthType=AD;Url=http://contoso:8080/Test; Domain=CONTOSO; Username=jsmith; Password=passcode" />  
```  
   -->
### Named account using Office 365  
  
```xml
<add name="MyCDSServer" 
 connectionString="
  AuthType=Office365;
  Username=jsmith@contoso.onmicrosoft.com; 
  Password=passcode;
  Url=https://contoso.crm.dynamics.com"/>  
```  
  
### OAuth using named account in Office 365 with UX to prompt for authentication  
  
```xml
<add name="MyCDSServer"
 connectionString="
  AuthType=OAuth;
  Username=jsmith@contoso.onmicrosoft.com;
  Password=passcode;
  Url=https://contosotest.crm.dynamics.com;
  AppId=<GUID>;
  RedirectUri =app://<GUID>;
  TokenCacheStorePath =c:\MyTokenCache;
  LoginPrompt=Auto"/>  
```  
  
<!-- ### OAuth using named account in CDS for Apps on-premises with UX to prompt for authentication  
  
```xml
<add name="MyCRMServer" connectionString="AuthType=OAuth;Username=jsmith@contoso.onmicrosoft.com; Password=passcode;Url=https://contoso:8080/Test;AppId=<GUID>;RedirectUri=app://<GUID>;TokenCacheStorePath =c:\MyTokenCache;LoginPrompt=Auto"/>  
```  
  
### IFD using a named account with delegation to a sub realm  
  
```xml
<add name="MyCRMServer" connectionString="AuthType=IFD;Url=http://contoso:8080/Test; HomeRealmUri=https://server-1.server.com/adfs/services/trust/mex/;Domain=CONTOSO; Username=jsmith; Password=passcode" />  
```   -->
  
<a name="ConnectionStatus"></a>

## Determine your connection status

 To determine if the connection request was successful, check the value of the <xref:Microsoft.Xrm.Tooling.Connector.CrmServiceClient>.<xref:Microsoft.Xrm.Tooling.Connector.CrmServiceClient.IsReady> property. If **true**, the connection is successful, and you are ready to work. Otherwise, check the values of the <xref:Microsoft.Xrm.Tooling.Connector.CrmServiceClient>.<xref:Microsoft.Xrm.Tooling.Connector.CrmServiceClient.LastCrmError> and <xref:Microsoft.Xrm.Tooling.Connector.CrmServiceClient>.<xref:Microsoft.Xrm.Tooling.Connector.CrmServiceClient.LastCrmException> properties for the cause of the connection failure.  
  
### See also

[Build Windows client applications using the XRM tools](build-windows-client-applications-xrm-tools.md)<br />
[Use CrmServiceClient constructors to connect to CDS for Apps](use-crmserviceclient-constructors-connect.md)<br />
[Use XRM Tooling to execute actions in CDS for Apps](use-xrm-tooling-execute-actions.md)<br />
<xref:Microsoft.Xrm.Tooling.Connector.CrmServiceClient>
