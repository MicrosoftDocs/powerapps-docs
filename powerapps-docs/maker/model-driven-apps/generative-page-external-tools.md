---
title: Create and edit generative pages with AI code generation tools
description: Learn how to use AI code generation tools like Claude Code to create and edit generative pages for model-driven apps in Power Apps.
author: jasongre
ms.author: jasongre
ms.reviewer: matp
ms.date: 04/10/2026
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

This article describes how to use AI code generation tools, such as GitHub Copilot CLI and Claude Code, to create and edit generative pages for model-driven apps in Power Apps. This approach allows you to integrate advanced code generation capabilities directly into your development workflow, allowing you to create new generative pages or iterate on existing ones using natural language instructions.

Using AI code generation tools with generative pages provides an alternative development approach that complements the UI-based experience in Power Apps (make.powerapps.com). This code-first approach is designed for developers and technical makers who prefer working with local development tools and CLI-based workflows.

## What you can do with code generation tools

- *Create one or more generative pages* in a single run from plain-language requirements
- *Create the supporting Dataverse tables* your pages need, or reuse existing ones, including sample data for new tables
- *Place artifacts into a new or existing app and solution*, including creating an app or solution on the fly
- *Update existing generative pages* by requesting changes or enhancements through your AI tool
- *Deploy directly* to your Power Apps environment using PAC CLI commands
- *Work locally* with your preferred IDE and development tools, with `npm install` and IntelliSense support for the generated code

### How it works

1. You describe what you want to build in natural language, for example, "Create a generative page dashboard showing top accounts by revenue."
2. A planner agent analyzes your request and proposes a plan. The plan may include one or more pages, the Dataverse tables the pages need (new or existing), and the app and solution where the artifacts will live. The planner then delegates to specialized agents (for example, an entity builder and a page builder) to build what the plan describes.
3. You review and adjust the plan before building. You can change the number of pages, swap or add tables, target a different app, or place the artifacts in a different solution.
4. The agents generate production-ready TypeScript and React code for your page or pages, along with supporting files for local development.
5. The tool deploys the artifacts to your environment using [generative page PAC CLI commands](/power-platform/developer/cli/reference/model), and optionally runs a verify-in-browser step that exercises the page with generated tests.
6. Your generative page appears in your model-driven app.

## Prerequisites

Before you start, ensure you have the required software and permissions described here.

### Software requirements

