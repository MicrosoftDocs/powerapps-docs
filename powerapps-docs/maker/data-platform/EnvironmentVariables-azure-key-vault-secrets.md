---
title: "Use environment variables for Azure Key Vault secrets | MicrosoftDocs"
description: "Use environment variables to reference Azure Key Vault secrets."
Keywords: environment variables, variables, Azure Key Vault, secrets, model-driven app, configuration data
author: caburk
ms.subservice: dataverse-maker
ms.author: caburk
ms.reviewer: matp
ms.date: 03/31/2025
ms.topic: overview
ms.collection: bap-ai-copilot
search.audienceType: 
  - maker
contributors:
  - matapg007
  - asheehi1
  - Laskewitz
---

# Use environment variables for Azure Key Vault secrets

Environment variables allow for referencing secrets stored in Azure Key Vault. These secrets are then made available for use within Power Automate flows and custom connectors. Notice that the secrets aren't available for use in other customizations or generally via the API.

The actual secrets are stored in Azure Key Vault and the environment variable references the key vault secret location. Using Azure Key Vault secrets with environment variables require that you configure Azure Key Vault so that Power Platform can read the specific secrets you want to reference.

Environment variables referencing secrets aren't currently available from the dynamic content selector for use in Power Automate flows.

## Configure Azure Key Vault

To use Azure Key Vault secrets with Power Platform, the Azure subscription that has the vault must have the `PowerPlatform` resource provider registered and the user who creates the environment variable must have appropriate permissions to the Azure Key Vault resource.

> [!IMPORTANT]
>
> - There are recent changes to the security role used to assert access permissions within Azure Key Vault. Previous instructions included assigning the Key Vault Reader role. If you have set up your key vault previously with the Key Vault Reader role, make sure that you add the Key Vault Secrets User role to ensure that your users and Microsoft Dataverse have sufficient permission to retrieve the secrets.
> - We recognize that our service is using the Azure role-based access control APIs to assess security role assignment even if you still have your key vault configured to use the vault access policy permission model. To simplify your configuration, we recommended that you switch your vault permission model to Azure role-based access control. You can do this on the **Access configuration** tab.

1. Register the `Microsoft.PowerPlatform` resource provider in your Azure subscription. Follow these steps to verify and configure: [Resource providers and resource types](/azure/azure-resource-manager/management/resource-providers-and-types)

   :::image type="content" source="media/env-var-secret1.png" alt-text="Register the Power Platform provider in Azure":::

