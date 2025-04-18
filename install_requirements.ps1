py -m pip install -r requirements.txt

Write-Host "Activating virtual environment..."
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\.venv\Scripts\Activate.ps1

Write-Host "Requirements installed successfully." -ForegroundColor Green