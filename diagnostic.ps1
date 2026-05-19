Add-Type -AssemblyName System.Drawing
$base = 'c:\Users\mkaur\Downloads\github\powerapps-docs-pr\powerapps-docs\maker\canvas-apps\media\data-platform-create-app-scratch'
$path = Join-Path $base 'close-data.png'

Write-Host "=== Test 1: Read close-data.png ==="
$img = [System.Drawing.Image]::FromFile($path)
Write-Host "Original: $($img.Width)x$($img.Height) | PixelFormat: $($img.PixelFormat)"
$bmp = New-Object System.Drawing.Bitmap $img
$img.Dispose()
Write-Host "Bitmap copy: $($bmp.Width)x$($bmp.Height) | PixelFormat: $($bmp.PixelFormat)"

Write-Host "=== Test 2: Draw a HUGE red rectangle in the middle ==="
$g = [System.Drawing.Graphics]::FromImage($bmp)
$pen = New-Object System.Drawing.Pen ([System.Drawing.Color]::Red), 10
$g.DrawRectangle($pen, 400, 200, 400, 200)
$g.Dispose()
$pen.Dispose()

Write-Host "=== Test 3: Check pixel at (400, 200) - should be red ==="
$px = $bmp.GetPixel(400, 200)
Write-Host "Pixel (400,200) = R$($px.R) G$($px.G) B$($px.B)"
$px = $bmp.GetPixel(410, 200)
Write-Host "Pixel (410,200) = R$($px.R) G$($px.G) B$($px.B)"

Write-Host "=== Test 4: Save and re-read ==="
$testPath = Join-Path $base 'close-data.png'
$bmp.Save($testPath, [System.Drawing.Imaging.ImageFormat]::Png)
$bmp.Dispose()

$bmp2 = New-Object System.Drawing.Bitmap $testPath
$px2 = $bmp2.GetPixel(400, 200)
Write-Host "Re-read pixel (400,200) = R$($px2.R) G$($px2.G) B$($px2.B)"
$px2 = $bmp2.GetPixel(410, 200)
Write-Host "Re-read pixel (410,200) = R$($px2.R) G$($px2.G) B$($px2.B)"
$bmp2.Dispose()