1. Create an Azure Key Vault vault. Consider using a separate vault for every Power Platform environment to minimize the threat in case of a breach. Consider configuring your key vault to use **Azure role-based access control** for the **Permission model**. More information: [Best practices for using Azure Key Vault](/azure/key-vault/general/best-practices#use-separate-key-vaults), [Quickstart - Create an Azure Key Vault with the Azure portal](/azure/key-vault/general/quick-create-portal)

1. Users who create or use environment variables of type secret must have permission to retrieve the secret contents. To grant a new user the ability to use the secret, select the **Access control (IAM)** area, select **Add**, and then select **Add role assignment** from the dropdown. More information: [Provide access to Key Vault keys, certificates, and secrets with an Azure role-based access control](/azure/key-vault/general/rbac-guide?tabs=azure-cli)

      :::image type="content" source="media/env-var-secret2.png" alt-text="View my access in Azure":::

1. On the **Add role assignment** wizard, leave the default assignment type as **Job function roles** and continue to the **Role** tab. Locate the **Key Vault Secrets User role** and select it. Continue to the members tab and select the **Select members** link and locate the user in the side panel. When you have the user selected and shown on the members section, continue to the review and assign tab and complete the wizard.

1. Azure Key Vault must have the **Key Vault Secrets User** role granted to the Dataverse service principal. If it doesn't exist for this vault, add a new access policy using the same method you previously used for the end user permission, only using the Dataverse application identity instead of the user. If you have multiple Dataverse service principals in your tenant, then we recommend that you select them all and save the role assignment. Once the role is assigned, review each Dataverse item listed in the role assignments list and select the Dataverse name to view the details. If the Application ID isn't 00000007-0000-0000-c000-000000000000**, then select the identity, and then select **Remove** to remove it from the list.

1. If you have enabled [Azure Key Vault Firewall](/azure/key-vault/general/network-security), you have to allow Power Platform IP addresses access to your key vault. Power Platform isn't included in the "Trusted Services Only" option. Go to [Power Platform URLs and IP address ranges](/power-platform/admin/online-requirements#ip-addresses-required) for the current IP addresses used in the service.

1. If you haven't done so already, add a secret to your new vault. More information: [Azure Quickstart - Set and retrieve a secret from Key Vault using Azure portal](/azure/key-vault/secrets/quick-create-portal#add-a-secret-to-key-vault)

## Create a new environment variable for the Key Vault secret

Once Azure Key Vault is configured and you have a secret registered in your vault, you can now reference it within Power Apps using an environment variable.

> [!NOTE]
>
> - User access validation for the secret is performed in the background. If the user doesn’t have at least read permission, this validation error is displayed: "This variable didn't save properly. User isn't authorized to read secrets from 'Azure Key Vault path'."
> - Currently, Azure Key Vault is the only secret store that is supported with environment variables.
> - The Azure Key Vault must be in the same tenant as your Power Platform subscription.

1. Sign on to [Power Apps](https://make.powerapps.com/?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc), and in the **Solutions** area, open the unmanaged solution you're using for development.
1. Select **New** > **More** > **Environment variable**.
1. Enter a **Display name** and optionally, a **Description** for the environment variable.
1. Select the **Data Type** as **Secret** and **Secret Store** as **Azure Key Vault**.
1. Choose from the following options:
   - Select **New Azure Key Vault value reference**. After the information is added in the next step and saved, an environment variable *value* record is created.
   - Expand **Show default value**, to display the fields to create a **Default Azure Key Vault secret**. After the information is added in the next step and saved, the default value demarcation is added to the environment variable *definition* record.
1. Enter the following information:
   - **Azure Subscription ID**: The Azure subscription ID associated with the key vault.
   - **Resource Group Name**: The Azure resource group where the key vault that contains the secret is located.
   - **Azure Key Vault Name**: The name of the key vault that contains the secret.
   - **Secret Name**: The name of the secret located in Azure Key Vault.

        > [!TIP]
        > The subscription ID, resource group name, and key vault name can be found on the Azure portal **Overview** page of the key vault. The secret name can be found on the key vault page in the Azure portal by selecting **Secrets** under **Settings**.

1. Select **Save**.

## Create a Power Automate flow to test the environment variable secret

A simple scenario to demonstrate how to use a secret obtained from Azure Key Vault is to create a Power Automate flow to use the secret to authenticate against a web service.

> [!NOTE]
> The URI for the web service in this example isn't a functioning web service.

1. Sign into [Power Apps](https://make.powerapps.com/?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc), select **Solutions**, and then open the unmanaged solution you want. [!INCLUDE [left-navigation-pane](../../includes/left-navigation-pane.md)]
1. Select **New** > **Automation** > **Cloud flow** > **Instant**.
1. Enter a name for the flow, select **Manually trigger a flow**, and then select **Create**.
1. Select **New step**, select the **Microsoft Dataverse** connector, and then on the **Actions** tab select **Perform an unbound action**.
1. Select the action named **RetrieveEnvironmentVariableSecretValue** from the dropdown list.
1. Provide the environment variable unique name (not the display name) added in the previous section, for this example *new_TestSecret* is used.
1. Select **...** > **Rename** to rename the action so that it can be more easily referenced in the next action. In this screenshot, it's renamed to **GetSecret**.

   :::image type="content" source="media/env-var-secret4.png" alt-text="Instant flow configuration for testing an environment variable secret":::

1. Select **...** > **Settings** to display the **GetSecret** action settings.
1. Enable the **Secure Outputs** option in the settings, and then select **Done**. This is to prevent the output of the action getting exposed in the flow run history.

   :::image type="content" source="media/env-var-secret5.png" alt-text="Enable secure outputs setting for the action":::

1. Select **New step**, search, and select the **HTTP** connector.
1. Select the **Method** as **GET** and enter the **URI** for the web service. In this example, the fictitious web service *httpbin.org* is used.
1. Select **Show advanced options**, select the **Authentication** as **Basic**, and then enter the **Username**.
1. Select the **Password** field, and then on the **Dynamic content** tab under the flow step name above (*GetSecret* in this example) select **RetrieveEnvironmentVariableSecretValueResponse EnvironmentVariableSecretValue**, which is then added as an expression `outputs('GetSecretTest')?['body/EnvironmentVariableSecretValue']` or `body('GetSecretTest')['EnvironmentVariableSecretValue']`.

   :::image type="content" source="media/env-var-secret6.png" alt-text="Create a new step using the HTTP connector":::

1. Select **...** > **Settings** to display the **HTTP** action settings.
1. Enable the **Secure Inputs** and **Secure Outputs** options in the settings, and then select **Done**. Enabling these options prevents the input and outputs of the action getting exposed in the flow run history.
1. Select **Save** to create the flow.
1. Manually run the flow to test it.

    Using the run history of the flow, the outputs can be verified.

    :::image type="content" source="media/env-var-secret7.png" alt-text="Flow output":::

## Use environment variable secrets in Microsoft Copilot Studio

Environment variable secrets in Microsoft Copilot Studio work a bit differently. You need to run through the steps in the sections in [Configure Azure Key Vault](#configure-azure-key-vault) and [Create a new environment variable for the Key Vault secret](#create-a-new-environment-variable-for-the-key-vault-secret) to use secrets with environment variables.

### Give Copilot Studio access to Azure Key Vault

Follow these steps:

1. Go back to your Azure Key Vault.
1. Copilot Studio needs access to the key vault. To grant Copilot Studio the ability to use the secret, select **Access control (IAM)** on the left navigation, select **Add**, and then select **Add role assignment**.

   :::image type="content" source="media/env-var-secret2.png" alt-text="View my access in Azure":::

1. Select the **Key Vault Secrets User** role, and then select **Next**.
1. Select **Select Members**, search for *Power Virtual Agents Service*, select it, and then choose **Select**.
1. Select **Review + assign** on the bottom of the screen. Review the information and select **Review + assign** again if all is correct.

### Add a tag to allow a copilot to access the secret in Azure Key Vault

By completing the previous steps in this section, Copilot Studio now has access to the Azure Key Vault, but you can't use it yet. To complete the task, follow these steps:

1. Go to [Microsoft Copilot Studio](https://copilotstudio.microsoft.com) and open the agent you want to use for the environment variable secret or create a new one.
1. Open an agent topic or create a new one.
1. Select the **+** icon to add a node, and then select **Send a message**.
1. Select the **Insert variable {x}** option in the **Send a message** node.
1. Select the **Environment** tab. Select the environment variable secret you created in the [Create a new environment variable for the Key Vault secret](#create-a-new-environment-variable-for-the-key-vault-secret) step.
1. Select **Save** to save your topic.
1. In the test pane, test your topic by using one of the start phrases of the topic where you just added the **Send a message** node with the environment variable secret. You should run into an error that looks like this:

   :::image type="content" source="media/env-var-secret8.png" alt-text="Error message: Bot isn't allowed to use environment variable. To add the bot to the allowed list add a tag 'AllowedBots' with value.":::
   
   This means you need to go back to Azure Key Vault and edit the secret. Leave Copilot Studio open, because you come back here later.

1. Go to Azure Key Vault. In the left navigation, select **Secrets** under **Objects**. Select the secret you want to make available in Copilot Studio by selecting the name.
1. Select the version of the secret.
1. Select **0 tags** next to **Tags**. Add a **Tag Name** and a **Tag Value**. The error message in Copilot Studio should give you the exact values of those two properties. Under **Tag Name** you need to add **AllowedBots** and in **Tag Value** you need to add the value that was displayed in the error message. This value is formatted as `{envId}/{schemaName}`. If there are multiple copilots that need to be allowed, separate the values with a comma. When done, select **OK**.
1. Select **Apply** to apply the tag to the secret.
1. Go back to Copilot Studio. Select **Refresh** in the **Test your copilot** pane.
1. In the test pane, test your topic again by using one of the start phrases of the topic.

The value of your secret should be shown in the test panel.

### Add a tag to allow all copilots in an environment access to the secret in Azure Key Vault

Alternatively, you can allow all copilots in an environment access to the secret in Azure Key Vault. To complete the task, follow these steps:

1. Go to Azure Key Vault. In the left navigation, select **Secrets** under **Objects**. Select the secret you want to make available in Copilot Studio by selecting the name.
1. Select the version of the secret.
1. Select **0 tags** next to **Tags**. Add a **Tag Name** and a **Tag Value**. Under **Tag Name** add **AllowedEnvironments** and in **Tag Value** add the environment ID of the environment you want to allow. When done, select **OK**
1. Select **Apply** to apply the tag to the secret.

## Limitation

Environment variables referencing Azure Key Vault secrets are currently limited for use with Power Automate flows, Copilot Studio agents, and custom connectors.

## Integrate Azure Key Vault private link with environment variables

Using Azure Key Vault secrets with environment variables requires configuring Azure Key Vault so that Power Platform can read the specific secrets you want to reference. This capability enables support for environment variables with Azure Key Vault secrets connecting via a private link, enhancing security and providing a more robust integration.

1. Set up Azure Virtual Network support for Power Platform to integrate environment variables with Azure Key Vault secrets without exposing them to the public internet. For detailed instructions, go to [set up virtual network](/power-platform/admin/vnet-support-setup-configure).
1. Ensure that the Azure subscription for Key Vault and Power Platform Virtual Network are in the same tenant, as cross-tenant integration isn't supported.
1. Ensure that the user who creates the environment variables has appropriate permissions to the Azure Key Vault resource. For more details, go to [Configure the Azure key Vault](/power-apps/maker/data-platform/environmentvariables-azure-key-vault-secrets#configure-azure-key-vault)
1. Create a key vault and establish a private link connection. The steps to create the key vault should include the following actions:

   - Disable public access.
   - Create a private endpoint.
   - Select the virtual network and subnet where you want this private endpoint to be created. Ensure to connect the Virtual Network (virtual network) delegated to Power Platform.
   - Validate the private link connectivity.

   For detailed steps, go to [Set up Virtual Network support for Power Platform](/power-platform/admin/vnet-support-setup-configure).

1. Create [environment variables](/power-apps/maker/data-platform/environmentvariables-azure-key-vault-secrets#create-a-new-environment-variable-for-the-key-vault-secret) secrets by linking to the Azure Key Vault.

### See also

[Use data source environment variables in canvas apps](environmentvariables-data-source-canvas-apps.md) <br>
[Use environment variables in Power Automate solution cloud flows](environmentvariables-power-automate.md) <br>
[Environment variables overview.](EnvironmentVariables.md)</BR>

[!INCLUDE[footer-include](../../includes/footer-banner.md)]
