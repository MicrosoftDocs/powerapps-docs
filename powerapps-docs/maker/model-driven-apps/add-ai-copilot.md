---
title: Add Copilot to a model-driven app | MicrosoftDocs
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
# Add Copilot to a model-driven app (preview)

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

## Prerequisites

- To enable Copilot for your model-driven app, your environment must have the monthly release channel enabled. Power Platform administrators can enable the monthly release channel feature from the Power Platform admin center. Go to **Environments** > open the environment you want > **Settings** > **Features**, under **Copilot** set **Requires this environment's model app refresh cadence to monthly channel** to **On**.
- Choose the data you want available for answers. Copilot in a model-driven app can answer questions about all the Dataverse tables in the model-driven app, provided they have been configured for Copilot. More information: 
