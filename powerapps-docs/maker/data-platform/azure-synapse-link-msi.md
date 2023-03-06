---
title: Use managed identities for Azure with your Azure data lake storage
description: This article explains how to use Azure Managed identity for your Microsoft Dataverse data in Azure.
author: "JasonHQX"
ms.author: jasonhuang
ms.reviewer: matp
ms.service: powerapps
ms.topic: how-to
ms.date: 03/06/2023
ms.custom: template-how-to 
---
# Use managed identities for Azure with your Azure data lake storage (preview)

[!INCLUDE [cc-beta-prerelease-disclaimer](../../includes/cc-beta-prerelease-disclaimer.md)]

Azure Data Lake Storage provides a layered security model. This model enables you to secure and control the level of access to your storage accounts that your applications and enterprise environments demand, based on the type and subset of networks or resources used. When network rules are configured, only applications requesting data over the specified set of networks or through the specified set of Azure resources can access a storage account. You can limit access to your storage account to requests originating from specified IP addresses, IP ranges, subnets in an Azure Virtual Network (VNet), or resource instances of some Azure services.

Managed identities for Azure, formerly know as Managed service Identity (MSI), help with the management of secrets. Microsoft Dataverse customers using Azure capabilities create a managed identity (part of Enterprise Policy creation) which can be used for one or more Dataverse environments. This managed identity that will be provisioned in the your tenant is then used by Dataverse to access your Azure data lake.

With managed identities, access to your storage account is restricted to requests originating from the Dataverse environment associated with your tenant. When Dataverse connects to storage on behalf of you, it includes additional context information to prove that the request originates from a secure, trusted environment. This allows storage to grant Dataverse access to your storage account. Managed identities are used to sign the context information in order to establish trust. This adds application-level security in addition to the network and infrastructure security provided by Azure for connections between Azure services.

> [!IMPORTANT]
> This is a preview feature.
> Environment Lifecycle Operations listed below will not be available if this preview feature is enabled:
>
> - Recover environment
> - Reset environment
> - Reset environment
> - Copy environment
> - Back up and restore environment

## Prerequisites

- Power platform administrator or Dynamics 365 administrator role to manage environments on the Power Platform admin center.
- Azure CLI is required on your local machine. [Download and install](https://aka.ms/InstallAzureCliWindows)
- Install these two Powershell Packages:
  - Install-Module Az
  - Install-Module -Name Microsoft.PowerApps.Administration.PowerShell
- These three PowerShell scripts must be in the same folder:
  - CreateIdentityEnterprisePolicy.ps1
  - NewIdentity.ps1
  - GetIdentityEnterprisePolicyforEnvironment.ps1
- We recommend that you create a new storage container under the same Azure resource group to onboard this feature.

## Create Enterprise policy

1. Obtain your Azure **Subscription ID**, **Location**, and **Resource group** name, from the overview page for the Azure resource group.
1. Open Azure CLI with run as administrator and sign into your Azure subscription use command az login  <!-- What's this? -->
1. (Optional) if you have multiple Azure subscriptions, make sure to run `Update-AzConfig -DefaultSubscriptionForLogin { Azure subscription id }` to update your default subscription.
1. To enable the enterprise policy for the selected Azure subscription, run the PowerShell Script **./SetupSubscriptionForPowerPlatform.ps1**.
   1. Provide the Azure subscription ID.
1. Create the enterprise policy. Run PowerShell script `./CreateIdentityEnterprisePolicy.ps1`

   - Provide the Azure subscription ID.
   - Provide the Azure Resource Group name.
   - Provide preferred enterprise policy name.
   - Provide the Azure resource group location.
1. Save the copy of the **ResourceId** after policy creation.

## Grant Reader access to the enterprise policy via Azure IAM/RBAC

Azure global admins, Dynamics 365 admins,and Power Platform admins can access the Power Platform admin center to assign environments to the enterprise policy. To access the enterprise policies, the global or Azure Key vault admin is required to grant the **Reader role** to the Dynamics 365 or Power Platform admin. Once the Reader role is granted, the Dynamics 365 or Power Platform admins will see the enterprise policies on the Power Platform admin center.

Only the Dynamics 365 and Power Platform admins who were granted the Reader role to the enterprise policy can ‘add environment’ to the policy. Other Dynamics 365 and PowerPlatform admins might be able to view the enterprise policy, but they will get an error when they try to add environment.

1. Sign into the [Azure portal](https://portal.azure.com/).
1. Obtain the Dynamics 365 Power Platform admin user’s **ObjectID**.
   1. Go to the **Users** area.
   1. Open the Dynamics 365 or Power Platform admin user.
   1. Under the overview page for the user, copy the **ObjectID**.
1. Obtain the Enterprise Policies id:
   1. Go to the Azure **Resource Graph Explorer**.
   1. Run this query: `resources | where type == 'microsoft.powerplatform/enterprisepolicies'`
   1. Scroll to the right of the results page and select the **See details** link.
   1. On the **Details** page, copy the ID.
1. Open Azure CLI and run the following command, replacing the {objId} with the user’s ObjectID and the {EP Resource Id} with the enterprise policy ID.
   - `New-AzRoleAssignment -ObjectId {objId} -RoleDefinitionName Reader -Scope {EP Resource Id}`

## Connect enterprise policy to Dataverse environment

1. Obtain Dataverse environment ID.
   1. Sign into to Power Platform admin center.
   1. Select **Environments**, and then open your environment. 
   1. In the **Details** section, copy the **Environment ID**.
   1. To link to the Dataverse environment run this Powershell script: `./ NewIdentity.ps1`
   1. Provide Dataverse environment ID <!-- Start here-->
   1. Provide ResourceId
   1. StatusCode = 202 shows indicates the link is created


## Next steps
<!-- Add a context sentence for the following links -->
- [Write how-to guides](contribute-how-to-write-howto.md)
- [Links](links-how-to.md)

<!--
Remove all the comments in this template before you sign-off or merge to the 
main branch.
-->
