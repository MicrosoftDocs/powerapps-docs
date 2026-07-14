---
title: "Work with Power Apps MCP server" 
description: Learn about the tools available with the Power Apps MCP Server.
ms.date: 04/07/2026
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

> [!IMPORTANT]
>
> Starting May 1st, 2026, agent feed only supports agents that use the Power Apps MCP Server to create tasks. Ensure your agents are properly onboarded to the [Power Apps MCP server](power-apps-mcp-server.md) by then to continue using the agent feed. If your agents don't use the Power Apps MCP Server, the agent feed doesn't appear in you model-driven app. More information: [Onboard your agent feed to use the Power Apps MCP server](#onboard-your-agent-to-use-the-power-apps-mcp-server)

The model context protocol (MCP) is an open protocol that enables seamless integration between large language model (LLM) applications and external data sources and tools. Your agent can use the Power Apps MCP Server to communicate with your Power Apps, providing right human-in-the-loop supervision or agentic workflows.

> [!IMPORTANT]
>
> - This is a preview feature.
> - Preview features aren't meant for production use and might have restricted functionality. These features are subject to [supplemental terms of use](https://go.microsoft.com/fwlink/?linkid=2216214), and are available before an official release so that customers can get early access and provide feedback.
> - This feature is available only in the English language and it replaces the earlier Microsoft Copilot Studio activity-based agent feed.
> - For information about how AI is used with this feature, go to [FAQ about Power Apps MCP Server invoke_data_entry tool](../common/faq-power-apps-mcp-server-invoke-data-entry.md).

The Power Apps MCP Server equips your agent with two types of capabilities:

- Automate repetitive app tasks:

   The Power Apps MCP Server enables agents to use advanced app tools developed in Power Apps. For example, the data‑entry agent capabilities previously available as an on‑demand AI feature are now accessible to any agent through Power Apps MCP server. To use them, you create your agent, configure the MCP tool, and direct it to unstructured content so it can generate Dataverse records with human review and approval through the enhanced agent feed.
- Supervise agent activity:

   The Power Apps MCP Server also provides specialized tools to business users to supervise any agent activity in the agent feed. Agents can now handoff control to humans for review, assistance, and steering with the MCP tools. These tools provide makers with much more control over the tasks they want to publish to the agent feed and when they need agent-human handoff.

:::image type="content" source="media/add-agents-to-app/power-apps-mcp-server.png" alt-text="Power Apps MCP server" lightbox="media/add-agents-to-app/power-apps-mcp-server.png":::

> [!NOTE]
> Access to the agent feed and supervision capabilities is limited by default to the System Administrator and System Customizer security roles. To allow additional users to view the agent feed, grant organization‑level read/write permissions on the tables listed here. You can create a new security role with these permissions and assign the role to multiple users as needed.
>
> - Agent Hub Goal(agenthubgoal)
> - Agent Hub Insight(agenthubinsight)
> - Agent Hub Metric(agenthubmetric)
> - Agent Task(agenttask)
> - Copilot(bot)

The Power Apps MCP tools improve the more you use them. For example, when you make corrections to suggestions in the agent canvas, the data entry tool improves based on your corrections. To use the enhanced agent feed capabilities, enable and configure the Power Apps MCP server from the Microsoft Copilot Studio agent. Once configured, you can invoke Power Apps MCP server tools from agent instructions using natural language.

More information: [Create an autonomous agent connected to Power Apps MCP server](add-agents-to-app.md#create-an-autonomous-agent-connected-to-power-apps-mcp-server)

## Onboard your agent to use the Power Apps MCP server

To configure an existing agent that was in the previous version of agent feed to use the Power Apps MCP server, you must do the following:

1. Add the Power Apps MCP server to your agent. To do this, open the agent in Copilot Studio and then select **Add tool**.
   :::image type="content" source="media/power-apps-mcp-server/copilot-studio-add-tool.png" alt-text="Add a tool to your agent" lightbox="media/power-apps-mcp-server/copilot-studio-add-tool.png":::  
1. Search for **Power Apps MCP Server**.
   :::image type="content" source="media/power-apps-mcp-server/copilot-studio-power-apps-mcp-search.png" alt-text="Find the Power Apps MCP Server" lightbox="media/power-apps-mcp-server/copilot-studio-add-tool.png":::
1. Select **Add and configure**.
   :::image type="content" source="media/power-apps-mcp-server/copilot-studio-add-power-apps-mcp.png" alt-text="Add Power Apps MCP Server" lightbox="media/power-apps-mcp-server/copilot-studio-add-tool.png":::

1. Update your agent instructions to use each of the tools in the Power Apps MCP Server at the proper times in it's orchestration.
   There are examples of how to do this in the remainder of this document.
1. Save and publish your agent.

> [!IMPORTANT]
>
> For autonomous agent scenarios where an agent runs via a trigger, the Power Apps MCP server must be configured to run using "Maker-provided credentials" as seen in the details section of the tool. Go to [Control maker-provided credentials for authentication](/microsoft-copilot-studio/configure-no-maker-authentication#scope-of-enforcement-and-experience) for more details if this option is disabled.
> :::image type="content" source="media/add-agents-to-app/copilot-studio-configure-maker-credentials.png" alt-text="Maker-provided credentials selection":::  

## List of tools

Once connected to the Power Apps MCP Server, the agent can choose from various tools in the Power Platform environment. These tools can generate agent feed items that render different user experiences, such as a side‑by‑side view for data entry agents or direct navigation to a record for `request_for_assistance` scenarios. 

| Tool | Description |
|------|-------------|
| [log_for_review](#log_for_review) | Log completed activity for passive human oversight. |
| [request_assistance](#request_assistance) | Request assistance from a human user. |
| [invoke_data_entry](#invoke_data_entry) | Create one or more records in a data source like Microsoft Dataverse, using contents from plain text or an email.|

## log_for_review

Records completed agent work to the agent feed for review. The `log_for_review` tool is intended for scenarios where an agent has sufficient information to act autonomously but the user should still be made aware of what the agent has done. This tool can be thought of as a way to passively oversee the high-confidence or low-risk actions performed by agents. It is best suited for decisions that can be easily revised or rolled back if the agent happens to perform the action incorrectly. Besides title, description, and steps you can also ask the tool to add a link to either the relevant Dataverse record or to an app-external URL. If an agent action touches multiple Dataverse records, you can instruct the agent which record it should navigate to in connection with the created task. It could be the link to the record the agent created using the Dataverse MCP server or a record link present in context like the record that triggered the agent execution. These tasks are shown in the agent feed's **Completed** tab.

### Sample instruction

When the customer makes a booking from the portal this agent must log the details for review. The review item title should be based on the booking reference number and must use the exact prefix “Review Web Booking: ”. In the review description, write a concise summary of the booking that includes main fields like Booking Reference, Booking Date, Seat Number, and Status, so a reviewer can quickly understand what was processed without opening the record. Ensure the description reads as a short paragraph and accurately reflects the current values from the booking record. Include your reasoning as steps. Also, include a link to the booking record.

:::image type="content" source="media/add-agents-to-app/log-for-review-example.png" alt-text="Log for review example":::

## request_assistance

The intended purpose of the `request_assistance` tool is to enable agents to surface errors, escalations, or exceptions to users, so they can take appropriate action. As a maker, you can define the scenarios for when to have your agent use the `request_assistance` tool. It creates an agent feed task that is populated in the **Needs Attention** section of the agent feed. This is an asynchronous operation that calls the Microsoft Copilot Studio agent that waits until the human completes the action. For details on completing the action feed activity, go to [Supervise agents in model-driven apps with agent feed (preview)](../../user/supervise-agents-with-agent-feed.md#supervise-agents-in-model-driven-apps-with-agent-feed-preview) 

You can observe the **In progress** status for the agent run in the activity tab when viewing the agent in Copilot Studio. Once the user completes the activity from agent feed, control comes back to agent via callback and agent can complete the task. 

:::image type="content" source="media/add-agents-to-app/copilot-studio-agent-in-progress.png" alt-text="In progress status in Copilot Studio":::

Like with the `log_for_review` tool, you can control the task output for title, description, and steps and can be specific when telling the agent which link to associate with a given task.

### Sample instruction

When this agent is triggered by the creation of a new support case, it should request assistance. In the request, set the title by prefixing the value of issue with “Assistance needed: ”. In the task description include the issue type, issue description, date reported, and the resolved value. Include your reasoning steps. Also include a link to the related Dataverse issue record. Once the user completes the task, continue processing by setting the case status to Closed.

:::image type="content" source="media/add-agents-to-app/request-assistance-with-nav-example.png" alt-text="Request user assistance example":::

## Design your user-in-the-loop

Before writing your agent's instructions, decide where human oversight belongs in your workflow. Use the following questions to identify which moments should use `request_assistance`, which should use
`log_for_review`, and which the agent can handle autonomously.

| Question | Guidance | Tool |
|---|---|---|
| **Where are the stakes high?** | High-stakes outcomes require oversight regardless of agent confidence. Give the agent explicit instructions to pause. | `request_assistance` |
| **When is user intervention always needed?** | If you can state it as a rule, encode it directly in the agent's instructions. | `request_assistance` |
| **Which inputs vary unpredictably?** | Unstructured data, edge cases, and novel situations can't always be anticipated. Instruct the agent to surface these dynamically. | `request_assistance` |
| **Does the agent need an answer to keep going?** | If the agent is blocked without human input, it should wait for a response. If it can proceed and a human audits later, it shouldn't. | `request_assistance` if yes, `log_for_review` if no |
| **Does a user own the outcome?** | Compliance requirements, high-value approvals, or policy decisions may require a human sign-off even when the agent is confident. | `log_for_review` |

> [!TIP]
> A well-designed agent doesn't ask for help constantly. Instead, it asks at the right moments. Use `request_assistance` sparingly for genuine decision points, and let `log_for_review` handle the rest.

### Example instructions by pattern

**Explicit rule:**
> *"For any claim with an estimated loss amount over $5,000, use `request_assistance` to route the claim to the assigned adjuster before proceeding."*

**Dynamic judgment:**
> *"If the cause of loss is ambiguous or claim documents conflict with each other, use `request_assistance` to flag the claim for adjuster review."*

**Passive oversight:**
> *"After completing the coverage determination, use `log_for_review` to record the outcome and confirm the claim has been cleared to advance."*

---

## Example: Homeowner's insurance coverage determination agent

The following example shows how these patterns apply to a complete, real-world workflow.

The agent triggers automatically when a new claim is submitted. It pulls the relevant policy, endorsements, and supporting documents from Dataverse, then reasons over them to produce a coverage determination, checking whether the policy was active, whether the claimed peril is covered, and whether any document conflicts affect confidence in the outcome.

From there, the agent uses the Power Apps MCP server to surface results in the agent feed based on what it found. If the claim is ambiguous, conflicted, or requires adjuster judgment, the agent uses
`request_assistance` to create a task for the assigned adjuster with the context they need to act. If the claim is clear-cut, the agent uses `log_for_review` to record the outcome passively and no action is
required. When an adjuster completes a task, the agent resumes, reads the decision, updates the claim record, and logs a completion notice back to the feed.

The result is a workflow where the agent handles the routine volume autonomously and pulls a human in only at genuine decision points with enough context that the adjuster can act immediately.

## invoke_data_entry

The `invoke_data_entry` tool streamlines the creation of Dataverse records by extracting structured information from unstructured inputs such as emails, messages, or documents. When invoked from a Copilot Studio agent, it automatically analyzes incoming content, fills out the appropriate form with the extracted data, and presents the proposed entry as a task in the agent feed for user review and approval. It requires review of the proposed entry by a user before creating the record. **Records are never created automatically using the `invoke_data_entry` tool.** This enables fast, reliable data capture with minimal manual effort.

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
> - Ensure that the user has permission to create records for the target table.

### How the invoke_data_entry tool works

When you configure a Copilot Studio agent to use the Power Apps MCP Server and enable the `invoke_data_entry` tool, the agent follows this process:

1. [An agent trigger](/microsoft-copilot-studio/authoring-triggers-about) is fired based on your configuration — such as an email arriving in a monitored mailbox or new document uploaded to SharePoint.
1. The agent analyzes incoming content and your instructions to determine whether the `invoke_data_entry` tool should be used.
1. If needed, the `invoke_data_entry` tool is invoked, passing the input content and the target Dataverse table and table columns to predict.
1. The tool processes the input, extracts relevant information, and populates a Dataverse form with suggested values for each mapped column.
1. A task appears in the agent feed. Selecting it opens the data‑entry review experience. The left panel shows the original input, and the right panel displays the form populated with suggested values.
1. The user can review the extracted values, make corrections if needed, and then save the record to Dataverse.

### Provide feedback

To provide feedback about the invoke_data_entry tool:

1. Open a invoke_data_entry task in the agent feed.
1. Select the feedback button in the task header.
1. Choose to give a compliment, report an issue, or make a suggestion.

:::image type="content" source="media/add-agents-to-app/agent-feed-feedback.png" alt-text="Agent feed feedback button":::

## Related articles

[Add agents to your model-driven app (preview)](add-agents-to-app.md)

[Supervise agents in model-driven apps with agent feed (preview)](../../user/supervise-agents-with-agent-feed.md)
