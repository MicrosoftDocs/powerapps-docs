---
title: "Work with Power Apps MCP server" 
description: Learn about the tools available with the Power Apps MCP server.
ms.date: 02/10/2026
ms.reviewer: matp
ms.topic: how-to
author: HemantGaur
ms.subservice: mda-maker
ms.author: hemantg
ms.service: powerapps
search.audienceType: 
  - maker
---
# Work with Power Apps MCP server

The model context protocol (MCP) is an open protocol that enables seamless integration between large language model (LLM) applications and external data sources and tools. Your agent can use the Power Apps MCP server to communicate with your Power Apps, providing right human-in-the-loop supervision or agentic workflows.

> [!IMPORTANT]
>
> - This is a preview feature.
> - Preview features aren't meant for production use and might have restricted functionality. These features are subject to [supplemental terms of use](https://go.microsoft.com/fwlink/?linkid=2216214), and are available before an official release so that customers can get early access and provide feedback.
> - This feature is available only in the English language and it replaces the earlier Microsoft Copilot Studio activity-based agent feed.
> - For information about how AI is used with this feature, go to [FAQ about Power Apps MCP server invoke_data_entry tool](../common/faq-power-apps-mcp-server-invoke-data-entry.md).

The Power Apps MCP server equips your agent with two types of app skills:

- Automate repetitive app tasks:

   The Power Apps MCP server enables agents to use advanced app skills developed in Power Apps. For example, the data‑entry agent capabilities previously available as an on‑demand AI feature are now accessible to any agent through Power Apps MCP server. To use them, you create your agent, configure the MCP tool, and direct it to unstructured content so it can generate Dataverse records with human review and approval through the enhanced agent feed.
- Supervise agent activity:

   The Power Apps MCP server also provides specialized tools to business users to supervise any agent activity in the agent feed. Agents can now handoff control to humans for review, assistance, and steering with the MCP tools. These tools provide makers with much more control over the tasks they want to publish to the agent feed and when they need agent-human handoff.

:::image type="content" source="media/add-agents-to-app/power-apps-mcp-server.png" alt-text="Power Apps MCP server" lightbox="media/add-agents-to-app/power-apps-mcp-server.png":::

The Power Apps MCP tools improve the more you use them. For example, when you make corrections to suggestions in the agent canvas, the data entry tool improves based on your corrections. To use the enhanced agent feed capabiltities, enable and configure the Power Apps MCP server from the Microsoft Copilot Studio agent. Once configured, you can invoke Power Apps MCP server tools from agent instructions using natural language.

