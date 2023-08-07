---
title: Use managed identities for Azure with your Azure data lake storage
description: This article explains how to use Azure Managed identity to restrict public network access for your Microsoft Dataverse data in Azure with connected Synapse Link.
author: "JasonHQX"
ms.author: jasonhuang
ms.reviewer: matp
ms.service: powerapps
ms.topic: how-to
ms.date: 06/13/2023
ms.custom: template-how-to 
---
# Use managed identities for Azure with your Azure data lake storage

Azure Data Lake Storage provides a layered security model. This model enables you to secure and control the level of access to your storage accounts that your applications and enterprise environments demand, based on the type and subset of networks or resources used. When network rules are configured, only applications requesting data over the specified set of networks or through the specified set of Azure resources can access a storage account. You can limit access to your storage account to requests originating from specified IP addresses, IP ranges, subnets in an Azure Virtual Network (VNet), or resource instances of some Azure services.

Managed identities for Azure, formerly know as Managed Service Identity (MSI), help with the management of secrets. Microsoft Dataverse customers using Azure capabilities create a managed identity (part of enterprise policy creation) that can be used for one or more Dataverse environments. This managed identity that will be provisioned in your tenant is then used by Dataverse to access your Azure data lake.

With managed identities, access to your storage account is restricted to requests originating from the Dataverse environment associated with your tenant. When Dataverse connects to storage on behalf of you, it includes additional context information to prove that the request originates from a secure, trusted environment. This allows storage to grant Dataverse access to your storage account. Managed identities are used to sign the context information in order to establish trust. This adds application-level security in addition to the network and infrastructure security provided by Azure for connections between Azure services.

## Before you start

