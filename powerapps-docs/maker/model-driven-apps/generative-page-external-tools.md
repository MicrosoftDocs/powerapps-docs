---
title: Create and edit generative pages with AI code generation tools
description: Learn how to use AI code generation tools like Claude Code to create and edit generative pages for model-driven apps in Power Apps.
author: jasongre
ms.author: jasongre
ms.reviewer: matp
ms.date: 2026-02-12
ms.topic: how-to
ms.service: powerapps
ms.subservice: mda-maker
search.audienceType:
- maker
- developer
ms.collection:
- bap-ai-copilot
applies_to:
- PowerApps
---

# Create and edit generative pages with AI code generation tools

This article describes how to use AI code generation tools, such as Claude Code, to create and edit generative pages for model-driven apps in Power Apps. This approach enables you to integrate advanced code generation capabilities directly into your development workflow, allowing you to create new generative pages or iterate on existing ones using natural language instructions.

## Overview

Using AI code generation tools with generative pages provides an alternative development approach that complements the UI-based experience in the Power Apps maker portal. This code-first approach is designed for developers and technical makers who prefer working with local development tools and CLI-based workflows.

### What you can do

- **Create new generative pages** using plain-language requirements
- **Update existing generative pages** by requesting changes or enhancements through your AI tool
- **Deploy directly** to your Power Apps environment using PAC CLI commands
- **Work locally** with your preferred IDE and development tools

### How it works

1. You describe what you want to build in natural language (for example, "Create a generative page dashboard showing top accounts by revenue")
2. The AI code generation tool asks clarifying questions about your requirements
3. The tool generates production-ready TypeScript/React code for your generative page
4. The tool deploys the code to your environment using PAC CLI commands
5. Your generative page appears in your model-driven app

## Prerequisites

Before you start, ensure you have the following:

- **AI code generation tool**: Claude Code CLI or another AI code generation tool that supports custom instructions and workflows
- **Power Apps environment**: A Power Platform environment with a model-driven app to deploy pages to
- **PAC CLI**: Microsoft Power Platform CLI (PAC CLI) authenticated to your Dataverse environment
  - [Install Power Platform CLI](/power-platform/developer/cli/introduction)
