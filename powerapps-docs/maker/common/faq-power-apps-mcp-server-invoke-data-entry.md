---
title: FAQ about Power Apps MCP server invoke_data_entry tool in Power Apps
description: This FAQ provides information about the AI technology used in the Power Apps MCP server invoke_data_entry tool with key considerations and details about how AI is used, how it was tested and evaluated, and any specific limitations.
ms.date: 02/10/2026
ms.custom: 
  - responsible-ai-faqs
ms.topic: faq
author: HemantGaur
ms.author: hemantg 
ms.reviewer: matp
ms.collection: 
    - bap-ai-copilot 
---
# FAQ about Power Apps MCP server invoke_data_entry tool

These frequently asked questions (FAQ) describe the AI impact of Power Apps MCP server invoke_data_entry tool in Power Apps.

## What is the invoke_data_entry tool in Power Apps MCP?  

Create your own AI agent that utilizes the Power Apps MCP server’s invoke_data_entry tool to create records in Dataverse. This tool accepts various formats of unstructured input, such as PDF or Excel files, and creates draft records in Microsoft Dataverse based on the inputs. You can review and edit these draft records using the agent feed, and save to Dataverse once ready.

## What can the invoke_data_entry tool do?

The invoke_data_entry tool can accept unstructured inputs, such as PDF or Excel files, parse them, and identify how to fill in Dataverse forms from these unstructured inputs in order to create a record. These are presented as suggestions for users to review in agent feed, where users can choose to save them to Dataverse. At this time, no records get automatically created in Dataverse.  

## What is the invoke_data_entry tool’s intended use(s)?  

The data entry agent (form fill) tool can take an unstructured input, such as PDF or Excel files, and create a Dataverse record based on its contents. This is a manual process today, but with the tool, customers can create an agent to automatically create a draft record. This draft can be reviewed in the agent feed, and once the user chooses to save, the record gets written to Dataverse.  

## How was the invoke_data_entry tool evaluated? What metrics are used to measure performance?  

In our evaluations, we look at how good the suggestions are based on the provided input files, and how often they're accepted in the form to be saved in the record in Dataverse. Moreover, the suggestions are evaluated for satisfying Microsoft’s responsible AI principles.

## What are the limitations of the invoke_data_entry tool? How can users minimize the impact of invoke_data_entry tool’s limitations when using the system?  

At this time, the invoke_data_entry tool only supports a limited number of unstructured input formats, and only creates records in Dataverse. The tool isn't supported for use with an unsupported input format or for creating records in a non-Dataverse data source.

## What operational factors and settings allow for effective and responsible use of the invoke_data_entry tool?  

The invoke_data_entry tool is effective when used with the supported file formats provided as inputs, and is used to create records in Dataverse. Agent feed must be used by users to review invoke_data_entry tool’s draft records and saving these to Dataverse once ready.

## How do I provide feedback on the invoke_data_entry tool?  

Users can provide feedback on the invoke_data_entry tool while reviewing the draft records in the agent feed.

## Related articles

[Add agents to your model-driven app (preview)](../model-driven-apps/add-agents-to-app.md)

[Work with Power Apps MCP server](../model-driven-apps/power-apps-mcp-server.md)