This folder contains media files that are used in include files for use across BAP Skilling product documentation articles and training units.

Images that are used in an include file can't be stored in the shared content repo (GitHub path: `MicrosoftDocs/powerapps-docs-pr/shared`, path for include files: `~/../shared-content/shared/`).

Instead, store the image files in a subfolder of `MicrosoftDocs/powerapps-docs-pr/powerapps-docs/media/shared`.

1. Create a folder for your product in `MicrosoftDocs/powerapps-docs-pr/powerapps-docs/media/shared`.
1. Upload your media file to the new folder.
1. Call the media file in your include file like this:  
    `source="/power-apps/media/shared/{product}/filename.png"`
