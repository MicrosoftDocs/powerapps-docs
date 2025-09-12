---
title: "Code interpreter PCF component sample"
description: "Learn how to use code interpreter enabled prompts from a PCF component in a model-driven application."
ms.date: 09/11/2025
ms.reviewer: jdaly
ms.topic: article
author: rapraj
ms.author: rapraj
ms.subservice: dataverse-developer
search.audienceType: 
  - developer
contributors:
 - JimDaly
 - ColinBe
---
# Code interpreter PCF component sample

This sample shows how to generate content using a prompt defined by Copilot Studio or AI Builder

This sample is a Power Apps Component Framework (PCF) control that integrates with Code Interpreter–enabled prompts to render interactive HTML/JavaScript data visuals or generate previews and downloads for PDF, Word, PowerPoint and Excel files.

## Available for

Model-driven apps

## Code

You can find the code for sample here: [PowerApps-Samples/component-framework/CodeInterpreterControl/](https://github.com/microsoft/PowerApps-Samples/tree/master/component-framework/CodeInterpreterControl).

> [!IMPORTANT]
> See the sample README for detailed instructions about how to build the control and configure the PCF component in the form.

## Demonstrates

This example demonstrates how a single PCF control can render different output in the model-driven app form that depends on the prompt provided. This sample provides a solution you can install that contains three prompts that are prepared for you.

### Prompt: Create sample data for the example table

The provided solution includes the definition for a table named `sample_example`. Testing this prompt creates 10 sample records to use in this demonstration.

:::image type="content" source="media/code-interpreter-create-sample-data-prompt.jpg" alt-text="A prompt designed to create sample data for the sample_example table":::

> [!TIP]
> Copy one of the example GUID values to set as a test `sample_example` record for your environment when you test the other prompts.

### Prompt: Example interactive row summary chart

This prompt specifies an interactive chart that returns a mimetype of text/html:

:::image type="content" source="media/code-interpreter-interactive-row-summary-chart-prompt.png" alt-text="Example interactive row summary chart prompt":::

> [!TIP]
> If you **Test** this prompt, use one of the example GUID values from the first prompt and set it as the **Sample data** for the **RecordId** parameter.

:::image type="content" source="media/code-interpreter-set-recordid.png" alt-text="Setting sample data for the recordid parameter":::

The HTML isn't currently rendered in the **Model response**, but you can view the **Run details** to confirm it ran successfully.

The control renders this interactive HTML within the form:

:::image type="content" source="media/code-interpreter-comparison-credit-limit-accross-records.png" alt-text="The code interpreter PCF component sample showing generated HTML interactive row summary chart":::

### Prompt: Example sales proposal document

This prompt specifies a preview and direct download for this generated PDF file.

:::image type="content" source="media/code-interpreter-sales-proposal-prompt.png" alt-text="foo":::

> [!TIP]
> If you **Test** this prompt, use one of the example GUID values from the first prompt and set it as the **Sample data** for the **RecordId** parameter.

If you **Test** this prompt, you can preview results in the **Model response**.

The control renders a different experience within the form:

:::image type="content" source="media/code-interpreter-sales-proposal.png" alt-text="The code interpreter PCF component sample showing generated PDF sales proposal document":::

Generated .docx, .pptx and .xlsx files are also supported, but the sample PCF control currently doesn't support .pptx.

### App: sample_example app

The solution also includes a pre-configured model-driven application with form available for you to configure the CodeInterpreter PCF control.