- **.NET SDK**: .NET 10 SDK or .NET Framework 4.8
  - [Download .NET 10.0 SDK](https://dotnet.microsoft.com/download/dotnet/10.0)
- **Node.js**: Node.js runtime environment
  - [Download Node.js](https://nodejs.org/)

> [!NOTE]
> Your Power Platform environment must be located in the US region. Generative pages are not available in other regions yet.

## Setup

### Step 1: Install and authenticate PAC CLI

If you haven't already installed and authenticated PAC CLI, follow these steps:

1. Install the Microsoft Power Platform CLI. More information: [Install Power Platform CLI](/power-platform/developer/cli/introduction)

2. Authenticate PAC CLI to your Power Apps environment:

   ```bash
   # Create a new authentication profile using environment URL
   pac auth create --environment https://your-org.crm.dynamics.com

   # Or use environment GUID
   pac auth create --environment 00000000-0000-0000-0000-000000000000

   # Verify authentication
   pac auth list
   ```

> [!TIP]
> You can have multiple authentication profiles for connecting to different environments. Use `pac auth select` to switch between them.

### Step 2: Set up the generative page skill (for Claude Code)

If you're using Claude Code, you need to configure the generative page skill:

1. Create a new project folder for working with generative pages on your local machine
2. Download the `genux-skill.zip` file (provided by your Microsoft contact) and extract it to your project folder
3. Open Claude Code from your project folder

The generative page skill should be automatically detected when you ask Claude Code to create or edit a generative page. If the skill isn't detected, you can manually invoke it:

```
/genpage <instruction>
```

### Using other AI code generation tools

If you're using a tool other than Claude Code, ensure your tool has access to the generative page skill resources, including:

- Component library and API documentation
- Sample generative page code
- PAC CLI command reference
- Workflow instructions for creating and deploying generative pages

Your AI tool should read all context from the generative page skill folder (resources, samples, and skill documentation) to understand:

- How to structure generative page code
- Which data APIs to use
- The workflow and commands needed to deploy changes to your environment

## Create a new generative page

Follow this workflow when building a new page from scratch.

### Step 1: Start a conversation with your AI tool

Open your AI code generation tool from your project folder and describe what you want to create.

**Example prompts:**

- "Create a generative page dashboard showing our top 10 accounts by revenue"
- "Build a generative page form for creating and editing contact records"
- "Make a generative page for displaying incident reports on a map"
- "Create a generative page for a sales pipeline visualization with opportunities"

### Step 2: Answer clarifying questions

The AI tool asks questions to understand your requirements.

**Tips:**

- Be specific about business needs and data requirements
- Identify mobile requirements early in the conversation
- Mention any specific UI components or layout preferences
- Don't worry about technical implementation details—focus on what you need

### Step 3: Review the implementation plan

The AI tool presents a plan describing:

- Components to be built
- Dataverse tables and columns to be used
- Key features and interactions
- Data retrieval and manipulation approach

Review the plan and confirm it meets your requirements, or request changes before proceeding.

### Step 4: Review code, publish, test, and iterate

The AI tool generates complete TypeScript code, including:

- Explanation of the implementation approach
- Summary of what was built
- Production-ready code

**To deploy your page:**

1. Ask the AI tool to publish or deploy your page to the environment when you're ready
2. Optionally specify a sitemap name for the page (the tool generates a meaningful name by default)
3. Wait for the deployment to complete

**To test your page:**

1. Open your model-driven app in Power Apps
2. Navigate to the new page using the sitemap
3. Verify the page functions as expected

**To iterate:**

If you need to make changes, return to your AI tool and describe the updates you need using natural language. The tool can make incremental updates without starting over.

> [!NOTE]
> You can change the name or position of the generative page in the sitemap at any time from the model-driven app designer.

## Edit an existing generative page

Use this workflow to update a page that already exists in your environment.

### Step 1: Retrieve the existing page

In your AI code generation tool, request to retrieve the existing generative page. You can identify the page by:

- Page ID (GUID)
- Page name in the sitemap and the app it's in

**Example:**

"I want to update the Pet Adoption generative page from the Demo app"

### Step 2: Describe your updates

Tell the AI tool what changes you want to make to the page.

**Example prompts:**

- "Add a filter to show only active records"
- "Change the layout to display cards in a grid instead of a list"
- "Add a chart showing adoption trends over time"
- "Update the form to include the new custom field for pet temperament"

### Step 3: Review, publish, test, and iterate

The AI tool generates updated TypeScript code based on your requested changes. Follow the same review, publish, and test process described in the "Create a new generative page" section.

Continue iterating with natural language instructions until the page meets your requirements.

## Troubleshooting

### Page fails to load in Power Apps

If you navigate to your generative page and see an error message or blank screen:

1. Open browser developer tools (F12 in most browsers)
2. Navigate to the **Console** tab
3. Copy the complete error message, including the stack trace
4. Return to your AI code generation tool and paste the error with context:

   "I'm getting this error when opening the page: [paste error here]. Please fix the issue."

5. The AI tool analyzes the error, identifies the root cause, and generates a fix
6. Review the fix and ask the tool to republish the page

### Reverting to a working version

If recent changes broke your page or made issues worse, you can ask the AI tool to roll back to a previous working version:

"The recent changes broke the page. Please revert to the last working version."

The AI tool then:

1. Identifies the changes that were made
2. Restores the previous working code
3. Redeploys the stable version

### Deployment failures

If the PAC CLI deployment command fails:

1. Verify you're authenticated to the correct environment (`pac auth list`)
2. Check that you have the necessary permissions to create or update generative pages
3. Ensure the PAC CLI version includes generative page commands
4. Copy the error message and ask your AI tool to diagnose and resolve the issue

## Best practices

- **Start simple**: Begin with a basic version of your page and iterate to add complexity
- **Test frequently**: Deploy and test your page after each significant change
- **Be specific**: Provide detailed requirements to get better initial results
- **Use existing patterns**: Reference similar pages or UI patterns when describing your requirements
- **Validate generated code**: Always review the generated code to ensure it meets your organization's standards and compliance requirements

> [!IMPORTANT]
> While AI code generation tools make a best-effort attempt to generate complete, production-ready code with accessibility and security best practices, you're ultimately responsible for validating the code. Ensure the generated code meets your organization's standards, policies, and compliance requirements.

## Limitations

The limitations for generative pages created with AI code generation tools are the same as those for generative pages created in the Power Apps maker portal:

- Your page can connect to only Dataverse tables (up to six for a single page)
- Only US English is supported
- Collaboration isn't supported—ensure only one maker is working on a generative page at a time
- Only specific data types are supported (Choice, Currency, Customer, Date and Time, Date Only, Decimal Number, Floating Point Number, Image, Lookup, Multiline Text, Status, Status Reason, Text, Whole Number, Yes/No, Unique Identifier)

More information: [Generative pages limitations](/power-apps/maker/model-driven-apps/generative-pages#limitations)

## Related content

- [Generate a page using natural language with model-driven apps](/power-apps/maker/model-driven-apps/generative-pages)
- [dataApi object methods for generative pages](/power-apps/developer/model-driven-apps/generative-page/data-api/)
- [Power Platform CLI reference](/power-platform/developer/cli/reference/index)
