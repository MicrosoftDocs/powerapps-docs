---
title: "Download tools from NuGet (Microsoft Dataverse) | Microsoft Docs"
description: "Download the Plug-in Registration, Package Deployment, and other developer tools from NuGet.org."
ms.date: 06/24/2022
ms.reviewer: pehecke
ms.topic: article
applies_to: 
  - "Dynamics 365 (online)"
author: marcelbf # GitHub ID
ms.subservice: dataverse-developer
ms.author: marcelbf
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---

# Download tools from NuGet

[!INCLUDE[cc-terminology](includes/cc-terminology.md)]

You can download tools used in code development from NuGet using the  PowerShell script found below. These tools include:

|Tool|NuGet Package|
|-|-|
|Code Generation tool `CrmSvcUtil.exe`|[Microsoft.CrmSdk.CoreTools](https://www.nuget.org/packages/Microsoft.CrmSdk.CoreTools)|
|Configuration Migration tool `DataMigrationUtility.exe`|[Microsoft.CrmSdk.XrmTooling.ConfigurationMigration.Wpf](https://www.nuget.org/packages/Microsoft.CrmSdk.XrmTooling.ConfigurationMigration.Wpf)|
|Package Deployer `PackageDeployer.exe`|[Microsoft.CrmSdk.XrmTooling.PackageDeployment.WPF](https://www.nuget.org/packages/Microsoft.CrmSdk.XrmTooling.PackageDeployment.Wpf)|
|Plug-in Registration tool `PluginRegistration.exe` |[Microsoft.CrmSdk.XrmTooling.PluginRegistrationTool](https://www.nuget.org/packages/Microsoft.CrmSdk.XrmTooling.PluginRegistrationTool)|
|SolutionPackager tool `SolutionPackager.exe`|[Microsoft.CrmSdk.CoreTools](https://www.nuget.org/packages/Microsoft.CrmSdk.CoreTools)|

## Download tools using PowerShell

You can download all SDK tools using the PowerShell script provided below. Note that this script works with the version of Windows PowerShell that ships in Microsoft Windows 10. The script does not presently work with cross-platform versions of PowerShell based on .NET 5 or later (formerly .NET Core).

1. In your Windows Start menu, type `Windows Powershell` and open it.
1. Navigate to the folder you want to install the tools to. For example if you want to install them in a `devtools` folder on your D: drive, type `cd D:\devtools`.
1. Copy and paste the following PowerShell script into the PowerShell window and press Enter.

    ```powershell
    [Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12
    $sourceNugetExe = "https://dist.nuget.org/win-x86-commandline/latest/nuget.exe"
    $targetNugetExe = ".\nuget.exe"
    Remove-Item .\Tools -Force -Recurse -ErrorAction Ignore
    Invoke-WebRequest $sourceNugetExe -OutFile $targetNugetExe
    Set-Alias nuget $targetNugetExe -Scope Global -Verbose

    if (-not (./nuget source | Where-Object { $_ -like "*https://api.nuget.org/v3/index.json*"})) {
      .\nuget sources Add -Name nuget.org.v3 -Source  https://api.nuget.org/v3/index.json
    }

    ##
    ##Download Plug-in Registration tool
    ##
    ./nuget install Microsoft.CrmSdk.XrmTooling.PluginRegistrationTool -O .\Tools
    mkdir .\Tools\PluginRegistration
    $prtFolder = (Get-ChildItem ./Tools | Where-Object {$_.Name -match 'Microsoft.CrmSdk.XrmTooling.PluginRegistrationTool.'}).Name
    Move-Item .\Tools\$prtFolder\tools\*.* .\Tools\PluginRegistration
    Remove-Item .\Tools\$prtFolder -Force -Recurse
    
    ##
    ##Download CoreTools
    ##
    ./nuget install  Microsoft.CrmSdk.CoreTools -O .\Tools
    mkdir .\Tools\CoreTools
    $coreToolsFolder = Get-ChildItem ./Tools | Where-Object {$_.Name -match 'Microsoft.CrmSdk.CoreTools.'}
    Move-Item .\Tools\$coreToolsFolder\content\bin\coretools\*.* .\Tools\CoreTools
    Remove-Item .\Tools\$coreToolsFolder -Force -Recurse

    ##
    ##Download Configuration Migration
    ##
    ./nuget install  Microsoft.CrmSdk.XrmTooling.ConfigurationMigration.Wpf -O .\Tools
    mkdir .\Tools\ConfigurationMigration
    $configMigFolder = Get-ChildItem ./Tools | Where-Object {$_.Name -match 'Microsoft.CrmSdk.XrmTooling.ConfigurationMigration.Wpf.'}
    Move-Item .\Tools\$configMigFolder\tools\*.* .\Tools\ConfigurationMigration
    Remove-Item .\Tools\$configMigFolder -Force -Recurse
    
    ##
    ##Download Package Deployer 
    ##
    ./nuget install  Microsoft.CrmSdk.XrmTooling.PackageDeployment.WPF -O .\Tools
    mkdir .\Tools\PackageDeployment
    $pdFolder = Get-ChildItem ./Tools | Where-Object {$_.Name -match 'Microsoft.CrmSdk.XrmTooling.PackageDeployment.Wpf.'}
    Move-Item .\Tools\$pdFolder\tools\*.* .\Tools\PackageDeployment
    Remove-Item .\Tools\$pdFolder -Force -Recurse

    ##
    ##Remove NuGet.exe
    ##
    Remove-Item nuget.exe    
    ```

1. You will find the tools in the following folders:

- `[Your folder]\Tools\ConfigurationMigration`
- `[Your folder]\Tools\CoreTools`
- `[Your folder]\Tools\PackageDeployment`
- `[Your folder]\Tools\PluginRegistration`

To get the latest version of these tools, repeat these steps.

## See Also

[Developer tools](developer-tools.md)<br />
[Visual Studio and the .NET Framework](org-service/visual-studio-dot-net-framework.md)<br />
[Generate early-bound classes for the Organization service](org-service/generate-early-bound-classes.md)<br />
[Create extensions for the Code Generation tool](org-service/extend-code-generation-tool.md)<br />
[Browse the metadata for your organization](browse-your-metadata.md)<br />
[Deploy packages using Package Deployer and Windows PowerShell](/power-platform/admin/deploy-packages-using-package-deployer-windows-powershell)<br />
[Register a plug-in](register-plug-in.md)<br />

[!INCLUDE[footer-include](../../includes/footer-banner.md)]
