---
title: "Use template tags for a portal | MicrosoftDocs"
description: "Learn about template tags available in portal"
author: tapanm-msft
manager: kumarvivek
ms.service: powerapps
ms.topic: conceptual
ms.custom: 
ms.date: 10/07/2019
ms.author: tapanm
ms.reviewer:
---

# Template tags

Template tags control the output of a template in various ways, and allow the combination of multiple templates into a single output.

## include

Includes the contents of one template in another, by name. In Power Apps portals, the source of this other template will generally be a [web template](store-content-web-templates.md). This allows for the reuse of common template fragments in multiple places.  

When a template is included in another, the included template will have access to any variables defined in the parent template.

`{% include 'My Template' %}`

It's also possible to pass any number of named parameters to the include tag. These will then be defined as variables in the included template.

`{% include 'My Template' a:x, b:y %}`

## block

Used in conjunction with extends to provide template inheritance. See extends for usage.

## extends

Used in conjunction with the block tag, provides template inheritance. This allows multiple templates to use a shared layout, while overriding specific areas of the parent layout.

In Power Apps portals, the parent template name provided to the tag will generally refer to the name of a [web template](store-content-web-templates.md).  

When extends is used, it must be the first content in the template, and can only be followed by one or more block tags.

If a block defined in the parent template is not overridden, its contents in the parent template (if any) will be rendered.

## comment

Allows you to leave un-rendered code inside a Liquid template. Any content within the block will not be rendered, and any Liquid code within will not be executed.

**Code**

`Hello{% comment %}, {{ user.fullname }}{% endcomment %}. My name is Charles.`

**Output**

`Hello. My name is Charles.`

## raw

Allows output of Liquid code on a page without having it parsed and executed.

**Output**

`Hello, {{ user.fullname }}. My name is Charles.`

## substitution

When user has enabled the header and footer caching, and he wants to avoid caching of certain section output, he can use this tag. This tag provides the content block in header or footer where output of the wrapped content block doesn't get cached. This is helpful in the scenarios where user is using an object which can frequently get updated, such as request, page, language, and date. For example, refer to the header and footer web template source code update scenarios when [header and footer caching is enabled](../configure/enable-header-footer-output-caching.md).

### See also

[Control flow tags](control-flow-tags.md)<br>
[Iteration tags](iteration-tags.md)<br>
[Variable tags](variable-tags.md)<br>
[Power Apps common data service entity tags](portals-entity-tags.md)
