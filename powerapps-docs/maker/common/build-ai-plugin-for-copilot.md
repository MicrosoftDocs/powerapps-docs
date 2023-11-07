---
title: Building AI plugins for discovery by Copilot  (preview)
description: Building AI plugins for discovery by Copilot .
ms.date: 11/07/2023
author: mduelae
ms.author: mkaur
ms.reviewer: mkaur
ms.topic: how-to
ms.subservice: common
manager: tapanm
ms.custom: bap-template
search.audienceType: 
  - maker, admin
---

# Building AI plugins for discovery by Copilot (preview)

[This article is prerelease documentation and is subject to change.]

Microsoft Dataverse supports three types of AI plugins – Dataverse custom APIs, Dataverse Table Search, and Dataverse File Search. Before you start building AI plugins for discoverability by Copilots across Microsoft 365, you’ll need to decide which one of the supported AI plugin types to create.

While additional AI plugin types might be added as supported by Dataverse, the steps to define plugin remains the same. AI pluginAI pluginAI plugincustom API

All components within an AI plugin are solution-aware, and can follow the standard application lifecycle management principles. AI pluginIn general, there are two main steps in defining an AI pluginAI plugin: 

1. Define the core functionality that you want to expose as an AI plugin. <br>
   This is a pre-requisite and an existing step in Dataverse about defining a custom API or a custom connector. This means that you can define an AI plugin for your existing custom APIs or custom connectors without any major changes.
1. Define the metadata of the AI plugin that can be discovered by a Copilot.
This is a new step allowing you to define the metadata for your AI plugin that can be used by the Copilots to discover and invoke this plugin. This process includes the following three main components:
    1. **AI plugin definition**: This is the metadata of your plugin. For example, “SalesAIPlugin”/
    1. **AI plugin operation**: This is a list of operations supported by your plugin. For example, "GetOpportunities", “CreateOpportunity”/
    1. **AI plugin instance**: This controls the state of your plugin, which are:  Enable or Disable.

Let’s get started and define our first AI plugin. In this example, we will define an AI plugin of type custom API. 

> [!Note]
> A basic understanding and knowledge of application lifecycle management (ALM) in Dataverse is required to follow this example. See [Solution concepts](/power-platform/alm/solution-concepts-alm) in Power Platform ALM to learn more.

The plugin infrastructure currently supports only custom APIs with ‘IsFunction=False’ and ‘IsPrivate=False’. Hence, ensure that your custom API is not a function or private API. At this point, you can test your custom API using a Postman client.

## Defining a Dataverse custom API as an AI plugin 

### Step 1 – Define custom API

You can create a custom API using the Power Apps. More information: [Create a custom API in Power Apps](../../developer/data-platform/create-custom-api-maker-portal.md)

The plugin infrastructure currently supports only custom APIs with ‘IsFunction=False’ and ‘IsPrivate=False’. Hence, ensure that your custom API is not a function or private API. At this point, you can test your custom API using a Postman client.

### Step 2 – Define AI plugin

Once you have defined the custom API, you can define the AI plugin using Power Apps. First, [Create a solution](../data-platform/create-solution.md). Once you have created a solution, follow the steps below to create an AI plugin:

1. In your solution, select **New** > **More** > **Other** > **AI plugin** from the drop-down.
1. Enter the values for the required fields.
    1. **Name**: Enter a name that starts with a prefix. For example,  new_myAIPlugin
    1. **PluginType**: Dataverse
1. HumanName, HumanDescription, ModelName, Model Description fields control how your plugin will be discovered by the LLM. So, provide meaningful values for those for your plugins. The remaining fields you can leave blank for now.
1. Select **Save**.

:::image type="content" source="media/ai-plugins.png" alt-text="Define AI plugin":::

### Step 3 – Define AI operations

Once you have defined an AI plugin, the next step is to add the operations you want the plugin to expose. This can be done by selecting “+ New AIPluginOperation” from the top menu bar.

Enter the following fields in this form:

- **Name**: Provide a name for your operation
- **OperationID**: this needs to be a value with a prefix like shown below
- **Custom API**: This will be a look up to the custom API you created in Step 1.
- **Description**: This field is currently used by BizChat for plugin matching, so don’t leave it blank

Select **Save and close**. If you have additional operations, you can add those following the same steps.

:::image type="content" source="media/plugin-define-ai-operation.png" alt-text="Defile AI operations":::

### Step 5 – Package as a solution

Once you have added all the required plugin metadata to your solution, make sure that you add your custom API to the same solution as well. This can be done in your solution, select **Add Existing** > **More** > **Other** > **CustomAPI** from the drop-down and select the custom API you created in Step 1.

Go to **Solutions** section in Power apps and select your solution. Then, select **Export** from the menu > select **Managed**. You can download the exported zip file and import into another test environment and test your changes.

### Step 6 – E2E Testing

At this point you should be able to test your plugin from BizChat.

