This folder contains include files for use across BAP Skilling product documentation articles and training units.

The include files may be used for the following values of ms.service:

- dynamics-365
- industry-solutions
- power-platform

## How to use the shared content repo

- GitHub path: `MicrosoftDocs/powerapps-docs-pr/shared`
- Path for include files: `~/../shared-content/shared/`

Full instructions for [using include files](https://review.learn.microsoft.com/help/platform/includes-best-practices?branch=main) are in the Learn contributors guide. Here's a quick summary of how to use the shared content repo for BAP Skilling include files.

1. Create a folder in `MicrosoftDocs/powerapps-docs-pr/shared`.

1. Upload your include file to the new folder.

1. Use the following syntax to insert your include file: `[!INCLUDE [File name](~/../shared-content/shared/filename.md)]`

The following example inserts the file gdpr-intro.md, which is stored in the folder **shared/privacy-includes**: `[!INCLUDE [gdpr-intro](~/../shared-content/shared/privacy-includes/gdpr-intro.md)]`

The following example inserts a lightbox accessibility tip, which is stored at the root level of the **shared** folder: `[!INCLUDE [Lightbox tip](~/../shared-content/shared/lightbox-tip.md)]`

## A note about images in include files

Images that are used in an include file can't be stored in the shared content repo. Instead, store the image files in a subfolder of `MicrosoftDocs/powerapps-docs-pr/powerapps-docs/media/shared`.

1. Create a folder for your product in `MicrosoftDocs/powerapps-docs-pr/powerapps-docs/media/shared`.
1. Upload your media file to the new folder.
1. Call the media file in your include file like this:  
    `source="/power-apps/media/shared/{product}/filename.png"`

## Why does the shared content repo live in the powerapps-docs-pr repo?

It's a long story. The TL;DR: is that powerapps-docs-pr is already set up for all the languages we localize our docs in. Lots of extra work would have been required to localize files stored in, say, MicrosoftDocs/reusable-content.

## Where can I get help with the shared content repo?

[Submit a Content Engineering request](content-engineering-requests.md?branch=main) or reach out to [BAP Skilling Content Engineering](mailto:crmce@microsoft.com).
