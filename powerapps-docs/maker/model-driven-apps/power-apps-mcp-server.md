---
title: "Work with Power Apps MCP server" 
description: Learn about the tools available with the Power Apps MCP server.
ms.date: 02/05/2026
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
The Model Context Protocol (MCP) is an open protocol that enables seamless integration between large language model (LLM) applications and external data sources and tools. Your agent can use the Power Apps MCP server to communicate with your Power Apps, providing right human-in-the-loop supervision or agentic workflows. 

To use the enhanced Agent Feed capabiltities, you need to enable and configure the Power Apps MCP server from Microsoft Copilot Studio agent. For more information: see (Configure the Dataverse MCP server)[https://review.learn.microsoft.com/en-us/power-apps/maker/model-driven-apps/add-agents-to-app?branch=matp-36387#create-an-autonomous-agent-connected-to-power-apps-mcp-server]. Once configured, you can invoke Power Apps MCP server tools from agent instructions using natural language.

# List of tools
Once connected to the Power Apps MCP Server, agent can choose from various tools in the Power Platform environment.

| Tool | Description |
|------|-------------|
| log_for_review | Log completed activity for passive human oversight. |
| request_assistance | Request assistance from a human user. |
| invoke_data_entry | Create one or more records in a data source like Dataverse, using contents from plain text or an email.|

# log_for_review 
Logs completed agent work to the Agent Feed for human review. This tool is intended for scenarios where an agent has sufficient information to act autonomously but needs human validation before the result is finalized or trusted. It is best suited for decisions that can be easily revised or rolled back. Besides Title and Description, you can also ask the tool to add a link to dataverse record. It could be the link to the record agent has creaated using DV MCP or one present in context like the record which triggered agent execution. These tasks are shown in the Agent feed's **completed tab**.

**Sample instruction**
When the customer makes a booking from the portal this agent must log the details for human review. The review item title should be based on the booking reference number and must use the exact prefix “Review Web Booking: ”. In the review description, write a concise, natural‑language summary of the booking that includes main fields like Booking Reference, Booking Date, Seat Number, and Status, so a reviewer can quickly understand what was processed without opening the record. Ensure the description reads as a short paragraph and accurately reflects the current values from the booking record.

log_for_review_example.png

# request_assistance 
The request assistance tool will create a Agent Feed task to reach out to a human. This is an asynchronous operation and calling copilot studio agent will wait until the human completes the action. For details on completing the action feed acivity see (https://review.learn.microsoft.com/en-us/power-apps/user/supervise-agents-with-agent-feed?branch=matp-36387#take-action-on-agent-activity). You can see **in progress** status for the agent run in the avtivity tab when viewing agent in Microsoft Copilot Studio. Once the user completes the activity from agent feed, control comples back to agent via callback and agent can complete the task. 

copilot-studio-agent-inprogress.png

**Sample instruction**
When this agent is triggered by the creation of a new support case, it should request human assistance. For the request assistance set the title by prefixing the value of issue1 with “Assistance needed: ”. In the task description includes the issue type, issue description, date reported, and the Resolved value as steps. Also include a navigation link to the Dataverse issue record.

request_assistance_withNavexample.png

# invoke_data_entry 

