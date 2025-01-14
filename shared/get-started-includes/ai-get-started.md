---
author: edupont04
ms.topic: include
ms.date: 06/19/2024
ms.author: edupont
---
## How does generative AI relate to what Microsoft offers in Azure?

*Generative AI* is a type of artificial intelligence that can create new content or data for you based on your input or *prompt*. For example, generative AI can write text, generate images, compose music, or synthesize speech. Microsoft offers a range of AI models and services in Azure, such as Azure Cognitive Services, Azure Machine Learning, and Azure OpenAI Service. [Azure OpenAI Service](/azure/ai-services/openai/overview) is a flavor of generative AI that lets you access and use OpenAI models, such as GPT-4 and DALL-E, for various tasks and scenarios. Dynamics 365 apps use Azure OpenAI Service to provide generative AI capabilities to help business users in their work. Our partners can also integrate Azure OpenAI Service in their solutions.

Learn more in the blog post at [Innovate faster with generative AI on Azure OpenAI Service](https://startups.microsoft.com/blog/innovate-faster-with-generative-ai-on-azure-openai-service/).

## How can generative AI help businesses?

The term *generative AI* sounds intriguing, but how can businesses use it to get ahead? Here's a blog post that provides some interesting examples that might inspire you: [Azure OpenAI Service: Ten ways generative AI is transforming businesses](https://azure.microsoft.com/blog/azure-openai-service-10-ways-generative-ai-is-transforming-businesses/).

You can also get a quick overview of generative AI capabilities in Dynamics 365 apps at [Microsoft Copilot in Dynamics 365](/dynamics365/copilot/).  

> [!TIP]
> The next two sections are intended for organizations that want to deliver generative AI themselves, meaning not people who want to use the generative AI capabilities that are built into Dynamics 365 apps. If you're a business user, jump to one of the other sections - use the links in the *In this article* section at the top to find the right subject for you.

## How do I get access to Azure OpenAI Service, and choose and deploy AI models?

To get access to Azure OpenAI Service, you must have an Azure subscription and an Azure OpenAI Service account. You can sign up for both on the Azure portal. Your account lets you create an Azure OpenAI Service resource and get an API key that you can use to access the Azure OpenAI Service models. You can choose from various models for different domains and purposes. For example, text generation, text analysis, image generation, image analysis, and conversational AI.

You can customize, train, and deploy models by providing your own data and parameters. However, you can typically skip that expensive and time consuming process. The Azure OpenAI Service model is trained on vast amounts of data already.

The following table provides an overview of tasks and resources.

|What  |Where|Learn more|
|---------|---------|---------|
|Get an Azure subscription. Sign up for a paid plan, or start for free.| [azure.microsoft.com](https://azure.microsoft.com)| |
|Request access to Azure OpenAI Service for your subscription. Currently, access to this service is granted only by applying for access. | [https://aka.ms/OAIapply](https://aka.ms/OAIapply) |[What is Azure OpenAI Service?](/azure/ai-services/openai/overview) |
|Get permissions on your account to create Azure OpenAI resources and deploy models.|[Azure portal](https://portal.azure.com/)|[Role-based access control for Azure OpenAI Service](/azure/ai-services/openai/how-to/role-based-access-control)|
|Create Azure OpenAI Service resource and deploy a model.|[Azure portal/](https://portal.azure.com/) and [Azure AI Foundry portal](https://oai.azure.com/)|[Create and deploy an Azure OpenAI Service resource](/azure/ai-services/openai/how-to/create-resource)|

After you complete this step, you can start to develop your Copilot experience, which requires the following information about the resource and deployed model:

|What|Where to find it|
|-|-|
|Azure OpenAI API key and endpoint (URL)|**Keys and Endpoint** page for the resource in the Azure portal.|
|Deployment name for the model|**Deployments** page in the Azure AI Foundry portal.|

## How much does this cost, and are there tools to predict and measure cost?

The cost of using Azure OpenAI Service depends on the type and amount of resources that you use, which in turn depend on the model. You can use the [Azure pricing calculator](https://azure.microsoft.com/pricing/calculator/) to estimate the cost of using Azure OpenAI Service based on your expected usage and configuration.

Because your AI features are attached to your Azure OpenAI Service key, you're responsible for the operating costs of Azure OpenAI resources throughout development and testing. You remain responsible when your customers use the feature in production or sandbox environments. For example, an AI feature that provides a handful of monthly suggestions to business owners likely consume fewer resources and costs less. In contrast, an AI feature that generates a daily, two-page project summary for each employee probably consumes more resources and costs more.

Optionally, use the [Microsoft Cost Management and Billing](/azure/cost-management-billing/cost-management-billing-overview) tools to monitor and control your spending on Azure OpenAI Service. You can set budgets, alerts, and policies to track and optimize your costs. You can also view and download detailed reports and invoices that show your usage and charges.

Learn more about how much Azure OpenAI Service costs and what are the tools to predict/measure cost at [Azure OpenAI Service pricing](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/).

## Are there pros and cons for using the popular models?

The popular models that are available in Azure OpenAI Service today are *GPT-4* and *DALL-E*. GPT-4 is a large-scale language model that can generate natural and coherent text for various tasks and domains, such as summarization, translation, question answering, and content creation. DALL-E is a large-scale image model that can generate realistic and diverse images from text or image prompts, such as drawings, logos, icons, and scenes.

Both models are good at producing high-quality and relevant outputs that can enhance your applications and workflows. However, both models also have some limitations and challenges that you should be aware of. For example, the models might not always generate accurate or factual outputs, respect ethical and social norms, or protect the privacy and security of the data.

To learn more about what the popular models are good at or less good at, go to [Azure OpenAI Service models](/azure/ai-services/openai/concepts/models).

## What are the pitfalls and best practices for prompts?

A prompt is the input that you provide to the model to generate an output. A prompt can be text, image, or a combination of both. The way you write a prompt can affect the quality and relevance of the output. Therefore, it's important to follow some guidelines and best practices when you write prompts. Some of the pitfalls and best practices are:

- Be clear and specific about what you want the model to do and what kind of output you expect.
- Provide enough context and information for the model to understand the task and the domain.
- Use examples, keywords, and formatting to guide the model and constrain the output.
- Avoid ambiguous, vague, or misleading prompts that might confuse the model or lead to undesired outputs.
- Test and evaluate the outputs on different prompts and scenarios to check the performance and reliability of the model.
- Review and verify the outputs for accuracy, relevance, quality, and ethics before using them in your applications or workflows.

Learn more about how to write effective prompts, and what the pitfalls and best practices are, at [The art of the prompt: How to get the best out of generative AI](https://news.microsoft.com/source/features/ai/the-art-of-the-prompt-how-to-get-the-best-out-of-generative-ai/).

## How can I manage prompt outputs and uncertainty?

The outputs that the model generates aren't always perfect or predictable. Models might generate outputs that are inaccurate, irrelevant, incomplete, inconsistent, or even inappropriate. Therefore, you need a strategy for managing outputs and handling uncertainty.

- Use the model parameters and settings to control the output format, length, and diversity.
- Use the model metrics and scores to measure the output quality, confidence, and similarity.
- Use the model feedback and logs to monitor and improve the output performance and reliability.
- Use the model filters and safeguards to prevent and detect the output errors and issues.
- Use human review to validate and correct the output results and outcomes.

Learn more about how to manage outputs and uncertainty at [How To Control Azure OpenAI Models](https://techcommunity.microsoft.com/t5/ai-azure-ai-services-blog/how-to-control-azure-openai-models/ba-p/4146793). Learn more about Copilot prompts at [Learn about Copilot prompts](https://support.microsoft.com/topic/learn-about-copilot-prompts-f6c3b467-f07c-4db1-ae54-ffac96184dd5).
