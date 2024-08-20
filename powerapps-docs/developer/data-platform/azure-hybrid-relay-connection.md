---
title: Use an Azure hybrid relay connection
description: Learn about sending Dataverse message processing data to Azure using the ServiceBus and a hybrid relay connection. 
author: phecke
ms.author: pehecke
ms.subservice: dataverse-developer
ms.topic: concept-article
ms.date: 08/19/2024
---

# Use an Azure hybrid relay connection

There are different types of messaging contracts with Microsoft Azure that Microsoft Dataverse supports - queue, one-way, REST, topic, etc. This article will delve into the hybrid relay connection, which uses a REST contract, as a means to send the Dataverse execution context across the Azure ServiceBus to a listener app.

The hybrid relay is presently the only supported Dataverse to Azure ServiceBus connection type that:

- You can target a .NET Core build of a listener app
- Uses the latest [Microsoft.Azure.Relay](https://www.nuget.org/packages/Microsoft.Azure.Relay#supportedframeworks-body-tab) messaging APIs

So if you are interested in developing a .NET Core version of ServiceBus listener app today, read on.

<!-- 2. Introductory paragraph
----------------------------------------------------------

Required. Lead with a light intro that describes what the article covers. Answer the fundamental “why would I want to know this?” question. Keep it short.

* Answer the fundamental "Why do I want this knowledge?" question.
* Don't start the article with a bunch of notes or caveats.
* Don’t link away from the article in the introduction.
* For definitive concepts, it's better to lead with a sentence in the form, "X is a (type of) Y that does Z."

-->

[Introductory paragraph]
TODO: Add your introductory paragraph

<!-- 3. Prerequisites --------------------------------------------------------------------

Optional: Make **Prerequisites** your first H2 in the article. Use clear and unambiguous
language and use a unordered list format. 

-->

## Prerequisites

TODO: [List the prerequisites if appropriate]

<!-- 4. H2s (Article body)
--------------------------------------------------------------------

Required: In a series of H2 sections, the article body should discuss the ideas that explain how "X is a (type of) Y that does Z":

* Give each H2 a heading that sets expectations for the content that follows.
* Follow the H2 headings with a sentence about how the section contributes to the whole.
* Describe the concept's critical features in the context of defining what it is.
* Provide an example of how it's used where, how it fits into the context, or what it does. If it's complex and new to the user, show at least two examples.
* Provide a non-example if contrasting it will make it clearer to the user what the concept is.
* Images, code blocks, or other graphical elements come after the text block it illustrates.
* Don't number H2s.

-->

## [Section 1 heading]

All Dataverse to Azure ServiceBus supported connection types, other than the hybrid relay connection, target .NET Framework and use the (now) deprecated Microsoft.WindowsAzure.Messaging APIs. Those connections will continue to be supported for some time since the Microsoft.WindowsAzure.Messaging APIs will be supported by Microsoft until the year 2026.

## [Section 2 heading]

TODO: add your content

## [Section n heading]

TODO: add your content

<!-- 5. Next step/Related content ------------------------------------------------------------------------ 

Optional: You have two options for manually curated links in this pattern: Next step and Related content. You don't have to use either, but don't use both.
  - For Next step, provide one link to the next step in a sequence. Use the blue box format
  - For Related content provide 1-3 links. Include some context so the customer can determine why they would click the link. Add a context sentence for the following links.

-->

## Next step

TODO: Add your next step link(s)

> [!div class="nextstepaction"]
> [Write concepts](article-concept.md)

<!-- OR -->

## Related content

TODO: Add your next step link(s)

- [Write concepts](article-concept.md)

<!--
Remove all the comments in this template before you sign-off or merge to the main branch.
-->

<!-- 6. Next step/Related content ------------------------------------------------------------------------

Optional: You have two options for manually curated links in this pattern: Next step and Related
content. You don't have to use either, but don't use both. For Next step, provide one link to the
next step in a sequence. Use the blue box format For Related content provide 1-3 links. Include some
context so the customer can determine why they would click the link. Add a context sentence for the
following links.

-->

## Next step

TODO: Add your next step link(s)
> [!div class="nextstepaction"]
> [Write concepts](article-concept.md)

<!-- OR -->

## Related content

TODO: Add your next step link(s)

- [Write concepts](article-concept.md)

<!--
Remove all the comments in this template before you sign-off or merge to the 
main branch.

-->
