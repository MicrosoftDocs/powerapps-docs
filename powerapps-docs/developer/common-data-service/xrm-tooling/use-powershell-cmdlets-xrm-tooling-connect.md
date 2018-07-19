---
title: "Use PowerShell cmdlets for XRM tooling to connect to CDS for Apps (Common Data Service for Apps)| Microsoft Docs"
description: "Learn how to use Powershell cmdlets for XRM tooling like Get-CrmConnection and Get-CrmOrganizations to connect to Common Data Service for Apps and retrieve organizations that the current user has access to"
ms.custom: ""
ms.date: 06/16/2018
ms.reviewer: ""
ms.service: "crm-online"
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "get-started-article"
applies_to: 
  - "Dynamics 365 (online)"
ms.assetid: 81816457-c963-46ca-b350-615fa75f56a7
caps.latest.revision: 27
author: "ashvarma"
ms.author: "kvivek"
manager: "kvivek"
---
# Use PowerShell cmdlets for XRM tooling to connect to CDS for Apps

XRM tooling provides you with the following Windows PowerShell cmdlets that you can use to connect to CDS for Apps and retrieve organizations that the current user has access to: `Get-CrmConnection` and `Get-CrmOrganizations`.  
  
<a name="Prereq"></a>   

## Prerequisites  
  
-   To use the XRM tooling cmdlets, you need PowerShell version 3.0 or later. To check the version, open a PowerShell window and run the following command: `$Host`  
  
-   Set the execution policy to run the signed PowerShell scripts. To do so, open a PowerShell window as an administrator and run the following command: `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned`  
  
<a name="register"></a>   

