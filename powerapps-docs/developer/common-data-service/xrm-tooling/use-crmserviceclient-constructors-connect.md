---
title: "Use CrmServiceClient constructors to connect to CDS for Apps (Common Data Service for Apps)| Microsoft Docs"
description: "You can create an instance of the CrmServiceClient class, and then use one of the constructors to connect to Common Data Service for Apps"
ms.custom: ""
ms.date: 10/31/2018
ms.reviewer: ""
ms.service: "crm-online"
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
applies_to: 
  - "Dynamics 365 (online)"
ms.assetid: 74862506-a955-4846-a148-ac266f65592f
caps.latest.revision: 27
author: "MattB-msft"
ms.author: "kvivek"
manager: "kvivek"
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---
# Use CrmServiceClient constructors to connect to CDS for Apps

To connect to CDS for Apps, you create an instance of the <xref:Microsoft.Xrm.Tooling.Connector.CrmServiceClient> class, and then use one of the constructors to connect. All the calls to CDS for Apps using the <xref:Microsoft.Xrm.Tooling.Connector.CrmServiceClient> class are thread safe.  
  
Apart from the constructors mentioned in this topic, you can also use connection strings with <xref:Microsoft.Xrm.Tooling.Connector.CrmServiceClient> to connect to CDS for Apps. More information: [Use connection strings in XRM tooling to connect to CDS for Apps](use-connection-strings-xrm-tooling-connect.md)  
  
<a name="orgServiceproxy"></a>

## Connect to CDS for Apps using OrganizationServiceProxy

 Use the following constructor to connect to CDS for Apps using the user-provided <xref:Microsoft.Xrm.Sdk.Client.OrganizationServiceProxy> instance.  
  
```csharp
CrmServiceClient crmSvc = new CrmServiceClient(<externalOrgServiceProxy>);  
```  
  
<a name="orgWebProxyClient"></a>

## Connect to CDS for Apps using OrganizationWebProxyClient

 Use the following constructor to connect to CDS for Apps using the user-provided <xref:Microsoft.Xrm.Sdk.WebServiceClient.OrganizationWebProxyClient> instance.  
  
```csharp
CrmServiceClient crmSvc = new CrmServiceClient(<externalOrgWebProxyClient>);  
```  
  
<a name="Office365"></a>

## Connect to CDS for Apps (Office 365)

 Use the following constructor to connect to your CDS for Apps instance in Office 365.  
  
```csharp  
CrmServiceClient crmSvc = new CrmServiceClient("<crmUserId>", CrmServiceClient.MakeSecureString("<crmPassword>"), "<crmRegion>", "<orgName>", useUniqueInstance:false, useSsl:false, <orgDetail>, isOffice365:false);  
```  
  
 Valid values for the `<crmRegion>` parameter are:  `NorthAmerica`, `EMEA`, `APAC`, `SouthAmerica`,  `Oceania`, `JPN`, `CAN`, `IND`, and `NorthAmerica2`. If you set this to `String.Empty`, it will search servers in all the regions for the CDS for Apps organization. For the `<orgName>` parameter, you can specify either the unique or friendly name.  
  
 The following parameters are optional:  `useUniqueInstance`, `useSsl`, and `orgDetail`.  
  
<a name="Office365oAuth"></a>

## Connect to CDS for Apps (Office 365) using OAuth
 
 Use the following constructor to use OAuth protocol to connect to your CDS for Apps instance in Office 365. The OAuth support is introduced in CDS for Apps.  
  
> [!NOTE]
>  Global Discovery now supports for all instance lookup, regional and global. For `OAuth` authentication type, the `crmRegion` parameter value global is defaultly set to `Online Region  = Don't Know`, except where special region rules are required. 
>  Germany and North America 2 are not scanned when `Online Region = Don't Know` is selected.

```csharp  
CrmServiceClient crmSvc = new CrmServiceClient("<crmUserId>", CrmServiceClient.MakeSecureString("<crmPassword>"), "<crmRegion>", "<orgName>", useUniqueInstance:false, <orgDetail>,  
                  <user>, <clientId>, <redirectUri>, <tokenCachePath>, <externalOrgWebProxyClient>, PromptBehavior.Auto);  
```  
  
 This constructor uses [Microsoft Azure Active Directory Authentication Library (ADAL)](/azure/active-directory/develop/active-directory-authentication-libraries) to authenticate users. If the user credentials (user name and password) aren’t specified, ADAL prompts the user to provide the credentials depending on the `PromptBehavior` parameter (optional) specified in the constructor. ADAL authenticates the credentials using the OAuth protocol, obtains the access and refresh tokens from Azure Active Directory, and then uses the access token to make requests to CDS for Apps.  
  
 Valid values for the `<crmRegion>` parameter are: `NorthAmerica`, `EMEA`, `APAC`, `SouthAmerica`, `Oceania`, `JPN`, `CAN`, `IND`, and `NorthAmerica2`. If you set this to **String.Empty**, it will search servers in all the regions for the CDS for Apps organization. For the `<orgName>` parameter, you can specify either the unique or friendly name.  
  
<!-- No on-premises or IFD enabled for this version yet
<a name="ActiveDirectory"></a>

## Connect to CDS for Apps on-premises (Active Directory)

Use the following constructor to connect to an on-premises instance with Active Directory authentication.  
  
