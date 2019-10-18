---
title: "Create Custom Help Pages | MicrosoftDocs"
description: "Create custom help pages on UCI"
ms.custom: ""
ms.date: 09/13/2019
ms.reviewer: ""
ms.service: "powerapps"
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "get-started-article"
applies_to: 
  - "Dynamics 365 (online)"
  - "Dynamics 365 Version 9.x"
  - "powerapps"
ms.assetid: 
caps.latest.revision:
author: "Mattp123"
ms.author: "matp"
manager: "kvivek"
search.audienceType: 
  - maker
search.app: 
  - PowerApps
  - D365CE
---

# Create guided help for your Unified Interface app [Public Preview]

[!INCLUDE [cc-beta-prerelease-disclaimer](../../includes/cc-beta-prerelease-disclaimer.md)]

Use Custom Help Panes and Guided Tasks (“Custom Help Panes”) to give your UCI application a custom in-product help experience that is tailored to your organization.  Use Custom Help Panes to provide entity, form, and language specific help and guidance that includes rich text, content links, images, and video links.  Custom Help panes (UCI) replace the previous Learning Path (WebClient) guided learning feature.

## Custom Help Panes and Learning Path

The new guided help implementation of Custom Help Panes differs from the previous Learning Path guided help feature.  Both features enable you to create custom help for your application however Custom Help Panes is optimized for the most common guided help scenarios.   

Custom Help Panes **provide** the following key features that are not available on Learning Path: 
* Free-form rich text – including bullets and numbering.
* Visibly linked coachmarks and help balloons.
* More options for video sources (including private sources.)
* Storage of help content in the Common Data Service as part of your solution. 

Custom Help Panes **do not provide** the following key features that are in Learning Path: 
* Sequential help balloons
* Help pages per role
* Help pages for per device form factor (e.g., phone)

## Prerequisites 

You must have Dynamics version <<Need a version #>>

## Turn on Custom Help Panes for your account.

1. Sign into Dynamics 365 with an admin account.
2. Go to **Settings**, and the select **Administration** under **System**.  
3. On the **Administration** page, select **System Settings**.
4. On the **General** tag, under **Set custom Help URL**, select **Yes** for **“Enable Custom Help Panes and Guided Tasks.”**

You can enable Custom Help Panes or customizable Help, but not both at the same time. Confirm that Use custom Help for customizable entities and Append parameters to URL are set to No.  

 
## Context sensitive custom help

Each help pane is unique for a context of 1. application, 2. entity, 3. form, and 4. language.   

## Help pane navigation

By default, a help page stays open and on the help content you first opened it with even when you navigate to a different form.  This allows for the help content to remain intact as you direct users to different parts of the product. 

## Authoring Custom Help Panes

To author a Custom Help Pane you must have sufficient rights.  Several roles have rights – including administrator.  The Help Page Author role specifically gives rights for this capability.

### To author help pane content
1.	Open the help pane by selecting the ? icon.   This will open the help pane. 
2.	Select the vertical ellipses and select Edit.  This will place the help pane in edit mode and position the cursor on the title.
3.	Add content by either typing directly in the help page area or insert sections, video, images, links, coachmarks or balloon help.
4.	Save your content by selecting the Save button.  This will either create a new help record in the Help Page entity or update one. 

### Free form text

Text can live anywhere.  Enter free form text before, in, or after sections.   Text supports bold, italic, and strike out formats.  Cut, copy, and paste are supported as is multi-level undo. 

### Bullets and numbering

Selecting the bullet or number icon will toggle the current line to be bulleted/numbered.  If you have multiple lines selected, it will bullet/number each line.  Tabbing / indenting will sub-number a line.  

### Sections

A section is a collapsible text box.  You can put links or free form text in it.  Use a section to group like items.  It can be either open or collapsed by default. 

### Video and static images

You can insert videos and static images into your help pane. (Be sure to copy the linkURL.) These are links to content on the internet.   Custom Help Panes do not store these assets in your help pane.  When the help pane is opened, Custom Help Panes bring the content in from the link to display it.  You can use a link to a Microsoft Stream video if you wish to reference corporate private content.  Custom Help Panes support the following video sources.

* Microsoft Stream (use for private content.) 
* YouTube
* Facebook
* Vimeo


### Links

Links can be to websites (including in Dynamics) and open in the same window (the default) or open in a separate window.  The ability to link to an existing help page is not yet enabled.   


### Balloons and Coach marks