## Register the cmdlets  

 Before you can use the PowerShell cmdlets, you have to register them. The XRM tooling PowerShell cmdlets are available as a NuGet package here: [https://www.nuget.org/packages/Microsoft.CrmSdk.XrmTooling.CrmConnector.PowerShell](https://www.nuget.org/packages/Microsoft.CrmSdk.XrmTooling.CrmConnector.PowerShell/). To download and register the cmdlets: 
  
1. Open notepad, and copy the following script:

    ```powershell
    @PowerShell.exe -ExecutionPolicy RemoteSigned -Command "Invoke-Expression -Command ((Get-Content -Path '%~f0' | Select-Object -Skip 2) -join [environment]::NewLine)"
    @exit /b %Errorlevel%
    $currentFolder = Get-Location
    cd $currentFolder
    $sourceNugetExe = "https://dist.nuget.org/win-x86-commandline/latest/nuget.exe"
    $targetNugetExe = ".\nuget.exe"
    Remove-Item .\Tools -Force -Recurse -ErrorAction Ignore
    Invoke-WebRequest $sourceNugetExe -OutFile $targetNugetExe
    Set-Alias nuget $targetNugetExe -Scope Global -Verbose

    ##
    ##Specify the NuGet package source
    ##
    $nugetPackageSource = "https://api.nuget.org/v3/index.json"

    ##
    ##Download XRM Tooling PowerShell cmdlets
    ##
    ./nuget install -source $nugetPackageSource Microsoft.CrmSdk.XrmTooling.CrmConnector.PowerShell -O .\Tools
    md .\Tools\XRMToolingPowerShell
    $cmdletFolder = Get-ChildItem ./Tools | Where-Object {$_.Name -match 'Microsoft.CrmSdk.XrmTooling.CrmConnector.PowerShell.'}
    move .\Tools\$cmdletFolder\tools\*.* .\Tools\XRMToolingPowerShell
    Remove-Item .\Tools\$cmdletFolder -Force -Recurse

    ##
    ##Remove NuGet.exe
    ##
    Remove-Item nuget.exe
  
1. Save the notepad file as batch file on your computer: **GetTools.bat**.
1. Navigate to the folder where you saved the file, for example C:\SDK, and double-click the **GetTools.bat** file to run the script. This will create a Tools\XRMToolingPowerShell folder in the same location as your **GetTools.bat** file. The Tools\XRMToolingPowerShell folder contains the `RegisterXRMTooling.ps1` script to register the cmdlets, and other associated files.
1. Start PowerShell on your computer with elevated privileges (run as administrator).  
  
1.  At the prompt, change your directory to the folder that contains the PowerShell script for registering the cmdlets. For example:  
  
    ```powershell  
    cd c:\SDK\Tools\XRMToolingPowerShell  
    ```  
  
1.  Run the `RegisterXRMTooling.ps1` script to register the XRM tooling PowerShell cmdlets. Type the following command, and press ENTER:  
  
    ```powershell
    .\RegisterXRMTooling.ps1  
    ```
  
 You’re now ready to use these PowerShell cmdlets. To list the cmdlets that you registered, run the following command in the PowerShell window:  
  
```powershell
Get-Help “Crm”  
```  
  
<a name="RetrieveOrgs"></a>   

## Use the cmdlet to retrieve organizations from CDS for Apps  

Use the `Get-CrmOrganizations` cmdlet to retrieve the organizations that you have access to.  
  
1.  Provide your credentials to connect to your CDS for Apps instance. Running the following command will prompt you to type your user name and password to connect to the CDS for Apps instance, and it will be stored in the `$Cred` variable.  
  
    ```powershell  
    $Cred = Get-Credential  
    ```  
2.  Use the following command to retrieve your organizations, and store the information in the `$CRMOrgs` variable: 

    - If you’re connecting to a CDS for Apps instance:  
  
        ```powershell  
        $CRMOrgs = Get-CrmOrganizations -Credential $Cred -DeploymentRegion NorthAmerica –OnlineType Office365  
        ```  
  
        > [!NOTE]
        >  For the `DeploymentRegion` parameter, valid values are `NorthAmerica`, `EMEA`, `APAC`, `SouthAmerica`, `Oceania`, `JPN`, `CAN`, `IND`, and `NorthAmerica2`. For the `OnlineType` parameter, specify `Office365`.
<!--   
    -   If you’re connecting to the on-premises server:  
  
        ```powershell  
        $CRMOrgs = Get-CrmOrganizations –ServerUrl http://<CRM_Server_Host> –Credential $Cred  
        ```      
  
    -   If you’re connecting to the CDS for Apps server using the claims-based authentication against the specified Home realm:  
  
        ```powershell  
        $CRMOrgs = Get-CrmOrganizations –ServerUrl http://<CRM_Server_Host> –Credential $Cred –HomRealmURL http://<Identity_Provider_Address>  
        ```   -->
  
3.  Your supplied credentials are validated when you run the command in step 2. On successful execution of the command, type the following command, and press ENTER to display the organizations that you have access to:  
  
    ```powershell  
    $CRMOrgs  
    ```  
  
    <!-- TODO:
     ![CDS for Apps organization information](../media/xrmtooling-powershell-1.png)   -->
  
    > [!TIP]
    >  You can use the variable that was used to store the retrieved CDS for Apps organizations (in this case `$CRMOrgs`) with the `Get-CrmConnection` cmdlet to connect to CDS for Apps. To specify the org name, use the following command: `$CRMOrgs.UniqueName`.  
    >   
    >  If there is more than one organization value stored in the `$CRMOrgs` variable, you can refer to the `nth` organization using the following command: `$CRMOrgs[n-1]`. For example, to refer to the unique name of the second organization in the `$CRMOrgs` variable, use the following command: `$CRMOrgs[1].UniqueName`. More information: [Accessing Values in an Array](/previous-versions/windows/it-pro/windows-powershell-1.0/ee692791\(v=technet.10\))  
  
<a name="ConnecttoCRM"></a>
   
## Use the cmdlet to connect to CDS for Apps  

Use the `Get-CrmConnection` cmdlet to connect to a CDS for Apps instance. The cmdlet lets you either use the XRM tooling common login control to specify your credentials and connect to CDS for Apps or lets you specify your credentials as inline parameters. More information: [Use the XRM Tooling common login control](use-xrm-tooling-common-login-control-client-applications.md)

> [!IMPORTANT]
> Before using the `Get-CrmConnection` cmdlet, ensure that you use the following command to enforce usage of TLS 1.2 by PowerShell to connect to your Customer Engagement instance:<br/>
> `[System.Net.ServicePointManager]::SecurityProtocol = [System.Net.SecurityProtocolType]::Tls12`<br/>
> More information about TLS 1.2 requirement for Customer Engagement connection: [Blog Post: Updates coming to Dynamics 365 Customer Engagement connection security](https://blogs.msdn.microsoft.com/crm/2017/09/28/updates-coming-to-dynamics-365-customer-engagement-connection-security/)   
  
### Connect to CDS for Apps by using the common login control  
  
1.  If you want to use the common login control to provide your credentials to connect to CDS for Apps, use the following command. The connection information is stored in the `$CRMConn` variable so that you can use it later.  
  
    ```powershell  
    $CRMConn = Get-CrmConnection -InteractiveMode  
    ```  
  
2.  The **LoginControl** dialog box appears. Provide your credentials to connect to your CDS for Apps instance, and click **Login**.  
  
### Connect to CDS for Apps by specifying credentials inline  
  
1.  To connect to CDS for Apps, use the following commands. Note that these commands use the `$Cred` variable created earlier to store the credential while retrieving the organizations. The connection information is stored in the `$CRMConn` variable:

    <!-- -   If you’re connecting to a CDS for Apps instance:   -->
  
        ```powershell  
        $CRMConn = Get-CrmConnection -Credential $Cred -DeploymentRegion <Deployment region name> –OnlineType Office365 –OrganizationName <OrgName>  
        ```
  
        > [!NOTE]
        >  For the `DeploymentRegion` parameter, valid values are `NorthAmerica`, `EMEA`, `APAC`, `SouthAmerica`, `Oceania`, `JPN`, `CAN`, `IND` and `NorthAmerica2`. For the `OnlineType` parameter, specify `Office365`. 
  
    <!-- not available for this version at this time
     -   If you’re connecting to the on-premises server:  
  
        ```powershell  
        $CRMConn = Get-CrmConnection –ServerUrl http://<CRM_Server_Host> -Credential $Cred -OrganizationName <OrgName>  
        ```
  
    -   If you’re connecting to the CDS for Apps server using the claims-based authentication against the specified Home realm:  
  
        ```powershell  
        $CRMConn = Get-CrmConnection –ServerUrl http://<CRM_Server_Host> -Credential $Cred -OrganizationName <OrgName> –HomRealmURL http://<Identity_Provider_Address>  
        ```   -->
  
    > [!NOTE]
    > For the `OrganizationName` parameter in all the preceding commands, you can either specify the organization unique name or friendly name. You can also use the organization unique name or friendly name that you retrieved using the `Get-CrmOrganizations` cmdlet and stored in the `$CRMOrgs` variable. For example, you can use `$CRMOrgs[x].UniqueName` or `$CRMOrgs[x].FriendlyName`.  
  
2.  Your supplied credentials are validated when you run the command in step 1. On successful execution of the cmdlet, type the following command, and press ENTER to display the connection information and status:  
  
    ```powershell  
    $CRMConn  
    ```  
  
    <!--TODO:
     ![CDS for Apps connection information and status](../media/xrm-tooling-powershell-2.png "CDS for Apps connection information and status")   -->
  
### See also
  
[Use XRM Tooling API to connect to CDS for Apps](use-crmserviceclient-constructors-connect.md)<br />
[Build Windows client applications using the XRM tools](build-windows-client-applications-xrm-tools.md)<br />
[Blog: PowerShell module for performing data operations and manipulating user and system settings in CRM](http://blogs.msdn.com/b/crm/archive/2015/09/25/powershell-module-for-performing-data-operations-and-manipulating-user-and-system-settings-in-crm.aspx)