---
title: "Use environment variables in solutions | MicrosoftDocs"
description: "Use environment variables to migrate application configuration data in solutions."
Keywords: environment variables, variables, model-driven app, configuration data
author: caburk
ms.subservice: dataverse-maker
ms.author: caburk
ms.reviewer: matp
ms.date: 07/13/2023
ms.topic: overview
search.audienceType: 
  - maker
contributors:
  - shmcarth
---
# Environment variables overview

Environment variables enable the basic application lifecycle management (ALM) scenario of moving an application between Power Platform environments. In this scenario, the application stays exactly the same except for a few key external application references (such as tables, connections, and keys) that are different between the source environment and the destination environment. The application requires the structure of the tables or connections to be exactly the same between the source and the destination environments, with some differences. Environment variables allow you to specify which of these different external references should be updated as the application is moved across environments.

Environment variables store the parameter keys and values, which then serve as input to various other application objects. Separating the parameters from the consuming objects allows you to change the values within the same environment or when you migrate solutions to other environments. The alternative is leaving hard-coded parameter values within the components that use them. This is often problematic; especially when the values need to be changed during ALM operations. Because environment variables are solution components, you can transport the references (keys) and change the values when solutions are migrated to other environments.

> [!NOTE]
> New capabilities for data sources are just now being deployed and may not be available yet in your region.

Benefits of using environment variables:
- Provide new parameter values while **importing solutions** to other environments.
- Store configuration for the **data sources** used in canvas apps and flows. For example, SharePoint Online site and list parameters can be stored as environment variables; therefore allowing you to connect to different sites and lists in different environments without needing to modify the apps and flows.
- Package and transport your customization and configuration together and manage them in a single location.
- Package and transport secrets, such as credentials used by different components, separately from the components that use them.
- One environment variable can be used across many different solution components - whether they're the same type of component or different. For example, a canvas app and a flow can use the same environment variable. When the value of the environment variable needs to change, you only need to change one value. 
- Additionally, if you need to retire a data source in production environments, you can simply update the environment variable values with information for the new data source. The apps and flows don't require modification and will start using the new data source.
- Supported by [SolutionPackager](/power-platform/alm/solution-packager-tool) and [DevOps](/power-platform/alm/devops-build-tools) tools enable continuous integration and continuous delivery (CI/CD).
- The environment variables can be unpacked and stored in source control. You may also store different environment variables values files for the separate configuration needed in different environments. Solution Packager can then accept the file corresponding to the environment the solution will be imported to.

## How do they work?

Environment variables can be created and modified within the modern solution interface, automatically created when connecting to certain data sources in canvas apps, or by [using code](/powerapps/developer/data-platform/work-with-data). They can also be imported to an environment via solutions. Once environment variables are present in an environment, they can be used as inputs when authoring canvas apps, Power Automate flows, when developing plug-ins, as well as many other places such as adding a Power BI dashboard to a model-driven app. When these types of objects use environment variables, the values are then derived from the environment variables, and can be changed when solutions are imported to other environments. 

### Create an environment variable in a solution

1. Sign in to Power Apps (make.powerapps.com), and then on the left pane select **Solutions**. [!INCLUDE [left-navigation-pane](../../includes/left-navigation-pane.md)]
1. Open the solution you want or create a new one.
1. On the command bar, select **New** > **More**, and then select **Environment variable**. 
1. On the right pane, complete the following columns, and then select **Save**:  
   - **Display name**. Enter a name for the environment variable. 
   - **Name**. The unique name is automatically generated from the **Display name**, but you can change it. 
   - **Data Type**. Select from **Decimal number**, **Text**, **JSON**, **Two options**, **Data source**, or **Secret**.
     >[!NOTE]
     > 
     > - If **Data source** is the selected type, you'll also need to select the **connector**, a valid **connection** for the selected connector, and the **parameter type**. However, the connection is not stored as part of the environment variable. The connection is only used for retrieving available parameter values such as the SharePoint sites you have access to, or the lists associated with a site. For certain parameters such as SharePoint lists, you'll also need to select a parent data source environment variable such as the SharePoint site. Once saved, these will be related in the database.
     >
     > - If **Secret** is the selected type, additional information to set up and configure Azure Key Vault is needed to allow Power Platform to access the secret.
   - **Current Value**. Also known as the value. This property is optional and is a part of the environment variable value table. When a value is present it will be used, even if a default value is also present. Remove the value from your solution if you don't want to use it in the next environment. The values are also separated into separate JSON files within the exported solution.zip file and can be edited offline. More information: [How do I remove a value from an environment variable?](#how-do-i-remove-a-value-from-an-environment-variable)
   - **Default Value**. This column is part of the environment variable definition table and is not required. The default value is used if there's no current value. 
  

      Separation of default value and current value allows you to service the definition and the default value separately from the value. For example, an application publisher may list their offer on AppSource with a default value. Then optionally, the customer can provide a new value. When the application publisher publishes updates to the application, the value set by the customer won't be overwritten. 

      > [!div class="mx-imgBorder"] 
      > ![New environment variable.](media/new-environment-variable.png)

      >[!NOTE]
      > A value can't exist without a definition. The interface only allows creation of one value per definition.

