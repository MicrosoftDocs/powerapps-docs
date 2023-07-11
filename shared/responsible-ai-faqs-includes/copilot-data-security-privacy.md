---
author: KumarVivek
ms.author: waltsun
ms.date: 05/19/2023
ms.topic: include
---

<!--Any changes to this article must be reviewed by RAI Champ Leads and CELA-->

With the introduction of [generative AI across Microsoft business applications](https://www.microsoft.com/ai/dynamics-365-ai) including Dynamics 365, Viva Sales, and Microsoft Power Platform, interactions with AI across business roles and processes will become second nature. With Copilot, Dynamics 365 and Power Platform introduce a new way to generate ideas, content drafts, and methods to access and organize information across the business.

Before your business starts using Copilot capabilities in Dynamics 365 and Power Platform, you may have questions about how it works, how it keeps your business data secure and adheres to privacy requirements, and other important considerations.

This article provides answers to common questions related to business data security and privacy to help your organization get started with Copilot in Dynamics 365 and Power Platform.

## What's the difference between ChatGPT and Copilot?

ChatGPT is a general-purpose large language model (LLM) trained by OpenAI on a massive dataset of text, designed to engage in human-like conversations and answer a wide range of questions on several topics.

Copilot also uses an LLM, however, the enterprise-ready AI technology powered by [Azure OpenAI Service](/azure/cognitive-services/openai/overview) is prompted and optimized for your business processes and your business data to meet security and privacy requirements. For Dynamics 365 and Power Platform users, Copilot suggests optional actions and content recommendations in context with the task at hand.

A few ways in which Copilot for natural language generation is unique:  

- The AI-generated responses are uniquely contextual, relevant to the task at hand, and informed by business data whether it's a response to an email from Dynamics 365, an application that automates a specific manual process, or creating a targeted list of customer segments from your CRM system.

- Copilot uses both an LLM (like GPT) and your organization’s business data to produce more accurate, relevant, and personalized results. Your business data is used to improve context only for your scenario, and the LLM itself doesn't learn from your usage. For more information on how Copilot works, go to the next question.

- Powered by Azure OpenAI Service, Copilot is designed from the ground up on a foundation of enterprise-grade security, compliance, and privacy.
  
## How does Copilot work in Dynamics 365 and Power Platform?

With Copilot, Dynamics 365 and Power Platform harness the power of foundation models coupled with proprietary Microsoft technologies and apply to your business data with:

- Search (using Bing and [Azure Cognitive Search](/azure/search/search-what-is-azure-search)), which brings domain-specific context to a Copilot prompt, enabling a response to integrate information from content like manuals, documents or other data within the organization's tenant. Currently, Power Virtual Agents and Dynamics 365 Customer Service use this retrieval augmented generation approach as preprocessing to call an LLM.

- Microsoft applications like Dynamics 365, Viva Sales, Dataverse, and Power Platform.

- [Microsoft Graph API](/graph/use-the-api), which brings more context from customer signals into the prompt, such as information from emails, chats, documents, and meetings when you have authorized Copilot to do so.

Here's a high-level overview of how Copilot works in Dynamics 365 and Power Platform.

:::image type="content" source="/power-apps/media/shared-content/copilot.png" alt-text="<This diagram illustrates how Copilot works in Dynamics 365 and Power Platform, which is also described in the content following the diagram.>":::

1. Copilot requests an input prompt from a business user in an app, like Dynamics 365 Sales or Power Apps.

1. Copilot preprocesses the prompt through an approach called *grounding*, which improves the specificity of the prompt, so the user gets answers that are relevant and actionable to their specific task. It does this, in part, by making a call to Microsoft Graph and Dataverse and accessing the enterprise data the user consents to and grants permissions to use for the retrieval of their business content and context. We also scope the grounding to documents and data that are visible to the authenticated user through role-based access controls (RBAC). For instance, an intranet question about benefits would  return only an answer based on documents relevant to the employee’s role.

    This retrieval of information is referred to as a *retrieval augmented generation* approach and allows Copilot to provide more contextual information as input to an LLM, combining the user data with other inputs such as information retrieved from knowledge base articles to improve the prompt.  

1. Copilot takes the response from the LLM and post processes it. Depending on the scenario, this post-processing includes some combination of additional grounding calls to Microsoft Graph, responsible AI checks, filtering with Azure content moderation, and additional business-specific constraints and command generation.

1. Finally, Copilot returns a recommended response to the user and sends commands back to the apps where a human-in-the-loop can review. Copilot iteratively processes and orchestrates these sophisticated services to produce results that are relevant to your business, accurate, and secure.

## How does Copilot use your proprietary business data? Is it used to train AI models?

Copilot unlocks business value by connecting LLMs to your business data in a secure, compliant, privacy-preserving way.

With your (customer) approval, which you can revoke at any time, Copilot has real-time access to both your content and context in Microsoft 365 Graph and Dataverse. Using this, Copilot:

1. Generates answers anchored in your business content when relevant and with consent. The business data could include, for example, your documents, emails, calendar, chats, meetings, or contacts.

1. Combines them with your working context. For example, the meeting you’re in now, the email exchanges you’ve had on a topic, or the chat conversations you had last week.

1. Validates that you have appropriate access to receive the information in response.

1. Delivers grounded, relevant, and contextual responses based on the above.

> [!IMPORTANT]
>
> - Microsoft doesn't use customers’ data to train LLMs. We believe the customers’ data is their data, aligned to the [Microsoft' data privacy policy](https://aka.ms/privacy).
> - AI-powered LLMs are trained on a large but limited corpus of data. However, prompts, responses, and data accessed through Microsoft 365 Graph and Microsoft services aren't used to train Copilot capabilities in Dynamics 365 and Power Platform for use by other customers.
> - The foundation models aren't improved through your usage. This means your data is accessible only by authorized users within your organization unless you explicitly consent to other access or use.

## Are Copilot responses always factual?

The responses that generative AI produces aren't guaranteed to be 100% factual. While we continue to improve responses to fact-based inquiries, people should still use their judgment when reviewing the output before sending them to others. Our Copilot capabilities provide useful drafts and summaries to help you achieve more while giving you a chance to review the generated AI rather than fully automating these tasks.

Our teams continue to improve algorithms to proactively address issues, such as misinformation and disinformation, content blocking, data safety, and preventing the promotion of harmful or discriminatory content in line with our [responsible AI principles](https://www.microsoft.com/ai/our-approach?activetab=pivot1:primaryr5).

We also provide guidance within the user experience to reinforce the responsible use of AI-generated content and actions. To help guide users on how to effectively use Copilot and suggested actions and content, we provide:  

- **Instructive guidance and prompts**. When using Copilot, informational elements instruct users how to responsibly use suggested content and actions, including prompts to review and edit responses as needed prior to usage, and to manually check facts, data, and text for accuracy.

- **Cited sources**. Copilot cites public sources when applicable, so you’re able to see links to the web content it references.

## How does Copilot protect sensitive business information and data?

Microsoft is uniquely positioned to deliver enterprise-ready AI. Powered by [Azure OpenAI Service](https://learn.microsoft.com/azure/cognitive-services/openai/overview), Copilot features built-in responsible AI and enterprise-grade Azure security.

- **Built on Microsoft’s comprehensive approach to security, compliance, and privacy**. Copilot is integrated into Microsoft services like Dynamics 365, Viva Sales, Power Platform, and Microsoft 365 and inherits these products' valuable security, compliance, and privacy policies and processes. Two-factor authentication, compliance boundaries, privacy protections, and more make Copilot the AI solution you can trust.

- **Architected to protect tenant, group, and individual data**. We know data leakage is a concern for customers. LLMs are not further trained on, or learn from, your tenant data or your prompts. Within your tenant, our time-tested permissions model provides safeguards and enterprise grade security as seen in our Azure offerings. On an individual level, Copilot presents data that only you can access using the same technology that we’ve been using for years to secure customer data.

- **Designed to learn new skills**. Copilot’s foundation skills are a game changer for productivity and business processes. The capabilities allow you to create, summarize, analyze, collaborate, and automate using your specific business content and context. In addition, Copilot recommends actions for you (for example, "create a time and expense application to enable employees to submit their time and expense reports"). Copilot is designed to learn new skills. For example, with Viva Sales, Copilot can learn how to connect to CRM systems of record to pull customer data, like interaction and order histories, into communications. As Copilot learns about new domains and processes, it will be able to perform even more sophisticated tasks and queries.

## Will Copilot meet requirements for regulatory compliance mandates?

Microsoft is offering Copilot within the Dynamics 365 and Power Platform ecosystem. For details on the regulatory certifications for a Microsoft service, go to [Service Trust Portal](https://servicetrust.microsoft.com). Additionally, Copilot adheres to our commitment to responsible AI, which is described in our [responsible AI principles](https://www.microsoft.com/ai/responsible-ai).

As regulation in the AI space evolves, Microsoft will continue to adapt and respond to fulfill future regulatory requirements in this space.
