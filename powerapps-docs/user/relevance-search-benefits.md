---
title: What is Dataverse search?
description: Dataverse search for model-driven apps helps you quickly find what you're looking for. 
author: shwetamurkute
ms.component: pa-user
ms.topic: article
ms.date: 01/13/2026
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

Dataverse search is the foundation that enables Copilot and in-app search experiences to understand and process business data. It turns raw information into actionable intelligence.

:::image type="content" source="media/dataverse-types.png" alt-text="Screenshot of Dataverse types and clients." lightbox="media/dataverse-types.png":::

Dataverse search powers global search experiences, API calls, and agents built with Copilot Studio, including those running on Microsoft 365 Copilot and MCP tools. Beyond helping users of model-driven apps quickly, find what they need, Dataverse search enables rich search and AI-driven experiences across products that use Dataverse as a data source.


## What type of data does Dataverse search index?

Dataverse search includes structured data (tables) and unstructured data (files). 

:::image type="content" source="media/dataverse-search-structured.png" alt-text="Screenshot of Dataverse showing structured data examples." lightbox="media/dataverse-search-structured.png":::

:::image type="content" source="media/dataverse-search-unstructured.png" alt-text="Screenshot of Dataverse showing unstructured and structured data examples." lightbox="media/dataverse-search-unstructured.png":::

Legend:
1. **Structured data**: Supports multiple experiences, including global search, Copilot for model-driven apps, and Copilot Studio agents that use Dataverse knowledge from tables.
1. **Unstructured data**: Supports experiences like Copilot Studio agents that use Dataverse knowledge from files.


Dataverse search includes three index types:
- **Relevance search**: Powers global search and SearchQuery API.
- **Structured index**: Enables Copilot and generative AI experiences.
- **Unstructured index**: Enables Copilot and generative AI experiences.

The structured and unstructured indexes enable Copilot and generative AI experiences in scenarios such as agents built with Copilot Studio, Copilot in Dynamics 365, declarative agents, app Copilot, Copilot chat, and Dataverse MCP.

### What's the value of indexed data?

Dataverse search uses indexed Dataverse data to help systems perform more efficient searches. Indexed Dataverse data is enterprise content that's organized in a specific structure, like a data catalog. When an agent or system uses the indexed data structure, search performance increases based on a specific input.


## Experiences enabled by Dataverse search

Dataverse search lets you use multiple features in Power Platform, including Copilot indexes. Here are the experiences:

**Microsoft Copilot Studio Agents**

- [Add files as a knowledge source](/microsoft-copilot-studio/knowledge-add-file-upload)
- [Add Dataverse as a knowledge source](/microsoft-copilot-studio/knowledge-add-dataverse)
- [Add SharePoint as a knowledge source](/microsoft-copilot-studio/knowledge-add-sharepoint)
- [Add OneDrive as a knowledge source](/microsoft-copilot-studio/knowledge-add-unstructured-data)
- [Agent Copilot](/microsoft-copilot-studio/guidance/generative-ai-math-data-queries)

**Dynamics 365 Copilots**

- [Sales Copilot](/dynamics365/sales/copilot-overview)
- [Customer Service Copilot](/dynamics365/contact-center/use/use-copilot-features)
- [Contact Center Copilot](/dynamics365/contact-center/administer/configure-copilot-features)
- [Field Service Copilot](/dynamics365/field-service/copilot-side-pane)

**Power Apps: Model-driven apps**

- [Copilot for app users in model-driven apps](/power-apps/maker/model-driven-apps/add-ai-copilot)
- [Dataverse search](/power-platform/admin/configure-relevance-search-organization)

**Experiences across the Power Platform**

- [In Power Apps or Power Automate](/ai-builder/prompt-library)
- [In Microsoft Copilot Studio](/microsoft-copilot-studio/nlu-prompt-node)
- [Power Apps or Power Automate—custom AI prompts](/ai-builder/create-a-custom-prompt)


## Benefits of Dataverse search