| Component | Minimum version | More information |
|-----------|-----------------|------------------|
| Node.js | 18.0 or later | [Download Node.js](https://nodejs.org/) |
| Power Platform CLI (PAC CLI) | Latest | [Install PAC CLI](/power-platform/developer/cli/introduction?tabs=windows#install-microsoft-power-platform-cli) |
| GitHub Copilot CLI, Claude Code, or other code generation tool | Latest | [GitHub Copilot CLI](https://github.com/features/copilot/cli/) or [Claude Code](https://claude.ai/code) |

### Additional requirements

- A Power Platform environment with a model-driven app to deploy pages.
- An *authenticated PAC CLI session* connected to your target environment.
   - Go to [Authenticate Power Platform CLI](/power-platform/developer/cli/reference/auth) for more details on getting connected.

> [!NOTE]
> This capability is available worldwide in public clouds.

### Install the plugin

Run the installer to set up all Power Platform plugins in either PowerShell or a Windows command window.

``powershell
iwr https://raw.githubusercontent.com/microsoft/power-platform-skills/main/scripts/install.js -OutFile install.js; node install.js; del install.js
``

``dos
curl -fsSL https://raw.githubusercontent.com/microsoft/power-platform-skills/main/scripts/install.js | node
``

The installer automatically:

- Detects available tools (Claude Code, GitHub Copilot CLI)
- Registers the plugin marketplace and installs all plugins  
- Enables auto-update so plugins stay current

After installation, restart your AI tool if needed.

### Install only the generative page plugin

To install only the generative page plugin for GitHub Copilot CLI or Claude Code:

1. Add the Power Platform Skills marketplace plugin: `/plugin marketplace add microsoft/power-platform-skills`
2. Install the Power Apps plugin: `/plugin install model-apps@power-platform-skills`

> [!NOTE]
> For Claude Code, you can install the plugin with different scopes, such as global, local, or user. Depending on the scope, you need to be in the correct directory for Claude Code to use the plugin. Go to [Extend Claude with skills](https://code.claude.com/docs/en/skills#share-skills)

Once installed, you can use the plugin by either:

- Running the `/genpage` command explicitly.
- Describing the page you want to create. The tool automatically detects and uses the plugin.

> [!TIP]
> Turn on auto-update to automatically receive updates to the marketplace and skills. Use the `/plugin` command, navigate to **Marketplaces**, choose the marketplace, and turn on auto-update.

### Using other AI code generation tools

For other AI code generation tools, ensure your tool has access to the generative page resources from the [Power Platform skills](https://github.com/microsoft/power-platform-skills/tree/main/plugins/model-apps) GitHub repository. The model-apps plugin folder includes component documentation, sample code, PAC CLI command reference, and workflow instructions necessary to create code adhering to generative page requirements, including how to create pages that support multiple languages and regions. Consult the repository [readme](https://github.com/microsoft/power-platform-skills/blob/main/plugins/model-apps/README.md) for information about accessing and using these resources with your preferred tool.

## Skills overview

The Power Apps plugin provides this skill for working with generative pages.

| Skill | Command | Description | 
|-------|-------------|---------| 
| Generative pages |  `/genpage` | Create code for generative pages (for creation or editing scenarios) |

This skill enables you to describe what you want to build and have the AI tool generate complete TypeScript and React code for your generative page, then deploy it directly to your Power Apps environment.

## Create a new generative page

Follow this workflow when building a new page or set of pages from scratch.

1. **Start a conversation with your AI tool** and describe what you want to create. Be as specific or as open-ended as you want — the more vague the request, the more the agent fills in itself. You can also attach an image or other materials to guide visuals, theming, and layout. For example:
   - "Create a generative page dashboard showing our top 10 accounts by revenue using the Account table"
   - "Build two pages for managing my volunteer signups — one to browse open shifts and one to confirm a signup — using sample data"
   - "Make a generative page for displaying incident reports on a map using the Incident table"

1. **Choose create or edit if asked.** If the planner agent isn't sure whether you want a new page or to update an existing one, it asks. To follow this workflow, choose to create a new page. (For editing, go to [Edit an existing generative page](#edit-an-existing-generative-page).)

1. **Answer questions about what to build.** The planner may ask what kind of page you want, offering a few examples and accepting a custom description (what data to use, layout, what information to display, interactions, and so on). Be specific about business needs and data requirements, identify mobile requirements early, and mention any UI components or layout preferences. The planner may also ask clarifying questions such as whether to use Dataverse tables or hard-coded sample data, and whether to add the page to an existing app or create a new app.

1. **Review and adjust the plan.** The planner presents a plan that includes the page or pages it intends to build, the Dataverse tables to use or create (with the columns it plans to use), the app to host the page (new or existing), and the solution where the artifacts will live. Iterate with the agent to adjust anything you want changed &mdash; for example, the number of pages, which tables are used or created, the target app, or the target solution. Confirm the plan when it matches your intent.

1. **Let the agents build and deploy.** The specialized agents generate the page or pages, supporting tables, and code, then deploy to your environment.

1. **Optionally verify in browser.** After the build, the agent may offer to run a verify-in-browser step that runs automatically generated Playwright tests against the page to confirm it loads and functions correctly. Use this to catch obvious issues before testing manually.

1. **Test and iterate.** Open your model-driven app in Power Apps and navigate to the new page. If you need to make changes, return to your AI tool and describe the updates in natural language.

> [!NOTE]
> You can change the name or position of the generative page in the sitemap at any time from the model-driven app designer.

## Edit an existing generative page

Use this workflow to update a page that already exists in your environment.

1. Retrieve the existing page. In your AI code generation tool, request to retrieve the existing generative page by providing the page ID (GUID) or the page name in the sitemap and the app it's in. For example, "I want to update the Pet Adoption generative page from the Demo app."

1. Describe your updates. Tell the AI tool what changes you want to make. For example:
   - "Add a filter to show only active records"
   - "Change the layout to display cards in a grid instead of a list"
   - "Add a chart showing adoption trends over time"
   - "Update the form to include the new custom field for pet temperament"

1. Review, publish, test, and iterate. The AI tool generates updated TypeScript code based on your requested changes. Follow the same review, publish, and test process described in the "Create a new generative page" section. Continue iterating with natural language instructions until the page meets your requirements.

## Local development files

When the AI tool generates a page, it also writes two supporting files to your local workspace to make reviewing and iterating on the code easier:

- **`package.json`** &mdash; declares the runtime and development dependencies the generated page compiles against. Run `npm install` after generation to install these dependencies.
- **`genpage.d.ts`** &mdash; ambient TypeScript declarations for objects that aren't installed via npm, such as `dataApi` and `pageInput`.

With both files in place and `npm install` complete, your editor's IntelliSense (for example, in VS Code) works against the generated code, so you can review or hand-edit the page without seeing red squiggles for unresolved types.

## Set up a page to accept input parameters

Generative pages can accept the input parameters `recordId`, `entityName`, and `data`, enabling them to receive contextual data when navigated to from other pages or code. When you instruct the AI tool to configure input parameters, it generates the appropriate initialization code so the page reads and uses those values when it loads.

Describe the parameters you want in your prompt:

- "Set up the page to accept an Account recordId and entityName. When the page loads, use these parameters to fetch and display the corresponding account details."
- "Configure this page to accept a data parameter containing a custom filter object. Use it to filter the displayed records when the page loads."

To navigate to the page and pass these parameters, see [Navigate to and from a generative page using Client API](../../developer/model-driven-apps/clientapi/navigate-to-generative-page-examples.md).

## Localization

When you create a generative page using the Power Apps plugin for Claude Code or GitHub Copilot CLI, localization is handled automatically. The agent detects all languages enabled in your environment and generates code so that the page works with all of those languages. The page respects each user's preferred language and regional formatting preferences for dates, numbers, and currency.

If you want to target a different set of languages than those enabled in your environment, you can ask the agent to adjust, for example:

> "Update this page to support English, French, and Spanish only."

> [!NOTE]
> The sitemap entry for a generative page isn't localized by default. To localize sitemap entries, update them separately in the app designer.

For more information, go to the [localization instructions](https://github.com/microsoft/power-platform-skills/blob/main/plugins/model-apps/references/genpage-rules-reference.md#localization) in the Power Platform Skills repository.

## Troubleshooting

### Page fails to load in Power Apps

If you navigate to your generative page and observe an error message or blank screen:

1. Open browser developer tools (F12 in most browsers).
2. Select the **Console** tab.
3. Copy the complete error message, including the stack trace.
4. Return to your AI code generation tool and paste the error with context:

   "I'm getting this error when opening the page: [paste error here]. Please fix the issue."

   The AI tool analyzes the error, identifies the root cause, and generates a fix.
5. Review the fix and ask the tool to republish the page.

### Reverting to a working version

If recent changes broke your page or made issues worse, you can ask the AI tool to roll back to a previous working version:

"The recent changes broke the page. Please revert to the last working version."

The AI tool then:

1. Identifies the changes that were made
1. Restores the previous working code
1. Redeploys the stable version

## Best practices

- Start simple. Begin with a basic version of your page and iterate to add complexity.
- Test frequently. Deploy and test your page after each significant change.
- Be specific. Provide detailed requirements to get better initial results.
- Use existing patterns. Reference similar pages or UI patterns when describing your requirements.
- Validate generated code. Always review the generated code to ensure it meets your organization's standards and compliance requirements.

> [!IMPORTANT]
> While AI code generation tools make a best-effort attempt to generate complete, production-ready code with accessibility and security best practices, you're ultimately responsible for validating the code. Ensure the generated code meets your organization's standards, policies, and compliance requirements.

## Limitations

The limitations for generative pages created with AI code generation tools are the same as those for generative pages created in the Power Apps maker portal:

- Your page can connect to only Dataverse tables.
- Collaboration isn't supported—ensure only one maker is working on a generative page at a time.
- Only these data types are supported: Choice, Currency, Customer, Date and Time, Date Only, Decimal Number, Floating Point Number, Image, Lookup, Multiline Text, Status, Status Reason, Text, Whole Number, Yes/No, Unique Identifier.

## Related content

- [Generate a page using natural language with model-driven apps](/power-apps/maker/model-driven-apps/generative-pages)
- [Navigate to and from a generative page using Client API](../../developer/model-driven-apps/clientapi/navigate-to-generative-page-examples.md)
- [dataApi object methods for generative pages](/power-apps/developer/model-driven-apps/generative-page/data-api/)
- [Power Platform CLI reference](/power-platform/developer/cli/reference/index)