```csharp  
CrmServiceClient crmSvc = new CrmServiceClient(new System.Net.NetworkCredential("<credential>"), authType, "<hostName>", "<port>", "<orgName>", useUniqueInstance:false, useSsl:false, <orgDetail>);  
  
```  
  
 This will run an Active Directory authentication based on the specified domain. For the `<hostName>` parameter, specify the host name of your CDS for Apps server, for example: `cdstest`. For the `<orgName>` parameter, you can specify either the unique or friendly name.  
The following parameters are optional: `useUniqueInstance`, `useSsl`, and `orgDetail`.  
  
<a name="IFD"></a> 
  
## Connect to CDS for Apps Internet-facing deployment (IFD) 
 
 Use the following constructor to connect to a CDS for Apps IFD instance.  
  
```csharp
CrmServiceClient crmSvc = new CrmServiceClient(new System.Net.NetworkCredential("<credential>"), authType, "<hostName>", "<port>", "<orgName>", useUniqueInstance:false, useSsl:false, <orgDetail>);  
  
```  
  
 This will run a claims-based authentication based on the specified local domain. This is useful for customers that use AD FS, and have configured their CDS for Apps server as claims, where the user population lives in the same AD FS domain as the CDS for Apps server. For the `<hostName>` parameter, specify the host name of your CDS for Apps server, for example, `cdstest`. For the `<orgName>` parameter, you can specify either the unique or friendly name.  
  
 The following parameters are optional: `useUniqueInstance`,  `useSsl`, and `orgDetail`.  
  
<a name="OPoAuth"></a> 

## Connect to CDS for Apps Internet-facing deployment (IFD) using OAuth

 Use the following constructor to use the OAuth protocol in Active Directory Federation Services (AD FS) in Windows Server 2012 R2 to connect to a CDS for Apps IFD instance. For this constructor to work, the computer where CDS for Apps is installed must have been configured to use AD FS 2.2 as the security token service (STS).  
  
```csharp
CrmServiceClient crmSvc = new CrmServiceClient("<crmUserId>", CrmServiceClient.MakeSecureString("<crmPassword>"), "<domain>","<homeRealm>", "<hostName>", "<port>", "<orgName>", useSsl, useUniqueInstance,   
                        <orgDetail>, <user>, <clientId>, <redirectUri>, <tokenCachePath>, externalOrgWebProxyClient, PromptBehavior.Auto);  
  
```  
 The `clientId` and `redirectUri` values for the application supporting OAuth should be registered in the IFD server.  
  
 If the user credentials (user name and password) aren’t specified, ADAL prompts the user to provide the credentials depending on the `PromptBehavior` parameter (optional) specified in the constructor. ADAL authenticates the user using the security token from AD FS, and uses the token to perform actions in CDS for Apps.  
  
<a name="ClaimsBased"></a>
   
## Connect to CDS for Apps (claims-based)
  
 Use the following constructor to use claims-based authentication.  
  
```  
CrmServiceClient crmSvc = new CrmServiceClient(new System.Net.NetworkCredential("<UserId>", "<password>", “<domain>”, "<homeRealm>"),"<hostName>", "<port>", "<orgName>");    
```  
  
 This will run a claims-based authentication against the specified Home realm. This is useful for customers that use AD FS, and have configured their CDS for Apps server as claims, where the user population lives in the same AD FS domain as the CDS for Apps server. For the `<hostName>` parameter, specify the host name of your CDS for Apps server, for example, `cdstest`. For the `<orgName>` parameter, you can specify either the unique or friendly name.  
   -->
  
 ## Connect to Dynamics 365 (online) using Certificate based authentication
 Use the following constructor to use certificate based authentication.
 
 ```csharp
 CrmServiceClient CrmSvc = new CrmServiceClient("<certificate>", "<certificateStoreName>", "<certificateThumbPrint>", "<instanceUrl>", <useUniqueInstance>, <orgDetail>, <clientId>, <redirectUri>, <tokenCachePath>);
 ```
 This will run the certificate based authentication. The `clientId` and `redirectUri` values for the application are supplied when you register an app in **Azure Portal**. 
 
 The following parameters are optional: `useUniqueInstance`,  `useSsl`, and `orgDetail`.
 
<a name="Determine"></a>

## Determine your connection status
 
 To determine if the connection request was successful, check the value of the <xref:Microsoft.Xrm.Tooling.Connector.CrmServiceClient>.<xref:Microsoft.Xrm.Tooling.Connector.CrmServiceClient.IsReady> property. If **true**, the connection is successful, and you are ready to work. Otherwise, check the values of the <xref:Microsoft.Xrm.Tooling.Connector.CrmServiceClient>. <xref:Microsoft.Xrm.Tooling.Connector.CrmServiceClient.LastCrmError> and <xref:Microsoft.Xrm.Tooling.Connector.CrmServiceClient>.<xref:Microsoft.Xrm.Tooling.Connector.CrmServiceClient.LastCrmException> properties for the cause of the connection failure.  
  
### See also

[Use connection strings in XRM tooling to connect to CDS for Apps](use-connection-strings-xrm-tooling-connect.md)<br />
[Use XRM Tooling Windows PowerShell Cmdlets to connect to CDS for Apps](use-powershell-cmdlets-xrm-tooling-connect.md)<br />
[Use XRM Tooling API to execute actions in CDS for Apps](use-xrm-tooling-execute-actions.md)
<xref:Microsoft.Xrm.Tooling.Connector.AuthenticationType><br />
[Build windows client applications using the XRM tools](build-windows-client-applications-xrm-tools.md)
<!-- TODO:[Sample: Quick Start for CDS for Apps](../sample-quick-start.md)-->