More information: [Create an autonomous agent connected to Power Apps MCP server](add-agents-to-app.md#create-an-autonomous-agent-connected-to-power-apps-mcp-server)

## List of tools

Once connected to the Power Apps MCP Server, the agent can choose from various tools in the Power Platform environment. These tools can generate agent feed items that render different user experiences, such as a side‑by‑side view for data entry agents or direct navigation to a record for `request_for_assistance` scenarios. 

| Tool | Description |
|------|-------------|
| [log_for_review](#log_for_review) | Log completed activity for passive human oversight. |
| [request_assistance](#request_assistance) | Request assistance from a human user. |
| [invoke_data_entry](#invoke_data_entry) | Create one or more records in a data source like Microsoft Dataverse, using contents from plain text or an email.|

## log_for_review

Records completed agent work to the agent feed for human review. The `log_for-review` tool is intended for scenarios where an agent has sufficient information to act autonomously but needs human validation before the result is finalized or trusted. It is best suited for decisions that can be easily revised or rolled back. Besides title and description, you can also ask the tool to add a link to the Dataverse record. It could be the link to the record the agent created using the Dataverse MCP server or a record link present in context like the record that triggered the agent execution. These tasks are shown in the agent feed's **Completed** tab.

### Sample instruction

When the customer makes a booking from the portal this agent must log the details for human review. The review item title should be based on the booking reference number and must use the exact prefix “Review Web Booking: ”. In the review description, write a concise, natural‑language summary of the booking that includes main fields like Booking Reference, Booking Date, Seat Number, and Status, so a reviewer can quickly understand what was processed without opening the record. Ensure the description reads as a short paragraph and accurately reflects the current values from the booking record.

:::image type="content" source="media/add-agents-to-app/log-for-review-example.png" alt-text="Log for review example":::

## request_assistance

The `request_assistance` tool creates an agent feed task to reach out to a human. This is an asynchronous operation that calls the Microsoft Copilot Studio agent that waits until the human completes the action. For details on completing the action feed acivity, go to [Supervise agents in model-driven apps with agent feed (preview)](../../user/supervise-agents-with-agent-feed.md#supervise-agents-in-model-driven-apps-with-agent-feed-preview) 

You can observe the **In progress** status for the agent run in the activity tab when viewing the agent in Copilot Studio. Once the user completes the activity from agent feed, control comples back to agent via callback and agent can complete the task. 

:::image type="content" source="media/add-agents-to-app/copilot-studio-agent-in-progress.png" alt-text="In progress status in Copilot Studio":::

### Sample instruction

When this agent is triggered by the creation of a new support case, it should request human assistance. For the request assistance set the title by prefixing the value of issue1 with “Assistance needed: ”. In the task description includes the issue type, issue description, date reported, and the Resolved value as steps. Also include a navigation link to the Dataverse issue record.

:::image type="content" source="media/add-agents-to-app/request-assistance-with-nav-example.png" alt-text="Request user assistance example":::

## invoke_data_entry

The `invoke_data_entry` tool streamlines the creation of Dataverse records by extracting structured information from unstructured inputs such as emails, messages, or documents. When invoked from a Copilot Studio agent, it automatically analyzes incoming content, fills out the appropriate form with the extracted data, and presents the completed entry as a task in the agent feed for user review and approval. This enables fast, reliable data capture with minimal manual effort.

### Sample instruction - shared email triggered agent

You are the travel idea generator agent. Your job is to process incoming emails and create travel idea records in Dataverse.

When an email arrives:

1. Determine if it contains travel-related information (either in the email body or attachments).
2. Use the `invoke_data_entry` tool to create a travel idea record with the extracted information in the following columns:

   - cr3ea_title
   - cr3ea_description
   - cr3ea_triptype
   - cr3ea_customername
   - cr3ea_customeremail
   - cr3ea_customerphone
   - cr3ea_destinationcity
   - cr3ea_travelstart
   - cr3ea_travelend
   - cr3ea_numberoftravelers
   - cr3ea_budgetusd
   - cr3ea_specialrequests
3. If information is missing, still create the record with available data - leave unknown fields empty.

:::image type="content" source="../../user/media/agent-supervision/agent-feed-accept-complete.png" alt-text="Agent feed accept and complete button" lightbox="../../user/media/agent-supervision/agent-feed-accept-complete.png":::

> [!NOTE]
>
> - When you write instructions for your agent, always reference Dataverse columns by their logical names as shown in the sample instruction. Clear, direct instructions help the agent reliably create records from the input. You can view a column’s logical name by opening the table in make.powerapps.com, select **Columns**, and then open the column to view the details.
> - `invoke_data_entry` tool supports .pdf, .xlsx, .docx, .jpeg, .jpg, .png, .gif and.bmp formats.
> - `invoke_data_entry` tool can populate single line of text (None format), Whole number and Decimal column types.

### How the invoke_data_entry tool works

When you configure a Copilot Studio agent to use the Power Apps MCP server and enable the `invoke_data_entry` tool, the agent follows this process:

1. [An agent trigger](/microsoft-copilot-studio/authoring-triggers-about) is fired based on your configuration — such as an email arriving in a monitored mailbox or new document uploaded to SharePoint.
1. The agent analyzes incoming content and your instructions to determine whether the `invoke_data_entry` tool should be used.
1. If needed, the `invoke_data_entry` tool is invoked, passing the input content and the target Dataverse table and table columns to predict.
1. The tool processes the input, extracts relevant information, and populates a Dataverse form with suggested values for each mapped column.
1. A task appears in the agent feed. Selecting it opens the data‑entry review experience. The left panel shows the original input, and the right panel displays the form populated with suggested values.
1. The user can review the extracted values, make corrections if needed, and then save the record to Dataverse.

## Related articles

[Add agents to your model-driven app (preview)](add-agents-to-app.md)

[Supervise agents in model-driven apps with agent feed (preview)](../../user/supervise-agents-with-agent-feed.md)