1. **Integration with AI and Copilot experiences:**
By using natural language, you can have a conversation with your data and identify themes, patterns, and insights. This feature uses AI technology to interpret natural language, such as misspellings, common abbreviations, and synonyms, to deliver quality results.
1. **Unified search:**
Dataverse search lets you quickly find content in model-driven apps and other products that use Dataverse as a data source. It provides a better user experience than [quick find](quick-find.md), where all words in the search term must be found in one column.     
1. **Efficient relevance-based results:**
Intelligent ranking algorithms return the most relevant records first, with performance that's superior to [categorized search](quick-find.md#multiple-table-quick-find-categorized-search). This feature reduces time spent searching and increases accuracy.
1. **Smart fuzzy search:**
Dataverse search handles variations in spelling and terminology, so it doesn't depend on exact keyword matches.
1. **Security and compliance:**
Dataverse search respects Dataverse security roles and permissions. Users can only see search results for records that they have access to.
1. **Scalability and performance:**
Dataverse search is optimized for large datasets and supports multiple data types, such as Choice and Lookup.
1. **Search across documents in Microsoft Dataverse:**
Dataverse search includes search results for text in documents that are stored in Dataverse, such as PDF, Microsoft Office documents, HTML, XML, ZIP, EML, plain text, and JSON file formats. It also searches text in notes and attachments.

> [!NOTE]
> Global search supports up to 2 MB of file search.


## Dataverse search implications