- Azure CLI is required on your local machine. [Download and install](https://aka.ms/InstallAzureCliWindows)
- You need these two PowerShell modules. If you don't have them, open PowerShell and run these commands:
  - Azure Az PowerShell module: `Install-Module -Name Az`
  - Power Platform admin PowerShell module: `Install-Module -Name Microsoft.PowerApps.Administration.PowerShell`
- Go to this [compressed folder file on GitHub]((https://github.com/microsoft/PowerApps-Samples/blob/master/powershell/managed-identities/Common.zip). Then select **Download** to download it. Extract the compressed folder file to a computer in a location where you can run PowerShell commands. **All files and folders extracted from a compressed folder should be preserved in their original location.**
- We recommend that you create a new storage container under the same Azure resource group to onboard this feature.

## Enable enterprise policy for the selected Azure subscription

> [!IMPORTANT]
>
> You must have **Azure subscription Owner** role access to complete this task.
> Obtain your Azure **Subscription ID** from the overview page for the Azure resource group.

1. Open Azure CLI with run as administrator and sign into your Azure subscription using the command: `az login`  More information: [Sign in with Azure CLI](/cli/azure/authenticate-azure-cli)
1. (Optional) if you have multiple Azure subscriptions, make sure to run `Update-AzConfig -DefaultSubscriptionForLogin { Azure subscription id }` to update your default subscription.
1. Expand the compressed folder you downloaded as part of the [Before you start](#before-you-start) for this feature to a location where you can run PowerShell.
1. To enable the enterprise policy for the selected Azure subscription, run the PowerShell script **./SetupSubscriptionForPowerPlatform.ps1**.
   - Provide the Azure subscription ID.

## Create enterprise policy

> [!IMPORTANT]
> You must have **Azure resource group Owner** role access to complete this task.
> Obtain your Azure **Subscription ID**, **Location**, and **Resource group** name, from the overview page for the Azure resource group.

1. Create the enterprise policy. Run PowerShell script `./CreateIdentityEnterprisePolicy.ps1`

   - Provide the Azure subscription ID.
   - Provide the Azure resource group name.
   - Provide preferred enterprise policy name.
   - Provide the Azure resource group location.
1. Save the copy of the **ResourceId** after policy creation.

> [!NOTE]
> The following are the valid **location** inputs supported for policy creation. Select the location that's most appropriate for you.

### Locations available for enterprise policy

:::row:::
   :::column span="":::
      United States EUAP
   :::column-end:::
   :::column span="":::
      United States
   :::column-end:::
   :::column span="":::
      South Africa
   :::column-end:::
   :::column span="":::
      UK
   :::column-end:::
   :::column span="":::
      Australia
   :::column-end:::
   :::column span="":::
      Korea
   :::column-end:::
:::row-end:::
:::row:::
   :::column span="":::
      Japan
   :::column-end:::
   :::column span="":::
      India
   :::column-end:::
   :::column span="":::
      France
   :::column-end:::
   :::column span="":::
      Europe
   :::column-end:::
   :::column span="":::
      Asia
   :::column-end:::
   :::column span="":::
      Norway
   :::column-end:::
:::row-end:::
:::row:::
   :::column span="":::
      Germany
   :::column-end:::
   :::column span="":::
      Switzerland
   :::column-end:::
   :::column span="":::
      Canada
   :::column-end:::
   :::column span="":::
      Brazil
   :::column-end:::
   :::column span="":::
      UAE
   :::column-end:::
   :::column span="":::
      Singapore
   :::column-end:::
:::row-end:::

## Grant reader access to the enterprise policy via Azure

Azure global admins, Dynamics 365 admins, and Power Platform admins can access the Power Platform admin center to assign environments to the enterprise policy. To access the enterprise policies, the global or Azure Key vault admin is required to grant the **Reader role** to the Dynamics 365 or Power Platform admin. Once the reader role is granted, the Dynamics 365 or Power Platform admins will see the enterprise policies on the Power Platform admin center.

Only the Dynamics 365 and Power Platform admins who were granted the reader role to the enterprise policy can ‘add environment’ to the policy. Other Dynamics 365 and PowerPlatform admins might be able to view the enterprise policy, but they'll get an error when they try to add environment.

> [!IMPORTANT]
> You must have - `Microsoft.Authorization/roleAssignments/write` permissions, such as  [User Access Administrator](/azure/role-based-access-control/built-in-roles#user-access-administrator) or [Owner](/azure/role-based-access-control/built-in-roles#owner) to complete this task.

1. Sign into the [Azure portal](https://portal.azure.com/).
1. Obtain the Dynamics 365 Power Platform admin user’s **ObjectID**.
   1. Go to the **Users** area.
   1. Open the Dynamics 365 or Power Platform admin user.
   1. Under the overview page for the user, copy the **ObjectID**.
1. Obtain the enterprise policies ID:
   1. Go to the Azure **Resource Graph Explorer**.
   1. Run this query: `resources | where type == 'microsoft.powerplatform/enterprisepolicies'`
   :::image type="content" source="media/azure-graph-enterprise-pol-id.png" alt-text="Run query from Azure Resource Graph Explorer":::
   1. Scroll to the right of the results page and select the **See details** link.
   1. On the **Details** page, copy the ID.
1. Open Azure CLI and run the following command, replacing the `<objId>` with the user’s **ObjectID** and the `<EP Resource Id>` with the enterprise policy ID.
   - `New-AzRoleAssignment -ObjectId <objId> -RoleDefinitionName Reader -Scope <EP Resource Id>`

## Connect enterprise policy to Dataverse environment

> [!IMPORTANT]
> You must have the **Power Platform administrator** or **Dynamics 365 administrator** role to complete this task.
> You must have the **Reader** role for the enterprise policy to complete this task.

1. Obtain the Dataverse environment ID.
   1. Sign into the [Power Platform admin center](https://admin.powerplatform.microsoft.com).
   1. Select **Environments**, and then open your environment.
   1. In the **Details** section, copy the **Environment ID**.
   1. To link to the Dataverse environment, run this PowerShell script: `./NewIdentity.ps1`
   1. Provide the Dataverse environment ID. 
   1. Provide the **ResourceId**. <br />
   **StatusCode = 202** indicates the link was successfully created.
1. Sign into the [Power Platform admin center](https://admin.powerplatform.microsoft.com).
1. Select **Environments**, and then open the environment you specified earlier.
1. In the **Recent operations** area, select **Full history** to validate the connection of the new identity.

## Configure network access to the Azure Data Lake Storage Gen2

> [!IMPORTANT]
> You must have an Azure Data Lake Storage Gen2 **Owner** role to complete this task.

1. Go to the [Azure portal](https://portal.azure.com/).
1. Open the storage account connected to your Azure Synapse Link for Dataverse profile.
1. On the left navigation pane, select **Networking**. Then, on the **Firewalls and virtual networks** tab select the following settings:

   1. **Enabled from selected virtual networks and IP addresses**.
   1. Under **Resource instances**, select **Allow Azure services on the trusted services list to access this storage account**
1. Select **Save**.

## Configure network access to the Azure Synapse Workspace

> [!IMPORTANT]
> You must have an Azure **Synapse administrator** role to complete this task.

1. Go to the [Azure portal](https://portal.azure.com/).
1. Open the Azure Synapse workspace connected to your Azure Synapse Link for Dataverse profile.
1. On the left navigation pane, select **Networking**.
1. Select **Allow Azure services and resources to access this workspace**.
1. If there are **IP firewall rules** created for all IP range, delete them to restrict public network access.
   :::image type="content" source="media/synapse-workspace-network-settings.png" alt-text="Azure Synapse workspace network settings":::
1. Add a new **IP firewall rule** based on the client IP address.
1. Select **Save** when done. More information: [Azure Synapse Analytics IP firewall rules](/azure/synapse-analytics/security/synapse-workspace-ip-firewall#ip-firewall-rules)

## Create Azure Synapse Link for Dataverse with managed identity

> [!IMPORTANT]
>
> Dataverse: You must have the Dataverse **system administrator** security role. Additionally, tables you want to export via Synapse Link must have the **Track changes** property enabled. More information: [Advanced options](create-edit-entities-portal.md#advanced-options)
> Azure Data Lake Storage Gen2: You must have an Azure Data Lake Storage Gen2 account and **Owner** and **Storage Blob Data Contributor** role access. Your storage account must enable **Hierarchical namespace** and **public network access** for both initial setup and delta sync. **Allow storage account key access** is required only for the initial setup.  
> Synapse workspace: You must have a Synapse workspace and the **Synapse Administrator** role access within the Synapse Studio. The Synapse workspace must be in the same region as your Azure Data Lake Storage Gen2 account with **allowAll** IP addresses access rule. The storage account must be added as a linked service within the Synapse Studio. To create a Synapse workspace, go to [Creating a Synapse workspace](/azure/synapse-analytics/get-started-create-workspace).

When you create the link, Azure Synapse Link for Dataverse gets details about the currently linked enterprise policy under the Dataverse environment then caches the identity client secret URL to connect to Azure.

1. Sign into [Power Apps](https://make.powerapps.com/?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc) and select your environment.
1. On the left navigation pane, select **Azure Synapse Link**, and then select **+ New link**. [!INCLUDE [left-navigation-pane](../../includes/left-navigation-pane.md)]
1. Select **Select Enterprise Policy with Managed Service Identity**, and then select **Next**.
1. Add the tables you want to export, and then select **Save**.

## Troubleshooting

If you receive 403 errors during the link creation:

- Managed identities take extra time to grant transient permission during initial sync. Give it some time and try the operation again later.
- Make sure the linked storage doesn't have the existing Dataverse container(**dataverse-environmentName-organizationUniqueName**) from the same environment.
- You can identify the linked enterprise policy and `policyArmId` by running the PowerShell script `./GetIdentityEnterprisePolicyforEnvironment.ps1` with the Azure **Subscription ID** and **Resource group** name.
- You can unlink the enterprise policy by running the PowerShell script `./RevertIdentity.ps1` with the Dataverse environment ID and `policyArmId`.
- You can remove the enterprise policy by running the PowerShell script **.\RemoveIdentityEnterprisePolicy.ps1 with policyArmId**.

## See also

[What is Azure Synapse Link for Dataverse?](export-to-data-lake.md)
