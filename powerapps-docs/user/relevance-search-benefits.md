---
title: What is Dataverse search?
description: Dataverse search for model-driven apps helps you quickly find what you're looking for. 
author: shwetamurkute
ms.component: pa-user
ms.topic: article
ms.date: 11/24/2025
ms.subservice: end-user
ms.author: smurkute
ms.custom: 
ms.reviewer: smurkute
ms.assetid: 
search.audienceType: 
  - enduser
ms.contributors:
- mspilde
- JimDaly
---

# What is Dataverse search?

Dataverse search is the foundation that enables Copilot and in-app search experiences to understand and reason over business data, helping organizations turn raw information into actionable intelligence.

<img width="1157" height="580" alt="image" src="https://github.com/user-attachments/assets/84e56b80-f5e5-44de-a5d5-ba53cc17ffef" />

Dataverse search today powers Global Search experiences, API calls, agents built with Copilot Studio, agents run on Microsoft 365 Copilot and MCP tools. As such, in addition to helping users of model-driven apps quickly find what they're looking for, Dataverse search is how Microsoft enables rich search and AI-powered experiences across different products that use Dataverse as one of the data sources.


## What type of data Dataverse search indexes

Dataverse Search is made of Structured data (Tables) and Unstructured data (Files). These can support multiple experiences such as Global Search (that uses structured data), Copilot for model driven apps (that uses structured data) and Copilot Studio agents that use Dataverse knowledge such as files (unstructured data) and Dataverse tables (structured data). See What is Dataverse search? for more information.
Dataverse Search includes three index types:
1. Relevance Search (powers Global Search and SearchQuery API)
2. Structured index
3. Unstructured index

The latter two types power Copilot / generative AI experiences customers commonly see in agents built with Copilot Studio, Copilot in Dynamics 365 experiences, declarative agents, app Copilot / Copilot chat and Dataverse MCP.

<img width="1026" height="384" alt="image" src="https://github.com/user-attachments/assets/4f531873-6586-43fb-b7ae-aea69b9c8997" />
<img width="690" height="484" alt="image" src="https://github.com/user-attachments/assets/b0166a68-b219-460c-97cc-bdbd8e44fe57" />



### What is the value of indexed data

Dataverse search is made of indexed Dataverse data that helps a system perform more efficient searches. Indexed Dataverse data is enterprise content that is organized in a specific structure, like a data catalog. By having an agent or a system leveraging the indexed data structure, it helps increase the performance of a search, based on a specific input.


## Experiences enabled by Dataverse search

Dataverse search lets you use multiple features in Power Platform, including Copilot indexes. These experiences include:

**Microsoft Copilot Studio Agents**

- [Add Files as a knowledge source](/microsoft-copilot-studio/knowledge-add-file-upload)
- [Add Dataverse as a knowledge source](/microsoft-copilot-studio/knowledge-add-dataverse)
- [Add Sharepoint as a knowledge source](/microsoft-copilot-studio/knowledge-add-sharepoint)
- [Add OneDrive as a knowledge source](/microsoft-copilot-studio/knowledge-add-unstructured-data)
- [Agent Copilot](/microsoft-copilot-studio/guidance/generative-ai-math-data-queries)

**Dynamics 365 Copilots**

- [Sales Copilot](/dynamics365/sales/copilot-overview)
- [Customer Service Copilot](/dynamics365/contact-center/use/use-copilot-features)
- [Contact Center Copilot](/dynamics365/contact-center/administer/configure-copilot-features)
- [Field Service Copilot](/dynamics365/field-service/copilot-side-pane)

**Power Apps – Model-Driven Apps**

- [Copilot for app users in model-driven apps](/power-apps/maker/model-driven-apps/add-ai-copilot)
- [Dataverse search](/power-platform/admin/configure-relevance-search-organization)

**Experiences across the Power Platform**

- [In Power Apps / Power Automate](/ai-builder/prompt-library)
- [In Microsoft Copilot Studio](/microsoft-copilot-studio/nlu-prompt-node)
- [Power Apps / Power Automate - Custom AI Prompts](/ai-builder/create-a-custom-prompt)


### How Dataverse Search is used across experiences:

<img width="1026" height="384" alt="image" src="https://github.com/user-attachments/assets/1509bf10-c9ea-42d9-85e0-155e431006ae" />
<img width="797" height="495" alt="image" src="https://github.com/user-attachments/assets/c664300f-afaa-4c71-b030-cbe376ed2562" />


## Benefits of Dataverse Search:

1.	**Integration with AI / Copilot experiences**
    Users can have a “conversation” with their data and identify themes, patterns and insights using natural language. Applies AI technology to interpret natural language such as misspellings, common abbreviations, and synonyms to deliver quality results.
  	
2.	**Unified Search**
    Dataverse search lets you quickly find content in model-driven apps and other products that use Dataverse as a data through a single unified search experience. Provides a better user experience compared to [quick find](quick-find.md) search, where all words in the search term must be found in one column. 
  	
3.	**Efficient Relevance-Based Results**
    Intelligent ranking algorithms to return the most relevant records first, with a performance that's superior to [categorized search](quick-find.md#multiple-table-quick-find-categorized-search), reducing time spent searching and increasing its accuracy.
  	
4.  **Smart fuzzy search**
    Handles variations in spelling and terminology, so it does not depend on exact keyword matches.
    
5.	**Security and Compliance**
    Respects Dataverse security roles and permissions: users can only see search results for records that they have access to.
  	
6.	**Scalability and Performance**
    Optimized for large datasets and supports multiple data types (such as Choice and Lookups).

7.   **Search across documents in Microsoft Dataverse**
      Includes search results for text in documents that are stored in Dataverse such as PDF, Microsoft Office documents, HTML, XML, ZIP, EML, plain text, and JSON file formats. It also searches text in notes and attachments.

> Note: Global Search supports up to 2MB of file search.


## Dataverse Search implications

Dataverse search is an opt-out feature, for which setting is set to On for all new production environments and Default for all other environment types. This setting can be found in PPAC > Manage > Environment > Setting > Product > Features > Dataverse Search:
<img width="1125" height="582" alt="image" src="https://github.com/user-attachments/assets/ee6047e9-fe9a-4796-89e5-c6f59b518b46" />

