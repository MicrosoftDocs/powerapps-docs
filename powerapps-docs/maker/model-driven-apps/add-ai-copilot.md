---
title: Add Copilot to model-driven apps | MicrosoftDocs
description: Learn how to add Copilot in a model-driven app to assist app users.
author: Mattp123
ms.service: powerapps
ms.subservice: mda-maker
ms.author: mijosh
ms.reviewer: matp
ms.date: 08/10/2023
ms.topic: how-to
applies_to: 
  - "powerapps"
search.audienceType: 
  - maker
---
# Add Copilot to model-driven apps (preview)

[!INCLUDE [cc-beta-prerelease-disclaimer](../../includes/cc-beta-prerelease-disclaimer.md)]

Copilot for model-driven apps in Power Apps is a next-generation AI assistant for app users to get insights about the data in their apps through conversation in natural language. Copilot helps app users boost their productivity through AI-powered insights and intuitive app navigation.

> [!IMPORTANT]
>
> - This is a preview feature.
> - To use this capability your environment must be in the US region.
> - Preview features aren’t meant for production use and may have restricted functionality. These features are available before an official release so that customers can get early access and provide feedback.
> - For more information, go to our [preview terms](https://go.microsoft.com/fwlink/?linkid=2189520).
> - This capability is powered by [ Azure OpenAI Service](/azure/cognitive-services/openai/overview).
> - This capability is in process of rolling out, and may not be available in your region yet.
> - This capability  may be subject to usage limits or capacity throttling.

When enabled, Copilot can be accessed through the Copilot icon in the right navigation bar when you play a model-driven app. The Copilot pane can be expanded or minimized as desired. Copilot in model-driven apps answers questions about the configured Dataverse table data in the app. Copilot can also help you navigate the app. For example, when a user enters *take me to Accounts* or *show me Contacts*.

:::image type="content" source="media/model-driven-app-copilot.png" alt-text="Copilot right pane in a model-driven app" lightbox="media/model-driven-app-copilot.png":::

## Prerequisites

- To enable Copilot for your model-driven app, your environment must have the monthly release channel enabled. Power Platform administrators can enable the monthly release channel feature from the Power Platform admin center. Go to **Environments** > open the environment you want > **Settings** > **Features**, under **Copilot** set **Requires this environment's model app refresh cadence to monthly channel** to **On**.
- Choose the data you want available for answers. Copilot in a model-driven app can answer questions about all the Dataverse tables in the model-driven app, provided they have been configured for Copilot. More information: [Configure tables to use Copilot (preview)](../data-platform/table-settings-for-copilot.md)

## Give feedback

To provide feedback to help improve Copilot, app users can click the thumbs up or thumbs down icons included in each Copilot response:

### Provide positive feedback

1. On the right navigation bar, select the “thumbs up” icon.
1. Optionally, provide feedback in your own words about what you liked.
1. Select **Submit** after you're done entering your feedback.

### Provide feedback for improvement

1. On the right navigation bar, select the “thumbs down” icon.
1. Optionally, provide feedback, such as feedback about the content of Copilot’s response, or a description in your own words about what went wrong, or how you would like Copilot to improve.
1. Select **Submit** after you're done entering your feedback.

## Disable feedback

If you want to disable the ability for users to submit feedback about Copilot in model-driven apps, follow these steps.

1. Sign in to [Power Apps](https://make.powerapps.com/).
1. Go to **Tables**, and then open the **Organization** table.
1. In the **Organization columns and data** section, select **+nnn more** to display the column search box.
1. In the search box search for the *Allow users to provide feedback for App Copilot* column.
   :::image type="content" source="media/disable-mda-copilot-feedback1.png" alt-text="Find the Allow users to provide feedback for App Copilot column":::

1. Set the column to **No**, and then **Save** the table.
   :::image type="content" source="media/disable-mda-copilot-feedback2.png" alt-text="Set the Find the Allow users to provide feedback for App Copilot column to No":::

## See also

[Responsible AI FAQs for Power Apps](../common/responsible-ai-overview.md) <br />
[Add Copilot control to a canvas app (preview)](../canvas-apps/add-ai-copilot.md)