---
author: sericks007
ms.author: sericks
ms.date: 03/21/2024
ms.topic: include
---

<!--Any changes to this article must be reviewed by RAI Champ Leads and CELA-->

Copilot for Dynamics 365 and Power Platform features follow a set of core security and privacy practices and the Microsoft [Responsible AI Standard](https://www.microsoft.com/ai/principles-and-approach). Dynamics 365 and Power Platform data is protected by comprehensive, industry-leading compliance, security, and privacy controls.

Copilot is built on [Microsoft Azure OpenAI Service](/azure/cognitive-services/openai/overview) and runs completely within the Azure cloud. Azure OpenAI offers regional availability and responsible AI content filtering. Copilot uses OpenAI models with all the [security capabilities of Microsoft Azure](/azure/security/fundamentals/overview). OpenAI is an independent organization. We don't share your data with OpenAI.

Copilot features aren't available in all Azure geographies and languages. Depending on where your environment is hosted, you might need to allow data movement across geographies to use them. For more information, see the articles listed under [Data movement across geographies](#data-movement-across-geographies).

## What happens to my data when I use Copilot? 

You are in control of your data. Microsoft doesn't share your data with a third party unless you've granted permission to do so. Further, we don't use your customer data to train Copilot or its AI features, unless you provide consent for us to do so. Copilot adheres to existing data permissions and policies, and its responses to you're based only on data that you personally can access. For more information about how you can control your data and how your data is handled, see the articles listed under [Copilot in Dynamics 365 apps and Power Platform](#copilot-in-dynamics-365-apps-and-power-platform).

Copilot monitors for abusive or harmful uses of the service with transient processing. We don't store or conduct eyes-on review of Copilot inputs and outputs for abuse monitoring purposes.

## How does Copilot use my data? 

Each service or feature uses Copilot based on the data that you provide or set up for Copilot to process.

Your prompts (inputs) and Copilot's responses (outputs or results):

- Are NOT available to other customers.

- Are NOT used to train or improve any third-party products or services (such as OpenAI models).

- Are NOT used to train or improve Microsoft AI models, unless your tenant admin opts in to sharing data with us.

[Learn more about Azure OpenAI Service data privacy and security](/legal/cognitive-services/openai/data-privacy?context=%2Fazure%2Fai-services%2Fopenai%2Fcontext%2Fcontext). To learn more about how Microsoft protects and uses your data more generally, read our [Privacy Statement](https://go.microsoft.com/fwlink/?LinkId=521839).

## Where does my data go? 

Microsoft runs on trust. We're committed to security, privacy, and compliance in everything we do, and our approach to AI is no different. Customer data, including Copilot inputs and outputs, is stored within the Microsoft Cloud trust boundary.

In some scenarios, such as features powered by Bing and third-party copilot plug-ins, customer data might be transmitted outside the Microsoft Cloud trust boundary.

## Can Copilot access encrypted content?

Data is provided to Copilot based on the access level of the current user. If a user has access to encrypted data in Dynamics 365 and Power Platform, and the user provides it to Copilot, then Copilot can access it.

## How does Copilot protect customer data? 

Microsoft is uniquely positioned to deliver enterprise-ready AI. Copilot is powered by Azure OpenAI Service and complies with our existing privacy, security, and regulatory commitments to our customers.

- **Built on Microsoft's comprehensive approach to security, privacy, and compliance.** Copilot is integrated in Microsoft services like Dynamics 365 and Power Platform and inherits their security, privacy, and compliance policies and processes, such as multifactor authentication and compliance boundaries.

- **Multiple forms of protection safeguard organizational data.** Service-side technologies encrypt organizational content at rest and in transit for robust security. Connections are safeguarded with Transport Layer Security (TLS), and data transfers between Dynamics 365, Power Platform, and Azure OpenAI occur over the Microsoft backbone network, ensuring both reliability and safety. [Learn more about encryption in the Microsoft Cloud](/purview/office-365-encryption-in-the-microsoft-cloud-overview).

- **Architected to protect your data at both the tenant and the environment level.** We know that data leakage is a concern for customers. Microsoft AI models are not trained on and don't learn from your tenant data or your prompts, unless your tenant admin has opted in to sharing data with us. Within your environments, you can control access through permissions that you set up. Authentication and authorization mechanisms segregate requests to the shared model among tenants. Copilot utilizes data that only you can access, using the same technology that we've been using for years to secure customer data.

## Are Copilot's responses always factual? 

As with any generative AI, Copilot responses aren't guaranteed to be 100% factual. While we continue to improve responses to fact-based inquiries, you should still use your judgment and review the output before you send it to others. Copilot provides helpful drafts and summaries to help you do more, but it's fully automatic. You always have a chance to review the AI-generated content.

Our teams are working to proactively address issues such as misinformation and disinformation, content blocking, data safety, and promotion of harmful or discriminatory content, in line with our [responsible AI principles](https://www.microsoft.com/ai/our-approach?activetab=pivot1:primaryr5).

We also offer guidance in the user experience to reinforce the responsible use of AI-generated content and suggested actions.

- **Instructions and prompts.** When you use Copilot, prompts and other instructional elements remind you to review and edit responses as needed and to manually check facts, data, and text for accuracy before you use the AI-generated content.

- **Cited sources.** Where applicable, Copilot cites its information sources, whether public or internal, so that you can review them yourself to confirm its responses.

For more information, see the Responsible AI FAQ for your product on Microsoft Learn.

## Does Copilot block prompt injections (jailbreak attacks)? 

[Jailbreak attacks](/azure/ai-services/openai/whats-new#responsible-ai) are user prompts that are designed to provoke the generative AI model into behaving in ways it was trained not to or breaking the rules it's been told to follow. Services across Dynamics 365 and Power Platform are required to protect against prompt injections. [Learn more about jailbreak attacks and how to use Azure AI Content Safety to detect them](/azure/ai-services/content-safety/concepts/jailbreak-detection).

## How does Microsoft test and validate Copilot quality, including prompt injection protection and grounded responses? 

Every new Copilot product and language model iteration must pass an internal responsible AI review before it can be launched. Before release, we use a process called "red teaming" (in which a team simulates an enemy attack, finding and exploiting weaknesses to help the organization improve its defenses) to assess potential risks in harmful content, jailbreak scenarios, and grounded responses. After release, we use automated testing and manual and automated evaluation tools to assess the quality of Copilot responses.

## How does Microsoft enhance the foundation model and measure improvements in grounded responses? 

In the context of AI, especially AI that deals with language models like the one that Copilot is based on, *grounding* helps the AI generate responses that are more relevant and make sense in the real world. Grounding helps ensure that the AI's responses are based on reliable information and are as accurate and relevant as possible. Grounded response metrics assess how accurately the facts stated in the grounding content that's provided to the model are represented in the final response.

Foundation models like GPT-4 are enhanced by Retrieval Augmented Generation (RAG) techniques. These techniques allow the models to use more information than they were trained on to understand a user's scenario. RAG works by first identifying data that is relevant for the scenario, similar to how a search engine identifies web pages that are relevant for the user's search terms. It uses multiple approaches to identify what content is relevant to the user prompt and should be used to ground the response. Approaches include searching against different types of indexes, such as inverted indexes using information retrieval techniques like term matching, or vector indexes using vector distance comparisons for semantic similarity. After it identifies the relevant documents, RAG passes the data to the model along with the current conversation, giving the model more context to better understand the information it already has and generate a response that's grounded in the real world. Finally, RAG checks the response to make sure that it's supported by the source content it provided to the model. Copilot generative AI features incorporate RAG in multiple ways. One example is chat with data using, where a chatbot is grounded with the customer's own data sources.

Another method for enhancing foundational models is known as *fine-tuning*. A large dataset of query-response pairs is shown to a foundational model to augment its original training with new samples that are targeted to a specific scenario. The model can then be deployed as a separate model—one that's fine-tuned for that scenario. While grounding is about making the AI's knowledge relevant to the real world, fine-tuning is about making the AI's knowledge more specific to a particular task or domain. Microsoft uses fine-tuning in multiple ways. For example, we use Power Automate flow creation from natural language descriptions provided by the user.

## How does Copilot block harmful content?

Azure OpenAI Service includes a content filtering system that works alongside core models. The content filtering models for the Hate & Fairness, Sexual, Violence, and Self-harm categories have been specifically trained and tested in various languages. This system works by running both the input prompt and the response through classification models that are designed to identify and block the output of harmful content.

Hate and fairness-related harms refer to any content that uses pejorative or discriminatory language based on attributes like race, ethnicity, nationality, gender identity and expression, sexual orientation, religion, immigration status, ability status, personal appearance, and body size. Fairness is concerned with making sure that AI systems treat all groups of people equitably without contributing to existing societal inequities. Sexual content involves discussions about human reproductive organs, romantic relationships, acts portrayed in erotic or affectionate terms, pregnancy, physical sexual acts, including those portrayed as an assault or a forced act of sexual violence, prostitution, pornography, and abuse. Violence describes language related to physical actions that are intended to harm or kill, including actions, weapons, and related entities. Self-harm language refers to deliberate actions that are intended to injure or kill oneself.

[Learn more about Azure OpenAI content filtering](/azure/ai-services/openai/concepts/content-filter?tabs=warning%2Cpython#harm-categories).

## Does Copilot meet requirements for regulatory compliance? 

Microsoft Copilot is part of the Dynamics 365 and Power Platform ecosystem and meets the same requirements for regulatory compliance. For more information about the regulatory certifications of Microsoft services, go to [Service Trust Portal](https://servicetrust.microsoft.com/). Additionally, Copilot adheres to our commitment to responsible AI, which is put into action through our [Responsible AI Standard](https://www.microsoft.com/ai/responsible-ai). As regulation in AI evolves, Microsoft continues to adapt and respond to new requirements.

[Learn more about Dynamics 365, Power Platform, and Copilot availability, customer data locations, and compliance with global, regional, and industry-specific requirements for managing data](https://dynamics.microsoft.com/availability-reports/).

## Learn more

### Copilot in Dynamics 365 apps and Power Platform

- [Enable copilots and generative AI features in Power Platform](/power-platform/admin/geographical-availability-copilot)
- [Enable Copilot features in Customer Service](/dynamics365/customer-service/administer/configure-copilot-features#region-availability-and-data-movement)
- [Copilot in Dynamics 365 Sales](/dynamics365/sales/copilot-overview)
- [Copilot for Sales architecture](/microsoft-sales-copilot/architecture)
- [Microsoft Copilot Studio overview](/microsoft-copilot-studio/fundamentals-what-is-copilot-studio)
- [AI Copilot overview in Power Apps](/power-apps/maker/canvas-apps/ai-overview)
- [Get started with Copilot in cloud flows – Power Automate](/power-automate/get-started-with-copilot)

### Regional and language availability

[Copilot international availability](https://dynamics.microsoft.com/availability-reports/copilotreport/)

### Data movement across geographies

- [How data movement across regions works](/power-platform/admin/geographical-availability-copilot#how-data-movement-across-regions-works)
- [Configure data movement across geographic locations for generative AI features outside United States](/microsoft-copilot-studio/manage-data-movement-outside-us)
- [Copilot data movement across geographies in Dynamics 365 Sales](/dynamics365/sales/sales-copilot-data-movement)
- [Copilot data movement across geographies in Dynamics 365 Business Central](/dynamics365/business-central/ai-copilot-data-movement)

### Security at Microsoft

- [Introduction to Azure security](/azure/security/fundamentals/overview)
- [Encryption in the Microsoft Cloud](/purview/office-365-encryption-in-the-microsoft-cloud-overview)
- [Data, privacy, and security for Azure OpenAI Service – Azure AI services](/legal/cognitive-services/openai/data-privacy?context=%2Fazure%2Fcognitive-services%2Fopenai%2Fcontext%2Fcontext)

### Privacy at Microsoft

[Microsoft Privacy Statement](https://go.microsoft.com/fwlink/?LinkId=521839)

### Responsible AI

- [Microsoft Responsible AI Standard](https://www.microsoft.com/ai/responsible-ai)
- [Responsible AI FAQ for Microsoft Power Platform](/power-platform/responsible-ai-overview)
- [Responsible AI FAQ for Dynamics 365](/dynamics365/responsible-ai-overview)
- [Responsible AI FAQs for Microsoft Copilot Studio](/microsoft-copilot-studio/responsible-ai-overview)