## Use data source environment variables in canvas apps
### Use pre-existing data source environment variables

Environment variables can be reused across other apps and even different types of resources like cloud flows. You may wish to first create them within your solution and later use them while authoring canvas apps and cloud flows.
1. Follow the steps above to [Create an environment variable in a solution](#create-an-environment-variable-in-a-solution).
1. Edit or create a canvas app from your solution.
1. Add a **new** data source for SharePoint online.
1. Select the **Advanced** tab. You'll see a filtered list of environment variables that you have access to and that match the parameter being set. For example, when you select the SharePoint site, you'll see a list of all data source environment variables with **Connector** = **SharePoint** and **Parameter type** = **Site**. The same is true when selecting SharePoint lists for a given site. 
2. Select the desired environment variable(s), and then select **Connect.**

>[!IMPORTANT]
>If an environment variable from a different solution is selected, a dependency will exist on the solution containing the environment variable. Therefore, be sure to either: 
> - Add the environment variable to your current solution prior to exporting. 
> - Ensure the solution containing the environment variable is imported to the destination environment before your current solution is imported.

### Automatically create data source environment variables when connecting to data

This option provides simplicity and ensures environment variables will always be used for data sources, such as SharePoint Online. However, some customers prefer to provide their own schema names and therefore should create them from solutions.

1. Edit or create a canvas app from your solution.
1. Select **Settings** > **General** and enable the setting to **Automatically create environment variables when adding data sources**.
1. Add a **New** data source for SharePoint online.
1. Select a SharePoint **site**, one or more **lists**, and then **Connect**.
   >[!NOTE]
   >To prevent creation of duplicate environment variables, you'll be prompted to use the existing environment variable when duplicates are identified. You can clear the option to use the existing environment variable if creation of a duplicate is desired. 
1. Select **Save**. 

>[!NOTE]
>Pre-existing canvas apps will not automatically use data source environment variables. Remove the data source from the app and add them back using the above steps to upgrade these apps to use environment variables. 

## Use environment variables in Power Automate solution cloud flows

Environment variables can be used in solution cloud flows since they're available in the dynamic content selector. All types of environment variables can be used in triggers and actions.
To use an environment variable in a solution cloud flow:
1. Edit or create a cloud flow in a solution.
1. In an action or a trigger, determine the parameter that you want to use for the environment variable:
    
    a. If the parameter takes a simple value, such as a string or number, enter the parameter.
    
    b. If the parameter is a lookup, scroll to the bottom of the lookup, and then select **Enter custom value**. Environment variables that you have access to are listed in the dynamic content selector with other dynamic content.
       :::image type="content" source="media/select-environment-variable.png" alt-text="Select an environment variable to add to a cloud flow trigger or action.":::
1. Select the desired environment variable.

## Enter new values while importing solutions

The modern solution import interface includes the ability to enter values for environment variables. This sets the value property on the `environmentvariablevalue` table.

   >[!NOTE]
   > You may remove the value from your solution before exporting the solution. This ensures the existing value will remain in your development environment, but will not get exported in the solution. This approach allows a new value to be provided while importing the solution into other environments. You will **not** be prompted for new values during solution import if the environment variables already have either a default value or value present; whether values are part of your solution or are already present in the target environment. More information: [How do I remove a value from an environment variable?](#how-do-i-remove-a-value-from-an-environment-variable)

## Notifications

A notification is displayed when the environment variables don't have any values. This is a reminder to set the values so that components dependent on environment variables don't fail. 

## Security

The `environmentvariabledefinition` table is [user or team owned](/powerapps/maker/data-platform/types-of-entities). When you create an application that uses environment variables, be sure to assign users the appropriate level of privilege to this table. Permission to the `environmentvariablevalue` table is inherited from the parent `environmentvariabledefinition` table and therefore doesn't require separate privileges. Privileges for `environmentvariabledefinition` tables are included in Environment Maker and Basic User security roles by default. More information: [Security in Dataverse](/power-platform/admin/wp-security).

## Naming

Ensure environment variable names are unique so they can be referenced accurately. Duplicate environment variable display names make environment variables difficult to differentiate and use. Ensure environment variable names are unique so they can be referenced accurately.
The names **$authentication** and **$connection** are specially reserved parameters for flows and should be avoided. Flow save will be blocked if environment variables with those names are used.
If an environment variable is used in a flow and the display name of the environment variable is changed, then the designer will show both the old and new display name tokens to help with identification. When updating the flow, it's recommended to remove the environment variable reference and add it again.

## Use Azure Key Vault secrets

Environment variables allow for referencing secrets stored in Azure Key Vault. These secrets are then made available for use within Power Automate flows and custom connectors. Notice that the secrets aren't available for use in other customizations or generally via the API.

The actual secrets are stored in Azure Key Vault and the environment variable references the key vault secret location. Using Azure Key Vault secrets with environment variables require that you configure Azure Key Vault so that Power Platform can read the specific secrets you want to reference.

Environment variables referencing secrets aren't currently available from the dynamic content selector for use in flows.

### Configure Azure Key Vault

To use Azure Key Vault secrets with Power Platform, the Azure subscription that has the vault must have the `PowerPlatform` resource provider registered and the user who creates the environment variable must have appropriate permissions to the Azure Key Vault resource.

#### Prerequisites

1. Register the `Microsoft.PowerPlatform` resource provider in your Azure subscription.  Follow these steps to verify and configure: [Resource providers and resource types](/azure/azure-resource-manager/management/resource-providers-and-types)

   :::image type="content" source="media/env-var-secret1.png" alt-text="Register the Power Platform provider in Azure":::

1. Create an Azure Key Vault vault. Consider using a separate vault for every Power Platform environment to minimize the threat in case of a breach. Consider configuring your key vault to use **Azure role-based access control** for the **Permission model**. Go to [Best practices for using Azure Key Vault](/azure/key-vault/general/best-practices#use-separate-key-vaults) for more information. For more information about how to create a key vault, go to [Quickstart - Create an Azure Key Vault with the Azure portal](/azure/key-vault/general/quick-create-portal)
1.	Users who create or use environment variables of type secret must have permission to retrieve the secret contents. To grant a new user the ability to use the secret, select the **Access control (IAM)** area, select **Add**, and then select **Add role assignment** from the dropdown. More information: [Provide access to Key Vault keys, certificates, and secrets with an Azure role-based access control](/azure/key-vault/general/rbac-guide?tabs=azure-cli)

      :::image type="content" source="media/env-var-secret2.png" alt-text="View my access in Azure":::

1. On the **Add role assignment** wizard, leave the default assignment type as **Job function roles** and continue to the **Role** tab. Locate the **Key Vault Secrets User role** and select it. Continue to the members tab and select the **Select members** link and locate the user in the side panel. When you have the user selected and shown on the members section, continue to the review and assign tab and complete the wizard.

1. Azure Key Vault must have the **Key Vault Secrets User** role granted to the Dataverse service principal. If it doesn't exist for this vault, add a new access policy using the same method you previously used for the end user permission, only using the Dataverse application identity instead of the user. If you have multiple Dataverse service principals in your tenant, then we recommend that you select them all and save the role assignment. Once the role is assigned, review each Dataverse item listed in the role assignments list and select the Dataverse name to view the details. If the **Application ID** isn't **00000007-0000-0000-c000-000000000000** then select the identity and then select **Remove** to remove it from the list.

1. If you haven't done so already, add a secret to your new vault. More information: [Azure Quickstart - Set and retrieve a secret from Key Vault using Azure portal](/azure/key-vault/secrets/quick-create-portal#add-a-secret-to-key-vault)

> [!NOTE]
> We have recently changed the security role that we use to assert access permissions within Azure Key Vault. Previous instructions included assigning the Key Vault Reader role. If you have set up your key vault previously with the Key Vault Reader role, make sure that you add the Key Vault Secrets User role to ensure that your users and Dataverse will have sufficient permissions to retrieve the secrets.

> [!TIP]
> We recognize that our service is using the Azure role-based access control APIs to assess security role assignment even if you still have your key vault configured to use the vault access policy permission model. To simplify your configuration, we recommended that you switch your vault permission model to Azure role-based access control. You can do this in the Access configuration tab.

### Create a new environment variable for the Key Vault secret

Once Azure Key Vault is configured and you have a secret registered in your vault, you can now reference it within Power Apps using an environment variable.

1.	Sign on to [Power Apps](https://make.powerapps.com/?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc), and in the **Solutions** area, open the unmanaged solution you're using for development.
1. Select **New** > **More** > **Environment variable**.
1.	Enter a **Display name** and optionally, a **Description** for the environment variable.
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

> [!NOTE]
> - User access validation for the secret is performed in the background. If the user doesn’t have at least read permission, this validation error is displayed: **This variable didn't save properly. User is not authorized to read secrets from 'Azure Key Vault path'.**
> 
> - Currently, Azure Key Vault is the only secret store that is supported with environment variables.
>
> - The Azure Key Vault must be in the same tenant as your Power Platform subscription.

### Create a Power Automate flow to test the environment variable secret

A simple scenario to demonstrate how to use a secret obtained from Azure Key Vault is to create a Power Automate flow to use the secret to authenticate against a web service.

> [!NOTE]
> The URI for the web service in this example is not a functioning web service.

1.	Sign into [PowerApps](https://make.powerapps.com/?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc), select **Solutions**, and then open the unmanaged solution you want. [!INCLUDE [left-navigation-pane](../../includes/left-navigation-pane.md)]
1. Select **New** > **Automation** > **Cloud flow** > **Instant**.
1. Enter a name for the flow, select **Manually trigger a flow**, and then select **Create**.
1.	Select **New step**, select the **Microsoft Dataverse** connector, and then on the **Actions** tab select **Perform an unbound action**.
1.	Select the action named **RetrieveEnvironmentVariableSecretValue** from the dropdown list.
1. Provide the environment variable unique name (not the display name) added in the previous section, for this example *new_TestSecret* is used.
1. Select **...** > **Rename** to rename the action so that it can be more easily referenced in the next action. In the below screenshot, it has been renamed to **GetSecret**.

   :::image type="content" source="media/env-var-secret4.png" alt-text="Instant flow configuration for testing an environment variable secret":::
1. Select **...** > **Settings** to display the **GetSecret** action settings.
1. Enable the **Secure Outputs** option in the settings, and then select **Done**. This is to prevent the output of the action getting exposed in the flow run history.

   :::image type="content" source="media/env-var-secret5.png" alt-text="Enable secure outputs setting for the action":::
1. Select **New step**, search and select the **HTTP** connector.
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

## Current limitations

- SharePoint Online is currently the only data source supported for environment variables of type "data source" within canvas apps. However, the Dataverse connector will be updated soon for when connectivity is required to Dataverse environments other than the current environment. Other types of environment variables may be used within canvas apps by retrieving them as you would record data via a Dataverse connection.
- If you’re using environment variables for storing SharePoint data source parameters in canvas apps, ensure you use **Display Name** (instead of logical name, or ID) when using "Lookup" or "Person or group" column types.
- When environment variable values are changed directly within an environment instead of through an ALM operation like solution import, flows will continue using the previous value until the flow is either saved or turned off and turned on again.  
- Validation of environment variable values happens within the user interfaces and within the components that use them, but not within Dataverse. Therefore ensure proper values are set if they're being modified through code. 
- [Power Platform Build Tools tasks](/power-platform/alm/devops-build-tool-tasks) aren't yet available for managing data source environment variables. However, this doesn't block their usage within Microsoft provided tooling and within source control systems.
- Interacting with environment variables via custom code requires an API call to fetch the values; there isn't a cache exposed for third party code to leverage. 
- When editing a cloud flow, the environment variables shown in the dynamic content selector are unfiltered, but will be filtered by data type in the future. 
- When editing a cloud flow, if an environment variable is added in another browser tab, the flow needs to be reopened in the flow designer to refresh the dynamic content selector.
- Environment variables referencing Azure Key Vault secrets are currently limited for use with Power Automate flows and custom connectors.

## Frequently asked questions

### How can I view where environment variables are being used?

Either through selecting **Show dependencies** in the solution interface, while authoring components, or in source control and in the solution file by viewing the app or flow metadata. 

### Are data source environment variables the same as connections?

No. Although they're related. A connection represents a credential or authentication required to interact with the connector. Data source environment variables store parameters that are required by one or more actions in the connector and these parameters often vary depending on the action. For example, a SharePoint Online connection doesn't store any information about sites, lists, or document libraries. Therefore calling the connector requires both a valid connection as well as some additional parameters. 

### Can data source environment variables be used with shared connections such as SQL Server with SQL authentication?

Generally no. Shared connections with SQL Server store the parameters required to connect to data within the connection. For example, the Server and Database name are provided when creating the connection and therefore are always derived from the connection.

Data source environment variables are used for connectors that rely on user based authentication such as Azure Active Directory because the parameters can't be derived from the connection. For these reasons authentication with SQL Server, which is a shared connection, won't use data source environment variables. 

### Can my automated ALM pipeline use different values files for different environments?

Yes. Solution packager accepts file name as input parameters so your pipeline can pack a different values file into the solution depending on the environment type it’s executing against.

### What if someone inadvertently deletes a value?

If not already prevented by dependency system, runtime will use the last known value as a fallback.

### If a value is changed, when does the new value get used in canvas apps and cloud flows?

It may take up to an hour to fully publish updated environment variables because the value is pushed into the apps and flows asynchronously.

### Are premium licenses required?

No. While ALM requires Dataverse (or Dynamics 365 for Customer Engagement), use of premium connectors isn't required. The one caveat is if you're using the Dataverse connector to interact with environment variables as you would with other data records like accounts or contacts. Previously this was the only way to use environment variables in canvas apps and flows.  

### Is there a limit to the number of environment variables I can have?

No. However, the max size of a solution is 120 MB. See [Create a solution](/power-apps/maker/data-platform/create-solution)

### Can environment variable display names and descriptions be localized?

Yes.

### Should I use environment variables instead of storing configuration data in custom tables?

Yes if your configuration data isn't relational. Environment variables should be used for key: value pairs and when the value likely needs to different in other environments. Other tools such as the Configuration migration utility are better suited for migration of relational configuration data stored within custom tables. Unlike other configuration data, environment variables are migrated within solutions and therefore much simpler to manage and more performant to import. 

### How do I remove a value from an environment variable?

You might want to remove the value of an environment variable from your solution before exporting the solution. Then, the existing value will remain in your development environment, but won't be exported in the solution. This approach allows a new value to be provided while importing the solution into another environment.

To remove the value, follow these steps:

1. In the solution where the environment variable is located select the environment variable to display the properties.
1. Under **Current Value**, select **...** > **Remove from this solution**.
   :::image type="content" source="media/remove-value-env-var.png" alt-text="Remove the value from an environment variable":::

### Can I use environment variables in custom connectors?

Yes. [Environment variable support in custom connectors](/connectors/custom-connectors/environment-variables)

### See also
[Power Apps Blog: Environment variables available in preview!](https://powerapps.microsoft.com/blog/environment-variables-available-in-preview/) </BR>
[EnvironmentVariableDefinition table/entity reference](/powerapps/developer/data-platform/reference/entities/environmentvariabledefinition) </BR>
[Web API samples](/powerapps/developer/data-platform/webapi/web-api-samples) </BR>
[Create Canvas app from scratch using Dataverse.](/powerapps/maker/canvas-apps/data-platform-create-app-scratch) </BR>
[Create a flow with Dataverse](/flow/connection-cds)</BR>
[Environment variable support in custom connectors](/connectors/custom-connectors/environment-variables)</BR>


[!INCLUDE[footer-include](../../includes/footer-banner.md)] 

