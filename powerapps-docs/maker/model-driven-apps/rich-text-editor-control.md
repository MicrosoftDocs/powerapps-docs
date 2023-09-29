---
title: Add the rich text editor control to a model-driven app
description: Learn how to add and customize the rich text editor control in Power Apps model-driven apps to create and edit formatted text.
ms.date: 08/25/2023
ms.topic: how-to
ms.author: "craigm"
author: Mattp123
ms.reviewer: matp
ms.subservice: mda-maker
search.audienceType:
 - maker
ms.custom:
 - bap-template
 - ai-gen-docs-bap
 - ai-gen-desc
 - ai-seo-date:09/28/2023
---

# Add the rich text editor control to a model-driven app

The rich text editor control is a lightweight, HTML-based editor built on the popular CKEditor plug-in framework. It lets you create, paste, and edit formatted text in text columns in your model-driven apps.

To format the text, you can use the editor toolbar or HTML tags. You can also paste formatted text from other applications, like a web browser or Word. You can customize its appearance, features, and behavior. The control's default configuration is shown in the following screenshot.

:::image type="content" source="./media/rich-text-control.png" alt-text="Screenshot of the default rich text editor in a model-driven app.":::

## Add the rich text editor control to a text column

When you format a text column as rich text, the default rich text editor control is added automatically.

