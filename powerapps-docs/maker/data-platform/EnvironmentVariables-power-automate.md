---
title: "Use environment variables in Power Automate solution cloud flows | MicrosoftDocs"
description: "Use environment variables to as parameters in Power Automate cloud flows."
Keywords: environment variables, variables, model-driven app, configuration data
author: caburk
ms.subservice: dataverse-maker
ms.author: caburk
ms.reviewer: matp
ms.date: 12/11/2023
ms.topic: overview
search.audienceType: 
  - maker
contributors:
  - shmcarth
  - asheehi1
---
# Use environment variables in Power Automate solution cloud flows

Environment variables can be used in solution cloud flows since they're available in the dynamic content selector. All types of environment variables can be used in triggers and actions.

To use an environment variable in a solution cloud flow:

1. Edit or create a cloud flow in a solution.
1. In an action or a trigger, determine the parameter that you want to use for the environment variable:

    1. If the parameter takes a simple value, such as a string or number, enter the parameter.
    1. If the parameter is a lookup, scroll to the bottom of the lookup, and then select **Enter custom value**. Environment variables that you have access to are listed in the dynamic content selector with other dynamic content.

        :::image type="content" source="media/select-environment-variable.png" alt-text="Select an environment variable to add to a cloud flow trigger or action.":::

1. Select the desired environment variable.

## Limitations

- When environment variable values are changed directly within an environment instead of through an ALM operation like solution import, flows will continue using the previous value until the flow is either saved or turned off and turned on again.
- When editing a cloud flow, the environment variables shown in the dynamic content selector are unfiltered, but will be filtered by data type in the future. 
- When editing a cloud flow, if an environment variable is added in another browser tab, the flow needs to be reopened in the flow designer to refresh the dynamic content selector.

### See also

[Use data source environment variables in canvas apps](environmentvariables-data-source-canvas-apps.md) <br>
[Create a flow with Dataverse](/flow/connection-cds)</BR>
[Environment variables overview.](EnvironmentVariables.md)</BR>


[!INCLUDE[footer-include](../../includes/footer-banner.md)]
