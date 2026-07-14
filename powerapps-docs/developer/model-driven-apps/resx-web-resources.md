---
title: "String (RESX) web resources (model-driven apps)"
description: "Learn about using string web resources to make localized strings available for use"
author: anushikhas96
ms.author: anushisharma
ms.date: 04/01/2022
ms.reviewer: jdaly
ms.topic: how-to
ms.subservice: mda-developer
search.audienceType: 
  - developer
contributors: 
  - JimDaly
  - caburk
---
# RESX web resources

Use these web resources to manage localized strings in any user interface you define or with error messages you display. 

## Using RESX web resources

RESX web resources contain the keys and localized string values for a single language defined using the RESX XML format. RESX is a common format for defining localized resources for windows applications. There's common tooling available to work with this type of file and localization vendors are familiar with working with them. When the file is published as a web resource in Dataverse, it's converted to a JSON format which is downloaded to the application when needed.

[!INCLUDE[cc-terminology](../data-platform/includes/cc-terminology.md)]

When you create RESX web resources, you must explicitly set the language value and include the locale identifier (LCID) for the appropriate language in the name of the web resource. For example, `new_/strings/MyAppResources.1033.resx` would contain resources for English language. See [Microsoft locale ID values](/previous-versions/windows/embedded/ms912047(v=winembedded.10)) for a list of LCID values.

> [!NOTE]
> If you have multiple RESX web resources with the same name for multiple languages, ensure there is a localized string value for each resource key.

The appropriate string value is determined by the individual user's language preference and the languages available in the organization. This determination is done in two steps.

1. Determining the right RESX web resource: If there's a RESX web resource for user's preferred language, that RESX is used. If a RESX web resource for user's preferred language isn't found, then the RESX web resource for base language is chosen.
2. Returning the string value: Within the chosen RESX web resource in Step 1, the string corresponding to the resource key is returned. If the RESX web resource that matches the user's preferred language doesn't have the resource key, a null response is returned.
 
For example, `Xrm.Utility.getResourceString("new_/strings/MyAppResources","hello")` returns the localized string value for the resource key hello within the `new_/strings/MyAppResources.1033.resx` web resource if the user's preferred language is English. If the user's preferred language is Spanish/Spain, then the localized string value for the resource key hello within the `new_/strings/MyAppResources.1034.resx` web resource is returned. If there's no resource key hello in `new_/strings/MyAppResources.1034.resx` web resource, then a null response is returned. You can see that the function doesn't refer to any specific language or full name of any RESX web resource. This functionality depends on the RESX web resource being associated to the calling JavaScript web resource as a dependency. More information: [Web resource dependencies](web-resource-dependencies.md)


### See also

[Web resources](web-resources.md)<br />
[Create accessible web resources](create-accessible-web-resources.md)<br />
[Web resource dependencies](web-resource-dependencies.md)<br />
[Webpage (HTML) web resources](webpage-html-web-resources.md)<br />
[JavaScript web resources](script-jscript-web-resources.md)<br />
[Image (JPG, PNG, GIF, ICO) web resources](image-web-resources.md)<br />
[Stylesheet (XSL) web resources](stylesheet-xsl-web-resources.md)<br />
[Data (XML) Web resources](data-xml-web-resources.md)<br />
[CSS web resources](css-web-resources.md)<br />
[WebResource table messages and methods](../data-platform/reference/entities/webresource.md)<br />
[Sample: Pass multiple values to a  web resource through the data parameter](sample-pass-multiple-values-web-resource-through-data-parameter.md)<br />
[Sample: Import files as web resources](sample-import-files-web-resources.md)


[!INCLUDE[footer-include](../../includes/footer-banner.md)]