Balloons and coach marks can be used to point to specific UI elements.  A balloon can have text in it.  A coach mark simply highlights an element with a coach pointer.  A way to illustrate several UI elements sequentially is to simply collect links in a list that the user can select.  For instance:

1. Link to first UI element with instructions / comments.
2. Link to second UI element with instructions / comments.
3. Link to third UI element with instructions / comments.

A user can easily either select element in order or go back to a specific one and just highlight it.

# Solutions and Custom Help Pane content

All help content is stored in a Help Page component in CDS as part of your solution.  When you move your solution from one environment to another (e.g., test to production) you can define that your help records are exported and move with the solution.  This enables you to keep your help content in sync with features in your solution as it moves to different environments.  As a part of your solution, Custom Help Panes participate in all standard Solution ALM features.

## Moving content via solutions

By default, all new Help Pages will appear in the default solution. If you want to move your content to another environment, you will need to first add your existing Help Pages into an unmanaged solution before you can export them. To add a Help Page to an unmanaged solution:

1. Navigate to your unmanaged solution.
2. Select **Switch to classic** from the ellipses in the command bar.
3. Select **Add Existing**.
4. Select **Help Page**.
5. Check the Help Pages that you want to add and select **Ok**.

> [!NOTE]
> Currently it is not possible to add existing Help Panes to an unmanaged solution in the modern solution explorer. Support for this functionality will come as custom help panes and guided tasks becomes GA.






# Help page documentation automation

Many customers like to back up or store their content in a source code control system.  Some customers also like to use documentation automation tools (e.g., translation tools, checkers, … ) on content as well.  The Custom Help Pane data is stored directly in CDS and can be exported and imported for this purpose.  

Microsoft uses and supports a custom HTML format for the help content.  This format is documented below for customer reference.  

When exported, each help page is exported as a separate file.   


# Frequently asked questions

## Are Custom Help Panes the same as Customizable Help?

Custom Help Panes and Guided Tasks are an option in the **Set custom help URL ** section of System Settings.  Custom Help Panes and Guided tasks enable a customizable help pane that shows up right next to the user’s form.  The other options in this section comprise the Customizable Help features. They allow you to to override the default Dynamics 365 apps Help and point users in your organization to a different URL for Help. Or you can override the Help for a highly customized entity so that you can better describe your workflow.

For more information about customizable Help, see Customize the Help experience. <https://docs.microsoft.com/en-us/previous-versions/dynamicscrm-2016/administering-dynamics-365/dn832079(v=crm.8)?redirectedfrom=MSDN>


## How do I migrate my data from Learning Path (WebClient) to Custom Help Panes (UCI)

Learning Path has two types of help: help panes and sequential help balloons.   The sequential help balloon locations are deeply integrated with the WebClient UI and are not transferrable to the new Custom Help Panes.  

Depending on how much text you have in your guided help it might be easiest to simply copy the information directly from the Learning Path user interface to the new Custom Help Pane user interface.  However, you can also export your Learning Path help content.  The simplest way to do this is to export your content using the Learning Path > Content Library > Localize > Export feature.  Select the records you wish to export and export them.  This creates an XLIFF file for each help pane and guided task.  Then, use a publicly available XLIFF editor or XLIFF to HTML converter to retrieve your content.



# Custom Help XML definition

## PPHML

```
<pphml>
    <h1>FAQ</h1>
    <collapsible title="What is PPHML?">
        <p>PPHML is a domain specific language for help content. It is used to create help content that includes elements such as images, videos, balloons, coachmarks, etc.</p>
    </collapsible>
    <collapsible title="What does PPHML stand for?">
        <p>PPHML stands for Power Platform Help Markup Language</p>
    </collapsible>
</pphml>
```

### Definition and Usage

The `<pphml>` tag tells the Help browser that this is a PPHML document.

The `<pphml>` tag represents the root of a PPHML document.

The `<pphml>` tag is the container for all other PPHML elements.

## Title

How to represent a title in a Help Page:

```
<h1>This will be displayed at the top of the Help Page</h1>
```

### Definition and Usage

The **`<h1>`** tag defines the title of a Help page.

`<h1>` This must be the first element inside `<pphml>`.

## Image

How to represent an image in a Help Page:

```
<img src="smiley.gif" alt="Smiley face" title="Smiley face"/>
```

### Definition and Usage

The **`<img>`** tag embeds an image in a Help page.

### Attributes

- `src`: Specifies the URL of an image. Required.