1. Sign in to [Power Apps](https://make.powerapps.com/?powerappsEntities.enableColumnFormatUpdate=true&powerappsEntities.enableModernColumn=true).
1. In the left navigation pane, select **Solutions**.
1. Open a solution and a table in the solution.
1. In the **Columns and data** area, select a text column.

    If the table doesn't contain a text column, select **+** (**New column)** and enter a name for the column.

1. In **Data type**, select **>** to the right of **Text**, and then select the appropriate **Rich text** option based on whether the column will contain a single line of text or multiple lines.
1. Save the column, and then add it to a form.

## Add the rich text editor control to a text column in a form

1. Sign in to [Power Apps](https://make.powerapps.com/?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc).
1. In the left navigation pane, select **Solutions**.
1. Open a solution and a table in the solution.
1. In the **Data experiences** area, select **Forms**, and then find the form that contains the text column you want to add the rich text editor to.
1. Select **&vellip;** > **Edit** > **Edit in new tab**.
1. On the form designer canvas, select, add, or create a text column.
1. In the column properties pane, expand the **Components** list, select **+ Component**, and then select **Rich Text Editor Control**.
1. In the **Add Rich Text Editor Control** pane, select **Web**, **Phone**, and **Tablet** to allow apps running on any device to use the editor.

    If you want to [customize the editor](#customize-the-rich-text-editor-control), enter the relative URL of its configuration file, a JavaScript web resource that contains the properties you want to change, in the **Static value** box. If you leave this field empty, the editor uses its default configuration.

1. Select **Done**.
1. Select **Save and publish** to apply your changes to the form.

## Customize the rich text editor control

Power Apps allows you to change the properties of the rich text editor control to customize its appearance, features, and behavior. To [customize a specific instance of the control](#customize-a-specific-instance-of-the-rich-text-editor), specify properties and their values in JSON format in a JavaScript web resource. To [customize the control's global configuration](#use-the-default-web-resource-for-organization-wide-changes), change the properties in the default web resource.

### Levels of customization

Up to three levels, or layers, of configuration can be applied to customize the rich text editor:

1. At the most fundamental level, every instance of the control takes its configuration from the file `RTEGlobalConfiguration_Readonly.json`. The file is read-only, so you can't change these properties directly.
1. At the next level, every instance of the control takes its configuration from the properties in the file `RTEGlobalConfiguration.json`. This configuration is layered on top of the previous one, so the properties in this file *replace* the same named properties in the read-only file.
1. Finally, at the highest level, a specific instance of the control takes its configuration from a specific configuration file, if one exists. This configuration is layered on top of the previous one, so the properties in this file *replace* the same named properties in the two lower-level files.

We have to add a slight qualification here. Not *all* properties are replaced by those in a higher-level configuration. The `extraPlugins` properties are merged to allow the use of a wide range of external and out-of-the-box plug-ins in the default configuration. That lets you activate and deactivate plug-ins as needed in the configuration file for specific instances of the control.

### Customize a specific instance of the rich text editor

1. In Visual Studio Code or other text editor, create a file and give it a meaningful name.

    The file `RTEGlobalConfiguration.json` contains the rich text editor's default, or global, configuration. If you're customizing the control in, say, a contact form, you might name the file something like `RTEContactFormConfiguration.json`.

1. Copy and paste the following code snippet in the file:

    ```json
    "defaultSupportedProps": {
      "propertyName": "value",
      "propertyName": "value",
      "propertyName": "value"
    },
    ```

    Note that the last *propertyName:value* pair doesn't end with a comma.

1. Replace *propertyName* and *value* with the [rich text editor control properties](#rich-text-editor-properties) you want to change. String values must be enclosed in quotation marks.

      We've provided a few [example configurations](#example-configurations) for you, but you can define others to suit your needs.

1. In Power Apps, [create a **JavaScript (JS)** type web resource](create-edit-web-resources.md) using the JSON file you created in step 1.
1. [Add the rich text editor control to a text column in a form](#add-the-rich-text-editor-control-to-a-text-column-in-a-form) and in the **Add Rich Text Editor Control** pane > **Static value**, enter the relative URL of the JavaScript web resource.

      Although you may enter the absolute URL of the web resource, we recommend you enter the relative URL. That way, the web resource still works if you import it as a solution into a different environment, provided the relative path is the same.

      For example, if the URL of the web resource is *https://yourorg.crm.dynamics.com/WebResources/rtecontactform*, the relative URL is */WebResources/rtecontactform*.

1. Select **Done**.
1. Select **Save and publish** to apply your changes to the form.

## Rich text editor properties

The JSON file that determines the "look and feel" of an instance of the rich text editor contains two sets of properties:

- The [`defaultSupportedProps` section](#defaultsupportedprops) contains properties of plug-ins that determine what the control can do. You're not limited to the properties of [CKEditor and its plug-ins](https://ckeditor.com/cke4/addons/plugins/all). You can also set values for properties of plug-ins that you add or create.
- The [individual properties section](#individual-properties) contains properties that determine what the control looks like.

### Example configuration file

The following code is an example of a JSON file that contains both [`defaultSupportedProps`](#defaultsupportedprops) properties and [individual configuration properties](#individual-properties). If a property has a default value, the default value is shown. If a property doesn't have a default value, a sample value is shown to illustrate the syntax. The properties are described in the two tables that follow.

```json
"defaultSupportedProps": {
  "height": 185,
  "stickyStyle": {
    "font-size": "9pt",
    "font-family": "'Segoe UI','Helvetica Neue',sans-serif"
  },
  "stickyStyles_defaultTag": "div",
  "font_defaultLabel": "Segoe UI",
  "fontSize_defaultLabel": "9",
  "toolbarLocation": "bottom",
  "toolbar": [
  [ "CopyFormatting" ],
  [ "Font" ],
  [ "FontSize" ],
  [ "Bold" ],
  [ "Italic" ],
  [ "Underline" ],
  [ "BGColor" ],
  [ "TextColor" ],
  [ "BulletedList" ],
  [ "NumberedList" ],
  [ "Outdent" ],
  [ "Indent" ],
  [ "Blockquote" ],
  [ "JustifyLeft" ],
  [ "JustifyCenter" ],
  [ "JustifyRight" ],
  [ "Link" ],
  [ "Unlink" ],
  [ "Subscript" ],
  [ "Superscript" ],
  [ "Strike" ],
  [ "Image" ],
  [ "BidiLtr" ],
  [ "BidiRtl" ],
  [ "Undo" ],
  [ "Redo" ],
  [ "RemoveFormat" ],
  [ "Table" ]
 ],
  "plugins": [["button,toolbar,dialogui,dialog,autogrow,notification,clipboard,textmatch,fakeobjects,link,autolink,basicstyles,bidi,blockquote,panelbutton,panel,floatpanel,colorbutton,colordialog,listblock,richcombo,menu,contextmenu,copyformatting,enterkey,entities,popup,find,floatingspace,font,format,htmlwriter,horizontalrule,indent,indentblock,indentlist,justify,lineutils,openlink,list,liststyle,maximize,undo,menubutton,notificationaggregator,xml,ajax,pastetools,pastefromword,pastetext,preview,table,quicktable,removeformat,resize,selectall,showborders,sourcearea,specialchar,stylescombo,tab,tabletools,tableresize,tableselection,widgetselection,widget,wysiwygarea,textwatcher"]],
  "extraPlugins": "accessibilityhelp,autogrow,autolink,basicstyles,bidi,blockquote,button,collapser,colorbutton,colordialog,confighelper,contextmenu,copyformatting,dialog,editorplaceholder,filebrowser,filetools,find,floatpanel,font,iframerestrictor,indentblock,justify,notification,panel,panelbutton,pastefromword,quicktable,selectall,stickystyles,superimage,tableresize,tableselection,tabletools,uploadfile,uploadimage,uploadwidget",
  "removePlugins": "a11yhelp,codemirror,magicline,scayt,showborders",
  "superimageImageMaxSize": 5,
  "disallowedContent": "form[action]; *[formaction]; script; *[on*]",
  "linkTargets": ["notSet", "_blank"],
},
"attachmentEntity": {
  "name": "msdyn_richtextfiles",
  "fileAttributeName": "msdyn_fileblob"
},
"disableContentSanitization": true,
"disableDefaultImageProcessing": false,
"disableImages": false,
"externalPlugins": [
  {
    "name": "EmbedMedia",
    "path": "/WebResources/msdyncrm_/myplugins/embedmedia/"
  }
],
"imageEntity": {
  "imageEntityName": "msdyn_richtextfiles",
  "imageFileAttributeName": "msdyn_imageblob"
},
"readOnlySettings": {
  "height": 500,
  "showFullScreenExpander": true
},
"sanitizerAllowlist": {
  "attributes": [],
  "cssProperties": [],
  "domains": [],
  "protocols": [],
  "tags": []
},
"showAsTabControl": false,
"showFullScreenExpander": false,
"showHtml": false,
"showPreview": false,
"showPreviewHeaderWarning": false,
"allowSameOriginSandbox": false
```

### defaultSupportedProps

The following table describes the most commonly used properties, but you can configure all the [properties that CKEditor supports](https://ckeditor.com/docs/ckeditor4/latest/api/CKEDITOR_config.html). The rich text editor control uses CKEditor 4.

| Property | Description | Default value |
| --- | --- | --- |
| height | Sets the initial height of the content area, in pixels. | "185" |
| stickyStyle | Sets the editor font and size. | See [defaultSupportedProps](#defaultsupportedprops) |
| stickyStyles_defaultTag | Creates a wrapper around the text in the editor content area. It's initially set to "div", but you can change it to "p" or any alternate tag. | "div" |
| font_defaultLabel | Sets the font label that's displayed in the toolbar. The label is for appearance only and isn't functional. The `stickyStyle` property determines the editor font and size. | "Segoe UI" |
| fontSize_defaultLabel | Sets the font size label that's displayed in the toolbar. The label is for appearance only and isn't functional. The `stickyStyle` property determines the editor font and size. | "9" |
| toolbarLocation | Sets the location of the toolbar in the editor content area. Supported values are "top" and "bottom". | "bottom" |
| toolbar | Lists the toolbar buttons to display. | See [defaultSupportedProps](#defaultsupportedprops) |
| plugins | Lists pre-set plug-ins that the editor can use. The plug-ins in this list might be different from the plug-ins that are loaded, if `extraPlugins` and `removePlugins` are given a value. If you set this property to an empty string, the editor loads without the toolbar. | See [defaultSupportedProps](#defaultsupportedprops) |
| extraPlugins | Appends plug-ins to the `plugins` list to load additional plug-ins.<br/>Many plug-ins require other plug-ins to work. The rich text editor automatically adds them, and you can't use this property to override them. Use `removePlugins` instead. | See [defaultSupportedProps](#defaultsupportedprops) |
| removePlugins | Lists plug-ins not to load. Use it to change which plug-ins are loaded without changing the `plugins` and `extraPlugins` lists. | See [defaultSupportedProps](#defaultsupportedprops) |
| superimageImageMaxSize | Sets the maximum size in megabytes (MB) allowed for embedded images when using the superimage plug-in. | "5" |
| [disallowedContent](https://ckeditor.com/docs/ckeditor4/latest/guide/dev_disallowed_content.html#disallowed-content-rules) | Lets you prevent users from inserting elements that you don't want to have in your content. You can disallow entire elements or by attributes, classes, and styles. | See [defaultSupportedProps](#defaultsupportedprops) |
| linkTargets | Allows you to configure which link target options are available for users when they create links:<br/>- "notSet": No target set<br/>- "frame": Opens the document in the specified frame<br/>- popupWindow": Opens the document in a popup window<br/>- "_blank": Opens the document in a new window or tab<br/>- "_top": Opens the document in the full body of the window<br/>- "_self": Opens the document in the same window or tab where the link is activated<br/>- "_parent": Opens the document in the parent frame | "notSet", "_blank" |
| | |

### Individual properties

The following table describes additional properties you can use to customize the rich text editor control.

| Property | Description | Default value |
| --- | --- | --- |
| attachmentEntity | To enforce more security on [uploaded files](/power-apps/developer/data-platform/file-attributes) by using a table other than the default, set this property and specify a different table.<br/>Syntax: "name": "*tableName*", "fileAttributeName": "*attributeNameofBlobReference*" | See [defaultSupportedProps](#defaultsupportedprops) |
| disableContentSanitization | Content sanitization removes some custom attributes or tags from rich text content. It's disabled by default to allow copying and pasting of rich text content from external sources. This property applies only to edit mode. When the editor control is read-only or disabled, content is always sanitized. | true |
| disableDefaultImageProcessing | By default, images that are inserted in the editor are uploaded to the `attachmentEntity` defined in the configuration. External users might lack privileges to view the content in the table. Instead, set this property to true to store images as base64 strings directly in the column that's configured to use the rich text editor control. | false |
| disableImages | Determines whether images can be inserted in the editor. This property has highest priority. When this property is set to true, images are disabled, regardless of the value of the `imageEntity` property. | false |
| externalPlugins | Lists external plug-ins or plug-ins that you create that can be used in the rich text editor control.<br/>Syntax: "name": "*pluginName*", "path": "*pathToPlugin*" (the path value can be an absolute or relative URL) | None; see [defaultSupportedProps](#defaultsupportedprops) for an example |
| imageEntity | To enforce more security on [images](/power-apps/developer/data-platform/image-attributes) by using a table other than the default, set this property and specify a different table.<br>Syntax: "imageEntityName": "*tableName*", "imageFileAttributeName": "*attributeNameofBlobReference*" | See [defaultSupportedProps](#defaultsupportedprops) |
| readOnlySettings | These properties determine the behavior of the column when it's viewed in a read-only or disabled state. You can specify any supported property. | None; see [defaultSupportedProps](#defaultsupportedprops) for an example |
| sanitizerAllowlist | Lists additional kinds of content that can be displayed in the editor. | See [defaultSupportedProps](#defaultsupportedprops) |
| showAsTabControl | Allows you to display more commands above the content area. Must be set to true to use the following properties: `showFullScreenExpander`, `showHtml`, `showPreview`, `showPreviewHeaderWarning` | false |
| showFullScreenExpander | Determines whether the editor can be used in full-screen mode. `showAsTabControl` must be set to true. | false |
| showHtml | Allows users to display and edit the HTML content directly. `showAsTabControl` must be set to true. | false |
| showPreview | Allows users to preview the editor content rendered as HTML. `showAsTabControl` must be set to true. | false |
| showPreviewHeaderWarning | Allows you to show or hide the warning message that's displayed when previewing content. `showAsTabControl` and `showPreview` must be set to true. | false |
| allowSameOriginSandbox | Allows the content in the editor to be treated as from the same origin as the rendering app.<br/>**Use this property with caution.** Only use trusted external content. When this property is set to true, any external content could have access to internal resources. | false |
| | | |

## Example configurations Rhana

The following are common configurations for the rich text editor. These sample configurations can be used to enable specific types of rich text experiences. For each sample, you create a JSON web resource or modify the default web resource configuration. More information: [Create and use advanced configuration for the rich text editor control](#create-and-use-advanced-configuration-for-the-rich-text-editor-control) and [Use the default web resource for organization-wide changes](#use-the-default-web-resource-for-organization-wide-changes)

### Set the default font to Calibri with font-size 11 pt
Set your default font and size to match the Microsoft Windows defaults. This example shows which settings you use to implement this change in your experience.

Set these ```defaultSupportedProps``` properties in your configuration file. Each value should be followed by a ```,``` (```comma```) unless it's the last value:
(More information: [defaultSupportedProps](#visualization-of-the-rich-text-editor-configuration-file))
 ```

  "font_defaultLabel": "Calibri"
  
  "fontSize_defaultLabel": "11"
  
  "stickyStyle": {
   "font-size": "11pt",
   "font-family": "Calibri/Calibri, Helvetica, sans-serif;"
  }

 ```

 ### Make line breaks (Enter key) create a &lt;br&gt; instead of &lt;p&gt;
 The default behavior for the enter key creates paragraph blocks with the &lt;p&gt; HTML tag (also used when interpreting pasted content). Paragraph blocks are used in HTML to group information. In some cases, when creating new or pasting information from Microsoft Word or other content editor, due to how each browser interprets the formatting for the paragraph block tag (&lt;p&gt;) slightly differently, you might want to use the &lt;br&gt; HTML tag instead of paragraph blocks. The vertical spacing for &lt;br&gt; HTML tags in certain cases can be more visually consistent across a variety of browsers and experiences. This example shows you how to change from &lt;p&gt; to &lt;br&gt;.

Set this ```defaultSupportedProps``` property in your configuration file. Each value should be followed by a ```,``` (```comma```) unless it's the last value:
(More information: [defaultSupportedProps](#visualization-of-the-rich-text-editor-configuration-file))
 ```

  "enterMode": 2

 ```

### All content pasted or created is HTML 5 compliant
The rich text editor control works best with HTML 5 content, although HTML 4 tags and formatting can also be used successfully. In some cases, the mixture of both HTML 4 and HTML 5 tags can create usability challenges when selecting and setting fonts and sizes. Use of "allowedContent" can ensure all your content is HTML 5. This example allows all supported HTML 5 tags. Any non-compliant tags are converted to their HTML 5 equivalent.

Set this ```defaultSupportedProps``` property in your configuration file. Each value should be followed by a ```,``` (```comma```) unless it's the last value:
(More information: [defaultSupportedProps](#visualization-of-the-rich-text-editor-configuration-file))
 ```

  "allowedContent": "a(*)[*]{*};abbr(*)[*]{*};address(*)[*]{*};area(*)[*]{*};article(*)[*]{*};aside(*)[*]{*};audio(*)[*]{*};b(*)[*]{*};base(*)[*]{*};bdi(*)[*]{*};bdo(*)[*]{*};blockquote(*)[*]{*};body(*)[*]{*};br(*)[*]{*};button(*)[*]{*};canvas(*)[*]{*};caption(*)[*]{*};cite(*)[*]{*};code(*)[*]{*};col(*)[*]{*};colgroup(*)[*]{*};data(*)[*]{*};datalist(*)[*]{*};dd(*)[*]{*};del(*)[*]{*};details(*)[*]{*};dfn(*)[*]{*};dialog(*)[*]{*};div(*)[*]{*};dl(*)[*]{*};dt(*)[*]{*};em(*)[*]{*};embed(*)[*]{*};fieldset(*)[*]{*};figcaption(*)[*]{*};figure(*)[*]{*};footer(*)[*]{*};form(*)[*]{*};h1(*)[*]{*};h2(*)[*]{*};h3(*)[*]{*};h4(*)[*]{*};h5(*)[*]{*};h6(*)[*]{*};head(*)[*]{*};header(*)[*]{*};hr(*)[*]{*};html(*)[*]{*};i(*)[*]{*};iframe(*)[*]{*};img(*)[*]{*};input(*)[*]{*};ins(*)[*]{*};kbd(*)[*]{*};label(*)[*]{*};legend(*)[*]{*};li(*)[*]{*};link(*)[*]{*};main(*)[*]{*};map(*)[*]{*};mark(*)[*]{*};meta(*)[*]{*};meter(*)[*]{*};nav(*)[*]{*};noscript(*)[*]{*};object(*)[*]{*};ol(*)[*]{*};optgroup(*)[*]{*};option(*)[*]{*};output(*)[*]{*};p(*)[*]{*};param(*)[*]{*};picture(*)[*]{*};pre(*)[*]{*};progress(*)[*]{*};q(*)[*]{*};rp(*)[*]{*};rt(*)[*]{*};ruby(*)[*]{*};s(*)[*]{*};samp(*)[*]{*};section(*)[*]{*};select(*)[*]{*};small(*)[*]{*};source(*)[*]{*};span(*)[*]{*};strong(*)[*]{*};style(*)[*]{*};sub(*)[*]{*};summary(*)[*]{*};sup(*)[*]{*};svg(*)[*]{*};table(*)[*]{*};tbody(*)[*]{*};td(*)[*]{*};template(*)[*]{*};textarea(*)[*]{*};tfoot(*)[*]{*};th(*)[*]{*};thead(*)[*]{*};time(*)[*]{*};title(*)[*]{*};tr(*)[*]{*};track(*)[*]{*};u(*)[*]{*};ul(*)[*]{*};var(*)[*]{*};video(*)[*]{*};wbr(*)[*]{*};"

 ```


## More sample rich text editor configurations


### Add the full screen expander

Set these ```Individual configuration settings``` properties in your configuration file. Each value should be followed by a ```,``` (```comma```) unless it's the last value:
(More information: [Individual configuration settings](#visualization-of-the-rich-text-editor-configuration-file))
 ```
 
 "showAsTabControl": true
 
 "showFullScreenExpander": true
 
 ```

:::image type="content" source="media/cke-screen-expander.png" alt-text="Screen expander control.":::

### Add the HTML source view tab

Set these ```Individual configuration settings``` properties in your configuration file. Each value should be followed by a ```,``` (```comma```) unless it's the last value:
(More information: [Individual configuration settings](#visualization-of-the-rich-text-editor-configuration-file))
 ```

 "showAsTabControl": true
 
 "showHtml": true

 ```

:::image type="content" source="media/cke-html-source.png" alt-text="HTML tab control.":::

### Add a simple toolbar with font size, bold, italic, underline, and highlight

Set this ```defaultSupportedProps``` property in your configuration file. Each value should be followed by a ```,``` (```comma```) unless it's the last value:
(More information: [defaultSupportedProps](#visualization-of-the-rich-text-editor-configuration-file))
 ```

  "toolbar": [ { "items": [ "FontSize", "Bold", "Italic", "Underline", "BGColor" ] } ]

 ```

:::image type="content" source="media/cke-simple-editor.png" alt-text="Controls for a simple editor.":::

### Remove the toolbar to make a rich text rendering surface

Set this ```defaultSupportedProps``` property in your configuration file. Each value should be followed by a ```,``` (```comma```) unless it's the last value:
(More information: [defaultSupportedProps](#visualization-of-the-rich-text-editor-configuration-file))
 ```

  "toolbar": []

 ```

:::image type="content" source="media/cke-no-toolbar.png" alt-text="No toolbar.":::

### Add a new font list and set Brush Script MT as the default font with a default size of 20 px

Set these ```defaultSupportedProps``` properties in your configuration file. Each value should be followed by a ```,``` (```comma```) unless it's the last value:
(More information: [defaultSupportedProps](#visualization-of-the-rich-text-editor-configuration-file))
 ```

  "font_names": "Brush Script MT/'Brush Script MT', cursive;Calibri/Calibri, Helvetica, sans-serif;Calibri Light/'Calibri Light', 'Helvetica Light', sans-serif;"
  
  "font_defaultLabel": "Brush Script MT"
  
  "fontSize_sizes": "8/8px;12/12px;20/20px;32/32px"
  
  "fontSize_defaultLabel": "20"
  
  "stickyStyle": {
   "font-size": "20px",
   "font-family": "'Brush Script MT', cursive"
  }

 ```

:::image type="content" source="media/cke-default-font.png" alt-text="Set a new default font.":::

### Position the toolbar at the top of the rich text editor

Set this ```defaultSupportedProps``` property in your configuration file. Each value should be followed by a ```,``` (```comma```) unless it's the last value:
(More information: [defaultSupportedProps](#visualization-of-the-rich-text-editor-configuration-file))
 ```

  "toolbarLocation": "top"

 ```

:::image type="content" source="media/cke-toolbar-top.png" alt-text="Toolbar positioned at the top of the rich text editor.":::

### Start the editor at 30-px height and then autogrow to fit content

Set these ```defaultSupportedProps``` properties in your configuration file. Each value should be followed by a ```,``` (```comma```) unless it's the last value:
(More information: [defaultSupportedProps](#visualization-of-the-rich-text-editor-configuration-file))
 ```

  "autoGrow_onStartup": false
  
  "autoGrow_maxHeight": 0
  
  "autoGrow_minHeight": 30
  
  "height": 30

 ```

:::image type="content" source="media/cke-autogrow.png" alt-text="Typing into the rich text area will increase it to fit the content.":::

### Fix the height of the editor at 500 px

Set these ```defaultSupportedProps``` properties in your configuration file. Each value should be followed by a ```,``` (```comma```) unless it's the last value:
(More information: [defaultSupportedProps](#visualization-of-the-rich-text-editor-configuration-file))
 ```

  "removePlugins": [ "autogrow" ]
  
  "height": 500

 ```

:::image type="content" source="media/cke-fixed-height.png" alt-text="With a fixed height, the editor remains at the same height. When enough content is added, a scroll bar appears.":::


### Create a plain text surface that removes all html tags except for the "br" tag

Set these ```defaultSupportedProps``` properties in your configuration file. Each value should be followed by a ```,``` (```comma```) unless it's the last value:
(More information: [defaultSupportedProps](#visualization-of-the-rich-text-editor-configuration-file))
 ```

  "enterMode": 2
  
  "shiftEnterMode": 2
  
  "allowedContent": "*"
  
  "disallowedContent": "*"
  
  "forcePasteAsPlainText": true
  
  "toolbar": []
  
  "removePlugins": "contextmenu,liststyle,openlink,tableresize,tableselection,tabletools"

 ```


Set this ```Individual configuration settings``` property in your configuration file. Each value should be followed by a ```,``` (```comma```) unless it's the last value:
(More information: [Individual configuration settings](#visualization-of-the-rich-text-editor-configuration-file))
 ```

 "disableImages": true

 ```

:::image type="content" source="media/rte-plain-text-surface.png" alt-text="Creating a plain text surface makes the strips html.":::

### Remove the context menu so right-clicking works with the default browser's spell check

Enabling this functionality removes the contextual right-click editing capability.

Set this ```defaultSupportedProps``` property in your configuration file. Each value should be followed by a ```,``` (```comma```) unless it's the last value:
(More information: [defaultSupportedProps](#visualization-of-the-rich-text-editor-configuration-file))
 ```

  "removePlugins": "contextmenu,liststyle,openlink,tableresize,tableselection,tabletools"

 ```

:::image type="content" source="media/rte-right-click-config.png" alt-text="Remove the context menu so right-clicking works with the default browser spell check.":::

## Use the default web resource for organization-wide changes

The default RTE web resource is available with the display name RTEGlobalConfiguration.json. This configuration is used for all instances of the RTE control and can be used to make organization-wide changes. This includes RTE used in timeline rich-text notes, knowledge management, and single and multi-line fields that are configured to use the RTE control.
By default, RTEGlobalConfiguration.json is empty. Based on your business requirements, you can specify the values you want to customize in this file. Use the non-editable RTEGlobalConfiguration.json as a sample to add the parameters in the required structure format.

An example of the custom values you can add to the RTEGlobalConfiguration.json is:

 ```
 {
   "defaultSupportedProps": {
       "height": 300,
    "toolbarLocation" : "top"
   }
  }  
 ```


## Find the current setting for a rich text editor configuration

1. In a Microsoft Edge or Google Chrome web browser, run your model-driven app and open a form that has the rich text editor control, such as an account row.
2. Press **Ctrl** while clicking the rich text editor control area, and then select **Inspect**.
3. In the inspection pane, select the **Console** tab, and then select the parent **Main.aspx** page in the drop-down list box on the command bar.

  :::image type="content" source="media/cke-select-parent-main.png" alt-text="Select the Console tab and then select the parent main.aspx page from the drop-down list box.":::

4. Select **Clear console** on the inspection pane command bar.

  :::image type="content" source="media/cke-clear-console.png" alt-text="Clear console command.":::

5. In the inspection pane console, enter **CKEDITOR.config.** to display the different configurations.

  :::image type="content" source="media/cke-configs.png" alt-text="List of CK Editor configurations.":::

6. Select a configuration, such as **autoGrow_minHeight**, to display the current setting.

## Use the rich text editor toolbar

The rich text editor toolbar provides features and functionality that allows you to work with rich text format in notes and email.

### Formatting options

The following table describes the different formatting features and functionality options that are available in the rich text editor that you can use.

|Icon | Name | Shortcut key | Description |
|----------------------|-------------------------|-----------------------------|-----------------------------|
|![Format Painter.](media/format-painter.png "Format Painter")| Format Painter | Ctrl+Shift+C, Ctrl+Shift+V | Apply the look of a particular section to another section. |
|![Font.](media/format-font.png "Font") | Font | Ctrl+Shift+F | Select a font. The application considers the font that you select as the default font. Segoe UI is the default font if you don't select any.<br /><br /> **Note**: When you select any formatted content, the font name for that content displays. If your selection contains multiple fonts, the topmost font name of your selection is displayed.<br> |
|![Font Size.](media/font-size.png "Font Size") | Font size | Ctrl+Shift+P | Change the size of your text. The application considers the font size that you select as the default font size. 12 is the default font if you don't select any.<br /><br /> **Note**: When you select any formatted content, the font size for that content displays. If your selection contains multiple font sizes, the topmost font name of your selection is displayed.|
|![Bold.](media/format-bold.png "Bold")| Bold | Ctrl+B | Make your text bold. |
|![Italic.](media/format-italic.png "Italic")| Italic | Ctrl+I | Italicize your text. |
|![Underline.](media/format-underline.png "Underline")| Underline | Ctrl+U | Underline your text. |
|![Text Highlight Color.](media/text-highlight-color.png "Text Highlight Color")| Text Highlight Color | | Make your text stand out by highlighting it in a bright color. |
|![Font Color.](media/font-color.png "Font Color")| Font Color | | Change the color of your text. |
|![Bullets.](media/format-bullets.png "Bullets")| Bullets | | Create a bulleted list. |
|![Numbering.](media/format-numbering.png "Numbering")| Numbering | | Create a numbered list. |
|![Decrease Indent.](media/decrease-indent.png "Decrease Indent")| Decrease Indent | | Move your paragraph closer to the margin. |
|![Increase Indent.](media/increase-indent.png "Increase Indent")| Increase Indent | | Move your paragraph farther away from the margin. |
|![Block Quote.](media/block-quote.png "Block Quote")| Block Quote | | Apply a block-level quotation format in your content. |
|![Align Left.](media/align-left.png "Align Left")| Align Left | Ctrl+L | Align your content with the left margin. (Commonly used for body text to make it easier to read.) |
|![Align Center.](media/align-center.png "Align Center")| Align Center | Ctrl+E | Center your content on the page. (Commonly used for a formal appearance.) |
|![Align Right.](media/align-right.png "Align Right")| Align Right | Ctrl+R | Align your content with the right margin. (Commonly used for a formal appearance.) |
|![Link.](media/format-link.png "Link")| Link | | Create a link in your document for quick access to web pages and files.<br /><br />Pasted or typed URL text is converted into a link. For example, "http://myexample.com" becomes "<a href="http://myexample.com">http://myexample.com</a>".<br /><br /> In the **Link** dialog box, choose the type of link you'd like to insert.<br /><br />The **Link Info** tab allows you to choose the link type as well as set the link protocol and URL.<br /><br />The **Target** tab is only available for the URL link type. It specifies the location where the link opens after you select it.<br /> |
|![Remove Link.](media/remove-link.png "Unlink")| Unlink | | Delete a link in your email or document.<br /><br />When you place the cursor on a link, the **Unlink** button on the toolbar becomes active. Select the button to remove the link and make it plain text. |
|![Superscript.](media/format-superscript.png "Superscript")| Superscript | | Type small letters just above the line of text. |
|![Subscript.](media/format-subscript.png "Subscript")| Subscript | | Type small letters just below the line of text. |
|![Strikethrough.](media/format-strikethrough.png "Strikethrough")| Strikethrough | | Cross out text by drawing a line through it. |
|![Insert Image.](media/insert-picture.png "Insert Image")| Insert Image| |You can insert an image by directly copying and pasting it inline in the editor, dragging and dropping it from your desktop or local folder directly into the editor, or by typing a URL. The following formats are supported: .PNG, .JPG., or .GIF.<br /><br />To insert an image inline in your article: <br />1. Drag and drop the image or copy and paste it directly into the article. <br />2. Drag any corner of the image to resize it.<br /><br />To insert an image using a URL or navigating to the local image:<br />1. Choose Insert Image.<br />2. In the **Image** property dialog, choose from the following options:<br /><ul><li>Select **Browse** to navigate to the image on your computer.</li><li>Or specify the web address of the image, and properties to define how the image will appear in the email or article.</li><br />**Note:**<ul><li>If the image is located on the external server, use the full absolute path. </li><li>If the image is located on a local server, you can use a relative path. </li><li>If you want the image to be linked to a target, add a URL for the image.</li><li>You can also specify if you want the targeted page to open in a new window, topmost window, same window, or parent window.</li></ul>
|![Left to Right.](media/left-to-right.png "Left to Right")| Left to Right | | Change the text to left-to-right for content such as a paragraph, header, table, or list. Commonly used for bi-directional language content. This is the default setting.|
|![Right to Left.](media/right-to-left.png "Right to Left")| Right to Left | | Change the text to right-to-left for content such as a paragraph, header, table, or list. Commonly used for bi-directional language content. The default setting is left-to-right. |
|![Undo Typing.](media/undo-typing.png "Undo Typing")| Undo Typing | | Undo changes you made to the content. |
|![Redo Typing.](media/redo-typing.png "Redo Typing")| Redo Typing | | Redo changes you made to the content. |
|![Clear All Formatting.](media/clear-formatting.png "Clear All Formatting")| Clear All Formatting | | Remove all formatting from a selection of text, leaving only the normal, unformatted text. |
|![Add a Table.](media/add-table.png "Add a Table")| Add a Table | | Add a table to your content. <br /><br />After adding a table, you can do any of the following:<br /><br /><ul><li>Resize table columns by clicking and dragging your mouse to resize to the columns to the desired width.</li><li>Select one or several cells within a table and apply specific formatting, add links to the selection, or cut, copy, or paste entire rows or columns.</li><li>Right-click to access the properties. This supports features such as cell type, width and height, word wrapping, alignment, merging, and splitting cells horizontally and vertically, inserting or deleting rows and columns, row and column span, and cell and border color.</li></ul>|
|| Accessibility help | Alt+0 | Display list of accessibility shortcuts available when using the rich text editor control. |
|![Expand Toolbar.](media/show-more.png "Expand Toolbar")| Expand Toolbar | | Displays when the toolbar is collapsed and not all options appear. Select to expand the toolbar and make all options visible. |
| | | | |

> [!Tip]
> You can access your browser's context menu by selecting **Ctrl** + right-click. This is useful if you need to use your browser's built-in spellchecker. Otherwise, you can right-click to provide contextual formatting for any element you are using.<br><br>
> Also, an alternative to your browser's built-in spellchecker is the [Microsoft Editor browser extension](https://www.microsoft.com/microsoft-365/microsoft-editor). Microsoft Editor works seamlessly with the rich text editor control, and when enabled, provides fast and easy inline grammar and spellcheck capabilities.

## Use Copilot to refine text (Preview)

[!INCLUDE [cc-beta-prerelease-disclaimer](../../includes/cc-beta-prerelease-disclaimer.md)]

Copilot uses natural language processing (NLP) algorithms to help refine and improve written text. You can provide an initial draft or a partial piece of writing, and Copilot generates suggestions to enhance the content, grammar, clarity, or overall quality of the text. More information: [Use Copilot in rich text editor for email](../model-driven-apps/use-copilot-email-assist.md)

To add the Copilot button to a rich text editor toolbar, see [Add the Copilot option to a rich text editor](../model-driven-apps/copilot-control.md)

## Accessibility shortcuts

The following table outlines a list of accessibility shortcuts available when using the rich text editor control. You can access this list while composing content by pressing **Alt+0**.

|Type | Shortcut key | Description |
|----------------------|-------------------------|-----------------------------|
| General | Alt+F11 | Toggle full-screen view. |
| Tab navigation | Alt+Ctrl+0 | Go to editor toolbar. |
| Tab navigation | Alt+1 | Go to the rich-text editor. |
| Tab navigation | Alt+2 | Go to the HTML editor. |
| Tab navigation | Alt+3 | Go to the preview view. |
| General editor commands | Alt+F10 | Navigate to the editor toolbar. Move to the next and previous toolbar group with Tab and Shift+Tab. Move to the next and previous toolbar button with Right Arrow or Left Arrow. Press Space or Enter to activate the toolbar button. |
| General editor commands | Alt+- | Expand/Collapse the editor toolbar. |
| General editor commands | See description. | Editor dialog: Inside a dialog, press Tab to navigate to the next dialog element, press Shift+Tab to move to the previous dialog element, press Enter to submit the dialog, press ESC to cancel the dialog. When a dialog has multiple tabs, the tab list can be reached either with Alt+F10 or with Tab, following the dialog tabbing order. With a tab list focused, move to the next and previous tab with Right and Left Arrow, respectively. |
| General editor commands | See description. | Editor list box: Inside a list box, move to next list item with Tab or Down Arrow. Move to previous list item with Shift+Tab or Up Arrow. Press Space or Enter to select the list option. Press ESC to close the list box. |
| Base commands | Ctrl+Z | Undo command. |
| Base commands | Shift+Ctrl+Z | Redo command. |
| Base commands | Ctrl+B | Bold command. |
| Base commands | Ctrl+I | Italic command. |
| Base commands | Ctrl+U | Underline command. |
| Base commands | Alt+0 | Accessibility help. |
| Base commands | Esc | Cancel operation. |
| | | |



## Offline experience

The rich text editor control is available when working offline with a basic configuration. The following is a list of supported plug-ins and formatting options when working offline. All configuration added through web resource files aren't available while offline.

Images uploaded using the default configuration won't be available offline.

### Plugins available for offline

The following plug-ins are available to the rich text editor while offline.
```
ajax,autogrow,basicstyles,bidi,blockquote,button,confighelper,contextmenu,dialog,dialogui,editorplaceholder,enterkey,entities,fakeobjects,floatingspace,floatpanel,format,horizontalrule,htmlwriter,indent,indentblock,indentlist,justify,lineutils,list,listblock,maximize,menu,menubutton,notification,notificationaggregator,panel,panelbutton,popup,preview,removeformat,resize,richcombo,selectall,showborders,sourcearea,specialchar,stylescombo,tab,textmatch,textwatcher,toolbar,undo,widgetselection,wysiwygarea,xml
```

### Formatting options for offline

The following table describes the different formatting features and functionality options that are available in the rich text editor while offline.

|Icon | Name | Shortcut key | Description |
|----------------------|-------------------------|-----------------------------|-----------------------------|
|![Bold.](media/format-bold.png "Bold")| Bold | Ctrl+B | Make your text bold. |
|![Italic.](media/format-italic.png "Italic")| Italic | Ctrl+I | Italicize your text. |
|![Underline.](media/format-underline.png "Underline")| Underline | Ctrl+U | Underline your text. |
|![Bullets.](media/format-bullets.png "Bullets")| Bullets | | Create a bulleted list. |
|![Numbering.](media/format-numbering.png "Numbering")| Numbering | | Create a numbered list. |
|![Decrease Indent.](media/decrease-indent.png "Decrease Indent")| Decrease Indent | | Move your paragraph closer to the margin. |
|![Increase Indent.](media/increase-indent.png "Increase Indent")| Increase Indent | | Move your paragraph farther away from the margin. |
|![Block Quote.](media/block-quote.png "Block Quote")| Block Quote | | Apply a block-level quotation format in your content. |
|![Align Left.](media/align-left.png "Align Left")| Align Left | Ctrl+L | Align your content with the left margin. (Commonly used for body text to make it easier to read.) |
|![Align Center.](media/align-center.png "Align Center")| Align Center | Ctrl+E | Center your content on the page. (Commonly used for a formal appearance.) |
|![Align Right.](media/align-right.png "Align Right")| Align Right | Ctrl+R | Align your content with the right margin. (Commonly used for a formal appearance.) |
|![Strikethrough.](media/format-strikethrough.png "Strikethrough")| Strikethrough | | Cross out text by drawing a line through it. |
|![Left to Right.](media/left-to-right.png "Left to Right")| Left to Right | | Change the text to left-to-right for content such as a paragraph, header, table, or list. Commonly used for bi-directional language content. This is the default setting.|
|![Right to Left.](media/right-to-left.png "Right to Left")| Right to Left | | Change the text to right-to-left for content such as a paragraph, header, table, or list. Commonly used for bi-directional language content. The default setting is left-to-right. |
|![Undo Typing.](media/undo-typing.png "Undo Typing")| Undo Typing | | Undo changes you made to the content. |
|![Redo Typing.](media/redo-typing.png "Redo Typing")| Redo Typing | | Redo changes you made to the content. |
|![Clear All Formatting.](media/clear-formatting.png "Clear All Formatting")| Clear All Formatting | | Remove all formatting from a selection of text, leaving only the normal, unformatted text. |
| | | | |


## Best practices for using the rich text editor

Consider the following when using the rich text editor:

- The best performance is achieved when the HTML content size is 1 MB or less. When your HTML content size exceeds 1 MB, you may notice slower response times for loading and editing content. By default, image content is referenced from the content HTML but isn't stored as part of the HTML content, so in the default configuration, images don't negatively impact performance.

- Rich text fields store HTML tags, which are required for formatting along with user entered data. When setting the maximum size for your field, make sure to assign a large enough size for both the HTML tags and user-entered data.

- By default, the rich text editor uploads images to the Azure Blob storage store and isn't stored as part of the field. Images are stored in the same field as base64 when the submitter doesn't have permissions to the `msdyn_richtextfiles` entity. Base64 content is large, so you generally don't want to store images as base64.

- If you have a system administrator or basic user security role, the user personalization feature works by default. If you don't have these roles, you must have create, read, and write privileges added to the msdyn_customcontrolextendedsettings table for the plug-in to work.



## Frequently asked questions

Q: Why are typed characters slow to display?

A. Large content size can cause latency. More information: [Best practices for using the rich text editor](#best-practices-for-using-the-rich-text-editor). Spelling or grammar checks can also slow the typing performance.

Q: Why can't I upload an image, and why does the image preview fail to load?

A. If the image file name is long or contains many full-width characters, it may fail to upload or the preview might not be displayed. Try shortening the file name and then upload it again.

  :::image type="content" source="media/rte-image-preview.png" alt-text="Image preview failure.":::

## Known issues

- HTML markup is displayed for columns configured to use the rich text editor control that are displayed in components other than a column on a form, which don't have the format set to RichText. For example, this occurs in views, subgrids, paginated reports, and Power Pages.
> [!div class="mx-imgBorder"]
> ![HTML markup displayed in a column on a subgrid.](media/html-markup-issue.png)
To resolve this issue, see [Simple configuration](#simple-configuration) for the steps necessary to set the **Format** option to **Rich text**.


### See also

[Create and edit columns for Microsoft Dataverse using Power Apps portal](../data-platform/create-edit-field-portal.md)
[Use Copilot in rich text editor for email](../model-driven-apps/use-copilot-email-assist.md)


[!INCLUDE[footer-include](../../includes/footer-banner.md)]