In Power Platform admin center, admins can [leverage the Dataverse Search setting](power-platform/admin/configure-relevance-search-organization#managing-dataverse-search) to manage it. The state selected for Dataverse Search impacts the ability to leverage Dataverse data across the enabled experiences for all the organization.
The following tables show how each Dataverse Search setting impact Global Search experiences (including SearchQuery API) and Generative AI experiences, and how can Admins leverage this setting to manage it:

## What Dataverse Search setting means for Global Search

When Dataverse search is set to "On", the Global Search search box appears at the top of every page in your model-driven app and is the default global search experience for all model-driven apps.
For more information please refer to: [Search for records by using Dataverse search - Power Apps | Microsoft Learn.](https://learn.microsoft.com/en-us/power-apps/user/relevance-search)

| Dataverse Search set to On	|  Dataverse Search set to Default	|   Dataverse Search set to Off  |
|-----------------------------|-----------------------------------|--------------------------------|
| Search bar is visible. (Quick Find is not visible/accessible)  |	Search bar is not visible (Quick Find can be used alternatively).  |	Search bar is not visible  |  Quick Find can be used alternatively.)  |
|  Dataverse Search is used for all production environments  |  Dataverse Search is not available for Global Search in any environment	|  Dataverse Search is not available for Global Search in any environment  |
|  Dataverse data is automatically indexed = data is searchable  |  Dataverse data is not indexed = data is not searchable	|  Dataverse data is not indexed = data is not searchable  |


## What Dataverse Search means for Generative AI enabled experiences

Some Generative AI experiences are enabled by Dataverse Search data. When enabled, Copilot chat can be accessed through the Copilot icon in the right navigation bar in a model-driven app. The Copilot chat pane can be opened or minimized as desired.
-	**Power Apps**: [Copilot chat for model-driven apps in Power Apps]([url](https://learn.microsoft.com/en-us/power-apps/maker/model-driven-apps/add-ai-copilot)) is a next-generation AI assistant that helps app users get insights about the data in their apps through conversation in natural language.
- **Copilot Studio**: [Integrating Dataverse tables as your knowledge source]([url](https://learn.microsoft.com/en-us/microsoft-copilot-studio/knowledge-add-dataverse)) allows you to ground your agent in the data contained in your tables. This can also happen using [unstructured data as knowledge]([url](https://learn.microsoft.com/en-us/microsoft-copilot-studio/knowledge-unstructured-data)) or [Dataverse tools]([url](https://learn.microsoft.com/en-us/microsoft-copilot-studio/advanced-plugin-actions)).

| Dataverse Search set to On	|  Dataverse Search set to Default	|   Dataverse Search set to Off  |
|-----------------------------|-----------------------------------|--------------------------------|
|  An enabled Generative AI  feature’s availability is not managed by Dataverse Search itself = may be enabled via its own feature setting  |
|  Dataverse Search is used in all production environments	|  Dataverse Search is used for Gen. AI experiences in Sandbox, Trial, Developer, Dataverse for Teams environments	|  Dataverse Search is not used in any environment  |
|  Dataverse prompts and knowledge (Tables / Files) is automatically indexed = data is searchable  |  Dataverse prompts and knowledge (Tables / Files) is indexed when triggered = data is searchable (i.e. Copilot is prompted)	|  Dataverse data is not indexed = data is not searchable  |

## What actions can Makers or Admins take to manage Dataverse Search efficiently?

Depending on the experience that leverages Dataverse Search and its usage, consumption size may increase more drastically. As such, below are some recommendations to optimize storage consumption for an efficient and value-added output, from a more granular / less impactful (data level) to a more broad and impactful action (environment level).

### Data level:

To manage search index at the data level, Makers can review each table and each column to confirm that search is needed. If not, the Maker can take the following actions:
1.	**Global Search: Break down tables into multiple columns**

**Why**
Indexed data often includes additional structures like inverted indexes, metadata, and pointers to enable fast search and retrieval, which adds overhead beyond the raw data. These extra components can significantly increase storage requirements compared to the original dataset.

**How**
- Ensuring the data is consistently formatted across records helps increase repetitiveness of words, reducing the number of indexes.
- By breaking down the data across multiple columns, you can be more specific around which data to search over:

Example:
Instead of using a single column with a long, inconsistent text string such as the following "Address" column:
|   Address (Searchable)  |
|-------------------------|
|  1234 Main St, NY 98052  |
|  7890 Main Street, NY 98052  |

Consider breaking the data into separate columns and only select the specific attributes that would make the search more valuable:

|  Street Number |  Street |  City	(Searchable) |  Zip Code  (Searchable) |
|----------------|---------|---------------------|-------------------------|
|  1234  |  Main Street	|  NY  |	 98052  |
|  7890  |  Main Street	 |  NY	|  98052  |

> **Note**: While this action helps reduce some of the indexed data, the impact on Dataverse Search consumption is relative to the baseline consumption. For more drastic approaches, go through the other steps, in order of recommendation.


2.	**Global Search: Only select columns that need to be “searchable”**

**Why**
There are default selected columns for Dataverse search. By default, certain columns such as Primary Name and ID are indexed for all tables, which are part of the 50 fields indexed by default and are not counted for every table. 
Furthermore, columns are enabled for Dataverse search only if a Quick Find view is set as the default view for the table. (Know more at /configure-relevance-search-organization?tabs=new#managing-dataverse-search)

**How to unselect tables that are not being used so that they are not indexed / searchable**
1.	Go to Power Apps
 
2.	In the navigation pane, select Solutions
 
3.	Choose the solution you want to modify, then select Edit in the command bar:
 
4.	On the Objects page, in the navigation pane, select Overview:
 
5.	In the Dataverse search pane, select Manage search index:
 
6.	This will show all tables that are indexed:
 
7.	Unselect the tables and Save the change:
 
 
**How to unselect columns that are not being used so that they are not indexed / searchable**
1.	Go to Power Apps
 
2.	In the navigation pane, select Tables:
 
3.	On the Tables page, select the table you want to edit.
 
4.	In the Data experiences pane, select Views
 
5.	From the list of views, select the Quick Find View type. For example, select Quick Find Active Accounts.
 
6.	Edit View columns
 
7.	Go to the desired column(s) to remove and in the dropdown menu, select Remove
 
8.	Select Save and Publish to publish the changes to the view:
 

> Note: If this action is exclusively taken, additional Dataverse Search consumption may be incurred, triggered by other experiences, such as a Generative AI experience.


3.	**Copilot Studio: Ensure specific Dataverse Tables or files are added to Copilot Studio agent’s knowledge**

**Why**
When a Dataverse tool or knowledge such as Dataverse MCP, Dataverse table or file is added to a Copilot Studio agent, all the underlying Dataverse data is processed and indexed for efficient, semantically relevance based searches.
Reducing knowledge and tools to strictly the necessary content not only helps indexing processing and storage consumption but also helps increasing the quality of the searches.

**How to remove unnecessary content or imagery / tables from files**
-	File Upload, OneDrive and Sharepoint upload: On the files themselves, reduce the file to the needed content. Consider removing pages, sheets or any accessory data point from the files.
- OneDrive and Sharepoint upload: Ensure that only selected files or folders are needed instead of selecting nested folders.

> Note: If this action is exclusively taken, additional Dataverse Search consumption may be incurred, triggered by other experiences, such as a Global Search (if Dataverse Search is set to “On” for the environment).


### App / Agent level:

To manage search index at the app or agent level, review purpose and usage of each application and agent to confirm that search is needed. If not, the Maker can take the following actions:

4.	**Copilot for Power Apps: Specify which applications you'd like COpilot to be enabled for**
**Why**
Copilot in model-driven apps uses AI to interpret natural language queries and generate suggestions or actions based on the app’s underlying Dataverse data. It leverages semantic indexing and context from the app’s schema to provide relevant answers and automate tasks within the application. In some situations, applications do not require that level of enhanced search through Copilot, thus managing Copilot at an app level may help with consumption control.

**How to turn off Copilot feature for each model-driven application**
1.	Open the model-driven app in the app designer for Edit:
 
2.	Select Settings from the command bar:
 
3.	On the Settings screen, click on Upcoming:
 
4.	Click on the “Copilot control” setting:
 
5.	Set the Copilot control to Off:
 
6.	Save and Publish the model-driven app for the changes to take effect:
 

> Notes:
> - Even if this action is taken, additional Dataverse Search consumption may be incurred, triggered by other experiences, such as a Dynamics 365 Copilot for Sales.


5.	**Copilot for Dynamics 365 Apps: Specify which applications you'd like Copilot to be enabled for**
**Why**
Just like model driven applications in Power Apps, Copilot in model-driven apps uses AI to interpret natural language queries and generate suggestions or actions based on the app’s underlying Dataverse data. In some situations, applications do not require that level of enhanced search through Copilot, thus managing Copilot at an app level may help with consumption control.

**How to turn off Copilot feature for each Dynamics 365 application**
1.	In the Sales Hub app, go to Change area in the lower-left corner of the page  
2.	Select App Settings:
 
3.	Sales Settings opens:
 
4.	Select Copilot:
 
5.	Select Edit settings:
 
6.	Select “Advanced settings”:
 
7.	A new Copilot in Dynamics 365 Sales appears:
 
8.	Select “Individual apps”:
 
9.	Select desired app and turn the setting to “Off”:
 
**How to turn off Copilot feature for each Dynamics 365 application**
1.	Repeat the steps 1-7 and select “All Apps”:
 
2.	OR Repeat steps 1-5 above
   
4.	Change dropdown to “Off”, which prompts the modal to appear:
 
5.	Select “Continue” and save changes: 

> Note: If this action is exclusively taken, additional Dataverse Search consumption may be incurred, triggered by other experiences, such as Copilot for Power Apps, or agents using Dataverse knowledge in Copilot Studio.



6.	**Copilot Studio: Remove all Dataverse tools, Dataverse Tables or files from Copilot Studio agent’s knowledge**
**Why**
Dataverse tables and files in Copilot Studio knowledge leverage indexed data by creating semantic indexes that map content and relationships for fast, context-aware retrieval. These indexes enable Copilot to interpret natural language queries and deliver precise answers or actions based on structured and unstructured data.

**How to remove Dataverse Tables or files from Copilot Studio agent’s knowledge**
The same instructions are applicable for the following knowledge sources:
-	Dataverse Tables
-	Files uploaded
-	OneDrive files
-	Sharepoint files (from upload)

1.	In the Overview or Knowledge tabs, on a Copilot Studio agent, go to the “Knowledge” section and select the dot menu for each of the Dataverse-enabled knowledge source:
 
2.	Select “Delete” when the modal appears:
 
> Note: If this action is exclusively taken, additional Dataverse Search consumption may be incurred, triggered by other experiences, such as a Copilot in Power Apps or Dynamics 365.
> Note: The same process is applicable to Dataverse MCP tools, except it happens in the Tools section (as opposed to the Knowledge section).



### Environment level:
To manage search index at the environment level, Admins can review purpose and usage of each application and agent, as well as Global Search to confirm that search is needed. If not, Admins can take the following actions:

7.	**Global Search not needed: Just focus on Copilot experiences**
**Why**
When Dataverse Search is set to “Default”, the Global Search experience is not enabled on the navigation of the model-driven apps or Dynamics 365. This means that users cannot query Global Search nor data that is marked as “searchable” for exclusive purpose of Global Search will be indexed, while still allowing for Dataverse data to be indexed for other experiences, such as Copilot in Copilot Studio or in model driven applications.

**How to change Dataverse Search to “Default”**
1.	In Power Platform Admin Center go to Manage > Environments:
 
2.	Select environment and then select “Settings”:
 
3.	Go to Product > Features:
 
4.	Change “Dataverse search” to “Default”:
 
5.	Save changes

> Notes:
> For organizations that want to search in these applications and don’t need relevance-based search, they can enable [Quick Find]([url](https://learn.microsoft.com/en-us/power-apps/user/quick-find)).
> If this action is exclusively taken, additional Dataverse Search consumption may be incurred, triggered by other experiences, such as Copilot for Power Apps, or agents using Dataverse knowledge or tools in Copilot Studio.


8.	**Copilot for Power Apps and Dynamics 365 apps not needed: Focus just on Global Search**
**Why**
Copilot in Power Apps uses Dataverse indexed data to quickly retrieve and interpret relevant records when responding to natural language queries within the model driven app. The semantic indexes enable efficient search across tables and relationships, allowing Copilot to provide accurate suggestions and automate actions based on the underlying data context. For organizations that do not want Copilot to be used with their model-driven applications, Admins can turn the feature off at an environment level.

**How to turn off the “Copilot” setting in Power Platform Admin Center**
1.	In Power Platform Admin Center go to Manage > Environments:
 
2.	Select environment and then select “Settings”:
 
3.	Go to Product > Features:
 
4.	Turn the toggle and the set the dropdown to “Off”:
 

> Note: If this action is exclusively taken, additional Dataverse Search consumption may be incurred, triggered by other experiences, such as agents using Dataverse knowledge in Copilot Studio.



9.	**Dataverse Search is not needed for the environment.**
**Why**
At any time, Dataverse can be manually set to "Off". If Dataverse search is set to "Off" for the environment, you can't use the search capability in the Power Apps navigation bar or any generative AI experience that relies on Dataverse, like uploaded files or using OneDrive or Sharepoint files in Microsoft Copilot Studio agents, among other experiences. 

**How to turn off Dataverse Search for the environment**
1.	In Power Platform Admin Center go to Manage > Environments:
 
2.	Select environment and then select “Settings”:
 
3.	Go to Product > Features:
 
4.	Change “Dataverse search” to “Off”. This prompts a confirmation modal. Acknowledge the impact of turning Dataverse Search off, write the name of the environment and select “Turn Off”:
 
5.	Save changes:
 
> Notes:
> -	Turning off Dataverse search deprovisions and removes the index within a period of 12 hours. If you turn on Dataverse search after its been off for 12 hours, it provisions a fresh index that needs to go through a full sync. Syncing may take up to an hour or more for average size organizations, and a couple of days for large organizations. Be sure to consider these implications when you turn off Dataverse search temporarily. ([Configure Dataverse search for your environment]([url](https://learn.microsoft.com/en-us/power-platform/admin/configure-relevance-search-organization?tabs=new)))
> -	Index removal (or provisioning) can take multiple days to be completed, depending on the amount of Dataverse Search consumption. Example: an organization with 10GB of indexed data may take 1 day to clean up all indexes, while an organization with 500GB may take multiple days to see it reflected in Dataverse search reporting. Please give a few days or a week before sumitting a support ticket, to ensure a complete removal of Dataverse Search indexed data.


## What happens if Dataverse search is turned off?

| Feature |	Maker experience | End User Experience|
|---------|------------------|--------------------|
| Microsoft Copilot Studio Agent – Add Knowledge  | You can't upload files. You can't select Dataverse tables. The agent doesn't provide results that rely on this indexed data until Dataverse search is enabled for the environment. Ask the environment's admin to enable Dataverse search.  | The agent doesn't provide results that rely on this indexed data until Dataverse search is enabled for the environment. The agent uses the fallback answer by default.  |
| Microsoft Copilot Studio Agent – Using Copilot Chat	|	The agent doesn't provide results that rely on this indexed data until Dataverse search is enabled for the environment. Ask your environment admin to enable Dataverse search.  | The agent doesn't provide results that rely on this indexed data until Dataverse search is enabled for the environment. By default, the agent uses a fallback answer. |
| Model Driven Applications – Dataverse search  |	The search bar isn't visible in model-driven apps. | Search bar isn't visible in model-driven apps |

### See also

[Search for tables and rows by using Dataverse search](relevance-search.md)<br/>
[Configure facets and filters](facets-and-filters.md)<br/>
[Frequently asked questions about Dataverse search](relevance-faq.md)<br />
[Developer's guide: Search for Dataverse records using the API](../developer/data-platform/search/overview.md)<br/>
[Compare search options in Microsoft Dataverse](search.md)

[!INCLUDE[footer-include](../includes/footer-banner.md)]