- `title`: Specifies a title to show along with the image, typically as a hover tooltip.

- `alt`: Specifies an alternate text for an image. This text is used by screen readers.

## Video

How to represent a video in a Help Page:

```
<video src="https://www.youtube.com/watch?v=WSWmn7WM3i4" />
```

### Definition and Usage

The **`<video>`** tag embeds a video, such as a tutorial or training movie in a Help page.

#### Supported sources

- Microsoft Stream
- YouTube
- Facebook
- Vimeo

### Attributes

- `src`: Specifies the URL of the video. Required.

- `allowFullScreen`: Specifies whether the user can switch the video to full screen. Possible values are "true" or "false". Not supported for all video sources.

- `autoplay`: Specifies that the video will start playing as soon as the Help Page loads. Possible values are "true" or "false". Not supported for all video sources.

- `startTime`: Specifies -in seconds- from which point to start playing the video.

## Paragraph

How to represent a paragraph in a Help Page:

```
<p>This is some text in a paragraph.</p>
```

### Definition and Usage

The **`<p>`** tag defines a paragraph.

Text inside a paragraph can be decorated in the following ways:

- bold, with `<strong>` tag
- italic, with `<em>` tag
- strikethrough, with `<del>` tag
- underline, with `<u>` tag

These decorations can be combined, making it possible to -for example- have a fragment of text that is both bold and underline at the same time.

## Bulleted List

How to represent a bulleted list in a Help Page.

```
<ul>
    <li>Coffee</li>
    <li>Tea</li>
    <li>Milk</li>
</ul>
```

### Definition and Usage

The **`<ul>`** tag defines a bulleted list.

Use the `<ul>` tag together with the `<li>` tag to create bulleted lists.

## Numbered List

How to represent a numbered list in a Help Page:

```
<ol>
    <li>First step</li>
    <li>Second step</li>
    <li>Third step</li>
</ol>
```

### Definition and Usage

The **`<ol>`** tag defines an ordered list.

Use the `<ol>` tag together with the `<li>` tag to create numbered lists.

## Collapsible

How to represent a collapsible in a Help Page:

```
<collapsible title="This is a Section">
    <p>This is a paragraph inside a section</p>
    <img src=smiley.gif" title="This is an image inside a section" />
</collapsible>
```

### Definition and Usage

The **`<collapsible>`** tag defines a section of content that the user can view or hide on demand.

### Attributes

- `collapsed`: Specifies whether the collapsible is expanded or collapsed initially. Possible values are "true" or "false".

## Link

How to represent a link in a Help Page:

Link to a Website (opens in a new window)

```
<a href="https://www.microsoft.com" target="_blank">Microsoft Home Page</a>
```

Link to another Help Page

```
<a href="./LearnMore">Learn More</a>
```

### Definition and Usage

The `<a>` tag defines a link, which allows the user to navigate from a Help Page to a Website, or to another Help Page.

### Attributes

- `href`: Specifies the URL of the Website or Help Page to which to navigate. Required.
- `target`: Specifies where to open the linked URL.
  -- If not present or `_self`, the Link is assumed to be to another Help Page and it's opened in the Help browser.
  -- If `_blank`, the link is opened in a new browser window.
  -- If `_top`, the Link is opened in the current browser window.
  -- If the value is the name of an [`iframe`](https://www.w3schools.com/tags/tag_iframe.asp), the link is opened in that `iframe`.

## Coachmark

How to represent coachmark in a Help Page:

```
<coachmark target="#my-html-button">Click to highlight the HTML element with id [my-html-button]</coachmark>
```

### Definition and Usage

A coachmark is an interactive element that can be used to draw the user's attention to a specific point in the UI of the application hosting the Help browser.

### Attributes

- `target`: [CSS selector](https://www.w3schools.com/cssref/css_selectors.asp) that specifies the HTML element over which the coachmark will be shown. Required.

## Balloon

How to represent a balloon in a Help Page:

```
<balloon target="#my-html-button" title="This button submits the form" details="Please click this button to continue and submit the form">Click to show a balloon over the HTML element with id [my-html-button]</balloon>
```

### Definition and Usage

A balloon is an interactive element that can be used to help the user perform an action in the UI of the application hosting the Help browser.

### Attributes

- `target`: [CSS selector](https://www.w3schools.com/cssref/css_selectors.asp) that specifies the HTML element over which the balloon link will shown. Required.
- `title`: Specifies the title of the balloon.
- `details`: Specifies the content to show inside the balloon.


