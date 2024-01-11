---
author: sericks007
ms.author: sericks
ms.date: 01/11/2024
ms.topic: include
---

<!--Any changes to this article must be reviewed by RAI Champ Leads and CELA-->

Copilot for Microsoft Dynamics 365 and Power Platform features follow a set of core security practices and [Responsible AI principles](https://www.microsoft.com/en-us/ai/principles-and-approach).

Copilot is built on the Microsoft Azure OpenAI Service and is run completely within the Azure cloud. With Azure OpenAI Service, customers get the security capabilities of Microsoft Azure. Azure OpenAI Service offers private networking, regional availability, and responsible AI content filtering. Microsoft has a technology collaboration agreement with OpenAI, which is an independent organization.

Microsoft Dynamics 365 and Power Platform data is protected by comprehensive, industry-leading compliance and security controls. Copilot is available in certain regions and may move data across geographies. You can decide which Copilot features you wish to enable. For more information on how your data is handled, refer to the documentation for your product on Microsoft Learn.

## What happens to my data when I use Copilot? 

You are in control of your data. Data is not shared with a third party unless you've granted permission to do so. Further, Microsoft doesn't use your data to train or improve Copilot or its AI features, unless you've provided consent for Microsoft to do so. Copilot adheres to existing data permissions and policies, and users will only see responses based on data they personally have access to. Refer to the documentation for the product or feature that is using Copilot for details about how you can control your data and how your data is managed.

## How does Copilot use my data? 

Each service or feature uses Copilot based on the data you've provided or have configured to be processed by Copilot.

Your prompts (inputs) and results (outputs):

-   Are NOT available to other customers.

-   Are NOT used to train or improve any third-party products or services (such as OpenAI).

-   Are NOT used to train or improve Microsoft AI models unless your tenant admin has opted into optional data sharing.

To learn more about Azure AI Service data privacy and security reference [Data, privacy, and security for Azure OpenAI Service - Azure AI services \| Microsoft Learn](https://learn.microsoft.com/en-us/legal/cognitive-services/openai/data-privacy?context=%2Fazure%2Fai-services%2Fopenai%2Fcontext%2Fcontext). To learn more about how Microsoft and Microsoft Copilot data privacy, read our [Privacy Statement](https://go.microsoft.com/fwlink/?LinkId=521839).

## Does Copilot block prompt injections (jailbreak attacks)? 

[Jailbreak attacks](https://learn.microsoft.com/en-us/azure/ai-services/openai/whats-new#responsible-ai) are user prompts designed to provoke the generative AI model into exhibiting behaviors it was trained to avoid or to break the rules set in the System Message. Services across Dynamics 365 and Power Platform are required to implement prompt injection protection.

## Can Copilot access encrypted content?

Data provided to Copilot is only provided based on the access level of the current user. Therefore, if a user has access to the encrypted data in Dynamics 365 and Power Platform, and it is provided to Copilot, then Copilot will access it.

## How does Copilot protect customer data? 

Microsoft is uniquely positioned to deliver enterprise-ready AI. Powered by [Azure OpenAI Service](https://learn.microsoft.com/en-us/azure/cognitive-services/openai/overview), Copilot is compliant with our existing privacy, security, and compliance commitments to our customers.

- **Multiple forms of protection to safeguard organizational data**. Service-side technologies are utilized to encrypt customer content both at rest and in transit, ensuring robust security measures. For comprehensive information on encryption protocols, go to [Encryption in the Microsoft Cloud](https://learn.microsoft.com/en-us/purview/office-365-encryption-in-the-microsoft-cloud-overview). Connections are safeguarded using Transport Layer Security (TLS). The transmission of data from Dynamics 365 and Power Platform to Azure OpenAI Service is facilitated through the Microsoft backbone network to ensure the reliability and safety of the transfer.

- **Architected to protect tenant, group, and individual data**. We know data leakage is a concern for customers. Large Language Models (LLMs) are not further trained on, or learn from, your tenant data or your prompts. Within your tenant, our permissions model provides safeguards and enterprise-grade security as seen in our Azure offerings. On an individual level, Copilot presents data that only you can access using the same technology that we've been using for years to secure customer data.

- **Built on Microsoft's comprehensive approach to security, compliance, and privacy**. Copilot is integrated into Microsoft services like Dynamics 365 and Power Platform and inherits these products' security, compliance, and privacy policies and processes. Multi-factor authentication, compliance boundaries, privacy protections, and more make Copilot the AI solution you can trust.

## Are Copilot responses always factual?

The responses that generative AI produces aren't guaranteed to be 100% factual. While we continue to improve responses to fact-based inquiries, people should still use their judgment when reviewing the output before sending it to others. Our Copilot capabilities provide useful drafts and summaries to help you achieve more while giving you a chance to review the AI-generated content rather than fully automating these tasks.

Our teams continue to improve algorithms to proactively address issues such as misinformation and disinformation, content blocking, data safety, and promotion of harmful or discriminatory content in line with our [responsible AI principles](https://www.microsoft.com/ai/our-approach?activetab=pivot1:primaryr5).

We also provide guidance within the user experience to reinforce the responsible use of AI-generated content and actions. To help guide users on how to effectively use Copilot and suggested actions and content, we provide:

-   Instructive guidance and prompts. When using Copilot, informational elements instruct users how to responsibly use suggested content and actions, including prompts to review and edit responses as needed prior to usage, and to manually check facts, data, and text for accuracy.

-   Cited sources. Copilot cites public sources when applicable, so you're able to see links to the web content it references.

Refer to the Responsible AI FAQ in the product documentation for the product or feature using Copilot to better understand how the specific AI system works.

## Does Copilot meet requirements for regulatory compliance mandates? 

Microsoft is offering Copilot within the Dynamics 365 and Power Platform ecosystem. For details on the regulatory certifications of a Microsoft service, go to [Service Trust Portal](https://servicetrust.microsoft.com/). Additionally, Copilot adheres to our commitment to responsible AI, which is put into action through our [Responsible AI Standard](https://www.microsoft.com/ai/responsible-ai).

As regulation in AI evolves, Microsoft will continue to adapt and respond to future regulatory requirements in this space.

Dynamics 365 and Power Platform [trust](https://learn.microsoft.com/en-us/dynamics365/get-started/availability) documentation provides comprehensive information about customer data locations, and compliance with global, regional, and industry-specific requirements for managing data.