Dataverse search is an opt-out feature. The feature is **On** for all new production environments and set to **Default** for all other environment types. 
Find this setting in [Power Platform admin center](https://admin.powerplatform.microsoft.com/) by going to **Manage** > **Environment** > **Settings** > **Product** > **Features** > **Dataverse Search**.

:::image type="content" source="media/dataverse-search-admin.png" alt-text="Screenshot of Dataverse search option in Power Platform admin center." lightbox="media/dataverse-search-admin.png":::


In Power Platform admin center, admins can [use the Dataverse Search setting](/power-platform/admin/configure-relevance-search-organization?tabs=new#managing-dataverse-search) to manage search. The selected Dataverse search state affects how to use Dataverse data across the enabled experiences for the entire organization.
The following tables show how each Dataverse search setting affects global search experiences (including SearchQuery API) and Generative AI experiences, and how admins can use this setting to manage it.

### What Dataverse search setting means for global search

When you set Dataverse search to **On**, the **Global Search** box appears at the top of every page in your model-driven app. This search box is the default global search experience for all model-driven apps.
Learn more in [Search for records by using Dataverse search](relevance-search.md).

| Dataverse search set to On	|  Dataverse search set to Default	|   Dataverse Search set to Off  |
|-----------------------------|-----------------------------------|--------------------------------|
| Search bar is visible. (Quick Find isn't visible or accessible)  |	Search bar isn't visible. (Quick Find is an alternative)  |	Search bar isn't visible.  (Quick Find is an alternative.)  |
|  Dataverse search is used for all production environments  |  Dataverse search isn't available for Global search in any environment	|  Dataverse search isn't available for Global search in any environment  |
|  Dataverse data is automatically indexed. Data is searchable for global search  |  Dataverse data isn't indexed. Data isn't searchable for global search	|  Dataverse data isn't indexed. Data isn't searchable for global search  |


### What Dataverse search means for generative AI enabled experiences

Some generative AI experiences use Dataverse search data, such as Copilot chat in model-driven applications. You can access Copilot chat through the Copilot icon in the right navigation bar in a model-driven app. You can open or minimize the Copilot chat pane as needed.
-	**Power Apps**: [Copilot chat for model-driven apps in Power Apps](../maker/model-driven-apps/add-ai-copilot.md) is a next-generation AI assistant that helps app users get insights about the data in their apps through conversation in natural language.
- **Copilot Studio**: [Integrating Dataverse tables as your knowledge source](/microsoft-copilot-studio/knowledge-add-dataverse) allows you to ground your agent in the data contained in your tables. This integration can also happen by using [unstructured data as knowledge](/microsoft-copilot-studio/knowledge-unstructured-data) or [Dataverse tools](/microsoft-copilot-studio/advanced-plugin-actions).

> [!NOTE]
> An enabled generative AI feature's availability isn't managed by Dataverse search itself and is enabled through its own feature setting.

| Dataverse search set to **On**	|  Dataverse search set to Default	|   Dataverse search set to **Off**  |
|-----------------------------|-----------------------------------|--------------------------------|
|  All production environments use Dataverse search	|  Sandbox, Trial, Developer, Dataverse for Teams environments use Dataverse search for generative AI experiences	|  No environment uses Dataverse search  |
|  Dataverse data is automatically indexed and becomes searchable  |  Dataverse data (tables and files) is indexed when triggered and becomes searchable	|  Dataverse data isn't indexed nor searchable  |

## What actions can makers or admins take to manage Dataverse search efficiently?

Depending on the experience that uses Dataverse search and its usage, consumption size can increase. The following recommendations help you optimize storage consumption for efficient and value-added output, from granular and less impactful actions (data level) to broader and more impactful actions (environment level).

> [!NOTE]
> While one action helps optimize the amount of indexed data within a specific feature, other enabled features might trigger index provisioning. For more impactful approaches, go through all the steps, in order of recommendation, or consider turning off features in the Power Platform admin center.


### Data level

To manage the search index at the data level, review each table and each column to confirm that search is needed. If not, take the following actions:

#### Global Search: Break down tables into multiple columns

##### Why this helps?
Indexed data includes structures like inverted indexes, metadata, and pointers to enable fast search and retrieval. These components add overhead beyond the raw data and can significantly increase storage requirements compared to the original dataset.

##### How to implement?
- Ensure the data is consistently formatted across records to increase repetitiveness of words and reduce the number of indexes.
- By breaking down the data across multiple columns, you can be more specific about which data to search over.

#### Global Search: Only select columns that need to be searchable

##### Why this helps?
Dataverse search has default selected columns. By default, certain columns like Primary Name and ID are indexed for all tables. These columns are part of the 50 fields indexed by default and don't count toward the limit for every table.
Enable columns for Dataverse search only if a Quick Find view is set as the default view for the table. For more information, see [Managing Dataverse search](/power-platform/admin/configure-relevance-search-organization?tabs=new#managing-dataverse-search).

##### How to unselect tables that aren't used so that they're not indexed or searchable
1. Sign in to [Power Apps](https://make.powerapps.com/).
1. On the left navigation pane, select **Solutions**.
1. Choose the solution you want to modify, and then select **Edit** in the command bar.
1. On the **Objects** page, in the navigation pane, select **Overview**.
1. In the Dataverse search pane, select **Manage search index**.
1. Review the tables that are indexed.
1. Unselect the tables, and then select **Save**.
 
 
##### How to unselect columns that aren't used so that they're not indexed or searchable
1. Sign in to [Power Apps](https://make.powerapps.com/).
1. On the left navigation pane, select **Tables**.
1. On the **Tables** page, select the table you want to edit.
1. In the **Data experiences** pane, select **Views**.
1. From the list of views, select the Quick Find view type. For example, select **Quick Find Active Accounts**.
1. Edit **View columns**.
1. Go to the columns you want to remove, and select **Remove** in the dropdown menu.
1. Select **Save and Publish** to publish the changes to the view.
 

#### Copilot Studio: Ensure specific Dataverse tables or files are added to Copilot Studio agent's knowledge

##### Why this helps?
When you add a Dataverse tool or knowledge, such as Dataverse MCP, Dataverse table, or file to a Copilot Studio agent, the process automatically indexes all the underlying Dataverse data for efficient, semantically relevant searches.
Reducing knowledge and tools to only the necessary content helps indexing processing and storage consumption and increases search quality.

##### How to remove unnecessary content or imagery, or tables from files
- **File Upload, OneDrive, and SharePoint upload**: Remove files that aren't needed for search from the agent's knowledge base. You might want to consider removing pages, sheets, or any accessory data point from the files themselves.
- **OneDrive and SharePoint upload**: Select only the files or folders you need instead of selecting nested folders.

##### How to remove Dataverse tables or files from Copilot studio agent’s knowledge

In the **Overview** or **Knowledge** tabs on a Copilot Studio agent, go to the **Knowledge** section and select the dot menu for each of the Dataverse-enabled knowledge sources, and then select **Delete**.
Use the same instructions for the following knowledge sources:
-	Dataverse Tables
-	Files you upload
-	OneDrive files
-	SharePoint files (from upload)
 
> [!NOTE]
> The same process applies to Dataverse MCP tools, but you complete it in the Tools section (instead of the Knowledge section).

### App or agent level

To manage the search index at the app or agent level, review the purpose and usage of each application and agent to confirm search is needed. If not, take the following actions:

#### Copilot for Power Apps: Specify which applications you'd like Copilot to be enabled for

##### Why this helps?
Copilot in model-driven apps uses AI to interpret natural language queries and generates suggestions or actions based on the app's underlying Dataverse data. In some situations, applications don't require enhanced search through Copilot, so managing Copilot at an app level can help control consumption.

##### How to turn off Copilot feature for each model-driven application
1. In the app designer, open the model-driven app for editing.
1. Select **Settings** from the command bar.
1. On the **Settings** screen, select **Upcoming**.
1. Select the **Copilot control** setting, and set it to **Off**.
1. Select **Save and Publish** to apply your changes.


#### Copilot for Dynamics 365 Apps: Specify which applications you'd like Copilot to be enabled for

##### Why this helps?
Just like model-driven applications in Power Apps, Copilot in model-driven apps uses AI to interpret natural language queries and generate suggestions or actions based on the app's underlying Dataverse data. In some situations, applications don't require that level of enhanced search through Copilot. Managing Copilot at an app level can help with consumption control.

##### How to turn off Copilot feature for each Dynamics 365 application

1. In the Sales Hub app, change the area by using the option in the lower-left corner of the page.
1. Select **App Settings** to open sales setting.
1. Select **Copilot** > **Edit settings** > **Advanced settings**, which opens a new Copilot in Dynamics 365 Sales page.
1. Select **Individual apps**.
1. Select desired app and turn the setting to **Off**.
 
##### How to turn off Copilot feature for all Dynamics 365 application

1. In the Sales Hub app, change the area by using the option in the lower-left corner of the page.
1. Select **App Settings** to open sales setting.
1. Select **Copilot** > **Edit settings** > **Advanced settings**, which opens a new Copilot in Dynamics 365 Sales page.
1. Select **All Apps** and turn the setting to **Off**.
 
The other way to turn off Copilot feature for all apps is as follows:

1. In the Sales Hub app, change the area by using the option in the lower-left corner of the page.
1. Select **App Settings** to open sales settings.
1. Select **Copilot** > **Edit settings**.
1. Select **Off** from the Copilot dropdown, which opens a dialog box.
1. Select **Continue**, and then save your changes. 

### Environment level
To manage the search index at the environment level, admins can review the purpose and usage of each application and agent, as well as global search to confirm that search is needed. If not, admins can take the following actions:

#### Global search is disabled while Copilot experiences are enabled

##### Why this helps?
When Dataverse search is set to **Default**, the global search experience isn't enabled on the navigation of the model-driven apps or Dynamics 365. This setting means that users can't query global search, and data marked as "searchable" for the exclusive purpose of global search isn't indexed. However, Dataverse data might still be indexed for other experiences, such as Copilot in model-driven applications or Copilot Studio agents.

##### How to change Dataverse search to Default value
1. In Power Platform admin center, go to **Manage** > **Environments**.
1. Select the environment, and then select **Settings**.
1. Select **Product** > **Features**.
1. Change **Dataverse search** to **Default**.
1. Select **Save**.

> [!NOTE]
> For organizations that want to search in these applications and don't need relevance-based search, they can enable [Quick Find](quick-find.md).

#### Copilot for Power Apps and Dynamics 365 apps is disabled while global search is anabled

##### Why this helps?
Copilot in Power Apps uses Dataverse indexed data to quickly retrieve and interpret relevant records when responding to natural language queries within the model-driven app. The semantic indexes enable efficient search across tables and relationships, allowing Copilot to provide accurate suggestions and automate actions based on the underlying data context. For organizations that don't want Copilot to be used with their model-driven applications, admins can turn off the feature at an environment level.

##### How to turn off the Copilot setting in Power Platform admin center
1. In Power Platform admin center, go to **Manage** > **Environments**.
1. Select the environment, and then select **Settings**.
1. Select **Product** > **Features**.
1. Turn the toggle and the set the dropdown to **Off**:
 

#### Dataverse search isn't needed for the environment

##### Why this helps?
At any time, you can manually set Dataverse to **Off**. If you set Dataverse search to "Off" for the environment, all users of features, apps, or agents of the environment can't use the search capability in the Power Apps navigation bar or any generative AI experience that relies on Dataverse, like uploaded files or using OneDrive or SharePoint files (via upload) in Microsoft Copilot Studio agents, among other experiences.  

##### How to turn off Dataverse search for the environment
1. In Power Platform admin center, go to **Manage** > **Environments**.
1. Select the environment, and then select **Settings**.
1. Select **Product** > **Features**.
1. Change **Dataverse search** to **Off**. This change opens a dialog box. Acknowledge the impact of turning off Dataverse search, write the name of the environment, and select **Turn Off**:
1. Select **Save**.
 
> [!NOTE]
> - Turning off Dataverse search deprovisions and removes the index within a period of 12 hours. If you turn on Dataverse search after it's been off for 12 hours, it provisions a fresh index that needs to go through a full sync. Syncing might take up to an hour or more for average size organizations, and a couple of days for large organizations. Be sure to consider these implications when you turn off Dataverse search temporarily. [Configure Dataverse search for your environment](/power-platform/admin/configure-relevance-search-organization)
> -	Index removal (or provisioning) can take multiple days to be completed, depending on the amount of Dataverse search consumption. For example, an organization with 10 GB of indexed data might take one day to clean up all indexes, while an organization with 500 GB might take multiple days to see it reflected in Dataverse search reporting. Give a few days or a week before submitting a support ticket, to ensure a complete removal of Dataverse search indexed data.


## What happens when you turn off Dataverse search?

| Feature | Maker experience | End user experience |
|---------|------------------|--------------------|
| Microsoft Copilot Studio Agent – Add Knowledge  | You can't upload files or select Dataverse tables. The agent doesn't provide results that rely on this indexed data until Dataverse search is enabled for the environment. Ask the environment's admin to enable Dataverse search.  | The agent doesn't provide results that rely on this indexed data until Dataverse search is enabled for the environment. The agent uses the fallback answer by default.  |
| Microsoft Copilot Studio Agent – Using Copilot Chat	|	The agent doesn't provide results that rely on this indexed data until Dataverse search is enabled for the environment. Ask your environment admin to enable Dataverse search.  | The agent doesn't provide results that rely on this indexed data until Dataverse search is enabled for the environment. By default, the agent uses a fallback answer. |
| Model Driven Applications – Dataverse search | The search bar isn't visible in model-driven apps. | The search bar isn't visible in model-driven apps. |

### See also

[Search for tables and rows by using Dataverse search](relevance-search.md)<br/>
[Configure facets and filters](facets-and-filters.md)<br/>
[Frequently asked questions about Dataverse search](relevance-faq.md)<br />
[Developer's guide: Search for Dataverse records using the API](../developer/data-platform/search/overview.md)<br/>
[Compare search options in Microsoft Dataverse](search.md)

[!INCLUDE[footer-include](../includes/footer-banner.md)]
